# 用Claude电脑操作起草并发送邮件和消息

## 中文

    让Claude操控电脑发送电子邮件和iMessage
    一位作者让Claude电脑操作功能控制电脑三个小时；它打开Outlook撰写并发送邮件，还找到一个iMessage对话给朋友发消息。
    使用的是
    Claude电脑操作
    他们做了什么
    Claude CoWork的Outlook连接器需要IT批准，而iMessage集成此前失败，所以作者改为开启电脑操作功能。设置分五步，包括Chrome扩展、屏幕录制和辅助功能设置。随后Claude打开Outlook桌面应用，撰写并发送邮件；又找到正确的iMessage对话并发送短信。作者告诉它要联系谁以及说什么。
    进展与成效
    邮件和短信均未通过API或集成发送。Claude还通过Teams联系了一位同事，在发送前暂停并取得作者批准。作者没有报告这些运行出现失败。
    值得注意
    Outlook加载用了几分钟，因为这个桌面应用此前从未打开过。首次启动的应用可能需要等待。
    亲自尝试
    使用
    Claude电脑操作
    复制提示词
    在我的电脑上打开[邮件应用]，起草一封给[收件人]、关于[主题]的邮件；然后打开[消息应用]，找到我与[朋友]的对话，起草内容为[消息]的信息。每条发送前都停止，把文字展示在屏幕上让我批准。获得批准后发送，并在两条都发出后告诉我。
    原始来源：https://www.thegrowthcmo.co/p/i-gave-claude-control-of-my-computer

<details><summary>English original</summary>

    Send emails and iMessages by letting Claude control your computer
    An author gave Claude computer use control for three hours; it opened Outlook to compose and send an email, and found an iMessage conversation to message a friend.
    Done with
    CU
    Claude computer use
    What they did
    Claude CoWork's Outlook connector needed IT approval and its iMessage integration had failed earlier, so the author turned on computer use instead. That took five setup steps, including a Chrome extension, screen recording and accessibility settings. Claude then opened the Outlook desktop app, composed and sent an email, and found the right iMessage conversation and sent a text. The author told it who to message and what to say.
    How it went
    Both the email and the text were sent without any API or integration. Claude also messaged a coworker in Teams, pausing for the author's approval before sending. The author doesn't report any failures in these runs.
    Worth knowing
    Outlook took a few minutes to load because the desktop app had never been opened. Expect a delay on apps you haven't launched before.
    Try it yourself
    with
    Claude computer use
    Copy prompt
    On my computer, open [email app] and draft an email to [recipient] about [topic], then open [messaging app] and find my conversation with [friend] and draft a message saying [message]. Stop before sending each one and show me the text on screen so I can approve it. After I approve, send them and tell me once both are sent.
    Original source: https://www.thegrowthcmo.co/p/i-gave-claude-control-of-my-computer

</details>

## 原作者的方法与来源

