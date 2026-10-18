# 用 AI agent 将 Telegram 消息转为 Todoist 待办事项

## 中文

    通过 Telegram 向 Todoist 添加待办事项
    一个结合了 LLM 和编排平台（n8n 或 windmill）的 Telegram 机器人，会根据自然语言消息向作者的 Todoist 账户添加待办事项。
    实际使用
    n8n
    他们做了什么
    这位评论者使用 n8n 或 windmill.dev 这样的编排平台，并将其连接到一个 Telegram 机器人。LLM 负责自然语言交互，因此，发给机器人的消息会被转换成待办事项，并添加到他们的 Todoist 账户中。他们将其描述为一种比 OpenClaw 更可控的替代方案。
    结果如何
    这位评论者说，他们自己就在这样做，而且它能满足人在别处时向家庭待办清单添加事项的需求。这条评论没有给出数字、设置步骤或限制。
    需要知道的事
    这条评论很简短，没有提供工作流细节，因此你需要自行在 n8n 或 windmill 中设计 Telegram 触发器、LLM 步骤和 Todoist 动作。
    自己试试
    推荐工具
    n8n
    复制提示词
    构建一个工作流：当我向 Telegram 机器人发送类似“提醒我在[日期]之前完成[任务]”的消息时，它会向我的 Todoist 添加一项任务，并填写正确的标题和到期日期。使用一个 LLM 步骤来解析消息。完成的标准是：一条测试消息能在我的[Todoist 项目]中创建正确的任务，而且机器人会回复，确认它添加了什么。
    原始来源：https://news.ycombinator.com/item?id=47728484

<details>
<summary>英文原文</summary>

    Add todo items to Todoist from Telegram
    A Telegram bot with an LLM and an orchestration platform (n8n or windmill) adds todos to the author's Todoist account from natural language messages.
    Done with
    N8
    n8n
    What they did
    The commenter uses an orchestration platform, either n8n or windmill.dev, connected to a Telegram bot. An LLM handles the natural language side, so a message sent to the bot gets turned into a todo item and added to their Todoist account. They describe it as a more controlled alternative to OpenClaw.
    How it went
    The commenter says they do this themselves and that it covers the use case of adding home todos from elsewhere. The comment gives no numbers, setup steps, or limitations.
    Worth knowing
    The comment is brief and gives no workflow details, so expect to design the Telegram trigger, LLM step, and Todoist action yourself in n8n or windmill.
    Try it yourself
    with
    n8n
    Copy prompt
    Build a workflow where I message a Telegram bot like 'remind me to [task] by [day]' and it adds a task to my Todoist with the right title and due date. Use an LLM step to parse the message. Finished means a test message creates a correct task in my [Todoist project], and the bot replies to confirm what it added.
    Original source: https://news.ycombinator.com/item?id=47728484

</details>

## 原作者的方法与来源

