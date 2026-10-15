# 源站试用模板收录修复：预验证

独立分支 `fix/source-copy-prompt`，基线main `1c66421`。认证Tiee7，作者与提交者Tiee <tieetheai@gmail.com>。未启动新研究、未修改调度或Wanted。

## 已验证

- 公开SSR的tryIt.prompt/agent提取，按case ID隔离相关案例；SSR不可用时读取真实DOM卡片的标题行后第一提示词段落，排除广告。
- 建立独立source_trial观测，记录建议运行工具、文本、来源URL、观测时间、状态及HTML哈希；不将它当成案例实际agent或原作者真实提示词。
- SQLite迁移、逐轮存储、source-trials.json导出、registry同步、已完成research及Markdown同步；未研究案例不新建完成记录。旧历史不能覆盖新观测，新的缺失/失败状态不会静默复用旧文本。
- 阅读站源站模板优先，自编模板保留为补充；目录提供独立试用页。特殊字符通过文本节点转义和textContent复制。
- 42项Python测试、6项内容测试、27项本地浏览器回归通过；构建及公开文件白名单通过。隔离合成站点同时验证报告和独立试用页的注入文本不会执行、复制内容逐字一致。

## 实际fixture证据

父任务提供Library原ID：账单DOM `libfile_23fb134470788191ab2ee9a37549726b`；Reconcile DOM `libfile_8e13686593348191a2023ee84144d13f`；可见模板截图 `libfile_9d1a06c2afe081919e2a480d86989008`。本环境通过Library物化、核对字节数并读取像素；DOM最小片段保存于tests/fixtures/source-trials，截图保存于source-trial-evidence/retention-prompt-visible.jpg。

两DOM均实际提取完整提示词，建议工具分别Manus和Claude Code，未混入Vibe Coding Academy广告。父任务报告源站按钮从Copy prompt变为Copied，但剪贴板读取为空；不声称源站剪贴板内容逐字校验。截图显示源站提示词区域及Copy prompt按钮。

## 未完成部分

收到的HTML实际仅包含卡片，没有来源URL或观测时间。账单页URL已由父任务明确给出，Reconcile确切URL与两页观测时间仍待补充；实际SSR片段也待提供。未猜测来源或用导入时间冒充网页观测时间，尚未将两样本写入registry/research，真实样本的阅读站端到端验收也尚未完成。当前浏览器回归中的真实source_trial循环为空；已用隔离合成source_trial覆盖新路由与优先展示。

待父任务补齐元数据后，使用离线导入命令的`--db`与`--apply`完成持久化和发布投影，重新构建、检查真实模板复制与页面，再合并main推送并回读。没有调用源站/api、没有重试取消curl或本项目线上GET/浏览器验证，没有新凭据、付费API或手动部署。
