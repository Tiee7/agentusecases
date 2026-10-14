"""Adapter for public server-rendered pages; never calls disallowed /api/."""
import json
import re
import xml.etree.ElementTree as ET
from urllib.parse import urlsplit
from .crawler import Page

def extract_seed(html):
    def find(value):
        if isinstance(value, dict):
            if isinstance(value.get('seed'), dict) and 'firstPage' in value['seed']:
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
    for match in re.finditer(r'self\.__next_f\.push\(\[1,("(?:[^"\\]|\\.)*")\]\)', html):
        for line in json.loads(match[1]).splitlines():
            if ':' not in line:
                continue
            try:
                value = json.loads(line.split(':', 1)[1])
            except (ValueError, TypeError):
                continue
            result = find(value)
            if result is not None:
                return result
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
