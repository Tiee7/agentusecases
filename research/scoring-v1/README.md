# 双轨评分 v1

本目录是独立扩展，不替代旧 completed v2 的七维商业分，不将两种分数线性互换。Schema 见 [dual-track-v1](../../schemas/dual-track-v1.schema.json)。

固定画像 solo-generalist-v1：单人经营者，普通低代码和基础脚本能力，无独家数据、品牌、现成客户或专业执照；商业验证四周、每周最多十小时、总现金 USD 200，人工机会成本 USD 25/小时。自用为普通知识工作者，月新增现金最多 USD 20、周维护最多一小时。专业或高频场景仅作敏感性说明，不替换主画像。

每维整数 0–4：0 必须有最低锚点的反向证据，2 为有限支持，4 为反复且强的实证。1、3 需解释介于相邻锚点的证据。缺证填 null，confidence=unknown，不以零分或低分占位。非空分数须引用实际来源并说明限制。

- 商业：demand_payment（具体付款人与付费痛点）、acquisition（可触达且已验证的渠道）、delivery_economics（含人工、维护及获客的交付经济）、differentiation（相对替代方案的便利或可积累差异）、validation_replication（可复核的小样本至多场景效果）
- 自用：audience_frequency（固定画像的任务与复用频次）、net_benefit（扣设置、复核、返工、维护与现金后的收益）、reliability（边界与错误恢复）、setup_maintenance（画像能力与维护预算）、cost_data_control（完整费用及权限、删除与迁移）

完整且有证据时每维折算 score×5，总计100。任一维缺证或 analysis_depth=brief，该轨 total 始终为 null，不发布部分总分或排名。confidence 不是成功概率；Wanted、评论数、搜索结果和源站编辑模板均不当销量或已验证效果。

本批十案均为简报，没有升级为完整深研。透明且有限的正贡献情景可支持 delivery_economics=2/low，但不是实际盈利证明。费用未知保留 null；所有现金预算判断同时列未计费用的条件。完整报告及译文见[简报索引](../brief/INDEX.md)，本次验收见[批次报告](../../reports/audits/spark-ten-case-acceptance-20261019.md)。
