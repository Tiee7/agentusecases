# 用Claude Code指导SQL项目迁移并练习dbt

## 中文

    在自己的学习环境中，把Claude Code当作可操作工具的导师
    作者通过CLAUDE.md说明文件给Claude Code设定导师角色，让它解释概念，并与他的学习环境交互。
    使用的是
    CC
    Claude Code
    他们做了什么
    作者把以前的SQL流水线博客和gist代码交给Claude，再让它编写CLAUDE.md，要求教自己dbt，而不是直接迁移代码。Claude解释概念、提供让他填空的代码骨架，并执行安装和诊断。当它开始自己搭建东西时，他就介入制止。
    进展与成效
    他通过迁移自己的流水线学习了dbt，并认为体验很好。Claude仍不断抢先搭建东西，建议SELECT *等捷径，还会编造列的取值，直到受到质疑。他让它编写了Dagster的Python代码。
    值得了解
    你需要不断纠正Claude想直接完成工作的倾向。作者也提醒它可能误导人，因此应检查它的说法，尤其涉及较新或小众技术时。
    亲自尝试
    使用
    Claude Code
    复制提示词
    在这个项目文件夹中，担任我的[学科，例如Rust或线性代数]导师。先写一份CLAUDE.md，说明：按[我的水平]解释概念，在给出答案前先问我问题，并把此文件夹中的文件、笔记本和练习用作教材。然后读取文件夹，先讲一小节[第一个主题]，再给我一道练习。未经先询问我，不要更改或删除我的文件。
    原始来源：https://rmoff.net/2026/02/20/claude-the-instructor/

<details><summary>English original</summary>

    Use Claude Code as an agentic tutor in your learning environment
    The author gave Claude Code a tutor role with a CLAUDE.md brief so it could explain concepts and interact with his learning environment.
    Done with
    CC
    Claude Code
    What they did
    The author gave Claude his old SQL pipeline blog post and gists, then had it write a CLAUDE.md telling it to teach him dbt instead of just migrating the code. Claude explained concepts, gave skeletons for him to fill in, and ran installs and diagnostics. He stepped in whenever it started building things itself.
    How it went
    He learned dbt by migrating his pipeline and called it great. Claude kept jumping ahead to build things, suggested shortcuts like SELECT *, and invented column values until challenged. He let it write the Dagster Python.
    Worth knowing
    Expect to keep correcting Claude's urge to just do the work. The author also notes it can mislead, so check its claims, especially on newer or niche technology.
    Try it yourself
    with
    Claude Code
    Copy prompt
    Act as my tutor for [subject, e.g. Rust or linear algebra] inside this project folder. First write a CLAUDE.md that says: explain concepts at [my level], ask me questions before giving answers, and use the files, notebooks and exercises in this folder as teaching material. Then read the folder and start with a short lesson on [first topic] followed by one exercise for me. Don't change or delete my files without asking me first.
    Original source: https://rmoff.net/2026/02/20/claude-the-instructor/


</details>

## 原作者的方法与来源

