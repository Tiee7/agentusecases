# Agent 研读 · 静态阅读站

暖纸色、深墨色与朱红标记的商业研究刊物。提供已完成深研的搜索、商业判断、自用价值独立筛选与排序，独立的全量案例目录，以及包含目录、事实、来源、成本情景和打印排版的长文页。

## 本地使用

从仓库根目录运行，使用 Node.js 24 与 Python 3（浏览器测试的本地静态服务器）：

```sh
npm --prefix site ci --ignore-scripts
npm --prefix site test
ASTRO_TELEMETRY_DISABLED=1 npm --prefix site run build
npm --prefix site run check:output
npm --prefix site exec -- playwright install chromium
npm --prefix site run test:prompt-security
ASTRO_TELEMETRY_DISABLED=1 npm --prefix site run test:e2e
```

开发：`ASTRO_TELEMETRY_DISABLED=1 npm --prefix site run dev`。构建目录为 `site/dist`。页面无需运行时服务、环境秘密、数据库或第三方模型。应用不发送搜索词，不包含分析跟踪、外部字体或登录流程；浏览器仅在用户打开来源链接后访问相应第三方网站。

## 内容契约

构建时读取仓库的 `registry/cases.json` 和固定 ID 对应的 `research/<id>.json`，并检查 `reports/<id>.md` 存在。仅当版本为 2、状态为 completed、ID 与 URL 均匹配时生成研究页。其他案例仅进入目录，标记待研究，链接至公开案例来源。

网站使用结构化记录渲染正文，不另存一套报告，不修改既有研究生成与发布流程。来源引用跳转至同页来源条目。分数按既有七项权重重算，经济表按记录中的输入重算。新增研究提交后，下一次静态构建会自动纳入符合条件的报告。

公开投影只包含阅读字段：标题、行业、日期、结论、分析段落、事实、分数、经济情景、反证、限制、来源及其支持范围、自用价值和可复制试用模板。不会序列化整个原始记录。目录只输出 ID、标题、类别、研究状态与安全 HTTPS 来源。正文保留研究证据边界，但不发布维护文档、任务说明、执行日志、缓存、认证值或原始 JSON 文件。

`check:output` 对实际输出文件做白名单检查。单元测试覆盖状态、身份匹配、缺失报告、路径穿越、URL 协议和额外私有字段；浏览器测试覆盖阅读流程、无脚本阅读、三个视口、全部报告与无障碍扫描。

## Vercel 部署配置（由发布协调方执行）

- 项目根目录：仓库根目录 `.`，**不能只选 `site/`**，因为研究资料位于相邻目录。
- Node.js：24.x。
- Framework Preset：Other；仓库根 `vercel.json` 已明确构建设置。
- Install Command：`npm --prefix site ci --ignore-scripts`。
- Build Command：`ASTRO_TELEMETRY_DISABLED=1 npm --prefix site run build`。
- Output Directory：`site/dist`。
- Production Branch：`main`。无需环境秘密、服务端 adapter、数据库或付费 API。
- Git 集成完成后，main 的内容变更应触发新构建。仅成功构建的 `site/dist` 可部署，不要部署仓库根目录作为静态文件目录。

发布协调方已在用户重新授权后完成生产部署并关联 main 自动发布，详见[2026-10-15 部署回执](docs/deployment-receipt-2026-10-15.md)。已确认 READY 与匿名 HEAD 200；后续完整 GET 和浏览器验收被取消，完整线上验收仍未完成。本地通过不代替线上验收。

## 设计与验证依据

本环境没有 `taste-skill`、`AGENTS.md` 或本地 `.agents/skills`。已阅读可用 Superdesign 技能，因其外部生成流程与当前限制不符而未调用或安装。直接编写前端；应用已读取的 `vercel:verification` 完整阅读流程验证思路。未使用生成图像或假定存在的品牌素材。技术参考为 [Astro 静态路由](https://docs.astro.build/en/guides/routing/)与 [Astro 的 Vercel 静态部署说明](https://docs.astro.build/en/guides/deploy/vercel/)。

## 自用与复制的验证边界

旧v2记录缺少扩展时显示待核实及原文缺失；新发布流程要求填写扩展。提示词通过Astro文本节点转义、通过textContent复制，不插入HTML，不把提示词拼接到脚本。自动复制失败时提供选择文本的手动回退，无脚本时仍可阅读和选择。`test:prompt-security`构建隔离的合成案例，并在仅本地Chromium中检查中英文、HTML攻击文本和剪贴板原样复制。

本轮验收见 [自用价值与提示词验证](docs/personal-value-verification.md)。仅本地浏览器验收；未重试此前取消的线上GET或浏览器验证，未手动重复部署。

## 源站模板收录

源站SSR/DOM建议模板独立保存在source_trial，优先展示，其建议agent不当作案例作者实际工具。两份真实DOM目前分别进入账单协商报告与Reconcile目录试用页；后者没有深研记录，仍标待研究。页面原样呈现时间区间，并保留自编模板作为补充。source_trial的available/missing/unparseable/not_observed分别代表已取得、本次未提取到、解析失败、未观测；后面三者均不证明源站不存在模板。查看[完整验证和边界](docs/source-trial-verification.md)。
