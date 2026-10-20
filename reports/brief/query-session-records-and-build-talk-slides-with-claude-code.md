# 用Claude Code查询会话统计并制作演讲幻灯片

## 中文

    用Claude Code查询会话记录并制作演讲幻灯片
    一位计算机科学教师用Claude Code查询记录下来的会话数据库，获取提交统计和时间线，并为一次教师演讲制作幻灯片。
    使用的是
    CC
    Claude Code
    他们做了什么
    Geoffrey Challen事先构建了Claude Recorder，把自己的Claude Code会话记录到本地SQLite数据库，包含时间戳、工具使用和词元数量。为准备教师研讨会演讲，他让Claude Code查询数据库，提取统计数据和提交时间线。随后它设计了包含交互时间线的reveal.js幻灯片，做成一个独立HTML文件。它还用WhisperX转录他的练习录音，并起草书面摘要。
    进展与成效
    统计覆盖一个17小时的工作日：903条提示、63次提交，以及约16,000行新增代码。Claude制作了幻灯片和文字稿。来源没有描述制作幻灯片本身出现的失败。
    值得了解
    会话数据来自他事先构建的自定义记录器。那一天的用量若按API计费，大约需要1,000美元，但他使用的是每月200美元的Max套餐。
    亲自尝试
    使用
    Claude Code
    复制提示词
    我在[数据库路径]有一个记录工作会话的数据库。先探索它的结构，再回答这些问题：[例如每周提交次数、项目时间线、最大的变更]。随后根据这些发现，为面向[听众]、主题为[主题]、时长[分钟数]分钟的演讲制作一套幻灯片。完成标准是：我拿到这些数字及其计算方法说明，并得到一个能打开的幻灯片文件。不要修改数据库。
    原始来源：https://www.geoffreychallen.com/talks/2026-01-15-a-day-with-claude-using-and-teaching-coding-agents

<details><summary>English original</summary>

    Query session records and build talk slides with Claude Code
    A CS instructor used Claude Code to query his recorded session database for commit stats and timelines and to build slides for a faculty talk.
    Done with
    CC
    Claude Code
    What they did
    Geoffrey Challen had built Claude Recorder, a tool that logs his Claude Code sessions to a local SQLite database with timestamps, tool use and token counts. For his faculty retreat talk, he had Claude Code query that database for stats and commit timelines. It then designed the reveal.js slides, including an interactive timeline, as one standalone HTML file. It also transcribed his practice recordings with WhisperX and drafted the written summary.
    How it went
    The stats covered one 17-hour day: 903 prompts, 63 commits, and about 16,000 lines added. Claude produced the slides and the write-up. The source doesn't describe any failures in the slide-building itself.
    Worth knowing
    The session data comes from a custom recorder he built beforehand. The day's API usage would have cost about $1,000, but he's on the $200 per month Max plan.
    Try it yourself
    with
    Claude Code
    Copy prompt
    I have a database of recorded work sessions at [path to database]. Explore its structure, then answer these questions: [e.g. commit counts per week, a timeline of the project, the biggest changes]. Then build a slide deck for a [length]-minute talk to [audience] on [topic] using those findings. You're done when I have the numbers with a note on how you computed them, plus a slide file I can open. Don't modify the database.
    Original source: https://www.geoffreychallen.com/talks/2026-01-15-a-day-with-claude-using-and-teaching-coding-agents

</details>

## 原作者的方法与来源

https://www.geoffreychallen.com/talks/2026-01-15-illinois-faculty-retreat-day-of-claude/slides.html

作者在公开HTML演讲中展示自录工作统计和项目时间线。
The author presents self-recorded work statistics and project timelines in a public HTML slide deck.

演讲实物可见，底层记录与生产率提升因果尚未独立核验。
The artifact is observable, while underlying records and causal productivity gains were not independently checked.

## 简要分析

商业分数未评定。

### 公开幻灯片可见，底层数字仍属作者报告

作者公开HTML实物已读取，并在云浏览器打开封面及下一页。它支持确有可浏览演讲产物；底层SQLite、日志与Git提交没有独立审计。903提示、63提交和新增行数不能换算为完成业务价值、节省工时或教学效果。未描述幻灯片制作失败也不意味着全流程零失败。

