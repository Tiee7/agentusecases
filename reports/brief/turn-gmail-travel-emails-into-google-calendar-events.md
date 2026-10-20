# 用Agent将Gmail旅行邮件整理为日历事件

## 中文

    将Gmail旅行邮件转换为Google日历事件
    用户尝试让Manus和ChatGPT Agent读取Gmail中的旅行详情并创建日历事件；Manus很慢，而且两者都失败了。
    使用的是
    Manus
    ChatGPT Agent
    他们做了什么
    发帖者尝试了Manus，也尝试了ChatGPT Agent，来完成一项旅行行政任务：读取Gmail中的预订详情，并将其转换为Google日历事件。他们不得不密切监督整个过程。Manus本应处理Gmail和Google日历的集成，但它太慢且不可靠，因此发帖者放弃了它，手动完成了工作。
    进展与成效
    这个用例没有成功。发帖者说，监督Manus花了约1.5小时，而他们估计手动完成这项工作只需15分钟；Manus和ChatGPT Agent都未能根据Gmail创建旅行事件。他们还补充说，Claude聊天在不到一分钟内成功了。
    值得了解
    主要问题是Gmail和Google日历集成的可靠性：发帖者说，智能体方式带来了负收益，因为监督所花的时间远远超过直接完成任务。
    亲自尝试
    使用
    Manus
    复制提示词
    搜索我的Gmail，查找[航空公司、酒店或铁路公司]发来的、涉及[行程或日期范围]的旅行确认邮件。对每项预订，提取日期、时间、确认号和地点，然后起草Google日历事件，并把这些详情放在描述里。向我展示你打算创建的事件列表，在保存任何事件之前等待我的批准。
    原始来源：https://www.reddit.com/r/ChatGPT/comments/1ry946y/manus_review_for_a_task_chatgpt_agent_couldnt

<details><summary>English original</summary>

    Turn Gmail travel emails into Google Calendar events
    User tried Manus and ChatGPT Agent to read Gmail travel details and create a calendar event; Manus was slow and both failed.
    Done with
    MA
    Manus
    GA
    ChatGPT Agent
    What they did
    The poster tried Manus, and also ChatGPT Agent, on a travel-admin task: read booking details from Gmail and turn them into a Google Calendar event. They had to supervise the process heavily, and Manus was supposed to handle the Gmail and Google Calendar integrations but was so slow and unreliable that the poster abandoned it and finished the work manually.
    How it went
    It did not work for this use case. The poster says supervising Manus took about 1.5 hours for work they estimate would take 15 minutes by hand, and both Manus and ChatGPT Agent failed to create the travel event from Gmail; they add that Claude chat succeeded in under a minute.
    Worth knowing
    The main catch was reliability of the Gmail and Google Calendar integrations: the poster says the agentic route became a net negative because oversight took far longer than doing it directly.
    Try it yourself
    with
    Manus
    Copy prompt
    Search my Gmail for travel confirmation emails from [airline, hotel, or train company] for [trip or date range]. For each booking, pull the dates, times, confirmation number, and location, then draft a Google Calendar event with those details in the description. Show me the list of events you plan to create and wait for my approval before saving any of them.
    Original source: https://www.reddit.com/r/ChatGPT/comments/1ry946y/manus_review_for_a_task_chatgpt_agent_couldnt

</details>

## 原作者的方法与来源

原帖位于此前明确受限Reddit，本轮不重试或绕过。未读取私人邮件、账户、日历、执行日志或Claude输出。

