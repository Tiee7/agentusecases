import json
import sqlite3
import tempfile
import unittest
from pathlib import Path
from agentwatch.archive import extract, public_observation, apply, sha
from agentwatch.crawler import database, save
from agentwatch.public_history import export
from agentwatch.source_case import latest

URL='https://agentusecases.ai/use-case/fixture'
TIME='2026-10-16T09:00:00+00:00'
class ArchiveTests(unittest.TestCase):
    def test_visible_zero_is_distinct_from_unknown_and_related_tags(self):
        html='<h1>Fixture</h1><button>I want this 0</button><a href="/category/work">Work</a>Related use cases<a href="/topics/other">Other</a>'
        raw=extract(html,URL,TIME)
        self.assertEqual(raw['fields']['wanted'],0)
        self.assertIsNone(raw['fields']['tags'])
        self.assertEqual(raw['fields']['category']['label'],'Work')
        self.assertIsNone(extract(html.replace('this 0','this'),URL,TIME)['fields']['wanted'])
    def test_public_receipt_preserves_case_text_and_unknown(self):
        raw={'url':URL,'observed_at':TIME,'html_sha256':sha('html'),'body_sha256':sha('body'),'fields':{'method':'PUBLIC CASE NARRATIVE','wanted':0,'actual_agents':['Actual agent']}}
        value=public_observation(raw)
        self.assertEqual(value['fields']['method']['value'],'PUBLIC CASE NARRATIVE')
        self.assertEqual(value['fields']['wanted']['value'],0)
        self.assertEqual(value['fields']['author']['status'],'not_observed')
        self.assertEqual(value['fields']['method']['status'],'observed')
    def test_refresh_retains_review_basis_and_failed_attempt(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);db=database(root/'db')
            old={'observed_at':None,'editorial':{'based_on_body_sha256':'old'}}
            (root/'fixture.json').write_text(json.dumps(old))
            payload={'url':URL,'observed_at':TIME,'body_sha256':'new'}
            db.execute('INSERT INTO archive_observations VALUES(?,?,?,?)',(URL,TIME,'hash',json.dumps(payload)))
            db.execute('INSERT INTO fetch_attempts VALUES(?,?,?,?)',(URL,TIME,'failed','Fixture error'))
            apply(db,root)
            got=json.loads((root/'fixture.json').read_text())
            self.assertEqual(got['body_sha256'],'new');self.assertEqual(got['editorial'],old['editorial'])
            self.assertEqual(got['last_attempt']['status'],'failed')
            db.close()
    def test_export_retains_case_body_actual_agents_and_hash(self):
        with tempfile.TemporaryDirectory() as tmp:
            source=Path(tmp)/'source';target=Path(tmp)/'public'
            db=database(source)
            body='Title\nDone with\nClaude Code\nWhat they did\nPUBLIC CASE NARRATIVE'
            save(db,'https://agentusecases.ai/','site_category_top',[{'url':URL,'title':'Title','body':body}],None,[])
            before=latest(db);db.close();export(source,target)
            db=sqlite3.connect(target)
            self.assertEqual(db.execute('SELECT body FROM observations').fetchone()[0],body)
            self.assertEqual(latest(db),before);db.close()
            self.assertIn(b'PUBLIC CASE NARRATIVE',target.read_bytes())
    def test_public_archive_coverage_and_review_provenance(self):
        cases=json.loads(Path('registry/cases.json').read_text())['cases'];reviewed=0
        for c in cases:
            a=json.loads(Path('registry/archives',c['id']+'.json').read_text())
            self.assertEqual(a['url'],c['url']);self.assertEqual(len(a['body_sha256']),64)
            self.assertEqual(sha(a['source_text']['body']),a['body_sha256'])
            for key in ('introduction','method','outcome','notes'):
                if a['fields'][key]['status']=='observed':self.assertTrue(a['fields'][key]['value'])
            if a.get('editorial'):
                reviewed+=1;self.assertEqual(len(a['editorial']['based_on_body_sha256']),64)
                self.assertEqual(set(a['editorial']['sections']),{'introduction','method','outcome','notes'})
        self.assertGreaterEqual(reviewed,23)

    def test_external_articles_are_outside_archive_scope(self):
        with self.assertRaises(ValueError):public_observation({'url':'https://other.example/article'})
    def test_full_translations_match_source_version_and_hash(self):
        count=0
        for p in Path('registry/archives').glob('*.json'):
            a=json.loads(p.read_text());t=a.get('translation')
            if t:
                count+=1;self.assertEqual(t['based_on_body_sha256'],a['body_sha256'])
                self.assertEqual(sha(t['body']),t['body_sha256'])
                for url in a['fields']['original_sources']['value'] or []:self.assertIn(url,t['body'])
        self.assertGreaterEqual(count,7)
