# 用Claude生成并审查Home Assistant自动化

## 中文

    用Claude构建Home Assistant自动化
    一位时间紧张的家长让Claude构建Home Assistant自动化，包括一个根据用电情况推断炉灶是否开启的辅助实体。
    使用的是
    Claude
    他们做了什么
    发帖者是一位忙碌的家长，此前Home Assistant基本闲置。他通过MCP把Claude连接到自己的HA实例，用它构建和改进自动化，而不再手写YAML。帖子中，他和其他人描述了让Claude检查设备与自动化，生成有人活动检测和状态检查等逻辑。其中一个例子是创建辅助实体，根据炉灶功率推断炉灶是否开启，再添加警告和排风扇自动化；人们仍然自己审核方案、代码和备份。
    进展与成效
    他们说，以前需要几天的任务现在只需几分钟。一位评论者说，通常需要几天的自动化，第一次尝试便在10分钟内成功。讨论的主要限制是Claude可能把事情复杂化，或者处理超出部分用户愿意暴露范围的HA数据。
    值得了解
    反复被提到的注意事项是：保留Claude无法访问的备份，应用更改前审核它的方案或YAML，并注意MCP配置可能消耗大量词元。
    亲自尝试
    使用Claude
    复制提示词
    我使用Home Assistant，希望实现一个自动化：[希望发生的事情，例如在炉灶可能忘记关闭时提醒我]。相关设备和实体是[列出实体，例如智能插座功率传感器sensor.stove_power]。请编写完整YAML，包括推断状态所需的辅助实体或模板传感器，并逐步解释应粘贴到哪里，以及如何安全地测试。
    原始来源：https://www.reddit.com/r/homeassistant/comments/1wpy5q6/claude_and_home_assistant

<details><summary>English original</summary>

    Build Home Assistant automations with Claude
    A time-strapped parent had Claude build Home Assistant automations, including a helper that infers whether the stove is on from power usage.
    Done with
    CL
    Claude
    What they did
    The poster, a busy parent who had let Home Assistant sit mostly dormant, connected Claude to their HA instance using MCP and used it to build and improve automations instead of hand-writing YAML. In the thread, they and others describe Claude reviewing devices and automations, generating logic like occupancy and state checks, and in one example building a helper that infers whether the stove is on from range power usage, then adding warnings and exhaust-fan automation; people still review plans, code, and backups themselves.
    How it went
    They say tasks that used to take days now take minutes, and one commenter said an automation that normally would have taken days worked on the first shot in 10 minutes. The main limitation raised is that Claude can overcomplicate things or act on more HA data than some users are comfortable exposing.
    Worth knowing
    A repeated catch is to keep backups Claude cannot access, review its plan or YAML before applying changes, and be aware MCP setups may consume a lot of tokens.
    Try it yourself
    with
    Claude
    Copy prompt
    I use Home Assistant and want an automation that [what I want to happen, e.g. alert me if the stove has likely been left on]. My relevant devices and entities are [list entities, e.g. smart plug power sensor sensor.stove_power]. Write the full YAML, including any helpers or template sensors needed to infer the state, and explain step by step where to paste it and how to test it safely.
    Original source: https://www.reddit.com/r/homeassistant/comments/1wpy5q6/claude_and_home_assistant

</details>

## 原作者的方法与来源

https://www.reddit.com/r/homeassistant/comments/1wpy5q6/claude_and_home_assistant
原站已出现站点安全拦截，本链接未继续访问；没有原作者实现或完整代码。

## 简要分析

商业分数未评定。

### 适合已有设备、缺少配置时间的人

目录中的家长已有HA但长期闲置，需求是把自然语言想法变成可审核的自动化。有人活动、状态判断和提醒是具体场景；没有设备的人还需硬件集成，不能把生成YAML当成完整智能家居交付。几天变几分钟和一次10分钟成功都是转述自述，缺计时口径、任务复杂度和长期运行记录。当前判断为内部效率用途，保留未评分简报。

