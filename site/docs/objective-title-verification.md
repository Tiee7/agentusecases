# 客观用途标题验收 · 2026-10-16

基线：`7bf722d6c57ad15b71c2b3f32908d5185f0c2f39`。本站 28 篇研究统一为 agent＋具体动作＋任务对象的标题；完整前后对照见 [28 项修改清单](objective-title-changes.json)。案例总数 1,359、研究数 28、完整译文数 12 均未变化。

覆盖结构化研究 `title`、Markdown H1、首页卡片、目录、reports/cases/trials H1、HTML title、总索引与目录索引。报告 H1 改为同一编辑标题，不再另取源站标题。源站登记标题、原始归档、译文、来源引用标题、slug 和链接保持不变。逐项比对确认研究 JSON 除 title 外无变化，Markdown 除首行外无变化；评分、评价、事实和正文分析均保留。

`schemas/editorial-title-policy.json` 定义客观动作开头与已知评价短语规则，`agentwatch.titles` 在发布与报告生成时校验。两份生成模板、研究流程、定时任务流程和研究标准已更新；关键词校验之外仍要求编辑检查语义，不能通过绕开关键词将结论塞入标题。

验证：Python 69 项；Node 内容契约 14 项；Astro 静态构建；公开输出白名单；全部 28 个编辑案例跨路由 H1/SEO/卡片一致性；1,359 篇原文、12 篇译文与源站模板完整性；隔离提示词安全测试。60 项浏览器测试全部通过。浏览器覆盖桌面 1440×1000、平板 820×1180、手机 390×844，包含首页、目录搜索、reports/cases/trials 标题、正文评价保留和无横向溢出。

仅本地 Chromium 页面验证。正式域名此前存在 `ERR_CERT_AUTHORITY_INVALID`，本次没有访问、重试或绕过证书警告；线上页面验收未做，等待独立验收。Vercel 仅通过管理 API 核对现有项目与部署状态，READY 不等于正式域名证书或用户阅读路径验收通过。

本地视觉复核：[桌面卡片](objective-title-evidence/desktop-objective-titles-cards.png) · [手机卡片](objective-title-evidence/mobile-objective-titles-cards.png) · [桌面报告](objective-title-evidence/desktop-objective-titles-report.png) · [手机报告](objective-title-evidence/mobile-objective-titles-report.png)。补拍截图的 3 项定向测试亦通过。
