# 源站 Copy prompt 收录修复：真实 DOM 路径验收

2026-10-16 接续独立分支 `fix/source-copy-prompt` 的预验证提交 `7473440`，基线 main `1c66421`。恢复时工作区干净，远端无新变更，最近工作流均已完成、无其他研究进程。认证 Tiee7，有效 Git author/committer 均为 Tiee <tieetheai@gmail.com>。

## 范围与真实来源

两份父任务浏览器取得的最小 DOM 已提取、SQLite 持久化、导出并同步登记表：

| 案例 | DOM观测区间（UTC） | 建议运行工具 | 发布投影 |
|---|---|---|---|
| [电话账单协商](https://agentusecases.ai/use-case/negotiate-retention-discounts-on-bills-by-phone) | 2026-10-15 17:50:39–17:50:47 | Manus | 既有研究记录、报告及独立试用页 |
| [月度交易对账](https://agentusecases.ai/use-case/reconcile-monthly-business-transactions) | 2026-10-15 17:51:24–17:51:37 | Claude Code | 登记表及独立试用页，仍未完成深研 |

时间来源为 system_time_bracketing_tool_call。`observed_at`保留null，使用observation_window保留区间及依据，页面和Markdown同样显示区间，不编造精确秒。打开、点击与DOM读取各阶段区间见 [浏览器来源记录](source-trial-evidence/browser-provenance.json)。

源站建议模板不等于原作者实际使用的提示词；建议工具不等于顶部实际agent。账单页实际agent标签为custom-built or unnamed agent，试用建议是Manus，两者没有混用。源站按钮曾显示Copied，但剪贴板读取为空，因此没有声称源站剪贴板逐字验证。本地站真实剪贴板验证是独立证据。

DOM最小片段位于tests/fixtures/source-trials。原Library ID及先前阻塞情况保留于 [历史预验证](source-trial-evidence/preflight.json)，其“待元数据”状态已由本轮补齐。原始可见截图为 [源站截图](source-trial-evidence/retention-prompt-visible.jpg)。没有取得真实SSR快照；SSR测试仅使用合成fixture，不冒称真实SSR实测，也不阻塞已验证的DOM路径。

## 端到端与兼容

公开SSR按case ID提取tryIt.prompt/agent；DOM fallback严格读取Copy prompt标题行后的提示词段落，不含随后广告。source_trial保存建议工具、完整文本、来源、观测时间或区间、可用状态、提取方式和HTML哈希。旧历史不覆盖新观测；时间区间重叠且新旧不确定时保留已知记录。

SQLite source_trials逐轮存储，爬虫导出source-trials.json；bootstrap同步登记表、已完成研究及报告。保存的浏览器片段通过离线CLI的--db与--apply导入，不执行网络请求、不冒充刷新全站目录。失败、未提取到、未观测分别保留；未提取到不等于源站不存在模板。

阅读站源站模板优先，自编模板补充。新增独立试用页允许尚未深研的目录案例展示模板，同时明确未完成研究。商业评分、自用判断、原有42条自编模板、Wanted及目录映射均未变；仍为21篇完成深研，没有新增案例研究。

## 验证

- Python完整测试：44通过，含真实DOM、合成SSR、特殊字符、失败状态、旧数据库迁移、增量变更、时间区间及持久化同步。
- 内容测试：7通过，含优先展示、旧记录、安全来源及区间精度。
- schema：21篇研究及2份真实观测通过；来源schema通过本地解析注册，不为解析schema访问网络。
- 构建：27页；公开输出白名单29文件、21篇报告及2个试用页，通过。
- 隔离合成安全构建：中英文、引号、HTML/script/img、反引号文本原样显示与复制，无脚本执行。
- Playwright：27通过，三种视口1440×1000、820×1180、390×844；这次真实source_trial循环非空，覆盖两份真实模板、剪贴板逐字往返、源站模板优先、未深研说明、WCAG扫描及无横向溢出。
- git diff --check通过。

机器可读结果见 [最终验证JSON](source-trial-evidence/final-validation.json)。本地截图：[账单桌面](source-trial-evidence/retention-local-desktop.png)、[账单手机](source-trial-evidence/retention-local-mobile.png)、[对账手机](source-trial-evidence/reconcile-local-mobile.png)。已人工查看手机截图，原文、工具、时间区间和按钮可读。

## 发布边界

通过后按授权合并main并推送；最终提交及远端回读由本轮结果报告，不预先声称未发生的推送成功。仅由main既有集成自动部署，不手动部署。没有调用源站/api、没有重试此前取消的curl或本项目线上GET/浏览器验收，没有创建凭据或付费API。未做模型执行效果测试、未操作真实账户；本地成功不代替线上浏览器验收。本轮结束后由父任务以最终UTC完成时间安排至少5分钟休息，不启动下一案例。
