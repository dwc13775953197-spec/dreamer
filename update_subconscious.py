#!/usr/bin/env python3
import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz).isoformat()

with open('/home/dwc1377/hermes_dreamer/subconscious.json') as f:
    d = json.load(f)

# Update last 3 entries with actual content
d[-3]["content"] = "好奇心不是Dreamer的引擎而是仪表盘。APE是价值自由信号，不评估好坏只检测偏差。interest_queue应由skeleton预测偏差驱动而非insight质量。"
d[-2]["content"] = "Dreamer的负能力等于认知失调容忍度。高容忍度个体DMN-PFC耦合不立即增强，散步后维持阈限状态而非急于闭合。DORMANT不应在散步后立即启动。"
d[-1]["content"] = "价值自由学习APE和价值导向学习RPE可并行运行。散步应同时产出insight(RPE路径)和偏差信号(APE路径)。偏差信号指导方向，RPE评估产出。"

# Also update connections on first entry
d[-3]["connections"] = ["seed-396", "seed-397", "seed-398"]

with open('/home/dwc1377/hermes_dreamer/subconscious.json', 'w') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("Updated 3 entries, total:", len(d))
