// Build a disposable synthetic repository and inspect it in a local-only browser.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {spawnSync,spawn} from 'node:child_process';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
import {chromium} from '@playwright/test';
import {repoRoot,loadContent} from '../src/lib/content.mjs';
const tmp=fs.mkdtempSync(path.join(os.tmpdir(),'prompt-security-'));
const id=loadContent().reports[0].id;
const record=JSON.parse(fs.readFileSync(path.join(repoRoot,'research',`${id}.json`)));
const prompt='中文 & "双引号" \'单引号\' </pre><script>globalThis.promptInjected=true</script>\nEnglish `backticks` ${template} \\ slash\n```\n<img src=x onerror="globalThis.promptInjected=true">';
const archiveText='\n  中文标题 & <img src=x onerror="globalThis.promptInjected=true">  \r\n\r\n  具体做法  \r\n'+prompt+'\n</div><script>globalThis.promptInjected=true</script>\r\n \t\r\n结果如何\n保留尾空格  \n';
const originalText='Original title\n'+prompt;
const sha=body=>createHash('sha256').update(body).digest('hex');
let server,browser;
try {
 for(const dir of ['research','reports','registry','site'])fs.mkdirSync(path.join(tmp,dir));
 fs.mkdirSync(path.join(tmp,'registry/archives'));
 fs.writeFileSync(path.join(tmp,'registry/cases.json'),JSON.stringify({cases:[{id,url:record.url,title:record.title,original_sources:['https://author.test/story']}]}));
 fs.writeFileSync(path.join(tmp,'registry/archives',`${id}.json`),JSON.stringify({version:1,url:record.url,body_sha256:sha(originalText),source_text:{format:'extracted_page_text',body:originalText,body_sha256:sha(originalText)},translation:{status:'available',format:'full_extracted_text_translation',body:archiveText,body_sha256:sha(archiveText),based_on_body_sha256:sha(originalText)}}));
 record.author_method={version:1,status:'author_summary',presentation:'bilingual_summary',source_url:'https://author.test/story',source_title:'Synthetic author',accessed_at:'2026-10-16T00:00:00Z',source_sha256:'a'.repeat(64),steps:[{en:prompt,zh:prompt}]};
 record.source_trial={status:'available',text:prompt,agent:'Synthetic tool',source_url:record.url,observed_at:'2026-10-15T17:00:00Z',method:'dom'};
 record.try_it.prompts[0].text=prompt;record.try_it.prompts[0].source_url='javascript:globalThis.promptInjected=true';
 fs.writeFileSync(path.join(tmp,'research',`${id}.json`),JSON.stringify(record));
 fs.writeFileSync(path.join(tmp,'reports',`${id}.md`),'Synthetic security fixture');
 for(const name of ['src','public','package.json','astro.config.mjs'])fs.cpSync(path.join(repoRoot,'site',name),path.join(tmp,'site',name),{recursive:true});
 fs.symlinkSync(path.join(repoRoot,'site/node_modules'),path.join(tmp,'site/node_modules'),'dir');
 const built=spawnSync(process.execPath,[path.join(repoRoot,'site/node_modules/astro/bin/astro.mjs'),'build'],{cwd:path.join(tmp,'site'),env:{...process.env,ASTRO_TELEMETRY_DISABLED:'1'},encoding:'utf8'});
 assert.equal(built.status,0,built.stderr);
 server=spawn('python3',['-m','http.server','4323','--bind','127.0.0.1','--directory',path.join(tmp,'site/dist')],{stdio:'ignore'});
 browser=await chromium.launch();const page=await browser.newPage();
 await page.addInitScript(()=>Object.defineProperty(navigator,'clipboard',{value:{writeText:async text=>{window.copied=text}}}));
 for(let i=0;i<30;i++){try{await page.goto(`http://127.0.0.1:4323/reports/${id}/`);break}catch(e){if(i===29)throw e;await new Promise(r=>setTimeout(r,100));}}
 for(const width of [1440,390])for(const route of ['reports','cases']){
  await page.setViewportSize({width,height:1000});
  await page.goto(`http://127.0.0.1:4323/${route}/${id}/`);
  assert.equal(await page.locator('#source-translation').textContent(),archiveText);
  assert.equal(await page.locator('#source-original').textContent(),originalText);
  assert.deepEqual(await page.locator('#source-translation .archive-heading').allTextContents(),['  具体做法  ','结果如何']);
  assert.equal(await page.locator('#source-translation script,#source-translation img,#source-original script,#source-original img').count(),0);
  assert.equal(await page.locator('.archive-heading').first().evaluate(el=>getComputedStyle(el).borderLeftWidth),'3px');
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  await page.locator('.source-original summary').click();
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  assert.equal(await page.evaluate(()=>window.promptInjected),undefined);
 }
 await page.goto(`http://127.0.0.1:4323/reports/${id}/`);
 assert.equal(await page.locator('#author-method [lang="zh-CN"] li').textContent(),prompt);
 assert.equal(await page.locator('#author-method script,#author-method img').count(),0);
 assert.equal(await page.locator('#prompt-0').textContent(),prompt);
 assert.equal(await page.locator('#prompt-0 script,#prompt-0 img').count(),0);
 assert.equal(await page.locator('#try-it a[href^="javascript:"]').count(),0);
 await page.locator('[data-copy="prompt-0"]').click();
 assert.equal(await page.evaluate(()=>window.copied),prompt);
 assert.equal(await page.evaluate(()=>window.promptInjected),undefined);
 await page.goto(`http://127.0.0.1:4323/trials/${id}/`);
 assert.equal(await page.locator('#source-prompt').textContent(),prompt);
 await page.locator('#copy-source').click();assert.equal(await page.evaluate(()=>window.copied),prompt);
 assert.equal(await page.evaluate(()=>window.promptInjected),undefined);
 console.log('PASS: isolated Astro build + desktop/mobile Chromium preserve exact bilingual archive whitespace, headings, hostile text and clipboard content without execution on reports/cases/trials.');
} finally {
 await browser?.close();server?.kill();fs.rmSync(tmp,{recursive:true,force:true});
}
