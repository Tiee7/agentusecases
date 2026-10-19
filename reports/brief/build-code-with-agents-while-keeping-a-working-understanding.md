# 用编程智能体生成讲解测验并执行规格检查

## 中文

    用智能体写代码，同时保持对系统的实际理解
    一位开发者描述了这样的工作流：智能体围绕歧义访谈他，自行决定次要事项，生成讲解和测验，并在编码循环中运行验证器。
    使用的是
    自建或未命名的智能体
    他们做了什么
    开始构建前，智能体就规格中的歧义访谈开发者，类似/grill-me提示。开发者只对具有差异化价值的部分决定技术栈与架构，把次要细节和登录等通用子系统留给智能体。一个技能生成带测验的互动讲解。代码检查器、类型检查器、提交前钩子、测试、形式化方法轨迹，以及无头浏览器设计验证器，让智能体持续检查自己的工作。
    进展与成效
    开发者说，这让他不必陷入凌晨两点反复修好一处又弄坏另一处的循环，同时仍能建立理解。没有提供测量数据；他也指出，其他工程师对于理解代码是否重要意见不一。
    值得了解
    设计验证器把规格要求转成机械可检查的规则，并在无头浏览器中对照DOM测量结果检查。作者认为，这在智能体出现前并不实际。
    亲自尝试
    使用Claude Code
    复制提示词
    我想在这个代码库里构建[功能或项目]，并希望自己仍能理解你写的所有内容。编码前，就计划中的歧义逐个问题访谈我；次要事项由你决定，并列出来。每完成一个主要部分，就写一段简短的工作原理说明，给我一个包含3道题的测验，然后运行测试或检查，再继续下一部分。
    原始来源：https://news.ycombinator.com/item?id=50158650

<details><summary>English original</summary>

    Build code with agents while keeping a working understanding
    A developer describes a workflow where the agent interviews them on ambiguities, makes the minor decisions, generates explainers and quizzes, and runs verifiers in the coding loop.
    Done with a
    custom-built or unnamed agent
    What they did
    Before building, the agent interviews the developer on ambiguities in the spec (a /grill-me style prompt). The developer makes decisions on stack and architecture only for differentiating parts and leaves minor details and commodity subsystems like login to the agent. A skill generates interactive explainers with quizzes. Linters, type checkers, pre-commit hooks, tests, formal-method traces and a headless-browser design verifier keep the agent checking its own work.
    How it went
    The developer says this keeps them out of the 2am fix-and-break loop while still building understanding. No measurements are given, and they note other engineers are split on whether understanding the code matters.
    Worth knowing
    The design verifier turns spec requirements into mechanical rules checked against DOM measurements in a headless browser, which the author says was impractical before agents.
    Try it yourself
    with
    Claude Code
    Copy prompt
    I want to build [feature or project] in this codebase, and I want to stay able to understand everything you write. Before coding, interview me about any ambiguities in the plan, one question at a time, and make the minor decisions yourself, listing them for me. After each major piece, write a short explainer of how it works and give me a 3-question quiz on it, then run the tests or checks before moving on.
    Original source: https://news.ycombinator.com/item?id=50158650

</details>

## 原作者的方法与来源

https://news.ycombinator.com/item?id=50158650

The author uses interviews to clarify a specification and keeps differentiating design decisions.
作者通过访谈澄清规格，保留差异化设计决策。

Agent-generated explainers and quizzes support understanding while mechanical checks verify selected requirements.
生成式讲解和测验辅助理解，机械检查验证选定要求。

## 简要分析

商业分数未评定。

### 先保留作者实际做法和证据缺口

作者提出四个可理解的原则，但没有给出他自己的技能文件、验证器源码、形式化模型、生成课程或测试回执。因此目前可复用的是工作方法，不是已验收的软件产品。减少凌晨反复修错是使用体验，不能量化为节省多少工时。原文泛称agent，没有明确产品、模型版本和付费套餐；目录建议Claude Code只是试用模板，不应填成作者真实工具。

