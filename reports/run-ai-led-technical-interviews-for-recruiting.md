# 用Claude进行技术面试并生成候选人报告

## 中文原案例

    用AI主导技术面试来招聘
    micro1使用Claude与候选人进行技术面试，据称每天超过3000场；这些数字是在供应商案例研究中自行报告的。
    使用的是
    CL
    Claude
    他们做了什么
    micro1基于Claude Platform API搭建了面试平台。Claude可以在任何时间、跨时区与候选人进行动态技术对话，随后撰写面试报告。通过AI初筛的候选人交给人类面试官。除使用Anthropic的文档和提示词指南外，该页面几乎没有提供实施细节。
    进展与成效
    案例研究称，每天进行超过3000场AI面试，招聘成本降低85%。在Deel，人类面试的通过率从10%升至50%。Legal Soft将初筛团队从33人缩减到12人。
    值得了解
    所有数字都来自一篇未提供方法说明的供应商案例研究，也没有说明提示词、评分方式或如何评价候选人。
    亲自尝试
    使用
    Claude
    复制提示词
    担任[公司类型]的[职位名称]岗位技术面试官。围绕[技能，例如Python、系统设计、SQL]一次问我一个问题，根据我的回答调整追问，并对含糊之处深入询问。问完[问题数量]个问题后停止，给我一份评分卡：每项技能按1到5分评级，列出来自我回答的证据，并给出录用或不录用的建议及理由。
    原始来源：https://www.anthropic.com/customers/micro1

<details><summary>English original</summary>

    Run AI-led technical interviews for recruiting
    micro1 uses Claude to conduct technical interviews with candidates, reportedly over 3,000 per day; figures are self-reported in a vendor case study.
    Done with
    CL
    Claude
    What they did
    micro1 built its interview platform on the Claude Platform API. Claude holds dynamic technical conversations with candidates at any hour and across time zones, then writes an interview report. Human interviewers take the candidates who pass the AI screen. The page gives few implementation details beyond using Anthropic's documentation and prompting guidelines.
    How it went
    The case study reports over 3,000 AI interviews a day and 85% lower recruiting costs. At Deel, the human interview pass rate rose from 10% to 50%. Legal Soft cut its screening team from 33 to 12.
    Worth knowing
    All figures come from a vendor case study with no methodology, and it gives no detail on prompts, scoring, or how candidates are rated.
    Try it yourself
    with
    Claude
    Copy prompt
    Act as a technical interviewer for a [job title] role at [company type]. Ask me one question at a time covering [skills, e.g. Python, system design, SQL], adapt follow-ups to my answers, and probe where I am vague. After [number] questions, stop and give me a scorecard with a rating from 1 to 5 for each skill, evidence from my answers, and a hire or no-hire recommendation with reasons.
    Original source: https://www.anthropic.com/customers/micro1

</details>

## English

    Run AI-led technical interviews for recruiting
    micro1 uses Claude to conduct technical interviews with candidates, reportedly over 3,000 per day; figures are self-reported in a vendor case study.
    Done with
    CL
    Claude
    What they did
    micro1 built its interview platform on the Claude Platform API. Claude holds dynamic technical conversations with candidates at any hour and across time zones, then writes an interview report. Human interviewers take the candidates who pass the AI screen. The page gives few implementation details beyond using Anthropic's documentation and prompting guidelines.
    How it went
    The case study reports over 3,000 AI interviews a day and 85% lower recruiting costs. At Deel, the human interview pass rate rose from 10% to 50%. Legal Soft cut its screening team from 33 to 12.
    Worth knowing
    All figures come from a vendor case study with no methodology, and it gives no detail on prompts, scoring, or how candidates are rated.
    Try it yourself
    with
    Claude
    Copy prompt
    Act as a technical interviewer for a [job title] role at [company type]. Ask me one question at a time covering [skills, e.g. Python, system design, SQL], adapt follow-ups to my answers, and probe where I am vague. After [number] questions, stop and give me a scorecard with a rating from 1 to 5 for each skill, evidence from my answers, and a hire or no-hire recommendation with reasons.
    Original source: https://www.anthropic.com/customers/micro1

