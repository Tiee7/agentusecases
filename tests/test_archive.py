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
    def test_changed_source_preserves_old_text_and_translation_as_stale_history(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);db=database(root/'db')
            old_source={'format':'extracted_page_text','language':'en','body':'Old source','body_sha256':sha('Old source'),'archived_at':TIME}
            translation={'status':'available','format':'full_extracted_text_translation','body':'旧译文','body_sha256':sha('旧译文'),'based_on_body_sha256':sha('Old source'),'translated_at':TIME}
            old={'observed_at':TIME,'body_sha256':sha('Old source'),'source_text':old_source,'translation':translation}
            (root/'fixture.json').write_text(json.dumps(old))
            at='2026-10-17T09:00:00+00:00'
            new_source=dict(old_source,body='New source',body_sha256=sha('New source'),archived_at=at)
            payload={'url':URL,'observed_at':at,'body_sha256':sha('New source'),'source_text':new_source}
            db.execute('INSERT INTO archive_observations VALUES(?,?,?,?)',(URL,at,'hash',json.dumps(payload)))
            apply(db,root);got=json.loads((root/'fixture.json').read_text())
            self.assertEqual(got['source_text'],new_source)
            self.assertEqual(got['translation']['status'],'stale')
            self.assertTrue(got['translation']['review_required'])
            self.assertEqual(got['translation']['stale_reason'],'source_body_changed')
            for field in ('body','body_sha256','based_on_body_sha256','translated_at'):
                self.assertEqual(got['translation'][field],translation[field])
            self.assertEqual(got['source_history'][0]['source_text'],old_source)
            self.assertEqual(got['source_history'][0]['translation'],translation)
            before=(root/'fixture.json').read_bytes();apply(db,root)
            self.assertEqual((root/'fixture.json').read_bytes(),before)
            db.close()
    def test_only_latest_capture_determines_translation_freshness(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);db=database(root/'db')
            translation={'status':'available','body':'译文','body_sha256':sha('译文'),'based_on_body_sha256':sha('Current source')}
            old={'observed_at':None,'body_sha256':sha('Current source'),'translation':translation}
            (root/'fixture.json').write_text(json.dumps(old))
            for at,body in ((TIME,'Earlier source'),('2026-10-17T09:00:00+00:00','Current source')):
                payload={'url':URL,'observed_at':at,'body_sha256':sha(body)}
                db.execute('INSERT INTO archive_observations VALUES(?,?,?,?)',(URL,at,'hash',json.dumps(payload)))
            apply(db,root)
            self.assertEqual(json.loads((root/'fixture.json').read_text())['translation'],translation)
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

    def test_daily_preserves_exact_reviewed_edition_and_retains_latest_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp);root=base/'archives';root.mkdir();db=database(base/'db')
            old={'url':URL,'observed_at':TIME,'body_sha256':sha('Old source'),
                 'source_text':{'body':'Old source'},'translation':{'body':'旧译文','status':'available'}}
            exact=json.dumps(old,ensure_ascii=False,indent=4)+'\n'
            path=root/'fixture.json';path.write_text(exact)
            at='2026-10-21T06:00:00+00:00'
            payload={'url':URL,'observed_at':at,'body_sha256':sha('New source'),'source_text':{'body':'New source'}}
            db.execute('INSERT INTO archive_observations VALUES(?,?,?,?)',(URL,at,'hash',json.dumps(payload)))
            db.execute('INSERT INTO fetch_attempts VALUES(?,?,?,?)',(URL,at,'ok',None))
            apply(db,root,preserve_reviewed=True)
            self.assertEqual(path.read_text(),exact)
            pending=base/'archive-observations/fixture.json';got=json.loads(pending.read_text())
            self.assertEqual(got['source_text']['body'],'New source')
            self.assertNotIn('translation',got)
            self.assertEqual(got['published_edition']['archive_file_sha256'],sha(exact))
            self.assertTrue(got['published_edition']['review_required'])
            self.assertEqual(got['last_attempt']['status'],'ok')
            before=pending.read_bytes();apply(db,root,preserve_reviewed=True)
            self.assertEqual(pending.read_bytes(),before);self.assertEqual(path.read_text(),exact)
            # Older capture cannot replace a newer separately retained observation.
            db.execute('DELETE FROM archive_observations')
            db.execute('INSERT INTO archive_observations VALUES(?,?,?,?)',(URL,TIME,'old',json.dumps(dict(payload,observed_at=TIME))))
            apply(db,root,preserve_reviewed=True)
            self.assertEqual(pending.read_bytes(),before);db.close()

    def test_external_articles_are_outside_archive_scope(self):
        with self.assertRaises(ValueError):public_observation({'url':'https://other.example/article'})
    def test_full_translations_match_source_version_and_hash(self):
        count=0
        for p in Path('registry/archives').glob('*.json'):
            a=json.loads(p.read_text());t=a.get('translation')
            if t:
                self.assertEqual(sha(t['body']),t['body_sha256'])
                if t['status']=='available':
                    count+=1;self.assertEqual(t['based_on_body_sha256'],a['body_sha256'])
                    for url in a['fields']['original_sources']['value'] or []:self.assertIn(url,t['body'])
                else:
                    self.assertEqual(t['status'],'stale');self.assertTrue(t['review_required'])
                    self.assertEqual(t['stale_reason'],'source_body_changed')
                    self.assertTrue(any(h.get('body_sha256')==t['based_on_body_sha256'] and sha(h['source_text']['body'])==t['based_on_body_sha256'] for h in a.get('source_history',[])),p.name)
        self.assertGreaterEqual(count,7)
