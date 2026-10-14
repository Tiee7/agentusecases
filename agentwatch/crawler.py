"""Conservative public-page collector; never infer completeness or popularity."""
import argparse
import hashlib
import json
import re
import sqlite3
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from urllib.error import HTTPError, URLError
import time
import urllib.robotparser
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urldefrag
from urllib.request import Request, urlopen

UA = 'AgentUseCaseWatch/0.1'
ADAPTER_VERSION = 'public-ssr-v1'
RATE_LOCK = threading.Lock()
NEXT_REQUEST = 0.0
REQUEST_DELAY = 0.0

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.text = []
        self.hidden = 0
        self.anchor = None
        self.h1 = []
        self.in_h1 = False
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'h1':
            self.in_h1 = True
        if tag in ('script', 'style'):
            self.hidden += 1
        if tag == 'a' and attrs.get('href'):
            self.anchor = [attrs['href'], []]
    def handle_endtag(self, tag):
        if tag == 'h1':
            self.in_h1 = False
        if tag in ('script', 'style'):
            self.hidden = max(0, self.hidden - 1)
        if tag == 'a' and self.anchor:
            self.links.append((self.anchor[0], ' '.join(self.anchor[1]).strip()))
            self.anchor = None
    def handle_data(self, data):
        if not self.hidden and data.strip():
            self.text.append(data.strip())
            if self.in_h1:
                self.h1.append(data.strip())
            if self.anchor:
                self.anchor[1].append(data.strip())

def candidates(html, base, pattern):
    page = Page()
    page.feed(html)
    found = {}
    for href, title in page.links:
        url = urldefrag(urljoin(base, href))[0]
        parts = urlsplit(url)
        if parts.scheme == 'https' and parts.netloc == urlsplit(base).netloc and re.search(pattern, parts.path):
            found.setdefault(url, title or parts.path)
    return found

def fetch(url):
    global NEXT_REQUEST
    for attempt in range(3):
        with RATE_LOCK:
            wait = max(0, NEXT_REQUEST - time.monotonic())
            if wait:
                time.sleep(wait)
            NEXT_REQUEST = time.monotonic() + REQUEST_DELAY
        try:
            with urlopen(Request(url, headers={'User-Agent': UA}), timeout=30) as response:
                if urlsplit(response.url).netloc != urlsplit(url).netloc:
                    raise RuntimeError('Cross-host redirect requires explicit review')
                raw = response.read(5_000_001)
                if len(raw) > 5_000_000:
                    raise RuntimeError('Page exceeds 5 MB limit')
                return raw.decode('utf-8')
        except HTTPError as error:
            if error.code not in (429, 500, 502, 503, 504) or attempt == 2:
                raise
            retry_after = error.headers.get('Retry-After', '')
            time.sleep(min(30, int(retry_after)) if retry_after.isdigit() else 2 ** (attempt + 1))
        except (URLError, TimeoutError):
            if attempt == 2:
                raise
            time.sleep(2 ** (attempt + 1))

