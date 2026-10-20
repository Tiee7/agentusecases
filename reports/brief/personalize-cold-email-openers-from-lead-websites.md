# 用n8n读取线索网站并起草邮件开场白

## 中文

    根据线索网站个性化撰写冷邮件开场白
    一个n8n工作流通过Apify从Apollo获取线索，阅读每条线索的网站，让AI把个性化开场白写入电子表格，供发送工具使用。
    使用的是
    N8
    n8n
    他们做了什么
    作者重建了Nick Saraev的n8n系统。它获取线索，阅读线索的主页和最多两个重要页面，让AI总结并把开场白草稿写入Google Sheets，供发送工具使用。由于Apify的Apollo抓取器已废弃，他改用Podcast Index线索。通过OpenRouter调用的Claude为每条线索提取三项有来源的事实；在发送任何内容之前，他会阅读每份草稿。
    进展与成效
    Podcast Index每100条提供40条可用线索，而Apify来源每100条只有6到8条。每条优质线索的AI成本约为0.006美元。回复结果还没有出来，草稿读起来比较平淡。
    值得了解
    发送成本远高于AI：Smartlead每月39美元，Google Workspace每个邮箱8.40美元，邮箱预热需要数周。
    亲自尝试
    使用
    n8n
    复制提示词
    为我搭建一个工作流，从[电子表格或线索来源]读取线索，访问每条线索的网站[网站列]，并用AI为关于[我的产品或服务]的冷邮件写一句个性化开场白。把每句内容写到电子表格中该线索旁的新列，不要发送任何邮件。先测试5条线索，在运行完整列表之前给我看结果。
    原始来源：https://unpromptable.substack.com/p/ai-cold-email-system-tested

<details><summary>English original</summary>

    Personalize cold email openers from lead websites
    An n8n workflow pulls leads from Apollo via Apify, reads each lead's website, and has AI write personalized opening lines into a spreadsheet for a sending tool.
    Done with
    N8
    n8n
    What they did
    The author rebuilt Nick Saraev's n8n system. It pulls leads, reads a lead's homepage and up to two key pages, and has AI summarize them and draft opening lines into Google Sheets for a sending tool. Because the Apify Apollo scraper is deprecated, he swapped in Podcast Index leads. Claude via OpenRouter extracts three sourced facts per lead, and he reads every draft before anything is sent.
    How it went
    Podcast Index gave 40 usable leads per 100, against 6 to 8 from the Apify source. AI cost was about $0.006 per good lead. Reply results aren't in yet, and the drafts read flat.
    Worth knowing
    Sending costs far more than the AI: Smartlead is $39 a month, Google Workspace is $8.40 per inbox, and inbox warm-up takes weeks.
    Try it yourself
    with
    n8n
    Copy prompt
    Build me a workflow that reads leads from [spreadsheet or lead source], visits each lead's website [website column], and uses AI to write a one-sentence personalized opening line for a cold email about [what I offer]. Write each line into a new column next to the lead in my spreadsheet, and don't send any emails. Test it on 5 leads first and show me the results before running the full list.
    Original source: https://unpromptable.substack.com/p/ai-cold-email-system-tested

</details>


## 原作者的方法与来源

