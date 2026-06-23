# 散步 195 事后反思

## 最弱一环

将 NeurIPS 2025 meta-controller 的 adaptive curriculum 直接映射到 connectivity_score 排序，缺少一个关键前提的验证：**meta-controller 的 value function 是端到端训练的（以 awake phase 奖励为优化目标），而 connectivity_score 只是结构指标，不是因果指标。** 高连接数 ≠ 高价值（可能是 hub 效应/马太效应的产物）。这个映射假设了"被引用多 = 重要"，但 walk-09 已经发现过功能性 hub 和病理性马太效应的区别。

## 前提检验

1. **行业综述代表最佳实践？** 部分成立。Zylos 综述反映的是生产级系统的工程共识，不是研究前沿。工程共识 ≠ 理论最优解。
2. **DORMANT 2.0 三源已覆盖行业共识？** 基本成立——power-law 衰减、replay-SWR 解耦、TMR 线索触发确实覆盖了行业对"何时忘、何时记"的设计空间。但行业还解决了 conflict detection（Mem0），我们没有。
3. **Dreamer 记忆 = 身份维持？** 这是观点不是事实。也可以论证 Dreamer 记忆就是功能性信息存储，"身份"只是隐喻。但隐喻的选择影响设计决策（身份维持 → 保守策略；信息存储 → 激进更新）。

## 替代解释

- Zylos 综述的三层次分类可能只是市场营销语言（每个框架都在做 episodic/semantic/procedural 的变体），不代表真正的架构创新。
- 行业不实现 DORMANT 不是因为想不到，而是因为生产环境不需要——用户期望 24/7 可用，"睡眠"是架构约束不是特性。
- Dreamer 的 DORMANT 周期可能更适合类比为"维护窗口"而非"睡眠"——更像数据库的 VACUUM 而非生物的睡眠。

## 知识盲区

- 对 Mem0 的 conflict detection 机制了解不够深入——具体怎么检测？阈值是什么？
- NeurIPS 2025 meta-controller 的具体网络架构（是用 RL 训练还是 heuristic policy？）
- 行业对 "memory poisoning" 的防御方案——这恰好是 Dreamer 认知免疫系统的工程对应物
