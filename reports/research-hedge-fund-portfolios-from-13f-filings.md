# 用 Finance 智能体检索13F申报并整理机构持仓变化

## 中文

    从13F申报研究对冲基金投资组合
    一个能访问实时数据的开源金融研究智能体，使用13F申报来分析机构投资组合披露。
    使用的是
    自建或未命名智能体
    他们做了什么
    帖子介绍一个开源金融研究应用，让AI智能体查询实时金融数据，包括SEC申报、内部人交易、财报、股价，以及新加入的13F、13D和13G披露。用户用自然语言询问某基金最大的新增持仓等问题，智能体通过Next.js应用检索和分析数据，使用Vercel AI SDK调用工具、Daytona执行代码、Valyu进行搜索；人的职责是组织问题并复核输出。
    进展与成效
    创建者说，应用接近1,000个GitHub星标，并可通过一个提示词呈现机构投资组合及相关申报。一位评论者提醒，13F数据存在延迟，更适合产生研究线索和历史追踪，而非实时判断投资信念。
    值得注意
    它被介绍为完全免费、开源，也能用本地模型离线运行。
    亲自尝试
    使用Manus
    复制提示词
    使用SEC EDGAR数据，研究[对冲基金或机构投资者名称]最新的13F申报。按市值总结前十大持仓、最大的新增持仓、相较上一季度增持、减持或退出的持仓，以及行业集中度。最后提供一页摘要表和三项最值得注意的变化，并引用所用申报链接。
    原始来源：https://www.reddit.com/r/aiagents/comments/1rvhnqo/ai_for_financial_research_i_gave_my_opensource

<details>
<summary>English original</summary>


    Research hedge fund portfolios from 13F filings
    An open-source financial research agent with live data access works with 13F filings to analyze institutional portfolio disclosures.
    Done with a
    custom-built or unnamed agent
    What they did
    The post describes an open-source financial research app that lets an AI agent query live financial data, including SEC filings, insider transactions, earnings, stock prices, and newly added 13F, 13D, and 13G disclosures. The user asks in plain English for things like a fund’s biggest new positions, and the agent searches and analyzes that data through a Next.js app using the Vercel AI SDK for tool calling, Daytona for code execution, and Valyu search; the human’s role is framing the prompt and reviewing the output.
    How it went
    The creator says the app had close to 1,000 GitHub stars and can surface institutional portfolios and related filings from one prompt. A commenter notes 13F data is delayed, so it is better for idea generation and historical tracking than real-time conviction.
    Worth knowing
    It is presented as 100% free, open-source, and able to run offline with local models.
    Try it yourself
    with
    Manus
    Copy prompt
    Research the latest 13F filing for [hedge fund or institutional investor name] using SEC EDGAR data. Summarize its top 10 holdings by value, the biggest new positions, the positions it increased, reduced or exited since the prior quarter, and its sector concentration. Finish with a one-page summary table and a short list of the three most notable changes, citing the filing links you used.
    Original source: https://www.reddit.com/r/aiagents/comments/1rvhnqo/ai_for_financial_research_i_gave_my_opensource


</details>

## 原作者的方法与来源

