# Claude Code 整理扣除项与 Schedule C

案例来源：https://agentusecases.ai/use-case/compile-deductions-and-schedule-c-with-claude-code
研究日期：2026-10-14
状态：draft · 证据置信度：低；仅核对聚合站详情

这是一份初步案头研究：已读取案例详情，原始报道被云环境网络策略拦截；没有运行项目或验证金额、效果与现时产品可用性。维度分数是基于这些有限材料的研究判断，不是性能测评或最终结论。

案例描述 Chris Blattman 用 Claude Code skills 搜索 Gmail 税务附件、汇总捐赠与信用卡记录、生成税务软件可用表格和 Schedule C。医疗与托儿费用分类仍由本人检查，并手动输入税务软件。站点转述约三小时完成，相比会计报价约1,000美元。

| 维度 | 权重 | 分数（0–5） | 依据 |
|---|---:|---:|---|
| 需求价值 | 25% | 4 | 收集凭证和对账是具体重复工作，输出可以交给已有税务流程。 https://agentusecases.ai/use-case/compile-deductions-and-schedule-c-with-claude-code |
| 效果证据 | 25% | 1 | 指向个人工作流文章，但原文尚未读取；没有原始输入、技能代码或对照样本。 https://agentusecases.ai/use-case/compile-deductions-and-schedule-c-with-claude-code |
| 落地可行性 | 20% | 4 | 任务被拆成提取、缺失追踪、汇总、人工分类和手动填报，流程比整套自动报税更可检查。 https://agentusecases.ai/use-case/compile-deductions-and-schedule-c-with-claude-code |
| 成本与维护 | 15% | 3 | 三小时与约1,000美元是单人陈述，并非同范围成本实验；模型和维护费用未单列。 https://agentusecases.ai/use-case/compile-deductions-and-schedule-c-with-claude-code |
| 风险控制 | 15% | 3 | 案例明确保留人工检查与手动填报，但云端模型读取本地文件仍有敏感信息处理问题。 https://agentusecases.ai/use-case/compile-deductions-and-schedule-c-with-claude-code |

综合评分：59.0/100

## 分析与建议

首批最值得优先复现：先做“凭证清单、缺失追踪、分类草稿、合计核对”，保留人工签核。初评分针对该受限流程，不代表税务准确率。

## 待验证问题

- 原始 skills 或工作流是否公开，授权范围如何限制？
- 相同输入复跑是否产生一致合计？哪些分类需要专家？
- 三小时是否包含最终复核，模型调用和后续维护成本是多少？

## 下一步实验

使用10份合成收据与一份人工标准表，比较字段提取、去重和合计；禁用邮箱写入和自动填报。

## 来源核验

- https://agentusecases.ai/use-case/compile-deductions-and-schedule-c-with-claude-code：已读取公开详情；网站为二手案例整理
- https://claudeblattman.com/tax-workflow/：原始报道未读取：代理网络返回403
