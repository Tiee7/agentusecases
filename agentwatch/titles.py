"""Validate site-edited usage titles; source titles and analysis are untouched."""
import json
from pathlib import Path

POLICY = json.loads((Path(__file__).resolve().parent.parent / 'schemas/editorial-title-policy.json').read_text())

def validate_editorial_title(title):
    if not isinstance(title, str) or not title.strip():
        raise ValueError('Editorial title must describe agent usage')
    if title != title.strip() or '\n' in title or len(title) > POLICY['max_length']:
        raise ValueError('Editorial title must be one concise line')
    if not title.startswith(tuple(POLICY['usage_prefixes'])):
        raise ValueError('Editorial title must start with an objective usage action')
    if any(word in title for word in POLICY['judgment_phrases']):
        raise ValueError('Editorial title must not contain a judgment; keep evaluations in the body')
    return title
