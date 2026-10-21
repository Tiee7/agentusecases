# 用 Claude Code 汇总发布变更与产品 KPI 周报

## 中文

    生成结合 KPI 与拉取请求的定期周报
    一位产品负责人用 Claude Code 自动生成定期报告，分析开发人员交付了什么，以及功能帮助还是损害了 KPI。
    使用工具
    CC
    Claude Code
    做了什么
    产品负责人 David Kelly 在 Metabase 仪表盘跟踪每款产品的 KPI。他提示 Claude Code 构建一个系统，拉取每周 GitHub 拉取请求，将其与各期 KPI 变化进行比较，并为每个拉取请求影响每项 KPI 的可能性评分。他通过 Zen MCP 工具连接 OpenAI 和 Gemini API，让多个模型交叉核查分析。他公开了完整提示词。
    结果如何
    他获得每周报告，了解已发布功能是否帮助或损害了 KPI，并据此迭代。文章没有提供这些相关性判断的准确率数据。
    值得了解
    需要付费 Claude 方案。他建议每月20美元的 Pro 方案，并建议不要用 API，因为费用可能迅速累积。
    亲自试用
    使用
    Claude Code
    复制提示词
    每到[周一早晨]，拉取[仓库名称]过去一周已合并的拉取请求，以及来自[KPI来源，例如CSV或仪表盘导出]的KPI数字。写一页报告，说明交付了什么、哪些功能可能帮助或损害了[KPI名称]、下周需要关注什么。保存为[文件路径或格式]，在设置任何定期计划或向任何人发送之前，先给我看初稿。
    原始来源：https://dmkthinks.org/blog/claude-code-examples/

<details><summary>English original</summary>

    Generate recurring weekly reports combining KPIs and pull requests
    A product leader uses Claude Code for automatic recurring reports on what developers shipped and whether features helped or hurt KPIs.
    Done with
    CC
    Claude Code
    What they did
    David Kelly, a product leader, tracks KPIs for each product in a Metabase dashboard. He prompts Claude Code to build a system that pulls weekly GitHub pull requests, compares them with period-over-period KPI changes, and scores how likely each PR affected each KPI. He connects Zen MCP tools to the OpenAI and Gemini APIs so several models cross-check the analysis. He publishes the full prompt.
    How it went
    He gets a weekly report on whether shipped features helped or hurt KPIs, and he uses it to iterate. The post gives no accuracy figures for the correlations.
    Worth knowing
    A paid Claude plan is needed. He suggests Pro at $20 a month and advises against the API because costs can add up quickly.
    Try it yourself
    with
    Claude Code
    Copy prompt
    Every [Monday morning], pull the pull requests merged in [repo name] over the past week and our KPI numbers from [KPI source, e.g. a CSV or dashboard export]. Write a one-page report of what shipped, which features likely helped or hurt [KPI names], and what to watch next week. Save it as [file path or format] and show me the first draft before setting up any recurring schedule or sending it to anyone.
    Original source: https://dmkthinks.org/blog/claude-code-examples/

</details>

## 原作者的方法与来源

