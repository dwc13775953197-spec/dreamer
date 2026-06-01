# 潜意识评分系统参考

## ⚠️ 两套评分系统

Dreamer 有**两套独立的评分系统**，用于不同场景：

| 系统 | 用途 | 公式 | 所在位置 |
|------|------|------|---------|
| **通用六信号评分** | 日常散步后维护潜意识条目 | 6 加权信号（relevance/frequency/diversity/recency/consolidation/richness） | 本文件 |
| **DORMANT 四信号评分** | Deep Sleep 晋升/淘汰决策 | 4 信号（strength/diversity/recency/type_bonus） | SKILL.md Phase 3 章节 |

**不要混用**。日常散步后更新 score 字段时用通用公式；DORMANT Deep Sleep 计算晋升资格时用 DORMANT 公式。

---

## 通用六信号评分（日常维护）

### 评分信号定义

| 信号 | 权重 | 计算方式 |
|------|------|---------|
| **relevance** | 0.30 | 当前散步/研究主题与条目的语义匹配度（0-1，由 LLM 判断） |
| **frequency** | 0.24 | min(被引用的次数 / 10, 1.0) |
| **diversity** | 0.15 | min(来源类型数 / 4, 1.0)。来源类型：walk/research/TIL/dormant |
| **recency** | 0.15 | 1.0 - min(距今天数 / 30, 1.0)。30天内线性衰减 |
| **consolidation** | 0.10 | min(被 reinforce 次数 / 5, 1.0) |
| **richness** | 0.06 | min(该条目触发的联想数 / 5, 1.0) |

## 综合评分公式

```
score = relevance * 0.30 + frequency * 0.24 + diversity * 0.15 + recency * 0.15 + consolidation * 0.10 + richness * 0.06
```

范围：0.0 - 1.0

## 阈值

| 阈值 | 值 | 动作 |
|------|-----|------|
| 晋升 | score >= 0.8 AND 被引用 >= 3 | 晋升为 pattern 或 procedural |
| 候选 | score 0.5-0.8 | 保留观察 |
| 淘汰 | score < 0.2 AND strength < 3 | 移入 decayed |

> **注意**：DORMANT Deep Sleep 使用不同的晋升阈值：score ≥ 0.75 AND strength ≥ 6 AND type ≠ pattern。详见 SKILL.md Phase 3 章节。

## subconscious.json 条目结构

```json
{
  "id": "ins-001",
  "text": "涌现意味着不可预测性——复杂系统的行为只能通过演化来发现",
  "type": "insight",
  "source": "walk-001",
  "strength": 6,
  "score": 0.72,
  "signals": {
    "relevance": 0.8,
    "frequency": 0.6,
    "diversity": 0.5,
    "recency": 0.9,
    "consolidation": 0.4,
    "richness": 0.3
  },
  "decay_speed": 1,
  "created": "2026-05-28T12:00:00",
  "last_reinforced": "2026-05-29T00:00:00",
  "references": ["walk-001", "walk-003", "research/dormant-dmn"]
}
```

## 更新时机

- **散步后**：更新被引用条目的 frequency、recency、consolidation
- **DORMANT Light**：更新 recency
- **DORMANT REM**：更新 diversity、生成 pattern
- **DORMANT Deep**：计算所有 score，执行晋升/淘汰
- **周复盘**：全量重算 score

## 示例

一条在 walk-001 中产生、被 walk-003 和 research 引用过的 insight：

```
relevance = 0.9  (与当前主题高度相关)
frequency = 0.3  (被引用 3 次 → 3/10)
diversity = 0.5  (来自 walk + research = 2/4)
recency = 0.95 (1天前)
consolidation = 0.2 (被 reinforce 1 次 → 1/5)
richness = 0.2  (触发 1 个联想 → 1/5)

score = 0.9*0.30 + 0.3*0.24 + 0.5*0.15 + 0.95*0.15 + 0.2*0.10 + 0.2*0.06
      = 0.27 + 0.072 + 0.075 + 0.143 + 0.02 + 0.012
      = 0.592 → 候选区，继续观察
```
