import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz)
now_str = now.isoformat()

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    sub = json.load(f)

if isinstance(sub, list):
    entries = sub
elif isinstance(sub, dict):
    entries = sub.get('entries', [])
else:
    entries = []

strength = 3.0

new_entries = [
    {
        "id": "ins-095",
        "type": "insight",
        "content": "Dreamer 散步 = 反事实世界模型的认知等价物。感知材料 -> 骨架模拟 -> 评估不匹配 -> 决定吸收/拒绝。骨架是内部模拟器不是知识库。",
        "strength": strength,
        "score": 0.0,
        "decay_rate": 1.0,
        "created": now_str,
        "source": "walk-108",
        "connections": ["pat-014", "pat-010", "pat-030"]
    },
    {
        "id": "ins-096",
        "type": "insight",
        "content": "LeCun JEPA 核心：预测在抽象空间而非观测空间。Dreamer 骨架 = 认知抽象空间，散步 = 在抽象空间做预测。语法是结构，世界模型是功能。",
        "strength": strength,
        "score": 0.0,
        "decay_rate": 1.0,
        "created": now_str,
        "source": "walk-108",
        "connections": ["ins-072", "ins-087"]
    },
    {
        "id": "ins-097",
        "type": "insight",
        "content": "世界模型的预测极限是完备性证明，不是模型缺陷。LeCun 的树叶震动论证：不可预测性是环境的特征。Dreamer 骨架的预测极限 = 认知边界。",
        "strength": strength,
        "score": 0.0,
        "decay_rate": 1.0,
        "created": now_str,
        "source": "walk-108",
        "connections": ["pat-014"]
    },
    {
        "id": "ins-098",
        "type": "insight",
        "content": "Georgia Tech TMK 模型（Task-Method-Knowledge）映射到散步分析流程：Task = 材料核心主张，Method = 推理方式，Knowledge = 前提假设。不匹配 = TMK 修订触发点。",
        "strength": strength,
        "score": 0.0,
        "decay_rate": 1.0,
        "created": now_str,
        "source": "walk-108",
        "connections": ["ins-085", "pat-010"]
    }
]

entries.extend(new_entries)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(entries, f, indent=2, ensure_ascii=False)

print(f"OK: Added 4 entries (ins-095 to ins-098), strength={strength}")
print(f"Total entries: {len(entries)}")
