# 用 AI agent 识别手写日程并归档邮件 PDF

分析深度：简要研究（brief）；商业评分未评定；不计入深研完成数。

## 案例完整中文译文

    将手写预约添加到日历并归档PDF
    一位评论者描述了一个自建agent：通过OCR识别手写预约的照片并将其添加到日历，进行网页搜索，还能把邮件中的PDF归档到paperless。
    实际使用
    自建或未命名agent
    具体做法
    这位评论者描述的是自行构建个人agent，而不是依赖聊天订阅。它读取手写预约的照片并将其添加到日历，搜索网页，还能找到带有PDF的邮件，并将PDF归档到本地paperless实例。它使用低价的flash级别模型，按token计费。
    结果如何
    评论者称它很容易构建，并表示flash模型对于简单的agent任务已经绰绰有余。他们估计token费用每年约15美元，而订阅费用每月20美元。没有提供详细结果。
    值得知道
    费用数字是评论者自己的估计，评论中没有提供构建细节，因此各个工具的集成需要自行摸索。
    自行试用
    推荐工具
    OpenClaw
    复制提示词
    当我发送手写预约的照片时，读取文字，并将日期、时间和地点添加到我的[日历名称]中。当我通过邮件转发PDF时，将其归档到[paperless或文件夹]，并设置合适的标题和标签。保存之前，先向我展示每个日历条目和文件名；当天这一批内容全部归档后停止。
    原始来源：https://news.ycombinator.com/item?id=49627493

<details>
<summary>English · 完整归档原文</summary>

<pre>Add handwritten appointments to calendar and file PDFs
A commenter describes a self-built agent that OCRs a photo of a handwritten appointment into their calendar, searches the web, and files an emailed PDF into paperless.
Done with a
custom-built or unnamed agent
What they did
The commenter describes building a personal agent rather than relying on a chat subscription. It reads a photo of a handwritten appointment and adds it to a calendar, searches the web, and finds an email with a PDF and files it in a local paperless instance. It runs on cheap flash-tier models paid per token.
How it went
The commenter calls it easy to build and says flash models are more than enough for simple agent tasks. They estimate about 15 dollars a year in tokens, versus 20 a month for a subscription. No detailed results are given.
Worth knowing
The cost figure is the commenter&#x27;s own estimate, and the comment gives no build details, so expect to work out the tool integrations yourself.
Try it yourself
with
OpenClaw
Copy prompt
When I send you a photo of a handwritten appointment, read the text and add it to my [calendar name] with the date, time, and place. When I forward a PDF by email, file it into [paperless or folder] with a sensible title and tags. Show me each calendar entry and filename before saving, and stop once everything from today&#x27;s batch is filed.
Original source: https://news.ycombinator.com/item?id=49627493</pre>

</details>

## 原作者的方法与来源

