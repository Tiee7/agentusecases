# 来源核验记录

2026-10-20 05:59:43–06:00:15 UTC实际读取。

许可目录 https://agentusecases.ai/use-case/sync-monday-orders-to-xero-pos-invoices-and-bills 已用自有云浏览器读取，与现有英文档案核对。三条Make场景；生产运行、全测试是作者经目录转述，无交易量或结果数字。原Reddit已有明确安全限制，不读取替代路径或搜索摘录；第二Reddit来源也不当独立验证。未实际操作Monday、Make、Xero或发邮件。

https://help.make.com/scenario-settings 公开网页全文读取：webhooks默认并行，process data in order串行且未完成执行会阻塞后续；执行日志保留载荷，confidential选项减少保留但限制排错；存储满且discard启用会丢失失败数据。不能将状态设Needs Attention等同幂等重试或全部外部副作用回滚。

https://help.make.com/overview-of-error-handling 返回404，本轮没有再次读取；已有settings可支撑边界。

Xero两官方页web工具只返回JavaScript提示，不算正文成功。之后自有云浏览器读取 https://developer.xero.com/documentation/guides/idempotent-requests/idempotency/ 已正常呈现：POST/PUT/PATCH可传Idempotency-Key，相同请求用相同key；key仅缓存6分钟，过期后可能重处理；重复请求仍计速率。多次错误应GET核资源是否已创建，再决定新请求。文档示例段“changing its value each time”与前后规范叙述不一致，不引用该句作为建议。不能依赖6分钟缓存处理数小时后人工改状态重试，需持久记录目标ID、业务键及步骤状态。

https://developer.xero.com/documentation/api/accounting/invoices 尚未用浏览器读取正文，仅JS提示。待核票据类型、状态、邮件和附件边界。

本记录为研究时点笔记；后续简报、验证和真实完成记录分别保存。

06:00:44–06:01:01 UTC自有云浏览器已读取Xero Invoices正文：ACCPAY的InvoiceNumber非唯一，不能只靠PO reference盲选第一个bill。销售发票邮件只允许ACCREC且SUBMITTED/AUTHORISED/PAID，DRAFT不在发送状态。发给主要邮箱及IncludeInEmails联系人，API204是发送请求成功不是收件/付款证明。demo组织邮件额度0/日，trial20、付费1000，故目录“test mode先展示邮件样本”应落实为模拟输出或隔离测试收件人，不声称demo能真实发送。SentToContact置true是标记，不等于调用发送接口。这些是当前官方能力，不证明原作者实际采用特定接口/配置。
