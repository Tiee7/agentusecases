# Agent usecase watch

每日跟踪 [agentusecases.ai](https://agentusecases.ai) 的案例目录及内容变化，并分批研究、评分、生成报告。

## 已验证的范围

真实 sitemap 包含 **1,289** 个案例，与首页公开计数一致。已完成**1,289个唯一案例的本地全站详情遍历**并核对数据库覆盖率。GitHub每日爬虫的5条详情试运行已经成功，全量定时运行与跨批历史恢复仍需验证。

入口：[商业深度研究总索引](INDEX.md)。已完成一份阅读14个原始/竞争/市场/反馈来源的商业深研，税务凭证整理案例为45/100，结论“适合内部效率工具”。原有5份介绍型初稿中4份仍待重做，不能当深研完成；历史初稿说明见[首批记录](reports/batch-001.md)。

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

适配真实站点的 `/use-case/` 详情、公开 Next.js 服务端页面和 sitemap；不调用 robots.txt 禁止的 `/api/`。全局请求起始间隔至少2秒，最多4个默认并发请求；机器人规则声明更长间隔时遵守该间隔。重定向会被阻止，目标路径需要单独核验。仅对限流、服务器错误和网络错误最多尝试3次，保留HTTPS验证。任何详情获取或解析失败、目录数量不符均终止，不保存成功快照。

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

队列将已观察到的首屏top放在前面，随后按sitemap顺序；每条标明排序来源。未知排名不标成热门，`hot_order_verified`仅对整批均来自首屏top时为真。每日旧队列每批默认5个；商业深研每轮只选择一个未完成案例。`reviewed`或`completed`记录会跳过，`draft`不会被视为完成。

逐项研究：公开详情→原始报道→项目官网/公开代码/文档/定价→必要时用合成数据做有限测试。研究与评分需要来源核验和判断，当前脚本不会自动替人工完成，也不会把未经读取的报道当已核验来源。

## 评分与报告

当前商业深研使用[研究标准](RESEARCH_STANDARD.md)与`research-business-template.json`，用户反馈权重5%。旧介绍型草稿保留旧评分标准，仅供历史参考，不与新版商业分数比较。旧版生成器仅适用于旧模板`research-template.json`：

```sh
python -m agentwatch.report research/negotiate-bills-handle-returns-and-cancel-subscriptions.json --output reports/negotiate-bills-handle-returns-and-cancel-subscriptions.md
```

旧版维度：需求价值25%、效果证据25%、落地可行性20%、成本与维护15%、风险控制15%。0–5分加权为100分；未知用null，任一维度缺失则不算总分。旧分数是低置信度初评，不是商业投入判断。新版需通过`agentwatch.business`来源、对应关系、完整性及经济计算校验，再由Codex逐条审核事实与结论。

报告明确区分自述、教学虚构数字、研究者情景假设和实测。已经深研的税务案例未运行完整项目、没有验证最终税务结果，不能把代码阅读称为生产验证。

## 每日自动运行

`.github/workflows/daily.yml` 每天**北京时间09:00**运行，也支持手动触发。GitHub可能延迟调度。手动触发可将`limit`设为5以快速验证工作流；定时运行默认为0，即全量。工作流先测试、恢复上次成功运行的历史，再全量采集和生成下一批研究队列，上传 `usecase-history` artifact，成功后同步案例登记表与索引、提交推送main。样本采集使用完整目录登记，不将未采样案例误判为消失。

工作流必须位于GitHub默认分支，且仓库Actions可用。首次发布后需手动触发，验证全量抓取、历史恢复和artifact上传，再检查次日调度。仓库变量 `LISTING_URL`、`CASE_ORDERING`可覆盖默认值，但非首页URL或未知布局需要重新验证适配器。

Artifact保留90天；长期停用、删除或过期会导致恢复失败，应外部备份数据库。累计SQLite可能达到GitHub单artifact容量限制。公开仓库长期无活动也可能暂停定时工作流。任务超时为300分钟；任何失败均不宣称当天完成。

## 云环境与待办

站点域名、首批原始报道域名、GitHub API域名和复用启动说明已保存到环境配置草稿。草稿不代表运行策略已更新或环境已发布；请在环境设置审阅并保存，然后发布环境。没有需要安装的第三方依赖，所以未添加安装脚本。

当前已恢复原始来源与GitHub访问，完成一份商业深研和GitHub爬虫试运行。Python标准库即能运行，不需要安装第三方依赖。每小时研究调度是单独的尚未完成项，见下文。

## 每小时商业深度研究

用户要求由Codex账号直接研究，不使用模型API。此前误接的API研究工作流已停用、移除；每日全量爬虫继续运行。

入口：[商业深度研究总索引](INDEX.md)；[完整对应目录](registry/CATALOG.md)；[研究标准](RESEARCH_STANDARD.md)。用户反馈占5%，其余评分围绕付费需求、效果、利润、获客、壁垒与经营风险。旧介绍型初稿不算深研完成。

完整任务正文及每小时调度规则：[Codex定时研究任务](tasks/hourly-business-research.md)。任务每轮选择一个未完成案例、读取原始资料、完成明确商业判断，通过检查后更新单篇文件与索引并推送main。

**定时研究尚未生效：当前会话没有创建原生Codex定时任务的工具。** 仓库内的任务说明不会自行运行，也不能把临时云环境后台进程当作持续定时任务。不需要提供API密钥；需要在支持项目执行的原生Scheduled入口创建任务。