依据：[Sdirectory](https://agentusecases.ai/use-case/query-session-records-and-build-talk-slides-with-claude-code), [Sslides](https://www.geoffreychallen.com/talks/2026-01-15-illinois-faculty-retreat-day-of-claude/slides.html)

### 把散落工作证据转为可讲述材料

推断需求是教师或工程负责人在准备汇报时，不想凭记忆整理一段工作的过程。记录器先积累结构化数据，agent再做查询与叙事，价值在于可追溯的统计和可理解的时间线。没有历史记录的用户无法仅用一句提示复现，应先明确数据是否存在、覆盖哪些项目与时间。

依据：[Sdirectory](https://agentusecases.ai/use-case/query-session-records-and-build-talk-slides-with-claude-code)

### 统计口径比数字大小重要

拟议复现必须定义日期边界、时区、会话去重、合并提交、生成文件与删除行的口径。17小时是报告中的时间范围，不自动代表连续有效劳动；新增行数也可能包含重复或生成内容。作者两项目26加37等于63，只是内部算术一致，不能代替逐条核验。最好给每项数字附查询方法与异常处理说明。

依据：[Sdirectory](https://agentusecases.ai/use-case/query-session-records-and-build-talk-slides-with-claude-code), [Sslides](https://www.geoffreychallen.com/talks/2026-01-15-illinois-faculty-retreat-day-of-claude/slides.html)

### 数据库分析、幻灯片与练习转录分开验收

目录所述原始agent是Claude Code，前置是Claude Recorder/SQLite，输出用reveal.js，练习录音用WhisperX。应分别检查聚合数字、图表叙事、页面呈现与转录校对。能生成HTML并不说明每个图准确，转录顺畅也不证明讲话内容正确。本轮没有使用WhisperX、读取录音或重建原作者系统。

依据：[Sdirectory](https://agentusecases.ai/use-case/query-session-records-and-build-talk-slides-with-claude-code)

### 用实际只读边界保护数据

原模板明确不要修改数据库。SQLite提供只读连接方式，但仍要确认连接实现识别URI参数；只在提示词里写只读不是完整控制。若数据持续变化，不能把immutable当通用加速开关。拟议流程只使用用户提供且获准的稳定脱敏副本，限制查询与导出；本轮不读取任何私人会话数据库或受限日志目录。

依据：[Ssqlite](https://sqlite.org/uri.html), [Sdirectory](https://agentusecases.ai/use-case/query-session-records-and-build-talk-slides-with-claude-code)

### 演讲文件需要浏览与脱网条件说明

作者实物是公开网页，可浏览的事实已经验证，所有依赖是否完全内嵌和离线可用没有独立测试。交付时应说明所需浏览器、字体与资源、打印或PDF替代、时间线标签与无障碍阅读方式。reveal.js基础文件可直接打开，但外部Markdown等功能可能需要服务，不能把一种部署方式概括为所有演讲文件都通用。

依据：[Sreveal](https://revealjs.com/installation/), [Sslides](https://www.geoffreychallen.com/talks/2026-01-15-illinois-faculty-retreat-day-of-claude/slides.html)

### 收费候选是证据整理与汇报质量

可以假设为已有日志的团队提供周期汇报或定制演讲制作，按数据接入、统计核验和制作范围收费。但本案是教师自用，没有外部客户、订单或付费意愿。若只提供漂亮模板，已有办公工具与人工导出是替代；若卖可靠证据链，需要更严格的权限、查询审计与人工签核，本案未证明商业交付成熟。

依据：[Sdirectory](https://agentusecases.ai/use-case/query-session-records-and-build-talk-slides-with-claude-code)

### 历史API等价数不能当现金节省

约1,000美元是那天用量的API等价估算，200美元是当时作者月订阅陈述，不是本轮核验的当前报价或真实日成本。不能直接相减得出一天省800美元，也不能按月无限外推。实际成本还包括记录器开发、存储、资料脱敏、查询复核、演讲修订与转录；当前套餐、用量限制和净省时均未知。

依据：[Sdirectory](https://agentusecases.ai/use-case/query-session-records-and-build-talk-slides-with-claude-code)

### 适用人群、维护与隐私单列

适合已经有可授权工作记录、需定期复盘或演讲的人。实际收益仅确认作者产物存在，节省未测量。设置需要字段字典、时间范围、统计规则和脱敏；维护要跟进记录器版本、缺失会话及异常值。频率可按演讲或复盘周期。会话可能含私人通信、学生资料和凭据，不能把全部原文导入公开幻灯片；错误汇总也可能误导评价个人工作。

依据：[Sdirectory](https://agentusecases.ai/use-case/query-session-records-and-build-talk-slides-with-claude-code), [Ssqlite](https://sqlite.org/uri.html)

### 用合成会话表验证计数与页面

拟议演练只使用虚构的少量会话和提交记录，刻意加入重复提交、跨午夜及缺字段。预期得到查询口径、去重结果和简单时间线，并验证输入未被改写。此演练尚未执行，当前只核对作者公开产物。若合成数据尚算不准或输出暴露不需展示字段，应先修统计与导出规则，而不是接真实私人日志。

依据：[Ssqlite](https://sqlite.org/uri.html), [Sreveal](https://revealjs.com/installation/)

## 试用准备与预期结果

虚构会话及提交小表、预期计数和时间口径。
可复核聚合与时间线，输入不变；合成演练未运行。
只使用提供的虚构会话和提交表，明确日期时区，去除重复，列出缺失项和计算方法，输出简单演讲时间线。不要修改输入、读取其他会话目录或包含个人通信。

## 来源

- [许可目录案例](https://agentusecases.ai/use-case/query-session-records-and-build-talk-slides-with-claude-code)：自定义SQLite记录器是前置；统计、幻灯片、转录和摘要的链路来自作者转述，历史API等价费用不是本轮账单。
- [作者公开演讲幻灯片](https://www.geoffreychallen.com/talks/2026-01-15-illinois-faculty-retreat-day-of-claude/slides.html)：作者2026-01-15公开幻灯片：前一天903提示、17小时、63提交，16266新增及5801删除；两个项目分别26和37提交。公开HTML首页及下一页实际可浏览。底层记录未核，公开实物不等于指标独立审计；不复制其会话或学生引文。
- [SQLite URI只读说明](https://sqlite.org/uri.html)：支持URI的连接可用mode=ro打开只读；immutable会跳过锁与变更检查，不能用于仍在变化的文件。
- [reveal.js安装与运行方式](https://revealjs.com/installation/)：基础方案可浏览器打开，无需构建；外部Markdown等功能需要服务器，HTML文件不自动等于离线自包含。
- [作者演讲摘要的检索版本](https://www.geoffreychallen.com/talks/2026-01-15-a-day-with-claude-using-and-teaching-coding-agents)：成功搜索返回摘要正文；未另行打开该www规范页。非www变体普通读取失败两次后停止，不将检索副本记为现场完整读取。
