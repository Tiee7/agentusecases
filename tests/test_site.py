import json
import unittest
from agentwatch.site import extract_seed, catalog, detail
from agentwatch.crawler import database, save
import tempfile
from pathlib import Path

class SiteTests(unittest.TestCase):
    def test_ssr_seed_decodes_without_api(self):
        seed = {'total': 1, 'firstPage': [{'items': [{'id': 'a'}]}]}
        payload = '10:' + json.dumps(['$', 'node', None, {'seed': seed}]) + '\n'
        html = '<script>self.__next_f.push([1,' + json.dumps(payload) + '])</script>'
        self.assertEqual(extract_seed(html), seed)
    def test_sitemap_filters_external_hosts(self):
        xml = '<urlset><url><loc>https://agentusecases.ai/use-case/a</loc><lastmod>2026-10-14</lastmod></url><url><loc>https://evil.test/use-case/b</loc></url></urlset>'
        self.assertEqual(catalog(xml, 'agentusecases.ai'), {'https://agentusecases.ai/use-case/a': '2026-10-14'})
    def test_detail_excludes_related_and_preserves_prompt_and_source(self):
        html = '<h1>Case</h1><p>Summary</p><h2>What they did</h2><p>Work</p><h2>Try it yourself</h2><p>Prompt</p><h2>Want help getting this working?</h2><p>Sponsor</p><a href="https://example.test/source">Read the original ↗</a><h2>Related use cases</h2><p>Random</p>'
        body = detail(html)
        self.assertIn('Prompt', body)
        self.assertIn('https://example.test/source', body)
        self.assertNotIn('Sponsor', body)
        self.assertNotIn('Random', body)
    def test_catalog_and_detail_completeness_separate(self):
        with tempfile.TemporaryDirectory() as tmp:
            db=database(str(Path(tmp)/'db'))
            row={'url':'a','title':'A','body':'body'}
            result=save(db,'listing','site_category_top',[row],{'a':'2026-10-14','b':'2026-10-14'},{'a':(1,'money')})
            self.assertTrue(result['complete_catalog'])
            self.assertFalse(result['details_complete'])
            second=save(db,'listing','site_category_top',[row],{'a':'2026-10-15','c':'2026-10-14'})
            self.assertEqual(second['catalog']['newly_listed'],['c'])
            self.assertEqual(second['catalog']['no_longer_listed'],['b'])
            self.assertEqual(second['catalog']['lastmod_changed'],['a'])
