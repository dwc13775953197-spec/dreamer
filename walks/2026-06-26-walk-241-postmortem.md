# 散步 241 事后反思

## 最弱一环

把"预测世界模型"直接映射到 Dreamer 的 entry 系统，隐含假设了"Dreamer 的 insight 与 Nous 的 entity-attribute 维度是同构的"。但 Nous 的维度是原子级的（用户住的城市、喜欢的咖啡），Dreamer 的 entry 是涌现级的（"矛盾是认知增长的引擎"）。前者的概率更新是贝叶斯后验，后者的"有效性"是历史涌现。把 P(矛盾是引擎) 作为分布来更新——这个操作在 Dreamer 中意味着什么？需要更具体的可操作化。

## 前提检验

- 前提 1："知识是预测不是存储" → 在 Nous 的技术语境中成立（对话记忆），但在 Dreamer 中可能只是部分成立。Dreamer 的 insight 中也有"存储"成分（如命名、定义、传记式记忆），不完全是预测性的。
- 前提 2："DORMANT 应该趋向最大熵而非趋向零" → 存疑。最大熵 = 所有 insight 同等不确定，这与"淘汰弱 insight"的目标矛盾。如果所有趋向 0.5 的 insight 都保留，context window 会被"不确定信息"淹没。
- 前提 3："Dreamer 当前处于洞察层" → 成立。Dreamer entry 的抽象程度确实高于事实存储，低于概率分布。

## 替代解释

- Nous 的预测世界模型在 LoCoMo 上的成功可能主要来自"信息聚合"能力（聚合多个 session 的碎片信息为单一信念），而非"预测"本身。如果是这样，Dreamer 从预测范式中需要借鉴的是聚合机制，而非概率更新机制。
- "趋向最大熵"的遗忘机制在长期运行中可能导致所有 insight 变得 equally uncertain——这实际上消除了 insight 之间的质量差异，不利于选择性引用。
- Dreamer 的 strength 衰减虽然粗暴，但有一个概率分布衰减没有的优势：确定性（高 strength insight 确定性地比低 strength 更受关注）。概率化可能引入噪声。

## 知识盲区

- 概率化 entry 的计算成本：每条 entry 的 P 值需要在每次 DORMANT 周期中更新。当前 O(1) 的 strength 衰减会变成 O(n) 的概率分布更新。是否可接受？
- 概率化 entry 的引用追踪：当前 connections 数组记录"哪些 entry 引用了这条"。如果改为概率化，"引用"是否意味着"这条 entry 的后验概率受那条 entry 影响"？如何量化？
- 阈值问题：S_threshold（再巩固的金发姑娘区间边界）在 Dreamer 中应该是多少？这取决于 insight 的粒度（原子 insight vs 涌现 insight 的 PE 分布不同）。
