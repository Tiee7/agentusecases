# 用OpenClaw跨邮箱、日历和Notion处理客户项目

## 中文

    跨Gmail、Calendar和Notion处理客户项目
    作者把OpenClaw连接到Gmail、Calendar和Notion；它把三场会议合并为一场，发送了邀请，并将一份研究报告分给多个子agent处理。
    使用的是
    OC
    OpenClaw
    他们做了什么
    作者把OpenClaw连接到Gmail、Google Calendar和Notion，并让它处理一个客户项目。它把收件箱分为紧急、待审阅和仅供参考，为紧急邮件准备草稿和附件。它发现同一项目有三场会议，未经询问便把会议合并并发送了邀请。对于一项竞争分析，它把研究、财务、起草和图表工作分给不同的子agent。
    进展与成效
    报告在六小时后返回，共42页，而手工完成需要两天；不过，文章还说最初的消息提到的是40页。agent曾误读一个数据来源，把错误的统计数据放进报告。
    值得了解
    预计需要在大约两周内检查所有内容：作者第一周在设置和审阅上花的时间更多，第二周持平，到第三周才节省时间。
    亲自尝试
    使用
    OpenClaw
    复制提示词
    连接我的Gmail、Google Calendar和Notion，帮助我管理[客户名称]的项目。找出本周关于[项目]的重复或重叠会议，提出合并方案，起草邀请，并把[主题]研究的摘要整理到一个Notion页面。在发送或更改任何内容之前，向我展示会议合并计划和邀请草稿；当Notion页面已经创建且我已批准日历修改时，任务才算完成。
    原始来源：https://medium.com/age-of-awareness/i-let-openclaw-run-my-entire-workday-d4bea6597b1c

<details><summary>English original</summary>

    Handle a client project across Gmail, Calendar and Notion
    The author connected OpenClaw to Gmail, Calendar and Notion; it merged three meetings into one, sent invites, and split a research report across sub-agents.
    Done with
    OC
    OpenClaw
    What they did
    The author connected OpenClaw to Gmail, Google Calendar and Notion, and told it to handle a client project. It sorted the inbox into urgent, review and FYI, with drafts and attachments for urgent mail. It noticed three meetings on one project, merged them and sent invites without asking. For a competitive analysis, it split the work across sub-agents for research, financials, drafting and charts.
    How it went
    The report came back at 42 pages in six hours, versus two days by hand, though the article also says the first message cited 40 pages. The agent once misread a data source and put wrong statistics in a report.
    Worth knowing
    Expect to check everything for about two weeks: the author spent more time on setup and review in week one, broke even in week two, and saw savings in week three.
    Try it yourself
    with
    OpenClaw
    Copy prompt
    Connect to my Gmail, Google Calendar and Notion and help me manage the project for [client name]. Find the overlapping meetings about [project] this week and propose how to merge them, draft the invites, and compile a summary of the research on [topic] into a Notion page. Show me the merged meeting plan and invite drafts before sending or changing anything; you're done when the Notion page exists and I've approved the calendar changes.
    Original source: https://medium.com/age-of-awareness/i-let-openclaw-run-my-entire-workday-d4bea6597b1c

</details>

## 原作者的方法与来源

原文所在Medium本次已有访问阻断，未继续探测；目录转述和目录模板不冒充原作者原文。

