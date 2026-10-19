import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {loadContent,projectBrief,repoRoot} from '../src/lib/content.mjs';
const data=loadContent();
const raw=id=>JSON.parse(fs.readFileSync(path.join(repoRoot,'research/brief',`${id}.json`),'utf8'));
const entry=b=>({id:b.id,url:b.url,title:b.title});
test('all completed briefs are projected separately with exhaustive three-state coverage',()=>{
 const expected=fs.readdirSync(path.join(repoRoot,'research/brief')).filter(n=>n.endsWith('.json')).map(n=>raw(n.slice(0,-5))).filter(b=>b.schema_version===1&&b.status==='completed'&&b.analysis_depth==='brief'&&!data.reports.some(r=>r.id===b.id)&&fs.existsSync(path.join(repoRoot,'reports/brief',`${b.id}.md`))).map(b=>b.id).sort();
 assert.deepEqual(data.briefs.map(b=>b.id).sort(),expected);
 assert.equal(new Set([...data.briefs,...data.reports].map(x=>x.id)).size,data.briefs.length+data.reports.length);
 assert.equal(data.catalog.filter(c=>c.status==='completed').length,data.reports.length);
 assert.equal(data.catalog.filter(c=>c.status==='brief').length,data.briefs.length);
 assert.equal(data.catalog.filter(c=>c.status==='pending').length+data.briefs.length+data.reports.length,data.catalog.length);
 for(const b of data.briefs){assert.equal(b.depth,'brief');assert.equal(b.score,null);assert.equal(b.scoreAvailable,false);assert.equal(b.path,`/briefs/${b.id}/`);const c=data.catalog.find(c=>c.id===b.id);assert.equal(c.complete,false);assert.equal(c.readingPath,b.path);assert.equal(c.title,b.title);assert.equal(b.sections.length,raw(b.id).analysis.filter(s=>s.body.trim()).length);}
});
test('brief projection rejects wrong identity, schema, drafts and unsafe source links without leaking private metadata',()=>{
 const b=raw(data.briefs[0].id);for(const patch of [{id:'wrong'},{url:'https://wrong.test/'},{schema_version:2},{status:'draft'},{analysis_depth:'deep'}])assert.equal(projectBrief({...b,...patch},entry(b)),null);
 const hostile='literal </pre><script>globalThis.injected=true</script> & "quote"';
 b.sources=[{id:'archive',url:'https://example.test/archive',summary:hostile,status:'fetched',archive_path:'/workspace/private',hash_scope:'SECRET'},{id:'unsafe',url:'javascript:alert(1)'},{id:'bad id',url:'https://example.test/'}];
 b.facts=[{statement:hostile,type:'author_claim',source_ids:['archive','unsafe','missing']}];b.analysis=[{id:'sources',title:hostile,body:hostile,source_ids:['archive']}];b.import_provenance={secret:'PRIVATE-METADATA'};
 const p=projectBrief(b,entry(b));assert.deepEqual(p.sources.map(s=>s.id),['archive']);assert.deepEqual(p.facts[0].refs,['archive']);assert.equal(p.facts[0].type,'作者自述');assert.equal(p.sections[0].id,'analysis-1');assert.equal(p.sections[0].body,hostile);assert.equal(p.sources[0].supports,hostile);assert(!JSON.stringify(p).includes('/workspace/private'));assert(!JSON.stringify(p).includes('PRIVATE-METADATA'));assert(!JSON.stringify(p).includes('SECRET'));
});
test('source restrictions and source-id references survive historical brief formats',()=>{
 const b=raw(data.briefs[0].id);b.sources=['failed','blocked_robots','skipped_previous_access_denial','skipped_previous_robots_restriction','skipped_previous_access_restriction','not_read'].map((status,i)=>({id:`archive-${i}`,url:`https://example.test/${i}`,status}));
 const p=projectBrief(b,entry(b));assert(p.sources.every(s=>s.status.includes('未读取')));
 for(const brief of data.briefs){const ids=new Set(brief.sources.map(s=>s.id));for(const item of [...brief.facts,...brief.sections,...brief.trial.prompts,...brief.models])assert(item.refs.every(id=>ids.has(id)));}
});
test('all three generations of cost fields retain unknowns, zero and annual cash prepayments',()=>{
 const b=raw(data.briefs[0].id);b.unit_economics=[{price:100,generation_cost:2,human_cost:10,other_variable_cost:null,acquisition_cost:0,monthly_volume:3,monthly_fixed_cost:4},{price:100,api_cost:null,generation_cost:99,other_variable_cost:0}];
 const p=projectBrief(b,entry(b));assert.deepEqual([p.models[0].api,p.models[0].other,p.models[0].acquisition,p.models[0].volume,p.models[0].fixed],[2,null,0,3,4]);assert.deepEqual([p.models[1].api,p.models[1].human,p.models[1].other,p.models[1].volume,p.models[1].fixed],[null,null,0,null,null]);
 const make=data.briefs.find(b=>b.id==='automate-customer-onboarding-with-a-make-scenario');assert.equal(make.models[1].cashUpfront,144);assert.equal(make.models[1].fixed,12);assert.equal(make.models[1].other,null);
});
test('entry source templates win, complete methods stay separate from archive-reported summaries',()=>{
 const b=raw('automate-customer-onboarding-with-a-make-scenario');const e={...entry(b),archive:{version:1,url:b.url,body_sha256:b.source_body_sha256},source_trial:{status:'available',source_url:b.url,text:'current literal <script>',agent:'Current tool',observed_at:'2026-10-19T00:00:00Z',method:'dom'}};
 const p=projectBrief(b,e);assert.equal(p.trial.prompts[0].text,e.source_trial.text);assert.equal(p.authorMethod.status,'unavailable');assert(p.reportedMethod.steps.length);assert(p.reportedMethod.title.includes('归档转述'));e.archive.body_sha256='wrong';assert.equal(projectBrief(b,e).reportedMethod,null);
});
test('discovery never promotes a draft, a missing Markdown pair or a stale brief over deep research',()=>{
 const root=fs.mkdtempSync(path.join(os.tmpdir(),'brief-projection-'));try{
 for(const dir of ['registry','research/brief','reports/brief'])fs.mkdirSync(path.join(root,dir),{recursive:true});
 const base=raw(data.briefs[0].id);const cases=['valid','draft','missing'].map(id=>({id,url:`https://example.test/${id}`,title:id}));fs.writeFileSync(path.join(root,'registry/cases.json'),JSON.stringify({cases}));
 for(const c of cases){fs.writeFileSync(path.join(root,'research/brief',`${c.id}.json`),JSON.stringify({...base,...c,status:c.id==='draft'?'draft':'completed'}));if(c.id!=='missing')fs.writeFileSync(path.join(root,'reports/brief',`${c.id}.md`),'fixture');}
 assert.deepEqual(loadContent(root).briefs.map(b=>b.id),['valid']);
 const deep=JSON.parse(fs.readFileSync(path.join(repoRoot,'research',`${data.reports[0].id}.json`)));fs.writeFileSync(path.join(root,'research/valid.json'),JSON.stringify({...deep,...cases[0]}));fs.writeFileSync(path.join(root,'reports/valid.md'),'fixture');const promoted=loadContent(root);assert.equal(promoted.reports.length,1);assert.equal(promoted.briefs.length,0);assert.equal(promoted.catalog.find(c=>c.id==='valid').status,'completed');
 }finally{fs.rmSync(root,{recursive:true,force:true});}
});
