# 用 n8n 和 Supabase 记忆处理房源对话与预约

## 中文

    使用带记忆的助手处理房地产运营
    发帖者构建了一个AI智能体工作流，通过保留记忆进行有上下文的对话，并动态更新房产数据。
    使用的是
    n8n
    他们做了什么
    发帖者在n8n中搭建了一个房地产公司的运营助手。它接收客户聊天消息，使用带记忆的AI智能体进行上下文对话，通过Supabase中的向量嵌入保存长期知识，更新房产数据、检查可用时间，并通过Google Calendar预约、改期或取消，然后用Gmail发送确认和通知；开发者编写了逻辑，也能按客户需要更换日历工具。
    进展与成效
    来源称它把对话、排期、线索资格判断、跟进和房产更新放在同一个系统中，发帖者表示Google Calendar的预约、排期和取消运行顺利。没有提供硬指标、部署数量或失败案例。
    值得注意
    最清楚的实现细节是，长期记忆使用向量嵌入加Supabase，排期使用Google Calendar而不是cal.com。
    亲自尝试
    使用n8n
    复制提示词
    构建一个n8n工作流，让AI智能体使用[电子表格或数据库]中的数据，回答[客户/租户/团队]关于我的[房产]的问题。让它具备记忆，记住每个人此前的对话；当我指示时，允许它更新[价格、可用情况、状态]等房产字段。在更改任何记录或发送任何消息前，先展示将进行的更改并等待我的批准；当一次测试对话完整跑通后就停止。
    原始来源：https://www.reddit.com/r/n8n_ai_agents/comments/1tha9mp/ive_built_an_ai_real_estate_assistant_heres_what

<details><summary>English original</summary>

    Run real-estate operations with a memory-equipped assistant
    The poster built a workflow with an AI agent that keeps memory for contextual conversations and updates property data dynamically.
    Done with
    N8
    n8n
    What they did
    The poster built the workflow in n8n as an operations assistant for a real estate business. It takes incoming client chat messages, uses an AI agent with memory for contextual conversations, stores long-term knowledge with vector embeddings in Supabase, updates property data, checks availability, and books, reschedules, or cancels appointments through Google Calendar, then sends confirmations and notifications through Gmail; the person built the logic and can swap calendar tools for a client.
    How it went
    The source says it handles conversations, scheduling, lead qualification, follow-up, and property updates in one system, with the poster saying Google Calendar booking, scheduling, and canceling worked smoothly. It gives no hard metrics, deployment numbers, or failure cases.
    Worth knowing
    The clearest implementation catch is that long-term memory was handled with vector embeddings plus Supabase, and scheduling used Google Calendar rather than cal.com.
    Try it yourself
    with
    n8n
    Copy prompt
    Build an n8n workflow with an AI agent that answers questions from [clients/tenants/team] about my [properties] using data in [spreadsheet or database]. Give it memory so it remembers each person's earlier conversation, and let it update property fields like [price, availability, status] when I tell it to. Before it changes any record or sends any message, show me what it will change and wait for my approval; stop once a test conversation works end to end.
    Original source: https://www.reddit.com/r/n8n_ai_agents/comments/1tha9mp/ive_built_an_ai_real_estate_assistant_heres_what

</details>

## 原作者的方法与来源

