# 用 n8n 和 Gemini 回复诊所患者咨询

分析深度：简要研究（brief）；商业评分未评定，不计入深研完成数。

## 案例完整中文译文

    通过聊天回答诊所患者的咨询
    一个使用 n8n 和 Gemini 的 agent 接收患者的聊天消息、保留上下文、使用 Google Sheets 中的诊所信息，并回复咨询。
    实际使用
    n8n
    Gemini
    具体做法
    患者通过聊天界面发送消息，消息进入一个 n8n 工作流。Gemini agent 使用 Simple Memory 保留上下文，从 Google Sheets 获取诊所详情，并自行生成咨询回复。
    结果如何
    没有报告结果或指标。所述目标是让诊所沟通更智能，并减少人工工作。
    自行试用
    推荐工具
    n8n
    复制提示词
    为我的[诊所类型]构建一个 n8n 工作流，使用由 Gemini 驱动的聊天 agent，根据我的[Google Sheet]中的信息回答患者有关[服务、营业时间、价格、位置]的咨询。在消息之间保留对话上下文；对于任何医疗问题或不明确的问题，告诉患者工作人员会跟进，并通知[工作人员邮箱]。用示例问题测试，在上线前向我展示答案。
    原始来源：https://x.com/SahilWagave/status/2109697093778690255

<details>
<summary>English · 完整归档原文</summary>

<pre>Answer patient enquiries for a clinic by chat
An n8n and Gemini agent receives patient chat messages, keeps context, uses clinic info from Google Sheets and responds to enquiries.
Done with
N8
n8n
GE
Gemini
What they did
Patients send messages through a chat interface into an n8n workflow. Gemini agent with Simple Memory for context pulls clinic details from Google Sheets and generates replies to enquiries on its own.
How it went
No results or metrics are reported. The stated goal was smarter clinic communication and less manual work.
Try it yourself
with
n8n
Copy prompt
Build an n8n workflow with a Gemini-powered chat agent for my [clinic type] that answers patient enquiries about [services, hours, pricing, location] using the info in my [Google Sheet]. Keep conversation context between messages, and for anything medical or unclear, tell the patient staff will follow up and notify [staff email]. Test with sample questions and show me the answers before going live.
Original source: https://x.com/SahilWagave/status/2109697093778690255</pre>

</details>

## 原作者的方法与来源

