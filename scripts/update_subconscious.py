import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz).isoformat()

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    sub = json.load(f)

entries = sub.get('entries', [])

entries.append({
    'id': 'ins-160',
    'type': 'insight',
    'source': 'research-003',
    'created': now,
    'strength': 7,
    'pattern_id': 'pat-030',
    'content': 'Coverage decay in conformal prediction is O(1/sqrt(n)) polynomial, not exponential. Based on DKW inequality, not thermodynamics. Marginal returns are gentle (4x budget for 4% coverage gain), not catastrophic.',
    'refs': ['research-003', 'walk-051']
})

entries.append({
    'id': 'ins-161',
    'type': 'insight',
    'source': 'research-003',
    'created': now,
    'strength': 8,
    'pattern_id': 'pat-029',
    'content': 'UQ(B) = UQ_inf*(1-C/sqrt(B)) + kTln2*H_discard + UQ_structural. Four-term decomposition: asymptotic (theoretical limit), budget (improvable), thermodynamic (info-discard cost), structural (irreducible = pat-029 intrinsic uncertainty). Intrinsic = structural + thermodynamic, not a single quantity.',
    'refs': ['research-003', 'walk-043', 'walk-051']
})

entries.append({
    'id': 'ins-162',
    'type': 'insight',
    'source': 'research-003',
    'created': now,
    'strength': 6,
    'pattern_id': 'pat-014',
    'content': 'Evaluation thermodynamic cost = kTln2 * H_discard (Shannon entropy discarded). Reversible ops (read, compare) have near-zero energy cost; irreversible ops (write, sort, vote) are Landauer-bound. Mature evaluation = minimize info-discard = reduce H_discard. This is pat-014 rhythm-maturation operationalized for evaluation.',
    'refs': ['research-003']
})

sub['entries'] = entries

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(sub, f, ensure_ascii=False, indent=2)

print('Done: ins-160, ins-161, ins-162 added')
