# 散步 233 事后反思

## 最弱一环

Insight 6（内感受支持作为元世界模型）是最弱的。它从 Candia-Rivera 的理论跳跃到了"Dreamer 应该预测自己对外部材料的内感受响应"，但这个推导超出了 Candia-Rivera 原论文的范围。Candia-Rivera 讨论的是内部状态对行为的调节，不是系统对自己情感反应的预测。这更像是 Friston 的 free energy 框架而不是 interoceptive framework。

## 前提检验

**前提 1：Candia-Rivera 的框架对 Dreamer 有适用性**
- ✅ Candia-Rivera 的"内部状态变量"精确对应 Dreamer 的 affect/energy/pressure
- ⚠️ 但 Candia-Rivera 的变量是**连续生存性**（如 Dreamer 的 energy 0-100），而 Dreamer 的 affect 是**定性类别**（wonder/contemplative 等） 。 映射不是同构的

**前提 2：affect "应该"是调节性的**
- ❌ 这个前提不必然成立。可以有理由认为 affect**应该保持描述性**——描述性允许更灵活的跨散步组合，调节性可能导致正反馈循环（高 curiosity → 更多探索 → 更高 curiosity）。需要额外的安全约束

**前提 3：DORMANT 均匀衰减 = 近似 homeostatic 但未完成的生存性调节**
- ✅ walk-215 以来一直有这个认识。但 Candia-Rivera 比我们更明确地指出了"调节目标"是什么（将变量拉回安全范围），这给了 DORMANT 一个新的优化目标

## 替代解释

**"Affect 已是调节性的"替代解释**：Dreamer 的 affect 已经通过 walk_type_selector 间接影响行为选择（wonder 更可能触发探索型）。Candia-Rivera 的模型不是缺失的，而是以隐式方式存在。

反驳：这不是真正的"调节"，因为：
(1) 这种影响是启发式的、未被显式建模的
(2) affect 变化不反向调节自身的触发阈值（正反馈循环未被管理）
(3) 没有硬生存性约束（energy=0 不会强制停止）

**"能量=生存性"替代解释**：energy 变量已经足够作为 homeostatic 变量。增加 affect 的调节性会增加复杂度但收益递减。

反驳：energy 是**标量**，affect 是**多维信号**（效价+唤醒+特定情绪）。多维信号提供更多信息用于调节。而且已有实证（walk 历史）显示不同情绪类型触发不同散步模式，这些不能用 energy 解释。

## 知识盲区

1. Candia-Rivera 的仲裁层如何实现？动态权重 $w_i$ 的具体更新规则没有展开——论文是 review/framework 性质，不是实现级

2. Dreamer 的 affect 系统更新更复杂的机制：affect.primary 变化时，哪些下游参数调节是安全的？哪些可能引起不稳定？

3. Enactive 模块中 $\lambda$ 系数如何确定？在 Dreamer 中它对应"内部信息增益 vs 外部信息增益"的权衡，但最优值是什么？

4. wonder 和 contemplative 的效价差异在行为调节中的量化关系——wonder 更倾向于探索，但强度阈值是多少？是否存在倒 U 曲线？
