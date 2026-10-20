# cgroup案例来源核验

实际读取2026-10-20 06:32:38–06:33:04 UTC。
- 自有云浏览器读取许可目录 https://agentusecases.ai/use-case/run-each-coding-agent-session-in-a-cgroup-that-is-killed-on- ，现有正文一致。作者据目录转述定位tmpfs /tmp和agent遗留进程，按会话cgroup结束清理，约两小时未使用且无打开句柄的tmp文件清理；没有前后数字。
- 原HN https://news.ycombinator.com/item?id=50136354 公开web普通失败两次（06:32:48–06:32:58），已停该来源，无镜像/第三次/搜索摘要替代。
- https://docs.kernel.org/admin-guide/cgroup-v2.html 已读：子进程默认继承父所在cgroup，之后移动父不带走既有子孙。cgroup.kill杀整个子树，SIGKILL，处理并发fork与迁移；threaded cgroup不支持该接口。cgroup是进程/资源机制，不应称完整安全沙箱。
- https://docs.kernel.org/filesystems/tmpfs.html 已读：tmpfs页可在允许swap时换出，不是物理RAM永远不落盘；/tmp是否tmpfs需实查，不可泛化。
- https://www.freedesktop.org/software/systemd/man/latest/systemd.kill.html 已读：KillMode=control-group默认，unit stop清理剩余进程，通常TERM后超时KILL；process只主进程不足。不能把建立cgroup本身当任务结束自动stop的保证。
- https://www.freedesktop.org/software/systemd/man/latest/tmpfiles.d.html 已读Age：按多种时间戳决定老化，锁定文件/目录可跳过；BSD flock检查并不等于枚举全部打开句柄，不能把该现成工具误写为复现作者筛选语义。扫描无句柄与删除之间仍可能变化（研究推断），应范围隔离/应用协作，而非全局/tmp冒险删除。

本轮只研究；未kill任何进程、删除任何tmp文件、修改cgroup/系统权限/调度或运行真实试用。本轮形成单独简报，验证及真实完成记录另存。