来源：[I gave Claude control of my computer](https://www.thegrowthcmo.co/p/i-gave-claude-control-of-my-computer)

方法摘要未收录

## 简要分析

商业分数未评定。

### 本轮能证明什么

目录记述作者进行了三小时体验，并用屏幕操作发送邮件、iMessage及Teams消息。原文读取失败，因此没有核验作者身份、文章日期、实际截图、原始消息和成功回执。三小时是体验时段，不是每条消息耗时，也不是节省时间。作者未报告失败只是目录所述，不能改写为零失败率。完整翻译保留来源表述，分析另外标明证据范围。

依据：[Sdirectory](https://agentusecases.ai/use-case/send-emails-and-imessages-by-letting-claude-control-your-com)

### 更换操作路径不等于取得授权

目录说Outlook连接器需要IT批准后改用电脑操作；这是行为转述，不是本报告建议绕开公司审批。原文无法读取，未知公司是否另行批准桌面操作，不能推定作者违规，也不能把连接器审核当成应绕过的障碍。面向组织交付时，先确认相同数据与发送用途是否获准；换API、浏览器或屏幕路径不会自动扩大授权。

依据：[Sdirectory](https://agentusecases.ai/use-case/send-emails-and-imessages-by-letting-claude-control-your-com), [Sadmin](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)

### 连接器与桌面各有什么代价

当前官方优先使用可用连接器，再考虑浏览器和屏幕，说明屏幕操作是覆盖缺失集成的办法，而非普遍更优。它能操作没有专用接口的应用，但需要关注窗口、启动和界面变化。对于一封短消息，手动输入或复制草稿可能成本更低；只有跨应用准备和重复步骤足够多时，自动化的设置与监督才可能划算。本案没有净省时计量。

依据：[Scomputer](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork)

### 不要把Cowork可用当电脑操作可用

当前专门电脑操作页列出Pro/Max及macOS/Windows条件，组织页则描述Cowork在团队与企业的其他能力。两者范围不同，不能将云端任务、内置浏览器、桌面应用操作混成一种权限。原案的五步安装描述只适用于当时体验，不保证现在每人都需Chrome扩展。实际试用应核对所用版本、套餐、可见功能与组织策略，不按旧截图更改设置。

依据：[Scomputer](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork), [Sadmin](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)

### 收件人和发送结果是主要验收点

发送前不仅核对正文，还应确认完整收件人标识、账户和具体对话，避免同名误选。草稿完成、点击发送、平台显示已发送和对方阅读是不同状态。结果未知时先查已发送记录，不再次点击制造重复通信。本案没有可供研究者独立检查的回执，研究没有访问用户邮箱、聊天或第三方账户，不能把目录成功描述当我们的发送结果。

依据：[Sdirectory](https://agentusecases.ai/use-case/send-emails-and-imessages-by-letting-claude-control-your-com)

### 更像自用功能而非独立付费产品

潜在需求是减少跨应用操作，但原案没有客户、报价、收入或复购。若提供帮助，较合理的假设交付是“在明确授权下整理草稿与操作流程”，而不是代管全部私人通信。付款人、使用频率和节省程度尚不明；不能因三个应用都能点击就推出多渠道营销服务。大量外发还涉及名单、内容和频率等独立授权，超出此案例证据与本轮任务。

依据：[Sdirectory](https://agentusecases.ai/use-case/send-emails-and-imessages-by-letting-claude-control-your-com)

### 成本应包含复核与接管

研究者以每月20组“邮件加一条消息”的经授权操作为同一单位测算，不是作者实际用量。低接管：设置维护1h，加每组复核3min共1h，人工2h×30USD=60，模型预算2，共62/月；高接管：设置维护2h，加每组9min共3h，人工5h×30=150，模型预算6，共156/月。设备、订阅和获客未知另计，售价未知不算利润。该模型不鼓励卖按条无人发送，目的是对比手工流程是否更简单。

依据：[Sdirectory](https://agentusecases.ai/use-case/send-emails-and-imessages-by-letting-claude-control-your-com), [Scomputer](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork)

### 屏幕内容与执行环境分开看

即便某些代码在隔离环境运行，电脑操作仍直接接触真实应用，屏幕截图可能包括本次任务以外的信息。应尽量使用非敏感演示内容和单一目标窗口，不为了找一个人翻遍全部私人历史。消息中的第三方要求也不能自动成为新任务。没有API连接并不等于没有数据外传或隐私风险，具体数据处理与权限应按实际产品和组织条款核对。

依据：[Ssafety](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely), [Scomputer](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork)

### 适用人群和维护负担

对已获准使用桌面助手、能随时核对收件人与正文的人可能有辅助价值。准备包括可用Desktop、已启动的应用、明确联系人和审批人；维护涉及登录、窗口变化、电脑休眠与失败恢复。目录里首次打开Outlook花几分钟，不能拿它当固定延迟或性能基准。对低频通信，设置和监督可能比自己发送更花时间，实际收益待验证。

依据：[Sdirectory](https://agentusecases.ai/use-case/send-emails-and-imessages-by-letting-claude-control-your-com), [Scomputer](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork)

### 先用草稿演示，不连接真实联系人

下一步只在获准演示环境使用虚构联系人与无敏感内容，检验定位窗口、起草、停在发送前和错误状态报告。若收件人有歧义、权限不明或必须绕过组织限制，停止并说明所缺确认。源站模板要求逐条批准后发送，保留这一边界；本轮不执行模板、不改变屏幕录制或辅助功能权限、不发任何消息。

依据：[Sdirectory](https://agentusecases.ai/use-case/send-emails-and-imessages-by-letting-claude-control-your-com), [Ssafety](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)

## 自用价值：待核实

只有目录成功转述，未取得原文或独立净省时证据。

依据：Sdirectory, Scomputer

- 适用人群：已获准使用桌面助手、能核对收件人与正文的个人。
- 用途：跨邮件和消息应用准备草稿，并在逐条批准后发送。
- 预期收益：可能减少操作切换，实际净节省和可靠性未知。
- 设置成本：Desktop可用、明确联系人、应用授权和非敏感演示材料。
- 维护成本：登录、窗口变化、休眠、重复发送核对。
- 使用频率：原案三小时体验不是固定频率；实际次数未知。
- 隐私风险：截图与对话可能暴露任务以外信息；不用私人历史试错。
- 错误风险：同名收件人、错账户、重复发送、误把点击当送达。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/send-emails-and-imessages-by-letting-claude-control-your-com

建议工具：Claude computer use

    On my computer, open [email app] and draft an email to [recipient] about [topic], then open [messaging app] and find my conversation with [friend] and draft a message saying [message]. Stop before sending each one and show me the text on screen so I can approve it. After I approve, send them and tell me once both are sent.

自编试用模板

准备条件：获准演示环境、虚构联系人、无敏感正文、明确审批人。

工具：具备所需电脑操作能力的Claude Desktop；本轮未安装或接入。

预期结果：两份草稿与发送前检查清单；未实测，不发送真实消息。

### 源站Copy prompt

原文模板

出处：https://agentusecases.ai/use-case/send-emails-and-imessages-by-letting-claude-control-your-com

依据：Sdirectory

    On my computer, open [email app] and draft an email to [recipient] about [topic], then open [messaging app] and find my conversation with [friend] and draft a message saying [message]. Stop before sending each one and show me the text on screen so I can approve it. After I approve, send them and tell me once both are sent.

### 跨应用草稿演示计划

自编模板

出处：研究团队自编

依据：Sdirectory, Ssafety

    只制定[邮件应用]与[消息应用]的虚构联系人草稿演示计划。不连接真实账户、不改权限、不发送。列出完整收件人核对、草稿检查、发送前批准和结果未知防重复规则；组织授权不清就停止，不更换路径绕过。

## 来源

- [许可目录：电脑操作发送通信](https://agentusecases.ai/use-case/send-emails-and-imessages-by-letting-claude-control-your-com)：邮件和iMessage发送及Teams审批均来自目录转述，原作者文章两次普通读取失败；不是本轮实测。
- [官方：电脑操作能力与限制](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork)：当前文档优先连接器、再浏览器、最后屏幕操作；屏幕交互较慢，需电脑唤醒且Desktop打开，应用逐项许可；computer use本身没有应用间沙箱。专门能力页列Pro/Max，不能由Cowork团队版可用推导电脑操作也可用。
- [官方：Cowork安全边界](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)：隔离代码执行不等于限制通过已连接应用读写；读取不可信内容与具有写权限组合有提示注入风险，电脑操作直接影响真实应用。
- [官方：组织审批与访问控制](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)：组织控制Cowork、云端会话、浏览器及连接器工具审批；写工具始终允许默认关闭，最严格层优先。此页描述Cowork组织功能，不证明所有组织都有电脑操作能力。
