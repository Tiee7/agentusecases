# 用 Claude Code 裁决子智能体和分阶段审查开发应用

## English

    Build apps with a judge subagent and multi-stage review
    A Claude Code setup for app development uses a judge subagent, context management, and multi-stage review for quality control.
    Done with
    CC
    Claude Code
    What they did
    The post describes a solo developer using Claude Code to build a Windows app with a separate read-only judge subagent for unresolved decisions. The judge had to label claims as confirmed, guessed, or unknown and avoid deciding from guesses; the developer also started each issue in a fresh child session, then ran two review passes on code: a general code review and a second pass using coding-guideline skills, with deferred issues left in PRs for human review.
    How it went
    The workflow reportedly led to a Microsoft Store shipment and 142 merged PRs in 17 days. The post also notes the setup is complex and may be hard for beginners.
    Worth knowing
    The main catch is overhead: this workflow adds fresh sessions, a separate judge, and two review stages, so it is presented as an advanced setup rather than a lightweight default.
    Try it yourself
    with
    Claude Code
    Copy prompt
    Set up my project in [repo path] so that after you implement each feature of [app description], a separate judge subagent reviews the work against the requirements and tests and sends back a list of problems. Repeat the fix and review loop until the judge has no blocking issues. Keep a short notes file of decisions so context survives between sessions, and summarize the final state when finished.
    Original source: https://www.reddit.com/r/ClaudeWorkflows/comments/1x9vwqf/workflow_advanced_claude_code_workflow_judge

## 中文

    使用裁决子智能体和多阶段审查开发应用
    这套用于应用开发的 Claude Code 配置，通过裁决子智能体、上下文管理和多阶段审查进行质量控制。
    使用工具
    CC
    Claude Code
    做了什么
    帖子描述了一位独立开发者使用 Claude Code 开发 Windows 应用，并将尚未解决的决策交给一个独立、只读的裁决子智能体。裁决者必须把说法标为已确认、推测或未知，且不能以推测作出决定。开发者还会为每个问题开启全新的子会话，然后对代码进行两轮审查：先做一般代码审查，再用编码规范技能做第二轮检查；暂缓处理的问题留在拉取请求中，交由人工审阅。
    结果如何
    据帖子转述，这套流程促成了应用在 Microsoft Store 上架，并在17天内合并142个拉取请求。帖子也指出，配置较复杂，初学者可能难以掌握。
    值得注意
    主要代价是额外开销：流程增加了新会话、独立裁决者和两轮审查，因此它被呈现为高级配置，而非轻量的默认方案。
    亲自试用
    使用
    Claude Code
    复制提示词
    请配置我在[仓库路径]中的项目：每次你实现[应用描述]的一个功能后，由独立的裁决子智能体依据需求和测试审查工作，并返回问题清单。重复修复与审查循环，直到裁决者认为没有阻塞性问题。保留一份简短决策笔记，使上下文能跨会话延续；结束时总结最终状态。
    原始来源：https://www.reddit.com/r/ClaudeWorkflows/comments/1x9vwqf/workflow_advanced_claude_code_workflow_judge

## 原作者的方法与来源

