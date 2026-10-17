"""Exact archive text and inert, explicitly allowed presentation markup checks."""
import hashlib
import json
import re
from pathlib import Path
from html.parser import HTMLParser


class TextBlock(HTMLParser):
    def __init__(self, identifier):
        super().__init__(convert_charrefs=True)
        self.identifier = identifier
        self.count = 0
        self.stack = []
        self.parts = []
        self.blocks = []
        self.root_tag = None

    @staticmethod
    def safe_attrs(attrs, allowed):
        names = [name for name, _ in attrs]
        assert len(set(names)) == len(names), 'Duplicate archive attribute'
        assert all(name in allowed or re.fullmatch(r'data-astro-cid-[a-z0-9]+', name) for name in names), 'Unexpected archive attribute'

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if attributes.get('id') == self.identifier:
            self.count += 1
            assert not self.stack, 'Nested archive root'
            assert tag == 'pre' or (self.identifier == 'source-translation' and tag == 'div'), 'Unexpected archive root'
            self.safe_attrs(attrs, {'id', 'class', 'lang'})
            self.root_tag = tag
            self.stack.append(tag)
        elif self.stack:
            assert self.root_tag == 'div' and len(self.stack) == 1 and tag in {'h3', 'p'}, 'Executable or unexpected archive child'
            self.safe_attrs(attrs, {'class'})
            classes = attributes.get('class', '').split()
            assert (tag == 'h3' and classes in [['archive-title'], ['archive-heading']]) or (tag == 'p' and classes in [[], ['archive-blank-line']]), 'Unexpected archive presentation'
            self.blocks.append({'tag': tag, 'classes': classes, 'text': ''})
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if self.stack:
            assert self.stack[-1] == tag, 'Unbalanced archive markup'
            self.stack.pop()

    def handle_data(self, data):
        if self.stack:
            self.parts.append(data)
            if len(self.stack) == 2:
                self.blocks[-1]['text'] += data
            elif self.root_tag == 'div':
                assert not data.strip('\r\n'), 'Extra text between archive lines'

    def handle_comment(self, data):
        assert not self.stack, 'Archive text parsed as an HTML comment'


def check_text_block(html, identifier, expected):
    parser = TextBlock(identifier)
    parser.feed(html)
    parser.close()
    assert not parser.stack, (identifier, 'Unclosed archive block')
    assert parser.count == int(bool(expected)), (identifier, 'Wrong archive count', parser.count)
    if not expected:
        return
    assert ''.join(parser.parts) == expected, (identifier, 'Archive text or whitespace changed')
    if parser.root_tag == 'div':
        lines = re.split(r'\r\n|\r|\n', expected)
        if not lines[-1]:
            lines.pop()
        assert [block['text'] for block in parser.blocks] == lines, (identifier, 'Archive line boundaries changed')
        nonempty = [block for block in parser.blocks if block['text'].strip()]
        assert not nonempty or nonempty[0]['classes'] == ['archive-title'], (identifier, 'Missing article title')


def main():
    root = Path(__file__).resolve().parents[2]
    cases = json.loads((root / 'registry/cases.json').read_text())['cases']
    originals = translations = 0
    for case in cases:
        archive = json.loads((root / 'registry/archives' / f"{case['id']}.json").read_text())
        raw = archive.get('source_text', {}).get('body')
        translation = archive.get('translation', {})
        if raw:
            assert hashlib.sha256(raw.encode()).hexdigest() == archive['body_sha256']
            originals += 1
        translated = translation.get('body') if translation.get('based_on_body_sha256') == archive['body_sha256'] else None
        if translated:
            assert hashlib.sha256(translated.encode()).hexdigest() == translation['body_sha256']
            translations += 1
        paths = [root / 'site/dist/cases' / case['id'] / 'index.html']
        report = root / 'site/dist/reports' / case['id'] / 'index.html'
        if report.exists():
            paths.append(report)
        for path in paths:
            html = path.read_text()
            for name, expected in [('source-original', raw), ('source-translation', translated)]:
                try:
                    check_text_block(html, name, expected)
                except AssertionError as error:
                    raise AssertionError((str(path.relative_to(root)), error.args)) from error
    print(f'Archive exact-text and inert-markup checks passed: {originals} originals, {translations} complete translations; all report copies checked.')


if __name__ == '__main__':
    main()
