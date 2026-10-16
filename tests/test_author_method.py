import copy
import json
import unittest
from pathlib import Path
from agentwatch.author_method import validate_author_method, render_author_method

class AuthorMethodTests(unittest.TestCase):
    def setUp(self):
        self.entry={'original_sources':['https://author.test/story']}
        self.method={'version':1,'status':'author_summary','presentation':'bilingual_summary','source_url':'https://author.test/story','source_title':'Author','source_language':'en','accessed_at':'2026-10-16T00:00:00Z','source_sha256':'a'*64,'steps':[{'en':'Read the input documents.','zh':'读取输入文件。'}]}
        self.receipts=[{'url':'https://author.test/story','status':'fetched','sha256':'a'*64}]
    def test_summary_needs_original_source_and_matching_read_receipt(self):
        validate_author_method({'author_method':self.method},self.entry,self.receipts,True)
        for field,value in [('source_url','https://aggregator.test/prompt'),('presentation','full_text'),('source_sha256','b'*64)]:
            method=dict(self.method,**{field:value})
            with self.assertRaises(ValueError):validate_author_method({'author_method':method},self.entry,self.receipts,True)
    def test_no_invented_steps_for_unavailable_source(self):
        m=dict(self.method,status='unavailable',unavailable_reason='Unavailable')
        with self.assertRaises(ValueError):validate_author_method({'author_method':m},self.entry,self.receipts,True)
        m['steps']=[];validate_author_method({'author_method':m},self.entry,[],True)
    def test_translation_required_and_new_publication_cannot_omit_method(self):
        m=copy.deepcopy(self.method);del m['steps'][0]['zh']
        with self.assertRaises(ValueError):validate_author_method({'author_method':m},self.entry,self.receipts,True)
        with self.assertRaises(ValueError):validate_author_method({},self.entry,[],True)
        validate_author_method({},self.entry)
    def test_all_backfilled_methods_have_receipts_and_markdown_order(self):
        root=Path(__file__).resolve().parents[1]
        entries=json.loads((root/'registry/cases.json').read_text())['cases'];count=0
        for entry in entries:
            path=root/'research'/f"{entry['id']}.json"
            if not path.exists():continue
            record=json.loads(path.read_text())
            if 'author_method' not in record:continue
            receipt_path=root/'research/author-method-evidence'/f"{entry['id']}.json"
            if not receipt_path.exists():receipt_path=root/'research/evidence'/f"{entry['id']}.json"
            receipts=json.loads(receipt_path.read_text())
            validate_author_method(record,entry,receipts,True);count+=1
            report=(root/'reports'/f"{entry['id']}.md").read_text()
            self.assertLess(report.index('## 原作者的方法与来源'),report.index('## 我们的分析'))
        self.assertGreater(count,0)
