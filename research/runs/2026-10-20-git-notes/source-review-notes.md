# Git笔记案例来源核验记录

2026-10-20 06:22:21–06:22:52 UTC。

- 自有云浏览器已读许可目录 https://agentusecases.ai/use-case/save-ai-q-a-summaries-into-git-repos-as-persistent-notes ，ChatGPT/GitHub MCP/三四个repo/AGENTS.md链接讨论与决定文件；“比内置记忆可靠”只是作者经目录转述，无量化失败或收益。
- 原HN https://news.ycombinator.com/item?id=50128580 经公开网页工具06:22:27及06:22:31两次普通读取失败（不可访问/InternalError），已停止，不镜像、不第三次、不以搜索摘要冒充原文。
- https://github.com/github/github-mcp-server 官方README读取：允许选择工具和toolsets、read-only模式跳过写工具，工具组可叠加；当前能力不证明当时作者配置，也不证明任何ChatGPT会自动读取AGENTS.md。MCP提供工具与存储通路，不保证摘要正确或未来会话自动检索。
- https://docs.github.com/en/rest/repos/contents 已读取；文件更新带sha，创建/更新与删除并行会冲突，串行写入并读最新版本再核差异；不覆盖其他工作。尚未独立实际试用本案例。
- https://git-scm.com/docs/git-revert 已读：用新提交逆转旧改动；历史仍保留。推断：纠正错误摘要有版本依据，但撤回正文不等于清除历史中的敏感内容，因此一开始不应提交私密通信/凭据。

本轮形成单独简报，验证与真实完成记录另存。本轮未建新MCP、凭据、权限或额外仓库，不复制外链长文。
