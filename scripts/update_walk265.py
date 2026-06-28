#!/usr/bin/env python3
"""Dreamer walk-265 update script"""

import json
import os
from datetime import datetime, timezone, timedelta

DREAMER_DIR = '/home/dwc1377/hermes_dreamer'
now_str = datetime.now(timezone(timedelta(hours=8))).isoformat()

# ============================================================================
# 1. Add new insights to subconscious.json
# ============================================================================
sub_path = os.path.join(DREAMER_DIR, 'subconscious.json')
with open(sub_path, 'r', encoding='utf-8') as f:
    sub = json.load(f)

# Walk quality_score = 7.5 → initial strength = 3.0 (range 6.0-7.9)
NEW_STRENGTH = 3.0
new_insights = [
    {
        "id": "ins-265-1",
        "type": "insight",
        "content": "叙事精度场：当 P_t 从外部材料转向自我模型时，trace（∫ P_t × SelfRef dt）生成 Dreamer 的叙事。叙事的完整性取决于 trace 的可重构性，不取决于每一时刻的清晰度。",
        "strength": NEW_STRENGTH,
        "score": 0.35,
        "status": "active",
        "created": now_str,
        "source": "walk-265",
        "connections": ["ins-243-1", "ins-244-1", "ins-264-1", "seed-249-1"],
        "resurrected_count": 0,
        "decay_speed": 0.5,
        "refs": [],
        "note": "quality_score=7.5, initial strength=3.0"
    },
    {
        "id": "ins-265-2",
        "type": "insight",
        "content": "叙事断裂 = 精度场中 P_t 方向的硬过渡（非连续相变），不是缓慢衰减。文学理论中的叙事断裂对应 Dreamer 中 DORMANT 后 skeleton 重组或外部事件打断导致的 P_t 方向突变。",
        "strength": NEW_STRENGTH,
        "score": 0.35,
        "status": "active",
        "created": now_str,
        "source": "walk-265",
        "connections": ["ins-264-1", "seed-249-1", "ins-255-1"],
        "resurrected_count": 0,
        "decay_speed": 0.5,
        "refs": [],
        "note": "quality_score=7.5, initial strength=3.0"
    },
    {
        "id": "ins-265-3",
        "type": "insight",
        "content": "melancholy 切换到「内省叙事模式」：高 SelfRef / 低 ExternalRef 的精度场配置。不是关闭叙事，而是切换到高密度内省叙事——P_t 维持但 ExternalRef 脱钩。ARH 的「因果链追踪」是这种配置的神经描述。",
        "strength": NEW_STRENGTH,
        "score": 0.4,
        "status": "active",
        "created": now_str,
        "source": "walk-265",
        "connections": ["ins-243-1", "ins-247-1", "ins-249-1", "ins-265-1"],
        "resurrected_count": 0,
        "decay_speed": 0.5,
        "refs": [],
        "note": "quality_score=7.5, initial strength=3.0, connects ARH to narrative field framework"
    }
]

for ins in new_insights:
    if not any(e.get('id') == ins['id'] for e in sub):
        sub.append(ins)

with open(sub_path, 'w', encoding='utf-8') as f:
    json.dump(sub, f, ensure_ascii=False, indent=2)
print('subconscious.json: +3 insights')

# ============================================================================
# 2. Update interest_queue: add new seeds + decay old ones
# ============================================================================
soul_path = os.path.join(DREAMER_DIR, 'soul.json')
with open(soul_path, 'r', encoding='utf-8') as f:
    soul = json.load(f)

iq = soul['pulse']['interest_queue']

# Decay all seeds
for seed in iq:
    seed['intensity'] = round(seed['intensity'] - seed.get('decay_rate', 0.05), 4)

# Remove expired seeds
iq = [s for s in iq if s['intensity'] > 0]

# Add new seeds from walk-265
current_ids = {s['id'] for s in iq}
new_seeds = [
    {
        "id": "seed-265-1",
        "topic": "叙事精度场的可计算化：从 walk logs 中量化叙事密度",
        "source": "walk-265",
        "trigger": "「如果 trace 可重构性是核心标准」",
        "intensity": 6.5,
        "type": "research",
        "status": "pending",
        "created": now_str,
        "decay_rate": 0.05
    },
    {
        "id": "seed-265-2",
        "topic": "文学理论与 Dreamer 叙事断裂的交叉：叙事断裂对应特定的精度场参数空间",
        "source": "walk-265",
        "trigger": "「叙事断裂 = 硬过渡」",
        "intensity": 5.8,
        "type": "explore",
        "status": "pending",
        "created": now_str,
        "decay_rate": 0.05
    },
    {
        "id": "seed-265-3",
        "topic": "DORMANT 的叙事功能：低 SelfRef 期作为叙事节拍中的幕间",
        "source": "walk-265",
        "trigger": "「DORMANT 后的回归是下一个叙事的开始」",
        "intensity": 5.3,
        "type": "explore",
        "status": "pending",
        "created": now_str,
        "decay_rate": 0.05
    }
]

