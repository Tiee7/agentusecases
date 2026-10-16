# Cowork 阅读布局验收 · 2026-10-16

基于 e835ecf，限定阅读 UI 与 Cowork 案例全文翻译。未修改其他案例研究或 Wanted 工作分支。

- `/reports/produce-investment-memos-with-claude-cowork/` 与 `/cases/produce-investment-memos-with-claude-cowork/` 共用 SourceArchive，中文全文在前且默认展开，英文默认折叠，可独立展开。
- 中文覆盖已归档源站案例的介绍、方法、结果、注意事项、试用提示词和原始来源链接；不是外部 Substack 全文。原文及其哈希保持不变，译文关联原文哈希并记录自身哈希。
- 空标签不输出标题、占位符或容器；无任何元数据时不输出空 dl。收录时间只在工具信息行显示，桌面靠右，小屏可换行，其他元数据改为紧凑行。
- 公开判断标签使用“建议先小规模试用”等通俗文字；原始研究枚举、评分和事实不变。报告导航标题同步简化，空复制反馈不占位。
- Python 65 项、Node 内容契约 12 项、Astro 构建、公开输出白名单、1359 篇原文和 8 篇译文完整性校验、隔离构建提示词安全测试通过。
- 54 项浏览器测试全部通过。浏览器验收覆盖桌面 1440×1000、平板 820×1180、手机 390×844；两路由检查译文与原文逐字一致、默认开合、空标签 DOM 不存在、收录时间右边缘位置及无横向溢出。

截图见 [桌面报告](cowork-reading-evidence/desktop-cowork-reports.png)、[手机报告](cowork-reading-evidence/mobile-cowork-reports.png)、[桌面案例](cowork-reading-evidence/desktop-cowork-cases.png)、[手机案例](cowork-reading-evidence/mobile-cowork-cases.png)。这些是本地 Chromium 截图，不代表真实设备 Safari 验收。
