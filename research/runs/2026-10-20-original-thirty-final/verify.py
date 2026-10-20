"""Fixed-batch checks. No network, account actions or claimed product trials."""
import hashlib,json
from pathlib import Path
from agentwatch.business import validate
from agentwatch.personal import validate_personal
from agentwatch.author_method import validate_author_method
ROOT=Path(__file__).resolve().parents[3]
RUN=Path(__file__).parent
read=lambda p:json.loads(p.read_text())
sha=lambda text:hashlib.sha256(text.encode()).hexdigest()
def verify():
 scope=read(RUN/'scope.json');entries={x['id']:x for x in read(ROOT/'registry/cases.json')['cases']};checks=[]
 assert len(scope['cases'])==30 and len({x['id'] for x in scope['cases']})==30
 assert sum(x['depth']=='deep' for x in scope['cases'])==11
 for x in scope['cases']:
  k=x['id'];r=read(ROOT/x['path']);a=read(ROOT/'registry/archives'/f'{k}.json');entry=entries[k]
  ep=ROOT/'research/evidence'/f'{k}.json';ev=read(ep) if ep.exists() else r['sources']
  assert r['id']==k and r['analysis_depth']==x['depth'] and r['status']=='completed'
  if x['depth']=='deep':validate(r,ev,k)
  validate_personal(r,True)
  ap=ROOT/'research/author-method-evidence'/f'{k}.json';validate_author_method(r,entry,read(ap) if ap.exists() else ev,True)
  assert sha(a['source_text']['body'])==a['body_sha256']
  assert sha(a['translation']['body'])==a['translation']['body_sha256']
  assert a['translation']['based_on_body_sha256']==a['body_sha256']
  assert sha((ROOT/'registry/archives'/f'{k}.json').read_text())==x['baseline_archive_file_sha256'], 'Licensed original and full translation must be preserved'
  assert r['source_trial']==entry['source_trial'], 'Copy prompt and suggested agent must match registered observation'
  ids={s['id'] for s in r['sources']}
  def refs(o):
   if isinstance(o,dict):
    for key,v in o.items():
     if key=='source_ids':assert isinstance(v,list) and all(i in ids for i in v),(k,v)
     else:refs(v)
   elif isinstance(o,list):
    for v in o:refs(v)
  refs(r)
  rp=ROOT/'reports'/('brief' if x['depth']=='brief' else '')/f'{k}.md';assert rp.exists()
  checks.append({'rank':x['rank'],'id':k,'depth':x['depth'],'record_sha256':sha((ROOT/x['path']).read_text()),'report_sha256':sha(rp.read_text()),'original_sha256':a['body_sha256'],'translation_sha256':a['translation']['body_sha256'],'schema_personal_method_references_prompt_original_translation':'passed'})
 restaurant=read(ROOT/'research/book-a-restaurant-table-and-add-it-to-the-calendar.json')
 assert restaurant['score_status']=='not_assessed' and all(v['score'] is None for v in restaurant['scores'].values())
 models=restaurant['unit_economics'];costs=[]
 for m in models:
  assert m['price'] is None and m['units_per_month']==20 and m['revenue_status']=='unknown'
  costs.append(sum(m[f] for f in ['api_cost','human_cost','other_variable_cost','acquisition_cost'])*20+m['fixed_monthly_cost'])
 assert abs(costs[0]-320)<1e-6 and abs(costs[1]-583.3333333333)<1e-6
 return {'case_checks':checks,'deep':11,'brief':19,'restaurant_monthly_cost_scenarios':costs,'scope':'Document/schema/source traceability and hypothetical arithmetic only; no real agent or business execution.'}
if __name__=='__main__':print(json.dumps(verify(),ensure_ascii=False,indent=2))
