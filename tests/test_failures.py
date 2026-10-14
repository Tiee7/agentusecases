import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from agentwatch.crawler import main

class FailureTests(unittest.TestCase):
    def test_failed_detail_does_not_commit_partial_success(self):
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
                with self.assertRaisesRegex(RuntimeError,'Fixture network failure'):
                    main()
            self.assertFalse(path.exists(), 'Failed crawl must not create a successful snapshot')
