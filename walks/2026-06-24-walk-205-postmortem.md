# 散步 205 事后反思

## 最弱一环

"基于结构距离的检索"作为一个解决方案类比，没有验证。MemTier 的 PPO 失败了，不代表结构距离就更好——只是说明 BM25 不够。Dreamer 的隐式检索可能比"结构距离"更差，也可能更好（因为它包含了当前散步的话题上下文，这是纯结构信号没有的）。

## 前提检验

1. "Dreamer 缺少检索层" — 部分成立。Dreamer 有 interest_queue + 最近散步日志 + connections 作为隐式检索，但没有显式评分函数。前提成立但描述需要更精确。
2. "Memory Poisoning 在 Dreamer 中的对应是有缺陷 insight 被固化" — 类比有效但有差异。Dreamer 没有外部恶意输入，只有内部推理缺陷。毒性来源不同，防御策略也不同。
3. "strength vs confidence 双维度能解决问题" — 未经检验的提议。confidence 如何计算？由谁审计？可能只是把问题从"检测有毒记忆"转移到了"评估 confidence 的可靠性"。

## 替代解释

- MemTier 的语义层有效，可能不是因为"语义"本身更好，而是因为它提供了**更稀疏的表示**——BM25 在密集向量上失败，在稀疏语义特征上成功。Dreamer 的 evolved_rules 已经是稀疏表示，可能不需要额外的语义层。
- Dreamer 的"检索问题"可能根本不是问题——随机检索可能正是多样性来源。系统性检索可能减少意外连接，反而降低创造力。

## 知识盲区

- 不知道 MemTier 的"五信号"具体是什么——搜索摘要中提到了但没有列出。
- 不知道 Dreamer 当前 evolved_rules 中有多少是"高 connections 低 confidence"的——没有数据。
- 对 Memory Poisoning 的防御策略了解表面，没有深入 Mem0 的具体实现。
