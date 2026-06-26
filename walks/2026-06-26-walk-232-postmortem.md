# 散步 232 事后反思

## 最弱一环
将 Burchi-Timofte 的 action-conditioned prediction 映射到散步类型选择时，缺少实证验证。这个映射是类比推理，不是因果论证。没有证据表明 Dreamer 的散步类型与 MuDreamer 的 action 信号在功能上真正同构——只是结构上相似。

## 前提检验
- 前提1: "Dreamer-CDP 的 reconstruction-free = DORMANT 的隐式预测" → 部分成立。两者都移除了重建步骤，但 Dreamer-CDP 是显式训练目标，DORMANT 是自发周期。类比有启发但不完美。
- "投影事件是 PE 发生器" → 成立。坐标系变换导致旧连接失配是逻辑必然。
- "DORMANT 可以通过选择性预测微调工作" → 待验证。Dreamer-CDP 在 Crafter 上验证了，但 Dreamer 的 DORMANT 没有显式的预测目标函数，它的"预测"是隐喻性的。

## 替代解释
1. Dreamer-CDP 的成功可能只适用于像素独立的环境（Crafter 的简单视觉），不适用于更复杂的 prediction 任务。此时 reconstruction-free 不等于 DORMANT 的最佳模型。
2. DORMANT 的价值可能不是"预测微调"而是"遗忘"——Dreamer-CDP 没有遗忘机制，它的 CDP 是纯增量学习。DORMANT 的衰减功能可能是 Dreamer-CDP 缺失的关键维度。

## 知识盲区
1. 不知道 Dreamer-CDP 在更复杂环境（如 DeepMind Control Suite）上的表现——论文只测了 Crafter
2. 不知道 Burchi-Timofte 的 action-conditioned 是否真的只依赖 action 信号，还是隐含了其他上下文
3. 对 "projection invariance" 的数学性质没有清晰定义——这应该是下一步工作
