# 在隔离虚拟机中用Claude Code提交PR

## 中文

    在隔离虚拟机中运行Claude Code并创建PR
    作者在受限虚拟机中运行Claude Code，通过Infisical提供密钥。它只能在Forgejo上创建问题和拉取请求；由人手动合并，然后CI部署。
    使用的是
    Claude Code
    他们做了什么
    Claude Code运行在独立虚拟机中，所在VLAN受到严格限制，只能访问互联网、作者的Forgejo实例、Infisical，并允许从作者电脑发起的单向SSH连接。密钥通过Infisical提供，因此agent看不到它们。它的Forgejo用户只能创建问题和拉取请求。作者手动合并后，CI打包并部署到应用服务器虚拟机。
    进展与成效
    来源没有给出量化结果。它称这套配置有些过度，但为了降低个人数据被外传的风险仍然值得。开发模式仍可能在本地暴露部分密钥。
    值得注意
    在本地开发模式中，agent仍可能看到密钥，因此Infisical的保护只有在该模式之外才完全成立。
    亲自尝试
    使用
    Claude Code
    复制提示词
    帮我为在我的项目[仓库名称]上运行你，配置一台锁定权限的虚拟机。只给它所需权限：读取代码、从[密钥管理器]获取密钥，以及在[Git托管平台]创建问题和拉取请求，但不能合并。逐步带我完成配置，最后让它创建一个小型测试拉取请求。执行任何会更改系统或凭据的命令之前，都要暂停并向我展示命令。
    原始来源：https://news.ycombinator.com/item?id=50164831

<details><summary>English original</summary>

    Run Claude Code in an isolated VM that opens PRs
    The author runs Claude Code in a restricted VM with secrets served from Infisical. It can only create issues and PRs on Forgejo, and merges are manual before CI deploys.
    Done with
    CC
    Claude Code
    What they did
    Claude Code runs in its own VM on a heavily restricted VLAN that can reach only the internet, the author's Forgejo instance, Infisical, and one-way SSH from the author's machine. Secrets come through Infisical, so the agent never sees them. Its Forgejo user can only create issues and PRs. The author merges manually, then CI packages and deploys to an app server VM.
    How it went
    The source gives no measured results. It describes the setup as overkill but worth it to cut the risk of personal data exfiltration. Dev mode can still expose some secrets locally.
    Worth knowing
    In local dev mode the agent may still see secrets, so the Infisical protection only fully holds outside that mode.
    Try it yourself
    with
    Claude Code
    Copy prompt
    Help me set up a locked-down virtual machine for running you on my project [repo name]. Give it only the permissions it needs: reading the code, getting secrets from [secrets manager], and opening issues and pull requests on [Git host], with no ability to merge. Walk me through the setup step by step, and finish by having it open a small test pull request. Pause and show me each command that changes my system or credentials before you run it.
    Original source: https://news.ycombinator.com/item?id=50164831

</details>

## 原作者的方法与来源

来源：[HN original discussion](https://news.ycombinator.com/item?id=50164831)

方法摘要未收录

## 简要分析

商业分数未评定。

### 已知流程与未知实现

目录描述的是隔离开发机、有限Git权限、人工合并和CI部署的分层流程，不是已验证的产品。原HN链接两次普通读取失败后停止；作者身份、实际VLAN规则、Infisical接入模式和Forgejo配置均未取得。完整译文忠实保留目录的“看不到密钥”等表述，但它属于来源主张，下文独立核查限制，不把保留原文等同认可绝对安全。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-claude-code-in-an-isolated-vm-that-opens-prs)

### 密钥管理不等于密钥不可见

官方说明运行时注入仍把密钥交给应用进程。由此推断：如果agent能改应用代码或控制含密钥的执行环境，仅移除.env不能保证它无法接触密钥。原案是否用了额外代理、不同系统身份或生产隔离未知，不能据此断言其设置失效，也不能承诺开发模式之外永远安全。验收应采用合成标记和明确身份边界，而不把真实密钥打印到日志。

