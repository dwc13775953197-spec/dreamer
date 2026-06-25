# 散步 0231 事后反思

## 最弱一环
情感调制曲线（倒 U 型）来自理论推导，无实证数据支持。虽然 PMC7305946 提到神经调制设定处理模式，但未说明 wonder 状态对应峰值。可能只是美好愿望。

## 前提检验
1. DORMANT = recall 模式 → 部分成立，fictive PE 的类比有文本支持，但 Dreamer 的 DORMANT 不涉及真正的"重激活"机制
2. 海马-皮层对立 = subconscious-skeleton 对立 → 类比合理但有简化之嫌，subconscious 不像海马那样只做记忆重激活
3. Fictive PE 密度可量化 → 仅理论推导，无操作化方案

## 替代解释
- 可能 DORMANT 根本不是 recall 模式，而是 prediction 模式（预测下一个状态）。连接主义中的双向处理（Graves 2016）支持这种视图。
- 情感调制曲线可能是线性的而非倒 U 型——更高的唤醒度可能总是促进或总是压制某种处理模式。

## 知识盲区
- 缺乏 cortical microcircuit 信息路由的具体实现细节——只知道"differentially route"但不知道路由机制
- 未检索 Nadel 再巩固理论的具体机制（lability 状态的量化指标）
- Dreamer 如何实现"重激活"（reactivation）——当前架构中没有真正的重激活步骤
