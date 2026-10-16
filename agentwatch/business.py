"""One-case commercial research, validation, stable mapping and deterministic indexes."""
import argparse
import hashlib
import json
import math
import re
import sqlite3
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit
from .personal import validate_personal, render_personal

WEIGHTS={'demand':20,'outcome':20,'economics':20,'distribution':15,'moat':10,'execution':10,'feedback':5}
LABELS={'demand':'付费需求','outcome':'业务价值与效果证据','economics':'单位经济与利润','distribution':'获客与市场进入','moat':'竞争壁垒','execution':'交付与经营风险','feedback':'独立用户反馈信号'}
DECISIONS=('建议投入客户验证','仅建议受控试点','适合内部效率工具','不建议商业投入')
SECTIONS=('customer','workflow','market','competition','economics','distribution','moat','execution','feedback','decision')
REGISTRY=Path('registry/cases.json')

def safe_id(value):
    if not isinstance(value,str) or not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,199}',value):
        raise ValueError('Invalid stable case ID')
    return value

def read_registry():
    return json.loads(REGISTRY.read_text())

def bootstrap(db_path, sync_research=True):
    db=sqlite3.connect(f'file:{Path(db_path).resolve()}?mode=ro',uri=True)
    run=db.execute('SELECT MAX(id) FROM runs').fetchone()[0]
    if run is None:
        raise ValueError('No successful crawl')
    catalog_count=db.execute('SELECT count(*) FROM catalogs WHERE run_id=?',(run,)).fetchone()[0]
    if catalog_count:
        rows=db.execute('SELECT c.url,o.title,o.body,p.position,p.category FROM catalogs c LEFT JOIN observations o ON o.run_id=c.run_id AND o.url=c.url LEFT JOIN priorities p ON p.run_id=c.run_id AND p.url=c.url WHERE c.run_id=? ORDER BY p.position IS NULL,p.position,c.url',(run,)).fetchall()
    else:
        rows=db.execute('SELECT o.url,o.title,o.body,p.position,p.category FROM observations o LEFT JOIN priorities p ON p.run_id=o.run_id AND p.url=o.url WHERE o.run_id=? ORDER BY p.position IS NULL,p.position,o.url',(run,)).fetchall()
    from .source_trial import validate_observation, newer_observation
    trial_table = db.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='source_trials'").fetchone()
    trials = {url:json.loads(payload) for url,payload in db.execute('SELECT url,payload FROM source_trials ORDER BY run_id')} if trial_table else {}
    first_seen = dict(db.execute("SELECT url, MIN(fetched_at) FROM (SELECT c.url,r.fetched_at FROM catalogs c JOIN runs r ON r.id=c.run_id UNION ALL SELECT o.url,r.fetched_at FROM observations o JOIN runs r ON r.id=o.run_id) GROUP BY url"))
    from .source_case import latest, merge
    source_cases = latest(db)
    archives = {}
    if db.execute("SELECT 1 FROM sqlite_master WHERE name='archive_observations'").fetchone():
        archives={url:json.loads(payload) for url,payload in db.execute('SELECT url,payload FROM archive_observations ORDER BY observed_at')}
    old=read_registry() if REGISTRY.exists() else {'cases':[]}
    existing={c['id']:c for c in old['cases']}
    cases=[]
    for url,title,body,rank,category in rows:
        case_id=safe_id(urlsplit(url).path.rstrip('/').rsplit('/',1)[-1])
        previous=existing.pop(case_id,{})
        if url in trials:
            previous['source_trial'] = newer_observation(previous.get('source_trial'), validate_observation(trials[url], url))
        if url in source_cases:
            previous['source_case'] = merge(previous.get('source_case'), source_cases[url])
        title=title or previous.get('title') or case_id.replace('-',' ')
        original_sources=re.findall(r'^Original source: (https://\S+)$',body,re.M) if body else previous.get('original_sources',[])
        original_field=archives.get(url,{}).get('fields',{}).get('original_sources',{})
        if not body and original_field.get('status')=='observed':
            original_sources=original_field.get('value') or []
        cases.append(dict(previous,first_seen_at=previous.get('first_seen_at') or first_seen.get(url),id=case_id,title=title,url=url,category=category or previous.get('category'),site_top_position=rank,report=f'reports/{case_id}.md',record=f'research/{case_id}.json',original_sources=original_sources,listed=True))
    # Retain historical mappings if a case disappears from the current listing.
    cases.extend(dict(c,listed=False) for c in existing.values())
    REGISTRY.parent.mkdir(exist_ok=True)
    REGISTRY.write_text(json.dumps({'schema_version':1,'ranking_scope':'public SSR category top, then sitemap order','cases':cases},ensure_ascii=False,indent=2)+'\n')
    if sync_research:
        sync_source_trials(cases)
    return len(cases)

