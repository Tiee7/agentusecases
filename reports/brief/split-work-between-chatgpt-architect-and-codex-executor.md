# 用ChatGPT规划审阅并由Codex执行本地任务

## 中文

    让ChatGPT架构师与Codex执行者分工
    发帖者搭建了一座桥梁，让ChatGPT负责规划和审阅，Codex负责本地执行工作。
    使用的是
    GP
    ChatGPT
    CX
    Codex
    他们做了什么
    发帖者看到ChatGPT通过澄清问题、与子agent协作近一小时来处理本地CAD任务后，使用MCP式本地文件访问，将ChatGPT与本地Codex环境连接起来。随后，他们构建了一个小型工作流层，把规划与审阅交给ChatGPT，文件操作、运行命令和检查结果等本地执行步骤交给Codex，并添加了基本安全边界。
    进展与成效
    当时的CAD测试显示ChatGPT的高层次能力强于Codex，不过CAD输出本身只是一般。这座桥梁仍是实验性的，尚无性能数字，作者也在询问他人会怎样设计这个工作流。
    值得了解
    它是为Windows版Codex构建的。作者说，直接在ChatGPT桌面应用等原生应用里使用电脑操作通常失败，所以改用Codex网页端的Chrome控制来避开这一问题。
    亲自尝试
    使用
    ChatGPT
    复制提示词
    我将ChatGPT用作[项目或仓库路径]的规划者和审阅者，你是执行者。阅读我在下面粘贴的计划，在本地仓库中逐步执行，每一步之后运行[测试或构建命令]。完成后，简要总结修改内容、涉及的文件和测试结果，供我粘贴回ChatGPT审阅。删除文件或推送任何内容之前，先暂停并询问我。计划：[粘贴ChatGPT给出的计划]
    原始来源：https://www.reddit.com/r/OpenAI/comments/1uow2ld/i_built_a_bridge_between_chatgpt_and_codex

<details><summary>English original</summary>

    Split work between ChatGPT architect and Codex executor
    The poster built a bridge where ChatGPT plans and reviews while Codex does the local execution work.
    Done with
    GP
    ChatGPT
    CX
    Codex
    What they did
    The poster used MCP-style local file access to connect ChatGPT with a local Codex setup, after seeing ChatGPT handle a local CAD task by asking clarifying questions and working with subagents for nearly an hour. They then built a small workflow layer that assigns ChatGPT the planning and review role, while Codex handles local execution steps like touching files, running commands, and checking results, with basic safety boundaries added by the poster.
    How it went
    The immediate CAD test showed stronger high-level capability from ChatGPT than Codex, though the CAD output itself was only so-so. The bridge itself is presented as experimental, with no performance numbers yet and the author asking others how they would design the workflow.
    Worth knowing
    It was built for the Windows version of Codex, and the author said using computer-use directly inside native apps like the ChatGPT desktop app usually failed, so they bypassed that with Codex web Chrome control.
    Try it yourself
    with
    ChatGPT
    Copy prompt
    I'm using ChatGPT as the planner and reviewer for [project or repo path], and you're the executor. Read the plan I paste below, carry it out step by step in the local repo, and run [tests or build command] after each step. When finished, give me a short summary of what changed, the files touched, and any test results that I can paste back to ChatGPT for review. Pause and ask me before deleting files or pushing anything. Plan: [paste plan from ChatGPT]
    Original source: https://www.reddit.com/r/OpenAI/comments/1uow2ld/i_built_a_bridge_between_chatgpt_and_codex

</details>

## 原作者的方法与来源

原帖与补充账户链接均在此前受限的Reddit，本轮未访问或使用偶然摘要，未取得原文和实现。

