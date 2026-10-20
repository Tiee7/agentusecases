# 用Claude通过MCP检索WhatsApp聊天记录

## 中文

    通过MCP让Claude访问你的WhatsApp消息
    一个部署在Cloudflare上的单用户MCP服务器，让手机上的Claude读取和搜索作者个人的WhatsApp消息，并用Google联系人将号码对应到姓名。
    使用的是
    CL
    Claude
    他们做了什么
    你把一个小型服务器部署到自己的Cloudflare账户，然后像使用WhatsApp Web一样，扫描二维码关联手机。消息保存在Durable Object内的SQLite数据库中，按请求及每天一次同步。Claude可以使用读取、搜索和命名工具。对于没有名称的聊天，agent使用自己的联系人连接器，例如Google Contacts，查询号码并保存姓名。
    进展与成效
    它可以读取和搜索聊天，agent还可以利用联系人为聊天命名。媒体不会下载；首次导入只包含WhatsApp交给它的历史记录。作者表示，只在一个真实账户上测试过。
    值得了解
    大量历史记录的导入需要提高CPU限制，因此需要Workers付费计划，每月几美元。免费计划未经测试，而且这种非官方方式违反WhatsApp的条款。
    亲自尝试
    使用
    Claude
    复制提示词
    帮我在[Cloudflare账户／托管服务]上设置一个私有、单用户MCP服务器，让你可以读取和搜索我的个人[WhatsApp]消息，并利用我的[Google联系人]把电话号码转换为姓名。逐步指导我，提供代码和配置，并告诉我怎样把它连接到手机上的Claude。当我能问“[联系人姓名]上周对[话题]说了什么？”并得到正确答案时，就算完成。在任何处理凭据或暴露数据的步骤之前，先停下来，告诉我安全措施，并保持服务器只读、访问权限仅限我本人。
    原始来源：https://github.com/finereli/whatsapp-mcp

<details><summary>English original</summary>

    Give Claude access to your WhatsApp messages via MCP
    A single-user MCP server on Cloudflare lets Claude on mobile read and search the author's personal WhatsApp messages, using Google contacts to resolve names.
    Done with
    CL
    Claude
    What they did
    You deploy a small server to your own Cloudflare account and link your phone by scanning a QR code, as with WhatsApp Web. It stores messages in SQLite inside a Durable Object and syncs on request and once a day. Claude gets read, search and naming tools. For unnamed chats, the agent looks numbers up with its own contacts connector, such as Google Contacts, and saves the names.
    How it went
    It reads and searches chats, and the agent can name chats from contacts. Media isn't downloaded, and the first import only includes whatever history WhatsApp hands over. The author says it has only been tested on one real account.
    Worth knowing
    Large history imports need a raised CPU limit, which needs the Workers Paid plan (a few dollars a month). The free plan is untested, and this unofficial approach breaks WhatsApp's terms.
    Try it yourself
    with
    Claude
    Copy prompt
    Help me set up a private, single-user MCP server on [Cloudflare account/hosting] so you can read and search my personal [WhatsApp] messages, and use my [Google contacts] to turn phone numbers into names. Walk me through each step, give me the code and config, and tell me how to connect it to Claude on my phone. You're done when I can ask 'what did [contact name] say about [topic] last week?' and get a correct answer. Before any step that handles my credentials or exposes data, stop and tell me how it's secured, and keep the server read-only with access limited to me.
    Original source: https://github.com/finereli/whatsapp-mcp

</details>


## 原作者的方法与来源