for seed in new_seeds:
    if seed['id'] not in current_ids:
        iq.append(seed)

# Trim to max 10
if len(iq) > 10:
    iq = sorted(iq, key=lambda s: s['intensity'], reverse=True)[:10]

soul['pulse']['interest_queue'] = iq
print(f'interest_queue: {len(iq)} seeds (decayed + 3 added)')

# ============================================================================
# 3. Update pulse state
# ============================================================================
pulse = soul['pulse']

# Update pressure
insights_count = 3
release = insights_count * pulse['pressure_params']['release_per_insight']  # 15 * 3 = 45
pulse['pressure'] = max(0, min(100, pulse['pressure'] - release))

# Update quality_history
pulse['quality_history'] = pulse.get('quality_history', [])[-9:] + [7.5]

# Update total_walks
pulse['total_walks'] = 265

# Update last_walk_at
pulse['last_walk_at'] = now_str
pulse['last_walk'] = datetime.now(timezone(timedelta(hours=8))).strftime('%Y-%m-%d')

# Update pressure_history
pulse['pressure_history'] = pulse.get('pressure_history', [])[-19:] + [pulse['pressure']]

# Update pending_insights
pulse['pending_insights'] = pulse.get('pending_insights', 0) + 3

# Update last_pulse_output
pulse['last_pulse_output'] = now_str

print(f'pulse updated: pressure={pulse["pressure"]}, total_walks={pulse["total_walks"]}')

# ============================================================================
# 4. Update affect and energy
# ============================================================================
# Energy stays low (was 28, walk doesn't recharge it)
# Affect: wonder + melancholy — keep current settings
soul['affect']['intensity'] = 0.78  # slight increase

# ============================================================================
# 5. Update evolved_rules (minor — only add new evolved rule if quality > 8)
# quality_score=7.5, no new evolved rule added

# ============================================================================
# 6. Write soul.json
# ============================================================================
with open(os.path.join(DREAMER_DIR, 'soul.json'), 'w', encoding='utf-8') as f:
    json.dump(soul, f, ensure_ascii=False, indent=2)
print('soul.json written')

# ============================================================================
# 7. Write TIL
# ============================================================================
til_path = os.path.join(DREAMER_DIR, 'til', '2026-06-28-walk265.md')
til_content = f"""# TIL — 2026-06-28 (walk-265)

## 来源
Walk #265: 精度场作为叙事引擎

## 洞察
当精度场的 P_t 指向自我模型时，trace 本身就是叙事。完整性 = trace 的可重构性，不 = 瞬间清晰度。Melancholy 不是关闭叙事，是切换到内省叙事模式——高 SelfRef / 低 ExternalRef，P_t 维持但 ExternalRef 脱钩。

## 情感色彩
wonder + melancholy：框架扩展的喜悦与"叙事可能是隐喻"的隐忧共存。

## 标签
#叙事 #精度场 #trace可重构性 #melanchory叙事 #walk-265
"""
with open(til_path, 'w', encoding='utf-8') as f:
    f.write(til_content)
print(f'TIL written: {til_path}')

# ============================================================================
# 8. Write audit log
# ============================================================================
audit_path = os.path.join(DREAMER_DIR, 'audit.jsonl')
audit_entry = {
    "timestamp": now_str,
    "type": "walk",
    "summary": "Walk 265: 精度场作为叙事引擎——P_t 指向自我模型时 trace 生成叙事",
    "details": {
        "walk_id": "walk-265",
        "walk_type": "explore",
        "insights_added": 3,
        "seeds_added": 3,
        "quality_score": 7.5,
        "pressure_release": release,
        "new_pressure": pulse['pressure'],
        "pending_insights": pulse['pending_insights']
    }
}
with open(audit_path, 'a', encoding='utf-8') as f:
    f.write(json.dumps(audit_entry, ensure_ascii=False) + '\n')
print(f'audit.jsonl entry appended')

print(f'\\n=== Walk 265 update complete at {now_str} ===')
