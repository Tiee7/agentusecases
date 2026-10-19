# 用 Claude Code 生成跨平台内容草稿并交由本人审批

## 中文

    自动向Reddit和LinkedIn分发内容
    一个Claude Code智能体运行六项云端自动化，把新文章转成Reddit帖子与回复，以及带信息图的LinkedIn帖子；Reddit回复需要Slack批准。
    使用的是
    Claude Code
    他们做了什么
    一个定时Claude Code Routine每六小时在Anthropic云端唤醒，运行到期任务。它从Gmail读取每篇新文章，归入wiki，起草Reddit帖子和回复，并发布LinkedIn文字及图片。草稿发到Slack，由Daria批准、拒绝或重写。每周一，它根据她的修改重写自身指令。
    进展与成效
    系统已运行一个多月，每天完成她此前一直回避的Reddit和LinkedIn工作。它不是完全无人参与，Instagram文案也还没好到可以交出去。
    值得注意
    六项自动化的完整拆解、文件夹结构与注意清单位于付费墙后，因此这份记录只覆盖概览。
    亲自尝试
    使用Claude Code
    复制提示词
    每当我在[博客或RSS链接]发布新文章，为其起草一篇[长度]词的LinkedIn帖子，以及一篇遵守[Reddit社区]规则的简短帖子。将草稿保存到[文件夹或文档]，并在我的[Slack频道]发布摘要供批准。在我逐一批准每篇草稿前，不要在任何地方发布或回复；所有草稿都等待我审阅时就停止。
    原始来源：https://aiblewmymind.substack.com/p/claude-code-content-distribution-ai-agent

<details><summary>English original</summary>

    Automate content distribution across Reddit and LinkedIn
    A Claude Code agent runs six cloud automations that turn new articles into Reddit posts and replies and LinkedIn posts with infographics; Reddit replies need Slack approval.
    Done with
    CC
    Claude Code
    What they did
    A scheduled Claude Code Routine wakes in Anthropic's cloud every six hours and runs whatever task is due. It reads each new article from Gmail, files it into a wiki, drafts Reddit posts and replies, and posts LinkedIn text and images. Drafts go to Slack, where Daria approves, rejects or rewrites them. On Mondays it rewrites its own instructions from her edits.
    How it went
    The system has run for over a month and gets daily Reddit and LinkedIn work done that she had been avoiding. It isn't fully hands-off, and Instagram copy isn't good enough to hand over yet.
    Worth knowing
    The full breakdown of the six automations, folder structure and watch-out checklist is behind the paywall, so this account covers only the overview.
    Try it yourself
    with
    Claude Code
    Copy prompt
    Whenever I publish a new article at [blog or RSS URL], draft a LinkedIn post of [length] words for it, plus a short [Reddit community] post that follows that community's rules. Save the drafts in [folder or doc], and post a summary in my [Slack channel] for approval. Do not publish or reply anywhere until I approve each draft, and stop once all drafts are waiting for my review.
    Original source: https://aiblewmymind.substack.com/p/claude-code-content-distribution-ai-agent

</details>

## 原作者的方法与来源

https://aiblewmymind.substack.com/p/claude-code-content-distribution-ai-agent

Daria describes a cloud routine preparing content for her approval and publishing approved LinkedIn drafts.
Daria描述云端任务准备待审内容，并发布已批准LinkedIn草稿。

Detailed implementation is paywalled; this review uses only the public overview.
详细实现处于付费墙后，本研究只使用公开概览。

## 简要分析

商业分数未评定。

### 概览够判断方向，不能还原六套实现

公开文章介绍运行一个多月、每六小时触发、稿件进入Slack审核以及每周调整指令。这些为作者自述，未见发布日志或独立效果证明。完整自动化、文件结构与检查清单在付费区，本轮止于可读部分，没有购买、登录或绕过。目录日期2026-10-18与原文显示2026-06-11不同，两者保留，不混成同一天发布。缺关键实现细节，交付未评分简报。

