import {test,expect} from '@playwright/test';import AxeBuilder from '@axe-core/playwright';import {loadContent} from '../src/lib/content.mjs';
const {reports,catalog}=loadContent();
test('reader can search, filter, reset and follow a report',async({page})=>{const errors=[];page.on('pageerror',e=>errors.push(e.message));await page.goto('/');await expect(page.locator('[data-item]')).toHaveCount(reports.length);await page.locator('#search').fill('EU261');await expect(page.locator('[data-item]:visible')).toHaveCount(1);await page.locator('#search').fill('zzzz-nothing-found');await expect(page.locator('#empty')).toBeVisible();await page.locator('#reset').click();await page.locator('#filter').selectOption('适合内部效率工具');const expected=reports.filter(r=>r.verdict.decision==='适合内部效率工具').length;await expect(page.locator('[data-item]:visible')).toHaveCount(expected);await page.reload();await expect(page.locator('[data-item]:visible')).toHaveCount(expected);await page.locator('#reset').click();await page.locator('#sort').selectOption('score');await expect(page.locator('[data-item]:visible').first()).toHaveAttribute('data-score',String(Math.max(...reports.map(r=>r.score))));await page.locator('[data-item]:visible h3 a').first().click();await expect(page.locator('.prose')).toBeVisible();expect(errors).toEqual([])});
test('catalog separates unfinished cases and paginates/searches all entries',async({page})=>{
 await page.goto('/catalog/');await expect(page.locator('[data-item]')).toHaveCount(catalog.length);
 await expect(page.locator('[data-item]:visible')).toHaveCount(Math.min(30,catalog.length));
 await page.getByRole('button',{name:'下一页 →'}).click();
 await expect(page.locator('[data-page-label]')).toHaveText(`2 / ${Math.ceil(catalog.length/30)}`);
 await page.locator('#filter').selectOption('completed');
 const completedPages=Math.ceil(reports.length/30),seen=[];
 for(let current=1;current<=completedPages;current++){
  await expect(page.locator('[data-page-label]')).toHaveText(`${current} / ${completedPages}`);
  await expect(page.locator('[data-item]:visible')).toHaveCount(Math.min(30,reports.length-(current-1)*30));
  seen.push(...await page.locator('[data-item]:visible .catalog-title a[href^="/reports/"]').evaluateAll(links=>links.map(a=>a.getAttribute('href'))));
  if(current<completedPages)await page.getByRole('button',{name:'下一页 →'}).click();
 }
 expect([...seen].sort()).toEqual(reports.map(r=>`/reports/${r.id}/`).sort());
 await page.locator('#filter').selectOption('pending');await expect(page.locator('[data-item]:visible a[href^="/reports/"]')).toHaveCount(0);
 await page.locator('#search').fill(catalog.at(-1).id);await page.locator('#filter').selectOption('');await expect(page.locator('[data-item]:visible')).toHaveCount(1);
});
test('long article has working contents, citations, full economics and responsive width',async({page},testInfo)=>{await page.goto(`/reports/${reports[0].id}/`);await expect(page.locator('h1')).toHaveText(reports[0].title);if(!(await page.locator('.toc details').evaluate(el=>el.open)))await page.locator('.toc summary').click();await page.locator('.toc a[href="#models"]').click();await expect(page).toHaveURL(/#models$/);await expect(page.locator('#models .economic-model')).toHaveCount(reports[0].models.length);await page.locator('.refs a').first().click();await expect(page).toHaveURL(/#source-S/);for(const url of ['/', '/catalog/', `/reports/${reports[0].id}/`, '/method/']){await page.goto(url);expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);await page.screenshot({path:`test-results/${testInfo.project.name}-${url==='/'?'home':url.startsWith('/reports')?'report':url.split('/')[1]}.png`,fullPage:url==='/' });const a11y=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();expect(a11y.violations).toEqual([])}});
test('all research routes and sources render and no internal content routes are shipped',async({page,request})=>{for(const r of reports){const response=await page.goto(`/reports/${r.id}/`);expect(response.status()).toBe(200);await expect(page.locator('#sources')).toBeVisible();await expect(page.locator('h1')).toHaveText(r.title)}for(const path of ['/data/','/tasks/maintenance.md','/research/runs/','/.git/config'])expect((await request.get(path)).status()).toBe(404)});
test('without JavaScript the documents and navigation remain readable',async({browser})=>{const context=await browser.newContext({javaScriptEnabled:false});const page=await context.newPage();await page.goto('http://127.0.0.1:4322/');await expect(page.locator('[data-item]:visible')).toHaveCount(reports.length);await page.locator('[data-item] h3 a').first().click();await expect(page.locator('#sources')).toBeVisible();await context.close()});
test('independent personal value filter persists and combines with commercial filters',async({page})=>{
 await page.goto('/');await page.locator('#personal').selectOption('低');await expect(page.locator('[data-item]:visible')).toHaveCount(reports.filter(r=>r.personal.level==='低').length);await page.reload();await expect(page.locator('#personal')).toHaveValue('低');await page.locator('#filter').selectOption('适合内部效率工具');await expect(page.locator('[data-item]:visible')).toHaveCount(reports.filter(r=>r.personal.level==='低'&&r.verdict.decision==='适合内部效率工具').length);await page.locator('#reset').click();await expect(page.locator('#personal')).toHaveValue('');await expect(page.locator('[data-item]:visible')).toHaveCount(reports.length);
});
test('both prompt languages copy exact literal text, with a manual fallback',async({page})=>{
 await page.addInitScript(()=>{Object.defineProperty(navigator,'clipboard',{configurable:true,value:{writeText:async text=>{window.copiedPrompt=text}}})});await page.goto(`/reports/${reports[0].id}/`);
 await expect(page.locator('.copy-prompt')).toHaveCount(reports[0].trial.prompts.length);
 for(let i=0;i<reports[0].trial.prompts.length;i++){await expect(page.locator(`#prompt-${i}`)).toHaveText(reports[0].trial.prompts[i].text);await page.locator(`[data-copy="prompt-${i}"]`).click();expect(await page.evaluate(()=>window.copiedPrompt)).toBe(reports[0].trial.prompts[i].text);}
 await page.evaluate(()=>{Object.defineProperty(navigator,'clipboard',{value:{writeText:async()=>{throw new Error('denied')}}})});await page.locator('[data-copy="prompt-0"]').click();await expect(page.locator('.copy-status').first()).toContainText('手动复制');expect(await page.evaluate(()=>getSelection().toString())).toBe(reports[0].trial.prompts[0].text);
});
test('real browser clipboard preserves both languages',async({page,context})=>{
 await context.grantPermissions(['clipboard-read','clipboard-write']);await page.goto(`/reports/${reports[0].id}/`);
 for(let i=0;i<reports[0].trial.prompts.length;i++){await page.locator(`[data-copy="prompt-${i}"]`).click();expect(await page.evaluate(()=>navigator.clipboard.readText())).toBe(reports[0].trial.prompts[i].text)}
});
test('source trial pages keep literal prompts and do not imply completed research',async({page,context})=>{
 test.setTimeout(180000);
 // All template text is checked in check:output; exercise shared browser UI once per tool,
 // plus interval observations and the newest report. This scales with the UI, not crawl size.
 const representatives=new Map();
 for(const c of catalog.filter(c=>c.sourceTrial.status==='available')){if(!representatives.has(c.sourceTrial.agent))representatives.set(c.sourceTrial.agent,c);if(c.sourceTrial.observedAt.includes('时间区间'))representatives.set(c.id,c);}
 const newest=catalog.find(c=>c.id===reports[0].id);if(newest?.sourceTrial.status==='available')representatives.set(newest.id,newest);
 await context.grantPermissions(['clipboard-read','clipboard-write']);
 for(const c of representatives.values()){
  await page.goto(`/trials/${c.id}/`);await expect(page.locator('#source-prompt')).toHaveText(c.sourceTrial.text);await expect(page.locator('#source-trial')).toContainText(c.sourceTrial.agent);await page.locator('#copy-source').click();expect(await page.evaluate(()=>navigator.clipboard.readText())).toBe(c.sourceTrial.text);if(c.status==='pending')await expect(page.locator('.article-top')).toContainText('待研究');expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);
  const a11y=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();expect(a11y.violations).toEqual([]);
 }
 for(const r of reports.filter(r=>r.sourceTrial.status==='available')){
  await page.goto(`/reports/${r.id}/`);await expect(page.locator('#prompt-0')).toHaveText(r.sourceTrial.text);await expect(page.locator('.prompt-card').first()).toContainText('源站试用模板');await expect(page.locator('.prompt-card').first()).toContainText(r.sourceTrial.agent);
 }
});
test('home keeps collection navigation without a recent collection section',async({page})=>{
 await page.goto('/');await expect(page.locator('.collection-links a[href="/catalog/"]')).toContainText(catalog.length.toLocaleString('en-US'));
 await expect(page.locator('[data-recent-id]')).toHaveCount(0);await expect(page.getByRole('heading',{name:'最近收录'})).toHaveCount(0);
 await page.locator('.collection-links a[href="/catalog/"]').click();await page.locator('#search').fill(catalog[0].id);await expect(page.locator('[data-item]:visible')).toHaveCount(1);
});
test('author method precedes analysis, bilingual summary expands, unread sources stay explicit',async({page})=>{
 const available=reports.find(r=>r.authorMethod.status==='author_summary');
 await page.goto(`/reports/${available.id}/`);
 await expect(page.locator('.prose section').first()).toHaveAttribute('id','source-case');
 await expect(page.locator('#author-method')).toContainText('作者方法摘要');
 await expect(page.locator('#author-method [lang="zh-CN"] li')).toHaveCount(available.authorMethod.steps.length);
 await page.locator('#author-method summary').click();await expect(page.locator('#author-method ol[lang="en"]')).toBeVisible();
 await expect(page.locator('#author-method ol[lang="en"]')).toContainText(available.authorMethod.steps[0].en);
 expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);
 const a11y=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();expect(a11y.violations).toEqual([]);
 const missing=reports.find(r=>r.authorMethod.status==='unavailable');await page.goto(`/reports/${missing.id}/`);await expect(page.locator('#author-method')).toContainText('方法摘要未收录');await expect(page.locator('#author-method li')).toHaveCount(0);await expect(page.locator('#author-method a')).toHaveAttribute('href',missing.authorMethod.source);
});
test('case originals and original-agent search work',async({page})=>{
 for(const r of reports){await page.goto(`/reports/${r.id}/`);await expect(page.locator('#source-original')).toHaveText(r.archive.sourceText);await expect(page.locator('.editorial-summary')).toHaveCount(0);}
 await page.goto('/catalog/');await page.locator('#search').fill('Grok Bot');
 const expected=catalog.filter(c=>c.sourceCase.agents.includes('Grok Bot'));
 await expect(page.locator('[data-item]:visible')).toHaveCount(Math.min(30,expected.length));
 await expect(page.locator('[data-item]:visible').filter({hasText:'原始agent：Grok Bot'}).first()).toBeVisible();
});
test('independent archives show detailed facts, pending restatements and exact templates',async({page,context})=>{
 await context.grantPermissions(['clipboard-read','clipboard-write']);
 for(const c of [catalog.find(c=>c.id==='produce-investment-memos-with-claude-cowork'),catalog.find(c=>!c.archive.sections.length)]){
  await page.goto(`/cases/${c.id}/`);await expect(page.locator('#source-case dt').filter({hasText:/^(Wanted|发布日期|外部来源日期)$/})).toHaveCount(0);await expect(page.locator('.case-tools')).toContainText('原始agent：');
  if(c.complete)await expect(page.locator('#source-case')).toContainText('Adyen');else await expect(page.locator('.editorial-summary')).toHaveCount(0);
  await page.locator('#copy-source').click();expect(await page.evaluate(()=>navigator.clipboard.readText())).toBe(c.sourceTrial.text);
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);const a11y=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();expect(a11y.violations).toEqual([]);
 }
});

