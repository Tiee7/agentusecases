import copy
import json
import sqlite3
import unittest
from pathlib import Path
from agentwatch.source_case import observe, merge, latest

URL='https://agentusecases.ai/use-case/fixture'
TIME='2026-10-14T15:02:21+00:00'
class SourceCaseTests(unittest.TestCase):
    def test_actual_and_recommended_are_distinct(self):
        body='Title\nDone with\nGB\nGrok Bot\nCC\nClaude Code\nN8\nn8n\nA+\nAlexa+\nWhat they did\nPrivate full prose\nHow it went\nUnverified\nTry it yourself\nwith\nChatGPT Agent\nCopy prompt\nPrivate prompt'
        value=observe(body,URL,TIME)
        self.assertEqual(value['actual_agents'],['Grok Bot','Claude Code','n8n','Alexa+'])
        self.assertNotIn('Private',json.dumps(value))
        self.assertEqual(value['agent_status'],'observed')
    def test_unknown_is_not_recommendation(self):
        value=observe('Done with a\ncustom-built or unnamed agent\nWhat they did\nWork\nTry it yourself\nwith\nManus',URL,TIME)
        self.assertEqual(value['agent_status'],'custom_or_unnamed');self.assertEqual(value['actual_agents'],[])
        value=observe('What they did\nWork\nTry it yourself\nwith\nManus',URL,TIME)
        self.assertEqual(value['agent_status'],'not_observed')
    def test_hash_invalidates_summary_and_older_observations_do_not_replace(self):
        old=observe('What they did\nFirst',URL,TIME);old['summary']={'fixture':True}
        self.assertIn('summary',merge(old,observe('What they did\nFirst',URL,TIME)))
        self.assertNotIn('summary',merge(old,observe('What they did\nChanged',URL,TIME)))
        earlier=observe('Earlier',URL,'2026-01-01T00:00:00Z')
        self.assertEqual(merge(old,earlier),old)
    def test_undated_previous_observations_accept_dated_updates(self):
        for stamp in (None, ''):
            for unchanged in (True, False):
                with self.subTest(stamp=stamp, unchanged=unchanged):
                    previous=observe('What they did\nFirst',URL,stamp)
                    previous['summary']={'fixture':True}
                    incoming=observe('What they did\n'+('First' if unchanged else 'Changed'),URL,TIME)
                    result=merge(previous,incoming)
                    self.assertIs(result,incoming)
                    self.assertEqual(result['observed_at'],TIME)
                    self.assertEqual('summary' in result,unchanged)
        previous=observe('First',URL,None);del previous['observed_at']
        self.assertEqual(merge(previous,observe('Changed',URL,TIME))['observed_at'],TIME)
    def test_undated_incoming_observations_do_not_replace_dated_metadata(self):
        previous=observe('What they did\nFirst',URL,TIME);previous['summary']={'fixture':True}
        for stamp in (None, ''):
            with self.subTest(stamp=stamp):
                self.assertIs(merge(previous,observe('Changed',URL,stamp)),previous)
        incoming=observe('Changed',URL,None);del incoming['observed_at']
        self.assertIs(merge(previous,incoming),previous)
    def test_two_undated_observations_still_follow_body_hash_rules(self):
        previous=observe('First',URL,None);previous['summary']={'fixture':True}
        self.assertEqual(merge(previous,observe('First',URL,None))['summary'],previous['summary'])
        self.assertNotIn('summary',merge(previous,observe('Changed',URL,None)))
    def test_unsampled_history_is_retained(self):
        db=sqlite3.connect(':memory:');db.executescript('CREATE TABLE observations(run_id,url,body);CREATE TABLE runs(id,fetched_at);')
        db.executemany('INSERT INTO runs VALUES(?,?)',[(1,TIME),(2,'2026-10-15T00:00:00Z')]);db.execute('INSERT INTO observations VALUES(1,?,?)',(URL,'Old body'))
        self.assertEqual(latest(db)[URL]['observed_at'],TIME)
    def test_complete_coverage_and_summary_provenance(self):
        cases=json.loads(Path('registry/cases.json').read_text())['cases'];count=0
        for c in cases:
            value=c['source_case'];self.assertEqual(value['source_url'],c['url'])
            if value.get('summary'):
                count+=1;s=value['summary'];self.assertEqual(s['based_on_sha256'],value['body_sha256'])
                self.assertEqual(set(s['sections']),{'introduction','method','outcome'})
                for section in s['sections'].values():self.assertTrue(section['en'] and section['zh'])
                record=json.loads(Path(c['record']).read_text());self.assertEqual(record['source_case']['source_url'],value['source_url'])
        # Coverage is a dated receipt, not a quota: future source changes invalidate summaries.

    def test_report_generation_uses_original_not_editorial(self):
        from agentwatch.source_case import render
        c=next(c for c in json.loads(Path('registry/cases.json').read_text())['cases'] if c['id']=='produce-investment-memos-with-claude-cowork')
        a=json.loads(Path('registry/archives',c['id']+'.json').read_text());result='\n'.join(render(c['source_case']))
        self.assertIn('## English',result);self.assertIn('\n'.join('    '+x if x else '' for x in a['source_text']['body'].splitlines()),result)
        self.assertNotIn('原创双语摘要',result);self.assertNotIn('观测时间',result);self.assertIn('## 中文',result);self.assertIn('\n'.join('    '+x if x else '' for x in a['translation']['body'].splitlines()),result)
    def test_report_generation_does_not_present_a_pending_translation_as_current(self):
        import os
        import tempfile
        from agentwatch.archive import sha
        from agentwatch.source_case import render
        previous=os.getcwd()
        with tempfile.TemporaryDirectory() as tmp:
            try:
                os.chdir(tmp);Path('registry/archives').mkdir(parents=True)
                value={'url':URL,'body_sha256':sha('English'),'source_text':{'body':'English'},'translation':{'status':'stale','body':'旧译文','body_sha256':sha('旧译文'),'based_on_body_sha256':sha('English')}}
                Path('registry/archives/fixture.json').write_text(json.dumps(value))
                result='\n'.join(render({'source_url':URL}))
                self.assertIn('English',result);self.assertNotIn('旧译文',result);self.assertNotIn('## 中文',result)
            finally:os.chdir(previous)
