# 用 ChatGPT 销售代理寻找网页设计客户

## English

    Find web design prospects with sales agents
    The poster set up multiple agents that sell web services, including one that searches Google Maps for businesses, checks for websites and ranks them by priority.
    Done with
    GP
    ChatGPT
    What they did
    The poster says they chained six agents in OpenClaw on a cheap always-on server, using ChatGPT or Claude plus Google Places API, Twilio, and ElevenLabs. For prospecting, the first agent searched a chosen city and business type, checked Google Maps listings for websites, tested speed and mobile experience, flagged businesses with no site as high priority, and ranked leads; later agents diagnosed issues, built a demo site and videos, sent email and SMS outreach, and prepared the poster for reply calls.
    How it went
    The stated result for this prospecting step is a daily ranked list of businesses to contact without manual searching. But the thread gives no conversion, revenue, or close-rate numbers, and commenters repeatedly ask for proof the system actually makes money.
    Worth knowing
    The only concrete operating cost stated is a cheap server at about $5-10 per month, plus separate paid services like Twilio, Google Places API, and ElevenLabs.
    Try it yourself
    with
    Claude in Chrome
    Copy prompt
    Search Google Maps for [type of local business] in [city or area] and collect at least [number] results. For each, record the name, phone, address, rating, review count, and whether it has a website and whether that site looks outdated or not mobile friendly. Rank them from best to worst prospect for my [web design or other] services, with no website at the top, and put the result in a table with a one-line reason for each. Stop when the table is complete and do not contact anyone.
    Original source: https://www.reddit.com/r/passive_income/comments/1rmsb2o/i_set_up_6_ai_agents_that_sell_web_services_24_7

## 中文

    用销售代理寻找网页设计潜在客户
    发帖者搭建了多个销售网站服务的代理，其中一个会在Google Maps上查找商家、检查其是否有网站，并按优先级排序。
    实际使用
    ChatGPT
    具体做法
    发帖者称，他们在一台廉价、始终运行的服务器上，用OpenClaw串联了六个代理，使用ChatGPT或Claude，并结合Google Places API、Twilio和ElevenLabs。在寻找潜在客户这一环节，第一个代理会按选定城市和商家类型进行搜索，检查Google Maps商家信息中是否有网站，测试网站速度和移动端体验，将没有网站的商家标为高优先级，并对销售线索排序；后续代理则诊断问题、制作演示网站和视频、发送推广邮件和短信，并帮助发帖者为回复电话做好准备。
    结果如何
    据称，这一寻找潜在客户的步骤每天会生成一份按优先级排列的待联系商家名单，无需人工搜索。但帖子没有给出转化、收入或成交率数据，评论者也反复要求提供系统确实能赚钱的证据。
    值得知道
    唯一明确给出的运营成本是每月约5–10美元的廉价服务器，此外还要另外支付Twilio、Google Places API和ElevenLabs等服务的费用。
    自行试用
    推荐工具
    Claude in Chrome
    复制提示词
    在Google Maps上搜索[城市或地区]的[本地商家类型]，至少收集[数量]条结果。对每家商家记录名称、电话、地址、评分、评论数量，以及是否有网站、网站是否显得陈旧或对移动设备不友好。根据其作为我的[网页设计或其他]服务潜在客户的适合程度，从高到低排序，把没有网站的商家放在最前面，并整理成表格，每家附上一句理由。表格完成后就停止，不要联系任何人。
    原始来源：https://www.reddit.com/r/passive_income/comments/1rmsb2o/i_set_up_6_ai_agents_that_sell_web_services_24_7

## 原作者的方法与来源