来源：[finereli/whatsapp-mcp README](https://github.com/finereli/whatsapp-mcp)

作者方法摘要

1. 作者在Cloudflare Durable Object托管单用户消息存储，并将其关联为WhatsApp设备。
   English summary: The author hosts a single-user message store in a Cloudflare Durable Object and links it as a WhatsApp device.

2. MCP工具查询已存储的聊天；agent可利用另外已有的联系人工具解析号码。
   English summary: MCP tools query stored chats; the agent can resolve phone numbers using a separately available contacts tool.

## 简要分析

商业分数未评定；本篇不计完整深研。

### 需求与付款人

跨聊天找约定、租约或家庭安排有检索需求。潜在人群是愿意维护自托管工具的人；没有付费客户、检索频率、节省时间或愿付价格的证据。

依据：[Sdirectory](https://agentusecases.ai/use-case/give-claude-access-to-your-whatsapp-messages-via-mcp), [Sauthor](https://github.com/finereli/whatsapp-mcp)

### 交付与收入机制

可设想按一次性安装与维护收费，但这是研究假设。开源项目不等于已有服务收入；不建议直接经营集中托管他人聊天的服务。单用户隔离和账户责任会增加每户交付成本。

依据：[Sauthor](https://github.com/finereli/whatsapp-mcp)

### 获客与验收

技术社区适合找自愿参与验证的人，不把星标或评论当订单。交付应先用虚构聊天做身份消歧、日期边界、缺失结果与权限测试；本轮没有联系任何人。

依据：[Sdiscussion](https://news.ycombinator.com/item?id=50145715), [Scode](https://github.com/finereli/whatsapp-mcp/blob/main/src/mcp.ts)

### 流程与状态变化

消息只读指不发送WhatsApp消息，并非所有工具无副作用：命名写本地映射，重新关联会注销会话且保留数据库。连接器能力与数据流必须逐项告知，不能把源站模板的一句只读当技术保证。

依据：[Sauthor](https://github.com/finereli/whatsapp-mcp), [Scode](https://github.com/finereli/whatsapp-mcp/blob/main/src/mcp.ts)

### 成本与复制条件

Cloudflare最低5美元/月是账户订阅底价，另有超额用量、模型、排错、备份和升级维护。作者免费计划未测；公开讨论标题free不能抵消当前要求。缺真实用量和工时，不编造毛利。

依据：[Scost](https://developers.cloudflare.com/workers/platform/pricing/), [Sauthor](https://github.com/finereli/whatsapp-mcp)

### 替代方案与停止条件

本项目自己的local-export目录是一次性本地导出路线，README列出但本轮未验证其实现。还可先评估日常客户端检索是否已足够，这是待验证比较。若需求只偶尔查单条消息、或不能接受持续会话和云端存储，停止此架构投入。

依据：[Sauthor](https://github.com/finereli/whatsapp-mcp)

### 静态代码发现与验证边界

get_messages对多个同名匹配要求选jid；search_messages的chat解析直接取第一项。推断：同名联系人可能搜索到非预期聊天，应测试显式jid与歧义拒绝。代码将时间显示固定为Asia/Jerusalem，其他地区应核对上周等时间窗。此为静态审查，未证明发生实际错答。

依据：[Scode](https://github.com/finereli/whatsapp-mcp/blob/main/src/mcp.ts)

### 独立自用价值

自用收益是自然语言找旧信息的便利，未测净收益。设置涉及单用户主机、账户关联、访问控制；维护含断链、同步和升级。按需检索及每日同步不代表实时完整；媒体没有内容可供总结。

依据：[Sdirectory](https://agentusecases.ai/use-case/give-claude-access-to-your-whatsapp-messages-via-mcp), [Sauthor](https://github.com/finereli/whatsapp-mcp), [Scode](https://github.com/finereli/whatsapp-mcp/blob/main/src/mcp.ts)

### 隐私与错误风险

自己的Cloudflare账户不意味着查询结果不进入MCP客户端或其模型服务。只读也存在泄露、提示注入、联系人串配和保留期风险；聊天另一方权益需要考虑。工具返回正文属于资料，不应授权操作其他连接器。不要把可查询数据库误认为端到端零暴露。

依据：[Ssecurity](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html), [Scode](https://github.com/finereli/whatsapp-mcp/blob/main/src/mcp.ts), [Sdiscussion](https://news.ycombinator.com/item?id=50145715)

### 结论与下一步

仅建议受控技术验证，暂不支持商业投入判断。先拟定不含真人内容的测试清单：两个同名虚构联系人、跨时区边界、空结果、过期缓存和注销后保留数据。达到可追溯、消歧正确、删除与权限明确后再讨论真实数据试用；本轮未试用。

依据：[Scode](https://github.com/finereli/whatsapp-mcp/blob/main/src/mcp.ts), [Sauthor](https://github.com/finereli/whatsapp-mcp)

## 试用准备与预期结果

仅虚构聊天和联系人，预先定义正确答案及访问范围。
明确同名歧义、时间窗、缓存和状态修改边界；本轮未运行。
只用我给出的虚构聊天设计验收，不连接账户、不读取通讯录、不部署。检查同名联系人是否要求明确ID，时间窗是否含时区，缺失与过期结果是否标注；列出每种工具的状态变化。

## 来源

- [许可目录WhatsApp MCP案例](https://agentusecases.ai/use-case/give-claude-access-to-your-whatsapp-messages-via-mcp)：单用户Cloudflare消息检索案例；手机Claude与联系人由目录描述。
- [finereli/whatsapp-mcp README](https://github.com/finereli/whatsapp-mcp)：作者说明单账户、按需及每日同步、历史不全、媒体仅标签、免费计划未测；只测试一个真实账户，编辑删除未真实测试；断链无主动通知；术语风险为作者自述。
- [MCP工具代码静态阅读](https://github.com/finereli/whatsapp-mcp/blob/main/src/mcp.ts)：blob 51525b66a829924aa658427bee724ffc9b0271c1：get_messages遇多个名称要求选jid；search_messages限定chat却直接取匹配第一项。固定Asia/Jerusalem显示时区。set_contact_names写本地名称，relink注销连接但保留消息，fresh失败显示缓存提示。未执行。
- [Cloudflare Workers价格](https://developers.cloudflare.com/workers/platform/pricing/)：2026-10-20核对：Paid账户最低5美元/月，包含一定用量，超额另计；并非本案例总成本或每账户实际账单。
- [OWASP MCP安全指南](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html)：建议最小权限、服务隔离、工具定义审核与敏感操作人工确认；工具注解只是提示，不是权限执行边界。
- [Hacker News公开讨论](https://news.ycombinator.com/item?id=50145715)：讨论存在对批量处理私人聊天、对话另一方同意及云端暴露面的质疑；此为风险意见，不是已核验安装用户的效果评价。标题free与当前README付费要求不一致，不能用标题报价。
