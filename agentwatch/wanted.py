"""Visible Wanted counts and translation queues; unknown is never zero."""
import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path


def parse_button(text):
    text = ' '.join(text.split())
    number = r'(?:0|[1-9][0-9]*|[1-9][0-9]{0,2}(?:,[0-9]{3})+)'
    match = re.fullmatch(r'I want this\s+(?:·\s*)?(?:(' + number + r')|\((' + number + r')\))', text)
    return int((match[1] or match[2]).replace(',', '')) if match else None


def translation_queue(root):
    from .archive import sha
    observed, unknown = [], []
    total = translated = 0
    for path in sorted(Path(root).glob('*.json')):
        archive = json.loads(path.read_text())
        total += 1
        translation = archive.get('translation', {})
        if (translation.get('status') == 'available'
                and translation.get('format') == 'full_extracted_text_translation'
                and translation.get('language') == 'zh-CN'
                and translation.get('based_on_body_sha256') == archive.get('body_sha256')
                and translation.get('body')
                and translation.get('body_sha256') == sha(translation['body'])):
            translated += 1
            continue
        field = archive.get('fields', {}).get('wanted', {})
        value = field.get('value')
        at = field.get('observed_at') or archive.get('observed_at')
        valid = field.get('status') == 'observed' and type(value) is int and value >= 0 and bool(at)
        row = {'id': path.stem, 'wanted': value if valid else None,
               'wanted_observed_at': at if valid else None}
        (observed if valid else unknown).append(row)
    observed.sort(key=lambda row: (-row['wanted'], row['id']))
    for index, row in enumerate(observed, 1):
        row.update(rank=index, group='A' if index % 2 else 'B')
    for index, row in enumerate(unknown, 1):
        row.update(provisional_position=index, provisional_group='A' if index % 2 else 'B')
    return {'version': 1, 'generated_at': datetime.now(timezone.utc).isoformat(),
            'archive_count': total, 'translated_count': translated,
            'ordering': 'Observed Wanted descending, ties by slug. Unknown entries remain unranked.',
            'grouping': 'A odd / B even. Unknown slug order and groups are provisional, not Wanted ranks.',
            'wanted_ranked': observed, 'unknown_unranked': unknown}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--archives', type=Path, default=Path('registry/archives'))
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = translation_queue(args.archives)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({key: value for key, value in result.items() if key not in ('wanted_ranked', 'unknown_unranked')}, ensure_ascii=False))
    print(f"Ranked: {len(result['wanted_ranked'])}; unknown: {len(result['unknown_unranked'])}")


if __name__ == '__main__':
    main()
