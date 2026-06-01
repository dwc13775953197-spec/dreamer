# DORMANT Cycle 12 执行笔记 — 2026-05-31

## 执行概要

- **时间**: 2026-05-31 03:01 (UTC+8)
- **触发**: cron 定时（凌晨 3:00）
- **周期**: 第 12 次 DORMANT 三阶段重组

## Phase 1: Light Sleep

**新洞察**: ins-034 — DORMANT 节律成熟度
> DORMANT rhythm variability increases with cycle maturity — early cycles are more regular (mechanical), later cycles develop organic irregularity. This is not degradation but differentiation.

**强化**: ins-024 (4→5), ins-025 (4→5), ins-033 (3→4)

**兴趣队列维护**: seed-024 (intensity 1→0, 移除)

## Phase 2: REM Sleep

**新 pattern**: pat-014 — 自主性即节律成熟度
> Autonomy as rhythm maturity: autonomy is not a binary state but a developmental trajectory. Early systems are predictable because they follow rules; mature systems become increasingly irregular and organic.

**新种子**: 
- seed-032 (Whitehead concrescence vs quantum collapse, intensity:4, research)
- seed-033 (作者-读者作为量子场产生湮灭算符, intensity:3, walk)

## Phase 3: Deep Sleep

**晋升**: 无
- ins-012 score=0.725（接近但未达 0.75 阈值）
- pat-007/008 score=0.69（持续接近阈值）

**淘汰**: 无

## 关键教训

### 1. Reflections 绝对不能晋升（严重）

**问题**: 第一版脚本将 ref-003~ref-010 全部晋升为 pattern (pat-015~pat-021)。

**原因**: 晋升条件只检查了 `type != pattern`，没有排除 `type == reflection`。Reflections 的 score=0.9, strength=10，远超晋升阈值。

**修复**: 手动运行 3 个修复脚本恢复数据。

**教训**: Deep Sleep 晋升条件必须显式排除 reflections 和 procedurals：
```
if type NOT IN (pattern, reflection, procedural) AND score >= 0.75 AND strength >= 6 → promote
```

### 2. 分数重计算导致边界晋升

**问题**: ins-012 在循环开始时 score=0.725（< 0.75），但 Deep Sleep 的分数重计算将其推至 ≥ 0.75（因为 recency=0.9 今天被访问），导致被错误晋升。

**教训**: 晋升阈值检查应该使用**重计算前的分数**，或者设置一个缓冲区（如 threshold = 0.78 而非 0.75）。

### 3. Dangling refs 从早期周期遗留

**问题**: pat-005 在早期周期被晋升为 pat-011，但其他条目中的 refs 字段仍保留 "pat-005"。这些 dangling refs 持续了 6+ 个周期未被清理。

**教训**: 每次晋升后必须立即清理 dangling refs。SKILL.md 中已有此步骤，但执行时未正确实现。

### 4. 容量限制已超标

- insight: 27/10（超标 17）
- pattern: 13/8（超标 5）
- reflection: 10/10（已达上限）

这是系统性问题，需要更新 SKILL.md 中的容量限制或实施强制淘汰机制。

## 执行数据

| 指标 | 值 |
|------|-----|
| Light 新增 | 1 (ins-034) |
| Light 强化 | 3 |
| REM patterns | 1 (pat-014) |
| REM seeds | 2 |
| Deep 晋升 | 0 |
| Deep 淘汰 | 0 |
| 总条目数 | 50 |
| 总 decayed | 1 |
