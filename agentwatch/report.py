"""Render auditable research records; incomplete evidence never gets a total score."""
import argparse
import json
from pathlib import Path

WEIGHTS = {'value': 25, 'evidence': 25, 'feasibility': 20, 'economics': 15, 'risk_control': 15}
LABELS = {'value': '需求价值', 'evidence': '效果证据', 'feasibility': '落地可行性', 'economics': '成本与维护', 'risk_control': '风险控制'}

def render(record):
    from .titles import validate_editorial_title
    title = record['title']
    validate_editorial_title(title)
    url = record['url']
    lines = [f'# {title}', '', f'案例来源：{url}', f"研究日期：{record['researched_at']}", f"状态：{record.get('status', 'pending')} · 证据置信度：{record.get('confidence', '未标注')}", '', record.get('evidence_scope', ''), '', record['summary'], '', '| 维度 | 权重 | 分数（0–5） | 依据 |', '|---|---:|---:|---|']
    total = 0
    complete = True
    dimensions = record.get('dimensions', {})
    for key, weight in WEIGHTS.items():
        item = dimensions.get(key, {})
        score = item.get('score')
        sources = item.get('sources', [])
        rationale = item.get('rationale', '').strip()
        if score is None:
            complete = False
            display = '待研究'
        else:
            if isinstance(score, bool) or not isinstance(score, (int, float)) or not 0 <= score <= 5:
                raise ValueError(f'{key}: score must be between 0 and 5')
            if not sources or not rationale:
                raise ValueError(f'{key}: rated dimensions require rationale and sources')
            if any(not s.startswith('https://') for s in sources):
                raise ValueError('Sources must be HTTPS URLs')
            total += weight * score / 5
            display = str(score)
        evidence = (rationale + ' ' + ' '.join(sources)).replace('|', '\\|').replace('\n', ' ')
        lines.append(f'| {LABELS[key]} | {weight}% | {display} | {evidence or "证据不足"} |')
    lines += ['', f'综合评分：{total:.1f}/100' if complete else '综合评分：暂不计算（研究或证据未完成）', '', '## 分析与建议', '', record.get('recommendation', '待研究'), '', '## 待验证问题', '']
    lines += [f'- {q}' for q in record.get('open_questions', [])]
    lines += ['', '## 下一步实验', '', record.get('next_experiment', '待制定')]
    lines += ['', '## 来源核验', '']
    for source in record.get('source_checks', []):
        lines.append(f"- {source['url']}：{source['status']}")
    return '\n'.join(lines) + '\n'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('record')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    record = json.loads(Path(args.record).read_text())
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render(record))

if __name__ == '__main__':
    main()
