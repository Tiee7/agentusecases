# 用OpenClaw通过WhatsApp管理日历、语音笔记和习惯记录

## 中文

    通过WhatsApp运行个人助手
    作者在一台低价VPS上运行OpenClaw，通过WhatsApp发消息，让它管理日历、浏览网页、回复语音笔记，并把习惯记录写入由Git跟踪的文件。
    使用的是
    OC
    OpenClaw
    他们做了什么
    OpenClaw运行在每月5美元的VPS上的Docker容器中，用无头Chromium浏览网页，网关只能通过SSH隧道访问。作者通过WhatsApp与它通信。它借助gog命令行工具管理Google Calendar和Gmail，把习惯记录到Markdown文件，并用Gemini把语音笔记转成归档的行动项。它把笔记提交到一个私有GitHub仓库。家人被路由到另一个agent。
    进展与成效
    他停用了付费的Notion、Todoist和一款习惯追踪器。agent还通过自己的一个5美元eSIM号码打电话和预订。来源没有给出准确性或可靠性测量。
    值得了解
    OpenClaw在启动时会重写配置并移除WhatsApp白名单，因此他加入了基准配置恢复和看门狗。Docker中的Chromium还需要2GB共享内存。
    亲自尝试
    使用
    OpenClaw
    复制提示词
    设置一个我可以通过[WhatsApp/Telegram]发送消息的个人助手，它能查看和编辑[日历服务]中的日历、浏览网页、转录语音笔记，并把日常习惯（[习惯列表]）记录到位于[路径]的Git仓库中的文本文件。指导我在[VPS/电脑]上完成设置，再让我分别发送每种类型的一条消息进行测试。当所有测试都正常工作时，设置才算完成；向我之外的任何人发送消息或更改任何日历事件之前，先询问我。
    原始来源：https://medium.com/@srechakra/sda-f079871369ae

<details><summary>English original</summary>

    Run a personal assistant over WhatsApp
    The author runs OpenClaw on a cheap VPS, messaging it over WhatsApp to manage his calendar, browse the web, answer voice notes, and log habits to a Git-tracked file.
    Done with
    OC
    OpenClaw
    What they did
    OpenClaw runs in Docker on a $5/month VPS, with headless Chromium for browsing and the gateway reachable only through an SSH tunnel. The author messages it on WhatsApp. It manages Google Calendar and Gmail through the gog CLI, logs habits to markdown files, and turns voice notes into filed action items using Gemini. It commits notes to a private GitHub repo. Family members are routed to a separate agent.
    How it went
    He dropped paid Notion, Todoist and a habit tracker, and the agent also made phone calls and reservations from its own $5 eSIM number. The source gives no accuracy or reliability measurements.
    Worth knowing
    OpenClaw rewrites its config on startup and strips the WhatsApp allowlist, so he added a golden-config restore and a watchdog. Chromium in Docker also needs 2GB of shared memory.
    Try it yourself
    with
    OpenClaw
    Copy prompt
    Set up a personal assistant I can message over [WhatsApp/Telegram] that can check and edit my calendar at [calendar service], browse the web, transcribe voice notes, and log daily habits ([list habits]) to a text file in a Git repo at [path]. Walk me through setup on my [VPS/computer], then test it by having me send one message of each type. Setup is done when each of those tests works; ask before it sends any message to anyone besides me or changes any calendar events.
    Original source: https://medium.com/@srechakra/sda-f079871369ae

</details>

## 原作者的方法与来源

原文位于本次已确认Cloudflare阻断的Medium origin，未继续访问或换路；只保留许可目录转述。

[原始链接](https://medium.com/@srechakra/sda-f079871369ae)

## 简要分析

商业分数未评定。

### 手机入口后面仍是一套需要维护的系统

目录描述的是WhatsApp入口、VPS上的Docker与Chromium、gog日历邮箱、Gemini语音、Markdown习惯记录和私有Git归档。用途横跨多个组件，某个测试成功不能代表所有动作可靠。未取得作者配置和版本，不能把一段模板当成可复制安装包。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-a-personal-assistant-over-whatsapp)

### 取消订阅是个人选择，不是净收益证明

作者说停用了Notion、Todoist和习惯追踪器，但没有原套餐、实际节省金额、缺失功能或持续使用时长。服务可以替代他个人用到的部分功能，不等于完整替代这些产品。电话和预订也是自述，没有对方确认或完整成功率；不把它们当本研究演示。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-a-personal-assistant-over-whatsapp)

### 不要把旧配置问题写成当前普遍行为