[X 原帖](https://x.com/SahilWagave/status/2109697093778690255)：依既有访问限制跳过，未新请求、重试、登录或换路。作者方法摘要不可用，源站模板不作为作者实现步骤。

## 我们的简要分析

商业判断：现有证据不建议商业投入；自用价值待核实。

### 功能说明不足以证明实际服务效果

本轮商业评分不评定，现有证据不建议商业投入。归档只描述患者消息进入n8n、Gemini结合Simple Memory和Google Sheets生成回复，没有回答准确率、服务量、人工净省时、成本或患者结果。目标是减少人工工作，不能改写为已经减少人工。X原帖依既有限制跳过，作者方法不可用；六份技术与竞争资料可以帮助列验收条件，但不能填补本案例实际部署和效果缺口。因此保存schema-1简要分析，不冒充completed v2深研。 依据：[archive-case-20261017](https://agentusecases.ai/use-case/answer-patient-enquiries-for-a-clinic-by-chat), [Sb17c1939c941](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow), [S06d05da8421d](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger), [S3fbc146d47ad](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets)。

### 实际工具、模板和作者方法分别保留

实际agent标注为n8n和Gemini，推荐试用工具为n8n，两者都按归档保留。医疗或不明确问题告知患者工作人员会跟进并通知邮箱，是源站建议模板里的要求；归档方法段没有明确描述该人工通知分支。不能把模板要求补成原作者已完成的接管、邮件送达或工作人员跟进。也不知道具体Gemini型号、提供方式、提示词、数据访问权限或实际诊所类型。当前官方文档只是技术对照，不用它们反推这套工作流的真实设置。 依据：[archive-case-20261017](https://agentusecases.ai/use-case/answer-patient-enquiries-for-a-clinic-by-chat), [Sea81b114bc49](https://ai.google.dev/gemini-api/docs/safety-settings), [S06d05da8421d](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger)。

### 诊所资料要可追踪且不能由聊天改写

营业时间、地址、服务和价格需要对应经诊所确认的数据行、版本和有效时间。Google Sheets节点既有读取也有创建、更新与删除操作，因此接了表格并不自动形成只读权限；本轮不配置真实连接。拟议验收应把聊天和表格中未审阅的内容视为输入资料，不能直接改权威资料或工具行为。缺价、过期信息、表格不可用应保留未知并转为人工待核对，不补一个看似合理的答案。本地合成检查只证明固定规则下的版本处理，不测量检索召回、模型理解或真实表格权限。 依据：[S3fbc146d47ad](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets), [archive-case-20261017](https://agentusecases.ai/use-case/answer-patient-enquiries-for-a-clinic-by-chat)。

### 记忆上下文不等于可靠隔离与保存

Simple Memory官方文档提供Session Key和Context Window Length，并明确生产队列模式下不能保证请求都到同一个worker，因而不适用；子节点表达式处理多项时还可能只取第一项。不能据此假设任意多用户或多worker部署都可靠。拟议验收用诊所与会话的组合键检查隔离、上下文过期和重复消息，但会话ID本身不证明患者身份，也不保证所有执行日志或副本被删除。若需要跨设备、后台恢复或多机构共享，应另行核对实现与保留策略；本轮不读取任何真实患者消息或健康资料。 依据：[Sb17c1939c941](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow), [S06d05da8421d](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger)。

### 医疗边界、模型阻断和人工确认分开

用途先限定为已批准的行政资料。任何医疗或不明确请求都按源站模板转成人工待处理；本报告不提供诊断、治疗或紧急分诊规则。Gemini内容过滤是类别和概率阈值机制，不能替代医疗正确性审核，也不能证明能识别全部医疗意图。阻断、超时或空输出时不应用另一个未审阅回答兜底。通知草稿、未知送达、已送达与工作人员确认需要独立状态，不把“将跟进”的文字当作实际通知完成。合成任务只含虚构消息ID及原因，未发邮件，人工类型标签由测试者提供，不能当自然语言分流准确率。 依据：[Sea81b114bc49](https://ai.google.dev/gemini-api/docs/safety-settings), [S06d05da8421d](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger), [archive-case-20261017](https://agentusecases.ai/use-case/answer-patient-enquiries-for-a-clinic-by-chat)。

### 人工前台与现成收件箱是具体基线

潜在使用者是诊所前台与行政人员，付款人可能是经营负责人；没有可核验的采购或续费客户。先比较现有FAQ、人工前台和带共享收件箱的现成客服系统，目标应是减少重复行政整理，并保持人工处理责任清楚。Intercom当前价格包含席位、Fin outcome及部分渠道等口径，但它不是本案例使用工具，也不能凭价格页推定满足某诊所的健康数据或合规要求。采购范围、司法辖区、隐私条款和实际数据路径均未知，本轮不作医疗机构可直接上线的结论。 依据：[S21bc2cd4aaf4](https://www.intercom.com/pricing), [archive-case-20261017](https://agentusecases.ai/use-case/answer-patient-enquiries-for-a-clinic-by-chat)。

### 执行量和人工返工决定预算

以下均为美元假设预算，不是厂商报价、作者收入或实际利润。月度行政问答维护每客户650：模型/平台预算70、人工7小时乘40为280、其他30、获客80，单位贡献190；每月8客户、固定400，月经营贡献1120。人工增至14小时则单位负90、月负1120。一次设置2400：用量50、人工35小时乘45为1575、其他125、获客250，单位贡献400；每月2项固定300，贡献500；增加10小时返工则单位负50、月负400。Chat Trigger每条用户消息都会执行工作流，一段十条消息的会话会用十次执行；不能把会话数直接当执行数。n8n欧元标价未兑换或当作上述美元预算，真实模型、额外通道、税和维护等费用仍需核实。 依据：[S06d05da8421d](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger), [S9c31625dedcc](https://n8n.io/pricing/), [S21bc2cd4aaf4](https://www.intercom.com/pricing)。

### 缺失证据与下一步验收

公开网页、GitHub和Hacker News方向检索SahilWagave诊所流程，没有取得可归属本案例的独立实际使用或付费结果。搜索出现其他汇编目录及无关内容，没有访问这些内容来替代被限制的原帖，也不把它们算成独立用户证据。下一步仅用虚构资料验收行政问答、缺失/过期数据、跨会话、跨诊所、医疗/不明确标签、模型阻断、重复消息和通知未知。若资料没有版本、会话串用、模型越界、通知未知被当成功、人工无人领取或总成本超过预算，就停止扩展。当前证据只能支持整理验收条件，不能承诺真实患者沟通改善。 依据：[archive-case-20261017](https://agentusecases.ai/use-case/answer-patient-enquiries-for-a-clinic-by-chat), [Sb17c1939c941](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow), [S06d05da8421d](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger), [S3fbc146d47ad](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets), [Sea81b114bc49](https://ai.google.dev/gemini-api/docs/safety-settings), [S9c31625dedcc](https://n8n.io/pricing/), [S21bc2cd4aaf4](https://www.intercom.com/pricing)。

## 自用与试用准备

可能辅助整理行政咨询，但回答准确性、记忆隔离、人工跟进和净省时尚未验证。

准备：虚构诊所行政目录、资料行版本、会话ID、人工标签与事件，不含真实患者或凭据。

工具：现有Python标准库；不接入n8n、Gemini、Google Sheets、邮箱或诊所系统。

预期：合成行政问答与人工待处理状态表、资料依据及未知项，无真实回复或医疗结论。

### 用虚构资料验收诊所行政聊天

研究团队自编，未调用模型实测。

    仅使用[虚构诊所服务/时间/价格/地址、资料行版本/有效期、会话ID和人工标签样例]设计离线行政聊天验收。实际工具保留n8n和Gemini，但不要接入它们或Google Sheets。对行政答案列可信资料行和版本，缺失、过期或表格不可用时保留未知；聊天不能改写权威资料。按诊所与会话分开上下文，检查过期、重复消息、跨会话及跨诊所。医疗、不明确、请求人工或模型阻断只生成待人工事项，不输出医疗建议；类型标签由测试者提供，不宣称模型分类已测。只生成含虚构消息ID和原因的通知草稿，把未知送达、已送达和人工确认分开，不发送任何消息。不读取真实患者聊天、健康资料、账号或凭据，不注册、创建凭据、购买、调用付费API、上线或联系任何人。输出结果表和未知项后停止。研究团队自编，未调用模型实测。

## 来源

- [Answer patient enquiries for a clinic by chat](https://agentusecases.ai/use-case/answer-patient-enquiries-for-a-clinic-by-chat)：归档所述n8n/Gemini、Simple Memory、Google Sheets聊天工作流及没有结果指标；医疗问题转人工和邮件通知仅见建议模板。
- [X 原帖（本轮未读取）](https://x.com/SahilWagave/status/2109697093778690255)：只保留登记链接，不新请求、不登录、不重试、不以镜像或搜索摘要补原文。
- [Safety settings  |  Gemini API  |  Google AI for Developers](https://ai.google.dev/gemini-api/docs/safety-settings)：Gemini官方安全过滤类别、概率阈值和阻断错误机制；不构成医疗正确性、识别全部医疗问题或通知成功证明。
- [n8n Plans and Pricing - n8n.io](https://n8n.io/pricing/)：n8n当前计划按工作流执行等项目计费；成本还需模型、消息和人工复核，不能把一段会话当成一次执行。
- [Intercom Pricing | Plans for every team size](https://www.intercom.com/pricing)：Intercom当前共享收件箱、人工转交、席位/Fin outcome及渠道等收费构成具体竞争基线，不证明适用本案例医疗场景或任何合规结论。
- [/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow)：n8n官方Simple Memory会话键、上下文窗口、子节点表达式取首项和生产队列模式限制；不证明本案例实际隔离、删除或部署配置。
- [/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger)：n8n官方Chat Trigger每条消息一次执行、访问认证和先前会话加载机制；会话ID不是患者身份验证，也不证明本案例已设置这些控制。
- [/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets)：n8n官方Google Sheets节点包含读取和写入操作；数据源连接不自动意味着agent只读，且没有本案例表结构或更新策略。
