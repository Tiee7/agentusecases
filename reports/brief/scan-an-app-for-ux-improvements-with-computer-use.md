# 用Claude Code检查应用用户体验

## 中文

    用computer use扫描应用，寻找UX改进
    一名用户尝试在Windows上使用Claude Code的computer-use功能，扫描自己的应用寻找用户体验改进，并询问它在这个平台上是否好用。
    使用的是
    Claude Code
    他们做了什么
    发帖者尝试用Claude Code的新computer-use功能，在Windows上检查自己的应用是否存在UX问题。在那次运行中，它无法使用截图MCP服务器，于是改用Shell脚本等方式截屏。评论者表示，内置computer-use MCP服务器会出现在macOS上，但在Windows PowerShell或WSL中的Claude Code里没有出现；不过，有一人报告说，在WSL2中截屏、调试和视频分析可以工作。
    进展与成效
    对于这次Windows应用评审，用例报告的是原生支持不可靠，而不是一次顺畅的UX扫描。讨论没有提供量化改进或输出质量，只说明原生Windows似乎不受支持，而WSL2可能更好一些。
    值得注意
    主要问题是配置：讨论称Claude Code开箱即用时缺少原生Windows computer-use支持，因此照搬这个用法可能需要WSL2，或自行接入额外工具。
    亲自尝试
    使用
    Claude Code
    复制提示词
    按[启动方式]运行我的应用，使用computer use点击检查主要流程：[列出2至3个关键界面或任务]。从用户角度记下令人困惑、不一致或缓慢的地方。最后给出按优先级排列的[5至10]项UX改进，每项注明对应界面；在我选定要做的项目之前，不要修改任何代码。
    原始来源：https://www.reddit.com/r/ClaudeAI/comments/1sp0r2s/is_cc_computer_use_crappy_on_windows

<details><summary>English original</summary>

    Scan an app for UX improvements with computer use
    A user tried Claude Code's computer-use feature on Windows to scan their app for UX improvements, and asks whether it works well there.
    Done with
    CC
    Claude Code
    What they did
    The poster tried Claude Code’s new computer-use feature on Windows to inspect their app for UX issues. In their run, it could not use the screenshot MCP server, so it fell back to shell-script ways of grabbing screenshots; commenters said the built-in computer-use MCP server showed up on macOS, not in Claude Code on Windows PowerShell or WSL, though one person reported screenshots, debugging, and video analysis working in WSL2.
    How it went
    For this Windows app-review use case, the reported result was unreliable native support rather than a smooth UX scan. The thread offers no measured improvements or output quality, only that native Windows seemed unsupported while WSL2 may work better.
    Worth knowing
    The main catch is setup: out of the box, Claude Code was described as lacking native Windows computer-use support, so copying this likely means using WSL2 or wiring in extra tooling yourself.
    Try it yourself
    with
    Claude Code
    Copy prompt
    Run my app at [how to start it] and use computer use to click through the main flows: [list of 2-3 key screens or tasks]. Note anything confusing, inconsistent, or slow from a user's point of view. Finish with a prioritized list of [5-10] UX improvements, each with the screen it applies to, and don't change any code until I pick which to do.
    Original source: https://www.reddit.com/r/ClaudeAI/comments/1sp0r2s/is_cc_computer_use_crappy_on_windows

</details>

## 原作者的方法与来源

