# 用 AI agent 核对承包商报价与变更单并起草异议邮件

## 中文

    就承包商报价与变更单提出异议
    AI审阅了承包商采购订单、邮件和逐项费用，并起草争议邮件，发现用户遗漏的问题，最终带来两万美元抵扣。
    实际使用
    自建或未命名agent
    具体做法
    用户向AI提供了全部逐项费用、采购订单及所有承包商邮件。AI审阅这些资料，为报价与变更单争议起草详细邮件，其中包括用户此前没有发现的质疑点。用户几乎没有再补充内容就发送了邮件。
    结果如何
    这些争议在整个项目期间带来了两万美元的累计抵扣。
    值得知道
    用户投入的精力很少。
    自行试用
    推荐工具
    Claude Cowork
    复制提示词
    审阅[文件夹路径]中有关我的[项目]的承包商采购订单、邮件与逐项费用。比较原报价、实际账单和变更单，列出每项差异、金额及证据。用我的口吻为每个问题起草争议邮件，但不要发送任何内容。最后汇总我可以提出争议的总金额。
    原始来源：https://x.com/AddictedHoosier/status/2105711009327456547

<details>
<summary>英文原文</summary>

    Dispute contractor pricing and change orders
    An AI reviewed a contractor PO, emails and line items and drafted dispute emails, spotting issues the user missed and leading to $20K credited back.
    Done with a
    custom-built or unnamed agent
    What they did
    User fed the AI every line item, the PO, and all contractor emails. The AI reviewed them and drafted detailed dispute emails on pricing and change orders, including challenges the user had not spotted. The user sent the emails with little further input.
    How it went
    The disputes produced $20K credited back over the project life.
    Worth knowing
    Required little effort on the user's part.
    Try it yourself
    with
    Claude Cowork
    Copy prompt
    Review the contractor purchase order, emails and line items in [folder path] for my [project]. Compare what was quoted with what was billed and the change orders, and list every discrepancy with amounts and the evidence. Draft a dispute email for each issue in my voice, but don't send anything. Finish with a summary of the total I could dispute.
    Original source: https://x.com/AddictedHoosier/status/2105711009327456547

</details>

## 原作者的方法与来源