def database(path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(path)
    db.executescript('''
    CREATE TABLE IF NOT EXISTS runs(id INTEGER PRIMARY KEY, fetched_at TEXT, listing_url TEXT, ordering TEXT);
    CREATE TABLE IF NOT EXISTS priorities(run_id INTEGER, url TEXT, position INTEGER, category TEXT, PRIMARY KEY(run_id,url));
    CREATE TABLE IF NOT EXISTS catalogs(run_id INTEGER, url TEXT, lastmod TEXT, PRIMARY KEY(run_id,url));
    CREATE TABLE IF NOT EXISTS observations(run_id INTEGER, url TEXT, title TEXT, position INTEGER, digest TEXT, body TEXT, PRIMARY KEY(run_id,url));
    ''')
    columns = {r[1] for r in db.execute('PRAGMA table_info(runs)')}
    if 'adapter_version' not in columns:
        db.execute("ALTER TABLE runs ADD COLUMN adapter_version TEXT NOT NULL DEFAULT 'legacy'")
        db.commit()
    return db

def save(db, listing, ordering, rows, catalog_rows=None, priorities=None):
    previous = db.execute('SELECT MAX(id) FROM runs WHERE listing_url=? AND adapter_version=?', (listing,ADAPTER_VERSION)).fetchone()[0]
    old = {r[0]: r[1:] for r in db.execute('SELECT url,title,digest,position FROM observations WHERE run_id=?', (previous,))}
    old_catalog = dict(db.execute('SELECT url,lastmod FROM catalogs WHERE run_id=?', (previous,)))
    changes = []
    with db:
        run = db.execute('INSERT INTO runs(fetched_at,listing_url,ordering,adapter_version) VALUES(?,?,?,?)', (datetime.now(timezone.utc).isoformat(), listing, ordering,ADAPTER_VERSION)).lastrowid
        if priorities:
            db.executemany('INSERT INTO priorities VALUES(?,?,?,?)', [(run,url,rank,category) for url,(rank,category) in priorities.items()])
        if catalog_rows is not None:
            db.executemany('INSERT INTO catalogs VALUES(?,?,?)', [(run,url,lastmod) for url,lastmod in catalog_rows.items()])
        for position, row in enumerate(rows, 1):
            digest = hashlib.sha256(row['body'].encode()).hexdigest()
            db.execute('INSERT INTO observations VALUES(?,?,?,?,?,?)', (run, row['url'], row['title'], position, digest, row['body']))
            before = old.get(row['url'])
            kind = 'baseline' if previous is None else 'newly_observed' if before is None else 'content_changed' if before[:2] != (row['title'], digest) else 'position_changed' if before[2] != position else 'unchanged'
            changes.append({'url': row['url'], 'title': row['title'], 'position': position, 'change': kind})
    catalog_delta = None if catalog_rows is None else {'count': len(catalog_rows), 'baseline': not old_catalog, 'newly_listed': sorted(set(catalog_rows)-set(old_catalog)) if old_catalog else [], 'no_longer_listed': sorted(set(old_catalog)-set(catalog_rows)), 'lastmod_changed': sorted(url for url in set(catalog_rows)&set(old_catalog) if catalog_rows[url] != old_catalog[url])}
    return {'adapter_version': ADAPTER_VERSION, 'catalog': catalog_delta, 'details_complete': catalog_rows is not None and len(rows)==len(catalog_rows), 'run_id': run, 'previous_run_id': previous, 'ordering': ordering, 'complete_catalog': catalog_rows is not None, 'not_observed': sorted(set(old) - {r['url'] for r in rows}), 'cases': changes}

def main():
    global REQUEST_DELAY
    parser = argparse.ArgumentParser()
    parser.add_argument('--listing', default='https://agentusecases.ai/')
    parser.add_argument('--ordering', choices=['unknown', 'site_category_top'], default='site_category_top')
    parser.add_argument('--limit', type=int, default=20, help='0 scans every sitemap case; positive values sample first N')
    parser.add_argument('--workers', type=int, default=4)
    parser.add_argument('--db', default='data/history.sqlite3')
    args = parser.parse_args()
    if args.limit < 0:
        parser.error('limit must be nonnegative')
    if not 1 <= args.workers <= 8:
        parser.error('workers must be between 1 and 8')
    base = urlsplit(args.listing)
    if base.scheme != 'https' or base.username or base.password:
        parser.error('listing must be a public HTTPS URL')
    robots_url = f'https://{base.netloc}/robots.txt'
    robots = urllib.robotparser.RobotFileParser()
    robots.parse(fetch(robots_url).splitlines())
    if not robots.can_fetch(UA, args.listing):
        raise RuntimeError('robots.txt disallows listing')
    delay = max(2, robots.crawl_delay(UA) or 0)
    REQUEST_DELAY = delay
    listing_html = fetch(args.listing)
    from .site import extract_seed, catalog, detail
    seed = extract_seed(listing_html)
    sitemap_url = f'https://{base.netloc}/sitemap.xml'
    if not robots.can_fetch(UA, sitemap_url):
        raise RuntimeError('robots.txt disallows sitemap')
    catalog_rows = catalog(fetch(sitemap_url), base.netloc)
    if len(catalog_rows) != seed['total']:
        raise RuntimeError('Sitemap case count differs from public catalog count')
    links = {}
    priorities = {}
    for section in seed['firstPage']:
        for item in section['items']:
            url = urljoin(args.listing, '/use-case/' + item['id'])
            links[url] = item['title']
            priorities[url] = (len(priorities)+1, section['id'])
    for url in catalog_rows:
        links.setdefault(url, urlsplit(url).path.rsplit('/', 1)[-1])
    if not links:
        raise RuntimeError('No cases found: inspect source structure/API; no snapshot saved')
    selected = list(links.items())[:args.limit] if args.limit else list(links.items())
    def collect(entry):
        index, (url,title) = entry
        if not robots.can_fetch(UA, url):
            raise RuntimeError(f'robots.txt disallows case: {url}')
        html = fetch(url)
        page = Page()
        page.feed(html)
        body = detail(html)
        if len(body) < 50:
            raise RuntimeError(f'Empty or client-rendered case: {url}')
        if not page.h1:
            raise RuntimeError(f'Case title missing: {url}')
        title = ' '.join(page.h1)
        print(f'Fetched {index}/{len(selected)}: {title}', file=sys.stderr, flush=True)
        return {'url': url, 'title': title, 'body': body}
    pool = ThreadPoolExecutor(max_workers=args.workers)
    try:
        rows = list(pool.map(collect, enumerate(selected,1)))
    except BaseException:
        pool.shutdown(wait=True, cancel_futures=True)
        raise
    else:
        pool.shutdown(wait=True)
    db = database(args.db)
    result = save(db, args.listing, args.ordering, rows, catalog_rows, priorities)
    Path('data').mkdir(exist_ok=True)
    Path('data/catalog.json').write_text(json.dumps(catalog_rows,ensure_ascii=False,indent=2))
    Path('data/runs').mkdir(parents=True, exist_ok=True)
    Path(f"data/runs/{result['run_id']}.json").write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
