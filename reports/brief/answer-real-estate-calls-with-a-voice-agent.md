# 用 n8n 和 ElevenLabs 接听房产咨询来电

分析深度：简要研究（brief）；商业评分未评定，不计入深研完成数。

## 案例完整中文译文

    用语音 agent 接听房地产来电
    一名开发者为一家房地产公司构建了一个使用 ElevenLabs 和 n8n 的语音 agent，用来接听电话、收集预算和地点信息，并将这些信息传入自动化工作流。
    实际使用
    n8n
    具体做法
    开发者为 Agape Real Estate 将 ElevenLabs 语音与 n8n 工作流连接起来。agent 接听来电、理解咨询内容、收集来电者的预算和地点信息，再将两项信息传入 n8n 自动化。集成和连接由开发者设置，来电处理则由 agent 端到端运行。
    结果如何
    该工作流现在将未接来电转化为团队可以跟进的有用线索。发布的视频演示了这一流程，但由于 Loom 的限制，没有录到 agent 的语音输出。
    值得注意
    Loom 没有在演示视频中录到 agent 的口头回复。
    自行试用
    推荐工具
    n8n
    复制提示词
    帮我为一个语音 agent 构建 n8n 工作流，用来接听[企业类型，例如房地产公司]的来电。它应向来电者询问[预算、地点和其他详情]，然后把答案保存到[CRM 或电子表格]，并触发向来电者发送后续跟进邮件。使用示例数据进行一次测试通话，并在工作流发送任何真实消息之前暂停，等待我批准。
    原始来源：https://x.com/oluwatomisint6/status/2106878686519587312

<details>
<summary>English · 完整归档原文</summary>

<pre>Answer real estate calls with a voice agent
A builder made an ElevenLabs and n8n voice agent for a real estate firm that answers calls, collects budget and location, and feeds an automated workflow.
Done with
N8
n8n
What they did
The builder connected ElevenLabs voice to n8n workflows for Agape Real Estate. The agent answers incoming calls, understands the enquiry, collects the caller&#x27;s budget and location, then passes both into the n8n automation. The person set up the integration and connections but the agent runs the call handling end to end.
How it went
The workflow now turns missed calls into usable leads the team can follow up. The posted video demonstrates the flow but omits the agent&#x27;s voice output due to Loom limits.
Worth knowing
Loom did not capture the agent&#x27;s spoken responses in the demo video.
Try it yourself
with
n8n
Copy prompt
Help me build an n8n workflow for a voice agent that answers inbound calls for [type of business, e.g. a real estate firm]. It should ask callers for [budget, location, and other details], then save the answers to [CRM or spreadsheet] and trigger a follow-up email to the caller. Run a test call with sample data, and pause for my approval before the workflow sends any real message.
Original source: https://x.com/oluwatomisint6/status/2106878686519587312</pre>

</details>

## 原作者的方法与来源

