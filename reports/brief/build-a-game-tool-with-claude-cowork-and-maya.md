# 用Claude Cowork与Maya迭代游戏工具代码

## 中文

    用Claude Cowork和Maya开发游戏工具
    发帖者几个月来一直用Claude Cowork讨论架构并为一款游戏工具生成代码，将结果转到PowerShell和Maya中运行，再把截图发回去继续处理。
    使用的是
    Claude Cowork
    他们做了什么
    发帖者表示，自己不会编程，花了几个月开发一款游戏相关工具。他准备了一个Claude.md提示文件，并形成了这样的循环：在Claude Cowork中讨论架构，让Cowork生成代码，在PowerShell中运行这些代码，将结果导入Maya，然后把截图发回Claude，继续迭代。有时他还会让Claude做一次审查，再把审查内容交给ChatGPT征求额外意见后继续。
    进展与成效
    帖子没有报告已经完成的成果，也没有性能数字；主要记录了发帖者称几个月来一直能使用的一套迭代流程。一个明确的限制是，Claude需要截图才能判断毛发渲染效果，因为未着色的样条线视图难以看清。
    值得注意
    主要问题在于人工交接：代码在Claude之外的PowerShell中运行，在Maya中检查，再通过截图审查，而不是集成的渲染循环。
    亲自尝试
    使用
    Claude Cowork
    复制提示词
    我正在用[Maya或其他应用]为[游戏或3D制作流程]开发一款工具。目标是：[描述工具]。先和我讨论架构，再以可测试的小步骤编写代码，并告诉我每一部分应该在哪里运行。我会把错误信息和截图发给你，以便修复问题。当这款工具能在我的项目中实现[预期行为]时，我们就完成了。
    原始来源：https://www.reddit.com/r/ClaudeAI/comments/1u8atjx/claude_coworker_claude_coder

<details><summary>English original</summary>

    Build a game tool with Claude Cowork and Maya
    The poster used Claude Cowork for months to discuss architecture and generate code for a game tool, moving results into PowerShell and Maya and sending screenshots back for follow-up.
    Done with
    CW
    Claude Cowork
    What they did
    The poster says they spent a couple of months building a game-related tool as a non-coder, with a Claude.md prompt file and a loop where they discussed architecture in Claude Cowork, had Cowork generate code, ran that code in PowerShell, imported the results into Maya, then sent screenshots back to Claude to continue iterating. They also sometimes asked Claude for an audit and passed that to ChatGPT for extra input before proceeding.
    How it went
    The thread does not report a finished result or any performance numbers; it mainly documents an iterative workflow the poster says has been workable for months. A stated limitation is that Claude could not directly judge the hair renders without screenshots because the unshaded spline view was hard to read.
    Worth knowing
    The main catch is manual handoff: code was run outside Claude in PowerShell, checked in Maya, and reviewed through screenshots rather than an integrated render loop.
    Try it yourself
    with
    Claude Cowork
    Copy prompt
    I'm building a tool for [game or 3D pipeline] in [Maya or another app]. Here's the goal: [describe the tool]. Talk through the architecture with me, then write the code in small testable steps, and tell me where to run each piece. I'll send back error messages and screenshots so you can fix problems. We're done when the tool does [expected behavior] in my project.
    Original source: https://www.reddit.com/r/ClaudeAI/comments/1u8atjx/claude_coworker_claude_coder

</details>

## 原作者的方法与来源

