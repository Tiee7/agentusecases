// Build a disposable synthetic repository and inspect it in a local-only browser.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {spawnSync,spawn} from 'node:child_process';
import assert from 'node:assert/strict';
import {chromium} from '@playwright/test';
import {repoRoot,loadContent} from '../src/lib/content.mjs';
const tmp=fs.mkdtempSync(path.join(os.tmpdir(),'prompt-security-'));
const id=loadContent().reports[0].id;
const record=JSON.parse(fs.readFileSync(path.join(repoRoot,'research',`${id}.json`)));
const prompt='中文 & "双引号" \'单引号\' </pre><script>globalThis.promptInjected=true</script>\nEnglish `backticks` ${template} \\ slash\n```\n<img src=x onerror="globalThis.promptInjected=true">';
let server,browser;
try {
 for(const dir of ['research','reports','registry','site'])fs.mkdirSync(path.join(tmp,dir));
 fs.writeFileSync(path.join(tmp,'registry/cases.json'),JSON.stringify({cases:[{id,url:record.url,title:record.title}]}));
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
 assert.equal(await page.locator('#prompt-0').textContent(),prompt);
 assert.equal(await page.locator('#prompt-0 script,#prompt-0 img').count(),0);
 assert.equal(await page.locator('#try-it a[href^="javascript:"]').count(),0);
 await page.locator('[data-copy="prompt-0"]').click();
 assert.equal(await page.evaluate(()=>window.copied),prompt);
 assert.equal(await page.evaluate(()=>window.promptInjected),undefined);
 console.log('PASS: isolated Astro build + local Chromium preserve bilingual hostile text and exact clipboard content without execution.');
} finally {
 await browser?.close();server?.kill();fs.rmSync(tmp,{recursive:true,force:true});
}
