# 用Claude Desktop整理并填写ITR-1申报资料

## 中文

    通过税务门户提交所得税申报表
    Claude Desktop agent提交了用户的ITR-1：将工资与AIS交叉核对、处理更换雇主的情况、修正校验错误，并提交申报。
    使用的是
    Claude
    他们做了什么
    用户提供了多份Form 16，并指示Claude Desktop agent提交ITR-1。agent打开所得税门户，将工资数字与AIS交叉核对，自动处理年中更换雇主的情况，从会话超时中恢复，修正门户的一项校验错误，然后提交申报表。
    进展与成效
    ITR-1已提交，没有CA（特许会计师）或会计师参与，也无需花三小时手动操作门户。
    亲自尝试
    使用
    Claude
    复制提示词
    帮助我在[税务门户网址]准备[税务年度]的所得税申报表。我会自行登录。将我的工资和收入数字与[这个文件夹中的Form 16、AIS或同等报表]交叉核对，考虑[工作变动或其他收入]，并填写申报表。修正你发现的所有校验错误，然后停下来，在提交任何内容前向我展示每个数字的完整汇总，等待我同意后再申报。
    原始来源：https://x.com/trq212/status/2067255423842103670

<details><summary>English original</summary>

    File an income tax return through the tax portal
    Claude Desktop agent filed the user's ITR-1: cross-checked salary against AIS, handled an employer switch, fixed validation errors, and submitted.
    Done with
    CL
    Claude
    What they did
    User supplied Form 16s and instructed the Claude Desktop agent to file ITR-1. The agent opened the income tax portal, cross-checked salary figures against AIS, automatically handled the mid-year employer switch, recovered from session timeouts, corrected a portal validation error, and submitted the return.
    How it went
    The ITR-1 was filed with no CA or accountant involved and without three hours of manual portal work.
    Try it yourself
    with
    Claude
    Copy prompt
    Help me prepare my income tax return for [tax year] on [tax portal URL]. I'll log in myself. Cross-check my salary and income figures against [Form 16, AIS, or equivalent statements in this folder], account for [any job change or other income], and fill in the return form. Fix any validation errors you find, then stop and show me a full summary of every figure before you submit anything, and wait for my go-ahead to file.
    Original source: https://x.com/trq212/status/2067255423842103670

</details>

## 原作者的方法与来源

X原帖普通读取首次Internal Error，按规则仅重试一次返回403 Forbidden，此后停止。未读取私人税表、身份或银行信息，也未登录税务门户。

