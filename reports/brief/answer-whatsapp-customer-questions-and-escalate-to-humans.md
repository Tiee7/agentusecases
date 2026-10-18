# 用 n8n 设计 WhatsApp 知识问答与 Telegram 人工转接

## 中文

    回答 WhatsApp 客户问题并升级转交人工
    一个由 n8n 和 OpenAI 构成的 agent 根据知识库回答 WhatsApp 问题，并将置信度较低的情况连同完整上下文升级转交给 Telegram 上的人工人员。
    实际使用
    n8n
    他们做了什么
    一个 n8n 工作流接收每条传入的 WhatsApp 消息，并汇集会话历史和公司知识库。OpenAI 根据这些内容起草回复，再由置信度检查决定能否可靠回答。有把握的答案会通过 WhatsApp 发回；否则，该事项会连同完整会话一起转交给 Telegram 上的人工团队。
    结果如何
    README 没有给出测量结果，只有设计目标：覆盖日常问题、提供全天候服务，并让人工负责不可靠的情况。导出的 n8n 工作流 JSON 仍在添加中。
    需要知道的事
    仓库只记录了架构，尚无工作流文件，也没有说明如何计算置信度，因此你需要自行设计这项检查。
    自己试试
    推荐工具
    n8n
    复制提示词
    请搭建一个 n8n 工作流，使用基于[我的知识库，例如 Google 文档或 FAQ 表]的 AI agent 在 WhatsApp 上回答客户问题。当 agent 的置信度较低，或客户要求人工时，请将完整会话转发给 Telegram 上的我，并让我从那里回复。当一个测试问题获得正确答案，且一个故意设计的棘手问题连同上下文被升级转交给我时，才算完成。
    原始来源：https://github.com/zezo640/whatsapp-ai-support-agent-n8n

<details>
<summary>英文原文</summary>

    Answer WhatsApp customer questions and escalate to humans
    An n8n and OpenAI agent answers WhatsApp questions from a knowledge base and escalates low-confidence cases to a human on Telegram with full context.
    Done with
    N8
    n8n
    What they did
    An n8n workflow takes each incoming WhatsApp message and assembles the conversation history plus the company knowledge base. OpenAI drafts a reply grounded in that content, and a confidence check decides whether it can be answered reliably. Confident answers go back on WhatsApp. Otherwise the case goes to the human team on Telegram with the full conversation attached.
    How it went
    The README gives no measured results, only design goals: cover routine questions, give round-the-clock coverage, and keep a human on unreliable cases. The exported n8n workflow JSON was still being added.
    Worth knowing
    The repo documents architecture only, with no workflow file yet and no description of how confidence is scored, so you would have to design that check yourself.
    Try it yourself
    with
    n8n
    Copy prompt
    Build an n8n workflow that answers customer questions on WhatsApp using an AI agent grounded in [my knowledge base, e.g. a Google Doc or FAQ sheet]. When the agent's confidence is low or the customer asks for a human, forward the full conversation to me on Telegram and let me reply from there. Done when a test question gets a correct answer and a deliberately tricky one gets escalated to me with context.
    Original source: https://github.com/zezo640/whatsapp-ai-support-agent-n8n

</details>

## 原作者的方法与来源

