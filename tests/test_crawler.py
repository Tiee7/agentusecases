import tempfile
import unittest
from pathlib import Path
from agentwatch.crawler import candidates, database, save

class CrawlerTests(unittest.TestCase):
    def test_links_are_same_host_unique_and_filtered(self):
        html = '<a href="/cases/a#top">A</a><a href="/cases/a">duplicate</a><a href="https://evil.test/cases/b">B</a><a href="/about">About</a>'
        self.assertEqual(candidates(html, 'https://agentusecases.ai/', r'/cases/[^/]+$'), {'https://agentusecases.ai/cases/a': 'A'})
    def test_baseline_changes_and_missing_are_distinct(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = database(str(Path(tmp) / 'history.sqlite3'))
            a = {'url': 'https://example.test/cases/a', 'title': 'A', 'body': 'first'}
            b = {'url': 'https://example.test/cases/b', 'title': 'B', 'body': 'second'}
            self.assertEqual(save(db, 'listing', 'unknown', [a,b])['cases'][0]['change'], 'baseline')
            updated = dict(a, body='updated')
            result = save(db, 'listing', 'unknown', [updated])
            self.assertEqual(result['cases'][0]['change'], 'content_changed')
            self.assertEqual(result['not_observed'], [b['url']])
            self.assertFalse(result['complete_catalog'])
            self.assertEqual(save(db, 'listing', 'unknown', [updated])['cases'][0]['change'], 'unchanged')
    def test_reordering_is_not_content_change(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = database(str(Path(tmp) / 'history.sqlite3'))
            rows = [{'url': str(n), 'title': str(n), 'body': str(n)} for n in range(2)]
            save(db, 'listing', 'site_hot', rows)
            self.assertTrue(all(r['change'] == 'position_changed' for r in save(db, 'listing', 'site_hot', rows[::-1])['cases']))

if __name__ == '__main__':
    unittest.main()
