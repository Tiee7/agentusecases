"""Exact original/translation text checks for every independent archive and report."""
import hashlib
import json
from pathlib import Path
from html.parser import HTMLParser
class TextBlock(HTMLParser):
    def __init__(self, identifier):
        super().__init__(convert_charrefs=True);self.identifier=identifier;self.inside=False;self.count=0;self.children=0;self.parts=[]
    def handle_starttag(self,tag,attrs):
        if self.inside:self.children+=1
        if tag=='pre' and dict(attrs).get('id')==self.identifier:self.count+=1;self.inside=True
    def handle_endtag(self,tag):
        if tag=='pre':self.inside=False
    def handle_data(self,data):
        if self.inside:self.parts.append(data)
root=Path(__file__).resolve().parents[2]
cases=json.loads((root/'registry/cases.json').read_text())['cases'];originals=translations=0
for c in cases:
    a=json.loads((root/'registry/archives'/f"{c['id']}.json").read_text());raw=a.get('source_text',{}).get('body');t=a.get('translation',{})
    if raw:assert hashlib.sha256(raw.encode()).hexdigest()==a['body_sha256'];originals+=1
    translated=t.get('body') if t.get('based_on_body_sha256')==a['body_sha256'] else None
    if translated:assert hashlib.sha256(translated.encode()).hexdigest()==t['body_sha256'];translations+=1
    paths=[root/'site/dist/cases'/c['id']/'index.html'];report=root/'site/dist/reports'/c['id']/'index.html'
    if report.exists():paths.append(report)
    for path in paths:
        html=path.read_text()
        for name,expected in [('source-original',raw),('source-translation',translated)]:
            p=TextBlock(name);p.feed(html)
            assert p.count==int(bool(expected)),(c['id'],name,p.count)
            if expected:assert p.children==0 and ''.join(p.parts)==expected,(c['id'],name)
print(f'Archive exact-text and inert-markup checks passed: {originals} originals, {translations} complete translations; all report copies checked.')
