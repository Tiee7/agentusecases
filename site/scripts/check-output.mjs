import {execFileSync} from 'node:child_process';
import fs from 'node:fs';import path from 'node:path';import assert from 'node:assert/strict';import {loadContent} from '../src/lib/content.mjs';
const {reports,briefs,catalog}=loadContent();const allowed=new Set(['index.html','404.html','catalog/index.html','briefs/index.html','method/index.html','favicon.svg',...catalog.map(c=>`cases/${c.id}/index.html`),...reports.map(r=>`reports/${r.id}/index.html`),...briefs.map(r=>`briefs/${r.id}/index.html`),...catalog.filter(c=>c.sourceTrial.status==='available').map(c=>`trials/${c.id}/index.html`)]);
// Check exact text and inert markup before exempting archive containers below.
process.stdout.write(execFileSync('python3',['scripts/check-archive-output.py'],{encoding:'utf8'}));
const files=fs.readdirSync('dist',{recursive:true}).filter(f=>fs.statSync(path.join('dist',f)).isFile());
for(const file of files){assert(allowed.has(file)||/^_astro\/[\w.-]+\.(css|js)$/.test(file),`Unexpected public file: ${file}`);const body=fs.readFileSync(path.join('dist',file),'utf8').replace(/<(pre|div)\b(?=[^>]*\bid="source-(?:original|translation)")[^>]*>[\s\S]*?<\/\1>/g,'');assert(!/GH_TOKEN|["\s]\/workspace\/|data\/source-cache|verify-sources|git push|hourly-business-research|remote-readback|BEGIN PRIVATE KEY/.test(body),`Internal data in ${file}`)}
for(const required of allowed)assert(files.includes(required),`Missing public file: ${required}`);
console.log(`Public output allowlist passed: ${files.length} files, ${reports.length} reports; no raw JSON, logs, task files, caches or source maps.`);

const home=fs.readFileSync('dist/index.html','utf8'), index=fs.readFileSync('dist/catalog/index.html','utf8');
assert(!home.includes('data-recent-id') && !home.includes('最近收录'));
assert.equal((index.match(/data-item /g)||[]).length,catalog.length);
for(const c of catalog)assert(index.includes(`data-search="${c.title.replaceAll('&','&amp;').replaceAll('"','&quot;')}`),`Missing catalog case ${c.id}`);
for(const phrase of ['证据先于结论','没有验证的成功，不写成确定的收益','读结论，也读限制。','工具调用前后计时区间','不代表源站没有标签','不以发布域名推断作者','外部原作者页面是否取得','字段覆盖、时间与哈希','非作者实际提示词','元数据不等于完整正文','已收录源站试用模板 · 源站建议模板，不是作者实际提示词或本站自编模板。','（链接不等于已经读取）','原始长文只保留在本地缓存；公开存储提供元数据、哈希与已审核重述，未获得全文转载许可。','实际 agent（源站标注）','源站观测：已读取','已审核的详细事实重述 · 英文与对应中文','中文详细整理','English · Detailed case archive','以下为我们整理的源站叙述，未经独立结果验证；不是逐字全文。外部原作者页面是否取得，与本页源站观测分别记录。'])for(const file of files.filter(f=>f.endsWith('.html')))assert(!fs.readFileSync(path.join('dist',file),'utf8').includes(phrase),`Repeated disclaimer in ${file}`);
console.log(`Discovery synchronization passed: ${catalog.length} catalog cases and ${reports.length} reports.`);

for(const r of reports){const html=fs.readFileSync(`dist/reports/${r.id}/index.html`,'utf8');assert(html.indexOf('id="author-method"')<html.indexOf('id="verdict"'));assert(html.includes('原作者的方法与来源'));for(const section of r.sections)assert(html.includes(`href="#${section.id}"`),`Missing deep section in contents: ${r.id}/${section.id}`);}

process.stdout.write(execFileSync('python3',['scripts/check-trial-output.py'],{encoding:'utf8'}));

// Every edited title must agree across all static routes; never rewrite source blocks.
const escapeHtml=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
for(const r of reports){
 const title=escapeHtml(r.title);
 assert(home.includes(`>${title}</a></h3>`),`Card title mismatch: ${r.id}`);
 for(const route of ['reports','cases',...(r.sourceTrial.status==='available'?['trials']:[])]){
  const html=fs.readFileSync(`dist/${route}/${r.id}/index.html`,'utf8');
  assert(html.includes(`<h1>${title}</h1>`),`H1 mismatch: ${route}/${r.id}`);
  assert(html.includes(`<title>${title}`),`SEO title mismatch: ${route}/${r.id}`);
 }
}
console.log(`Objective titles synchronized across ${reports.length} edited cases, cards and SEO titles.`);

// Every brief is publicly reachable, without changing deep-research counts.
const briefIndex=fs.readFileSync('dist/briefs/index.html','utf8');
assert(home.includes(`data-brief-count="${briefs.length}"`));
assert.equal((briefIndex.match(/data-item /g)||[]).length,briefs.length);
const statusCounts={completed:reports.length,brief:briefs.length,pending:catalog.filter(c=>c.status==='pending').length};
for(const [status,count] of Object.entries(statusCounts))assert.equal((index.match(new RegExp(`data-status="${status}"`,'g'))||[]).length,count);
assert.equal(Object.values(statusCounts).reduce((a,b)=>a+b,0),catalog.length);
for(const b of briefs){
 const html=fs.readFileSync(`dist/briefs/${b.id}/index.html`,'utf8');
 const source=fs.readFileSync(`dist/cases/${b.id}/index.html`,'utf8');
 const title=escapeHtml(b.title);
 assert(briefIndex.includes(`href="${b.path}"`),`Missing brief link: ${b.id}`);
 assert(html.includes(`<h1>${title}</h1>`) && html.includes(`<title>${title}`),`Brief title mismatch: ${b.id}`);
 assert(source.includes(`href="${b.path}"`) && source.includes('已完成简报'),`Missing case-to-brief link: ${b.id}`);
 assert(html.includes('简报不设总分。') && !html.includes('commercial-score-badge'),`Brief score misclassified: ${b.id}`);
 for(const section of b.sections)assert(html.includes(`id="${section.id}"`),`Missing brief section: ${b.id}`);
 const targets=new Set([...html.matchAll(/\bid="([^"]+)"/g)].map(m=>m[1]));
 for(const match of html.matchAll(/href="#([^"]+)"/g))assert(targets.has(match[1]),`Broken brief anchor: ${b.id} #${match[1]}`);
 for(const source of b.sources)assert(html.includes(`id="source-${source.id}"`),`Missing source: ${b.id}/${source.id}`);
}
console.log(`Brief publication passed: ${briefs.length} brief routes, three catalog states, titles, sources and internal anchors.`);