来源：[作者开发回顾：Jotteo与可逆决策](https://note.com/lirispp/n/n4112b5c7b620)

作者方法摘要

1. 只读裁决者区分可逆决策与需要人工处理的重大决策。
   English summary: A read-only judge separates reversible decisions from consequential ones requiring human input.

2. 每个问题用新会话实现，再运行测试和两阶段审查。
   English summary: Fresh issue sessions implement changes, then run tests and two review stages.

3. 显式保留未审决策，并把特定设备验证留给人工。
   English summary: Keep unreviewed decisions visible and reserve device-specific verification for human review.

## 我们的分析

**商业结论：适合内部效率工具。先用于已有工程团队的受控审查流程，不把裁决提示词或免费应用上架直接当生意**

这个案例最有用的是把实现、证据核查和人工决策责任分开，适合已能写验收用例、管理权限并处理回归的小团队。可见资料不足以证明它降低总交付成本，更没有付费客户、缺陷率或留存对照。若经营服务，买方应购买可验收的工程改进和维护，而非几份通用提示词；若经营笔记应用，则仍要单独验证日常留存和相对现成免费产品的优势。当前因此先判为内部效率工具，不给未经证实的收入和商业分数。

案例ID：`build-apps-with-a-judge-subagent-and-multi-stage-review` · 案例来源：https://agentusecases.ai/use-case/build-apps-with-a-judge-subagent-and-multi-stage-review
研究时间：2026-10-21T08:49:24.868128+00:00

**商业评分：未评定；缺证不补零，不生成总分。**

| 维度 | 权重 | 分数 /5 | 商业依据 |
|---|---:|---:|---|
| 付费需求 | 20% | 待核实 | 工程审查痛点合理，但没有本流程的付费试点或采购预算证据，不能由开发者调查直接量化购买需求。 [Ssurvey, Ssupport] |
| 业务价值与效果证据 | 20% | 待核实 | 作者的PR合并数与上架陈述缺少对照工时和缺陷数据，也不能核对私有源码，不给效果百分制。 [Sauthor, Ssupport] |
| 单位经济与利润 | 20% | 待核实 | 仅有两种研究者假设的成本模型，真实售价、调用账单、返工分布与支持成本均未取得，利润未知。 [Sclaude, Sapp] |
| 获客与市场进入 | 15% | 待核实 | 未见销售渠道转换率、客户案例或复购资料；技术文章的可见度不能替代服务获客验证。 [Ssupport, Sapp] |
| 竞争壁垒 | 10% | 待核实 | 官方原生子智能体与公开规范降低方法独占性，尚未看到专有评测集或可验证的持续交付优势。 [Sclaude, Srust] |
| 交付与经营风险 | 10% | 待核实 | 权限限制和可测性可设计，但作者工程未执行，设备适配、恢复流程与发布责任的实际负担待测。 [Sclaude, Srust] |
| 独立用户反馈信号 | 5% | 待核实 | 没有核实到独立采用该开发流程并给出结果的客户样本；空issues不是差评也不是质量背书。 [Ssupport, Ssurvey] |

## 自用价值：中

有工程基础的人可借鉴只读复核和证据记录，但实际节省时间取决于已有验收能力；对初学者额外配置可能增加负担。

依据：Sclaude, Srust, Sauthor

- 适用人群：已有代码库与测试基础的独立开发者或小团队；不是无需编程知识的全自动造应用方案。
- 用途：在实现之外设置独立检查，把可逆小决策与需要负责人确认的大决策分开，记录版本与未决问题。
- 预期收益：预期减少自我确认式审查与上下文混乱；未量化净节省、缺陷下降或交付成功率。
- 设置成本：准备仓库副本、需求和验收样例、只读角色权限、合并规则及真实设备验证清单；不需要本任务新建凭据。
- 维护成本：每次模型、依赖或业务规则变化后维护测试和权限；清理误报、未审决策及失效来源仍需人工。
- 使用频率：适合持续迭代时按任务调用；低频一次性脚本可先用普通测试和人工审查，避免固定开销。
- 隐私风险：审查者读取的代码和日志仍有泄露风险，限制可见范围并排除凭据及生产个人数据。
- 错误风险：多个角色可能共享需求误读，测试可能只是复述实现；真实设备与上线状态必须另验。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/build-apps-with-a-judge-subagent-and-multi-stage-review

建议工具：Claude Code

    Set up my project in [repo path] so that after you implement each feature of [app description], a separate judge subagent reviews the work against the requirements and tests and sends back a list of problems. Repeat the fix and review loop until the judge has no blocking issues. Keep a short notes file of decisions so context survives between sessions, and summarize the final state when finished.

自编试用模板

准备条件：有授权的测试仓库、一个明确小功能、已知通过与失败样例、可回滚分支；先确认只读审查者的实际工具权限。

工具：Claude Code及其子智能体、版本控制、项目自身测试；不自动安装或接入真实客户系统。

预期结果：得到问题清单及其代码位置、修复提交、未决事项、实际执行检查与设备验收缺口；不预设首次成功或商业收益。

### 限定范围的只读复核模板

自编模板

出处：研究团队自编

依据：Sclaude, Srust

    在已授权测试仓库中，只审查指定基线到当前提交的这一项功能。逐条对照验收条件，列出文件位置、可复现输入与结果；区分事实、推断、未知。不要改文件，不运行写入外部系统的动作，不处理无关任务。报告未覆盖的设备与环境检查。只有负责人允许后实现者才能修改或发布；结束时列出确切提交和检查状态。

## 已核验事实

- 目录将实际工具标为Claude Code，并给出独立的建议试用模板；模板不等于作者实际提示词。 [Sdirectory]
- 作者回顾把决策可逆性作为自动推进与人工介入的分界；这是一名开发者自述的方法，不是对照实验。 [Sauthor]
- 作者截至2026年10月13日自述17天合并142个PR，同时152项AI决策只人工审阅1项；不能把合并数量当缺陷少或收益高。 [Sauthor]
- Claude Code官方说明子智能体有独立上下文并可限制工具，但其请求仍计入共享用量限额。 [Sclaude]
- 微软Rust规范把可测试API与行为覆盖列为AI协作工程条件，并提醒避免只复述定义的测试。 [Srust]
- Jotteo作者在10月18日称现有功能免费、无广告和无需注册，未来只可能对部分新增功能收费；不是现有订阅收入证明。 [Sapp]
- 2025 Stack Overflow调查中不信任AI输出准确性的比例高于信任比例；这一历史样本只能辅助解释复核需求。 [Ssurvey]
- 微软官方页面列有可免费使用的OneNote和支持本地笔记的Windows桌面版，构成具体替代，而非空白市场。 [Sonenote]
- 公开jotteo-support仓库明确不含应用源码；当前空issues列表不能核验作者私有应用的PR数量或用户质量。 [Ssupport]

## 谁真正需要，谁会付钱

本案应拆成两类用户，而不能用“独立开发者做出了应用”混为一种需求。第一类是已经持续维护软件的小团队、技术负责人或独立开发者，他们缺的是把需求、实现、审查、设备验证连起来的可靠流程。工具使用者往往就是工程师，潜在预算所有者则是承担延期和事故责任的负责人。第二类是Windows手写笔记用户，他们关心笔迹、PDF、检索、备份和数据迁移，不会因为开发过程用了裁决智能体就付钱。作者发布说明能够帮助界定后一人群，但没有揭示其中多少人持续使用或愿意购买。我们的判断是：先把流程用于内部工程交付，产品端另行评估，不能把两边的利益混合计算。对小型一次性脚本，增加多阶段审查可能比问题本身更贵；对有文件格式、用户数据和设备适配的软件，遗漏的返工成本更值得测量。这是场景推断，不是已有客户调查。付款问题最终应落到“谁为少一次返工或更清楚的验收证据买单”，而非“谁喜欢多智能体”。

依据：Sauthor, Sapp, Ssurvey

## 从需求到可验收交付

可复制对象不是一句让judge检查的提示词，而是一条有版本和证据的交付链：先固定需求与验收输入，再由实现者提交可复核变更，裁决者仅返回有位置、有依据的问题，最后由构建、测试及适用设备验证确认结果。官方工具权限支持把审查者限制为读文件等能力，但实际配置仍需逐项检查；不要假定它因为名字叫只读就不可能执行写入。建议保留任务标识、基线提交、问题清单、修复提交和最终验证产物，让审查结论能对应到确切代码。每轮应区分代码错误、测试夹具失效和环境故障，避免为了全绿删除有效断言。审查者说“没有阻塞”只说明这次检查未发现问题，不是全面正确证明。对于设备输入、渲染或系统集成，单独列出不能被本地合成测试覆盖的项目。我们没有安装作者应用或运行他的私有工程；上述链路是从公开方法抽取的实施建议，不是已完成客户部署。

依据：Sdirectory, Sclaude, Srust

## 需求信号与市场证据边界

审查需求有合理动机，但不能从AI使用增长推导某个裁决流程的付费市场。2025开发者调查的信任问题说明人们担心输出准确性，调查时间、样本自选和问题措辞都限制外推；它没有问受访者是否购买本案配置。真正应找的需求信号，是团队已有未处理缺陷、审查排队或重复返工，以及他们愿意提供基线和接受明确验收。作者的开发记录是一个方法线索，而不是企业需求样本。若将它作为服务，优先限定一种代码栈和一种交付单位，先测流程是否减少总工时；若推广为通用平台，必须承担更多权限、项目差异和支持成本。也不能把独立开源项目或工具教程中的热度当采购预算。市场规模在此保留未知，不编造团队数量、转换率或客单价。与其估算一个缺乏证据的大市场，不如把能被一次授权试点证伪的条件写清：真实任务重复发生，结果可量化，负责人愿意把人工复核计入成本。

依据：Ssurvey, Ssupport, Sclaude

## 替代品来自工程流程和终端产品两侧

流程侧最直接的替代不是另一个名字相近的judge插件，而是工程师自己采用官方子智能体能力、成熟的编译测试、人工代码评审和清晰的合并规则。已有团队往往不需要再购买通用提示词，而需要针对其代码库排除具体失败模式。可销售的差异只能建立在适配、回归样本、权限配置和持续维护上。产品侧则不能把免费、本地存储、手写笔记都当独占优势：微软官方OneNote资料已覆盖免费使用及Windows桌面本地笔记能力。比较时应限定具体任务，例如同一设备导入一份PDF、手写一页、检索并导出，而不是泛称谁更好。不同应用在数据格式、同步和输入体验上可能有差别，但本轮没有运行对比，不能编造胜负。若用户现有工具已经完成任务，迁移成本本身就是强反证。最终应把“开发效率更高”与“用户愿意换软件”当成两个独立假设，分别取得证据，而不是让前者替代后者。

依据：Sclaude, Srust, Sonenote

## 按验收后的任务计算，而非按PR数量

本轮不填售价和利润，收入状态为未知。两种成本情景以一个通过验收的小功能为单位，不以一次调用或一个PR为单位：简单场景假设工具调用摊销3美元、人工20分钟按60美元每小时计20美元、其他可变成本3美元、获客摊销5美元，合计31美元；每月20个单位加40美元固定费，总成本660美元。复杂场景假设8美元工具成本、人工60分钟计60美元、其他8美元、获客10美元，合计86美元；每月20个加80美元固定费，总成本1800美元。所有输入都是研究者假设，不是作者账单，也不绑定某个订阅价格。人工应包含解释需求、筛掉误报、真实设备验证、回读部署和事后支持，而非只算写代码的时间。若拿31美元作为报价下限还不够，因为失败任务、退款和未成交沟通未必均匀摊销。内部自用可把获客项设零重新计算，但不能因此把人工变免费。多个子智能体共用用量预算，重试和额外上下文都会吃掉节省，需在试点里单独记录。

依据：Sclaude, Srust

## 怎样获得第一批客户并交付

当前没有证据说明作者出售了流程配置或获得外部服务收入，因此以下是待验证的获客方案，不是经营成果。最小服务应面向已有工程负责人、已有代码和明确验收的小团队，展示一个可复查的前后对照，而不是宣传一天生成多少代码。客户需要看到失败样例、边界和回滚办法，才可能评估是否值得让外部流程接触仓库。交付物可以是只读审查规则、权限清单、验收用例和一份带提交号的试点报告，后续维护应明确包含哪些升级与故障。触达渠道可考虑已有技术合作关系和公开案例展示，但本任务只做研究，不发送信息、不接入客户仓库也不代收款。销售周期、购买人和持续付费仍未知。免费内容能够帮助建立可信度，但若只能吸引想复制提示词的人，不足以支撑持续服务；应把成功指标放在完成有预算的试点和复购维护，而不是教程浏览量。也不能默认可把作者文章或私有配置打包销售，原创交付与许可边界必须独立处理。

依据：Ssupport, Sclaude, Sapp

## 壁垒应是累积的失败知识，而非角色名字

裁决者、实现者和分阶段审查这些构件容易被复制，官方产品已经提供基础能力。因此，把一个角色文件当作长期壁垒并不稳健。若要形成可积累价值，应该来自某一行业或代码栈的真实失败样本、可复现回归用例、稳定的交付约束和对系统边界的理解。每次问题都能落到明确输入与断言，下一次才有机会更快识别，而不是让模型重新猜测。反过来，若审查规范只是泛泛要求“代码质量高”，它既难以验收也容易被替代。还要防止指标被流程自己优化：发现问题多、合并PR多、反复给出通过结论，都不等于交付价值上升。应记录漏检、误报、人工撤销决策及发布后的回归，允许这些记录推翻最初假设。两次同模型审查也不构成统计意义的独立验证；共享需求误读可能在所有角色中重复。长期维护的优势应体现在更少真实故障和更低总成本，而非更多自动化层级。

依据：Sclaude, Srust, Ssurvey

## 权限、隐私、交付与责任

要复用该方法，先限定测试仓库、可读取目录、允许执行的检查，以及哪些动作必须由负责人确认。源码、日志、客户数据和认证材料不能为了审查方便被全量上传。让审查者只读能降低它意外改坏文件的风险，但它读到的内容仍可能敏感；角色隔离与数据访问授权不是一回事。对不可逆数据格式、外部发布或付费动作，应有真实权限控制，而不是只靠提示词提醒。验收应覆盖恢复路径：中断后如何找到原任务和提交，如何识别已经成功的发布，如何避免同一任务重复执行，以及如何保存不可丢失的证据。代码层测试、实际设备测试和上线回读分别记录，不能互相冒充。作为服务方也不能承诺把所有判断责任移给模型，客户仍需指定需求与最终责任人。作者产品关于本机存储的说明只涉及终端应用的设计自述，不自动证明开发过程中源码或笔记没有进入第三方服务；两条数据路径要分别审查。

依据：Sclaude, Sapp, Srust

## 反馈调查与反证怎样改变判断

暂无直接用户反馈。

依据：Ssupport, Ssurvey, Sdirectory, Sauthor

## 最小可执行验证与停止条件

当前结论是内部效率工具，而不是已经验证的独立生意。可执行的下一步是选一个有权限、无敏感生产数据的小仓库，先建立人工认可的验收样例，再用同等难度任务比较原流程与新流程。只统计最终接受的交付，记录总人工分钟、模型调用成本、误报和漏检、恢复次数及设备验收发现的问题。样本不足时不宣称普遍提效，发生关键回归时应扩大对应测试而不是放宽标准。如果流程省下的实现时间被审查、反复解释和维护耗尽，就停止增加角色；若只在作者熟悉的工程上可用，不能直接出售通用承诺。若要做笔记应用商业化，则另测同一批用户在现成替代与新应用之间的真实迁移、重复使用和愿付，不能拿工程交付数字代替市场验证。本文给出的成本情景只是帮助确定需要测什么，不是收入预测，也不是四周或200美元的准入规则。本轮未安装应用、未执行原流程、未联系任何人；文档审查和算术验证的边界随报告保留。

依据：Sonenote, Sclaude, Sapp, Ssurvey

## 单位经济测算：情景假设，不是项目已实现的财务结果

| 情景 / 交付单位 | 收入 | 可变成本（含获客） | 单位贡献 | 月交付量 | 月固定成本 | 月经营贡献 |
|---|---:|---:|---:|---:|---:|---:|
| 研究者假设：简单变更 / 一个验收通过的小功能 (USD) | 待核实 | 31.00 | 待核实 | 20 | 40.00 | 待核实 |
| 研究者假设：复杂变更 / 一个验收通过的小功能 (USD) | 待核实 | 86.00 | 待核实 | 20 | 80.00 | 待核实 |

研究者假设：简单变更假设：全部输入是假设；人工20分钟×60美元/小时=20；工具3、其他3、获客5；单位31，每月31×20+40=660，无真实售价。；API成本 3，人工成本 20，其他可变成本 3，分摊获客成本 5。依据：Sclaude, Srust

研究者假设：复杂变更假设：全部输入是假设；人工60分钟×60美元/小时=60；工具8、其他8、获客10；单位86，每月86×20+80=1800，无真实售价。；API成本 8，人工成本 60，其他可变成本 8，分摊获客成本 10。依据：Sclaude, Srust

## 反证与未核实信息

作者未审决策负债、公开仓库不含应用源码、现成免费本地笔记替代以及缺少净工时/付费验证，共同限制从产出速度推导生意成立。

未安装Jotteo、未运行作者私有工程、未取得142PR列表或到账/留存资料。2025调查不是2026销量。源站建议模板不是作者实际提示词。原在途稿丢失后，本篇基于保留归档和重新读取的来源完成恢复，未冒称旧草稿复原；云浏览器note两次普通导航超时，采用支持的公开网页阅读器，未绕限制。

## 具体动作与止损条件

在有授权的单个测试仓库选取同等难度的小任务，记录原流程与裁决流程的人类总工时、验收缺陷、调用费用和返工；把未决事项及实际设备测试单列。先做内部验证，不联系或代运营客户。

停止投入条件：若审查误报与返工抵消节省，或需反复人工解释才能完成基本需求，停止扩展；若设备问题仍被单元测试漏过，不出售无人值守交付承诺。

## 来源与对应关系

- [Sdirectory] [获许可案例目录：裁决子智能体与多阶段审查](https://agentusecases.ai/use-case/build-apps-with-a-judge-subagent-and-multi-stage-review)：许可目录归档保留Claude Code、只读裁决、两阶段审查及完整Copy prompt；142 PR/17天为目录转述，不是实测或收入。
- [Sauthor] [作者开发回顾：Jotteo与可逆决策](https://note.com/lirispp/n/n4112b5c7b620)：作者自述按决策可逆性分工，使用只读judge与每Issue新会话；截至10月13日合并142PR/17天，152项AI决策只人工审过1项，部分Windows实机验证仍需人。10月15日补记v1.0上架。并非独立效率或缺陷率测量。
- [Sclaude] [Claude Code官方子智能体文档](https://code.claude.com/docs/en/sub-agents)：官方允许独立上下文、工具白名单和权限配置；子智能体请求占用同一用量限额。配置只读工具是能力限制，不能把提示词宣称只读当作权限隔离。
- [Srust] [微软Rust AI工程规范](https://microsoft.github.io/rust-guidelines/guidelines/ai/index.html)：规范强调类型、文档、可测试API和有意义行为测试，并反对只重复定义的同义反复测试；可作为复核规则来源，而非某应用质量认证。
- [Sapp] [作者Jotteo产品发布说明](https://note.com/lirispp/n/n2e443e811f2d)：10月18日作者称Jotteo免费、无广告、无需账户，笔记及手写识别留在本机；已有功能保持免费，未来可能只对部分新功能收费。面向Windows手写/PDF记录人群，未见销量、活跃或到账证明。
- [Ssurvey] [2025 Stack Overflow开发者调查](https://survey.stackoverflow.co/2025/ai)：历史调查页面显示46%受访开发者不信任AI输出准确性，33%信任；这是2025受访者态度，不能当2026审查服务销量或本方法增益。
- [Sonenote] [Microsoft官方OneNote版本对比](https://support.microsoft.com/en-us/onenote/what-s-the-difference-between-the-onenote-versions)：官方页面列出受支持OneNote版本可免费下载使用及部分付费高级功能；Windows桌面版支持本地笔记存储。免费和本地存储因此不是Jotteo独有卖点，未实测手写体验。
- [Ssupport] [Jotteo公开支持仓库](https://github.com/liris/jotteo-support)：公开README明确仓库只放支持、帮助与隐私政策，不含应用源码；公开issues列表当前为空，不能据此验证私有应用142PR，也不能推导没有缺陷。

结构化记录：[research/build-apps-with-a-judge-subagent-and-multi-stage-review.json](../research/build-apps-with-a-judge-subagent-and-multi-stage-review.json)
