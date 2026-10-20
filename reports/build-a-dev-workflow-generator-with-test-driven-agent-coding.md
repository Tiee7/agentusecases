# 用Claude Code构建项目开发工作流生成器

## 中文

    通过测试驱动的agent编程构建开发工作流生成器
    作者完全使用Claude Code构建了一个开源系统，通过访谈生成项目专用的开发工作流；Claude Code编写并调试了550多项测试。
    使用的是
    Claude Code
    他们做了什么
    作者称，整个系统都在Claude Code会话中构建：通过/bootstrap访谈了解项目技术栈后，生成项目专用的斜杠命令、防护钩子、推送前检查和agent配置。Claude Code还编写了主要代码文件，在测试驱动工作流中生成并调试550多项测试，使用四个并行审查agent开展自审，并通过/task-hunter和Backlog.md CLI自主选择任务、实现改动、提交和关闭任务。
    进展与成效
    产出是采用MIT许可的开源工作流系统；作者称它包含1.5万多行代码、200多项任务和20多个钩子文件，支持许多常见Web技术栈以及通用模式。作者指出的不足是Claude Code需要防护措施：没有钩子、任务结构和自动审查，它会写入错误目录、丢失上下文，并漏过细微错误。
    值得注意
    要按描述试用，需要Claude Code CLI和Backlog.md CLI，然后将模板指向自己的代码库并运行/bootstrap。
    亲自尝试
    使用
    Claude Code
    复制提示词
    帮助我用[语言]通过测试驱动开发构建[实现X的工具]。对于每个功能，先编写会失败的测试，再编写使测试通过的代码；每完成一步就运行完整测试套件，并自行调试失败项。当[功能列表]全部实现且所有测试通过时停止，然后总结测试覆盖范围。
    原始来源：https://www.reddit.com/r/claude/comments/1s383nj/i_built_agentic_workflow_entirely_with_claude

<details><summary>English original</summary>

    Build a dev-workflow generator with test-driven agent coding
    The author built an open-source system that generates project-specific dev workflows from an interview, entirely with Claude Code, which wrote and debugged 550+ tests.
    Done with
    CC
    Claude Code
    What they did
    The author says they built the whole system through Claude Code sessions: after a /bootstrap interview about a project's stack, it generates project-specific slash commands, guard hooks, pre-push checks, and agent configs. Claude Code also wrote the main code files, produced and debugged 550+ tests in a test-driven workflow, ran self-audits with four parallel review agents, and, via /task-hunter plus Backlog.md CLI, picked tasks, implemented changes, committed, and closed them autonomously.
    How it went
    The result was an open-source, MIT-licensed workflow system the author says spans 15k+ lines, 200+ tasks, 20+ hook files, and supports many common web stacks plus a generic mode. The stated shortcoming was that Claude Code needed guardrails: without hooks, task structure, and automated review, it wrote to wrong directories, lost context, and let subtle bugs through.
    Worth knowing
    To try it as described, you need both Claude Code CLI and Backlog.md CLI, then point the template at your codebase and run /bootstrap.
    Try it yourself
    with
    Claude Code
    Copy prompt
    Help me build [tool that does X] in [language] using test-driven development. For each feature, write failing tests first, then the code to make them pass, and run the full suite after each step, debugging any failures yourself. Stop when [the feature list] is implemented and all tests pass, then summarize the test coverage.
    Original source: https://www.reddit.com/r/claude/comments/1s383nj/i_built_agentic_workflow_entirely_with_claude

</details>

## 原作者的方法与来源

