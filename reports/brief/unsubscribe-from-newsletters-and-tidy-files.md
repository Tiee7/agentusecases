# 用OpenClaw退订邮件列表并整理文件

## 中文

    退订newsletter并整理文件
    
    一位开发者在一台隔离的笔记本电脑上测试OpenClaw：它处理了847封邮件，退订了203个邮件列表，准确率约90%，漏判了几封客户邮件；它还发送了邀请并重命名文件。
    
    使用的是：
    OC
    OpenClaw
    
    ## 他们做了什么
    
    在一台旧的、隔离的Ubuntu笔记本电脑上，这位开发者将OpenClaw连接到一个存有约2,000封邮件的临时Gmail账户，并让它退订newsletter和促销邮件。它还发送了日历邀请，并将300个不同类型的文件分类、重命名后放入文件夹。他随后抽查了约50封邮件。
    
    ## 进展与成效
    
    它在大约20分钟内处理了847封newsletter邮件，并退订203个邮件列表，准确率约90%。它漏判了一些通过营销平台发送的正常客户邮件。文件重命名表现不错。日历任务在实际上未完全成功时却报告了成功。
    
    ## 值得了解
    
    邮件任务的Claude Sonnet API调用费用约8美元，整周费用47美元，因此应从一开始就为API密钥设置使用限额。”
    
    ## 亲自尝试
    
    使用：OpenClaw
    
    复制提示词：检查我的[邮箱账户]收件箱，找出我在[月数]个月内未打开的newsletter和促销邮件列表。列出准备退订的发件人，绝不要包含[客户、家人或重要发件人]。向我展示完整清单，等待我的批准，再进行任何退订、发送邀请或重命名文件操作；当我批准清单且你向我提供已退订项目报告后，任务才算完成。
    
    原始来源：https://medium.com/@likhitkumarvp/i-spent-47-testing-openclaw-for-a-week-heres-what-s-actually-happening-c274dc26a3fd

<details><summary>English original</summary>

    Unsubscribe from newsletters and tidy files
    A developer tested OpenClaw on an isolated laptop: it processed 847 emails and unsubscribed from 203 lists at about 90% accuracy, missing a few client emails, and also sent invites and renamed files.
    Done with
    OC
    OpenClaw
    What they did
    On an old, isolated Ubuntu laptop, the developer connected OpenClaw to a throwaway Gmail account holding about 2,000 emails and told it to unsubscribe from newsletters and promotions. It also sent calendar invites, and sorted and renamed 300 mixed files into folders. He spot-checked about 50 emails afterward.
    How it went
    It handled 847 newsletter emails in about 20 minutes and unsubscribed from 203 lists, at roughly 90% accuracy. It missed some legitimate client emails sent through a marketing platform. File renaming worked well. The calendar task reported success when it hadn't fully worked.
    Worth knowing
    The email run cost about $8 in Claude Sonnet API calls, and the whole week cost $47, so set usage limits on your API keys from the start.”
    Try it yourself
    with
    OpenClaw
    Copy prompt
    Go through my inbox at [email account] and find newsletters and promotional mailing lists I haven't opened in [number] months. Build a list of the senders you plan to unsubscribe from, and never include anything from [clients, family, or important senders]. Show me the full list and wait for my approval before unsubscribing from anything or sending any invites or renaming files; you're done when I've approved the list and you've given me a report of what was unsubscribed.
    Original source: https://medium.com/@likhitkumarvp/i-spent-47-testing-openclaw-for-a-week-heres-what-s-actually-happening-c274dc26a3fd

</details>

## 原作者的方法与来源

本次浏览器复核受阻；已有历史阅读笔记，但缺可独立核对的原文凭据，不冒充本次原文核验。目录转述另列。

