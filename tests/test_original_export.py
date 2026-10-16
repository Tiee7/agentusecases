import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch
from agentwatch.export_originals import export,digest
class OriginalExportTests(unittest.TestCase):
    def test_export_only_original_fields_and_deterministic_manifest(self):
        body='Original case\nWhat they did\nPublic method';url='https://agentusecases.ai/use-case/fixture'
        case={'id':'fixture','source_trial':{'text':'Public prompt','internal_note':'EXCLUDED'}}
        archive={'url':url,'observed_at':'2026-10-16T00:00:00Z','body_sha256':digest(body.encode()),'source_text':{'body':body},'fields':{'method':{'status':'observed','value':'Public method','internal_note':'EXCLUDED'},'internal_note':'EXCLUDED'},'editorial':'EXCLUDED','translation':'EXCLUDED'}
        def read(cmd,**kwargs):
            if cmd[1]=='rev-parse':return 'a'*40+'\n'
            return json.dumps({'cases':[case]} if cmd[-1].endswith('registry/cases.json') else archive).encode()
        with tempfile.TemporaryDirectory() as tmp,patch('agentwatch.export_originals.subprocess.check_output',read):
            first=export(Path(tmp)/'one.zip');second=export(Path(tmp)/'two.zip')
            self.assertEqual(first['sha256'],second['sha256']);self.assertEqual(first['cases'],1)
            with zipfile.ZipFile(first['file']) as z:
                data=z.read('cases/fixture.json');manifest=json.loads(z.read('manifest.json'))
                self.assertNotIn(b'EXCLUDED',data);self.assertEqual(manifest['files']['cases/fixture.json']['sha256'],digest(data))
                self.assertEqual(json.loads(data)['source_text'],body)
