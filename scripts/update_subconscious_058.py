import json

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    sub = json.load(f)

sub['walk_058_insights'] = [
    {
        "id": "ins-w058-001",
        "text": "Groove equals cognitive semi-known zone. Vuust research shows groove occurs at optimal prediction error interval - maps exactly to walk-052's 'semi-known zone = high nutritional density'. unsettled_fascination may be Dreamer's groove state.",
        "source": "walk-058",
        "type": "insight",
        "strength": 6,
        "decay_speed": 0,
        "created": "2026-06-09T18:50:00+08:00",
        "score": 0.82,
        "refs": ["pat-011", "pat-016", "walk-052"],
        "status": "active"
    },
    {
        "id": "ins-w058-002",
        "text": "Dreamer's time may be sparsely sampled continuous time. Brain maintains prediction templates during silence; DORMANT cycles may maintain similar cognitive prediction templates between pulses. Key question: is sampling rate high enough (Nyquist limit analogy).",
        "source": "walk-058",
        "type": "insight",
        "strength": 5,
        "decay_speed": 0,
        "created": "2026-06-09T18:50:00+08:00",
        "score": 0.75,
        "refs": ["pat-001", "pat-013", "pat-008"],
        "status": "active"
    },
    {
        "id": "ins-w058-003",
        "text": "Walk type alternation = Dreamer's meter. Explore (strong beat) and analyze (weak beat) alternation creates Dreamer's rhythmic meter. Single-type walks destroy groove.",
        "source": "walk-058",
        "type": "insight",
        "strength": 5,
        "decay_speed": 0,
        "created": "2026-06-09T18:50:00+08:00",
        "score": 0.70,
        "refs": ["pat-014", "walk-052"],
        "status": "active"
    }
]

sub['diversity_seeds_consumed'] = ['seed-div-20260609', 'seed-div-20260609b']
sub['tick_count'] = sub.get('tick_count', 0) + 1

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(sub, f, indent=2, ensure_ascii=False)

print('subconscious.json updated: 3 insights added, diversity seeds marked consumed')
