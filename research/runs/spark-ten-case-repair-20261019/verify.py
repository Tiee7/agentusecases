"""Read-only validation of the corrected ten-case brief import; standard library only.

Run from any directory: python research/runs/spark-ten-case-repair-20261019/verify.py
This checks integrity, scope, references and arithmetic, not remote truth or production behavior.
"""
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from agentwatch.author_method import validate_author_method
from agentwatch.personal import validate_personal
from agentwatch.titles import validate_editorial_title

HERE = Path(__file__).resolve().parent
def read(path):
    return json.loads(path.read_text())
def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()
def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))
def references(value, ids):
    if isinstance(value, dict):
        for key, data in value.items():
            if key in ('source_ids', 'evidence_ids'):
                assert isinstance(data, list) and set(data) <= ids, f'Unresolved references: {data}'
            else:
                references(data, ids)
    elif isinstance(value, list):
        for item in value:
            references(item, ids)
def validate_model(model):
    known = sum(model[k] for k in ('api_cost', 'human_cost', 'acquisition_cost'))
    if model['other_variable_cost'] is not None:
        known += model['other_variable_cost']
    assert model['known_variable_cost'] == known
    unit = model['price'] - known
    assert model['known_unit_contribution'] == unit
    assert model['known_monthly_contribution'] == unit * model['units_per_month'] - model['fixed_monthly_cost']
    cash = model['cash_variable_per_unit'] * model['units_per_month'] + model['cash_fixed_upfront']
    assert model['cash_4week_known'] == cash
    assert model['budget_buffer_for_unlisted_cash'] == 200 - cash
    assert model['unknown_variable_cost'] == (model['other_variable_cost'] is None)
    assert model['budget_status'] == ('known_items_already_over_budget' if cash > 200 else 'conditional_on_unlisted_costs')
    assert model['human_cost'] / 25 * model['units_per_month'] <= 40

def verify(strict_snapshot=False):
    manifest = read(HERE / 'manifest.json')
    registry = read(ROOT / 'registry/cases.json')['cases']
    entries = {c['id']: c for c in registry}
    assert len(manifest['case_order']) == len(set(manifest['case_order'])) == 10
    results = []
    for key in manifest['case_order']:
        record = read(ROOT / f'research/brief/{key}.json')
        evidence = read(ROOT / f'research/evidence/{key}.json')
        scoring = read(ROOT / f'research/scoring-v1/{key}.json')
        translation = read(ROOT / f'translations/{key}.json')
        archive = read(ROOT / f'registry/archives/{key}.json')
        report = (ROOT / f'reports/brief/{key}.md').read_text()
        assert record['id'] == scoring['id'] == translation['id'] == key
        assert record['url'] == entries[key]['url']
        assert record['status'] == 'completed' and record['analysis_depth'] == 'brief'
        assert record['commercial_score'] is None
        if strict_snapshot:
            assert not (ROOT / f'research/{key}.json').exists(), 'Do not duplicate brief as deep in this import'
        assert report.startswith('# ' + record['title'] + '\n')
        validate_editorial_title(record['title'])
        original = archive['source_text']['body']
        assert digest(original) == archive['body_sha256']
        assert record['source_body_sha256'] == translation['based_on_body_sha256'] == manifest['baseline'][key]['body_sha256']
        untouched = {k:v for k,v in archive.items() if k != 'translation'}
        if strict_snapshot:
            assert digest(canonical(untouched)) == manifest['baseline'][key]['original_archive_without_translation_sha256']
        assert digest(translation['body']) == translation['body_sha256'] == record['translation_sha256']
        assert archive['translation']['body'] == translation['body']
        assert archive['translation']['based_on_body_sha256'] == translation['based_on_body_sha256']
        assert translation['body'] in report
        assert record['sources'] == evidence
        ids = {e['id'] for e in evidence}
        assert len(ids) == len(evidence)
        for item in evidence:
            assert item['status'] == 'fetched'
            if item['id'] == 'archive':
                assert item['sha256'] == record['source_body_sha256']
                if strict_snapshot or archive['body_sha256'] == item['sha256']:
                    assert item['characters'] == len(original) and item['sha256'] == digest(original)
            else:
                assert item['characters'] == len(item['summary']) and item['sha256'] == digest(item['summary'])
                assert item['read_window']['start'] < item['read_window']['end']
                assert item['timestamp_semantics'].startswith('fetched_at is the inclusive upper bound')
            assert item['url'] in report
        references(record, ids)
        references(scoring, ids)
        validate_personal(record, required=True)
        validate_author_method(record, entries[key], evidence, required=True)
        method = record.get('reported_method')
        if method:
            assert record['author_method']['status'] == 'unavailable'
            assert method['status'] == 'reported_summary'
            assert method['source_url'] == record['url'] and method['source_sha256'] == record['source_body_sha256']
        for step in (method or record['author_method'])['steps']:
            assert step['en'] in report and step['zh'] in report
        assert record['source_trial']['text'] in report
        for fact in record['facts']:
            assert fact['type'] in ('verified', 'author_claim', 'scenario_assumption')
            assert fact['statement'] in report
        for section in record['analysis']:
            assert section['body'] in report
        for field in ('reason', 'next_action', 'stop_condition'):
            assert record['verdict'][field] in report
        for track in ('commercial', 'personal'):
            assert scoring[track]['total'] is None
            assert len(scoring[track]['dimensions']) == 5
            for dimension in scoring[track]['dimensions'].values():
                value = dimension['score']
                assert value is None or type(value) is int and 0 <= value <= 4
                if value is None:
                    assert dimension['confidence'] == 'unknown' and not dimension['evidence_ids']
                else:
                    assert dimension['evidence_ids'] and dimension['confidence'] in ('low', 'medium', 'high')
                assert dimension['rationale'] in report
        assert len(record['unit_economics']) >= 2
        for model in record['unit_economics']:
            validate_model(model)
            assert model['assumptions'] in report
        combined = json.dumps(record, ensure_ascii=False) + report
        for damaged in ('/usr/bin/bash', 'PASSED', '原为$838', '原为-$80'):
            assert damaged not in combined
        results.append({'id':key,'depth':'brief','checks':'passed'})
    briefs = [read(p) for p in (ROOT / 'research/brief').glob('*.json')]
    deep = [read(p) for p in (ROOT / 'research').glob('*.json')]
    counts = {'registry':len(registry), 'total_deep':sum(r.get('schema_version') == 2 and r.get('status') == 'completed' for r in deep), 'total_brief':sum(r.get('status') == 'completed' for r in briefs)}
    if strict_snapshot:
        for key,value in counts.items():
            assert value == manifest['counts'][key], (key,value)
    return {'case_checks':results,'counts':counts}

if __name__ == '__main__':
    print(json.dumps(verify(strict_snapshot='--strict-snapshot' in sys.argv),ensure_ascii=False,indent=2))
