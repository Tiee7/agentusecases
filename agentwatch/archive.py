"""Source observations: local raw snapshots, public field receipts and reviewed facts."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import urlsplit
from .crawler import Page
from .site import detail

FIELDS = ('title','introduction','method','outcome','notes','actual_agents','original_sources','author','category','tags','wanted','source_date','added_at','try_it')
NARRATIVES = {'introduction','method','outcome','notes'}

def sha(value):
    return hashlib.sha256(value.encode()).hexdigest()

def objects(html):
    def walk(v):
        if isinstance(v,dict):
            yield v
            for x in v.values(): yield from walk(x)
        elif isinstance(v,list):
            for x in v: yield from walk(x)
    for m in re.finditer(r'self\.__next_f\.push\(\[1,("(?:[^"\\]|\\.)*")\]\)',html):
        for line in json.loads(m[1]).splitlines():
            try: yield from walk(json.loads(line.split(':',1)[1]))
            except (ValueError,IndexError): continue

def split_body(body):
    lines=body.splitlines(); result={}
    labels={'What they did':'method','How it went':'outcome','Worth knowing':'notes'}
    stops=set(labels)|{'Try it yourself'}
    for label,key in labels.items():
        if label in lines:
            start=lines.index(label)+1
            end=next((i for i in range(start,len(lines)) if lines[i] in stops or lines[i].startswith('Original source:')),len(lines))
            result[key]='\n'.join(lines[start:end]).strip()
    done=next((i for i,x in enumerate(lines) if x in ('Done with','Done with a')),None)
    if done is not None:
        result['title']=lines[0];result['introduction']='\n'.join(lines[1:done]).strip()
    return result

def extract(html,url,at):
    from .source_case import observe
    from .source_trial import extract_source_trial
    body=detail(html); fields=split_body(body); page=Page();page.feed(html)
    fields['title']=' '.join(page.h1)
    parsed=observe(body,url,at)
    fields['actual_agents']=parsed['actual_agents'] if parsed['agent_status']=='observed' else (['custom-built or unnamed agent'] if parsed['agent_status']=='custom_or_unnamed' else None)
    fields['original_sources']=[u for u,t in page.links if t=='Read the original ↗'] or None
    scope=Page();scope.feed(html.split('Related use cases')[0])
    cats=[{'id':u.split('/')[-1],'label':t} for u,t in scope.links if u.startswith('/category/')]
    fields['category']=cats[0] if cats else None
    fields['tags']=[{'id':u.split('/')[-1],'label':t} for u,t in scope.links if u.startswith('/topics/') or u.startswith('/topic/') ] or None
    fields['author']=next((line.split(':',1)[1].strip() for line in scope.text if line.startswith('Author:') and line.split(':',1)[1].strip()),None)
    # Never infer an author from a publisher, domain or related article.
    fields['wanted']=None
    # A number must be visibly attached to the voting button; no API fallback.
    for button in re.findall(r'<button\b[^>]*>(.*?)</button>',html,re.S):
        p=Page();p.feed(button);text=' '.join(p.text)
        if 'I want this' in text:
            m=re.fullmatch(r'I want this\s*(?:\(?([0-9][0-9,]*)\)?)?',text)
            if m and m[1] is not None: fields['wanted']=int(m[1].replace(',',''))
    fields['source_date']=None;fields['added_at']=None
    source_line=next((line for line in scope.text if line.startswith('Source:')),None)
    if source_line:
        date_match=re.search(r'\b(20\d{2}-\d{2}-\d{2})\b',source_line)
        if date_match:fields['source_date']=date_match[1]
    for obj in objects(html):
        if fields['added_at'] is None and isinstance(obj.get('addedAt'),str):fields['added_at']=obj['addedAt']
    trial=extract_source_trial(html,url,at)
    fields['try_it']={'agent':trial['agent'],'text':trial['text']} if trial['status']=='available' else None
    return {'version':1,'url':url,'observed_at':at,'html_sha256':sha(html),'body_sha256':sha(body),'body':body,'fields':fields,'trial':trial,'source_date_label':'undated' if 'Undated' in scope.text else None}

def public_observation(raw):
    fields={}
    for name in FIELDS:
        value=raw['fields'].get(name)
        status='observed' if value is not None and value!='' and value!=[] else 'not_observed'
        field={'status':status,'value':None,'sha256':sha(json.dumps(value,ensure_ascii=False,sort_keys=True)) if status=='observed' else None}
        if status=='observed':
            if name in NARRATIVES:field['publication']='reviewed_restatement_required'
            elif name=='try_it':field['publication']='existing_source_trial_field'
            else:field['value']=value
        else:field['reason']='Not present in the captured public page; not a zero or proof of absence.'
        fields[name]=field
    if raw.get('source_date_label')=='undated':fields['source_date']['reason']='Source explicitly labels the external publication date Undated.'
    return {'version':1,'url':raw['url'],'observed_at':raw['observed_at'],'html_sha256':raw['html_sha256'],'body_sha256':raw['body_sha256'],'status':'observed','fields':fields,'publication':'original_structured_restatement_not_full_text','license_status':'no_republication_license_found'}

def store_local(db,html,url,at,root=Path('data/source-archive')):
    raw=extract(html,url,at);root.mkdir(parents=True,exist_ok=True)
    (root/(raw['html_sha256']+'.html')).write_text(html)
    (root/(raw['html_sha256']+'.json')).write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
    db.execute('CREATE TABLE IF NOT EXISTS archive_observations(url TEXT, observed_at TEXT, html_sha256 TEXT, payload TEXT, PRIMARY KEY(url,observed_at))')
    db.execute('INSERT OR REPLACE INTO archive_observations VALUES(?,?,?,?)',(url,at,raw['html_sha256'],json.dumps(public_observation(raw),ensure_ascii=False)))
    db.commit();return raw

def apply(db,root=Path('registry/archives')):
    if not db.execute("SELECT 1 FROM sqlite_master WHERE name='archive_observations'").fetchone():return
    root.mkdir(parents=True,exist_ok=True)
    for url,at,payload in db.execute('SELECT url,observed_at,payload FROM archive_observations ORDER BY observed_at'):
        key=urlsplit(url).path.rstrip('/').rsplit('/',1)[-1]
        if not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,199}',key):raise ValueError('Invalid archive ID')
        path=root/(key+'.json');value=json.loads(payload)
        old=json.loads(path.read_text()) if path.exists() else {}
        if (old.get('observed_at') or '')>at:continue
        if old.get('editorial'):value['editorial']=old['editorial']
        path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
    if db.execute("SELECT 1 FROM sqlite_master WHERE name='fetch_attempts'").fetchone():
        for url,at,status,error in db.execute('SELECT url,attempted_at,status,error FROM fetch_attempts ORDER BY attempted_at'):
            path=root/(urlsplit(url).path.rstrip('/').rsplit('/',1)[-1]+'.json')
            key=urlsplit(url).path.rstrip('/').rsplit('/',1)[-1]
            if not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,199}',key):raise ValueError('Invalid attempt ID')
            value=json.loads(path.read_text()) if path.exists() else {'version':1,'url':url,'status':'not_observed','fields':{}}
            if (value.get('last_attempt',{}).get('at') or '') > at:continue
            value['last_attempt']={'at':at,'status':status,'error':error};path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def cached(body,url,at,entry):
    fields=split_body(body)
    from .source_case import observe
    observed=observe(body,url,at)
    original=re.findall(r'^Original source: (https://\S+)$',body,re.M)
    fields.update(actual_agents=observed['actual_agents'] or (['custom-built or unnamed agent'] if observed['agent_status']=='custom_or_unnamed' else None),original_sources=original or None)
    lines=body.splitlines()
    if 'Copy prompt' in lines:
        start=lines.index('Copy prompt')+1
        stop=next((i for i in range(start,len(lines)) if lines[i].startswith('Original source:')),len(lines))
        agent=lines[start-2] if start>=2 else None
        fields['try_it']={'agent':agent,'text':'\n'.join(lines[start:stop]).strip()}
    raw={'url':url,'observed_at':at,'html_sha256':None,'body_sha256':sha(body),'fields':fields}
    rawroot=Path('data/source-archive');rawroot.mkdir(parents=True,exist_ok=True)
    (rawroot/('body-'+raw['body_sha256']+'.json')).write_text(json.dumps(dict(raw,body=body),ensure_ascii=False,indent=2)+'\n')
    out=public_observation(raw);out['capture_basis']='historical extracted body; HTML and omitted fields unavailable'
    return out
