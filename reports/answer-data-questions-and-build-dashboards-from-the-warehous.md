# 用 Devin 查询数据仓库并生成 SQL 与看板

## 案例完整中文译文

    查询数据仓库中的数据问题并构建看板
    Cognition 团队使用一个名为 DANA 的 Devin 变体来查询数据仓库、构建看板并回答数据问题，Devin 还会填写报表表单。
    实际使用
    Devin
    具体做法
    DANA 是一个 Devin 变体，可从网页应用的 agent 选择器中访问，也可在 Slack 中通过 /dana 或 @Devin !dana 调用。它通过 MCP 连接数据仓库（Redshift、Postgres、Snowflake、BigQuery），并维护自己对数据结构的认识。它执行 SQL，用 seaborn 图表给出简洁的答案，还能构建可分享的 Metabase 看板。
    结果如何
    过去需要在工程师的任务队列中等待几天的临时问题，现在任何人都可以在 Slack 中获得答案，而且回答附带 SQL，便于检查逻辑。文章没有给出这方面的数字。
    值得注意
    明确说明指标，写出时间范围，并要求提供可视化。阅读 DANA 返回的 SQL，检查其逻辑。
    自行试用
    推荐工具
    Devin
    复制提示词
    使用[配置文件或环境变量]中的只读凭据连接我的数据仓库，并回答这个问题：[业务问题，例如过去90天按渠道划分的每周注册量]。向我展示所用的 SQL、结果表，以及我可以打开的简单图表或看板文件。在执行任何会写入或修改数据的查询之前，停下来征求我的同意；除此之外，当我得到经过验证的答案，并且查询已保存在[文件夹]中时，任务即告完成。
    原始来源：https://cognition.com/blog/how-cognition-uses-devin-to-build-devin

<details>
<summary>English · 完整归档原文</summary>

<pre>Answer data questions and build dashboards from the warehouse
Cognition&#x27;s team uses a Devin variant called DANA to query their data warehouse, build dashboards and answer data questions, and Devin fills out report forms.
Done with
DE
Devin
What they did
DANA is a Devin variant reached from the web app&#x27;s agent picker or in Slack with /dana or @Devin !dana. It connects to the warehouse (Redshift, Postgres, Snowflake, BigQuery) through MCP and keeps its own knowledge of the schema. It runs SQL, returns concise answers with seaborn charts, and can build shareable Metabase dashboards.
How it went
Ad-hoc questions that used to wait days in an engineer&#x27;s queue can now be answered by anyone in Slack, with the SQL included so the logic can be checked. The post gives no numbers for this.
Worth knowing
Be specific about metrics, include time periods, and ask for visualizations. Read the SQL that DANA returns to check its logic.
Try it yourself
with
Devin
Copy prompt
Connect to my data warehouse using the read-only credentials in [config file or env var] and answer this question: [business question, e.g. weekly signups by channel for the last 90 days]. Show me the SQL you used, the result table, and a simple chart or dashboard file I can open. Before running any query that writes or modifies data, stop and ask me; otherwise you&#x27;re done when I have a verified answer and the query saved in [folder].
Original source: https://cognition.com/blog/how-cognition-uses-devin-to-build-devin</pre>

</details>

## English

    Answer data questions and build dashboards from the warehouse
    Cognition's team uses a Devin variant called DANA to query their data warehouse, build dashboards and answer data questions, and Devin fills out report forms.
    Done with
    DE
    Devin
    What they did
    DANA is a Devin variant reached from the web app's agent picker or in Slack with /dana or @Devin !dana. It connects to the warehouse (Redshift, Postgres, Snowflake, BigQuery) through MCP and keeps its own knowledge of the schema. It runs SQL, returns concise answers with seaborn charts, and can build shareable Metabase dashboards.
    How it went
    Ad-hoc questions that used to wait days in an engineer's queue can now be answered by anyone in Slack, with the SQL included so the logic can be checked. The post gives no numbers for this.
    Worth knowing
    Be specific about metrics, include time periods, and ask for visualizations. Read the SQL that DANA returns to check its logic.
    Try it yourself
    with
    Devin
    Copy prompt
    Connect to my data warehouse using the read-only credentials in [config file or env var] and answer this question: [business question, e.g. weekly signups by channel for the last 90 days]. Show me the SQL you used, the result table, and a simple chart or dashboard file I can open. Before running any query that writes or modifies data, stop and ask me; otherwise you're done when I have a verified answer and the query saved in [folder].
    Original source: https://cognition.com/blog/how-cognition-uses-devin-to-build-devin

