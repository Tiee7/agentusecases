# 让编程智能体通过 SSH 在远程 WSL 运行构建测试

## 中文

    在远程Windows虚拟机上运行智能体构建和测试
    一位开发者给编程智能体提供远程Windows虚拟机中WSL实例的SSH访问，让它们在那里构建和测试，而不是在自己的Mac笔记本上运行。
    使用的是
    Codex
    他们做了什么
    开发者的雇主提供Mac笔记本和远程Windows虚拟机。智能体通过SSH访问这些虚拟机中的WSL实例，在那里运行构建和测试。配置较临时：智能体需要拉取最新代码，或由开发者维护每台机器上的主工作副本。
    进展与成效
    构建不再占用Mac，因此后台智能体不再导致会议视频流掉线。开发者对此满意，但认为目前只是够用。
    值得注意
    虚拟机代码同步仍是手动的；开发者正在考虑用容器或GitHub Actions让流程更整洁。
    亲自尝试
    使用Codex
    复制提示词
    我在[Mac/Linux]机器的[项目文件夹]中工作，但构建和测试必须在远程Windows机器上运行。你可以通过SSH连接[user@host]，并使用那里的WSL。把代码同步到[远程路径]，通过SSH运行[构建命令]和[测试命令]，报告通过与失败的测试及相关错误输出。不要删除或覆盖远程机器上[远程路径]之外的内容；如果某命令会这样做，运行前先展示给我。
    原始来源：https://news.ycombinator.com/item?id=50137976

<details><summary>English original</summary>

    Run agent builds and tests on remote Windows VMs
    A developer gives coding agents ssh access to WSL instances on remote Windows VMs to run builds and tests instead of on their Mac laptop.
    Done with
    CX
    Codex
    What they did
    The developer's employer supplies a Mac laptop plus remote Windows VMs. The agents get ssh access to WSL instances on those VMs and run their builds and tests there. Setup is ad hoc: agents have to pull the latest code, or the developer keeps the main enlistment current on each machine.
    How it went
    Builds no longer run on the Mac, so background agents stop causing video streams to drop during meetings. The developer is happy with it, though the setup is only good enough for now.
    Worth knowing
    Keeping code in sync on the VMs is manual; the developer is considering containers or GitHub Actions to make it cleaner.
    Try it yourself
    with
    Codex
    Copy prompt
    I'm working in [project folder] on my [Mac/Linux] machine, but builds and tests must run on a remote Windows machine. You can reach it with ssh at [user@host] and use WSL there. Sync the code to [remote path], run [build command] and [test command] over ssh, and report which tests passed and failed with the relevant error output. Do not delete or overwrite anything on the remote machine outside [remote path], and show me any command that would do so before running it.
    Original source: https://news.ycombinator.com/item?id=50137976

</details>

## 原作者的方法与来源

https://news.ycombinator.com/item?id=50137976

The commenter moves agent builds and tests from a Mac to employer-provided remote WSL instances over SSH.
评论者通过SSH把智能体构建测试从Mac移到雇主提供的远程WSL实例。

Code synchronization remains ad hoc; improved meeting-video behavior is self-reported.
代码同步仍较临时，会议视频体验改善为作者自述。

## 简要分析

商业分数未评定。

### 一条有效使用线索，缺完整工程记录

bentcorner说明雇主提供Mac与远程Windows VM，自己把智能体构建测试移到WSL。评论没有仓库、语言、构建命令、VM配置或耗时对照，不能据此得出速度更快或成本更低。减少会议视频干扰是作者体验，不是受控CPU或网络测量。目录标Codex，评论本身泛称agents；保留目录标签，不补造具体版本和模型。

