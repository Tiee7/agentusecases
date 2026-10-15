# 阅读站部署回执 · 2026-10-15

本回执依据发布协调方（父任务）提供的 Vercel 插件结果和 HTTP 检查记录整理。文档维护任务未重新查询 Vercel、访问线上站点或主动发起部署。

## 已确认的发布事实

- 用户重新授权使用 `tiee1` 创建项目，关联 `Tiee7/agentusecases`，由 `main` 自动发布；未升级计划。
- Vercel 项目：`prj_eAqx9XXQmUi8TC0xUWqjYV5aTQ5C`。
- 部署：`dpl_Ho5xsm8UtcmEuUR3BZJLHtFoVxET`。
- `get_deployment` 返回状态 `READY`，目标 `production`。
- 部署对应提交：[`452f59cc001c33976b74053a7bafbdb236b1ac77`](https://github.com/Tiee7/agentusecases/commit/452f59cc001c33976b74053a7bafbdb236b1ac77)。
- Node.js：`24.x`。
- 正式别名：[agentusecases-alpha.vercel.app](https://agentusecases-alpha.vercel.app)。
- 发布前 [Reading site checks #38774862327](https://github.com/Tiee7/agentusecases/actions/runs/38774862327) 成功；该 CI 对应研究提交 `f3a5f2794761d3c7c2ae6f285d8426e84056c04d`。随后部署提交只新增远端研究验收记录。
- 发布前内容规模：21 篇报告、25 个静态页面、1334 个登记案例。相关本地构建和浏览器检查记录见[本轮验证](../../research/runs/2026-10-15-parking-appeal/site-validation.json)。这些数字描述发布前构建，未通过线上完整页面遍历重新计数。

## 线上检查范围与未完成项

发布协调方报告匿名 `HEAD` 请求返回 `200`、`Content-Type: text/html`，响应记录显示长度 `271963` bytes，且没有登录重定向。`HEAD` 不读取完整响应正文，该结果不等同于验证实际下载了相同长度的 HTML，也不证明所有报告路由和页面交互正常。

后续完整 `GET` 和浏览器验收工具被取消，未重试。因此**完整线上验收尚未完成**，不能声称线上手机阅读、搜索筛选、全部报告路由、来源链接或浏览器可访问性检查已通过。本地与 CI 的通过结果不能替代这些线上检查。

本次仅将非敏感回执保存到 Git，未变更保护设置、创建凭据或额外服务。此文档提交到 `main` 后可能由既有 Git 集成触发自动构建；其新部署状态由发布协调方另行检查，本回执中的 `READY` 仅指上述部署 ID。