## 中文

    用AI主导技术面试来招聘
    micro1使用Claude与候选人进行技术面试，据称每天超过3000场；这些数字是在供应商案例研究中自行报告的。
    使用的是
    CL
    Claude
    他们做了什么
    micro1基于Claude Platform API搭建了面试平台。Claude可以在任何时间、跨时区与候选人进行动态技术对话，随后撰写面试报告。通过AI初筛的候选人交给人类面试官。除使用Anthropic的文档和提示词指南外，该页面几乎没有提供实施细节。
    进展与成效
    案例研究称，每天进行超过3000场AI面试，招聘成本降低85%。在Deel，人类面试的通过率从10%升至50%。Legal Soft将初筛团队从33人缩减到12人。
    值得了解
    所有数字都来自一篇未提供方法说明的供应商案例研究，也没有说明提示词、评分方式或如何评价候选人。
    亲自尝试
    使用
    Claude
    复制提示词
    担任[公司类型]的[职位名称]岗位技术面试官。围绕[技能，例如Python、系统设计、SQL]一次问我一个问题，根据我的回答调整追问，并对含糊之处深入询问。问完[问题数量]个问题后停止，给我一份评分卡：每项技能按1到5分评级，列出来自我回答的证据，并给出录用或不录用的建议及理由。
    原始来源：https://www.anthropic.com/customers/micro1

## 原作者的方法与来源

