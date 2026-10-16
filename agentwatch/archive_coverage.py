"""Current source-text/translation coverage, separate from dated historical batches."""
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

def update():
    cases=json.loads(Path('registry/cases.json').read_text())['cases']
    archives={c['id']:json.loads(Path('registry/archives',c['id']+'.json').read_text()) for c in cases if Path('registry/archives',c['id']+'.json').exists()}
    original=[k for k,a in archives.items() if a.get('source_text',{}).get('body')]
    translations=[k for k,a in archives.items() if a.get('translation',{}).get('status')=='available' and a['translation']['based_on_body_sha256']==a['body_sha256']]
    editorial=[k for k,a in archives.items() if a.get('editorial')]
    counts=Counter(c.get('source_case',{}).get('agent_status','not_observed') for c in cases)
    missing={key:[c['id'] for c in cases if archives.get(c['id'],{}).get('fields',{}).get(key,{}).get('status')!='observed'] for key in ('introduction','method','outcome','notes','author','category','tags','wanted','source_date','added_at')}
    value={'schema_version':2,'generated_at':datetime.now(timezone.utc).isoformat(),'current':{'registered_cases':len(cases),'original_texts_in_git':len(original),'complete_chinese_translations':len(translations),'chinese_translation_pending':len(cases)-len(translations),'detailed_bilingual_editorials':len(editorial),'editorial_pending':len(cases)-len(editorial),'completed_business_research':sum(Path(c['record']).exists() for c in cases),'legacy_short_summaries':sum(bool(c.get('source_case',{}).get('summary')) for c in cases),'html_receipts':sum(bool(a.get('html_sha256')) for a in archives.values()),'historical_extracted_text_receipts':sum(not bool(a.get('html_sha256')) for a in archives.values()),'agent_status_counts':dict(counts)},'original_text_missing_ids':[c['id'] for c in cases if c['id'] not in original],'translation_ids':translations,'translation_pending_ids':[c['id'] for c in cases if c['id'] not in translations],'editorial_ids':editorial,'missing_field_counts':{k:len(v) for k,v in missing.items()},'missing_field_ids':{k:v for k,v in missing.items() if k in ('introduction','method','outcome','notes')},'history':[{'stage':'initial source-case context fix','registered_cases':1348,'local_body_observations':1289,'short_bilingual_summaries':22,'actual_agent_not_observed':59},{'stage':'detailed archive baseline at c7fef31','registered_cases':1359,'detailed_bilingual_editorials':23,'source_texts_in_git':0,'local_body_snapshots_audited':1359}], 'storage':{'git':'registry/archives/*.json stores captured source text, metadata, original links, and separately versioned translations/editorials.','local_only':'HTML and working SQLite caches are not committed; local survival depends on this environment. The prior 1359-file local snapshot audit was historical, not a durable backup guarantee.','scope':'Source case pages only; linked external article text is not imported.'}}
    Path('registry/source-case').mkdir(parents=True,exist_ok=True)
    Path('registry/source-case/coverage.json').write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
    return value
if __name__=='__main__':print(json.dumps(update()['current'],ensure_ascii=False,indent=2))
