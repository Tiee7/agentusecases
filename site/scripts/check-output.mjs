import fs from 'node:fs';import path from 'node:path';import assert from 'node:assert/strict';import {loadContent} from '../src/lib/content.mjs';
const {reports,catalog}=loadContent();const allowed=new Set(['index.html','404.html','catalog/index.html','method/index.html','favicon.svg',...reports.map(r=>`reports/${r.id}/index.html`),...catalog.filter(c=>c.sourceTrial.status==='available').map(c=>`trials/${c.id}/index.html`)]);
const files=fs.readdirSync('dist',{recursive:true}).filter(f=>fs.statSync(path.join('dist',f)).isFile());
for(const file of files){assert(allowed.has(file)||/^_astro\/[\w.-]+\.(css|js)$/.test(file),`Unexpected public file: ${file}`);const body=fs.readFileSync(path.join('dist',file),'utf8');assert(!/GH_TOKEN|["\s]\/workspace\/|data\/source-cache|verify-sources|git push|hourly-business-research|remote-readback|BEGIN PRIVATE KEY/.test(body),`Internal data in ${file}`)}
for(const required of allowed)assert(files.includes(required),`Missing public file: ${required}`);
console.log(`Public output allowlist passed: ${files.length} files, ${reports.length} reports; no raw JSON, logs, task files, caches or source maps.`);

const home=fs.readFileSync('dist/index.html','utf8'), index=fs.readFileSync('dist/catalog/index.html','utf8');
assert.equal((home.match(/data-recent-id=/g)||[]).length,Math.min(6,catalog.filter(c=>c.firstSeen).length));
assert.equal((index.match(/data-item /g)||[]).length,catalog.length);
for(const c of catalog)assert(index.includes(`data-search="${c.title.replaceAll('&','&amp;').replaceAll('"','&quot;')}`),`Missing catalog case ${c.id}`);
for(const phrase of ['证据先于结论','没有验证的成功，不写成确定的收益','读结论，也读限制。','工具调用前后计时区间'])for(const file of files.filter(f=>f.endsWith('.html')))assert(!fs.readFileSync(path.join('dist',file),'utf8').includes(phrase),`Repeated disclaimer in ${file}`);
console.log(`Discovery synchronization passed: ${catalog.length} catalog cases and ${reports.length} reports.`);
