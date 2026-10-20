# 用Claude Code跟踪公开交易披露并记录小额账户操作

## 中文

    跟踪政治人物交易，用小额Robinhood账户进行交易
    作者通过MCP把Claude Code接入Robinhood的智能体交易测试版，并投入100美元；它观察政治人物和企业高管的交易，追踪持仓实时盈亏，并执行真实交易。
    使用的是
    Claude Code
    他们做了什么
    Ryan Doser把Robinhood的交易MCP端点加入Claude Code，在桌面端完成OAuth，并在Robinhood手机应用中进行验证。他花15至30分钟编写了一个观察政治人物和企业高管交易的技能。Claude询问他的交易偏好，还在没有被要求的情况下建立了Markdown交易日志。随后它买入了四只股票。
    进展与成效
    资金隔夜结算后，它在次日开盘买入四只股票，包括几只保险股和挪威邮轮。开盘时账户约上涨33美分。收益尚未得到证明。
    值得了解
    要执行交易，电脑上的Claude Code必须保持开启，因为定时任务只有它运行时才工作。这是测试版，因此只应投入能够承受损失的钱。
    亲自尝试
    使用Claude Code
    复制提示词
    帮我设计一个小型实验，观察[政治人物或企业高管]公开披露的交易，并为[券商]的[美元金额]账户维护持仓和实时盈亏日志。先以只读模式运行，每天报告你会考虑做什么交易以及原因。在下任何真实订单之前，停下来向我展示股票代码、数量和价格，并等待我明确说“是”。
    原始来源：https://ryandoser.com/ai-trading-agent-robinhood/

<details><summary>English original</summary>

    Trade a small Robinhood account by tracking politician trades
    The author connected Claude Code to Robinhood's agentic trading beta via MCP with a $100 account; it watches politician and executive trades, tracks positions with live P&L and places real trades.
    Done with
    CC
    Claude Code
    What they did
    Ryan Doser added Robinhood's trading MCP endpoint to Claude Code and finished OAuth on desktop, with a verification step in the Robinhood mobile app. He wrote a skill in 15 to 30 minutes that watches politician and executive trades. Claude asked him about his trading preferences, and it started a markdown trade log without being asked. It then bought four stocks.
    How it went
    After overnight fund settlement, it bought four stocks at market open, including a couple of insurance names and Norwegian Cruise Line. The account was up about 33 cents at open. Returns are unproven.
    Worth knowing
    Claude Code has to stay open on your computer for trades to execute, since the cron job only works while it's running. It's a beta, so only fund it with money you can afford to lose.
    Try it yourself
    with
    Claude Code
    Copy prompt
    Help me build a small experiment that watches publicly disclosed trades by [politicians or executives] and keeps a log of my positions with live profit and loss for a [dollar amount] account at [broker]. Start in read-only mode and give me a daily report of what you would trade and why. Before placing any real order, stop and show me the ticker, size and price and wait for my explicit yes.
    Original source: https://ryandoser.com/ai-trading-agent-robinhood/

</details>

## 原作者的方法与来源

https://ryandoser.com/ai-trading-agent-robinhood/
原文发布日期2026-06-11；以下仅简要转述，不复制外链全文。

作者接入专用券商账户，设定偏好并观察小额实验。
The author connected a dedicated brokerage account, specified preferences, and monitored a small experiment.

他描述了生成的决策日志与依赖本地会话的运行方式，业绩仍未证实。
He describes a generated decision log and a locally running session; performance remains unproven.

## 简要分析

商业分数未评定。

### 已展示连接与买入流程，策略仍不可复核

作者文章日期为2026年6月11日，本次目录按10月18日收录顺序处理，两者不是同一时间。文章有连接、交易日志和持仓的展示，但没有完整可下载策略、输入披露数据版本、长期交易流水或受控比较。因此交付有依据简报，不能把通用交易接口资料补成对作者策略的完整深研，也不能把营销作者的介绍转为审计结论。

