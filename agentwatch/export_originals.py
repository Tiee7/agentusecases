"""Deterministic original-case-only backup from committed Git data."""
import argparse
import hashlib
import json
import subprocess
import zipfile
from pathlib import Path
from .business import safe_id
from .archive import FIELDS

def encode(value):return (json.dumps(value,ensure_ascii=False,sort_keys=True,indent=2)+'\n').encode()
def digest(data):return hashlib.sha256(data).hexdigest()
def export(output,revision='HEAD'):
    sha=subprocess.check_output(['git','rev-parse',revision],text=True).strip()
    def read(path):return json.loads(subprocess.check_output(['git','show',f'{sha}:{path}']))
    cases=read('registry/cases.json')['cases'];files={}
    for case in cases:
        key=safe_id(case['id']);a=read(f'registry/archives/{key}.json');body=a.get('source_text',{}).get('body')
        if not body:continue
        if digest(body.encode())!=a['body_sha256']:raise ValueError('Original hash mismatch: '+key)
        value={'id':key,'source_url':a['url'],'observed_at':a['observed_at'],'body_sha256':a['body_sha256'],'html_sha256':a.get('html_sha256'),'source_text':body,'fields':{k:{name:a['fields'][k][name] for name in ('status','value','sha256') if name in a['fields'][k]} for k in FIELDS if k in a['fields']},'source_trial':{k:case.get('source_trial',{}).get(k) for k in ('status','agent','text','source_url','observed_at')}}
        files[f'cases/{key}.json']=encode(value)
    manifest={'format_version':1,'source_revision':sha,'case_count':len(files),'registered_cases':len(cases),'missing_original_ids':[c['id'] for c in cases if f"cases/{c['id']}.json" not in files],'scope':'Source case text, original public fields and templates only. No editorial, translation, research, HTML or workspace files.','files':{name:{'bytes':len(data),'sha256':digest(data)} for name,data in sorted(files.items())}}
    payload=encode(manifest);files['manifest.json']=payload
    output=Path(output);output.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for name,data in sorted(files.items()):
            info=zipfile.ZipInfo(name,(1980,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16;z.writestr(info,data)
    manifest_path=output.with_suffix('.manifest.json');manifest_path.write_bytes(payload)
    result={'file':str(output.resolve()),'source_revision':sha,'cases':len(files)-1,'sha256':digest(output.read_bytes()),'bytes':output.stat().st_size,'manifest':str(manifest_path.resolve()),'manifest_sha256':digest(payload)}
    output.with_suffix('.sha256').write_text(result['sha256']+'  '+output.name+'\n')
    return result
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',default='data/exports/source-originals.zip');p.add_argument('--revision',default='HEAD');a=p.parse_args();print(json.dumps(export(a.output,a.revision),indent=2))
