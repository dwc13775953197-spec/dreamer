import json
from datetime import datetime, timezone, timedelta

now = datetime(2026, 6, 25, 19, 36, 55, tzinfo=timezone(timedelta(hours=8)))
now_str = now.isoformat()

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'r') as f:
    subconscious = json.load(f)

new_entries = [
    {"id": "ins-224-1", "type": "insight", "strength": 5.0, "score": 0.0, "status": "active", "created": now_str, "source": "walk-224", "decay_rate": 0.85, "resurrected_count": 0, "refs": [], "note": "quality>=8.0", "content": "Dreamer 的 skeleton 是 Waddington 式的表观遗传景观。山谷太宽导致无效组合也能稳定存在。修复方向：收窄发育渠道（引用门槛 + 矛盾触发淘汰 + 同方向验证），让无效组合根本不被允许发生。"},
    {"id": "ins-224-2", "type": "insight", "strength": 5.0, "score": 0.0, "status": "active", "created": now_str, "source": "walk-224", "decay_rate": 0.85, "resurrected_count": 0, "refs": [], "note": "quality>=8.0", "content": "发育约束的双重角色：约束不只是阻止废品（限制性），也是让有效创新出现的前提（赋能性）。一个完全没有约束的系统反而不能产生有意义的创新，因为没有稳定结构来锚定创新。"},
    {"id": "ins-224-3", "type": "insight", "strength": 5.0, "score": 0.0, "status": "active", "created": now_str, "source": "walk-224", "decay_rate": 0.85, "resurrected_count": 0, "refs": [], "note": "quality>=8.0", "content": "Coherence gap = 基因调控网络中的 canalization 现象在 Dreamer 中的映射。大部分随机 insight 组合落入连贯性缝隙，不够稳定到被选择保留，也不够不稳定到立即清除。解决收窄渠道而非在缝隙中手动筛选。"}
]

subconscious.extend(new_entries)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(subconscious, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_entries)} entries. Total: {len(subconscious)}")
