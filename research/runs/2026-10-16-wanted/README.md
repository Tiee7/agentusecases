# Wanted 计数核查与翻译清单

本次基于 e835ecf，未更改 UI、已有中文译文或任何案例的 Wanted 字段。

公开 robots.txt 禁止 `/api/`。公开应用脚本显示票数由 `/api/votes` 加载，因此未发送该请求。允许的详情页返回 200，浏览器按钮显示 `I want this`，没有数值。浏览器同时报告脚本错误，不能声称完成了动态加载；即使空按钮正常显示，脚本也会隐藏零值，因此空按钮仍不能证明为零。

非敏感核查凭据见 [probe.json](probe.json)。原始 HTML、脚本和截图只留在忽略的本地 data/；未发布私人许可、聊天、凭据或外部文章。

新增解析器支持实际按钮分隔符 `I want this · N`，仅接受明确整数；未知仍为 null。翻译清单按已观测 Wanted 降序、同值 slug 排序；已完成且源文哈希匹配的中文全文译文排除。未观测条目单独列出，不赋 Wanted 排名。

运行 `python -m agentwatch.wanted --output registry/translation-queue.json` 可重新生成清单。当前 1,359 条中 7 条已译、1,352 条待译；已观测 Wanted 排名为空，故没有可信的 Wanted 前20及奇偶分工。下列仅为未知池按 slug 排序的前20，甲奇乙偶是临时防重分组，须由协调线程决定是否使用，不能称为热门优先。

| 临时序号 | 组 | slug | Wanted |
|---:|:---:|---|---|
| 1 | 甲 | add-61-kid-friendly-mini-games-to-an-app | 未知 |
| 2 | 乙 | add-a-battle-of-alesia-expansion-to-a-1990s-game-remake | 未知 |
| 3 | 甲 | add-a-third-party-api-integration-via-devin-pr | 未知 |
| 4 | 乙 | add-agentic-forgetting-to-an-agent-s-memory | 未知 |
| 5 | 甲 | add-family-to-a-dental-plan-by-voice-from-the-car | 未知 |
| 6 | 乙 | add-handwritten-appointments-to-calendar-and-file-pdfs | 未知 |
| 7 | 甲 | add-home-todo-items-by-telegram-message | 未知 |
| 8 | 乙 | add-todo-items-to-todoist-from-telegram | 未知 |
| 9 | 甲 | add-travel-bookings-from-email-to-calendar | 未知 |
| 10 | 乙 | alert-ai-agencies-to-businesses-with-bad-reviews-as-leads | 未知 |
| 11 | 甲 | analyze-10-ks-for-value-investing | 未知 |
| 12 | 乙 | analyze-170k-llm-logs-overnight | 未知 |
| 13 | 甲 | analyze-a-piano-recording-s-bpm-structure-and-stems | 未知 |
| 14 | 乙 | analyze-budgets-and-research-investments-from-bank-data | 未知 |
| 15 | 甲 | analyze-competitor-ads-and-generate-on-brand-ad-creatives | 未知 |
| 16 | 乙 | analyze-garmin-data-for-meal-planning-and-health-patterns | 未知 |
| 17 | 甲 | analyze-your-chess-games-into-commented-videos | 未知 |
| 18 | 乙 | analyze-youtube-thumbnails-from-channel-analytics | 未知 |
| 19 | 甲 | answer-after-hours-calls-and-book-appointments | 未知 |
| 20 | 乙 | answer-business-phone-calls-with-a-voice-agent | 未知 |
