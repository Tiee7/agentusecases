# 逐案例商业深研与独立目录爬虫

## 当前优先交付（2026-10-20）

先执行[欠交成果清单](quality-closure-20261020.md)及其[结构记录](quality-closure-20261020.json)：修正 Spark 第二批 10 案并补自身固定 30 案最终审查。两项尚未完成时不得认领新案例，不等待 Spark 返修而停工。完成必须有逐案交付、适用测试、提交与远端回读证据；最终结果主动回复用户。200美元/四周不是用户准入条件。

## 调度与职责

- 独立爬虫保留 `.github/workflows/daily.yml` 的 `0 1 * * *`（UTC；北京时间09:00），不另建定时任务。GitHub 调度可能延迟，以实际 run 为准。
- 默认批量读取完整公开目录及详情，检测新增、移出、内容变化和源站试用模板变化；`limit=5` 仅供明确发起的采样检查，不冒称完整详情刷新。恢复最近成功历史，保存本轮数据库及变化报告 artifact。
- 爬虫与深研各自工作。深研每篇开始前**不运行全量或采样爬虫**，也不因一个案例结束而触发目录刷新。
- 当前主对话助手在自有环境单一串行研究，每次处理一个案例，不启动第二研究执行者、用户云端 Codex 或保存编码环境。独立分支完成验证、推送和远端回读后即可继续下一例，不再设置五分钟冷却。main 由整合任务串行处理；网站展示或部署验收不作为研究继续的前置条件。

## 开始研究

1. 核对现有认证为 Tiee7，仓库为 `Tiee7/agentusecases`，仓库级 author/committer 为 `Tiee <tieetheai@gmail.com>`。保留无关修改；有其他写入在途则等待父任务协调。
2. 同步最新 main，在独立分支工作。读取 `registry/cases.json`、`registry/refresh.json`（若存在）、当前 research 状态、`research/brief/` 简要完成记录和最近完成记录，排除已完成同层级研究以避免重复；记录使用的目录提交 SHA、抓取时间、总数和详情采样范围。没有 refresh 元数据时，以最近成功 daily run 和已提交目录为依据，明确时间未知部分，不为此重爬。爬虫最近失败时可使用最近成功快照并标明日期；没有可用目录则停止选择。
3. 阅读 `RESEARCH_STANDARD.md`、`research-business-template.json`、`tasks/research-one-case.md`，运行 Python 单元测试，先检查欠交成果清单，仅两项闭环后按已核实原站 `/new` 从新到旧选择；不得用 Wanted 或 Trending 替代新旧排序。选择不是爬取。若已无待研究案例，记录状态并等待独立爬虫后续更新。
4. 深入核查所选案例的原始作者来源、产品、技术、市场和替代方案；只读取研究所需来源。遵守 robots 和既有访问限制，不调用被禁止的源站 `/api/`，不绕过权限拒绝、验证码、安全警告或已取消的访问。普通临时读取失败最多再试一次，仍失败跳过该来源；明确拒绝或 robots 禁止直接跳过。外部原帖无法取得不阻塞案例研究，可用已有源站正文、归档和其他可访问来源分析，但不以聚合摘要或试用模板替代作者方法。
5. 原作者的方法与来源置于我们分析之前。`author_method` 使用短的中英方法摘要：直接作者资料标 `author_summary`，媒体/汇编转述标 `reported_summary` 并说明非作者原文，无法取得标 `unavailable`。中文是英文摘要的翻译，不是长文全文翻译。每个步骤必须有已读原始来源支持；保存读取凭据，不公开整篇缓存或编造缺失步骤。
6. 按研究标准完成商业判断、独立自用价值、至少两种可复算经济情景、事实、反证与来源。源站 Copy prompt、自编提示词和作者方法分别标识。完整深研保留既有质量门槛并标记 `analysis_depth: deep`。材料不足时保存有依据的简要分析，标记 `analysis_depth: brief` 并与深研分开统计，不编造原文、数字或评分。现行 v2 发布校验仅支持深研；简要稿另存 `research/brief/<id>.json` 和对应简报，不冒充通过该校验的 completed v2 记录。目录收录和页面修订不增加研究数。

## 发布与冲突处理