目录原文保留“启动重写白名单”的表述，分析需补充边界：相关公开issue讨论2026.5.7与特定包装器组合，已关闭；关闭说明称main已有保护，但没有执行包装器。现有材料不足以证明作者就是该issue场景，也不足以承诺所有发布版已经修好。应固定版本并实测启动、重启、升级后的实际权限，而非默认必须持续覆盖配置。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-a-personal-assistant-over-whatsapp), [Sissue](https://github.com/openclaw/openclaw/issues/79738), [Sclose](https://github.com/openclaw/openclaw/issues/79738#issuecomment-4412129834)

### 入站白名单不是所有动作的总开关

WhatsApp文档区分入站DM政策与显式群组/频道外发；gog又提供只读、命令限制和禁发邮件等不同控制。配置一个允许来信的号码，不能推断它限制了所有外发或日历修改。复制时应分别列出能读、能写、能发的动作，禁止项在工具层落实，不能只写“请先问我”。

依据：[Swhatsapp](https://github.com/openclaw/openclaw/blob/main/docs/channels/whatsapp.md), [Sgog](https://github.com/openclaw/gogcli/blob/main/docs/commands/gog.md)

### 分成两个agent不自动获得严格隔离

家人路由到另一个agent是作者配置自述，尚无会话、目录、账号凭据和日志隔离的测试。家庭成员同意什么数据被处理也需要明确。建议用虚构的两套联系人和笔记验证检索不串、路由正确、撤权立即生效；不需要为研究收集家人实际聊天。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-a-personal-assistant-over-whatsapp)

### 2GB共享内存不等于整机只需2GB

Docker的shm-size与memory是不同配置，浏览器页面数量、模型客户端和其他进程仍影响总资源使用。目录给出的2GB是该方案的说法，不是通用最低硬件标准。应通过实际工作负载测量并关闭不用的标签，而不是仅调大一个参数就宣布解决内存问题。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-a-personal-assistant-over-whatsapp), [Sdocker](https://docs.docker.com/engine/containers/run/)

### 每月5美元只是VPS一项

还要核算模型调用、语音处理、号码及通话、存储备份、维护与故障恢复。目录只写5美元eSIM，未说明计费周期，不擅自算成每月5美元。自用应比较取消订阅后的现金变化与新增维护时间；对外服务还要计入获客、账号接入、客户支持和退出迁移，无法凭VPS价格算毛利。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-a-personal-assistant-over-whatsapp)

### 可验证的商业方向是有限范围配置服务

假设付费人是有高频跨工具事务但不愿自己维护的个人或小团队。收入可探索一次性设置加维护，而非先卖“万能秘书订阅”。获客演示应限定一套合成日历和笔记，展示权限、失败恢复和导出；实际客户是否愿付钱没有证据。跨账号定制与持续支持若无法标准化，会吞掉低价服务的空间。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-a-personal-assistant-over-whatsapp)

### 一套聊天助手不必替代全部工具

可以先保留原日历和任务应用，仅将语音转成待确认的行动项，再比较是否值得接入更广功能。Markdown加Git有可追踪记录的价值，但需要版本、同步和删除政策；私有仓库也不是对数据拥有者自动合规或绝对私密的保证。替代方案按实际必需功能比较，不按功能列表长短决定。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-a-personal-assistant-over-whatsapp)

### 自用价值取决于频率和运维意愿

适合有基本服务器管理能力、经常在手机上记录和协调事务的人。潜在收益是减少工具切换，净时间未测。初期需要接入、路由、权限与备份；后续要处理登录失效、组件升级、配置漂移、误识别和费用。低频用户可能用原生应用更省心，不能把能安装等同于适合长期使用。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-a-personal-assistant-over-whatsapp)

### 先验收只读与重启恢复，再考虑写入

先用虚构邮件标题、日历和习惯记录生成候选操作，不连接真实服务。技术试点若另行开展，应保存版本/权限基线，测试重启与升级后是否保持限制，并核对每个已执行动作的回执与可恢复记录。发现未知外发、越权读取或权限漂移应停止写操作；本轮不运行安装、授权或真实消息测试。

依据：[Sgog](https://github.com/openclaw/gogcli/blob/main/docs/commands/gog.md), [Sissue](https://github.com/openclaw/openclaw/issues/79738)

## 试用准备与预期结果

虚构消息、日历、两名用户的合成笔记，不登录真实账号。
按身份隔离的只读建议、明确待批准项和恢复检查表；本轮未运行。
只处理我提供的合成数据。把语音转写文本整理为行动项，按用户隔离日历和笔记，列出需要批准的动作及对应依据。不要安装软件、接入账号、发消息、改日历或提交Git。输出重启后权限核对清单，标记未知情况。

## 来源

- [许可目录现场正文](https://agentusecases.ai/use-case/run-a-personal-assistant-over-whatsapp)：低价VPS、自托管工具链、取消订阅、eSIM通话、启动配置问题及2GB共享内存均为目录转述，未实测。
- [OpenClaw WhatsApp官方文档](https://github.com/openclaw/openclaw/blob/main/docs/channels/whatsapp.md)：官方支持独立号码及个人号码自聊模式；dmPolicy/allowFrom控制入站，显式群组或频道外发不受同一DM名单直接约束。需要按动作另核授权。
- [gog命令行官方参考](https://github.com/openclaw/gogcli/blob/main/docs/commands/gog.md)：文档分别列出readonly、enable-commands-exact、gmail-no-send；read-only不是仅靠提示词，也不应把只读、草稿与发送权限混为一谈。
- [配置重写问题公开记录](https://github.com/openclaw/openclaw/issues/79738)：问题针对OpenClaw2026.5.7与u4s-openclaw包装器组合，报告重启改写allowFrom等配置。状态closed，关闭日期2026-08-02；不能泛化为所有当前版本必然行为。
- [问题关闭说明](https://github.com/openclaw/openclaw/issues/79738#issuecomment-4412129834)：关闭评论称当前main已保护插件启用的源配置修改和单次启动快照，同时明确未执行包装器。属于维护/自动审查说明，不是本研究独立复现或作者部署已修复证明。
- [Docker官方运行资源约束](https://docs.docker.com/engine/containers/run/)：shm-size设定/dev/shm大小，默认64m；与容器memory内存上限为不同参数。未证明每个Chromium场景均必须2GB或作者VPS容量足够。
- [原作者文章](https://medium.com/@srechakra/sda-f079871369ae)：原文未读；目录转述和试用模板不冒充作者实现。