来源：[David Kelly：2025年9月20日非编码用途](https://dmkthinks.org/blog/claude-code-examples/)

作者方法摘要

1. 在定期报告中结合各期KPI比较与GitHub变更。
   English summary: Combine period KPI comparisons with GitHub changes in recurring reports.

2. 用Zen连接的模型交叉检查分析，但没有公开准确率测量。
   English summary: Use Zen-connected models to cross-check analysis, without published accuracy measurements.

## 我们的分析

**商业结论：适合内部效率工具。把周报当成会前资料与解释候选，不自动认定功能影响**

结论是适合内部效率工具，暂不把它包装成自动判定开发贡献的商业产品。使用者通常是要主持产品例会的人，真正预算所有者可能是产品负责人或工程管理者，但这只是目标客户假设，不是已签单画像。需要先判断他们是否已能获得稳定的发布记录和指标定义；没有这些基础，付费需求更像数据治理而非写周报。交付的价值应是减少会前拼接资料并暴露待核问题，不能以PR数或代码行数代替业务价值。多产品团队的周期性复盘可产生重复需求，单仓库、低频发布团队则未必需要新服务。采购时还需数据所有者和安全人员允许源代码与指标进入指定模型环境，这些审批时间应纳入售前而非留给客户免费承担。没有已付价格、续费或预算数据，因此本研究不给付费需求量化评分。以一份无需新增敏感访问的历史导出包做示范，可以验证资料整理需求，但示范被阅读或称赞仍不是订单。

案例ID：`generate-recurring-weekly-reports-combining-kpis-and-pull-re` · 案例来源：https://agentusecases.ai/use-case/generate-recurring-weekly-reports-combining-kpis-and-pull-re
研究时间：2026-10-21T12:25:09.661110+00:00

**商业评分：未评定；缺证不补零，不生成总分。**

| 维度 | 权重 | 分数 /5 | 商业依据 |
|---|---:|---:|---|
| 付费需求 | 20% | 待核实 | 只有公开个人用法，未见预算所有者实际采购与续费证据；目标人群需求可界定，但不能据此补商业需求分。 [Sauthor] |
| 业务价值与效果证据 | 20% | 待核实 | 报告流程有自述，未见同条件计时与归因校准；模型共识不能弥补因果识别，效果分暂不评定。 [Sauthor, Scausal] |
| 单位经济与利润 | 20% | 待核实 | 可计算假设成本但实际售价、失败重试与一次性接入工时未知，不把低模型费用当作利润证据。 [Scost, Spal] |
| 获客与市场进入 | 15% | 待核实 | 未取得付费获客、成交渠道或采购周期，已有服务关系仅是验证路径设想，不是已运行漏斗。 [Sauthor, Spermissions] |
| 竞争壁垒 | 10% | 待核实 | 原生定时订阅与开源多模型组件已存在；客户指标映射可能形成价值，但缺留存与独占资产证据。 [Smetabase, Spal] |
| 交付与经营风险 | 10% | 待核实 | 通知权限与数据解释有可识别风险，尚无本案生产恢复和边界实测，不用文档存在给交付可靠性打分。 [Spermissions, Scausal] |
| 独立用户反馈信号 | 5% | 0 | 未取得本案独立效果验证；历史Metabase求助只是相邻流程，所以独立反馈信号为0而非满意度为零。 [Sfeedback, Srender] |

## 自用价值：中

定性推断：对已有清晰指标与发布记录的产品负责人有汇总价值，必须人工检查；量化收益未证。

依据：Sauthor, Smetabase, Scausal

- 适用人群：已有GitHub发布记录和稳定指标口径的产品负责人。
- 用途：准备复盘材料与列出待核解释。
- 预期收益：可能减少资料拼接，不保证发现真因或提高收入。
- 设置成本：定义指标、周期、发布映射和只读数据范围。
- 维护成本：数据口径、权限、供应商费用与异常复核。
- 使用频率：随周会或月度复盘重复。
- 隐私风险：代码、产品指标和人员信息被不当发送或传给外部模型。
- 错误风险：把合并当发布、把相关当因果、混用未成熟人群。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/generate-recurring-weekly-reports-combining-kpis-and-pull-re

建议工具：Claude Code

    Every [Monday morning], pull the pull requests merged in [repo name] over the past week and our KPI numbers from [KPI source, e.g. a CSV or dashboard export]. Write a one-page report of what shipped, which features likely helped or hurt [KPI names], and what to watch next week. Save it as [file path or format] and show me the first draft before setting up any recurring schedule or sending it to anyone.

自编试用模板

准备条件：两个已结束周期的脱敏PR和指标导出、口径、时区及人工基线；不提供凭据。

工具：Claude Code与本地文件；多模型不是前置，不运行付费API。

预期结果：可核查清单、变化描述、解释假设和未知项，未实测。

### 源站Copy prompt

原文模板

出处：https://agentusecases.ai/use-case/generate-recurring-weekly-reports-combining-kpis-and-pull-re

依据：Sdirectory

    Every [Monday morning], pull the pull requests merged in [repo name] over the past week and our KPI numbers from [KPI source, e.g. a CSV or dashboard export]. Write a one-page report of what shipped, which features likely helped or hurt [KPI names], and what to watch next week. Save it as [file path or format] and show me the first draft before setting up any recurring schedule or sending it to anyone.

### 只读验证模板

自编模板

出处：研究团队自编

依据：

    只读我提供的脱敏PR与KPI导出。先核日期时区、指标定义和缺失字段，再列变更与数值变化；每条带来源。区分已部署、仅合并和未知。解释只标假设，列同期其它因素，不评价员工、不编造因果概率。保存一页草稿及错误清单，不发送、不建调度、不修改输入，不访问其他系统。

## 已核验事实

- 作者公开了KPI与PR周期分析的使用方法，但没有提供可复验准确率或付费客户证据。 [Sauthor]
- 目录建议的试用模板要求先看草稿，再设置计划或发送；它不是实际已执行证据。 [Sdirectory]
- Metabase已有邮件与Slack的周期仪表盘送达功能，不需要新建代理才能生成定期通知。 [Smetabase]
- Metabase通知数据按创建者权限展示，不能把收件人平台权限等同已发送内容的过滤器。 [Spermissions]
- Microsoft Research指出因果识别需要反事实思考，单纯相关模式可能误导决策。 [Scausal]
- 原Zen项目链接现转到PAL，README有多模型consensus与供应商接入说明，但未证明本案分析正确。 [Spal]
- Claude Code现行成本说明区分订阅额度、额外用量及API计费，不宜把历史月费当全链路总费。 [Scost]
- 2023年Metabase用户曾报告订阅管理权限困难，这是相邻历史流程反馈而不是本案效果评价。 [Sfeedback]

## 客户、付款人与预算边界

结论是适合内部效率工具，暂不把它包装成自动判定开发贡献的商业产品。使用者通常是要主持产品例会的人，真正预算所有者可能是产品负责人或工程管理者，但这只是目标客户假设，不是已签单画像。需要先判断他们是否已能获得稳定的发布记录和指标定义；没有这些基础，付费需求更像数据治理而非写周报。交付的价值应是减少会前拼接资料并暴露待核问题，不能以PR数或代码行数代替业务价值。多产品团队的周期性复盘可产生重复需求，单仓库、低频发布团队则未必需要新服务。采购时还需数据所有者和安全人员允许源代码与指标进入指定模型环境，这些审批时间应纳入售前而非留给客户免费承担。没有已付价格、续费或预算数据，因此本研究不给付费需求量化评分。以一份无需新增敏感访问的历史导出包做示范，可以验证资料整理需求，但示范被阅读或称赞仍不是订单。

依据：Sauthor, Spermissions

## 数据链路与可核验的交付

建议的复制链路从固定报告周期、时区、指标定义和版本开始：读取授权导出的PR元数据、实际发布记录与KPI，再做去重和缺失检查，最后由模型写解释候选。合并PR时间不等于用户实际接触新功能的时间，还可能存在灰度、回滚和开关；这属于研究者提出的控制点，原文章没有证明已经覆盖。每条解释应引用变更链接、数据时间窗、分子分母和适用人群，列出同期其它变化与未知项。人工只需核查关键解释和异常，但必须能够回到原始记录。失败恢复按产品与周期保存状态，数据抓取失败应显示缺失，而不是用上周值生成貌似完整的周报；重跑同一期不自动重复发送。报告先存草稿，由负责人确认后才分发。如此形成的产物是可追溯的会议准备材料，不是自动发现真因的仪器。 建议输出一个覆盖表：本期实际发布总数、成功取得详情数、缺失数、指标导出截止时间与是否过完整观察窗。每项状态须来源于输入，不能由模型估计。如果发布记录缺少用户曝光信息，报告直接写未建立时间关联。人工纠正应附原理由，下一轮沿用已确认口径而不是让模型重新猜。

依据：Sdirectory, Smetabase, Scausal

## 可进入需求与不能估出来的市场

公开案例说明至少有人把此类工具用于产品管理，但无法据一名负责人推导市场规模、付费率或行业平均节省。可进入范围应收窄到已使用GitHub且已有可导出产品指标的团队，避免一开始同时做埋点、数仓、权限和经营咨询。验证问题也要分层：客户究竟缺少数据送达、缺少发布上下文，还是缺少能解释指标的分析师？只有第二类与本方案最贴近，第一类已有原生订阅，第三类可能需要实验设计和业务分析而不是更多模型。季度或月度预算审查与每周产品会议的需求不同，不能把报告频率当续费承诺。可在已有技术服务项目内以脱敏历史材料做小样，记录客户提出的实际纠错和下一步问题。若最常见要求变成自动评价员工薪酬或承诺提升收入，应先重新界定服务，不以未经校准的分数承担这类结果。

依据：Sauthor, Smetabase, Scausal

## 原生仪表盘、人工复盘和多模型工具

Metabase已有定时送达能力，所以只把图表截图写成邮件的产品很容易被替代。它与本案的差别在于是否把发布上下文整理进同一份材料，而不是是否支持周一发送。另一条基线是负责人拿发布清单和原仪表盘人工复盘，优势是熟悉活动背景，代价是时间；本轮没有同条件耗时测量，不能先判代理便宜。PAL提供多模型讨论组件，降低技术拼接门槛，却不提供本团队指标的真实因果标签。多位模型从相同错误输入得出相同结论，并不构成独立业务证据。客户迁移成本主要在指标口径、权限、产品映射和复盘习惯，不在提示词长度。应把自动汇总、可解释假设和已验证影响显示成不同状态，避免为了与仪表盘区分就夸大解释能力。

依据：Smetabase, Spal, Scausal

## 两种以验收周报为单位的成本

每个情景以一份一个产品的核对周报为单位，全部数值为研究者假设，不是任何服务商报价。轻量：模型及工具摊销2美元、人工15分钟按40美元/小时计10、其他可变1、获客摊销2，合计15美元；每月16份加固定维护40，合计280美元。高维护：多模型与工具8、人工60分钟计40、其它5、获客8，单位61美元；同样16份加固定维护120，合计1096美元。实际服务售价未知，故利润、毛利率与盈亏平衡销量都不计算。设置接入和历史口径清理尚未量化，应单独登记一次性工时，不隐含为零。模型费用只是成本一项，解释错误后的返工、管理者审阅和安全审批可能占更多。Claude订阅与外部供应商调用须分别看实际账单；历史20美元建议不能覆盖所有路径。只有在相同输入和验收要求下比较总人工分钟，才能判断哪种场景更接近客户。 还需区分固定订阅被多个任务共享与新增付费调用的增量成本，避免重复摊销。若按客户包月报价，每份报告的返工和未完成任务仍消耗成本；不能只以成功报告作为分母而漏掉失败尝试。建议试点记录设置、正常运行、异常恢复三类工时，再决定一次性设置费与周期服务费是否需要分开。

依据：Scost, Spal

## 获客与交付包装

首批验证可从既有数据分析或工程交付关系切入，因为接入私人仓库和业务指标需要信任。此处是经营建议，不是本研究已经触达客户。演示内容先使用合成数据或客户明确可分享的历史导出，不要求完整生产数据库权限；成果只交给指定负责人。一个合理的试点交付包括指标字典、发布映射、带来源的一页报告及错误清单，约定哪些问题仅列假设，哪些必须人工核实。不要把自动发邮件作为价值的核心，原生产品已经能做，也不能以模型写得流畅推定高层愿付。若客户只需要每周固定图表，直接配置现成订阅可能更合适；若数据口径频繁争论，则应先交付口径治理。扩大前先观察同一流程重复运行后的纠错量，而不是为吸引客户承诺无监督解释所有收入变化。

依据：Smetabase, Spermissions, Scausal

## 真正可积累的资产

提示词、多模型调用和报告排版容易复制，不能单独作为经营壁垒。更有价值的可能是客户批准保存的指标定义、发布映射和人工纠错历史，但必须清楚区分可复用方法与不可跨客户共享的数据。将过去猜测标成正确或错误需要可靠验证依据，不能让模型自己给自己打分后形成伪标签。可以积累的是哪些信息缺失会让报告不可信、哪些事件需要延后观察、哪些字段要人工确认。对客户而言，可迁移的配置和透明记录也会降低锁定风险，这可能提高信任，却不一定提高价格。平台将来增加发布上下文集成会压缩通用服务空间，专门行业的事件解释或严格审计流程才可能形成差异。所有壁垒判断仍是推断，本案没有竞争赢单、留存或专有数据规模支撑。

依据：Spal, Sauthor, Scausal

## 权限、错误与因果判断责任

报告应把观察到的数值变化、时间上的相邻事件、模型提出的解释以及实验验证结果分开。随机分配或可信的识别策略未建立时，不能把相关性评分改名为影响概率，更不能据此自动奖励、解雇或评判个人价值。研究者建议同时记录促销、渠道变化、异常流量、埋点调整、节假日与样本成熟度，无法取得就列未知。七日激活与三十日转化的观察窗不同，同一批新用户尚未成熟时比较本周和上周会误导。模型共识只能帮助发现遗漏或矛盾，不消除这些数据问题。通知权限也需要独立验收，Metabase说明按创建者权限生成内容，因此不能依赖收件人网页登录权限补救已发出的敏感附件。试点只处理脱敏导出，不设置真实调度、不创建凭据、不向任何人发送，生产接入另行授权。 对转化率的百分比变化还要记录绝对百分点，分母变小可放大波动；跨产品汇总也可能掩盖各自不同走势。没有样本量与人群定义时只描述数值，不输出显著性或改善概率。人审不只是给模型文字盖章，而是检查这些输入条件是否成立；证据不足时保留未知比强行排序更有用。

依据：Scausal, Spermissions, Sauthor

## 反馈检索与反证的权重

相关体验：订阅移交和权限需要验收。

相关体验：任务运行与卡片实际送达是不同状态。

依据：Sfeedback, Srender, Smetabase, Scausal

## 内部工具先行的停止与升级条件

建议先做内部效率工具验证，不把它当成已经证实的商业机会。最小实验是使用同一产品两个已结束周期的脱敏导出，人工先形成基线，再让代理只生成变更清单与候选解释，核对来源完整率、数值一致性、遗漏、总人工分钟和需要返工的解释。这里的周期数是建议设计，不是已执行样本，不设置四周或200美元统一门槛。若报告出现不存在的PR、修改原指标、把未部署变更归因给当期数据，或泄露超出授权受众的数据，立即停止分发并修正。若只是重复图表且未减少会前准备，采用原生订阅；若解释必须依赖未取得的实验信息，保留为待验证清单。只有连续运行稳定、负责人认可可核实价值、明确预算所有者愿付且接入维护成本可覆盖时，才升级为客户服务测试。未取得这些条件前，不用模型的自信语气替经营结论背书。 试点验收表应分别记结果正确、资料可追溯、权限符合、实际人工负担，而不是用一项综合高分掩盖问题。报告可读却数值错误不能通过，数值正确却没有解释证据也不能宣传成归因服务。这种分级能让客户只为真正解决的任务决定是否继续。

依据：Sdirectory, Scausal, Smetabase

## 单位经济测算：情景假设，不是项目已实现的财务结果

| 情景 / 交付单位 | 收入 | 可变成本（含获客） | 单位贡献 | 月交付量 | 月固定成本 | 月经营贡献 |
|---|---:|---:|---:|---:|---:|---:|
| 研究者轻量假设 / 一个产品的一份验收周报 (USD) | 待核实 | 15.00 | 待核实 | 16 | 40.00 | 待核实 |
| 研究者高维护假设 / 一个产品的一份验收周报 (USD) | 待核实 | 61.00 | 待核实 | 16 | 120.00 | 待核实 |

研究者轻量假设假设：全部假设；人工15分钟×40/小时，单位15，每月16份+40=280美元。一次性接入成本未量化另列，不是零。；API成本 2，人工成本 10，其他可变成本 1，分摊获客成本 2。依据：Scost, Spal

研究者高维护假设假设：全部假设；人工60分钟×40/小时，单位61，每月16份+120=1096美元。没有售价，不算利润。；API成本 8，人工成本 40，其他可变成本 5，分摊获客成本 8。依据：Scost, Spal

## 反证与未核实信息

原生订阅能满足只送图表的需求；同时变化与多模型共识不足以证明因果，人工核查与接入维护可能吃掉节约。

未接入私人仓库或数据库，未运行PAL或额外付费模型API，未试验调度/发送。作者2025说明与2026组件文档分开；无准确率、收入或净省时实测。自有云浏览器12:20:40左右导航超时，公开内容由支持的Web读取。

## 具体动作与止损条件

对两个已结束周期的同一脱敏导出比较人工基线与代理报告，核对数值、链接、遗漏和总人工分钟。

停止投入条件：虚构变更、误改指标、越权分发或准备时间不降；仅需图表送达则用原生订阅。

## 来源与对应关系

- [Sdirectory] [许可目录：KPI与PR周报](https://agentusecases.ai/use-case/generate-recurring-weekly-reports-combining-kpis-and-pull-re)：目录记录Claude Code、Metabase与Zen多模型交叉检查，未给相关判断准确率；完整试用模板独立于作者方法。
- [Sauthor] [David Kelly：2025年9月20日非编码用途](https://dmkthinks.org/blog/claude-code-examples/)：作者将Metabase指标与GitHub变更做周期比较，并用Zen连接外部模型。是本人使用记录，不含可复验准确率；文中广告和异常用户也能改变指标。
- [Smetabase] [Metabase定期仪表盘订阅](https://www.metabase.com/docs/latest/dashboards/subscriptions)：原生支持定期通过邮件或Slack发送仪表盘，需要管理员配置；不等于自动识别PR对指标的因果效应。
- [Spermissions] [Metabase通知权限](https://www.metabase.com/docs/latest/permissions/notifications)：订阅通知按创建者的数据及集合权限展示给接收者，不能假设接收者网页登录权限会自动过滤所有已发送内容。
- [Scausal] [Microsoft Research因果研究](https://www.microsoft.com/en-us/research/group/causal-inference/)：研究说明仅有相关模式不足以可靠判断因果，需要反事实与因果推理；多模型共识不是随机实验。
- [Spal] [PAL MCP公开项目（原Zen链接跳转）](https://github.com/BeehiveInnovations/pal-mcp-server)：README提供多模型consensus及供应商接入说明；按凭据启用服务。当前名称不应倒写成2025作者当时名称。未安装或运行。
- [Scost] [Claude Code成本管理](https://code.claude.com/docs/en/costs)：官方区分订阅额度、可选额外用量及API/云平台计费路径；不能把历史20美元建议解释为多供应商无限调用总成本。
- [Sfeedback] [2023年Metabase订阅管理讨论](https://discourse.metabase.com/t/users-can-not-see-or-edit-others-dashboard-subscriptions/24913)：0.45.2用户报告普通用户不能管理他人订阅，后续询问多人管理。历史相邻流程反馈，不代表当前缺陷或本案效果。
- [Srender] [2021年订阅卡片显示故障讨论](https://discourse.metabase.com/t/dashboard-subscriptions-an-error-occurred-while-displaying-this-card/14410)：用户报告订阅卡片报错，回复指出版本修复方向；是历史交付异常，不据此计算现行失败率。

结构化记录：[research/generate-recurring-weekly-reports-combining-kpis-and-pull-re.json](../research/generate-recurring-weekly-reports-combining-kpis-and-pull-re.json)
