"""Regression coverage for source fidelity and the archive HTML boundary."""
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location('archive_output', Path(__file__).resolve().parents[1] / 'site/scripts/check-archive-output.py')
archive_output = importlib.util.module_from_spec(spec)
spec.loader.exec_module(archive_output)


class ArchiveOutputTests(unittest.TestCase):
    def test_legacy_and_structured_text_preserve_whitespace_and_entities(self):
        expected = '\n  标题 & <img>  \r\n\r\n正文  \n'
        html = '<div id="source-translation"><p class="archive-blank-line"></p>\n<h3 class="archive-title">  标题 &amp; &lt;img&gt;  </h3>&#13;\n<p class="archive-blank-line"></p>&#13;\n<p>正文  </p>\n</div>'
        archive_output.check_text_block(html, 'source-translation', expected)
        archive_output.check_text_block('<pre id="source-translation">原文 &lt;script&gt;\n</pre>', 'source-translation', '原文 <script>\n')

    def test_rejects_trimmed_text_missing_blank_lines_and_added_spaces(self):
        expected = '  标题  \n\n正文\n'
        for html in [
            '<div id="source-translation"><h3 class="archive-title">标题</h3>\n<p class="archive-blank-line"></p>\n<p>正文</p>\n</div>',
            '<div id="source-translation"><h3 class="archive-title">  标题  </h3>\n<p>正文</p>\n</div>',
            '<div id="source-translation"><h3 class="archive-title">  标题  </h3> <p class="archive-blank-line"></p>\n<p>正文</p>\n</div>',
        ]:
            with self.subTest(html=html), self.assertRaises(AssertionError):
                archive_output.check_text_block(html, 'source-translation', expected)

    def test_rejects_executable_markup_and_attributes_even_with_matching_text(self):
        for child in ['<script>标题</script>', '<h3 class="archive-title" onclick="alert(1)">标题</h3>', '<h3 class="archive-title"><img src="x" onerror="alert(1)">标题</h3>', '<!--标题-->', '<h3 class="archive-title"><b>标题</b></h3>']:
            with self.subTest(child=child), self.assertRaises(AssertionError):
                archive_output.check_text_block(f'<div id="source-translation">{child}</div>', 'source-translation', '标题')
        with self.assertRaises(AssertionError):
            archive_output.check_text_block('<pre id="source-original"><p>正文</p></pre>', 'source-original', '正文')

    def test_rejects_duplicates_missing_blocks_and_unbalanced_markup(self):
        for html in ['', '<pre id="source-original">正文</pre>' * 2, '<pre id="source-original">正文']:
            with self.subTest(html=html), self.assertRaises(AssertionError):
                archive_output.check_text_block(html, 'source-original', '正文')