依据：[Sdirectory](https://agentusecases.ai/use-case/trade-a-small-robinhood-account-by-tracking-politician-trade), [Sauthor](https://ryandoser.com/ai-trading-agent-robinhood/)

### 33美分不是稳定赚钱模式

目录明确说收益未证实。100美元是实验本金，33美分是开盘时点的账户变化，不是收费收入、完整周期净收益或风险调整结果。研究者判断：缺交易费用、价差、持仓风险、持续时间和基准，任何年化外推都没有依据。一次成功调用买入工具只能说明执行链路发生，无法证明选股信息有优势。

依据：[Sdirectory](https://agentusecases.ai/use-case/trade-a-small-robinhood-account-by-tracking-politician-trade)

### 披露时点必须与交易时点分开

众议院要求相关人员对部分超过1000美元证券交易在知悉后30日与交易后45日两者较早的日期申报。Form 4通常在交易后两个工作日提交，两类数据不能混为实时信号。研究者建议记录交易日、披露日和系统实际取得时间；模拟只能使用当时已公开的信息，不能把后来公开的记录回填到过去，否则会产生前视偏差。

依据：[Shouse](https://ethics.house.gov/financial-disclosure/), [Ssec](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-69)

### 不是所有高管持仓变化都是主动买卖信号

SEC教育材料区分购买、出售、授予、行权、缴税和赠与等交易代码，并说明出售可能出于流动性或分散需求。研究者建议先规范事件分类，再讨论是否形成信号；把所有增加都当看多、所有减少都当看空会混淆含义。还需核对主体、重复报告和更正版本，这些处理本案没有可审查实现。

依据：[Ssec](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-69)

### 专用交易账户不代表数据全部隔离

当前官方说明外部智能体可读取全部Robinhood账户的账号、余额、持仓和交易历史，但交易权限限专用Agentic账户。因此100美元实验资金不能等同于只暴露100美元账户资料。只读访问也可能涉及敏感财务数据，复制前必须看实际授权范围。本轮只读公共说明，没有连接券商、访问个人账户、创建凭据或资金操作。

依据：[Saccess](https://robinhood.com/us/en/support/articles/agentic-trading-overview/)

### 提示词确认与平台审核设置分别核对

官方说明内置Robinhood Agents默认开启交易审核，外部MCP账户默认关闭；MCP审核功能仍逐步开放，并非所有客户已有。开启后用户需在应用内审核并手动下单。目录模板要求等待明确确认，这是模板文字，不能据此认定账户已有强制审核。研究建议的演练只保留离线记录，不进入真实下单；不能用聊天中的泛化许可替代实际金融操作边界。

依据：[Sapproval](https://robinhood.com/us/en/support/articles/trading-with-your-agent/), [Sdirectory](https://agentusecases.ai/use-case/trade-a-small-robinhood-account-by-tracking-politician-trade)

### 不能用托管智能体价格套算外部Claude

Robinhood词元充值页面明确限定托管智能体，不能据此为外部Claude Code计算费用。作者的运行环境、订阅占用、披露数据服务、维护与复核总工时仍未知。研究者建议将模型和数据费用、运行维护、人工复核以及交易成本分别记录；不以本金规模代替运行成本，也不把Markdown日志自动出现当作模型已经有效学习。

依据：[Scost](https://robinhood.com/us/en/support/articles/token-usage-billing/), [Sdirectory](https://agentusecases.ai/use-case/trade-a-small-robinhood-account-by-tracking-politician-trade)

### 更可检验的是研究记录工具，而不是收益承诺

商业假设可限于公开披露去重、时点标注和研究日志整理，先与手工检索官方披露比较。潜在付款人是确有重复研究负担的人，尚未验证本案愿付费或留存。现有券商数据和公开官方查询已提供基础替代，自定义工具需证明减少核对工作。若进一步涉及他人资金、个性化建议或代执行，需另行核实适用资质与义务；本报告不认定某种服务天然合规，也不代用户开展经营。

依据：[Saccess](https://robinhood.com/us/en/support/articles/agentic-trading-overview/), [Ssec](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-69)

### 个人价值取决于能否持续校验

自用者应具备理解公开披露和检验交易记录的能力。价值可能在组织资料、解释动作和保留日志；实际净收益待测。初始设置包括策略定义和数据口径，维护包括会话运行、数据延迟、重复任务和错误恢复。目录提醒本案例定时任务依赖Claude Code持续开启，这不是所有平台的通用限制。频率需要根据披露更新而设，没有必要用高频调用制造“实时”假象。

依据：[Sdirectory](https://agentusecases.ai/use-case/trade-a-small-robinhood-account-by-tracking-politician-trade)

### 先完成不接账户的历史可用性审计

下一步可自制几条虚构披露事件，逐条写交易日、公开日、取得日、事件代码和假设观察价，验证程序不会提前看到未来资料。输出研究日志和缺失项，不输出真实订单，不连接账户；加入重复事件、更正和会话中断，检查恢复后是否重复处理。只有拿到原策略与完整成本资料，才能继续评价复制价值。若只剩收益截图、无法重建时点，或费用超过可解释的研究价值，应停止投入。

依据：[Shouse](https://ethics.house.gov/financial-disclosure/), [Ssec](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-69)

## 试用准备与预期结果

虚构披露事件与人工可核验的时间线，无账户数据。
时点明确的研究日志、重复项和未知项清单；本轮未测试。
只分析给定虚构事件，不联网取账户数据，不连接券商或下单。分别记录交易日、公开日、取得时间和事件代码；没有公开的资料在模拟当时不可使用。识别重复和更正，生成研究日志与未知项；不要给真实证券买卖建议或收益承诺。

## 来源

- [许可目录既有正文档案](https://agentusecases.ai/use-case/trade-a-small-robinhood-account-by-tracking-politician-trade)：原文及模板保留；原档案日期不冒充本次采集。
- [Ryan Doser的2026-06-11实操文章](https://ryandoser.com/ai-trading-agent-robinhood/)：100美元、四笔买入、33美分为作者自述，展示连接和日志流程，未证明收益。
- [Robinhood外部智能体接入说明](https://robinhood.com/us/en/support/articles/agentic-trading-overview/)：交易限专用账户，读取范围涉及所有Robinhood账户。
- [Robinhood交易审核设置](https://robinhood.com/us/en/support/articles/trading-with-your-agent/)：内置与外部账户默认审核设置不同，MCP审核功能仍在逐步开放。
- [众议院交易披露期限](https://ethics.house.gov/financial-disclosure/)：特定超过1000美元证券交易以知悉30日/交易45日孰早为期限。
- [SEC投资者教育：Form 4](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-69)：两工作日及交易代码区分，出售不必然表达看空。
- [Robinhood托管智能体计费边界](https://robinhood.com/us/en/support/articles/token-usage-billing/)：该词元充值说明只适用于托管智能体，不适用于本案外部Claude Code。
