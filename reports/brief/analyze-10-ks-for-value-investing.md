# 用 AI agent 分析 10-K 年报并估算企业价值

## 中文

    分析 10-K 年报以进行价值投资研究
    发帖人正在试验一个 LLM agent，让它读取 10-K 年报，并处理正常化盈利、投资资本回报率（ROIC）、股东盈余（owner earnings）和粗略的反向现金流折现估值（reverse DCF）。
    实际使用
    自建或未命名的 agent
    他们做了什么
    发帖人正在测试一个 LLM 投资助手，让它读取 10-K 年报，并尝试生成正常化盈利、ROIC、股东盈余和粗略的反向 DCF。帖子中，他们说自己先使用 EDGAR/XBRL Companyfacts，后来改用更容易使用的 API，但遇到了自定义标签、附注和回测数据泄漏的问题。评论者建议采用这样一种工作流：把结构化的主要财务数字与对申报文件正文的检索结合起来，将来源段落和逐年整理的陈述保存在聊天之外，并由人核验棘手的可比性问题。
    结果如何
    来源没有报告绩效结果，只讨论了问题和部分修正：把整段历年申报文件输入模型会触及上下文限制；分块处理又导致证据遗漏和事实编造；由于重述与申报时滞，回测结果好得不真实。发帖人的体会是，带引用的检索、合理性检查，以及仅使用当时可获得的输入，让这套流程更可信，但仍没有解决跨公司附注比较的问题。
    需要知道的事
    大部分实用建议都围绕避免虚假的信心：每份申报文件只处理一次，保留提取后的结构和段落位置，此后只处理新申报文件，以控制成本。
    自己试试
    推荐工具
    Claude
    复制提示词
    分析[公司名称或股票代码]最新的 10-K 年报，我会附上文件或链接：[文件或 URL]。计算正常化盈利、ROIC 和股东盈余，展示每项调整及所用的报表项目。然后做一个粗略的反向 DCF，说明在[折现率]%的折现率下，当前[价格]隐含了怎样的增长。最后写一页摘要，列出你的假设及任何不确定之处。
    原始来源：https://www.reddit.com/r/ValueInvesting/comments/1x52d8o/anyone_building_a_value_investing_agent_what_are

<details>
<summary>英文原文</summary>

    Analyze 10-Ks for value investing
    The poster is experimenting with an LLM agent that reads 10-Ks and handles normalized earnings, ROIC, owner earnings and a rough reverse DCF.
    Done with a
    custom-built or unnamed agent
    What they did
    The poster was testing an LLM investing assistant that read 10-Ks and tried to produce normalized earnings, ROIC, owner earnings, and a rough reverse DCF. In the thread, they say they first used EDGAR/XBRL Companyfacts, then easier APIs, but ran into custom tags, footnotes, and backtest leakage; commenters pushed a workflow that combines structured headline figures with retrieval over filing text, stores source passages and year-by-year claims outside the chat, and leaves the human to verify tricky comparability issues.
    How it went
    The source reports no performance results, only problems and partial fixes: feeding whole filing histories hit context limits, chunking led to missed evidence and invented facts, and backtests looked unrealistically good because of restatements and filing lag. The poster’s takeaway was that retrieval with citations, sanity checks, and point-in-time inputs made the setup more trustworthy but did not solve cross-company footnote comparisons.
    Worth knowing
    Most practical advice was about avoiding false confidence: process filings once, keep extracted structure and passage locations, and only run new filings afterward to control cost.
    Try it yourself
    with
    Claude
    Copy prompt
    Analyze the latest 10-K for [company name or ticker], which I'll attach or link: [file or URL]. Calculate normalized earnings, ROIC, and owner earnings, showing each adjustment and the line items you used. Then build a rough reverse DCF showing what growth the current price of [price] implies at a [discount rate]% discount rate. Finish with a one-page summary that notes your assumptions and anything you were unsure about.
    Original source: https://www.reddit.com/r/ValueInvesting/comments/1x52d8o/anyone_building_a_value_investing_agent_what_are

</details>

## 原作者的方法与来源

