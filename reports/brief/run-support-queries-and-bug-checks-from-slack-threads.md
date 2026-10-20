# 用Doozy在Slack线程中查询支持问题

## 中文

    从Slack讨论串执行支持查询和缺陷检查
    Doozy是一款Slack agent，它接收支持人员交办的任务，在沙箱内对Postgres、Stripe、GitHub和Linear执行操作，再将结果发回讨论串；有13个人每天使用它。
    使用的是
    自建或未具名agent
    他们做了什么
    在Spur，支持人员在Slack讨论串中提及Doozy并交给它任务。它在一个全新、不保存凭据的E2B沙箱中运行，由外部网关针对每次请求添加凭据。它查询Postgres、Stripe、GitHub、Linear、PostHog、MCP服务器或网页，然后将结果和文件发回讨论串。破坏性工具默认被拒绝，直到所有者启用。
    进展与成效
    Spur有13个人每天使用它，主要是支持和客户成功人员，而不是工程师；作者称它已成为团队的重要组成部分。最初的版本比较粗糙，连讨论串里发来的文件都不太能读取。
    值得注意
    将凭据放在沙箱外，并默认拒绝破坏性工具；作者表示，提示词注入仍可能滥用已授权工具，但无法泄露密钥。
    亲自尝试
    使用
    Claude Code
    复制提示词
    配置一个可以接收支持任务的助手。当我描述问题，例如[客户付款失败或疑似缺陷]时，通过对[你的数据库、Stripe、GitHub和Linear]的只读访问进行查询，并写下发现，附上对应记录的链接。当你给出一份可以发到Slack讨论串的简短摘要时，任务完成。不要修改或删除任何数据；在写入或发送任何内容之前，暂停并向我展示。
    原始来源：https://news.ycombinator.com/item?id=50166597

<details><summary>English original</summary>

    Run support queries and bug checks from Slack threads
    Doozy, a Slack agent, takes tasks from support staff and runs them against Postgres, Stripe, GitHub and Linear in a sandbox, then posts results in the thread; 13 people use it daily.
    Done with a
    custom-built or unnamed agent
    What they did
    At Spur, support staff mention Doozy in a Slack thread with a task. It runs in a fresh sandbox (E2B) holding no credentials, while gateways outside add them per request. It queries Postgres, Stripe, GitHub, Linear, PostHog, MCP servers or the web, then posts results and files back in the thread. Destructive tools start denied until owners enable them.
    How it went
    13 people at Spur use it daily, mostly support and success rather than engineers, and the author calls it a critical part of the team. The first version was hacky and barely read files sent in a thread.
    Worth knowing
    Keep credentials outside the sandbox and deny destructive tools by default; the author says injection can still misuse granted tools, though it can't leak a key.
    Try it yourself
    with
    Claude Code
    Copy prompt
    Set up a helper I can hand support tasks to. When I describe a problem, like [a customer's failed payment or a suspected bug], look it up using read-only access to [your database, Stripe, GitHub and Linear] and write up what you found with links to the records. You're done when you've given me a short summary I could post in a Slack thread. Never change or delete any data, and pause and show me anything you'd write or send before doing it.
    Original source: https://news.ycombinator.com/item?id=50166597

</details>

## 原作者的方法与来源

来源：[HN original discussion](https://news.ycombinator.com/item?id=50166597)

方法摘要未收录

## 简要分析

商业分数未评定。

### 先避免同名产品错配

本案是Spur内部名为Doozy的Slack助手，目录标记自建agent；试用区推荐Claude Code不证明实际底层模型是Claude Code。搜索出现同名Doozy服务和不同Spur代码项目，未取得可靠交叉身份链接，因此未把它们的功能、价格或客户数据拼入本案。原HN及实现代码不可得，保留为证据简报。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-support-queries-and-bug-checks-from-slack-threads)

### 把任务入口、查询和结果分开

目录转述支持人员在线程内提及助手，助手进入新沙箱、经网关访问业务系统，并返回结果与文件。13人日用是内部采用主张，不是13个客户、付费席位或已处理工单数。没有公开准确率、处理时长、人工接管率和最终客户满意度，不能由重要组成部分的评价算省时或收入。初版读文件能力弱，说明输入完整性也需验收。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-support-queries-and-bug-checks-from-slack-threads)

