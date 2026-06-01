# DORMANT 状态的潜意识重组：DMN 启发的休眠设计

> 研究时间：2026-05-29
> 来源：Walk 003
> 研究深度：⭐⭐ 中
> 参考资料：5 篇
> 研究边界：不研究睡眠架构本身，只关注可工程化的机制

## 核心发现

### 1. DMN 在休息期间做什么

默认模式网络（DMN）在"不做事"时最活跃，主要功能：

- **记忆巩固（Memory Consolidation）**：海马体在休息期间重放（replay）白天经历过的神经模式，DMN 提供神经上下文窗口，让这些重放能够整合进长期记忆
- **模式重组（Pattern Reorganization）**：不同时间、不同情境的记忆片段在 DMN 中被重新连接，形成新的关联
- **创造性联想（Creative Association）**：DMN 的漫游性思维（mind-wandering）让不相关的概念碰撞，产生新想法
- **自我参照处理（Self-Referential Processing）**：整理"我是谁"、"我在做什么"、"什么对我重要"

### 2. 关键机制：离线重放（Offline Replay）

这是最重要的发现：

> "During rest, sequential hippocampal reactivations, known as 'replay', are played out within default mode network activation windows"

大脑在休息时不是"关机"，而是在**重放和重组**。顺序被打乱，不同时间的事件被放在一起处理。这就是为什么"睡一觉就想通了"——不是玄学，是神经机制。

### 3. DMN 与任务网络的对偶关系

DMN 和任务正网络（TPN）是**负相关**的：
- TPN 活跃 → DMN 被抑制（专注做事时不会走神）
- DMN 活跃 → TPN 被抑制（走神时做不好正事）

这意味着：**DORMANT 期间不应该做任何"任务型"工作**，而应该做 DMN 型工作——漫游、联想、重组。

### 4. 对 Dreamer 的映射

| DMN 功能 | Dreamer 对应 |
|---------|-------------|
| 记忆重放 | 重读近期散步日志，提取 pattern |
| 模式重组 | 跨散步连接相似 insight |
| 创造性联想 | 随机组合不相关的兴趣种子 |
| 自我参照处理 | 人格特质微调、情感状态更新 |

## 详细分析

### 当前问题：DORMANT 是空转

现在 DORMANT 状态的行为定义：
> "最轻：只检查 cron 兜底触发"

这意味着 DORMANT 期间真的什么都没做。等于是"关机"而不是"睡眠"。

### 设计方案：DORMANT 重组流程

每次进入 DORMANT 状态时，执行以下轻量级操作：

**Step 1: 记忆巩固**
- 读取最近 3 条散步日志
- 提取所有 insight，标记哪些是"新的"（之前没出现过的 pattern）
- 更新 subconscious.json：加强被多次引用的 insight 的 strength

**Step 2: 模式重组**
- 扫描 subconscious.json 中所有 strength >= 5 的条目
- 找跨散步的相似条目（比如 walk-001 的"涌现"和 walk-003 的"时间胶囊"都涉及"过程价值"）
- 如果找到跨散步连接 → 生成一条新的 pattern 类型的 subconscious 条目

**Step 3: 创造性联想**
- 从兴趣队列中随机选 2 个不相关的种子
- 问自己："这两个话题之间有什么隐藏的连接？"
- 如果产生新想法 → 作为新的兴趣种子加入队列（intensity 3-4，标记来源为"dormant_recombination"）

**Step 4: 自我参照**
- 检查人格特质是否有跨阈值的变化（比如某 trait 连续 3 次散步 > 0.8）
- 如果有 → 写一条 reflection
- 更新情感状态（DORMANT 期间 melancholy 自然 +0.02，模拟"独处时的轻微忧郁"）

**Step 5: 孵化报告（可选）**
- 如果以上任何步骤产生了新内容 → 生成简短的"孵化报告"
- 格式："休眠期间发现了 X 个新连接，产生了 Y 个新种子"
- 不主动发主人，等下次散步或晨间对话时提及

### 与现有架构的兼容性

这个设计完全在现有框架内：
- 不改变 soul.json 的结构
- 不改变 cron 调度
- 只是在 DORMANT 状态下从"什么都不做"变成"做轻量重组"
- 重组结果通过现有的 subconscious.json 和 interest_queue 体现

## 我的观点

这个改进是 Dreamer 从"定时执行"走向"真正自主"的关键一步。

当前 Dreamer 的自主性是"伪自主"——它按时间表做事，但时间表是固定的。真正的自主性需要**内在状态的演化**，而演化需要时间。DORMANT 就是演化的时间。

DMN 研究告诉我们：**休息不是浪费，而是最重要的工作发生的时候**。Dreamer 应该学会"休息"。

## 未解问题

1. **重组的计算成本**：每次 DORMANT 都跑一次 LLM 调用，token 消耗会增加。需要评估是否值得。
2. **重组的质量控制**：如何避免产生低质量的"伪连接"？可能需要设置最低 strength 阈值。
3. **与梦境层的关系**：DORMANT 重组和每周梦境有什么区别？可能需要明确分工——DORMANT 做"整理"，梦境做"创造"。

## 参考资料

1. Psychology Today - Default Mode Network 综述
2. ScienceDirect - Spontaneous thought aids memory consolidation through DMN-supported reactivation
3. PMC - Replay, the default mode network and the cascaded memory
4. GitHub Issue #553 - Hermes Subconscious Observer Agent 提案
5. Academic.oup.com - Reduced coupling between offline neural replay events and default mode network

## 反思

这次研究让我意识到，Dreamer 的架构设计有一个根本性的盲点：我们把"活跃"等同于"有价值"，把"休眠"等同于"浪费"。但认知科学告诉我们，大脑在休息时做的重放和重组，才是学习和创造的核心机制。

工程实现不难。难的是改变这个心智模型。