test('source originals and full Chinese translations render without becoming business research',async({page})=>{
 for(const c of catalog.filter(c=>c.archive.translationText).slice(0,7)){
  await page.goto(`/cases/${c.id}/`);await expect(page.locator('#source-original')).toHaveText(c.archive.sourceText);await expect(page.locator('#source-translation')).toHaveText(c.archive.translationText);
  if(c.status==='pending')await expect(page.locator('.article-top')).toContainText('待研究');expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);
 }
 const pending=catalog.find(c=>!c.archive.translationText);await page.goto(`/cases/${pending.id}/`);await expect(page.locator('.source-translation')).toHaveCount(0);await expect(page.locator('#source-translation')).toHaveCount(0);
});
test('stale translations are pending review while the current English source stays available',async({page})=>{
 for(const c of catalog.filter(c=>c.archive.translationStale)){
  await page.goto(`/cases/${c.id}/`);
  await expect(page.locator('.translation-review')).toHaveText('中文译文待复核。');
  await expect(page.locator('#source-translation')).toHaveCount(0);
  await expect(page.locator('#source-original')).toHaveText(c.archive.sourceText);
 }
});

test('reader copy stays concise while source records keep provenance',async({page})=>{
 const translated=catalog.find(c=>c.archive.translationText);const pending=catalog.find(c=>!c.archive.translationText);const unread=reports.find(r=>r.authorMethod.status==='unavailable');
 for(const url of ['/', '/catalog/', '/method/', `/cases/${translated.id}/`, `/cases/${pending.id}/`, `/reports/${unread.id}/`, `/trials/${translated.id}/`]){
  await page.goto(url);for(const phrase of ['不代表源站没有标签','不以发布域名推断作者','外部原作者页面是否取得','字段覆盖、时间与哈希','非作者实际提示词','不是0','元数据不等于完整正文','已收录源站试用模板 · 源站建议模板，不是作者实际提示词或本站自编模板。','（链接不等于已经读取）','原始长文只保留在本地缓存；公开存储提供元数据、哈希与已审核重述，未获得全文转载许可。','实际 agent（源站标注）','源站观测：已读取','已审核的详细事实重述 · 英文与对应中文','中文详细整理','English · Detailed case archive','以下为我们整理的源站叙述，未经独立结果验证；不是逐字全文。外部原作者页面是否取得，与本页源站观测分别记录。'])await expect(page.locator('body')).not.toContainText(phrase);
 }
 await page.goto(`/reports/${unread.id}/`);await expect(page.locator('#author-method')).toContainText('方法摘要未收录');await expect(page.locator('#author-method')).not.toContainText(unread.authorMethod.reason);
 await page.goto(`/cases/${pending.id}/`);await expect(page.locator('.source-translation')).toHaveCount(0);await expect(page.locator('#source-case')).not.toContainText('暂无标签');
});
test('catalog action links share a column and source reading panels collapse cleanly',async({page},testInfo)=>{
 await page.goto('/catalog/');const row=page.locator('[data-item]:visible').first();await expect(row.locator(':scope > .catalog-actions')).toHaveCount(1);await expect(row.locator('.catalog-actions a')).toHaveCount(3);
 const actions=await row.locator('.catalog-actions').boundingBox();const title=await row.locator('.catalog-title').boundingBox();if(page.viewportSize().width>=700)expect(actions.x).toBeGreaterThan(title.x+title.width);else expect(actions.y).toBeGreaterThan(title.y);
 const c=catalog.find(c=>c.archive.translationText);await page.goto(`/cases/${c.id}/`);await expect(page.locator('#source-translation')).toBeVisible();await page.locator('.source-original summary').click();await expect(page.locator('#source-original')).toBeVisible();await page.locator('.source-original summary').click();await expect(page.locator('#source-original')).not.toBeVisible();await page.locator('.source-translation summary').click();await expect(page.locator('#source-translation')).not.toBeVisible();await page.locator('#source-trial').scrollIntoViewIfNeeded();await expect(page.locator('#source-prompt')).toBeVisible();expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);
});

