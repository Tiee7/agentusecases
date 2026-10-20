# 用Claude规划PRD并分派实现任务

## 中文

    用PRD规划，并把任务交给成本更低的agent
    一位开发者使用高层agent编写PRD，将它拆成任务列表，再在生产工作流中把工作交给成本更低的agent。
    使用的是
    Claude Code
    Claude
    他们做了什么
    评论者描述了一套内部配置，包含两个系统：一个基于任务的工作流，强制执行TDD，并可配合Git工作树运行多agent流程；另一个是带hooks和内部风格规则的持久记忆系统。日常流程是先与Opus等高层agent一起写PRD，将其拆成任务清单，再把实现工作交给成本更低的agent。他们还说，自己正在搭建Python编排器，通过API调用Haiku或其他agent。
    进展与成效
    来源没有提供硬性性能指标或商业结果。它把这套方法描述为持续演进的内部工作流，而不是已完成的系统；使用者还在搭建周边执行框架。
    值得注意
    实际难点是，这依赖评论者自己创建的基础设施，包括任务执行约束、持久记忆和仍在开发中的编排器。
    亲自尝试
    使用
    Claude Code
    复制提示词
    我想在[仓库路径]构建[功能或项目]。先写一份简短PRD，涵盖目标、范围和验收标准，然后将它拆成TASKS.md文件中小而独立的任务，为每项写清完成标准。在实现任何内容之前停下来，向我展示PRD和任务清单供我审阅，以便我把任务交给成本更低的模型。
    原始来源：https://www.reddit.com/r/ClaudeCode/comments/1stmgpn/serious_question_whats_your_actual_ai_workflow

<details><summary>English original</summary>

    Plan with PRDs and delegate tasks to cheaper agents
    A developer uses a high-level agent to write a PRD, splits it into a task list, and hands the work to cheaper agents in a production workflow.
    Done with
    CC
    Claude Code
    CL
    Claude
    What they did
    The commenter described an internal setup with two systems: a task-based workflow that enforces TDD and can run multi-agent flows with git trees, plus persistent memory with hooks and house-style rules. Their day-to-day process is to work with a high-level agent like Opus to create a PRD, break it into a task list, and then hand implementation work to cheaper agents; they also said they are building their own Python orchestrator to call Haiku or other agents by API.
    How it went
    The source gives no hard performance numbers or business results. It frames the approach as an actively evolving internal workflow rather than a finished system, with the user still building the harness around it.
    Worth knowing
    The practical catch is that this depends on custom infrastructure the commenter created, including task enforcement, persistent memory, and an in-progress orchestrator.
    Try it yourself
    with
    Claude Code
    Copy prompt
    I want to build [feature or project] in [repo path]. First write a short PRD covering goals, scope, and acceptance criteria, then split it into small, independent tasks in a TASKS.md file with clear done criteria for each. Stop and show me the PRD and task list so I can review it before anything is implemented, so I can hand the tasks to a cheaper model.
    Original source: https://www.reddit.com/r/ClaudeCode/comments/1stmgpn/serious_question_whats_your_actual_ai_workflow

</details>

## 原作者的方法与来源

