import test from 'node:test';import assert from 'node:assert/strict';import fs from 'node:fs';import os from 'node:os';import path from 'node:path';
import {loadContent,projectReport,safeId,safeUrl,repoRoot} from '../src/lib/content.mjs';
test('only completed v2 records with existing reports and matching identity become pages',()=>{
 const root=fs.mkdtempSync(path.join(os.tmpdir(),'reader-fixture-'));try{
  for(const dir of ['registry','research','reports'])fs.mkdirSync(path.join(root,dir));
  const cases=['good','draft','old','missing','mismatch'].map(id=>({id,title:id,url:'https://example.org/'+id,report:'../../secret.md'}));
  fs.writeFileSync(path.join(root,'registry/cases.json'),JSON.stringify({cases}));
  for(const e of cases){const d={schema_version:2,status:'completed',id:e.id,url:e.url,verdict:{decision:'仅建议受控试点'},internal_secret:'never-publish',sources:[{id:'Ssafe',url:'https://example.org/source',title:'source',token:'private'}],scores:{}};if(e.id==='draft')d.status='draft';if(e.id==='old')d.schema_version=1;if(e.id==='mismatch')d.id='other';fs.writeFileSync(path.join(root,'research',e.id+'.json'),JSON.stringify(d));if(e.id!=='missing')fs.writeFileSync(path.join(root,'reports',e.id+'.md'),'report');}
  const result=loadContent(root);assert.deepEqual(result.reports.map(r=>r.id),['good']);assert.equal(result.catalog.filter(c=>c.complete).length,1);assert(!JSON.stringify(result).includes('never-publish'));assert(!JSON.stringify(result).includes('private'));assert(!JSON.stringify(result).includes('../../'));
 }finally{fs.rmSync(root,{recursive:true,force:true})}
});
test('untrusted IDs and nonpublic schemes are rejected',()=>{assert(!safeId('../secret'));assert(!safeId('UpperCase'));assert.equal(safeUrl('javascript:alert(1)'),'');assert.equal(safeUrl('https://user:password@example.org'),'');assert.equal(safeUrl('file:///tmp/secret'),'')});
test('actual published reports match score, source references and repository eligibility',()=>{const {reports,catalog}=loadContent();assert(reports.length>0);assert(catalog.length>=reports.length);for(const r of reports){const raw=JSON.parse(fs.readFileSync(path.join(repoRoot,'research',r.id+'.json')));assert.equal(raw.schema_version,2);assert.equal(raw.status,'completed');assert(fs.existsSync(path.join(repoRoot,'reports',r.id+'.md')));assert.equal(r.sections.length,10);assert(r.sources.length>=6);assert(r.score>=0&&r.score<=100);assert(r.facts.every(f=>f.refs.length>0));assert(r.sections.every(s=>s.refs.length>0));assert(r.models.length>=2)}});
