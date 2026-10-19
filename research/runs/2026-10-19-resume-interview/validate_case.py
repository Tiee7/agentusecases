"""Offline checks of this research artifact; no real interviews or model calls."""
import json,hashlib
from pathlib import Path
from agentwatch.business import validate,economics
from agentwatch.author_method import validate_author_method
K='interview-candidates-based-on-their-resume'
r=json.load(open('research/'+K+'.json'));e=json.load(open('research/evidence/'+K+'.json'))
c=next(x for x in json.load(open('registry/cases.json'))['cases'] if x['id']==K)
checks=[]
def check(n,v):
 assert v,n
 checks.append(n)
validate(r,e,K);check('deep_schema_and_sources',True)
validate_author_method(r,c,e,required=True);check('original_author_receipt_matches',True)
a=json.load(open('registry/archives/'+K+'.json'));t=json.load(open('translations/'+K+'.json'))
check('original_hash',hashlib.sha256(a['source_text']['body'].encode()).hexdigest()==a['body_sha256'])
check('translation_binding',t['based_on_body_sha256']==a['body_sha256'])
check('translation_hash',hashlib.sha256(t['body'].encode()).hexdigest()==t['body_sha256'])
check('actual_vs_recommended_tools',r['source_case']['actual_agents']==['n8n'] and r['source_trial']['agent']=='Claude')
check('trial_literal_preserved',r['try_it']['prompts'][0]['text']==r['source_trial']['text'])
check('synthetic_only_trial','完全虚构' in r['try_it']['prompts'][1]['text'] and '不输出候选排名' in r['try_it']['prompts'][1]['text'])
check('no_false_product_feedback',r['scores']['feedback']['score']==0 and all(x['directness']=='adjacent_workflow' for x in r['feedback']['observations']))
check('basic_economics',economics(r['unit_economics'][0])==(8.5,3.5,50.0))
check('stress_economics',all(abs(a-b)<1e-7 for a,b in zip(economics(r['unit_economics'][1]),(18.2,-6.2,-810))))
claim=json.load(open('research/claims/'+K+'.json'));check('spark_exclusion',len(set(claim['excluded_spark_ids']))==20 and K not in claim['excluded_spark_ids'])
check('one_new_record',len([x for x in json.load(open('registry/cases.json'))['cases'] if x['id']==K])==1)
print(json.dumps({'passed':len(checks),'checks':checks,'scope':'Research record, exact source binding and arithmetic only; no product or hiring performance validation.'},ensure_ascii=False,indent=2))
