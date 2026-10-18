# 用 Claude Code 为怀旧游戏重制版添加阿莱西亚战役场景

## 中文

    为一款20世纪90年代游戏的重制版添加阿莱西亚战役扩展
    Nate Combs 用 ChatGPT 做研究并生成提示词，再由 Claude Code 实现扩展，按他的试玩反馈迭代。
    实际使用的 Agent
    Claude Code
    他们做了什么
    ChatGPT 对阿莱西亚战役进行历史研究，并为 Claude Code 编写提示词。随后，Claude Code 为一款20世纪90年代电子游戏的重制版制作了扩展。地图根据 ChatGPT 提供的文本资料重建，包括一份凯撒著作的译本、The Latin Library、Britannica，以及法国一家考古博物馆的资料。Nate Combs 试玩并提出批评意见，Claude Code 随之修改。
    结果如何
    Combs 称这个扩展有些古怪却引人入胜，并分享了截图。他发帖时仍在试玩，因此没有最终结果或经过测量的成果。
    需要知道的事
    来源未给出费用或耗时数字。这个流程依赖 ChatGPT 的研究结果和交接给 Claude Code 的提示词，以及反复多轮的试玩反馈。]
    自己试试
    推荐工具
    Claude Code
    复制提示词
    我的[经典游戏]重制版源代码位于[项目路径]。请使用以下研究简报：[粘贴笔记]，添加一个基于[历史战役，例如阿莱西亚战役]的扩展场景。实现地图、单位和胜利条件，然后让我试玩，并根据我的反馈反复修改，直到我说完成。把改动放在独立分支上。
    原始来源：https://substack.com/@natecombsai/note/c-207873186

<details>
<summary>英文原文</summary>

    Add a battle-of-Alesia expansion to a 1990s game remake
    Nate Combs used ChatGPT for research and a prompt, and Claude Code implemented the expansion, iterating on his playtest feedback.
    Done with
    CC
    Claude Code
    What they did
    ChatGPT did the historical research on the battle of Alesia and wrote the prompt for Claude Code. Claude Code then built the expansion for a remake of a 1990s video game. The map was reconstructed from text sources ChatGPT supplied, including a Caesar translation, The Latin Library, Britannica and a French archaeology museum. Nate Combs playtests it and gives criticism, and Claude Code revises.
    How it went
    Combs calls the expansion odd but gripping and shares screenshots. He was still playtesting when he posted, so there is no final result or measured outcome.
    Worth knowing
    The source gives no cost or time figures. The workflow depended on ChatGPT's research and prompt handing off to Claude Code, plus repeated rounds of playtest feedback.]
    Try it yourself
    with
    Claude Code
    Copy prompt
    I have the source for my remake of [classic game] in [project path]. Add an expansion scenario based on [historical battle, e.g. the Battle of Alesia] using this research brief: [paste notes]. Implement the map, units, and win conditions, then let me playtest and iterate on my feedback until I say it's done. Keep changes on a separate branch.
    Original source: https://substack.com/@natecombsai/note/c-207873186

</details>

## 原作者的方法与来源

