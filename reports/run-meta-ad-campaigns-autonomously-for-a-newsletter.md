# 用Claude Code生成素材并管理Meta广告活动

## 中文原案例

    为newsletter自主运行Meta广告活动
    一个Claude Code agent生成广告图片、通过API管理Meta广告活动、制作落地页变体并获取分析数据，在31天内测试了约50个变体。
    使用的是
    Claude Code
    他们做了什么
    作者给一个Claude Code agent 1,500美元和一个Meta Ads账户，用于一份newsletter。每天早上他输入一条命令。agent读取此前自己的日志，获取Meta和PostHog数据，决定创建、暂停还是扩大广告投放，执行后把决策依据记入git。他干预过一次，在获客表单中加入邮箱验证。
    进展与成效
    它花费1,493美元，获得243条线索，每条成本6.14美元，没有达到2.50美元的目标。白板风格广告表现最好。那次人工改动让每条线索成本飙升至50美元以上，账户始终没有完全恢复。
    值得了解
    告诉agent实验在第30天结束，使它采取了保守策略；直到第16天它才关注线索质量。因此应把目标表述为持续进行，并在开始时明确质量要求。
    亲自尝试
    使用
    Claude Code
    复制提示词
    帮我为[我的newsletter或产品]运行一个小规模Meta广告测试。面向[受众]生成[数量]个广告图片和文案变体，制作匹配的落地页变体，并通过Meta API把广告活动设置为暂停状态的草稿。将结果整理为按[指标，例如每次注册成本]排序的简明报告。在激活任何内容或产生任何花费之前，向我展示每个广告活动、预算和受众。
    原始来源：https://technically.dev/posts/claude-code-autonomous-ad-campaign

<details><summary>English original</summary>

    Run Meta ad campaigns autonomously for a newsletter
    A Claude Code agent generated ad images, managed Meta campaigns via API, built landing page variants and pulled analytics, testing about 50 variants over 31 days.
    Done with
    CC
    Claude Code
    What they did
    The author gave a Claude Code agent $1,500 and a Meta Ads account for a newsletter. Each morning he typed one command. The agent read its own prior logs, pulled Meta and PostHog data, decided whether to create, pause or scale ads, executed, and logged its reasoning to git. He intervened once, adding email validation to the lead form.
    How it went
    It spent $1,493 and got 243 leads at $6.14 each, missing the $2.50 target. Whiteboard-style ads won. The one human change spiked cost per lead above $50, and the account never fully recovered.
    Worth knowing
    Telling the agent the experiment ended at day 30 made it play safe, and it ignored lead quality until day 16, so frame the goal as ongoing and specify quality upfront.
    Try it yourself
    with
    Claude Code
    Copy prompt
    Help me run a small Meta ads test for [my newsletter or product]. Generate [number] ad image and copy variants aimed at [audience], build matching landing page variants, and set up campaigns as paused drafts through the Meta API. Pull results into a simple report ranked by [metric, e.g. cost per signup]. Show me every campaign, budget, and audience before anything is activated or any money is spent.
    Original source: https://technically.dev/posts/claude-code-autonomous-ad-campaign

</details>

## English

    Run Meta ad campaigns autonomously for a newsletter
    A Claude Code agent generated ad images, managed Meta campaigns via API, built landing page variants and pulled analytics, testing about 50 variants over 31 days.
    Done with
    CC
    Claude Code
    What they did
    The author gave a Claude Code agent $1,500 and a Meta Ads account for a newsletter. Each morning he typed one command. The agent read its own prior logs, pulled Meta and PostHog data, decided whether to create, pause or scale ads, executed, and logged its reasoning to git. He intervened once, adding email validation to the lead form.
    How it went
    It spent $1,493 and got 243 leads at $6.14 each, missing the $2.50 target. Whiteboard-style ads won. The one human change spiked cost per lead above $50, and the account never fully recovered.
    Worth knowing
    Telling the agent the experiment ended at day 30 made it play safe, and it ignored lead quality until day 16, so frame the goal as ongoing and specify quality upfront.
    Try it yourself
    with
    Claude Code
    Copy prompt
    Help me run a small Meta ads test for [my newsletter or product]. Generate [number] ad image and copy variants aimed at [audience], build matching landing page variants, and set up campaigns as paused drafts through the Meta API. Pull results into a simple report ranked by [metric, e.g. cost per signup]. Show me every campaign, budget, and audience before anything is activated or any money is spent.
    Original source: https://technically.dev/posts/claude-code-autonomous-ad-campaign