[原始链接](https://www.reddit.com/r/ChatGPT/comments/1ry946y/manus_review_for_a_task_chatgpt_agent_couldnt)

## 简要分析

商业分数未评定。

### 失败是工作流线索，不是模型排行榜

目录记录的是一次作者体验，没有相同邮件、账户、权限、提示词和输出验收。Claude聊天“成功”究竟指提取文本、生成文件还是实际写入日历未知；不能与两种agent的端到端写入直接比较。15分钟是作者估计而非配对计时，监督1.5小时也缺具体失败阶段。

依据：[Sdirectory](https://agentusecases.ai/use-case/turn-gmail-travel-emails-into-google-calendar-events)

### 先用现成功能建立基线

Google已有旅行确认邮件生成日历事件并随预订变化更新的功能，但需检查智能功能及事件设置。抄送、邮件列表、跨账户转来的邮件等有限制。本案是否符合条件未知；应先检查是否已有事件，避免agent再创建一份。未启用不代表系统不能做，已启用也不保证每封邮件都支持。

依据：[Snative](https://support.google.com/calendar/answer/6084018?co=GENIE.Platform%3DDesktop&hl=en)

### 把提取、批准和写入拆开

先限定日期范围与发件方，只提取本次旅行相关资料，输出每项来源和不确定字段。用户核对后才创建，不擅自邀请他人或发送通知。写入后应读取事件ID和实际字段核对，网络超时先查是否已经成功，再决定重试。提供可追溯ID不等于完整解决同一订单不同邮件的语义去重。

依据：[Sdirectory](https://agentusecases.ai/use-case/turn-gmail-travel-emails-into-google-calendar-events), [Screate](https://developers.google.com/workspace/calendar/api/guides/create-events)

### 跨时区和跨日需要逐字段核对

拟议验收应覆盖出发与到达时区不同、过午夜、夏令时转换、酒店入住退房日期以及缺失结束时间。不能把邮件显示时区默认当机场当地时区，也不要凭空补抵达时间。全天与定时事件分开处理；不确定时先标待确认，不用一个看似完整的事件掩盖未知。

依据：[Sevent](https://developers.google.com/workspace/calendar/api/v3/reference/events)

### 商业缺口是异常处理而非普通转录

假设人群是经常出差或管理复杂行程的人，但本案没有用户规模和付费证据。候选服务应先验证原生功能没覆盖的转发、多来源、改签冲突等问题，交付待审行程和核对记录。可以探索按行程整理收费或持续维护，但获客、支付意愿和稳定交付均待验证，不能靠“AI日历”标签推定需求。

依据：[Snative](https://support.google.com/calendar/answer/6084018?co=GENIE.Platform%3DDesktop&hl=en), [Sdirectory](https://agentusecases.ai/use-case/turn-gmail-travel-emails-into-google-calendar-events)

### 监督时间可能吃掉便利

成本包括设置、授权、筛选、核对时区、处理重复与改签、等待和返工。没有调用账单、模型版本和真实人工基线，不计算利润或节约率。自用是否划算需比较全部时间与错误代价，不只统计生成文字速度。低频旅行者可能用原生事件加人工更省事。

依据：[Sdirectory](https://agentusecases.ai/use-case/turn-gmail-travel-emails-into-google-calendar-events)

### 自用价值与维护分开判断

适合有重复旅行整理需求且愿意审核的人。设置需要限定邮箱范围与目标日历；维护包括连接器权限、邮件格式、改签与取消同步。频率按真实出行而非假设每天。可能收益是减少抄写，但漏航班或错误提醒损失较大，不能把一封成功处理当长期可靠。

依据：[Sdirectory](https://agentusecases.ai/use-case/turn-gmail-travel-emails-into-google-calendar-events), [Snative](https://support.google.com/calendar/answer/6084018?co=GENIE.Platform%3DDesktop&hl=en)

### 确认号和行程不应默认公开

邮件可能包含姓名、确认号、住址、同行人及个人行踪。最小化读取并核对目标日历可见性，描述中只保留必要内容，不默认把邮件全文复制进去。API受邀人和通知字段可能把行程发给第三方，必须单独确认；本轮没有访问邮箱或修改任何日历。

依据：[Sdirectory](https://agentusecases.ai/use-case/turn-gmail-travel-emails-into-google-calendar-events), [Screate](https://developers.google.com/workspace/calendar/api/guides/create-events)

### 先离线做合成样例

准备虚构航班、酒店、改签、取消、重复邮件和缺失时区样例，预先列正确日期与是否创建。只输出草稿清单和待确认项，检查重复、更新与删除建议，不执行真实写入。预期结果是来源对应、未知不补造、变更可审核；本轮未进行此试验。

依据：[Sdirectory](https://agentusecases.ai/use-case/turn-gmail-travel-emails-into-google-calendar-events), [Sevent](https://developers.google.com/workspace/calendar/api/v3/reference/events)

## 试用准备与预期结果

虚构旅行邮件与预期结果表，不接真实邮箱日历。
待审事件清单、来源、时区和未知字段，不保存、不通知；未实测。
仅从以下虚构旅行邮件提取事件草稿。标注来源、起止日期时区、重复与改签关系；缺失信息写待确认。不访问账户、不保存日历、不发送邀请。

## 来源

- [许可目录现场正文](https://agentusecases.ai/use-case/turn-gmail-travel-emails-into-google-calendar-events)：许可目录转述两种agent失败、Manus监督约1.5小时对比估计手动15分钟，以及Claude聊天不到一分钟成功的自述，未提供同条件结果。
- [Google日历：Gmail事件](https://support.google.com/calendar/answer/6084018?co=GENIE.Platform%3DDesktop&hl=en)：官方支持从旅行确认邮件自动生成事件并随预订变化更新；受设置、账户和邮件类型限制，抄送、邮件列表及转自其他账户的邮件等不适用。
- [Google Calendar创建事件指南](https://developers.google.com/workspace/calendar/api/guides/create-events)：官方要求目标日历写权限，支持调用方生成符合规则的事件ID，避免后端已成功而客户端失败后的重复创建；添加受邀人并发送更新会产生通知。
- [Google Calendar事件字段](https://developers.google.com/workspace/calendar/api/v3/reference/events)：事件开始和结束分别有日期、带偏移的日期时间和时区字段，定时与全天事件需区分。
- [原作者文章](https://www.reddit.com/r/ChatGPT/comments/1ry946y/manus_review_for_a_task_chatgpt_agent_couldnt)：原文未读；目录转述和试用模板不冒充作者实现。