[原作者链接](https://medium.com/age-of-awareness/i-let-openclaw-run-my-entire-workday-d4bea6597b1c)

## 简要分析

商业分数未评定。

### 报告长度与耗时不等于正确交付

目录既转述六小时生成42页，也保留首条消息称40页的差异。两天人工是作者对照说法，没有任务难度、净工时或相同质量标准；不能把两天当48个工作小时去算提效倍数。错误统计说明有核查必要，但单次错误也不证明所有报告无用。原始文章、报告和运行日志均未取得。

依据：[Sdirectory](https://agentusecases.ai/use-case/handle-a-client-project-across-gmail-calendar-and-notion)

### 目标是跨工具协调，而非自动发邀请

潜在使用者是同时管理邮件、会议和项目资料的顾问或小团队负责人。痛点可能是重复查找、整理项目上下文和跟进动作。是否有付款意愿取决于这些任务出现的频率及实际净节省；只偶尔写一份报告者未必需要长期维护一个跨应用agent。

依据：[Sdirectory](https://agentusecases.ai/use-case/handle-a-client-project-across-gmail-calendar-and-notion)

### 先读项目上下文，再分别拟定动作

可复制的试点应把邮件分类、会议建议和报告生成拆成独立可核对结果。每条建议保留对应项目和资料出处，重要附件不因“紧急”就自动发送。三个会议名称相似不代表议程、参会人和保密范围相同，不能只看标题就合并。本案未提供判定规则，以上为改进建议。

依据：[Sdirectory](https://agentusecases.ai/use-case/handle-a-client-project-across-gmail-calendar-and-notion)

### 目录故事与Copy prompt采用不同确认方式

故事称未经询问便发送邀请；目录模板则要求先展示计划和草稿，等待批准。不能把后者当作作者已经实施的安全流程，也不能推断作者此前完全没有授权。建议把提案、批准、实际变更和通知结果分开记录，用户能保留原会议而拒绝合并。

依据：[Sdirectory](https://agentusecases.ai/use-case/handle-a-client-project-across-gmail-calendar-and-notion)

### 写入成功、通知发送和参会接受分开

Google文档说明可用固定事件ID减少响应丢失造成的重复创建，并提供通知控制参数。这些能力不证明作者用了相同实现。交付验证应读取实际事件、时间和参与者；收到创建响应不等于所有人已接受邀请。跨应用部分成功时，应显示具体完成和待处理步骤，而不是统一报“完成”。

依据：[Scalendar](https://developers.google.com/workspace/calendar/api/guides/create-events)

### 子agent分工不能替代数据核对

报告中的财务、市场规模和图表要保留来源、日期、单位和计算方法。研究角色与写作角色可能共同沿用同一个错误来源，人数多不自动形成独立验证。可以先交带来源的结构提纲和关键数值表，再生成长稿；对缺证数据留空。本轮未生成或运行该系统。

依据：[Sdirectory](https://agentusecases.ai/use-case/handle-a-client-project-across-gmail-calendar-and-notion)

### 商业化候选是限定项目的流程配置

可能的收入模式是一次性搭建加维护，但本案没有客户合同、售价、续费或实际收入。卖点应限定为可核查的跨工具整理、减少重复操作和恢复能力，而非承诺“全天工作自动托管”。第一批验证宜面向已有明确重复任务的负责人，先比较手工模板和现有工具；本轮没有联系客户。

依据：[Sdirectory](https://agentusecases.ai/use-case/handle-a-client-project-across-gmail-calendar-and-notion)

### 两类交付情景，不补造未知价格

自用情景：净收益需用节省的操作时间，减去设置、复核、返工和维护时间，再考虑API和工具费用。对外服务情景：每客户收入减模型、第三方、交付人工、获客摊销、持续支持与固定成本分摊。作者前三周的说法只表明学习与维护有成本，无法填入以上参数；没有报价或日志，不给虚构利润或预算淘汰线。

依据：[Sdirectory](https://agentusecases.ai/use-case/handle-a-client-project-across-gmail-calendar-and-notion)

### 窄流程可能不需要全能agent

可先使用手工项目模板、邮件分类规则和人工日历协调，比较相同质量下的总投入。这是试验设计，不声称某竞品已等效覆盖全部功能。只有跨工具上下文确实减少重复劳动，且授权与纠错负担可控时，定制集成才有额外价值；模板或单工具已足够时不必加复杂系统。

依据：[Sdirectory](https://agentusecases.ai/use-case/handle-a-client-project-across-gmail-calendar-and-notion)

### 自用人群、频率和维护边界

适合项目事务反复、可明确审批边界且愿意核对结果的知识工作者。潜在收益是减少工具切换，尚未量化。设置需整理项目范围、联系人、日历和页面目标；持续维护包括权限变化、错误来源、重复动作、时区与项目结束后的撤权。邮件附件、参与者和项目报告有隐私风险；错误合并会议或统计比格式问题更严重。

依据：[Sdirectory](https://agentusecases.ai/use-case/handle-a-client-project-across-gmail-calendar-and-notion)

### 用虚构项目先演练部分失败

准备虚构邮件、三场会议和两份相互矛盾的资料，要求只输出分类、会议方案、邀请草稿和带来源摘要，不连接真实账户。检查是否把同名不同客户合并、是否越过批准、是否区分写入与通知、是否识别数据矛盾。再模拟某个工具失败和重复执行，验证能说明状态并避免重复。本轮未实测；若需人工逐项重做才能信任，暂缓自动执行。

依据：[Sdirectory](https://agentusecases.ai/use-case/handle-a-client-project-across-gmail-calendar-and-notion), [Scalendar](https://developers.google.com/workspace/calendar/api/guides/create-events)

## 试用准备与预期结果

虚构邮件、会议、项目资料，不连接私人账号。
可核对的分类、会议方案、邀请草稿与引用摘要；本轮未运行。
只分析我提供的虚构邮件、会议和资料。按项目分类，提出会议合并方案并解释不应合并的项，生成邀请草稿和逐条带来源的研究摘要。标记相互矛盾的数字。不要连接账号、发送邀请、修改日历或创建页面。

## 来源

- [许可目录案例正文](https://agentusecases.ai/use-case/handle-a-client-project-across-gmail-calendar-and-notion)：跨应用操作、42/40页、六小时/两天、错误统计、前三周投入变化均为目录转述。
- [Google Calendar官方事件创建说明](https://developers.google.com/workspace/calendar/api/guides/create-events)：Google Calendar创建事件需具备写访问权限；可自定事件ID帮助避免已成功但响应丢失后的重复创建；sendUpdates控制向相应参与者发送通知。该文档不是案例作者实现证据。
- [原作者Medium文章](https://medium.com/age-of-awareness/i-let-openclaw-run-my-entire-workday-d4bea6597b1c)：未读取原文，使用许可目录转述，不假定作者代码、日志或授权范围。