依据：[Sauthor](https://aiblewmymind.substack.com/p/claude-code-content-distribution-ai-agent), [Sdirectory](https://agentusecases.ai/use-case/automate-content-distribution-across-reddit-and-linkedin)

### 所有发布都要区分草稿和批准版本

原文明确分发仍由本人把关，不能因目录开头强调Reddit回复批准，就推断LinkedIn无需批准。目录模板也要求所有草稿逐一批准。本研究建议批准记录绑定平台、目标位置、正文图片和版本，批准后改稿需重审；审批一个示例不应放行后来所有内容。这是拟议实现要求，未确认作者是否采用此数据结构。

依据：[Sauthor](https://aiblewmymind.substack.com/p/claude-code-content-distribution-ai-agent), [Sdirectory](https://agentusecases.ai/use-case/automate-content-distribution-across-reddit-and-linkedin)

### 定时触发不等于可靠交付

云端Routine机制可核，但一个任务被唤醒并不证明已发布。候选实现需分待生成、待审、已批准、发送中、已核回执等状态，按文章和平台去重。发送后超时先核回执，不盲目再发；后台任务重入也不能重复领取。作者的锁、状态存储与失败处理细节未知，不能把本研究提出的设计写成其已实现能力。

依据：[Sroutine](https://code.claude.com/docs/en/routines)

### 每周改指令也需要检查

作者称从编辑反馈修改自身指令，这不等于模型权重训练。可取的验证方式是保留旧版本、检查差异并用固定样稿回归；不能让文风学习同时改掉批准要求或目标范围。拒绝一篇稿可能因为时机或主题，不一定是永久文风偏好。没有看到完整反馈归纳规则，不能宣称已经建立稳定自学习闭环。

依据：[Sauthor](https://aiblewmymind.substack.com/p/claude-code-content-distribution-ai-agent)

### 本人批准和平台允许是两件事

Reddit对重复、无关或不受欢迎的推广限制同时适用于人工与自动行为，并非只要手动点批准就没有风险。LinkedIn也限制未获准的网站自动活动；实际连接方式与权限仍待核。另一方面，Reddit官方明确某类违规标签不意味着所有机器人或AI辅助内容都违法规则。研究应核具体社区、用途和发布渠道，既不宣布全盘安全，也不把一切辅助起草说成禁止。

依据：[Sreddit](https://support.reddithelp.com/hc/en-us/articles/360043504051-Spam), [Slinkedin](https://www.linkedin.com/help/linkedin/answer/a1341543), [Srule8](https://support.reddithelp.com/hc/en-us/articles/53416317564820-Changelog-September-10-2026)

### 队列容易买到，文风与复核才是难点

Buffer已有草稿和团队批准排期功能，因此“定时生成再审批”本身不足以形成独立产品优势。潜在增量是基于作者获准内容生成适合不同语境的草稿，仍需测改稿时间。作者没公开新增订阅收入、成交归因或每稿维护成本；不以每天发帖当增长，也不把未来Gumroad产品计划当已实现收入。本例不建立缺乏输入的利润模型。

依据：[Sbuffer](https://buffer.com/publish), [Sauthor](https://aiblewmymind.substack.com/p/claude-code-content-distribution-ai-agent)

### 先用自写文章做无发布测试

准备一篇自写文章和两套虚构社区规则，要求生成两种草稿及各自依据，记录哪些观点来自原文、哪些为改写。故意加入互相冲突的规则、重复输入和批准后改稿情况，预期重复项不增加、改稿回到待审、规则不明不发布。本轮没有执行这些试用，没有读取私人Gmail或Slack，也没有发帖。

依据：[Sdirectory](https://agentusecases.ai/use-case/automate-content-distribution-across-reddit-and-linkedin)

### 下一步只补决定可复制性的证据

如果继续核查，应取得获准公开的状态模型、审批版本绑定、发布接口和失败回执样例，再谈端到端复制。文章付费细节不可读不妨碍形成有限判断，但不应靠通用文档充作原系统源码。若审核时间接近人工写作、重复发布无法可靠阻止或平台不允许相应接入，保留离线草稿辅助并停止扩大自动发布范围。

依据：[Sauthor](https://aiblewmymind.substack.com/p/claude-code-content-distribution-ai-agent), [Sroutine](https://code.claude.com/docs/en/routines)

## 试用准备与预期结果

一篇自写文章、两套虚构规则，无真实社媒账户或私人通信。
可追溯草稿、待审状态、重复检测和版本变化重审。

把这篇自写文章按两套虚构规则分别改写，逐条列观点来源与不确定项。重复输入不新增草稿。每稿待审，修改正文后取消旧批准；不发布、不回复、不联系任何人。

## 来源

- [许可目录概览](https://agentusecases.ai/use-case/automate-content-distribution-across-reddit-and-linkedin)：目录标2026-10-18，保留原文和逐稿批准模板。
- [Daria公开文章部分，页面日期2026-06-11](https://aiblewmymind.substack.com/p/claude-code-content-distribution-ai-agent)：公开概览明确所有内容需本人批准；详细实现位于付费墙后，未访问。
- [Claude Code Routines官方文档](https://code.claude.com/docs/en/routines)：云端调度与连接器范围机制可核，不证明作者系统的配置或实际成功率。
- [Reddit垃圾信息规则](https://support.reddithelp.com/hc/en-us/articles/360043504051-Spam)：人工和自动重复推广均受限制，社区另有规则，审批不等于平台许可。
- [LinkedIn自动活动说明](https://www.linkedin.com/help/linkedin/answer/a1341543)：禁止未获准的网站自动活动，需核实际发布途径，不能凭作者故事判定合规。
- [Buffer草稿与审阅队列](https://buffer.com/publish)：现成排期产品支持草稿及团队审批，通用审批队列并非独有。
- [Reddit 2026-09-10说明](https://support.reddithelp.com/hc/en-us/articles/53416317564820-Changelog-September-10-2026)：平台说明自动账号违规标签不适用于所有机器人或所有AI辅助内容。
