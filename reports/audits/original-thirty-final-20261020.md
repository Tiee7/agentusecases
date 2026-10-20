# 原批次30例：最终逐案审查与修订

审查记录时间：2026-10-20T17:48:58.466078+00:00。固定原批次，不重新取今天的/new前30条。

状态：已完成。逐案修订、104项Python、24项站点测试、93项远端浏览器测试、构建输出、合并和精确回读均通过。

## 范围与证据口径

保留11篇完整深研、19篇有依据简报；没有把30篇都称为深研，也没有统一降级。逐案比对原批次记录，30/30与本轮修订前基线一致。已存许可英文原文、完整中文译文及其SHA-256均保持原样。价格、政策和产品能力沿用各案注明的读取日期，不称本轮重新浏览验证；本轮是最终资料审查与修订，不是经营或产品实测。

## 实质修复

- 餐厅案例：撤掉用户未指定的200美元/四周门槛；价格与评分未知，20单/月同口径成本情景包含设置摊销与维护。低/高情景320与583.3333美元/月只是预算，不是账单或利润。
- 12篇简报：已保存Copy prompt但使用了错误状态枚举available，统一修为collected；模板内容未改。新增固定批次验证覆盖这些简报，避免只校验深研而漏过。
- 购物案例：方法来源缺尾斜杠导致无法与读取回执严格对应，现引用实际读取URL与时间，同时保留原注册链接。
- HTML课件：方法摘录来自引用教师的文章，标签改为“报道摘要”；教师原帖证据仍独立保留。
- 餐厅Markdown：中文默认展开，英文折叠；作者来源与分析分开，站点由结构记录渲染。

## 逐案可核对清单