来源：[AI real estate assistant with memory](https://www.reddit.com/r/n8n_ai_agents/comments/1tha9mp/ive_built_an_ai_real_estate_assistant_heres_what/)

The author processes client messages with an AI agent and stores long-term knowledge using embeddings and Supabase.
作者通过AI智能体处理客户消息，并用向量嵌入及Supabase存储长期知识。

The workflow updates property data and uses Google Calendar for appointments, with Gmail notifications.
工作流更新房产资料，用Google Calendar管理预约并通过Gmail通知。

The author reports smooth scheduling and says the calendar integration can be changed for a client.
作者自述排期顺利，并表示可以按客户需要更换日历接入。

## 简要分析

商业分数未评定。

### 有记忆不等于已验证长期运营

原帖和流程图提供了组件与动作描述，评论又确认当前使用Google Calendar、过去用过cal.com。没有可运行工作流、跨会话测试、房源更新后的回答样本或真实部署数量。有人提出想介绍给客户，只能算合作兴趣；另有人问是否卖出，没有可核答案。因此保存未评分简报，重点验证记忆是否会串人、过期或被错误更新，暂不填写商业收入与利润。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-real-estate-operations-with-a-memory-equipped-assistant), [Sauthor](https://www.reddit.com/r/n8n_ai_agents/comments/1tha9mp/ive_built_an_ai_real_estate_assistant_heres_what/)

### 三类数据需要不同处理

建议将短期对话、长期说明资料和实时房源状态分开。向量相似检索适合找相关说明，不适合作为唯一的价格、可售状态和预约事实来源；这些字段应回查带版本和更新时间的结构记录。用户说以前喜欢某个区域，不代表其当前需求永远不变。记忆更新应保留来源和时间，冲突时询问或待核。这些是研究建议，不是作者已经实现的功能。

依据：[Srag](https://supabase.com/docs/guides/ai/rag-with-permissions), [Ssession](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/common-issues)

### 记忆必须与权限绑定

不同客户、门店和员工可见范围要先确定，再执行检索；不能先把所有人的内容取出交给模型自行保密。Supabase提供RLS等机制，但需要正确的角色、授权和测试；高权限服务角色不能被想当然地视作普通用户。流程中传入一个session字符串也不等于身份验证。原帖没有公开这些配置，所以不能判定已安全，也不能反过来声称已泄露。

依据：[Srag](https://supabase.com/docs/guides/ai/rag-with-permissions), [Srls](https://supabase.com/docs/guides/database/postgres/row-level-security)

### 会话连续性与写入确认

n8n官方说明Simple Memory的会话键和共享实例行为，并指出它不适用于queue模式。本案未明确是否使用该节点，不能将它的限制直接算到作者头上；复制者仍应核实际记忆实现。价格修改、取消预约和通知发送分别是独立操作，建议先显示变更再批准，保留回执和版本；失败后核是否已完成再重试。模型生成的旧记忆不能覆盖当前业务记录。

依据：[Ssession](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/common-issues), [Smemory](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/)

### 先判断是否需要向量记忆

如果需求只是预约、改期和提醒，Cal.com个人免费方案已是具体替代；并不意味着团队协作、特定渠道或完整房源运营都免费。Supabase当前Free列500MB数据库和不活跃一周暂停，Pro从25美元/月起，这只是数据库平台费用，还需模型、n8n、渠道、维护和人工。没有任务量和部署方式，不能给总成本或利润数字。低频个人使用可先用结构表和预约工具，减少维护组件。

依据：[Salt](https://cal.com/pricing), [Sprice](https://supabase.com/pricing)

### 可能收费的部分仍待验证

潜在客户是重复处理房源咨询、已有可整理数据的中介或管理团队，付款人可能是业务负责人。可售交付可能是数据整理、身份隔离、更新验证和持续支持，属于推断。只有一个“能记住对话”的演示，难以证明比现有CRM笔记更值钱。获客可从已有实施关系中的单一流程验证开始，但本轮没有联系任何人。没有实际工时、客户报价和复购，本例不做伪精确评分。

依据：[Sauthor](https://www.reddit.com/r/n8n_ai_agents/comments/1tha9mp/ive_built_an_ai_real_estate_assistant_heres_what/), [Srag](https://supabase.com/docs/guides/ai/rag-with-permissions)

### 讨论与使用结果分开

原帖评论主要是希望了解、请求合作、询问日历或记忆刷新方案，没有独立部署者提供长周期效果。外部聚合转载不能增加独立来源数。检索n8n社区与GitHub找到session配置问题，但不是作者这个助手的缺陷证据。它们适合提示验收覆盖边界，不适合推断本产品失败率。缺反馈不代表没有价值，意味着应优先取得可重放测试和匿名结果，而不是堆积赞美评论。

依据：[Sauthor](https://www.reddit.com/r/n8n_ai_agents/comments/1tha9mp/ive_built_an_ai_real_estate_assistant_heres_what/), [Ssession](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/common-issues)

### 合成数据的验收顺序

先准备两个虚构门店、两个客户和同名房源：相同问题不能返回他人记忆；修改价格后必须使用新结构记录；删除或撤回资料后不应继续检索到旧片段；未确认的价格变更只能形成草稿。再测试重启、并发消息、会话键缺失和取消预约超时。成功标准是隔离与状态结果可逐项核对，不预填准确率。若无法解释记忆来源、无法可靠撤回或现成工具已足够，就停止增加自动写入权限。

依据：[Srag](https://supabase.com/docs/guides/ai/rag-with-permissions), [Srls](https://supabase.com/docs/guides/database/postgres/row-level-security), [Ssession](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/common-issues)

## 试用准备与预期结果

仅虚构门店、客户、房源、预约和记忆记录；不含真实凭据或通信。
带来源和版本的答复、建议变更及批准点；不发送消息、不更新真实房源。

使用两个虚构门店、客户和同名房源建立测试表。每次请求先验证客户及门店范围，显示命中资料来源、日期和版本；价格以当前结构记录为准，旧聊天不能覆盖。测试串会话、价格修改、撤回资料和预约取消超时。只输出答复草稿及变更建议，真实发送或修改前等待批准；来源不足时说待核，不补造记忆。

## 来源

- [目录原文和试用模板](https://agentusecases.ai/use-case/run-real-estate-operations-with-a-memory-equipped-assistant)：完整目录仅说明能力自述，未给部署指标或失败样本。
- [作者原帖与公开评论](https://www.reddit.com/r/n8n_ai_agents/comments/1tha9mp/ive_built_an_ai_real_estate_assistant_heres_what/)：作者提及Supabase向量记忆、Google Calendar和Gmail；评论中的合作意向不等于成交。
- [向量检索权限设计](https://supabase.com/docs/guides/ai/rag-with-permissions)：向量相似检索也可按用户权限过滤，不自动证明本案已配置隔离。
- [数据库行级权限与角色](https://supabase.com/docs/guides/database/postgres/row-level-security)：授权与行级策略需要共同核验，service_role等高权限路径不能默认视为受限。
- [Simple Memory会话键](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/common-issues)：多个节点默认共享实例，非聊天触发器需管理session；固定测试键不可直接生产。
- [Simple Memory运行边界](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/)：窗口长度与会话键，queue模式不适合该节点；不推断作者实际使用此节点。
- [Supabase现行价格](https://supabase.com/pricing)：Free500MB数据库且不活跃一周暂停，Pro25美元起，非整个助手总成本。
- [Cal.com预约替代](https://cal.com/pricing)：个人免费预约方案，团队功能另计；不能替代所有房源记忆需求。