[X 原帖](https://x.com/oluwatomisint6/status/2106878686519587312)：依既有限制跳过，未新请求、重试、登录或换路；没有取得声音或视频。作者方法摘要不可用，建议模板不作为作者实现步骤。

## 我们的简要分析

商业判断：现有证据不建议商业投入；自用价值待核实。

### 流程与可用线索的证据分开

本轮商业评分不评定，现有证据不建议商业投入。归档称工作流把未接来电变为可跟进线索，但没有通话总量、成功收集比例、人工净省时、预约或成交结果。原帖依既有X访问限制跳过，作者方法不可用；归档还明确演示没有录到agent的口头回复。因此既不能把视频流程当作语音听感、时延、打断处理和理解能力的验证，也不能从“有用线索”推导收入。本轮保存schema-1简要分析；官方技术和竞争资料只能支持验收条件，不能补出案例实际效果。 依据：[archive-case-20261017](https://agentusecases.ai/use-case/answer-real-estate-calls-with-a-voice-agent), [S68a3de50ac11](https://elevenlabs.io/docs/eleven-agents/workflows/post-call-webhooks), [Sbc9b5d80cf1f](https://elevenlabs.io/docs/eleven-agents/customization/agent-analysis/data-collection)。

### 保留语音组件与agent字段的层次

源站Done with实际agent字段是n8n，正文另称ElevenLabs提供语音；两个层次按原样保存，不增改actual_agents字段。源站建议模板要求保存CRM或表格、发跟进邮件、测试通话并在真实消息前等批准；这不表示作者确实采用了相同CRM、邮件平台或提示词。归档方法只清楚提到预算、地点传入自动化，未披露电话运营商、模型、联系人验证、人工接管、权限和故障恢复。当前ElevenLabs的通话后接口也不能倒推为作者实际采用的集成架构。 依据：[archive-case-20261017](https://agentusecases.ai/use-case/answer-real-estate-calls-with-a-voice-agent), [S68a3de50ac11](https://elevenlabs.io/docs/eleven-agents/workflows/post-call-webhooks), [S7b31c553d69e](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook)。

### 预算和地点不是两个任意文本框

拟议验收应保存来电者明确给出的预算数值、币种、租赁周期或购买总价口径，以及确认过的地点。币种、周期、范围或地点模糊时保留未知并交人工，不能默认某个国家、月租或货币；零也不等于未知。ElevenLabs官方数据收集文档说明字段提取来自转录后的LLM分析，缺失或歧义可能返回空值，因此类型正确不代表语义正确。还需区分原话、模型提取和来电者确认后的字段。本轮仅用人工标注的合成字段测试状态，不测语音识别、自然语言提取准确率或房产匹配，不作报价、贷款资格或成交决定。 依据：[Sbc9b5d80cf1f](https://elevenlabs.io/docs/eleven-agents/customization/agent-analysis/data-collection), [archive-case-20261017](https://agentusecases.ai/use-case/answer-real-estate-calls-with-a-voice-agent)。

### 通话后事件、保存和发信各自验收

ElevenLabs当前文档区分转录、音频和通话发起失败事件，音频回调并不同时带完整字段分析。收到某个事件不能直接当作可用线索。生产接收方还需按官方机制验证来源，并处理重试、重复及顺序；本地测试只假设上游已验证的标志，没有创建密钥或验证真实HMAC。n8n可以立即回复工作流已启动，这不等于CRM记录成功，更不等于跟进邮件送达。拟议流程分别记录字段待复核、本地待保存、保存未知、跟进草稿和发送状态；保存超时不自动重发邮件，不把无新事件当成成功。 依据：[S68a3de50ac11](https://elevenlabs.io/docs/eleven-agents/workflows/post-call-webhooks), [S7b31c553d69e](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook), [Sbc9b5d80cf1f](https://elevenlabs.io/docs/eleven-agents/customization/agent-analysis/data-collection)。

### 前台、回拨和现成接待服务是基线

潜在使用者是经纪团队的接待或行政人员，预算负责人可能是门店或机构负责人。Agape Real Estate仅是归档提及的公司名，本轮未核验其付费合同、部署或身份，也不尝试联系同名机构。替代方案包括人工前台、语音信箱加回拨、现成AI接待与人工升级服务。Smith.ai提供这类组合，并对人工介入的条件与加收项目作区分；其供应商页面的自选证言不能当本案例客户反馈。应比较相同通话样本的完整记录、复核分钟、失败回拨、总费用和可跟进比例，而非只比较接通数量。 依据：[Sccd928733206](https://smith.ai/ai-receptionist), [archive-case-20261017](https://agentusecases.ai/use-case/answer-real-estate-calls-with-a-voice-agent)。

### 分钟、执行、线索与成交不能混用

ElevenAgents公开计划以通话分钟和并发等为口径，LLM和外部电话运营商费用另列；本轮通过官网Creative价格页中的Agents链接找到对应计划，没有把TTS字符或Creative共享积分换算成电话成本。n8n另按工作流执行等计费，同一通话可能触发多个事件与重试。Smith.ai的人工介入与服务组合又是另一种成本结构。所有这些都还没有包含资料维护、人工复核、异常回拨和获客。采购条件、实际通话时长及峰值并发未知，本轮不声称测出了真实单条线索成本；也不能把线索收入当成交易佣金已实现。 依据：[S2927392d8f4c](https://elevenlabs.io/pricing/agents), [S9c31625dedcc](https://n8n.io/pricing/), [Sccd928733206](https://smith.ai/ai-receptionist), [S68a3de50ac11](https://elevenlabs.io/docs/eleven-agents/workflows/post-call-webhooks)。

### 人工返工足以改变两个预算

以下均为美元假设，不是厂商报价、作者收入或实测利润。月度线索整理维护每客户750，用量预算120、人工6小时乘45为270、其他35、获客90，单位贡献235；月8客户固定450，月贡献1430。人工增至12小时则单位负35、月负730。一次设置2800，用量75、人工40小时乘45为1800、其他125、获客300，单位贡献500；月2项固定400，贡献600。若多12小时返工，单位负40、月负480。真实分钟、模型、运营商、CRM、消息、并发超额、税和采购等额外费用仍未知，预算中的用量项是占位估算，不能冒充已覆盖全部实际采购成本。 依据：[S2927392d8f4c](https://elevenlabs.io/pricing/agents), [S9c31625dedcc](https://n8n.io/pricing/), [Sccd928733206](https://smith.ai/ai-receptionist)。

### 缺失音频与独立用户结果不能补写

本轮在公开网页、GitHub和Hacker News方向检索发帖者与Agape流程，出现同名机构、汇编目录和无关内容，没有取得可归属本案例的独立实际付费或使用结果；没有访问这些汇编来替代受限原帖。下一步只用虚构事件检查预算/币种/周期/地点缺失、来电者确认、重复和旧修订、跨机构、音频或失败事件、CRM未知与邮件草稿。若缺字段被自动补齐、记录串用、保存未知却发送跟进、人工复核超预算或无法取得合法可听音频来验证通话质量，应停止扩展。17个合成检查不构成真实电话、声学或端到端生产可靠性验证。 依据：[archive-case-20261017](https://agentusecases.ai/use-case/answer-real-estate-calls-with-a-voice-agent), [S68a3de50ac11](https://elevenlabs.io/docs/eleven-agents/workflows/post-call-webhooks), [Sbc9b5d80cf1f](https://elevenlabs.io/docs/eleven-agents/customization/agent-analysis/data-collection), [S7b31c553d69e](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook), [S2927392d8f4c](https://elevenlabs.io/pricing/agents), [S9c31625dedcc](https://n8n.io/pricing/), [Sccd928733206](https://smith.ai/ai-receptionist)。

## 自用与试用准备

可能辅助接待后的字段整理，但语音质量、字段准确性、保存与实际净省时未验证。

准备：虚构机构/通话ID、字段和人工标签、事件修订与保存状态，不含真实录音或联系人。

工具：现有Python标准库；不运行电话、模型、ElevenLabs、n8n、CRM或邮箱。

预期：合成字段与保存/跟进状态表、未知项和人工复核问题，不产生真实线索或消息。

### 用虚构事件验收房产来电线索

研究团队自编，未调用模型实测。

    仅使用[虚构来电ID、机构ID、人工标注转录字段、事件ID/修订号与CRM状态]设计离线线索验收。来源实际agent字段保留n8n，正文ElevenLabs语音组件另记，不推定作者接口。预算列数值、币种和月租/总价口径，地点与来电者确认单列；缺失、歧义或未确认转人工，不补默认值。区分转录、音频、失败事件和旧修订；按机构与通话ID隔离记录，重复事件不得重复跟进，新通话不因同一联系人被自动丢弃。只生成本地虚构记录及跟进草稿，CRM保存未知不得变成成功或触发发信。上游可信标志和确认标志均为测试输入，不宣称已验证签名、身份或语音理解。不得拨打或接听真实电话、发邮件/消息、读取真实录音/联系人/房产资料/凭据、接入ElevenLabs/n8n/CRM、注册、创建凭据、购买或调用付费API。输出测试表与未知项后停止。研究团队自编，未调用模型实测。

## 来源

- [Answer real estate calls with a voice agent](https://agentusecases.ai/use-case/answer-real-estate-calls-with-a-voice-agent)：n8n实际agent字段、正文ElevenLabs语音集成、预算/地点收集、未接来电变线索的定性声称，以及Loom未录到agent语音；未独立核实。
- [X 原帖（本轮未读取）](https://x.com/oluwatomisint6/status/2106878686519587312)：仅保留登记链接，未重试、登录或以搜索摘要/镜像补原文和视频。
- [/integrations/builtin/core-nodes/n8n-nodes-base.webhook](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook)：n8n官方Webhook测试/生产入口、认证和响应模式；立即返回启动信息不等于线索保存或跟进邮件送达。
- [n8n Plans and Pricing - n8n.io](https://n8n.io/pricing/)：n8n当前工作流执行等计划口径，不能当成一次通话、合格线索或成交费用。
- [Smith.ai: 24/7 AI Receptionist Backed by Live Agents](https://smith.ai/ai-receptionist)：Smith.ai当前AI接待与人工升级方案构成竞争基线，人工介入费用与条件需区分；厂商自选评价不是本案例独立用户证据。
- [Post-call webhooks | ElevenLabs Documentation](https://elevenlabs.io/docs/eleven-agents/workflows/post-call-webhooks)：ElevenLabs官方通话后转录/音频/发起失败事件、HMAC验证与重试机制；不证明本案例采用此接口或通话质量。
- [Data collection | ElevenLabs Documentation](https://elevenlabs.io/docs/eleven-agents/customization/agent-analysis/data-collection)：ElevenLabs官方基于转录的LLM字段提取、数据类型和缺失/歧义返回空值；不证明预算/地点提取已准确。
- [ElevenAgents Pricing for creators and businesses of all sizes](https://elevenlabs.io/pricing/agents)：ElevenAgents当前按通话分钟与并发等计费，LLM及外部运营商费用分开；不能用Creative/TTS价格替代真实语音交付总成本。