来源：[spoupervisor describes a custom internal task and memory workflow](https://www.reddit.com/r/ClaudeCode/comments/1stmgpn/serious_question_whats_your_actual_ai_workflow)

作者方法摘要

1. 与高层agent一起编写PRD，并拆成任务。
   English summary: Work with a high-level agent to produce a PRD and decompose it into tasks.

2. 在任务驱动的TDD系统中使用成本更低的agent实现。
   English summary: Use lower-cost agents for implementation within a task-driven TDD system.

3. 维护项目规则和记忆；Python API编排器仍在开发。
   English summary: Maintain project rules and memory; the Python API orchestrator was still being built.

## 简要分析

商业分数未评定。

### 有流程描述，没有节省账单

目标来源是spoupervisor的评论，不是主帖作者，也不是旁边贴出多个GitHub仓库的另一个人。评论没有提交记录、已验收功能、测试日志或费用对照。内部任务和记忆系统被描述为已创建，Python编排器明确仍在构建；不能把整套未完成框架写成已成熟投产的产品。

依据：[Sauthor](https://www.reddit.com/r/ClaudeCode/comments/1stmgpn/serious_question_whats_your_actual_ai_workflow)

### PRD是任务契约，不是长文越多越好

以下是研究者复制设计：先写目标、非目标、输入输出、约束和验收例，再拆成可单独检查的小任务。每项至少有依赖、允许修改范围和完成证据。涉及共享接口或数据库迁移的任务不应为了并行而假装独立，先统一接口再实现，避免多个低价agent各自补出不同需求。

依据：[Sauthor](https://www.reddit.com/r/ClaudeCode/comments/1stmgpn/serious_question_whats_your_actual_ai_workflow)

### 便宜模型需要相同验收条件

当前文档允许对子agent选择模型与工具，实际模型仍应核对。把容易任务交给较低成本模型是候选策略，不是所有小模型都等价。先用同类任务对比首次通过率、重试次数和审核时间；超过预定返工预算再升级处理，不能为降低单次价格放松测试或隐瞒模型变化。原评论未提供这种对照。

依据：[Sagents](https://code.claude.com/docs/en/sub-agents)

### 工作树解决文件竞争但不替代安全隔离

Git工作树可让不同分支各自检出，部分引用和配置仍共享。端口、数据库、外部账号和机器资源不会因为有工作树就独立。因此需要分开的输出/测试资源和单一合并负责人；串行合并后重新测试组合结果，不以各分支单测成功推断最终无冲突。此处是工程设计分析，不是原作者已验证的能力。

依据：[Sgit](https://git-scm.com/docs/git-worktree)

### TDD约束还需要独立验收

先写失败测试有助于明确目标，但agent也可能写出只验证自己实现的测试。建议保留需求负责人审核的验收例、边界输入与回归基线，禁止用删除或放宽测试来让任务通过。完成应关联代码、测试结果和审查意见，任务卡打勾本身不算交付。原案没有公开测试覆盖与缺陷结果。

依据：[Sauthor](https://www.reddit.com/r/ClaudeCode/comments/1stmgpn/serious_question_whats_your_actual_ai_workflow)

### 长期记忆必须可纠正

项目记忆可减少重复说明，也可能让过期假设持续传播。建议区分用户要求、代码事实、决策和暂时猜测，记录来源与更新时间；新版要求覆盖旧规则而不是累加矛盾。密钥、私人通信和多项目无关内容不应混入共享记忆。hooks执行什么、有什么权限与失败方式都需审核，不把持久化等同可靠性。

依据：[Sauthor](https://www.reddit.com/r/ClaudeCode/comments/1stmgpn/serious_question_whats_your_actual_ai_workflow)

### 客户付费的是稳定开发交付

假设面向已有代码仓库、测试和审核者的小团队，预算属于研发负责人。可提供固定范围的工作流配置、验收示例和维护，而非只售PRD模板或保证降本比例。获客可从现有开发服务的小样本演示开始，本轮不联系任何人。原案无真实客户、销售或复购信息，商业化仍待验证。

依据：[Sauthor](https://www.reddit.com/r/ClaudeCode/comments/1stmgpn/serious_question_whats_your_actual_ai_workflow)

### 应比较每个验收功能的总成本

研究者假设一包同范围功能：单模型基线模型12USD+人工2h×40=80，共92。顺利分层时规划2+实现1+审查2=模型5，加同样人工80，共85，每月10包850；高返工时模型2+6+5=13、人工3h×40=120，共133，每月1330。都是情景预算不是现价或作者账单。顺利情景只省7美元，多10.5分钟人工就抵消；维护、CI、获客未知另计，售价未知不计利润。

依据：[Scost](https://code.claude.com/docs/en/costs)

### 配额与API成本不能直接混算

订阅额度、API账单和命令显示的美元估算不是一个数。子agent请求仍消耗用量，不能用多开agent当作额外免费额度。记录实际模式、模型版本、规划/执行/审查及失败请求，才能复算一项已验收交付的消耗。本轮没有付费API调用、切换模型或更改用户的执行策略。

依据：[Scost](https://code.claude.com/docs/en/costs), [Sagents](https://code.claude.com/docs/en/sub-agents)

### 自用需要能看懂和验收代码

适合任务较多且已有工程经验、能判断实现是否满足目标的开发者。潜在收益是把重复实现交出去，但净省时未知，维护自己的编排框架也会消耗时间。准备测试仓库、明确任务边界和不覆盖原件的备份；频率随开发任务而定，维护来自依赖、模型行为、规则及上下文变化。

依据：[Sauthor](https://www.reddit.com/r/ClaudeCode/comments/1stmgpn/serious_question_whats_your_actual_ai_workflow)

### 先让同范围任务形成证据

用自有演示仓库挑两个可回归的小功能，固定验收与版本，只比较规划、实现和审核总时间/成本及遗漏缺陷。原站模板要求规划后先停给用户审阅，不能跳过直接实现。若分层产生更多返工或模糊责任，就退回较简单流程。本轮仅研究公开来源，没有跑作者框架或修改其他项目。

依据：[Sauthor](https://www.reddit.com/r/ClaudeCode/comments/1stmgpn/serious_question_whats_your_actual_ai_workflow)

## 自用价值：待核实

没有净省时、费用或缺陷测量。

依据：Sauthor, Sagents

- 适用人群：能审核代码和测试、具有重复开发任务的开发者。
- 用途：需求规划、任务拆解、受控实现与验收。
- 预期收益：可能降低实现消耗，返工可能抵消。
- 设置成本：演示仓库、验收、工作树/权限与规则。
- 维护成本：框架、模型、依赖、旧记忆和集成冲突。
- 使用频率：随软件开发任务，原案无固定频率。
- 隐私风险：代码、密钥和项目记忆跨agent外发。
- 错误风险：错误拆分、测试自证、语义冲突和任务卡误报完成。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/plan-with-prds-and-delegate-tasks-to-cheaper-agents

建议工具：Claude Code

    I want to build [feature or project] in [repo path]. First write a short PRD covering goals, scope, and acceptance criteria, then split it into small, independent tasks in a TASKS.md file with clear done criteria for each. Stop and show me the PRD and task list so I can review it before anything is implemented, so I can hand the tasks to a cheaper model.

自编试用模板

准备条件：自有演示仓库、固定验收例与修改边界。

工具：Claude/Claude Code；原作者Python编排器仍开发，本轮未运行。

预期结果：可审阅PRD和任务清单，不冒充代码已完成。

### 源站Copy prompt

原文模板

出处：https://agentusecases.ai/use-case/plan-with-prds-and-delegate-tasks-to-cheaper-agents

依据：Sdirectory

    I want to build [feature or project] in [repo path]. First write a short PRD covering goals, scope, and acceptance criteria, then split it into small, independent tasks in a TASKS.md file with clear done criteria for each. Stop and show me the PRD and task list so I can review it before anything is implemented, so I can hand the tasks to a cheaper model.

### 分层交付成本核验计划

自编模板

出处：研究团队自编

依据：Scost, Sgit

    先为自有演示功能写目标、非目标、验收例和任务依赖，不实现。比较单模型与分层方案时记录规划/实现/审查/返工及人工总成本。不得放宽测试或改权限；用户审阅后才另行授权实现。

## 来源

- [许可目录：PRD与分层agent工作流](https://agentusecases.ai/use-case/plan-with-prds-and-delegate-tasks-to-cheaper-agents)：完整目录和模板，历史日期2026-04-01；没有量化结果。
- [spoupervisor：内部TDD及记忆系统](https://www.reddit.com/r/ClaudeCode/comments/1stmgpn/serious_question_whats_your_actual_ai_workflow)：目标评论者spoupervisor描述任务/TDD、多agent/Git树、记忆hooks/HouseStyle；高层Opus或Sonnet规划，Haiku实现；PythonAPI编排仍在构建，无测量。其他评论者的GitHub工具和额度规避不是此人的实现，未使用。
- [Claude Code自定义子agent文档](https://code.claude.com/docs/en/sub-agents)：子agent可选择模型和工具/权限，在独立上下文请求并消耗相同用量限制；有worktree配置但具体版本和实际执行模型需要核对，不把文档默认当历史作者配置。
- [Git工作树官方说明](https://git-scm.com/docs/git-worktree)：工作树可并行检出不同分支，有独立HEAD但共享部分refs和默认配置；不是资源或权限安全隔离。仅阅读，未创建测试仓库。
- [Claude Code成本与用量说明](https://code.claude.com/docs/en/costs)：API消耗、订阅配额与usage美元估算不同；真实账单以Console为准，多agent各自上下文增加请求与tokens。未采用文档平均费用作为本案例价格。
