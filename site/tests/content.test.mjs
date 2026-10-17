import test from 'node:test';import assert from 'node:assert/strict';import fs from 'node:fs';import os from 'node:os';import path from 'node:path';
import {loadContent,projectReport,projectAuthorMethod,projectArchive,safeId,safeUrl,repoRoot} from '../src/lib/content.mjs';
import {archiveLines,archiveEndings} from '../src/lib/archive-text.mjs';
test('archive presentation preserves blank lines, indentation and every newline without interpreting markup',()=>{
 const body='\n  中文标题  \r\n\r\n  具体做法  \r\n正文 <script>alert(1)</script> & literal\n \t\n结果如何\r保留尾空格  \n';
 const lines=archiveLines(body);
 assert.equal(lines.map(line=>line.text+line.ending).join(''),body);
 assert.equal(lines[0].kind,'blank');assert.equal(lines[1].kind,'title');
 assert.equal(lines.find(line=>line.text==='  具体做法  ').kind,'heading');
 assert.equal(lines.find(line=>line.text.includes('<script>')).kind,'paragraph');
 assert.equal(lines.at(-1).text,'保留尾空格  ');
 assert(lines.every(line=>Object.hasOwn(archiveEndings,line.ending)));
 assert.equal(archiveEndings['\r\n'],'&#13;\n');
 assert.deepEqual(archiveLines(''),[]);
});
test('only completed v2 records with existing reports and matching identity become pages',()=>{
 const root=fs.mkdtempSync(path.join(os.tmpdir(),'reader-fixture-'));try{
  for(const dir of ['registry','research','reports'])fs.mkdirSync(path.join(root,dir));
  const cases=['good','draft','old','missing','mismatch'].map(id=>({id,title:id,url:'https://example.org/'+id,report:'../../secret.md'}));
  fs.writeFileSync(path.join(root,'registry/cases.json'),JSON.stringify({cases}));
  for(const e of cases){const d={schema_version:2,status:'completed',id:e.id,url:e.url,verdict:{decision:'仅建议受控试点'},internal_secret:'never-publish',sources:[{id:'Ssafe',url:'https://example.org/source',title:'source',token:'private'}],scores:{}};if(e.id==='draft')d.status='draft';if(e.id==='old')d.schema_version=1;if(e.id==='mismatch')d.id='other';fs.writeFileSync(path.join(root,'research',e.id+'.json'),JSON.stringify(d));if(e.id!=='missing')fs.writeFileSync(path.join(root,'reports',e.id+'.md'),'report');}
  const result=loadContent(root);assert.deepEqual(result.reports.map(r=>r.id),['good']);assert.equal(result.reports[0].verdict.decision,'建议先小规模试用');assert.equal(result.catalog.filter(c=>c.complete).length,1);assert(!JSON.stringify(result).includes('never-publish'));assert(!JSON.stringify(result).includes('private'));assert(!JSON.stringify(result).includes('../../'));
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
test('catalog uses first collection time, keeps unknown dates last, and never promotes drafts',()=>{
 const root=fs.mkdtempSync(path.join(os.tmpdir(),'discovery-fixture-'));
 try{for(const dir of ['registry','research','reports'])fs.mkdirSync(path.join(root,dir));
 const cases=[{id:'old',first_seen_at:'2026-01-01T00:00:00Z'},{id:'unknown'},{id:'new',first_seen_at:'2026-10-16T00:00:00Z'}].map(c=>({...c,title:c.id,url:`https://example.org/${c.id}`}));
 fs.writeFileSync(path.join(root,'registry/cases.json'),JSON.stringify({cases}));
 let result=loadContent(root);assert.deepEqual(result.catalog.map(c=>c.id),['new','old','unknown']);assert.equal(result.reports.length,0);assert(result.catalog.every(c=>!c.complete));
 cases.push({id:'newest',title:'newest',url:'https://example.org/newest',first_seen_at:'2026-10-17T00:00:00Z'});fs.writeFileSync(path.join(root,'registry/cases.json'),JSON.stringify({cases}));
 assert.equal(loadContent(root).catalog[0].id,'newest');
 }finally{fs.rmSync(root,{recursive:true,force:true})}
});

test('author methods reject unregistered sources and incomplete translations; never substitute prompts',()=>{
 const {reports}=loadContent();assert(reports.some(r=>r.authorMethod.status==='author_summary'));assert(reports.some(r=>r.authorMethod.status==='reported_summary'));
 const entry={original_sources:['https://author.test/post']};
 const valid={version:1,presentation:'bilingual_summary',status:'author_summary',source_url:entry.original_sources[0],source_title:'Author',accessed_at:'2026-10-16T00:00:00Z',source_sha256:'a'.repeat(64),steps:[{en:'Read inputs.',zh:'读取输入。'}]};
 assert.equal(projectAuthorMethod(valid,entry).status,'author_summary');
 for(const invalid of [undefined,{...valid,source_url:'https://agentusecases.ai/use-case/a'},{...valid,steps:[{en:'No translation'}]},{...valid,source_sha256:''},{...valid,presentation:'full_text'}])assert.equal(projectAuthorMethod(invalid,entry).status,'unavailable');
 const unavailable=projectAuthorMethod({...valid,status:'unavailable',steps:valid.steps},entry);assert.deepEqual(unavailable.steps,[]);
});

test('source case summaries have bilingual provenance and actual agents never use recommendations',()=>{
 const {reports,catalog}=loadContent();
 for(const r of reports.filter(r=>r.sourceCase.sections.length)){assert.equal(r.sourceCase.sections.length,3);assert(r.sourceCase.sections.every(s=>s.en && s.zh));}
 const eu=reports.find(r=>r.id==='dispute-an-airline-s-eu261-delay-compensation-rejection');assert.deepEqual(eu.sourceCase.agents,['Grok Bot']);
 const phone=catalog.find(c=>c.id==='negotiate-retention-discounts-on-bills-by-phone');assert.deepEqual(phone.sourceCase.agents,[]);assert.equal(phone.sourceCase.agentLabel,'自建或未命名 agent');
 assert(catalog.filter(c=>c.sourceCase.status==='not_observed').every(c=>c.sourceCase.agents.length===0));
});
test('detailed archives keep reviewed provenance, unknown counts, and original failure reason',()=>{
 const {reports,catalog}=loadContent();assert(catalog.length>=1359);assert(reports.filter(r=>r.archive.sections.length===4).length>=23);
 for(const c of catalog){assert.equal(c.archive.status,'observed');assert.equal(c.archive.bodyHash.length,64);assert(c.archive.wanted===null || (Number.isSafeInteger(c.archive.wanted) && c.archive.wanted>=0))}
 const r=reports.find(r=>r.id==='produce-investment-memos-with-claude-cowork');assert.match(r.authorMethod.reason,/403/);assert.equal(r.archive.status,'observed');const prose=JSON.stringify(r.archive.sections);for(const word of ['Adyen','IREN','yfinance','DCF'])assert(prose.includes(word));
 const entry={original_sources:['https://example.com/source']};assert.equal(projectAuthorMethod({version:1,presentation:'bilingual_summary',status:'unavailable',source_url:entry.original_sources[0],unavailable_reason:'HTTP 403; external page not read'},entry).reason,'HTTP 403; external page not read');
});

test('originals and full translations are distinct from editorial summaries and version checked',()=>{
 const {catalog}=loadContent();assert.equal(catalog.filter(c=>c.archive.sourceText).length,catalog.length);
 const translated=catalog.filter(c=>c.archive.translationText);assert(translated.length>=7);
 for(const c of translated){assert(c.archive.translationText.length>0);}
 const c=catalog.find(c=>c.archive.translationText);const raw=JSON.parse(fs.readFileSync(path.join(repoRoot,'registry/archives',c.id+'.json')));
 assert.equal(projectArchive(raw,{id:c.id,url:raw.url}).sourceText,raw.source_text.body);
 raw.translation.based_on_body_sha256='0'.repeat(64);const stale=projectArchive(raw,{id:c.id,url:raw.url});assert.equal(stale.translationText,'');assert(stale.translationStale);
 raw.source_text.body+='tampered';assert.equal(projectArchive(raw,{id:c.id,url:raw.url}).sourceText,'');
});

test('public report prose uses plain verdict wording without changing stored research',()=>{
 for(const r of loadContent().reports){assert(!JSON.stringify([r.verdict,r.sections,r.counter,r.limitations]).includes('仅建议受控试点'));}
});

test('editorial usage titles are shared by report and catalog while source titles stay separate',()=>{
 const policy=JSON.parse(fs.readFileSync(path.join(repoRoot,'schemas/editorial-title-policy.json')));
 const {reports,catalog}=loadContent();
 for(const r of reports){
  assert(policy.usage_prefixes.some(prefix=>r.title.startsWith(prefix)));
  assert(!policy.judgment_phrases.some(word=>r.title.includes(word)),r.title);
  assert.equal(catalog.find(c=>c.id===r.id).title,r.title);
  const raw=JSON.parse(fs.readFileSync(path.join(repoRoot,'research',r.id+'.json')));
  assert.equal(raw.title,r.title);assert.equal(fs.readFileSync(path.join(repoRoot,'reports',r.id+'.md'),'utf8').split('\n')[0],`# ${r.title}`);
 }
});
