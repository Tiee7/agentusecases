"""Public listing model regression: shared items must retain their positions."""
import copy
import io
import json
import sqlite3
import tempfile
import unittest
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path
from unittest.mock import patch

from agentwatch.crawler import main, validate_catalog_seed
from agentwatch.site import extract_seed

FIXTURE = Path(__file__).parent / 'fixtures/catalog-flight-reference.html'
TARGET = 'research-stocks-and-update-a-watchlist-in-the-browser'


def flight(records, split=None):
    stream = ''.join(key + ':' + json.dumps(value) + '\n' for key, value in records)
    chunks = [stream] if split is None else [stream[:split], stream[split:]]
    return ''.join('<script>self.__next_f.push([1,' + json.dumps(chunk) + '])</script>' for chunk in chunks)


def model(item):
    return ['$', '$L19', None, {'seed': {
        'total': 1, 'firstPage': [{'id': 'money', 'items': [item]}]}}]


class FlightCatalogTests(unittest.TestCase):
    def test_observed_element_props_reference_preserves_all_positions_and_fields(self):
        html = FIXTURE.read_text()
        raw = json.loads(json.loads(html.split('push([1,', 1)[1].split('])</script>', 1)[0]).split(':', 1)[1])
        raw_seed = raw[3]['children'][0][0][3]['seed']
        expected = [x['id'] if isinstance(x, dict) else TARGET for x in raw_seed['firstPage'][0]['items']]
        seed = extract_seed(html)
        validate_catalog_seed(seed)
        items = seed['firstPage'][0]['items']
        self.assertEqual(seed['total'], 1427)
        self.assertEqual(len(items), 30)
        self.assertEqual([x['id'] for x in items], expected)
        self.assertEqual(items[13], raw_seed['latestSample'][2])
        self.assertEqual(items[13]['submittedBy'], '$undefined')
        self.assertEqual(items[13]['agents']['labels'], '$10:props:children:0:0:props:seed:latestSample:2:agents:filter')
        self.assertEqual(seed['latestSample'], raw_seed['latestSample'])

    def test_forward_chained_reference_and_chunks_split_inside_record(self):
        item = {'id': 'a', 'title': '$100 of literal text'}
        records = [('10', model('$a:items:0')), ('a', {'items': ['$b']}), ('b', item)]
        for split in (None, 5, 31, 120):
            with self.subTest(split=split):
                self.assertEqual(extract_seed(flight(records, split))['firstPage'][0]['items'], [item])

    def test_seed_section_and_items_can_be_shared_containers(self):
        seed = {'total': 1, 'firstPage': '$b'}
        section = {'id': 'money', 'items': '$d'}
        item = {'id': 'a', 'title': 'A'}
        records = [('10', {'seed': '$a'}), ('a', seed), ('b', ['$c']), ('c', section), ('d', ['$e']), ('e', item)]
        self.assertEqual(extract_seed(flight(records)), {
            'total': 1, 'firstPage': [{'id': 'money', 'items': [item]}]})

    def test_numeric_element_props_index_and_dictionary_props_are_supported(self):
        item = {'id': 'a', 'title': 'A'}
        for reference, target in [('$a:3:item', ['$', 'node', None, {'item': item}]),
                                  ('$a:props:item', {'props': {'item': item}})]:
            with self.subTest(reference=reference):
                result = extract_seed(flight([('10', model(reference)), ('a', target)]))
                self.assertEqual(result['firstPage'][0]['items'], [item])

    def test_missing_records_and_paths_fail_closed(self):
        for reference in ('$f', '$a:absent', '$a:items:2', '$a:items:0:missing'):
            with self.subTest(reference=reference), self.assertRaisesRegex(RuntimeError, 'SSR catalog reference'):
                extract_seed(flight([('10', model(reference)), ('a', {'items': [{'id': 'a'}]})]))

    def test_unsupported_and_malicious_references_fail_closed(self):
        for reference in ('$L1', '$@a', '$undefined', '$$a', '$a:', '$a:../x', '$a:items:-1',
                          '$a:items:01', '$a:items:99999999999999999999999', '$a:__proto__',
                          '$a:constructor', '$a:prototype', '$a:items:props', 'ordinary string'):
            with self.subTest(reference=reference), self.assertRaises(RuntimeError):
                extract_seed(flight([('10', model(reference)), ('a', {'items': [1], '__proto__': {}})]))

    def test_props_alias_requires_a_react_element(self):
        with self.assertRaisesRegex(RuntimeError, 'list path'):
            extract_seed(flight([('10', model('$a:props')), ('a', ['x', 'node', None, {'id': 'a', 'title': 'A'}])]))

    def test_direct_indirect_and_path_cycles_fail_closed(self):
        cases = [('$a', [('a', '$a')]), ('$a', [('a', '$b'), ('b', '$a')]),
                 ('$a:child', [('a', {'child': '$a:child'})]),
                 ('$a:child:id', [('a', {'child': '$b'}), ('b', '$a:child')])]
        for reference, records in cases:
            with self.subTest(reference=reference, records=records), self.assertRaisesRegex(RuntimeError, 'Cyclic'):
                extract_seed(flight([('10', model(reference)), *records]))

    def test_excessive_reference_chain_is_bounded(self):
        records = [('10', model('$100'))]
        records += [(format(i, 'x'), '$' + format(i + 1, 'x')) for i in range(256, 326)]
        records.append((format(326, 'x'), {'id': 'a', 'title': 'A'}))
        with self.assertRaisesRegex(RuntimeError, 'limit exceeded'):
            extract_seed(flight(records))

    def test_wrong_container_types_are_rejected(self):
        cases = [model(42), model(None), model([]), model('$a')]
        cases += [{'seed': {'firstPage': value}} for value in ({}, None, 'text')]
        cases += [{'seed': {'firstPage': [value]}} for value in (None, [], 1)]
        cases += [{'seed': {'firstPage': [{'items': value}]}} for value in (None, {}, 1)]
        for value in cases:
            with self.subTest(value=value), self.assertRaises(RuntimeError):
                extract_seed(flight([('10', value), ('a', 'not a model reference')]))

    def test_duplicate_model_record_is_rejected(self):
        with self.assertRaisesRegex(RuntimeError, 'Duplicate'):
            extract_seed(flight([('10', model({'id': 'a'})), ('10', model({'id': 'b'}))]))

    def test_non_json_flight_records_do_not_break_legacy_inline_seed(self):
        html = '<script>self.__next_f.push([1,' + json.dumps('a:I["module"]\n') + '])</script>'
        item = {'id': 'a', 'title': 'A'}
        self.assertEqual(extract_seed(html + flight([('10', model(item))]))['firstPage'][0]['items'], [item])

    def test_required_fields_and_safe_ids_are_validated(self):
        seed = model({'id': 'a', 'title': 'A'})[3]['seed']
        bad = []
        for total in (None, True, '1', 0, -1, 1.5):
            bad.append(dict(seed, total=total))
        for item in ({}, {'id': 'a'}, {'id': 7, 'title': 'A'}, {'id': 'a', 'title': 2},
                     {'id': 'a', 'title': ' '}, {'id': '', 'title': 'A'},
                     {'id': '../escape', 'title': 'A'}, {'id': 'a?x=1', 'title': 'A'},
                     {'id': '//evil', 'title': 'A'}, '$a'):
            value = copy.deepcopy(seed);value['firstPage'][0]['items'] = [item];bad.append(value)
        for section in ({'items': []}, {'id': 1, 'items': []}, {'id': '', 'items': []}, {'id': 'money'}, None):
            bad.append(dict(seed, firstPage=[section]))
        bad += [None, {}, dict(seed, firstPage=[]), dict(seed, firstPage={})]
        for value in bad:
            with self.subTest(value=value), self.assertRaisesRegex(RuntimeError, 'no snapshot saved'):
                validate_catalog_seed(value)
        validate_catalog_seed(seed)

    def test_invalid_listing_never_fetches_details_or_writes_snapshot(self):
        for value in (model('$missing'), model({'id': '../escape', 'title': 'A'}), model({'id': 'a', 'title': None})):
            with self.subTest(value=value), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp);db = root / 'history.sqlite3'
                def fetch(url):
                    if url.endswith('/robots.txt'):
                        return 'User-agent: *\nAllow: /'
                    self.assertEqual(url, 'https://agentusecases.ai/')
                    return flight([('10', value)])
                with patch('sys.argv', ['crawler', '--db', str(db)]), patch('agentwatch.crawler.fetch', fetch):
                    with self.assertRaises(RuntimeError):
                        main()
                self.assertEqual(list(root.iterdir()), [])

    def test_real_format_crawler_saves_reference_at_original_priority_and_position(self):
        html = FIXTURE.read_text()
        seed = extract_seed(html)
        ids = [x['id'] for x in seed['firstPage'][0]['items']]
        catalog_ids = ids + ['extra-' + str(i) for i in range(1427 - len(ids))]
        sitemap = '<urlset>' + ''.join('<url><loc>https://agentusecases.ai/use-case/' + i + '</loc></url>' for i in catalog_ids) + '</urlset>'
        def fetch(url):
            if url.endswith('/robots.txt'):
                return 'User-agent: *\nAllow: /'
            if url.endswith('/sitemap.xml'):
                return sitemap
            if '/use-case/' in url:
                return '<h1>Case title</h1><p>A public case body that is long enough for a valid saved observation.</p><h2>Want help getting this working?</h2>'
            return html
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / 'history.sqlite3'
            with patch('sys.argv', ['crawler', '--limit', '30', '--workers', '1', '--db', str(db)]), patch('agentwatch.crawler.fetch', fetch), redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                main()
            with sqlite3.connect(db) as connection:
                observed = connection.execute('SELECT url,position FROM observations ORDER BY position').fetchall()
                priorities = connection.execute('SELECT url,position,category FROM priorities ORDER BY position').fetchall()
                self.assertEqual([url.rsplit('/', 1)[-1] for url, _ in observed], ids)
                self.assertEqual(observed[13], ('https://agentusecases.ai/use-case/' + TARGET, 14))
                self.assertEqual(priorities[13], (observed[13][0], 14, 'money'))
                self.assertEqual(connection.execute('SELECT count(*) FROM catalogs').fetchone()[0], 1427)
                self.assertEqual(connection.execute('SELECT count(*) FROM archive_observations').fetchone()[0], 30)
            result = json.loads((db.parent / 'runs/1.json').read_text())
            self.assertEqual(result['failures'], [])
            self.assertTrue(result['complete_catalog'])
            self.assertFalse(result['details_complete'])