## 中文

    为newsletter自主运行Meta广告活动
    一个Claude Code agent生成广告图片、通过API管理Meta广告活动、制作落地页变体并获取分析数据，在31天内测试了约50个变体。
    使用的是
    Claude Code
    他们做了什么
    作者给一个Claude Code agent 1,500美元和一个Meta Ads账户，用于一份newsletter。每天早上他输入一条命令。agent读取此前自己的日志，获取Meta和PostHog数据，决定创建、暂停还是扩大广告投放，执行后把决策依据记入git。他干预过一次，在获客表单中加入邮箱验证。
    进展与成效
    它花费1,493美元，获得243条线索，每条成本6.14美元，没有达到2.50美元的目标。白板风格广告表现最好。那次人工改动让每条线索成本飙升至50美元以上，账户始终没有完全恢复。
    值得了解
    告诉agent实验在第30天结束，使它采取了保守策略；直到第16天它才关注线索质量。因此应把目标表述为持续进行，并在开始时明确质量要求。
    亲自尝试
    使用
    Claude Code
    复制提示词
    帮我为[我的newsletter或产品]运行一个小规模Meta广告测试。面向[受众]生成[数量]个广告图片和文案变体，制作匹配的落地页变体，并通过Meta API把广告活动设置为暂停状态的草稿。将结果整理为按[指标，例如每次注册成本]排序的简明报告。在激活任何内容或产生任何花费之前，向我展示每个广告活动、预算和受众。
    原始来源：https://technically.dev/posts/claude-code-autonomous-ad-campaign

## 原作者的方法与来源

