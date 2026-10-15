import fs from 'node:fs';import path from 'node:path';import assert from 'node:assert/strict';import {loadContent} from '../src/lib/content.mjs';
const {reports,catalog}=loadContent();const allowed=new Set(['index.html','404.html','catalog/index.html','method/index.html','favicon.svg',...reports.map(r=>`reports/${r.id}/index.html`),...catalog.filter(c=>c.sourceTrial.status==='available').map(c=>`trials/${c.id}/index.html`)]);
const files=fs.readdirSync('dist',{recursive:true}).filter(f=>fs.statSync(path.join('dist',f)).isFile());
for(const file of files){assert(allowed.has(file)||/^_astro\/[\w.-]+\.(css|js)$/.test(file),`Unexpected public file: ${file}`);const body=fs.readFileSync(path.join('dist',file),'utf8');assert(!/GH_TOKEN|["\s]\/workspace\/|data\/source-cache|verify-sources|git push|hourly-business-research|remote-readback|BEGIN PRIVATE KEY/.test(body),`Internal data in ${file}`)}
for(const required of allowed)assert(files.includes(required),`Missing public file: ${required}`);
console.log(`Public output allowlist passed: ${files.length} files, ${reports.length} reports; no raw JSON, logs, task files, caches or source maps.`);
