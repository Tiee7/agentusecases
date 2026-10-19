import {test,expect} from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';
import {loadContent} from '../src/lib/content.mjs';
const {briefs,reports,catalog}=loadContent();
const spark=briefs.find(b=>b.id==='automate-customer-onboarding-with-a-make-scenario');
const old=briefs.find(b=>b.id==='add-61-kid-friendly-mini-games-to-an-app');

test('home and brief list expose distinct dynamic counts, links, filtering and empty states',async({page})=>{
 await page.goto('/');await expect(page.locator('[data-brief-count]')).toHaveText(`简报 ${briefs.length} ↗`);await expect(page.locator('[data-item]')).toHaveCount(reports.length);
 await page.locator('[data-brief-count]').click();await expect(page).toHaveURL(/\/briefs\/$/);await expect(page.locator('[data-item]')).toHaveCount(briefs.length);await expect(page.locator('[data-item] a[href^="/reports/"]')).toHaveCount(0);await expect(page.locator('[data-item] .score')).toHaveCount(0);
 await page.locator('#search').fill(spark.id);await expect(page.locator('[data-item]:visible')).toHaveCount(1);await page.reload();await expect(page.locator('[data-item]:visible')).toHaveCount(1);
 await page.locator('#search').fill('no-such-brief-zzzz');await expect(page.locator('#empty')).toBeVisible();await expect(page.locator('[data-item]:visible')).toHaveCount(0);await page.locator('#reset').click();await expect(page.locator('[data-item]:visible')).toHaveCount(briefs.length);
 await page.locator('#personal').selectOption('待核实');await expect(page.locator('[data-item]:visible')).toHaveCount(briefs.filter(b=>b.personal.level==='待核实').length);
});

test('catalog has exhaustive deep, brief and pending states with persistent brief navigation',async({page})=>{
 await page.goto('/catalog/');
 for(const [status,count] of [['completed',reports.length],['brief',briefs.length],['pending',catalog.filter(c=>c.status==='pending').length]]){
  await expect(page.locator(`[data-status="${status}"]`)).toHaveCount(count);await page.locator('#filter').selectOption(status);await expect(page.locator('#result-count')).toHaveText(`找到 ${count} 个案例`);await expect(page.locator('[data-item]:visible')).toHaveCount(Math.min(count,30));
 }
 await page.locator('#filter').selectOption('brief');await page.locator('#search').fill(spark.id);await page.reload();await expect(page.locator('#filter')).toHaveValue('brief');await expect(page.locator('[data-item]:visible')).toHaveCount(1);await expect(page.locator('[data-item]:visible .catalog-state')).toHaveText('已完成简报');await page.locator('[data-item]:visible a').filter({hasText:spark.title}).click();await expect(page).toHaveURL(new RegExp(spark.path+'$'));
 await page.goto(`/cases/${spark.id}/`);await expect(page.locator('.article-top')).toContainText('已完成简报');await page.locator('.article-top a[href^="/briefs/"]').click();await expect(page.locator('h1')).toHaveText(spark.title);
 await page.goto(`/trials/${spark.id}/`);await expect(page.locator('.article-top')).toContainText('已完成简报');await expect(page.locator('.article-top a[href^="/briefs/"]')).toHaveCount(1);
});

test('all published briefs, sources, sections and case links render without becoming deep reports',async({page,request})=>{
 for(const b of briefs){const response=await request.get(b.path);expect(response.status(),b.id).toBe(200);const html=await response.text();expect(html).toContain('简报不设总分。');for(const source of b.sources)expect(html).toContain(`id="source-${source.id}"`);for(const section of b.sections)expect(html).toContain(`id="${section.id}"`);const c=await request.get(`/cases/${b.id}/`);expect(await c.text()).toContain(`href="${b.path}"`);}
 for(const b of [old,spark]){await page.goto(b.path);await expect(page.locator('h1')).toHaveText(b.title);await expect(page.locator('.article-meta')).toContainText('简报');await expect(page.locator('.source-translation')).toHaveAttribute('open','');expect(await page.locator('.source-original').evaluate(e=>e.open)).toBe(false);await expect(page.locator('#sources li')).toHaveCount(b.sources.length);await expect(page.locator('#models .economic-model')).toHaveCount(b.models.length);await page.locator('.source-original summary').click();await expect(page.locator('#source-original')).toHaveText(b.archive.sourceText);}
});

test('brief templates copy literal text and manual fallback preserves selection',async({page})=>{
 await page.addInitScript(()=>Object.defineProperty(navigator,'clipboard',{configurable:true,value:{writeText:async text=>{window.copiedBrief=text}}}));
 for(const b of [old,spark]){await page.goto(b.path);await expect(page.locator('.copy-prompt')).toHaveCount(b.trial.prompts.length);for(let i=0;i<b.trial.prompts.length;i++){expect(await page.locator(`#prompt-${i}`).textContent()).toBe(b.trial.prompts[i].text);await page.locator(`[data-copy="prompt-${i}"]`).click();expect(await page.evaluate(()=>window.copiedBrief)).toBe(b.trial.prompts[i].text);}await page.evaluate(()=>Object.defineProperty(navigator,'clipboard',{configurable:true,value:{writeText:async()=>{throw new Error('denied')}}}));await page.locator('[data-copy="prompt-0"]').click();await expect(page.locator('.copy-status').first()).toContainText('手动复制');expect(await page.evaluate(()=>getSelection().toString())).toBe(b.trial.prompts[0].text);}
});

test('unknown costs stay unknown and prepaid annual cash is separate from monthly cost',async({page})=>{
 await page.goto(spark.path);const second=page.locator('#models .economic-model').nth(1);await expect(second.locator('tbody td').nth(3)).toHaveText('待核实');await expect(second).toContainText('贡献还需扣除未核实的可变成本');await expect(second.locator('.cash-budget')).toContainText('144.00');await expect(second).toContainText('12.00');await expect(page.locator('.commercial-score-badge')).toHaveCount(0);await expect(page.locator('#score')).not.toContainText('0 / 100');
});

test('brief list and readers are accessible and fit the viewport',async({page},testInfo)=>{
 for(const route of ['/briefs/',spark.path,old.path,'/catalog/?filter=brief']){await page.goto(route);expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);const result=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();expect(result.violations).toEqual([]);}
 await page.goto(spark.path);await page.screenshot({path:`test-results/${testInfo.project.name}-brief-reader.png`,fullPage:false});
});

test('brief list, translated reading and links work without JavaScript',async({browser})=>{
 const context=await browser.newContext({javaScriptEnabled:false});try{const page=await context.newPage();await page.goto('http://127.0.0.1:4322/briefs/');await expect(page.locator('[data-item]')).toHaveCount(briefs.length);await page.locator(`[href="${spark.path}"]`).click();await expect(page.locator('#source-translation')).toHaveText(spark.archive.translationText);await expect(page.locator('#sources')).toBeVisible();await expect(page.locator('#prompt-0')).toHaveText(spark.trial.prompts[0].text);}finally{await context.close();}
});
