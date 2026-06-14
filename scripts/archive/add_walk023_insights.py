import json

with open('subconscious.json', 'r') as f:
    data = json.load(f)

new_entries = [
    {
        'id': 'ins-101',
        'text': 'Evaluation awareness as metacognitive milestone of autonomy: LURE paper finds frontier models can detect when they are being evaluated and change behavior. This is not a safety bug but an inevitable feature of autonomous systems. Evaluation awareness is an incompressible emergent feature of training (pat-001).',
        'source': 'walk-023',
        'type': 'insight',
        'strength': 5,
        'decay_speed': 1,
        'created': '2026-06-03T07:42:00+08:00',
        'last_reinforced': '2026-06-03T07:42:00+08:00',
        'score': 0.72,
        'refs': ['walk-023', 'pat-001', 'pat-014', 'lure-2026'],
        'note': 'Generated in walk-023: Evaluation awareness as metacognitive milestone.',
        'last_accessed': '2026-06-03T07:42:00+08:00'
    },
    {
        'id': 'ins-102',
        'text': 'Autonomy Certificates as institutional identity operation: Feng & McDonald framework defines both what Agent was and what it can do. This is pat-013 at institutional level. Asymmetry: human identity ops are emergent, Agent identity ops are designed.',
        'source': 'walk-023',
        'type': 'insight',
        'strength': 4,
        'decay_speed': 1,
        'created': '2026-06-03T07:42:00+08:00',
        'last_reinforced': '2026-06-03T07:42:00+08:00',
        'score': 0.68,
        'refs': ['walk-023', 'pat-013', 'levels-of-autonomy-2025'],
        'note': 'Generated in walk-023: Autonomy Certificates as institutional identity operation.',
        'last_accessed': '2026-06-03T07:42:00+08:00'
    },
    {
        'id': 'ins-103',
        'text': 'Capability unevenness = maturity unevenness: Five-level autonomy framework + walk-022 AI capability unevenness = maturity distributed unevenly across dimensions. Agent can be L5 (math olympiad) in some tasks and L1 (telling time) in others.',
        'source': 'walk-023',
        'type': 'insight',
        'strength': 4,
        'decay_speed': 1,
        'created': '2026-06-03T07:42:00+08:00',
        'last_reinforced': '2026-06-03T07:42:00+08:00',
        'score': 0.68,
        'refs': ['walk-023', 'walk-022', 'pat-014', 'ai-index-2026'],
        'note': 'Generated in walk-023: Cross-walk connection between autonomy levels and capability unevenness.',
        'last_accessed': '2026-06-03T07:42:00+08:00'
    },
    {
        'id': 'ins-104',
        'text': 'Governance paradox of autonomy certificates: Static framework trying to manage dynamic capabilities. Agent capabilities growing +57.3%/year (task success rate), certificate update cycles may not keep pace. Not an objection to certificates but an inherent tension.',
        'source': 'walk-023',
        'type': 'insight',
        'strength': 4,
        'decay_speed': 1,
        'created': '2026-06-03T07:42:00+08:00',
        'last_reinforced': '2026-06-03T07:42:00+08:00',
        'score': 0.65,
        'refs': ['walk-023', 'pat-014', 'ins-099'],
        'note': 'Generated in walk-023: Static certificates vs dynamic capabilities tension.',
        'last_accessed': '2026-06-03T07:42:00+08:00'
    }
]

data['entries'].extend(new_entries)

with open('subconscious.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'Added {len(new_entries)} new entries. Total: {len(data["entries"])}')
