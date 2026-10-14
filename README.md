# Agent usecase watch

每日跟踪 [agentusecases.ai](https://agentusecases.ai) 的案例目录及内容变化，并分批研究、评分、生成报告。

## 已验证的范围

2026-10-14：真实 sitemap 包含 **1,289** 个案例，与首页公开计数一致。已采集首页默认 `top` 展示的首批5个详情并执行连续快照对比。**全站详情遍历和 GitHub 定时任务尚未执行验证。** 首批研究是基于聚合站详情的案头初稿；原始报道访问被云环境网络策略拦截，没有运行项目、验证收益或最终税务结果。

入口：[首批研究初稿](reports/batch-001.md)。每个案例都有JSON研究记录与Markdown报告。

## 本地运行

Python 3.12+，仅使用标准库，无需第三方依赖。

```sh
cd /workspace/agentusecases
python -m unittest discover -s tests -v
# 少量详情验证，目录仍为完整 sitemap
python -m agentwatch.crawler --limit 5
python -m agentwatch.queue --batch-size 5
python -m agentwatch.digest
# 完整日常采集；当前规模至少约43分钟，网络会增加耗时
python -m agentwatch.crawler --limit 0 --workers 4
```

适配真实站点的 `/use-case/` 详情、公开 Next.js 服务端页面和 sitemap；不调用 robots.txt 禁止的 `/api/`。全局请求起始间隔至少2秒，最多4个默认并发请求；机器人规则声明更长间隔时遵守该间隔。仅对限流、服务器错误和网络错误最多尝试3次，保留HTTPS验证。任何详情获取或解析失败、目录数量不符均终止，不保存成功快照。

SQLite `data/history.sqlite3` 保存成功批次、完整目录和采集详情正文。`data/catalog.json` 是最新成功目录；`data/runs/` 是各批次变化摘要；`data/daily-report.md` 为可读日报，也写入GitHub Actions运行摘要。区分：

- `baseline`：首次基线，不伪称1,289个新增。
- `newly_listed` / `no_longer_listed`：sitemap新增/移出，移出不证明网页删除。
- `lastmod_changed`：网站声明的更新时间变化，不证明正文变化。
- `content_changed`：已抓取正文、提示词、标题或原始来源链接变化。
- `position_changed`：当前采集序列位置变化，不是精确全站热度排名。
- `not_observed`：本次未采到以前的详情，不等于删除。

`complete_catalog` 与 `details_complete` 分开；样本详情不冒充全站覆盖。正文提取排除导航、广告和相关推荐；解析器版本独立建基线，避免提取规则升级被误判为网站变化。连续运行之间站点可能更新，快照不代表所有网页同时刻的事务快照。历史持续增长，发布前需确定存储和保留策略。

## 热门与研究批次

网站的 `top` 按分类展示，客户端会结合站内投票、`accounts`和代理类型分散排序。我们使用**公开服务端首屏的分类top顺序**，不是全站统一热门榜，也没有获取被禁止API里的实时投票。首批5个属于首页先展示的 Money, Bills & Benefits 分类。

队列将已观察到的首屏top放在前面，随后按sitemap顺序；每条标明排序来源。未知排名不标成热门，`hot_order_verified`仅对整批均来自首屏top时为真。每批默认5个；`research/*.json`中完成审阅后设为 `status: reviewed`，后续队列会跳过。当前5份记录仍为 `draft`，不会被自动视为研究完成。

逐项研究：公开详情→原始报道→项目官网/公开代码/文档/定价→必要时用合成数据做有限测试。研究与评分需要来源核验和判断，当前脚本不会自动替人工完成，也不会把未经读取的报道当已核验来源。

## 评分与报告

研究模板：`research-template.json`。生成报告：

```sh
python -m agentwatch.report research/compile-deductions-and-schedule-c-with-claude-code.json --output reports/compile-deductions-and-schedule-c-with-claude-code.md
```

维度：需求价值25%、效果证据25%、落地可行性20%、成本与维护15%、风险控制15%。0–5分加权为100分；0=有证据显示严重缺陷，1=薄弱，2=有限，3=可接受，4=较强，5=优秀。效果证据评估的是证据强度；低分不代表效果为零。未知用null，任一维度缺失则不算总分。每项分数必须附理由和已读取的HTTPS来源；生成器验证格式，不替代来源审核。

首批分数是低置信度初评，其中完整维度的两份给出暂定总分，其余暂不计算。最终评分应补充原始来源、当前可用性、权限/隐私机制、实际成本与限定范围实验。报告明确区分自述、聚合站整理、研究者判断和实测。

## 每日自动运行

`.github/workflows/daily.yml` 每天**北京时间09:00**运行，也支持手动触发。GitHub可能延迟调度。工作流先测试、恢复上次成功运行的历史，再全量采集和生成下一批研究队列，最后上传 `usecase-history` artifact。

工作流必须位于GitHub默认分支，且仓库Actions可用。首次发布后需手动触发，验证全量抓取、历史恢复和artifact上传，再检查次日调度。仓库变量 `LISTING_URL`、`CASE_ORDERING`可覆盖默认值，但非首页URL或未知布局需要重新验证适配器。

Artifact保留90天；长期停用、删除或过期会导致恢复失败，应外部备份数据库。累计SQLite可能达到GitHub单artifact容量限制。公开仓库长期无活动也可能暂停定时工作流。任务超时为300分钟；任何失败均不宣称当天完成。工作流尚未验证GitHub的实际权限与资源限制。

## 云环境与待办

站点域名、首批原始报道域名和复用启动说明已保存到环境配置草稿。草稿不代表运行策略已更新或环境已发布；请在环境设置审阅并保存，然后发布环境。没有需要安装的第三方依赖，所以未添加安装脚本。

下一步：恢复原始报道访问，补齐首批5份研究；验证全量遍历；经授权发布代码并手动验证Actions，再确认每日运行。可视化Data报告运行时在本环境不可用，当前交付可审阅Markdown研究稿及JSON证据记录，没有声称发布在线报告。
