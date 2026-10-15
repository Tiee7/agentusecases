import fs from 'node:fs';
import path from 'node:path';
// Resolve from the command directory, not import.meta.url (Astro moves build chunks).
function findRepository(start) {
  let current = path.resolve(start);
  while (!fs.existsSync(path.join(current, 'registry/cases.json'))) {
    const parent = path.dirname(current);
    if (parent === current) throw new Error('Repository content is unavailable');
    current = parent;
  }
  return current;
}
export const repoRoot = findRepository(process.cwd());
const weights = { demand:20, outcome:20, economics:20, distribution:15, moat:10, execution:10, feedback:5 };
export const labels = { demand:'付费需求', outcome:'效果证据', economics:'单位经济', distribution:'获客路径', moat:'竞争壁垒', execution:'交付风险', feedback:'独立反馈' };
export const decisions = ['建议投入客户验证','仅建议受控试点','适合内部效率工具','不建议商业投入'];
export const categories = { money:'财务与消费', health:'健康与医疗', work:'工作与效率', coding:'开发与技术', life:'生活与事务' };
export const safeId = id => typeof id === 'string' && /^[a-z0-9][a-z0-9-]{0,199}$/.test(id);
const text = value => typeof value === 'string' ? value : '';
export function safeUrl(value) {
  try { const u = new URL(value); return u.protocol === 'https:' && !u.username && !u.password ? u.href : ''; } catch { return ''; }
}
const number = value => typeof value === 'number' && Number.isFinite(value) ? value : 0;
// Deliberate public projection: never spread a record or publish its filesystem paths.
export function projectReport(record, entry) {
  if (record.schema_version !== 2 || record.status !== 'completed' || record.id !== entry.id || record.url !== entry.url) return null;
  if (!decisions.includes(record.verdict?.decision)) throw new Error(`Invalid verdict: ${entry.id}`);
  const sources = (record.sources || []).map(s => ({ id:text(s.id), title:text(s.title), url:safeUrl(s.url), supports:text(s.supports) })).filter(s => s.url && /^S[a-zA-Z0-9-]+$/.test(s.id));
  const sourceIds = new Set(sources.map(s => s.id));
  const refs = values => (values || []).filter(id => sourceIds.has(id));
  const scores = Object.entries(weights).map(([key,weight]) => ({ key, label:labels[key], weight, value:number(record.scores?.[key]?.score), rationale:text(record.scores?.[key]?.rationale), refs:refs(record.scores?.[key]?.source_ids) }));
  const sections = (record.sections || []).filter(s => ['customer','workflow','market','competition','economics','distribution','moat','execution','feedback','decision'].includes(s.id)).map(s => ({ id:s.id, title:text(s.title), body:text(s.body), refs:refs(s.source_ids) }));
  return { id:entry.id, title:text(record.title), industry:text(record.industry), category:text(entry.category), date:text(record.researched_at), confidence:text(record.confidence),
    verdict:{ decision:record.verdict.decision, headline:text(record.verdict.headline), reason:text(record.verdict.reason), next:text(record.verdict.next_action), stop:text(record.verdict.stop_condition) },
    score:Math.round(scores.reduce((sum,s) => sum + s.value*s.weight/5,0)*10)/10, scores, sections, sources,
    facts:(record.facts || []).map(f => ({ statement:text(f.statement), refs:refs(f.source_ids) })),
    models:(record.unit_economics || []).map(m => ({ scenario:text(m.scenario), unit:text(m.unit), currency:text(m.currency), price:number(m.price), api:number(m.api_cost), human:number(m.human_cost), other:number(m.other_variable_cost), acquisition:number(m.acquisition_cost), volume:number(m.units_per_month), fixed:number(m.fixed_monthly_cost), assumptions:text(m.assumptions), refs:refs(m.source_ids) })),
    counter:text(record.disconfirming_evidence), limitations:text(record.limitations),
    minutes:Math.max(1,Math.ceil((sections.map(s=>s.body).join('').length + text(record.verdict.reason).length)/350)),
  };
}
export function loadContent(root = repoRoot) {
  const registry = JSON.parse(fs.readFileSync(path.join(root,'registry/cases.json'),'utf8'));
  const catalog = [], reports = [], seen = new Set();
  for (const entry of registry.cases) {
    if (!safeId(entry.id) || seen.has(entry.id)) throw new Error('Invalid or duplicate catalog ID');
    seen.add(entry.id);
    const file = path.join(root,'research',`${entry.id}.json`);
    const reportFile = path.join(root,'reports',`${entry.id}.md`);
    let report = null;
    if (fs.existsSync(file) && fs.existsSync(reportFile)) report = projectReport(JSON.parse(fs.readFileSync(file,'utf8')),entry);
    if (report) reports.push(report);
    catalog.push({ id:entry.id, title:report?.title || text(entry.title), category:text(entry.category), listed:entry.listed !== false, complete:Boolean(report), source:safeUrl(entry.url) });
  }
  reports.sort((a,b) => b.date.localeCompare(a.date) || a.id.localeCompare(b.id));
  return { reports, catalog };
}
export const dateLabel = date => new Intl.DateTimeFormat('zh-CN',{year:'numeric',month:'2-digit',day:'2-digit',timeZone:'UTC'}).format(new Date(date));
export const tone = decision => decisions.indexOf(decision) === 1 ? 'trial' : decisions.indexOf(decision) === 3 ? 'avoid' : 'internal';
