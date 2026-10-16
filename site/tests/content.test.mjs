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
test('personal use is independent and old records have honest fallbacks',()=>{
 const {reports}=loadContent();const r=reports[0];const raw=JSON.parse(fs.readFileSync(path.join(repoRoot,'research',r.id+'.json')));const entry={id:raw.id,url:raw.url};
 const score=r.score;delete raw.personal_value;delete raw.try_it;delete raw.source_trial;
 const old=projectReport(raw,entry);assert.equal(old.personal.level,'待核实');assert.equal(old.trial.status,'missing');assert.equal(old.trial.prompts.length,0);assert.equal(old.score,score);
 for(const report of reports){assert(['高','中','低','待核实'].includes(report.personal.level));assert.equal(report.personal.details.length,8);assert(report.personal.refs.length);assert(['missing','collected'].includes(report.trial.status));}
});
test('prompt projection preserves literal bilingual text and rejects unsafe source URLs',()=>{
 const {reports}=loadContent();const raw=JSON.parse(fs.readFileSync(path.join(repoRoot,'research',reports[0].id+'.json')));const text='中文 </pre><script>globalThis.injected=true</script> & "quote"\nEnglish `code` ${x}';delete raw.source_trial;raw.try_it.prompts[0].text=text;raw.try_it.prompts[0].source_url='javascript:alert(1)';
 const r=projectReport(raw,{id:raw.id,url:raw.url});assert.equal(r.trial.prompts[0].text,text);assert.equal(r.trial.prompts[0].url,'');
});
test('source-site templates lead, with separate agent and provenance, without replacing authored supplements',()=>{
 const {reports}=loadContent();const raw=JSON.parse(fs.readFileSync(path.join(repoRoot,'research',reports[0].id+'.json')));const entry={id:raw.id,url:raw.url,source_trial:{status:'available',text:'原文 & <tag>\nEnglish',agent:'Manus',source_url:raw.url,observed_at:'2026-10-15T17:00:00Z',method:'dom'}};
 const r=projectReport(raw,entry);assert.equal(r.trial.prompts[0].kind,'site_template');assert.equal(r.trial.prompts[0].agent,'Manus');assert.equal(r.trial.prompts[0].text,entry.source_trial.text);assert.equal(r.trial.prompts.length,raw.try_it.prompts.length+1);assert(r.trial.prompts[0].attribution.includes('不代表'));
 entry.source_trial.source_url='https://wrong.test/case';const invalid=projectReport(raw,entry);assert.equal(invalid.sourceTrial.status,'unparseable');assert(!invalid.trial.prompts.some(p=>p.kind==='site_template'));
});
test('browser observation intervals render without pretending an exact second',()=>{
 const {reports}=loadContent();const raw=JSON.parse(fs.readFileSync(path.join(repoRoot,'research',reports[0].id+'.json')));const entry={id:raw.id,url:raw.url,source_trial:{status:'available',text:'Literal',agent:'Manus',source_url:raw.url,observed_at:null,method:'dom',observation_window:{start:'2026-10-15T17:50:39Z',end:'2026-10-15T17:50:47Z',basis:'system_time_bracketing_tool_call'}}};
 const r=projectReport(raw,entry);assert(r.sourceTrial.observedAt.includes('17:50:39Z 至 2026-10-15T17:50:47Z'));assert.equal(r.trial.prompts[0].text,'Literal');entry.source_trial.observation_window.end='2026-10-15T17:00:00Z';assert.equal(projectReport(raw,entry).sourceTrial.status,'unparseable');
});