来源：[Intelligent_Day_7282 describes a manual Cowork–Maya loop](https://www.reddit.com/r/ClaudeAI/comments/1u8atjx/claude_coworker_claude_coder)

作者方法摘要

1. 在Cowork讨论架构，再用PowerShell运行生成代码，并将结果导入Maya。
   English summary: Discuss architecture in Cowork, then run generated code in PowerShell and import results into Maya.

2. 把渲染截图发回审查；有时将Claude的审查交给ChatGPT获取另一份意见。
   English summary: Send rendered screenshots back for review; sometimes pass Claude’s audit to ChatGPT for another opinion.

3. 作者当时尚未使用Claude Code，正在询问切换是否会改善流程。
   English summary: The author had not used Claude Code and was asking whether switching would improve this workflow.

## 简要分析

商业分数未评定。

### 原案是一条人工参与的开发循环

能核实的是作者公开描述了几个月的使用方式，不是工具已经交付。架构讨论、代码执行、Maya导入和截图评价由人串起来；不能改写成Cowork自主控制Maya，也不能把评论者建议CLI互通写成作者已实现。帖子没有工具规格、代码仓库、运行环境版本或成功产物，无法复现其具体功能，因此保留为有依据简报。

依据：[Sauthor](https://www.reddit.com/r/ClaudeAI/comments/1u8atjx/claude_coworker_claude_coder), [Sdirectory](https://agentusecases.ai/use-case/build-a-game-tool-with-claude-cowork-and-maya)

### 代码通过与视觉通过分开

作者解释毛发在未着色时像难辨形体的蓝色样条，截图不是多余附件，而是视觉评价的输入。拟议验收应固定相机、灯光、材质和渲染设置，并保存生成代码版本及对应截图；不把两张机位不同的图误判为改进。截图能帮助判断形状与体积，却不能证明动画、导出、性能或游戏内效果。每轮应说明哪些是人工美术判断、哪些由程序检查。

依据：[Sauthor](https://www.reddit.com/r/ClaudeAI/comments/1u8atjx/claude_coworker_claude_coder)

### PowerShell不等于Maya运行环境

PowerShell只是命令入口，不能从名字判断里面运行普通Python、mayapy还是外部工具。Autodesk说明Maya脚本编辑器和外部解释器的初始化方式不同，说明环境明确比“代码能运行”更重要。建议记录Maya/Python/插件版本、输入文件、命令、输出和错误；这些是改进建议，不是原作者已有配置。本轮没有安装Maya、启动其许可证或运行未知脚本。

依据：[Smaya](https://help.autodesk.com/cloudhelp/2026/ENU/Maya-Scripting/files/GUID-D457D6A0-1E7F-4ED2-B0B4-8B57153B563B.htm), [Sauthor](https://www.reddit.com/r/ClaudeAI/comments/1u8atjx/claude_coworker_claude_coder)

### 今天的Cowork与历史帖子分开

本次2026年10月20日读取的官方专项文档已说明：Pro/Max新Cowork任务自10月6日起在云端，之前开始的本地任务保留；接触本机文件和应用仍需要在线Desktop。目录所述历史工作流仍忠实保存，不用今天架构倒推作者当时设置。部分通用安装介绍仍有本地VM表述，当前范围判断优先采用明确日期与条件的专项说明，不把所有账户或旧任务一概而论。

依据：[Sarchitecture](https://support.claude.com/en/articles/14479288-claude-cowork-architecture-overview), [Ssurface](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile)

### 换工具不能自动消除交接

当前官方提供computer use beta和本地Claude Code路线，证明存在不同接入方式，不证明Maya里的复杂渲染已经可靠自动化。可以先把稳定文件处理和脚本步骤整理成明确命令，再对比手工截图流程；视觉审美和异常处理仍需验证。现有Maya脚本工具、技术美术协作或继续人工循环也是替代，不能只因为CLI更可编程就假定更适合不会代码的作者。

依据：[Scomputer](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork), [Ssurface](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile)

### 谁可能为这类协作付钱

直接使用者是懂3D目标但不熟悉编程的艺术家，可能付款者是有重复制作需求的小团队或工作室。可销售的假设不是一款已成型的毛发工具，而是边界明确的流程配置、脚本辅助和验收材料。本案没有客户、合同、收入或净省时数据，使用几个月也不等于有商业复购。低频单次需求可能更适合请技术美术完成；重复任务才值得评估维护成本。

依据：[Sauthor](https://www.reddit.com/r/ClaudeAI/comments/1u8atjx/claude_coworker_claude_coder)

### 先以小范围可检查交付验证

假设从已有3D制作合作或工具支持关系展示自有样例，先承诺一个输入、一个输出和明确不改的场景对象，而非承诺完全代替开发者。获客渠道与愿付价未验证，本轮没有联系作者或客户。复制条件包括目标DCC版本、插件许可、场景规范、原资产授权和回退方法；如果每个客户的材质与工具链都不同，收益更接近定制工时服务而非通用订阅。

依据：[Sauthor](https://www.reddit.com/r/ClaudeAI/comments/1u8atjx/claude_coworker_claude_coder), [Smaya](https://help.autodesk.com/cloudhelp/2026/ENU/Maya-Scripting/files/GUID-D457D6A0-1E7F-4ED2-B0B4-8B57153B563B.htm)

### 两种同范围成本情景

以一个小脚本的实现与一次受控场景验收包为单位，每月4包，不含大型工具产品或持续无限修改。低返工假设人工4小时按30美元为120、模型预算2，已列122/包、488/月；高返工12小时为360、模型预算6，已列366/包、1464/月。所有数值是研究者假设，不是作者工资、套餐价或实际耗时。Maya及插件许可、渲染硬件、获客和长期版本维护未知，另计且不能默认为零。售价未知，不算利润。

依据：[Sauthor](https://www.reddit.com/r/ClaudeAI/comments/1u8atjx/claude_coworker_claude_coder)

### 自用价值在于降低表达与尝试门槛

对能明确表达形状目标并判断结果的艺术家，讨论架构和分步生成代码可能帮助尝试原本难以启动的工具。但设置、执行、截图、解释错误和返工都消耗时间，原案没有量化净收益。频率随项目迭代而非固定每日任务；维护依赖软件更新和插件兼容。不会编程仍不意味着可以跳过文件备份、差异检查和简单失败恢复。

依据：[Sauthor](https://www.reddit.com/r/ClaudeAI/comments/1u8atjx/claude_coworker_claude_coder)

### 项目资产与截图也可能需要许可

客户模型、纹理、路径和截图里的项目名称可能受保密约束。当前云端工作流不能描述为所有资料不离本机；应先核哪些文件允许处理，只提供自有或获准样例，关闭无关敏感窗口。生成脚本先审其文件访问与删除行为，输出到副本而非覆盖原场景。第二模型意见不自动增加正确性，也不是把客户资产再传给另一服务的授权。

依据：[Sarchitecture](https://support.claude.com/en/articles/14479288-claude-cowork-architecture-overview), [Scomputer](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork)

### 建议先验证一个最小闭环

用自有简单场景定义一个可观察修改，保留原文件和标准截图。每次只执行一小步，记录运行环境、命令、日志和产物；含错误回退及重复运行是否意外叠加的检查。视觉比较用固定条件，功能与性能另列。预期得到可复核的改动链，不是成品游戏工具。本轮未执行Maya或模型试用，原始Claude.md未取得，不能编造其内容。

依据：[Smaya](https://help.autodesk.com/cloudhelp/2026/ENU/Maya-Scripting/files/GUID-D457D6A0-1E7F-4ED2-B0B4-8B57153B563B.htm), [Sauthor](https://www.reddit.com/r/ClaudeAI/comments/1u8atjx/claude_coworker_claude_coder)

## 自用价值：待核实

人工流程有自述，但没有功能成品或净省时测量。

依据：Sauthor, Smaya, Sarchitecture

- 适用人群：能判断3D效果、希望分步构建工具的艺术家。
- 用途：架构讨论、小步代码、日志与截图反馈。
- 预期收益：可能降低开始制作工具的门槛，未量化收益。
- 设置成本：明确目标、软件/插件版本、自有样例和回退副本。
- 维护成本：版本兼容、失败恢复、截图与渲染成本。
- 使用频率：随项目反复迭代，非固定高频。
- 隐私风险：客户资产、屏幕内容与云端处理权限。
- 错误风险：运行环境错配、无关场景修改、重复执行和视觉误判。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/build-a-game-tool-with-claude-cowork-and-maya

建议工具：Claude Cowork

    I'm building a tool for [game or 3D pipeline] in [Maya or another app]. Here's the goal: [describe the tool]. Talk through the architecture with me, then write the code in small testable steps, and tell me where to run each piece. I'll send back error messages and screenshots so you can fix problems. We're done when the tool does [expected behavior] in my project.

自编试用模板

准备条件：自有简单Maya场景、明确目标与不改范围、软件版本和备份。

工具：获准助手及合法可用Maya环境；本轮没有安装或执行。

预期结果：小步改动、日志、固定条件截图及回退记录，未实测。

### 源站Copy prompt

原文模板

出处：https://agentusecases.ai/use-case/build-a-game-tool-with-claude-cowork-and-maya

依据：Sdirectory

    I'm building a tool for [game or 3D pipeline] in [Maya or another app]. Here's the goal: [describe the tool]. Talk through the architecture with me, then write the code in small testable steps, and tell me where to run each piece. I'll send back error messages and screenshots so you can fix problems. We're done when the tool does [expected behavior] in my project.

### 最小视觉工具验收计划

自编模板

出处：研究团队自编

依据：Sauthor, Smaya

    只为这份自有简单场景制定一项小改动计划。先列运行环境、输入输出、不可修改对象、日志、固定相机截图和回退方法；不执行脚本、不覆盖文件、不上传客户资产。区分代码正确、视觉判断和性能验证。

## 来源

- [许可目录：Cowork与Maya开发流程](https://agentusecases.ai/use-case/build-a-game-tool-with-claude-cowork-and-maya)：完整目录原文、实际Cowork与试用模板；未声称成品或性能数据。
- [Intelligent_Day_7282：Coworker到Coder的流程讨论](https://www.reddit.com/r/ClaudeAI/comments/1u8atjx/claude_coworker_claude_coder)：作者自述3D艺术家不会代码，几个月使用Cowork讨论架构、生成代码，再人工PowerShell运行、导入Maya、发截图；偶尔Claude审查送ChatGPT。作者说未用过Claude Code，想了解收益；毛发需要着色渲染，蓝色样条难判断。评论提出自动化或CLI互通，但未证明作者已采用。没有成品、代码、性能或收入。
- [Autodesk Maya2026：Python初始化与退出](https://help.autodesk.com/cloudhelp/2026/ENU/Maya-Scripting/files/GUID-D457D6A0-1E7F-4ED2-B0B4-8B57153B563B.htm)：外部Python/mayapy需加载初始化Maya库并正确退出；Maya脚本编辑器内已初始化，不应重复调用。这个环境边界不证明原作者具体用哪种脚本，也不证明渲染视觉已正确。
- [Anthropic：Cowork架构说明](https://support.claude.com/en/articles/14479288-claude-cowork-architecture-overview)：当前说明新会话默认云端，Pro/Max自2026-10-06后新任务为云端，旧本地任务例外；本地文件经在线Desktop及已连文件夹访问，读入内容在服务端处理。不能把旧本地VM描述当当前全局事实，也不能把企业数据承诺套所有个人账户。
- [Anthropic：Cowork computer use](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork)：当前Pro/Max computer use为beta，macOS/Windows Desktop需应用权限与在线设备；连接器、浏览器、屏幕按适用路径处理。官方提示复杂任务仍可能出错，截图可见资料有暴露风险。不能据此称自动Maya毛发渲染已验收。
- [Anthropic：各端Cowork与10月6日变化](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile)：2026-10-06后Pro/Max新Cowork任务在云端，旧本地任务保留；访问本机文件/浏览器/应用仍要求Desktop在线。新任务若需只在本机运行，官方指向Claude Code Desktop；历史作者体验与当前能力应分开。
