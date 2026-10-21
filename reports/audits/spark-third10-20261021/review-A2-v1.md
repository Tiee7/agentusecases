# A2 邮件通知：第一轮定点返修

时间：2026-10-21 18:05 UTC。仅 track-incoming-emails-and-notify-about-key-ones，状态需返修、未最终验收。保留已读作者失败自述，不把返修误解为要改成正面结论。

## 已复核的边界

- 原帖确实有最近两封漏一封、8:50称无新信、随后两小时漏通知的自述。它不是公开原始邮件日志或可复现实验；不要称已经独立验证的精确召回率或故意“谎报”。可写错误报告/漏报，自述来源清楚。
- OpenAI公开说明写自主暂停/唤醒及定时任务，不足以确定此作者的实际插件、检索覆盖、触发配置或漏报根因。F9虽标推断，却断言没有挂载Gmail watch、注意力机制导致遗漏，应改成待验证假设并列可能路径，不能当已定位根因。
- Gmail官方明确推送可能延迟或丢失，并需定期history.list补同步。这直接否定开篇“Webhook/IMAP过滤器100%召回率”的无条件保证。Gmail界面过滤规则、IMAP客户端同步、Gmail API watch、Zapier具体触发器与轮询套餐是不同方案，不要合并为零成本即时可靠系统。

来源：
1. https://www.reddit.com/r/OpenAI/comments/1wu77gv/thoughts_on_dots/
2. https://learn.chatgpt.com/docs/dots （How dots work）
3. https://help.openai.com/en/articles/20001530-getting-started-with-your-dot （Scheduled tasks）
4. https://developers.google.com/workspace/gmail/api/guides/push （Reliability与Maximum notification rate）

## 返修要求

1. 全文、record.json与自检同步删除“100%召回”“任何商业交付首日必败”等超出证据的绝对断言，保留“不应作为时效敏感邮件唯一提醒渠道”的有据结论。
2. 所有召回率必须交代完整分母、是否同批/重复、观察窗与自述局限；无法确定就保留事件数量，不给产品总体百分比。小样本检查只是试点，不证明长期可靠。
3. 替代方案补失败恢复、漏事件补同步、去重、水位线/消息ID、令牌或watch续期、权限与消息投递链成本；不要将事件到达与用户最终看到通知当同一步。
4. 官方订阅总价不能全算邮箱提醒的新增成本又把已有Gmail当零成本，分开既有订阅边际成本与专为本任务新增订阅成本。保留同单位双情景和人工核对维护成本。
5. 对未知架构与商业可交付性保持明确推断，不用承认一个失败自述推出所有用户/所有配置失败。禁止测试真实用户邮箱或自行发送压力测试邮件。

只返修此案，保留v1，向OUTPUT-A提交v2与逐条CHANGELOG，STATUS/INDEX指向新版本但仍待审查。无需重复其他案例。主助手继续其余实质复核，本文不是最终整组报告。
