# 用 Claude Code 汇集市场数据并生成投资分析

## English

    Generate investment analysis from live market data
    The poster built a personal wealth advisor in Claude Code that feeds live market data, macro indicators and news into investment analysis.
    Done with
    CC
    Claude Code
    What they did
    The poster used Claude Code CLI to build a personal wealth advisor that pulled live market data, macro indicators and news into one workflow, then fed it to Claude with a CFA-style system prompt. In comments, they say a memory system let it recall and revisit earlier calls from weeks prior, which improved analysis quality; the person built the setup and used Claude’s output rather than handing decisions over fully.
    How it went
    They say the goal was analysis beyond generic stock tips, but the thread excerpt gives no performance numbers or verified investing results. What’s shown is a personalized research workflow, with the strongest claimed benefit being better output from retained memory.
    Worth knowing
    The main catch mentioned is that the memory layer mattered a lot: being able to reference what it said two weeks earlier noticeably changed output quality.
    Try it yourself
    with
    Claude Code
    Copy prompt
    Build me a small personal investment research tool in this folder. It should pull live market data for [tickers or funds I hold], key macro indicators like [rates, inflation, unemployment], and recent news, then write a short analysis of how these affect my portfolio of [brief description]. It is done when I can run one command and get a dated report with sources, and it should not place any trades.
    Original source: https://www.reddit.com/r/ClaudeAI/comments/1sdtgof/used_claude_code_to_build_myself_a_personal

## 中文

    根据实时市场数据生成投资分析
    发帖者用 Claude Code 搭建了一位个人财富顾问，将实时市场数据、宏观指标和新闻输入投资分析流程。
    使用的 Agent
    Claude Code
    他们做了什么
    发帖者使用 Claude Code 命令行工具搭建了一位个人财富顾问，将实时市场数据、宏观指标和新闻汇集到同一套工作流程中，再配合一段 CFA 风格的系统提示词，将这些内容交给 Claude。发帖者在评论中称，一套记忆系统让它能够回忆并重新审视数周前的判断，从而改善了分析质量；这个人搭建了整套系统并参考 Claude 的输出，而没有把决策完全交出去。
    结果如何
    他们说，目标是获得超越泛泛股票建议的分析，但帖子摘录没有给出表现数据，也没有经过核实的投资结果。展示出来的是一套个性化研究流程，其中声称最明显的收益是保留记忆后输出有所改善。
    需要知道的事
    提到的主要关键点是记忆层影响很大：能够引用自己两周前说过的话，明显改变了输出质量。
    自己试试
    推荐工具
    Claude Code
    复制提示词
    在这个文件夹里，为我搭建一个小型个人投资研究工具。它应获取[我持有的股票或基金代码]的实时市场数据、[利率、通胀、失业率]等关键宏观指标，以及近期新闻，然后简要分析这些因素如何影响我的投资组合[简短描述]。当我能够运行一条命令，得到一份带日期和来源的报告时，任务就算完成；它不应执行任何交易。
    原始来源：https://www.reddit.com/r/ClaudeAI/comments/1sdtgof/used_claude_code_to_build_myself_a_personal

## 原作者的方法与来源

