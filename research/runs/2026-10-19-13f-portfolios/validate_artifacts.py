import json,hashlib
from pathlib import Path as P
from agentwatch.author_method import validate_author_method
K='research-hedge-fund-portfolios-from-13f-filings';run=P('research/runs/2026-10-19-13f-portfolios')
d=json.load(open('research/'+K+'.json'));a=json.load(open('registry/archives/'+K+'.json'));tr=json.load(open('translations/'+K+'.json'));e=json.load(open('research/evidence/'+K+'.json'));c=next(x for x in json.load(open('registry/cases.json'))['cases'] if x['id']==K);text=P('reports/'+K+'.md').read_text();checks=[]
def ck(n,v):assert v,n;checks.append(n)
sha=lambda t:hashlib.sha256(t.encode()).hexdigest()
ck('source_hash',sha(a['source_text']['body'])==a['body_sha256'])
ck('translation_binding',tr['based_on_body_sha256']==a['body_sha256'] and sha(tr['body'])==tr['body_sha256'])
ck('whole_english',all('    '+s in text for s in a['source_text']['body'].splitlines()))
ck('whole_chinese',all('    '+s in text for s in tr['body'].splitlines()))
ck('chinese_first_english_folded',text.index('## 中文')<text.index('<details>') and '<summary>English original</summary>' in text)
validate_author_method(d,c,e,required=True);ck('author_receipt',True)
ck('original_prompt_exact',c['source_trial']['text']==d['source_trial']['text']==next(x['text'] for x in d['try_it']['prompts'] if x['kind']=='original'))
ck('spark_excluded',K not in json.load(open('research/claims/'+K+'.json'))['excluded_spark_ids'])
ck('ten_sections',len(d['sections'])==10 and sum(len(x['body']) for x in d['sections'])>=3500)
for r in e:ck('receipt_'+r['id'],sha(P('data/research-reads/13f/'+r['id']+'.txt').read_text())==r['sha256'])
for x,target in zip(d['unit_economics'],[300,-310]):
 result=(x['price']-x['api_cost']-x['human_cost']-x['other_variable_cost']-x['acquisition_cost'])*x['units_per_month']-x['fixed_monthly_cost'];ck('economic_'+str(target),result==target)
ck('all_briefs_stay_brief',all('| brief |' in next(l for l in P('registry/CATALOG.md').read_text().splitlines() if l.startswith('| `'+json.load(open(f))['id']+'` |')) for f in P('research/brief').glob('*.json') if json.load(open(f)).get('status')=='completed'))
print(json.dumps({'passed':len(checks),'checks':checks,'scope':'Artifact and arithmetic verification, no real product or growth trial.'},ensure_ascii=False,indent=2))