def sync_source_trials(cases):
    from .source_trial import sync_record
    for case in cases:
        if not case.get('source_trial'):
            continue
        path = Path(case['record'])
        if not path.exists():
            continue
        record = json.loads(path.read_text())
        if record.get('schema_version') != 2 or record.get('status') != 'completed':
            continue
        if record.get('source_trial') == case['source_trial']:
            continue
        sync_record(record, case['source_trial'])
        path.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
        Path(case['report']).write_text(render(record))


def case_state(case):
    path=Path(case['record'])
    if not path.exists():
        return 'pending',None
    record=json.loads(path.read_text())
    if record.get('schema_version')==2 and record.get('status')=='completed':
        return 'completed',record
    return 'legacy_draft',record

def select_case(case_id=None):
    cases=read_registry()['cases']
    if case_id:
        safe_id(case_id)
        case=next((c for c in cases if c['id']==case_id),None)
        if not case:
            raise ValueError('Case is not registered')
        return case
    return next((c for c in cases if c.get('listed',True) and case_state(c)[0]!='completed'),None)

def refs(values,source_ids):
    if not isinstance(values,list) or not values or any(v not in source_ids for v in values):
        raise ValueError('Claim references an unread or unknown source')

def weighted_score(record):
    return round(sum(WEIGHTS[k]*record['scores'][k]['score']/5 for k in WEIGHTS),1)

