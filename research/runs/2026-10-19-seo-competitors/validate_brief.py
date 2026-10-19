import json,hashlib
from pathlib import Path as P
from agentwatch.author_method import validate_author_method
k='find-seo-competitors-with-chatgpt-pro-agent';b=json.load(open('research/brief/'+k+'.json'));a=json.load(open('registry/archives/'+k+'.json'));t=json.load(open('translations/'+k+'.json'));e=json.load(open('research/evidence/'+k+'.json'));c=next(x for x in json.load(open('registry/cases.json'))['cases'] if x['id']==k);checks=[]
def ck(name,v):
 assert v,name
 checks.append(name)
ck('brief_not_deep',b['analysis_depth']=='brief' and b['commercial_score'] is None and not P('research/'+k+'.json').exists())
ck('full_source_hash',hashlib.sha256(a['source_text']['body'].encode()).hexdigest()==a['body_sha256'])
ck('full_translation_hash_binding',t['based_on_body_sha256']==a['body_sha256'] and hashlib.sha256(t['body'].encode()).hexdigest()==t['body_sha256'])
ck('report_contains_whole_source',all('    '+x in P('reports/brief/'+k+'.md').read_text() for x in a['source_text']['body'].splitlines()))
ck('report_contains_whole_translation',all('    '+x in P('reports/brief/'+k+'.md').read_text() for x in t['body'].splitlines()))
ck('original_prompt_preserved',c['source_trial']['text']==b['source_trial']['text'])
validate_author_method(b,c,e,required=True);ck('author_receipt',True)
ids={s['id'] for s in e};ck('all_refs_valid',all(set(s['source_ids'])<=ids for s in b['analysis']+b['facts']))
ck('no_invented_economics',b['unit_economics']==[])
claim=json.load(open('research/claims/'+k+'.json'));ck('spark_excluded',len(set(claim['excluded_spark_ids']))==20 and k not in claim['excluded_spark_ids'])
print(json.dumps({'passed':len(checks),'checks':checks,'scope':'Brief artifact checks only; no real SEO changes or traffic outcome test.'},indent=2))
