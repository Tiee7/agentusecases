# 用 OpenClaw 通过 Telegram 添加家庭待办事项

## 中文

    通过 Telegram 消息添加家庭待办事项
    作者曾在办公室通过 Telegram 指示 OpenClaw agent，经由自定义 API 向家里的待办清单添加事项，后来停止了使用。
    实际使用
    OpenClaw
    他们做了什么
    作者运行了 OpenClaw，并编写了一个自定义 API，用来向仅保存在家中 PC 上、没有与手机同步的待办清单添加事项。他们从办公室发送 Telegram 消息，agent 就调用该 API 添加事项。来源没有给出更多设置细节。
    结果如何
    这个功能用起来不错，以至于作者现在还很想念它。他们在 QEMU 软件出故障后停止使用 OpenClaw，现在正在询问如何在免去繁琐设置的情况下复现这一功能。
    需要知道的事
    作者说，让 OpenClaw 完成任务比为每个用例单独编写工具更省事；但它还不够可靠，不值得花上数周追求一套完美的设置。
    自己试试
    推荐工具
    OpenClaw
    复制提示词
    连接我的 Telegram，让我可以通过消息请你向保存在[应用、文件或 API]中的家庭待办清单添加事项。当我发送类似“添加[家务或要办的事]”的消息时，把它加入清单，并回复更新后的清单。完成的标准是：清单中出现一条测试事项，并且我可以请你把清单读回来。移除任何事项前先询问我。
    原始来源：https://news.ycombinator.com/item?id=47724016

<details>
<summary>英文原文</summary>

    Add home TODO items by Telegram message
    The author told an OpenClaw agent over Telegram to add items to a home TODO list via a custom API while at the office, before they stopped using it.
    Done with
    OC
    OpenClaw
    What they did
    The author ran OpenClaw and wrote a custom API that adds items to a TODO list kept only on their home PC, with no phone syncing. From the office they sent a Telegram message, and the agent called that API to add the item. The source gives no further setup detail.
    How it went
    It worked well enough that the author misses it. They stopped using OpenClaw after their QEMU software broke, and are now asking how to replicate this without the setup hassle.
    Worth knowing
    The author says OpenClaw was less effort than writing a tool per use case, but not worth weeks chasing a perfect setup because it isn't reliable enough.
    Try it yourself
    with
    OpenClaw
    Copy prompt
    Connect to my Telegram so I can message you to add items to my home to-do list stored at [app, file, or API]. When I send something like 'add [chore or errand]', add it and reply with the updated list. Finished means one test item appears in the list and I can ask you to read the list back. Ask before removing any items.
    Original source: https://news.ycombinator.com/item?id=47724016

</details>

## 原作者的方法与来源

