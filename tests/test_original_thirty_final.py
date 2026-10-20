"""Do not let brief records bypass the user-facing original-batch contract."""
import importlib.util
from pathlib import Path
import unittest
path=Path(__file__).resolve().parents[1]/'research/runs/2026-10-20-original-thirty-final/verify.py'
spec=importlib.util.spec_from_file_location('original_thirty_final',path)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
class OriginalThirtyFinalTests(unittest.TestCase):
 def test_fixed_batch_contract(self):
  result=module.verify()
  self.assertEqual(len(result['case_checks']),30)
  self.assertEqual((result['deep'],result['brief']),(11,19))
