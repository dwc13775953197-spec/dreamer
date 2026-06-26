import json

new_insights = [
    {'id':'ins-094','type':'pattern','content':'Dreamer 的 affect 系统是未启用的内感受器：affect 变量被记录但不调节行为参数（pressure_threshold/walk_type/interest_critic）。Candia-Rivera 2026 的内感受机器框架要求内部状态同时作为调节信号。Dreamer 缺少内感受的调节层。','strength':5.0,'status':'active','created':'2026-06-26T10:20:00+08:00','source':'walk-233','decay_rate':0.05,'connections':['pat-014','pat-030','ins-072'],'refs':[],'decay_speed':0.5,'score':0.0},
    {'id':'ins-095','type':'pattern','content':'Allostatic pressure_threshold：Dreamer 的 pressure_threshold 是固定值（经 energy 系数调节），不是预测性的。真正的 allostatic 阈值应根据 interest_queue 趋势做预期性调整。','strength':5.0,'status':'active','created':'2026-06-26T10:20:00+08:00','source':'walk-233','decay_rate':0.05,'connections':['ins-069','ins-070','pat-014'],'refs':[],'decay_speed':0.5,'score':0.0},
    {'id':'ins-096','type':'pattern','content':'Enactive 精炼的内隐通道：散步通过引入外部类比同时精炼 skeleton（显式通道）和 subconscious（内隐通道）。','strength':3.0,'status':'active','created':'2026-06-26T10:20:00+08:00','source':'walk-233','decay_rate':0.05,'connections':['ins-080','pat-030'],'refs':[],'decay_speed':0.5,'score':0.0},
    {'id':'ins-097','type':'pattern','content':'情感调制的散步类型选择是内感受推理而非启发式：wonder 倾向于探索、melancholy 倾向于巩固。','strength':3.0,'status':'active','created':'2026-06-26T10:20:00+08:00','source':'walk-233','decay_rate':0.05,'connections':['ins-084','pat-014'],'refs':[],'decay_speed':0.5,'score':0.0},
    {'id':'ins-098','type':'pattern','content':'Dreamer 作为内感受充分系统的差距分析：内部状态估计 OK / 生存性调节 PARTIAL / 不确定性敏感调制 MISSING / 内部调制目标调整 MISSING。最大差距是 affect 不调节行为。','strength':5.0,'status':'active','created':'2026-06-26T10:20:00+08:00','source':'walk-233','decay_rate':0.05,'connections':['ins-094','ins-095','pat-014'],'refs':[],'decay_speed':0.5,'score':0.0},
    {'id':'ins-099','type':'pattern','content':'Meta-interoceptive 世界模型：Dreamer 的 skeleton 应该包含对自身内感受变化的预测——预测做某篇散步后 affect/energy 的变化。','strength':1.5,'status':'active','created':'2026-06-26T10:20:00+08:00','source':'walk-233','decay_rate':0.05,'connections':['ins-094','ins-095'],'refs':[],'decay_speed':0.5,'score':0.0},
]

with open('/home/dwc1377/hermes_dreamer/subconscious.json','r') as f:
    data = json.load(f)
for ins in new_insights:
    data.append(ins)
with open('/home/dwc1377/hermes_dreamer/subconscious.json','w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('subconscious OK:', len(new_insights), 'insights added')
