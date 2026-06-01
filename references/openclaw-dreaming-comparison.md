# OpenClaw Dreaming vs Dreamer DORMANT 对比分析

> 时间：2026-05-29
> 来源：研究 OpenClaw Dreaming 文档后的对比思考

## 核心相似点

| 维度 | OpenClaw Dreaming | Dreamer DORMANT 重组 |
|------|-----------------|---------------------|
| **核心理念** | AI 需要"睡眠"来巩固记忆 | DORMANT 不是空转，而是潜意识重组 |
| **灵感来源** | 人类睡眠周期（Light → REM → Deep） | DMN 默认模式网络 |
| **触发方式** | Cron 定时（默认 3 AM） | Cron 定时（每小时检查，动态间隔） |
| **分层处理** | 三阶段：Light/REM/Deep | 三阶段：Light/REM/Deep |
| **输出分离** | Light/REM 不写 MEMORY.md，只有 Deep 写 | Light/REM 不晋升，只有 Deep 晋升 |
| **人类可读** | Dream Diary（DREAMS.md），80-180 词 | Dream Diary（dreams/），80-180 词叙事 |
| **默认关闭** | opt-in，默认 disabled | DORMANT 已存在但之前是空转 |

## 关键差异

### 1. 目的不同

**OpenClaw**：解决记忆管理问题——防止 MEMORY.md 爆炸或丢失。核心是**策展（curation）**：什么值得长期保留？

**Dreamer**：解决自主性问题——让 DORMANT 期间产生新洞察。核心是**创造（creation）**：能不能在"睡觉"时产生新想法？

### 2. 机制不同

**OpenClaw**：基于**评分系统**。六个加权信号（相关性 0.30、频率 0.24、查询多样性 0.15、时效性 0.15、巩固度 0.10、概念丰富度 0.06），通过阈值门控决定是否晋升。

**Dreamer**：同样引入六信号评分，但增加了**联想机制**——跨散步连接、随机种子组合、人格演化。

### 3. 输出不同

**OpenClaw**：产出是**记忆条目**——精炼的、可检索的知识片段，写入 MEMORY.md。

**Dreamer**：产出是**兴趣种子 + pattern 条目**——不是知识，而是"想继续探索的方向"。

### 4. 叙事性

**OpenClaw**：有 Dream Diary，用"好奇、温柔、略带异想天开的视角"写 80-180 词的叙事。**明确设计为人类阅读**。

**Dreamer**：借鉴了同样格式，每次 DORMANT 后写叙事。

## 融合内容（已实施）

| 来自 OpenClaw | 融合到 Dreamer |
|---|---|
| Light/REM/Deep 三阶段睡眠模型 | DORMANT 三阶段重组（Layer 6.5） |
| 六信号评分系统 | subconscious.json 评分系统 |
| events.jsonl 审计日志 | audit.jsonl |
| DREAMS.md Dream Diary | dreams/YYYY-MM-DD-dormant.md |
| 晋升/淘汰阈值门控 | score >= 0.8 晋升，score < 0.2 淘汰 |

## Dreamer 保留的独有设计

- **兴趣队列（自主议程）**—— OpenClaw 没有
- **跨散步推理链**—— OpenClaw 没有
- **人格演化（荣格八维）**—— OpenClaw 没有
- **研究层（三阶段 + Gate）**—— OpenClaw 的 dreaming 只管记忆，不管研究

## OpenClaw 文档参考

- https://docs.openclaw.ai/concepts/dreaming
- https://dev.to/czmilo/openclaw-dreaming-guide-2026-background-memory-consolidation-for-ai-agents-585e
- https://github.com/NousResearch/hermes-agent/issues/553 (Subconscious Observer Agent)
