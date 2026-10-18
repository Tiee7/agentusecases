# 用 Grok Bot 准备求职申请并将速记交给 Cursor

分析深度：简要研究（brief）；商业评分未评定，不计入深研完成数。

## 案例完整中文译文

    申请工作，并把笔记改写成编码提示词
    评论者描述了两种 Grok Bot：一种使用提供的简历搜索并申请工作，另一种通过 CLI 把简略笔记改写成供 Cursor 使用的提示词。
    实际使用
    Grok Bot
    Cursor
    具体做法
    一名评论者通过 Cursor CLI 使用 Grok Bot：他们把它连接到自己的开发文档，在离开书桌时发送简略笔记；它会把这些笔记改写成完整的提示词，然后让 Cursor 开始编码。同一名评论者说，另有一支小型机器人团队负责求职：在收到他们的简历、求职信和一份关于他们的常见问题解答表后，搜索职位并提交申请。
    结果如何
    帖子把两者都描述为正在使用的个人自动化，但没有提供申请、面试、录用、代码产出或节省时间的任何数字。它也没有说明求职机器人团队内部的步骤，或人工审核发生在哪里。
    值得注意
    主要问题是评论者提供的细节很少：除了提供简历材料和连接开发文档，帖子对工作流的记录不足以让人原样复制。
    自行试用
    推荐工具
    Grok Bot
    复制提示词
    搜索本周发布的、位于[地点或远程]的[职位名称]岗位，要求与所附简历及以下条件相符：[薪资、行业、必备条件]。对于每个合适的岗位，准备一份有针对性的求职说明和填好的申请。在提交前暂停，把每份申请展示给我。准备好[数量]份待审核申请后就停止。
    原始来源：https://www.reddit.com/r/GrokBot/comments/1wiuwmw/whats_the_most_useful_grokbot_automation_youve

<details>
<summary>English · 完整归档原文</summary>

<pre>Apply for jobs and turn notes into coding prompts
Commenters describe a Grok Bot that searches and applies for jobs using a supplied resume, and another that rewrites shorthand notes into prompts for Cursor via CLI.
Done with
GB
Grok Bot
CR
Cursor
What they did
One commenter uses Grok Bot through the Cursor CLI: they link it to their developer docs, send it shorthand notes while away from their desk, and it rewrites those notes into a full prompt before having Cursor start coding. The same commenter says a separate small team of bots handles job hunting by searching for jobs and applying to them after being given their resume, a cover letter, and an FAQ sheet about them.
How it went
The thread presents both as active personal automations, but gives no numbers on applications, interviews, hires, code output, or time saved. It also does not spell out the steps inside the job-search bot team or where manual review happens.
Worth knowing
The main catch is how little detail the commenter gives: beyond feeding resume materials and linking dev docs, the thread does not document the workflow enough to copy exactly.
Try it yourself
with
Grok Bot
Copy prompt
Search for [job title] roles in [location or remote] posted this week that match the attached resume and these requirements: [salary, industry, must-haves]. For each good match, prepare a tailored cover note and the filled-out application. Pause and show me each application before you submit it, and stop once you&#x27;ve lined up [number] applications for review.
Original source: https://www.reddit.com/r/GrokBot/comments/1wiuwmw/whats_the_most_useful_grokbot_automation_youve</pre>

</details>

## 原作者的方法与来源