来源：[BeetleB在Hacker News介绍家庭TODO入口及补充约束](https://news.ycombinator.com/item?id=47724016)

作者方法摘要

1. 作者从办公室通过Telegram和OpenClaw调用自定义API，向家庭PC的待办清单新增事项；不与手机同步是有意设计。
   English summary: From the office, the author used Telegram and OpenClaw to call a custom API for a TODO list on a home PC; the list was intentionally not phone-synced.

2. QEMU软件故障后，他们因没有时间排查而停用，但仍认可这个便捷的待办入口。
   English summary: They stopped after their QEMU software failed and they lacked time to investigate, while still valuing the convenient task intake.

3. 对于替代方案，他们希望限制功能范围，由LLM生成标题与详细说明，并继续使用长期沿用的本地系统；API并未对外暴露。
   English summary: For a replacement, they want limited functionality, LLM-written titles and detailed notes, and continued use of their long-standing local system; the API is not externally exposed.

## 我们的分析

**商业结论：适合内部效率工具。复用既有本地环境验证入口，暂不单独投入家庭待办产品**

作者要保留长期定制且不与手机同步的家庭清单，Telegram到本地API的入口确有便利；但直接停用由运行环境故障触发，仍需维护整条依赖链。现成机器人与工作流平台可替代部分能力，且没有客户、付费或成本对照。低客单设置和维护情景对人工支持很敏感，因此优先做内部可逆验收，不将个人喜爱转化为独立产品的收入预测。

案例ID：`add-home-todo-items-by-telegram-message` · 案例来源：https://agentusecases.ai/use-case/add-home-todo-items-by-telegram-message
研究时间：2026-10-18T01:17:56.343554+00:00

**商业评分：22.0/100。用户反馈信号占5%。**

| 维度 | 权重 | 分数 /5 | 商业依据 |
|---|---:|---:|---|
| 付费需求 | 20% | 1 | 一个不愿迁移旧系统的家庭用户有明确需求，但没有客户、收费或重复采购证据，不能外推普遍付费市场。 [S8ca2c2978e62] |
| 业务价值与效果证据 | 20% | 2 | 作者肯定该入口并想恢复使用，但缺少运行日志、成功率和工时对照，且实际已因环境问题停用。 [S86c2b1d68d88, S8ca2c2978e62] |
| 单位经济与利润 | 20% | 1 | 99美元设置包和19美元维护的假设均对人工敏感，50客户也只薄利，实际价格、用量与支持频率未知。 [S8ca2c2978e62, S9c31625dedcc] |
| 获客与市场进入 | 15% | 1 | 技术论坛能发现受限接口需求，但没有获客转化或购买验证，个人设备接入还增加信任和支持负担。 [S8ca2c2978e62, Sb90d40811f52] |
| 竞争壁垒 | 10% | 0 | 通道和消息触发能力均有现成构件，未见独家接口、数据或分发，个人定制历史不能当作可销售壁垒。 [S8ca2c2978e62, Sd423ce29f149, Sb90d40811f52] |
| 交付与经营风险 | 10% | 1 | 整条在线依赖链与重复更新需要维护和恢复，现有访问控制可缩小范围，但原例配置及端到端结果未实测。 [S8ca2c2978e62, Sd423ce29f149, S69b841c7350d, Sb90d40811f52] |
| 独立用户反馈信号 | 5% | 1 | 仅有作者正反自述及相邻论坛用户经验，没有独立复现或总体分母；该信号权重5%，不是用户星级。 [S8ca2c2978e62] |

## 自用价值：中

对已有稳定本地系统、接口与代理环境的人有明确的捕获便利，但需人工设置和恢复；未测得节时或质量收益。

依据：S86c2b1d68d88, S8ca2c2978e62, Sd423ce29f149, S69b841c7350d

- 适用人群：维护家庭本地TODO系统且能检查接口和运行环境的人。
- 用途：从既有Telegram入口新增任务并读回，保留原清单。
- 预期收益：减少回到家庭PC后补记的摩擦；收益大小和频率未知。
- 设置成本：已有获准的消息连接、在线家庭设备、受限API契约和合成测试清单。
- 维护成本：设备/网络/运行环境维护，检查写入、重复消息与失败恢复。
- 使用频率：随离开家庭PC时的真实记录需要使用；先确认频率。
- 隐私风险：家庭待办经消息与模型环节处理，不能跨用户混用或把私人清单、聊天、凭据公开。
- 错误风险：可能丢任务、重复新增、字段被误整理或过早回复完成，需要读回和恢复检查。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/add-home-todo-items-by-telegram-message

建议工具：OpenClaw

    Connect to my Telegram so I can message you to add items to my home to-do list stored at [app, file, or API]. When I send something like 'add [chore or errand]', add it and reply with the updated list. Finished means one test item appears in the list and I can ask you to read the list back. Ask before removing any items.

自编试用模板

准备条件：已有获准使用的Telegram连接和家庭API说明、合成清单、允许的用户/聊天及新增和读回权限；本轮不创建凭据或连接真实设备。

工具：案例实际和源站推荐均为OpenClaw；模型和版本未知。n8n仅作为替代构件比较。

预期结果：合成清单上的一次新增与读回方案、去重和恢复验收记录；以下自编模板未实测，不声称原API兼容。

### 在合成清单上验收受限待办入口

自编模板

出处：研究团队自编

依据：S86c2b1d68d88, S8ca2c2978e62, Sd423ce29f149, S69b841c7350d

    我已有[获准使用的Telegram连接]和[家庭TODO接口说明]。先只根据说明及[合成测试清单]设计新增与读回链路，不连接真实设备、不发送真实消息，也不创建机器人或凭据。保持家庭API非公开，不建议端口转发。把自然语言任务整理成待确认的简短标题与详细说明，标出原文没有给出的日期或优先级；不要替我编造。只允许[用户/聊天]触发新增和读回，禁止删除、任意Shell或扩大访问。展示一条测试事项写入与读回的预期结果，并列出重复消息、API失败、写入后回复前重启的验收步骤，区分收到消息与业务写入成功。只用现有工具，不调用额外付费API；记录假设与所缺接口信息，不把方案当成实测。

### Check a constrained TODO intake with a synthetic list

自编模板

出处：研究团队自编

依据：S86c2b1d68d88, S8ca2c2978e62, Sd423ce29f149, S69b841c7350d

    Using only [existing authorized Telegram connection documentation], [home TODO API contract] and [synthetic list], design add-and-read-back operations. Do not connect to a real device, send a real message, create credentials, or expose the home API publicly. Turn a sample task into a proposed short title and detailed note; mark missing dates or priorities without inventing them. Limit the design to [allowed user/chat], add and read-back; exclude deletion, arbitrary shell access and broader permissions. Show expected results for one test task, repeated delivery, API failure, and restart after write but before reply. Separate message receipt from successful storage. Use existing tools only, make no additional paid API calls, and label the output as an untested plan.

## 已核验事实

- 源站实际使用和推荐工具均标注OpenClaw；归档保存了完整源站Copy prompt，但它不是作者实际提示词。 [S86c2b1d68d88]
- BeetleB自述在办公室通过Telegram让OpenClaw调用自定义API，为家庭PC上的TODO清单新增事项。 [S8ca2c2978e62]
- 作者在回复中明确说家庭API未暴露到外部世界，清单不与手机同步是有意的设计。 [S8ca2c2978e62]
- 作者说自己的TODO系统从2009年持续定制，不愿切换到其他人的应用；这限制了通用同步应用作为替代的适配性。 [S8ca2c2978e62]
- 作者停用的直接原因是QEMU软件故障且没有时间调试，原帖没有提供OpenClaw核心故障定位或总体可靠性数据。 [S8ca2c2978e62]
- 作者寻找的替代方案仍希望由LLM把随口任务整理成简短标题和详细说明，再调用API。 [S8ca2c2978e62]
- 当前OpenClaw官方Telegram文档说明默认长轮询、可选Webhook，以及默认私聊配对；不能认定案例采用当前配置。 [Sd423ce29f149]
- Telegram官方FAQ说明长轮询与Webhook不能同时接收更新，并解释未确认更新可能再次返回。 [S69b841c7350d]
- n8n官方Telegram Trigger支持消息事件及按Chat IDs、User IDs限制触发，不意味着能直接访问本例非公开家庭API。 [Sb90d40811f52]
- 采集时n8n Starter显示20欧元/月、按年付费、2.5K月工作流执行；该报价不是原案例费用或付费需求证明。 [S9c31625dedcc]

## 谁需要保留本地清单，谁可能付款

原始使用者BeetleB的目标并不是寻找另一款通用清单应用。他在HN回复中说，TODO系统从2009年起持续定制，清单只在家庭PC上，不与手机同步，也不愿迁移到别人的应用。这个限制决定了产品边界：需要的是从现有聊天入口把任务送进既有系统，而不是重新建立一套任务数据库。把“装一个手机TODO应用”作为默认答案，会绕开他真正要保留的工作方式。

 潜在自用人群是有稳定本地工作流、已有可调用接口、愿意维护一台在线设备的人。潜在付款人则只能作为假设：不想迁移旧系统、愿为集成和故障恢复付费的个人或很小的团队。案例没有采购流程、合同、付费记录或复购证据，不能把一个坚定的个人需求外推成广泛的消费者市场。家庭清单的偶发价值也不等于企业任务系统的预算。

 因此本报告把它判断为适合内部效率工具。已有OpenClaw和其他自动化用途时，增加这个入口可能复用现成维护投入；若仅为新增一条待办就搭建完整代理环境，设置、排错与恢复很容易超过输入便利本身。自用价值评为中，需要已有基础设施和人工复核，不能从商业分数直接换算。

依据：S86c2b1d68d88, S8ca2c2978e62

## 消息如何成为家庭系统中的一条待办

已知链路是办公室的Telegram消息进入OpenClaw，再由agent调用作者写的API，把事项加入家庭PC上的清单。作者后来明确说API没有暴露到外部世界。这不意味着远程访问不可能，也不要求直接打开家庭API的公网入口；消息入口、代理运行位置和目标API是三个不同环节。原帖没有披露具体网络地址、认证方式、模型或代码，不能补写为某种确定的隧道或部署拓扑。

 在寻找替代方案时，作者进一步要求LLM把随口描述整理成简短标题与详细说明，再调用API。这是他表达的替代需求，不能倒推为原API已经采用我们设想的字段格式。他还提到过去的语音链路包括ogg录音、Whisper及LLM整理；这个附加用途增加了模型和转录环节，并非源站推荐文本里“一条测试事项”的同义词。

 可检查的交付应从现有接口契约开始：确认字段、允许的新增动作和读回方式，再验证一次请求确实写入、返回的内容与存储一致。聊天机器人说“已完成”只是回复，只有成功读回目标清单才能证明这一次写入。本文没有连接作者设备、发送Telegram消息或运行他的API，下面的设计建议与原作者实际实现分别归因。

依据：S86c2b1d68d88, S8ca2c2978e62, Sd423ce29f149, S69b841c7350d

## 需求频率、可进入范围与成本参照

案例体现的是远离家庭PC时捕获待办的摩擦，以及用户不愿迁移历史系统的约束；没有消息频率、漏记数量、节省时间或家庭人数。不能按Telegram用户数、OpenClaw关注量或TODO应用下载量推算可付费客户，更不能把论坛赞同当成订单。首先要确认一个人每周真正需要多少次这类操作、现在怎样补记、一次失败会造成多少返工。

 n8n的公开价格为工作流自动化提供了可见参照：采集页面的Starter显示年付折算20欧元/月、2.5K月执行量。这是供应商当时的报价口径，不是本例支出，也不证明家庭用户会付这个价。执行量、模型调用、家庭设备和定制接口维护不是同一个成本单位，不能因为一个工作流只运行一次就忽略后续支持。本文不把欧元报价换算成美元收益，也不假定该计划包含任意模型用量。

 更现实的进入范围是少数明确允许接入的本地工具，而不是泛称“替所有人管理生活”。每多支持一种旧清单格式，就多一套字段、重复请求、数据恢复和版本兼容问题。先记录一个固定接口的安装与维护工时，才有依据决定能否把它标准化；当前没有市场规模或收费意愿证据。

依据：S8ca2c2978e62, Sb90d40811f52, S9c31625dedcc

## 已有代理、普通机器人与工作流平台

对已经稳定运行OpenClaw的人，复用现有Telegram通道与受限工具调用是一个基线。对只需要新增和读回待办的人，另一基线是保持一个常驻的窄功能机器人，按明确规则或经LLM整理后调用本地API。原讨论中的用户提出邮件、脚本、n8n和其他应用；这些是建议与个人体验，不是我们已经替作者复现的迁移方案。简单固定命令也未必满足他希望口语描述自动整理的要求。

 n8n官方提供Telegram Trigger，支持消息事件以及按聊天或用户ID限制触发，说明聊天入口并非OpenClaw独占。可是能收到消息，并不表示某个托管工作流可以访问家庭PC上的非公开接口。部署位置、持续在线、接口可达性和维护责任仍需单独决定，不能把购买云计划当成网络问题自动解决，也不应默认让家庭API对公网开放。

 同样，通用同步TODO应用对愿意迁移的用户可能更简单，却不符合本例已经明确的“不迁移、不与手机同步”偏好。比较应围绕保留现有系统、人工设置时长、失败可发现性和恢复成本，不能只比较功能清单。本文没有安装这些替代项目，也不建议绕过任何工具的认证或订阅规则。

依据：S8ca2c2978e62, Sd423ce29f149, S69b841c7350d, Sb90d40811f52, S9c31625dedcc

## 一次性设置与月度维护的单位经济

作者说OpenClaw比为每个用途单写工具省事，同时又认为不值得为完美设置消耗数周；这不是精确工时或费用测量。自用是否合算取决于原来已有多少环境、一次错误新增会怎样处理，以及排查时间由谁承担。家庭PC、模型、语音转录、消息通道与人工维护应分别记账，不能把开源入口或已有订阅理解为每次业务操作都没有成本。

 以下全部是经营假设，币种统一USD，未发生任何收费或付费API调用。第一种99美元的一次性接入包，假设模型/测试预算1美元、人工3小时×30美元=90美元、其他3美元、获客15美元，可变成本109美元，单位贡献-10美元；每月20包、固定200美元，月经营贡献-400美元。接口越不标准，越难靠低价设置回收人工。

 第二种19美元/客户月的有限维护服务，假设模型1美元、人工15分钟×30美元=7.5美元、其他2美元、获客摊销4美元，可变成本14.5美元，贡献4.5美元；50客户、月固定200美元，月贡献25美元。一次额外30分钟支持就让该客户当月贡献变为-10.5美元。该情景不含首次集成工时，不能与亏损设置包拼成已验证盈利；客户数、报价、用量和支持频率都需要实测。

依据：S86c2b1d68d88, S8ca2c2978e62, S9c31625dedcc

## 触达与交付如何保持可重复

原帖和回复能帮助识别一类熟悉本地工具、愿意讨论具体接口的人，但一个自选技术论坛不是可直接购买的客户渠道。没有搜索转化率、付费试点、推荐比例或获客账单，不能假设发一篇教程就能稳定取得订阅用户。用户也可能更愿意自己写一个窄功能脚本；他需要帮助，不代表一定愿意把家庭设备交给陌生服务商维护。

 若验证对外服务，交付范围应固定为一个已有接口、一种消息入口、允许的写入与读回动作、约定的维护窗口。接口说明、部署位置和可恢复记录要在接入前明确，避免把客户每个新的想法都算进低价套餐。把可选语音转录、任务删除、跨用户共享或任意系统操作单独处理，否则一次新增清单会迅速变成不可控的通用远程代理项目。

 本轮没有联系作者、论坛用户或潜在客户，没有发送消息、报价或收取费用。下一步更有价值的是在获准的合成清单和已有工具上测出交付工时，再通过用户自行提供的反馈验证需求；当前不需要注册机器人、创建凭据或购买云计划来让商业判断成立。

依据：S8ca2c2978e62, Sd423ce29f149, Sb90d40811f52, S9c31625dedcc

## 什么能积累，什么容易被替代

Telegram消息入口、工具调用和自然语言整理都已是现成能力，简单封装没有明显独占性。OpenClaw官方通道和n8n触发器都能覆盖入口部分，原讨论也出现了多种自建方式。没有证据表明作者拥有独家接口、数据、销售渠道或专用模型；他自己的长期定制清单是个人使用资产，不是可以直接复制出售给所有人的产品壁垒。

 真正可能积累的是受限连接器的适配规范、可靠的写入与读回记录、故障复现样本和清晰的恢复流程。但这些目前是我们提出的经营方向，未由案例验证。尤其不能把客户的私人待办内容当作可公开训练、转售或跨客户共享的数据资产；有价值的是经过允许、去标识化的错误类型与接口测试，而不是原始生活记录。

 如果平台原生通道逐步改善，单纯“能在Telegram加任务”的溢价会进一步缩小。只有当固定接口的维护负担明显低于用户自行搭建，并且能证明失败可发现、可恢复时，服务才可能获得续费理由。现有材料还不能支持规模化、网络效应或持续利润的判断。

依据：S8ca2c2978e62, Sd423ce29f149, Sb90d40811f52

## 在线依赖、重复消息和权限边界

停用的直接原因是作者的QEMU软件出故障且没有时间调试，不是已经定位出的OpenClaw核心缺陷。另一方面，这件事说明用户购买或自建的是整条依赖链：家庭机器、虚拟化或运行环境、网络、消息通道、模型和自定义API。任何一环停止都可能使新增任务失效，不能用某一份通道文档的“production-ready”表述代替端到端验收。

 Telegram官方说明支持长轮询与Webhook，并解释未确认更新可能重复出现。工程上应把消息接收、任务写入和回复读回分开记录；确认更新并不自动等于业务写入成功。建议以聊天与消息标识做幂等控制，并测试断网、重复投递、目标API失败、写入后回复前重启等情况。这些是待验证设计，本轮没有实现或测量任何组件的恰好一次语义。

 当前OpenClaw文档的默认私聊配对和n8n按用户/聊天ID限制触发，提供了访问控制构件，但具体工具权限仍需限定。对家庭待办只开放新增与读回，不能因此授予任意Shell、删除文件或通用网络访问。敏感待办经消息和模型处理的范围需要用户自己明确；私人内容、凭据和聊天不进入本研究仓库。

依据：S8ca2c2978e62, Sd423ce29f149, S69b841c7350d, Sb90d40811f52

## 直接使用者与相邻流程的反馈

BeetleB说Telegram到家庭自定义API的待办入口很方便，想念该功能；同时不愿为理想设置耗费数周，QEMU软件故障后停用。API不对外开放且保留旧清单是明确约束，没有量化成本、可用率或客户记录。

相关体验：lucw自述通过编排工具从Telegram把事项写入自己的Todoist。它说明相邻流程有人使用，但目标系统不同，不是对本例家庭API的复现，也未提供收费或可靠性数据。

相关体验：SyneRyder描述自己使用邮件触发Claude并通过MCP管理Toodledo等工具。该经验说明窄功能消息入口可以是替代方向，通道与后端都与本例不同，不能当作OpenClaw Telegram的性能测试。

依据：S8ca2c2978e62

## 先作为内部入口，再决定是否值得经营

结论是适合内部效率工具，不建议仅凭这一条用途开展独立产品投入。原始讨论证明了一个具体、持续偏好很强的需求，也显示了设置与故障恢复的代价。最有利的反证是：作者原本已在使用OpenClaw，增加多个小用途的边际成本可能很低，工具的总价值也可能高于这条TODO入口。但这支持复用已有环境，而不是证明每个家庭会为一个新服务付费。

 继续条件应围绕原约束做小而完整的验证：用合成清单和已有、获准的消息连接，完成一条自然语言任务的标题/说明整理、单次写入和读回；重放同一消息不能重复新增，失败必须可见，恢复后不能悄悄丢失。记录设置、每次人工纠错和一周维护时间，再决定是否扩大消息量或增加语音。这里是研究提出的验收计划，本轮未运行真实代理或操作用户设备。

 若只有开放家庭API公网、扩大任意系统权限、频繁人工重启或重写用户清单才能继续，应停在方案阶段重新选择架构。对外验证时，若99美元设置包仍需三小时人工，或19美元月费平均支持超过预算，就应调整范围与报价，而不是用未来客户量掩盖亏损。尚无客户与账单，不能把假设情景的薄利当作已实现财务结果。

依据：S86c2b1d68d88, S8ca2c2978e62, Sd423ce29f149, S69b841c7350d, Sb90d40811f52, S9c31625dedcc

## 单位经济测算：情景假设，不是项目已实现的财务结果

| 情景 / 交付单位 | 收入 | 可变成本（含获客） | 单位贡献 | 月交付量 | 月固定成本 | 月经营贡献 |
|---|---:|---:|---:|---:|---:|---:|
| 假设：一次性固定接口接入包 / 一个现成家庭TODO接口的新增/读回接入 (USD) | 99.00 | 109.00 | -10.00 | 20 | 200.00 | -400.00 |
| 假设：有限范围月度维护 / 客户月，不含首次集成 (USD) | 19.00 | 14.50 | 4.50 | 50 | 200.00 | 25.00 |

假设：一次性固定接口接入包假设：全部未实测假设：人工3小时×30美元，模型/测试预算1美元，其他3、获客15；可变109、单位贡献-10，20包减固定200，月贡献-400。不是作者账单、市场报价或实际交付。；API成本 1，人工成本 90，其他可变成本 3，分摊获客成本 15。依据：S8ca2c2978e62, Sd423ce29f149, Sb90d40811f52

假设：有限范围月度维护假设：全部假设：每客户月人工15分钟×30美元、模型1、其他2、获客摊销4，可变14.5、贡献4.5；50客户减固定200，月贡献25。额外30分钟支持使该客户当月贡献-10.5。未含首次集成、税费和退款，不是已验证盈利。；API成本 1，人工成本 7.5，其他可变成本 2，分摊获客成本 4。依据：S8ca2c2978e62, Sd423ce29f149, S9c31625dedcc

## 反证与未核实信息

作者肯定多用途复用比逐个写工具省事，已有OpenClaw用户可能获得比单个待办场景更高的总价值；其直接停用原因是QEMU环境故障，不能归因于已定位的OpenClaw缺陷。相邻评论说明Telegram编排和窄功能入口可用，也意味着单一聊天入口没有明显独占性。

未取得作者代码、API契约、网络/权限/模型配置、用量、成功率、维护账单或付费客户；未运行真实OpenClaw、发送消息、访问家庭设备或接触私人清单。当前官方文档和定价不代表原帖当时版本；论坛自述未独立复现。原文和完整译文只覆盖已归档案例页，外部讨论仅做摘要。

## 具体动作与止损条件

先用合成清单和已有获准连接验收一条任务的整理、写入与读回，再测试重复消息和失败恢复，记录设置与一周维护工时；本轮不创建机器人或凭据。

停止投入条件：若需暴露家庭API到公网、扩大任意系统权限或频繁人工恢复才能运行，先停下重选架构；若真实设置或月维护工时持续超过假设预算，停止扩大服务范围。

## 来源与对应关系

- [S86c2b1d68d88] [源站归档：Add home TODO items by Telegram message](https://agentusecases.ai/use-case/add-home-todo-items-by-telegram-message)：支持源站实际工具OpenClaw、家庭本地清单、自定义API、Telegram入口、QEMU故障后停用与源站试用模板；原始正文未改写。
- [S8ca2c2978e62] [Hacker News：BeetleB 的本地 TODO 讨论](https://news.ycombinator.com/item?id=47724016)：支持作者原始自述与补充限制：API未对外暴露、不愿替换2009年以来的定制清单、QEMU故障及标题/详情需求；也含其他用户的相邻工作流自述，不是独立性能试验。
- [Sd423ce29f149] [OpenClaw 官方：Telegram](https://docs.openclaw.ai/channels/telegram)：支持Telegram通道默认长轮询、可选Webhook和默认DM配对等当前能力；不证明案例采用当前版本、具体网络配置或可靠性水平。
- [S69b841c7350d] [Telegram 官方：Bots FAQ](https://core.telegram.org/bots/faq)：支持长轮询和Webhook的更新接收方式、两者不能同时使用及更新确认机制；不保证自定义TODO写入能去重或业务成功。
- [Sb90d40811f52] [n8n 官方：Telegram Trigger](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger)：支持现有Telegram消息触发器及按chat/user IDs限制触发的替代构件；不证明云端流程能直接访问本例未公开家庭API。
- [S9c31625dedcc] [n8n 官方：Plans and Pricing](https://n8n.io/pricing/)：支持采集时云计划按月工作流执行量定价，以及Starter年付折算每月20欧元、2.5K执行的公开报价；不是作者费用、模型账单或家庭用户付费意愿。

结构化记录：[research/add-home-todo-items-by-telegram-message.json](../research/add-home-todo-items-by-telegram-message.json)
