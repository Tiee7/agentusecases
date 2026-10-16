import copy
import json
import os
import tempfile
import unittest
from pathlib import Path
from agentwatch.business import validate, weighted_score, economics, render, safe_id, select_case, indexes, publish, WEIGHTS, SECTIONS

class BusinessTests(unittest.TestCase):
    def setUp(self):
        self.previous=os.getcwd()
        self.temp=tempfile.TemporaryDirectory()
        os.chdir(self.temp.name)
        Path('registry').mkdir();Path('research').mkdir();Path('reports').mkdir()
        Path('registry/cases.json').write_text(json.dumps({'cases':[{'id':'real-case','url':'https://agentusecases.ai/use-case/real-case','title':'Case','report':'reports/real-case.md','record':'research/real-case.json','listed':True,'original_sources':['https://publisher0.test/doc']}]}))
        kinds=['primary','primary','independent','competitor','market','feedback']
        self.receipts=[{'id':f'S{i}','url':f'https://publisher{i}.test/doc','kind':kind,'status':'fetched','sha256':'fixture','fetched_at':'2026-10-14T14:00:00+00:00'} for i,kind in enumerate(kinds)]
        self.record={'schema_version':2,'status':'completed','id':'real-case','url':'https://agentusecases.ai/use-case/real-case','title':'用测试 agent 整理资料','industry':'Fixture','researched_at':'2026-10-14T22:00:00+08:00','confidence':'Fixture, not real data','verdict':{'decision':'适合内部效率工具','headline':'A specific fixture commercial decision with evidence','reason':'A fixture commercial argument '*10,'next_action':'Measure fixture cost','stop_condition':'No measurable value'},'sources':[{'id':r['id'],'url':r['url'],'title':r['id'],'supports':'A specific bounded business fact in this synthetic source'} for r in self.receipts],'facts':[{'statement':'A specific source-backed synthetic business fact','source_ids':['S0']} for _ in range(8)],'sections':[{'id':key,'title':key,'body':('Substantive synthetic commercial analysis. '*12),'source_ids':['S0']} for key in SECTIONS],'scores':{k:{'score':4,'rationale':'A specific evidence-backed commercial rationale','source_ids':['S0']} for k in WEIGHTS},'feedback':{'searches':[{'channel':str(i%2),'query':'fixture query','outcome':'No verified users'} for i in range(3)],'observations':[]},'unit_economics':[{'scenario':f'Scenario {i}','unit':'delivery','currency':'USD','price':100,'api_cost':2,'human_cost':30,'other_variable_cost':3,'acquisition_cost':5,'units_per_month':10,'fixed_monthly_cost':100,'assumptions':'All synthetic scenario assumptions, not real operations','source_ids':['S0']} for i in range(2)],'disconfirming_evidence':'Synthetic opposing evidence','limitations':'No real model or business verification'}
        self.record['scores']['feedback']['score']=0
    def tearDown(self):
        os.chdir(self.previous);self.temp.cleanup()
    def test_complete_report_and_exact_mapping(self):
        from agentwatch.personal import FIELDS
        self.record['personal_value'] = dict(version=1,level='待核实',reason='Synthetic fixture',source_ids=[],**{k:'Unverified fixture' for k in FIELDS})
        self.record['try_it'] = dict(source_prompt_status='missing',source_prompt_note='Not collected',prerequisites='Synthetic data',tools='Text editor',expected_result='Draft',prompts=[])
        self.record['author_method']={'version':1,'status':'unavailable','presentation':'bilingual_summary','source_url':'https://publisher0.test/doc','source_title':'Fixture source','steps':[],'unavailable_reason':'Source unavailable'}
        validate(self.record,self.receipts,'real-case')
        Path('draft.json').write_text(json.dumps(self.record));Path('receipts.json').write_text(json.dumps(self.receipts))
        publish('draft.json','receipts.json','real-case')
        self.assertTrue(Path('reports/real-case.md').exists())
        self.assertIn('reports/real-case.md',Path('INDEX.md').read_text())
        self.assertIn('completed',Path('registry/CATALOG.md').read_text())
        self.assertIsNone(select_case())
    def test_new_publication_requires_extensions_but_old_validation_works(self):
        validate(self.record,self.receipts,'real-case')
        Path('draft.json').write_text(json.dumps(self.record));Path('receipts.json').write_text(json.dumps(self.receipts))
        with self.assertRaisesRegex(ValueError,'New publications'):
            publish('draft.json','receipts.json','real-case')
        self.assertFalse(Path('research/real-case.json').exists())
    def test_judgment_titles_cannot_publish_or_render(self):
        self.record['title']='用测试 agent 整理资料：适合内部效率工具'
        with self.assertRaisesRegex(ValueError,'judgment'):
            validate(self.record,self.receipts,'real-case')
        with self.assertRaisesRegex(ValueError,'judgment'):
            render(self.record)
    def test_aggregate_intro_only_cannot_pass(self):
        bad=copy.deepcopy(self.record);bad['sources']=bad['sources'][:1]
        with self.assertRaises(ValueError):validate(bad,self.receipts,'real-case')
    def test_unread_or_fabricated_sources_cannot_pass(self):
        receipts=copy.deepcopy(self.receipts);receipts[0]['status']='blocked'
        with self.assertRaises(ValueError):validate(self.record,receipts,'real-case')
    def test_mismatched_case_cannot_publish(self):
        bad=copy.deepcopy(self.record);bad['id']='another-case'
        with self.assertRaises(ValueError):validate(bad,self.receipts,'real-case')
    def test_old_draft_is_not_completed(self):
        Path('research/real-case.json').write_text(json.dumps({'status':'draft','url':self.record['url']}))
        self.assertEqual(select_case()['id'],'real-case')
        indexes();self.assertIn('旧版简略初稿 **1**',Path('INDEX.md').read_text())
    def test_no_user_evidence_cannot_get_feedback_credit(self):
        self.record['scores']['feedback']['score']=5
        with self.assertRaises(ValueError):validate(self.record,self.receipts,'real-case')
    def test_costs_and_feedback_weight_are_exact(self):
        self.assertEqual(economics(self.record['unit_economics'][0]),(40,60,500))
        self.assertEqual(weighted_score(self.record),76)
        self.assertEqual(WEIGHTS['feedback'],5)
        self.assertIn('月经营贡献',render(self.record))
    def test_path_traversal_is_rejected(self):
        with self.assertRaises(ValueError):safe_id('../stolen')
    def test_nonfinite_financial_assumptions_are_rejected(self):
        self.record['unit_economics'][0]['price']=float('nan')
        with self.assertRaises(ValueError):validate(self.record,self.receipts,'real-case')
    def test_research_time_requires_timezone(self):
        self.record['researched_at']='2026-10-14T22:00:00'
        with self.assertRaises(ValueError):validate(self.record,self.receipts,'real-case')
    def test_scenario_rows_form_one_readable_table(self):
        text=render(self.record)
        rows=[line for line in text.splitlines() if line.startswith('| Scenario')]
        self.assertEqual(len(rows),2)
        self.assertIn(rows[0]+'\n'+rows[1],text)
    def test_sampled_details_do_not_delist_unsampled_cases(self):
        from agentwatch.crawler import database,save
        from agentwatch.business import bootstrap,read_registry
        db=database('sample.sqlite3')
        urls=['https://agentusecases.ai/use-case/real-case','https://agentusecases.ai/use-case/second-case']
        save(db,'https://agentusecases.ai/','site_category_top',[{'url':urls[0],'title':'Case','body':'body'}],dict.fromkeys(urls,'2026-10-14'))
        db.close()
        bootstrap('sample.sqlite3')
        cases=read_registry()['cases']
        self.assertEqual(len(cases),2)
        self.assertTrue(all(c['listed'] for c in cases))
        self.assertTrue(all(c['first_seen_at'] for c in cases))
        dates={c['id']:c['first_seen_at'] for c in cases}
        bootstrap('sample.sqlite3')
        self.assertEqual(dates,{c['id']:c['first_seen_at'] for c in read_registry()['cases']})
    def test_generic_sources_cannot_be_misassigned_to_a_case(self):
        registry=json.loads(Path('registry/cases.json').read_text())
        registry['cases'][0]['original_sources']=['https://another-project.test/original']
        Path('registry/cases.json').write_text(json.dumps(registry))
        with self.assertRaises(ValueError):validate(self.record,self.receipts,'real-case')
