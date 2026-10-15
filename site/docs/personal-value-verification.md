# 自用价值与 Copy prompt 本地验证

2026-10-15，基线 main `9fbcf32`，独立分支 `feat/personal-value-prompts`。开始时远端仅有 main，最近8个工作流均 completed，本地没有研究进程或未提交修改。GitHub 认证 Tiee7，有效 Git author/committer 均为 `Tiee <tieetheai@gmail.com>`。

## 数据与范围

21篇旧研究仅增加 personal_value 与 try_it；逐字段比较确认所有既有内容、来源、时间戳及商业评分未改。登记表、Wanted及票数未改。本轮没有新研究，没有读取源站或源站API，没有重试被取消的线上GET/浏览器检查。

自用评级为研究者对限定辅助用途的定性判断（20中、1低），不能外推为实测收益。所有21篇明确标为未提取核验源站提示词；42条中英文模板均为我们编写、未做模型实测，不冒充原文或原产品执行日志。

## 验证结果

- `python -m unittest discover -s tests -q`：33通过，含21篇凭据及引用校验、旧记录兼容、新发布必填校验。
- `npm --prefix site test`：5通过，含独立评分、缺失值兼容与提示词投影。
- JSON Schema Draft 2020-12：schema自身有效，21篇均通过；旧字段与基线完全一致。
- `ASTRO_TELEMETRY_DISABLED=1 npm --prefix site run build`：25个页面构建成功。
- `npm --prefix site run check:output`：27个公开文件、21篇报告，白名单通过；未输出原始JSON、日志、任务文件或缓存。
- `npm --prefix site run test:prompt-security`：隔离的合成案例实际构建并由本地Chromium读取；中文、英文、引号、反引号、script/img注入文本保持字面文本，复制完全一致且无脚本执行。
- `npm --prefix site run test:e2e`：24通过，桌面1440×1000、平板820×1180、手机390×844。涵盖独立筛选组合与URL状态恢复、原有搜索排序、全报告路由、无JS阅读、无横向溢出、WCAG扫描、中英文真实剪贴板读取验证、拒绝剪贴板后的手动选择回退。
- `git diff --check`：通过。依赖安装使用临时目录缓存及禁用Astro遥测，未申请提权。

机器可读结果见 [验证JSON](personal-value-verification.json)。本地截图：[自用价值](screenshots/personal-value-desktop.png)、[桌面提示词](screenshots/prompt-desktop.png)、[手机提示词](screenshots/prompt-mobile.png)、[手机独立筛选](screenshots/personal-filter-mobile.png)。人工查看了桌面自用区与手机提示词、筛选截图，文字及按钮可读。

## 发布与流程边界

验证完成后按用户授权合并并推送main，最终SHA及远端回读由本轮返回结果报告；此文件不预先宣称尚未发生的推送成功。仅由既有main集成触发自动部署，不手动重复Vercel部署。本地通过不代表线上GET或浏览器验收完成。

流程已要求全局串行互斥、记录最终completed_at与resume_not_before（加5分钟）。父任务负责调度与全局运行权；本轮不创建锁服务、不启动下一轮研究，也不声称已经等待完下一轮的冷却期。