## 中文

    查询数据仓库中的数据问题并构建看板
    Cognition 团队使用一个名为 DANA 的 Devin 变体来查询数据仓库、构建看板并回答数据问题，Devin 还会填写报表表单。
    实际使用
    Devin
    具体做法
    DANA 是一个 Devin 变体，可从网页应用的 agent 选择器中访问，也可在 Slack 中通过 /dana 或 @Devin !dana 调用。它通过 MCP 连接数据仓库（Redshift、Postgres、Snowflake、BigQuery），并维护自己对数据结构的认识。它执行 SQL，用 seaborn 图表给出简洁的答案，还能构建可分享的 Metabase 看板。
    结果如何
    过去需要在工程师的任务队列中等待几天的临时问题，现在任何人都可以在 Slack 中获得答案，而且回答附带 SQL，便于检查逻辑。文章没有给出这方面的数字。
    值得注意
    明确说明指标，写出时间范围，并要求提供可视化。阅读 DANA 返回的 SQL，检查其逻辑。
    自行试用
    推荐工具
    Devin
    复制提示词
    使用[配置文件或环境变量]中的只读凭据连接我的数据仓库，并回答这个问题：[业务问题，例如过去90天按渠道划分的每周注册量]。向我展示所用的 SQL、结果表，以及我可以打开的简单图表或看板文件。在执行任何会写入或修改数据的查询之前，停下来征求我的同意；除此之外，当我得到经过验证的答案，并且查询已保存在[文件夹]中时，任务即告完成。
    原始来源：https://cognition.com/blog/how-cognition-uses-devin-to-build-devin

## 原作者的方法与来源

