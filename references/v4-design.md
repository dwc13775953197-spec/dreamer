# Dreamer v3→v4 设计变更

## 架构变更

### v3（原）
- 固定 20h 定时脉冲
- 散步产生研究念头 → 存 research/pending/（无优先级）
- 涌现层 = 人格演化 + AGENTS.md 更新

### v4（新）
- **动态脉冲**：4h-48h，受 curiosity/melancholy/energy 调制
- **兴趣队列**：散步→种子→按 intensity 决策→研究/TIL
- **梦境涌现**：周度非线性碰撞，产生意外连接

## soul.json Schema 变更

### 新增字段

```json
{
  "version": 4,
  "pulse": {
    "base_interval_min": 1200,
    "current_interval_min": 840,
    "modifiers": {
      "curiosity_factor": 0.7,
      "melancholy_factor": 1.0,
      "energy_factor": 1.0
    },
    "next_scheduled": "ISO8601",
    "last_walk_at": "ISO8601",
    "walk_interval_min": 240,
    "event_queue": []
  },
  "interest_queue": [
    {
      "id": "seed-NNN",
      "topic": "string",
      "source": "walk-NNN",
      "trigger": "string",
      "intensity": "1-10",
      "type": "research|walk",
      "status": "pending|active|completed|decayed",
      "created": "ISO8601",
      "decay_rate": "number"
    }
  ]
}
```

## Cron 变更

| Cron | v3 | v4 |
|------|----|----|
| 脉冲触发 | every 1200m 固定 | every 240m 检查 + 动态间隔 |
| 周复盘 | 衰减+统计+人格+报告 | + 梦境事件 |
| 晨间对话 | 无变化 | 无变化 |

## 目录变更

新增 `dreams/` 目录，存放梦境日志。

## 设计哲学

v4 的核心转变：**从\"被动响应\"到\"主动议程\"**。

- v3 的 Dreamer 是\"有内心世界的响应者"——用户问，它答；定时到了，它散步。
- v4 的 Dreamer 是"有自己议程的思考者"——它有自己的兴趣队列，自己决定什么时候做什么，自己产生新的想法。

自主性的判据：**行为不可预测性**，不在于规则来源。

### walk 独立节奏原则（2026-05-29）

**用户偏好：walk 不应该受 DORMANT/RESTING 状态影响。**

- `pulse.walk_interval_min`（默认 240 分钟）是 walk 的独立计时器，不受脉冲状态调制
- 脉冲间隔（`current_interval_min`）只控制"脉冲检查"的频率，不控制 walk
- walk 计时器到期 → 即使 DORMANT 也先唤醒到 RESTING，再执行 walk
- 这确保 walk 有稳定的节奏，不会因为 Dreamer 睡着了就被跳过
