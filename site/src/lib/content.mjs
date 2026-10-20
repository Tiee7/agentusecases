import fs from 'node:fs';
import {createHash} from 'node:crypto';
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
export const personalLevels = ['高','中','低','待核实'];
export const personalFields = {audience:'适用人群',use:'用途',benefit:'预期收益',setup_cost:'设置成本',maintenance_cost:'维护成本',frequency:'使用频率',privacy_risk:'隐私风险',error_risk:'错误风险'};
const storedDecisions = ['建议投入客户验证','仅建议受控试点','适合内部效率工具','不建议商业投入'];
export const decisions = ['建议找客户试用验证','建议先小规模试用','适合内部效率工具','不建议商业投入'];
export const categories = { money:'财务与消费', health:'健康与医疗', work:'工作与效率', coding:'开发与技术', life:'生活与事务' };
export const safeId = id => typeof id === 'string' && /^[a-z0-9][a-z0-9-]{0,199}$/.test(id);
const text = value => typeof value === 'string' ? value : '';
const readerText = value => text(value).replaceAll('仅建议受控试点','建议先小规模试用').replaceAll('建议投入客户验证','建议找客户试用验证');
export function safeUrl(value) {
  try { const u = new URL(value); return u.protocol === 'https:' && !u.username && !u.password ? u.href : ''; } catch { return ''; }
}
const number = value => typeof value === 'number' && Number.isFinite(value) ? value : 0;
export function projectSourceTrial(value, expectedUrl) {
  const empty = {status:'not_observed',agent:'',text:'',url:safeUrl(expectedUrl),observedAt:'',method:'none'};
  if (!value) return empty;
  if (value.source_url !== expectedUrl || !safeUrl(value.source_url) || !['available','missing','unparseable','not_observed'].includes(value.status)) return {...empty,status:'unparseable'};
  const w=value.observation_window;
  const validWindow=w && value.observed_at===null && w.basis==='system_time_bracketing_tool_call' && Number.isFinite(Date.parse(w.start)) && Number.isFinite(Date.parse(w.end)) && Date.parse(w.start)<=Date.parse(w.end);
  const observedLabel=validWindow?`${w.start} 至 ${w.end}（时间区间）`:text(value.observed_at);
  if (value.status==='available' && (!text(value.text).trim() || !text(value.agent).trim() || !['ssr','dom'].includes(value.method) || !(validWindow || (!w && Number.isFinite(Date.parse(value.observed_at)))))) return {...empty,status:'unparseable'};
  return {status:value.status,agent:value.status==='available'?text(value.agent):'',text:value.status==='available'?text(value.text):'',url:safeUrl(value.source_url),observedAt:observedLabel,method:text(value.method)};
}
export const sourceStatusLabels = {available:'源站试用模板',missing:'模板未收录',unparseable:'模板未收录',not_observed:'模板未收录'};
function sourcePrompt(source) {
  return {title:'源站试用模板',language:'源站原文',kind:'site_template',attribution:'源站提供的试用模板；不代表案例原作者实际使用的提示词。',url:source.url,refs:[],text:source.text,agent:source.agent,observedAt:source.observedAt};
}
export function projectSourceCase(value, expectedUrl) {
  const empty={status:'not_observed',url:safeUrl(expectedUrl),agents:[],agentLabel:'未收录',observedAt:'',sections:[]};
  if (!value || value.version!==1 || value.source_url!==expectedUrl || value.status!=='observed' || !/^[a-f0-9]{64}$/.test(value.body_sha256 || '') || !Number.isFinite(Date.parse(value.observed_at))) return empty;
  const agents=value.agent_status==='observed' && Array.isArray(value.actual_agents)?value.actual_agents.map(text).filter(Boolean):[];
  const summary=value.summary;
  const valid=summary?.presentation==='original_bilingual_summary' && summary.based_on_sha256===value.body_sha256;
  const sections=valid?['introduction','method','outcome'].map((key,i)=>({label:['介绍','方法','结果与限制'][i],en:text(summary.sections?.[key]?.en),zh:text(summary.sections?.[key]?.zh)})):[];
  return {...empty,status:'observed',agents,agentLabel:agents.length?agents.join(' · '):value.agent_status==='custom_or_unnamed'?'自建或未命名 agent':empty.agentLabel,observedAt:value.observed_at,sections:sections.length===3 && sections.every(s=>s.en && s.zh)?sections:[]};
}
export function projectArchive(value,entry) {
  const v=value?.version===1 && value.url===entry.url?value:{};
  const source=v.source_text; const translated=v.translation;
  const matches=(body,hash)=>typeof body==='string' && body.length>0 && createHash('sha256').update(body).digest('hex')===hash;
  const sourceText=source?.format==='extracted_page_text' && source.body_sha256===v.body_sha256 && matches(source.body,source.body_sha256)?source.body:'';
  const translationText=translated?.status==='available' && translated.format==='full_extracted_text_translation' && translated.based_on_body_sha256===v.body_sha256 && matches(translated.body,translated.body_sha256)?translated.body:'';
  const f=v.fields || {}; const get=k=>f[k]?.status==='observed'?f[k].value:null;
  const editorial=v.editorial; const sections=editorial?.status==='reviewed' && editorial.format==='detailed_bilingual_restatement' ? ['introduction','method','outcome','notes'].map(key=>({key,items:(editorial.sections?.[key] || []).filter(x=>text(x.en) && text(x.zh)).map(x=>({en:text(x.en),zh:text(x.zh)}))})).filter(s=>s.items.length):[];
  return {sourceText,translationText,translationStale:Boolean(translated && (translated.status==='stale' || translated.based_on_body_sha256!==v.body_sha256)),status:v.status==='observed'?'observed':'not_observed',url:safeUrl(entry.url),path:`/cases/${entry.id}/`,observedAt:text(v.observed_at),historical:Boolean(v.capture_basis),bodyHash:text(v.body_sha256),htmlHash:text(v.html_sha256),stale:Boolean(editorial && editorial.based_on_body_sha256!==v.body_sha256),sections,
  agents:Array.isArray(get('actual_agents'))?get('actual_agents').map(text).filter(Boolean):[], category:text(get('category')?.label),tags:Array.isArray(get('tags'))?get('tags').map(x=>text(x.label)).filter(Boolean):[],author:text(get('author')),wanted:Number.isSafeInteger(get('wanted')) && get('wanted')>=0?get('wanted'):null,sourceDate:text(get('source_date')),addedAt:text(get('added_at')),originals:(Array.isArray(get('original_sources'))?get('original_sources'):(entry.original_sources||[])).map(safeUrl).filter(Boolean),
  lastAttempt:v.last_attempt?{at:text(v.last_attempt.at || v.last_attempt.attempted_at),status:text(v.last_attempt.status),error:text(v.last_attempt.error)}:null,
  fields:['title','introduction','method','outcome','notes','actual_agents','original_sources','author','category','tags','wanted','source_date','added_at','try_it'].map(key=>({key,status:text(f[key]?.status)||'not_observed',sha:text(f[key]?.sha256),pending:['introduction','method','outcome','notes'].includes(key) && f[key]?.status==='observed' && !sections.some(s=>s.key===key)}))};
}
export function projectAuthorMethod(value, entry) {
  const sources=(entry.original_sources || []).map(safeUrl).filter(Boolean);
  const fallback={status:'unavailable',source:sources[0] || '',title:'原始案例来源',steps:[],reason:'外部原作者页面尚未取得；这不表示源站案例未读取。'};
  if (!value || value.version!==1 || value.presentation!=='bilingual_summary' || !sources.includes(value.source_url)) return fallback;
  if (value.status==='unavailable') return {...fallback,title:text(value.source_title)||fallback.title,reason:text(value.unavailable_reason)||fallback.reason};
  if (!['author_summary','reported_summary'].includes(value.status) || !/^[a-f0-9]{64}$/.test(value.source_sha256 || '') || !Number.isFinite(Date.parse(value.accessed_at))) return fallback;
  if (!Array.isArray(value.steps) || !value.steps.length || value.steps.length>6 || value.steps.some(s=>!text(s.en).trim() || !text(s.zh).trim())) return fallback;
  return {status:value.status,source:safeUrl(value.source_url),title:text(value.source_title),steps:value.steps.map(s=>({en:text(s.en),zh:text(s.zh)})),reason:''};
}
// Deliberate public projection: never spread a record or publish its filesystem paths.
export function projectReport(record, entry) {
  if (record.schema_version !== 2 || record.status !== 'completed' || record.id !== entry.id || record.url !== entry.url) return null;
  if (!storedDecisions.includes(record.verdict?.decision)) throw new Error(`Invalid verdict: ${entry.id}`);
  const sources = (record.sources || []).map(s => ({ id:text(s.id), title:text(s.title), url:safeUrl(s.url), supports:text(s.supports) })).filter(s => s.url && /^S[a-zA-Z0-9-]+$/.test(s.id));
  const sourceIds = new Set(sources.map(s => s.id));
  const refs = values => (values || []).filter(id => sourceIds.has(id));
  const scores = Object.entries(weights).map(([key,weight]) => ({ key, label:labels[key], weight, value:number(record.scores?.[key]?.score), rationale:text(record.scores?.[key]?.rationale), refs:refs(record.scores?.[key]?.source_ids) }));
  const scoreAvailable = Object.keys(weights).every(key => typeof record.scores?.[key]?.score === 'number' && Number.isFinite(record.scores[key].score) && record.scores[key].score >= 0 && record.scores[key].score <= 5);
  const sections = (record.sections || []).filter(s => ['customer','workflow','market','competition','economics','distribution','moat','execution','feedback','decision'].includes(s.id)).map(s => ({ id:s.id, title:text(s.title), body:readerText(s.body), refs:refs(s.source_ids) }));
  const sourceTrial = projectSourceTrial(entry.source_trial || record.source_trial, entry.url);
  return { id:entry.id, archive:projectArchive(entry.archive,entry), caseTitle:text(entry.title), sourceCase:projectSourceCase(entry.source_case || record.source_case,entry.url), authorMethod:projectAuthorMethod(record.author_method,entry), sourceTrial, title:text(record.title), industry:text(record.industry), category:text(entry.category), date:text(record.researched_at), confidence:text(record.confidence),
    personal:{level:personalLevels.includes(record.personal_value?.level) ? record.personal_value.level : '待核实', reason:text(record.personal_value?.reason) || '旧记录尚未评估自用价值。', refs:refs(record.personal_value?.source_ids), details:Object.entries(personalFields).map(([key,label]) => ({label,body:text(record.personal_value?.[key]) || '待核实'}))},
    trial:{status:sourceTrial.status==='available'?'collected':text(record.try_it?.source_prompt_status) || 'missing', note:sourceTrial.status==='available' ? '优先展示源站提供的试用模板。下方自编模板仅作补充，未做模型实测。' : text(record.try_it?.source_prompt_note) || '原始提示词尚未收集；暂无试用模板。', prerequisites:text(record.try_it?.prerequisites), tools:text(record.try_it?.tools), expected:text(record.try_it?.expected_result), prompts:[...(sourceTrial.status==='available'?[sourcePrompt(sourceTrial)]:[]), ...(record.try_it?.prompts || []).filter(p => ['original','adapted','ours'].includes(p.kind) && text(p.text)).map(p => ({title:text(p.title),language:text(p.language),kind:p.kind,attribution:text(p.attribution),url:safeUrl(p.source_url),refs:refs(p.source_ids),text:text(p.text)}))]},
    verdict:{ decision:decisions[storedDecisions.indexOf(record.verdict.decision)], headline:readerText(record.verdict.headline), reason:readerText(record.verdict.reason), next:readerText(record.verdict.next_action), stop:readerText(record.verdict.stop_condition) },
    score:scoreAvailable ? Math.round(scores.reduce((sum,s) => sum + s.value*s.weight/5,0)*10)/10 : null, scoreAvailable, scores, sections, sources,
    facts:(record.facts || []).map(f => ({ statement:text(f.statement), refs:refs(f.source_ids) })),
    models:(record.unit_economics || []).map(m => ({ scenario:text(m.scenario), unit:text(m.unit), currency:text(m.currency), price:finiteOrNull(m.price), api:number(m.api_cost), human:number(m.human_cost), other:number(m.other_variable_cost), acquisition:number(m.acquisition_cost), volume:number(m.units_per_month), fixed:number(m.fixed_monthly_cost), assumptions:text(m.assumptions), refs:refs(m.source_ids) })),
    counter:readerText(record.disconfirming_evidence), limitations:readerText(record.limitations),
    minutes:Math.max(1,Math.ceil((sections.map(s=>s.body).join('').length + readerText(record.verdict.reason).length)/350)),
  };
}
// Briefs are a distinct public projection; never promote them to v2 research.
const finiteOrNull = value => typeof value === 'number' && Number.isFinite(value) ? value : null;
const presentNumber = (value, ...keys) => finiteOrNull(value[keys.find(key => Object.hasOwn(value,key))]);
export function projectBrief(record, entry, scoring) {
  if (!safeId(entry.id) || record.schema_version !== 1 || record.analysis_depth !== 'brief' || record.status !== 'completed' || record.id !== entry.id || record.url !== entry.url) return null;
  const sources=(record.sources || []).filter(s=>safeUrl(s.url) && typeof s.id==='string' && /^[A-Za-z0-9][A-Za-z0-9-]*$/.test(s.id || '')).map(s=>({id:s.id,title:text(s.title) || new URL(s.url).hostname,url:safeUrl(s.url),supports:text(s.supports)||text(s.summary),status:/^(failed|blocked|skipped|not_read)/.test(s.status || '')?'未读取 / 访问受限':'资料来源'}));
  if(new Set(sources.map(s=>s.id)).size!==sources.length)throw new Error(`Duplicate brief source: ${entry.id}`);
  const sourceIds=new Set(sources.map(s=>s.id));
  const refs=values=>Array.isArray(values)?values.filter(id=>sourceIds.has(id)):[];
  const sourceTrial=projectSourceTrial(entry.source_trial || record.source_trial,entry.url);
  const personal=record.personal_value || {};
  const trial=record.try_it || {};
  const sections=(record.analysis || []).filter(s=>text(s.body).trim()).map((s,i)=>({id:`analysis-${i+1}`,title:text(s.title)||`分析 ${i+1}`,body:readerText(s.body),refs:refs(s.source_ids)}));
  const reported=record.reported_method;
  const reportedMethod=reported?.status==='reported_summary' && reported.source_url===entry.url && reported.source_sha256===entry.archive?.body_sha256 && Array.isArray(reported.steps) ? {title:'归档转述的方法摘要',source:safeUrl(reported.source_url),steps:reported.steps.filter(s=>text(s.en)&&text(s.zh)).map(s=>({en:text(s.en),zh:text(s.zh)}))}:null;
  const scoreLabels={demand_payment:'需求与付费',acquisition:'获客可行性',delivery_economics:'交付与利润',differentiation:'差异化',validation_replication:'验证与复制',audience_frequency:'需求与频率',net_benefit:'净收益',reliability:'可靠性',setup_maintenance:'设置与维护',cost_data_control:'成本与数据可控性'};
  const scoreTracks=scoring?.id===entry.id && scoring.analysis_depth==='brief' && scoring.score_version==='dual-track-v1' ? ['commercial','personal'].map(track=>({title:track==='commercial'?'商业价值':'自用价值',dimensions:Object.entries(scoring[track]?.dimensions || {}).filter(([key])=>Object.hasOwn(scoreLabels,key)).map(([key,d])=>({label:scoreLabels[key],value:Number.isInteger(d.score)&&d.score>=0&&d.score<=4?d.score:null,rationale:text(d.rationale),refs:refs(d.evidence_ids)}))})):[];
  const date=Number.isFinite(Date.parse(record.researched_at))?record.researched_at:'';
  return {id:entry.id,depth:'brief',path:`/briefs/${entry.id}/`,title:text(record.title),caseTitle:text(entry.title),industry:text(record.industry),category:text(entry.category),date,
    archive:projectArchive(entry.archive,entry),sourceTrial,authorMethod:projectAuthorMethod(record.author_method,entry),reportedMethod,
    personal:{level:personalLevels.includes(personal.level)?personal.level:'待核实',reason:text(personal.reason),refs:refs(personal.source_ids),details:Object.entries(personalFields).filter(([key])=>text(personal[key]).trim()).map(([key,label])=>({label,body:text(personal[key])}))},
    trial:{status:sourceTrial.status==='available'?'collected':'missing',prerequisites:text(trial.prerequisites),tools:text(trial.tools),expected:text(trial.expected_result),prompts:[...(sourceTrial.status==='available'?[sourcePrompt(sourceTrial)]:[]),...(trial.prompts || []).filter(p=>['original','adapted','ours'].includes(p.kind)&&text(p.text).trim()).map(p=>({title:text(p.title),language:text(p.language),kind:p.kind,attribution:text(p.attribution),url:safeUrl(p.source_url),refs:refs(p.source_ids),text:text(p.text)}))]},
    verdict:{decision:readerText(record.verdict?.decision),headline:readerText(record.verdict?.headline),reason:readerText(record.verdict?.reason),next:readerText(record.verdict?.next_action),stop:readerText(record.verdict?.stop_condition)},
    briefReason:text(record.brief_reason),score:null,scoreAvailable:false,scoreTracks,sections,sources,
    facts:(record.facts || []).filter(f=>text(f.statement)).map(f=>({statement:text(f.statement),type:({verified:'资料核实',author_claim:'作者自述',scenario_assumption:'情景假设'})[f.type] || '资料记载',refs:refs(f.source_ids)})),
    models:(record.unit_economics || []).map(m=>({scenario:text(m.scenario),unit:text(m.unit),currency:text(m.currency),price:finiteOrNull(m.price),api:presentNumber(m,'api_cost','generation_cost'),human:finiteOrNull(m.human_cost),other:finiteOrNull(m.other_variable_cost),acquisition:finiteOrNull(m.acquisition_cost),volume:presentNumber(m,'units_per_month','monthly_volume'),fixed:presentNumber(m,'fixed_monthly_cost','monthly_fixed_cost'),assumptions:text(m.assumptions),refs:refs(m.source_ids),valueType:text(m.value_type),cashUpfront:finiteOrNull(m.cash_fixed_upfront),cashVariable:finiteOrNull(m.cash_variable_per_unit),cashKnown:finiteOrNull(m.cash_4week_known),cashLimit:finiteOrNull(m.cash_budget_limit),cashBuffer:finiteOrNull(m.budget_buffer_for_unlisted_cash),budgetStatus:text(m.budget_status)})),
    feedback:{note:text(record.feedback?.note)||text(record.feedback?.signal),searches:(record.feedback?.searches || []).map(s=>({channel:text(s.channel),query:text(s.query),outcome:text(s.outcome)})),observations:(record.feedback?.observations || []).map(o=>({finding:text(o.finding)||text(o.bias),refs:refs([o.source_id])})).filter(o=>o.finding)},
    counter:readerText(record.disconfirming_evidence),limitations:readerText(record.limitations),minutes:Math.max(1,Math.ceil(sections.map(s=>s.body).join('').length/350))};
}

