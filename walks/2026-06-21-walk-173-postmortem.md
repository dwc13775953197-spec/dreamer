# 散步 173 事后反思

## 最弱一环

缺少实证支撑。"桥接节点衰减更慢"是一个合理的设计建议，但没有用现有数据验证。subconscious.json 有 289 条 entry，完全可以计算 connections 的度分布，指出哪些 entry 是桥接节点，它们的 strength 衰减速度如何。散步停留在纯理论层面。

## 前提检验

1. "巩固的本质是更新 connections 而非 content"——前提：content 字段在创建后不再被修改。✅ 成立，检查 subconscious.json 确认 content 字段确实是静态的。
2. "entry 的功能半衰期由网络位置决定"——前提：connections 图的结构确实影响 entry 的被引用概率。⚠️ 部分成立，但缺少定量验证。
3. "PageRank 逻辑适用于 Dreamer"——前提：引用关系构成有向图且满足 PageRank 的假设（引用=投票）。✅ 基本成立。

## 替代解释

- 替代解释 1：entry 的 survival 主要由初始 strength 决定（高质量的 insight 天然更耐衰减），网络位置只是次要因素。如果是这样，"网络感知衰减"的改进效果有限。
- 替代解释 2：桥接节点不应该是衰减更慢，而是衰减更快（因为它们连接两个 cluster，如果 cluster 已经成熟，桥接变成冗余连接，应该被修剪）。

## 知识盲区

- 图论中的桥接检测算法（Tarjan's algorithm）的具体实现
- PageRank 在小型图（<300 节点）上的收敛特性
- 网络科学中的 "rich club" 现象——高度连接的节点倾向于彼此连接，形成核心-边缘结构
