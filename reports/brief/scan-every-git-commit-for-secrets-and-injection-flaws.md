# 用 Claude Code 在 Git 提交前检查代码风险

## 中文

    扫描每次 Git 提交中的秘密信息与注入缺陷
    一个免费工具在每次提交时运行11个 Claude Code CLI 智能体，在代码进入仓库前检查秘密信息、注入缺陷和有问题的迁移。
    使用工具
    CC
    Claude Code
    CL
    Claude
    做了什么
    创建者将 Manta 构建成一种本地 Git 工作流，挂接到每次提交，在代码到达仓库前自动运行11个 Claude Code CLI 智能体。它们检查硬编码秘密信息、注入和XSS等OWASP类问题、代码质量与异步／查询问题，以及不安全的数据库迁移；提交被阻止时，工具可以建议修复，但复杂逻辑仍需人工审查。
    结果如何
    声称的结果是更早发现问题：危险提交在进入仓库前被阻止；工具免费、开源，并使用 Claude Code 免费层上的 Claude Sonnet 运行。作者也说明它并非独立工具，并会为每次提交增加几秒。
    值得了解
    主要限制是需要 Claude Code CLI，而且提交前钩子会为每次提交增加几秒。
    亲自试用
    使用
    Claude Code
    复制提示词
    在[仓库路径]设置 Git 提交前钩子，运行 Claude Code，检查每次暂存差异中的硬编码秘密信息、注入缺陷（SQL、命令、XSS）和高风险数据库迁移。如果发现问题，阻止提交，并打印文件、行号和建议修复。在永久安装之前，向我展示钩子脚本，并用一份示例问题提交测试它。
    原始来源：https://www.reddit.com/r/codereview/comments/1u6mhos/i_built_a_free_tool_that_runs_11_ai_agents_on

<details><summary>English original</summary>

    Scan every git commit for secrets and injection flaws
    A free tool runs 11 Claude Code CLI agents on each commit to catch secrets, injection flaws, and bad migrations before code lands.
    Done with
    CC
    Claude Code
    CL
    Claude
    What they did
    The creator built Manta as a local git workflow that hooks into each commit and runs 11 Claude Code CLI agents automatically before code reaches the repo. Those agents check for hardcoded secrets, OWASP-style issues like injection and XSS, code quality and async/query problems, and unsafe database migrations; when a commit is blocked, it can suggest fixes, while human review is still needed for complex logic.
    How it went
    The stated result is earlier detection: dangerous commits are blocked before landing, and the tool is free, open source, and runs with Claude Sonnet on the Claude Code free tier. The author also says it is not standalone and adds a few seconds to each commit.
    Worth knowing
    The main catch is that it requires Claude Code CLI and its pre-commit hooks add a few seconds per commit.
    Try it yourself
    with
    Claude Code
    Copy prompt
    Set up a git pre-commit hook in [repo path] that runs Claude Code to review each staged diff for hardcoded secrets, injection flaws (SQL, command, XSS), and risky database migrations. If it finds a problem, block the commit and print the file, line, and a suggested fix. Show me the hook script and test it on a sample bad commit before installing it permanently.
    Original source: https://www.reddit.com/r/codereview/comments/1u6mhos/i_built_a_free_tool_that_runs_11_ai_agents_on

</details>

## 目录转述方法

目录描述由提交触发的Claude Code审查，检查秘密信息、注入风险与迁移。
The directory describes commit-triggered Claude Code reviews for secrets, injection risks and migrations.

来源声称可以阻断并建议修复，复杂逻辑仍需人工审查。
Blocking and fix suggestions are claimed; complex logic still needs human review.

## 结论

原版与现行实现口径不同，缺同版本脚本执行、检出率和实际成本复验，保存证据简报。

## 先纠正版本与费用口径

目录历史原文保持不改，但研究不能把11个智能体与免费Claude层当作当前操作规格。项目当前README有新的总数和分阶段路由，说明实现已经变化；现行模型方案也不支持“装了免费工具就无限免费审查”的推论。源码软件费用、模型费用、网络处理与人工审查是不同项目，必须分别确认。README的示例阻断输出只说明作者如何展示功能，不是本轮实测日志，也不证明每个秘密或缺陷都会被发现。

来源：Sdirectory, Smanta, Sprice

## 付费需求在减少真实风险与返工

使用者是频繁提交代码的开发者，潜在预算方可能是工程或安全负责人。若团队已经有可靠静态规则和人审，仅增加多个模型未必值得付费；若审查积压、迁移事故或泄密风险突出，则可能愿意试点，但本案没有这些客户的采购和续费记录。客户购买的应是可核验的风险发现与交付流程，不是智能体数量。不能以“20比11多”判断效果，更不能从星标和免费开源推出商业收入。

来源：Smanta, Sgitleaks

## 本地挂钩不等于本地模型

工作流可以从本机启动，却仍由云端模型处理代码；是否传输何种内容需按CLI、供应商和配置核查，不能只凭本地二字作隐私承诺。可复制流程应固定被审差异版本、记录扫描是否实际运行、区分错误与真正通过，并将结果关联到文件和规则。研究者建议模型失败、超时、缺权限等状态显式展示，不悄悄当成无问题。当前只读取README，钩子源码目录工具读取失败，因此未判定其真实失败放行策略，也不声称已验证阻断有效。

来源：Smanta, Sbilling, Sgit

## 多层防护不能由一个客户端钩子替代