[原帖](https://substack.com/@natecombsai/note/c-207873186)未取得，未生成作者方法摘要。下文是独立简要分析。

## 我们的简要分析

商业判断：现有证据下不建议商业投入。商业分数未评定；自用价值：中。此稿是brief简报，不计入已完成v2深研。

已归档正文可完整翻译；原作者外部帖子未读，游戏、代码、构建与许可不明，缺少实际成本、直接玩家反馈和完成结果。两份官方补充资料只支持流程与假设发行条件；本稿不满足v2深研证据广度，独立保存为brief。

### 研究、实现与试玩的交接

归档呈现的流程是ChatGPT整理历史研究并撰写交接提示词，Claude Code把材料转成扩展场景，再由人试玩和提出具体意见。已记录的实际agent仍按Done with保留为Claude Code；不能把推荐工具或其他项目反填成作者配置。地图尺寸、兵力、地形、单位行为与胜负条件究竟怎样实现没有材料。应把史料摘录、据史料作出的推断和为可玩性调整的设计分别保存，否则下游代码很容易把研究阶段的不确定假设固化成规则。这里是对流程的分析，没有重建作者代码或观看其截图。

依据：archive-case-20261017, S9686dc1633cd

### 先建立可以检查的场景验收

官方文档支持给编码代理可执行的验证标准，但能构建不等于好玩。针对已有且获准修改的工程，建议先固定一个小场景，核对进入地图、单位移动与交战、胜利和失败触发、重开及原有场景是否仍正常。存读档只有原游戏具备该功能时才纳入回归，不能假设案例引擎或接口存在。人工试玩应记录操作顺序、版本与可复现的问题；游戏平衡和历史解释仍需人判断。没有本例代码与构建，本轮没有进行游戏运行验证，也没有测得代理成功率。

依据：archive-case-20261017, S9686dc1633cd

### 自用范围与准备负担

自用价值为中，是对已有合法可修改源码、能够检查游戏行为的爱好者或独立开发者的条件性推断。辅助作用是把研究简报转为场景修改草案、减少资料与代码之间的手工交接，尚无节时数据。准备工作包括确认工程可运行、已有测试与素材来源，整理可追溯的史料和一个小场景的目标。后续负担主要是试玩、回归与维护；若连基础工程都不能稳定启动，先排除环境问题，不应把它混入扩展制作预算。项目隐私、未公开源码及素材只按原有访问范围处理。

依据：archive-case-20261017, S9686dc1633cd

### 潜在客户、替代与商业判断

现有证据下不建议商业投入，先保留为个人原型与学习流程。假设付款人是拥有可修改游戏的独立团队，购买的会是能集成、可验收且修改范围清楚的场景交付，而不是一段代理提示词。替代方案包括团队手工编写场景、现有编辑器或聘请开发者；由于游戏本身未知，不能列举某款编辑器为已核验直接竞品，也无法比较真实报价、社区规模或兼容成本。没有付费客户、销售记录或直接玩家评价，尚不能证明获客渠道、复购或可积累的壁垒。

依据：archive-case-20261017, S9686dc1633cd

### 从私人试玩到公开交付的差距

可运行扩展和可公开发行是两步。Steam官方资料仅被当作一种假设渠道：内容权利和构建审核是发行条件。本例是否使用Steam、是否有重制版或素材许可，均未知，不能因为作品源自20世纪90年代就默认可以销售。下一步应先列出代码、引擎、图像与音频的来源及允许用途，未确认前仅在已获准的本地范围内做原型。历史叙述来自哪些具体译本、文章和地图仍需逐项核对，本轮没有用任意同题历史网页冒充作者读过的资料。

依据：archive-case-20261017, S200b6377ed2e-web

### 两种可复算成本情景

案例未披露模型用量、订阅分摊、失败次数或人工工时。第一种个人原型规划：收入0美元，现有资源分摊预算5美元，加6小时×20美元的机会成本120美元，总投入125美元；其中120美元不是新增现金支出。第二种固定范围接单假设：每份299美元，资源5美元、8小时×30美元人工240美元、其他15美元和获客60美元，变动成本320美元，单位贡献-21美元；每月4份再扣100美元固定成本为-184美元。全部是用于检验报价的假设，未实际支出或核实市场价；多返工2小时，第二种单位贡献变-81美元。

依据：archive-case-20261017

### 补证条件、反证与停止投入

反对暂缓商业投入的理由是：爱好者自用并不需要付费客户，人工试玩也可能足以带来创作乐趣；这支持条件性的自用价值，不足以证明商业收益。下一轮最有用的材料是一份可确认归属与允许用途的项目说明、一个可运行的小场景、明确的验收记录，以及真实的修改工时。先约定一张地图和最多两轮试玩反馈，达到预算就停下来复盘。如果基础工程不可运行、关键许可未知或反复无法复现胜负条件，暂停扩展。取得这些证据后再升级研究层级，不按来源数量凑出深研。

依据：archive-case-20261017, S9686dc1633cd, S200b6377ed2e-web

## 事实与证据边界

- 归档Done with记录的实际agent是Claude Code；简介另外提到ChatGPT负责研究与提示词交接。（archive-case-20261017）
- 归档称地图依据ChatGPT提供的文本资料重建，列举凯撒著作译本、The Latin Library、Britannica和法国一家考古博物馆；没有给出这些资料的具体链接、版本或地图数据。（archive-case-20261017）
- 归档称Nate Combs反复试玩、提出批评意见，由Claude Code修改；仍在试玩，没有最终结果或量化成效。（archive-case-20261017）
- 归档未给出游戏名、游戏引擎、代码仓库、可运行构建、费用或耗时，无法据此确认可销售产品。（archive-case-20261017）
- 源站Copy prompt要求实现地图、单位与胜利条件，在独立分支上迭代；这是推荐模板，不是已核验的作者实际提示词。（archive-case-20261017）
- Claude Code官方文档建议明确可执行验证条件，并把探索、规划与实现分开；技术建议不能替代本案例的运行验收。（S9686dc1633cd）
- Steam官方规则把内容权利与发布前构建审核作为发行条件；此规则只用于说明假设渠道的交付门槛。（S200b6377ed2e-web）

## 成本情景（全部是假设）

| 情景 | 收入 | 资源分摊 | 人工 | 其他 | 获客 | 单位贡献 |
|---|---:|---:|---:|---:|---:|---:|
| 规划假设：个人小场景 | 0 | 5 | 120 | 0 | 0 | -125 |
| 规划假设：固定范围开发服务 | 299 | 5 | 240 | 15 | 60 | -21 |

币种USD。个人原型人工为机会成本；固定范围服务每月4份、固定成本100美元，月利润-184美元。未实际支出或验证报价。
## 自用价值：中

条件性推断：已有获准修改的源码且能人工试玩时，可辅助把研究简报转为场景草案；未测得节时或质量收益。

依据：archive-case-20261017, S9686dc1633cd

- 适用人群：拥有可修改工程、能检查代码和游戏行为的爱好者或独立开发者。
- 用途：整理历史资料交接、制作小场景并记录试玩问题。
- 预期收益：有机会减少研究到代码之间的手工交接；无实际收益数字。
- 设置成本：能正常启动的现有工程、素材用途记录、可追溯研究简报及明确场景范围。
- 维护成本：手工试玩、回归检查、环境与版本维护、修改失败后的复盘。
- 使用频率：按已有游戏项目需要使用，先做一次小场景。
- 隐私风险：源码、未发布内容与私人反馈保持原有访问范围，不上传无关资料。
- 错误风险：历史假设可能被当成事实，地图、AI行为和胜负条件可能出错，需人工复核。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/add-a-battle-of-alesia-expansion-to-a-1990s-game-remake

建议工具：Claude Code

    I have the source for my remake of [classic game] in [project path]. Add an expansion scenario based on [historical battle, e.g. the Battle of Alesia] using this research brief: [paste notes]. Implement the map, units, and win conditions, then let me playtest and iterate on my feedback until I say it's done. Keep changes on a separate branch.

自编试用模板

准备条件：已有获准修改且能运行的工程、资料来源清单、一张地图范围和人工试玩时间。

工具：实际实现与源站推荐均为Claude Code；ChatGPT在归档叙述中负责研究和提示词交接。

预期结果：小场景设计、变更清单及可复现的试玩验收步骤；本轮未运行游戏，不保证可玩或完成。

### 为现有工程准备可检查的小场景

自编模板

出处：研究团队自编

依据：archive-case-20261017, S9686dc1633cd

    我已有获准修改且能正常运行的[游戏工程路径]，希望制作[历史战役]的一张小地图。先阅读现有场景格式、构建说明与测试，整理[研究简报和逐条来源]，把史料事实、推断和游戏设计假设分开。先给出地图、单位、胜负条件与最小文件改动计划，再在独立分支实施；只用已有工程和已配置工具。最多安排两轮我的试玩反馈，逐次记录版本、操作步骤、问题与修复。检查启动、地图进入、单位行为、胜利、失败、重开与原有场景回归；存读档只在原工程已有功能时检查。保留中间文件与改动清单，不覆盖原始素材；无法启动或缺少关键资料时说明阻碍并停在方案阶段。不要安装陌生项目、创建凭据、调用额外付费API、发布或联系他人。

## 来源

- archive-case-20261017：[Add a battle-of-Alesia expansion to a 1990s game remake](https://agentusecases.ai/use-case/add-a-battle-of-alesia-expansion-to-a-1990s-game-remake)。案例站已归档简介、ChatGPT到Claude Code的交接、试玩仍进行中、费用和耗时未报告，以及源站试用模板。
- S9686dc1633cd：[Best practices for Claude Code - Claude Code Docs](https://code.claude.com/docs/en/best-practices)。Claude Code官方建议先探索与规划，提供可执行的验证标准并检查运行结果；不证明本例实际实现、画面或性能。
- S200b6377ed2e-web：[Onboarding (Steamworks Documentation)](https://partner.steamgames.com/doc/gettingstarted/onboarding)。Steam作为一种假设发行渠道，要求有足够内容权利并在发布前审核构建；不证明本例在Steam发行或已获许可。

## 仍待核实

未读取Substack原帖、未观看截图或运行游戏，未确认游戏名、引擎、代码归属、许可、史料具体版本、完工状态、客户需求、实际工时和成本。未把同题其他作者仓库当成此项目。Source Copy prompt是建议模板。Wanted未知，暂用稳定登记顺序，不是热度排名。