def validate(record,receipts,expected_id):
    safe_id(expected_id)
    case=select_case(expected_id)
    if record.get('schema_version')!=2 or record.get('status')!='completed' or record.get('id')!=expected_id or record.get('url')!=case['url']:
        raise ValueError('Record identity or completion status does not match the selected case')
    stamp=datetime.fromisoformat(record['researched_at'])
    if stamp.tzinfo is None:
        raise ValueError('Research time must include its timezone')
    if any(not isinstance(record.get(k),str) or not record[k].strip() for k in ('title','industry','confidence')):
        raise ValueError('Report title, industry and confidence are required')
    fetched={r['id']:r for r in receipts if r.get('status')=='fetched'}
    sources=record.get('sources',[])
    ids={s['id'] for s in sources}
    if len(sources)<6 or len(ids)!=len(sources) or not ids<=set(fetched):
        raise ValueError('At least six distinct actually fetched sources are required')
    known_origins={case['url'],*case.get('original_sources',[])}
    if not known_origins.intersection(s['url'] for s in sources):
        raise ValueError('Sources must include the selected case page or its actual original source')
    hosts={urlsplit(fetched[s]['url']).hostname for s in ids}
    kinds=Counter(fetched[s]['kind'] for s in ids)
    if len(hosts)<3 or kinds['primary']<2 or not (kinds['independent'] or kinds['market']) or not kinds['competitor']:
        raise ValueError('Require three publishers, two primary sources, independent/market evidence and a competitor source')
    for source in sources:
        receipt=fetched[source['id']]
        if source['url']!=receipt['url'] or len(source.get('supports',''))<20:
            raise ValueError('Every source must explain exactly what it supports')
    facts=record.get('facts',[])
    if len(facts)<8:
        raise ValueError('At least eight sourced business facts are required')
    for fact in facts:
        if len(fact.get('statement',''))<20:
            raise ValueError('Fact is too thin to support a commercial decision')
        refs(fact.get('source_ids'),ids)
    sections={s['id']:s for s in record.get('sections',[])}
    if set(sections)!=set(SECTIONS):
        raise ValueError('Missing required business analysis sections')
    if sum(len(s.get('body','')) for s in sections.values())<3500:
        raise ValueError('Business report is too brief; depth also requires sourced facts and decision coverage')
    for section in sections.values():
        if len(section.get('body',''))<150:
            raise ValueError('A business section lacks substantive analysis')
        refs(section.get('source_ids'),ids)
    decision=record.get('verdict',{})
    if decision.get('decision') not in DECISIONS or len(decision.get('headline',''))<15 or len(decision.get('reason',''))<100 or not decision.get('next_action') or not decision.get('stop_condition'):
        raise ValueError('Give one explicit commercial decision, rationale, next action and stop condition')
    for key in WEIGHTS:
        dimension=record['scores'][key]
        score=dimension.get('score')
        if isinstance(score,bool) or not isinstance(score,(int,float)) or not 0<=score<=5 or len(dimension.get('rationale',''))<30:
            raise ValueError('Every score must be justified and between zero and five')
        refs(dimension.get('source_ids'),ids)
    searches=record.get('feedback',{}).get('searches',[])
    if len(searches)<3 or len({s['channel'] for s in searches})<2 or any(not s.get('query') or not s.get('outcome') for s in searches):
        raise ValueError('User feedback must be investigated in at least three searches over two channels')
    for observation in record.get('feedback',{}).get('observations',[]):
        refs([observation['source_id']],ids)
        if observation.get('directness') not in ('direct_user','adjacent_workflow') or not observation.get('bias'):
            raise ValueError('Classify direct versus adjacent users and selection bias')
    if not record['feedback'].get('observations') and record['scores']['feedback']['score']!=0:
        raise ValueError('No verified feedback means zero independent feedback signal, not a claimed negative user rating')
    models=record.get('unit_economics',[])
    if len(models)<2:
        raise ValueError('At least two explicit unit economics scenarios are required')
    for model in models:
        for key in ('price','api_cost','human_cost','other_variable_cost','acquisition_cost','units_per_month','fixed_monthly_cost'):
            v=model.get(key)
            if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v) or v<0:
                raise ValueError('Economic inputs must be nonnegative numbers')
        if not model.get('assumptions') or not model.get('unit') or not model.get('currency') or not model.get('scenario'):
            raise ValueError('Label every economic assumption and delivery unit')
        refs(model.get('source_ids'),ids)
        if not all(math.isfinite(v) for v in economics(model)):
            raise ValueError('Computed economic results must be finite')
    if not record.get('disconfirming_evidence') or not record.get('limitations'):
        raise ValueError('Include contrary evidence and concrete unverified claims')
    validate_personal(record)
    return record

def economics(model):
    variable=sum(model[k] for k in ('api_cost','human_cost','other_variable_cost','acquisition_cost'))
    contribution=model['price']-variable
    profit=contribution*model['units_per_month']-model['fixed_monthly_cost']
    return variable,contribution,profit

