import json
import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from agentwatch.crawler import main

class FailureTests(unittest.TestCase):
    def test_failed_detail_records_failure_without_successful_observation(self):
        seed={'total':1,'firstPage':[{'id':'money','items':[{'id':'a','title':'A'}]}]}
        payload='10:'+json.dumps(['$', 'node', None, {'seed':seed}])+'\n'
        html='<script>self.__next_f.push([1,'+json.dumps(payload)+'])</script>'
        def fake_fetch(url):
            if url.endswith('/robots.txt'):
                return 'User-agent: *\nAllow: /'
            if url.endswith('/sitemap.xml'):
                return '<urlset><url><loc>https://agentusecases.ai/use-case/a</loc></url></urlset>'
            if '/use-case/' in url:
                raise RuntimeError('Fixture network failure')
            return html
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'db.sqlite3'
            with patch('sys.argv',['crawler','--limit','1','--workers','1','--db',str(path)]),patch('agentwatch.crawler.fetch',fake_fetch):
                main()
            db=sqlite3.connect(path)
            self.assertEqual(db.execute('SELECT count(*) FROM observations').fetchone()[0],0)
            status,error=db.execute('SELECT status,error FROM fetch_attempts').fetchone()
            self.assertEqual(status,'failed');self.assertIn('Fixture network failure',error)
            self.assertEqual(db.execute('SELECT count(*) FROM catalogs').fetchone()[0],1)
            db.close()