来源：[How Cognition Uses Devin to Build Devin | Cognition](https://cognition.com/blog/how-cognition-uses-devin-to-build-devin)

作者方法摘要

1. Cognition团队将DANA描述为面向仓库问题的专门Devin，可从网页agent选择器或Slack调用。
   English summary: The Cognition team describes DANA as a specialized Devin for warehouse questions, accessed through the web agent picker or Slack.

2. DANA通过MCP仓库连接和schema知识执行SQL，返回简短答案、可视化与可检查的SQL。
   English summary: DANA uses MCP warehouse connections and schema knowledge to run SQL and return concise answers with visualizations and inspectable SQL.

3. 同一文章在MCP部分展示Metabase看板，并定性描述临时问题排队的改善，没有提供DANA的量化效果。
   English summary: The same article shows Metabase dashboards in its MCP discussion. It reports qualitative relief from ad-hoc question queues, without DANA outcome measurements.

## 我们的分析

**商业结论：适合内部效率工具。SQL与图表可供审阅，先核实口径和人工净省时再考虑外部服务**

原文提供内部DANA工作流的一手描述，六份已读资料足以支持权限、复杂SQL与竞争基线分析；但没有案例正确率、人工净省时、真实成本、独立付费客户或当前DANA采购条件。适合由具备SQL和业务审阅能力的人先作内部辅助，不足以据此承诺自动决策或规模化服务收益。

案例ID：`answer-data-questions-and-build-dashboards-from-the-warehous` · 案例来源：https://agentusecases.ai/use-case/answer-data-questions-and-build-dashboards-from-the-warehous
研究时间：2026-10-18T03:12:38.025709+00:00

**商业评分：35.0/100。用户反馈信号占5%。**

| 维度 | 权重 | 分数 /5 | 商业依据 |
|---|---:|---:|---|
| 付费需求 | 20% | 2 | 已有内部临时查询工作流，但没有独立客户采购或续费证据，付费需求只能待验证。 [S4da357a2f3b4, S28d436fb8ccb] |
| 业务价值与效果证据 | 20% | 2 | 返回SQL和图表的工作流有一手描述，缺正确率、人工净省时及受控对照结果。 [S4da357a2f3b4, S11775be95e18] |
| 单位经济与利润 | 20% | 2 | 可以预算人工与用量，但DANA独立价格和真实复核时间未知，返工会快速侵蚀贡献。 [S58791169610f, S3203eeb395d9] |
| 获客与市场进入 | 15% | 1 | 潜在买方可识别，尚无本案例独立付费用户和获客证据，供应商内部使用不等于销售渠道。 [S4da357a2f3b4, S58791169610f] |
| 竞争壁垒 | 10% | 2 | 指标字典与验收可积累，已有BI和内建代理功能使单纯自然语言SQL入口差异有限。 [S28d436fb8ccb, S886a192f0a23] |
| 交付与经营风险 | 10% | 2 | 局部合成口径可检查，但生产权限、语义正确性、配额与分享仍需实际独立验收。 [S3203eeb395d9, S886a192f0a23, S11775be95e18] |
| 独立用户反馈信号 | 5% | 0 | 本轮跨公开网页与代码/讨论渠道未取得可归属DANA数据工作流的独立用户结果，不解释为负面评分。 [S4da357a2f3b4, S11775be95e18] |

## 自用价值：中

能检查SQL与指标口径的人可能得到可复查初稿，净省时和真实准确率尚未测量。

依据：S4da357a2f3b4, S3203eeb395d9, S886a192f0a23, S11775be95e18, S28d436fb8ccb

- 适用人群：维护企业指标、懂SQL且有数据审阅权限的成年数据或运营人员。
- 用途：只读、受审阅的数据问答与图表初稿，先从固定无敏感样本开始。
- 预期收益：可能减少重复查询整理和等待，不能推定净工时、收入或经营决策改善。
- 设置成本：数据字典、口径与租户范围、权限和参考答案、查询预算及历史问题集。
- 维护成本：schema与指标变化、SQL审阅、失败处理、用量与分享权限复查。
- 使用频率：适合重复临时问题，先小规模验收，没有持续真实使用效果数据。
- 隐私风险：数仓可能包含客户与经营数据；本轮只用虚构数据，不读取凭据或上传真实材料。
- 错误风险：重复连接、时间边界、空值当零、指标误解、跨租户和看板越权。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/answer-data-questions-and-build-dashboards-from-the-warehous

建议工具：Devin

    Connect to my data warehouse using the read-only credentials in [config file or env var] and answer this question: [business question, e.g. weekly signups by channel for the last 90 days]. Show me the SQL you used, the result table, and a simple chart or dashboard file I can open. Before running any query that writes or modifies data, stop and ask me; otherwise you're done when I have a verified answer and the query saved in [folder].

自编试用模板

准备条件：虚构数据库、指标字典、人工参考答案和固定时间窗口，不含真实凭据或客户数据。

工具：现有本地Python标准库SQLite；不运行DANA、Devin、MCP、仓库或Metabase。

预期结果：保存可复核SQL、参数、结果、合成表/图及未知项，不生成真实业务结论。

### 用虚构数据验收SQL与图表

自编模板

出处：研究团队自编

依据：S4da357a2f3b4, S3203eeb395d9, S886a192f0a23, S11775be95e18

    仅使用[虚构数据库、数据字典和人工参考答案]准备数据问答验收。先确认指标、UTC时区、半开时间区间、租户、去重键、测试账户、NULL和已知零的区别。只在本地只读副本运行已审阅SQL，保存参数、结果、查询与图表；检查周边界、重复事件、一对多连接、未知渠道和缺失金额。对每个结果说明哪些是已知部分，哪些仍未知。不要读取配置/环境变量中的凭据，不接入仓库、MCP、Devin或Metabase，不注册、购买、创建凭据、调用付费API或发送消息。遇到写入、权限不明或数据不足就停止，输出复核问题。此为研究团队自编，不代表作者当时所用提示词，未调用模型实测。

## 已核验事实

- Cognition团队原文自述使用DANA进行仓库数据问答并返回SQL和可视化，未披露该任务量化净收益。 [S4da357a2f3b4]
- 归档推荐模板中的只读凭据不是DANA默认权限配置的实测证据，调试章节与数据工作流不可混同。 [S4da357a2f3b4, S3203eeb395d9]
- PostgreSQL官方文档说明默认事务可读写，只读模式也不意味着阻止所有磁盘写入。 [S3203eeb395d9]
- PostgreSQL的READ COMMITTED与REPEATABLE READ使用不同快照可见性，复核需说明快照口径。 [S3203eeb395d9]
- Metabase官方说明权限授予组，多组成员会获得各组中最宽松的访问权限。 [S886a192f0a23]
- 当前Metabase内建Metabot与MCP均提供问答路径，agent开发工作流另有计划与同步权限要求。 [S28d436fb8ccb]
- Metabase当前价格页把基础计划和可选AI用量分列，不等于Devin或DANA采购价格。 [S58791169610f]
- Spider2研究覆盖复杂企业SQL环境并持续更新评估设置，不能移植其成绩作为DANA准确率。 [S11775be95e18]
- Metabase的MCP返回内容受使用者权限范围约束，但本案例实际分享权限没有公开实测。 [S28d436fb8ccb, S886a192f0a23]

## 使用者、付款人与已知需求

使用者是已经有数仓、但经常需要临时统计的产品、运营和工程人员；预算负责人可能是数据平台或业务部门负责人。Cognition原文只能证明团队自述在内部使用DANA，不能证明另一家公司已经为独立数据分析服务付费，也没有公开合同、续费或客户名单。适合先验收内部效率：让有明确口径的问题少经过一次排队，把分析师时间留给定义指标和解释结果。对没有稳定数据源的小团队，接入agent之前通常还要清理字段、权限和指标，这项准备成本不能隐藏在“问一句即可”的演示里。潜在付费需求应以现有请求积压、人工处理时长和错误代价核实，而不是用文章讨论热度替代。Metabase本来就有问答与SQL工具，买方也可能直接使用现有BI系统。若只有少数固定报表，先维护经过审核的查询可能比新增通用代理更容易交付。

依据：S4da357a2f3b4, S28d436fb8ccb, S58791169610f

## 从问题到可复查结果的工作流

作者方法是从网页或Slack进入DANA，经MCP获取仓库结构与数据，再返回SQL和图表。同文另有Metabase看板示例；归档把这些能力合并描述，本报告保留归档原文及译文，同时不把所有章节都当作DANA部署保证。实际验收应先写清指标定义、时区、时间窗口、去重键、测试账户和租户范围，再运行只读查询，保存参数、结果及生成时间，最后才生成图表。看板需要记录刷新方式与访问者，不能把一个可打开的链接直接等同于授权正确、数据最新。源站试用提示词是建议模板，并非作者公开的实际提示词；其中只读凭据也不能反推DANA默认只读。原文相邻调试章节的只读数据库配置不应挪作本工作流的权限证据。回答附SQL有利于检查，但仍需要懂口径的人验证SQL与问题是否一致。每次交付还应保存输入问题的版本和修改记录，区分用户后来改变问题与系统首次答错。图表轴、分母和样本量必须与表格一致，不能为了视觉简洁省掉异常或未知类别。不能仅凭有图表就认定分析完成。

依据：S4da357a2f3b4, S3203eeb395d9, S886a192f0a23

## 市场证据与可替代任务

公开材料显示企业SQL不只是单表聚合。Spider2研究项目包含企业环境、长上下文、多方言和复杂查询，其任务与评价设置会更新；这些事实支持针对自己的问题做独立验收，却不支持把某个榜单模型分数贴在DANA身上。内部数据问答的需求可以从工单中验证：哪些问题重复、哪些等待较久、哪些只有工程师能回答。排队时间、执行时间与人工投入必须分开计量，等待减少不等于同等工时被省下，更不能直接折算新增收入。原文没有这些数字，所以本报告不估算实际市场规模或自动化替代比例。优先客户应是已经有可读指标层与固定权限、愿意保留人工审阅的小团队；缺少数据字典或经常改变业务定义的环境，分析准备可能比自然语言入口更重要。研究基准是独立技术证据，不能冒充本案例独立用户反馈。评测集应有可答和不可答问题，包含数据缺失、定义冲突与需要业务判断的情形；拒答的质量也应纳入验收。不能只挑已知能成功的演示问题，再用成功样本推算总体效果。

依据：S11775be95e18, S4da357a2f3b4, S28d436fb8ccb

## 现成BI、分析师与通用agent

竞争基线包括人工写SQL、固定报表、Metabase查询构建器和内建Metabot，以及连接MCP的通用agent。当前Metabase文档把内建日常问答、MCP临时问答与由开发者创建可复用内容分成不同路径，权限和计划也不同；不能默认所有路径同价或具备同样的发布能力。其公开计划页有基础托管和AI额外使用费，自托管也有基础设施与维护成本。DANA方案若只是生成SQL，差异很容易被已有BI功能覆盖；可交付价值更可能来自企业指标字典、审阅流程和异常定位。比较时应使用同一组问题、同一数据快照和人工答案，记录正确率、审阅分钟、失败恢复与总成本。没有对照测量时，“比分析师快”只能是假设。Metabase当前内建能力是竞争基线，不是证明2026年2月原文团队使用了这些当前功能的证据。

依据：S28d436fb8ccb, S58791169610f, S886a192f0a23, S4da357a2f3b4

## 两种预算与人工敏感性

以下均为美元假设预算，不是DANA报价、作者收入或已实现利润。月度维护服务按每客户600：平台/模型/仓库用量预算80，人工6小时乘40为240，其他30，获客摊销60，单位贡献190；每月10客户、固定500，则经营贡献1400。若复核与返工翻倍到12小时，单位变成负50、月度负1000。一次设置项目按3000：用量预算60，人工45小时乘45为2025，其他100，获客300，单位贡献515；每月2项、固定500，经营贡献530。多12小时返工即多540，单位负25、月度负550。这里没有用厂商标价硬推DANA成本：本轮DANA文档和Devin主页/定价链接返回404，独立DANA采购资格、价格与用量未知。Metabase标价只用于理解替代采购结构，不能抵销现有仓库费用。税、采购折扣、超额扫描和意外事故等额外支出尚未知；实际成本超出预算时必须重算。

依据：S58791169610f, S28d436fb8ccb, S3203eeb395d9

## 进入方式与可核验承诺

合理的第一步是向已有数仓和BI负责人展示一个可审阅的历史问题样本包，而不是向陌生客户承诺通用数据专家。样本包应包含原问题、固定时间窗口、人工参考答案、SQL、结果、图表和未解决项；此报告没有发送推销或联系任何人。可以先选择十到二十个重复的内部问题，将口径、权限和结果复核成本记账，再决定是否提供维护服务。对外定价应围绕有边界的报表或受审阅问答批次，明确不承诺无限查询、任意数据接入或自动经营决策。获客成本不仅是广告，也包括需求沟通、数据可用性排查与合规采购时间。Cognition是供应商内部使用自述，不能当成第三方采购背书；没有已核验独立付费案例时，分销评分应低，不能从其品牌和文章曝光推导我们能低成本获客。

依据：S4da357a2f3b4, S58791169610f, S28d436fb8ccb

## 指标定义与维护资产

可积累的资产是经过业务负责人确认的指标定义、字段版本、查询测试和异常说明，而不是某一次生成的SQL或一个MCP连接。需要记录表关系与更新频率，特别处理一对多连接、删除/退款、延迟事件、空值和跨租户字段。Spider2说明真实任务会跨复杂环境，但并不保证某个自动schema记忆可以持续正确；数据结构变化后仍要重新验收。权限资产也不是简单多存一份凭据：Metabase按组授予权限，多组可能取最宽松访问，需要实际检查数据与集合的组合。维护这些知识可能形成可靠交付能力，同时也是持续人工成本。若企业已有成熟语义层和分析团队，服务的差异会缩小。不能把客户数据或私人约定放进公开Git来建立所谓壁垒，本轮只发布无真实数据的检查收据。

依据：S11775be95e18, S886a192f0a23, S28d436fb8ccb

## 本地合成检查和生产边界

本轮用Python标准库SQLite构造虚构租户、八个用户和四条事件，未运行Devin、MCP、云仓库或Metabase。参数化查询在半开区间、UTC、排除测试账户下得到四周2、1、1、0，渠道有一项unknown；只有已知完整覆盖的合成周可补零。重复事件让直接连接后的行数为5、实际用户4、金额20；按虚构唯一事件去重后已知金额10，另有一个NULL和一个真实零，10只能称已知部分合计。只读URI、query_only与授权器拦截UPDATE、CREATE、ATTACH和关闭只读设置，数据库前后哈希一致；恶意租户字符串返回空。此处去重键与冲突策略仅针对固定样本，不能推广为生产ETL方案。PostgreSQL只读事务不等于阻止全部磁盘写入，也不能单独替代角色授权、租户隔离、扫描限额与超时；SQLite检查不是这些云仓库控制的验证。人工SQL检查还需看语义，查询跑通并不代表答案正确。本地收据保存查询文本、参数与预期结果，另生成标有纯合成数据的独立HTML表图文件。只提交无真实数据的结果与哈希，原始数据库留在忽略目录。一次固定样本通过不代表未来输入、并发或不同SQL方言都已覆盖。

依据：S3203eeb395d9, S11775be95e18, S886a192f0a23

## 独立反馈检索与证据缺口

暂无直接用户反馈。

依据：S4da357a2f3b4, S11775be95e18, S28d436fb8ccb

## 先作为受审阅的内部效率工具

商业结论是适合内部效率工具，暂不据此承诺外部服务规模或自动决策收益。原文足以支持一个可检查工作流，公开技术资料也提供权限和竞争基线，但真实正确率、净省时、成本、DANA当前可用资格和独立付费需求均未知。自用价值为中：懂SQL与业务口径的人可能减少重复整理、异步获取初稿；没有审阅能力的人不应将图表当作事实。下一步是选少量无敏感信息的固定历史问题，由两名业务/数据审阅者分别核对口径和结果，计入准备、修正和维护的全部时间，再比较固定报表或内建BI。停止条件包括权限范围不明、跨租户结果、空值当零、重复连接未识别、分享者越权、人工总时间不降或超出预算。需要额外付费、凭据或真实数据的验证留为未知，本轮不进行这些操作。在统计净收益时，应把工程师等待队列、实际执行耗时和审阅者工作量分别记录；即使响应更快，若审阅更重，也不能宣称已经降低成本。没有合法公开采购与用户结果时，保留不确定性比补一个看似精确的收益数字更有用。

依据：S4da357a2f3b4, S3203eeb395d9, S886a192f0a23, S11775be95e18, S58791169610f, S28d436fb8ccb

## 单位经济测算：情景假设，不是项目已实现的财务结果

| 情景 / 交付单位 | 收入 | 可变成本（含获客） | 单位贡献 | 月交付量 | 月固定成本 | 月经营贡献 |
|---|---:|---:|---:|---:|---:|---:|
| 假设：月度受审阅数据问答维护 / 客户/月 (USD) | 600.00 | 410.00 | 190.00 | 10 | 500.00 | 1400.00 |
| 假设：一次设置与验收 / 项目 (USD) | 3000.00 | 2485.00 | 515.00 | 2 | 500.00 | 530.00 |

假设：月度受审阅数据问答维护假设：全为预算假设，人工6小时×40；增至12小时则单位-50、月-1000。DANA价格/仓库扫描/采购与税等未知，不是厂商报价或实测收益。；API成本 80，人工成本 240，其他可变成本 30，分摊获客成本 60。依据：S58791169610f, S28d436fb8ccb, S3203eeb395d9

假设：一次设置与验收假设：全为预算假设，人工45小时×45；多12小时返工增加540，单位-25、月-550。额外费用未知，不是已成交收入或实际利润。；API成本 60，人工成本 2025，其他可变成本 100，分摊获客成本 300。依据：S58791169610f, S28d436fb8ccb, S3203eeb395d9

## 反证与未核实信息

当前Metabase已有内建问答、SQL与MCP路径，简单入口容易被替代；复杂SQL研究说明必须按自身任务验证，不能只看执行成功。原文工程PR总数不是DANA结果。

未运行DANA、模型、云仓库、MCP或Metabase，也未使用真实凭据/业务数据。DANA文档、Devin定价与主页请求404，不重试。SQLite合成结果不构成生产只读/隔离、模型准确率或可分享看板权限证明；Spider2技术基准非DANA用户评价。原站仅使用批准Git归档，无证书警告后请求。

## 具体动作与止损条件

用无敏感信息的固定问题集核对SQL、人工参考答案、权限与总投入时间，再与现有BI比较。

停止投入条件：口径或权限不明、跨租户、空值当零、重复连接、分享越权、总人工不降或预算超标时停止扩展。

## 来源与对应关系

- [S4da357a2f3b4] [How Cognition Uses Devin to Build Devin | Cognition](https://cognition.com/blog/how-cognition-uses-devin-to-build-devin)：Cognition团队一手内部工作流：DANA查询、SQL和图表、Slack入口；Metabase示例来自同文MCP章节。没有DANA量化净收益，通篇工程PR数不属于该数据案例。
- [S3203eeb395d9] [PostgreSQL: Documentation: 18: SET TRANSACTION](https://www.postgresql.org/docs/current/sql-set-transaction.html)：PostgreSQL官方事务访问模式与快照语义；只读是数据库层配置，默认读写，且并不阻止所有磁盘写入。不是DANA权限实测。
- [S886a192f0a23] [Permissions introduction | Metabase Documentation](https://www.metabase.com/docs/latest/permissions/introduction)：Metabase官方分组、最宽松权限及数据/集合权限机制；用于分享与访问验收对照，不是原案例权限配置记录。
- [S11775be95e18] [Spider 2.0](https://spider2-sql.github.io/)：独立研究团队Spider2真实企业SQL工作流评估及动态版本说明；支持必须评测复杂SQL的依据，不是DANA成绩或用户满意度。
- [S58791169610f] [Metabase Pricing](https://www.metabase.com/pricing?use_case=bi)：Metabase当前公开计划与额外AI使用费用，说明替代方案和成本口径；不构成Devin/DANA报价或实际采购。
- [S28d436fb8ccb] [AI in Metabase overview | Metabase Documentation](https://www.metabase.com/docs/latest/ai/overview)：Metabase官方当前内建Metabot、MCP及agent开发路径及权限/计划区别，构成现成竞争基线；不推定原案例采用当前全部功能。

结构化记录：[research/answer-data-questions-and-build-dashboards-from-the-warehous.json](../research/answer-data-questions-and-build-dashboards-from-the-warehous.json)