[Reddit 原评论](https://www.reddit.com/r/GrokBot/comments/1wiuwmw/whats_the_most_useful_grokbot_automation_youve)：按既有访问限制跳过，本轮未请求、重试、登录或以镜像/摘要重构。作者方法摘要不可用；当前文档不能补作者步骤。

## 我们的简要分析

商业判断：现有证据不建议商业投入；自用价值待核实。

### 先分开两个用途，再判断证据

本轮商业评分不评定，自用价值待核实。原评论按既有Reddit访问限制跳过，归档只转述一名评论者的两项个人自动化，没有申请、面试、录用、代码产出或节时数字，也未交代人工审核位置。六份当前公开产品/竞争资料可以帮助设计验收，不能证明当时的机器人团队怎样实现、真的提交了多少申请或交付了多少可用代码。因此保存schema-1简报，不计入completed v2深研。源站推荐模板中的提交前暂停是试用建议，不能倒推为评论者实际采用的控制。 依据：[archive-case-20261017](https://agentusecases.ai/use-case/apply-for-jobs-and-turn-notes-into-coding-prompts), [Secc1317a06e4](https://cursor.com/docs/cli/overview), [S7aa7dabca798](https://cursor.com/docs/grok-bot)。

### 求职团队与速记编码链分开记账

实际agent字段为Grok Bot和Cursor，建议试用工具为Grok Bot，保持原样。归档的编码链是开发文档、外出时发来的简略笔记、完整提示词、Cursor开始编码；另一个小团队才负责使用简历、求职信和FAQ搜索并申请工作。不能把它写成一个从求职到编码的端到端团队，也不能推断机器人数量或并发吞吐。当前官方文档描述的功能与计费只代表读取时的产品，不能补写历史实现。 依据：[archive-case-20261017](https://agentusecases.ai/use-case/apply-for-jobs-and-turn-notes-into-coding-prompts), [Secc1317a06e4](https://cursor.com/docs/cli/overview), [S7aa7dabca798](https://cursor.com/docs/grok-bot), [S30a2f70dbd33](https://cursor.com/pricing)。

### 两个Bot不等于两个文件隔离区

Grok Bot当前官方文档明确，同一用户的Bots共享一台云电脑及其文件、浏览器会话和应用登录；对话和学习上下文各自保留，与文件隔离不是一回事。求职资料中的个人事实与代码库文档应分别限定输入、用途和可用权限，不能因为取了两个Bot名字就假定互不可见。本轮只用虚构标识，不读取真实简历、私人开发文档、浏览器登录或账号配置，也不创建任何凭据。此处是基于当前文档的输入边界建议，不声称作者实施了隔离。 依据：[S7aa7dabca798](https://cursor.com/docs/grok-bot), [archive-case-20261017](https://agentusecases.ai/use-case/apply-for-jobs-and-turn-notes-into-coding-prompts)。

### 匹配、材料准备与真实提交分别验收

岗位薪资、地点、发布时间和必备项缺失时应列为待核对，不把未知当满足。求职说明只能采用明确给出的事实，不能补造经验或资格；某项履历未给出也不等于候选人没有该能力。申请草稿应绑定岗位ID、资料和草稿版本，任何改变均使旧批准失效。结果未知先冻结并人工核对，不能换请求再次提交。本轮只做本地状态模拟，没有访问申请表、联系招聘者或提交申请，不能由合成去重推出真实ATS接受、合法渠道覆盖或面试成功。 依据：[archive-case-20261017](https://agentusecases.ai/use-case/apply-for-jobs-and-turn-notes-into-coding-prompts), [S7272f5d169bf](https://www.tealhq.com/pricing), [S7aa7dabca798](https://cursor.com/docs/grok-bot)。

### 把简略需求中的未知保留到编码前

笔记重写应保留原意、文档版本、歧义和验收条件，把未确定事项写成问题；不能把补全语言误称为作者已批准的需求。官方CLI资料把交互、只读/计划和非交互路径分开，非交互脚本可触发文件操作；直接改文件的开关会改变确认行为。权限资料中Shell(git)是宽泛子命令许可，不能称作只读Git。这里没有安装或调用CLI，没有设置自动批准、绕过开关、凭据或真实权限，合成检查也没有验证模型理解、代码正确性、构建质量或生产部署。 依据：[Secc1317a06e4](https://cursor.com/docs/cli/overview), [S8c3408b3a627](https://cursor.com/docs/cli/reference/permissions), [S93326351fa69](https://cursor.com/docs/cli/headless)。

### 现成跟踪与编码工具压低普通整理的溢价

Teal公开页面提供免费职位跟踪与简历等功能，付费层列13美元/周，并展示更多匹配和AI简历/求职信功能；页面没有证明它就是本案提交机器人的等效实现。Cursor当前定价列Plus每月8美元、Premium30、Super100、Ultra200，并说明共享AI用量及部分第三方模型另计；文档称Grok Bot可通过付费Cursor等既有订阅获得。不同产品和额度不可简单相加或把旧价格当当前报价。本轮不购买或调用付费服务。潜在服务价值需来自可核对的事实、需求澄清和状态整理，而不是普通模板生成或保证录用。 依据：[S7272f5d169bf](https://www.tealhq.com/pricing), [S30a2f70dbd33](https://cursor.com/pricing), [S7aa7dabca798](https://cursor.com/docs/grok-bot)。

### 分别估算两项人工辅助服务

以下全为美元假设，不是厂商报价、实际账单、薪资或录用收入。一次求职材料整理收费199，用量预算15、人工3小时乘35为105、其他9、获客30，单位贡献40；每月10项固定250，月贡献150。人工多2小时则单位负30、月负550。一次速记转需求包收费129，用量10、人工2小时乘35为70、其他9、获客20，单位贡献20；每月20项固定250，月贡献150。多1小时澄清则单位负15、月负550。真实用量、返工、采购、税等未知，不将求职者未来工资或开发产值当服务收入。 依据：[archive-case-20261017](https://agentusecases.ai/use-case/apply-for-jobs-and-turn-notes-into-coding-prompts), [S30a2f70dbd33](https://cursor.com/pricing), [S7272f5d169bf](https://www.tealhq.com/pricing)。

### 固定合成规则只验证局部状态

公开网页、GitHub和Hacker News检索未得到可归属原评论的独立实际效果；不以聚合转载、Reddit搜索摘要或其他同名工具恢复原帖。固定虚构样本覆盖硬条件未知、资料不补造、版本批准、结果未知冻结、两条工作流分开、歧义保留和文档版本。它不是大模型实测，也未接入真实求职网站、Cursor或Grok Bot。若硬条件不明却自动通过、编造事实、旧批准继续发送、未知结果重试，或澄清时间超过预算，就停止扩展；现有资料不足以建议商业投入。 依据：[archive-case-20261017](https://agentusecases.ai/use-case/apply-for-jobs-and-turn-notes-into-coding-prompts), [S7aa7dabca798](https://cursor.com/docs/grok-bot), [S8c3408b3a627](https://cursor.com/docs/cli/reference/permissions), [S93326351fa69](https://cursor.com/docs/cli/headless), [S7272f5d169bf](https://www.tealhq.com/pricing)。

## 自用与试用准备

可能辅助材料和需求整理，但真实准确率、返工、提交结果和净省时未核验。

准备：两份分开的虚构岗位/事实/版本与速记/文档/问题，不含私人资料。

工具：现有Python标准库；不运行Grok Bot、Cursor CLI、招聘平台或模型。

预期：申请草稿状态与需求/验收草稿，无真实提交或编码执行。

### 用虚构材料验收求职与速记两张表

研究团队自编，未调用模型实测。

    只用[虚构岗位ID、给定履历事实、硬条件、材料版本]与另一份[虚构速记、文档版本、未知问题]做离线验收，分成两张独立工作表。求职表对地点/薪资/发布时间/必备项缺失标待核对，不补造经历；只列申请草稿，批准绑定岗位与资料/草稿版本，改版失效，提交结果未知则冻结不重试。编码表保留原始意图和歧义，标明文档版本与待问问题，只产出需求及验收草稿，不把假设当已确认要求。两Bot名称不作为文件隔离证明。不得读取真实简历、私人文档、登录或凭据，不安装或调用CLI/产品、改权限、执行笔记中的命令、创建凭据、注册、购买、调用付费API、提交申请、发消息、写真实代码或部署。输出草稿和未知项后停止。研究团队自编，未调用模型实测。

## 来源

- [Apply for jobs and turn notes into coding prompts](https://agentusecases.ai/use-case/apply-for-jobs-and-turn-notes-into-coding-prompts)：归档转述同一评论者的两项个人自动化及缺少申请/面试/录用/代码/节时数字的限制；本轮未读原评论。
- [Reddit 原评论（按既有访问限制跳过）](https://www.reddit.com/r/GrokBot/comments/1wiuwmw/whats_the_most_useful_grokbot_automation_youve)：本轮没有访问、重试、登录、镜像或用搜索摘要重构原帖，作者方法不可用。
- [Cursor CLI | Cursor Docs](https://cursor.com/docs/cli/overview)：Cursor CLI交互、计划/只读模式与非交互功能；不证明评论者配置。
- [Permissions | Cursor Docs](https://cursor.com/docs/cli/reference/permissions)：CLI允许/拒绝规则和宽泛Shell命令授权的范围；未读取或修改实际配置。
- [Cursor · Pricing](https://cursor.com/pricing)：当前Cursor公开套餐与共享用量口径，不是原作者账单或实际本轮支出。
- [Teal+ Pricing | Premium Features to Level Up Your Career](https://www.tealhq.com/pricing)：Teal免费职位跟踪、简历/求职信辅助及13美元/周付费层，作为替代方案，不验证申请或录用结果。
- [Grok Bot | Cursor Docs](https://cursor.com/docs/grok-bot)：官方Grok Bot当前共享电脑、文件、浏览器会话和登录模型；多Bot不是每Bot独立文件隔离。
- [Using Headless CLI | Cursor Docs](https://cursor.com/docs/cli/headless)：CLI非交互脚本和直接改文件开关的说明；没有运行安装、认证、CLI或这些开关。