def render(record):
    from .reader_copy import project
    record=project(record)
    v=record['verdict']
    lines=[f"# {record['title']}",'',f"**商业结论：{v['decision']}。{v['headline']}**",'',v['reason'],'',f"案例ID：`{record['id']}` · 案例来源：{record['url']}",f"研究时间：{record['researched_at']}",'',f"**商业评分：{weighted_score(record):.1f}/100。用户反馈信号占5%。**",'','| 维度 | 权重 | 分数 /5 | 商业依据 |','|---|---:|---:|---|']
    from .author_method import render_author_method
    from .source_case import render as render_source_case
    lines = lines[:1] + render_source_case(record.get('source_case')) + render_author_method(record) + ['','## 我们的分析'] + lines[1:]
    for key,weight in WEIGHTS.items():
        d=record['scores'][key]
        rationale=d['rationale'].replace('|','\\|').replace('\n',' ')
        lines.append(f"| {LABELS[key]} | {weight}% | {d['score']} | {rationale} [{', '.join(d['source_ids'])}] |")
    lines += ['', *render_personal(record), '', '## 已核验事实', '']
    for fact in record['facts']:
        lines.append(f"- {fact['statement']} [{', '.join(fact['source_ids'])}]")
    for section in record['sections']:
        lines += ['',f"## {section['title']}",'',section['body'],'',f"依据：{', '.join(section['source_ids'])}"]
    lines += ['','## 单位经济测算：情景假设，不是项目已实现的财务结果','','| 情景 / 交付单位 | 收入 | 可变成本（含获客） | 单位贡献 | 月交付量 | 月固定成本 | 月经营贡献 |','|---|---:|---:|---:|---:|---:|---:|']
    for model in record['unit_economics']:
        variable,contribution,profit=economics(model)
        lines.append(f"| {model['scenario']} / {model['unit']} ({model['currency']}) | {model['price']:.2f} | {variable:.2f} | {contribution:.2f} | {model['units_per_month']} | {model['fixed_monthly_cost']:.2f} | {profit:.2f} |")
    for model in record['unit_economics']:
        lines += ['',f"{model['scenario']}假设：{model['assumptions']}；API成本 {model['api_cost']}，人工成本 {model['human_cost']}，其他可变成本 {model['other_variable_cost']}，分摊获客成本 {model['acquisition_cost']}。依据：{', '.join(model['source_ids'])}"]
    lines += ['','## 反证与未核实信息','',record['disconfirming_evidence'],'',record['limitations'],'','## 具体动作与止损条件','',v['next_action'],'',f"停止投入条件：{v['stop_condition']}",'','## 来源与对应关系','']
    for source in record['sources']:
        lines.append(f"- [{source['id']}] [{source['title']}]({source['url']})：{source['supports']}")
    lines += ['',f"结构化记录：[research/{record['id']}.json](../research/{record['id']}.json)"]
    return '\n'.join(lines)+'\n'

def indexes():
    cases=read_registry()['cases']
    completed=[];drafts=[];pending=[]
    for case in cases:
        state,record=case_state(case)
        item=(case,state,record)
        (completed if state=='completed' else drafts if state=='legacy_draft' else pending).append(item)
    lines=['# 商业深度研究总索引','',f"已完成深度研究 **{len(completed)}** / 注册案例 **{len(cases)}**。旧版简略初稿 **{len(drafts)}** 份不计入完成。",'','研究按串行互斥执行，每轮完成后至少休息5分钟；调度由父任务管理，本轮不修改调度。历史计划触发验证不代表当前持续运行，见[任务指令与实际状态](tasks/hourly-business-research.md)。一个case ID对应一份报告、一份结构化记录及来源凭据。用户反馈只占5%。','', '[完整案例目录与计划报告路径](registry/CATALOG.md) · [机器可读对应表](registry/cases.json) · [商业研究标准](RESEARCH_STANDARD.md)','', '| 案例 | 商业结论 | 分数 /100 | 自用价值 | 源站试用模板 | 行业 | 研究时间 |','|---|---|---:|---|---|---|---|']
    for case,_,record in completed:
        lines.append(f"| [{record['title']}]({case['report']}) | {record['verdict']['decision']} | {weighted_score(record)} | {record.get('personal_value', {}).get('level', '待核实')} | {record.get('source_trial', {}).get('status', 'not_observed')} | {record['industry']} | {record['researched_at']} |")
    lines += ['','## 需要重做的旧版简略初稿','']
    for case,_,_ in drafts:
        lines.append(f"- [{case['title']}]({case['report']}) · `{case['id']}`")
    lines += ['','## 下一批优先案例','']
    for case,_,_ in (drafts+pending)[:10]:
        lines.append(f"- {case['title']} · `{case['id']}`")
    Path('INDEX.md').write_text('\n'.join(lines)+'\n')
    catalog=['# 完整案例目录','', '已生成的报告可点击；待研究案例列出固定目标路径。目录移出的案例仍保留ID。','', '| ID | 案例 / 来源 | 状态 | 对应报告 | 源站试用模板 | 实际 agent（源站标注） |','|---|---|---|---|---|---|']
    for case in cases:
        state,_=case_state(case)
        title=case['title'].replace('|','\\|')
        report=f"[报告](../{case['report']})" if Path(case['report']).exists() else f"`{case['report']}`"
        sc=case.get('source_case', {})
        agents=('、'.join(sc.get('actual_agents', [])) or ('自建或未命名 agent' if sc.get('agent_status')=='custom_or_unnamed' else '尚未观测')).replace('|', '\\|')
        catalog.append(f"| `{case['id']}` | [{title}]({case['url']}) | {state} | {report} | {case.get('source_trial', {}).get('status', 'not_observed')} | {agents} |")
    Path('registry/CATALOG.md').write_text('\n'.join(catalog)+'\n')

