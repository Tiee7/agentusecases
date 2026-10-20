# 用Claude Code整理本地新闻并上传WordPress文章

## 中文原案例

    自动将本地新闻文章发布到WordPress
    Claude Code agent研究本地新闻、撰写HTML文章、上传到WordPress、设置特色图片、核验并记录结果，也会检查Airtable和Gmail。
    使用的是
    CC
    Claude Code
    他们做了什么
    Koka Sexton在终端里运行Claude Code，并为它配置WordPress、Airtable和Gmail的凭据。agent研究本地新闻，获取来源文章并撰写完整HTML文章。随后，它使用WP-CLI或自己编写的脚本上传文章，设置特色图片，检查HTTP响应并记录结果。发布三篇文章只需提出一次请求。
    进展与成效
    他说，原本需要人工90分钟完成的流程，现在一个对话轮次就能完成。吞吐量数字来自他自己的内部基准，文章没有提供独立测量结果。
    值得了解
    在生成第一份输出之前就编写验证脚本，否则幻觉内容可能直接上线。文章还建议让agent与人工流程并行运行两周。
    亲自尝试
    使用
    Claude Code
    复制提示词
    搭建一个工作流，研究关于[我的城镇或主题]的近期新闻，撰写[数量]篇附带来源的简短HTML文章，并在我的WordPress网站[网站URL]上将它们准备为带特色图片的草稿。之后，检查每份草稿是否正常加载，并将标题和链接记录到[Airtable或电子表格]。草稿准备好后停下来，在发布任何内容之前先展示给我。
    原始来源：https://kokasexton.com/claude-code-marketing-ops-power-tool/

<details><summary>English original</summary>

    Publish local news posts to WordPress automatically
    Claude Code agents research local news, write HTML posts, upload them to WordPress, set featured images, verify and log results, and also check Airtable and Gmail.
    Done with
    CC
    Claude Code
    What they did
    Koka Sexton runs Claude Code in a terminal with credentials for WordPress, Airtable and Gmail. The agent researches local news, fetches source articles and writes full HTML posts. It then uploads them with WP-CLI or a script it writes, sets featured images, checks HTTP responses and logs the results. Publishing three articles takes a single request.
    How it went
    He says a 90-minute human process now happens in one conversation turn. The throughput figures come from his own internal benchmarks, and the article gives no independent measurements.
    Worth knowing
    Write the verification script before the first output, because hallucinations can go live otherwise. The article also suggests running the agent in parallel with a human for two weeks.
    Try it yourself
    with
    Claude Code
    Copy prompt
    Build a workflow that researches recent news about [my town or topic], writes [number] short HTML posts with sources, and prepares them as drafts on my WordPress site [site URL] with a featured image. Afterward, check each draft loads correctly and log the titles and links in [Airtable or a spreadsheet]. Stop with the drafts ready and show me them before anything is published.
    Original source: https://kokasexton.com/claude-code-marketing-ops-power-tool/

</details>

## English

    Publish local news posts to WordPress automatically
    Claude Code agents research local news, write HTML posts, upload them to WordPress, set featured images, verify and log results, and also check Airtable and Gmail.
    Done with
    CC
    Claude Code
    What they did
    Koka Sexton runs Claude Code in a terminal with credentials for WordPress, Airtable and Gmail. The agent researches local news, fetches source articles and writes full HTML posts. It then uploads them with WP-CLI or a script it writes, sets featured images, checks HTTP responses and logs the results. Publishing three articles takes a single request.
    How it went
    He says a 90-minute human process now happens in one conversation turn. The throughput figures come from his own internal benchmarks, and the article gives no independent measurements.
    Worth knowing
    Write the verification script before the first output, because hallucinations can go live otherwise. The article also suggests running the agent in parallel with a human for two weeks.
    Try it yourself
    with
    Claude Code
    Copy prompt
    Build a workflow that researches recent news about [my town or topic], writes [number] short HTML posts with sources, and prepares them as drafts on my WordPress site [site URL] with a featured image. Afterward, check each draft loads correctly and log the titles and links in [Airtable or a spreadsheet]. Stop with the drafts ready and show me them before anything is published.
    Original source: https://kokasexton.com/claude-code-marketing-ops-power-tool/

