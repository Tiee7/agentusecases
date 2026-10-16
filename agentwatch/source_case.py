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
            'publication': 'facts_and_original_summary_only', 'license_status': 'no_republication_license_found'}

def merge(previous, observation):
    if previous and previous.get('observed_at', '') > observation['observed_at']:
        return previous
    if previous and previous.get('body_sha256') == observation['body_sha256'] and previous.get('summary'):
        observation['summary'] = previous['summary']
    return observation

def latest(db):
    result = {}
    for url, body, observed_at in db.execute('SELECT o.url,o.body,r.fetched_at FROM observations o JOIN runs r ON r.id=o.run_id ORDER BY r.id'):
        if body:
            result[url] = observe(body, url, observed_at)
    return result

def render(value):
    if not value:
        return []
    lines = ['', '## 源站案例介绍、方法与结果', '', 'agentusecases.ai 的原创双语摘要 · 非全文 · 非独立结果核验', '',
             f"来源：{value['source_url']}", f"观测时间：{value.get('observed_at', '未观测')}",
             '实际 agent（源站标注）：' + ('、'.join(value.get('actual_agents', [])) or ('自建或未命名 agent' if value.get('agent_status') == 'custom_or_unnamed' else '尚未观测'))]
    summary = value.get('summary', {})
    if summary.get('based_on_sha256') == value.get('body_sha256'):
        for key, label in [('introduction','介绍'),('method','方法'),('outcome','结果与限制')]:
            section = summary.get('sections', {}).get(key)
            if section:
                lines += ['', '### '+label, '', section['en'], '', section['zh']]
    else:
        lines += ['', '摘要尚未复核。']
    return lines
