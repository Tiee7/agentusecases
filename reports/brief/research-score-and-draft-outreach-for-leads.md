# 用Make研究销售线索、评分并起草跟进邮件

## 中文

    研究线索、评分并起草外联内容
    一个基于Make的AI agent会自动研究线索、评分，并起草个性化后续外联内容。
    使用的是
    MK
    Make
    他们做了什么
    帖子描述了一套自动评估线索的Make工作流，将HubSpot联系人数据与Slack、Gmail和Google Calendar连接起来。帖子称，agent会自动研究线索、评分并起草个性化外联回复，同时通过Slack通知让销售团队了解进展；团队可以利用Gmail中草拟的回复和日历空闲时间继续跟进。
    进展与成效
    来源把成效描述为：工作流负责资格判断和后续跟进草稿，让销售团队专注成交。所展示的帖子没有提供绩效数字、评分实例或任何报告出的不足。
    值得了解
    实际限制在于应用组合：这套配置需要Make、HubSpot CRM访问权限，以及Slack、Gmail和Google Calendar；帖子还链接了一个预先搭好的场景模板。
    亲自尝试
    使用
    Make
    复制提示词
    搭建一个Make场景，从[线索来源，例如Google表格或CRM]取得新线索，在网上研究每家公司及联系人，并按我理想客户的标准[描述ICP]给他们打1到10分。对于达到[阈值]或更高分数的线索，起草一封个性化跟进邮件，引用研究中发现的具体信息，并作为草稿保存到[邮件工具]。不要发送任何内容；为最先的[数量]条线索写好草稿和评分后就停止，让我审核。
    原始来源：https://www.reddit.com/r/Make/comments/1to8mmo/tutorial_aiagent_for_lead_qualification_automated

<details><summary>English original</summary>

    Research, score and draft outreach for leads
    A Make-based AI agent researches leads, scores them, and drafts personalized follow-up outreach automatically.
    Done with
    MK
    Make
    What they did
    The post describes a Make workflow for automated lead qualification that connects HubSpot contact data with Slack, Gmail, and Google Calendar. It says the agent researches leads, scores them, and drafts personalized outreach replies automatically, while the sales team is kept in the loop through Slack notifications and can use the drafted Gmail responses and calendar availability for follow-up.
    How it went
    The source frames the result as letting the sales team focus on closing while the workflow handles qualification and draft follow-up. It does not give performance numbers, examples of scores, or any reported shortcomings in the thread shown.
    Worth knowing
    The practical catch is the app stack: the setup requires Make plus HubSpot CRM access, Slack, Gmail, and Google Calendar; the post also links a ready-built scenario template.
    Try it yourself
    with
    Make
    Copy prompt
    Build a Make scenario that takes new leads from [lead source, e.g. a Google Sheet or CRM], researches each company and contact on the web, and scores them 1 to 10 against my ideal customer: [describe ICP]. For leads scoring [threshold] or higher, draft a personalized follow-up email referencing something specific from the research, and save it as a draft in [email tool]. Do not send anything; stop once drafts and scores are written for the first [number] leads for me to review.
    Original source: https://www.reddit.com/r/Make/comments/1to8mmo/tutorial_aiagent_for_lead_qualification_automated

</details>


## 原作者的方法与来源

