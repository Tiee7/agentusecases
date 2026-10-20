# 用agent匹配Twitter关注账户并在Bluesky关注

## 中文

    将Twitter关注列表迁移到Bluesky
    作者的agent逐一查看他们在Twitter上关注的账户，将其匹配到Bluesky个人资料，并在那里关注这些账户。
    使用的是
    自建或未具名的agent
    他们做了什么
    Cube Flipper的帖文说，他们的agent正在处理自己在Twitter上关注的账户列表。它把每个账户匹配到一个Bluesky个人资料，并在Bluesky上关注该资料。帖文没有给出工具、匹配方法或任何人工检查的细节。
    进展与成效
    这条公告是在任务仍在运行时发布的。它没有说明数量、匹配率或错误。它说，当天被关注的人都是这次运行的一部分。
    亲自尝试
    使用
    Claude in Chrome
    复制提示词
    我已在这个浏览器中登录Twitter和Bluesky。查看我在Twitter上[我的Twitter用户名]关注的账户，找到每个账户对应的Bluesky个人资料（检查其Twitter简介，或按姓名和用户名搜索Bluesky），并在那里关注他们。遇到不能确定是同一个人的账户就跳过，最后列出已匹配、已关注和未匹配的账户。点击任何按钮之前，先暂停并向我展示计划关注的名单。
    原始来源：https://bsky.app/profile/smoothbrains.net/post/3myb2rk34m22g

<details><summary>English original</summary>

    Move Twitter follows over to Bluesky
    The author's agent goes through the accounts they follow on Twitter, matches them to Bluesky profiles, and follows them there.
    Done with a
    custom-built or unnamed agent
    What they did
    Cube Flipper's post says their agent is working through the list of accounts they follow on Twitter. It matches each one to a Bluesky profile and follows that profile on Bluesky. The post gives no detail on tooling, matching method, or any human checks.
    How it went
    The post is an announcement made while the run was under way. It states no counts, match rates or errors. It says that anyone followed today was part of this run.
    Try it yourself
    with
    Claude in Chrome
    Copy prompt
    I'm logged into Twitter and Bluesky in this browser. Go through the accounts I follow on Twitter at [my Twitter handle], find each one's Bluesky profile (check their Twitter bio or search Bluesky by name and handle), and follow them there. Skip any account where you aren't confident it's the same person and give me a final list of matched, followed and unmatched accounts. Pause and show me the list of planned follows before you click anything.
    Original source: https://bsky.app/profile/smoothbrains.net/post/3myb2rk34m22g

</details>

## 原作者的方法与来源

https://bsky.app/profile/smoothbrains.net/post/3myb2rk34m22g
仅有作者在途自述，未给实现细节或结束结果。
The author says an unnamed agent is matching followed Twitter accounts to Bluesky and following them there.
作者说一个未具名agent正在把Twitter关注账户匹配到Bluesky，并在那里关注。

## 简要分析

商业分数未评定。

### 作者只报告正在运行

实际读到Cube Flipper的公开帖，作者说agent在处理Twitter关注列表，匹配后在Bluesky关注，并向当天新关注的人打招呼。这支持正在尝试这类工作流，不支持全部迁移完成。帖子未给工具名、总数、误配、重试或耗时；可见回复没有独立试用结果。目录推荐Claude in Chrome不代表作者使用它。资料有限，交付有依据简报，不把自建工具和方法补写出来。

