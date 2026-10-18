# 用 n8n 筛选低分未回复商家评论并整理候选清单

分析深度：简要研究（brief）；商业评分未评定；不计入深研完成数。

## 案例完整中文译文

    向AI机构推送收到差评的商家作为线索
    n8n智能体会在商家收到差评时通知自动化机构，让他们能够率先致电，并提供负面评价应对工具。
    实际使用
    n8n
    具体做法
    一个n8n AI Agent节点位于托管的聊天界面之后。用户指定一个国家。Agent调用Bright Data工具，为Google Maps评论数据创建快照，然后取回数据。它筛选整体评分较高、存在3星或以下评论且商家未回复的商家，再汇总前5项，并在用户要求时通过邮件或Slack发送结果。
    结果如何
    这是一个提交给挑战赛的可用演示，作者没有将其商业化的计划。销售话术生成工具目前已停用。来源没有给出线索数量或转化数据。
    值得知道
    使用Bright Data快照，避免了按每个place_id循环调用Google Places和Reviews接口；作者说，这种循环很快会让你被封禁。构建前应阅读每个节点的文档。
    自行试用
    推荐工具
    n8n
    复制提示词
    构建一个n8n工作流，每天检查[本地商家类型，例如我所在城市的牙医]的Google评论，并标记刚收到[1星或2星]评论的商家。对每一家商家，让AI步骤概括投诉内容，并起草一段简短的电话话术，推荐[我的负面评价应对工具或服务]，然后通过邮件把商家名称、电话号码、评论原文和话术发给我。用几家商家进行测试并展示结果；不要自行联系任何商家。
    原始来源：https://dev.to/myopicoracle/communitypulse-4230

<details>
<summary>English · 完整归档原文</summary>

<pre>Alert AI agencies to businesses with bad reviews as leads
n8n agents notify automation agencies when a business receives bad reviews so they can call first and offer a damage-control tool.
Done with
N8
n8n
What they did
An n8n AI Agent node sits behind a hosted chat interface. The user names a country. The agent calls Bright Data tools to snapshot Google Maps review data, then retrieves it. It filters for well-rated businesses with reviews of 3 stars or lower and no owner reply, then summarizes the top 5 and sends results by email or Slack on request.
How it went
It works as a demo submitted to a challenge, and the author has no plans to commercialize it. The sales-script generation tool is currently disabled. The source states no lead or conversion numbers.
Worth knowing
Bright Data snapshots avoided looping Google Places and Reviews calls per place_id, which the author says gets you blocked quickly; read each node&#x27;s docs before building.
Try it yourself
with
n8n
Copy prompt
Build an n8n workflow that checks Google reviews for [type of local business, e.g. dentists in my city] every day and flags any business that just got a review of [1 or 2 stars]. For each one, have an AI step summarize the complaint and draft a short call script offering [my damage-control tool or service], then email me the business name, phone number, review text and script. Test it on a few businesses and show me the results; do not contact any business yourself.
Original source: https://dev.to/myopicoracle/communitypulse-4230</pre>

</details>

## 原作者的方法与来源

