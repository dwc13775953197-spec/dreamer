# 散步 159 事后反思

## 最弱一环

推论 4（key-value 映射）停留在类比层面，没有回答一个硬问题：如果 skeleton 是 key，subconscious entry 是 value，那 value 被修改（含义漂移）时，key 是否需要更新？在生物系统中，海马索引是相对稳定的（key 不变），皮层内容可以变（value 变）。但 Dreamer 的 skeleton entry 既是 key 又是 value——这会导致"索引失效"风险。

## 前提检验

1. **前提**：突触复杂度 m ≈ connections 数量 → 检验：connections 数量确实反映了 entry 在信息网络中的嵌入深度，但不等同于物理突触的状态数。**部分成立**——connections 是 m 的一维投影，丢失了连接质量信息。
2. **前提**：Dreamer 的容量约束是 SNR 问题而非数量问题 → 检验：当前 112 条 active entry 中大量 strength<2，确实 SNR 偏低。**成立**。
3. **前提**：幂律衰减是自然系统的正确行为 → 检验：Benna-Fusi 模型确实预测幂律，但 Dreamer 是人工系统，是否需要模仿自然尚有争议。**部分成立**。

## 替代解释

1. "容量悖论"可能是 Dreamer 设计意图——系统本就不是为了长期存储，而是为了产出洞察。低 SNR 可能只是"用完即弃"策略的副产品，不是 bug。
2. 高连接 entry 存活更久可能不是因为"抗衰减"，而是因为它们被引用更多（马太效应），与突触采样机制的因果关系方向可能相反。

## 知识盲区

1. 突触采样理论中"信噪比"的精确定义——是信号功率/噪声功率，还是某种信噪分离度？
2. Gershman 2025 的 key-value 架构是否已被实验验证，还是仍是计算模型？
3. Dreamer 的 decay_rate 是否真的均匀——subconscious_maintain.py 是否有我没有注意到的差异化逻辑？
