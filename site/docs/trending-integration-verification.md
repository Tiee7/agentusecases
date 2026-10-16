# 两篇研究整合验收 · 2026-10-16

在已发布的 Cowork 阅读修复 `6096317` 上，串行合并：

- `research/trending-ai-stock-models`：`cb1aacc`（内容 `9c40398`）。
- `translate/wanted-even-batch-01`：`b9effb8`（内容 `489691c`）。

仅 INDEX.md 发生合并冲突，使用 `python -m agentwatch.business index` 从实际内容重新生成总索引与目录。`python -m agentwatch.archive_coverage` 重建覆盖计数，README 与档案说明同步更新。未引入 `feat/wanted-observations` 或临时 slug 排名文件。

最终内容：1,359 个案例、25 篇商业报告、1,359 篇原文、9 篇完整中文译文、1,350 篇待翻译。股票案例已有译文，本次更新保持在同一案例 ID 下，不重复计数。

两篇报告、研究 JSON、来源凭据、档案 JSON 均与原分支逐字节一致；两份研究通过 `agentwatch.business.validate`。Cowork 原文与新译文未被覆盖。65 项 Python 测试、13 项内容测试、Astro 构建、公开输出检查和隔离提示词安全测试通过。输出共 2,749 个文件，未发布原始 JSON、日志、任务文件或缓存。

57 项浏览器测试全部通过。浏览器测试包含两个新案例及 Cowork 的 reports/cases 路由、完整中英文文本、默认开合状态、来源条数、桌面/平板/手机无横向溢出；截图保存在 integration-evidence。生产主域由 main 的 Git 集成自动发布，不修改部署保护设置。

补充检查：旧报告正文的判断短语也在公开阅读投影中统一为通俗表述；原始研究、原文、译文与提示词保持原样。首页可检索文本及报告正文一并覆盖，避免只替换徽标。