def publish(record_path,evidence_path,expected_id):
    record=json.loads(Path(record_path).read_text())
    receipts=json.loads(Path(evidence_path).read_text())
    case = select_case(expected_id)
    if case.get('source_case'):
        record['source_case'] = case['source_case']
    if case.get('source_trial'):
        from .source_trial import sync_record
        sync_record(record, case['source_trial'])
    validate(record,receipts,expected_id)
    validate_personal(record, required=True)
    from .author_method import validate_author_method
    validate_author_method(record, case, receipts, required=True)
    directory=Path('research/evidence');directory.mkdir(parents=True,exist_ok=True)
    # Source receipts carry metadata only; cache paths and full scraped text stay private to the runner.
    clean=[{k:v for k,v in r.items() if k not in ('text_path','links')} for r in receipts]
    Path(f'research/{expected_id}.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    Path(f'research/evidence/{expected_id}.json').write_text(json.dumps(clean,ensure_ascii=False,indent=2)+'\n')
    Path(f'reports/{expected_id}.md').write_text(render(record))
    indexes()

def main():
    parser=argparse.ArgumentParser()
    sub=parser.add_subparsers(dest='command',required=True)
    boot=sub.add_parser('bootstrap');boot.add_argument('--db',default='data/history.sqlite3');boot.add_argument('--catalog-only',action='store_true')
    prep=sub.add_parser('prepare');prep.add_argument('--case-id')
    pub=sub.add_parser('publish');pub.add_argument('--record',default='data/business-draft.json');pub.add_argument('--evidence',required=True);pub.add_argument('--expected-id',required=True)
    check=sub.add_parser('verify-sources');check.add_argument('--record',default='data/business-draft.json');check.add_argument('--evidence',required=True);check.add_argument('--expected-id',required=True)
    sub.add_parser('index')
    args=parser.parse_args()
    if args.command=='bootstrap':
        print('Registered cases:',bootstrap(args.db, sync_research=not args.catalog_only));indexes()
    elif args.command=='prepare':
        case=select_case(args.case_id)
        Path('data').mkdir(exist_ok=True)
        Path('data/selected-case.json').write_text(json.dumps(case,ensure_ascii=False,indent=2))
        print(case['id'] if case else '')
    elif args.command=='verify-sources':
        record=json.loads(Path(args.record).read_text())
        receipts=json.loads(Path(args.evidence).read_text())
        validate(record,receipts,args.expected_id)
        from .evidence import capture
        source_ids={s['id'] for s in record['sources']}
        # Re-fetch independently of the original collection before publishing.
        verified=[capture(args.expected_id,r['url'],r['kind'],Path('data/verified')) for r in receipts if r['id'] in source_ids]
        validate(record,verified,args.expected_id)
        Path(args.evidence).write_text(json.dumps(verified,ensure_ascii=False,indent=2))
    elif args.command=='publish':
        publish(args.record,args.evidence,args.expected_id)
    else:
        indexes()

if __name__=='__main__':
    main()
