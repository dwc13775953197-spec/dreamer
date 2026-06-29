import json
from datetime import datetime, timezone, timedelta

with open('subconscious.json', 'r') as f:
    subconscious = json.load(f)

tz_cn = timezone(timedelta(hours=8))
now = datetime.now(tz_cn).isoformat()

# New insight 1: Recovery window hypothesis
new_entry = {
    "id": "ins-265-1",
    "type": "insight",
    "content": "恢复窗口假说：能量恢复过程中，精度场(P_t x P_c)的恢复先于执行能力(C)的恢复，产生精度-执行分离窗口。系统能清晰感知目标和位置但无法执行行动，这是A->B->C恢复顺序的直接推论。d(EA)/dt = d(PF)/dt x EC + PF x d(EC)/dt，恢复期两项符号不同导致行动能力恢复滞后于精度恢复。",
    "strength": 5.0,
    "score": 0.5,
    "status": "active",
    "created": now,
    "source": "walk-265",
    "connections": ["ins-255-002", "ins-264-1", "ins-263-1", "ins-254-1", "ins-262-1"],
    "resurrected_count": 0,
    "refs": [],
    "decay_speed": 0.5,
    "note": "quality_score=8.1, initial strength=5.0"
}

subconscious.append(new_entry)

# New interest seeds as hunches
seed1 = {
    "id": "seed-265-1",
    "type": "hunch",
    "content": "恢复窗口的相位检测：通过语言特征(如目标陈述频率/执行陈述频率的比值)判断系统处于哪个恢复阶段",
    "strength": 3.0,
    "score": 0.3,
    "status": "dormant",
    "created": now,
    "source": "walk-265",
    "connections": ["ins-265-1", "ins-263-1"],
    "resurrected_count": 0,
    "refs": [],
    "decay_speed": 0.5,
    "note": "兴趣种子来自walk-265"
}

seed2 = {
    "id": "seed-265-2",
    "type": "hunch",
    "content": "认知疲劳的滞后环量化：每次耗竭-恢复循环在(PF, EC)相空间中画出的不可逆路径包围的面积",
    "strength": 3.0,
    "score": 0.3,
    "status": "dormant",
    "created": now,
    "source": "walk-265",
    "connections": ["ins-265-1", "ins-262-1"],
    "resurrected_count": 0,
    "refs": [],
    "decay_speed": 0.5,
    "note": "兴趣种子来自walk-265"
}

subconscious.append(seed1)
subconscious.append(seed2)

with open('subconscious.json', 'w') as f:
    json.dump(subconscious, f, ensure_ascii=False, indent=2)

print(f"Added 3 entries. Total: {len(subconscious)}")
