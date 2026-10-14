import unittest
from agentwatch.digest import render

class DigestTests(unittest.TestCase):
    def test_partial_baseline_does_not_claim_no_changes_or_deletions(self):
        result={'run_id':1,'catalog':{'count':1289,'baseline':True},'details_complete':False,'cases':[{'change':'baseline','title':'A','url':'https://example.test/a'}]}
        text=render(result)
        self.assertIn('不将现有案例计为新增',text)
        self.assertIn('全量详情完成：否',text)
        self.assertIn('未采集的正文不能声称没有变化',text)
    def test_changed_content_and_sitemap_delta_both_reported(self):
        result={'run_id':2,'catalog':{'count':2,'baseline':False,'newly_listed':['https://example.test/b'],'no_longer_listed':[],'lastmod_changed':[]},'details_complete':True,'cases':[{'change':'content_changed','title':'A','url':'https://example.test/a'}]}
        text=render(result)
        self.assertIn('目录新增 1',text)
        self.assertIn('[A](https://example.test/a)',text)