### 密钥保密与工具授权不是一回事

E2B官方提供沙箱外HTTPS请求头注入，说明不必把密钥交给可执行代码；但本次不能证明原案使用该特定产品或配置。即使拿不到密钥，agent仍可能用获准接口读出不该读取的数据，或发起范围过宽的动作。目录的无法泄露密钥应作为来源主张保留，而不是整套系统安全保证。需要同时限定身份、目标、动作和输出。

依据：[Se2b](https://e2b.dev/resources/introducing-e2b-secrets), [Sdirectory](https://agentusecases.ai/use-case/run-support-queries-and-bug-checks-from-slack-threads)

### 只读查询仍有敏感数据边界

只读账户能阻止一部分写入，却可能读取整张表。PostgreSQL行级策略可约束数据行，但默认、角色和所有者例外必须核对。研究建议把Slack请求者映射到被允许的客户和字段，采用限定查询、结果行数与超时，避免任意SQL。这些是设计建议，未连接数据库或检验原案租户隔离，也不声称它已采用RLS。

依据：[Spg](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)

### 线程回复也是一次数据披露

查询获得结果不意味着线程里的每个人都有权看到。返回文件尤其可能扩大范围，建议只给必要摘要与授权记录链接，并核对目标频道与接收者。Slack官方提示模型生成URL的预览可能带来外传，关闭不必要预览与限制出站目标可降低风险，但不能代替内容审查。本轮未读取私人Slack或发送任何消息到团队。

依据：[Sslack](https://docs.slack.dev/concepts/security/)

### 商业需求在跨系统交接

假设客户是支持团队已在Slack沟通、排错却经常要向工程师追问的SaaS公司。潜在付款者为支持或工程负责人，购买的是更快得到可检查线索、减少上下文切换，而不是一个聊天入口。可交付项目可能包括只读连接、业务字段映射、权限测试与人工接管。需求频率和预算需实际验证；原案没有外部销售、套餐或收益，不能直接包装成已验证SaaS生意。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-support-queries-and-bug-checks-from-slack-threads)

### 优先对比已有支持工具

人工支持控制台、固定SQL报表和工单内的已有记录链接都可能解决主要问题，不一定需要能写代码的沙箱。对于少数固定问法，受限查询模板更易审查；任务跨多个系统且长尾多时，自由工具编排才可能有额外价值。复制条件包括清晰schema、工单与用户ID对应、获准数据范围及业务负责人；这些通常比模型调用本身更费维护。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-support-queries-and-bug-checks-from-slack-threads), [Spg](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)

### 先交付一个可复核问题类型

建议从自有合成数据中的一种查询开始，例如解释失败状态并附记录链接，不执行退款、改订单或修改客户信息。每条结果应包含查到什么、没有查到什么和人工下一步。假设首批客户来自已有支持系统集成合作，使用演示证据获得试点；本轮没有联系第三方。若每客户都需要大量定制字段和权限，服务更接近集成项目，而非低成本自助订阅。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-support-queries-and-bug-checks-from-slack-threads), [Sslack](https://docs.slack.dev/concepts/security/)

### 人工复核决定单位成本

以一份跨系统问题调查摘要为单位，每月200份。低返工假设审核5分钟×24USD/h=2，模型预算0.10，已列2.10/份、420/月；高返工15分钟=6，模型0.30，6.30/份、1260/月。均为研究者情景，不是作者工时或工具报价。沙箱、存储、接口维护、首次集成与获客成本未知另计，不能默认零；售价未知，不算利润。13名内部用户不足以确定月工单量。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-support-queries-and-bug-checks-from-slack-threads)

### 自用价值需要团队条件

适用的是已有多系统访问需求且能审查结果的支持/成功团队，而不是普通个人随手安装就用。可能收益为减少切换和重复问询，实际净省时待核实。设置需要映射数据、授权与日志，维护依赖系统更新、密钥轮换和权限撤销。使用可随工单每日发生，但低量团队维护负担可能更高。错误包括查错客户、误认状态、混淆线程与把未知写成已解决。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-support-queries-and-bug-checks-from-slack-threads)

