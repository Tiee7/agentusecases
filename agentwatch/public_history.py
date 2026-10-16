"""Export case-text history without HTML caches or unrelated workspace files."""
import sqlite3
import json
from .source_case import latest
from pathlib import Path

def export(source='data/history.sqlite3',target='data/public-history/history.sqlite3'):
    Path(target).parent.mkdir(parents=True,exist_ok=True)
    original=sqlite3.connect(f'file:{Path(source).resolve()}?mode=ro',uri=True)
    public=sqlite3.connect(target);original.backup(public);original.close()
    public.execute('CREATE TABLE IF NOT EXISTS public_source_cases(url TEXT PRIMARY KEY,payload TEXT)')
    for url,value in latest(public).items():
        public.execute('INSERT OR REPLACE INTO public_source_cases VALUES(?,?)',(url,json.dumps(value)))
    public.commit();public.execute('VACUUM');public.close()

if __name__=='__main__':export()
