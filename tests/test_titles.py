import json
import unittest
from pathlib import Path
from agentwatch.titles import validate_editorial_title

class EditorialTitleTests(unittest.TestCase):
    def test_usage_titles_allow_specific_tasks(self):
        for title in ['用 Claude Code 整理税务凭证', '将 OpenClaw 技能迁移到 Grok Bot', '用 AI agent 测算项目盈利']:
            self.assertEqual(validate_editorial_title(title), title)

    def test_verdicts_are_rejected_even_after_usage_prefix(self):
        for title in ['用 Claude 写报告：适合内部效率工具', '用 AI 做交易：不建议商业投入', '用 agent 整理资料，建议先小规模试用', '用 AI 生成文档：优缺点总结', '价值评级：高', '业务的商业研究标题']:
            with self.subTest(title=title), self.assertRaises(ValueError):
                validate_editorial_title(title)

    def test_all_editorial_titles_match_reports_and_indexes(self):
        root=Path(__file__).resolve().parents[1]
        index=(root/'INDEX.md').read_text()
        catalog=(root/'registry/CATALOG.md').read_text()
        for path in (root/'research').glob('*.json'):
            record=json.loads(path.read_text())
            if record.get('status')!='completed':continue
            title=validate_editorial_title(record['title'])
            self.assertEqual((root/'reports'/f'{record["id"]}.md').read_text().splitlines()[0], '# '+title)
            self.assertIn(title,index)
            self.assertIn(title,catalog)
