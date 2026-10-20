# 用AI agent筛选创始人并准备联系

## 中文

    为风险投资筛选新创始人并开展联系
    一名投资人的agent系统监控新公司注册申报，研究创始人，标记匹配对象，起草和发送联系邮件、安排会议并准备问题。
    使用的是
    自建或未具名agent
    他们做了什么
    一篇基于访谈、讨论AI如何影响风险投资的文章描述：一名投资人搭建了一个agent，监控新公司注册申报并研究每位创始人。它会标记背景符合投资人偏好的创始人，然后起草并发出联系邮件、安排会议和准备问题。在一家机构，投资人的判断偏好被写成一份八页提示词，用来给新创始人评分。
    进展与成效
    投资人只需要参加Zoom会议。文章没有给出指标。它说最终投资决定仍由人作出，并认为每家机构都会搭建类似系统。
    值得注意
    文章认为，既然每个人都能搭建这种系统，优势就来自你写入agent的判断偏好，以及已有的创始人关系。
    亲自尝试
    使用
    Lindy
    复制提示词
    每[天/周]检查[新公司申报来源，例如州注册处或特拉华州申报]，寻找符合[行业、阶段、地点]的新公司。研究每位创始人，给我一份简短介绍，并按照[我的投资标准]评估匹配程度；为合适对象起草一封联系邮件。先向我展示草稿并取得批准，再发送任何邮件或安排任何会议。
    原始来源：https://mgilfoyle.substack.com/p/part-1-of-2-ai-is-changing-the-job

<details><summary>English original</summary>

    Screen new founders and run outreach for venture investing
    An investor's agent system monitors new company filings, researches founders, flags matches, drafts and sends outreach, schedules meetings and prepares questions.
    Done with a
    custom-built or unnamed agent
    What they did
    One investor, described in an interview-based essay on AI in venture capital, built an agent that watches new company filings and researches each founder. It flags founders who fit the backgrounds the investor wants, then drafts and emails outreach, schedules the meeting and prepares questions. At one firm, the investor's taste is encoded as an eight-page prompt that scores new founders.
    How it went
    The investor only has to show up to the Zoom call. The essay gives no metrics. It says the final investment decision stays human, and that every firm will build something similar.
    Worth knowing
    Since everyone can build this, the essay says the edge comes from the taste you encode in the agent and from your existing founder relationships.
    Try it yourself
    with
    Lindy
    Copy prompt
    Every [day/week], check [source of new company filings, e.g. state registry or Delaware filings] for new companies that match [sector, stage, location]. Research each founder and give me a short profile with a fit rating against [my investment criteria], plus draft an outreach email for the good matches. Don't send any emails or book any meetings until you've shown me the drafts and I approve them.
    Original source: https://mgilfoyle.substack.com/p/part-1-of-2-ai-is-changing-the-job

</details>

## 原作者的方法与来源