## 中文

    自动将本地新闻文章发布到WordPress
    Claude Code agent研究本地新闻、撰写HTML文章、上传到WordPress、设置特色图片、核验并记录结果，也会检查Airtable和Gmail。
    使用的是
    CC
    Claude Code
    他们做了什么
    Koka Sexton在终端里运行Claude Code，并为它配置WordPress、Airtable和Gmail的凭据。agent研究本地新闻，获取来源文章并撰写完整HTML文章。随后，它使用WP-CLI或自己编写的脚本上传文章，设置特色图片，检查HTTP响应并记录结果。发布三篇文章只需提出一次请求。
    进展与成效
    他说，原本需要人工90分钟完成的流程，现在一个对话轮次就能完成。吞吐量数字来自他自己的内部基准，文章没有提供独立测量结果。
    值得了解
    在生成第一份输出之前就编写验证脚本，否则幻觉内容可能直接上线。文章还建议让agent与人工流程并行运行两周。
    亲自尝试
    使用
    Claude Code
    复制提示词
    搭建一个工作流，研究关于[我的城镇或主题]的近期新闻，撰写[数量]篇附带来源的简短HTML文章，并在我的WordPress网站[网站URL]上将它们准备为带特色图片的草稿。之后，检查每份草稿是否正常加载，并将标题和链接记录到[Airtable或电子表格]。草稿准备好后停下来，在发布任何内容之前先展示给我。
    原始来源：https://kokasexton.com/claude-code-marketing-ops-power-tool/

## 原作者的方法与来源

