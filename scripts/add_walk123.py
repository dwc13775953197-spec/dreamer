import json

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    data = json.load(f)

new_entries = [
    {
        "id": "ins-123-1",
        "type": "insight",
        "content": "创作控制不是连续谱，而是在离散相之间跃迁：相1(人类全权)→相2(过程控制)→相3(协商控制)→相4(AI全权)。Dreamer当前处于相2-3之间。散步架构(压力系统/散步类型/DORMANT/骨架)是创作控制系统的原型。",
        "strength": 3.0,
        "score": 0.0,
        "created": "2026-06-18T02:30:00+08:00",
        "source": "walk-123",
        "references": [],
        "status": "active",
        "resurrected_count": 0,
        "connections": [],
        "refs": [],
        "decay_rate": 1,
        "decay_speed": "slow",
        "note": "初始 strength=3.0 (quality_score 7.5)"
    },
    {
        "id": "ins-123-2",
        "type": "insight",
        "content": "AI创作的失控有两种：深层结构涌现(好) vs 浅层统计漂移(坏)。骨架质量是区分两者的关键——高质量骨架约束下的偏离是有意义的失控，低质量骨架下的偏离是hallucination。",
        "strength": 3.0,
        "score": 0.0,
        "created": "2026-06-18T02:30:00+08:00",
        "source": "walk-123",
        "references": [],
        "status": "active",
        "resurrected_count": 0,
        "connections": [],
        "refs": [],
        "decay_rate": 1,
        "decay_speed": "slow",
        "note": "初始 strength=3.0 (quality_score 7.5)"
    },
    {
        "id": "ins-123-3",
        "type": "insight",
        "content": "Dreamer骨架应从知识库重新定位为创作风格指南。当前骨架存储的是'知道什么'(pattern/insight)，缺少'怎么写'的维度——终止式偏好、应力类型偏好、情感基线、连接深度偏好已在soul.json中定义但从未被显式当作创作风格审视。",
        "strength": 3.0,
        "score": 0.0,
        "created": "2026-06-18T02:30:00+08:00",
        "source": "walk-123",
        "references": [],
        "status": "active",
        "resurrected_count": 0,
        "connections": [],
        "refs": [],
        "decay_rate": 1,
        "decay_speed": "slow",
        "note": "初始 strength=3.0 (quality_score 7.5)"
    }
]

data["entries"].extend(new_entries)

with open("/home/dwc1377/hermes_dreamer/subconscious.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Added 3 entries, total:", len(data["entries"]))