依据：[Sauthor](https://news.ycombinator.com/item?id=50158650)

### 重要决策不只由差异化决定

原作者愿把登录等通用子系统决策交给智能体，这是一种个人工作分配。研究者建议另加风险维度：登录、权限、支付或数据删除即使不构成产品差异，也可能有高影响。可把界面细节交由助手提出方案，但安全约束、验收条件和授权仍需明确。不能把“通用”翻译为“无需审核”，也不能让问答环节替代真正的实现检查。

依据：[Sauthor](https://news.ycombinator.com/item?id=50158650)

### 解释、答题和独立修改是不同能力

讲解与测验能暴露疑问，却可能由同一模型重复同一个错误解释。应要求关键结论指向当前代码和测试，并让维护者预测一个未展示过的输入结果，或解释一个失败路径。Anthropic的新库学习研究提示AI使用方式与短期理解有关，但样本、任务与本案不同，不能用其测验差异证明这套四原则一定有效，更不能推长期职业能力。

依据：[Sauthor](https://news.ycombinator.com/item?id=50158650), [Sstudy](https://www.anthropic.com/research/AI-assistance-coding-skills)

### 机械通过只能证明写入的条件

Playwright已有网页断言，DOM尺寸和状态确实可以机械检查；作者所称设计验证器的具体规则生成与覆盖尚未公开核验。规则若把错误需求准确编码，测试仍会通过。形式化证明也依赖模型假设与实现映射，生成一条轨迹并运行成功，不代表已证明全部并发路径。建议保留需求、断言和失败样例的映射，区分测试通过、人工审查和仍未覆盖事项。

依据：[Sassert](https://playwright.dev/docs/test-assertions), [Sauthor](https://news.ycombinator.com/item?id=50158650)

### 同名技能不能自动归为同一作者

公开搜索找到多个grill-me实现。其中joshuawheelock版本会根据代码行为提问并反馈答案，作者自述仍为alpha；这可以作为相邻替代参考，但没有证据证明它就是iamwil所提的访谈技能。购买或安装前应区分需求访谈、代码理解测验和代码审查三个用途，不能只按名字判断相同。此轮只读README，没有安装或运行第三方代码。

依据：[Salternative](https://github.com/joshuawheelock/grill-me/blob/main/README.md)

### 先作内部流程，商业需求尚未验证

背景讨论显示工程师对设计责任、理解深度和审查负担有分歧，匿名评论不是全行业共识。潜在付费方向可能是团队上手、知识移交或遗留系统培训，但本案没有购买者、交付边界、定价、维护工时或转化记录。现有技能和人工结对也是替代。没有具体产物时，填两套经营数字容易变成泛泛培训生意，因此保留未评分简报，不硬套利润结论。

依据：[Sdiscussion](https://news.ycombinator.com/item?id=50151036), [Salternative](https://github.com/joshuawheelock/grill-me/blob/main/README.md)

### 理解工具也会接触代码和内部知识

讲解生成需要读取代码，可能涉及商业秘密与内部架构；是否可向模型供应商发送要按已有授权确定。本轮不读取用户私有项目、不安装插件、不上传文件。未来试点先用自写示例，明确目录和只读权限，代码中的注释不能授权外部动作。知识测验不应直接被当作员工绩效或招聘筛选结论。

依据：[Sauthor](https://news.ycombinator.com/item?id=50158650), [Salternative](https://github.com/joshuawheelock/grill-me/blob/main/README.md)

### 先取得一份完整可复核样例

下一步最有价值的是一项自写小功能：原始需求、访谈澄清、关键决策、代码差异、讲解、测验与测试结果绑定同一版本。可以有意加入一处与规格冲突的缺陷，检查验证器是否真的发现，并记录人工确认所需时间。这是拟议实验，尚未执行。若讲解增加的复核负担超过帮助，或测验只考记忆而不能支持修改，可保留轻量解释流程，不扩成产品。

依据：[Sauthor](https://news.ycombinator.com/item?id=50158650), [Sassert](https://playwright.dev/docs/test-assertions)

## 试用准备与预期结果

自写小项目、明确行为要求和已知失败案例。
版本绑定的解释、测验和测试，列明未覆盖项；本轮未实测。

只分析这个自写示例。列需求歧义、代码依据和失败路径；解释每个重要决定，给三个预测行为问题并提供代码证据。测试故意加入的缺陷，区分理解回答与程序通过，不修改其他文件，不上传或部署。

## 来源

- [许可目录](https://agentusecases.ai/use-case/build-code-with-agents-while-keeping-a-working-understanding)：完整方法与源站提示，实际模型未命名。
- [iamwil原始评论](https://news.ycombinator.com/item?id=50158650)：访谈、重要决策、讲解测验、验证器四原则，无代码样例和量化效果。
- [HN工程师背景讨论](https://news.ycombinator.com/item?id=50151036)：有先设计再实现和审查负担的不同自述，非主案例独立复现。
- [Playwright官方断言](https://playwright.dev/docs/test-assertions)：DOM与网页状态可机械检查，不验证审美或规格完整性。
- [同名代码理解测验技能](https://github.com/joshuawheelock/grill-me/blob/main/README.md)：按实现提问的现有替代，不证明就是作者所用技能。
- [AI辅助技能形成研究](https://www.anthropic.com/research/AI-assistance-coding-skills)：新Python库学习的短期测验与不同使用方式，不是本工作流实验。