来源：[AI for financial research: open-source agent and institutional filings](https://www.reddit.com/r/aiagents/comments/1rvhnqo/ai_for_financial_research_i_gave_my_opensource/)

作者方法摘要

1. 创建者把对话应用接到金融资料检索与代码执行工具。
   English summary: The creator connects a conversational app to financial-data search and code-execution tools.

2. 用户询问机构披露，创建者加入13F、13D和13G检索，输出仍由人复核。
   English summary: Users ask about institutional disclosures; the creator added 13F, 13D and 13G search, while users still review the output.

3. 创建者将项目介绍为免费、开源并支持本地模型；这是创建者的说法。
   English summary: The creator presents the project as free, open-source and usable with local models; this is the creator’s claim.

## 我们的分析

**商业结论：仅建议受控试点。价值在披露整理与证据交付，免费离线和实时完整组合说法需限定**

公开代码和现行接口能够解释交付链路，上游数据服务也有明确收费边界。13F有季度时点和覆盖限制，不能当作所有资产的实时仓位。源码当前研究任务依赖远端服务，与历史README的离线宣传不能混用。已有公开导航和人工表格替代，初始验证应聚焦固定机构的可追溯比较、复核时间和输出文件，而不是复制一个聊天框后承诺收益。缺少客户结果与收入，本篇的完整商业分析不代表产品已通过实盘或经营验证。

案例ID：`research-hedge-fund-portfolios-from-13f-filings` · 案例来源：https://agentusecases.ai/use-case/research-hedge-fund-portfolios-from-13f-filings
研究时间：2026-10-19T19:57:01Z

**商业评分：41.0/100。用户反馈信号占5%。**

| 维度 | 权重 | 分数 /5 | 商业依据 |
|---|---:|---:|---|
| 付费需求 | 20% | 2.5 | 公开披露整理任务明确，但预算归属和付费客户尚未核实。是否替换现有工作仍需客户验证。 [Sauthor, Salt] |
| 业务价值与效果证据 | 20% | 2 | 源码与产品入口可查，独立准确率、净节时和客户结果仍缺证。公开功能不能替代实际交付的核验。 [Scode, Slive] |
| 单位经济与利润 | 20% | 2 | 软件免费不等于数据和人工免费，基础与压力模型对复核工时敏感。 [Sprice, Sbilling] |
| 获客与市场进入 | 15% | 2 | 开发者渠道可见，但星标不等于采购，缺可复制销售证据。需要验证客户复购而非开发者关注。 [Sauthor] |
| 竞争壁垒 | 10% | 2 | 有结构化交付机会，上游依赖强且原始披露与现成导航可替代。独立服务的差异化仍待实证。 [Sindex, Salt] |
| 交付与经营风险 | 10% | 2 | 单位、修订、权限和任务成本需控制，目前仅静态核验与受控试点。 [Ssec, Scode] |
| 独立用户反馈信号 | 5% | 1 | 有历史直接体验问题但无独立准确率与商业效果，不能据此评整体满意度。 [Sfeedback, Slogin] |

## 自用价值：中

对会核原始披露的研究者有整理价值，仍需检查日期、单位和来源，不代替投资判断。

依据：Ssec, Scode, Sprice

- 适用人群：有金融披露阅读能力的分析师或个人研究者。
- 用途：整理公开季度持仓及变化，并保留申报引用。
- 预期收益：可能减少检索与表格整理；未测净省时或投资收益。
- 设置成本：核机构实体、季度、证券口径、数据许可与版本；先合成数据。
- 维护成本：修订、单位变化、供应商和任务成本、来源失效与人工复核。
- 使用频率：围绕季度申报和特定研究问题，不需为13F持续实时交易轮询。
- 隐私风险：只用公开披露；客户私有研究和账户资料不得擅自上传上游。
- 错误风险：时滞当实时、把市值涨幅当增持、空头缺失、修订重复与单位错。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/research-hedge-fund-portfolios-from-13f-filings

建议工具：Manus

    Research the latest 13F filing for [hedge fund or institutional investor name] using SEC EDGAR data. Summarize its top 10 holdings by value, the biggest new positions, the positions it increased, reduced or exited since the prior quarter, and its sector concentration. Finish with a one-page summary table and a short list of the three most notable changes, citing the filing links you used.

自编试用模板

准备条件：两季度虚构持仓表与明确的证券标识、类型、金额单位；不含真实账户。

工具：现有助手与本地确定性计算；未使用额外付费模型API或上游研究服务。

预期结果：带季度、股数、金额、变化和来源占位的复核表；缺失/修订待查，不生成交易建议。

### 源站Copy prompt

原文模板

出处：https://agentusecases.ai/use-case/research-hedge-fund-portfolios-from-13f-filings

依据：Sdirectory

    Research the latest 13F filing for [hedge fund or institutional investor name] using SEC EDGAR data. Summarize its top 10 holdings by value, the biggest new positions, the positions it increased, reduced or exited since the prior quarter, and its sector concentration. Finish with a one-page summary table and a short list of the three most notable changes, citing the filing links you used.

### 两季度披露数据核对

自编模板

出处：研究团队自编

依据：Ssec

    比较这两份虚构季度表：[机构ID、报告期、申报日期、证券ID、类型、股数、金额、单位、来源占位]。先验证日期单位与重复项，按证券ID和类型匹配，分别计算股数变化和金额变化；股数不变但金额增加不能称增持。缺上一期、遇修订或单位未知时列待核，不补零。输出前十持仓与变化表，说明覆盖和时滞，不给买卖建议、不连接账户、不执行交易。

## 已核验事实

- 目录推荐Manus，但作者实际项目为Finance，自述Next.js、AI SDK、Valyu、Daytona与本地模型。 [Sdirectory, Sauthor]
- 固定提交3ba50a5的自托管研究代码需要Valyu API key，并发送远端DeepResearch请求。 [Scode]
- MIT覆盖开源代码，不能自动替代上游数据许可。 [Slicense]
- 公开产品界面显示Fast/Standard/Heavy、图表、代码及文件交付；本轮未启动查询。 [Slive]
- 13F具有申报范围，不含空头；并非机构全部实时资产。 [Ssec]
- SEC列2026第三季度截止2026-11-16，本轮10-19不能假定全部第三季披露齐备。 [Ssec]
- 当前Valyu SEC资料列在89美元月层，免费额度有限；DeepResearch列每任务0.10至15美元范围。 [Sprice]
- Daytona资源按生命周期计费，停止后的磁盘仍可能收费。 [Sbilling]
- 外部GitHub用户历史上询问在线演示和源码差异，尚无当前复现结论。 [Sfeedback]
- DATAROMA已有机构组合更新与活动导航，可作窄范围比较替代。 [Salt]

## 使用者与预算归属

本案首先解决资料整理问题：研究人员想知道某机构披露了哪些持仓、和上一季度相比有哪些变化，并把结果带进自己的研究笔记。可能的使用者包括个人研究者、分析师和小型研究团队，可能付款的是研究负责人或工具预算管理者。原帖没有公开付费客户、合同和净节时，所以这些画像是待验证的进入方向，不能从接近一千星标推算机构采购或订阅收入。
付费动机应落到可核对的表格和证据，而不是“跟着大基金赚钱”。若用户只关注一两家机构，公开聚合页或手查申报可能已经足够；如果需要固定格式、多个季度、机构名称归一和异常解释，辅助工具才可能节省重复劳动。采购前应明确交付是历史披露汇总，不是投资建议、实时仓位或交易执行。资料正确但交付格式不能进入客户现有工作表，也可能没有实际购买价值。

依据：Sauthor, Salt

## 历史描述与当前实现

原帖描述Next.js前端、Vercel AI SDK工具调用、Valyu检索、Daytona代码执行和本地模型。当前固定提交3ba50a5的研究流程已有变化：报告接口调用远端DeepResearch任务，自托管路径同样要求Valyu API key。公开界面能看到研究深度、图表、代码与文件交付选项，本轮只读取界面，没有启动收费任务。这些证据不能支持把全部当前研究流程说成断网可运行。
拟议的可靠交付应先确定机构实体、报告季度和比较季度，取完整申报及修订信息，按证券标识和类型对齐，再计算变化并输出引用。人工要核机构名称是否选错、报告日期与提交日期是否混淆，以及增持是否只是市值变动。模型负责解释和整理，数值运算应由可重复程序完成；未找到上一季就列缺失，不编造新增或退出。报告生成后还要能打开文件、追到原始记录，不能只验一段看似完整的文字。
交付表还应把机构管理人、报告期末、实际提交日和本次取数日分别显示。机构名称相似时以稳定标识复核，证券改名、拆股或类别变更时不能机械匹配成新增和清仓。行业集中度需要另有可追溯分类映射，原始持仓表并不自动包含所需行业标签。遇到无法确认的映射应展示未分类占比，避免只对成功匹配部分算出看似完整的集中度。

依据：Srepo, Scode, Slive

## 时滞限制决定适用场景

13F是有范围、有时点的披露，不覆盖机构全部资产和空头，也不能显示目前仍持有多少。SEC问答列出2026年第三季度的截止日为11月16日；本轮日期是10月19日，不能把所有机构的第三季度文件都当作已经齐全。即使数据商在申报落地后几分钟索引完成，解决的是发布后的检索延迟，仍没有消除季度持仓与披露之间的时间差。
因此更适合历史比较、研究线索与披露资料整理，不适合卖实时跟单信号。把13D、13G与13F放在同一搜索入口有便利性，但它们不是同一种表，不能用一个字段模板和一个截止规则处理。小团队最可进入的范围是固定机构名单和固定季度格式；如果一开始承诺所有市场、所有证券和即时变化，就会把数据授权、覆盖核验与责任成本放大。是否有足够市场，还需要真实客户工作样本与付费验证。

依据：Ssec, Sindex

## 原始披露与现成导航

原始SEC文件、公开机构持仓导航和现有分析工作表是实际替代。DATAROMA已提供机构组合更新、活动和分类入口，适合先找到所关心机构；它的覆盖范围与使用许可不能自动推成全市场数据库或任意转载授权。客户如果只需要看前十项持仓，购买复杂智能体可能增加维护而非减少工作。
代码MIT许可降低复制界面的门槛，也削弱只靠一个聊天框形成差异的可能。可收费的部分更可能是按客户规范输出、处理修订和标识异常、维护可追溯质量，以及将结果接到已有研究流程。代码许可不等于上游数据的再分发许可；商业产品应分别核软件版权、数据许可和报告分享范围。本轮只做公开资料研究，没有接受新条款、注册数据商或售卖任何报告。不要把开源项目名称和营销口号当作与专业终端完全等效的证据。

依据：Salt, Srepo, Slicense

## 两种假设交付模型

价格与实际利润分开。当前Valyu公开页列SEC资料在89美元月层，免费额度用完后不能当永久免费；DeepResearch另按任务范围列0.10至15美元，真实用量和适用额度需在采购前核对。拟议服务以一份经过人工核对的固定机构季度比较为单位，基础假设卖75美元，变量API预算2、计算存储1、人工半小时按40美元计20、获客摊销10，每月10份，固定费用120，月结果300美元。固定120含89数据访问预算和31运行预算，不把已包含额度再次作为变量重复收费。
压力情景售价仍75，变量API/超额预算8、计算存储4、人工两小时80、获客15，每月5份，固定150，月结果负310美元。除89公开价外，各输入都是待实测假设，变量API需明确属于模型或超额任务，不代表作者账单。真实计费若采用全包任务模式，要替换整套成本而非叠加重复组件。退款、税和合规审查尚未纳入，不能称净利润。最主要成本通常是对齐错误、返工和客户解释，而非生成文字的几分钱。

依据：Sprice, Sbilling

## 初始销售与证明方式

项目在GitHub和社区公开展示，能带来开发者关注，却没有证据说明这些人会购买研究交付。对新服务者而言，最合理的第一步是向已熟悉其工作方法的研究团队展示一份合成或公开历史资料样例，让对方核每个数字、日期和来源。展示应以减少复制核对工作为目标，不承诺选股收益，也不使用基金名称暗示背书。
获客验证要记录客户实际需要的输出文件、更新频率、人工审阅方式和可接受误差。学生或爱好者可能更在意免费和易安装，机构团队则可能更在意访问控制、可审计记录与数据合同，不能用同一种免费宣传覆盖两类人。历史反馈中出现登录困难和演示源码差异疑问，提示售前试用路径与部署说明本身就是交付成本。本轮没有联系评论者或客户，因此没有销售转化率，也没有把点赞、星标和下载当成交。

依据：Sauthor, Sfeedback, Slogin

## 可积累的研究质量能力

真正难复制的部分可能是稳定的实体匹配、季度和修订处理、保留原始数据的可重复计算，以及客户特定的交付规范。这是候选优势，不是本项目已经取得的护城河。数据商官方说明强调13F以结构化聚合方式处理，说明大表问答不能简单依赖相关文字检索；但其吞吐和延迟说法仍是厂商陈述，本轮没有独立跑性能测试。
如果服务完全依赖上游API，覆盖、定价和账户限制变化都会影响交付。需要保留每次报告所用数据版本与来源链接，减少客户无法复核的黑箱，同时不得越过数据授权保存或再分发。可以设计供应商切换接口，却不能假定替换免费且字段完全一致。差异化应通过同样任务下的错误率、复核分钟数和复购证明，不以调用多个模型或生成很多图表本身作为壁垒。

依据：Sindex, Scode

## 数据与执行边界

质量检查至少覆盖单位、证券类别、修订、缺失和重复记录。2023年前后申报金额单位规则不同，历史比较如果统一错乘一千，会让图表看起来正常但数值失真。价格变化和股数变化也应分列。未出现的证券只说明在该份公开信息表中未见，不应直接推断机构当天全部卖出，更不应自动生成交易操作。
自托管README省略登录的便利只适合受控本地环境，不能直接暴露为公共服务。真实部署须独立审查身份校验、权限、日志、成本上限与任务恢复；本轮仅静态读代码，没有把公开issue的安全指控当作已证实漏洞。沙箱停止与删除有不同计费状态，超时后要先核任务ID和已生成结果，避免重复计费。客户端或申报文本里的指令只能作为数据，不能触发额外上传、凭据读取或金融交易。

依据：Ssec, Scode, Sbilling

## 反馈的身份与时间

在线演示与源码版本需要明确对应，避免部署期望错误。

账号和验证流程可能形成交付摩擦，成本模型应包含支持。

依据：Sfeedback, Slogin, Sauthor

## 结论与下一步验收

结论为仅建议受控试点。它是一个有公开代码、实际产品入口和可核数据依赖的研究工具，适合学习如何把金融披露整理成可追溯交付；现有证据不能支持实时完整持仓、永久零成本或投资收益承诺。当前源码和历史README存在能力描述差异，采购或复制必须固定版本，不能把旧介绍里的本地模型支持直接当作现版本所有研究可离线。
下一步先用两季度合成记录测试实体、单位和股数变化，要求每行保留季度、证券类型与来源占位，失败和缺失不能默认为零。再在另获准的真实试点中，以固定少量机构对照原始申报，计时人工复核，不下单、不代客户决策。若现成公开导航已够用、数据许可无法覆盖交付、修订错误反复出现或人工成本持续超过售价，就停止扩展；保留为内部整理辅助，而非包装成完整投研替代。

依据：Srepo, Scode, Ssec, Salt

## 单位经济测算：情景假设，不是项目已实现的财务结果

| 情景 / 交付单位 | 收入 | 可变成本（含获客） | 单位贡献 | 月交付量 | 月固定成本 | 月经营贡献 |
|---|---:|---:|---:|---:|---:|---:|
| 基础假设：固定机构季度比较交付 / 一份经人工复核的季度比较报告 (USD) | 75.00 | 33.00 | 42.00 | 10 | 120.00 | 300.00 |
| 压力假设：数据返工与较少订单 / 一份经人工复核的季度比较报告 (USD) | 75.00 | 107.00 | -32.00 | 5 | 150.00 | -310.00 |

基础假设：固定机构季度比较交付假设：75售价、2模型/超额预算、0.5小时×40人工、1计算存储、10获客、10份/月均是假设；固定120含89官方数据访问价及31假设运行。不得重复计已含额度。须核实际任务计价与许可，月结果300，不是作者收入。；API成本 2，人工成本 20，其他可变成本 1，分摊获客成本 10。依据：Sprice, Sbilling

压力假设：数据返工与较少订单假设：人工2小时×40；固定含89数据价与61运行预算，其余均压力假设，月结果5×(75-8-80-4-15)-150=-310。未含税、退款和合规审查，不称净利润。；API成本 8，人工成本 80，其他可变成本 4，分摊获客成本 15。依据：Sprice, Sbilling

## 反证与未核实信息

现成公开导航和原始申报可替代窄查询；当前源码远端任务依赖推翻全流程离线零成本理解；13F范围时滞限制实时价值。

未安装运行上游代码、注册、付费查询、接真实账户或交易；无收益/准确率实测。历史用户问题不代表当前未修复；公开安全指控未验证不采为事实。

## 具体动作与止损条件

用两季度合成记录测试证券类型、单位和股数变化，保留来源；真实试点另获授权后核原始申报与复核分钟。

停止投入条件：数据许可不足、修订/单位错误不可控、人工贡献为负，或现成导航已经满足。

## 来源与对应关系

- [Sdirectory] [目录原文与Manus模板](https://agentusecases.ai/use-case/research-hedge-fund-portfolios-from-13f-filings)：保留许可全文；Manus是推荐试用工具，不是作者实际实现。
- [Sauthor] [Finance创建者的13F更新介绍](https://www.reddit.com/r/aiagents/comments/1rvhnqo/ai_for_financial_research_i_gave_my_opensource/)：作者披露Next.js、AI SDK、Daytona、Valyu和本地模型；星标与单提示词能力为自述。
- [Srepo] [Finance公开仓库说明](https://github.com/yorkeccak/finance)：开源README仍列本地模型与外部API依赖，不能推断实时金融数据离线免费。
- [Ssec] [SEC 13F官方问答](https://www.sec.gov/rules-regulations/staff-guidance/division-investment-management-frequently-asked-questions/frequently-asked-questions-about-form-13f)：季度披露范围和时滞、空头缺失、2023起金额单位变化，不能等同完整实时组合。
- [Sprice] [Valyu当前价格与额度](https://www.valyu.ai/pricing)：免费试用额度有限，SEC资料在89美元月层列出；DeepResearch每任务0.10至15美元，额度用完暂停除非另加值。
- [Sbilling] [Daytona资源计费](https://www.daytona.io/docs/billing)：依资源与生命周期付费，停止仍可能计磁盘；不是开源软件免费就所有执行免费。
- [Sindex] [Valyu的13F索引技术说明](https://www.valyu.ai/blogs/how-we-index-sec-filings-in-real-time)：厂商称13F聚合走列式存储与受限只读SQL，非一般向量搜索；性能宣称未独立测试。
- [Salt] [DATAROMA公开机构持仓导航](https://www.dataroma.com/m/home.php)：已有机构组合更新与活动导航，可作窄范围人工研究替代，不代表全市场覆盖或转载许可。
- [Sfeedback] [用户询问演示与源码差异](https://github.com/yorkeccak/finance/issues/18)：2025-12-19外部用户说已体验演示，询问源码为何不同；历史单例，不证明今天仍存在同样问题。
- [Slogin] [产品介绍下的登录反馈](https://www.linkedin.com/posts/prosperotemuyiwa_we-built-an-open-source-bloomberg-you-can-activity-7424132614376136704-KnDg)：产品方介绍下有外部用户登录及验证邮件困难自述；非当前复现或研究准确率证据。
- [Slive] [产品当前公开研究界面](https://finance.valyu.ai/)：实际公开界面显示深度、图表、代码、文件交付和Valyu登录；未运行收费查询。
- [Scode] [固定提交的真实研究任务调用](https://github.com/yorkeccak/finance/blob/3ba50a5c32e045540b874037c490854070c76ff7/src/lib/valyu-workflows.ts)：当前实现自托管仍用Valyu API key发起远端DeepResearch；与README概括的离线能力须分开。
- [Slicense] [MIT代码许可](https://github.com/yorkeccak/finance/blob/3ba50a5c32e045540b874037c490854070c76ff7/LICENSE)：代码可复用需保留版权许可，数据源授权不由代码MIT自动覆盖。

结构化记录：[research/research-hedge-fund-portfolios-from-13f-filings.json](../research/research-hedge-fund-portfolios-from-13f-filings.json)