[许可目录转述](https://agentusecases.ai/use-case/unsubscribe-from-newsletters-and-tidy-files)；[原作者链接](https://medium.com/@likhitkumarvp/i-spent-47-testing-openclaw-for-a-week-heres-what-s-actually-happening-c274dc26a3fd)。当前原文复核受阻。

## 简要分析

商业分数未评定；效果和账单均不是本次实测。

### 先分清自述与实测

目录讲述的是隔离Ubuntu笔记本和临时Gmail账户里的个人试验。847是处理邮件数，203是列表数，约50是抽查规模；约90%的准确率没有明确分母、标注方法或混淆矩阵，不能相除重算或外推稳定生产效果。日历误报成功与文件重命名表现是不同子任务，不能合成统一准确率。

依据：[Sdirectory](https://agentusecases.ai/use-case/unsubscribe-from-newsletters-and-tidy-files)

### 需求是减少清理负担，不是多一个聊天入口

潜在人群是订阅积累较多、又愿意审查操作的个人。重要客户也使用营销平台发邮件，因此按“推广邮件”自动处理可能误伤。偶尔整理一次与持续日常处理需求不同；本案没有用户付款或持续复用证据，不能据此推出订阅市场。

依据：[Sdirectory](https://agentusecases.ai/use-case/unsubscribe-from-newsletters-and-tidy-files)

### 候选清单、批准与结果核验分开

拟议交付先生成发件人及理由清单，由用户核对重要联系人，再仅执行获准项目。退订请求被提交与最终不再送达要分别记录；文件整理保留原名映射和恢复方法；日历邀请需要核实具体事件和邀请状态。以上是建议流程，不是原作者已实现能力。

依据：[Sdirectory](https://agentusecases.ai/use-case/unsubscribe-from-newsletters-and-tidy-files), [Sgmail](https://support.google.com/mail/answer/15621070?co=GENIE.Platform%3DDesktop&hl=en-GB)

### 可能收费的是配置与核查服务

商业假设可以是一次性配置、个性化规则及维护，而非承诺无人值守清理所有邮箱。付款人是否愿意为此付费还需验证。先提供不接真实邮箱的示例清单和报价测试，未明确价值前不进行付费投放或替别人托管邮箱。

依据：[Sdirectory](https://agentusecases.ai/use-case/unsubscribe-from-newsletters-and-tidy-files)

### 用明确差异而非笼统自动化获客

可面向已有大量订阅且同时需要文件整理的人展示可审查方案，比较原生工具与定制规则。获客演示应展示误判、人工接管及恢复，不只展示成功动作。尚无客户渠道、转化率或续费数据；本研究没有联系客户。

依据：[Sdirectory](https://agentusecases.ai/use-case/unsubscribe-from-newsletters-and-tidy-files)

### 先比较Gmail原生入口

Google官方已有集中管理订阅入口，但页面注明逐步开放。它允许先查看发件人邮件，相关列表按发件人一起处理；一些操作仍需到发件人网站。若原生工具已满足需求，定制agent的额外安装、费用和权限负担未必划算。

依据：[Sgmail](https://support.google.com/mail/answer/15621070?co=GENIE.Platform%3DDesktop&hl=en-GB)

### 历史账单不能代替交付利润

目录的8美元邮件API费用和47美元整周费用是历史自述，不是当前价格或每客户成本。还需计入设置、审查、返工、维护、第三方工具与获客。下面两种报价情景仅演示敏感性，没有付款和实测依据。

依据：[Sdirectory](https://agentusecases.ai/use-case/unsubscribe-from-newsletters-and-tidy-files)

### 隔离试验不等于可直接接客户邮箱

官方说明一个网关对应一个可信边界。若做多客户服务，应独立设计凭据和数据隔离，不能只用提示词隔开客户。邮件、文件名和日历可能含私人资料；只申请必要权限，外部文本不能成为执行指令。本文未接邮箱或客户资料，文档存在也不代表已完成安全测试。

依据：[Ssecurity](https://docs.openclaw.ai/gateway/security)

### 自用收益取决于复核负担

适合愿意配置工具、明确重要发件人并有重复整理需求的人。预期收益是减少重复操作，但本案无净节时测量。设置涉及账号授权、名单及目录规则，维护包括误判核对、失效链接、接口变化和费用监控；低频用户可能直接手工处理更省事。

依据：[Sdirectory](https://agentusecases.ai/use-case/unsubscribe-from-newsletters-and-tidy-files)

### 先用合成清单验证分类

准备含客户促销平台邮件、账单、家人消息、newsletter、重复列表和模糊标题的合成元数据，只输出候选，不进行退订、邀请或重命名。分别统计重要邮件误判、待人工判断项和核查耗时。若不能解释分类或无法保留恢复路径，停止自动执行，改用只读辅助。未运行该演练，不宣称通过。

依据：[Sdirectory](https://agentusecases.ai/use-case/unsubscribe-from-newsletters-and-tidy-files)

### 单位经济敏感性（全是假设，USD / 每客户一次配置）

|情景|收入|API|第三方|获客|人工|固定摊销|贡献|
|---|---:|---:|---:|---:|---:|---:|---:|
|一次配置假设|80|8|0|10|50|5|7|
|高返工假设|80|16|5|20|100|5|-66|

两项全为报价/用量/工时假设，含25美元小时机会成本和固定费摊销。第三方0是情景假设，不声称软件全部免费。

## 试用准备与预期结果

合成邮件与文件元数据；不接真实账号。
有理由、待批准、可排除的候选清单；本轮未运行。
只分析我给出的合成邮件和文件元数据，输出候选项目、理由、不确定项及重要联系人排除项。不要访问邮箱、退订、发送邀请、修改或重命名文件。

## 来源

- [许可目录案例现场读取](https://agentusecases.ai/use-case/unsubscribe-from-newsletters-and-tidy-files)：隔离设备、临时邮箱、847邮件、203列表、约50抽查、约90%准确率、300文件及历史费用均为目录转述，不是本次实测。
- [Gmail官方订阅管理](https://support.google.com/mail/answer/15621070?co=GENIE.Platform%3DDesktop&hl=en-GB)：Gmail提供集中订阅管理，逐步开放；退订前可查看发件人邮件，相关列表按发件人处理，生效可能需数天，部分需要跳转发件人网站。屏蔽与退订不同。
- [OpenClaw官方安全边界](https://docs.openclaw.ai/gateway/security)：每个网关面向一个可信操作方或相互信任团队，不是敌对多租户安全边界；混合信任需分离网关及凭据。文档提供权限配置和沙箱主题，不证明任何具体部署安全。
- [原作者Medium文章](https://medium.com/@likhitkumarvp/i-spent-47-testing-openclaw-for-a-week-heres-what-s-actually-happening-c274dc26a3fd)：既有研究日志记录08:16公开网页读取；本次云浏览器复核受Cloudflare及安全审批阻止，未重新取得正文。
