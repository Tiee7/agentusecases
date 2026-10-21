# 用 Claude Code 配合项目规则与数值日志开发终端应用

## 中文

    用 AGENTS.md 和日志，让 Claude Code 充当共同开发者
    作者将 Claude Code 用于规划、编码、测试和调试，通过 AGENTS.md 和数值日志改善准确性与上下文处理。
    使用工具
    CC
    Claude Code
    做了什么
    作者花了约七个月，在 WezTerm 基础上构建 Rust 终端复用器 ThinkTerm，让 Claude Code 充当共同开发者。Claude Code 负责规划、编写代码、测试和基准测试，作者审查输出；硬性规则写在 AGENTS.md 或 Claude.md 中。对于没有界面框架的 UI 工作，由于 Claude 看不到窗口，它会把画面保存为 PNG。
    结果如何
    成果是一个面向 macOS、Linux 和 Windows 的开源应用，作者称它可以管理多台机器上的智能体会话。作者指出的主要短板是调试准确性：Claude 曾在一个问题上反复猜错，直到作者让它记录实际尺寸数值。
    值得了解
    最具体的经验是强制 Claude 记录数字和真实测量值，而不是推测；作者说这样在五次错误猜测后修好了一个问题。
    亲自试用
    使用
    Claude Code
    复制提示词
    在[仓库路径]创建 AGENTS.md，描述项目结构、运行和测试方式、编码约定以及需要遵循的规则。然后帮助我处理[功能或问题]，先规划，再编码、测试和调试，并添加清晰的编号日志行，以便从输出核实行为。测试通过后停止，向我展示修改摘要。
    原始来源：https://www.reddit.com/r/ClaudeWorkflows/comments/1xax029/workflow_claude_code_as_a_codeveloper_planning

<details><summary>English original</summary>

    Use Claude Code as co-developer with AGENTS.md and logging
    The author uses Claude Code for planning, coding, testing, and debugging, with AGENTS.md and numerical logging to improve accuracy and context handling.
    Done with
    CC
    Claude Code
    What they did
    The author spent about seven months building ThinkTerm, a Rust terminal multiplexer on top of WezTerm, with Claude Code acting as a co-developer. Claude Code handled planning, code writing, tests, and benchmarks, while the author reviewed the output; hard rules lived in AGENTS.md or Claude.md, and for UI work without a framework Claude saved frames as PNGs because it could not see the window.
    How it went
    The result was an open-source app for macOS, Linux, and Windows that the author says lets them manage agent sessions across machines. The main shortcoming they call out is debugging accuracy: Claude guessed wrong repeatedly on one bug until they made it log actual numeric sizes.
    Worth knowing
    The most concrete catch is to force Claude to log numbers and real measurements instead of inferring them; the author says that fixed a bug after five wrong guesses.
    Try it yourself
    with
    Claude Code
    Copy prompt
    Create an AGENTS.md file in [repo path] that describes the project's structure, how to run and test it, coding conventions, and rules for you to follow. Then help me with [feature or bug] by planning first, then coding, testing, and debugging, adding clear numbered log lines so you can verify behavior from the output. Stop when the tests pass and show me a summary of the changes.
    Original source: https://www.reddit.com/r/ClaudeWorkflows/comments/1xax029/workflow_claude_code_as_a_codeveloper_planning

</details>

## 目录转述方法

Claude Code辅助规划、实现和测试，作者审查修改。
Claude Code assisted planning, implementation and tests while the author reviewed changes.

目录称，改用实际数值日志代替反复猜测后取得了调试进展。
The directory reports a debugging breakthrough after replacing repeated guesses with measured numeric logs.

## 结论

公开项目和方法资料可核，但原作者完整调试轨迹、效率及收入缺证，保存有依据简报。

## 开源成果可查，开发收益仍未量化

本案例研究的是Claude Code共同开发工作流，不是把ThinkTerm当作已盈利产品。目录中的七个月和五次猜错来自作者体验，没有对照工时、缺陷率或收入凭据。公开仓库提供了真实项目这一层证据，但不证明模型独立完成、每个平台都稳定，或该方法比传统开发节省多少。原Reddit全文未取得，作者方法标不可读，目录转述与当前仓库资料分别保存。

来源：Sdirectory, Srepo

## 从猜原因转到可重复测量

可复制的核心是把一个具体错误变成可观测事件：固定输入与版本，记预期和实际尺寸、坐标或状态，先复现失败，再改变一个相关因素并复测。日志应包含单位、测量时机和对象，单纯增加编号却仍打印推断结论没有帮助。对于界面，保存PNG可能补充观察，但截图、几何数据、交互和实际GPU渲染并不等价。研究者建议用同一错误样例做修复前失败、修复后成功与正常路径回归，不把某次测试通过当所有画面正确。此处是验证设计，未运行ThinkTerm或复现原作者错误。

来源：Sdirectory, Srepo

## 指令文件应先确认真正加载

目录保留AGENTS.md或Claude.md原写法；现在产品文档则有版本门槛与加载优先级。复制时应先核当前版本、实际读入哪些文件和工作目录，不要在已有CLAUDE.md旁增加另一份后就默认两者生效。规则最好写项目真实测试命令、约束和可验证要求，而非堆积笼统口号。预印本摘要提示上下文文件不必然提高任务正确性，但它样本有限，不能据此删除所有规则。更稳妥的目标是减少约定遗漏，并用失败样例验证具体改进，而不是把文件本身当质量保证。

来源：Smemory, Sstudy

## 客户付的是修好的问题，不是日志行数