来源：[原始 X 案例帖](https://x.com/AddictedHoosier/status/2105711009327456547)

方法摘要未收录

## 我们的分析

**商业结论：适合内部效率工具。先把报价、变更和账单整理成可复核证据，累计抵扣自述不足以证明自动争议业务**

项目费用跨报价、PO、批准变更、邮件和抵扣记录，现有通用agent可辅助查找和起草，但需要理解工程事实的负责人复核。原始案例未披露合同、模型、准确率或结算证据，不能把累计$20K当作普遍收益。现有项目系统和专业人员已经承担核心批准与判断，对外低价材料包容易被获客和返工吞没。建议先嵌入内部资料核对流程，记录引用、遗漏与人工耗时，再判断是否存在可独立经营的交付价值。

案例ID：`dispute-contractor-pricing-and-change-orders` · 案例来源：https://agentusecases.ai/use-case/dispute-contractor-pricing-and-change-orders
研究时间：2026-10-18T00:33:53.332368+00:00

**商业评分：45.0/100。用户反馈信号占5%。**

| 维度 | 权重 | 分数 /5 | 商业依据 |
|---|---:|---:|---|
| 付费需求 | 20% | 3.5 | 跨文件费用核对会影响项目付款与沟通，但不同客户频率和真实付费意愿仍未验证。 [S6ea558a1bbed, Se12cb4f75ee5, S94d2934f123f] |
| 业务价值与效果证据 | 20% | 2 | 有累计抵扣的源站自述，缺少原帖、明细和失败样本；合同字段与合成算术不能替代真实AI准确率。 [S6ea558a1bbed, S75dc12220a54, S809da17a1369] |
| 单位经济与利润 | 20% | 2.5 | 限定资料包仍有人工复核、获客与返工成本，较高价假设的月贡献对半小时额外工作很敏感。 [Se12cb4f75ee5, S94d2934f123f, S794f4f1d07d6] |
| 获客与市场进入 | 15% | 2 | 已有项目团队可内用，但新外部服务需赢得敏感资料信任且没有验证的客户渠道。 [S94d2934f123f, Se12cb4f75ee5, S794f4f1d07d6] |
| 竞争壁垒 | 10% | 1.5 | 通用文件agent、项目管理软件和结构化合同说明容易替代邮件封装，未发现专有数据或接入证据。 [S794f4f1d07d6, S75dc12220a54, Se12cb4f75ee5] |
| 交付与经营风险 | 10% | 2 | 可通过引用、版本和状态缩小风险，但法域、合同机制与实际工程判断仍需负责人复核。 [Sed0fc0209f7e, S809da17a1369, S75dc12220a54, S794f4f1d07d6] |
| 独立用户反馈信号 | 5% | 0 | 三组检索未取得本用途独立复现，官方教程与行业采访不是直接AI使用反馈。 [S6ea558a1bbed, S94d2934f123f] |

## 自用价值：中

适合有完整材料并能复核工程背景的人，可能改善跨文件查找和证据整理；实际省时、遗漏与抵扣结果未验证，不能让草稿替代负责人或专业判断。

依据：S6ea558a1bbed, S794f4f1d07d6, S75dc12220a54, Se12cb4f75ee5, S809da17a1369

- 适用人群：业主代表、项目成本或应付账款人员，以及能理解自身项目并愿意复核的个人业主。
- 用途：把报价、PO、变更、账单与抵扣对应起来，输出来源明确的待核实问题和未发送草稿。
- 预期收益：可能减少查找与遗漏，是基于任务结构的推断；不保证发现错误、追回金额或节省时间。
- 设置成本：整理版本、币种、计费口径与批准记录；先用合成或去标识资料，核对现有工具及组织允许的数据范围。
- 维护成本：持续记录项目新变更、抵扣与版本并人工复核；真实时间与维护负担未测量。
- 使用频率：可随项目账期和变更触发；个人项目通常阶段性，企业多项目频率尚无本案例数据。
- 隐私风险：合同与邮件可能含个人、商业及付款信息；当前工具可能涉及云端处理，须最小化资料并确认权限，不能把密码或完整银行资料放入试用。
- 错误风险：可能混淆批准与待定变更、重复附件、税费和抵扣，或错误判断合同效力；所有疑点保留证据与未知项并由人复核。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/dispute-contractor-pricing-and-change-orders

建议工具：Claude Cowork

    Review the contractor purchase order, emails and line items in [folder path] for my [project]. Compare what was quoted with what was billed and the change orders, and list every discrepancy with amounts and the evidence. Draft a dispute email for each issue in my voice, but don't send anything. Finish with a summary of the total I could dispute.

自编试用模板

准备条件：合成或去标识的报价、PO、发票行项、已知批准变更、邮件摘录及抵扣状态。为每份文件指定ID和版本，提供币种、计量与税费口径；缺失项留空，不包含密码、完整账户或银行信息。

工具：源站建议Claude Cowork；可用本人现有且被允许处理这些材料的文件分析工具。当前Cowork需要核对计划、桌面连接及云端数据范围；本轮不新增账户、连接邮箱或调用付费模型API。

预期结果：一份带文件引用、计算与反证的差异表，区分已解释、重复、待批准、候选金额、已确认抵扣和未知项；以及未发送的中性核对草稿，不替人判断应付权利。

### 我们编写：仅核对材料与起草问题

自编模板

出处：研究团队自编

依据：S6ea558a1bbed, S75dc12220a54, S809da17a1369, S794f4f1d07d6

    只用我提供的合成或去标识材料核对承包商费用。不要联系任何人、发送邮件、提交表单、接受或签署变更、认定违约或付款权利。保留原文件，只输出新表格与草稿。材料包括带ID和版本的报价、PO、发票行项、已批准及待定变更、邮件摘录和抵扣记录。逐项列出原范围/数量/单价、批准后的基准、实际账单、税费与币种口径、批准状态、已确认抵扣及具体出处。先识别重复附件和旧版本，不能把相同发票算两遍；待定变更和不同币种不得自动合计为可追回金额。每个疑点同时列支持与反对证据，缺失项标“待负责人核实”。区分已解释差异、候选差额、已确认抵扣与现金到账。最后输出中性核对问题和未发送的邮件草稿；不把案例$20K当作本项目预期收益，不给法律结论。

### Our template: evidence review and questions only

自编模板

出处：研究团队自编

依据：S6ea558a1bbed, S75dc12220a54, S809da17a1369, S794f4f1d07d6

    Review only the synthetic or de-identified contractor materials I provide. Do not contact anyone, send messages, submit forms, accept or sign changes, or decide breach or payment entitlement. Preserve originals and produce a new worksheet and draft only. Inputs include versioned quotes, purchase orders, invoice lines, approved and pending changes, correspondence excerpts, and credit records. Map each line to scope, quantity, unit price, approved baseline, invoice, currency/tax basis, approval status, confirmed credits, and exact evidence references. Deduplicate repeated documents and identify superseded versions. Do not automatically total pending changes or mixed currencies as recoverable money. Include supporting and contrary evidence; mark unknowns for the project owner. Separate explained differences, candidate amounts, confirmed credits, and cash settlement. Finish with neutral clarification questions and an unsent email draft. Do not treat the archived $20K as this project's expected recovery or give a legal conclusion.

## 已核验事实

- 源站将实际agent标为自建或未命名，Claude Cowork只出现在建议试用工具中；二者不能合并为同一项实际使用事实。 [S6ea558a1bbed]
- 源站叙述输入为逐项费用、PO和承包商邮件，AI起草异议后由用户自行发送；原始X帖未取得，无法核验逐步操作。 [S6ea558a1bbed]
- 源站称$20K在项目生命周期内累计抵扣，没有项目期限、逐笔记录或现金结算凭据；不能据此计算每封邮件收益。 [S6ea558a1bbed]
- AIA G701公开使用说明包含变更内容、合同金额与工期调整、支持文件和各方约定后的执行记录；不表明本案例使用该合同体系。 [S75dc12220a54]
- AIA文章区分已协商变更与某些合同机制下价格或工期尚待确定的变更指令；资料核对不能自动把缺少一类文件判为不应付款。 [S809da17a1369]
- 加州CSLB的住宅改造监管说明提及书面并签署的变更要求，适用范围是其说明的特定法域与事项，不是本案例未知合同的结论。 [Sed0fc0209f7e]
- Procore官方教程将PO与分包协议归入commitments，并提供根据项目配置处理变更订单的现有流程。 [Se12cb4f75ee5]
- 同一Procore教程明确变更创建受用户权限与变更层级等配置影响；简单对外封装不能忽略现有批准流程。 [Se12cb4f75ee5]
- Anthropic当前Cowork文档包含云端任务及桌面文件访问说明，本地连接需要桌面应用可用，不能据本地文件位置推断没有云端处理。 [S794f4f1d07d6]
- Construction Dive在2023年的独立报道强调理解合同、沟通和过程留痕；其引述的争议项目样本不应外推本案例的收益或市场平均值。 [S94d2934f123f]

## 谁承担核对工作，谁有理由付款

这条案例的使用者把采购订单、逐项费用和承包商邮件交给AI审阅，再自行发送草拟的异议邮件。源站称整个项目期间获得$20K抵扣，却没有原始合同、项目规模、持续时间、争议笔数、结算凭据或失败记录。现有中文译文把金额表述为两万美元，应原样保留；研究不能据此承诺每个资料包都可追回相同金额，更不能把项目抵扣当作服务商收入。

直接有用的人群是掌握材料、能判断项目实际发生了什么的业主、业主代表、成本控制或应付账款人员。他们可能需要把分散的文件变成可复核的差异表；终局判断、谈判和付款权限依然由负责人掌握。一次装修的个人用户与每月处理多个项目的公司不是同一种客户：前者需求偶发，后者可以反复使用，却通常已有流程、软件和专业人员，采购也会审查权限及责任。

本报告优先把用途判断为内部效率工具。若对外收费，付款人必须认可证据整理本身的价值，而不只是看到“可能争议金额”的大数字。项目地点、合同类型及执行中变更规则都未知，不能默认用户拥有某项扣款权利，也不能把发现数字差异等同于发现对方违法。本轮没有接触业主、承包商或任何真实项目客户。

依据：S6ea558a1bbed, Se12cb4f75ee5, S94d2934f123f

## 从文件对照到待核实事项

源站披露的是输入材料、生成详细邮件和用户发送邮件的概括，不是可复现的作者步骤。实际agent被标为自建或未命名，原始X帖未取得，无法补写模型、解析程序、提示词、审核清单或数据权限。Claude Cowork出现在源站试用建议中，应保留这个身份差别。下面的链路是我们基于可检查交付设计的辅助方法，不冒充作者真实操作。

先列文件清单和版本，再逐项对照报价、PO、已批准变更、发票与抵扣记录。核对对象至少包含计费主体、行号、数量、单价、币种、税费口径、工期影响和批准状态。不同版本、计量单位或计费阶段的数字不能直接相减。每条疑点需要指向具体页码、段落或邮件日期，并记录与该疑点相反的证据；缺少批准材料只应标为待核实。

输出应把已解释差异、重复资料、尚待批准的变更、候选金额、已确认抵扣和现金结算分开。本轮用合成数据做了确定性算术核对：原始重复差异一千，处理已批准变更与重复发票后候选五百五十，再扣除已确认二百五十抵扣，余三百仍因批准证据不明而待核对。这只证明示例台账的算术，不证明AI能准确解析真实文件或这些金额应当追回。

依据：S6ea558a1bbed, S75dc12220a54, Se12cb4f75ee5, S809da17a1369

## 项目风险与可进入的业务范围

变更管理的痛点不只在找价格差，还包括谁批准工作、何时通知、数量与范围怎样变化、是否已经开票或抵扣。Construction Dive在2023年的独立报道强调理解合同、明确沟通和持续保存材料。报道中所引争议项目样本不代表普通住宅装修或所有建筑项目，本文不据此估算消费者平均损失、市场总规模或本工具的平均收益。

公开的G701说明以已达成一致的范围、金额和工期变更为核心，提示核对不能只盯发票金额。另一方面，AIA介绍的某些变更指令可以在价格和工期尚未谈妥时推动工作继续。因此，缺少一份形式上的已签变更单并不能让通用AI替用户直接得出“这笔费用一定不用付”的结论。案例没有披露采用哪种合同机制，所有类似判断都应回到具体资料及合格专业人员。

可先进入的范围是材料已相对齐全、负责人愿意复核的内部资料核对，而不是跨地区自动处理争议。若每次都要重新收集核心文件、解释工程现场或判断法律效力，标准化交付就会被调查与专业审核时间吞没。已有项目团队可以先比较人工查找与agent辅助查找的准确性和返工量；本轮没有取得相关真实时间记录或客户需求样本。

依据：S94d2934f123f, S75dc12220a54, S809da17a1369, Se12cb4f75ee5

## 项目系统、表格和专业复核

第一类替代是现有项目管理系统。Procore的官方教程把采购订单和分包协议纳入commitment管理，并根据配置、权限和变更层级处理后续变化。这说明持续记录与批准的工具已经存在，新服务不能仅把“能生成邮件”视为独特壁垒。它还需要解释，为什么团队不直接从现有系统导出资料给自己的成本人员核对。

第二类替代是表格加负责人或专业顾问复核。对于只涉及少量清晰行项的任务，排序、版本控制和可复算的公式可能已足够；当解释涉及合同范围或现场事实，专业人员的工作又无法被语言流畅度替代。通用agent的潜在增量是在跨文件查找、引用整理与初稿准备，而不是自动接替批准流程。业主一侧的回溯核查和承包商系统里的日常变更管理也不是完全相同的产品场景。

源站推荐的Cowork可用于文件任务，但当前文档描述的云端任务和桌面文件连接意味着组织还需确认数据范围。一次性个人用户可能不愿为了未知节省额另购复杂系统；已有软件的企业则会关心重复工具、权限与导出成本。本报告没有读取或比较任何实际客户软件合同，不引用未知的Procore报价，也不把已有工具的销售宣传当成独立效果证明。

依据：Se12cb4f75ee5, S794f4f1d07d6, S75dc12220a54, S94d2934f123f

## 高金额自述不能代替单位利润

$20K是源站对一个项目生命周期累计抵扣的自述，没有费用、人工、样本或入账明细。不能把它设为每个客户的可回收金额，也不能把未处理的全部发票差异作为成功追回的基数。本文不设计以争议金额自动抽成的收费承诺；以下固定交付价、用量、工时和获客全部是压力测试假设，并非作者或现有服务的报价。

第一情景为四十九美元的基础资料草稿包：运行预算一美元，项目人员四十五分钟按每小时四十美元计三十，其他可变成本三、获客二十，总可变成本五十四，单位贡献负五。每月四十包、固定费用三百，经营贡献负五百。该情景说明即使不做正式专业意见，材料整理、版本核对与低价销售也不一定覆盖成本。

第二情景为二百四十九美元的有限资料复核包：人工和外部复核合计二点五小时按每小时六十美元计一百五十，运行二、其他十二、获客三十五，总成本一百九十九，单位贡献五十。每月二十包、固定八百，月贡献二百；每包多花半小时，月贡献降为负四百。小时单价只是预算假设，不代表法律或工程专业市场价格。薄弱的利润对返工非常敏感，因此更适合先在已有项目流程内部验证，不能凭较大的争议数字扩张经营。

依据：S6ea558a1bbed, Se12cb4f75ee5, S94d2934f123f

## 信任与场景决定销售难度

如果未来评估对外提供材料整理服务，较有解释力的入口是已有业主代表、项目财务或成本控制的工作场景。这些人能说明原始合同和后续资料来自哪里，知道哪些行项必须交给项目负责人。它们目前只是可能的渠道，不是本轮已经建立的客户网络；本轮没有联系任何人、发送异议、提交表单或利用案例作者的身份背书。

独立获客需要克服两项成本：用户得先相信资料不会被误用，又要理解交付只是证据整理及待核实问题，不是保证对方接受异议。若广告直接展示两万美元案例结果，容易让消费者把未知项目的累计抵扣当成自己的预计收益。复杂任务的报价还可能在拿到文件前无法确定，低价承诺之后不断加收补充材料或人工费用会损害信任。

内部使用可减少对外销售这一项支出，但并不自动消除信息收集与复核成本。应先记录交付范围、文件数量、版本缺口、负责人纠错与返工时间，再讨论是否值得把工具推广到下一个项目。若需要律师或工程人员承担核心判断，就应透明计入交付成本，并按实际资质和授权安排工作，而不能靠AI邮件的专业语气替代这些条件。

依据：S6ea558a1bbed, S94d2934f123f, S794f4f1d07d6, Se12cb4f75ee5

## 可复核记录比措辞更有价值

邮件写得详尽并不等于发现了可主张的权利。通用agent和现有办公软件都可以生成结构化文字，真正难以维持的是同一行费用在多个版本、变更与抵扣之间的对应关系，以及缺少关键文件时能否主动停下来。本案例没有公开代码、专有合同数据、支付接口或独立结果验证，不能推断已经有稳定的专有能力。

如果团队在内部使用，长期价值可能来自一致的行项编码、合同版本、批准链与资料出处，以及负责人修正过的重复计费或税费口径规则。这样的记录让下一次核查更容易复算；它也要求持续维护、访问控制和明确所有权。保存更多未经授权的合同、银行资料或邮件不是可接受的竞争优势，跨客户混用信息尤其会破坏信任。

AIA说明和Procore流程已经把一些结构化字段及批准环节明确展示，单纯把这些概念包装成聊天界面不够形成高壁垒。值得验证的是在用户已有材料与系统之上，是否能准确补齐引用、解释为什么某项不能合计，以及让负责人发现遗漏的反证。如果最终主要工作仍是专业人员重新阅读全部文件，外部产品的溢价空间就会很小，内部辅助仍应以节省的实际复核工作量来评价。

依据：S6ea558a1bbed, S75dc12220a54, Se12cb4f75ee5, S794f4f1d07d6

## 合同机制、法域与材料权限

加州CSLB的住宅改造说明要求相关变更以书面和签署方式记录，本文仅把它作为特定法域的材料要求示例。案例没有披露所在地、工程类型或适用合同，不能把这个规则推广成所有争议的胜诉条件。AIA对变更指令与已协商变更的区分又提示，形式和授权必须连同具体合同理解；本轮不提供对任何真实项目的法律意见。

材料侧的错误同样会带来后果。税、保留金、分期账单、不同计量单位、不同币种、已批准范围变化和已确认抵扣，都可能让看似相同的价格不能直接相减。重复附件还可能使“总争议金额”膨胀。输出中应明确哪些数值有证据、哪些只是候选差异、哪些需要工程或合同人员解释，而不是给每个缺口填上确定的结论。

当前Cowork资料说明任务与文件可能进入其云端环境，桌面本地访问又依赖应用连接；不能仅凭“文件在我的电脑上”推断材料从未被处理到云端。自用试用应先用合成或去标识文本，检查组织允许的数据范围，保留原件，只生成新的草稿。遇到拒绝、证书或安全警告即停止该访问。本轮只读公开资料并做本地合成算术，没有真实合同、承包商对话或提交行为。

依据：Sed0fc0209f7e, S809da17a1369, S794f4f1d07d6, S75dc12220a54

## 没有直接复现，反馈信号记零

暂无直接用户反馈。

依据：S6ea558a1bbed, S94d2934f123f, Se12cb4f75ee5, S794f4f1d07d6

## 先做内部核对，再讨论经营

结论是适合内部效率工具，而不是根据一次累计抵扣自述直接建立自动争议业务。掌握工程事实的负责人可以利用agent先整理证据、找出版本与行项对应关系，再决定哪些问题需要专业复核。商业评分反映仍缺少真实样本、准确率、人工耗时和客户采购证据；对外固定交付包的假设利润也会被少量返工迅速吃掉。

自用价值独立评为中：适合材料相对齐全、能够理解项目背景并愿意逐项核对的业主代表、项目财务或个人业主。对于文件非常分散、合同机制不明或金额影响重大的事项，先补齐资料及寻求适当专业判断更重要。源站Copy prompt及其Claude Cowork建议会原样保留，实际agent仍标为未命名；自编试用只生成新表格和中性问题草稿，不发送或认定任何应收金额。

本轮四行合成资料检查展示了为什么必须先处理批准变更、去重和已确认抵扣，但没有调用模型去解析真实文件，不能称为实际争议成功测试。下一步可另行在有权限的代表性样本上对照人工标准答案，记录每条引用、遗漏与复核时间；若无法指出原始证据、需要猜测授权或币种、或者负责人需要重新做完全部分析，就停止对外商业投入并缩小内部用途。

依据：S6ea558a1bbed, S75dc12220a54, S809da17a1369, S794f4f1d07d6, Se12cb4f75ee5

## 单位经济测算：情景假设，不是项目已实现的财务结果

| 情景 / 交付单位 | 收入 | 可变成本（含获客） | 单位贡献 | 月交付量 | 月固定成本 | 月经营贡献 |
|---|---:|---:|---:|---:|---:|---:|
| 假设：基础材料与草稿包 / 一个小范围、约定输入上限的资料包；不含争议处理或专业意见 (USD) | 49.00 | 54.00 | -5.00 | 40 | 300.00 | -500.00 |
| 假设：有限资料专业复核包 / 一份范围明确、由适当项目人员复核的材料清单和中性问题草稿 (USD) | 249.00 | 199.00 | 50.00 | 20 | 800.00 | 200.00 |

假设：基础材料与草稿包假设：全部为未实测设计假设：项目人员45分钟×40美元/小时；运行预算1、其他3、获客20，每月40包固定300。单位贡献-5，月贡献-500。不是作者收费、模型实际账单或追回金额。；API成本 1，人工成本 30，其他可变成本 3，分摊获客成本 20。依据：S6ea558a1bbed, Se12cb4f75ee5, S794f4f1d07d6

假设：有限资料专业复核包假设：所有金额为预算假设：项目与外部复核共2.5小时×60美元/小时，运行2、其他12、获客35，每月20包固定800。不是专业市场报价或正式法律意见；单位贡献50、月贡献200。每包再多0.5小时，月贡献-400；人工3小时20分钟时单位贡献归零。本轮无收费或付费模型API调用。；API成本 2，人工成本 150，其他可变成本 12，分摊获客成本 35。依据：S75dc12220a54, S809da17a1369, S94d2934f123f, S794f4f1d07d6

## 反证与未核实信息

报价差异不一定是错误：批准变更、税费口径、分期和已确认抵扣都能解释数字变化；某些AIA机制还允许价格/时间待定的变更指令。现有Procore流程与人工表格削弱新封装的差异。反过来，已掌握材料的团队可能无需独立获客，并能从引用整理中受益，因此不能把外部商业证据不足等同于完全没有自用价值。

原始X帖未读，实际agent未命名；没有合同法域、工程类型、原始文件、模型或提示词、20K明细、币种代码、项目期限、收费、真实人工时间或独立复现。公开文档的合同与法域仅作示例，不认定本案例适用。合成算术未测试AI抽取准确率，不能证明任何费用应当追回。

## 具体动作与止损条件

以后在明确授权的代表性资料上与人工标准答案比较引用、去重、批准状态、已确认抵扣和返工时间；本轮只做合成算术示例，不作为真实结果验证。

停止投入条件：无法定位原始依据、必须猜测授权或币种、需要负责人重做全部分析，或249美元假设包每件多花半小时导致月贡献转负时停止对外投入。

## 来源与对应关系

- [S6ea558a1bbed] [源站归档：Dispute contractor pricing and change orders](https://agentusecases.ai/use-case/dispute-contractor-pricing-and-change-orders)：支持实际agent未命名、输入PO/逐项费用与邮件、用户自行发送草稿，以及项目周期内$20K抵扣的源站自述；不证明现金回款、普遍成功率或Claude Cowork为实际工具。
- [S794f4f1d07d6] [Anthropic：Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)：支持当前Cowork文件读写、云端任务与桌面连接、权限及付费计划要求；用作源站建议工具的准备说明，不证明原案例运行环境或原模型。
- [S75dc12220a54] [AIA Contract Documents：Instructions G701–2017 Change Order](https://help.aiacontracts.com/hc/en-us/articles/1500009322061-instructions-g701-2017-change-order)：支持G701记录约定的工作范围、合同金额和工期调整以及相关签署和支持文件；只据公开说明归纳字段，不转载受许可保护的合同表单，也不认定本案例采用AIA合同。
- [Sed0fc0209f7e] [California CSLB：Learn About Home Improvement Contracts](https://www.cslb.ca.gov/Consumers/Hire_A_Contractor/Home_Improvement_Contracts/What_Is_A_Contract.aspx)：加州住宅改造监管说明强调书面变更与签署；只作特定法域的材料要求示例，本案例地点与合同适用法律未知。
- [Se12cb4f75ee5] [Procore：Create a Commitment Change Order](https://v2.support.procore.com/product-manuals/commitments-project/tutorials/create-a-commitment-change-order-cco)：支持采购订单/分包协议的变更管理、配置的层级与创建权限等现有产品能力；不证明本案例部署Procore或存在自动追回款项。
- [S94d2934f123f] [Construction Dive：Change orders often spark conflict, but they do not have to](https://www.constructiondive.com/news/the-dotted-line-change-orders-lawsuits/700507/)：2023年独立行业报道讨论合同理解、沟通与过程留痕；仅作运营背景，不将其中争议项目样本的金额或比率外推本案例或市场规模。
- [S809da17a1369] [AIA：Construction Change Directive vs Change Order](https://learn.aiacontracts.com/articles/construction-change-directive-vs-change-order/)：支持AIA所述合同机制下已协商变更与价格/工期尚待确定的变更指令有区别；不能由缺少某一张变更单就自动认定不应付款，实际效力仍须看合同及当地专业判断。

结构化记录：[research/dispute-contractor-pricing-and-change-orders.json](../research/dispute-contractor-pricing-and-change-orders.json)