Git文档表明客户端提交前钩子可阻止一次提交，但它不是组织不可规避的策略执行点。因此本地反馈、服务端推送保护、CI检查和人工审查应按职责组合，而非对客户承诺“危险代码绝不会进入仓库”。本研究不操作任何绕过开关，也不改变分支保护。一个检测结果没有发现问题不等于代码安全，尤其是跨文件授权、业务规则和迁移运行环境；这些需要上下文、人工判断和可重复测试。

来源：Sgit, Spush, Sdirectory

## 先用专用扫描器建立基线

Gitleaks是秘密信息检测的具体原生替代，GitHub推送保护位于另一层；它们不等于全面逻辑审计，但能让团队先知道哪些问题不需要模型。代理的候选增量价值在解释跨文件意图、迁移风险和更难写规则的缺陷，同时要承担误报和漏报。公平比较使用同一组无真实凭据的合成样例，分别记录规则工具和代理的发现、错误定位、误报、漏报、人工处置与延迟。没有这样的对照，不能证明多模型方案优于简单工具。

来源：Sgitleaks, Spush, Smanta

## 单位成本按一次有效检查计算

以下全为研究者假设，不是供应商收费或本案账单。轻量一次检查工具摊销0.1美元、人工0.5分钟按40美元/小时约0.333、其它0.02、获客0.05，单位约0.503；每月1000次加固定维护40，约543.33美元。高误报情景工具0.5、人工3分钟计2、其它0.1、获客0.2，单位2.8；同1000次加维护100，共2900美元。真实售价未知，不计算利润。环境接入、首次规则调试与事故责任成本未量化，须另列而不是当零；一次无效或重复尝试也要计入总成本。平台月费只是参考，不能把每次模型成本固定套为零。

来源：Sprice, Sbilling

## 先卖小范围验证，不卖安全保证

若验证经营机会，可在已有工程服务关系中做一个明确仓库范围的防御性评估包：支持语言和规则、脱敏样例结果、误报处置流程、版本与维护计划。此处没有触达客户、安装软件或扫描真实仓库。客户需要能够撤回接入并理解哪些代码会发送给供应商；日志不应保存真实密钥。经营壁垒更可能来自项目约束、低误报规则和可靠异常处理，而不是把免费工具换品牌。现行项目还有企业版宣传，但没有取得客户、实际价格或合规审计证据，不把“替代多名专家”的文案当交付能力。

来源：Smanta, Sbilling

## 反证与最小验证

本轮反馈检索找到推广和原帖片段，没有独立同版本检出率或延迟验证；不把评论对隐私的质疑当已复现漏洞。应先在临时隔离、无真实秘密的样例仓库离线核对钩子脚本，再在明确授权下测试可识别问题、干净样例、工具超时和失败状态；不能因任务是安全检查就自动取得生产访问或模型上传授权。本研究没有运行这些步骤。若错误被当通过、误报处置成本过高、代码去向不清或结果无法关联具体差异，就停止扩大；不以智能体数、四周或200美元设质量门槛。

来源：Sdirectory, Sgit, Sgitleaks

## 自用与试用

- 能理解安全检查边界并复核发现的开发者。
- 提交前防御性问题提示与审查准备。
- 可能提前发现部分问题，不保证阻止所有漏洞。
- 读脚本、选择模型与数据范围、准备合成验收样例。
- 模型变化、规则误报、钩子升级和失败恢复。
- 随提交和推送高频运行，延迟与限额需核算。
- 差异代码及疑似密钥可能传给模型供应商。
- 漏报、误报、错误被当通过、误认客户端钩子为强制防线。

只含虚构秘密的隔离样例，明确模型与资料传输范围。
可关联差异的发现及失败状态，不是安全认证。

## 来源

- [Sdirectory · 许可目录：Manta提交检查](https://agentusecases.ai/use-case/scan-every-git-commit-for-secrets-and-injection-flaws)：目录转述11智能体、免费层与几秒开销，缺基准、账单和漏洞检出率；保留为历史作者声称。
- [Smanta · Manta当前README](https://github.com/mantacron/manta)：当前说明为20智能体总集合，提交时3个、推送时3至4个按触发分流；模型调用消耗真实tokens，不能沿用旧版每次11个的成本假设。
- [Sprice · Claude当前方案表](https://claude.com/pricing)：现行表将Claude Code列为付费方案能力，Free为No；Pro月付20美元，年付200美元。不能保证原案例免费层说法今天成立。
- [Sbilling · Claude Code订阅与API认证](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)：官方说明设置API密钥时会走API计费而非订阅额度；本轮未读取或修改任何凭据。
- [Sgit · Git钩子说明](https://git-scm.com/docs/githooks)：提交前钩子以非零退出码阻止本次提交，但客户端钩子不是不可绕过的组织级强制控制。
- [Sgitleaks · Gitleaks公开项目](https://github.com/gitleaks/gitleaks)：已有专门秘密信息检测工具，可用于提交钩子或GitHub Actions；本轮只读，不扫描用户文件。
- [Spush · GitHub推送保护](https://docs.github.com/en/code-security/concepts/secret-security/push-protection)：GitHub提供推送时秘密信息保护的原生功能，属于与本地提交检查不同的控制层；不覆盖所有逻辑漏洞。

## 核验边界

原作者全文未读、钩子目录读取工具失败；未安装运行或扫描任何用户仓库，未接触真实秘密、配置权限或调用付费模型。云浏览器13:16首次导航超时，公开说明由Web取得。
