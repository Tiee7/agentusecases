"""Read public HTML only: source-site trial suggestions, never author execution logs."""
import argparse
import hashlib
import json
import re
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ATTRIBUTION = '源站提供的试用模板；不代表案例原作者实际使用的提示词。'
STATUSES = ('available', 'missing', 'unparseable', 'not_observed')


def observation_bounds(value):
    window = value.get('observation_window')
    if window is not None:
        if value.get('observed_at') is not None or not isinstance(window, dict) or window.get('basis') != 'system_time_bracketing_tool_call':
            raise ValueError('Bracketed observations must preserve their interval, not invent an exact time')
        start = datetime.fromisoformat(window.get('start', ''))
        end = datetime.fromisoformat(window.get('end', ''))
    else:
        start = end = datetime.fromisoformat(value.get('observed_at') or '')
    if start.tzinfo is None or end.tzinfo is None or start > end:
        raise ValueError('Source observation requires an ordered timezone-aware time or interval')
    return start, end


def observation_label(value):
    window = value.get('observation_window')
    return f"{window['start']} 至 {window['end']}（工具调用前后计时区间）" if window else value.get('observed_at') or '未观测'


def validate_observation(value, expected_url):
    if not isinstance(value, dict) or value.get('version') != 1 or value.get('status') not in STATUSES:
        raise ValueError('Invalid source trial observation')
    parts = urlsplit(value.get('source_url', ''))
    if value.get('source_url') != expected_url or parts.scheme != 'https' or not parts.netloc or parts.username or parts.password:
        raise ValueError('Source trial must belong to the case public HTTPS URL')
    if value['status'] != 'not_observed':
        observation_bounds(value)
    if value.get('method') not in ('ssr', 'dom', 'none'):
        raise ValueError('Invalid source trial extraction method')
    if value.get('attribution') != ATTRIBUTION:
        raise ValueError('Source suggestions must not be attributed to case authors')
    if value['status'] == 'available':
        if any(not isinstance(value.get(k), str) or not value[k].strip() for k in ('text', 'agent')):
            raise ValueError('Available source trial needs literal prompt and suggested agent')
        if value['method'] == 'none':
            raise ValueError('Available source trial needs an extraction method')
    elif value.get('text') is not None or value.get('agent') is not None:
        raise ValueError('Unavailable observation must not masquerade as a usable prompt')
    return value