[原始链接](https://x.com/trq212/status/2067255423842103670)

## 简要分析

商业分数未评定。

### 提交、验证与正确性不是一件事

目录给出的终点是提交，没有回执、验证状态、税务计算或后续处理结果。官方FAQ明确存在申报后的验证环节，因此不能把页面提交当作全部完成，也不能推断已收到退款、节税或免除后续责任。三小时是目录中的手工基线表述，未取得实际对照计时。

依据：[Sdirectory](https://agentusecases.ai/use-case/file-an-income-tax-return-through-the-tax-portal), [Sverify](https://www.incometax.gov.in/iec/foportal/itr-v-faqs)

### 先固定年度和适用表格

当前官方手册以AY2026-27示例并列适用条件，原案没有披露年度与完整收入情况。不能因为作者用了ITR1就把它推荐给所有工资收入者，也不把今天的规则倒推为原作者当时适用。拟议流程首先核对年度、居民身份和收入类别，复杂情况需要合格专业人员判断。这里不替具体纳税人选表或制度。 续接时实际读取的官方工资收入者页面还列出境外资产/收入、董事身份等排除条件，不能只凭两份Form16断言适用。

依据：[Smanual](https://www.incometax.gov.in/iec/foportal/newdownloads/itr/itr-UM?mobile-app=1), [Seligibility](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1)

### 多雇主核对需要来源账

换工作时应分别追踪每份资料对应雇主、期间和金额来源，检查重叠、缺失以及同一项在不同报表中重复出现。agent可以提出差异清单，但不应在没有依据时把不一致数值改成相等。预期交付是每个字段到文件及原字段的映射、差异与待问事项，不是一个无法追溯的最终总额。

依据：[Sdirectory](https://agentusecases.ai/use-case/file-an-income-tax-return-through-the-tax-portal)

### 校验通过不证明事实正确

门户校验可检查字段形式或规则，却不等于所有收入真实完整。发生错误应记录原因、拟改字段、证据和审核人，不能为了让界面接受而猜数字。会话超时恢复先确认保存状态，避免重复提交。此处是设计建议，本轮没有操作门户、修正任何真实申报或验证agent能处理这些错误。

依据：[Smanual](https://www.incometax.gov.in/iec/foportal/newdownloads/itr/itr-UM?mobile-app=1)

### 可交付边界比无人报税更清楚

候选商业需求是减少资料整理、对账和人工复核往返，不是仅靠浏览器自动点击替代税务判断。假设可为获准专业服务团队提供资料清单与差异报告，具体资质、责任、客户授权和适用法律仍需核查。本案没有付费用户、收入、定价或获客渠道证据，不将未请会计师推成可复制会计费收入。

依据：[Sdirectory](https://agentusecases.ai/use-case/file-an-income-tax-return-through-the-tax-portal)

### 一次年度任务也有维护成本

成本包括资料整理、隐私处理、模型、人工复核、异常恢复和年度表格规则更新。三小时不能直接乘客户数得到节省或利润，也不能把无会计师参与等同零成本。与人工、官方离线工具或已有税务软件比较时，应固定同样资料复杂度和最终审核标准，不只比较填写速度。

依据：[Sdirectory](https://agentusecases.ai/use-case/file-an-income-tax-return-through-the-tax-portal)

### 候选交付、获客与复用条件

可测试的交付单位是一个年度、一名客户的一份资料来源映射与差异清单，由有权限的专业人员复核，不承诺申报正确或节税。潜在付款者可能是已有客户的税务服务团队；通过现有文档管理或专业服务合作关系展示虚构样例，只是渠道假设，本轮未联系或获客。可复用部分是雇主/期间/字段规范、重复项检测和差异说明；税年规则、客户复杂度及最终判断不能无条件复制。客户自己看官方说明或用现有税务软件是替代，并非每个人需要新agent。

依据：[Sdirectory](https://agentusecases.ai/use-case/file-an-income-tax-return-through-the-tax-portal), [Seligibility](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1)

### 两种资料整理成本情景，不是报价

仅演示同一交付单位的敏感性：每月10份年度资料差异清单，不含税务判断、正式申报与验证。低返工假设每份人工20分钟，按15美元/小时机会成本为5美元，模型预算0.2，已列小计5.2；高返工假设60分钟和模型0.5，小计15.5。对应月度已列小计52和155美元。工时、人工单价、用量和模型预算均为研究者假设，不是本案实测、官方报价或专业税务服务费。工具固定费、获客、培训、年度维护及其他费用未知，须另加；售价与愿付价未知，因此不计算利润或宣称某预算内可开业。

依据：[Sdirectory](https://agentusecases.ai/use-case/file-an-income-tax-return-through-the-tax-portal)

### 自用收益取决于可审查性

自用人群是了解自身收入且能检查结果的纳税人，潜在收益为减少重复核对。设置需准备完整资料并定义待审输出；维护随税年与门户变化，通常季节性而非日常高频。错漏收入、选错适用表格或误触声明的风险远高于普通文本整理，因此应先保留人工核验和操作控制。

依据：[Sdirectory](https://agentusecases.ai/use-case/file-an-income-tax-return-through-the-tax-portal)

### 不把真实税务材料放进公开案例

Form16和AIS可能包含身份、收入、雇主、账户与其他个人信息。公开研究只保存已许可目录与原创分析，不保存私人税表、身份号码、凭据或银行资料。拟议试验完全使用合成数据；涉及正式声明、签署、付款或身份验证时由本人处理，不以目录Copy prompt代替实际授权。

依据：[Sdirectory](https://agentusecases.ai/use-case/file-an-income-tax-return-through-the-tax-portal)

### 合成双雇主样例只做核对

准备虚构两家雇主记录、一个重复项目、一处缺失期间和一个金额不一致项，预先给出标准差异表。让助手列字段来源、未解决问题和待审草稿，不给真实身份信息、不访问门户、不选择税制、不提交。预期是能发现重复缺项并保留未知，而不是自动生成自信的正确申报。本轮未运行试验。

依据：[Sdirectory](https://agentusecases.ai/use-case/file-an-income-tax-return-through-the-tax-portal)

## 自用价值：待核实

可探索核对和草稿辅助，正式报税正确性未证实。

依据：Sdirectory, Smanual, Sverify

- 适用人群：能审核本人收入资料的纳税人及获准专业协作者。
- 用途：整理多份工资来源，标注差异和缺项。
- 预期收益：可能减少核对，目录三小时说法非独立实测。
- 设置成本：完整资料、年度范围、差异标准与敏感信息处理。
- 维护成本：税年、门户、表格规则及人工审核更新。
- 使用频率：通常按税年和实际申报需求。
- 隐私风险：身份、收入与银行资料泄露。
- 错误风险：错表、重复或漏报、猜测修正、未验证却称完成。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/file-an-income-tax-return-through-the-tax-portal

建议工具：Claude

    Help me prepare my income tax return for [tax year] on [tax portal URL]. I'll log in myself. Cross-check my salary and income figures against [Form 16, AIS, or equivalent statements in this folder], account for [any job change or other income], and fill in the return form. Fix any validation errors you find, then stop and show me a full summary of every figure before you submit anything, and wait for my go-ahead to file.

自编试用模板

准备条件：虚构双雇主记录与标准差异表，不含身份号码或银行信息。

工具：已有获准助手或本地文档。

预期结果：字段来源和差异清单、待审草稿；不登录、不声明、不提交、不付款，未实测。

### 源站Copy prompt

原文模板

出处：https://agentusecases.ai/use-case/file-an-income-tax-return-through-the-tax-portal

依据：Sdirectory

    Help me prepare my income tax return for [tax year] on [tax portal URL]. I'll log in myself. Cross-check my salary and income figures against [Form 16, AIS, or equivalent statements in this folder], account for [any job change or other income], and fill in the return form. Fix any validation errors you find, then stop and show me a full summary of every figure before you submit anything, and wait for my go-ahead to file.

### 离线验证模板

自编模板

出处：研究团队自编

依据：Sdirectory

    根据以下虚构工资资料生成字段来源对照与差异清单，标记重复、缺失和冲突。不要补造数据，不访问门户、不判断实际税制、不提交申报或付款。

## 来源

- [许可目录现场正文](https://agentusecases.ai/use-case/file-an-income-tax-return-through-the-tax-portal)：目录声称Claude Desktop完成ITR1、Form16/AIS核对、雇主切换和错误恢复并提交；缺回执、课税年度、e-verification与后续税务结果。
- [印度税务部门ITR-1在线手册](https://www.incometax.gov.in/iec/foportal/newdownloads/itr/itr-UM?mobile-app=1)：当前手册明确AY2026-27，要求满足ITR1资格、复核预填字段，区分声明、校验和验证。首次读取错误，单次重试成功；不将当前规则反套未知年份原案。
- [印度税务部门30天验证FAQ](https://www.incometax.gov.in/iec/foportal/itr-v-faqs)：官方说明电子验证或ITR-V期限通常为申报后30天，迟验会影响申报日期及后果，未验证申报被视为无效。用于区分提交与最终有效状态，不证明原案已验证。
- [原作者文章](https://x.com/trq212/status/2067255423842103670)：原文未读；目录转述和试用模板不冒充作者实现。
- [印度税务部门：AY2026-27工资收入者适用表格](https://www.incometax.gov.in/iec/foportal/help/individual/return-applicable-1)：2026-10-20自有云浏览器读取官方AY2026-27工资收入者页面：ITR-1限定居民身份、收入类型与额度，并列董事、短期资本利得、境外资产或收入等排除条件。Form16由雇主提供，AIS包含多类税务信息；换雇主不自动决定适用表格。页面内容更新标2026-07-09，与全站页脚日期不同。这里只核适用边界，不替具体纳税人选表。
