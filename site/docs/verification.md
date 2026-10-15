# 阅读站验收 · 2026-10-15

用户路径：进入深研或目录 → 搜索与筛选 → 阅读报告 → 检查单位经济与来源。应用是纯静态阅读站，不存在运行时 API、数据库或登录步骤。

- 既有 Python 测试：28 项通过；内容契约测试：3 项通过。
- Astro 构建成功：19 篇报告，23 个页面，25 个公开输出文件。
- Playwright：桌面 1440×1000、平板 820×1180、手机 390×844，共 15 项通过。
- 搜索、筛选、排序、重置、URL 状态恢复、目录分页、文章目录、来源锚点、无脚本阅读通过。
- 所有 19 个报告路由返回成功；任务、原始数据、研究运行记录与 Git 路径均未部署。
- 四类页面在三个视口无文档横向溢出；axe WCAG 2 A/AA 与 2.1 AA 扫描未检出违规。
- 已人工查看首页、长文及目录截图；章节编号的对比度问题已修复。截图和机器可读摘要见下方。

[桌面首页](screenshots/desktop-home.png) · [平板首页](screenshots/tablet-home.png) · [手机首页](screenshots/mobile-home.png)

[桌面长文](screenshots/desktop-report.png) · [平板长文](screenshots/tablet-report.png) · [手机长文](screenshots/mobile-report.png)

[桌面目录](screenshots/desktop-catalog.png) · [手机目录](screenshots/mobile-catalog.png) · [机器可读验收记录](verification.json)

可复现命令与部署设置见[阅读站说明](../README.md)。截图仅为本地构建验收，不代表已上线。未验证真实设备 Safari/Firefox；外部来源页面未在本次前端构建中重新抓取。线上域名验收待发布权限明确后执行。
