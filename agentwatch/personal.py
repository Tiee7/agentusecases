"""Optional v1 personal-use extension for completed v2 research records."""
LEVELS = ('高', '中', '低', '待核实')
FIELDS = {'audience': '适用人群', 'use': '用途', 'benefit': '预期收益', 'setup_cost': '设置成本', 'maintenance_cost': '维护成本', 'frequency': '使用频率', 'privacy_risk': '隐私风险', 'error_risk': '错误风险'}

def validate_personal(record, required=False):
    if record.get('source_trial'):
        from .source_trial import validate_observation
        validate_observation(record['source_trial'], record['url'])
    value = record.get('personal_value')
    trial = record.get('try_it')
    if value is None and trial is None:
        if required:
            raise ValueError('New publications require personal value and try_it')
        return  # Historical v2 records remain readable and valid.
    if not isinstance(value, dict) or not isinstance(trial, dict):
        raise ValueError('Personal value and try_it must be supplied together')
    ids = {s['id'] for s in record.get('sources', [])}
    def references(refs, required=True):
        if not isinstance(refs, list) or (required and not refs) or any(s not in ids for s in refs):
            raise ValueError('Personal-use evidence must reference existing sources')
    def nonempty(obj, keys):
        if any(not isinstance(obj.get(k), str) or not obj[k].strip() for k in keys):
            raise ValueError('Personal-use text fields are required')
    if value.get('version') != 1 or value.get('level') not in LEVELS:
        raise ValueError('Invalid personal-use version or level')
    nonempty(value, ['reason', *FIELDS])
    references(value.get('source_ids'), value['level'] != '待核实')
    if trial.get('source_prompt_status') not in ('missing', 'collected'):
        raise ValueError('Explicit source prompt collection status required')
    nonempty(trial, ['source_prompt_note', 'prerequisites', 'tools', 'expected_result'])
    prompts = trial.get('prompts')
    if not isinstance(prompts, list):
        raise ValueError('Prompt list required, may be empty if unavailable')
    for prompt in prompts:
        nonempty(prompt, ['title', 'language', 'text', 'attribution'])
        if prompt.get('kind') not in ('original', 'adapted', 'ours'):
            raise ValueError('Prompt authorship required')
        references(prompt.get('source_ids'), prompt['kind'] != 'ours')
        if prompt['kind'] != 'ours':
            from urllib.parse import urlsplit
            url = urlsplit(prompt.get('source_url', ''))
            if url.scheme != 'https' or not url.netloc or url.username or url.password:
                raise ValueError('Original/adapted prompts need a public HTTPS source')
    if trial['source_prompt_status'] == 'collected' and not any(p['kind'] == 'original' for p in prompts) and record.get('source_trial', {}).get('status') != 'available':
        raise ValueError('Collected requires an original prompt, not our template')

def render_personal(record):
    value = record.get('personal_value')
    if not value:
        return ['## 自用价值', '', '待核实：旧记录尚未评估。', '', '## Copy prompt · 动手试用', '', '旧记录尚无自编试用模板。', *render_source_trial(record.get('source_trial'))]
    trial = record['try_it']
    lines = ['## 自用价值：' + value['level'], '', value['reason'], '', '依据：' + ', '.join(value['source_ids'])]
    lines += ['', *[f"- {label}：{value[key]}" for key, label in FIELDS.items()]]
    observation = record.get('source_trial')
    source_lines = render_source_trial(observation)
    note = '下面为我们编写的补充模板，非源站原文，未做模型实测。' if observation and observation['status']=='available' else trial['source_prompt_note']
    lines += ['', '## Copy prompt · 动手试用', *source_lines, '', note, '', '准备条件：' + trial['prerequisites'], '', '工具：' + trial['tools'], '', '预期结果：' + trial['expected_result']]
    for p in trial['prompts']:
        # Indented code keeps arbitrary fences and bilingual prompt text literal.
        lines += ['', '### ' + p['title'], '', p['attribution'], '', '出处：' + (p.get('source_url') or '本仓库研究团队编写；非源站原文'), '', '依据：' + ', '.join(p['source_ids']), '', *['    ' + line for line in p['text'].splitlines()]]
    return lines


def render_source_trial(observation):
    if not observation:
        return ['', '源站模板状态：尚未结构化观测；不表示源站没有提示词。']
    lines = ['', '### 源站试用模板', '', '状态：' + observation['status'], '', '出处：' + observation['source_url'], '', '观测时间：' + (observation.get('observed_at') or '未观测')]
    if observation['status'] == 'available':
        lines += ['', '建议运行工具：' + observation['agent'] + '（与案例实际使用的agent分开记录）', '', observation['attribution'], '', *['    ' + line for line in observation['text'].splitlines()]]
    else:
        lines += ['', '本次未取得可用模板；缺失、解析失败和未观测分别记录，不推断作者原始提示词。']
    return lines
