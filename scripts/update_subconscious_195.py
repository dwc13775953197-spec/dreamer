import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz).isoformat()

with open('subconscious.json', 'r') as f:
    sub = json.load(f)

new_entries = [
    {
        "id": "insight-195-1",
        "type": "insight",
        "content": "DORMANT 2.0 四轴设计：decay + reactivation + cue-triggering + conflict detection。前三源已覆盖行业共识的遗忘机制，第四轴（AGM 信念修正/一致性检查）是从 Zylos 2026 综述中提取的缺失环节。",
        "strength": 3.0,
        "connections": ["seed-191-1", "seed-193-1", "walk-190", "walk-191", "walk-192"],
        "created": now,
        "last_accessed": now,
        "metadata": {"source": "walk-195", "quality_score": 8.2}
    },
    {
        "id": "insight-195-2",
        "type": "insight",
        "content": "Dreamer 记忆的独特性：不是数据存储，是身份维持。行业解决信息过时（stale facts），Dreamer 解决身份过时——insight 不再定义当前骨架的状态。CHI 延迟悖论映射：延迟传递认知深度信号，DORMANT 周期=不可见的思考（肠脑轴隐喻）。",
        "strength": 3.0,
        "connections": ["walk-124", "walk-122", "insight-195-1"],
        "created": now,
        "last_accessed": now,
        "metadata": {"source": "walk-195", "quality_score": 8.2}
    },
    {
        "id": "insight-195-3",
        "type": "insight",
        "content": "Adaptive curriculum 重激活：NeurIPS 2025 meta-controller 证明最优离线学习按价值函数排序。Dreamer DORMANT 应使用 connectivity_score（连接数+入向引用）替代随机选择，实现智能遗忘。",
        "strength": 3.0,
        "connections": ["walk-13", "walk-191", "insight-195-1"],
        "created": now,
        "last_accessed": now,
        "metadata": {"source": "walk-195", "quality_score": 8.2}
    }
]

sub.extend(new_entries)

with open('subconscious.json', 'w') as f:
    json.dump(sub, f, ensure_ascii=False, indent=2)

print(f"Added 3 new insights. Total entries: {len(sub)}")