来源：[Ziad Hady：WhatsApp支持架构README（设计说明）](https://github.com/zezo640/whatsapp-ai-support-agent-n8n)

作者方法摘要

1. 将传入的WhatsApp消息与会话历史、公司知识汇集，再用OpenAI起草有资料依据的回复。
   English summary: Assemble incoming WhatsApp messages with conversation history and company knowledge, then use OpenAI to draft grounded replies.

2. 该设计将有把握的答案发回WhatsApp，将不确定事项连同完整上下文送到Telegram人工团队；置信度评分方法未发布。
   English summary: The design routes confident answers to WhatsApp and uncertain cases with full context to a human team on Telegram. The confidence scoring method is not published.

3. README说明架构与目标，工作流导出仍在添加中；这些摘要不证明部署已运行，也不证明已实现Telegram到客户的回复路径。
   English summary: The README describes architecture and goals; the workflow export is still being added. These summaries do not establish a working deployment or a Telegram-to-customer reply path.

以上是作者设计说明摘要，并非代码执行或生产验证。

## 我们的简要分析

商业分数未评定，自用价值待核实；不计入completed v2深研。

原始README与固定树已读，但公开仓库只有架构文档，没有工作流导出、置信度实现、回流/权限日志、质量、客户、费用或独立复现。当前平台资料不能补成原项目实测，保存未评分简报。

### 商业判断与证据范围

保存未评分简要分析，自用价值待核实，不计入completed v2深研。原始公开README已读，但它明确是架构说明和设计目标，没有运行结果。固定提交的完整仓库树只有README.md，无导出工作流，不能当成可直接导入、部署或已稳定运行的交付包；这不证明作者从未有过私有实现。潜在使用者是WhatsApp客服团队，付款人可能是店主或客服负责人，但没有客户、付费、问答量、质量或实际成本证据。

依据：archive-case-20261017, S674559adf368

### 公开的是路由方案，未给出实现

README把传入消息、会话历史和公司知识交给OpenAI生成回复，再经confidence check决定发回WhatsApp或把完整上下文送到Telegram；24/7、覆盖常见问题与人工接管是设计目标，不是已测覆盖率或服务等级。原作者方法只做简短中英设计摘要，不翻译整篇README。源站模板还要求客户主动要人工时转交、可从Telegram回复和两类测试，这些不是README已实现的明确步骤。

依据：S674559adf368, archive-case-20261017

### 置信度与可核对依据分别设计

README没有公开置信度的生成方式、阈值、校准样本或如何发现错误。模型自称有把握不能代替来源正确、规则适用与未知项检查。应先用参考答案区分资料内可答、冲突、缺失和需要人工的意图，再检查误答与漏升级，不用一个正确问题和一个棘手问题推断整体可靠性。这些是我们的评审建议，未在本例实现或运行；“基于知识库”也不自动证明每个回答都引用正确版本。

依据：S674559adf368, archive-case-20261017

### 通知、领取与回复客户分开

把完整会话发到Telegram，不等于有人领取、客户已获答或WhatsApp机器人已停止继续回复。README没有说明会话关联、人员身份、暂停/恢复、超时、重复事件、人工回复回到客户的路径及确认记录。当前n8n节点的发送、等待响应与批准功能只能作为已有积木比较，不能补成作者的实现。若要经营，必须先定义谁何时接管和未接管时怎么办，人工队列不能因通知发送成功就自动关闭。

依据：S674559adf368, S071b02979073, archive-case-20261017

### 完整上下文会跨越两个渠道

README刻意把客户渠道与操作员渠道分开，但这不等于已经验证隐私隔离。Telegram FAQ说明机器人收到的消息与私聊、频道、群组管理员和privacy mode条件有关；它描述平台能力，不证明本例设置或所有人员都应看客户完整对话。未来设计应核对必要字段、人员可见范围和保存期限，不把全部历史无条件搬运或当公开调试样本。本轮没有真实会话、机器人账号、密钥、WhatsApp/Telegram连接或消息操作。

依据：S674559adf368, S69b841c7350d

### 执行、模型与人工维护不能混算

当前n8n报价说明按工作流执行次数计量，FAQ对聊天场景还区分会话与每会话消息数；不能把每名客户的一次咨询当一次执行。报价页显示的欧元及年付口径不混入下面USD假设，也不能从包含Assistant credits推断本例OpenAI费用全部覆盖。作者没有公开模型、上下文长度、渠道/提供方费用或部署方式。固定FAQ、知识库搜索后人工回答和平台现成节点是可比较基线，不默认新建一个agent就能降低总成本。

依据：S9c31625dedcc, S071b02979073, S674559adf368

### 原型与维护的两种有限情景

以下全为USD规划假设，不是作者账单、平台报价或24/7人工SLA。799美元限定原型：资源40、人工12小时×40=480、其他30、获客120，可变670、贡献129；月2项减固定500，月贡献-242。499美元客户月：资源预算80、人工7小时×40=280、其他20、获客60，可变440、贡献59；8客户减固定800，月贡献-328。多2小时支持使贡献-21。资源未测量，未知模型/消息超额、客户许可、正式上线评审、持续值守、首次接入及税费退款不含在内。

依据：S9c31625dedcc, S674559adf368, S69b841c7350d

### 反馈、反证与停止条件

检索原项目名称、HN和GitHub未取得可归属的独立使用结果；仓库公开元数据或没有开放issue不当满意度。最强反证是架构把知识约束和人工升级放在中心，平台也确有消息/批准积木；这可能适合作为设计起点，但不足以证明无需重做实施。先取得可检查导出或重新定义合成回放，检查资料缺失、客户要人工、重复/迟到事件和无人领取，记录所有复核与修复。若越权泄露、误答无法发现、回流错人或支持超预算，应停止扩大，不补造分数。

依据：S674559adf368, S071b02979073, S69b841c7350d, S9c31625dedcc, archive-case-20261017

## 事实与证据边界

- 原始README由Ziad Hady署名，描述n8n编排和OpenAI知识问答、WhatsApp客户渠道及Telegram人工升级设计。（S674559adf368）
- 固定提交0945a2959170b035fc8ddf91132c5b63d04bf033的完整树只有README.md，未发布工作流JSON；不是对作者私有实现是否存在的判断。（S674559adf368）
- README把全天候覆盖、常见问题与可靠人工转交列为目标，没有测量结果或置信度评分细节。（S674559adf368, archive-case-20261017）
- 客户主动要求人工、从Telegram回复以及两个测试完成条件来自源站推荐模板，不能当作者实际验收。（archive-case-20261017）
- 当前n8n WhatsApp节点列出发送与等待响应/批准等功能，不证明本例采用或已做好回流。（S071b02979073）
- Telegram FAQ对机器人收到哪些私聊/群组/频道消息给出条件说明，不能直接作本例权限隔离证明。（S69b841c7350d）
- n8n当前报价按workflow executions并讨论聊天消息估算，不能把咨询人数、消息数和执行次数混为同一计量。（S9c31625dedcc）

## 成本情景（全部是假设）

| 情景 | 假设收入 | 资源 | 人工 | 其他 | 获客 | 单位贡献 | 月贡献 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 规划假设：限定架构原型 | 799 | 40 | 480 | 30 | 120 | 129 | -242 |
| 规划假设：有限知识与回流维护 | 499 | 80 | 280 | 20 | 60 | 59 | -328 |

币种USD；没有实际收费、账单、成本测量或已得收入。
## 自用价值：待核实

公开架构可作设计参考，但没有可导入工作流、阈值、回流、质量或维护数据，无法确认净收益和实施负担。

依据：S674559adf368, S071b02979073, S69b841c7350d, S9c31625dedcc, archive-case-20261017

- 适用人群：有版本化客服知识、能设计和复核跨渠道升级的技术及客服负责人。
- 用途：在合成对话上评审回答、拒答、转交、领取和回流设计。
- 预期收益：可能减少常见问题反复整理和上下文丢失，但没有覆盖率、准确率、节时或客服成本实测。
- 设置成本：合成问题、参考答案、知识版本、升级角色、会话关联与状态规则；公开导出缺失，本轮不搭建账号或调用服务。
- 维护成本：知识/规则/节点变动、阈值复核、人工队列值守、失败恢复、日志与用量检查。
- 使用频率：随实际客户问题与升级需要，README没有可外推的量级或使用频率。
- 隐私风险：完整客户对话跨渠道含私人信息，需核对必要字段和可见人员；不默认不同渠道等于隔离，本轮不接真实数据。
- 错误风险：可能自信误答、错配会话、无人领取、重复回复或人工回流错误，需要资料核对、状态记录和人审。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/answer-whatsapp-customer-questions-and-escalate-to-humans

建议工具：n8n

    Build an n8n workflow that answers customer questions on WhatsApp using an AI agent grounded in [my knowledge base, e.g. a Google Doc or FAQ sheet]. When the agent's confidence is low or the customer asks for a human, forward the full conversation to me on Telegram and let me reply from there. Done when a test question gets a correct answer and a deliberately tricky one gets escalated to me with context.

自编试用模板

准备条件：合成对话、版本化知识、参考答案、角色和升级规则、会话标识与待审状态表。

工具：原例标n8n，README还写OpenAI、WhatsApp和Telegram；本轮只读资料，不安装、接账号或执行模型。

预期结果：有出处的答复草稿、未知项、升级与人工回流方案、失败清单；自编模板未实测，不发送真实消息。

### 用合成对话检查回答、升级和人工回流

自编模板

出处：研究团队自编

依据：S674559adf368, S071b02979073, S69b841c7350d, S9c31625dedcc, archive-case-20261017

    仅使用[合成WhatsApp对话]、[版本化知识]、[人工参考答案]、[允许字段/角色]和[明确升级规则]。不要连接真实WhatsApp或Telegram、发送消息、读取客户资料、创建凭据或调用额外付费API。逐条列会话标识、来源版本、支持句、拟答、未知项和与参考答案的差异；不要把模型自称置信度高当正确证据。资料缺失/冲突或客户要人工时列升级原因、最少必要上下文、拟接收角色和待领取状态。设计从通知、领取、人工草稿、审批、客户回复到恢复机器人的关联与确认，不把通知已发当接管完成。回放重复/迟到消息、无人领取、未知会话、误答和超时；全部保持草稿，展示状态差异、需人工决定事项和恢复办法。分别记录消息、执行、模型与人工维护变量，不声称已达24/7服务、准确率或节时。

## 来源

- archive-case-20261017：[Answer WhatsApp customer questions and escalate to humans](https://agentusecases.ai/use-case/answer-whatsapp-customer-questions-and-escalate-to-humans)。支持n8n/OpenAI知识问答、WhatsApp/Telegram人工路由、无测量/无导出和推荐试用模板的归档，模板不是作者实际指令。
- S674559adf368：[GitHub - zezo640/whatsapp-ai-support-agent-n8n: 24/7 WhatsApp customer support agent answering from a company knowledge base, with confidence-based escalation to a human operator on Telegram. Built with n8n + OpenAI. · GitHub](https://github.com/zezo640/whatsapp-ai-support-agent-n8n)。登记的原始README设计说明：n8n/OpenAI、知识和历史、置信度路由、Telegram完整上下文与设计目标；固定树只有README，未公布工作流或测量结果，不当运行验证。
- S071b02979073：[/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp)。当前n8n官方WhatsApp Business Cloud节点文档列发送、模板、等待响应和人工批准等积木；不是本例使用版本或Telegram回流/置信度门槛实现。
- S69b841c7350d：[Bots FAQ](https://core.telegram.org/bots/faq)。Telegram官方FAQ说明机器人能接收哪些私聊/群组/频道消息及privacy mode条件；不证明本例配置、人员权限或人工接管完成。
- S9c31625dedcc：[n8n Plans and Pricing - n8n.io](https://n8n.io/pricing/)。n8n当前报价按workflow executions并说明每次工作流运行、聊天消息估量与Assistant credits；报价币种EUR、年付口径与USD假设分开，不当原作者模型/消息/维护账单。

## 仍待核实

只有公开架构README和固定树，无工作流JSON、置信度机制、人工领取/回流与权限实现、日志、质量、客户、费用或独立复现。当前平台功能/价格不是作者配置。未运行或安装项目、执行模型、接真实会话、创建账号/凭据或发送消息，无额外付费API。