来源：[Orinks reports a screenshot problem during an app UX scan](https://www.reddit.com/r/ClaudeAI/comments/1sp0r2s/is_cc_computer_use_crappy_on_windows)

作者方法摘要

1. 要求computer use在Windows上扫描应用，寻找UX改进。
   English summary: Ask computer use to scan the app for UX improvements on Windows.

2. 截图MCP尝试失败，运行转向Shell截屏方式。
   English summary: The screenshot MCP attempt failed, and the run fell back to shell-based screenshot methods.

3. 作者询问平台支持情况，没有展示已完成UX报告或量化改进。
   English summary: The author asked about platform support; no completed UX report or measured improvement was shown.

## 简要分析

商业分数未评定。

### 本案先遇到了工具可用性问题

原作者Orinks描述的是一次截图工具失败的尝试，并非完成的UX评审。帖子没有应用类型、版本、具体操作流程、问题清单、前后对比或用户测试数据，因此无法评价改进质量。Shell截图只是技术降级路径，也不能据此认定agent已正确看见所有界面。保留为有依据简报，不能补造5至10条应用缺陷。

依据：[Sauthor](https://www.reddit.com/r/ClaudeAI/comments/1sp0r2s/is_cc_computer_use_crappy_on_windows)

### 历史体验与当前支持必须分开

目录显示历史来源日期2026年5月6日，而本次官方文档核验是10月20日。当前CLI computer use文档限macOS，Desktop文档则明确macOS和Windows，二者不能混用。完整译文忠实保留当时Windows似乎不受支持的叙述，当前分析不再把它写成所有Claude Code形态都不支持Windows。新文档也不能反过来否定作者当时实际失败。

依据：[Sdirectory](https://agentusecases.ai/use-case/scan-an-app-for-ux-improvements-with-computer-use), [Scli](https://code.claude.com/docs/en/computer-use), [Sdesktop](https://code.claude.com/docs/en/desktop)

### WSL2不是一个保证成功的修复按钮

评论者对PowerShell、WSL与内置MCP的观察不同，另一个人称WSL2能截图和分析视频，却没有同一版本和工具配置。不能将这条评论升级为官方通用方案。复现前应明确CLI还是Desktop、运行系统、应用所在系统、版本、套餐和授权范围；桌面应用内置Code版本也可能不同于命令行版本。本轮没有更改系统、安装WSL或启用屏幕权限。

依据：[Sauthor](https://www.reddit.com/r/ClaudeAI/comments/1sp0r2s/is_cc_computer_use_crappy_on_windows), [Sdesktop](https://code.claude.com/docs/en/desktop)

### 截图、功能和用户体验是不同证据

能得到截图只证明取得一张图；点击成功不证明任务符合用户目标；模型说不美观也不等于真实用户无法完成任务。建议结果分为可复现缺陷、基于规则的可用性建议和待真人验证的假设，每项附界面、操作步骤与证据。原案没有这些产物，不能声称其已完成评审。性能慢也需计时和环境说明，不能仅凭模型感觉下结论。

依据：[Sauthor](https://www.reddit.com/r/ClaudeAI/comments/1sp0r2s/is_cc_computer_use_crappy_on_windows)

### Web应用可优先用浏览器测试

Playwright提供明确的Web端到端测试路线，适合稳定流程、断言与可复核轨迹；原生桌面工具需相应支持的应用控制方式。两者都不是所有UX问题的答案。对一次性评审，人工按固定流程检查或用户提供脱敏截图也可能更简单；若需要反复回归，建立断言与证据比每次自由漫游更有复制价值。

依据：[Splaywright](https://playwright.dev/docs/intro), [Scli](https://code.claude.com/docs/en/computer-use)

### 客户购买的是可行动的问题清单

假设客户是要发布Web或桌面产品的小团队，付款者为产品负责人或开发负责人。可交付范围是2至3个事先约定流程的观察与优先级建议，而非保证转化提升。每项问题需能复现、解释用户影响并注明不确定性。原案无真实客户、销售、报价或结果，不适合直接当自动UX审计服务的成功案例。

依据：[Sauthor](https://www.reddit.com/r/ClaudeAI/comments/1sp0r2s/is_cc_computer_use_crappy_on_windows)

### 限定流程减少重复排查

复制前固定应用构建、测试账号、窗口尺寸、语言和起点状态；只读观察也要避免点击产生真实交易或删除。首次先验证工具能访问目标界面，失败就明确工具阻塞，不把它变成一份通用建议报告。拟议获客从已有产品开发合作演示一个受控案例，本轮不联系第三方。若大量时间耗在每台机器授权与版本差异，成本更接近现场配置支持。

依据：[Splaywright](https://playwright.dev/docs/intro), [Sdesktop](https://code.claude.com/docs/en/desktop)

### 两种同范围评审成本情景

以三个限定流程的一份评审包为单位，每月10包。低返工假设人工2h×30USD/h=60，加模型预算1，已列61/包610/月；高返工6h=180，加模型预算3，183/包1830/月。数字为研究者假设，不是作者耗时或套餐报价。设备、测试账号、维护与获客未知另计，不默认零；售价未知，不算利润。不能用每张截图的模型费用代表完整交付成本。

依据：[Sauthor](https://www.reddit.com/r/ClaudeAI/comments/1sp0r2s/is_cc_computer_use_crappy_on_windows)

### 自用价值取决于明确的应用任务

对已有可启动应用、能判断问题真假的开发者，视觉反馈可能帮助发现遗漏。但原案没测净省时，配置排障也可能超过手工浏览时间。首次需准备测试环境、任务边界与备份；持续维护受系统权限、工具更新和界面变化影响。频率通常随版本发布，不必每日运行。缺少完成的扫描证据，自用价值保持待核实。

依据：[Sauthor](https://www.reddit.com/r/ClaudeAI/comments/1sp0r2s/is_cc_computer_use_crappy_on_windows)

### 屏幕权限不是隔离沙箱

当前官方说明computer use作用于真实桌面；应只授权目标应用并关闭或遮蔽无关私人资料。截图可能包含客户记录、通知和登录信息，不能因任务叫UX检查就默认允许上传全部画面。授权、截图来源和测试账户范围应在试用前明确；本轮只读公开资料，没有接入任何私人屏幕或服务。

依据：[Sdesktop](https://code.claude.com/docs/en/desktop), [Scli](https://code.claude.com/docs/en/computer-use)

### 预期交付可复核观察而不是自动改代码

先用自有演示应用定义2至3个流程，记录环境和访问检查；每个发现附步骤、截图来源、预期与实际行为、影响及置信度。没有证据的建议放入假设栏。原站模板明确在用户选择之前不改代码，应保留该边界。下一步是验证一份小报告能否被开发者复现，不是直接放任agent修改、部署或扩大权限。本轮没有真实产品试用。

依据：[Sauthor](https://www.reddit.com/r/ClaudeAI/comments/1sp0r2s/is_cc_computer_use_crappy_on_windows), [Splaywright](https://playwright.dev/docs/intro)

## 自用价值：待核实

原案没有成功评审产物或净收益测量。

依据：Sauthor, Sdesktop

- 适用人群：已有可启动应用并能复核观察的开发者。
- 用途：限定流程的视觉与交互检查。
- 预期收益：可能发现遗漏，未证明改进效果或省时。
- 设置成本：明确CLI/Desktop、版本、系统、应用与测试账号、授权边界。
- 维护成本：工具更新、权限与界面变化、失败复现。
- 使用频率：随版本发布或重要流程变化。
- 隐私风险：真实桌面截图中的客户信息、通知和账户数据。
- 错误风险：截错窗口、把主观建议当缺陷、遗漏步骤或误报完成。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/scan-an-app-for-ux-improvements-with-computer-use

建议工具：Claude Code

    Run my app at [how to start it] and use computer use to click through the main flows: [list of 2-3 key screens or tasks]. Note anything confusing, inconsistent, or slow from a user's point of view. Finish with a prioritized list of [5-10] UX improvements, each with the screen it applies to, and don't change any code until I pick which to do.

自编试用模板

准备条件：自有演示应用、三条关键流程、测试数据和许可画面范围。

工具：匹配平台的获准应用控制或Web测试工具；本轮未安装执行。

预期结果：带可复现步骤的观察清单，区分问题与假设；未实测。

### 源站Copy prompt

原文模板

出处：https://agentusecases.ai/use-case/scan-an-app-for-ux-improvements-with-computer-use

依据：Sdirectory

    Run my app at [how to start it] and use computer use to click through the main flows: [list of 2-3 key screens or tasks]. Note anything confusing, inconsistent, or slow from a user's point of view. Finish with a prioritized list of [5-10] UX improvements, each with the screen it applies to, and don't change any code until I pick which to do.

### 可复核UX观察计划

自编模板

出处：研究团队自编

依据：Sauthor, Sdesktop, Splaywright

    先只制定自有演示应用的三个流程检查计划，列系统、版本、窗口与许可截图范围。每条发现要有步骤、预期、实际、证据和置信度，区分缺陷与建议。工具不可达明确报告；不改代码、不启用新权限、不提交真实表单或交易。

## 来源

- [许可目录：Windows应用UX扫描尝试](https://agentusecases.ai/use-case/scan-an-app-for-ux-improvements-with-computer-use)：完整目录历史叙述和模板；目录显示2026-05-06，不作为当前平台支持证明。
- [Orinks：Windows computer use截图失败](https://www.reddit.com/r/ClaudeAI/comments/1sp0r2s/is_cc_computer_use_crappy_on_windows)：作者尝试应用UX扫描，截图MCP失败后使用Shell方法，未提供评审结果；评论macOS/PowerShell/WSL支持说法互相混杂，一位WSL2成功自述无具体配置。UIA是评论建议，不是作者采用。原URL自动重定向r/ClaudeCode同一帖子。
- [Claude Code：CLI computer use](https://code.claude.com/docs/en/computer-use)：当前CLI computer use为macOS研究预览，Pro/Max、交互会话，不支持-p或Team/Enterprise；文档将Desktop macOS/Windows另列。不能把CLI支持范围当全部产品范围。
- [Claude Code Desktop：当前屏幕控制](https://code.claude.com/docs/en/desktop)：当前英文文档明示Desktop computer use为macOS和Windows研究预览，需Pro/Max和运行中的Desktop、默认关闭、按应用授权；运行真实桌面不是Bash沙箱。Desktop内置Code与CLI版本可不同。
- [Playwright：Web应用端到端测试](https://playwright.dev/docs/intro)：官方定位现代Web应用端到端测试，可跨Chromium/WebKit/Firefox在Windows/Linux/macOS和CI运行，并提供断言、截图/trace等工具。浏览器自动化不等于所有原生桌面app控制，也不替代真人可用性验证。
