"""Validate every published template's literal text; browser tests cover shared UI."""
import json
from html.parser import HTMLParser
from pathlib import Path

class Prompt(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_prompt = False
        self.parts = []
        self.count = 0
        self.elements_inside = 0
    def handle_starttag(self, tag, attrs):
        if self.in_prompt:
            self.elements_inside += 1
        if tag == 'pre' and dict(attrs).get('id') == 'source-prompt':
            self.in_prompt = True
            self.count += 1
    def handle_endtag(self, tag):
        if tag == 'pre':
            self.in_prompt = False
    def handle_data(self, data):
        if self.in_prompt:
            self.parts.append(data)

root = Path(__file__).resolve().parents[2]
cases = json.loads((root/'registry/cases.json').read_text())['cases']
count = 0
for case in cases:
    source = case.get('source_trial', {})
    if source.get('status') != 'available':
        continue
    parser = Prompt()
    parser.feed((root/'site/dist/trials'/case['id']/'index.html').read_text())
    assert parser.count == 1 and parser.elements_inside == 0, case['id']
    assert ''.join(parser.parts) == source['text'], case['id']
    count += 1
print(f'All {count} source-template pages preserve exact text as inert content.')
