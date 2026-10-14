"""Create a readable change digest from a successful crawl, without false deletions."""
import argparse
import json
import sqlite3
from datetime import datetime
from zoneinfo import ZoneInfo
from collections import Counter
from pathlib import Path

def render(result):
    catalog=result.get('catalog') or {}
    cases=result['cases']
    counts=Counter(row['change'] for row in cases)
    lines=['# 案例变化日报', '', f"快照：{result['run_id']} · 时间：{result.get('fetched_at','见SQLite批次记录')}", '', f"目录：{catalog.get('count','未知')}个；详情采集：{len(cases)}个；全量详情完成：{'是' if result.get('details_complete') else '否'}。", '', '目录移出仅表示sitemap不再列出，不证明案例被删除；lastmod只是网站声明的更新时间。', '']
    if catalog.get('baseline'):
        lines.append('本次建立目录基线，不将现有案例计为新增。')
    else:
        lines.append(f"目录新增 {len(catalog.get('newly_listed',[]))}；目录移出 {len(catalog.get('no_longer_listed',[]))}；lastmod变化 {len(catalog.get('lastmod_changed',[]))}。")
    lines += ['', f"正文/标题/来源变化 {counts['content_changed']}；采集位置变化 {counts['position_changed']}；已验证未变 {counts['unchanged']}；新观察到详情 {counts['newly_observed']}；详情基线 {counts['baseline']}。", '']
    labels={'newly_listed':'目录新增','no_longer_listed':'目录移出','lastmod_changed':'网站声明的更新时间变化'}
    for key,label in labels.items():
        urls=catalog.get(key,[])
        if urls:
            lines += [f'## {label}', ''] + [f'- {url}' for url in urls[:50]]
            if len(urls)>50:
                lines.append(f'- 另有{len(urls)-50}条，完整列表见对应JSON快照。')
            lines.append('')
    changed=[row for row in cases if row['change'] in ('content_changed','position_changed','newly_observed')]
    if changed:
        lines += ['## 已采集详情的变化', '']
        for row in changed[:50]:
            title=row['title'].replace('[','\\[').replace(']','\\]')
            lines.append(f"- [{title}]({row['url']})：{row['change']}")
        if len(changed)>50:
            lines.append(f'- 另有{len(changed)-50}条，完整列表见对应JSON快照。')
    lines += ['', '排序位置是本采集序列的位置，不是全站统一热门榜。未采集的正文不能声称没有变化。']
    return '\n'.join(lines)+'\n'

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--snapshot')
    parser.add_argument('--db',default='data/history.sqlite3')
    parser.add_argument('--output',default='data/daily-report.md')
    args=parser.parse_args()
    path=Path(args.snapshot) if args.snapshot else max(Path('data/runs').glob('*.json'),key=lambda p:int(p.stem))
    result=json.loads(path.read_text())
    if not result.get('fetched_at') and Path(args.db).exists():
        db=sqlite3.connect(f'file:{Path(args.db).resolve()}?mode=ro',uri=True)
        row=db.execute('SELECT fetched_at FROM runs WHERE id=?',(result['run_id'],)).fetchone()
        if row:
            result['fetched_at']=datetime.fromisoformat(row[0]).astimezone(ZoneInfo('Asia/Shanghai')).isoformat()+' (北京时间)'
        db.close()
    output=Path(args.output)
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(render(result))

if __name__=='__main__':
    main()