class Document(HTMLParser):
    """Small tree preserving literal pre/textarea whitespace and decoded entities."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = {'tag': 'root', 'attrs': {}, 'children': []}
        self.stack = [self.root]
    def handle_starttag(self, tag, attrs):
        node = {'tag': tag, 'attrs': dict(attrs), 'children': []}
        self.stack[-1]['children'].append(node)
        if tag not in ('area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'):
            self.stack.append(node)
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if self.stack[-1]['tag'] == tag:
            self.stack.pop()
    def handle_endtag(self, tag):
        for i in range(len(self.stack)-1, 0, -1):
            if self.stack[i]['tag'] == tag:
                del self.stack[i:]
                break
    def handle_data(self, data):
        self.stack[-1]['children'].append(data)


def node_text(node):
    if isinstance(node, str):
        return node
    if node['tag'] == 'br':
        return '\n'
    return ''.join(node_text(c) for c in node['children'])


def nodes(node):
    if isinstance(node, dict):
        yield node
        for child in node['children']:
            yield from nodes(child)


def flight_values(document):
    """Decode JSON payloads, without evaluating scripts or making API calls."""
    for node in nodes(document.root):
        if node['tag'] != 'script':
            continue
        script = node_text(node)
        if node['attrs'].get('type') == 'application/json':
            try:
                yield json.loads(script)
            except ValueError:
                pass
        for match in re.finditer(r'self\.__next_f\.push\(\[1,("(?:[^"\\]|\\.)*")\]\)', script):
            payload = json.loads(match[1])
            for line in payload.split('\n'):
                if ':' not in line:
                    continue
                try:
                    yield json.loads(line.split(':', 1)[1])
                except ValueError:
                    continue


def find_trials(value, inherited_id=None):
    if isinstance(value, dict):
        identity = value.get('id', value.get('slug', inherited_id))
        if not isinstance(identity, str):
            identity = inherited_id
        if 'tryIt' in value:
            yield identity, value['tryIt']
        for child in value.values():
            yield from find_trials(child, identity)
    elif isinstance(value, list):
        for child in value:
            yield from find_trials(child, inherited_id)


def dom_trial(document):
    # The live card: header row (label + Copy prompt button), then prompt p,
    # then a separate sponsor p. Never use the whole card's innerText.
    cards = []
    for node in nodes(document.root):
        if node['tag'] in ('h1','h2','h3','h4') and node_text(node).strip() in ('Related use cases', 'Keep browsing'):
            break
        children = [c for c in node['children'] if isinstance(c, dict)]
        for i, header in enumerate(children[:-1]):
            header_children = [n for n in header['children'] if isinstance(n, dict)]
            buttons = [n for n in header_children if n['tag']=='button' and node_text(n).strip() in ('Copy prompt','Copied')]
            labels = [node_text(n).strip() for n in header_children if n['tag'] in ('p','h2','h3') and node_text(n).strip().startswith('Try it yourself')]
            prompt = children[i+1]
            if buttons and labels and prompt['tag'] in ('p','pre','textarea'):
                match = re.fullmatch(r'Try it yourself\s+with\s+(.+)', ' '.join(labels[0].split()))
                if match and node_text(prompt).strip() and not node_text(prompt).lstrip().startswith('Want help getting this working?'):
                    cards.append((match.group(1), node_text(prompt)))
    cards = list(dict.fromkeys(cards))
    if len(cards) == 1:
        return True, *cards[0]
    if cards:
        return True, None, None
    active = False
    labels, prompts = [], []
    for node in nodes(document.root):
        tag = node['tag']
        if tag in ('script','style'):
            continue
        text = node_text(node)
        if tag in ('h1','h2','h3','h4'):
            label = ' '.join(text.split())
            if label.startswith('Try it yourself'):
                active = True
                labels.append(label)
                continue
            if active:
                break
        if not active:
            continue
        if text.strip() in ('Want help getting this working?', 'Related use cases', 'Keep browsing'):
            break
        if tag in ('pre', 'textarea'):
            prompts.append(text)
        # Includes a separate with Manus badge, without confusing the header agent.
        if tag in ('span','p','a','div') and re.fullmatch(r'with\s+[^\n]{1,80}', text.strip()):
            labels.append(text.strip())
    agent = next((m.group(1).strip() for label in labels if (m := re.search(r'\bwith\s+(.+)$', label))), None)
    unique = list(dict.fromkeys(prompts))
    marker_present = any(n['tag'] in ('p','h2','h3','h4') and node_text(n).strip().startswith('Try it yourself') for n in nodes(document.root))
    return active or marker_present, agent, unique[0] if len(unique) == 1 else None


def extract_source_trial(html, source_url, observed_at=None, observation_window=None):
    case_id = urlsplit(source_url).path.rstrip('/').rsplit('/', 1)[-1]
    document = Document(); document.feed(html)
    candidates = [candidate for value in flight_values(document) for candidate in find_trials(value)]
    scoped = [v for identity, v in candidates if identity == case_id]
    if not scoped:
        scoped = [v for identity, v in candidates if identity is None] if not any(identity for identity, _ in candidates) else []
    unique = {json.dumps(v, sort_keys=True, ensure_ascii=False): v for v in scoped}
    base = {'version':1, 'status':'missing', 'text':None, 'agent':None, 'source_url':source_url,
            'observed_at':observed_at, 'method':'none', 'attribution':ATTRIBUTION,
            'html_sha256':hashlib.sha256(html.encode()).hexdigest()}
    if observation_window is not None:
        base['observation_window'] = observation_window
    if len(unique) == 1:
        trial = next(iter(unique.values()))
        if isinstance(trial, dict) and all(isinstance(trial.get(k), str) and trial[k].strip() and not re.fullmatch(r'\$[a-f0-9]+', trial[k]) for k in ('prompt','agent')):
            return validate_observation(dict(base, status='available', text=trial['prompt'], agent=trial['agent'], method='ssr'), source_url)
    present, agent, prompt = dom_trial(document)
    if agent and prompt and prompt.strip():
        return validate_observation(dict(base, status='available', text=prompt, agent=agent, method='dom'), source_url)
    if present or (unique and any(v is not None for v in unique.values())):
        base['status'] = 'unparseable'
    return validate_observation(base, source_url)


def sync_record(record, observation):
    validate_observation(observation, record['url'])
    record['source_trial'] = observation
    if isinstance(record.get('try_it'), dict):
        trial = record['try_it']
        trial['source_prompt_status'] = 'collected' if observation['status']=='available' or any(p.get('kind')=='original' for p in trial.get('prompts',[])) else 'missing'
        trial['source_prompt_note'] = '已收录源站提供的建议模板，不代表案例原作者实际提示词；自编模板作为补充，未做模型实测。' if observation['status']=='available' else '最新源站模板观测状态：'+observation['status']+'。不能据此推断原作者实际提示词；下方自编模板仅作补充。'
    return record


def newer_observation(previous, candidate):
    if not previous or previous.get('status') == 'not_observed':
        return candidate
    if candidate.get('status') == 'not_observed':
        return previous
    return candidate if observation_bounds(candidate)[0] >= observation_bounds(previous)[1] or observation_bounds(candidate) == observation_bounds(previous) else previous


def apply_observations(observations):
    """Update only registered cases; a browser snippet is not a fresh full catalog."""
    from .business import read_registry, REGISTRY, sync_source_trials, indexes
    registry = read_registry()
    known = {c['url']:c for c in registry['cases']}
    if set(observations) - set(known):
        raise ValueError('Cannot import a trial for an unregistered case')
    for url, value in observations.items():
        validate_observation(value, url)
        case = known[url]
        case['source_trial'] = newer_observation(case.get('source_trial'), value)
    REGISTRY.write_text(json.dumps(registry,ensure_ascii=False,indent=2)+'\n')
    sync_source_trials(registry['cases'])
    indexes()


def export_observations(db, run_id):
    return {url:json.loads(payload) for url,payload in db.execute('SELECT url,payload FROM source_trials WHERE run_id=?', (run_id,))}


def main():
    parser = argparse.ArgumentParser(description='Import an authorized saved public HTML fixture; no network requests')
    parser.add_argument('--html', required=True)
    parser.add_argument('--url', required=True)
    parser.add_argument('--observed-at')
    parser.add_argument('--observed-from')
    parser.add_argument('--observed-until')
    parser.add_argument('--output', required=True)
    parser.add_argument('--db', help='Optional SQLite observation history for this saved browser fixture')
    parser.add_argument('--apply', action='store_true', help='Update only the existing registered case and its completed report')
    args = parser.parse_args()
    window = None
    if args.observed_from or args.observed_until:
        if args.observed_at or not (args.observed_from and args.observed_until):
            parser.error('Provide an exact observed-at OR both interval bounds')
        window = dict(start=args.observed_from,end=args.observed_until,basis='system_time_bracketing_tool_call')
    elif not args.observed_at:
        parser.error('Observation time or interval is required')
    result = extract_source_trial(Path(args.html).read_text(), args.url, args.observed_at, window)
    Path(args.output).write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    if args.db:
        from .crawler import database, save
        db = database(args.db)
        saved = save(db, args.url, 'browser_fixture_import', [{'url':args.url,'title':args.url.rsplit('/',1)[-1],'body':'','source_trial':result}])
        exported = export_observations(db, saved['run_id'])
        db.close()
    else:
        exported = {args.url:result}
    if args.apply:
        apply_observations(exported)
    print(result['status'])

if __name__ == '__main__':
    main()