[CommunityPulse: Automating Lead Gen for AI Agencies with n8n Agents and Bright Data - DEV Community](https://dev.to/myopicoracle/communitypulse-4230)。以下为作者演示描述的短双语摘要，未独立复现工作流。

1. 作者描述了一个挑战赛演示：n8n聊天agent接收国家信息，创建Bright Data快照，再取回快照内容。
   English summary: The author describes a challenge demo where an n8n chat agent takes a country, creates a Bright Data snapshot, and retrieves its contents.

2. 它筛选整体评分较高但有低分未回复评论的商家，汇总少量候选；邮件或Slack交付被描述为可选。
   English summary: It selects high-rated businesses with low-rated, unanswered reviews and summarizes a small candidate list; email or Slack delivery is described as optional.

3. 销售话术工具被标为停用，作者在公开回复中表示当时没有商业化计划。
   English summary: The sales-script tool is marked disabled, and the author’s public reply says commercialization was not planned at that time.

## 我们的简要分析

商业判断：现有演示不足以支持商业投入。商业评分未评定；自用价值待核实。

### 演示完成与商业结果分开

原文是2025年挑战赛投稿，作者展示的是从聊天入口选择国家、查询快照、筛选并交付候选信息的演示。他在公开回复中说当时没有商业化计划，没有报告实际线索量、联系回复、签约或留存。文章中“零成本”“合格线索”等措辞属于作者主张，不是经账单或客户验证的经营结果。销售话术节点当时明确标为停用，不能把节点说明或后续设想当成已运行的功能。本轮没有打开托管聊天界面或运行工作流，避免触发真实采集或第三方用量；只核查公开资料和合成规则。 依据：[S4ecd4f2c2732](https://dev.to/myopicoracle/communitypulse-4230), [archive-case-20261017](https://agentusecases.ai/use-case/alert-ai-agencies-to-businesses-with-bad-reviews-as-leads)。

### 聊天触发不等于持续发现新差评

作者列出Chat Trigger、创建snapshot_id、等待可用、取回快照、提取前5项和可选投递，未展示每日调度、持续变更检测或去重验证。因此收到差评就能率先提醒、每天检查、生成电话话术，分别需要独立证据；源站试用模板的这些要求不是作者已经完成的事实。当前n8n文档说明Agent连接模型与工具后选择调用，并不使严格顺序、快照就绪或失败恢复自动成立。拟议验收应记录请求、待处理、可用、取回、过滤及待人工确认状态，快照失败或尚未返回不能被记为零条候选。 依据：[S4ecd4f2c2732](https://dev.to/myopicoracle/communitypulse-4230), [S50f7196cce5b](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)。

### 规则筛中的是候选，不是购买意向

原作者规则是overall_ratings大于4、单条ratings不高于3、owner_response为null；源站模板的1或2星是另一套编辑试用条件。整体恰好4分不满足大于4，字段缺失也不等于null；空字符串是否代表未回复，需要数据字典，不能自动猜测。合成试验只检查这些边界、重复记录和按商家归组，不证明真实匹配准确性。未回复可能来自延迟、数据缺失或已有人工处理安排，不能由此推断商家没有服务商或愿意付费。前5条结果若来自同一家商家，也不能算成5个独立客户；排序、数据年龄与行业匹配还需明确。 依据：[S4ecd4f2c2732](https://dev.to/myopicoracle/communitypulse-4230)。

### 数据产品、权限与替代方式

Bright Data当前Google Maps Scraper页面列出记录额度和计费方式，但作者用的是Filter dataset及Retrieve snapshot contents，不能直接套用另一产品的免费额度或单价，更不能把提供商可用当作已核验的用途许可。Google Place Details需要地点ID和字段选择；返回地点信息与形成完整、及时的评论流是不同工作。对于已经服务的商家，Google Business Profile原生评论管理和回复可作为替代，官方教程要求OAuth，并按账户及地点资源操作；连接某个节点不证明对陌生商家有操作权限。所有实际获取、存储和使用范围仍需核实，本轮没有测试采集、代理、绕限制或商家账户。 依据：[S4ecd4f2c2732](https://dev.to/myopicoracle/communitypulse-4230), [S324ea91d7e1b](https://brightdata.com/products/web-scraper/google-maps), [S0680d1521364](https://developers.google.com/maps/documentation/places/web-service/place-details), [Sd7a854996f3e](https://developers.google.com/my-business/content/review-data)。

### 付款人、需求与自用价值

潜在使用者是自动化机构的获客人员，潜在付款人是承担销售预算的机构负责人，终端商家则是后续服务的另一方。发现投诉、得到联系方式、确认需要、获得回应和签约是不同阶段，不能用第一步数量代替后续收入。作者提出先提供免费应对工具、再销售定制服务，但没有给出该路线的真实客户证据。已有客户的评论服务、人工查看公开页面以及平台原生回复是需要比较的基线，不应默认新增代理层一定省时。自用价值待核实：对能合法取得资料并人工核对的人，它可能整理候选信息，但准备数据字典、筛选口径、授权范围和复核清单都有成本。 依据：[S4ecd4f2c2732](https://dev.to/myopicoracle/communitypulse-4230), [Sd7a854996f3e](https://developers.google.com/my-business/content/review-data)。

### 把平台、数据与人工分开计算

n8n当前计划页面按工作流执行说明计费，不能用节点数量直接当收费次数，也不能由自托管或试用推出数据、模型与维护都免费。快照SKU、记录量和历史账单未核实，以下美元数字全部为预算假设：每客户每月99，数据20加模型2、人工1小时乘30、其他10、获客15，单位贡献22；月交付10份、固定100时贡献120。若人工3小时，单位负38、月负480；若仅数据预算翻倍，单位2、月负80。定制设置1500，数据/模型50、人工30小时乘35=1050、其他50、获客200，贡献150；月2项目固定100时贡献200，多10小时返工则单位负200、月负500。未扣税与其他固定费用，未验证客户报价，不能据此承诺利润。 依据：[S4ecd4f2c2732](https://dev.to/myopicoracle/communitypulse-4230), [S9c31625dedcc](https://n8n.io/pricing/), [S324ea91d7e1b](https://brightdata.com/products/web-scraper/google-maps)。

### 反馈与投入判断的证据缺口

本轮在DEV、公开GitHub和Hacker News方向做了三次检索，没有取得可归属CommunityPulse的独立付费使用结果。文章评论里的兴趣询问、产品扩展讨论以及第三方工具推荐，不等于这些人使用或购买过本工具。试图读取的独立研究页面返回403后已停止，未使用搜索摘要冒充已读论文；因此不据此推算评价对营收的影响。已读平台文档支持实现方向和费用边界，却不能替代本案例的市场与效果证据。本条作为简要分析保存，商业评分不评定，也不把缺少转化数据解释成实际转化率为零。 依据：[S4ecd4f2c2732](https://dev.to/myopicoracle/communitypulse-4230), [S9c31625dedcc](https://n8n.io/pricing/), [S324ea91d7e1b](https://brightdata.com/products/web-scraper/google-maps)。

### 验证动作与停止条件

结论是不建议依据现有演示投入商业交付。先在纯合成记录上验收字段类型、未知值、严格阈值、重复、同一商家多条评论和快照失败状态；人工核对输出仍只能称候选。若以后研究需求，先明确买方、合法数据范围、实际SKU、交付配额和人工验收，而不是先制作真实联系名单或发送话术。缺少关键字段、数据太旧、无法确认实际用量、人工成本超过预算或无人愿意为验收后的信息付费时，停止扩大范围。不得将可运行演示、节点数量或平台宣传作为获客壁垒；本轮不注册、不新建凭据、不购买、不调用收费采集/模型、不发送邮件或Slack，也不联系任何商家。 依据：[S4ecd4f2c2732](https://dev.to/myopicoracle/communitypulse-4230), [S9c31625dedcc](https://n8n.io/pricing/), [S324ea91d7e1b](https://brightdata.com/products/web-scraper/google-maps), [Sd7a854996f3e](https://developers.google.com/my-business/content/review-data)。

## 自用与试用准备

可能辅助整理候选，但没有独立实际使用、净省时或合格线索证据，仍需合法数据和人工复核。

准备：纯合成评分/回复/快照记录、字段字典及人工答案，无真实联系数据。

预期：候选/排除/未知验收表、数据状态与费用假设；不输出真实名单，自编模板未调用模型实测。

源站模板完整保留在上方原文与忠实译文中，不代表作者实际提示词或已运行功能。

### 用合成评论检验候选规则

研究团队自编，未调用模型实测。

    请只使用[纯合成商家编号、虚构评分、评论编号、回复字段、快照状态和人工答案]，设计一个离线候选筛选与复核流程。按作者描述的规则演示总评分大于4、单条评分不高于3且回复字段明确为null；缺失字段、空字符串或无法解析的评分应单列未知，不当作零或未回复。区分这套规则与源站模板的1或2星条件。检查重复记录、同一商家多条评论、快照尚未就绪、失败和数据年龄，分别列候选、排除与待核实理由。不要把候选叫成有购买意向的客户，不能把前5条当成5家独立客户。不要采集真实评论、联系方式或商家名单，不调用Bright Data、Google或付费模型，不注册、不创建凭据、不购买、不发送邮件/Slack、不生成真实外呼名单或联系商家。输出字段字典、合成验收表、未知项、用量记录设计及预算敏感性后停止；本模板为研究团队自编，未调用模型实测。

## 来源

- [Alert AI agencies to businesses with bad reviews as leads](https://agentusecases.ai/use-case/alert-ai-agencies-to-businesses-with-bad-reviews-as-leads)：源站对n8n演示、评论筛选和通知的归档转述；完整中文忠实保留，模板与实际功能另行区分。
- [CommunityPulse: Automating Lead Gen for AI Agencies with n8n Agents and Bright Data - DEV Community](https://dev.to/myopicoracle/communitypulse-4230)：作者挑战赛文章和公开回复：筛选条件、聊天/快照结构、停用的话术工具及当时无商业化计划；不含客户或转化证明。
- [n8n Plans and Pricing - n8n.io](https://n8n.io/pricing/)：当前官方按工作流执行计费及额度说明；不证明作者的历史支出，也不包含所有第三方数据与模型费用。
- [Google Maps Scraper API - 5K records/Month for Free](https://brightdata.com/products/web-scraper/google-maps)：当前Google Maps Scraper产品页的记录额度与按结果计价说明；不等于作者Dataset Filter快照产品的实际费率。
- [Place Details (New)  |  Places API (New)  |  Google for Developers](https://developers.google.com/maps/documentation/places/web-service/place-details)：官方Place Details使用地点ID和FieldMask选择字段，并说明计费及响应范围；不证明获取了完整新评论流。
- [Work with review data  |  Google Business Profile APIs  |  Google for Developers](https://developers.google.com/my-business/content/review-data)：Google Business Profile原生评论管理和回复接口及OAuth前提，构成具体替代；不证明对任意陌生商家有回复权限。
- [/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)：当前官方AI Agent需要模型和工具，由agent选择调用；文档不保证本演示版本、严格执行顺序或销售效果。