来源：[micro1 transforms technical recruiting with Claude](https://www.anthropic.com/customers/micro1)

报道摘要

1. 供应商案例描述Claude进行动态技术对话。
   English summary: The vendor case describes Claude conducting adaptive technical conversations.

2. 系统为招聘流程生成面试报告。
   English summary: The system generates interview reports for the recruiting workflow.

3. 该案例未披露详细提示词与评分实现。
   English summary: Detailed prompts and scoring implementation are not disclosed in this case study.

## 我们的分析

**商业结论：仅建议受控试点。先验证报告与人工复核价值，不把AI评分当最终录用决定**

案例说明了动态面试和报告生成的具体用途，但高吞吐和后续通过率并不能证明没有漏筛，也不能直接推出商业利润。候选人体验、数据用途、技术失败和合理便利都可能改变总成本。已有技术测评工具提供替代，新的实现应在一个岗位的受控影子流程中证明证据可追溯与净工作量减少，再考虑扩大使用。

案例ID：`run-ai-led-technical-interviews-for-recruiting` · 案例来源：https://agentusecases.ai/use-case/run-ai-led-technical-interviews-for-recruiting
研究时间：2026-10-20T10:53:13.090855+00:00

**商业评分：44.0/100。用户反馈信号占5%。**

| 维度 | 权重 | 分数 /5 | 商业依据 |
|---|---:|---:|---|
| 付费需求 | 20% | 3 | 高频技术招聘存在排期与复核负担，且现成付费工具提供替代；但本方案实际购买和续约意愿尚未验证。 [Sdirectory, Scompetitor] |
| 业务价值与效果证据 | 20% | 2.5 | 供应商给出成本和通过率叙述，但缺方法、分母及漏筛验证；不能视为对工作表现的因果证明。 [Soriginal, Spaper] |
| 单位经济与利润 | 20% | 2 | 两个可复算情景显示人工复核和失败补救可使贡献转负，未取得实际服务报价与完整交付账目。 [Scompetitor] |
| 获客与市场进入 | 15% | 2 | 需建立招聘方、工程和数据治理信任，销售周期与获客成本未知；不能仅凭案例品牌推定新服务容易成交。 [Soriginal, Sprivacy] |
| 竞争壁垒 | 10% | 2 | 通用问答容易复制，岗位校准与稳定接入才可能形成价值；当前没有独占能力或持续利润的独立验证。 [Scompetitor, Spaper] |
| 交付与经营风险 | 10% | 1.5 | 涉及候选人数据、可访问性和重要就业决定，必须保留人工复核与替代通道，工程和运营负担较高。 [Sprivacy, Sada] |
| 独立用户反馈信号 | 5% | 1 | 取得正负候选叙述，但匿名编辑、不同岗位和未经核实的结果限制独立性，不据此合成满意率。 [Spositive, Snegative, Sexperience] |

## 自用价值：中

可用于个人模拟练习或招聘人员报告草稿，不能替代正式岗位判断。

依据：Sdirectory, Sprivacy, Sexperience

- 适用人群：准备技术面试的个人、负责结构化面试的招聘人员。
- 用途：练习逐题回答、对照证据回顾或生成待人工核对的记录。
- 预期收益：可能减少练习排期和记录整理，未实测提分或录用收益。
- 设置成本：岗位范围、题目和评分说明；使用虚构身份与项目样本。
- 维护成本：题目更新、答案校验、模型变化与错误反馈。
- 使用频率：求职准备期或招聘批次，不推定每天持续使用。
- 隐私风险：真实简历、录音和项目秘密可能进入服务；应明确留存与用途。
- 错误风险：错评分、误解表达、超时、虚构反馈及把练习评分当就业结论。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/run-ai-led-technical-interviews-for-recruiting

建议工具：Claude

    Act as a technical interviewer for a [job title] role at [company type]. Ask me one question at a time covering [skills, e.g. Python, system design, SQL], adapt follow-ups to my answers, and probe where I am vague. After [number] questions, stop and give me a scorecard with a rating from 1 to 5 for each skill, evidence from my answers, and a hire or no-hire recommendation with reasons.

自编试用模板

准备条件：虚构职位和合成回答，不用真实候选人、受保护信息或商业秘密。

工具：已有文本助手与本地练习文档，不调用额外付费API。

预期结果：逐题练习记录、证据和待澄清点，不作真实录用决定；本轮未试运行。

### 源站Copy prompt

原文模板

出处：https://agentusecases.ai/use-case/run-ai-led-technical-interviews-for-recruiting

依据：Sdirectory

    Act as a technical interviewer for a [job title] role at [company type]. Ask me one question at a time covering [skills, e.g. Python, system design, SQL], adapt follow-ups to my answers, and probe where I am vague. After [number] questions, stop and give me a scorecard with a rating from 1 to 5 for each skill, evidence from my answers, and a hire or no-hire recommendation with reasons.

### 离线技能证据练习

自编模板

出处：研究团队自编

依据：Sdirectory

    仅对虚构岗位做练习，每次一个技术问题，允许澄清。结束后列出回答支持的技能证据、未观察项和练习建议；不推断受保护特征、不作真实录用建议，不虚构成绩或经历。

## 已核验事实

- 目录将3000+/日、85%及客户团队变化标为供应商自述，并保留Claude试用模板。 [Sdirectory]
- 实际跳转claude.com/customers/micro1；供应商叙述Claude技术对话和报告，没有给出成本与通过率指标的独立审计方法。 [Soriginal]
- 研究描述GPT-4o实现；三日4820次不成功面试，400个候选评分均值4.37/5，不能当标准NPS或Claude案例成本验证。 [Spaper]
- 2026-07-21版本列录制与评估数据、自有模型训练及退出入口；称最终决定前人工复核。属于政策文本而非执行审计。 [Sprivacy]
- 2022-05-12指导强调岗位相关技能、评估筛除影响及合理便利；本轮核实公开页面，不判断特定雇主违法。 [Sada]
- 现成技术面试工具支持协作编码、报告与招聘系统集成；本轮不采用未读成功的定价页报价。 [Scompetitor]
- 2026-09-17编辑发布，称六月工程面试节奏可预期并获offer；身份和结果未独立验证，正文难度与标签不一致。 [Spositive]
- 2026-09-04编辑发布，称七月技术任务具体但一次异常未产结果；匿名自述不构成故障率统计。 [Snegative]
- 2026-09-04发布、10-01更新的非技术岗位体验，称练习有帮助，也出现思考出声被当作答案；不代表工程岗位或整体录用结果。 [Sexperience]

## 客户要的是可复核的筛选证据，不是一个会问话的头像

最可能的付款人是有稳定技术招聘量的雇主或招聘机构，实际使用者还包括工程面试官、招聘运营人员和候选人。买方希望减少排期与重复提问，但候选人希望被准确理解、知道进度并有纠错机会；双方的收益不能互相替代。每天面试数量大，只能说明供应商叙述的吞吐，不能直接推出客户数、收入、岗位填补率或同一团队节省多少小时。应该先选择一个岗位族和一个招聘阶段，明确该阶段原本要解决的问题，保留原始问题、回答和人工判断作为可核对记录。低频招聘的小团队可能用一次人工结构化面试更简单；跨时区且初筛拥堵的团队才更值得测试。采购前需要工程负责人确认问题与工作相关，招聘方确认流程边界，数据负责人确认录制与保留方式；候选人不是可以忽略的免费数据提供者。供应商销售口径、企业实际预算和最终候选人接受程度，本案都没有足够独立证据把它们合并成已验证需求规模。

依据：Sdirectory, Soriginal, Sprivacy

## 把历史Claude案例与另一套GPT-4o研究分开

许可目录对应的供应商案例说明Claude承担动态技术对话和报告生成，但没有开放可直接部署的完整系统。另一个Zara研究文本描述GPT-4o和候选人反馈处理，不能据此断言当前系统只使用某个模型，或把两份材料拼成作者公开过的单一架构。可复制的工作流假设应从职位要求、技能范围与人工确认的评分说明开始，经过候选人知情与技术检查，再进入提问、澄清、工作样本和报告草稿；最终由有权限的人复核。每个评分需链接到可见回答或代码行为，证据不足要保留未观测，而不是用自信措辞填补。会话中断应成为技术状态，不自动等同能力不合格。版本、题目、时间窗和修改记录应能回查，重复运行不能悄悄覆盖先前报告。这里提出的是实施要求，不是声称micro1所有环节都已按此运行；本轮没有候选人数据、产品后台或实测记录。

依据：Soriginal, Spaper, Sprivacy

## 供应商结果值得核查，但不能代替因果验证

目录保留的规模和成本数字均来自供应商案例。人类面试通过率从10%到50%，描述的是进入后续阶段人群的条件通过率，不能直接证明所有合格候选人都被保留，更不能据此计算招聘质量提高五倍。筛掉更多人也可能提高后续通过率，因此必须同时观察漏筛、人工复核改判和最终工作表现。论文的三日数据明确写的是4820次不成功面试，不是全部面试；其400个评分的4.37/5也不是通常以推荐者减贬损者计算的标准NPS数值，不能改写成行业满意度。不同材料的时间、对象和模型实现不一致，不能用论文替案例补上未提供的成本计算方法。对新项目而言，合适的市场验证不是照搬85%节约目标，而是在有授权的样本上记录原流程成本、工具费用、复核与补面时间，比较审核后的净变化。没有这套基线，扩大面试量可能只是把成本从排期转移到申诉与人工补救。

依据：Sdirectory, Soriginal, Spaper

## 与结构化人工面试及现成评测平台比较

HackerRank官方FAQ提供代码协作、面试报告和招聘系统集成的现成路径，是工具辅助人类面试的具体替代，而非必须自建语音agent才能实现。另一个低技术替代是固定技能表、工作样本和两名面试官按同一标准记录证据；其排期成本可能高，但解释与澄清能力更直接。比较时应统一岗位、候选人数量、测试时长、复核深度和失败恢复范围，而不是把一种产品的API成本与另一种的完整服务报价对比。本轮定价页实际返回cookie要求，搜索索引与FAQ中的套餐数量也不一致，因此不把搜索价格写入已核验报价。下一次采购评估应取得有效方案和计费口径，再比较每份被人工采纳报告的总成本。若买方已有ATS和技术测评工具，新产品需要证明增量价值，而不是重复提供同样的报告界面。供应商能够连续迭代、支持候选人和保持题库质量，也是自建方案必须承担的工作。

依据：Scompetitor, Sdirectory

## 两种情景都把复核与失败成本算进去

以下数字全部是研究者用于敏感性分析的假设，不是micro1报价、模型实际账单或用户预算。标准情景按每次完成且可复核的面试报告收费25美元，API与语音2美元、人工复核8美元、其他可变成本2美元、获客摊销3美元，贡献10美元；每月300次、固定费用2000美元时，税前且未计额外研发的剩余为1000美元。压力情景保持价格25美元，但人工升至16美元、API3美元、其他4美元、获客5美元，单次贡献为负3美元，300次并承担同样固定费时亏2900美元。两情景不是盈利预测，而是在说明复核、技术失败和补面可以吃掉模型成本优势。按完成次数收费还需定义失败重做是否计费，按候选人包月则需限制重复评估与支持范围；只按自动筛掉的人数计费容易产生不良激励。投入前要通过真实日志验证人工分钟、完成率、退款和支持成本，不用营销节约比例回填缺失账目。固定费用覆盖基础运维与持续质检，但大型客户的安全审查和一次性接入需要另计。即使标准情景贡献为正，也只有超过200次完成报告才覆盖2000美元固定费用；若实际可计费量不足，不能拿启动中的申请总量替代交付量。现金收款周期与退款条款也可能使账面贡献和当月现金流不同。

依据：Sdirectory, Scompetitor

## 先验证一个岗位流程，再讨论对外销售

可行的进入方式假设是向已经存在初筛拥堵的技术招聘团队展示合成案例的证据报告，而不是向所有公司宣传无人面试替代招聘部门。第一阶段只测试题目质量、记录完整性和人工可采纳性，下一阶段才在另获授权后安排有知情同意的低风险试点。获客所需的信任材料包括数据流说明、删除流程、候选人替代通道、错误示例与人工纠错记录；这些工作都应计入交付成本。销售承诺宜围绕减少整理时间和提高证据可读性，不承诺录用质量、零偏见或固定节约比例。不同客户的岗位定义与技术栈会造成配置成本，不能以模型能生成问题就认为跨行业交付没有边际工作。本案只支持供应商有客户案例叙述，不提供新进入者的销售周期、转化率、续约或渠道价格，因此这些都保留未知。研究下一步是验证需求和流程，不是授权联系候选人、发送邀约或代企业作录用决定。

依据：Sdirectory, Soriginal

## 真正难复制的是校准与运行治理

一个逐题追问并生成评分卡的演示很容易被通用模型和现成工具覆盖。更有可能形成长期价值的是岗位能力与工作样本的映射、经授权积累的人工校准、可解释的争议处理和稳定的系统接入。但这些也不是有数据就自然出现：历史招聘决定可能包含偏差，样本选择可能只覆盖通过者，模型升级后旧分数也未必可比。流程资产应能显示题目为什么测量所需技能、评分如何与具体证据对应，以及何种错误需要人工接管。不能把候选人录音录像的数量本身当作可随意商业化的数据壁垒，训练与留存还需要符合承诺和适用要求。竞争者已有题库、集成和组织采购渠道，新服务若只有聊天界面，转换成本未必来自产品价值。复制条件应列明岗位专家、可访问的测试环境、数据管理和支持能力；本案未提供足以证明独占壁垒或持久超额利润的数据。

依据：Spaper, Scompetitor

## 复核、可访问性和隐私属于核心交付

micro1候选人隐私说明列出录音录像、转录及评估信息，并区分自有模型改进与不向模型公司提供训练数据；不要把后者简化为完全不训练。其说明还提到最终决定前人工复核与申诉途径，但文档承诺不等于本轮已审计执行。司法部指导强调招聘技术需衡量岗位技能并考虑合理便利安排，因此实现时应提供适当替代通道和人工纠错，而不是从声音、面部或交流风格推定工作能力。匿名体验中的故障叙述是需要测试的风险线索，不是故障率统计。工程验收应覆盖网络中断、录音缺失、转录错误、超时、题目不相关和重复会话；故障记录应允许恢复或补面，不自动出具负面结论。权限应按企业和岗位分隔，限制报告与原始录制的可见范围，并能说明保留和删除策略。本研究不替企业确定具体地区法律适用，也不推断任何候选人的受保护特征。

依据：Sprivacy, Sada, Snegative

## 直接体验有帮助，但样本和独立性有限

2026-09-17编辑发布，称六月工程面试节奏可预期并获offer；身份和结果未独立验证，正文难度与标签不一致。

2026-09-04编辑发布，称七月技术任务具体但一次异常未产结果；匿名自述不构成故障率统计。

2026-09-04发布、10-01更新的非技术岗位体验，称练习有帮助，也出现思考出声被当作答案；不代表工程岗位或整体录用结果。

依据：Spositive, Snegative, Sexperience

## 先在小范围验证辅助价值

本案足以支持一个可复核的面试辅助流程假设，但不足以支持全自动招聘决定或复制供应商的经济结果。建议先构建一个岗位的离线试验：使用自愿提供或合成的回答与工作样本，由两位岗位专家独立标注可观察证据，随后比较agent报告是否漏记、错归因或虚构。测量人工读报告加纠错的总时间，而不只测生成速度；另设断网、空音频、问题歧义和用户请求澄清等情形，检查系统是否保持待复核而非伪装完成。下一步真实试点必须另有授权和候选人知情，先采用影子模式，不改变现有录用流程。继续条件是关键证据能回溯、严重错配为零、复核者认为报告有用且总工作量下降；这些是拟议验收标准，不是已取得结果。出现未授权数据使用、无人工接管、故障自动淘汰或无法解释的重要结论就停止扩展；若支持与复核后单次贡献长期为负，也不应靠增加候选人数量掩盖亏损。对照测试还应固定题目与岗位等级，随机交换报告顺序，避免评审者因知道哪份来自AI而偏好某一组。建立错误清单时分别记录转录、事实提取、技能解释和业务决策错误，不能用一个平均分掩盖严重个案。成功条件应事先写下，失败样本应保留以便复验，避免只展示顺利完成的演示。

依据：Sdirectory, Sprivacy, Sada

## 单位经济测算：情景假设，不是项目已实现的财务结果

| 情景 / 交付单位 | 收入 | 可变成本（含获客） | 单位贡献 | 月交付量 | 月固定成本 | 月经营贡献 |
|---|---:|---:|---:|---:|---:|---:|
| 标准情景：研究者假设 / 每次完成且可复核的面试报告 (USD) | 25.00 | 15.00 | 10.00 | 300 | 2000.00 | 1000.00 |
| 压力情景：研究者假设 / 每次完成且可复核的面试报告 (USD) | 25.00 | 28.00 | -3.00 | 300 | 2000.00 | -2900.00 |

标准情景：研究者假设假设：全部为演算假设，不是供应商报价或真实账单。人工按每小时40美元，分别12或24分钟；其他包括重做与支持摊销。未计税和额外研发，无本轮付费API。；API成本 2，人工成本 8，其他可变成本 2，分摊获客成本 3。依据：Sdirectory, Scompetitor

压力情景：研究者假设假设：全部为演算假设，不是供应商报价或真实账单。人工按每小时40美元，分别12或24分钟；其他包括重做与支持摊销。未计税和额外研发，无本轮付费API。；API成本 3，人工成本 16，其他可变成本 4，分摊获客成本 5。依据：Sdirectory, Scompetitor

## 反证与未核实信息

现成面试工具已具备报告和集成；成本比例缺方法，候选反馈有故障线索，论文与Claude案例模型及样本不同。

未运行真实面试、处理简历、联系或筛选候选人。Capterra与Glassdoor各普通读取失败两次，Reddit不访问；定价页正文未取得，不引用搜索价格。未确认当前生产模型栈、客户收入、准确率或真实净收益。

## 具体动作与止损条件

用合成回答和工作样本验证报告、澄清、中断及人工改判；真实候选人试点另行授权。

停止投入条件：越权使用数据、故障被判不合格、关键评分不可追溯或复核支持后持续负贡献即停止扩展。

## 来源与对应关系

- [Sdirectory] [许可目录现场正文](https://agentusecases.ai/use-case/run-ai-led-technical-interviews-for-recruiting)：目录将3000+/日、85%及客户团队变化标为供应商自述，并保留Claude试用模板。
- [Soriginal] [Anthropic micro1客户案例](https://www.anthropic.com/customers/micro1)：实际跳转claude.com/customers/micro1；供应商叙述Claude技术对话和报告，没有给出成本与通过率指标的独立审计方法。
- [Spaper] [Zara候选人反馈研究](https://arxiv.org/html/2507.02869v1)：研究描述GPT-4o实现；三日4820次不成功面试，400个候选评分均值4.37/5，不能当标准NPS或Claude案例成本验证。
- [Sprivacy] [micro1候选人隐私说明](https://www.micro1.ai/legal/privacy-notice-candidates)：2026-07-21版本列录制与评估数据、自有模型训练及退出入口；称最终决定前人工复核。属于政策文本而非执行审计。
- [Sada] [司法部招聘技术与残障歧视指导](https://www.ada.gov/resources/ai-guidance/)：2022-05-12指导强调岗位相关技能、评估筛除影响及合理便利；本轮核实公开页面，不判断特定雇主违法。
- [Scompetitor] [HackerRank官方FAQ](https://www.hackerrank.com/frequently-asked-questions)：现成技术面试工具支持协作编码、报告与招聘系统集成；本轮不采用未读成功的定价页报价。
- [Spositive] [PracHub正面候选人叙述](https://prachub.com/interview-experiences/micro1-software-engineer-fifty-minute-zara-ai-interview-6ec5c8c874)：2026-09-17编辑发布，称六月工程面试节奏可预期并获offer；身份和结果未独立验证，正文难度与标签不一致。
- [Snegative] [PracHub面试不稳定叙述](https://prachub.com/interview-experiences/micro1-software-engineer-interview-ai-assessment-instability-f018cacf4e)：2026-09-04编辑发布，称七月技术任务具体但一次异常未产结果；匿名自述不构成故障率统计。
- [Sexperience] [UX岗位第一人称Zara体验](https://aitrainer.work/guides/micro1-zara-interview-experience)：2026-09-04发布、10-01更新的非技术岗位体验，称练习有帮助，也出现思考出声被当作答案；不代表工程岗位或整体录用结果。

结构化记录：[research/run-ai-led-technical-interviews-for-recruiting.json](../research/run-ai-led-technical-interviews-for-recruiting.json)
