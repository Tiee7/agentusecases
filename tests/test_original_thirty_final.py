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

 def test_only_capture_receipt_metadata_can_advance(self):
  original={'status':'available','agent':'Claude','text':'Exact prompt','url':'https://example.test/case','method':'dom','observed_at':None,'html_sha256':'old'}
  latest=dict(original,method='ssr',observed_at='2026-10-21T06:00:00Z',html_sha256='new',observation_window=None)
  self.assertEqual(module.trial_content(original),module.trial_content(latest))
  for key,value in [('status','missing'),('agent','Other'),('text','Changed prompt'),('url','https://other.test')]:
   changed=dict(latest,**{key:value})
   self.assertNotEqual(module.trial_content(original),module.trial_content(changed),key)
  self.assertNotEqual(module.trial_content(original),module.trial_content(dict(latest,new_semantic_field=True)))