来源：[AdEast5873 describes test-driven generation and review](https://www.reddit.com/r/claude/comments/1s383nj/i_built_agentic_workflow_entirely_with_claude)

作者方法摘要

1. 访谈项目技术栈，生成命令、钩子与agent配置。
   English summary: Interview the project stack and generate commands, hooks and agent configurations.

2. 使用Claude Code编写测试和实现，再用并行agent审查产出。
   English summary: Use Claude Code to write tests and implementation, then review output with parallel agents.

3. 通过Backlog.md跟踪任务，由task-hunter实现、测试、提交并关闭限定工作。
   English summary: Track tasks through Backlog.md and let task-hunter implement, test, commit and close scoped work.

## 我们的分析

**商业结论：适合内部效率工具。流程生成有具体实现，但提醒与强制门禁不能混为一谈**

作者提供可追溯的开源实现和开发流程，适合已有测试与审查能力的团队参考。当前代码显示提醒、提交前测试和推送前告警具有不同语义，多宿主也不自动共享Claude钩子保护。没有独立付费客户、实际交付工时和净节省证据，外部接入服务仍应限定试点，不能把历史测试数或自动提交数量当作收益。

案例ID：`build-a-dev-workflow-generator-with-test-driven-agent-coding` · 案例来源：https://agentusecases.ai/use-case/build-a-dev-workflow-generator-with-test-driven-agent-coding
研究时间：2026-10-20T21:48:20.558058+00:00

**商业评分：未评定；缺证不补零，不生成总分。**

| 维度 | 权重 | 分数 /5 | 商业依据 |
|---|---:|---:|---|
| 付费需求 | 20% | 待核实 | 有开发者自用痛点与历史行业复核需求，但本产品真实付款人和采购规模未知。 [Srepo, Sauthor, Sfeedback] |
| 业务价值与效果证据 | 20% | 待核实 | 公开代码能证明机制存在，550项测试属于作者自述，没有独立运行和业务效果对照。 [Srepo, Sauthor, Sfeedback] |
| 单位经济与利润 | 20% | 待核实 | 双情景只作人工与维护预算，缺实际成本和成交价，不据此生成盈利分数。 [Srepo, Sauthor, Sfeedback] |
| 获客与市场进入 | 15% | 待核实 | 社区及开源是实际展示入口，未取得线索转化与获客成本，不等同稳定销售渠道。 [Srepo, Sauthor, Sfeedback] |
| 竞争壁垒 | 10% | 待核实 | MIT模板容易复制，跨栈适配与回归资产可能积累但尚无持续客户和续费证据。 [Srepo, Sauthor, Sfeedback] |
| 交付与经营风险 | 10% | 待核实 | 提醒与阻断语义不同，多宿主运行边界需验证，当前静态阅读不足以打稳定性分。 [Srepo, Sauthor, Sfeedback] |
| 独立用户反馈信号 | 5% | 待核实 | 搜索与公开PR未取得独立客户效果；缺证不是负面评价，也不拿作者跨帖凑样本。 [Srepo, Sauthor, Sfeedback] |

## 自用价值：中

推断：对已有工程审查能力的多项目开发者有可检查的流程参考；收益需自有项目验证。

依据：Srepo, Scode, Sgitcode

- 适用人群：能维护测试与配置的开发者、工作室技术负责人。
- 用途：生成项目专用任务、审查、提交和配置流程。
- 预期收益：可能减少重复配置和会话交接遗漏，没有量化净省时证据。
- 设置成本：技术栈访谈、已有测试核对、Backlog/basic-memory等依赖与钩子兼容审查。
- 维护成本：宿主升级、规则失效、路径变更、共享记忆及回归维护。
- 使用频率：按任务执行，项目接入或技术栈变更时更新配置；真实频率未知。
- 隐私风险：任务与共享记忆可能包含客户代码结构或秘密，应隔离并脱敏。
- 错误风险：误认提醒为硬阻断、配置覆盖、错误目录、同模型测试与实现共同误解需求。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/build-a-dev-workflow-generator-with-test-driven-agent-coding

建议工具：Claude Code

    Help me build [tool that does X] in [language] using test-driven development. For each feature, write failing tests first, then the code to make them pass, and run the full suite after each step, debugging any failures yourself. Stop when [the feature list] is implemented and all tests pass, then summarize the test coverage.

自编试用模板

准备条件：获准非敏感演示仓库、可恢复副本、既有测试命令、明确不改范围和人工验收人。

工具：获准编码agent；本项目当前依赖与宿主适配需审查，本轮未安装或运行。

预期结果：配置差异和负向验收计划，区分提醒、警告、阻断与实际执行；未实测。

### 源站Copy prompt

原文模板

出处：https://agentusecases.ai/use-case/build-a-dev-workflow-generator-with-test-driven-agent-coding

依据：Sdirectory

    Help me build [tool that does X] in [language] using test-driven development. For each feature, write failing tests first, then the code to make them pass, and run the full suite after each step, debugging any failures yourself. Stop when [the feature list] is implemented and all tests pass, then summarize the test coverage.

### 先检查再接入工作流

自编模板

出处：研究团队自编

依据：Srepo, Scode, Sgitcode

    只读审查[演示仓库]现有任务、测试、CI和钩子。列出工作流生成器适配方案，逐项区分提醒、警告和硬阻断；写出缺少可执行位、路径错误、失败测试及宿主切换的负向验收。不要安装依赖、覆盖配置、连接真实数据库或发布。先给差异、未知项与撤回计划，等待我批准具体改动。

## 已核验事实

- 原作者称Claude Code编写550多项测试并通过四agent审查自己的输出，数字是历史自述。 [Sauthor]
- 当前固定提交README将产品描述为多宿主共同工作流，Claude钩子不会自动在其他宿主运行。 [Srepo]
- 当前README列出Backlog.md与basic-memory依赖，graphify是可选项而不是必装。 [Srepo]
- MIT许可允许使用修改和分发软件，要求保留版权与许可说明，不提供效果保证。 [Slicense]
- test-enforcer静态模板发送systemMessage后退出成功，并不直接运行测试。 [Scode]
- 生成器的测试命令生成位于GIT_PRECOMMIT_TEST，推送前破坏性迁移逻辑增加警告计数。 [Sgitcode]
- Git官方说明没有可执行位的钩子会被忽略，hooksPath可改变加载位置。 [Sgit]
- 2025调查准确性问题33244名回答者中46%不信任、33%信任AI输出，是历史态度而非本项目购买数据。 [Smarket]
- Backlog.md提供Markdown任务及规格、计划、代码检查点，可作为较轻流程组成部分。 [Scompetitor]
- 固定SHA查询未取得Actions运行记录，公开工作流配置存在不能当作该SHA已通过测试。 [Sci]

## 谁需要它、谁可能付费

使用者首先是已经让编码agent参与真实项目的开发者或技术负责人，不是想完全跳过工程判断的初学者。访谈生成规则的价值，在于把项目技术栈、目录、测试命令和交付习惯统一起来，减少每次会话重新解释。可能的付款人是管理多个相似代码库的工作室负责人，预算来自开发工具或项目交付；但本次没有看到该项目收费方案、付费客户或采购合同，这只是服务模式假设，不是原作者收入机制。
可出售的最小交付单位应是一份单仓库工作流接入包：确认既有构建与测试、映射路径、生成可审查配置、演示失败如何阻断、留下维护与撤回说明。不能以模板文件数量作为验收，也不能承诺接入后无需人审。只有一个小脚本、已有稳定CI和任务规范的团队，直接用Backlog.md或现有任务系统可能更省事。要验证的不是客户愿不愿意“用AI”，而是哪些反复返工真的由配置与流程缺失造成，现有负责人愿意为减少多少工作支付什么。

依据：Sauthor, Srepo, Scompetitor

## 从访谈到提交的实际链路

历史原帖描述由访谈了解技术栈，生成专用命令、钩子和配置，随后以Backlog.md任务驱动实现、测试、审查和提交。550多项测试是作者对当时开发过程的报数，公开代码支持确有生成器与测试结构，但不能恢复每次“先红后绿”的执行顺序，也不能证明所有功能都经独立验收。测试由同一模型生成并审查时，可能一起误解需求；重复审查角色增加视角，不自动构成独立正确性证明。
本次固定到2026-09-24提交8112ecc9，当前README已扩展为多宿主。generate.js生成共同流程，transform.js转换宿主适配，不等于每种宿主具有相同钩子运行时。静态检查发现test-enforcer只发提醒，不运行测试；真正的测试命令生成属于pre-commit阶段。pre-push中的破坏性迁移只报警继续。接入包必须分别交付“生成了什么”“什么已启用”“哪种失败会停下”“谁做业务验收”，不能把一个BOOTSTRAP_COMPLETE标记扩张成产品已安全可用。

依据：Sauthor, Srepo, Scode, Sgitcode

## 需求信号和市场边界

2025年Stack Overflow调查的准确性问题有33244名回答者，其中46%不信任AI输出、33%信任。这是历史受访者态度，支持人工核查仍重要，不是2026年开发者总体比例，更不是愿为本模板付钱的客户数量。不能将不信任直接乘开发者人数得到市场规模；不信任也可能使客户减少agent使用，而不是购买另一层自动化。
本项目的展示贴说明开发者愿意公开分享流程痛点，但作者本身既是制作人也是使用人。公开问题查询本次只得到贡献和机器人PR，没有可核实客户节省时间或付费评价。市场进入应从已在使用编码agent、明确遇到目录误写或回归漏项的团队开始，区分“偶发错误”和每周真实重复成本。研究判断是内部工具有明确机制参考，外部服务需求仍需逐个验证。行业通用调查只能提供背景，不能替代本项目的客户访谈、采购记录和长期留存。

依据：Smarket, Sauthor, Sfeedback

## 为什么不直接用现有工具

最直接替代不是另买一个大平台，而是现有Git仓库、CI、少量原生Claude钩子和Backlog.md任务记录。Backlog.md本身已经提供规格、计划、代码三个检查点，团队若只是缺少可核对验收条件，未必需要完整生成器。Git和宿主官方文档可用于手动配置窄范围检查，维护面较小；代价是每个仓库要自行整理命令与路径。生成器的优势是重复配置和跨栈模板化，而不是创造此前不存在的测试能力。
转换成本包括现有钩子如何保留、团队已用哪些任务ID、共享记忆写入哪里、升级后谁复核。当前README明确其他宿主不会自动运行Claude钩子，因此多CLI文件生成不能当保护一致性保证。比较应在同一演示项目、同一失败用例下计算设置工时和后续维修，而非对比自动生成多少文件。对稳定老项目，薄层接入通常更容易审计；对大量同构新项目，模板可能节省重复工作，但需要实际测量。

依据：Scompetitor, Shooks, Sgit, Srepo

## 成本按单仓库接入包计算

以下均是研究者预算，不是作者账单、软件现价或已成交报价。统一单位为一份单仓库工作流接入包，包含技术栈访谈、生成配置、有限负向验收和交接，不含无限需求开发。低适配情景：人工4小时×40美元=160；模型/测试推理预算10，测试环境等其他变量10，获客沟通摊销40，合计220/包。每月4包加固定工具预算40，列出成本920/月。高适配情景：人工10小时×40=400，模型30、其他20、获客80，共530/包；4包加固定80，总2200/月。
两者最重要差异是既有测试、钩子冲突和宿主适配，而不是模型单次输出长度。售价未知，收入、利润与回本不计算。MIT许可免费不等于交付免费，客户代码保密审查、旧流程迁移、版本升级和售后都可能继续消耗人工。后续若加持续维护，需单独限定周期与响应范围，不把一次接入费默认覆盖所有未来故障。收集实际记录后应替换预算，特别是交付后每周接管时间，避免只计第一次生成脚本的几分钟。

依据：Srepo, Sauthor

## 获客与交付样例

作者通过公开仓库和社区展示自己的工作流，属于可验证的分发入口；它证明有展示渠道，不证明渠道已有成交或稳定线索。若探索服务，先制作一个不含客户秘密的小型示例，展示从任务定义、配置差异、失败用例到恢复的全过程。让潜在客户看到的是原本漏过的检查现在如何被发现，而不是一张全部绿灯的截图。公开模板降低试用门槛，也让客户更容易自己接入，因此服务费必须对应具体适配与维护责任。
初期可以从已有技术合作关系中核实需求，先询问现有CI、权限、测试维护者和最常见返工，不主动批量发销售消息。报价前确定仓库范围、验收人、不可改的生产配置、是否包含培训。对于有严格安全采购的团队，审查钩子和共享记忆的成本不能略去。本文仅研究这些可能路径，没有联系作者、客户、创建账户或发送报价。单纯复制作者帖子或者把星标数当潜在客户池，都不能说明获客成本。

依据：Sauthor, Srepo, Slicense

## 可积累的是适配经验而非模板数量

MIT许可允许使用、修改和销售副本，保留版权与许可是基本条件。因此模板和命令本身容易复制，不能作为排他壁垒。更有可能积累的是不同技术栈的失败样例、已有钩子与CI的兼容清单、可回滚迁移办法以及真正减少人工接管的证据。客户选择服务方，可能因为其对旧系统和业务风险更熟悉，而不是因为生成器有更多斜杠命令。
这些资产也不能通过把客户代码或私人记忆混入公共模板来积累。应抽象成非敏感测试夹具、路径规则与审查清单。跨宿主适配看起来扩展市场，实际上增加运行语义差异和维护面；如果每次升级都要重做所有客户配置，规模收益会被人工吃掉。平台原生功能持续扩展也是替代压力，长期价值应当落在验收质量和集成稳定，而不是绑定某个命令名字。本次未取得续费、迁移成功率和长期客户案例，不给壁垒强度编造数字。

依据：Slicense, Srepo, Sgitcode

## 保护边界必须逐层核对

最值得注意的实质差异是提醒、警告和硬性阻断。test-enforcer在文件编辑后提醒相关测试，并设置五分钟去重；这不等于每次编辑都运行测试。生成器把测试执行放进提交前钩子，推送前迁移告警可能继续推送。目录保护脚本检查指定Edit/Write路径，异常分支静默，不能推论它隔离了所有shell、MCP或其他宿主写入。以上来自固定提交静态阅读，尚未在真实运行时复现，不把代码审查写成已利用漏洞或已完成安全认证。
Git官方说明钩子可执行位和hooksPath决定加载；Claude文档说明事件、输出及错误处理影响是否阻断。验收因此要包含未激活、路径失效、测试失败和宿主切换，而不仅是正常成功一次。共享记忆可能接触项目结构与任务信息，应限制敏感内容和跨客户混用。未核对授权前不要把生成器接到真实生产库或自动发布流程，保留现有分支保护与服务器CI。此次没有安装、运行该仓库、注册MCP或变更任何用户开发环境。

依据：Scode, Sgitcode, Sguard, Sgit, Shooks

## 反馈调查结果与反证

暂无直接用户反馈。

依据：Sfeedback, Sauthor, Srepo, Sci

## 适合内部效率工具，外部服务先限定试点

本案足以进行完整的来源驱动商业拆解：有公开许可、可检查实现、明确工作流和具体替代方案；它并没有提供可验证经营收入或独立效果对照。结论是适合内部效率工具，不把“能构建开源项目”扩张成“可以卖无人开发公司”。如果团队本来没有可运行测试、没有验收责任人，生成更多工作流文件无法补齐这些基本条件。自用可以从最常失败的一类任务开始，保留人工业务验收，不要求达到任何人为收入门槛。
拟议下一步是在可恢复、无生产凭据的演示仓库比较三种窄范围：现有流程、任务与原生CI、完整生成器。每种采用同一需求和负向用例，记录配置工时、返工时间、错误是否被发现以及升级是否破坏保护；不调用付费模型或改真实权限，除非另有授权。若为了跑通必须关闭已有保护、无法明确证明钩子已激活，或复核成本持续高于原流程，就停止扩展并缩小范围。只有实际客户接受边界且愿付价覆盖完整成本时，才讨论经营复制。

依据：Srepo, Sauthor, Scompetitor, Smarket

## 单位经济测算：情景假设，不是项目已实现的财务结果

| 情景 / 交付单位 | 收入 | 可变成本（含获客） | 单位贡献 | 月交付量 | 月固定成本 | 月经营贡献 |
|---|---:|---:|---:|---:|---:|---:|
| 低适配假设 / 一份单仓库工作流接入包 (USD) | 待核实 | 220.00 | 待核实 | 4 | 40.00 | 待核实 |
| 高适配假设 / 一份单仓库工作流接入包 (USD) | 待核实 | 530.00 | 待核实 | 4 | 80.00 | 待核实 |

低适配假设假设：研究者预算：4h×40=160人工，模型10、环境10、获客40，共220/包；4包+固定40=920/月；非作者账单，售价未知。；API成本 10，人工成本 160，其他可变成本 10，分摊获客成本 40。依据：Srepo, Sauthor

高适配假设假设：研究者预算：10h×40=400人工，模型30、环境20、获客80，共530/包；4包+固定80=2200/月；同范围接入，售后超范围另估，非报价。；API成本 30，人工成本 400，其他可变成本 20，分摊获客成本 80。依据：Srepo, Sauthor

## 反证与未核实信息

提醒钩子不直接执行测试，部分迁移告警允许继续，多宿主钩子不等价；独立使用和客户收入未取得，轻量原生CI可能更合适。

静态读取固定提交，不执行第三方代码、不安装依赖或MCP、不连接真实项目/数据库；历史测试数量未独立复测，无当前提交CI成功证据，无价格、收入和长期净省时。

## 具体动作与止损条件

先在获准演示项目对比现有流程、轻量任务加CI、完整生成器，记录负向检查和人工总耗时。

停止投入条件：需关闭既有保护才能跑通、钩子激活与失败边界不明或复核成本持续更高时停止扩展。

## 来源与对应关系

- [Sdirectory] [许可目录：测试驱动工作流生成器](https://agentusecases.ai/use-case/build-a-dev-workflow-generator-with-test-driven-agent-coding)：完整目录正文和原始Copy prompt；目录展示Apr1,2026，不能将收录日写成原帖发表日。
- [Sauthor] [AdEast5873：用Claude Code开发Agentic Workflow](https://www.reddit.com/r/claude/comments/1s383nj/i_built_agentic_workflow_entirely_with_claude)：原作者自述550多项测试、约200任务、1.5万多行代码，四agent审查及测试驱动；没有收益、对照或第三方验收。
- [Srepo] [固定提交README：当前多宿主工作流](https://github.com/varienos/agentic-workflow/blob/8112ecc9b0a8fc9f878aec25b7a2e5cd362334cd/README.md)：当前支持多宿主但Claude钩子不自动在其他宿主执行；Backlog与basic-memory依赖、Python3.12+/uv，graphify可选。Agentbase与Codebase分离，不是OS隔离。
- [Slicense] [MIT许可](https://github.com/varienos/agentic-workflow/blob/8112ecc9b0a8fc9f878aec25b7a2e5cd362334cd/LICENSE)：许可允许使用修改分发及销售软件副本，须保留版权和许可说明；按现状提供，没有效果保证。
- [Scode] [静态代码：测试提醒钩子](https://github.com/varienos/agentic-workflow/blob/8112ecc9b0a8fc9f878aec25b7a2e5cd362334cd/Agentbase/templates/core/hooks/test-enforcer.skeleton.js)：PostToolUse Edit/Write触发，按文件映射发systemMessage并exit0；同文件五分钟去重，不执行测试或证明测试先失败。
- [Sgitcode] [静态代码：生成器测试与迁移检查](https://github.com/varienos/agentic-workflow/blob/8112ecc9b0a8fc9f878aec25b7a2e5cd362334cd/Agentbase/generate.js)：测试运行生成在GIT_PRECOMMIT_TEST；GIT_PREPUSH_DESTRUCTIVE增加WARNINGS而非ERRORS。结合pre-push模板读到WARN继续、合并检查部分错误静默跳过；不是全部危险动作硬阻断。
- [Sguard] [静态代码：目录保护边界](https://github.com/varienos/agentic-workflow/blob/8112ecc9b0a8fc9f878aec25b7a2e5cd362334cd/Agentbase/templates/core/hooks/codebase-guard.js)：Edit/Write路径检查保护Codebase下指定配置，捕获异常后静默；不是对所有工具和操作系统路径的完整沙箱。
- [Sgit] [Git官方：钩子加载与执行](https://git-scm.com/docs/githooks)：无可执行位的钩子被忽略，默认hooks目录可由core.hooksPath改变；写出脚本不等于已正确激活。
- [Shooks] [Claude Code官方：钩子结果与失败](https://code.claude.com/docs/en/hooks)：阻断语义取决于事件和输出；很多错误/超时默认不阻断，onFailure等配置改变特定行为。不能由脚本名称推断强制策略。
- [Scompetitor] [Backlog.md：底层任务工具与轻量替代](https://github.com/MrLesk/Backlog.md)：公开工具将任务保存为Markdown，强调规格/计划/代码三个人工检查点。可只用任务与验收结构，不必采用整个工作流生成器；不是本产品用户反馈。
- [Smarket] [2025 Stack Overflow开发者调查](https://survey.stackoverflow.co/2025/ai/)：2025历史自选受访样本：准确性问题46%不信任、33%信任，回答该题33244人；反映复核需求而非2026市场规模或本项目购买率。
- [Sfeedback] [公开问题与PR调查](https://api.github.com/repos/varienos/agentic-workflow/issues?state=all&per_page=30)：本次返回5项均为PR：3依赖机器人、1Copilot修复、1贡献者多CLI适配。贡献和自报测试不是独立付费客户验收；不能据列表推定无问题。
- [Sci] [公开测试工作流与当前提交检查](https://github.com/varienos/agentic-workflow/blob/8112ecc9b0a8fc9f878aec25b7a2e5cd362334cd/.github/workflows/test.yml)：YAML配置Node18/npm install/npm test；固定SHA的Actions runs查询返回空数组，未取得该SHA成功运行证据，没有运行本产品。

结构化记录：[research/build-a-dev-workflow-generator-with-test-driven-agent-coding.json](../research/build-a-dev-workflow-generator-with-test-driven-agent-coding.json)
