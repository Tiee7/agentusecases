"""Publish source facts and reviewed summaries, never unlicensed cached prose."""
import hashlib
import re

SECTIONS = ('What they did', 'How it went', 'Worth knowing')

def observe(body, url, observed_at):
    lines = [line.strip() for line in body.splitlines() if line.strip()]
    agents = []
    status = 'not_observed'
    start = next((i for i, line in enumerate(lines) if line in ('Done with', 'Done with a')), None)
    if start is not None:
        end = next((i for i in range(start + 1, len(lines)) if lines[i] in (*SECTIONS, 'Try it yourself')), None)
        if end is not None:
            candidates = [s for s in lines[start+1:end] if not re.fullmatch(r'[A-Z0-9+]{1,3}', s)]
            if candidates == ['custom-built or unnamed agent']:
                status = 'custom_or_unnamed'
            elif candidates:
                agents, status = candidates, 'observed'
    sections = {}
    for label in SECTIONS:
        if label in lines:
            start = lines.index(label) + 1
            end = next((i for i in range(start, len(lines)) if lines[i] in (*SECTIONS, 'Try it yourself') or lines[i].startswith('Original source:')), len(lines))
            sections[label] = hashlib.sha256('\n'.join(lines[start:end]).encode()).hexdigest()
    return {'version': 1, 'status': 'observed', 'source_url': url, 'observed_at': observed_at,
            'body_sha256': hashlib.sha256(body.encode()).hexdigest(), 'hash_scope': 'observations.body UTF-8',
            'section_sha256': sections, 'actual_agents': agents, 'agent_status': status,
            'agent_basis': 'source Done with; source attribution, not independent verification',
            'publication': 'source_case_metadata'}

def merge(previous, observation):
    if previous and previous.get('observed_at', '') > observation['observed_at']:
        return previous
    if previous and previous.get('body_sha256') == observation['body_sha256'] and previous.get('summary'):
        observation['summary'] = previous['summary']
    return observation

def latest(db):
    result = {}
    if db.execute("SELECT 1 FROM sqlite_master WHERE name='public_source_cases'").fetchone():
        import json
        result={url:json.loads(payload) for url,payload in db.execute('SELECT url,payload FROM public_source_cases')}
    for url, body, observed_at in db.execute('SELECT o.url,o.body,r.fetched_at FROM observations o JOIN runs r ON r.id=o.run_id ORDER BY r.id'):
        if body:
            result[url] = observe(body, url, observed_at)
    return result

def render(value):
    """Render captured original and matching full translation, never summary substitutes."""
    import json
    from pathlib import Path
    from urllib.parse import urlsplit
    if not value:return []
    key=urlsplit(value.get('source_url','')).path.rstrip('/').rsplit('/',1)[-1]
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,199}',key):return []
    path=Path('registry/archives')/(key+'.json')
    if not path.exists():return []
    archive=json.loads(path.read_text());source=archive.get('source_text',{})
    if archive.get('url')!=value.get('source_url') or not source.get('body'):return []
    if hashlib.sha256(source['body'].encode()).hexdigest()!=archive.get('body_sha256'):return []
    lines=['','## English','','\n'.join('    '+line if line else '' for line in source['body'].splitlines())]
    translation=archive.get('translation',{})
    if translation.get('based_on_body_sha256')==archive.get('body_sha256') and translation.get('body') and hashlib.sha256(translation['body'].encode()).hexdigest()==translation.get('body_sha256'):
        lines+=['','## 中文','','\n'.join('    '+line if line else '' for line in translation['body'].splitlines())]
    return lines