依据：[Sauthor](https://news.ycombinator.com/item?id=50137976), [Sdirectory](https://agentusecases.ai/use-case/run-agent-builds-and-tests-on-remote-windows-vms)

### 宿主Windows和测试目标必须分开

SSH进入WSL后，通常执行的是Linux环境中的工具；除非明确调用Windows工具链并验证产物，不能把通过的结果称为原生Windows兼容性测试。WSL2有Linux内核，原评论也没说WSL版本。下一步应先记录目标操作系统、CPU架构、编译器和实际可执行文件格式，避免把“跑在Windows机器里”误当平台验收。

依据：[Swsl](https://learn.microsoft.com/en-us/windows/wsl/compare-versions), [Sauthor](https://news.ycombinator.com/item?id=50137976)

### 拉取最新不等于测试正确版本

作者承认同步仍较临时，这是最关键的复制缺口。建议每次任务绑定明确commit和任务ID，远端使用独立工作目录并回报实际HEAD、工作树差异和测试命令。只运行git pull可能测到别人后来提交的版本，也可能漏掉本地未提交改动。这些是研究者拟议改进，未确认作者已有锁或版本绑定；不把主工作副本共享给多个写者当安全并行。

依据：[Sauthor](https://news.ycombinator.com/item?id=50137976)

### 回执比一句通过更重要

远程命令成功退出只证明进程结束，未必覆盖预期测试。拟议回执应含代码标识、平台、开始结束时间、完整命令、退出码及实际测试数量；失败保留必要错误信息但避免凭据。断连后先查询原任务是否还在跑，再决定重试，防止重复构建占满远端。日志与产物绑定同一任务，不能拿上次成功报告当这次结果。

依据：[Srunner](https://docs.github.com/en/actions/concepts/runners/github-hosted-runners)

### 先比较已有CI和现有机器

GitHub托管运行器可承担按提交触发的验证，也提供不同操作系统。交互式远程机器适合临时调试，标准CI更便于固定流程和记录，两者并不互斥。当前价目表按不同SKU计费并逐作业取整，不能只看任务持续几秒就按小数秒估价。作者使用雇主已提供VM，其新增现金成本未知，因此不能推断租云机器必然省钱或值得售卖托管服务。

依据：[Srunner](https://docs.github.com/en/actions/concepts/runners/github-hosted-runners), [Sprice](https://docs.github.com/en/billing/reference/actions-runner-pricing)

### 自用价值先于独立商业模式

明确价值是减少工作笔记本资源竞争，尤其会议与后台编译同时发生时。潜在服务可包括构建环境整理、回执规范与维护，但现成CI和内部IT已有替代。没有真实采购、维护工时、并发量或利用率，无法给有依据的利润模型；本例保持未评分简报。只想让电脑不卡的人未必需要购买一个完整agent平台。

依据：[Sauthor](https://news.ycombinator.com/item?id=50137976), [Srunner](https://docs.github.com/en/actions/concepts/runners/github-hosted-runners)

### 远程访问不是无限机器权限

研究阶段没有连接SSH、创建密钥或改防火墙。未来若实施，须明确获准机器、路径、命令与任务范围，使用已有合适权限；不能把提示词中的路径约束当操作系统隔离。构建脚本与依赖本身会执行代码，读取项目文件不代表它们可授权外发秘密。日志需检查敏感信息，不能依赖自动遮罩一定成功。

依据：[Ssecurity](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)

### 补一份可复核任务记录即可提升判断

优先拿到脱敏的单次任务：源commit、WSL版本、目标平台、命令、退出码及产物。不需要先搭建复杂调度。可先设计两个不同commit的合成回执，检查混用时是否被拒绝；本轮未执行该测试。若主要痛点通过限制本地并发就能解决，远程迁移未必划算；如果同步和维护成本高于减少的干扰，也应保留较简单方案。

依据：[Sauthor](https://news.ycombinator.com/item?id=50137976), [Swsl](https://learn.microsoft.com/en-us/windows/wsl/compare-versions)

## 试用准备与预期结果

合成任务记录与虚构路径，不含主机地址或密钥。
识别版本或平台不一致，列缺项，不把未知写成测试通过。

检查这两份虚构构建记录的任务ID、源commit、远端HEAD、操作系统架构、命令退出码和产物。版本不一致或平台目标不符就标未验证，不连接机器、不运行命令。

## 来源

- [许可目录](https://agentusecases.ai/use-case/run-agent-builds-and-tests-on-remote-windows-vms)：保留Codex标签、SSH到WSL方法及原始提示词。
- [bentcorner HN公开评论](https://news.ycombinator.com/item?id=50137976)：评论自述会议视频干扰减少，配置临时且同步仍手动，未给性能基准。
- [Microsoft WSL说明](https://learn.microsoft.com/en-us/windows/wsl/compare-versions)：WSL2运行Linux内核，宿主Windows不自动等于原生Windows测试。
- [GitHub托管运行器](https://docs.github.com/en/actions/concepts/runners/github-hosted-runners)：有Linux、Windows与macOS运行器，环境映像和工作日志可追溯。
- [GitHub运行器价格](https://docs.github.com/en/billing/reference/actions-runner-pricing)：当前基准Linux2核x64为0.006美元每分钟、Windows2核x64为0.010，并逐作业向上取整；不是作者实际账单。
- [GitHub安全实践](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)：最小权限和日志敏感信息检查适用于拟议CI方案，不能证明原SSH配置安全。