来源：[登记的Reddit原始讨论（本轮未读）](https://www.reddit.com/r/ValueInvesting/comments/1x52d8o/anyone_building_a_value_investing_agent_what_are)

方法摘要未收录

遵守既有来源访问停止，未请求原帖；案例站转述和搜索摘要不能替代已读作者原文。

## 我们的简要分析

商业判断：只在人工复核下验证研究辅助；商业分数未评定，自用价值待核实。本稿不计入completed v2深研。

仅有案例站转述及两份官方/学术基础资料；原始讨论未读、SEC API说明遭robots拒绝，缺少可归属实现、运行结果、独立验证、成本和客户。材料不足以完成v2商业深研；保留有依据简报，不生成商业分数。

### 商业判断与证据层级

当前仅建议把它作为人审辅助研究流程来验证，商业分数未评定，自用价值待核实。本稿是简要分析，不计入completed v2深研。已取得的案例站转述描述了一个试验中的未命名agent，同时报告数据、检索和回测问题；没有原作者代码、真实样本、逐项结果、客户或成本。不能因为出现ROIC、股东盈余和反向DCF等术语，就把它写成已经成立的投资产品或可靠收益来源。潜在使用者是假设中会逐项复核申报文件的研究人员，付款人、预算和购买意愿均未验证。

依据：archive-case-20261017, S41ca1220801c, S19844cab18d1

### 先保存来源与调整，再谈估值

归档转述的链路是结构化数字与申报正文检索结合，保留来源段落和逐年陈述，由人核对可比性。它不是可执行工作流说明，也没有披露模型、API供应商、提示词或分块策略。原始Reddit讨论未读，方法字段保持unavailable，不能根据搜索摘要编造作者步骤。Claude是源站推荐工具，实际agent仍自建或未命名。后续验证应先把年度、申报版本、币种、单位、对应原始行项和调整理由写成可检查台账，再用明确公式复算；一个数字带了引用，不代表引用真的支持该项调整。

依据：archive-case-20261017, S41ca1220801c

### 年度、版本与当时可获得信息分开

案例站转述提到自定义标签、附注、整段历史超出上下文、分块遗漏及事实编造，也提到重述和申报时滞让回测显得过好。这些都是转述，未取得原始样本或独立错误率。评估时应分别保存报告覆盖期、首次公开日期、所用版本及检索位置，明确某个回测时点到底能看到什么。最新可下载数字不能自动当成历史已知数字；只让模型写一句“按当时数据”也不是可复核的输入筛选。SEC API文档遭robots拒绝，未用它核实Companyfacts具体覆盖范围或接口字段，不补写其规则。

依据：archive-case-20261017, S41ca1220801c

### 公开申报与透明表格是必要基线

Investor.gov说明10-K覆盖公司业务和财务状况并包含审计财务报表，但审计不延伸到agent自己做的盈利调整、增长假设或估值结论。Damodaran目录公开列出正常化盈利、折现率及不同DCF模型的表格说明，显示透明计算本身已有可用比较构件；本轮没有下载或运行它们，也不宣称适合所有公司。正常化盈利、ROIC、股东盈余与FCFF/FCFE应给各自定义，不能换个标题就当作同一数字。反向DCF得到的是在指定模型和假设下的隐含条件，并不证明未来增长会发生。

依据：S41ca1220801c, S19844cab18d1, archive-case-20261017

### 验收应检查可追溯性和错误

可设计一个离线小样本：使用明确版本的公开或合成报表，包含一次性项目、单位变化、负盈利、缺失字段及同一期间的不同版本，先由人写参考台账。逐项检查提取值、来源位置、调整计算和跨年一致性，再比较直接人工表格与候选agent的修复工时。正文检索缺证据时应返回缺失，不从其他年度或另一公司补齐。模型推导和原报表事实分别展示，所有假设可变更和重算。本轮未跑模型、下载真实财务数据集或构建回测，没有准确率、收益率或节时结果。

依据：archive-case-20261017, S41ca1220801c, S19844cab18d1

### 两种交付预算与人工敏感性

以下全为USD规划假设，不是作者账单、市场报价或实际客户。99美元每份文件核对包，资源2、人工2小时×50美元=100、其他3、获客15，可变120，贡献-21；20份减固定200，月贡献-620。团队月度辅助服务299美元，资源10、人工3小时×50美元=150、其他20、获客摊销40，可变220，贡献79；10客户减固定500，月贡献290。额外两小时复核使单客户贡献变为-21。后者不含首次接入，数据许可与工具成本归属尚需按实际合同明确；不能因申报资料公开，就假设所有后续数据、分发和支持都零成本。

依据：archive-case-20261017, S41ca1220801c, S19844cab18d1

### 继续条件、反证与停止条件

有利反证是这套转述提出了保存结构与引用、按新增申报增量处理的务实方向，公开表格也使离线复算成为可能；它足以支持研究方案，不足以支持商业承诺。先取得可确认归属的实现、固定样本及可复现结果，再决定是否升级深研。若来源无法支持调整、单位和年度频繁混淆、历史时点不能锁定，或人工纠错超过预算，应停止扩大规模，保留台账返回基线。原始投资目标、持仓与私人账单不属于本次任务；本稿没有评价任何具体证券或执行交易。

依据：archive-case-20261017, S41ca1220801c, S19844cab18d1

## 事实与证据边界

- 源站实际工具是自建或未命名agent；Claude只是Try it yourself推荐，不能当成作者实际模型。（archive-case-20261017）
- 案例归档转述的是试验与问题，没有报告绩效结果、收益率、独立测试或付费客户。（archive-case-20261017）
- 归档转述建议保留结构化数字、来源段落及逐年陈述，并由人核对跨公司可比性；原始讨论本轮未读。（archive-case-20261017）
- Investor.gov说明Form 10-K包含公司业务与财务状况概述及审计财务报表，并区别于给股东的年度报告。（S41ca1220801c）
- Damodaran目录提供正常化盈利、折现率及FCFF/FCFE等表格说明，不等于本案例已采用这些模型。（S19844cab18d1）
- 本轮只读取文档和归档，没有执行agent、表格、回测或交易，也没有形成任何证券价格或收益判断。（archive-case-20261017, S41ca1220801c, S19844cab18d1）

## 成本情景（全部是假设）

| 情景 | 假设收入 | 资源 | 人工 | 其他 | 获客 | 单位贡献 | 月贡献 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 规划假设：单份申报文件核对包 | 99 | 2 | 100 | 3 | 15 | -21 | -620 |
| 规划假设：团队月度辅助维护 | 299 | 10 | 150 | 20 | 40 | 79 | 290 |

币种USD，全部为规划假设，不是实际收入、账单、投资收益或市场报价。
## 自用价值：待核实

没有可归属实现或实际样本，不能核实此agent的节时和质量；有财务背景的人可先检查离线提取与复算方案。

依据：archive-case-20261017, S41ca1220801c, S19844cab18d1

- 适用人群：能够逐项阅读申报文件、定义调整和核对公式的研究人员。
- 用途：建立来源与调整台账，评估有限范围的财报整理辅助。
- 预期收益：潜在减少重复查找，但未测得准确率、节时、金额或投资回报。
- 设置成本：明确版本与时点的合成/公开样本、人工参考台账、单位口径与离线计算工具。
- 维护成本：维护字段、申报版本、附注与回归样本，记录人工纠错和资源支出。
- 使用频率：按实际研究和新增申报需要使用，未核实原例频率。
- 隐私风险：本轮不收集持仓、私人账户或交易记录，不将个人材料公开。
- 错误风险：可能混年度、版本、单位和指标定义，漏附注或编造调整，必须回到原文和公式核对。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/analyze-10-ks-for-value-investing

建议工具：Claude

    Analyze the latest 10-K for [company name or ticker], which I'll attach or link: [file or URL]. Calculate normalized earnings, ROIC, and owner earnings, showing each adjustment and the line items you used. Then build a rough reverse DCF showing what growth the current price of [price] implies at a [discount rate]% discount rate. Finish with a one-page summary that notes your assumptions and anything you were unsure about.

自编试用模板

准备条件：离线合成或明确版本的公开报表样本、人工参考台账、指标定义与估值假设；不需要账户或新凭据。

工具：实际agent自建或未命名；源站推荐Claude。本轮仅文档与静态校验，不调用模型或付费数据。

预期结果：可追溯字段台账、调整公式、缺失项和测试计划；自编模板未实测，不生成真实买卖判断。

### 先核对来源与口径，再展示估值假设

自编模板

出处：研究团队自编

依据：archive-case-20261017, S41ca1220801c, S19844cab18d1

    只使用[明确版本的公开或合成10-K样本]、[人工参考台账]及[指标定义]。先输出报表项目、数值、币种、单位、覆盖期、申报版本、公开日期和来源段落；缺失项标未知，不从其他年度或公司补齐。为正常化盈利、ROIC和股东盈余逐项写出定义、公式、调整及原始行项，区分报表事实和研究假设；不要将不同现金流口径直接互换。需要反向DCF时，只在[给定价格、折现率、现金流口径、预测期和终值假设]下展示隐含条件及敏感性，不将其说成未来结果。用相同样本与人工表格比较，记录提取错误、无依据调整和修复工时；历史回放只用该时点已公开版本，明确无法核实的地方。不得访问私人账户、下单、创建凭据或调用额外付费API；不要绕过来源限制。本轮只给可检查台账与方案，不声称完成真实投资验证。

## 来源

- archive-case-20261017：[Analyze 10-Ks for value investing](https://agentusecases.ai/use-case/analyze-10-ks-for-value-investing)。支持源站归档转述的用途、数据与回测问题及推荐模板；不是已核实Reddit作者原文。
- S41ca1220801c：[Form 10-K | Investor.gov](https://www.investor.gov/introduction-investing/investing-basics/glossary/form-10-k)。SEC旗下Investor.gov说明10-K概述业务与财务状况、包含审计财务报表，并区别于股东年度报告；不证明agent派生估值或历史回测正确。
- S19844cab18d1：[Spreadsheet programs](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/spreadsh.htm)。Damodaran公开表格目录列出正常化盈利、折现率、FCFF/FCFE与模型协调工具，是透明计算的替代基线；本轮仅阅读说明，未下载或执行表格，也不把股东盈余自动等同于某一现金流模型。

## 仍待核实

没有原始讨论、作者代码、模型、API配置、真实财务样本、时点数据集、运行/回测结果、成本或客户。SEC API文档robots拒绝后停止，无换路；源站仅用既有Git归档。未下载执行NYU表格、未调用模型或真实财务API、未访问账户或交易。
