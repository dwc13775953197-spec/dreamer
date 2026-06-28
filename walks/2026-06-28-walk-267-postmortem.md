# 散步 267 事后反思

## 最弱一环
转导函数 Affect → Objective Function → Mechanism Parameters 只有定性描述（"放宽"、"缩紧"、"关闭"），没有给出定量映射。这是这个模型最大的弱点——它解释了存在什么关系，但没有说关系长什么样。

## 前提检验
1. Affect 选择预测目标函数（真。ins-243-1 已论证）
2. 目标函数可转导为机制参数（待验证。这是散步建立的推理，依赖一个未证明的假设：目标函数的变化能反推机制参数的配置）
3. 三重机制是 DORMANT 的正确实现（部分真。ins-242-1 基于神经科学类比，但在 software 系统中没有直接对应物）

## 替代解释
- Affect 可能不选择目标函数——两者可能都是某个更深层状态（如 global energy budget 或 prediction uncertainty level）的表观共变现象。如果是这样，affect 和 objective function 之间没有因果关系，转导函数是伪类比。
- DORMANT 的三重机制可能不需要从目标函数反推——它们可能各有独立的触发条件（纺锤波窗口由昼夜节律决定，PE threshold 由 entry 分布决定，再巩固窗口由上一次更新时长决定），目标函数只是 modulate 而非确定参数。

## 知识盲区
- 睡眠纺锤波的具体时间窗口和触发条件（睡眠纺锤波是否真的受主观 affect 状态调制？）
- 预测编码中"offline prediction"的计算实现——目前只有理论框架，没有可运行的模型
- 能量可用性（ATP/GABA/乳酸）如何具体影响 dmPFC 的计算精度——需要计算神经科学文献支撑