依据：[Sauthor](https://bsky.app/profile/smoothbrains.net/post/3myb2rk34m22g), [Sdirectory](https://agentusecases.ai/use-case/move-twitter-follows-over-to-bluesky)

### 同名只能成为候选

Sky Follower Bridge说明用相同handle、显示名或X简介中的Bluesky链接识别候选。Bluesky官方另有域名关联和验证徽章，二者不同。研究者建议按直接跨站链接、可信官网交叉指向、内容上下文等保留匹配依据；相同昵称和头像可能来自同名、粉丝或冒充账户。缺证据时保留未匹配，不用高匹配率目标迫使agent猜人。域名存在不自动证明它与原X账户属于同一人。

依据：[Smatch](https://www.sky-follower-bridge.dev/faq), [Sverify](https://bsky.social/about/blog/04-21-2025-verification)

### 关注动作和匹配列表分开验收

原创建议是先固定来源清单及时间，再输出X账户、Bluesky候选、证据链接和不确定项，逐项审阅后才考虑关注。已有关注需去重，实际动作须有回读结果，清单中的拟关注不能直接标成已关注。账号被删除、更名、未迁移、列表加载不全和多个候选分别记录。重复运行只核新增差异，不反复关注/取消关注，不把失败补成成功。该建议未在真实账号上执行。

依据：[Sdirectory](https://agentusecases.ai/use-case/move-twitter-follows-over-to-bluesky)

### 已有免费专用路线构成对照

Sky Follower Bridge官网提供桌面浏览器扩展的迁移流程，并明确提示偶尔会建议错误匹配、需核验资料；当前说明不支持手机浏览器。它是可比较的现成工具，不是本案作者工具。研究者认为通用agent若只重复同名检索与点击，付费差异很薄；只有改善证据审阅、复杂账户歧义、迁移记录或可访问性，才有继续验证的理由。本轮未安装扩展、登录或测试其真实匹配性能。

依据：[Sbridge](https://www.sky-follower-bridge.dev/get-started), [Smatch](https://www.sky-follower-bridge.dev/faq)

### 更像一次迁移服务，而非天然订阅

商业假设是帮助个人或小团队重建跨平台信息源，可能按限定数量收一次整理费，或作为已有社区迁移服务的附加项。用户自己或团队运营者可能付款，但本案无报价、客户或收入。获客假设可用匿名合成对照样本展示匹配解释和漏配，交付应为可批准清单与验证日志；不能保证粉丝随迁、曝光、互动或成交。单次关注迁移的低频率和现成免费工具，都削弱独立订阅逻辑。

依据：[Sauthor](https://bsky.app/profile/smoothbrains.net/post/3myb2rk34m22g), [Sbridge](https://www.sky-follower-bridge.dev/get-started)

### 成本主要取决于歧义复核

工具/模型及API费用未知，不能把未命名agent按某套餐报价。研究者列出的成本包括来源清单取得、长列表加载、同名核对、跨站链接确认、人工批准、限速等待、错配撤销和平台改版维护；商业服务还需获客与支持。应测每百条候选的人工分钟、精确率、未匹配比例和安全跳过量，不能只看新增关注数。无实测数据，简报不编利润或节省。

依据：[Sauthor](https://bsky.app/profile/smoothbrains.net/post/3myb2rk34m22g)

### 自用价值是找回信息源

适用者是正在跨平台迁移、能识别自己关注对象的人。潜在收益是减少逐个搜索，但实际节省未知。首次准备来源范围和目标账户，维护主要是改名、失效链接、重复项与后续新增；通常是一轮迁移加少量增量复查。关注关系可能暴露个人兴趣和关联，登录会话也需保护。错误风险是关注冒充者、误把粉丝列表当关注列表，或过度批量操作触发平台限制。本轮未读取用户私人关系图。

依据：[Sauthor](https://bsky.app/profile/smoothbrains.net/post/3myb2rk34m22g), [Sdirectory](https://agentusecases.ai/use-case/move-twitter-follows-over-to-bluesky)

### 授权范围只覆盖选定关注关系

原创控制建议：公开资料用于匹配不意味着允许发私信、点赞、转发或自动取消原平台关注；浏览器已登录也不能替代这些动作的授权。复制前需核对适用平台规则和账户限制；遇到拒绝、验证码或安全警告应停止相关动作，不换号或绕过。本轮只读公开资料，未访问用户X/Bluesky会话、创建凭据或调用关注API；官方限速页重定向后空白，没有虚构当前速率数值。

依据：[Sdirectory](https://agentusecases.ai/use-case/move-twitter-follows-over-to-bluesky), [Sbridge](https://www.sky-follower-bridge.dev/get-started)

### 用虚构档案先测误配

拟议演练制作十组虚构跨站档案，包含同名不同人、改名、粉丝账号、直链、未迁移和重复账户，人工预先标答案。让已有获准助手只产出候选及依据，预期得到明确匹配与待查清单，不实际关注。衡量人工复核总时间和错配，宁可保留未知。若同名误配仍多、无法解释证据或不比专用工具与人工快，停止扩大；完整真实迁移需要另外的明确账户授权及可回读结果。

依据：[Sbridge](https://www.sky-follower-bridge.dev/get-started), [Sverify](https://bsky.social/about/blog/04-21-2025-verification)

## 试用准备与预期结果

十组虚构跨站档案和人工匹配答案。
可解释的匹配、歧义和未知清单；本轮未试用。
只依据给定虚构档案列候选与匹配证据。相同昵称或头像不足以确认，标出同名、粉丝账户、未迁移及重复。输出待审清单，不登录、不关注、不发消息、不改任何账号关系。

## 来源

- [许可目录案例](https://agentusecases.ai/use-case/move-twitter-follows-over-to-bluesky)：工具未具名，Claude in Chrome是目录试用建议。
- [Cube Flipper公开迁移进度帖](https://bsky.app/profile/smoothbrains.net/post/3myb2rk34m22g)：2026-10-19作者自述运行中，未提供数量、错误率和终态。
- [Sky Follower Bridge官方使用说明](https://www.sky-follower-bridge.dev/get-started)：现成桌面浏览器工具包含匹配结果审阅与关注；官方警告会错配。
- [Sky Follower Bridge匹配说明](https://www.sky-follower-bridge.dev/faq)：依据同用户名、显示名或简介中的Bluesky链接找候选，不是原作者方法。
- [Bluesky域名与验证徽章说明](https://bsky.social/about/blog/04-21-2025-verification)：域名关联与验证徽章是不同身份信号，仍需跨站对应。
