# 用cgroup管理编码agent会话并清理遗留进程

## 中文

    让每次编码agent会话运行在完成后会被终止的cgroup中
    一位开发者制作了agent启动器，让每次编码agent会话在独立cgroup中运行，并在任务完成时终止遗留进程；另外还设置了清理过期tmp文件的任务。
    使用的是
    CX
    Codex
    他们做了什么
    开发者发现，大量交换空间使用来自基于内存的tmpfs /tmp，以及早先编码agent派生后遗留的进程。他们增加了一个频繁执行的任务，删除约两小时未使用、且没有任何命令持有打开句柄的tmp文件。他们还让agent启动器把每次会话放进独立cgroup，任务结束时终止其中所有进程。
    进展与成效
    来源没有给出测量数据。它称清理任务和每会话cgroup解决了交换空间占用及遗留进程问题，但只是简短论坛评论，没有前后对比数字。
    值得了解
    先确认交换空间占用是否真的来自基于内存的tmpfs /tmp，再判断是否由agent导致；清理任务只删除没有打开句柄的文件。
    亲自尝试
    使用
    Codex
    复制提示词
    在我的仓库[路径]中，为[Linux发行版或systemd环境]编写一个小型agent启动脚本，让每次编码agent会话在独立cgroup中运行，并在任务完成或失败时终止该cgroup中所有遗留进程。另外增加一个定时任务，删除[tmp目录]中超过[小时数]的过期文件。最后运行一次会留下后台进程的测试会话，向我展示它被清理。在删除任何文件或终止测试以外的进程之前，先展示将处理的对象，并等待我的批准。
    原始来源：https://news.ycombinator.com/item?id=50136354

<details><summary>English original</summary>

    Run each coding agent session in a cgroup that is killed on completion
    A developer built an agent spawner that launches each coding agent session in its own cgroup and kills leftover processes when the task completes, plus a job that clears stale tmp files.
    Done with
    CX
    Codex
    What they did
    The developer traced heavy swapping to a RAM-backed tmpfs /tmp and to processes that earlier coding agents had forked and abandoned. They added a frequently run job that deletes tmp files unused for about two hours and not held open by any command. They also built their agent spawner to launch each session in its own cgroup, killing every process in it when the task finishes.
    How it went
    The source gives no measurements. It says the cleanup job and per-session cgroups addressed the swap usage and the leftover processes, but it is a brief forum comment with no before-and-after figures.
    Worth knowing
    Check whether swap is really coming from a RAM-backed tmpfs /tmp before blaming the agents; the cleanup job only removes files with no open handles.
    Try it yourself
    with
    Codex
    Copy prompt
    In my repo at [path], write a small agent spawner script for [Linux distro or systemd setup] that launches each coding agent session in its own cgroup and kills every leftover process in that cgroup when the task finishes or fails. Also add a scheduled job that deletes stale files older than [number] hours in [tmp directory]. Finish by running a test session that leaves a background process behind and showing me that it gets cleaned up. Before deleting any files or killing processes outside the test, show me what would be removed and wait for my approval.
    Original source: https://news.ycombinator.com/item?id=50136354

</details>


## 原作者的方法与来源

来源：[HN coding session cleanup comment](https://news.ycombinator.com/item?id=50136354)

方法摘要未收录

## 简要分析

商业分数未评定；本篇不计完整深研。

### 需求与付款人

并行或长期编码任务可能遗留进程、临时文件，影响开发机器可用性。潜在人群是开发者和运维团队；当前只有单个自述，无故障率、损失或付费意向。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-each-coding-agent-session-in-a-cgroup-that-is-killed-on-)

### 交付与收入机制

可设想交付会话启动、结束清理、资源记录与异常恢复的工具或内部规范。收费配置/维护是假设；系统本来具备进程组管理能力，不能把包装脚本当独占壁垒。

依据：[Scgroup](https://docs.kernel.org/admin-guide/cgroup-v2.html), [Skill](https://www.freedesktop.org/software/systemd/man/latest/systemd.kill.html)

### 验证与获客

先确认机器确实存在该问题，再用隔离测试会话验证正常退出、失败和超时后遗留进程是否归零；记录前后内存、swap和临时目录大小。本轮没有获客、用户机器检查或运行试验。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-each-coding-agent-session-in-a-cgroup-that-is-killed-on-)

### 先区分原因

tmpfs可以在允许时使用swap，不应称全部固定在物理内存。目录名称/tmp不能证明挂载类型。进程RSS、共享内存与临时文件分别观察，不能把所有swap增长归因于模型或agent。

