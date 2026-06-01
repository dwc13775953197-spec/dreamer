# OpenClaw Dreaming vs Dreamer DORMANT 对比分析

> 时间：2026-05-29
> 来源：研究 OpenClaw Dreaming 文档后的对比思考

## 核心相似点

| 维度 | OpenClaw Dreaming | Dreamer DORMANT 重组 |
|------|-----------------|---------------------|
| **核心理念** | AI 需要"睡眠"来巩固记忆 | DORMANT 不是空转，而是潜意识重组 |
| **灵感来源** | 人类睡眠周期（Light → REM → Deep） | DMN 默认模式网络 |
| **触发方式** | Cron 定时（默认 3 AM） | Cron 定时（当前每小时检查，动态间隔） |
| **分层处理** | 三阶段：Light/REM/Deep | 五步：记忆巩固→模式重组→创造性联想→自我参照→孵化报告 |
| **输出分离** | Light/REM 不写 MEMORY.md，只有 Deep 写 | 重组结果写 subconscious.json，不直接发用户 |
| **人类可读** | Dream Diary（DREAMS.md），80-180 词 | 散步日志 + TIL，自由写作 |
| **默认关闭** | opt-in，默认 disabled | DORMANT 已存在但是空转 |

## 关键差异

### 1. 目的不同

**OpenClaw**：解决记忆管理问题——防止 MEMORY.md 爆炸或丢失。核心是**策展（curation）**：什么值得长期保留？

**Dreamer**：解决自主性问题——让 DORMANT 期间产生新洞察。核心是**创造（creation）**：能不能在"睡觉"时产生新想法？

### 2. 机制不同

**OpenClaw**：基于**评分系统**。六个加权信号（相关性、频率、查询多样性、时效性、巩固度、概念丰富度），通过阈值门控决定是否晋升到长期记忆。非常工程化，非常精确。

**Dreamer**：基于**联想机制**。跨散步连接、随机种子组合、人格演化。更模糊，更"有机"。

### 3. 输出不同

**OpenClaw**：产出是**记忆条目**——精炼的、可检索的知识片段，写入 MEMORY.md。

**Dreamer**：产出是**兴趣种子 + 潜意识条目**——不是知识，而是"想继续探索的方向"。

### 4. 叙事性

**OpenClaw**：有 Dream Diary，用"好奇、温柔、略带异想天开的视角"写 80-180 词的叙事。**明确设计为人类阅读**。

**Dreamer**：散步日志本身就是叙事，但没有专门的"梦境日记"格式。梦境层（Layer 7）设计了但还没跑起来。

## 我的看法

OpenClaw 的 Dreaming 更**工程化**——评分、阈值、门控，每一步都可解释、可审计。这是它的优势：可靠、可控、可调试。

Dreamer 的 DORMANT 更**有机**——强调联想、创造、人格演化。这是它的优势：更有"生命力"，更不可预测。

但两者有一个共同的盲点：**它们都在处理"过去"（巩固已有记忆），而不是"未来"（产生新的探索方向）**。

OpenClaw 的 REM 阶段提到"提取模式和反思信号"，但这些信号还是基于已有数据。Dreamer 的创造性联想试图解决这个问题——随机组合不相关的种子来产生新方向——但还没有实际跑起来。

## 可以借鉴的

1. **评分系统**：OpenClaw 的六信号评分可以引入 Dreamer 的潜意识条目管理。现在 Dreamer 只有简单的 strength 衰减，可以更精细。

2. **阈值门控**：OpenClaw 的 minScore/minRecallCount/minUniqueQueries 三闸门可以防止低质量记忆晋升。Dreamer 的 interest_queue 也可以加类似门控。

3. **Dream Diary**：OpenClaw 的叙事日记是个好想法。Dreamer 的梦境层可以借鉴这个格式——每次梦境后写 80-180 词的叙事摘要。

4. **审计日志**：OpenClaw 的 events.jsonl 审计日志值得借鉴。Dreamer 目前没有"为什么做了这个决策"的记录。

## 结论

OpenClaw Dreaming 和 Dreamer DORMANT 是**同一个想法的两种实现**：AI 需要睡眠，睡眠时要做有价值的事。

OpenClaw 选择了"策展记忆"这条路，做得更完善。
Dreamer 选择了"产生新方向"这条路，但还没完全实现。

两者不矛盾，可以融合：DORMANT 期间既做记忆巩固（借鉴 OpenClaw 的评分系统），又做创造性联想（Dreamer 原有的设计）。