export function loadContent(root = repoRoot) {
  const registry = JSON.parse(fs.readFileSync(path.join(root,'registry/cases.json'),'utf8'));
  const notePath=path.join(root,'registry/reading-notes.json');const notes=fs.existsSync(notePath)?JSON.parse(fs.readFileSync(notePath,'utf8')).limitations || {}:{};
  const catalog = [], reports = [], briefs = [], seen = new Set();
  for (const entry of registry.cases) {
    if (!safeId(entry.id) || seen.has(entry.id)) throw new Error('Invalid or duplicate catalog ID');
    seen.add(entry.id);
    const archivePath=path.join(root,'registry','archives',`${entry.id}.json`);
    if(fs.existsSync(archivePath)) entry.archive=JSON.parse(fs.readFileSync(archivePath,'utf8'));
    const file = path.join(root,'research',`${entry.id}.json`);
    const reportFile = path.join(root,'reports',`${entry.id}.md`);
    let report = null;
    if (fs.existsSync(file) && fs.existsSync(reportFile)) {
      const record=JSON.parse(fs.readFileSync(file,'utf8'));
      if(notes[record.id])record.limitations=notes[record.id];
      const feedback=(record.feedback?.observations || []).map(x=>(x.directness==='adjacent_workflow'?'相关体验：':'')+text(x.finding)).join('\n\n') || '暂无直接用户反馈。';
      record.sections=(record.sections || []).map(s=>s.id==='feedback'?{...s,body:feedback}:s);
      report=projectReport(record,entry);
    }
    if (report) reports.push(report);
    const briefFile=path.join(root,'research/brief',`${entry.id}.json`), briefReport=path.join(root,'reports/brief',`${entry.id}.md`);
    let brief=null;
    if(!report && fs.existsSync(briefFile) && fs.existsSync(briefReport)){
      const scoreFile=path.join(root,'research/scoring-v1',`${entry.id}.json`);
      brief=projectBrief(JSON.parse(fs.readFileSync(briefFile,'utf8')),entry,fs.existsSync(scoreFile)?JSON.parse(fs.readFileSync(scoreFile,'utf8')):undefined);
      if(brief)briefs.push(brief);
    }
    const status=report?'completed':brief?'brief':'pending';
    catalog.push({ id:entry.id, archive:projectArchive(entry.archive,entry), sourceCase:projectSourceCase(entry.source_case,entry.url), firstSeen:Number.isFinite(Date.parse(entry.first_seen_at)) ? new Date(entry.first_seen_at).toISOString() : '', title:report?.title || brief?.title || text(entry.title), category:text(entry.category), listed:entry.listed !== false, complete:Boolean(report), status, researchState:report?'deep':brief?'brief':'pending', readingPath:report?`/reports/${entry.id}/`:brief?.path || '', source:safeUrl(entry.url), sourceTrial:report?.sourceTrial || projectSourceTrial(entry.source_trial,entry.url) });
  }
  reports.sort((a,b) => b.date.localeCompare(a.date) || a.id.localeCompare(b.id));
  briefs.sort((a,b)=>b.date.localeCompare(a.date)||a.id.localeCompare(b.id));
  catalog.sort((a,b) => b.firstSeen.localeCompare(a.firstSeen) || a.id.localeCompare(b.id));
  return { reports, briefs, catalog };
}
export const dateLabel = date => new Intl.DateTimeFormat('zh-CN',{year:'numeric',month:'2-digit',day:'2-digit',timeZone:'UTC'}).format(new Date(date));
export const tone = decision => decisions.indexOf(decision) === 1 ? 'trial' : decisions.indexOf(decision) === 3 ? 'avoid' : 'internal';