来源：[个人投资研究工具的原始讨论](https://www.reddit.com/r/ClaudeAI/comments/1sdtgof/used_claude_code_to_build_myself_a_personal)

方法摘要未收录

## 我们的分析

**商业结论：适合内部效率工具。先验证来源准确和历史观点可回看，再判断能否减少研究准备时间**

这套流程适合已经了解自己持仓、能核对来源的个人研究者，或需要整理研究材料的小团队。可购买的交付是有日期、来源和旧观点对照的准备报告，不是CFA风格提示词带来的专业资质或确定收益。案例没有实测节时、客户付费或投资结果；实时行情权限、新闻使用、数据修订和持续人工核对都会影响成本。先把它作为内部研究整理工具，验证数字与历史记录可信，再考虑是否向外提供设置或维护服务。

案例ID：`generate-investment-analysis-from-live-market-data` · 案例来源：https://agentusecases.ai/use-case/generate-investment-analysis-from-live-market-data
研究时间：2026-10-16T18:02:24.876149+00:00

**商业评分：36.0/100。用户反馈信号占5%。**

| 维度 | 权重 | 分数 /5 | 商业依据 |
|---|---:|---:|---|
| 付费需求 | 20% | 2 | 持仓研究准备重复发生，但没有本工具付费客户、采购预算或持续使用测量。 [S3a6a528996dc, Sb330d233b801] |
| 业务价值与效果证据 | 20% | 2 | 带来源的报告是明确交付，记忆改善只有自述，无节时对照和经核实投资结果。 [S3a6a528996dc, Sf1c064262dc8] |
| 单位经济与利润 | 20% | 2 | 小范围内部整理可建模，但行情许可、上下文和逐份复核会压缩订阅利润。 [S7c26178a4fa1, S1cd92766e9ea, S0d35d49f9cdb] |
| 获客与市场进入 | 15% | 2 | 面向有研究习惯的客户展示样张可验证需求，缺少真实转化与销售渠道记录。 [S3a6a528996dc, Sb330d233b801] |
| 竞争壁垒 | 10% | 1 | 数据汇总、记忆和组合记录已有原生能力，CFA风格提示词本身难形成壁垒。 [Sf1c064262dc8, Sb330d233b801] |
| 交付与经营风险 | 10% | 2 | 报告流程可保持只读，但数据版本、持仓口径和历史判断审计需要维护。 [S8ee4e77ee196, S1cd92766e9ea, Se6592070cda0] |
| 独立用户反馈信号 | 5% | 0 | 读取到邻近开发工作流体验，但没有本个人投资工具的独立用户效果验证。 [S3a6a528996dc, Sb75449d97aab] |

## 自用价值：中

适合已有研究习惯的人整理输入和回看旧观点；这种辅助价值是基于流程的推断，没有已测节时或投资表现，与商业评分分开判断。

依据：S3a6a528996dc, Sf1c064262dc8, S8ee4e77ee196, S1cd92766e9ea, Se6592070cda0

- 适用人群：能核对持仓、行情口径和信息时间的个人研究者或小型团队。
- 用途：生成带日期与来源的准备报告，比较今天输入与过去观点及其依据。
- 预期收益：有机会减少重复汇总并改善记录完整度；不能据记忆存在推断判断正确或收益改善。
- 设置成本：先整理脱敏持仓比例、允许使用的行情/新闻和宏观快照、日期口径、人工样例及报告格式。
- 维护成本：检查数据更新与修订、公司行动、新闻来源和记忆记录；定期核对接口及输入变化。
- 使用频率：按实际研究需求每周或每天准备，先确定可接受延迟，不为追求实时而无上限刷新。
- 隐私风险：持仓金额与研究偏好需限制暴露，优先用脱敏比例；不提供券商交易凭据。
- 错误风险：复权、货币、数据版本与旧新闻混用会产生错误解释；历史记忆可能反复强化未经核实观点。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/generate-investment-analysis-from-live-market-data

建议工具：Claude Code

    Build me a small personal investment research tool in this folder. It should pull live market data for [tickers or funds I hold], key macro indicators like [rates, inflation, unemployment], and recent news, then write a short analysis of how these affect my portfolio of [brief description]. It is done when I can run one command and get a dated report with sources, and it should not place any trades.

自编试用模板

准备条件：提供脱敏持仓、来源与时间明确的数据快照、原始新闻链接或获准摘录、过往观点及人工核对样例。

工具：现有对话或编码工具可先分析提供的文件；实际行情API和新闻权限需另核实，不自动创建凭据或购买。

预期结果：日期化研究准备报告、确定性数字核对和旧观点变化说明；自编模板未实测，不承诺投资结果。

### 根据资料快照生成投资研究准备报告

自编模板

出处：研究团队自编

依据：S3a6a528996dc, S8ee4e77ee196, S1cd92766e9ea, Sf1c064262dc8

    请仅使用我提供的[脱敏持仓比例、行情与宏观快照、新闻资料、来源和时间、旧研究报告]，为[研究日期与基准货币]生成一份投资研究准备报告。先列数据时间、延迟、货币、复权与宏观版本；缺失或口径冲突单列，不补猜。金额和比例用明确公式核对，事实、推断和待核实项分开。对照[旧观点]时保留原文与日期，说明哪些新证据导致变化，不覆盖旧报告，不拿今天修订值冒充当时已知数据。每项重要判断附来源和时间。不要连接交易账户、买卖、下单、发送消息、创建凭据、购买服务或调用额外收费API。输出报告和需我人工核对的问题后停止，由我判断后续行动。

## 已核验事实

- 源站说作者用Claude Code CLI汇集市场、宏观与新闻，并以CFA风格系统提示词生成个人投资研究。 [S3a6a528996dc]
- 记忆能回看数周前判断并改善分析，是源站转述的用户声称；没有质量对照或投资表现数据。 [S3a6a528996dc]
- 源站试用模板要求一条命令生成带日期和来源的报告，并明确不执行交易；不是已核验的作者原始提示词。 [S3a6a528996dc]
- Claude Code官方文档将CLAUDE.md持久指令与自动记忆区分，项目指令可在会话开始加载。 [Sf1c064262dc8]
- Claude Code成本页说明API token使用与订阅用量口径不同，不能把会话成本估算直接当订阅账单。 [S7c26178a4fa1]
- FRED real-time period表示事实何时成立或信息何时已知；观察数据可修订，默认期间通常为今天。 [S8ee4e77ee196]
- FRED API文档要求请求携带key，并说明应用用户应使用自己的key；本案例未说明作者使用何种宏观接口。 [S0d35d49f9cdb, S3a6a528996dc]
- Alpha Vantage支持页列出一般免费服务每天25次API请求；实时和15分钟延迟美国行情为premium-only。 [S1cd92766e9ea]
- Alpha Vantage说明其复权处理考虑拆股与现金分红，并可为多类端点返回未复权数据。 [S1cd92766e9ea]
- Portfolio Performance记录买卖、税费等交易历史并计算时间加权收益率或IRR，支持XML存储及CSV/JSON导出。 [Sb330d233b801]
- Loomery工程负责人在2025年使用回顾中说复杂、高上下文任务需要小步拆解和复核，某些自动化负担可能大于节省。 [Sb75449d97aab]
- FINRA提示AI输出可能基于过期、错误或受操纵的信息，正确输入也不能保证生成结论正确。 [Se6592070cda0]

## 使用者、付款人与任务

直接使用者是有固定持仓、愿意自己核对信息的个人研究者。其问题通常是行情、宏观发布与新闻散落多处，过段时间又忘记当时为何形成某个观点。若成为付费服务，付款人可能是研究团队负责人，预算来自研究准备和报告维护；个人也可能支付定制工具的设置费用。但一个人的财富管理需求与一家机构的合规采购不是同一市场，不能把所有投资者都当成现成客户。
源站没有给出付费记录、使用频率、资产规模或研究时间。购买理由应落实到输入整理更快、来源更完整、旧观点更容易复核，而不是承诺组合表现。已经用成熟组合软件记录持仓的人，可能只需要把资料导出给研究流程；只想直接得到买卖答案的新手，缺少核对能力，未必适合这套自建系统。优先访谈本来就每周写研究笔记的人，了解其标的数量、数据订阅、最费时步骤和现有工具，再界定服务能替代哪段准备工作。

依据：S3a6a528996dc, Sb330d233b801

## 数据输入、分析与历史记录

案例自述使用Claude Code搭建程序，将实时行情、宏观指标与新闻汇总给Claude，再配合CFA风格系统提示词生成分析。记忆层让它回看数周前说过的话，真人参考输出，没有把决策完全交出。公开摘录未给出提供商、具体接口、完整提示词和程序代码，所以不能把下面的设计建议当作作者实际实现；CFA风格也不表示模型取得专业资格。
可复制流程应先保存持仓基准日、标的标识、计价货币和允许使用的数据来源，再统一价格时间、宏观发布日期与新闻原始链接。由程序做确定性的金额和比例计算，模型负责解释变化及待核实问题。报告中分开列事实、推断和旧观点对照，缺失输入不补猜。Claude Code的持久指令和自动记忆有助于保留上下文，但正式观点日志还应记录输入快照、时间和修订，旧报告不直接覆盖。这样才能比较“当时依据是什么”与“今天看法怎样变化”，而非只让模型重述上次结论。

依据：S3a6a528996dc, Sf1c064262dc8, S8ee4e77ee196

## 可进入范围与数据时效

这里较可验证的需求是个人研究准备和历史观点管理，而不是泛化的自动财富顾问市场。第一版可限定少量股票或基金、少数宏观指标、固定周报或日报；只有确有研究需要且数据权限足够时，再增加频率。源站没有显示客户愿付价格，也未证明分钟级更新比收盘数据更有帮助，不应借“实时”一词推导出更高采购预算。
真实数据接入可能改变可服务范围。Alpha Vantage一般免费服务限制为每日25次请求，美国实时及15分钟延迟行情需要premium访问；这不等于案例作者用了该服务，而是说明“能拿到免费数据”不能代表已获得所需时效。假设20只标的各发3次独立请求就是60次，已超过该基础额度，实际能否批量或缓存要看端点。FRED的实时期间则讲信息何时已知，不是股票逐笔行情。先按用户决策周期定义可接受延迟，再核对来源，不把不同数据的实时含义混为一个卖点。

依据：S3a6a528996dc, S1cd92766e9ea, S8ee4e77ee196

## 组合软件与简单研究笔记

Portfolio Performance是具体替代：它记录买卖、费用与税费，计算组合收益率，导入历史价格并支持数据导出。它解决组合账本和绩效统计，生成式分析流程则增加宏观、新闻解释与历史观点对照，两者功能不完全相同。若用户只想知道持仓、收益率和资产分配，原生组合软件或券商报表可能已经足够，不必再维护模型与新闻连接。
另一个替代是表格加日期化研究笔记，把行情快照、来源和结论按次保存，再用现有对话工具分析提供的材料。它自动化程度低，但起步负担小，也更容易核对过去记录。Claude Code原生记忆降低重复说明的成本，却不能独占“记得上次判断”这一能力。自建工具要证明多源数据整合和旧观点回顾确实更省时，否则客户可以直接使用已有软件与简单笔记。对外定价应比较完整使用成本，包括安装、数据许可、异常恢复和人工复核，不能只比较生成一次报告的token。

依据：Sb330d233b801, Sf1c064262dc8, S7c26178a4fa1

## 单位报告与维护成本

作者没有披露模型或订阅费用、行情和新闻许可、云执行、存储以及人工检查成本，也没有可归因的投资收益，因此不能算投资回报率。Claude Code成本文档区分API计费与订阅用量，会话估算不等于订阅实付账单。个人已经支付的订阅也不能自动视为对外服务的零成本容量；需要知道研究任务是否增加用量、额度限制和后续维护。
第一种假设为每用户每月20份准备报告，收费149美元；模型与数据预算20美元，人工每份10分钟按30美元每小时共100美元，平台与存储20美元，获客摊销15美元，单位成本155美元、贡献负6美元。20名用户再扣200美元固定费后为负320美元；复核每份15分钟时单位贡献降至负56美元。这个预算只适用于已获准使用的有限输入，不是实时行情套餐报价。第二种假设为1800美元的定制设置，API测试40、人工900、其他60、获客200美元，贡献600美元；三单扣600美元固定费后为1200美元，持续维护另定范围。

依据：S3a6a528996dc, S7c26178a4fa1, S1cd92766e9ea, S0d35d49f9cdb

## 首批用户与交付样张

先从已有投资研究习惯、能够说明自己如何形成结论的人群做需求验证。提供同一输入下的两份样张：原有人工笔记与工具辅助报告，让使用者核对关键数字、日期、新闻出处和旧观点变化。观察其是否真的缩短资料准备，而不是只觉得文字更专业。没有客户访谈和试点付款记录前，不能把CFA风格的呈现或记忆演示当作已验证销售理由。
若提供设置服务，应提前写清标的范围、可用数据、报告频率和异常交付方式，展示遇到旧新闻、停牌、缺失数据或接口限流时的实际报告样式。若销售持续订阅，买方还要知道数据许可证由谁提供、谁审核结论及谁维护新闻源。第一批信任更可能来自可复查的样张、清楚的输入范围和维护责任，原案例没有证明一个可复制的分发渠道。本研究没有联系潜在客户；这些步骤是待验证的经营选择，不是已完成销售过程。

依据：S3a6a528996dc, S1cd92766e9ea, Sb75449d97aab

## 记忆层与可积累资产

把行情和新闻拼到提示词，再保存前次结论，技术门槛正被原生记忆、数据接口和组合软件降低。单段CFA风格提示词容易复制，不能解释客户为何长期付费或迁移困难。记忆如果只是反复引用旧观点，还可能强化先入结论；有记忆与分析正确不是同一个指标。作者所说的质量改善值得验证，但目前没有对照样例支持稳定优势。
可能形成长期积累的是经过核验的标的映射、数据口径规则、历史输入与观点版本、错误纠正记录，以及用户同意保留的研究偏好。这些需要显示能降低下一次复核成本，不能仅凭日志越来越长就称为壁垒。历史观点应允许追踪修订而保留原稿，原始数据与模型推断分开。如果维护记录后仍经常混淆时区、复权或旧新闻，说明记忆层没有解决关键交付问题。客户愿留下来的原因应是可靠的研究流程和减少返工，而不是某个模型名称或代理数量。

依据：S3a6a528996dc, Sf1c064262dc8, Sb330d233b801, S8ee4e77ee196

## 时间、数据修订与权限

FRED明确指出观察值可修订，默认实时期间通常为今天。因此回看两周前的分析时，今天查询到的宏观历史值可能已经变化，不能直接拿修订后的数字判断模型当时是否合理。需要保存当时已知版本或明确使用历史期间，并分别记录观察期、发布日期与取得时间。行情也要区分交易时段、延迟、币种和复权，Alpha Vantage说明会考虑拆股与现金分红，混用口径可能制造虚假的组合变化。
真实持仓、金额和研究偏好属于需要谨慎处理的个人资料，可先使用脱敏比例与允许使用的数据导出。FRED接口要求key，市场与新闻源还可能有各自权限和再分发范围；不能把数据公开浏览等同于可转售全部内容。外部新闻只当信息来源，不允许其文字改变工具权限或执行交易。对外服务需按实际地区与用途确认边界，现有材料不能据“个人财富顾问”名称判断牌照要求。人工复核、失败记录和数据用途核对都应算入交付成本。

依据：S8ee4e77ee196, S0d35d49f9cdb, S1cd92766e9ea, Se6592070cda0

## 使用反馈与效果边界

相关体验：工程负责人描述Claude Code有助于重复任务，但需小步拆解和核对，高上下文自动化也可能增加负担。

依据：S3a6a528996dc, Sb75449d97aab

## 投入判断与验证步骤

商业结论是适合内部效率工具，36/100；独立自用价值为中。对于有明确持仓、数据来源和研究习惯的人，带来源报告与旧观点对照有合理辅助用途，但目前没有证据证明策略或投资回报。最值得先实现的是统一口径、保存输入快照、生成日期化报告和留下人工核对入口；不必先增加更多市场、新闻源或复杂角色。
建议先用10份历史快照和人工答案表检查数字、时间、宏观版本及观点引用，再做两周只读研究准备试验。预设关键数字可追溯、旧观点不覆盖、总人工准备时间下降25%，这些门槛尚未达成。若新报告只是更长、人工核对反而更多，暂停扩展。若确有改善，再验证少量真实客户是否愿为设置或持续维护付款。价格必须覆盖数据用途、维护、复核和异常处理，无法取得所需授权或可信时效时，就缩小输入范围；不能以生成文字的专业风格替代经营与效果证据。

依据：S3a6a528996dc, Sf1c064262dc8, S1cd92766e9ea, S8ee4e77ee196, Sb75449d97aab

## 单位经济测算：情景假设，不是项目已实现的财务结果

| 情景 / 交付单位 | 收入 | 可变成本（含获客） | 单位贡献 | 月交付量 | 月固定成本 | 月经营贡献 |
|---|---:|---:|---:|---:|---:|---:|
| 假设：有限输入的研究报告订阅 / 用户/月，20份准备报告 (USD) | 149.00 | 155.00 | -6.00 | 20 | 200.00 | -320.00 |
| 假设：定制个人研究工具设置服务 / 验收完成的设置项目 (USD) | 1800.00 | 1200.00 | 600.00 | 3 | 600.00 | 1200.00 |

假设：有限输入的研究报告订阅假设：全部为规划假设，无实售。模型与数据预算20美元不代表获得实时行情或新闻转售许可，限定已有获准输入；人工20份×10分钟×30美元/小时=100美元，平台与存储20美元，获客摊销15美元。单位贡献-6美元，20用户减固定200美元后-320美元；每份复核15分钟时人工150美元、单位贡献-56美元，月度-1320美元。；API成本 20，人工成本 100，其他可变成本 20，分摊获客成本 15。依据：S3a6a528996dc, S7c26178a4fa1, S1cd92766e9ea

假设：定制个人研究工具设置服务假设：全部为假设，非作者收费或收入。人工30小时×30美元含数据口径梳理、原型、人工样例核对、文档与培训，模型/API测试预算40美元、环境与存储60美元、获客200美元，单位贡献600美元；每月3单减固定600美元后1200美元。人工40小时则单位贡献300美元、月度300美元；50小时单位贡献0、月度-600美元。持续数据订阅、许可与维护另定，不包含无上限支持。；API成本 40，人工成本 900，其他可变成本 60，分摊获客成本 200。依据：S3a6a528996dc, S7c26178a4fa1, S1cd92766e9ea, S0d35d49f9cdb

## 反证与未核实信息

源站没有投资结果或节时对照；原生组合工具已提供账本与收益统计，Claude Code已有持久记忆。实时数据常需额外权限，宏观修订会影响历史回看，人工复核可能使低价报告订阅亏损。

可核验材料未包含原始代码、完整CFA风格提示词、记忆实现、行情及新闻提供商、数据费用、客户访谈或投资结果。记忆质量改善仍是转述，不能认定为测量结论；所列数据源是可比较的实现选择，不代表作者实际使用。所有经济数字和试验阈值均为假设。

## 具体动作与止损条件

用10份历史数据快照与人工核对表比较报告，检查价格时间、宏观版本、持仓口径及旧观点引用；再做两周只读准备试验，目标为关键数字来源可追溯、历史结论不被覆盖、总人工准备时间下降25%，这些目标尚未验证。

停止投入条件：若数据时效不能确认、旧观点被重写或修订数据被当作当时已知信息，暂停扩展；若复核时间不降或无法取得所需数据用途权限，不投入对外订阅。

## 来源与对应关系

- [S3a6a528996dc] [Generate investment analysis from live market data with Claude Code | Agent Use Cases](https://agentusecases.ai/use-case/generate-investment-analysis-from-live-market-data)：案例站的Claude Code CLI、CFA风格提示、记忆层自述及无投资结果，源站只读试用模板。
- [Sf1c064262dc8] [How Claude remembers your project - Claude Code Docs](https://code.claude.com/docs/en/memory)：CLAUDE.md和自动记忆的职责及持久指令加载方式，不等于投资判断审计账本。
- [S7c26178a4fa1] [Manage costs effectively - Claude Code Docs](https://code.claude.com/docs/en/costs)：API用量与订阅计费口径的区别，以及上下文和模型选择对成本的影响。
- [S8ee4e77ee196] [St. Louis Fed Web Services: FRED® API Real-Time Periods](https://fred.stlouisfed.org/docs/api/fred/realtime_period.html)：FRED实时期间表示何时已知的信息，观察值可修订，默认期间为今天。
- [S0d35d49f9cdb] [St. Louis Fed Web Services: API Key](https://fred.stlouisfed.org/docs/api/api_key.html)：FRED API请求需要key及各应用用户应使用自己的key，涉及接入准备。
- [S1cd92766e9ea] [Customer Support | Alpha Vantage](https://www.alphavantage.co/support/)：Alpha Vantage免费日请求限制、实时与延迟美国行情的高级访问，以及复权处理。
- [Sb330d233b801] [Portfolio Performance](https://www.portfolio-performance.info/en/)：原生开源组合工具的交易记录、收益率计算、历史价格与导出能力，作为具体替代。
- [Se6592070cda0] [Artificial Intelligence (AI) and Investment Fraud | FINRA.org](https://www.finra.org/investors/insights/artificial-intelligence-and-investment-fraud)：AI投资信息可能不完整、错误或过期，支持人工核对与输出边界。
- [Sb75449d97aab] [What is Claude Code actually good for: A road test | Loomery](https://www.loomery.com/insights/what-is-claude-code-actually-good-for-an-actual-road-test)：工程负责人九个月使用Claude Code的自述，涉及任务拆解、源头核查及复杂自动化成本；不是本投资流程评价。

结构化记录：[research/generate-investment-analysis-from-live-market-data.json](../research/generate-investment-analysis-from-live-market-data.json)
