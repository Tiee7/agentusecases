"""Recompute public V1 balance changes offline; never execute trading code."""
import csv
import hashlib
import json
import sys
from pathlib import Path

path = Path(sys.argv[1])
rows = list(csv.DictReader(path.open()))
rows = [r for r in rows if r['Date'] <= '2026-03-31']
assert rows and rows[0]['Date'] == '2026-01-05' and rows[-1]['Date'] == '2026-03-31'
assert len({r['Date'] for r in rows}) == len(rows)
result = {'source_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
          'source_commit': '08169121c677e8f0738d03fc321751ed85fb7a16',
          'start': rows[0]['Date'], 'end': rows[-1]['Date'], 'rows': len(rows),
          'method': 'Last logged balance divided by first balance minus one. No independent account audit or cash-flow adjustment.',
          'portfolios': {}}
for name in ('ChatGPT', 'Gemini', 'Claude', 'Perplexity', 'SP500'):
    values = [float(r[name]) for r in rows]
    high, drawdown = values[0], 0
    for value in values:
        high = max(high, value)
        drawdown = min(drawdown, value / high - 1)
    result['portfolios'][name] = {'initial': values[0], 'ending': values[-1],
                                 'balance_change_percent': round((values[-1] / values[0] - 1) * 100, 4),
                                 'max_drawdown_on_logged_dates_percent': round(drawdown * 100, 4)}
models = ['ChatGPT', 'Gemini', 'Claude', 'Perplexity']
result['combined_models'] = {'initial': sum(float(rows[0][x]) for x in models),
                             'ending': round(sum(float(rows[-1][x]) for x in models), 2)}
result['combined_models']['balance_change_percent'] = round((result['combined_models']['ending']/result['combined_models']['initial']-1)*100, 4)
print(json.dumps(result, indent=2))