[原始链接](https://www.reddit.com/r/OpenAI/comments/1uow2ld/i_built_a_bridge_between_chatgpt_and_codex)

## 简要分析

商业分数未评定。

### 一次CAD体验不是通用模型排名

目录描述特定任务、环境和当时表现，未给模型版本、相同输入或重复次数；不能据此宣布ChatGPT永远擅长架构而Codex只能执行。近一小时协作也不是净节省数据。

依据：[Sdirectory](https://agentusecases.ai/use-case/split-work-between-chatgpt-architect-and-codex-executor)

### 交接应携带计划版本和验收证据

拟议交接包包括任务范围、允许修改的路径、当前提交、验收条件和停止条件。执行者返回实际差异、命令与结果，规划者检查这些证据，而不是只阅读另一模型的成功总结。计划改变后需明确替换旧版本，避免执行过期要求。

依据：[Sdirectory](https://agentusecases.ai/use-case/split-work-between-chatgpt-architect-and-codex-executor)

### 第二个角色不天然独立

两边如果都依赖同一错误前提，复述计划不会形成有效复核。审阅应针对文件和测试证据，加入已知反例与失败样本。重要操作仍由有权限的人确认，不用多agent一致意见代替用户授权。

依据：[Sdirectory](https://agentusecases.ai/use-case/split-work-between-chatgpt-architect-and-codex-executor)

### 区分MCP式桥接与已移除的旧服务端

目录没有足够实现细节判断作者使用何种桥接。官方移除Codex MCP server的更新不能外推到全部MCP能力；反过来，旧Cookbook命令仍可见也不证明在当前版本可直接运行。复制时先确认接口版本和支持状态，本轮没有安装或验证旧示例。

依据：[Supdate](https://developers.openai.com/blog/openai-for-developers-2025), [Scookbook](https://developers.openai.com/cookbook/examples/codex/codex_mcp_agents_sdk/building_consistent_workflows_codex_cli_agents_sdk)

### 不一定需要操控另一个应用界面

官方集成层提供不同生命周期控制，适合自有应用的方案应按任务范围选择，而非依赖脆弱的界面点击。最轻方案仍是用户手工传递计划与结果。目录提到的桌面操作失败只是作者经验，不是普遍产品限制，更不是绕过安全限制的授权。

依据：[Splatform](https://developers.openai.com/blog/codex-as-a-platform)

### 收费价值可能在交接治理，而非两个聊天窗口

候选收入是特定团队流程配置与维护，但本案没有付款、留存或销售证据。获客验证应展示可审阅的差异与故障恢复，询问真实交接损失；不能以双agent概念推定客户会订阅。

依据：[Sdirectory](https://agentusecases.ai/use-case/split-work-between-chatgpt-architect-and-codex-executor)

### 分工也会增加传递与维护成本

成本包括两端运行、重复上下文、人工审阅、版本兼容与失败恢复。若小任务用一个助手已经足够，引入桥接可能更慢。没有计时或报价，不给利润与固定预算门槛；先比较人工总时间、返工和成功率。

依据：[Sdirectory](https://agentusecases.ai/use-case/split-work-between-chatgpt-architect-and-codex-executor)

### 适合已有本地工具和复核能力者

自用者需能理解计划、测试和权限，频率随项目任务。设置包括仓库范围、回执格式、失败规则；维护包括版本变化与上下文同步。风险是文件泄露、误命令、旧计划执行和把摘要当真实测试；传递敏感文件前要明确两端数据去向。

依据：[Sdirectory](https://agentusecases.ai/use-case/split-work-between-chatgpt-architect-and-codex-executor)

### 先做只读计划和合成结果审阅

使用一个虚构任务及预制的正确/错误差异，要求识别超范围修改、失败测试与缺失证据，不实际访问仓库或运行命令。通过标准是能指出未知、拒绝以成功总结代替证据，且保留删除和推送前确认。本轮未运行桥接、CAD或桌面应用。

依据：[Sdirectory](https://agentusecases.ai/use-case/split-work-between-chatgpt-architect-and-codex-executor)

## 试用准备与预期结果

虚构计划与预制差异、测试日志，无真实代码或凭据。
指出超范围修改、失败测试和缺失证据的审阅表；不执行，未实测。
比较这份虚构计划、差异和测试日志，列出验收通过项、失败项、未知项和超范围修改。不要仅凭执行者总结认定成功。不要访问文件、运行命令、删除或推送任何内容。

## 来源

- [许可目录现场正文](https://agentusecases.ai/use-case/split-work-between-chatgpt-architect-and-codex-executor)：许可目录转述Windows实验桥接、一次CAD体验及基本角色分工；无性能数字，未读原作者代码。
- [Codex官方集成层说明](https://developers.openai.com/blog/codex-as-a-platform)：官方说明codex exec适合有边界任务、SDK适合程序化操作、app-server提供持久会话事件与批准处理；不证明作者桥接实现或实际收益。
- [OpenAI开发者回顾更新](https://developers.openai.com/blog/openai-for-developers-2025)：页面明确2026-09-05更新称Codex MCP server已移除。这是Codex作为MCP服务端，不等于所有MCP客户端或自定义文件桥接被移除。
- [Codex工作流Cookbook](https://developers.openai.com/cookbook/examples/codex/codex_mcp_agents_sdk/building_consistent_workflows_codex_cli_agents_sdk)：本轮页面仍含旧MCP示例，同时提到app-server更深入集成；历史样例不能当作当前版本已实测的安装指南。
- [原作者文章](https://www.reddit.com/r/OpenAI/comments/1uow2ld/i_built_a_bridge_between_chatgpt_and_codex)：原文未读；目录转述和试用模板不冒充作者实现。