|序|原slug与交付|类型|核对结果及保留边界|修订|状态/下一步|
|---|---|---|---|---|---|
|1|[track-personal-investments-with-a-claude-built-portfolio-tra](../brief/track-personal-investments-with-a-claude-built-portfolio-tra.md)|简报|原作者手动表格/PWA不等于已验证XIRR；演示404、代码和视频不可得，保留简报；旧API价格与已读现价分开。|source_prompt_status available → collected；保留完整原模板与来源归属|已完成；保留所列证据边界|
|2|[find-errors-in-production-agent-traces](../find-errors-in-production-agent-traces.md)|深研|523个厂商困难样本、F1 0.835和特定上下文23倍速度不外推；OSS不等于Signals模型权重开放，隐私模式与训练说明保留。|既有内容核验后保留|已完成；保留所列证据边界|
|3|[book-a-restaurant-table-and-add-it-to-the-calendar](../book-a-restaurant-table-and-add-it-to-the-calendar.md)|深研|已撤掉四周200美元/固定画像准入门槛和无依据总分；改为同样20单/月的完整成本压力测试，收入未知；预算失误与弃用反证仍保留。|经营判断、同口径成本、未知分数、自用维护、中文展开/英文折叠及索引同步修正|已完成；保留所列证据边界|
|4|[order-ice-cream-delivery-and-build-schedule-spreadsheets](../brief/order-ice-cream-delivery-and-build-schedule-spreadsheets.md)|简报|媒体二手报道不是独立计时实验；必要操作审批不算失败；历史Operator价格与退出时间按原日期保留。|既有内容核验后保留|已完成；保留所列证据边界|
|5|[research-hedge-fund-portfolios-from-13f-filings](../research-hedge-fund-portfolios-from-13f-filings.md)|深研|实际Finance代码项目与目录推荐Manus分开；固定代码版本、外部数据依赖、13F报告期/提交日/单位及不含空头边界保留。|既有内容核验后保留|已完成；保留所列证据边界|
|6|[build-code-with-agents-while-keeping-a-working-understanding](../brief/build-code-with-agents-while-keeping-a-working-understanding.md)|简报|四项理解原则不是可运行验证器；相邻grill-me不是作者实现，解释清楚不等于理解正确。|source_prompt_status available → collected；保留完整原模板与来源归属|已完成；保留所列证据边界|
|7|[move-twitter-follows-over-to-bluesky](../brief/move-twitter-follows-over-to-bluesky.md)|简报|作者仍在迁移，不写成全部完成；实际工具未知，身份跨链匹配与免费局部替代保留。|既有内容核验后保留|已完成；保留所列证据边界|
|8|[interview-candidates-based-on-their-resume](../interview-candidates-based-on-their-resume.md)|深研|n8n实际实现与Claude试用推荐分开；权限、RLS、人工招聘判断与未来计划分开，欧元订阅和美元模型不直接相加。|既有内容核验后保留|已完成；保留所列证据边界|
|9|[run-personal-assistant-tasks-like-medical-data-and-finance-r](../brief/run-personal-assistant-tasks-like-medical-data-and-finance-r.md)|简报|四个机器人仅三项可辨；共享电脑不等于权限隔离；血糖单位/时间/缺失提示不代表临床有效，不接真实资料。|既有内容核验后保留|已完成；保留所列证据边界|
|10|[reorder-low-stock-from-suppliers-automatically](../reorder-low-stock-from-suppliers-automatically.md)|深研|7人14种产品、700搭建/60月费/40分钟均作者自述；实际平台未知；重复采购、Flow限制与现成软件/服务差异保留。|既有内容核验后保留|已完成；保留所列证据边界|
|11|[find-seo-competitors-with-chatgpt-pro-agent](../brief/find-seo-competitors-with-chatgpt-pro-agent.md)|简报|25%访问增长无基线或归因，不能称搜索点击或收入；先未读后重读的来源时间线保留。|source_prompt_status available → collected；保留完整原模板与来源归属|已完成；保留所列证据边界|
|12|[handle-family-logistics-reminders-and-research-with-a-person](../brief/handle-family-logistics-reminders-and-research-with-a-person.md)|简报|提醒确认不等于服药完成；家庭资料权限和重复剂量风险独立列明；自编HomeDepot例子不冒充原案例。|既有内容核验后保留|已完成；保留所列证据边界|
|13|[write-and-review-contracts-with-chatgpt](../brief/write-and-review-contracts-with-chatgpt.md)|简报|2023原帖与2026目录收录日期分开；原帖失败读取不伪造步骤；ABA资料适用范围不外推全世界。|source_prompt_status available → collected；保留完整原模板与来源归属|已完成；保留所列证据边界|
|14|[audit-seo-and-ai-search-visibility-with-an-agent](../audit-seo-and-ai-search-visibility-with-an-agent.md)|深研|TargetPilot多agent评论与MentionDesk作者分开；品牌提及、引用、访问、订单分开；失败请求不计品牌缺席，厂商品牌数不算客户。|既有内容核验后保留|已完成；保留所列证据边界|
|15|[review-contracts-and-check-consumer-protection-rules-with-le](../brief/review-contracts-and-check-consumer-protection-rules-with-le.md)|简报|消费者保护agent只是想法，不写成部署；商业隐私、留存和旧价均有限定，无法读取FTC不补造。|source_prompt_status available → collected；保留完整原模板与来源归属|已完成；保留所列证据边界|
|16|[book-site-visits-and-follow-up-with-real-estate-leads](../book-site-visits-and-follow-up-with-real-estate-leads.md)|深研|拒绝一次看房与拒绝联系不同；布尔状态/freebusy不提供预约锁，WhatsApp同意、窗口、退出与失败回执保留。|既有内容核验后保留|已完成；保留所列证据边界|
|17|[run-real-estate-operations-with-a-memory-equipped-assistant](../brief/run-real-estate-operations-with-a-memory-equipped-assistant.md)|简报|向量记忆不等于实时房价；会话身份和服务密钥/RLS有区别，咨询意向不是销量；成熟预约工具只覆盖部分流程。|source_prompt_status available → collected；保留完整原模板与来源归属|已完成；保留所列证据边界|
|18|[find-tattoo-clients-on-reddit-and-draft-replies](../brief/find-tattoo-clients-on-reddit-and-draft-replies.md)|简报|纹身获客仍为设想，无真实pipeline；GummySearch停止新用户及关停日期保留，电话按钮点击不算到店。|既有内容核验后保留|已完成；保留所列证据边界|
|19|[turn-meeting-transcripts-into-decks-and-organize-sharepoint-](../brief/turn-meeting-transcripts-into-decks-and-organize-sharepoint-.md)|简报|两个人两项任务不能合并成已实现系统；Move/Copy/版本语义分开，转录、幻灯和来源事实需一致。|source_prompt_status available → collected；保留完整原模板与来源归属|已完成；保留所列证据边界|
|20|[run-daily-business-operations-on-a-dedicated-agent-machine](../brief/run-daily-business-operations-on-a-dedicated-agent-machine.md)|简报|每周两三小时是负担自述，不是净省时；专用机器不自动隔离账户，OpenClaw仅推荐模板，原帖受限不绕过。|source_prompt_status available → collected；保留完整原模板与来源归属|已完成；保留所列证据边界|
|21|[turn-meeting-notes-into-a-prioritized-daily-action-list](../turn-meeting-notes-into-a-prioritized-daily-action-list.md)|深研|原博客1月25日与目录10月18日分开；省时/两千笔记自述不当收入；原文不可覆盖、重复任务和变更截止需留证据。|既有内容核验后保留|已完成；保留所列证据边界|
|22|[add-groceries-buy-on-amazon-and-price-shop-flights](../brief/add-groceries-buy-on-amazon-and-price-shop-flights.md)|简报|实际使用者是评论者而非征集记者；三类购物动作不等同下单成功；修正作者方法URL尾斜杠及读取时间，使其与原回执完全对应。|source_prompt_status available → collected；保留完整原模板与来源归属；来源URL与实际读取回执严格一致；注册列表增补原网址别名，不删原链接|已完成；保留所列证据边界|
|23|[negotiate-a-car-purchase-with-chatgpt](../negotiate-a-car-purchase-with-chatgpt.md)|深研|三千美元是家长自述，换车条件/店/家庭帮助同时变化；只比较同条件书面总价，不归因模型、不代签约或借贷决策。|既有内容核验后保留|已完成；保留所列证据边界|
|24|[run-literature-reviews-over-a-folder-of-papers](../brief/run-literature-reviews-over-a-folder-of-papers.md)|简报|50篇30分钟等是宣传自述，没有完整输出；lit-map命令和目录模板文件名分开，引用次数不等于重要性。|source_prompt_status available → collected；保留完整原模板与来源归属|已完成；保留所列证据边界|
|25|[redline-lawyer-documents-with-native-word-tracked-changes](../redline-lawyer-documents-with-native-word-tracked-changes.md)|深研|30页两段修改自述不等于法律质量；原生修订/批注可用性和机构许可、审计日志/Compliance API/留存分开。|既有内容核验后保留|已完成；保留所列证据边界|
|26|[automate-content-distribution-across-reddit-and-linkedin](../brief/automate-content-distribution-across-reddit-and-linkedin.md)|简报|原文日期与收录日期分开；六小时检查是作者描述，发帖审批不省略；每周改提示词不是训练模型权重。|source_prompt_status available → collected；保留完整原模板与来源归属|已完成；保留所列证据边界|
|27|[run-agent-builds-and-tests-on-remote-windows-vms](../brief/run-agent-builds-and-tests-on-remote-windows-vms.md)|简报|Windows宿主不等于原生Windows测试；雇主VM不是人人免费；提交与日志绑定为建议，无SSH或真实远端执行。|source_prompt_status available → collected；保留完整原模板与来源归属|已完成；保留所列证据边界|
|28|[generate-custom-interactive-html-lessons-for-students](../generate-custom-interactive-html-lessons-for-students.md)|深研|只真实检查相邻游戏一道题和Team1计分，不称整课/离线/手机通过；9.99是历史宣传，学习成效和资源销量未知。|方法归属修为报道摘要；保留教师原帖独立来源|已完成；保留所列证据边界|
|29|[build-home-assistant-automations-with-claude](../brief/build-home-assistant-automations-with-claude.md)|简报|原帖受限保留；10分钟为自述非基准；MCP权限与Run action跳过触发条件风险保留，仅建议虚拟实体测试。|既有内容核验后保留|已完成；保留所列证据边界|
|30|[order-from-a-restaurant-menu-photo-with-chatgpt](../brief/order-from-a-restaurant-menu-photo-with-chatgpt.md)|简报|菜单识图结果由服务员人工处理，不是餐厅系统下单；识别错误/过敏交叉接触不可由图片保证，适合简报。|既有内容核验后保留|已完成；保留所列证据边界|

## 复核方法与未完成项

逐案核对商业需求/收入机制/获客交付/成本复制条件、自用人群/收益/设置维护/频率/隐私错误、原agent/工具/Copy prompt/准备与预期；数据缺失继续明确未知，不为了提高评分编造收益。独立来源与转载、厂商与用户自述、历史功能与当前已读资料分开。

可重复检查：PYTHONPATH=. python research/runs/2026-10-20-original-thirty-final/verify.py。检查原文译文哈希与前基线完全相同、来源引用、方法回执、试用模板、11篇深研schema及全部30篇自用结构，另算餐厅成本。

完整证据见 [完成回执](../../research/runs/2026-10-20-original-thirty-final/completion.json)。[PR85](https://github.com/Tiee7/agentusecases/pull/85) 已合并，[CI39469837001](https://github.com/Tiee7/agentusecases/actions/runs/39469837001)通过，研究main提交 b41cf72f6c453c9c3ab98bf48805efc76320ea0d；28份变更文件逐字回读，合并树与本地完全一致，报告回读完成于2026-10-20 17:59:47 UTC。测试证明研究数据与阅读站交付，不证明原作者产品或商业结果。
