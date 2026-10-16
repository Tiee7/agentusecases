"""Case-source method summaries, kept separate from analysis and trial prompts."""
from datetime import datetime
from urllib.parse import urlsplit

STATUSES = ('author_summary', 'reported_summary', 'unavailable')

def validate_author_method(record, entry, receipts=None, required=False):
    method = record.get('author_method')
    if method is None and not required:
        return
    if not isinstance(method, dict) or method.get('version') != 1 or method.get('status') not in STATUSES:
        raise ValueError('author_method requires a version and explicit source status')
    url = method.get('source_url', '')
    parsed = urlsplit(url)
    if parsed.scheme != 'https' or parsed.username or parsed.password or url not in entry.get('original_sources', []):
        raise ValueError('Author method must cite the registered original source, not a trial template')
    if method.get('presentation') != 'bilingual_summary':
        raise ValueError('Only attributed bilingual summaries are supported; no unlicensed full text')
    steps = method.get('steps', [])
    if method['status'] == 'unavailable':
        if steps or not method.get('unavailable_reason'):
            raise ValueError('Unavailable author sources require a reason and no invented steps')
        return
    if not steps or len(steps) > 6 or any(not isinstance(s, dict) or not all(isinstance(s.get(lang), str) and s[lang].strip() for lang in ('en', 'zh')) for s in steps):
        raise ValueError('Each method step requires English and Chinese summaries')
    if sum(len(s['en'].split()) for s in steps) > 180:
        raise ValueError('Keep author method summaries concise')
    if not method.get('source_title') or not method.get('source_language'):
        raise ValueError('Method source title and language are required')
    try:
        if datetime.fromisoformat(method['accessed_at']).tzinfo is None: raise ValueError()
    except (KeyError, TypeError, ValueError):
        raise ValueError('Method source access time must include a timezone')
    sha = method.get('source_sha256', '')
    if len(sha) != 64 or any(c not in '0123456789abcdef' for c in sha):
        raise ValueError('Method source requires a content receipt')
    if receipts is not None and not any(r.get('url') == url and r.get('status') == 'fetched' and r.get('sha256') == sha for r in receipts):
        raise ValueError('Method source must match a successfully read receipt')

def render_author_method(record):
    m = record.get('author_method')
    if not m: return []
    lines = ['','## 原作者的方法与来源','',f"来源：[{m['source_title']}]({m['source_url']})"]
    if m['status'] == 'unavailable': return lines + ['', '方法摘要未收录']
    label = '作者方法摘要' if m['status'] == 'author_summary' else '报道摘要'
    lines += ['', label]
    for i,s in enumerate(m['steps'],1): lines += ['',f"{i}. {s['zh']}",f"   English summary: {s['en']}"]
    return lines
