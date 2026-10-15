import copy
import json
from pathlib import Path
import unittest
from agentwatch.personal import validate_personal, render_personal
from agentwatch.business import validate, weighted_score

class PersonalTests(unittest.TestCase):
    def setUp(self):
        self.record = json.loads(Path('research/build-a-spending-insights-app-from-bank-transactions.json').read_text())

    def test_all_existing_reports_validate_against_existing_receipts(self):
        records = [json.loads(p.read_text()) for p in Path('research').glob('*.json')]
        complete = [r for r in records if r.get('schema_version') == 2 and r.get('status') == 'completed']
        self.assertGreaterEqual(len(complete), 21)
        for record in complete:
            with self.subTest(id=record['id']):
                receipts = json.loads(Path('research/evidence', record['id'] + '.json').read_text())
                validate(record, receipts, record['id'])

    def test_legacy_and_score_independence(self):
        score = weighted_score(self.record)
        del self.record['personal_value']; del self.record['try_it']
        validate_personal(self.record)
        self.assertIn('待核实', '\n'.join(render_personal(self.record)))
        self.assertEqual(weighted_score(self.record), score)

    def test_invalid_levels_evidence_and_authorship(self):
        for change in [lambda r:r['personal_value'].update(level='5'), lambda r:r['personal_value'].update(source_ids=['unknown']), lambda r:r['try_it'].update(source_prompt_status='collected'), lambda r:r['try_it']['prompts'][0].update(kind='original', source_url='javascript:alert(1)'), lambda r:r['personal_value'].update(frequency='')]:
            r=copy.deepcopy(self.record); change(r)
            with self.assertRaises(ValueError): validate_personal(r)

    def test_bilingual_fences_are_literal_in_markdown(self):
        text='中文 <script>alert("x")</script> & `code`\n```\nEnglish ${value} \\ newline'
        self.record['try_it']['prompts'][0]['text']=text
        output='\n'.join(render_personal(self.record))
        self.assertIn('    ```',output)
        self.assertIn('    '+text.splitlines()[0],output)