依据：[Stmpfs](https://docs.kernel.org/filesystems/tmpfs.html)

### 进程生命周期

应在派生进程之前建立会话归属；仅事后移动父进程可能遗漏已有子孙。cgroup本身不是任务结束通知，启动器还需在完成、失败等出口触发stop并核组内状态。cgroup是资源/生命周期机制，不等于完整安全沙箱。

依据：[Scgroup](https://docs.kernel.org/admin-guide/cgroup-v2.html), [Skill](https://www.freedesktop.org/software/systemd/man/latest/systemd.kill.html)

### 文件清理边界

作者的无打开句柄筛选仅来自转述。systemd-tmpfiles的时间戳和BSD锁机制不等价。扫描与删除之间可能变化，且老文件未必无价值；优先会话专属目录、保留清单和明确边界，不直接清空全局/tmp。

依据：[Stmpfiles](https://www.freedesktop.org/software/systemd/man/latest/tmpfiles.d.html), [Sdirectory](https://agentusecases.ai/use-case/run-each-coding-agent-session-in-a-cgroup-that-is-killed-on-)

### 成本与替代

现成systemd生命周期和tmpfiles提供基础能力；成本在发行版/版本差异、权限、异常路径和误删责任。无测量及工时不能给虚构节省或利润。适合先内部可靠性改进而非独立产品定价。

依据：[Skill](https://www.freedesktop.org/software/systemd/man/latest/systemd.kill.html), [Stmpfiles](https://www.freedesktop.org/software/systemd/man/latest/tmpfiles.d.html)

### 独立自用价值

适合确认有遗留进程问题的Linux编码用户。设置会话标识、目录和结束规则，维护版本兼容与故障日志；按会话发生，清理频率由工作量决定。作者约两小时并非所有人通用阈值，无实测净收益。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-each-coding-agent-session-in-a-cgroup-that-is-killed-on-)

### 隐私与错误风险

错误组路径可能终止无关任务，强制终止可能丢失未保存输出，错误目录范围会误删文件。日志也可能含代码路径和秘密；只保留必要元数据。不得扩大系统权限以方便清理。

依据：[Scgroup](https://docs.kernel.org/admin-guide/cgroup-v2.html), [Stmpfiles](https://www.freedesktop.org/software/systemd/man/latest/tmpfiles.d.html)

### 结论与下一步

适合内部效率工具。先制定隔离测试清单与只展示候选对象的干运行，再单独取得实际清理许可；本轮未运行。如果无法可靠确定进程和文件归属，停止自动清理。

依据：[Sdirectory](https://agentusecases.ai/use-case/run-each-coding-agent-session-in-a-cgroup-that-is-killed-on-), [Skill](https://www.freedesktop.org/software/systemd/man/latest/systemd.kill.html)

## 试用准备与预期结果

虚构会话树与目录清单；所有真实清理须单独授权。
明确哪些对象属于会话、哪些须保留及异常恢复；本轮未运行。
只根据给定虚构进程树与目录清单制定验收，区分正常结束、失败、子进程脱离和仍被使用文件。不杀进程、不删文件、不挂载、不改权限或创建调度；列出预期保留与待确认对象。

## 来源

- [许可目录编码会话清理案例](https://agentusecases.ai/use-case/run-each-coding-agent-session-in-a-cgroup-that-is-killed-on-)：每会话cgroup清理和约两小时无句柄临时文件清理；成效为转述，无前后测量。
- [Linux cgroup v2官方文档](https://docs.kernel.org/admin-guide/cgroup-v2.html)：子进程继承当时父cgroup，移动父不自动移动已有子孙；cgroup.kill对子树SIGKILL并处理并发fork，threaded组不支持。
- [Linux tmpfs官方文档](https://docs.kernel.org/filesystems/tmpfs.html)：tmpfs存虚拟内存，允许swap时页可换出；/tmp挂载类型不能凭名称推断。
- [systemd进程终止语义](https://www.freedesktop.org/software/systemd/man/latest/systemd.kill.html)：KillMode=control-group在unit stop时处理组内进程，默认先TERM再按超时等条件KILL；只主进程模式不足以管理遗留子进程。
- [systemd临时文件老化](https://www.freedesktop.org/software/systemd/man/latest/tmpfiles.d.html)：Age依据时间戳组合；清理会检查BSD文件锁并跳过已有锁的路径；锁检查不是全部打开句柄检测。
