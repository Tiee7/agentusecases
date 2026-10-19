"""Regression guard for the imported Spark batch, separate from deep research rules."""
import copy
import importlib.util
from pathlib import Path
import unittest

RUN = Path(__file__).resolve().parents[1] / 'research/runs/spark-ten-case-repair-20261019'
spec = importlib.util.spec_from_file_location('spark_import_verify', RUN / 'verify.py')
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)

class SparkImportTests(unittest.TestCase):
    def test_current_batch_integrity_scope_and_arithmetic(self):
        self.assertEqual(len(verify.verify()['case_checks']), 10)

    def test_null_cost_does_not_become_confirmed_full_cost(self):
        model = verify.read(verify.ROOT / 'research/brief/automate-customer-onboarding-with-a-make-scenario.json')['unit_economics'][0]
        self.assertIsNone(model['other_variable_cost'])
        self.assertEqual(model['budget_status'], 'conditional_on_unlisted_costs')
        broken = copy.deepcopy(model)
        broken['budget_status'] = 'confirmed_within_budget'
        with self.assertRaises(AssertionError):
            verify.validate_model(broken)

    def test_annual_prepayment_is_not_monthly_amortization(self):
        model = verify.read(verify.ROOT / 'research/brief/automate-customer-onboarding-with-a-make-scenario.json')['unit_economics'][1]
        self.assertEqual(model['cash_fixed_upfront'], 144)
        broken = copy.deepcopy(model)
        broken['cash_fixed_upfront'] = 12
        with self.assertRaises(AssertionError):
            verify.validate_model(broken)

    def test_unknown_source_is_rejected(self):
        with self.assertRaises(AssertionError):
            verify.references({'facts':[{'source_ids':['invented-source']}]}, {'archive'})

if __name__ == '__main__':
    unittest.main()