- 按选中 ID 执行 `business verify-sources`、`business publish`、Python/网站测试、构建、输出检查、浏览器验证和 `git diff --check`。非敏感报告、结构记录、来源元数据、索引及完成记录入 Git；原文缓存、账户秘密和数据库不入 Git。
- 发布窗口与 daily 的 `case-research-publication` 协调；该 Actions concurrency 仅约束 Actions，不能代替父任务跨环境研究互斥。
- 推送前重新 fetch main。若独立爬虫已发布目录，先合并它的登记项、来源观察和刷新元数据，再基于当前 research 重建索引；保留固定 ID、首次收录时间及新案例。不得用研究开始时的整份旧 registry 覆盖新目录。
- 若出现同一研究记录的语义冲突，保留成果、停止发布并交父任务处理；不自动选择整边覆盖，不强推。合并后的结构记录、报告、目录和网站须重新验证。推送结果不确定时先回读远端再决定是否重试。
- daily 的独立发布仅写 `registry/cases.json`、`registry/CATALOG.md`、`registry/refresh.json`、`INDEX.md`，不改研究字段、报告或作者方法。并发 push 失败后读取最新 main、重新生成和验证目录，最多三次；拒绝或权限错误立即停止，不绕保护。
- 现有 `GITHUB_TOKEN` 产生的 push 不会启动另一个 Actions push workflow，因此 daily 自身在推送前运行 Python/内容/构建/输出检查；普通 Tiee7 研究推送继续触发 Reading site checks。生产发布由现有 Vercel Git 集成处理；部署和展示核验由整合任务另行记录，不阻塞独立分支研究完成或下一例开始。

## 完成与继续

记录 UTC `run_id`、`started_at`、`completed_at`、`resume_not_before`（与最终完成时间相同，无额外冷却）、提交 SHA、目录快照、`analysis_depth` 及结束状态到 `research/runs/<run-id>/completion.json`。独立分支验证、推送、远端回读和补交证据完成后且优先交付清单允许后，才可启动下一案例；main 合并另行串行协调。

报告案例链接、结论、分数、真实验证、远端身份及部署结果；分别报告独立爬虫最近真实运行和本轮使用的目录。一次成功不证明以后准点运行。本页面修订不新增深研，也不手动启动新研究。

## 源站试用模板

公开 SSR/限定 DOM 提取的 `source_trial` 独立于作者方法。记录原文、建议工具、URL、读取时间（或真实区间）、状态及哈希。独立爬虫只更新 registry 投影；网站优先使用 registry 的最新模板。研究发布时才同步所选案例的源站模板。失效观察不冒充可用，缺失不表示源站不存在模板。不得将建议工具当作作者实际工具或将 Copy prompt 当作作者原文。

## 本站编辑标题规范

研究记录 `title`、报告 H1、首页卡片、目录、试用页、SEO title 和总索引使用同一个客观用途标题，例如“用 Claude Cowork 生成投资备忘录并跟踪投资”。标题写实际 agent、动作、任务对象；不写建议、不建议、适合、值得、价值评级、优缺点或商业可行性结论。评价、评分、限制和论证放在正文分析与 verdict 中，不因改标题删除。未知工具可写“用 AI agent …”，不要用源站推荐工具冒充实际工具。

遵守 `schemas/editorial-title-policy.json`，运行 `agentwatch.titles.validate_editorial_title`。发布校验拦截已知评价短语，人工仍需检查是否夹带结论；不能靠避开关键词通过。保持案例 ID、slug 和链接稳定；不改 `registry/cases.json` 的源站标题、归档英文原文／原始标题、译文及引用来源标题。未编辑的源站标题仍按来源原样保留，规范仅约束本站编辑标题。

发布前核对研究 JSON title 与 Markdown H1 一致，重新生成 `python -m agentwatch.business index`，执行仓库与阅读站测试，并确认 reports/cases/trials 的 H1、浏览器标题、首页卡片与目录入口一致。

## 已审双语档案的目录刷新（2026-10-21修正）

独立目录刷新不得改写已翻译或已编辑的发布版档案，`registry/archives/<id>.json` 保持逐字节不变。最新爬取原文、字段和读取凭据单独保存在 `registry/archive-observations/<id>.json`；`published_edition` 指向已发布档案文件及原文哈希，正文不同明确标 `review_required: true`。新观察不携带旧译文冒充新正文译文，研究者复核时再决定如何发布新版本。未审档案仍正常刷新。覆盖与刷新元数据列出待复核数量/ID，目录增长不增加深研完成数。

固定30案仍检查原档案完整文件哈希、英文正文和中文译文哈希。Copy prompt约束逐字段保持工具、完整文本、URL和状态，仅允许独立读取凭据（method、observed_at、observation_window、html_sha256）随新抓取变化；语义字段变化仍使检查失败。
