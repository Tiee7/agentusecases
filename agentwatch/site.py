"""Adapter for public server-rendered pages; never calls disallowed /api/."""
import json
import re
import xml.etree.ElementTree as ET
from urllib.parse import urlsplit
from .crawler import Page

class _FlightReferences:
    """Read JSON model references only; never evaluate Flight code or load modules."""
    def __init__(self, records):
        self.records = records
        self.lookups = 0

    def resolve(self, value, active=()):
        if not isinstance(value, str):
            return value
        if not re.fullmatch(r'\$[0-9a-f]+(?::[A-Za-z0-9_-]+)*', value):
            raise RuntimeError('Unsupported SSR catalog reference')
        self.lookups += 1
        if value in active:
            raise RuntimeError('Cyclic SSR catalog reference')
        if len(active) >= 64 or self.lookups > 10000:
            raise RuntimeError('SSR catalog reference limit exceeded')
        active = (*active, value)
        record, *path = value[1:].split(':')
        if record not in self.records:
            raise RuntimeError('Missing SSR catalog reference record')
        target = self.records[record]
        for key in path:
            target = self.resolve(target, active) if isinstance(target, str) else target
            if key in ('__proto__', 'prototype', 'constructor'):
                raise RuntimeError('Unsafe SSR catalog reference path')
            if isinstance(target, dict) and key in target:
                target = target[key]
            elif isinstance(target, list):
                # React model elements encode props at index 3, not as a key.
                if key == 'props' and len(target) == 4 and target[0] == '$':
                    target = target[3]
                elif re.fullmatch(r'0|[1-9][0-9]*', key) and len(key) <= 10 and int(key) < len(target):
                    target = target[int(key)]
                else:
                    raise RuntimeError('Invalid SSR catalog reference list path')
            else:
                raise RuntimeError('Missing SSR catalog reference path')
        return self.resolve(target, active) if isinstance(target, str) else target

    def container(self, value, expected, label):
        value = self.resolve(value) if isinstance(value, str) else value
        if not isinstance(value, expected):
            raise RuntimeError(f'Invalid SSR catalog {label} type')
        return value

    def seed(self, value):
        seed = dict(self.container(value, dict, 'seed'))
        sections = self.container(seed.get('firstPage'), list, 'firstPage')
        seed['firstPage'] = []
        for value in sections:
            section = dict(self.container(value, dict, 'section'))
            items = self.container(section.get('items'), list, 'items')
            # Resolve only structural positions. Titles, summaries and other
            # case fields may contain literal dollar strings or Flight tokens.
            section['items'] = [dict(self.container(item, dict, 'item')) for item in items]
            seed['firstPage'].append(section)
        return seed

def extract_seed(html):
    def find(value):
        if isinstance(value, dict):
            if 'seed' in value and (isinstance(value['seed'], str) or
                                     isinstance(value['seed'], dict) and 'firstPage' in value['seed']):
                return value['seed']
            children = value.values()
        elif isinstance(value, list):
            children = value
        else:
            return None
        for child in children:
            result = find(child)
            if result is not None:
                return result
    # A record may span push chunks, and references may point forward.
    stream = ''.join(json.loads(match[1]) for match in re.finditer(
        r'self\.__next_f\.push\(\[1,("(?:[^"\\]|\\.)*")\]\)', html))
    records = {}
    for line in stream.splitlines():
        record, separator, body = line.partition(':')
        if not separator or not re.fullmatch(r'[0-9a-f]+', record):
            continue
        try:
            value = json.loads(body)
        except (ValueError, TypeError):
            continue
        if record in records:
            raise RuntimeError('Duplicate SSR model record')
        records[record] = value
    resolver = _FlightReferences(records)
    for value in records.values():
        result = find(value)
        if result is not None:
            return resolver.seed(result)
    raise RuntimeError('Public SSR seed not found: adapter must be updated')

def catalog(xml, host):
    root = ET.fromstring(xml)
    if not root.tag.endswith('urlset'):
        raise RuntimeError('Sitemap index unsupported; completeness unknown')
    result = {}
    for entry in root:
        fields = {child.tag.rsplit('}', 1)[-1]: child.text for child in entry}
        url = fields.get('loc', '')
        parts = urlsplit(url)
        if parts.scheme == 'https' and parts.netloc == host and re.fullmatch(r'/use-case/[^/]+/?$', parts.path):
            result[url] = fields.get('lastmod')
    if not result:
        raise RuntimeError('Empty sitemap catalog')
    return result

def detail(html):
    page = Page()
    page.feed(html)
    if not page.h1:
        raise RuntimeError('Case title missing; no snapshot saved')
    try:
        start = page.text.index(page.h1[0])
        stops = [page.text.index(label, start) for label in ('Want help getting this working?', 'Related use cases', 'Keep browsing') if label in page.text[start:]]
        if not stops:
            raise ValueError('No stable case boundary')
        end = min(stops)
    except ValueError as error:
        raise RuntimeError('Case content boundaries changed; no snapshot saved') from error
    originals = [url for url,title in page.links if title == 'Read the original ↗']
    return '\n'.join(page.text[start:end] + ['Original source: '+u for u in originals])
