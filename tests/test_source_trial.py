import copy
import json
import os
import sqlite3
import tempfile
import unittest
from pathlib import Path
from agentwatch.source_trial import extract_source_trial, validate_observation, export_observations
from agentwatch.crawler import database, save
from agentwatch.business import bootstrap

URL='https://agentusecases.ai/use-case/example'
STAMP='2026-10-15T17:00:00+00:00'  # synthetic fixture time, not a live observation

def ssr(value):
    return '<script>self.__next_f.push([1,'+json.dumps('a:'+json.dumps(value,ensure_ascii=False)+'\n').replace('<', r'\u003c')+'])</script>'

class SourceTrialTests(unittest.TestCase):
    def test_scoped_ssr_preserves_special_characters_and_separates_agent(self):
        prompt='中文 "quote" & <script>evil()</script>\nEnglish `code` ${value} \\ path'
        html=ssr({'id':'example','agent':'Custom-built','tryIt':{'agent':'Manus','prompt':prompt},'related':[{'id':'wrong','tryIt':{'agent':'Wrong','prompt':'AD'}}]})
        r=extract_source_trial(html,URL,STAMP)
        self.assertEqual((r['status'],r['agent'],r['text'],r['method']),('available','Manus',prompt,'ssr'))
        self.assertIn('不代表',r['attribution'])

    def test_actual_dom_cards_exclude_sponsor_and_preserve_complete_text(self):
        for filename,agent,start,end in [('retention-prompt-dom.html','Manus','Help me lower my','verification code.'),('reconcile-prompt-dom.html','Claude Code','Reconcile my business transactions','spot-check the categories.')]:
            r=extract_source_trial(Path('tests/fixtures/source-trials',filename).read_text(),URL,STAMP)
            self.assertEqual(r['status'],'available');self.assertEqual(r['method'],'dom');self.assertEqual(r['agent'],agent)
            self.assertTrue(r['text'].startswith(start));self.assertTrue(r['text'].endswith(end))
            self.assertNotIn('Vibe Coding',r['text']);self.assertNotIn('Want help',r['text'])

    def test_dom_entities_whitespace_and_nested_header(self):
        html='<p>Done with a custom-built agent</p><div><div><p>Try it yourself <span>with <!-- -->Manus</span></p><button>Copy prompt</button></div><p>中文 &lt;tag&gt; &amp; "quotes"\n  keep spaces</p><p>Want help getting this working? AD</p></div>'
        r=extract_source_trial(html,URL,STAMP)
        self.assertEqual(r['text'],'中文 <tag> & "quotes"\n  keep spaces')
        self.assertEqual(r['agent'],'Manus')

    def test_ssr_preferred_over_dom(self):
        html=Path('tests/fixtures/source-trials/retention-prompt-dom.html').read_text()+ssr({'id':'example','tryIt':{'agent':'Specific','prompt':'literal SSR text'}})
        self.assertEqual(extract_source_trial(html,URL,STAMP)['text'],'literal SSR text')

    def test_missing_null_malformed_related_and_ambiguous_do_not_invent_prompts(self):
        for html,status in [('<h1>Old detail</h1>','missing'),(ssr({'id':'example','tryIt':None}),'missing'),(ssr({'id':'wrong','tryIt':{'agent':'Wrong','prompt':'wrong'}}),'missing'),(ssr({'id':'example','tryIt':{'agent':'Manus','prompt':'$a1'}}),'unparseable'),(ssr([{'id':'example','tryIt':{'agent':'A','prompt':'a'}},{'id':'example','tryIt':{'agent':'B','prompt':'b'}}]),'unparseable')]:
            r=extract_source_trial(html,URL,STAMP);self.assertEqual(r['status'],status);self.assertIsNone(r['text'])

    def test_time_and_origin_validation(self):
        r=extract_source_trial(ssr({'tryIt':{'agent':'A','prompt':'P'}}),URL,STAMP)
        for change in [dict(source_url='javascript:bad'),dict(observed_at='2026-10-15'),dict(agent=''),dict(status='missing')]:
            with self.assertRaises(ValueError):validate_observation(dict(r,**change),URL)

    def test_database_migration_and_prompt_change_detection(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'history.sqlite3'
            old=sqlite3.connect(path);old.executescript('CREATE TABLE runs(id INTEGER PRIMARY KEY,fetched_at TEXT,listing_url TEXT,ordering TEXT);CREATE TABLE observations(run_id INTEGER,url TEXT,title TEXT,position INTEGER,digest TEXT,body TEXT,PRIMARY KEY(run_id,url));');old.close()
            db=database(path)
            trial=extract_source_trial(ssr({'tryIt':{'agent':'A','prompt':'P'}}),URL,STAMP)
            row=dict(url=URL,title='Example',body='body',source_trial=trial)
            a=save(db,'listing','unknown',[row],{URL:None});self.assertEqual(export_observations(db,a['run_id'])[URL],trial)
            row['source_trial']=dict(trial,observed_at='2026-10-15T18:00:00+00:00')
            self.assertEqual(save(db,'listing','unknown',[row],{URL:None})['cases'][0]['change'],'unchanged')
            row['source_trial']['text']='Changed prompt'
            self.assertEqual(save(db,'listing','unknown',[row],{URL:None})['cases'][0]['change'],'content_changed')
            db.close()

    def test_bootstrap_exports_and_preserves_unsampled_observations(self):
        previous=Path.cwd()
        with tempfile.TemporaryDirectory() as tmp:
            try:
                os.chdir(tmp)
                db=database('history.sqlite3')
                trial=extract_source_trial(ssr({'tryIt':{'agent':'A','prompt':'P'}}),URL,STAMP)
                save(db,'listing','unknown',[dict(url=URL,title='Example',body='body',source_trial=trial)],{URL:None})
                bootstrap('history.sqlite3')
                self.assertEqual(json.loads(Path('registry/cases.json').read_text())['cases'][0]['source_trial'],trial)
                save(db,'listing','unknown',[],{URL:None})
                bootstrap('history.sqlite3')
                self.assertEqual(json.loads(Path('registry/cases.json').read_text())['cases'][0]['source_trial'],trial)
                self.assertFalse(Path('research/example.json').exists())  # never fabricate a completed research
                db.close()
            finally:os.chdir(previous)

    def test_import_updates_only_known_case_and_completed_report(self):
        from agentwatch.source_trial import apply_observations
        original=json.loads(Path('research/negotiate-retention-discounts-on-bills-by-phone.json').read_text())
        previous=Path.cwd()
        with tempfile.TemporaryDirectory() as tmp:
            try:
                os.chdir(tmp)
                for folder in ('registry','research','reports'):Path(folder).mkdir()
                record=copy.deepcopy(original);record['id']='example';record['url']=URL
                Path('research/example.json').write_text(json.dumps(record));Path('reports/example.md').write_text('prior report')
                cases=[dict(id='example',url=URL,title='Example',record='research/example.json',report='reports/example.md',listed=True),dict(id='pending',url=URL+'-pending',title='Pending',record='research/pending.json',report='reports/pending.md',listed=True)]
                Path('registry/cases.json').write_text(json.dumps({'schema_version':1,'cases':cases}))
                trial=extract_source_trial(ssr({'tryIt':{'agent':'Manus','prompt':'Full source prompt'}}),URL,STAMP)
                pending=dict(trial,source_url=URL+'-pending')
                apply_observations({URL:trial,URL+'-pending':pending})
                revised=json.loads(Path('research/example.json').read_text())
                self.assertEqual(revised['source_trial'],trial);self.assertEqual(revised['try_it']['source_prompt_status'],'collected')
                self.assertEqual(revised['scores'],original['scores']);self.assertEqual(revised['try_it']['prompts'],original['try_it']['prompts'])
                self.assertLess(Path('reports/example.md').read_text().index('Full source prompt'),Path('reports/example.md').read_text().index('中文试用模板'))
                self.assertFalse(Path('research/pending.json').exists())
                # Reimport older history must not replace the newer observed prompt.
                older=dict(trial,observed_at='2026-10-14T17:00:00+00:00',text='Old')
                apply_observations({URL:older});self.assertEqual(json.loads(Path('research/example.json').read_text())['source_trial']['text'],'Full source prompt')
                with self.assertRaises(ValueError):apply_observations({'https://unknown.test/case':trial})
            finally:os.chdir(previous)
