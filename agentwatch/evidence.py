"""Read public research sources and retain verifiable receipts, never credentials."""
import argparse
import hashlib
import ipaddress
import json
import time
import urllib.robotparser
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import Request
from .crawler import OPENER, Page

UA = 'AgentUseCaseResearch/1.0'
KINDS = ('primary', 'independent', 'feedback', 'competitor', 'aggregator', 'market')

def public_url(url):
    parts=urlsplit(url)
    if parts.scheme!='https' or not parts.hostname or parts.username or parts.password:
        raise ValueError('Only public HTTPS sources without credentials are supported')
    if parts.hostname in ('localhost','metadata.google.internal') or parts.hostname.endswith(('.local','.internal')):
        raise ValueError('Private network sources are outside this research scope')
    try:
        address=ipaddress.ip_address(parts.hostname)
    except ValueError:
        address=None
    if address is not None and not address.is_global:
        raise ValueError('Private IP sources are outside this research scope')
    return parts

def request(url):
    with OPENER.open(Request(url,headers={'User-Agent':UA}),timeout=30) as response:
        raw=response.read(3_000_001)
        if len(raw)>3_000_000:
            raise ValueError('Source exceeds 3 MB limit')
        return raw.decode(response.headers.get_content_charset() or 'utf-8',errors='replace'),response.headers.get_content_type()

def capture(case_id,url,kind,root=Path('data')):
    from .business import safe_id
    safe_id(case_id)
    parts=public_url(url)
    if kind not in KINDS:
        raise ValueError('Unknown source kind')
    source_id='S'+hashlib.sha256(url.encode()).hexdigest()[:12]
    receipt={'id':source_id,'url':url,'kind':kind,'fetched_at':datetime.now(timezone.utc).isoformat()}
    try:
        robot=urllib.robotparser.RobotFileParser()
        try:
            robots,_=request(f'https://{parts.netloc}/robots.txt')
        except HTTPError as error:
            if error.code!=404:
                raise
            robots='User-agent: *\nAllow: /'
        robot.parse(robots.splitlines())
        if not robot.can_fetch(UA,url):
            raise ValueError('robots.txt disallows this source')
        time.sleep(max(2,robot.crawl_delay(UA) or 0))
        raw,content_type=request(url)
        if content_type in ('text/html','application/xhtml+xml'):
            page=Page();page.feed(raw)
            text='\n'.join(page.text)
            title=page.text[0] if page.text else ''
            links=page.links
        else:
            text=raw;title=parts.path;links=[]
        structured_empty = content_type=='application/json' and json.loads(raw) in ([], {})
        if len(text)<100 and not structured_empty:
            raise ValueError('Source has insufficient readable content')
        cache=root/'source-cache'/case_id
        cache.mkdir(parents=True,exist_ok=True)
        path=cache/(source_id+'.txt')
        path.write_text(text)
        receipt.update(status='fetched',title=title,characters=len(text),sha256=hashlib.sha256(text.encode()).hexdigest(),text_path=str(path),links=links)
    except Exception as error:
        receipt.update(status='blocked',error=f'{type(error).__name__}: {error}')
    directory=root/'evidence'
    directory.mkdir(parents=True,exist_ok=True)
    output=directory/(case_id+'.json')
    records=json.loads(output.read_text()) if output.exists() else []
    records=[r for r in records if r['id']!=source_id]+[receipt]
    output.write_text(json.dumps(records,ensure_ascii=False,indent=2))
    return receipt

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('case_id')
    parser.add_argument('url')
    parser.add_argument('--kind',choices=KINDS,required=True)
    args=parser.parse_args()
    from .business import safe_id
    safe_id(args.case_id)
    receipt=capture(args.case_id,args.url,args.kind)
    print(json.dumps(receipt,ensure_ascii=False,indent=2))
    if receipt['status']!='fetched':
        raise SystemExit(1)

if __name__=='__main__':
    main()