### 只制定合成数据试用计划

用两组互不授权的合成客户和一条失败交易状态，验证结果仅返回正确范围与必要字段；拒绝跨客户查询和任何写操作，确认敏感值不出现在日志、文件或URL。计划应区分任务成功、权限拒绝、来源不可达和需人工接管，不把失败沉默处理成无异常。本轮未搭沙箱、创建密钥、连接业务系统或进行真实试用；目标是可审阅验收方案。

依据：[Se2b](https://e2b.dev/resources/introducing-e2b-secrets), [Spg](https://www.postgresql.org/docs/current/ddl-rowsecurity.html), [Sslack](https://docs.slack.dev/concepts/security/)

## 自用价值：待核实

内部采用人数为目录转述，净省时与准确率无独立核验。

依据：Sdirectory, Spg, Sslack

- 适用人群：在Slack协作且需跨系统查问题的支持团队。
- 用途：只读排错、整理证据、生成线程摘要。
- 预期收益：可能减少系统切换，未量化实际收益。
- 设置成本：系统连接、客户ID与权限映射、合成样例与输出审批。
- 维护成本：schema变化、接口、密钥轮换、撤销与日志治理。
- 使用频率：随支持工单，目录称每日使用但工单量未知。
- 隐私风险：客户数据、跨租户结果、线程接收者及输出链接。
- 错误风险：错误关联客户、状态误判、遗漏文件与误报解决。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/run-support-queries-and-bug-checks-from-slack-threads

建议工具：Claude Code

    Set up a helper I can hand support tasks to. When I describe a problem, like [a customer's failed payment or a suspected bug], look it up using read-only access to [your database, Stripe, GitHub and Linear] and write up what you found with links to the records. You're done when you've given me a short summary I could post in a Slack thread. Never change or delete any data, and pause and show me anything you'd write or send before doing it.

自编试用模板

准备条件：自有合成数据、两组隔离客户、限定查询和输出范围。

工具：获准只读查询接口与助手；本轮无实际部署。

预期结果：一份有来源、未知项与人工下一步的支持摘要计划，未实测。

### 源站Copy prompt

原文模板

出处：https://agentusecases.ai/use-case/run-support-queries-and-bug-checks-from-slack-threads

依据：Sdirectory

    Set up a helper I can hand support tasks to. When I describe a problem, like [a customer's failed payment or a suspected bug], look it up using read-only access to [your database, Stripe, GitHub and Linear] and write up what you found with links to the records. You're done when you've given me a short summary I could post in a Slack thread. Never change or delete any data, and pause and show me anything you'd write or send before doing it.

### 支持查询权限测试计划

自编模板

出处：研究团队自编

依据：Spg, Sslack

    只使用提供的合成数据制定支持查询计划。列出请求者、获准客户、字段和回复接收者；只读、不改状态、不退款、不外发。区分成功、拒绝、来源不可达与未知，并提出跨客户拒绝和输出脱敏测试。不要连接真实服务或索取密钥。

## 来源

- [许可目录：Doozy支持查询流程](https://agentusecases.ai/use-case/run-support-queries-and-bug-checks-from-slack-threads)：目录转述Spur内部Doozy工作流与13人日用；未核实原作者、真实运行或客户收益。
- [E2B：沙箱外凭据注入](https://e2b.dev/resources/introducing-e2b-secrets)：2026-10-07官方说明通过目标HTTPS规则在沙箱外插入请求头，避免将真实密钥放入沙箱环境/文件；这支持一种机制，不证明Doozy具体实现。持有工具调用能力仍需权限边界。
- [PostgreSQL18：行级权限](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)：表访问权限与行级策略不同；默认无行策略，启用RLS且无适用策略时默认拒绝，owner/superuser/BYPASSRLS例外。只读不等于只能读获准客户数据。
- [Slack：最小权限与数据外传防护](https://docs.slack.dev/concepts/security/)：官方要求最小scope、请求来源核验、凭据关联owner并避免日志回显；模型输出URL可能经链接预览造成外传，建议默认关闭unfurl并约束出口。
- [HN原始讨论（未读取）](https://news.ycombinator.com/item?id=50166597)：保留原链接，不捏造原作者或代码；不再重试。
