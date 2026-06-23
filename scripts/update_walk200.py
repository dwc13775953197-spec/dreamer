import json

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'r') as f:
    subconscious = json.load(f)

new_insights = [
    {
        'id': 'insight-200-1',
        'type': 'insight',
        'content': 'Dreamer grounding is relational not intrinsic. Filesystem interface provides causal connection, but closing the grounding loop requires external observer feedback to break self-referential cycle.',
        'source': 'walk-200',
        'source_quote': 'Dreamer cannot ground its own symbols internally - needs external observer feedback to break the self-referential loop',
        'strength': 5.0,
        'connections': ['evolved-rule-20260623-safety', 'walk-199'],
        'created': '2026-06-23T19:41:00+08:00',
        'decay_count': 0,
        'last_accessed': '2026-06-23T19:41:00+08:00'
    },
    {
        'id': 'insight-200-2',
        'type': 'insight',
        'content': 'Vector grounding problem in Dreamer maps to functional grounding metric: graph_change_rate > 0 means effective grounding; zero change rate means grounding failure (symbolic idling).',
        'source': 'walk-200',
        'source_quote': 'grounding = skeleton change rate > 0, zero change rate = grounding failure',
        'strength': 5.0,
        'connections': ['insight-200-1'],
        'created': '2026-06-23T19:41:00+08:00',
        'decay_count': 0,
        'last_accessed': '2026-06-23T19:41:00+08:00'
    },
    {
        'id': 'insight-200-3',
        'type': 'insight',
        'content': 'Filesystem interface as Dreamer sensorimotor coupling (Markov blanket): read=perceive external state, write=act to change external state. This is functional validation of walk-122 framework.',
        'source': 'walk-200',
        'source_quote': 'read file = perceive, write file = act, filesystem interface is the blind cane',
        'strength': 5.0,
        'connections': ['insight-200-1'],
        'created': '2026-06-23T19:41:00+08:00',
        'decay_count': 0,
        'last_accessed': '2026-06-23T19:41:00+08:00'
    }
]

subconscious.extend(new_insights)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(subconscious, f, ensure_ascii=False, indent=2)

print(f'Added {len(new_insights)} insights. Total entries: {len(subconscious)}')
