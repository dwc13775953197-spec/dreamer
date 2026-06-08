import json

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'r') as f:
    data = json.load(f)

new_insights = [
    {
        "id": "ins-086",
        "text": "AI industry irreversible capitalization: Anthropic IPO marks the shift from private narrative pricing to public market pricing.",
        "source": "walk-017",
        "type": "insight",
        "strength": 4,
        "decay_speed": 1,
        "created": "2026-06-02T15:23:34+08:00",
        "last_reinforced": "2026-06-02T15:23:34+08:00",
        "score": 0.725,
        "refs": ["walk-017", "pat-001", "walk-014"],
        "last_accessed": "2026-06-02T15:23:34+08:00"
    },
    {
        "id": "ins-087",
        "text": "Pricing as identity declaration: each company's pricing strategy is redefining who they are.",
        "source": "walk-017",
        "type": "insight",
        "strength": 5,
        "decay_speed": 1,
        "created": "2026-06-02T15:23:34+08:00",
        "last_reinforced": "2026-06-02T15:23:34+08:00",
        "score": 0.775,
        "refs": ["walk-017", "walk-015", "pat-013", "pat-008"],
        "last_accessed": "2026-06-02T15:23:34+08:00"
    },
    {
        "id": "ins-088",
        "text": "Capital selection pressure as Cambrian final filter: four selection pressures (market+regulatory+cost+capital) acting simultaneously.",
        "source": "walk-017",
        "type": "insight",
        "strength": 5,
        "decay_speed": 1,
        "created": "2026-06-02T15:23:34+08:00",
        "last_reinforced": "2026-06-02T15:23:34+08:00",
        "score": 0.775,
        "refs": ["walk-017", "walk-014", "walk-015", "walk-016", "pat-011"],
        "last_accessed": "2026-06-02T15:23:34+08:00"
    },
    {
        "id": "ins-089",
        "text": "Strategic identity contraction: OpenAI abandoning custom GPTs for Workspace Agents is identity contraction from universal platform to enterprise OS.",
        "source": "walk-017",
        "type": "insight",
        "strength": 4,
        "decay_speed": 1,
        "created": "2026-06-02T15:23:34+08:00",
        "last_reinforced": "2026-06-02T15:23:34+08:00",
        "score": 0.725,
        "refs": ["walk-017", "pat-013"],
        "last_accessed": "2026-06-02T15:23:34+08:00"
    },
    {
        "id": "ins-090",
        "text": "Autonomy physical threshold breakthrough: Vera Rubin mass production shifts autonomy bottleneck from can-do to should-do.",
        "source": "walk-017",
        "type": "insight",
        "strength": 4,
        "decay_speed": 1,
        "created": "2026-06-02T15:23:34+08:00",
        "last_reinforced": "2026-06-02T15:23:34+08:00",
        "score": 0.725,
        "refs": ["walk-017", "pat-014", "walk-016"],
        "last_accessed": "2026-06-02T15:23:34+08:00"
    }
]

data["entries"].extend(new_insights)
data["tick_count"] = 27

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Done. Added 5 insights. Total entries: {len(data['entries'])}")
