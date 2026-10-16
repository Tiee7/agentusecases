"""Concise display copy; preserve detailed research observations in source records."""
import json
from pathlib import Path

def project(record):
    result=dict(record)
    path=Path('registry/reading-notes.json')
    if path.exists():result['limitations']=json.loads(path.read_text()).get('limitations',{}).get(record['id'],record.get('limitations',''))
    findings=record.get('feedback',{}).get('observations',[])
    feedback='\n\n'.join(('相关体验：' if x.get('directness')=='adjacent_workflow' else '')+x['finding'] for x in findings) or '暂无直接用户反馈。'
    result['sections']=[dict(s,body=feedback) if s['id']=='feedback' else s for s in record.get('sections',[])]
    return result
