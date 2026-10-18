# 用 OpenClaw 整理兽医费用并起草宠物保险理赔

## 中文

    把兽医费用转成可发送的宠物保险理赔材料
    一个个人OpenClaw agent从银行流水中识别兽医费用，在Gmail找到发票，填写保险公司的PDF表单，起草邮件并跟踪回复，供主人审阅和发送。
    实际使用
    OpenClaw
    具体做法
    主人手动上传银行CSV，因为agent从不保存银行登录凭据。agent每十五分钟运行一次，标记兽医费用，在Gmail搜索对应发票，并使用大语言模型Gemini提取内容；扫描件则回退使用OCR。它填写Petcover PDF，建立Gmail草稿，遇到不确定情况时通过Telegram询问。它从不发送邮件。
    结果如何
    在十份真实批准信上，它的结算算术检查准确到分；另一项检查对其中五份提出疑问。早期错误包括：把自己发出的请求邮件误匹配到十二笔理赔，以及旧的确认邮件让两笔已结算理赔的状态倒退。
    值得知道
    测试模式下的Gmail OAuth每七天失效，因此必须定期重新认证；免费Gemini额度在每日用尽后，需要一串备用模型来接续。
    自行试用
    推荐工具
    OpenClaw
    复制提示词
    扫描我最近[时间范围]的[银行账户或对账单]，找出兽医费用，在邮件中找到相应发票，并用它们填写[保险公司]的理赔表。起草理赔邮件，附上表单与发票，最后向我展示理赔草稿。未经我批准，不要发送任何内容。
    原始来源：https://github.com/jagberg/Me.OpenClaw

<details>
<summary>English</summary>

<pre>Turn vet charges into ready-to-send pet insurance claims
A personal OpenClaw agent spots vet charges in the bank feed, finds the invoice in Gmail, fills the insurer&#x27;s PDF form, drafts the email and tracks replies for the owner to review and send.
Done with
OC
OpenClaw
What they did
The owner uploads a bank CSV by hand, since the agent never stores bank logins. On a 15-minute tick the agent flags vet charges, searches Gmail for the matching invoice, and uses an LLM (Gemini) to extract it, falling back to OCR for scans. It fills the Petcover PDF, creates a Gmail draft, and asks on Telegram when unsure. It never sends.
How it went
Across ten live approval letters, its settlement arithmetic check passed to the cent, and a second check raised questions on five. Early bugs: its own request emails false-matched 12 claims, and old acknowledgements pushed two settled claims backwards.
Worth knowing
Gmail OAuth in testing mode expires every 7 days, so you must re-authenticate regularly; the free Gemini tier needed a chain of fallback models once daily limits ran out.
Try it yourself
with
OpenClaw
Copy prompt
Scan my [bank account or statement] for vet charges from the last [timeframe], find the matching invoices in my email, and fill out [insurer]&#x27;s claim form with them. Draft the claim email with the form and invoice attached, and finish by showing me the drafted claim. Don&#x27;t send anything until I approve it.
Original source: https://github.com/jagberg/Me.OpenClaw</pre>

</details>

## 原作者的方法与来源

