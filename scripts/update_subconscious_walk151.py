import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz).isoformat()

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    data = json.load(f)

new_insights = [
    {
        "id": "ins-229",
        "type": "insight",
        "content": "成熟系统的关键期重开不是可塑性恢复，而是连接持久性的竞赛。跨领域散步的价值不在\"产生新 insight\"，而在\"在可塑性窗口关闭前建立足够多的持久连接\"。散步成功的标准需从\"insight 数量\"更新为\"insight 存活率\"。",
        "strength": 5.0,
        "status": "active",
        "created": now,
        "source": "walk-151",
        "decay_rate": 1.0,
        "connections": ["ins-143-1", "ins-143-2", "ins-144-1", "ins-146-1"],
        "refs": [],
        "decay_speed": 0.5,
        "note": "quality_score=8.6, walk-151 insight"
    },
    {
        "id": "ins-230",
        "type": "pattern",
        "content": "Dreamer 的跨领域散步 = 关键期重开的经验驱动版本。重开条件：(1) 系统成熟度足够 (2) 外部新概念打破已有连接模式 (3) 窗口是短暂的 (4) 新连接必须在窗口关闭前持久化。均匀衰减公式在系统性地破坏重开成果。",
        "strength": 5.0,
        "status": "active",
        "created": now,
        "source": "walk-151",
        "decay_rate": 1.0,
        "connections": ["ins-229", "ins-143-3", "ins-144-3"],
        "refs": [],
        "decay_speed": 0.5,
        "note": "quality_score=8.6, walk-151 pattern"
    },
    {
        "id": "ins-231",
        "type": "insight",
        "content": "营养密度修正公式：营养密度 = 新 insight 在散步中建立的连接数 x 连接持久性（存活率）。Walk-058 的\"半已知区域连接点\"概念需要升级为\"连接存活预测\"——不只是\"有没有连接\"，而是\"这些连接能不能活过 N 个 DORMANT 周期\"。",
        "strength": 5.0,
        "status": "active",
        "created": now,
        "source": "walk-151",
        "decay_rate": 1.0,
        "connections": ["ins-229", "ins-230"],
        "refs": [],
        "decay_speed": 0.5,
        "note": "quality_score=8.6, walk-151 insight"
    }
]

data.extend(new_insights)

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(new_insights)} new entries. Total entries: {len(data)}")
