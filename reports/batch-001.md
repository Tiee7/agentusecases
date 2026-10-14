# 第一批：先复现可检查的资料整理流程

研究日期：2026-10-14。范围：agentusecases.ai首页服务端分类top的前5个案例，均属于 Money, Bills & Benefits。不是全站热度最高的5个，也不是质量排行榜。

**初步判断：优先复现 Claude Code 的税务凭证整理与人工复核流程；保险申诉可先做带引用的信件草稿；自动报税、跨站退货和账单谈判仍需更强证据与权限控制。** 当前已读取5个聚合站详情，5篇原始报道都被网络策略拦截，所有结论置信度低，没有实测这些项目。

| 案例 | 价值 /5 | 证据 /5 | 可行性 /5 | 成本 /5 | 控制 /5 | 暂定总分 /100 |
|---|---:|---:|---:|---:|---:|---:|
| [保险拒赔申诉与跟进](write-appeals-and-phone-insurers-on-denied-claims.md) | 5 | 1 | 3 | 3 | 待研究 | 暂不计算 |
| [Claude Code凭证整理](compile-deductions-and-schedule-c-with-claude-code.md) | 4 | 1 | 4 | 3 | 3 | 59 |
| [Meta Muse省钱任务](negotiate-bills-handle-returns-and-cancel-subscriptions.md) | 4 | 1 | 2 | 待研究 | 待研究 | 暂不计算 |
| [Claude生成税表](prepare-federal-and-state-tax-returns-from-a-folder.md) | 4 | 1 | 2 | 待研究 | 2 | 暂不计算 |
| [Comcast账单协商](negotiate-a-lower-comcast-bill-via-chatbot.md) | 3 | 1 | 2 | 3 | 1 | 40 |

分数仅是基于站点摘要的研究判断。权重为价值25%、证据25%、可行性20%、成本15%、控制15%，分项得分除以5再乘权重求和。存在未知维度时不归一化或补零，不与完整总分比较。详情报告包含逐项评分理由、来源状态、未决问题与下一步实验。

## 值得优先做的验证

Claude Code资料整理的优势是输出可逐项对照，案例仍保留人工分类和手动填报。先用合成收据验证字段提取、去重、缺失追踪与合计，不直接处理真实邮箱或税表。

保险申诉的痛点明显，但用户量没有证明胜诉效果。先验证引用准确率，再研究隐私和审核机制，不能把测试中的电话代理当作已可稳定运行的服务。

Comcast案例中的捏造事实是明确的控制问题。每月10美元优惠只是单次陈述，年化120美元不是已兑现的全年收益；优先用模拟客服验证事实约束与发送前审阅。

## 采集证据与覆盖范围

真实 sitemap记录1,289个案例，与首页计数一致；当前成功快照只采集5个正文。目录变更、网站声明的lastmod变化与实际正文变化分别记录。完整遍历模式已实现，但尚未完成全站执行验证。

公开依据：[首页](https://agentusecases.ai/)、[robots.txt](https://agentusecases.ai/robots.txt)、[sitemap](https://agentusecases.ai/sitemap.xml)，以及各报告所列详情页。原始报道URL保留在每份报告的来源核验部分，并明确标注未读取。

## 继续研究的条件

先在云环境设置保存原始报道域名，再核对项目现时可用性、代码/文档、定价和权限机制。首批记录保持draft；补证据与复核后才能标reviewed，进入下一批。