来源：[Make lead qualification tutorial original post](https://www.reddit.com/r/Make/comments/1to8mmo/tutorial_aiagent_for_lead_qualification_automated)

方法摘要未收录

## 简要分析

商业分数未评定；本篇不计完整深研。

### 需求与付款人

销售运营团队希望少花时间收集背景、筛选和写首稿。付款人可能是销售负责人；没有真实购买、预算或使用频率证据。需求应按每条线索人工审核成本衡量。

依据：[Sdirectory](https://agentusecases.ai/use-case/research-score-and-draft-outreach-for-leads)

### 交付与收入机制

拟议交付是一条带来源和规则解释的线索记录加待审核邮件草稿。可假设收配置及维护费，但不能把模板链接当付费客户或稳定订阅。业务结果仍需人工跟进。

依据：[Sdirectory](https://agentusecases.ai/use-case/research-score-and-draft-outreach-for-leads)

### 获客和验收

先在明确行业与获准数据上找小范围验证，不批量联系陌生人。验收分字段正确性、事实来源、评分一致性和草稿可用性；发送率、回复率、成交率不能混在一起。

依据：[Sdirectory](https://agentusecases.ai/use-case/research-score-and-draft-outreach-for-leads)

### 评分方法

把企业适配度和已观测互动分开，避免公开资料丰富就虚高。缺信息列未知，不能强行补数；1–10分是规则表达，未校准前不是购买概率。用相同输入重复比较结果，并记录规则版本。

依据：[Shubspot](https://knowledge.hubspot.com/scoring/understand-the-lead-scoring-tool), [Sdirectory](https://agentusecases.ai/use-case/research-score-and-draft-outreach-for-leads)

### 草稿与发送边界

保存草稿不代表发送，草稿ID与邮件message ID也不同。gmail.compose具有发信能力，需要移除发送动作、限制工具和人工批准步骤；一句不要发送不能证明实际权限隔离。案例实际授权配置未知。

依据：[Sdraft](https://developers.google.com/workspace/gmail/api/guides/drafts), [Sscope](https://developers.google.com/workspace/gmail/api/auth/scopes)

### 日历与跟进

可用忙闲区间辅助提出时间，但查询失败应标未知，不能推为空闲；空闲也不是客户同意或会议已创建。此案例没有预订结果，不应宣称全自动安排客户会议。

依据：[Scalendar](https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query)

### 成本与替代

成本含五应用访问、研究与模型调用、人工纠错、配额和流程维护。HubSpot自带规则评分是直接替代，是否可用需核账户订阅。未取得实际工时、用量与服务报价，因此不估虚构毛利。

依据：[Shubspot](https://knowledge.hubspot.com/scoring/understand-the-lead-scoring-tool)

### 独立自用价值

独立销售或小团队已有这套工具时，可能减少重复摘录与起草；没有量化收益。准备理想客户标准和审核样本，维护规则、数据新鲜度与草稿去重。低频用户搭建五应用可能不划算。

依据：[Sdirectory](https://agentusecases.ai/use-case/research-score-and-draft-outreach-for-leads)

### 隐私和错误

CRM联系人、邮件内容、Slack频道受众和日历应最小范围处理。网页事实可能过时或同名错配；个性化不能编造看过对方内容。网页和工具返回内容不能授权发送或扩大数据访问。

依据：[Sscope](https://developers.google.com/workspace/gmail/api/auth/scopes), [Sdirectory](https://agentusecases.ai/use-case/research-score-and-draft-outreach-for-leads)

### 结论和下一步

仅建议受控试点。用虚构公司与联系人设计已知、缺失、矛盾及重复条目，核来源、规则和草稿去重，不连接真实应用。本轮未试用；若审核成本不降、事实编造或无法阻止自动发送，停止扩大。

依据：[Sdirectory](https://agentusecases.ai/use-case/research-score-and-draft-outreach-for-leads), [Sdraft](https://developers.google.com/workspace/gmail/api/guides/drafts)

## 试用准备与预期结果

虚构公司与联系人、明确评分规则和预期答案。
每项分数有依据，未知项保留，重复条目不产生重复稿；本轮未运行。
只用虚构资料，分别列公司适配事实、互动事实、未知项及规则分。每条草稿引用给定事实并保留条目ID；不连接CRM、邮箱、Slack或日历，不发送、邀请或保存第三方草稿。

## 来源

- [许可目录线索评分案例](https://agentusecases.ai/use-case/research-score-and-draft-outreach-for-leads)：Make连接HubSpot、Slack、Gmail、Google Calendar，研究评分和草稿；无绩效数字或评分实例。1–10是源站试用模板，不是经核原作者算法。
- [HubSpot评分工具说明](https://knowledge.hubspot.com/scoring/understand-the-lead-scoring-tool)：2026-09-02更新，现成fit、engagement、combined评分；对象和AI能力有订阅条件，不是所有账户免费功能。
- [Gmail草稿创建与发送](https://developers.google.com/workspace/gmail/api/guides/drafts)：草稿容器ID稳定，替换正文时内部message ID改变；发送删除草稿并返回SENT新message。
- [Gmail权限范围](https://developers.google.com/workspace/gmail/api/auth/scopes)：gmail.compose同时允许管理草稿和发送邮件，不能仅凭此scope宣称技术上仅草稿。
- [Google Calendar忙闲查询](https://developers.google.com/workspace/calendar/api/v3/reference/freebusy/query)：查询返回busy区间及各日历errors，不创建会议；开始边界包含、结束边界不包含。
