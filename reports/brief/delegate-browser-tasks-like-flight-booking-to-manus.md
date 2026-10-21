# 用 Manus 处理旅行查询与浏览器预订事务

## 中文

    将订机票等浏览器任务交给 Manus
    评测者用 Manus 处理提取邮件登录验证码、预订航班等浏览器任务，认为它逐步点击界面的方式很慢，并更偏好 Claude。
    使用工具
    MA
    Manus
    GA
    ChatGPT Agent
    CL
    Claude
    做了什么
    使用 Manus 约一个月后，评测者尝试让它充当旅行事务的浏览器助手：预订航班和火车、从 Gmail 提取旅行信息，并添加到 Google Calendar。评测者也期望 Manus 自行获取邮件登录验证码，但实际不得不进行大量监督，有时还要亲自接手。
    结果如何
    对这些浏览器任务，评测者认为得不偿失：他们花了1.5小时监督原本以为15分钟就能完成的工作，最后仍自己完成了部分步骤。一次夜间运行还在等待登录验证码的步骤中耗尽了剩余的全部额度，而 Manus 本来已经获得处理该步骤的许可。
    值得注意
    主要问题是额度消耗与时间成本：一次无人看管的会话运行了一整夜，并耗尽账户剩余额度。
    亲自试用
    使用
    Manus
    复制提示词
    查找从[出发地]到[目的地]的最佳往返航班，[日期]出发、[日期]返回，预算为[金额]，偏好[直飞、上午出发等]。按价格、时长和中转比较至少[3]个选项，给出简短的排序清单及链接。在向我展示确切航班、价格并得到我的批准之前，不要输入付款信息，也不要预订任何行程。
    原始来源：https://www.reddit.com/r/AI_Agents/comments/1ry9biu/manus_vs_chatgpt_agent_claude_chat_won_my_review

<details><summary>English original</summary>

    Delegate browser tasks like flight booking to Manus
    Reviewer used Manus for browser tasks such as fetching an email login code and booking flights, finding it slow from clicking through the UI, and preferred Claude.
    Done with
    MA
    Manus
    GA
    ChatGPT Agent
    CL
    Claude
    What they did
    After about a month with Manus, the reviewer tried using it as a browser agent for travel admin: booking a flight and a train, pulling travel details from Gmail, and adding them to Google Calendar. Manus was also expected to fetch an email login code on its own, but instead the reviewer had to supervise it heavily and at times take over.
    How it went
    For these browser tasks, it was a net negative: the reviewer spent 1.5 hours overseeing work they thought should take 15 minutes, and eventually did parts themselves. An overnight run also used up all remaining credits while waiting on a login-code step Manus already had permission to do.
    Worth knowing
    The main catch was credit burn and time drain: one unattended session ran all night and exhausted the account’s remaining credits.
    Try it yourself
    with
    Manus
    Copy prompt
    Find the best round-trip flights from [origin] to [destination] departing [date] and returning [date], with a budget of [amount] and a preference for [nonstop, morning departure, etc.]. Compare at least [3] options by price, duration and layovers, and give me a short ranked list with links. Do not enter payment details or book anything until you show me the exact flight and price and I approve.
    Original source: https://www.reddit.com/r/AI_Agents/comments/1ry9biu/manus_vs_chatgpt_agent_claude_chat_won_my_review

</details>

## 目录转述方法

目录描述了尝试预订旅行、从Gmail读取行程并添加日历事件。
The directory describes attempts to book travel, read trip details from Gmail, and add calendar entries.

评测者称需要大量监督和人工接手，一次夜间会话还消耗了剩余额度。
The reviewer reports substantial supervision, manual takeover, and an overnight credit-consuming session.

## 结论

缺原评测回放、出票收据和额度明细，负面体验不可泛化；以有依据简报保留流程、成本与边界。
先证明节省总人工时间，再扩展到有外部副作用的步骤

## 负面体验保留，但不泛化成产品判决