来源：[lucw在Hacker News说明Telegram到Todoist用途](https://news.ycombinator.com/item?id=47728484)

作者方法摘要

1. 评论者建议使用n8n或windmill.dev一类编排平台，并保留Telegram机器人及LLM自然语言交互。
   English summary: The commenter recommends an orchestration platform such as n8n or windmill.dev, retaining a Telegram bot and an LLM for natural-language interaction.

2. 他们自述通过Telegram给自己的Todoist账户加任务；评论没有明确具体平台、配置或测量结果。
   English summary: They report adding tasks to their own Todoist account from Telegram; the comment does not identify their exact platform, configuration or measured results.

## 我们的分析

**商业结论：适合内部效率工具。先对比原生快速添加，验证聊天入口是否值得维护**

作者自述使用Telegram给Todoist加任务，说明一个具体便利需求，但没有工作流、量化效果、费用或付费证据。Todoist原生快速添加已支持自然语言日期，另有同类免费模板，功能组合本身难形成独立产品壁垒。设置和维护假设对人工支持敏感，优先在已有环境中做可恢复的内部验证，不将个人实践写成收费服务已经成立。

案例ID：`add-todo-items-to-todoist-from-telegram` · 案例来源：https://agentusecases.ai/use-case/add-todo-items-to-todoist-from-telegram
研究时间：2026-10-18T01:45:22.239106+00:00

**商业评分：23.0/100。用户反馈信号占5%。**

| 维度 | 权重 | 分数 /5 | 商业依据 |
|---|---:|---:|---|
| 付费需求 | 20% | 1 | 直接用户用途明确但无付款或购买验证，双平台习惯不能外推普遍市场。 [S2f112b268169, S47b07402e486] |
| 业务价值与效果证据 | 20% | 2 | 作者自述实际使用，缺少可复现配置、质量和时间对照，模板也不是效果测试。 [S2f112b268169, S13f757531172] |
| 单位经济与利润 | 20% | 1 | 设置假设亏损，月维护仅薄利且对额外支持敏感，没有账单和收费证据。 [S2f112b268169, S9c31625dedcc, S13f757531172] |
| 获客与市场进入 | 15% | 1 | 论坛与模板库只有发现入口，没有转化或客户，低客单仍需设置与交接。 [S2f112b268169, S13f757531172] |
| 竞争壁垒 | 10% | 0 | 原生快速添加与公开模板可替代主要功能，未见独家数据、接口或分发。 [S47b07402e486, Sd25b82e3a035, S13f757531172] |
| 交付与经营风险 | 10% | 2 | 可限制固定任务动作，但原例配置与恢复未知，日期、重复投递及账户边界仍需验收。 [Sd25b82e3a035, S47b07402e486, S69b841c7350d] |
| 独立用户反馈信号 | 5% | 0 | 只有原作者自述和另一模板作者的功能说明，没有可归属本实现的独立用户复现；0表示缺证据而非差评。 [S2f112b268169, S13f757531172] |

## 自用价值：中

条件性推断：既用Telegram又用Todoist且已有稳定环境的人可能减少切换，但需要核对日期、项目和恢复，未测得节时收益。

依据：S2f112b268169, S47b07402e486, Sd25b82e3a035, S69b841c7350d

- 适用人群：已有这两个平台和获准自动化连接，能检查任务结果的人。
- 用途：把聊天中的任务整理成Todoist草稿，再受限写入及读回。
- 预期收益：减少切换应用和重复输入的摩擦，收益及频率尚未量化。
- 设置成本：已有获准连接、固定测试项目、时区规则、合成任务和明确动作范围；先与原生Quick Add比较。
- 维护成本：检查解析偏差、重复写入、连接失效与回执缺失，保留可恢复记录。
- 使用频率：按真实跨应用任务输入需要使用，先确认每周频率；不是所有用户都需要。
- 隐私风险：待办和聊天可能经过编排与模型，不跨账户混用，不公开私人内容或凭据。
- 错误风险：相对日期、提醒与到期时间可能混淆，可能错项目、重复任务或错误确认；需要可见草稿和读回。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/add-todo-items-to-todoist-from-telegram

建议工具：n8n

    Build a workflow where I message a Telegram bot like 'remind me to [task] by [day]' and it adds a task to my Todoist with the right title and due date. Use an LLM step to parse the message. Finished means a test message creates a correct task in my [Todoist project], and the bot replies to confirm what it added.

自编试用模板

准备条件：已有获准Telegram/Todoist连接说明、合成项目、用户与项目范围、时区；条件不足只生成方案，不创建凭据。

工具：源站标签与推荐是n8n；原评论只建议n8n或windmill并自述Telegram到Todoist，未明确具体平台、模型和版本。

预期结果：可检查的解析草稿、写入/读回与去重恢复验收计划；自编模板未实测，本轮未发消息或修改账户。

### 比较原生入口与受限聊天入口

自编模板

出处：研究团队自编

依据：S2f112b268169, S47b07402e486, Sd25b82e3a035, S69b841c7350d

    仅根据[现有获准连接说明]和[合成任务清单]，为Telegram消息到Todoist的入口提出受限方案。先对照Todoist原生Quick Add，说明额外流程解决什么摩擦。只处理[用户]的[测试项目]，展示标题、明确日期、时区、项目和原始消息；未知项保留待确认，不把“提醒我”自动当成通知提醒。先输出草稿与字段差异，不发送真实消息、不写真实任务、不创建机器人或凭据。设计在获准后才执行的写入及按任务标识读回检查，另列重复消息、API失败、写入成功但回执失败的恢复步骤，不能直接重跑造成重复任务。排除删除、共享项目修改和任意系统权限。只用现有工具，不调用额外付费API，标明假设及未实测范围。

### Plan a constrained Telegram intake for Todoist

自编模板

出处：研究团队自编

依据：S2f112b268169, S47b07402e486, Sd25b82e3a035, S69b841c7350d

    Using [existing authorized connection documentation] and [synthetic tasks], compare a Telegram intake with Todoist Quick Add. Limit the plan to [allowed user] and [test project]. Show proposed title, explicit date, timezone, project and original message; leave missing fields unresolved and distinguish due dates from notification reminders. Return a draft only: do not send real messages, write real tasks, or create bots or credentials. Describe a later authorized create-and-read-back check, duplicate-message handling, API failures, and recovery after successful creation but failed acknowledgement. Exclude deletion, shared-project changes and arbitrary system permissions. Use existing tools only, make no additional paid API calls, and label untested assumptions.

## 已核验事实

- 已读原始评论的作者为lucw，他自述通过Telegram向自己的Todoist账户加入待办事项。 [S2f112b268169]
- lucw建议使用n8n或windmill.dev一类编排平台并保留LLM交互，没有明确说明自己采用其中哪一个平台。 [S2f112b268169]
- 源站实际使用标签是n8n，正文仍保留n8n或windmill；本报告不把该标签当成原作者具体实现已核实。 [Sd7faa1a4a589, S2f112b268169]
- 原始短评论没有配置、代码、用量、成功率、成本、付费客户或对照测试；更可控是作者判断。 [S2f112b268169]
- 当前n8n官方Todoist节点列出创建、读取、更新、关闭、重开与删除任务的操作；具体授权范围需另外配置。 [Sd25b82e3a035]
- Todoist官方Quick Add支持在任务文字中写自然语言日期及项目标记，也提供桌面全局快捷入口。 [S47b07402e486]
- Todoist官方提醒智能日期识别可能把任务名称中的词误判为日期，用户可以取消识别；不能据此推算本例LLM错误率。 [S47b07402e486]
- 采集时n8n Starter公开显示年付折算20欧元每月、2.5K月工作流执行；不是作者成本，也不是正确任务数量。 [S9c31625dedcc]
- Telegram官方说明长轮询与Webhook不能同时接收更新，未确认更新可能再次返回；任务业务去重不是自动结论。 [S69b841c7350d]
- Onur在n8n模板库发布同类免费模板说明，列出LLM、Todoist与Telegram回执，并要求模型及应用连接；它不是lucw代码或客户验证。 [S13f757531172]

## 现有双平台用户的输入摩擦

结论是适合内部效率工具，商业分数23/100；不建议仅凭这条入口开展独立产品投入。直接使用者lucw已经使用Todoist，并自述从Telegram向自己的账户加入任务。便利来自少切一次应用、把随口描述放入固定清单，不是替用户重新建立任务管理系统。来源没有使用频率、漏记损失、节省工时或付款记录，不能把个人习惯推算成广泛付费需求。

潜在人群是同时稳定使用Telegram和Todoist、确有跨应用输入摩擦的人；这一限定是研究推断。付款人可能是本人，或已经维护自动化工具的小团队，但作者没有描述团队采购、审批预算和商业客户。偶尔录入任务的人可以直接打开Todoist，不能因为消息机器人显得方便，就假定一个新的持续订阅会进入预算。

本例也不同于上一个家庭本地清单案例：目标是已托管的Todoist账户，不是保留一个不与手机同步的自定义API。不能把另一位用户的本地网络、2009年旧系统或QEMU故障移植过来充当本例困难。自用价值为中，前提是已有获准连接、能核对日期与任务结果；本轮没有测得实际收益。

依据：Sd7faa1a4a589, S2f112b268169, S47b07402e486

## 平台名称与作者实际步骤分开

原评论建议n8n或windmill.dev一类编排平台，保留Telegram机器人和LLM自然语言交互，并称自己确实通过Telegram给Todoist加任务。它没有明确指出自己选了哪一个平台。源站的实际使用标签是n8n，归档及忠实译文照样保留；本站分析则不能把标签扩写为已核实的n8n节点、模型或运行版本，故编辑标题使用AI agent这一较宽的表述。

能确认的链路只有消息入口、自然语言处理与Todoist写入的概念组合；提示词、字段映射、账户隔离、触发方式和确认逻辑未知。源站Copy prompt另外提出正确标题、到期日期、目标项目和回复确认，这些是推荐验收目标，并非作者已经展示的工作流。尤其“提醒我”不自动意味着已设置通知提醒，创建带日期的任务和配置提醒应分别核对。

当前n8n文档说明已有Todoist创建和读取动作，可作为设计构件。可检查交付应展示解析草稿、明确缺失日期及用户时区，再在写入后按返回任务标识读取核对。模型说已添加、Telegram消息已送达或工作流显示结束，都不能单独证明任务标题、项目与日期正确。本轮没有操作任何账户或运行原工作流。

依据：Sd7faa1a4a589, S2f112b268169, Sd25b82e3a035, S69b841c7350d

## 需求边界与可见成本参照

这里没有可核验的客户规模、流失率或购买意愿。Telegram和Todoist的总用户数不等于交集需求，更不等于愿意为第三个工具付费的人数。首先应询问既有使用者每周有多少条消息要转任务、是否真的因此漏记，以及原生录入为什么不够用；当前没有这些数据，不构造市场规模数字。

n8n公开页面在本次读取时显示Starter年付折算每月20欧元、2.5K次工作流执行，并说明按完整执行计费。这只能作为托管编排平台的报价参照，不是lucw实际账单；模型、目标应用订阅与人工维护需分别核对。一次消息可能触发一次或多次工作流，重试与拆分会影响用量，不能将2.5K次执行直接叫作2.5K条正确任务，也不将欧元报价直接放入美元利润计算。

对已有自动化环境的人，这条用途可能只增加少量配置；对新用户，则需要持续运行的入口、账户连接及故障维护。两者成本结构不同。合理进入范围是一个明确账户、固定项目与有限输入类型，验证实际使用后再扩展；没有依据承诺泛化到所有家庭、学生或企业团队。

依据：S2f112b268169, S9c31625dedcc, S47b07402e486, S13f757531172

## 先与原生快速添加及现成模板比较

Todoist官方快速添加本身支持自然语言日期及项目标记，还提供桌面全局快捷方式；因此自然语言生成一条任务不全是新能力。比较应让同一位用户完成相同任务，记录找入口、填写、检查和修复的总时间。Telegram入口若只是多加一层转发，反而可能增加模型误解和维护；若消息是用户主要工作入口，才可能减少切换摩擦。

官方帮助也提醒智能日期识别可能把任务名称里的词误当作日期，并允许用户取消识别。这个例子说明即使成熟原生入口也需要可见反馈，不能据此推算LLM解析的错误率。新流程至少要保持同等可检查性，让用户看到明确日期、时区和项目，不能用一条含糊的“完成了”替代原生编辑能力。

n8n模板库另有Onur发布的同类免费模板说明，覆盖文本、语音、LLM、Todoist和Telegram回执。它降低了功能独占性，但模板免费不等于运行、模型和维护免费，也不是lucw本人代码。本文只读说明，没有下载执行模板或配置其要求的密钥；windmill只是原帖提到的另一平台，没有核查其本例配置或报价。

依据：S2f112b268169, S47b07402e486, S13f757531172, S9c31625dedcc

## 人工支持决定小额服务能否成立

没有作者费用、部署工时、任务量或付款证据。以下两种情景全部是USD规划假设，既不是市场报价，也不是已实现收入；n8n的欧元订阅只作独立参照，不作未注明汇率的成本换算。设置服务与持续维护也分别计算，避免用订阅收入掩盖一次性交付亏损。

假设固定账户的149美元接入包，模型测试预算1美元、人工3小时乘40美元为120美元、其他5美元、获客25美元，可变成本151美元，单位贡献-2美元。每月10包、固定支出200美元，月经营贡献-220美元。现成模板只能减少部分连线工作，不能自动消除账户连接、日期例外、交接和售后；人工少算一次就可能扭转表面利润。

假设已有接入后的29美元每客户月维护，模型2美元、人工15分钟乘40美元为10美元、其他3美元、获客摊销5美元，可变20美元，贡献9美元。50客户减月固定300美元，月贡献150美元；若某客户额外需要30分钟支持，其当月贡献变为-11美元。模型、平台与目标应用必须按实际合同归属记录，维护情景不含首次接入，未算税费与退款。这些敏感性支持先验证工时，不能证明可以收费。

依据：S2f112b268169, S9c31625dedcc, S13f757531172

## 第一批验证应围绕已有工作习惯

技术论坛能发现这种需求，模板库也能展示如何连接工具，但浏览量、收藏或平台推荐不等于购买。没有任何证据说明lucw在经营该服务，不能把他的个人回答写成销售渠道、付费转化或创业结果。若尝试验证交付，最合适的对象是假设中已经使用两个平台且有重复录入问题的人，而不是让所有新用户先改变习惯。

可复用交付需要固定输入范围、目标项目、允许账户和维护责任。应说明日期模糊时返回草稿，写入失败怎样告知，用户怎样在Todoist中修复，不把所有语音转录、多任务拆分、跨项目分配都塞进低价服务。Onur模板提供较宽功能说明，但原案例没有声称需要这些能力；功能越多，解析、权限和支持例外也越多。

本轮没有联系任何作者或潜在客户，也没有发消息、报价、创建机器人或连接账户。下一步可以由用户提供已有工具上的合成输入，比较原生入口与候选流程的实际操作负担。只有拿到使用频率、首装工时与一段时间的支持记录，才有依据讨论获客预算和是否形成套餐。

依据：S2f112b268169, S47b07402e486, S13f757531172

## 连接现成功能本身不足以形成壁垒

Telegram入口、LLM整理和Todoist任务动作都是现成构件，公开同类模板进一步降低了组合难度。当前没有独家模型、专有数据、分发渠道或难迁移流程的证据；不能把工具调用链更长、节点更多或有一个聊天界面当成壁垒。对于愿意使用Todoist原生入口的人，增加第三个服务反而需要解释为什么值得维护。

可能积累的是针对特定任务输入的可恢复流程、日期歧义样本、账户隔离规范与真实支持工时，但这些只是未来经营假设。应使用获准的合成或脱敏例子验证，私人待办和聊天不是可以默认公开、跨客户复用或作为训练资产的数据。标准化的是错误处理与交接步骤，而不是收集越多用户生活内容就越有价值。

如果平台继续改善自然语言添加或现成模板维护，简单入口的收费空间会进一步收窄。只有在限定人群中证明整条链路比原生录入更便利、维护更省心，才可能获得持续服务理由。当前无法支持网络效应、规模经济或可持续利润的判断，商业评分中的壁垒维度记0分。

依据：Sd25b82e3a035, S47b07402e486, S13f757531172

## 日期、重复投递与成功回执要分别验收

原评论的“更可控”是作者判断，没有权限配置、故障记录或对照测试，不能当作已经测得的安全性。当前文档支持选择有限动作，但工作流是否只允许某个用户、只能写固定项目，仍由实际配置决定。一个个人待办入口不需要因此获得删除全部任务、修改共享项目或任意系统操作的权限。

Telegram官方说明长轮询与Webhook不能同时收取更新，未确认更新可能再次返回。设计时应将消息接收、解析草稿、任务创建和回执分开，考虑重放、网络中断及创建成功后回执失败。按消息标识记录业务处理状态是本文的工程建议，不能宣称原案例已实现幂等。仅重跑整个工作流可能重复创建任务，恢复时先核实已有结果。

日期还需区别相对日、时区、到期日期与提醒；未说日期的消息不能被模型补成明天。若涉及多用户和共享项目，还要检查归属和账户边界。任何账号连接、日志保留及模型处理范围都需由使用者明确。本轮没有真实Telegram消息、Todoist写入或模型调用，测试只覆盖研究数据、页面与复制功能，不证明业务链路可靠。

依据：S2f112b268169, Sd25b82e3a035, S47b07402e486, S69b841c7350d

## 一位作者的自述不能算独立复现

lucw自述确实用Telegram给自己的Todoist加任务，并推荐编排平台及LLM；未给实现、量化效果或维护成本。

相关体验：Onur提供另一同类模板的功能与设置说明，不是使用lucw实现的独立客户，也不是本轮实际运行结果。

依据：S2f112b268169, S13f757531172

## 先证明入口比原生录入值得维护

适合内部效率工具的结论来自一个明确的个人用途，加上现成构件足以组成可检查的小流程；不支持仅靠它成立新的独立产品。最有利反证是双平台重度用户已具备自动化环境，增加这个入口的边际成本可能很低，而且作者确实说自己在用。这足以支持小范围自用验证，但还不能证明一般用户愿为额外订阅和支持付款。

继续条件是：在合成项目与已有获准工具上，对比同一批任务的原生快速添加与候选聊天流程，确认标题、项目、日期和时区；含糊输入保持草稿，重复消息不重复新增，失败能被发现并恢复。记录设置工时、人工纠错和维护负担，而不是只展示一条成功消息。此处为下一步计划，本轮未运行业务代理，也没有创建凭据或购买API。

若原生入口已解决主要问题、消息流程需要频繁重录、出现跨账户写入，或首装及月支持工时持续超过预算，就应停止扩大范围。若未来拿到可复现工作流、实际用量和获准反馈，再评估收费与评分。当前29美元月费的薄利假设不能用来证明利润，149美元设置包的负贡献也不能靠未验证客户量掩盖。

依据：S2f112b268169, S47b07402e486, S9c31625dedcc, S69b841c7350d, S13f757531172

## 单位经济测算：情景假设，不是项目已实现的财务结果

| 情景 / 交付单位 | 收入 | 可变成本（含获客） | 单位贡献 | 月交付量 | 月固定成本 | 月经营贡献 |
|---|---:|---:|---:|---:|---:|---:|
| 全部假设：固定账户一次性接入 / 一套固定账户及项目的接入交付 (USD) | 149.00 | 151.00 | -2.00 | 10 | 200.00 | -220.00 |
| 全部假设：接入后的有限月度维护 / 客户月，不含首次设置 (USD) | 29.00 | 20.00 | 9.00 | 50 | 300.00 | 150.00 |

全部假设：固定账户一次性接入假设：未实测；人工3小时×40美元，模型测试1美元、其他5、获客25，可变151、贡献-2；10包减固定200，月贡献-220。不是作者支出、公开报价或实际收入；欧元平台报价未换算进来。；API成本 1，人工成本 120，其他可变成本 5，分摊获客成本 25。依据：S2f112b268169, S9c31625dedcc, S13f757531172

全部假设：接入后的有限月度维护假设：未实测；人工15分钟×40美元，模型2、其他3、获客摊销5，可变20、贡献9；50客户减固定300，月贡献150。额外30分钟支持20美元使该客户贡献变为-11；平台/目标应用成本以真实归属另核，不含首次设置、税费和退款。；API成本 2，人工成本 10，其他可变成本 3，分摊获客成本 5。依据：S2f112b268169, S9c31625dedcc, S13f757531172

## 反证与未核实信息

作者确实报告自己在用，已有双平台和自动化环境的用户可能以较低边际成本取得便利；公开模板也降低搭建门槛。但模板不是作者实现、效果复现或客户付费，原生Quick Add对同类输入已有能力。

原评论未明确其编排平台，未取得代码、模型、账户配置、任务量、错误率、成本、独立反馈或客户；未下载运行模板，未发消息、操作Todoist或调用模型。页面/数据测试不是端到端业务验证；Wanted未知，稳定位置38不是热度排序。

## 具体动作与止损条件

用合成任务及已有获准工具，对照Todoist原生入口检查标题、项目、日期、时区、重复消息和失败恢复，并记录首装与维护工时；本轮只给计划，未运行。

停止投入条件：原生入口已足够、聊天流程需反复重录、发生跨账户写入，或实际设置及支持持续超预算时，停止扩大范围。

## 来源与对应关系

- [Sd7faa1a4a589] [源站归档：Telegram 到 Todoist](https://agentusecases.ai/use-case/add-todo-items-to-todoist-from-telegram)：支持归档的完整案例叙述及源站推荐模板；n8n标签与正文n8n或windmill均按原样保留，不能以标签消除原评论的不确定性。
- [S2f112b268169] [Hacker News：lucw 的 Telegram 与 Todoist 自述](https://news.ycombinator.com/item?id=47728484)：支持作者确实自述通过Telegram往自己的Todoist加任务、建议编排平台和LLM，并认为更可控；没有代码、配置、成本或独立复现。
- [Sd25b82e3a035] [n8n 官方：Todoist 节点](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.todoist)：支持现有节点具有创建、读取等任务操作，以及可以供AI工具调用；不证明本案例具体使用n8n、节点版本或任何错误恢复配置。
- [S47b07402e486] [Todoist 官方：Task Quick Add](https://www.todoist.com/help/todoist/features/use-task-quick-add-in-todoist-va4Lhpzz)：支持原生快速添加可识别自然语言日期、指定项目，并有智能日期识别误判提示；是入口替代基线，不证明任意自然语言或语言都能正确解析。
- [S9c31625dedcc] [n8n 官方：定价](https://n8n.io/pricing/)：支持采集时Starter年付折算20欧元/月、2.5K月执行量及按工作流执行计费；不代表作者成本，也不保证模型、Todoist或支持人工包含在内。
- [S69b841c7350d] [Telegram 官方：Bots FAQ](https://core.telegram.org/bots/faq)：支持更新接收、长轮询与Webhook互斥及重复未确认更新的机制；不证明Todoist业务写入恰好一次或确认回复等同于落库成功。
- [S13f757531172] [n8n 模板库：Onur 的 Telegram 到 Todoist 模板](https://n8n.io/workflows/3052-effortless-task-management-create-todoist-tasks-directly-from-telegram-with-ai/)：支持存在公开的同类免费模板说明，列出文本/语音、LLM解析、Todoist创建和Telegram回执；这是另一作者的模板，不是lucw的实际实现或独立客户评价。

结构化记录：[research/add-todo-items-to-todoist-from-telegram.json](../research/add-todo-items-to-todoist-from-telegram.json)
