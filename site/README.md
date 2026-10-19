# Agent 研读 · 静态阅读站

暖纸色、深墨色与朱红标记的商业研究刊物。提供完整深研与简报的独立入口、搜索和筛选，全量案例目录，以及包含目录、事实、来源、成本情景和打印排版的阅读页。

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

构建时读取仓库的 `registry/cases.json` 和固定 ID 对应的 `research/<id>.json`，并检查 `reports/<id>.md` 存在。仅当版本为 2、状态为 completed、ID 与 URL 均匹配时生成研究页。同时读取 `research/brief/<id>.json`，要求 schema_version=1、analysis_depth=brief、status=completed、ID/URL匹配登记项且 `reports/brief/<id>.md` 存在，生成独立 `/briefs/<id>/` 阅读页。目录区分已完成深研、已完成简报和待研究；同ID符合深研条件时优先深研，不重复计数。

网站使用结构化记录渲染正文，不另存一套报告，不修改既有研究生成与发布流程。来源引用跳转至同页来源条目。深研分数按既有七项权重重算；简报不设总分，独立评分扩展仅展示已有维度与理由，不换算为深研分数。经济表按记录输入重算，简报缺失或null数值显示待核实，不补零；实际现金预付与按月固定费用分列。新增研究提交后，下一次静态构建会自动纳入符合条件的报告。

公开投影只包含阅读字段：标题、行业、日期、结论、分析段落、事实、分数、经济情景、反证、限制、来源及其支持范围、自用价值和可复制试用模板。不会序列化整个原始记录。目录只输出 ID、标题、类别、研究状态与安全 HTTPS 来源。正文保留研究证据边界，但不发布维护文档、任务说明、执行日志、缓存、认证值或原始 JSON 文件。

`check:output` 对实际输出文件做白名单检查。单元测试覆盖状态、身份匹配、缺失报告、路径穿越、URL 协议和额外私有字段；浏览器测试覆盖阅读流程、无脚本阅读、三个视口、全部报告与无障碍扫描。

## 简报路由与回归

- `/briefs/`：全部有效简报，可搜索并按商业判断、自用价值筛选；计数直接来自内容投影。
- `/briefs/<id>/`：复用深研阅读组件。完整译文中文默认展开、英文折叠，方法摘要、事实归属、分析、成本、来源和模板单独呈现。未读/受限来源明确标记；归档转述不冒充原作者说明。
- 首页保持深研计数独立，并提供简报计数入口；目录按三种互斥状态筛选，案例页和源站试用页均可跳转已有简报。
- 全部正文来自JSON投影，Markdown仅作为已完成交付配对条件，不解析五种历史Markdown版式，也不另存一份内容。爬虫、登记表和研究记录不因网站功能改变。
- `check:output` 核全部简报路由、内链、标题、三态计数和来源锚点；原文/译文逐字检查覆盖案例、深研及简报副本。合成恶意输入的真实浏览器安全回归也覆盖简报分析、事实、来源、方法及复制模板。
- 既有取消的线上验收属于历史记录；2026-10-19本次用户已另行授权网站简报功能与上线验收。本原生环境浏览器进程启动受限，不重试绕过；完整浏览器套件通过既有GitHub CI验证，生产站再由助手自己的云浏览器只读验收。

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

## 案例发现与自动同步（2026-10-16）

首页同时提供全部收录与已完成深研入口；最近收录区已按后续要求移除。目录按 `first_seen_at` 降序排列，同时间按 ID 排序，未知日期置后。未完成案例标记待研究并链接来源，只有符合原内容契约的记录生成报告页。

`bootstrap` 从 SQLite 的目录及详情观测历史取得首次收录时间，并保留登记表已有时间。此次为 1,348 条记录回填日期：1,289 条来自已有历史数据库，59 条来自 Git 中首次出现该 ID 的 registry 提交时间（含最新 14 条）。这些是本站收录记录时间，不是源站发布日期。构建仍只读取 Git 中的 registry/research/reports，不依赖本地数据库或 Git 历史；后续自动收录将日期一起提交，main 自动部署后即可出现。

验证覆盖新增未研究案例排序、未知日期回退、日期重复同步稳定性、首页入口及目录排序、目录搜索、构建目录数量与禁用重复文案。来源、具体风险、数据缺失仍保留；源站模板、自编未实测提示词及经济情景用短标签说明。

## 原作者方法（2026-10-16 后续修订）

单篇先显示案例名称、原作者的方法与来源，再显示我们的分析。author_method 三种状态分别是作者方法摘要、原始报道摘要（非作者原文）、原帖暂未读取。摘要采用英文与对应中文翻译；中文默认显示，英文可展开，均可在无脚本环境阅读。来源URL必须匹配登记的原始来源，成功读取凭据支持每个摘要；不把源站介绍、Copy prompt或自编模板视为作者原话。当前22篇中12篇取得摘要来源、10篇保留不可读状态，不算新增深研。

独立daily爬虫只发布目录及刷新元数据，不改research/reports；最新源站模板仍由registry投影。深研读取最近已提交目录，不在每篇前重爬。流程见[逐案任务](../tasks/hourly-business-research.md)。

## 源站案例与实际 agent

22 篇研读现优先展示 agentusecases.ai 的介绍、方法与结果：英文原创摘要和对应中文翻译，非源站全文；之后保留外部原作者的方法与分析。目录从 Done with 观测实际 agent，不使用 Try it yourself 推荐工具作替代。覆盖、许可检查、哈希、缺失清单与同步机制见[本轮记录](docs/source-case-verification.md)。

## 当前发布方式（2026-10-20，北京时间）

按用户要求，Git 自动部署已在根目录 `vercel.json` 关闭。研究仍正常测试、提交并合并 main；只有用户明确要求查看时，才从通过验证的提交手动发布。不要创建每小时发布任务，也不要自动恢复 Git 发布。GitHub 检查与部署分别处理。