原案的明确线索是旅行事务的监督负担：评测者尝试订航班、火车、读旅行邮件并写日历，却不得不反复介入。90分钟相对预期15分钟，是使用者对该次任务的评价，不是控制了路线、设备和网站条件的实验。未取得任务回放、实际出票状态、剩余额度起点或消耗分解，不能算每次预订的真实价格，也不能给产品总体失败率。原目录还标了ChatGPT Agent与Claude，本篇保留这些工具但不编造三者同题测试结果；推荐试用模板只指定Manus，不是原作者真实指令。

来源：Sdirectory

## 使用者与潜在付款人

经常出差的人可能愿意减少多网站比价、核航班和归档日历的操作；企业行政或旅行负责人则可能掌握预算。但旅行预订不是只有填表，改签、行李、转机、时区和实际出票都影响价值。一个人偶尔出游时，花时间配置浏览器权限不一定划算。若做服务，客户支付的应是可核验的候选和准确行程信息，不应把无人看管的点击次数当交付。当前没有付费客户、报价、复购或佣金记录，所有商业化设想仍待验证。

来源：Sdirectory, Sflights

## 把查找、登录、预订、出票分成状态

可复制流程应先只读查询并保留候选，再明确所选航班、总价、币种、旅客、行李及退款限制，只有用户授权才进入预订。验证码只能用于相应服务的本次登录，取到验证码不等于已经完成预订；页面付款成功也要与订单编号及出票凭据区分。日历应最后基于确认行程生成，并回读时区和航段，而不是把搜索候选当真实旅行。本研究没有取任何邮件验证码，也没有访问个人账户、预订或付款。提出这些状态边界是为避免重复副作用，不是声称原评测已有这样的实现。

来源：Sdirectory, Scalendar

## 夜间运行为什么需要停止规则

官方额度说明区分活跃处理和已完成产物存放，因此原案夜间消耗只能表述为该会话的自述结果，不能认定系统对静止页面整晚收费。可能持续存在推理、浏览器重试或其他处理，但缺日志无法确定。试点应在开始前限制允许的网站、尝试次数、人工等待和最高费用；遇登录或付款关口及时暂停并保存当前任务状态，而非用重复点击假装进展。记录每次尝试是否已经成功，再决定重试，避免重订。复杂浏览器任务的可预期成本来自可观测状态和停止边界，不是把代理长时间开着。

来源：Scredits, Sdirectory

## 哪些步骤已被现成产品解决

Google Flights已经提供不同排序口径和航班比较，便宜不一定满足方便与风险偏好；这些原生能力应先作为基线。支持的确认邮件进入Google Calendar也是现成能力，但必须检查账户与地区设置以及邮件类型，不能宣称任何旅行邮件都自动识别。若只需一次比价和日历归档，原生工具加人工确认可能比跨站代理更简单。Manus当前优先浏览器可复用授权的登录环境，但依赖设备在线和账号发布状态，不能把这一现有功能倒推成历史失败已经解决。

来源：Sflights, Scalendar, Sbrowser

## 按完成并核对的一次行程事务计算

两种情景均为研究者假设。轻量辅助：模型与运行摊销3美元、人工20分钟按30美元每小时计10、其他可变费用1、获客3，已列17美元；每月10单加固定维护20，共190美元。高监督：工具12、人工90分钟计45、其他3、获客8，已列68美元；每月10单加固定维护40，共720美元。票款不是服务收入，真实服务售价未知，所以不计算毛利或收益率。退款纠纷、责任承担和机构审批成本没有数据，另列待核。原案的90分钟不能直接套在每个客户身上；这两个场景只是说明人工监督如何吞掉工具节约。

来源：Scredits, Sdirectory

## 先卖清晰结果，不卖无边界代办

若验证经营机会，先限定为公开票价与行程条件比较包，不接管支付和敏感身份资料。交付三条有来源、时间与限制的候选，以及需要用户决定的问题，后续如需订票必须另有明确范围。获客可以从已有行政服务关系或重复差旅需求开始验证，但本任务不联系任何人。壁垒更可能是对企业出行规则、异常处理和可靠资料归档的理解，而不是使用同一款浏览器代理。若客户直接用现成搜索即可满足，就没有理由为通用截图和摘要再付费。

来源：Sflights, Sbrowser

## 常用登录态也意味着更大的误操作范围

