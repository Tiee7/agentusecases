import {test,expect} from '@playwright/test';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {spawnSync,spawn} from 'node:child_process';
import {get} from 'node:http';
import {loadContent,repoRoot} from '../src/lib/content.mjs';

const {reports}=loadContent();
const weights={demand:20,outcome:20,economics:20,distribution:15,moat:10,execution:10,feedback:5};
test('every report badge uses its actual research score and agrees with the breakdown',async({page})=>{
 for(const report of reports){
  const raw=JSON.parse(fs.readFileSync(path.join(repoRoot,'research',`${report.id}.json`)));
  const available=Object.keys(weights).every(key=>typeof raw.scores?.[key]?.score==='number' && Number.isFinite(raw.scores[key].score) && raw.scores[key].score>=0 && raw.scores[key].score<=5);
  await page.goto(`/reports/${report.id}/`);
  if(!available){
   await expect(page.locator('.report-score-value')).toHaveText('待评分');
   await expect(page.locator('#score')).toContainText('评分资料不完整');
   await expect(page.locator('#score h2 .red')).toHaveCount(0);
   await expect(page.locator('.report-score')).toHaveAccessibleName('商业评分待补充；查看评分依据');
   continue;
  }
  const expected=Math.round(Object.entries(weights).reduce((sum,[key,weight])=>sum+raw.scores[key].score*weight/5,0)*10)/10;
  await expect(page.locator('.report-score-value')).toHaveText(`${expected}/100`);
  await expect(page.locator('#score h2 .red')).toHaveText(String(expected));
  await expect(page.locator('.report-score')).toHaveAccessibleName(`商业评分 ${expected} 分，满分 100；查看评分依据`);
 }
});

test('right-hand badge remains separate from long titles and links to the score by keyboard',async({page},testInfo)=>{
 const longest=[...reports].sort((a,b)=>b.title.length-a.title.length)[0];
 const widths=[testInfo.project.use.viewport.width,390,320];
 for(const width of new Set(widths)){
  await page.setViewportSize({width,height:1000});
  await page.goto(`/reports/${longest.id}/`);
  const heading=await page.locator('h1').boundingBox(),badge=await page.locator('.report-score').boundingBox();
  expect(badge.x).toBeGreaterThanOrEqual(heading.x+heading.width+8);
  expect(badge.x+badge.width).toBeLessThanOrEqual(width);
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);
  await page.locator('.report-score').focus();await page.keyboard.press('Enter');
  await expect(page).toHaveURL(/#score$/);await expect(page.locator('#score')).toBeInViewport();
 }
});

test.describe('missing scores and boundary values in isolated static pages',()=>{
 let temporary,server;
 const fixtures=[['zero',0],['fraction',22],['maximum',100],['missing',null],['partial',null],['null',null],['text',null],['range',null]];
 test.beforeAll(async()=>{
  temporary=fs.mkdtempSync(path.join(os.tmpdir(),'commercial-score-'));
  for(const dir of ['registry','research','reports','site'])fs.mkdirSync(path.join(temporary,dir));
  const original=JSON.parse(fs.readFileSync(path.join(repoRoot,'research',`${reports[0].id}.json`))),entries=[];
  for(const [name] of fixtures){
   const record=structuredClone(original),id=`score-${name}`;record.id=id;record.url=`https://example.test/${id}`;
   for(const key of Object.keys(weights))record.scores[key].score=name==='maximum'?5:name==='fraction'?1.1:0;
   if(name==='missing')delete record.scores;
   if(name==='partial')delete record.scores.feedback;
   if(name==='null')record.scores.demand.score=null;
   if(name==='text')record.scores.demand.score='2';
   if(name==='range')record.scores.demand.score=6;
   entries.push({id,url:record.url,title:record.title});
   fs.writeFileSync(path.join(temporary,'research',`${id}.json`),JSON.stringify(record));
   fs.writeFileSync(path.join(temporary,'reports',`${id}.md`),'Local synthetic score fixture');
  }
  fs.writeFileSync(path.join(temporary,'registry/cases.json'),JSON.stringify({cases:entries}));
  for(const file of ['src','public','package.json','astro.config.mjs'])fs.cpSync(path.join(repoRoot,'site',file),path.join(temporary,'site',file),{recursive:true});
  fs.symlinkSync(path.join(repoRoot,'site/node_modules'),path.join(temporary,'site/node_modules'),'dir');
  const built=spawnSync(process.execPath,[path.join(repoRoot,'site/node_modules/astro/bin/astro.mjs'),'build'],{cwd:path.join(temporary,'site'),env:{...process.env,ASTRO_TELEMETRY_DISABLED:'1'},encoding:'utf8'});
  expect(built.status,built.stderr).toBe(0);
  server=spawn('python3',['-m','http.server','4324','--bind','127.0.0.1','--directory',path.join(temporary,'site/dist')],{stdio:'ignore'});
  await expect.poll(()=>new Promise(resolve=>{
   const request=get('http://127.0.0.1:4324/',response=>{
    const status=response.statusCode??0;response.resume();
    response.once('end',()=>resolve(status));response.once('error',()=>resolve(0));
   });
   request.once('error',()=>resolve(0));request.setTimeout(1000,()=>request.destroy());
  })).toBe(200);
 });
 test.afterAll(()=>{server?.kill();if(temporary)fs.rmSync(temporary,{recursive:true,force:true})});
 test('missing or malformed ratings are not presented as zero or a partial total',async({page})=>{
  for(const [name,score] of fixtures){
   await page.goto(`http://127.0.0.1:4324/reports/score-${name}/`);
   if(score===null){
    await expect(page.locator('.report-score-value')).toHaveText('待评分');
    await expect(page.locator('#score')).toContainText('评分资料不完整');
    await expect(page.locator('#score .score-breakdown')).toHaveCount(0);
   }else{
    await expect(page.locator('.report-score-value')).toHaveText(`${score}/100`);
    await expect(page.locator('#score h2 .red')).toHaveText(String(score));
   }
   await page.locator('.report-score').click();await expect(page).toHaveURL(/#score$/);
  }
 });
});