for(const route of ['reports','cases'])test(`Cowork ${route}: full Chinese first, compact metadata and responsive date`,async({page},testInfo)=>{
 const id='produce-investment-memos-with-claude-cowork';const a=catalog.find(c=>c.id===id).archive;
 expect(a.translationText).toContain('买入／持有／不买入');
 await page.goto(`/${route}/${id}/`);
 await expect(page.locator('#source-translation')).toBeVisible();await expect(page.locator('#source-translation')).toHaveText(a.translationText);
 await expect(page.locator('#source-original')).not.toBeVisible();await expect(page.locator('#source-original')).toHaveText(a.sourceText);
 await expect(page.locator('#source-case dt').filter({hasText:/^标签$/})).toHaveCount(0);
 await expect(page.locator('#source-case')).not.toContainText('暂无标签');await expect(page.locator('#source-case')).not.toContainText('仅建议受控试点');
 const date=page.locator('.case-added');await expect(date).toHaveText('收录于 2026-10-03');
 const box=await date.boundingBox(),row=await page.locator('.case-meta').boundingBox(),tools=await page.locator('.case-tools').boundingBox();
 expect(Math.abs(box.x+box.width-row.x-row.width)).toBeLessThan(2);
 if(testInfo.project.name==='desktop')expect(Math.abs(box.y-tools.y)).toBeLessThan(10);
 expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);
 await page.locator('#source-case').scrollIntoViewIfNeeded();await page.screenshot({path:`test-results/${testInfo.project.name}-cowork-${route}.png`});
 await page.locator('.source-original summary').click();await expect(page.locator('#source-original')).toBeVisible();
 expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);
});

