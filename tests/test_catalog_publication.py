"""Exercise the retry shell with real local Git repos and a competing main push.
Node validation is stubbed here; the real site suite is run separately in CI.
"""
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from agentwatch.crawler import database, save

class CatalogPublicationTests(unittest.TestCase):
    def test_competing_push_regenerates_without_overwriting_new_research(self):
        root=Path(__file__).resolve().parents[1]
        real_git=shutil.which('git')
        with tempfile.TemporaryDirectory() as tmp:
            tmp=Path(tmp);remote=tmp/'remote.git';repo=tmp/'repo';rival=tmp/'rival';bin_dir=tmp/'bin';bin_dir.mkdir()
            def git(*args,cwd=None):
                return subprocess.run([real_git,*args],cwd=cwd,text=True,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout
            git('init','--bare',str(remote));git('init','-b','main',str(repo))
            git('config','user.name','Fixture',cwd=repo);git('config','user.email','fixture@example.test',cwd=repo)
            shutil.copytree(root/'agentwatch',repo/'agentwatch',ignore=shutil.ignore_patterns('__pycache__'))
            for name in ('registry','research','reports','tests','data'): (repo/name).mkdir()
            (repo/'tests/test_snapshot.py').write_text("import unittest,json\nfrom pathlib import Path\nclass SnapshotTest(unittest.TestCase):\n def test_snapshot(self):\n  self.assertEqual(json.loads(Path('registry/refresh.json').read_text())['catalog_observed'],1)\n")
            (repo/'.gitignore').write_text('data/\n__pycache__/\n')
            url='https://agentusecases.ai/use-case/existing'
            entry={'id':'existing','url':url,'title':'Case','record':'research/existing.json','report':'reports/existing.md','original_sources':[]}
            (repo/'registry/cases.json').write_text(json.dumps({'cases':[entry]}))
            (repo/'research/existing.json').write_text(json.dumps({'schema_version':1,'title':'Initial research'}))
            (repo/'reports/existing.md').write_text('Initial research')
            git('add','.',cwd=repo);git('commit','-m','Fixture',cwd=repo);git('remote','add','origin',str(remote),cwd=repo);git('push','origin','main',cwd=repo)
            git('clone','--branch','main',str(remote),str(rival));git('config','user.name','Fixture',cwd=rival);git('config','user.email','fixture@example.test',cwd=rival)
            db=database(repo/'data/history.sqlite3')
            save(db,'https://agentusecases.ai/','site_category_top',[{'url':url,'title':'Refreshed case','body':'Public observation'}],{url:'2026-10-16'});db.close()
            (bin_dir/'npm').write_text('#!/bin/sh\nexit 0\n');(bin_dir/'npm').chmod(0o755)
            wrapper=bin_dir/'git'
            wrapper.write_text('''#!/usr/bin/env python3
import os,sys,subprocess,json
from pathlib import Path
real=os.environ['TEST_REAL_GIT'];rival=Path(os.environ['TEST_RIVAL']);flag=Path(os.environ['TEST_PUSH_FLAG'])
if sys.argv[1:2]==['push'] and not flag.exists():
 flag.touch()
 (rival/'research/existing.json').write_text(json.dumps({'schema_version':1,'title':'Newer researcher result','author_method':{'marker':'retain latest research'}}))
 (rival/'reports/existing.md').write_text('Newer researcher result')
 for args in [('add','research','reports'),('commit','-m','Concurrent research'),('push','origin','main')]: subprocess.run([real,*args],cwd=rival,check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
raise SystemExit(subprocess.run([real,*sys.argv[1:]]).returncode)
''');wrapper.chmod(0o755)
            env=dict(os.environ,GITHUB_ACTIONS='true',PATH=str(bin_dir)+os.pathsep+os.environ['PATH'],TEST_REAL_GIT=real_git,TEST_RIVAL=str(rival),TEST_PUSH_FLAG=str(tmp/'pushed'))
            result=subprocess.run(['bash',str(root/'.github/scripts/publish-catalog.sh')],cwd=repo,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            self.assertEqual(result.returncode,0,result.stdout)
            self.assertIn('Main changed during publication',result.stdout)
            git('fetch','origin','main',cwd=repo)
            record=json.loads(git('show','origin/main:research/existing.json',cwd=repo))
            self.assertEqual(record['author_method']['marker'],'retain latest research')
            self.assertEqual(git('show','origin/main:reports/existing.md',cwd=repo),'Newer researcher result')
            catalog=json.loads(git('show','origin/main:registry/cases.json',cwd=repo));self.assertEqual(catalog['cases'][0]['title'],'Refreshed case')
            self.assertIn('legacy_draft',git('show','origin/main:registry/CATALOG.md',cwd=repo))