来源：[Interview essay describes an anonymous investor system, not the system owner’s direct instructions](https://mgilfoyle.substack.com/p/part-1-of-2-ai-is-changing-the-job)

报道摘要

1. 访谈文章转述系统监控公司申报并按照投资人标准研究创始人。
   English summary: The essay reports monitoring company filings and researching founders against investor criteria.

2. 文章转述联系及会前准备流程，没有技术实现或量化结果。
   English summary: It reports outreach and meeting preparation; technical implementation and measured outcomes are absent.

## 简要分析

商业分数未评定。

### 匿名采访不是可复现产品说明

原文发表于7月31日，目录显示10月20日，二者应分开。原案仅提供匿名采访转述，没有可复核系统、名单、邮件回执或会议结果；八页提示词没有公开，也不确定与整套自动化属于同一机构。因此用reported_summary呈现方法，不将采访者、受访投资人和推荐工具拼成一个实名实施者。

依据：[Sessay](https://mgilfoyle.substack.com/p/part-1-of-2-ai-is-changing-the-job), [Sdirectory](https://agentusecases.ai/use-case/screen-new-founders-and-run-outreach-for-venture-investing)

### 推荐Lindy不是原始技术栈

原站实际agent字段是自建或未具名，试用模板推荐Lindy。保留这两个字段，但不声称原作者使用Lindy，也不替未知系统补造API、CRM或部署架构。模板要求先展示草稿并批准才能发信或预约，其权限边界比文章描述的自动外联更窄，应完整保留。

依据：[Sdirectory](https://agentusecases.ai/use-case/screen-new-founders-and-run-outreach-for-venture-investing)

### 注册处网页不等于获准增量数据流

模板举例Delaware，并不证明受访者使用它。该查询页明确限制数据挖掘和自动工具，不能把一个可打开的搜索框直接改成每日爬虫。复制前必须取得明确允许的增量数据来源与使用范围；本轮只读入口说明，没有查询公司、批量抓取或尝试绕过限制。数据供应不成立时，先停自动采集分支而不是扩大重试。

依据：[Sdelaware](https://icis.corp.delaware.gov/eCorp/EntitySearch/NameSearch.aspx)

### 公司注册代理不是创始人

实体名称、注册编号和成立日期可以作为公司记录线索，注册代理联系方式不能直接当作创始人联系方式。搜索结果也不证明当前经营状态。研究者建议用公司官网和经过核对的职业资料连接公司与人，同名或冲突标未知，不让模型猜联系人。注册日期更不能单独证明公司正在融资。

依据：[Sdelaware](https://icis.corp.delaware.gov/eCorp/EntitySearch/NameSearch.aspx), [Sfaq](https://corp.delaware.gov/faqs/)

### Form D不能替代公司新设数据

官方表格是豁免发行通知，成立时间与证券首售时间分开列示；可在首售前提交，适用申报也可能在首售后才出现。它可作为不同性质的公开线索，但不是所有新公司的及时名单。把新申报数量称为新创始人数量会混淆样本范围，原案实际使用哪一种申报仍未知。

依据：[Sformd](https://www.sec.gov/about/forms/formd.pdf)

### 匹配评分应服务人工复核

以下为研究者设计：将行业、阶段、产品与可核实的职业经历写成可解释条件，保留每项出处、未知项和拒绝原因。不要从姓名、照片或敏感资料推断背景，也不要自动排除人。定期抽查低分和未知样本，观察标准是否遗漏非典型团队。匹配度不是投资收益概率，本轮不评价任何真实创始人、不作投资决定。

依据：[Sessay](https://mgilfoyle.substack.com/p/part-1-of-2-ai-is-changing-the-job)

### 起草、发送和预约是三种权限

草稿应由获授权人员检查收件人与事实，发送需要独立明确授权；对方确认之前不把日历占位算会议成功。若属于商业邮件，要核对FTC关于主要目的和退订等要求，B2B并非自动豁免；具体投资邀约的适用性需按内容与地区审查，不在此作统一法律判断。本轮无邮件、表单、会议或投资操作。

依据：[Sftc](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business), [Sdirectory](https://agentusecases.ai/use-case/screen-new-founders-and-run-outreach-for-venture-investing)

### 可能卖资料与流程，不卖投资回报

假设客户是需要持续发现项目的小型投资团队，预算归属运营或投研负责人。可交付带证据的候选资料、人工复核队列及会前问题；按固定研究包或受控持续服务收费是商业假设。获客可从现有专业合作验证小样本，原案没有付费客户、售价或采购流程，不能把投资机构资金规模当服务商收入。

依据：[Sessay](https://mgilfoyle.substack.com/p/part-1-of-2-ai-is-changing-the-job)

### 单位成本按已审核资料计

研究者假设每月100份已审核候选资料。低返工每份15分钟×40USD/h=10，加模型与工具预算0.5，已列10.5/份1050/月；高返工45分钟×40=30，加预算1.5，为31.5/份3150/月。许可数据费、系统接入、固定维护和获客未知另计，不默认零；售价未知，不算利润。结果应按合格资料与真实确认的会面分开，而非用生成邮件量证明价值。

依据：[Sessay](https://mgilfoyle.substack.com/p/part-1-of-2-ai-is-changing-the-job)

### 自用价值也依赖数据与复核

对已有清晰研究范围和专业判断能力的人，可能减少整理线索的重复劳动；实际净省时未知，不适合把提示词当投资判断替代品。需准备获准来源、已有公司去重表和客观条件，持续维护身份关联、资料新鲜度和误判记录。频率随数据更新而定，可日或周批量审阅，但原案未给精确节奏。

依据：[Sessay](https://mgilfoyle.substack.com/p/part-1-of-2-ai-is-changing-the-job)

### 公开信息也需要最小化处理

订阅数据、历史联系和会议笔记的权限应分开，不因做研究而复制私人通信。只保留必要的职业和公司事实；删除过时或错误关联，避免多个agent重复联系同一人。未获许可的联系人数据、敏感特征或隐蔽信息不纳入评分。错误外联会损害信任，人工审核成本是交付的一部分。

依据：[Sftc](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business)

### 先做不发送的小样本

下一步只用已获准的10条样本，核对来源许可、公司人名关联和标准解释，产出候选表及邮件草稿，不发送不预约。先统计未知率、错误关联和审核时间，与人工基线比较；无法取得许可数据、不断误关联或无法解释排除原因时不扩量。本轮没有运行原系统，官方说明只是复制条件，不补足匿名案例的效果证据。

依据：[Sdirectory](https://agentusecases.ai/use-case/screen-new-founders-and-run-outreach-for-venture-investing), [Sdelaware](https://icis.corp.delaware.gov/eCorp/EntitySearch/NameSearch.aspx)

## 自用价值：待核实

没有净省时与误判数据，效果未知。

依据：Sessay, Sdelaware

- 适用人群：有专业研究目标且能核对公司与职业资料的投资研究人员。
- 用途：公开职业/公司资料整理与会前准备，不代替决策。
- 预期收益：可能减少重复整理，未经测量。
- 设置成本：许可来源、去重表、客观标准、人工审核与发送边界。
- 维护成本：来源变化、身份关联、未知项与偏差抽检。
- 使用频率：按数据节奏日或周审核，原案未给频率。
- 隐私风险：联系人、职业资料和内部笔记不应无边界合并。
- 错误风险：注册代理误当创始人、错误评分、重复邮件及预约误报。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/screen-new-founders-and-run-outreach-for-venture-investing

建议工具：Lindy

    Every [day/week], check [source of new company filings, e.g. state registry or Delaware filings] for new companies that match [sector, stage, location]. Research each founder and give me a short profile with a fit rating against [my investment criteria], plus draft an outreach email for the good matches. Don't send any emails or book any meetings until you've shown me the drafts and I approve them.

自编试用模板

准备条件：10条明确获准样本、非敏感职业字段、去重及审核条件。

工具：原系统未具名；Lindy为原站建议，本轮未验证其执行。

预期结果：来源可追溯的候选表和未发送草稿，不含投资建议或收益预测。

### 源站Copy prompt

原文模板

出处：https://agentusecases.ai/use-case/screen-new-founders-and-run-outreach-for-venture-investing

依据：Sdirectory

    Every [day/week], check [source of new company filings, e.g. state registry or Delaware filings] for new companies that match [sector, stage, location]. Research each founder and give me a short profile with a fit rating against [my investment criteria], plus draft an outreach email for the good matches. Don't send any emails or book any meetings until you've shown me the drafts and I approve them.

### 小样本线索核验计划

自编模板

出处：研究团队自编

依据：Sdelaware, Sformd

    仅对已获准的10条公司样本制作核验计划。区分成立日期与融资申报，注册代理不当创始人，记录职业事实出处、未知和冲突。不推断敏感属性，不自动排除，不发信不预约不投资。

## 来源

- [许可目录：创始人筛选及联系工作流](https://agentusecases.ai/use-case/screen-new-founders-and-run-outreach-for-venture-investing)：完整目录英文/中文与模板；实际自建未具名agent，Lindy仅为推荐。目录日期10月20日不是原文发表日期。
- [Maria A Gilfoyle：AI与风险投资工作](https://mgilfoyle.substack.com/p/part-1-of-2-ai-is-changing-the-job)：原文2026-07-31。访谈对象匿名，描述filings到创始人研究/邮件/会议/问题流程，无指标；八页提示词在一家机构，未证明与前述同一家。最终决策仍由人负责。未取得代码、数据源或八页原提示词。
- [Delaware实体查询范围与访问限制](https://icis.corp.delaware.gov/eCorp/EntitySearch/NameSearch.aspx)：静态入口列免费字段：名称、编号、成立日期、注册代理等；不提供完整创始人身份。明示禁止数据挖掘及过量反复搜索，自动工具可能被停用。本轮只读说明，未提交查询或采集实体。
- [Delaware公司信息FAQ](https://corp.delaware.gov/faqs/)：免费查询结果包含活跃和不活跃实体，不等于当前状态；注册代理与公司实体信息不是创始人确认。不能把搜索有结果当企业经营中或有融资需求。
- [SEC Form D官方表格及说明](https://www.sec.gov/about/forms/formd.pdf)：豁免证券发行通知，不是公司成立登记。说明要求适用发行首次销售后15日内申报，也可事先申报；首次销售指不可撤销投资承诺。表格区分成立年份、发行首售时间及首次尚未发生，不替代新公司全集。
- [FTC商业邮件合规指南](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business)：商业邮件适用主要目的判断，B2B不是一般豁免；商业消息需真实头部/主题、规定信息、退订机制及处理。不是对所有投资人邀请的具体法律分类，本轮不发送。
