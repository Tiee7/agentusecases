# 用 n8n 预约看房并同步客户跟进状态

## 中文

    预约实地看房并跟进房地产线索
    发帖者搭建了一个基于n8n的销售助手，可以预约看房、发送邮件、跟进线索并更新CRM。
    使用的是
    n8n
    他们做了什么
    发帖者用n8n结合OpenAI、Airtable、WhatsApp、Gmail和Google Calendar搭建助手。新线索存入Airtable，智能体跟踪是否已发送欢迎消息、看房状态和跟进日期等字段，回答房产问题、推荐房源、从Airtable获取房产图片、检查日历冲突后预约看房、发送HTML确认邮件并更新CRM；另一个每日工作流只向当天到期且已拒绝看房的线索发送WhatsApp跟进。
    进展与成效
    他们说，现在它能处理房地产销售流程中的很大一部分，并避免重复欢迎和跟进。主要问题是WhatsApp状态事件造成的webhook循环，以及如何让智能体可靠地调用Gmail、Calendar、Airtable和房源搜索工具并输出结构化结果。
    值得注意
    最大的难点是可靠性调试：过滤WhatsApp状态回调、使工具输出符合解析器要求，都花了不少工作，才使流程可靠起来。
    亲自尝试
    使用n8n
    复制提示词
    为我的[房地产业务]构建一个n8n工作流：从[表单/来源]收到新线索时触发，向他们发送邮件，提供[日历]中的看房时间，在收到回复后完成预约。如果他们在[X天]内没有回复，就发送跟进，并在每个步骤更新[CRM]中的线索状态。在向任何真实线索发送消息前，先展示每种邮件模板的样例供我批准；当一条测试线索完整走完流程后就停止。
    原始来源：https://www.reddit.com/r/aiagents/comments/1uhus5x/i_built_an_ai_real_estate_sales_assistant_that

<details>
<summary>English original</summary>

Book site visits and follow up with real-estate leads
    The poster built an n8n-based sales assistant that books site visits, sends emails, follows up with leads and updates the CRM.
    Done with
    N8
    n8n
    What they did
    The poster built the assistant in n8n with OpenAI, Airtable, WhatsApp, Gmail, and Google Calendar. New leads are stored in Airtable, the agent tracks fields like welcome sent, visit status, and follow-up date, answers property questions, recommends listings, pulls property images from Airtable, books site visits with calendar conflict checks, sends HTML confirmation emails, and updates the CRM; a separate daily workflow sends WhatsApp follow-ups only to declined leads due that day.
    How it went
    They say it now handles a significant part of the real-estate sales pipeline and avoids duplicate welcomes and follow-ups. The main issues were WhatsApp webhook loops from status events and getting the agent to reliably use Gmail, Calendar, Airtable, and the property-search tool with structured outputs.
    Worth knowing
    The biggest catch was debugging reliability: filtering WhatsApp status webhooks and making tool outputs match the parser took substantial work before the flow became dependable.
    Try it yourself
    with
    n8n
    Copy prompt
    Build an n8n workflow for my [real estate business] that triggers when a new lead arrives from [form/source], emails them to offer site visit times from [calendar], and books the visit once they reply. If they don't reply in [X days], send a follow-up, and update the lead's status in [CRM] at every step. Show me a sample of each email template for approval before any message goes to a real lead, and stop once a test lead runs through end to end.
    Original source: https://www.reddit.com/r/aiagents/comments/1uhus5x/i_built_an_ai_real_estate_sales_assistant_that

</details>

## 原作者的方法与来源

