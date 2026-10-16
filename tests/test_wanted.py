import json
import tempfile
import unittest
from pathlib import Path
from agentwatch.archive import extract, sha
from agentwatch.wanted import parse_button, translation_queue


class WantedTests(unittest.TestCase):
    def test_visible_counts_and_unknown(self):
        for text, expected in [('I want this · 1,234', 1234), ('I want this 0', 0),
                               ('I want this (17)', 17), ('I want this', None),
                               ('I want this · 1,2', None), ('I want this 1k', None),
                               ('Wanted 3', None), ('I want this -1', None)]:
            self.assertEqual(parse_button(text), expected)

    def test_real_separator_and_related_case_exclusion(self):
        html = '<h1>Case</h1><button>I want this · <span>12</span></button>Related use cases<button>I want this 99</button>'
        self.assertEqual(extract(html, 'https://agentusecases.ai/use-case/test', '2026-10-16T12:00:00Z')['fields']['wanted'], 12)

    def test_queue_keeps_unknown_separate_and_checks_translation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for slug, value in [('a', 2), ('b', 9), ('c', 9), ('d', None), ('e', 0), ('f', True), ('g', 3)]:
                item = {'observed_at': '2026-10-16T12:00:00Z', 'body_sha256': 'source',
                        'fields': {'wanted': {'status': 'observed', 'value': value}}}
                if slug == 'g':
                    item['translation'] = {'status': 'available', 'format': 'full_extracted_text_translation',
                                           'language': 'zh-CN', 'based_on_body_sha256': 'source',
                                           'body': '中文', 'body_sha256': sha('中文')}
                (root / (slug + '.json')).write_text(json.dumps(item))
            result = translation_queue(root)
            self.assertEqual([r['id'] for r in result['wanted_ranked']], ['b', 'c', 'a', 'e'])
            self.assertEqual([r['group'] for r in result['wanted_ranked']], ['A', 'B', 'A', 'B'])
            self.assertEqual([r['id'] for r in result['unknown_unranked']], ['d', 'f'])
            self.assertTrue(all(r['wanted'] is None and 'rank' not in r for r in result['unknown_unranked']))
            self.assertEqual(result['translated_count'], 1)
