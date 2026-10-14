"""Prepare the next research batch without claiming an unverified popularity rank."""
import argparse
import json
import sqlite3
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--db', default='data/history.sqlite3')
    parser.add_argument('--batch-size', type=int, default=5)
    parser.add_argument('--output', default='data/research-queue.json')
    args = parser.parse_args()
    if args.batch_size < 1:
        parser.error('batch-size must be positive')
    db = sqlite3.connect(f'file:{Path(args.db).resolve()}?mode=ro', uri=True)
    run = db.execute('SELECT id,ordering,fetched_at FROM runs ORDER BY id DESC LIMIT 1').fetchone()
    if not run:
        raise RuntimeError('No successful crawl; research queue cannot be generated')
    rows = db.execute('SELECT o.url,o.title,p.position,p.category FROM observations o LEFT JOIN priorities p ON p.run_id=o.run_id AND p.url=o.url WHERE o.run_id=? ORDER BY p.position IS NULL,p.position,o.url', (run[0],)).fetchall()
    completed = set()
    for path in Path('research').glob('*.json'):
        record = json.loads(path.read_text())
        if record.get('status') == 'reviewed':
            completed.add(record['url'])
    pending = [{'url': url, 'title': title, 'listing_position': position, 'category': category, 'priority_kind': 'site_category_top' if position is not None else 'sitemap_order'} for url,title,position,category in rows if url not in completed]
    batch = pending[:args.batch_size]
    result = {'run_id': run[0], 'fetched_at': run[2], 'ordering': run[1], 'hot_order_verified': bool(batch) and run[1] == 'site_category_top' and all(r['listing_position'] is not None for r in batch), 'ranking_scope': 'Public SSR first-page category top, not global popularity or live vote rank', 'batch': batch, 'remaining_observed': len(pending)}
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