[Well, it's much more than that. In general everybody's building agents now. You ... | Hacker News](https://news.ycombinator.com/item?id=49627493)。以下是评论建议与功能举例的短双语摘要，不是已复现的操作记录。

1. 评论者建议构建由个人控制的agent，而不只依赖聊天订阅。
   English summary: The commenter suggests building a personally controlled agent instead of relying only on a chat subscription.

2. 功能举例包括读取手写预约、更新日历、搜索网页，以及将邮件中的PDF归档到本地。
   English summary: Examples include reading a handwritten appointment, updating a calendar, searching the web, and filing an emailed PDF locally.

3. 他们设想以token支出替代订阅，但未提供实现细节、实测结果或分项账单。
   English summary: They sketch token spending as a subscription alternative, without implementation details, measured results, or an itemized bill.

## 我们的简要分析

商业判断：现有证据不支持收费集成业务投入。商业评分未评定；自用价值待核实。

### 归档叙述与原始评论的差别

完整译文忠实保留归档把功能描述成自建agent工作流的说法。实际读到的HN评论则是在举例：个人agent可以识别手写预约、写入日历、搜索网页和把邮件PDF放入本地paperless；没有明确提供一套已经运行的项目或结果。每年15美元token费用也以设想口吻与聊天订阅比较，不是可核对的年度账单。不能把功能主张、可能做法和实际成功记录合并为已验证案例。评论未给代码、OCR工具、模型版本、日历提供商、邮件服务、权限、测试集或归档接口，因此作者方法只能收录短的建议摘要，不能补写成执行步骤。 依据：[archive-case-20261017](https://agentusecases.ai/use-case/add-handwritten-appointments-to-calendar-and-file-pdfs), [Sed47bfd16613](https://news.ycombinator.com/item?id=49627493)。

### 日期识别和写入需要分别验收

读取手写文字只是第一步；日期、年份、开始与结束时间、时区、地点以及目标日历都要有明确来源，模糊的03/04不能静默选择月日顺序。以Google Calendar公开文档为具体参考，日期时间应符合RFC3339，且需偏移或明确时区；这不是识别作者实际日历产品的证据。合成验收可以覆盖模糊日期、缺少年份、全天日程、跨日以及夏令时重复小时，在生成待确认条目后停止。我们用本地时区库演示一个重复小时可对应两个UTC时刻，只验证时间歧义，未做OCR、调用模型或创建日历事件。重复批次也应有可检查的来源标记和重试规则，不能把再读一次照片变成再创建一条预约。 依据：[Sed47bfd16613](https://news.ycombinator.com/item?id=49627493), [S47a5e50a22fc](https://developers.google.com/workspace/calendar/api/v3/reference/events/insert)。

### 附件取得不等于归档完整

以Gmail官方附件方法为例，成功取得的是附件资源，并不会自动形成另一系统中的可检索档案；原作者是否使用Gmail未知。拟议流程应分别核对目标邮件、附件对应、原始文件、拟用标题与标签、保存位置以及最终可读取状态。相同文件名不必然是相同文件，重复批次和中断后的重试也要人工答案样例。Paperless文档本轮返回403，已停止且没有换路读取，因此不声称已核验其具体上传、去重、队列或回执机制，也不认定评论所指版本。只用合成文件与待保存清单即可研究边界，不需要访问真实邮箱、文件库或私人PDF。 依据：[Sed47bfd16613](https://news.ycombinator.com/item?id=49627493), [S7df3405c8543](https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages.attachments/get)。

### 工具身份与资料处理范围

实际agent在归档中标为自建或未命名，OpenClaw只属于源站建议试用模板，不能据此断言评论者使用了OpenClaw。评论中的flash级别也没有明确模型或服务版本，不能套用某个当前模型的费率。拥有代码和本地paperless配置，不足以说明每一步处理都在本地；若未来接远端文字或视觉服务，仍需明确图片、附件与日志的去向。本轮只读公开资料并使用合成样例，未读取私人日历、邮件、文件或聊天，也未建立任何集成。源站模板要求保存前展示日历条目与文件名，这是一条编辑提供的试用约束，不是已经核验的作者确认流程。 依据：[archive-case-20261017](https://agentusecases.ai/use-case/add-handwritten-appointments-to-calendar-and-file-pdfs), [Sed47bfd16613](https://news.ycombinator.com/item?id=49627493), [S47a5e50a22fc](https://developers.google.com/workspace/calendar/api/v3/reference/events/insert), [S7df3405c8543](https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages.attachments/get)。

### 自用价值与替代方式

自用价值待核实。对有能力维护集成并逐项复核的人，潜在用途是把一批手写记录和PDF整理成可确认的待办，而非保证识别正确或无人值守归档。现有手机日历、邮件搜索和手工文件夹整理是直接基线；资料量很少时，维护agent可能比手动录入更重。准备需要字段字典、时区与日期口径、合成照片或文字样例、重复文件规则和人工答案。维护包括权限、服务变更、识别错误、重试与归档核对。没有真实用户规模、准确率、净省时、持续成本或付款证据，不能从评论的轻松语气推断大多数人都能低成本复现。 依据：[Sed47bfd16613](https://news.ycombinator.com/item?id=49627493), [S47a5e50a22fc](https://developers.google.com/workspace/calendar/api/v3/reference/events/insert), [S7df3405c8543](https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages.attachments/get)。

### token估计与总交付成本

评论将token费用与聊天订阅比较，但模型费不含集成搭建、计算与存储、备份、人工确认或错误修复，两类服务范围也不相同。不得将年度token设想直接当作实际净节省。两种规划情景均未验证：一次设置收入300美元，模型/测试预算3、人工6小时×30=180、其他12、获客60，贡献45；多2小时返工则负15。月维护收入19美元，模型1、人工0.4小时×30=12、其他2、获客4，贡献0；人工0.8小时则负12。全部为假设，未扣税和固定费，不是作者支出或平台报价。先核对合成批次的日期、重复与归档状态，关键字段仍须猜测、错误无法重现或维护负担超过手工流程时停止扩大范围；未证明需求之前不开展收费交付。 依据：[Sed47bfd16613](https://news.ycombinator.com/item?id=49627493), [S47a5e50a22fc](https://developers.google.com/workspace/calendar/api/v3/reference/events/insert), [S7df3405c8543](https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages.attachments/get)。

## 自用与试用准备

预览和批次整理可能提供辅助，但原评论未证明已部署效果、准确率、净省时或总维护成本。

准备：纯合成日程和文档说明、目标时区、字段字典、重复规则及人工答案，不含私人资料。

预期：待确认日历条目和归档清单、缺失冲突表及合成验收矩阵；不创建真实事件或文件归档，自编模板未实测。

源站建议OpenClaw模板完整保留在上方原文与译文中，不代表作者实际工具。

### 用合成批次设计日历与文档预览

研究团队自编，未调用模型实测。

    请只使用[纯合成的手写日程文字或图片、合成邮件/PDF说明、字段字典、目标时区和人工答案]，设计一个先预览再确认的批次整理流程。先列出日期、年份、月日顺序、开始/结束、时区、地点和目标日历的缺失与冲突；模糊项不得猜测。区分文字识别、日历草案、附件取得、拟归档清单与最终状态；明确重复输入和中断重试如何被发现。只给出日历条目、文件名、标题、标签和来源的预览，不创建或修改任何真实日历，不读邮箱或私人PDF，不连接文件库，不注册、不创建凭据、不购买、不调用额外付费API、不发送或提交。讨论系统时区库下夏令时重复小时的两种解释，并要求人工选定；不要以15美元年度token设想承诺总成本或用源站建议的OpenClaw冒充作者实际工具。输出预览、缺失/冲突表、合成验收矩阵和未核验接口后停止。本模板是研究团队自编，非作者原话，未调用模型实测。

## 来源

- [Add handwritten appointments to calendar and file PDFs](https://agentusecases.ai/use-case/add-handwritten-appointments-to-calendar-and-file-pdfs)：源站对自建agent、手写预约、邮件PDF和费用估计的转述；原文中的功能举例和假设口吻需另行区分。
- [Well, it's much more than that. In general everybody's building agents now. You ... | Hacker News](https://news.ycombinator.com/item?id=49627493)：原始评论举例说明可自建agent及token与订阅费用的设想，没有代码、部署记录或经核对账单。
- [Events: insert  |  Google Calendar  |  Google for Developers](https://developers.google.com/workspace/calendar/api/v3/reference/events/insert)：Google官方说明日期时间格式与时区等事件字段，供验收设计参考；不证明作者实际使用Google日历。
- [Method: users.messages.attachments.get  |  Gmail  |  Google for Developers](https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages.attachments/get)：Google官方附件获取方法返回MessagePartBody；附件取得与归档是不同动作，不证明作者使用Gmail。