来源：[Claude the Instructor](https://rmoff.net/2026/02/20/claude-the-instructor/)

作者方法摘要

1. 作者以已有SQL项目为教材，在解释和本人实现之间交替，并把部分环境工作交给助手。
   English summary: The author used an existing SQL project as learning material, alternated explanations with his own implementation, and delegated selected environment work.

## 我们的分析

**商业结论：仅建议受控试点。先检验学员独立完成能力与辅导工时，再评估收费**

作者把真实项目用于学习，并公开了最终导师说明和测试配置，具备可研究的具体方法。但助手抢先代做、给出不可靠解释的反例也明确存在；官方Learning风格和dbt课程已有替代。潜在付款人是已有基础的成年学习者或培训负责人，是否愿为个性化核验付费、人工准备和维护是否可控都尚未得到验证，适合小范围受控试点。

案例ID：`use-claude-code-as-an-agentic-tutor-in-your-learning-environ` · 案例来源：https://agentusecases.ai/use-case/use-claude-code-as-an-agentic-tutor-in-your-learning-environ
研究时间：2026-10-20T02:45:22.422735+00:00

**商业评分：37.0/100。用户反馈信号占5%。**

| 维度 | 权重 | 分数 /5 | 商业依据 |
|---|---:|---:|---|
| 付费需求 | 20% | 2 | 有具体项目学习需求与相邻自述，但没有本方案付费学员、采购预算或复购证据。 [Sauthor, Scommunity] |
| 业务价值与效果证据 | 20% | 2 | 原作者过程与代码可查，未有独立学习前后对照，项目完成不等同掌握知识。 [Sauthor, Stests] |
| 单位经济与利润 | 20% | 2 | 两种原创辅导假设对人工时间敏感，缺成交账单和实际服务工时，不能判断稳定盈利。 [Scost, Sreadme] |
| 获客与市场进入 | 15% | 2 | 作者博客社区有可见传播入口，但访问到付费转化没有数据，获客计划仍是假设。 [Sauthor, Scommunity] |
| 竞争壁垒 | 10% | 1 | 角色文件容易模仿且平台有替代，原创题与验收积累可能有价值但尚未形成证明。 [Sstyle, Scourse] |
| 交付与经营风险 | 10% | 2 | 可读项目与测试支持工程可检查，教学模式漂移、权限与环境兼容仍需人工验收。 [Sbrief, Spermissions] |
| 独立用户反馈信号 | 5% | 1 | 两条相邻学习亲历有正反面取舍，无该项目独立复现或量化教学效果，只计弱信号。 [Scommunity, Sissues] |

## 自用价值：中

可适配已有项目并即时解释，但需主动限制代做、核验概念，学习增益待测。

依据：Sdirectory, Sbrief, Spermissions

- 适用人群：已有SQL基础、愿意亲手练习的成年技术学习者。
- 用途：概念讲解、填空骨架、代码反馈和限定环境诊断。
- 预期收益：作者评价积极且公开过程，没有可量化学习增益或省时保证。
- 设置成本：隔离目录、合成数据、学习目标、账号额度与操作边界。
- 维护成本：检查模型解释、依赖版本、进度文件和练习答案。
- 使用频率：按学习会话使用，长期留存未知。
- 隐私风险：项目文件和数据库可能含业务数据或凭据，应限定获准材料。
- 错误风险：抢先代写、虚构概念或字段、运行环境改动、把测试通过当掌握。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/use-claude-code-as-an-agentic-tutor-in-your-learning-environ

建议工具：Claude Code

    Act as my tutor for [subject, e.g. Rust or linear algebra] inside this project folder. First write a CLAUDE.md that says: explain concepts at [my level], ask me questions before giving answers, and use the files, notebooks and exercises in this folder as teaching material. Then read the folder and start with a short lesson on [first topic] followed by one exercise for me. Don't change or delete my files without asking me first.

自编试用模板

准备条件：原创SQL小练习、合成输入、人工答案与明确允许动作。

工具：先只读材料设计，若运行需已有获准Claude Code环境；本轮未安装或调用。

预期结果：一节有限提示和独立变式验收设计；本轮不是教学试用。

### 源站Copy prompt

原文模板

出处：https://agentusecases.ai/use-case/use-claude-code-as-an-agentic-tutor-in-your-learning-environ

依据：Sdirectory

    Act as my tutor for [subject, e.g. Rust or linear algebra] inside this project folder. First write a CLAUDE.md that says: explain concepts at [my level], ask me questions before giving answers, and use the files, notebooks and exercises in this folder as teaching material. Then read the folder and start with a short lesson on [first topic] followed by one exercise for me. Don't change or delete my files without asking me first.

### 项目学习验收设计

自编模板

出处：研究团队自编

依据：Stests, Sstyle

    基于这份原创SQL和合成数据，设计一节概念说明、一个留空骨架和一个无助手独立变式。先问我的理解，给提示后等我作答，不代写答案。不执行命令、不改文件或数据库；列出人工答案、概念检查点、错误分类和需要额外授权的环境动作。

## 已核验事实

- 原文2026-02-20发布，展示以旧SQL项目学习dbt并保留负面案例。 [Sauthor]
- 固定仓库CLAUDE.md含教学边界与进度，是项目结束后的演化版本。 [Sbrief, Sauthor]
- 事实表配置有两来源合并的合成输入与预期输出单元测试。 [Stests]
- 维表配置声明契约、非空和唯一性等检查，未由本研究执行。 [Scontract]
- Dagster实现区分必要与可选加载失败，并配置顺序执行及15分钟计划。 [Sdagster]
- 官方Learning风格仍处理常规实现，给人保留部分设计决策代码。 [Sstyle]
- 官方Pro美国月付20美元含Claude Code，但API和使用额度另有边界。 [Scost]
- 官方dbt课程目录覆盖模型、来源、测试、文档和部署，需注册进入。 [Scourse]
- 公开仓库license字段为null且树未见LICENSE，不认定商业复制许可。 [Srepo]
- Lobsters有两条相邻学习亲历，不能当本dbt项目独立复现。 [Scommunity]

## 先面向已有项目的成年技术学习者

本案的具体任务是借自己已有SQL项目学会dbt，而不是最快拿到迁移后的成品。研究者判断，最匹配的初始人群是会读SQL、能够核查代码、愿意亲手完成练习的成年人。使用者和个人付款人可以是同一人；若由团队采购，则付款理由需要落到新人能独立解释数据模型和排查错误，而不能只用课程完成率。没有任何材料证明作者经营培训服务、招收学员或取得收入。为此不从一篇好评推导大规模教育市场，也不默认适用于儿童、零基础者或高风险生产数据库。拟议需求访谈应先问最近一次学新工具在哪一步卡住：概念、环境、调试还是缺少反馈，再决定是否需要能执行命令的助手。只想了解概念的人，普通对话和官方课程可能更省事；已有复杂项目的人才可能愿意为上下文适配和人工检查付费。用户能够自己安装并不代表愿意为安装付费，真正需要验证的是少走弯路与独立完成任务的提升。

依据：Sdirectory, Sreadme, Scourse

## 教学环节与代做环节分别约定

作者展示了讲解、填空骨架与本人实现相结合的过程，也主动把部分编排代码交给助手。固定版本说明保存了教学边界和项目进度；测试文件中可见合成输入与预期结果，维表有契约，编排有顺序执行及定时配置。本轮仅静态读取，未安装、调用模型或运行流水线。研究者建议将一次教学交付拆为目标确认、只读理解、单步练习、学员作答、反馈、独立复做六步；环境诊断和代码代写应另列明确动作。每节开始时写清哪项必须本人实现、哪项允许助手代劳，避免把一句“继续”解释成完成全部迁移。完成记录应保存学员自己的解释、错误与修正，而非只记代码测试通过。技术测试能检查数据转换，不会自动检查学员理解；两套验收需要并行存在。使用合成数据和可回退目录能降低初次练习成本，但不能因只是学习项目就忽略写文件、安装依赖和启动后台任务的影响。

依据：Sauthor, Sbrief, Stests, Scontract, Sdagster

## 需求信号存在，教学增益还没有对照

公开讨论中有相邻编程学习者认可通过提问和提示学习，也有人更倾向不给助手工具，避免它直接代做。这支持“交互式解释有需求”的有限判断，不能证明此dbt项目的教学质量、付费规模或长期留存。官方基础课程已提供明确知识路径，说明通用入门供给充足。研究者建议把可进入市场限定为项目型学习中的个性化卡点，先比较普通文档、官方课程加答疑，以及具备环境操作能力的导师三种方式。评估重点应是撤掉助手后能否解释模型、修复相似错误、完成一个新变式，而非只问体验是否愉快。样本选择也应保留失败者和中途退出者，否则容易只看到愿意分享成功的人。若成年人已经能通过现成课程满足需求，新增工具和权限可能反而提高设置负担。当前没有足够数据量化市场规模或推定学习效率增长率，商业验证应从具体学习任务开始，而非从AI教育大盘倒推营收。

依据：Scommunity, Sauthor, Scourse

## Learning风格并不等于绝不代写

官方Learning风格会解释决策并留部分代码给人填写，但常规实现仍由Claude处理；输出风格本质是指令，不是强制执行的权限边界。它因此是直接替代，也与本案例要求“由我亲手做”存在范围差别。dbt官方课程目录涵盖模型、来源、测试、文档和部署，本地快速入门则提供另一条可自行操作的路线；本轮只读目录，未注册或参加课程，也没有把课程标注约五小时当学员实际完成时间。研究者建议先试现成路径加少量定向解释，仅在固定项目材料、错误反馈和环境排障确实改善结果时提供定制服务。比较必须使用同一学习目标与相近难度，不能拿复杂旧项目的迁移时间和最短入门示例直接比速度。定制方案也需保留退出路径：学员应能带走原创练习、自己的笔记和代码，在没有专属助手时继续学习，否则锁定成本可能成为反对采购的理由。

依据：Sstyle, Scourse, Squickstart

## 按限定辅导服务测算，不把订阅当免费

官方Pro美国月付标价为20美元并含Claude Code，API另行计费，实际额度受任务和账户影响；作者的订阅、耗时和账单未知。以下完全是研究者对原创辅导服务的敏感性假设，不是作者报价或已经获得的收入。交付单位定义为一次限定两节的项目学习辅导与验收包，假设价格149美元，用户自有账号自付订阅，服务商不代付API。基准人工两小时乘30美元为60，其他变动成本5，获客摊销20，单位贡献64；月8单、固定费用200，结果312美元。压力情景改为人工四小时120、其他8、获客35，贡献为负14；月4单仍有固定200，结果负256美元。未包含税、退款或超范围维护，不能把上述贡献称净利润。人工成本包含准备、审查和售后，因此环境问题、反复纠正代写和个别资料清理会迅速改变结果。若用户需新订阅，则其20美元等支出另计，不应从服务商零API成本误读为总学习成本为零。

依据：Scost, Sreadme

## 用可复做样例获客，避免承诺学会一切

作者文章、公开项目和社区讨论构成可以观察的传播入口，但没有公开访问到付费的转化数据。研究者提出的获客假设是面向已有SQL基础的技术社群，用一份自有版权、合成数据的小迁移练习展示教学方式，再邀请自愿成人比较两种学习路径。对外展示应包含助手曾经抢答、需要人核验以及没有理解的部分，不能只放最后成功的终端输出。交付前约定主题、会话数、时间上限、允许操作范围和最终独立题，避免用户把辅导服务理解为无限软件维护。对企业则应先使用脱敏示例，采购需要说明公司源码和数据库信息是否离开设备、谁能访问、何时删除；这些准备都应进入报价。用户自行登录自己的订阅，服务商不收集密码或共用账户。若渠道只能依赖持续付费投放而每单支持时间增加，前述低客单价情景很容易亏损，不能把一篇受欢迎文章当稳定获客能力。

依据：Sauthor, Scommunity, Sreadme

## 可积累验收题与错误库，角色提示本身很薄

一份导师角色文件很容易模仿，平台已有Learning输出风格也降低了通用包装的差异。研究者认为更值得积累的是原创任务序列、错误分类、独立复做题、环境兼容清单和人工审核方法；这些资产需要持续维护，不能靠把开源链接换成自己的品牌建立壁垒。此仓库本次元数据license为null且文件树未见许可证，公开可读不等于获得完整商业再分发许可。可以分析其方法并独立创作自己的练习，但若要复制代码、说明文件或文章进入收费教材，应先确认相应权利；本报告没有将外链长文或完整CLAUDE.md复制到公开站。测试配置说明项目有工程性检查，却不直接构成教育护城河。真正可比较的积累应包括常见误解怎样被识别、提示顺序怎样减少直接答案泄露、错误后的恢复怎样不覆盖学员原作。没有持续测量之前，不能宣称某套提示带来更高成绩或更低流失。

依据：Sbrief, Sstyle, Srepo, Stests

## 把权限、版本和学习模式一起验收

当前权限文档将只读、文件修改和命令执行分开；教学风格不能替代这些设置。研究者建议初期在隔离练习目录中使用最小权限，先读后讨论，只允许与当前学习目标有关的写入和依赖操作。不要把导师配置直接用于生产库或含凭据目录，也不要为了省确认而关闭保护。仓库README有安装命令但没有完整锁定环境，本轮没有运行，因此不承诺在任意系统安装成功。编排文件存在启动后可运行的调度定义，复制前需明确是否真的要后台刷新，测试结束需检查进程与资源，不应意外留下长期任务。每次换模型、版本或学习风格后重新做一个小验收：能否等待学员作答、拒绝未授权改动、正确识别资料缺失、保留原文件。错误提示和数据契约应有来源，不能为了让练习显得完整而编造字段取值。涉及公司资料时还要核对组织政策；本研究未改任何第三方账户或软件权限。

依据：Spermissions, Sstyle, Sreadme, Sdagster

## 相邻亲历支持交互答疑，也提供工具负担反证

相关体验：jorsk自述用无代写的问答完成C/SDL学习；非本项目。

相关体验：kraxen72自述长期借提示学编程数学，并认为工具权限可能妨碍学习。

依据：Scommunity, Sissues, Sdirectory

## 只做受控试点，先证明独立完成能力

结论是仅建议受控试点。原作者过程、最终配置与项目代码能支持方法确实存在，也有可追溯反例；它们尚未证明独立教学效果、付费需求或可盈利交付。研究者建议先设计一项原创、合成数据的短SQL迁移任务，明确两三个概念，先用普通文档完成基线，再提供有限提示，最后在不使用助手的情况下做新变式并解释理由。记录的是正确性、解释质量、人工准备与核对时间，以及助手代做次数，不把测试绿灯等同学员学会。本轮只完成来源和静态实现研究，没有招募、运行模型、安装课程环境或真实教学实验。继续条件可以预先设为：独立题改善且支持工时在报价范围内，关键操作全部获准，资料可追溯；停止条件是仍靠助手完成、常见概念被误导、持续越权代写或服务时间超过可承受范围。比较时还需先测原有基础，交替使用难度相近而非同一道题，避免把重复练习的熟悉程度当助手带来的增益。试点即使有效，也应限定到相似基础和主题，再决定是否扩展到团队培训或其他学科。

依据：Sdirectory, Stests, Sstyle, Scourse

## 单位经济测算：情景假设，不是项目已实现的财务结果

| 情景 / 交付单位 | 收入 | 可变成本（含获客） | 单位贡献 | 月交付量 | 月固定成本 | 月经营贡献 |
|---|---:|---:|---:|---:|---:|---:|
| 基准假设：限定两节辅导包 / 一次原创项目辅导与独立题验收包 (USD) | 149.00 | 85.00 | 64.00 | 8 | 200.00 | 312.00 |
| 压力假设：个别环境与复核耗时翻倍 / 一次原创项目辅导与独立题验收包 (USD) | 149.00 | 163.00 | -14.00 | 4 | 200.00 | -256.00 |

基准假设：限定两节辅导包假设：全部为假设，非实绩。人工2小时×30；8×(149-0-60-5-20)-200=312。用户自有账号另付订阅；零服务商API不代表模型免费；未计税退款。；API成本 0，人工成本 60，其他可变成本 5，分摊获客成本 20。依据：Scost, Sreadme

压力假设：个别环境与复核耗时翻倍假设：全部为假设。人工4小时×30；4×(149-0-120-8-35)-200=-256。订阅由用户另付；未计税退款和超范围维护。；API成本 0，人工成本 120，其他可变成本 8，分摊获客成本 35。依据：Scost, Scourse

## 反证与未核实信息

原作者反复制止代写、纠正编造；相邻用户偏好无工具对话；平台Learning与官方课程替代；缺独立学习和收入证据；仓库复制许可未确认。

仅静态代码与公开来源研究，没有安装运行、调用模型、招募学员或真实试用；无学习前后对照、真实账单或营收。仓库未见许可证，不公开复制完整代码和外链长文。

## 具体动作与止损条件

设计原创合成数据迁移题，对比有无有限提示后的独立变式表现与服务工时。

停止投入条件：仍依赖助手完成、关键概念误导、未经批准代写或人工工时使服务亏损。

## 来源与对应关系

- [Sdirectory] [许可目录案例](https://agentusecases.ai/use-case/use-claude-code-as-an-agentic-tutor-in-your-learning-environ)：保留原始用法、正负结果和完整试用模板，不改写为成功宣传。
- [Sauthor] [Robin Moffatt教学实践文章](https://rmoff.net/2026/02/20/claude-the-instructor/)：2026-02-20文章展示学习过程与反例；2026-03-02补入反馈，效果为作者自述。
- [Sbrief] [项目固定版本导师说明](https://github.com/rmoff/env-agency-dbt/blob/2e63f3348438fcabf1ace74e9f9df1bb46c94b53/CLAUDE.md)：最终说明含教学边界、进度与数据约束；不是开篇初始版本或硬权限策略。
- [Sreadme] [项目README与运行步骤](https://github.com/rmoff/env-agency-dbt/blob/2e63f3348438fcabf1ace74e9f9df1bb46c94b53/README.md)：Python、DuckDB、dbt和Dagster依赖；安装说明无版本锁定承诺。
- [Stests] [事实表单元测试配置](https://github.com/rmoff/env-agency-dbt/blob/2e63f3348438fcabf1ace74e9f9df1bb46c94b53/models/marts/fct_readings.yml)：有两个来源合并的合成输入期望结果；只读验证测试存在，未执行。
- [Scontract] [维表契约与列说明](https://github.com/rmoff/env-agency-dbt/blob/2e63f3348438fcabf1ace74e9f9df1bb46c94b53/models/marts/dim_stations.yml)：声明契约、唯一非空测试与真实业务键说明；不是本轮数据质量实测。
- [Sdagster] [Dagster编排实现](https://github.com/rmoff/env-agency-dbt/blob/2e63f3348438fcabf1ace74e9f9df1bb46c94b53/orchestration/definitions.py)：所需与可选加载错误处理不同、顺序执行和15分钟调度配置，未启动。
- [Scommunity] [Lobsters公开讨论](https://lobste.rs/s/nmyrxg/how_i_got_claude_teach_me_dbt)：两位相邻学习用户表达不同工具取舍，另有评论质疑自述学习证据。
- [Sstyle] [Claude Code输出风格说明](https://code.claude.com/docs/en/output-styles)：Learning仍会自己做常规实现，风格不是强制约束；不同于完全不写代码。
- [Spermissions] [Claude Code权限说明](https://code.claude.com/docs/en/permissions)：读写和命令权限独立于教学风格，按实际模式设置。
- [Scourse] [dbt官方基础课程目录](https://learn.getdbt.com/courses/dbt-fundamentals)：当前课程含模型、来源、测试、文档、部署；需注册，未参加课程。
- [Scost] [Claude Pro官方价格与额度](https://support.claude.com/en/articles/8325606-what-is-the-pro-plan)：美国20美元月付含Claude Code；API单独，额度并非无限，作者实际账单未知。
- [Squickstart] [dbt官方本地快速入门](https://docs.getdbt.com/guides/manual-install)：已有本地编辑与命令行学习路径，凭据配置需与项目代码分开。
- [Srepo] [公开仓库元数据与文件清单](https://github.com/rmoff/env-agency-dbt)：本次API license为null，树未见LICENSE；不把公开可读当完整商用复制许可。
- [Sissues] [公开问题检索](https://github.com/rmoff/env-agency-dbt/issues)：state=all返回空，无该仓库独立复现反馈；不是零缺陷证明。

结构化记录：[research/use-claude-code-as-an-agentic-tutor-in-your-learning-environ.json](../research/use-claude-code-as-an-agentic-tutor-in-your-learning-environ.json)