[公开README](https://github.com/jagberg/Me.OpenClaw)，以下为方法摘要及对应翻译，不是原文全文。

Start from an uploaded bank CSV, identify veterinary charges, and match them to invoice attachments.

从上传的银行CSV开始，识别兽医支出，并匹配发票附件。

Extract the invoice fields, prepare claim PDFs and stage Gmail drafts for human review.

提取发票字段，准备理赔PDF，并建立供人审阅的Gmail草稿。

Record insurer-reply events and compare settlement figures; surface ambiguous matches and assessment differences for review.

记录保险方回复事件并核对结算数字，将模糊匹配和评估差异交给人复核。

## 我们的简要分析

商业判断：先做小范围材料与状态核对试点；商业分数未评定。自用价值：中。

### 输入、匹配与草稿

本例从用户手动上传银行CSV开始，并不是代理登录银行获取完整账户。交易只提供线索，真正填表还要从发票核对宠物、就诊日期、费用项目及申报金额。作者README描述缺失必填项或模糊匹配时提问，而不是猜测；发票缺失、扫描不清和一笔付款涉及多只宠物都需要单独处理。可复制的价值是把“交易—发票—表单—草稿—回复”串成可审阅记录，并保留人工决定和发送。

### 十份核对能说明什么

作者报告的Check A，是把结算信已经打印的数字重新计算，十份信均对到分；它不是保险条款模型，也不是抽取、匹配或理赔全流程100%准确。Check B比较保险方评估金额与已记录的申报小计，对五份提出问题，不能据此认定五次少赔或额外追回款。早期自身请求邮件误匹配十二笔、旧确认信让两笔已结案记录倒退，说明去重、发件来源和状态顺序是实际交付难点。现有数字仍是作者自述，没有独立审计或节时记录。

### 授权、状态与项目边界

Google文档的七天限制适用于外部用户类型、发布状态为Testing的OAuth刷新token，并有仅身份基础scope的例外；不能写成所有Gmail授权每七天必然失效。Gmail API把创建草稿和发送分成不同操作，但“只显示草稿”本身不能证明程序绝无发送路径。作者README还同时保留网关迁移说明，项目名Me.OpenClaw与另一个OpenClaw网关并非同一个组件；应按部署版本核对连接方式，不能把此例包装为安装标准技能就自动具备的能力。状态事件需保留原始时间，旧确认不能覆盖已结算事实。

### 个人使用与维护

自用价值为中，适合经常产生兽医账单、愿意逐笔确认的宠物主人。一次偶发理赔可能用保险方现有表单和邮件模板就够了；多宠物、多发票与持续补件才更需要匹配台账。准备时先用脱敏CSV、发票、空表和保单字段做样例，确认哪些项目必须由人填写。每次检查附件、宠物、申报金额和收件人，定期看授权失效、额度耗尽及错误状态。银行登录不进入代理，不代表邮件、银行导出及宠物资料没有隐私风险。

### 付费交付与成本

潜在付款人是反复整理材料的主人，或愿意购买行政整理支持的服务机构；现有资料没有客户付费、续费或独立效果反馈。真正可收费的交付是核对完整的材料草稿与待确认项，不是保证获赔或代替保险方判断。仅作测算：每份收费35美元，人工15分钟×30美元/小时=7.5美元，模型/提取2美元、存储与工具2美元、获客摊销5美元，贡献18.5美元，尚未扣固定费；复杂单需一小时人工时贡献变为负4美元。假设400美元设置服务，8小时×35美元人工、20美元测试、10美元工具、40美元获客，贡献50美元，多两小时返工就转负。这些均非作者费用或市场报价。

### 先验证的五类样例

先用脱敏或合成材料验证：正常一单、一笔付款含多张发票、发票缺失、自己发出的请求邮件、已结算后又收到旧确认信。验收重点是金额与附件可追溯、未知不补猜、同一发票不重复申报、旧信不使状态倒退。随后再比较真实手工整理时间；若复核不减、授权维护过重或特定保险流程尚未核实，就缩小为离线材料清单。本次未运行作者项目、访问银行或Gmail、调用模型、填写真实表单或发送任何消息。

## 试用准备

源站模板原文已完整保留在上方原文与译文中。

准备：脱敏交易、发票、空白表、人工确认的宠物/保单字段与历史状态样例。

预期：匹配表、待确认项、表单与邮件草稿及附件清单；自编模板未实测，不承诺获赔。

### 用脱敏资料整理宠物理赔草稿

研究团队自编，未实测。

    请仅使用我提供且已脱敏的[银行CSV、发票、空白理赔表、保单中需填字段、历史状态样例]整理一份待人工确认的宠物保险理赔材料。按交易、发票号、宠物与就诊日期匹配，列出银行支出、发票金额、拟申报小计和证据，不能把它们混为同一数值。金额不匹配、一笔付款多宠物、附件缺失或字段未知时单列问题，不猜诊断、保单覆盖或收款信息。排除自己发出的索票邮件，已结算项目不能因旧确认信退回处理中。输出表单草稿、附件清单、邮件正文草稿及逐项确认表后停止。不要登录银行或邮箱、读取或创建凭据、调用额外付费模型API、提交理赔或发送消息；由我自行核对并决定后续。

## 来源

- [案例归档](https://agentusecases.ai/use-case/turn-vet-charges-into-ready-to-send-pet-insurance-claims)，快照2026-10-17；不代表重新访问源站。
- [GitHub - jagberg/Me.OpenClaw: Personal agent that turns bank transactions into ready-to-send insurance claims. An experiment in what an agentic system should be allowed to do unsupervised. · GitHub](https://github.com/jagberg/Me.OpenClaw)：作者公开README的理赔流程、两类结算核对、状态事件与已报告错误；非独立理赔结果审计。
- [Using OAuth 2.0 to Access Google APIs  |  Authorization  |  Google for Developers](https://developers.google.com/identity/protocols/oauth2)：外部Testing状态OAuth刷新token七天有效期及范围例外，不能外推到所有Gmail授权。
- [Create and send draft emails  |  Gmail  |  Google for Developers](https://developers.google.com/workspace/gmail/api/guides/drafts)：Gmail草稿是未发送消息，创建和发送分别有API操作；草稿界面不能替代程序边界检查。