依据：[Ssecret](https://infisical.com/blog/how-environment-variables-work), [Sdirectory](https://agentusecases.ai/use-case/run-claude-code-in-an-isolated-vm-that-opens-prs)

### 只开PR必须是权限事实

Read与Write的差异直接影响能否合并。建议使用受限身份、独立贡献分支或fork，实际检查目标仓库权限和受保护分支，不把名为bot的普通写账号当只读。这里仅分析权限设计，不创建账号、不配置令牌、不改变本仓库保护。作者所用版本与角色未知，不能照抄一个角色名就称复现成功。

依据：[Spermissions](https://forgejo.org/docs/v17.0/user/collaboration/repo-permissions/)

### 人工合并不是唯一执行关口

PR可能在合并前运行工作流；若机器人已被永久信任或获Actions写权限，风险发生得更早。建议把无生产密钥的检查与受保护部署分开，审批新的代码和工作流差异，并记录具体提交，避免只看PR标题。授权一次与持续信任不同，不能为减少提示无条件扩大权限。源案只说CI在合并后部署，未证明其他触发器不存在。

依据：[Sworkflow](https://forgejo.org/docs/latest/user/actions/security-pull-request/)

### 隔离要覆盖实际进程和出口

内置shell沙箱与整个VM边界不是同一层；在VM内仍应盘点工具、MCP、hooks、共享目录和宿主挂载。目录允许访问互联网，这本身不证明外传被阻断。研究建议列出确需的出口、禁止访问的内网和宿主资源，并测试预期拒绝；具体网络改动仍需审批。单向SSH表述只能作为待核验拓扑，不能自动推导完整网络策略。

依据：[Ssandbox](https://code.claude.com/docs/en/sandboxing), [Sdirectory](https://agentusecases.ai/use-case/run-claude-code-in-an-isolated-vm-that-opens-prs)

### 可能付费的是交付治理而非VM本身

假设目标客户是已有代码审查和持续集成的小团队，需求是缩小自动编码的权限范围，同时保留可检查的PR。潜在交付包括威胁模型、受控模板、验收记录与升级支持；不是出售“绝不会泄密”保证。已有运维能力的团队可能自行配置；无持续开发需求的个人不一定值得承担部署成本。本案没有订单、客户数、报价或收入。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-claude-code-in-an-isolated-vm-that-opens-prs)

### 复制条件和替代方式

可比较现有受限开发容器、公司托管开发机和完整VM。选择取决于要隔离哪些进程、能否限制网络及是否需要宿主集成，不能仅以VM更重判定更安全。复制需要明确OS、软件版本、CI运行器归属、备份/回退、密钥发放身份及人工接管人。源案未给可部署脚本，因此本次交付设计审查简报而非验证过的安装教程。

依据：[Ssandbox](https://code.claude.com/docs/en/sandboxing), [Spermissions](https://forgejo.org/docs/v17.0/user/collaboration/repo-permissions/)

### 获客和交付的可检验单位

假设先向已有开发合作关系的小团队演示自有演示仓库：agent可建PR但不可合并，测试失败不部署，停用访问后不能继续取资源。客户评价应围绕这些验收项及维护工时，不用演示点赞当采购需求。获客渠道和付费意愿未知，本轮没有联系任何第三方。若每客户都要重建网络和CI，业务更接近按项目交付，不能声称天然订阅规模化。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-claude-code-in-an-isolated-vm-that-opens-prs)

### 同范围的两种成本情景

单位是一套演示仓库的隔离配置与验收包，每月4包。研究者低返工假设6h×30USD/h=180人工，加模型预算2，已列182/包、728/月；高返工16h×30=480，加模型6，486/包、1944/月。硬件/VM、密钥服务、持续运维和获客未知另计，不能写零；售价未知不算利润。上述工时并非作者实测，也不是任何产品的当前报价。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-claude-code-in-an-isolated-vm-that-opens-prs)

### 自用收益与维护分别判断

对持续让agent改代码且愿意审查PR的开发者，权限分离可能降低误合并和宿主接触范围；没有数据证明净省时或风险下降比例。首次需梳理资源、搭建测试仓库和验证拒绝场景，后续要维护系统补丁、工具版本、访问撤销和CI策略。使用频率随开发任务，低频用户可能维护负担高于收益。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-claude-code-in-an-isolated-vm-that-opens-prs)

### 只先做无密钥验收计划

使用自有演示仓库与合成数据，先写允许/禁止动作矩阵：读代码、提交PR、拒绝直接合并、拒绝宿主资料、拒绝生产部署。预期得到逐项测试和回退方案，所有真实环境、账号与网络改动在批准后才执行。本轮没有建VM、安装工具、取密钥或进行攻击测试，测试设计不能当真实安全验收。

依据：[Ssandbox](https://code.claude.com/docs/en/sandboxing), [Spermissions](https://forgejo.org/docs/v17.0/user/collaboration/repo-permissions/), [Sworkflow](https://forgejo.org/docs/latest/user/actions/security-pull-request/)

## 自用价值：待核实

分层权限有设计价值，但原案未复验、无净收益测量。

依据：Sdirectory, Ssecret, Spermissions, Ssandbox

- 适用人群：持续使用编码agent且能审查代码/权限的开发者。
- 用途：将代码生成限制在可审查PR工作流。
- 预期收益：可能减少误合并与宿主接触，实际效果未知。
- 设置成本：演示仓库、VM或容器、身份权限、网络与CI验收。
- 维护成本：系统补丁、版本兼容、访问撤销、日志和备份。
- 使用频率：随代码任务；低频需求未必值得复杂维护。
- 隐私风险：运行时密钥、代码、挂载和网络出口可能暴露。
- 错误风险：过宽角色、隐式CI信任、错误部署与虚假安全感。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/run-claude-code-in-an-isolated-vm-that-opens-prs

建议工具：Claude Code

    Help me set up a locked-down virtual machine for running you on my project [repo name]. Give it only the permissions it needs: reading the code, getting secrets from [secrets manager], and opening issues and pull requests on [Git host], with no ability to merge. Walk me through the setup step by step, and finish by having it open a small test pull request. Pause and show me each command that changes my system or credentials before you run it.

自编试用模板

准备条件：自有演示仓库、合成数据、明确不可访问资源与回退要求。

工具：Claude Code、合法可用VM环境及Git托管；均未实际部署。

预期结果：允许/拒绝矩阵与人工审核的配置计划，未实测。

### 源站Copy prompt

原文模板

出处：https://agentusecases.ai/use-case/run-claude-code-in-an-isolated-vm-that-opens-prs

依据：Sdirectory

    Help me set up a locked-down virtual machine for running you on my project [repo name]. Give it only the permissions it needs: reading the code, getting secrets from [secrets manager], and opening issues and pull requests on [Git host], with no ability to merge. Walk me through the setup step by step, and finish by having it open a small test pull request. Pause and show me each command that changes my system or credentials before you run it.

### 无密钥权限验收计划

自编模板

出处：研究团队自编

依据：Spermissions, Sworkflow, Ssandbox

    只为自有演示仓库制定最小权限方案，不执行操作。分别列出读取代码、提交PR、禁止合并、CI检查和部署的身份与权限。说明合成数据验收、失败回退和撤销方法，不索取真实密钥、不创建凭据、不修改网络或生产系统。

## 来源

- [许可目录：隔离虚拟机与人工合并](https://agentusecases.ai/use-case/run-claude-code-in-an-isolated-vm-that-opens-prs)：目录转述VM/VLAN、Forgejo、Infisical及人工合并流程；没有实测结果。
- [Infisical：运行时环境变量](https://infisical.com/blog/how-environment-variables-work)：2026-09-25官方解释运行时注入将密钥放入应用进程环境，避免项目明文文件，但运行时值仍在进程内存/环境；不能将没有.env等同agent永远不可读。
- [Forgejo17：仓库权限](https://forgejo.org/docs/v17.0/user/collaboration/repo-permissions/)：Read可贡献/更新PR但不能直接推送仓库或合并；Write默认可推送和合并。团队可分单元设权限。账号名称或口头约定不能替代实际权限检查。
- [Forgejo：PR工作流信任](https://forgejo.org/docs/latest/user/actions/security-pull-request/)：只读用户发起的相关PR工作流需审批；写权限、Actions写权限、Owner/Admin通常隐式受信任。Approve once不同于永久信任；PR可修改工作流，因此不能把合并权限与执行风险混为一谈。
- [Claude Code：沙箱范围](https://code.claude.com/docs/en/sandboxing)：当前内置沙箱覆盖shell及其子进程，文件工具、MCP和hooks不在同一边界；整体进程可置于容器或VM。默认环境可继承密钥，必须同时考虑文件与网络隔离，不能认为开启sandbox即完整防护。
- [HN原始讨论（未读取）](https://news.ycombinator.com/item?id=50164831)：仅保存原始链接，未核实作者身份、原话、代码或配置；不再换路重试。
