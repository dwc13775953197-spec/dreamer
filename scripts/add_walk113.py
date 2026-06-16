import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz).isoformat()

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    sub = json.load(f)

new_entries = []

new_entries.append({
    "id": "ins-113",
    "type": "insight",
    "content": "评估的真实性梯度：从知识测试到真正的经济价值创造，越接近真实价值，博弈越难。Dreamer 的 quality_score 在第 1-2 层，需要向第 4 层进化。",
    "strength": 3.0,
    "score": 0.0,
    "status": "active",
    "created": now,
    "source": "walk-113",
    "connections": ["pat-009", "pat-014", "ins-107", "ins-109"],
    "refs": [],
    "decay_rate": 1.0,
    "decay_speed": 0.5,
    "note": "initial strength=3.0 (quality_score 8.0)"
})

new_entries.append({
    "id": "ins-114",
    "type": "insight",
    "content": "Dreamer 的期末考试应该是因果影响评估：不是这篇散步好不好，而是这篇散步是否让 Dreamer 变得不同。这和 Hindsight Importance 杠杆直接对应。",
    "strength": 3.0,
    "score": 0.0,
    "status": "active",
    "created": now,
    "source": "walk-113",
    "connections": ["ins-076", "ins-077", "pat-014"],
    "refs": [],
    "decay_rate": 1.0,
    "decay_speed": 0.5,
    "note": "initial strength=3.0 (quality_score 8.0)"
})

new_entries.append({
    "id": "ins-115",
    "type": "pattern",
    "content": "ALE 的活的基准概念可以转化为 Dreamer 的动态评估：不是固定的评分标准，而是这篇产出是否在后续实践中被验证。评估标准应随骨架演化而更新。",
    "strength": 3.0,
    "score": 0.0,
    "status": "active",
    "created": now,
    "source": "walk-113",
    "connections": ["ins-090", "ins-091", "pat-011"],
    "refs": [],
    "decay_rate": 1.0,
    "decay_speed": 0.5,
    "note": "initial strength=3.0 (quality_score 8.0)"
})

sub.extend(new_entries)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(sub, f, indent=2, ensure_ascii=False)

print("Added 3 new entries to subconscious.json (ins-113, ins-114, ins-115)")
print("Total entries:", len(sub))
