import json
import os
import tempfile
import unittest
from pathlib import Path
from agentwatch.crawler import database, save
from agentwatch.catalog_refresh import refresh, research_fingerprints

class CatalogRefreshTests(unittest.TestCase):
    def setUp(self):
        self.previous=os.getcwd();self.temp=tempfile.TemporaryDirectory();os.chdir(self.temp.name)
        for name in ('registry','research','reports'):Path(name).mkdir()
        self.url='https://agentusecases.ai/use-case/existing'
        entry={'id':'existing','url':self.url,'title':'Old title','category':'money','first_seen_at':'2026-01-01T00:00:00Z','record':'research/existing.json','report':'reports/existing.md','original_sources':[]}
        Path('registry/cases.json').write_text(json.dumps({'cases':[entry]}))
        # Non-completed research still belongs to research; the crawler cannot replace it.
        Path('research/existing.json').write_text(json.dumps({'schema_version':1,'title':'Research title','author_method':{'steps':['research-owned']},'private_fixture':'preserve'}))
        Path('reports/existing.md').write_text('Research-owned report')
    def tearDown(self):os.chdir(self.previous);self.temp.cleanup()
    def test_changed_and_new_catalog_entries_preserve_research_fields(self):
        db=database('history.sqlite3');new='https://agentusecases.ai/use-case/new'
        save(db,'https://agentusecases.ai/','site_category_top',[{'url':self.url,'title':'Changed title','body':'Changed public detail'},{'url':new,'title':'New case','body':'New detail'}],{self.url:'2026-10-16',new:'2026-10-16'});db.close()
        before=research_fingerprints();metadata=refresh('history.sqlite3');self.assertEqual(research_fingerprints(),before)
        entries=json.loads(Path('registry/cases.json').read_text())['cases'];self.assertEqual(len(entries),2)
        old=next(e for e in entries if e['id']=='existing');self.assertEqual(old['title'],'Changed title');self.assertEqual(old['first_seen_at'],'2026-01-01T00:00:00Z')
        self.assertEqual(metadata['detail_pages_read'],2);self.assertTrue(metadata['details_complete'])
        # A research update between refresh attempts is read from the current checkout,
        # not overwritten with the crawler artifact's earlier state.
        Path('reports/existing.md').write_text('Newer research from main')
        before=research_fingerprints();refresh('history.sqlite3');self.assertEqual(research_fingerprints(),before)
    def test_detail_sample_is_not_labelled_complete_and_missing_snapshot_fails(self):
        db=database('history.sqlite3')
        with self.assertRaisesRegex(ValueError,'No successful'):refresh('history.sqlite3')
        save(db,'https://agentusecases.ai/','site_category_top',[{'url':self.url,'title':'Updated','body':'Detail'}],{self.url:None,'https://agentusecases.ai/use-case/unsampled':None});db.close()
        result=refresh('history.sqlite3');self.assertFalse(result['details_complete']);self.assertEqual(result['catalog_observed'],2)
    def test_null_registry_source_timestamp_is_replaced_without_modifying_research(self):
        from agentwatch.source_case import observe
        body='What they did\nExisting public detail'
        registry=json.loads(Path('registry/cases.json').read_text())
        registry['cases'][0]['source_case']=observe(body,self.url,None)
        registry['cases'][0]['source_case']['summary']={'fixture':'reviewed summary'}
        Path('registry/cases.json').write_text(json.dumps(registry))
        db=database('history.sqlite3')
        save(db,'https://agentusecases.ai/','site_category_top',[{'url':self.url,'title':'Updated','body':body}],{self.url:None})
        fetched_at=db.execute('SELECT fetched_at FROM runs ORDER BY id DESC LIMIT 1').fetchone()[0]
        db.close()
        before=research_fingerprints()
        metadata=refresh('history.sqlite3')
        self.assertTrue(metadata['details_complete'])
        self.assertEqual(research_fingerprints(),before)
        result=json.loads(Path('registry/cases.json').read_text())['cases'][0]['source_case']
        self.assertEqual(result['observed_at'],fetched_at)
        self.assertEqual(result['summary'],{'fixture':'reviewed summary'})
        registry_bytes=Path('registry/cases.json').read_bytes()
        refresh('history.sqlite3')
        self.assertEqual(Path('registry/cases.json').read_bytes(),registry_bytes)
        self.assertEqual(research_fingerprints(),before)
    def test_refresh_keeps_exact_registered_sources_separate_from_latest_links(self):
        registered=['https://author.test/post/','https://earlier.test/report']
        observed=['https://author.test/post','https://different.test/new-source']
        registry=json.loads(Path('registry/cases.json').read_text())
        registry['cases'][0]['original_sources']=registered
        Path('registry/cases.json').write_text(json.dumps(registry))
        db=database('history.sqlite3')
        body='Public detail\n'+'\n'.join('Original source: '+url for url in observed)
        save(db,'https://agentusecases.ai/','site_category_top',[{'url':self.url,'title':'Updated','body':body}],{self.url:None});db.close()
        before=research_fingerprints();refresh('history.sqlite3')
        entry=json.loads(Path('registry/cases.json').read_text())['cases'][0]
        self.assertEqual(entry['latest_original_sources'],observed)
        self.assertEqual(entry['original_sources'],observed+registered)
        self.assertEqual(research_fingerprints(),before)
        refresh('history.sqlite3')
        self.assertEqual(json.loads(Path('registry/cases.json').read_text())['cases'][0],entry)