test('integrated stock and resale reports preserve full translated reading on both routes',async({page},testInfo)=>{
 for(const id of ['let-ai-models-trade-stocks-autonomously-with-1k-each','sell-your-unused-items-online-with-an-agent']){
  const a=catalog.find(c=>c.id===id).archive;expect(a.translationText.length).toBeGreaterThan(100);
  for(const route of ['reports','cases']){
   await page.goto(`/${route}/${id}/`);
   await expect(page.locator('#source-translation')).toBeVisible();await expect(page.locator('#source-translation')).toHaveText(a.translationText);
   await expect(page.locator('#source-original')).not.toBeVisible();await expect(page.locator('#source-original')).toHaveText(a.sourceText);
   expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);
   if(route==='reports'){await expect(page.locator('#sources li')).toHaveCount(reports.find(r=>r.id===id).sources.length);await page.locator('#source-case').scrollIntoViewIfNeeded();await page.screenshot({path:`test-results/${testInfo.project.name}-${id}.png`});}
  }
 }
});

test('objective usage title is consistent in cards, catalog, report, case, trial and SEO',async({page},testInfo)=>{
 const r=reports.find(r=>r.id==='produce-investment-memos-with-claude-cowork');
 await page.goto('/');await expect(page.locator(`h3 a[href="/reports/${r.id}/"]`)).toHaveText(r.title);
 await page.screenshot({path:`test-results/${testInfo.project.name}-objective-titles-home.png`});
 await page.locator(`h3 a[href="/reports/${r.id}/"]`).scrollIntoViewIfNeeded();await page.screenshot({path:`test-results/${testInfo.project.name}-objective-titles-cards.png`});
 await page.goto('/catalog/');await page.locator('#search').fill(r.title);await expect(page.locator('[data-item]:visible h2')).toHaveText(r.title);
 for(const route of ['reports','cases','trials']){
  await page.goto(`/${route}/${r.id}/`);await expect(page.locator('h1')).toHaveText(r.title);await expect(page).toHaveTitle(new RegExp(r.title));
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);
  if(route==='reports'){
   await expect(page.locator('#verdict')).toContainText(r.verdict.reason);
   await expect(page.locator('#source-original')).toHaveText(r.archive.sourceText);
   await page.screenshot({path:`test-results/${testInfo.project.name}-objective-titles-report.png`});
  }
 }
});
