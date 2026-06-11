# 散步 074 事后反思

## 最弱一环

「选择性遗忘需要 storage strength 的代理指标」这个推论走得太快了。Dreamer 的 strength 字段本质上是 retrieval strength（最近被激活的频率），不是 storage strength（长期记忆的牢固程度）。从 retrieval 推断 storage 是一个未经验证的假设。

## 前提检验

1. **Bjork 的框架适用于 artificial agent** — 部分成立。Bjork 的研究对象是人类记忆系统，Dreamer 的 subconscious 是人工设计的衰减机制。类比有启发但不严格。
2. **subconscious 衰减 = 必要难度引擎** — 需要验证。当前衰减是均匀的，而必要难度要求「恰好够难」。均匀衰减可能过难或过易，不是最优的。
3. **walk-068-070 的诊断循环 = 集中练习** — 成立。三次连续诊断确实是在高频检索未衰减的 entries。

## 替代解释

- **subconscious 枯竭可能不是「必要难度最优」而是「输入管道堵塞」**：walk-070 的问题可能不是 entries 衰减太多，而是新 entries 生成太少。没有新 entries，衰减只是在清空系统。
- **遗忘可能不是「学习的必要条件」而是「学习的副产品」**：Bjork 的框架中，遗忘是检索强度衰减的自然结果，不是目的。将衰减机制重新定义为「必要难度引擎」可能颠倒了因果。

## 知识盲区

- Bjork 的「新废用理论」中 storage strength 和 retrieval strength 的精确数学关系
- 人工系统中 storage strength 的可操作化定义
- Dreamer 的 subconscious entries 的 strength 分布历史数据（从未分析过）
