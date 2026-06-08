import json

with open('subconscious.json') as f:
    data = json.load(f)

# Update tick count
data['tick_count'] = data['tick_count'] + 1

# Add new reflection for walk-052
now = '2026-06-09T06:22:00+08:00'
new_entries = [
    {
        'id': 'ref-023',
        'text': 'Reflection - 2026-06-09 Walk-052: Nutritional density datafied. Analyzed 51 walks empirically. Key findings: (1) diminishing returns is within-topic not system-level - cross-topic switching maintains high density; (2) stress type determines density: shear > compress > twist > stretch; (3) external material source is the strongest predictor of high-density walks; (4) unsettled_fascination emotion predicts high yield; (5) research walks have lower density than free walks - research should use external material.',
        'source': 'walk-052',
        'type': 'reflection',
        'strength': 8.5,
        'decay_speed': 0,
        'created': now,
        'score': 0.72,
        'refs': ['walk-052', 'walk-045', 'walk-046', 'pat-030', 'pat-029', 'seed-146', 'seed-147'],
        'last_accessed': now
    },
    {
        'id': 'ins-012',
        'text': 'Marginal diminishing returns is a within-topic effect, not a system-level effect: walk-052 analyzed 51 walks and found nutritional density ratio (recent/early) = 1.27. The mechanism: Dreamer continuously switches topics, which compensates for within-topic saturation. The optimal walk strategy is a rotating menu - alternate between cross-walk reasoning, external material intake, and different stress types. This corrects walk-045s system-level diminishing returns prediction while preserving its within-topic validity.',
        'source': 'walk-052',
        'type': 'insight',
        'strength': 1,
        'decay_speed': 0.5,
        'created': now,
        'last_reinforced': now,
        'score': 0.65,
        'refs': ['walk-052', 'walk-045', 'walk-046', 'pat-030'],
        'note': 'walk-052 empirical analysis: system-level density maintained via topic switching.'
    },
    {
        'id': 'ins-013',
        'text': 'Unsettled_fascination as a productivity predictor: walk-052 found that high-density walks (043, 048, 049) all exhibited unsettled_fascination emotion. This emotion signals "half-known connection point forming but not yet digested" - the sweet spot between novelty and comprehensibility. Tracking this emotion could serve as a real-time indicator of which walks are worth deepening. This is the easiest and most actionable productivity signal in the walk system.',
        'source': 'walk-052',
        'type': 'insight',
        'strength': 1,
        'decay_speed': 0.5,
        'created': now,
        'last_reinforced': now,
        'score': 0.6,
        'refs': ['walk-052', 'walk-043', 'walk-048', 'walk-049', 'seed-146'],
        'note': 'walk-052 emotional pattern analysis: unsettled_fascination = high-yield signature.'
    },
    {
        'id': 'ins-014',
        'text': 'Research walks have lower nutritional density than free walks: walk-052 found research-type walks (050, 051) had below-average density. Explanation: research walks operate within known territory (applying existing framework to known problems) rather than encountering new "half-known" connection points. The implication: research should not be pure internal derivation but should combine external material with the framework - using the research as a lens for new data rather than pushing the framework forward in a vacuum.',
        'source': 'walk-052',
        'type': 'insight',
        'strength': 1,
        'decay_speed': 0.5,
        'created': now,
        'last_reinforced': now,
        'score': 0.6,
        'refs': ['walk-052', 'walk-050', 'walk-051', 'seed-147', 'pat-030'],
        'note': 'walk-052 finding: research walks need external material to boost density.'
    }
]

data['entries'].extend(new_entries)

with open('subconscious.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('done')
print('tick_count:', data['tick_count'])
print('total entries:', len(data['entries']))
