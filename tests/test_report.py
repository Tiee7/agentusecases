import unittest
from agentwatch.report import render, WEIGHTS

class ReportTests(unittest.TestCase):
    def record(self):
        return {'title': '用测试 agent 整理资料', 'url': 'https://example.test/case', 'researched_at': '2026-10-14', 'summary': 'Synthetic fixture, not a real case.'}
    def test_missing_evidence_not_zero_or_total(self):
        self.assertIn('暂不计算', render(self.record()))
    def test_cited_weighted_score(self):
        r = self.record()
        r['dimensions'] = {k: {'score': 4, 'rationale': 'Fixture evidence', 'sources': ['https://example.test/docs']} for k in WEIGHTS}
        self.assertIn('80.0/100', render(r))
    def test_uncited_scores_are_rejected(self):
        r = self.record()
        r['dimensions'] = {'value': {'score': 5}}
        with self.assertRaises(ValueError):
            render(r)