自用人群是能审查变更、理解测试边界的开发者。潜在经营方向可以是范围明确的缺陷修复或维护服务，付款人可能是产品负责人，但本案没有客户和预算证据。客户需要可复现修复、兼容性说明和回归记录，通常不会单独为一份规则文件长期付费。若任务无法复现、没有测试环境或需要凭据迁移，交付成本会迅速上升。不能从作者完成开源项目推断有人愿意购买其开发方法，更不能把程序会话数量当销量。

来源：Sdirectory, Srepo

## 原生复用与传统调试都是对照

ThinkTerm建立在已有终端基础上，WezTerm本来就有复用与远程域；其具体优势应在工作区组织与交互中实测，而不是宣称持久会话此前不存在。对于开发方法，调试器、可重复测试和人工审查也是现成路线。代理的价值是减少规划、修改和重复执行负担，但如果人仍需不断纠正猜测，净节省未必成立。用户问题#6说明配置与远端组件理解也是交付的一部分；回复中的成功应保留，不能只摘最初投诉营销。

来源：Swez, Sissue

## 按一次验收修复计算

所有输入均为研究者假设。轻量修复：工具摊销3美元、人工30分钟按40美元/小时计20、其它2、获客5，单位30；每月12次加固定维护40，共400美元。高监督修复：工具12、人工120分钟计80、其它5、获客10，单位107；同12次加固定维护100，共1384美元。实际售价未知，不计算毛利。初次环境准备和跨设备测试未取得工时，必须另记，不默认为零。重复猜错不仅耗模型额度，还占用审阅时间，因此应以最终验收所耗总资源为分母，而不是只统计最后一次成功执行。

来源：Scost, Sdirectory

## 复制条件、获客与责任

若未来验证服务，可以从既有软件维护关系里承接一个能够复现的具体缺陷，先交复现、日志证据、最小补丁和回归说明，限制变更范围。这里没有联系第三方或承接订单。客户代码与日志可能含账号和业务信息，应只采必要字段并避免持久保存凭据；公开错误报告也不能授权修改用户远端设备。经营壁垒更可能来自特定系统经验和可信验收，而非使用同一模型。任何重新分发开源代码的安排还应另核项目许可，本轮仅观察README许可说明，没有给法律结论或打包分发。

来源：Srepo, Sissue

## 反证与下一步

本轮检索公开项目、问题讨论和独立研究，未取得原案例五次猜错的完整轨迹或同条件效率复验。ThinkTerm用户反馈属于产物使用，不等于开发工作流的独立效果证明；预印本仅为方法反证，不能当商业市场数据。下一步可用自己已授权项目的一项可重复视觉尺寸错误，比较有测量日志与只描述症状的修复过程，记录实际修改、回归、人工分钟和工具成本。不运行额外付费API，不新增凭据。若不能复现、日志无真实测量、修改扩大范围或失败被隐藏，就停止交付并先补证据。

来源：Sissue, Sstudy, Sdirectory

## 自用与试用

- 能阅读代码并验证运行结果的开发者。
- 规划、补丁、测试和以实测为依据的调试。
- 可能减少重复操作，不保证所有错误都更快修复。
- 可复现环境、项目规则、测量点和测试命令。
- 规则与工具版本、日志噪声、跨平台回归。
- 随开发任务持续使用。
- 代码和日志可能带业务数据、凭据或远端信息。
- 猜测写成事实、测试范围不足、截图与实际渲染混淆。

自有授权仓库、可重复错误、版本和正常路径测试。
可核对的最小补丁和复现记录，不是跨平台质量认证。

## 来源

- [Sdirectory · 许可目录：共同开发与数值日志](https://agentusecases.ai/use-case/use-claude-code-as-co-developer-with-agents-md-and-logging)：目录转述七个月开发、一次五次错误猜测后通过数值日志修复；不是效率实验或经营收入。
- [Srepo · ThinkTerm公开项目README](https://github.com/RoversX/ThinkTerm)：公开项目基于Rust与WezTerm，介绍桌面、TUI和Web会话接入；移动端仍在开发。项目存在不等于各平台已由本研究实测。
- [Smemory · Claude Code指令文件文档](https://code.claude.com/docs/en/memory)：现行AGENTS.md直接加载受版本与配置影响，默认有CLAUDE.md时优先后者；文件存在本身不证明本次会话加载。
- [Swez · WezTerm复用文档](https://wezterm.org/multiplexing.html)：上游已有本地与远程复用能力；远程SSH复用需兼容远端组件。无需假定所有会话管理价值由新应用创造。
- [Sstudy · 上下文文件消融研究摘要](https://arxiv.org/abs/2607.27250)：2026年7月预印本摘要报告两种代理、17任务、3仓库及288次运行，该样本未测得上下文策略显著改变正确性；仅读摘要，不泛化为规则文件无用。
- [Sissue · ThinkTerm远端Codex识别问题](https://github.com/RoversX/ThinkTerm/issues/6)：0.1.9用户报告远端识别问题，讨论后称启用设置后工作正常；随后还有独立的Connect部署讨论。不能把全部问题合并成产品不可用或全部修好。
- [Scost · Claude Code成本说明](https://code.claude.com/docs/en/costs)：本日已读官方区分订阅额度、可选额外用量与API计费；持续调试的模型费用和人工监督须分别核算。

## 核验边界

未读取原Reddit全文、未运行ThinkTerm、未测GPU或远端连接、未读预印本全文。issue2与LICENSE链接普通工具读取失败，未用于结论；README许可描述不是法律审查。自有云浏览器12:57导航超时，公开资料用支持的Web读取。
 云端首导航超时后标签实际出现，但13:03的DOM与截图仅有Skip to content外壳；一次正常重载后仍如此，未取得云端README，不再重试。