来源：[AI cold email system tested](https://unpromptable.substack.com/p/ai-cold-email-system-tested)

方法摘要未收录

## 简要分析

商业分数未评定；本篇不计完整深研。

### 需求与付款人

需要逐条阅读网站、准备针对性开场白的销售人员可能希望减少研究时间。付款人可能是销售团队或服务商，但没有客户付费、购买意愿或成交证据。可用线索不是有购买意向的客户。

依据：[Sdirectory](https://agentusecases.ai/use-case/personalize-cold-email-openers-from-lead-websites)

### 实际流程和工具

保留旧导语，同时以正文说明作者换成Podcast Index，不能继续宣传Apollo链路已成功。n8n编排、Claude经OpenRouter提取事实、Google Sheets存稿，人工逐条审核；现成模板不代表无需维护。

依据：[Sdirectory](https://agentusecases.ai/use-case/personalize-cold-email-openers-from-lead-websites)

### 数据能说明什么

40/100与6–8/100只是作者被转述的可用线索比例，定义、样本和筛选条件未独立核实。不得称5至6倍回复率或转化提升。每条good lead的模型成本也不包含人工、失败输入及发送。

依据：[Sdirectory](https://agentusecases.ai/use-case/personalize-cold-email-openers-from-lead-websites)

### 收入机制与交付

可假设按已核验草稿包或工作流实施收费，但须对事实可追溯和内容质量验收。不能承诺回复或约见。没有真实服务价格，不构造毛利。

依据：[Sdirectory](https://agentusecases.ai/use-case/personalize-cold-email-openers-from-lead-websites)

### 费用边界与可复算示例

假设一个灵活Workspace用户、Smartlead Base及100条good lead，并暂按转述模型成本，则39+8.40+100×0.006=48美元/月的局部小计。它不是报价或完整成本，仍缺n8n/采集、域名、验证、税费、人工和失败重跑；只起草不发送时并不必购买发送工具。

依据：[Ssmart](https://helpcenter.smartlead.ai/en/articles/439-smartlead-pricing-plans), [Sgoogle](https://knowledge.workspace.google.com/admin/billing/compare-flexible-and-annual-fixed-term-payment-plans), [Sdirectory](https://agentusecases.ai/use-case/personalize-cold-email-openers-from-lead-websites)

### 获客和替代

替代方案包括人工读网站写开场白或既有CRM流程。应先比较少量草稿的来源准确率与人工修改分钟数，而非扩大量。销售模板的复制门槛低，行业知识与事实审核更可能构成交付价值；本轮无外联。

依据：[Sdirectory](https://agentusecases.ai/use-case/personalize-cold-email-openers-from-lead-websites)

### 维护与失败恢复

限定允许读取的网站和页面数，限流可等待分批，但访问拒绝直接停该源。失败不应编造个性化，也不应重复写行。保存线索ID、来源URL、读取时间、稿件版本与审核状态。

依据：[Sn8n](https://docs.n8n.io/integrations/builtin/handle-rate-limits.md)

### 独立自用分析

适合愿意逐条审核、已有明确服务和合法数据来源的人。可能少些摘录，但草稿平淡意味着仍需编辑；无净省时。设置数据列、证据字段与人工审稿，按线索批次运行，维护页面变化与来源弃用。

依据：[Sdirectory](https://agentusecases.ai/use-case/personalize-cold-email-openers-from-lead-websites)

### 隐私和错误风险

同名企业、过期网页、虚构赞美和把播客线索当通用商业买家都会失真。事实来源公开不代表可无限采集、发送或共享联系人。预热数周是来源说法，不是投递成功保证；不要把读稿批准当所有后续发送许可。

依据：[Sdirectory](https://agentusecases.ai/use-case/personalize-cold-email-openers-from-lead-websites)

### 结论与下一步

仅建议受控试点。先用虚构或已获准的少量网站材料生成草稿，测事实引用是否正确、是否空洞、人工改稿耗时；本轮未运行。若资料无法核验或编辑成本不降，不扩大自动化。

依据：[Sdirectory](https://agentusecases.ai/use-case/personalize-cold-email-openers-from-lead-websites)

## 试用准备与预期结果

虚构公司网页材料、明确服务和预期事实。
每条开场白引用真实给定事实并保留未知项；本轮未试用。
只用给定虚构公司网页材料，为明确服务写一句开场白并附事实出处；没有证据则留空说明。不要采集真实联系人、写入外部表格、连接发送工具或发送邮件。

## 来源

- [许可目录冷邮件开场白案例](https://agentusecases.ai/use-case/personalize-cold-email-openers-from-lead-websites)：导语Apollo/Apify与正文改用Podcast Index须分开；40/100对6–8/100、$0.006/goodlead均目录转述，回复未有结果且草稿平淡。
- [Smartlead价格说明](https://helpcenter.smartlead.ai/en/articles/439-smartlead-pricing-plans)：2026-10-20读取更新2026-08-21页面：Base起$39/月，6K发送和2K联系人存储，部分验证等附加项另收费。
- [Google Workspace计划价格](https://knowledge.workspace.google.com/admin/billing/compare-flexible-and-annual-fixed-term-payment-plans)：Business Starter灵活计划$8.40/月/用户，年承诺$7/月/用户，提前取消需付剩余承诺；地区和优惠另核。
- [n8n限流处理](https://docs.n8n.io/integrations/builtin/handle-rate-limits.md)：提供重试、等待和分批处理方法；技术重试不授予目标站数据访问或绕限制权限。