来源：[六代理销售网站服务的原始讨论](https://www.reddit.com/r/passive_income/comments/1rmsb2o/i_set_up_6_ai_agents_that_sell_web_services_24_7)

方法摘要未收录

## 我们的分析

**商业结论：适合内部效率工具。先给已有网页设计业务整理候选名单，不把自动名单包装成自动成交**

这条流程可帮助已有作品和交付能力的设计师减少重复整理，付款人更可能是网页设计机构的负责人，而不是名单中的商家。源站没有成交或收入证据，缺少网站也不表示商家愿意购买。地图数据使用条件、去重核实、演示制作和后续销售都要计入成本，5–10美元服务器费不足以说明盈利。先在已获准使用的数据上验证筛选准确度和人工时间，暂不投入六代理全天自动推广系统。

案例ID：`find-web-design-prospects-with-sales-agents` · 案例来源：https://agentusecases.ai/use-case/find-web-design-prospects-with-sales-agents
研究时间：2026-10-16T14:06:28.136453+00:00

**商业评分：36.0/100。用户反馈信号占5%。**

| 维度 | 权重 | 分数 /5 | 商业依据 |
|---|---:|---:|---|
| 付费需求 | 20% | 2 | 已有设计机构有持续筛选任务，但未展示愿意为本系统付费的客户或续费。 [Sd4c9e751639d, S17a36a249e3e] |
| 业务价值与效果证据 | 20% | 2 | 每日候选表是明确交付物，源站无节时测量和成交证明，不能由名单数量推断收入。 [Sd4c9e751639d] |
| 单位经济与利润 | 20% | 2 | 小规模内部筛选可能划算，对外名单服务的复核与销售成本会迅速侵蚀毛利。 [Sd4c9e751639d, S38fbdb77172f, S637a9f50ee08] |
| 获客与市场进入 | 15% | 2 | 已有设计客户与行业作品可支持试点，缺少平台以外的实际获客转化证据。 [Sd4c9e751639d, S17a36a249e3e] |
| 竞争壁垒 | 10% | 1 | 网页审计和名单整理可被现成工具覆盖，六代理编排本身不形成客户迁移成本。 [S17a36a249e3e, S29f73194612d] |
| 交付与经营风险 | 10% | 2 | 可限制在只读筛选，但数据许可、误判、触达要求和平台故障需要人工处理。 [S181224018b60, S001b96847a15, S194ba0c87fd7, S5cb4111647e0] |
| 独立用户反馈信号 | 5% | 0 | 只有邻近工具用户反馈，没有本六代理系统独立使用和盈利验证；零表示证据缺失。 [Sd4c9e751639d, S637a9f50ee08, S5cb4111647e0] |

## 自用价值：中

对已有网页设计经验的人，整理有限候选和核对网页问题有辅助价值；这是基于流程的推断，未证明节省时间或增加订单，与商业评分分别判断。

依据：Sd4c9e751639d, S181224018b60, S29f73194612d

- 适用人群：已有设计作品、能判断网站问题和服务适配度的独立设计师或小机构人员。
- 用途：整理已获准研究的商家信息、证据和待核实项，准备人工评估名单。
- 预期收益：有机会减少重复整理并统一比较格式；没有实测节时、回复率或收入。
- 设置成本：先准备合法可用的小名单、服务范围和判断标准；可用现有浏览器或对话工具处理已有材料。
- 维护成本：复查网站与经营状态，处理重复、过期和无证据判断；需要人工持续抽查。
- 使用频率：在业务需要补充候选时按小批次使用，无需为了运行代理每天扩充名单。
- 隐私风险：尽量不收集私人号码、邮箱与不必要个人信息；保留来源用途限制，不把公开电话视为推广许可。
- 错误风险：地图未列网站不等于商家没有网站；页面速度、审美与购买意愿需要分别判断。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/find-web-design-prospects-with-sales-agents

建议工具：Claude in Chrome

    Search Google Maps for [type of local business] in [city or area] and collect at least [number] results. For each, record the name, phone, address, rating, review count, and whether it has a website and whether that site looks outdated or not mobile friendly. Rank them from best to worst prospect for my [web design or other] services, with no website at the top, and put the result in a table with a one-line reason for each. Stop when the table is complete and do not contact anyone.

自编试用模板

准备条件：提供10–20条已获准用于此次研究的商家资料与网页截图或文本，注明日期和来源；写清自己的服务范围。

工具：现有对话工具即可分析提供的材料；如用浏览器，只读取允许访问的公开页面，不创建凭据或调用额外付费服务。

预期结果：一份可复核候选表、误判风险与缺失信息清单；以下模板自编，未实测，不承诺获客。

### 自编模板：只整理候选，不自动推广

自编模板

出处：研究团队自编

依据：Sd4c9e751639d, S181224018b60, S001b96847a15

    我的网页设计服务范围是[行业、地区、项目类型和预算范围]。请仅根据我提供且获准用于本次研究的[商家名单、网页截图或文本、来源和日期]整理候选表。每家列出名称、已知网址、可核实的网站问题、证据与日期、服务匹配理由、待核实事项和优先级。资料未列网站时写“未列出”，不要推断没有网站；不要猜测预算、个人联系方式或购买意愿。先去重，再把证据充分且与服务匹配的对象排前；证据不足单列。不要注册、付款、调用额外收费API、绕过访问限制、发送邮件或短信、联系商家、制作并发布商家演示站。输出后列出我需人工复核的三类问题并停止。

## 已核验事实

- 源站称六个OpenClaw代理串联查找、诊断、演示制作与推广；顶部实际工具标签是ChatGPT，正文同时提到Claude。 [Sd4c9e751639d]
- 源站明确没有转化、收入或成交率数据；评论者要求盈利证明这一点只是汇编转述，本研究没有独立读取评论。 [Sd4c9e751639d]
- 源站唯一明确基础费用为约5–10美元/月服务器，另有Places、Twilio、ElevenLabs等付费服务。 [Sd4c9e751639d]
- 源站试用工具是Claude in Chrome，提示词在名单完成后停止，不联系任何人；它不是原作者六代理配置。 [Sd4c9e751639d]
- Places政策限制预取、缓存和存储其内容，place ID属于可长期存储的例外；无地图展示仍有归属要求。 [S181224018b60]
- Places按请求涉及的最高SKU计费，字段掩码可减少不必要字段；调用需要结算与API密钥或OAuth令牌。 [S38fbdb77172f]
- Twilio政策要求发送前取得适用的明确同意并保留证明，接收方可撤回同意。 [S001b96847a15]
- FTC说明CAN-SPAM要求不豁免B2B商业邮件，涵盖真实发件身份、地址和退订方式。 [S194ba0c87fd7]
- BrightLocal机构产品提供本地审计、白标报告和让访客主动提交商家资料的获客组件。 [S17a36a249e3e]
- Outscraper社区2024年费用讨论将附加信息服务列为额外收费原因；不能据此给出当前单价。 [S637a9f50ee08]
- Outscraper社区有任务延迟报告；厂商2025年12月回复称已修复当时问题，2026年又有用户报告等待。 [S5cb4111647e0]
- BrightLocal 2026调查基于1002名美国成年人，通过SurveyMonkey完成；不能外推为无网站商家的购买率。 [S8c4f8af2a909]

## 谁使用、谁付款，以及名单解决什么问题

直接使用者是已有网页设计交付能力、需要定期寻找本地客户的独立设计师或小机构销售人员。若购买的是名单整理服务，付款人通常是机构负责人，预算来自获客或销售支持；名单里的餐馆、维修店和其他商家则是未来网页项目的潜在付款人。这是两次不同的购买决策，不能把发现一家没有网站的店直接当作获得设计订单。机构还要判断其服务价格、行业经验与商家的经营需求是否匹配。
源站只说明每天得到排序名单，没有展示机构愿意为这种名单支付多少钱。一个已有稳定转介绍渠道、订单排满的设计师，未必需要每天更多线索；缺少作品与交付流程的新手，也不会因为名单增加就自然成交。应先访谈正在反复手工查店、筛网站的团队，记录每周筛选量、无效数据比例、销售跟进能力和目前花费。把交付定义为有依据的候选资料及待核实项，避免承诺“高意向客户”。无网站、评分高低和评论多少只是筛选信号，购买时间、预算和决策人均需另外确认。

依据：Sd4c9e751639d, S17a36a249e3e

## 从搜索名单到销售之间还缺哪些步骤

案例自述把六个代理串成一条链：搜索城市与业态，核查网站及速度和移动体验，诊断问题，制作演示网站与视频，发送推广，再协助真人接听回复电话。可见的成果集中在前端排序表，未提供完整任务代码、各代理提示词、错误重试规则或交接日志。OpenClaw官方浏览器文档支持独立浏览器环境及页面读写操作，但这只能证明通用能力存在，不能证明该作者的六个角色已经稳定协同。
可复制的小步骤应是先限定城市、行业和来源，取得获准使用的商家候选资料，统一商家名称与地址，去掉重复和停业记录，再检查链接是否仍有效。Google Maps没有网站链接，应写“该条目未列出”，还需查验商家是否使用其他域名或平台店铺；网页旧、加载慢也需要测试时间、设备和具体证据。之后按服务适配度排序，附人工复核字段。任何演示制作、发送消息和客户承诺都另行处理。源站提供的Claude in Chrome模板只到表格完成，不能把它称为原作者全部系统。

依据：Sd4c9e751639d, S29f73194612d

## 可进入的市场是明确的一类设计客户

本地商家确实会被消费者在线查找和核实，但这不等于所有商家都有独立建站需求。BrightLocal的2026年消费者调查涉及1002名美国成年人，描述人们阅读评价后还会利用网站、社交页面等渠道核实信息；这是消费者行为资料，不是商家采购预算调查，也不能用它估算网页设计客户转化率。该公司本身销售本地营销软件，市场材料带有供应商立场。
适合首先验证的范围是一座城市中的一种业态，以及有相应作品的设计服务。例如可检查预约入口是否难找、移动端联系按钮是否失效，把问题连接到具体业务任务；这仍须商家自己确认价值。缺站商家可能主要依靠转介绍、平台页面或总部统一网站，甚至暂不接新客户。若一律把无网站排第一，容易把不愿购买者排在最前。可进入规模应从可合法使用的数据、真实经营状态、服务匹配和后续销售能力逐层缩小，再按已观察到的合格比例计算。当前资料不足以给出总市场金额或年收入预测。

依据：S8c4f8af2a909, Sd4c9e751639d

## 现成工具和人工流程为何仍有竞争力

最直接的替代是设计师自己用已获准使用的名单、浏览器和表格做小批量审查。它缺少全天自动运行，但初期无需维护六个代理，且能解释为何某个问题值得修复。BrightLocal面向机构的产品已经提供本地审计、白标报告和访客主动提交商家资料的获客组件。后者需要机构本来就有网站流量，并不能凭空提供客户，但主动请求审计与被动出现在地图中的商家有不同的意向强度。
本案例的潜在差异在于把多步整理连在一起，并按设计师的服务范围输出说明；不是新的原始数据来源，也不是独家获得需求。若卖名单，客户会比较自己用工具筛选和付费委托的总时间、有效率及可追溯性。若卖完整设计项目，又要与已有作品、售后和行业经验的服务商竞争。原方案涉及的外部服务不是只买服务器就能替代的。Outscraper现行定价页未能读取，本研究不使用旧社区报价给它标出“更便宜”的当前价格，也不将抓取产品的存在视为取得所有数据再利用许可。

依据：S17a36a249e3e, Sd4c9e751639d, S637a9f50ee08, S181224018b60

## 成本应算到合格交付与真正成交

第一种假设是对机构交付一批100条经过核实的候选资料，收费150美元。数据与模型预算15美元，人工4小时按25美元计100美元，其他处理5美元，获客摊销20美元，每批成本140美元，仅剩10美元贡献。每月10批且固定开销100美元时恰好持平。若复核提高到每条4分钟，人工约166.67美元，单批已亏损56.67美元。这里的4小时还必须覆盖筛出不合格候选的时间，不是只计算最终留下的100条。
第二种假设把寻找客户算入网页设计项目：每个完成项目收费1200美元，API与模型50美元，人工20小时按30美元计600美元，其他工具和演示托管50美元，销售获客摊销200美元，贡献300美元；每月3单、固定开销300美元，月贡献减固定费用后为600美元。20小时必须包括摊到成功项目上的失败演示和沟通时间，若返工使其达到30小时，单单贡献归零。这些数字均为敏感性假设，没有实收订单支持。Places字段组合影响计费，附加数据服务与失败重试也需计入；源站5–10美元服务器费不能代表全链路成本。

依据：Sd4c9e751639d, S38fbdb77172f, S637a9f50ee08

## 先证明筛选质量，再谈卖给别人

第一批验证对象应来自已有设计师同行、合作机构或正在使用相同销售流程的熟悉团队，以同一批资料做对照：人工原流程与代理辅助流程分别花多久，哪些对象被错误排前，哪些确有可解释的网站问题。先交付带证据的少量样张，让负责人判断是否值得替代现有做法。只有名单实际改善销售准备，才有理由讨论按批次或按月付费；本研究不代表已经联系任何人或完成客户访谈。
获客演示应展示可核实的改进机会与信息来源，不使用“全天自动销售”“保证获得客户”等未经验证的表述。若机构希望吸引主动需求，可以比较BrightLocal这类自助审计入口，但它也依赖流量、作品和可信的后续服务。对外销售名单时，还应解释来源使用范围、更新日期、重复处理与退款边界。销售项目时要展示设计与维护能力，而非把代理数量作为购买理由。长期记录合格率、人工复核时间和真实付费反馈，比累计搜索条目数更能判断渠道是否成立。

依据：Sd4c9e751639d, S17a36a249e3e

## 角色数量不是经营壁垒

六个角色分别搜索、评估和制作材料，属于容易复现的流程分工；OpenClaw的通用浏览器能力以及现成本地审计软件都降低了搭建门槛。因此，单靠把公开商家数据排成表格，很难让客户长期接受高价。自动化也会让竞争者同时接触相同商家，如果资料没有新的证据或明确行业理解，更多输出反而可能加重无差别推销。
可能形成积累的是某一行业的网站问题分类、真实项目中的修复效果、去重与误判记录，以及获得客户许可后保存的销售反馈。但这些是未来经营需要建立的资产，不是案例已经展示的成果；保留数据时还应分别处理第三方内容使用限制。机构与客户之间的信任、真实案例和持续维护责任，同样无法由一次模型调用复制。应衡量历史反馈能否让下一批筛选更准确、是否降低人工成本，若数周后仍只凭无网站这一项排序，就没有足够理由投入自建平台或向外出售订阅。

依据：Sd4c9e751639d, S17a36a249e3e, S29f73194612d, S181224018b60

## 数据使用、触达和故障如何影响交付

Places政策对预取、缓存和保存内容有限制，place ID有例外，展示结果也有归属要求。因此，不能默认API返回了电话、评分就可长期保存并转售完整数据库；真正经营前需按所用来源、地区与用途确认使用条件。这个限制会影响刷新频率、存储结构、客户交付形式和成本，而不是在报告末尾加一句提示就算解决。源站试用模板保持原样收录，并不表示本研究认可其在任何规模和用途下均可执行。
后续推广的边界也不同：Twilio要求适用的明确同意及证明，公开电话号码本身不满足这一要求；FTC的美国商业邮件说明同样涵盖B2B，要求真实身份、地址和退订等。不能把短信规则直接套成全部国家邮件规则，也不据此判断原作者已经违规。实际交付要建立退订与人工审批环节，限定地区和渠道。邻近抓取工具曾有任务延迟，需防止重复扣费、重复名单和重复联系；只读研究阶段可暂停并标记未知，不以自动重试突破页面限制。

依据：S181224018b60, S001b96847a15, S194ba0c87fd7, S5cb4111647e0

## 邻近工具反馈说明了什么

相关体验：用户与厂商讨论额外数据服务导致账单高于预期，提示完整费用需要逐项核对。

相关体验：用户报告任务延迟，厂商称修复当时问题，后续仍有等待反馈；交付应留异常处理时间。

依据：Sd4c9e751639d, S637a9f50ee08, S5cb4111647e0

## 先验证内部准备价值，暂不扩大自动推广

综合判断是适合内部效率工具，商业评分36/100。它能把重复的商家查找和网页问题整理成一个可复核步骤，最适合本来就知道如何判断需求、定价和交付的设计师。缺少销售能力的人不应把每日名单理解为稳定收入，也没有依据购买整套六代理自动销售系统。商业评分评价经营投入证据，自用价值另列为中：一次有限范围整理可有帮助，但仍需要输入准备和人工判断。
下一步用20家已获准研究的商家做不触达试验，提前写清服务范围和合格定义，记录所有被筛掉对象的耗时。建议试验目标为至少80%候选可核实且符合服务范围、总人工时间比原流程减少25%；这只是验证门槛，不能写成结果。若无网站误判超过10%、名单不能帮助筛选，或数据使用条件无法满足，应停止扩大。即使内部效率达标，对外收费仍须另做真实客户验证，并计入沟通、退款和维护成本。没有成交证据前，最合理的交付仍是一份有依据的准备清单。

依据：Sd4c9e751639d, S181224018b60, S17a36a249e3e, S637a9f50ee08, S5cb4111647e0

## 单位经济测算：情景假设，不是项目已实现的财务结果

| 情景 / 交付单位 | 收入 | 可变成本（含获客） | 单位贡献 | 月交付量 | 月固定成本 | 月经营贡献 |
|---|---:|---:|---:|---:|---:|---:|
| 假设：对机构销售核实后的候选批次 / 100条合格候选资料/批 (USD) | 150.00 | 140.00 | 10.00 | 10 | 100.00 | 0.00 |
| 假设：自用获客辅助完成网页设计项目 / 已付款并完成交付的网页项目 (USD) | 1200.00 | 900.00 | 300.00 | 3 | 300.00 | 600.00 |

假设：对机构销售核实后的候选批次假设：全部是规划假设，未实售。人工4小时×25美元含被剔除记录的筛选与最终复核；API/模型15美元不是服务商报价，其他5美元用于格式与交付，获客摊销20美元，固定100美元。须先确认数据使用允许该交付。单批贡献10美元，月贡献减固定后0；每条4分钟时人工约166.67美元，单批贡献约-56.67美元。；API成本 15，人工成本 100，其他可变成本 5，分摊获客成本 20。依据：Sd4c9e751639d, S38fbdb77172f, S637a9f50ee08, S181224018b60

假设：自用获客辅助完成网页设计项目假设：全部为假设，无已取得订单。20小时×30美元包括设计、复核、沟通及失败演示分摊；API/模型50美元、演示托管与工具50美元、其他获客支出200美元，月固定300美元。单位贡献300美元，三单减固定后600美元；人工30小时则单位贡献为0、月度为-300美元。持续维护另定范围，未将未来项目年化计作收入。；API成本 50，人工成本 600，其他可变成本 50，分摊获客成本 200。依据：Sd4c9e751639d, S38fbdb77172f, S17a36a249e3e

## 反证与未核实信息

最重要的反证是源站没有任何成交或收入数据，现成工具已覆盖审计与获客入口；无网站排名还可能偏向低购买意愿对象。地图内容许可和短信同意条件让“公开名单自动推广”不能直接作为可经营默认路径。

没有读取原始Reddit讨论，不推断完整六角色提示词、代码或真实账单。未实测任何代理、不发送消息、不购买数据、不调用收费API。Outscraper价格页403、Trustpilot robots限制均未重试；不提供其现价或评分。调查仅覆盖美国成年人且由供应商发布。所有经济数字与试验门槛是假设。

## 具体动作与止损条件

用20家已获准研究的商家做一次不联系外部的人工对照，记录有效候选率、误判和每条复核时间；达到预先设定的80%可核实且适合目标服务、总人工时间降低25%后，再由业务负责人决定是否做付费客户验证。阈值是试验目标，尚未达成。

停止投入条件：若无站误判超过10%、候选名单不能改善现有筛选时间，或数据使用与触达条件无法满足，停止扩大自动化；不要以发送量掩盖没有真实需求。

## 来源与对应关系

- [Sd4c9e751639d] [Find web design prospects with sales agents with ChatGPT | Agent Use Cases](https://agentusecases.ai/use-case/find-web-design-prospects-with-sales-agents)：案例自述的六代理流程、5–10美元服务器费、无收入证明及源站只读试用模板。
- [S181224018b60] [Policies and attributions for Places API  |  Places API (New)  |  Google for Developers](https://developers.google.com/maps/documentation/places/web-service/policies)：Places内容的缓存限制、place ID例外及展示归属要求。
- [S38fbdb77172f] [Places API Usage and Billing  |  Places API (New)  |  Google for Developers](https://developers.google.com/maps/documentation/places/web-service/usage-and-billing)：Places按请求SKU收费、字段掩码影响计费、需要启用结算；不沿用过期额度。
- [S001b96847a15] [Twilio Messaging Policy | Twilio](https://www.twilio.com/en-us/legal/messaging-policy)：Twilio消息发送前的同意、证明与撤回机制。
- [S194ba0c87fd7] [CAN-SPAM Act: A Compliance Guide for Business | Federal Trade Commission](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business)：美国商业邮件要求也涵盖B2B；真实身份、邮寄地址及退订。
- [S29f73194612d] [Browser (OpenClaw-managed) - OpenClaw](https://docs.openclaw.ai/tools/browser)：OpenClaw隔离浏览器、页面读取与操作能力，不证明作者配置实际运行。
- [S8c4f8af2a909] [LCRS 2026: Study Shows Reviews Matter More Than Ever - BrightLocal](https://www.brightlocal.com/research/local-consumer-review-survey/)：2026年美国1002名成年人调查的消费者核实习惯；不是网页设计采购意向调查。
- [S637a9f50ee08] [Outscraper price overcharging - Questions - Outscraper Community](https://community.outscraper.com/t/outscraper-price-overcharging/387)：2024年社区用户对费用及附加数据服务的讨论，非当前报价。
- [S5cb4111647e0] [Google Maps Scraper Not Working [Solved] - Feedback - Outscraper Community](https://community.outscraper.com/t/google-maps-scraper-not-working-solved/708)：2025–2026年抓取延迟反馈及厂商修复回复，非本案例故障率。
- [S17a36a249e3e] [Local SEO Tools for Agencies | Trusted by 6,000+ SEO Agencies](https://www.brightlocal.com/agencies/)：现成机构工具的本地审计、白标报告及主动提交资料的获客组件。

结构化记录：[research/find-web-design-prospects-with-sales-agents.json](../research/find-web-design-prospects-with-sales-agents.json)