依据：[Sdirectory](https://agentusecases.ai/use-case/build-home-assistant-automations-with-claude)

### 先确认连接器究竟可以做什么

官方当前文档说明MCP工具由所配置LLM API决定，新配置默认暴露全部LLM API并要求管理员；旧配置可能保留原选择。不能套用过去仅有Assist的印象，也不能由“MCP已连接”推断必然能编辑任意YAML。原作者用了哪个实现、暴露哪些工具尚不清楚。复制前需列具体读取、控制、写配置能力及授权范围；本轮没有建立连接或修改权限。

依据：[Smcp](https://www.home-assistant.io/integrations/mcp_server/), [Sdirectory](https://agentusecases.ai/use-case/build-home-assistant-automations-with-claude)

### 能运行一次与触发逻辑正确是两件事

官方Run actions会绕过顶层触发与条件，没有正常触发数据；应另外验证真实触发路径和trace。2025年另一用户遇到数值条件满足却不触发，体现事件与状态的理解负担；不是本案Claude的故障率。拟议验收需覆盖阈值跨越、缺失读数、重启、重复事件和条件不满足。模拟状态也可能触发现有真实设备动作，应在隔离的虚拟实体中准备，而不是直接在家庭设备上试。

依据：[Stest](https://www.home-assistant.io/docs/automation/testing/), [Sadjacent](https://community.home-assistant.io/t/automation-not-triggering-even-if-condition-is-met-numeric-state-issue/905663)

### 炉灶状态推断只能作为辅助信息

本报告推断：功率数据不能单独证明炉灶安全，设备类型、烹饪周期和传感器故障都可能改变解释。原文保留的智能插座示例并非本报告硬件选型建议，不应将普通插座用于不符合额定条件的大功率炉灶。试点改用虚拟灯光与合成读数，不提供实际炉灶接线或安全联锁改造。真实家居安全仍应依赖适当设备与人工检查，不能以生成代码代替。

依据：[Sdirectory](https://agentusecases.ai/use-case/build-home-assistant-automations-with-claude)

### 回退也需要验证

目录建议保留Claude无法接触的备份；官方说明另系统副本与恢复所需紧急资料的重要性。研究者建议把改动前版本、修改差异和回退范围绑定，先验证恢复流程再逐步扩大配置。备份存在并不证明能及时恢复，恢复整个系统也可能覆盖后续设置。密钥、访问凭据和家庭历史不应放进公共问题帖或研究仓库。

依据：[Sbackup](https://www.home-assistant.io/common-tasks/general/), [Sdirectory](https://agentusecases.ai/use-case/build-home-assistant-automations-with-claude)

### 收费价值更可能在验收和维护

商业假设是为已有HA的家庭提供有限范围配置检查、故障诊断和交付说明，收入可来自一次设置加明确范围的维护，但没有本案成交或愿付费证据。获客可先验证既有智能家居安装服务渠道需求；本轮未联系第三方。蓝图和可视化编辑器能解决常见场景，自定义服务须证明超出已有模板的价值。设备差异、夜间故障、客户解释和持续测试可能吃掉毛利，不能只算词元成本。

依据：[Sdirectory](https://agentusecases.ai/use-case/build-home-assistant-automations-with-claude), [Sblueprint](https://www.home-assistant.io/docs/automation/using_blueprints/)

### 自用成本独立核算

自用收益是降低学习YAML和梳理实体关系的门槛，仍需懂自己家庭的使用规则。设置包含实体清单、传感器意义和人工验收；维护包含HA版本、设备离线、误报与提示词迭代。MCP读取大量状态的词元负担只有目录提醒，未取得实际账单，不给虚构金额。频率宜随新增需求和设备变更，而非让模型持续参与每次开灯；后者不是目录已证明必要的方案。

依据：[Sdirectory](https://agentusecases.ai/use-case/build-home-assistant-automations-with-claude)

### 先做一个可核验的小样本

下一步先比较已有蓝图与一份原创虚拟灯光需求：明确开关事件、允许时段、重复触发、不可用状态和手工关闭优先级。要求只输出方案、差异、验证清单与回退说明，由人复核，再在隔离测试实例验证。记录准备、修正、测试和维护总时间。若无稳定实体定义、不能安全回退，或模板已足够，就停止定制投入。本轮未运行HA、未安装软件、未进行真实试用。

依据：[Sblueprint](https://www.home-assistant.io/docs/automation/using_blueprints/), [Stest](https://www.home-assistant.io/docs/automation/testing/)

## 试用准备与预期结果

虚拟灯光实体、合成状态变化、清楚的成功与失败条件。
可审核的方案、测试表和回退说明；本轮未实测。
仅分析虚拟灯光和合成状态。先比较已有蓝图是否满足需求，再写触发、条件、动作和失败测试表。覆盖状态不可用、重启、重复事件、手动关闭及回退。不连接或控制真实设备，不修改账号权限；不以Run actions成功代替完整触发验证。

## 来源

- [许可目录案例](https://agentusecases.ai/use-case/build-home-assistant-automations-with-claude)：Claude与MCP辅助开发；省时为目录转述自述。
- [官方MCP配置与工具范围](https://www.home-assistant.io/integrations/mcp_server/)：默认暴露全部LLM API及管理员要求；旧配置例外；工具由配置API决定。
- [官方自动化测试](https://www.home-assistant.io/docs/automation/testing/)：Run actions跳过顶层触发和条件；模拟事件仍可能操作真实设备。
- [官方备份恢复说明](https://www.home-assistant.io/common-tasks/general/)：建议另系统副本，恢复所需紧急资料应妥善保存。
- [现有自动化蓝图](https://www.home-assistant.io/docs/automation/using_blueprints/)：可复用蓝图是先评估的现有替代。
- [2025年社区数值触发问题](https://community.home-assistant.io/t/automation-not-triggering-even-if-condition-is-met-numeric-state-issue/905663)：另一用户混淆状态条件与触发事件；不能当作本案失败记录。
- [原始Reddit讨论](https://www.reddit.com/r/homeassistant/comments/1wpy5q6/claude_and_home_assistant)：原作者具体MCP、完整YAML及运行日志未读取。
