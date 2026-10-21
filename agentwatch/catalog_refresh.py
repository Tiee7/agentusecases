"""Publish crawler observations without modifying any research-owned files."""
import argparse
import hashlib
import json
import sqlite3
from pathlib import Path
from .business import bootstrap, indexes

def research_fingerprints():
    return {str(p): hashlib.sha256(p.read_bytes()).hexdigest()
            for root in ('research', 'reports') for p in Path(root).rglob('*') if p.is_file()}

def refresh(db_path):
    before = research_fingerprints()
    db = sqlite3.connect(f'file:{Path(db_path).resolve()}?mode=ro', uri=True)
    row = db.execute('SELECT id,fetched_at,listing_url FROM runs ORDER BY id DESC LIMIT 1').fetchone()
    if not row: raise ValueError('No successful crawl available')
    run, fetched_at, listing = row
    observed = db.execute('SELECT count(*) FROM catalogs WHERE run_id=?', (run,)).fetchone()[0]
    if not observed: raise ValueError('Independent publication requires a complete catalog snapshot')
    sampled = db.execute('SELECT count(*) FROM observations WHERE run_id=?', (run,)).fetchone()[0]
    count = bootstrap(db_path, sync_research=False)
    from .archive import apply
    apply(db,preserve_reviewed=True)
    from .archive_coverage import update
    update()
    indexes()
    if research_fingerprints() != before:
        raise RuntimeError('Catalog refresh modified research-owned files; refuse publication')
    metadata = {'schema_version':1, 'fetched_at':fetched_at, 'listing_url':listing,
                'run_id':run, 'catalog_observed':observed, 'registered_cases':count,
                'detail_pages_read':sampled, 'details_complete':sampled == observed,
                'reviewed_archives_preserved':sum(1 for p in Path('registry/archive-observations').glob('*.json')),
                'reviewed_source_changes_pending':sum(bool(json.loads(p.read_text()).get('published_edition',{}).get('review_required')) for p in Path('registry/archive-observations').glob('*.json'))}
    Path('registry/refresh.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2)+'\n')
    db.close()
    return metadata

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--db',default='data/history.sqlite3')
    print(json.dumps(refresh(parser.parse_args().db),ensure_ascii=False,indent=2))

if __name__ == '__main__': main()