来源：[How Claude Code Is Quietly Becoming the Marketing Ops Power Tool Nobody Saw Coming](https://kokasexton.com/claude-code-marketing-ops-power-tool/)

作者方法摘要

1. 作者描述收集来源并准备HTML文章。
   English summary: The author describes collecting sources and preparing HTML posts.

2. 脚本上传文章与图片，再检查响应并记录结果。
   English summary: Scripts upload posts and images, then check responses and log results.

3. 他建议先建立验证，并与人工流程作比较。
   English summary: He recommends building verification first and comparing with a human workflow.

## 我们的分析

**商业结论：适合内部效率工具。先做可核对草稿，把编辑确认和发布权限分开**

案例给出了跨工具内容流程，官方接口也支持草稿与回读，足以形成内部实施假设。但文章数量、对话轮数和HTTP成功并不能说明新闻真实、图片有权使用或业务盈利。已有固定工作流可替代一部分功能，实施应先验证来源链、人工总工时和错误恢复，避免将自动上传包装为无人编辑的新闻业务。

案例ID：`publish-local-news-posts-to-wordpress-automatically` · 案例来源：https://agentusecases.ai/use-case/publish-local-news-posts-to-wordpress-automatically
研究时间：2026-10-20T11:06:31.706905+00:00

**商业评分：41.5/100。用户反馈信号占5%。**

| 维度 | 权重 | 分数 /5 | 商业依据 |
|---|---:|---:|---|
| 付费需求 | 20% | 3 | 固定CMS任务和已有内容团队有可识别负担，但本方案的预算、付款意愿和读者增量价值尚未独立验证。 [Sdirectory, Sadjacent] |
| 业务价值与效果证据 | 20% | 2 | 作者有具体流程叙述，单轮对话与90分钟不是可比的完整计时，未取得可用率和净节省的独立测量。 [Soriginal] |
| 单位经济与利润 | 20% | 2 | 人工核查、素材授权和返工可能主导成本，情景计算可复核但全部经营输入是假设，无真实盈利证据。 [Sdirectory, Scompetitor] |
| 获客与市场进入 | 15% | 2 | 可向已有编辑团队验证流程，但获客转化、销售周期和维护续约没有实证，不能从作者自营服务推定可复制。 [Soriginal] |
| 竞争壁垒 | 10% | 1.5 | 发布接口和生成草稿模板公开可得，价值需来自许可资料和编辑流程，目前没有独占壁垒的证据。 [Swp, Scompetitor] |
| 交付与经营风险 | 10% | 2 | 需要来源、图片和发布权限治理，HTTP成功不能替代编辑核查；仍有较高人工与运行维护要求。 [Sap, Spermissions] |
| 独立用户反馈信号 | 5% | 0.5 | 只取得相邻新闻室经验，未取得本案例独立复现；有限信号不能作为产品满意度或收益验证。 [Sadjacent] |

## 自用价值：中

适合已有编辑能力者减少录入，净节省待验证。

依据：Sdirectory, Sap, Spermissions

- 适用人群：维护WordPress栏目、已有来源与审阅能力的个人或团队。
- 用途：整理来源、生成短稿和准备CMS草稿清单。
- 预期收益：可能减少排版与重复操作，未测实际净工时或读者收益。
- 设置成本：来源范围、栏目模板、权限、图片规则与回读检查。
- 维护成本：接口插件变化、事实更新、失败重试和编辑更正。
- 使用频率：按栏目发布周期，低频站点可能不值得额外设置。
- 隐私风险：CMS凭据、邮箱及未公开材料进入脚本或日志。
- 错误风险：虚构事实、旧闻当新、误图、重复创建和未经批准发布。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/publish-local-news-posts-to-wordpress-automatically

建议工具：Claude Code

    Build a workflow that researches recent news about [my town or topic], writes [number] short HTML posts with sources, and prepares them as drafts on my WordPress site [site URL] with a featured image. Afterward, check each draft loads correctly and log the titles and links in [Airtable or a spreadsheet]. Stop with the drafts ready and show me them before anything is published.

自编试用模板

准备条件：三份虚构来源与图片占位说明，不提供真实账户、凭据或私人邮件。

工具：已有文本助手与本地文档，暂不接CMS。

预期结果：短稿、事实来源对应、冲突与待审清单，不发布；未实测。

### 源站Copy prompt

原文模板

出处：https://agentusecases.ai/use-case/publish-local-news-posts-to-wordpress-automatically

依据：Sdirectory

    Build a workflow that researches recent news about [my town or topic], writes [number] short HTML posts with sources, and prepares them as drafts on my WordPress site [site URL] with a featured image. Afterward, check each draft loads correctly and log the titles and links in [Airtable or a spreadsheet]. Stop with the drafts ready and show me them before anything is published.

### 离线新闻草稿核对

自编模板

出处：研究团队自编

依据：Sap

    只依据这三份虚构资料写短草稿，每个事实列来源，冲突和缺项保持待核。不要补造引语，不生成现场纪实图，不登录或发布。列出图片权利、重复输入与人工确认清单。

## 已核验事实

- 目录记载本地新闻HTML、WordPress上传及三篇一次请求；90分钟与单轮对话均为作者自述。 [Sdirectory]
- 文章页面显示2026-05-26，与目录来源日期不同；描述终端跨工具工作流与先验证建议，没有独立计时或完整代码。作者同时提供营销服务。 [Soriginal]
- post_status默认draft；porcelain可返回新文章ID。创建成功不验证新闻内容真实性。 [Swp]
- 支持draft/pending/publish等状态和featured_media字段，并可按ID回读；文档更新2026-10-14。 [Srest]
- 2026-07-23更新强调发表前人工审阅及新闻摄影限制；这是AP内部政策，不是所有媒体的法律结论。 [Sap]
- 公开模板生成结构、HTML、草稿和特色图，建议人工审阅后发布；未证明新闻事实核查或实际用户效果。 [Scompetitor]
- 官方提供allow/ask/deny等权限规则；配置能力不证明作者的真实账户范围或安全隔离已审计。 [Spermissions]
- 相邻选举结果自动化经验强调现场监控、验证和人工介入；不是本案例新闻写作流程复现，也不是无人值守证明。 [Sadjacent]

## 客户需要可靠的出版准备，不只是更多文章

付款人假设是已有WordPress站点、固定发布任务和编辑负责人的小型媒体或内容团队。实际用户是选题、编辑与运营人员；读者则关心信息是否真实、当地是否相关以及错误能否及时更正。三篇文章一次请求产出，最多说明作者描述的操作批量化，不能直接推出读者增长、广告主需求或订阅意愿。不同类型的内容不能混成同一产品：活动信息整理、商家更新和突发事件报道的核查责任明显不同。优先切入来源明确、结构稳定、低风险的资料整理与排版，而不是一开始就自动生产涉及个人声誉或公共安全的新闻。买方还必须有权使用文章与图片，并能够安排最终审阅。没有稳定的原始资料与编辑能力，仅购买agent不会自动获得新闻业务。对于低频更新站点，手工录入和原生定时发布可能已经够用；真正待验证的是重复操作在总编辑时间中占多少，以及减少操作后是否仍有足够内容价值。

依据：Sdirectory, Soriginal, Sap

## 分开资料核对、草稿创建和正式发布

作者叙述从新闻研究到HTML、配图、上传与日志的链条，但本轮没有实际生成稿件或可运行脚本来复验。拟议实施应先将选题、来源、时间和权利状态组织成材料包，再生成只引用已取得材料的短草稿；缺失或冲突信息进入待核对项。WordPress创建草稿与正式发布是不同状态，上传成功也不等于完成编辑审批。每篇应有明确文章ID、标题、内容摘要、来源列表、图片来源和审阅状态，重试时先按ID核实，避免重复创建。配图缺失不能悄悄借用未经授权图片；外部网页内容也不能成为执行脚本或泄露凭据的指令。源站模板明确在草稿阶段停止，与作者文章描述的发布行为需要分开保存。平台支持某个字段，只能证明接口有能力，不能证明特定主题、插件或权限配置下已正确显示。因此最终回读应检查状态、内容、图片与前端呈现，再由有权限的人决定是否上线。

依据：Soriginal, Swp, Srest

## 一分钟的操作演示不等于新闻生产成本

作者将原来90分钟的人工作业与一次对话相比，但一次对话不是严格定义的运行时长，也没有覆盖选题、核查、更正和维护的统一计时。文章中的内部基准不能外推为整个营销市场的采用率或收益。目录显示的来源日期与原文章显示的日期不同，应保留各自观察，不把较新的目录时间当原文首次发布。相邻的Local News Matters新闻室经验说明，即使自动获取结构化结果，现场仍需监控和人工验证；这是不同项目的边界证据，不是该作者工具的独立成功复制。市场判断应从工作分解开始：录入和排版是否反复、来源是否稳定、编辑本来花多久验证，以及自动化后要多花多久纠错。文章发布量增加不保证分发、读者信任或收入改善。如果主要瓶颈是缺少采访与原创信息而不是CMS操作，自动写更多文章可能没有商业价值。可采用一个内容栏目做受控对照，统计可用草稿率和审核后的净时间，而不是把对话轮数当效率指标。

依据：Sdirectory, Soriginal, Sadjacent

## 可选原生草稿、固定工作流或agent

WordPress原生API与WP-CLI已经可以创建草稿、设置状态和返回文章标识，agent的价值不是发明发布接口。n8n公开模板也展示了从关键词到WordPress草稿与特色图的流程，并建议发布前审阅；它是具体替代路线，但不是新闻真实性经过验证的产品。稳定的表单输入、固定字段和少数来源，可能更适合可预测的工作流或简单脚本；开放选题、格式变化和临时资料整理才可能需要agent的灵活性。比较时要保持相同交付范围：都包括核查、授权图片、错误处理和人工确认，不能拿脚本运行成本与完整编辑服务报价相比。固定流程易于限制写权限，agent临时写代码则需要更多执行边界和维护。我们没有获得作者的正式服务报价或n8n该模板实际使用成本，因此不编造价格差。采购前先试现有CMS能力，再判断哪个环节确有无法被简单自动化覆盖的增量需求，避免把整套系统当作单个功能收费。

依据：Swp, Srest, Scompetitor

## 按可交付草稿计费，核查成本单列

以下经营数字完全是假设，用于检查敏感性，不是作者收入或当前工具报价。情景A为每篇经人工核查的草稿包，价格40美元、模型与工具2美元、人工15美元、其他可变成本3美元、获客摊销5美元；贡献15美元。每月100篇、固定成本1000美元时，税前且未计额外研发的剩余500美元。情景B为复杂来源与返工较多的同价服务，模型与工具3美元、人工30美元、其他5美元、获客5美元，贡献负3美元，100篇并承担1000美元固定成本时亏1300美元。人工按30美元每小时计，分别相当于30和60分钟，不声称是真实新闻编辑工时。收费单位应定义为可审阅草稿，而不是保证排名或阅读量。托管、图片授权、资料订阅、补采与更正可能改变成本；若客户另付这些费用应事先说明。正贡献也不等于现金流为正，还取决于交付量、回款和退款。没有实测就不使用作者90分钟叙述来证明上述情景成立。

依据：Sdirectory, Scompetitor

## 先展示来源链与审核体验，再卖自动化

候选进入方式是向已有稳定栏目和编辑责任人的团队展示虚构材料的草稿包，重点证明每条事实可以回到来源、每张图有明确用途，而不是承诺完全无人值守。本案作者同时提供营销服务，文章有获客目的；这可以解释一种销售渠道，但不能证明相同写法对新服务商也会带来客户。新项目需要说明哪些工作仍由编辑承担，什么材料不处理，什么情况下暂停发布，以及如何退出或导出。实施收费与按月维护可分别验证，不能把一次安装当作永久免维护。对当地新闻来说，信任和纠错能力可能比批量产出速度更重要，广告主或订阅者是否付钱还取决于读者价值。第一阶段可以收集已有团队对材料包的评价和真实工作分解，下一阶段才在明确授权后做试点；本文没有发出任何外联、申请账户或启动经营。没有转化和续约数据时，获客成本只能作为假设，并应设置明确的交付范围防止无限修改吃掉利润。

依据：Soriginal, Sap

## 流程资产比临时脚本更重要，但不是自动形成

关键词生成文章和上传CMS的功能已有公开模板，单靠提示词很难构成持久壁垒。可能有价值的资产是经过许可的本地资料渠道、栏目事实表、编辑规则、可靠的去重与更新机制，以及让客户能审阅和纠错的工作流。这些资产需要持续维护，不能把抓取到的第三方全文或用户邮箱内容直接当作可占有的数据优势。若每个客户都使用不同插件、主题和审核习惯，实施会变成定制服务，规模化收益不应预先假定。权限管理和稳定执行也是复制条件：只在文本里写“不要发布”不等于服务端阻止发布，临时脚本也可能超出原计划。一个合适的方案应能让编辑知道当前是草稿、已批准还是已发布，并保留修改依据。缺乏独占内容与分发优势时，供应商更可能靠可信交付和专业支持竞争，而不是靠模型本身。当前没有证据表明作者拥有难以复制的技术或可持续超额利润。

依据：Scompetitor, Spermissions

## HTTP成功只能验证上传，不验证新闻事实

检查状态码有助于发现接口失败，但不能检查事件日期、人物身份、引语、语境和图片是否真实。AP在2026年7月更新的内部标准仍要求发表前由记者审阅，并限制生成式AI新闻摄影；这是具体机构的政策，不是所有网站的法律条文，却提醒我们不能用技术成功替代编辑判断。实现上应分成机器可检与人工必检：字段缺失、链接、重复ID、草稿状态可自动检查，核心事实、敏感表述与图片语境需要有责任的人核实。输入新闻网页按资料处理，不执行其附带指令；邮箱和CMS凭据采用最小范围并避免进入正文与日志。Claude Code权限工具提供控制手段，但本轮没有审计作者的真实配置。遇到来源撤回、内容更正、图片失效或部分上传，应保持未完成状态并可追溯补救，不能反复重跑造成多篇重复公开稿。关于内容和图片的使用权，本研究仅提出核查要求，不认定任何未知材料已获许可。

依据：Swp, Srest, Sap, Spermissions

## 没有取得本案例的独立复现反馈

相关体验：相邻新闻室实施说明自动化仍需要现场监控与人工验证，不支持将上传成功等同新闻核验完成。

依据：Soriginal, Sadjacent

## 先验证草稿链，不直接自动发布新闻

建议把本案作为已有内容团队的内部效率工具来试验，初始范围限于有明确材料和编辑确认的草稿准备。先用三份虚构来源设计一篇正常草稿、一篇日期冲突稿和一篇图片权利不明稿，再加入同一请求重复触发与上传中断情形。预期输出是文章草稿、事实来源对应、缺项及待审清单，不是公开新闻。通过条件应包括来源可追溯、冲突没有被模型偷偷消解、无授权图片不被使用、重复请求不新增多份，以及没有未经批准转为发布。随后若取得真实试点授权，才比较人工总工时、可采纳比例和更正负担；两周可以作为观察窗口的示例，不能认为满两周就必然可靠。出现虚构引语、错认人物、泄露资料或越权发布即停止扩大；如果净节省很小、编辑返工较多或持续负贡献，就保留原生工作流。本文完成的是商业研究与演练设计，没有连接WordPress、Airtable或Gmail，也未实际发布任何文章。

依据：Sdirectory, Sap, Sadjacent

## 单位经济测算：情景假设，不是项目已实现的财务结果

| 情景 / 交付单位 | 收入 | 可变成本（含获客） | 单位贡献 | 月交付量 | 月固定成本 | 月经营贡献 |
|---|---:|---:|---:|---:|---:|---:|
| 标准草稿包：研究者假设 / 每篇经人工核查的草稿包 (USD) | 40.00 | 25.00 | 15.00 | 100 | 1000.00 | 500.00 |
| 复杂来源返工：研究者假设 / 每篇经人工核查的草稿包 (USD) | 40.00 | 43.00 | -3.00 | 100 | 1000.00 | -1300.00 |

标准草稿包：研究者假设假设：全部为敏感性演算假设，不是作者报价或账单。人工每小时30USD，分别30或60分钟；未计税及额外研发，没有本轮付费API。实际素材授权和补采需另核。；API成本 2，人工成本 15，其他可变成本 3，分摊获客成本 5。依据：Sdirectory, Scompetitor

复杂来源返工：研究者假设假设：全部为敏感性演算假设，不是作者报价或账单。人工每小时30USD，分别30或60分钟；未计税及额外研发，没有本轮付费API。实际素材授权和补采需另核。；API成本 3，人工成本 30，其他可变成本 5，分摊获客成本 5。依据：Sdirectory, Scompetitor

## 反证与未核实信息

现成接口与固定模板已覆盖上传；相邻新闻室仍需人工监控，作者没有完整计时与独立质量指标。

未连接任何WordPress、Airtable、Gmail账户或执行发布；没有原始工时、客户账目或编辑采纳记录。完整翻译仅限许可目录，外部文章只保存短摘要，未取得第三方新闻或图片再发布权。

## 具体动作与止损条件

用三份虚构来源测试冲突、图片缺权与重复请求，输出草稿清单，不连接真实账户或发布。

停止投入条件：虚构引语、错认人物、资料泄露或越权发布即停止；审核后无净节省或持续负贡献不扩大。

## 来源与对应关系

- [Sdirectory] [许可目录现场正文](https://agentusecases.ai/use-case/publish-local-news-posts-to-wordpress-automatically)：目录记载本地新闻HTML、WordPress上传及三篇一次请求；90分钟与单轮对话均为作者自述。
- [Soriginal] [Koka Sexton营销运营文章](https://kokasexton.com/claude-code-marketing-ops-power-tool/)：文章页面显示2026-05-26，与目录来源日期不同；描述终端跨工具工作流与先验证建议，没有独立计时或完整代码。作者同时提供营销服务。
- [Swp] [WordPress WP-CLI创建文章](https://developer.wordpress.org/cli/commands/post/create/)：post_status默认draft；porcelain可返回新文章ID。创建成功不验证新闻内容真实性。
- [Srest] [WordPress文章REST API](https://developer.wordpress.org/rest-api/reference/posts/)：支持draft/pending/publish等状态和featured_media字段，并可按ID回读；文档更新2026-10-14。
- [Sap] [AP新闻室AI标准更新](https://www.ap.org/the-definitive-source/announcements/ap-updates-newsroom-standards-for-artificial-intelligence/)：2026-07-23更新强调发表前人工审阅及新闻摄影限制；这是AP内部政策，不是所有媒体的法律结论。
- [Scompetitor] [n8n WordPress草稿模板](https://n8n.io/workflows/2187-write-a-wordpress-post-with-ai-starting-from-a-few-keywords)：公开模板生成结构、HTML、草稿和特色图，建议人工审阅后发布；未证明新闻事实核查或实际用户效果。
- [Spermissions] [Claude Code权限配置](https://code.claude.com/docs/en/permissions)：官方提供allow/ask/deny等权限规则；配置能力不证明作者的真实账户范围或安全隔离已审计。
- [Sadjacent] [Local News Matters新闻室实施经验](https://localnewsmatters.org/2026/04/23/a-playbook-for-newsrooms-revolutionizing-election-coverage-with-ai-part-ii/)：相邻选举结果自动化经验强调现场监控、验证和人工介入；不是本案例新闻写作流程复现，也不是无人值守证明。

结构化记录：[research/publish-local-news-posts-to-wordpress-automatically.json](../research/publish-local-news-posts-to-wordpress-automatically.json)