来源：[I Let Claude Code Autonomously Run Ads for a Month](https://technically.dev/posts/claude-code-autonomous-ad-campaign)

作者方法摘要

1. 每日新会话读取此前实验记录。
   English summary: Start a fresh daily session and retrieve earlier experiment notes.

2. 读取当前活动数据，依据实验规则决定执行或不动作。
   English summary: Retrieve current campaign measurements, decide within the experiment rules, then act or refrain.

3. 把结果和决定保存到版本化文件，供下一会话使用。
   English summary: Record outcomes and decisions in versioned files for the next session.

## 我们的分析

**商业结论：仅建议受控试点。先验证可审计的投放辅助，不以低CPL承诺收入**

案例有可追溯的作者设置和负面复盘，能够研究跨日状态、工具编排与指标偏差，但没有独立账户审计或已变现收入。成熟规则和分析软件提供具体替代，定制服务必须证明复核节省而非只生成更多广告。真实支出无法靠代码回滚撤销，当前适合离线历史数据验证和人工审批草稿，不支持由一次实验推断无人值守代理可盈利。

案例ID：`run-meta-ad-campaigns-autonomously-for-a-newsletter` · 案例来源：https://agentusecases.ai/use-case/run-meta-ad-campaigns-autonomously-for-a-newsletter
研究时间：2026-10-20T07:12:41.065326+00:00

**商业评分：41.0/100。用户反馈信号占5%。**

| 维度 | 权重 | 分数 /5 | 商业依据 |
|---|---:|---:|---|
| 付费需求 | 20% | 3 | 存在周期性投放管理和成熟收费替代，但本定制服务的付款转化与续费尚未验证。 [Sbirch, Sdirectory] |
| 业务价值与效果证据 | 20% | 2 | 作者完整披露目标未达成且名单未变现，流程运行结果不能外推为客户商业回报。 [Soriginal] |
| 单位经济与利润 | 20% | 2 | 假设收费方案对人工复核时间高度敏感，低价方案负贡献，尚无实际成本账。 [Sbirch, Sdirectory] |
| 获客与市场进入 | 15% | 2 | 咨询关系可能降低首次交付摩擦，但没有本工作流获客成本、销售周期和渠道转化证据。 [Soriginal] |
| 竞争壁垒 | 10% | 1.5 | 规则和分析已有成熟产品，差异需来自业务整合与审计，目前未证明独占数据或分发。 [Sbirch, Sposthog] |
| 交付与经营风险 | 10% | 2 | 写广告账户有真实资金与隐私风险，工具存在不等于权限、重试和恢复已经验证。 [Ssdk, Sposthog] |
| 独立用户反馈信号 | 5% | 0 | 本轮没有核实独立用户复制该系统后的反馈，公开赞赏与作者复盘不能替代此项证据。 [Ssetup] |

## 自用价值：中

适合已有营销能力者整理跨日数据与方案；收益未独立计时。

依据：Sdirectory, Soriginal, Sposthog

- 适用人群：已有投放账户和审批能力的小团队或newsletter作者。
- 用途：整理报表、生成素材草稿、记录实验决定。
- 预期收益：潜在减少重复搬运，原案例未达CPL目标，无收入证明。
- 设置成本：工具接入、素材规范、指标映射、测试与权限设计，实际工时未知。
- 维护成本：数据/API变更、失败恢复、素材审核与预算复核。
- 使用频率：原作者每日触发，是否适合他人需按业务频率。
- 隐私风险：账户权限、线索个人资料和业务数据，宜用聚合脱敏输入。
- 错误风险：错误目标、重复投放、花费不可逆、单日归因误判。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/run-meta-ad-campaigns-autonomously-for-a-newsletter

建议工具：Claude Code

    Help me run a small Meta ads test for [my newsletter or product]. Generate [number] ad image and copy variants aimed at [audience], build matching landing page variants, and set up campaigns as paused drafts through the Meta API. Pull results into a simple report ranked by [metric, e.g. cost per signup]. Show me every campaign, budget, and audience before anything is activated or any money is spent.

自编试用模板

准备条件：只用合成历史活动表、明确字段与人工规则，无账户或支付。

工具：本地表格与已有文本助手，不需新密钥。

预期结果：可复算报表、未知项、待审批动作清单；不产生真实投放。

### 源站Copy prompt

原文模板

出处：https://agentusecases.ai/use-case/run-meta-ad-campaigns-autonomously-for-a-newsletter

依据：Sdirectory

    Help me run a small Meta ads test for [my newsletter or product]. Generate [number] ad image and copy variants aimed at [audience], build matching landing page variants, and set up campaigns as paused drafts through the Meta API. Pull results into a simple report ranked by [metric, e.g. cost per signup]. Show me every campaign, budget, and audience before anything is activated or any money is spent.

### 离线投放复核

自编模板

出处：研究团队自编

依据：Sposthog, Ssdk

    只分析合成活动表，核对币种时区、转化定义、缺失值和归因窗口，列出方案及停止条件。不要访问账户或执行广告、预算、表单、支付和发布操作。

## 已核验事实

- 目录自述31天约50变体、1493支出243线索、6.14成本与2.50目标；不是收入或已核净利润。 [Sdirectory]
- 作者复盘更新2026-08-25，实验发生在1月；newsletter尚未变现，质量与指标并不一致。自述无独立账户审计。 [Soriginal]
- 2026-01-01同作者设置文；Claude Code与Opus4.5，图像技能、Meta工具、PostHog与文件状态；公开评论不构成复现反馈。 [Ssetup]
- 营销分析为opt-in beta，按campaign/source映射成本与转化，区分平台上报与自定义目标，不能直接推客户价值。 [Sposthog]
- 自有云浏览器月付选择，连接账户总月支出至10K档Essential49/月、Pro99/月，Pro含自动规则与自定义指标；结账币种地区可变。 [Sbirch]
- 公开代码含PAUSED、configured/effective status、spend_cap及validate_only，接口存在不证明实际账户权限或预算执行已验收。 [Ssdk]
- 2026-08-17营销软件商讨论预算节奏与单日误判，属相邻且有商业利益的观察，不独立验证本案；未使用未核样本数字。 [Smarket]
- 目录的建议试用模板要求先展示活动、预算和受众，激活或花费前暂停；这不是原作者实际执行提示词的证据。 [Sdirectory]

## 客户、需求与付款人

目标客户应收窄为已经有投放账户、有明确受众定义、愿意持续复核数据的小型营销团队或newsletter经营者。这个人既承担广告费，也有权决定什么算合格订阅者。研究者推断其可购买的价值是减少跨工具搬运、保留决策依据和整理次日待办，不宜把‘便宜线索’直接当交付承诺。业务尚未变现时，订阅者可以只是名单增长，不能用新增数量替代客户收入。作者自身做营销咨询，拥有搭建工具和判断异常的能力，因此该案例不是普通非技术新手开箱即用的证明。最先应排除没有转化定义、没有可核对的名单状态、只愿按最终收入结算又不给后续收入数据的客户。预算归属也要分清：平台消耗归广告主，工具和服务费归执行团队；把两者合在一个‘AI成本’里会掩盖真正的资金风险。低频的一次活动也可能需要这套流程，但未必适合月订阅，是否续费取决于持续运营频率与复核节省，而非是否生成过一次好看的广告。

依据：Sdirectory, Soriginal

## 输入、动作、交付与恢复

原案例搭建了图像、投放和分析工具，以文件保存跨会话状态。这能解释流程可行性，但尚未取得可以原样复现的完整代码与账户配置。研究者建议把交付拆成输入检查、只读报表、方案草稿、人工批准、执行回读和审计记录六段。首先固定账户、币种、时区、活动ID、归因窗口与转化事件，避免把另一个活动的结果用于调预算。素材与落地页各有版本，先验证链接、文案和表单，再提交待审方案。SDK存在PAUSED状态并不等于一切创建操作都零风险，必须确认所用接口、父子活动状态及账户权限。任何写操作超时先查询目标ID和当前状态，不能简单重复创建。日志保存输入数据摘要、动作、批准人和回读结果即可，无需保存敏感线索正文。下一次运行要区分已执行、仅计划、执行结果未知三种状态。实际试点前必须演练报告缺列、数据延迟、重复任务与目标账户错误，让系统停止或降级为只读，而不是让模型猜一个可继续执行的答案。

依据：Ssetup, Ssdk, Sposthog

## 市场证据与需求边界

目前证据足以说明投放管理存在周期性取数与判断工作，却不足以给自主agent服务计算市场规模。作者是一个具体使用者，另一家营销软件商讨论预算节奏属于相邻工作流经验，两者不是独立复现实验。PostHog的营销分析功能说明数据连接与口径统一本身已有产品化需求，也说明这些基础能力不必从零开发。由此可以提出一个更窄的验证问题：客户是否愿意为可靠的数据对齐、清楚的动作审批和长期实验记录付费，而不只是为‘AI自动投放’付费？要回答它，需要未来另行授权的客户访谈或付费试点，本轮没有联系任何人。行业增长、广告平台总收入和模型热度都不能替代这个答案。澳大利亚小众newsletter案例也不能直接推出美国电商品牌的获客成本；商品价格、复购、落地页、受众宽度和广告历史都会改变经济性。现阶段可以把需求视为有实际工作流支撑的假设，不能把案例曝光或媒体转载当购买意向，也不能把同一作者的两篇文章计作两家客户。

依据：Soriginal, Smarket, Sposthog

## 替代方案与购买理由

最直接的替代组合是现有投放规则工具、分析看板和人工创意审稿。Birch已把自动规则、时间窗和自定义指标做成付费功能，PostHog提供转化与成本汇总，因此单纯每天拉数据并按阈值停广告的脚本竞争空间有限。月费比较必须拿包含规则的方案，不应以更便宜但功能不同的入门价误导。自建agent可能的差异在于同时理解产品、生成跨系统草稿、发现口径缺口并留下可审计的决策记录；这是研究者提出的价值主张，尚未测得优于现有工具。转换成本包括旧活动与素材命名、数据字段、客户授权、失败报警和团队审批习惯，不能忽略。对只有一个低预算账户的客户，成熟规则工具加人工往往更容易解释，也减少自建维护；对多个业务系统确实需要协调的团队，定制服务才可能合理。评估时应该让两种方案使用同一批历史数据，比较错误率、复核分钟数和决策覆盖，不用新工具自行挑选最有利样例。平台原生自动化仍是替代压力，跨系统整合也不能保证形成长期壁垒。

依据：Sbirch, Sposthog, Ssdk

## 收入机制、完整成本与敏感性

作者披露的是广告支出与名单获取结果，不是向客户收取的服务费。本文两个模型均为研究者假设，统一用美元建模，与原案例未明确币种的$数字分开，不把它们混算为经营账。方案A是假设每账户每月收600美元，模型摊销30、人工四小时乘30为120、其他服务50、获客摊销100，单位贡献300；十账户且月固定维护1500后，经营贡献1500。若每账户复核从四小时变为九小时，人工多150，月贡献归零，尚未计初始研发和税费。方案B是低价每月199，模型30、人工90、其他40、获客60，单账户贡献负21，二十账户与固定1000合计亏1420；扩大规模不会自动修复负贡献。两种模型的广告费由客户另付，不属于服务收入也不算服务商毛利，但客户是否愿意续费仍取决于包含广告费的总收益。客户收入、合格率、付费转化与留存未知时，不能以CPL倒推合理服务费。应先测复核时间和错误恢复成本，再谈扩大客户量；人工审稿、数据修复、授权维护及退款处理都不能设为零。

依据：Sdirectory, Sbirch

## 获客与交付路径

合理的初始获客假设是面向已有营销执行能力的顾问或小团队，交付一个可比较的只读诊断包，而非直接要求陌生客户交出广告账户。诊断包可展示数据口径差异、过去决策依据是否完整和人工复核负担，并约定哪些信息不能用于模型。后续若用户另行授权客户验证，先确认付款人与使用者是否同一人、谁批准支出、发生错误谁处置，再提出有限范围服务。咨询合作、公开方法文章或既有客户转介绍可以作为测试渠道，但本案例没有提供渠道获客率、销售周期或订单金额，不能把这些路径写成已验证增长方式。交付验收应围绕字段准确、草稿版本、未批准动作拦截及审计完整度，不承诺订阅者数量或利润。对于不提供收入反馈的客户，服务合同不能用所谓ROAS改善作为无人可核的验收标准。若未来选择按效果收费，还需明确归因、退款、线索重复和结算窗口，否则优化指标与实际现金之间的争议会吞掉收入。这些是未来设计，不代表本轮联系、报价或签约。

依据：Soriginal, Sbirch

## 可复制条件与可积累部分

可复制的是把外部状态显式记录、按固定口径读取数据、在有限动作集合内作决策的组织方式。不能复制的假设是同一创意形式、同一受众和同一预算一定有效。工具编排和提示词本身容易被成熟产品吸收；如果没有持续客户反馈，文件越积越多也可能只是把旧错误反复引用。真正可能积累的资产是经过人工校验的异常类型、跨系统字段映射、明确的审批与恢复规则以及经过留存结果检验的实验记录。这些资产是否构成壁垒仍待验证，不能把收集更多客户数据本身当竞争优势，更不能默认可以跨客户复用私人数据。最小复制前提包括有权使用的素材、能识别目标账户的工具、稳定转化定义、能够及时暂停的人工负责人和可追溯的成本记录。缺少其中任何一项，都应退回报表辅助而不是提高自动化权限。若现成规则工具已覆盖大部分工作，定制系统只能靠更少的人工复核或更清楚的业务连接证明价值，不能靠多调用几个模型解释溢价。

依据：Ssetup, Sposthog, Sbirch

## 经营、权限与错误风险

主要风险集中在真实支出、错误受众和错误测量的结合：一个看似合理的动作可能同时消耗预算并强化错误目标。研究者建议把总支出上限、账户白名单、审批记录及动作频率放在工具层校验，而非只写入提示词。模型遇到缺数据应提出缺口，不应自行扩大预算、改变转化定义或更换目标账户。设置与维持凭据、平台审查、API变更、数据删除和客户退出也都需要明确负责人，本轮未建立任何新访问。含个人信息的线索不宜整表放入运行日志，聚合统计与最小必要字段通常更适合诊断。错误后的恢复未必能撤回已展示广告或已经花掉的钱，所以‘可回滚代码’不能等同于‘可回滚业务后果’。预算规则官方帮助页本轮受限，未取得当前完整条款，因此不输出具体每日超支百分比作为已核实政策。测试应覆盖超时后回读、重复执行、数据新鲜度和父子活动状态不一致，所有这些都必须在开启真实投放之前单独验证。

依据：Ssdk, Sposthog, Sdirectory

## 反馈、反证与因果边界

暂无直接用户反馈。

依据：Soriginal, Ssetup, Smarket

## 判断与可执行下一步

结论为仅建议受控试点，优先验证只读诊断与待审批方案，暂不把无人值守支出作为产品卖点。下一步可以在本地构造或合法取得脱敏的历史活动表，准备至少二十个包含延迟归因、缺失字段、重复任务、预算接近上限和无转化的场景。以人工规则方案为对照，检查关键数值计算是否全部可复算、未知数据是否正确标注、任何未批准动作是否被阻止，并计时人工审核。建议门槛是零越权、零跨账户、核心字段全部可追溯，复核时间比基线少三成；这些是拟议验收值，不是本轮已测结果。通过离线阶段以后，仍需另行批准具体账户、金额、受众与素材，才可讨论小范围真实试点。若复核成本不能降到方案A盈亏阈值内、客户拒绝定义合格转化，或必须靠模糊承诺才能获得付款，应停止商业扩张。总支出预算和停止日期依然应保留；让系统理解长期目标不意味着取消财务上限。最值得保留的是可追溯的工作方法，最不应直接复制的是把不明确的商业目标交给拥有花钱权限的执行器。

依据：Sdirectory, Sposthog, Sbirch

## 单位经济测算：情景假设，不是项目已实现的财务结果

| 情景 / 交付单位 | 收入 | 可变成本（含获客） | 单位贡献 | 月交付量 | 月固定成本 | 月经营贡献 |
|---|---:|---:|---:|---:|---:|---:|
| A：研究者假设的月度投放辅助服务 / 每账户每月 (USD) | 600.00 | 300.00 | 300.00 | 10 | 1500.00 | 1500.00 |
| B：研究者假设的月度投放辅助服务 / 每账户每月 (USD) | 199.00 | 220.00 | -21.00 | 20 | 1000.00 | -1420.00 |

A：研究者假设的月度投放辅助服务假设：所有经营输入均假设，收入为净服务费，广告费客户另付；模型30是摊销非本轮调用；不含初始研发及税费。人工4小时×30美元；达到9小时则月贡献归零。；API成本 30，人工成本 120，其他可变成本 50，分摊获客成本 100。依据：Sbirch, Sdirectory

B：研究者假设的月度投放辅助服务假设：所有经营输入均假设，收入为净服务费，广告费客户另付；模型30是摊销非本轮调用；不含初始研发及税费。人工3小时×30美元；单位贡献-21、月亏1420。；API成本 30，人工成本 90，其他可变成本 40，分摊获客成本 60。依据：Sbirch, Sdirectory

## 反证与未核实信息

广告目标未达成，newsletter未变现，名单质量缺口；现成规则工具替代强。相反，流程与审计记录仍可能降低重复劳动，需独立计时对照。

原例$未明确USD/AUD，中文美元沿目录表述不作汇率换算。作者两篇为同一证据链；本轮无账号/账单/完整代码/客户收入/工时审计。Meta帮助页受限停止，不引用百分比政策。无真实广告、联系、注册、凭据、付费API或试用。Breezeway为商业相关相邻观察，非独立本案验证。

## 具体动作与止损条件

离线20场景对照人工基线，验证字段与计算、重复任务、预算边界、归因延迟和审批；零越权且审核用时下降30%才提出另行授权的小试点。

停止投入条件：任何跨账户或未批准写入即停止；人工复核超过模型A九小时/账户月盈亏线、没有合格转化定义或客户拒绝提供可核结果时停止扩张。

## 来源与对应关系

- [Sdirectory] [许可目录newsletter广告案例](https://agentusecases.ai/use-case/run-meta-ad-campaigns-autonomously-for-a-newsletter)：目录自述31天约50变体、1493支出243线索、6.14成本与2.50目标；不是收入或已核净利润。
- [Soriginal] [作者31天投放复盘](https://technically.dev/posts/claude-code-autonomous-ad-campaign)：作者复盘更新2026-08-25，实验发生在1月；newsletter尚未变现，质量与指标并不一致。自述无独立账户审计。
- [Ssetup] [Giorgio Liapakis实验设置](https://medium.com/@giorgioliapakis/giving-claude-code-1-500-and-full-access-to-a-meta-ads-account-0602c343b90c)：2026-01-01同作者设置文；Claude Code与Opus4.5，图像技能、Meta工具、PostHog与文件状态；公开评论不构成复现反馈。
- [Sposthog] [PostHog营销分析文档](https://posthog.com/docs/web-analytics/marketing-analytics)：营销分析为opt-in beta，按campaign/source映射成本与转化，区分平台上报与自定义目标，不能直接推客户价值。
- [Sbirch] [Birch官方定价](https://bir.ch/pricing)：自有云浏览器月付选择，连接账户总月支出至10K档Essential49/月、Pro99/月，Pro含自动规则与自定义指标；结账币种地区可变。
- [Ssdk] [Meta官方Python SDK Campaign](https://github.com/facebook/facebook-python-business-sdk/blob/main/facebook_business/adobjects/campaign.py)：公开代码含PAUSED、configured/effective status、spend_cap及validate_only，接口存在不证明实际账户权限或预算执行已验收。
- [Smarket] [Breezeway预算节奏观察](https://www.breezeway.co/blog/your-daily-budget-isnt-daily/)：2026-08-17营销软件商讨论预算节奏与单日误判，属相邻且有商业利益的观察，不独立验证本案；未使用未核样本数字。

结构化记录：[research/run-meta-ad-campaigns-autonomously-for-a-newsletter.json](../research/run-meta-ad-campaigns-autonomously-for-a-newsletter.json)