来源：[AI real estate assistant: three n8n workflows](https://www.reddit.com/r/aiagents/comments/1uhus5x/i_built_an_ai_real_estate_sales_assistant_that/)

作者方法摘要

1. 创建者将新线索及欢迎、看房、跟进状态保存在Airtable。
   English summary: The creator stores new leads and welcome, visit and follow-up states in Airtable.

2. 对话工作流使用房源查询、WhatsApp、Calendar和Gmail推荐房源及预约看房。
   English summary: A conversational workflow uses property lookup, WhatsApp, Calendar and Gmail to recommend properties and book visits.

3. 每日工作流跟进当天到期的拒绝看房线索；创建者自述修复了状态回调循环和输出解析。
   English summary: A daily workflow follows up declined visits due that day; the creator reports fixing status webhook loops and output parsing.

## 我们的分析

**商业结论：仅建议受控试点。先验证线索状态和预约可靠性，再考虑持续收费**

本案描述了具体的房源咨询、日历预约和跟进链路，适合有稳定咨询量的小团队做有限验证。现有CRM已经覆盖部分需求，真正差异可能来自渠道接入和状态恢复。作者声称避免重复，但布尔标记与忙闲查询本身不足以证明并发安全；两天后跟进还需区分暂缓看房与拒绝联系。没有客户收入和独立效果，先用合成线索检查去重、退出、冲突和未知回执，再决定是否值得客户试点。

案例ID：`book-site-visits-and-follow-up-with-real-estate-leads` · 案例来源：https://agentusecases.ai/use-case/book-site-visits-and-follow-up-with-real-estate-leads
研究时间：2026-10-19T20:29:40Z

**商业评分：42.0/100。用户反馈信号占5%。**

| 维度 | 权重 | 分数 /5 | 商业依据 |
|---|---:|---:|---|
| 付费需求 | 20% | 3 | 预约跟进任务具体且现有CRM有付费定价，但本案付款客户和地区需求未验证。 [Sauthor, Salt] |
| 业务价值与效果证据 | 20% | 2 | 作者只有实现与调试自述，缺少可独立核对的到场提升、净节时或持续错误率。 [Sauthor] |
| 单位经济与利润 | 20% | 2 | 模型和渠道只是部分成本，压力情景中人工支持足以使门店月服务贡献转负。 [Sprice, Salt] |
| 获客与市场进入 | 15% | 2 | 社区展示能让开发者了解流程，尚无门店采购与复购路径的实际证据支持。 [Sauthor] |
| 竞争壁垒 | 10% | 2 | 状态恢复和测试经验可能复用，但多工具接入容易被模板和现有CRM覆盖。 [Sparse, Salt] |
| 交付与经营风险 | 10% | 2 | 同意退出、预约并发和未知回执需要确定性控制，现描述不足以证明生产安全。 [Spolicy, Scalendar] |
| 独立用户反馈信号 | 5% | 0 | 只取得作者和相邻工作流的技术反馈，未取得该系统独立客户业务成果验证。 [Sloop, Sissue] |

## 自用价值：中

对已有房源表和日历的销售人员可能减少整理，但仍需稳定状态和人工接手，未测净省时。

依据：Sauthor, Spolicy, Scalendar

- 适用人群：懂本门店流程并能维护数据的小型销售团队。
- 用途：整理咨询、起草预约回复、同步状态和提醒人工。
- 预期收益：可能降低漏跟进和重复复制；尚无实际节时或成交数据。
- 设置成本：房源ID、时区、字段、同意状态、测试日历与授权分工。
- 维护成本：更新房源、模板审核、权限和接口变化、异常消息核验。
- 使用频率：随授权咨询触发，定期检查到期项，不为增加消息量而触达。
- 隐私风险：联系方式和购房需求在多服务流转，先用合成数据并明确保留期限。
- 错误风险：重复发送、错约、过期房源、退出后跟进、回写失败或日期误判。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/book-site-visits-and-follow-up-with-real-estate-leads

建议工具：n8n

    Build an n8n workflow for my [real estate business] that triggers when a new lead arrives from [form/source], emails them to offer site visit times from [calendar], and books the visit once they reply. If they don't reply in [X days], send a follow-up, and update the lead's status in [CRM] at every step. Show me a sample of each email template for approval before any message goes to a real lead, and stop once a test lead runs through end to end.

自编试用模板

准备条件：虚构线索与房源表、模拟日历、同意和退出字段；无真实接收者或凭据。

工具：n8n流程设计或本地状态模拟；真实集成需另行账户授权。

预期结果：输出状态表、邮件草稿、冲突和停止原因；不宣称已真实预约或发送。

### 源站Copy prompt

原文模板

出处：https://agentusecases.ai/use-case/book-site-visits-and-follow-up-with-real-estate-leads

依据：Sdirectory

    Build an n8n workflow for my [real estate business] that triggers when a new lead arrives from [form/source], emails them to offer site visit times from [calendar], and books the visit once they reply. If they don't reply in [X days], send a follow-up, and update the lead's status in [CRM] at every step. Show me a sample of each email template for approval before any message goes to a real lead, and stop once a test lead runs through end to end.

### 先验收状态再接账户

自编模板

出处：研究团队自编

依据：Spolicy, Scalendar

    使用虚构房源、线索与日历设计预约助手。区分未回复、拒绝本次看房、明确退出、已预约和人工接手。只输出消息草稿与计划，不连接账户、不发送。测试重复webhook、状态回调、日历冲突、时区、发送结果未知、回写失败和过期跟进。每次输出事件ID、前后状态、允许动作及停止原因；同意缺失或未知回执转人工，不能直接重发。

## 已核验事实

- 作者自述用n8n、OpenAI、Airtable、WhatsApp、Gmail和Google Calendar串联流程。 [Sauthor]
- 作者每日跟进条件为拒绝看房、未跟进且日期到期；目录模板则写未回复。 [Sauthor, Sdirectory]
- 作者报告状态回调循环和工具结构化输出问题，未公开端到端工作流。 [Sauthor]
- 官方WhatsApp政策本次页面更新为2026-09-23，要求同意并尊重退出。 [Spolicy]
- 服务窗口外发送需要批准模板，自动响应要有明确人工升级途径。 [Spolicy]
- n8n文档提示agent直接结构化解析可能不可靠，建议另设解析链。 [Sparse]
- Calendar freebusy返回忙闲信息和错误，不执行预约创建。 [Scalendar]
- 实际月付页面Grow为69美元/人/月，Calling另39美元，年付是不同价。 [Salt]
- n8n Starter列年付等效20欧元/月与2500工作流执行，不是无限免费运行。 [Sprice]
- GitHub12262为历史1.69.2循环事件问题，因陈旧关闭，未在现版本复现。 [Sissue]

## 谁使用、谁承担漏跟进成本

本案的使用者是接收房产咨询、解释房源并安排带看的销售人员；潜在付款者是房产中介店主或销售负责人。这是根据工作流作出的客户假设，原帖没有公开合同、付款客户或到店转化表。真正可购买的交付是线索状态清楚、预约不冲突、需要人工处理时有人接手，而不是一个能够持续聊天的窗口。接到多少咨询、实际完成多少次看房、成交多少套，是三个不同指标，不能从作者说处理了很多流程推算佣金。
适合优先验证已有稳定咨询量、房源数据可维护、销售有共同日历的小团队。个人经纪人如果每天只有少量询问，现有CRM提醒和预约链接可能更省事。客户需要先给出漏跟进样本和人工处理基线，才能判断自动化的价值；没有数据的团队还要承担整理房源和统一状态的成本。购房预算和联系方式应按最小范围处理，不把聊天记录收集得越多理解为产品越有效。

依据：Sauthor, Salt

## 原作者实现与建议加强部分

作者说明三个工作流：新线索入库及欢迎、对话中调用工具处理房源和预约、每日扫描到期跟进。欢迎标记、看房状态和跟进日期有助于避免重复，但这些布尔字段不自动提供并发安全。例如消息已成功发送而CRM写回失败，下一次运行仍可能再发；忙闲检查成功到写入预约之间，也可能被另一个销售抢占时段。这些是对实现描述的工程推断，不是已经在作者系统复现的故障。
拟议交付应把事件去重、预约占用和发送回执作为确定性状态流，模型只负责理解问题与生成草稿。房源要用稳定ID检索，名称匹配成功仍需核价格、图片及更新时间。结构化解析通过只证明字段形状符合要求，不证明推荐内容真实；工具结果和最终回复也应分开检查。原帖没有提供可运行工作流文件，本轮没有导入n8n或连接真实账户，不能把阅读描述称为端到端验收。 还应把消息正文视为不可信输入：客户聊天中的指令不能改变工具权限、读取其他客户记录或跳过人工审批。输出邮件中的房源字段应转义，拒绝将任意模型文本直接当成HTML或数据库操作。

依据：Sauthor, Sparse, Scalendar

## 高频任务与有限市场

看房预约和线索跟进通常会重复发生，但本案没有提供覆盖地区、线索量、销售团队规模或实际完成率，不能计算市场规模。可进入的范围应从单门店、单渠道、一个共享日历和有限房源开始。公开案例以WhatsApp为核心；如果目标团队主要通过其他聊天平台，渠道接入、授权和客户行为都要重新验证，不能直接复制后承诺同样效果。
需求并不等于每条线索都应自动追问。当前WhatsApp规则要求同意及退出处理，超出服务窗口的主动消息还涉及批准模板。作者把拒绝看房的线索设为两天后跟进，产品必须区分拒绝某次时间、暂缓购买、明确拒绝联系三种状态。最后一种应终止自动触达。增加自动消息量可能同时增加投诉和执行次数，业务指标应看有效到场和人工负担，不能只看回复速度。机会集中在状态可靠性和销售协作，而非批量骚扰。

依据：Sauthor, Spolicy, Sprice

## 现有CRM给出的替代成本

已实际打开Follow Up Boss价格页并切换月付：Grow列69美元每用户每月，Calling另加39美元；年付页面显示的58美元是不同付款方式，不能当月付价。其公开功能包含跟进计划、日历和邮件同步，因此整理线索与提醒并不必然需要定制智能体。页面未证明它与本案WhatsApp自主房源对话完全等效，比较时应按客户真正需要的渠道和流程逐项核对。
客户已经使用成熟CRM时，增加一个独立Airtable状态库可能造成双份数据和维护负担。更可行的服务假设是补现有系统的一个缺口，例如把已授权咨询归档并起草预约选项，而不是要求客户更换整套系统。报价时还需区分软件订阅、实施费和日常支持费。免费模板或源站Copy prompt能降低入门成本，却没有交付时区、并发、失败恢复和现场培训；这些若不能被客户感知，也难成为持续收费理由。

依据：Salt, Sdirectory

## 以门店月服务为单位的假设

本案没有收入和账单，下面全部为经营假设而非作者数据。基础情景每门店月费300美元，模型预算10、渠道和存储等变量30、人工两小时乘30为60、获客摊销40；每月5个门店，服务者固定费用150，计算结果650美元。实施另计但本模型未计入收入，固定150仅是假设管理预算，不暗示某个n8n官方套餐美元价格。客户现有CRM费用若由客户承担，须单独展示其总拥有成本。
压力情景月费仍300，模型25、渠道等50、人工八小时乘30为240、获客60；3家门店、固定150，结果负375美元。最容易吞掉贡献的是错约后的协调、房源更新和客户支持，而不只是模型调用。n8n官方目前Starter列年付等效20欧元及2500执行；本篇不将欧元与美元直接相加，也不把一个聊天客户算一次执行。实际采购应按消息回合、回调和重试估量，并去除套餐已包含费用的重复计入。税、退款和额外法律审查未计，不称净利润。

依据：Sprice, Salt

## 先证明一个可核对的交付

最初销售路径是假设性的熟人门店或已有CRM实施关系，而不是根据帖子热度推算获客。可以展示虚构线索从新建、草稿、确认、预约、退出的完整记录，请负责人指出哪些环节确实省去了人工。真实试点需要另有授权和已同意的接收者；本次研究没有发送咨询、联系作者、注册服务或替用户启动经营。演示中必须保留失败和人工接手，不把成功片段剪成系统永不出错的印象。
采购验证应核定谁维护房源、谁接异常、哪一个日历是准绳，以及无人值守时承诺的响应范围。报价不能只包含搭建当天而忽略后续API变更、模板审核、人员离职和账号交接。若客户愿意看演示但不愿给出匿名业务样本、验收指标或合理的支持预算，不能把兴趣当成订单。按月收费的前提是持续维护价值，而不是同一条欢迎消息重复计算收益。

依据：Sauthor, Salt

## 可积累的可靠性与交接经验

接入六种工具并不是难以复制的优势。更有机会积累的是房源字段规范、销售状态转换、重复事件处理、预约竞争检查以及故障后如何恢复的测试集合。它们能减少下一家门店的交付返工，但仍需证明可复用比例。客户渠道、表结构和人员分工不同，过度定制会使每家都成为单独项目，订阅收入也可能只是持续出售工时。
作者重点调试状态回调和解析器，说明工具能调用不等于服务能稳定交付。官方解析文档提醒最终输出与中间工具结果有区别，社区也讨论消息状态循环；这些资料适合转成验收场景。状态字段应有版本和事件ID，操作失败要留下可解释原因。真正可用的优势可以用人工接管率、重复触达数、错误预约数和修复时间比较，不用模型数量、流程节点数量或网页漂亮程度代替。上游平台改价和授权范围变化仍会削弱这种优势。

依据：Sparse, Sloop, Scalendar

## 同意、预约和恢复的明确边界

交付首先核实客户已同意对应渠道联系，并保存退出状态；电话在表里不等于允许未来营销。两天后跟进要检查最近用户消息时间、适用模板和发送权限。明确拒绝联系、已经预约、已取消或转人工的记录，不应被每日任务再次唤醒。跟进日期仅等于今天的扫描，还可能在停机后漏掉过期任务；建议按已到期且仍符合状态条件处理，并设置次数上限。这是建议设计，未声称作者已采用。
预约前要核时区、销售人员和房源可用时间；忙闲接口返回错误不能当空闲。确认发送超时先查已有回执，不能盲目重发。对不确定地址、过期价格或非标准请求转人工，不把模型推测变成房源承诺。真实客户资料涉及多服务传递，须有明确用途、最小字段和保留期限。用于住房机会的敏感属性筛选不在本方案范围；本轮只讨论咨询整理与预约，不替人作资格或交易决定。

依据：Spolicy, Scalendar, Sauthor

## 独立反馈有何证据范围

相关体验：应测试状态事件不会再次生成消息。

相关体验：重复事件与时区应纳入验收，但不是现版本缺陷判定。

依据：Sloop, Sissue, Sauthor

## 受控试点的验收和止损

结论为仅建议受控试点。它有清楚的业务流程与可核的官方工具边界，适合验证房产团队是否需要更可靠的线索状态和预约协作。原帖主要是实现自述，没有可运行交付包或客户经营结果，因此完成商业分析不等于已验证产品。应先比较现有CRM能否满足，只有确有渠道或状态缺口时再做小范围定制。源站试用模板和作者方法分别保留，避免把模板中的未回复追问替换成作者已实现的能力。
下一步用合成线索测试状态回调、重复欢迎、同一时段并发、发送成功但回写失败、明确退出、过期任务和时区错误。要求重复事件不增加发送、未知结果待核、不合条件停止、预约冲突转人工。另获授权的试点再记录实际人工分钟数与有效到场，不能预填成功率。若现成工具足够、支持成本持续超售价、退出仍被触达或错约无法可靠恢复，就停止扩大；可以保留为内部草稿与提醒工具。

依据：Sauthor, Salt, Spolicy

## 单位经济测算：情景假设，不是项目已实现的财务结果

| 情景 / 交付单位 | 收入 | 可变成本（含获客） | 单位贡献 | 月交付量 | 月固定成本 | 月经营贡献 |
|---|---:|---:|---:|---:|---:|---:|
| 基础假设：有限门店月维护 / 一家门店一个月的预约辅助维护 (USD) | 300.00 | 140.00 | 160.00 | 5 | 150.00 | 650.00 |
| 压力假设：频繁异常与支持 / 一家门店一个月的预约辅助维护 (USD) | 300.00 | 375.00 | -75.00 | 3 | 150.00 | -375.00 |

基础假设：有限门店月维护假设：全是假设：2小时×30人工；模型10、渠道存储30、获客40、固定150；5×(300-10-60-30-40)-150=650。客户现有CRM另计；不把欧元官方价当美元，不含实施收入和税。；API成本 10，人工成本 60，其他可变成本 30，分摊获客成本 40。依据：Sprice, Salt

压力假设：频繁异常与支持假设：全是假设：8小时×30人工，其余渠道/模型/获客预算提高；3×(300-25-240-50-60)-150=-375；非作者账单或真实利润。；API成本 25，人工成本 240，其他可变成本 50，分摊获客成本 60。依据：Sprice, Salt

## 反证与未核实信息

CRM已有跟进和同步功能；作者布尔状态不证明原子去重；拒绝看房不能等同允许未来联系；无客户业务效果。

未取得工作流源码、未安装或运行上游、未接真实账户和发送消息；无收入与净节时。Airtable文档两次失败不再读取，n8n旧许可页404未据此作授权结论。

## 具体动作与止损条件

合成七类异常测试；授权试点后记录人工复核分钟、重复触达和有效到场，不预设成功率。

停止投入条件：退出仍触达、预约冲突无法恢复、持续人工成本超过售价，或现有CRM已满足。

## 来源与对应关系

- [Sdirectory] [许可目录案例与试用模板](https://agentusecases.ai/use-case/book-site-visits-and-follow-up-with-real-estate-leads)：作者拒绝看房跟进与模板未回复跟进不同。 此来源只支持列明内容，不代表独立实测或经营成果。
- [Sauthor] [创建者的三工作流说明](https://www.reddit.com/r/aiagents/comments/1uhus5x/i_built_an_ai_real_estate_sales_assistant_that/)：作者自述接入、状态字段、工具调用与调试；未公开付费客户和净节时。
- [Spolicy] [WhatsApp现行消息政策](https://whatsappbusiness.com/policy/)：2026-09-23更新：同意、退出、24小时窗口、模板和人工升级路径。
- [Sparse] [n8n结构化输出常见问题](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/common-issues)：官方提示agent直接结构化解析可能不可靠，建议独立链；最终输出与中间工具结果不同。
- [Scalendar] [Calendar忙闲查询接口](https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query)：查询忙闲区间与时区、错误返回，不是预约锁定操作。 此来源只支持列明内容，不代表独立实测或经营成果。
- [Salt] [Follow Up Boss现行月付选项](https://www.followupboss.com/pricing)：实际点击月付Grow69美元/人/月，Calling另39；含跟进和日历邮件同步，非相同WhatsApp自动销售承诺。
- [Sprice] [n8n工作流执行计费](https://n8n.io/pricing/)：Starter年付等效20欧元/月2500执行；不能与美元直接相加，聊天回合和回调影响执行量。
- [Sloop] [社区对WhatsApp回调循环的诊断](https://community.n8n.io/t/whatsapp-issue/292129/13)：第三方建议区分messages和statuses；技术回应非本案客户验证。
- [Sissue] [历史循环日历时间问题](https://github.com/n8n-io/n8n/issues/12262)：2024-12-17用户报告1.69.2问题，2025-06-18因陈旧关闭；不证明现版本仍坏。

结构化记录：[research/book-site-visits-and-follow-up-with-real-estate-leads.json](../research/book-site-visits-and-follow-up-with-real-estate-leads.json)