优先浏览器的好处是少重复登录，但这也把更多已登录系统放到可操作环境中。设置时应只授权确有需要的浏览器和标签，不能因为一个旅行任务就把全部私人邮箱和工作系统开放。跨站网页说明、广告或评论不是用户的新指令。自动化需要能够停止，并保留停止后的状态；关闭标签的产品介绍不能替代实测停止是否及时。对于不可逆的预订或付款，保留用户确认和具体收据；本轮只分析，不创建长期访问、不保存凭据。

来源：Sbrowser, Sextension

## 反馈与最小验证

公开搜索找到另一篇2025年旅行规划体验，描述等待与消耗，但任务是行程规划加网页制作，不能算本案订票的第二个复验样本。官方资料解释能力与计费，不等于满意度。原始评测完整帖子在既有读取限制下未访问，不把搜索片段当完整日志。最小验证可从公开三航班比较开始，同一查询分别人工和代理执行，记录总人工分钟、等待、费用和错误，再核最终链接是否仍对应日期与路线。无法给出明确候选、出现重复订单风险、消耗超过事先预算或监督时间超过人工基线，就停止扩展，不以四周或200美元作统一质量门槛。

来源：Sreview, Sdirectory, Sflights

## 自用与试用

- 原案有明显监督负担，缺同条件复验。
- 有重复差旅事务、能检查票务条件的人。
- 只读候选比较、确认后整理行程资料。
- 可能减少跨页整理，但原案没有净正收益证明。
- 定义行程、预算、合法授权和可停止浏览器环境。
- 登录、网页变化、额度、故障与订单核对。
- 随出行发生，低频使用未必值得配置。
- 旅行信息、登录邮件与已授权浏览器账户暴露。
- 日期时区错、漏行李费、重复预订、把候选当出票。

公开行程条件、预算和不预订边界；无需提供私密邮件或支付资料。
三条可核验候选及限制，未执行预订或出票。

## 来源

- [Sdirectory · 许可目录：Manus旅行事务评测](https://agentusecases.ai/use-case/delegate-browser-tasks-like-flight-booking-to-manus)：目录转述评测者监督90分钟而原预期15分钟、部分步骤人工接手、夜间会话耗尽剩余额度；没有完整轨迹或账单复验，不证明普遍失败率。
- [Scredits · Manus官方额度说明](https://manus.im/help/credits)：额度与模型token、虚拟机及第三方服务有关，官方称只在活跃处理时消耗，完成任务和产物存放不耗额度；不能仅凭“等待验证码”推定静止等待收费。
- [Sbrowser · Manus Preferred Browser说明](https://manus.im/blog/manus-preferred-browser)：可选择已授权、保持登录与联网的Chrome作为优先浏览器；可用性按账号及发布状态变化，不能证明原评测当时用了此配置。
- [Sextension · Manus官方浏览器扩展页](https://chromewebstore.google.com/detail/manus-ai-browser-operator/cecngibhkljoiafhjfmcgbmikfogdiko)：开发者说明可在指定标签中操作并通过关闭标签停止；本轮只读介绍，未安装或接受权限。
- [Sflights · Google Flights官方比较说明](https://support.google.com/travel/answer/7664728?hl=en)：Best与Cheapest排序目标不同，低价可能涉及自转行李或不同机场；结果不覆盖所有报价，最终条件仍需核对。
- [Scalendar · Google Calendar的Gmail事件](https://support.google.com/calendar/answer/6084018?hl=en)：支持的航班、火车等确认邮件可自动生成并更新日历事件，但依账号、地区和智能功能设置；抄送、转发等情况有限制。
- [Sreview · 2025年4月个人旅行规划体验](https://en.dulichdau.com/2025/04/manus-ai-review-promising-travel.html)：作者自述行程规划响应15至20分钟、再生成网页耗较多额度；是历史异任务体验，非实际出票、当前价目或本案复验。

## 核验边界

原帖完整内容未读；云浏览器案例导航11:48:43超时，使用已有许可归档及支持的公开网页读取。没有取验证码、登录、订票、付款、安装或任何实时行程测试。历史体验与现行功能分开。
