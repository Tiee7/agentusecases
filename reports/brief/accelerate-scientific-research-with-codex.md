# 用 Codex 和 ChatGPT 辅助量子化学计算与分析

## 中文

    使用 Codex 加快科学研究
    一位研究人员广泛使用 Codex 和 ChatGPT 开展科学研究，称一天能完成一周的工作，但最近的用量限制降低了产出。
    使用工具
    CX
    Codex
    GP
    ChatGPT
    做了什么
    一位理论化学家称，他们在围绕量子力学计算的研究流程中大量使用 ChatGPT 和 Codex，模拟分子、激发和自旋行为。在后续评论中，他们说重新安排了流程：用一个模型完成大部分分析，用另一个模型做最终审查和协调，再用成本较低的模型处理启动和停止计算、复制文件、解析数据等日常任务；需要更复杂推理时，由他们决定何时升级处理。
    结果如何
    他们称过去一年取得了前所未有的生产力，借助这些工具完成的研究远多于此前十多年的经历，但最近相同的工作会在一天内耗尽一周的用量。他们说 OpenAI 后来告知有一个错误影响了其用量，并提供了500美元额度；他们还说，此前也曾很快用完3000美元额度。
    值得注意
    主要问题是成本和限制：他们现在每次运行前都会衡量成本与性能，并称由于费用难以持续承担，已经不得不缩减使用。
    亲自试用
    使用
    Codex
    复制提示词
    我正在研究[科学问题或主题]。请使用[文件夹路径]中的数据和代码，复现[分析或结果]，然后运行[下一项实验或分析]，把图表保存到[输出文件夹]并总结发现。记录假设以及任何无法验证的事项。只有当脚本能从头到尾运行，并且我获得一份简短的结果与待解决问题说明时，任务才算完成。
    原始来源：https://www.reddit.com/r/OpenaiCodex/comments/1xae775/codex_used_to_supercharge_my_scientific_research

<details><summary>English original</summary>

    Accelerate scientific research with Codex
    A researcher uses Codex and ChatGPT extensively for scientific research, getting a week's work done in a day, though recent usage limits reduced output.
    Done with
    CX
    Codex
    GP
    ChatGPT
    What they did
    A theoretical chemist says they used ChatGPT and Codex heavily in a research workflow built around quantum-mechanical simulations of molecules, excitations, and spin behavior. In a follow-up comment, they say they reworked the setup to use one model for most analysis, another as a final reviewer and coordinator, and a cheaper model for routine jobs like starting and stopping calculations, copying files, and parsing data, while they chose when to escalate harder reasoning.
    How it went
    They report unprecedented productivity over the past year, saying the tools let them do far more research than in 10+ years before, but that recently the same work now burns through a weekly allowance in a day. OpenAI later told them a bug affected their usage and gave them $500 in credits; they say they had previously burned through $3,000 in credits quickly too.
    Worth knowing
    The main catch is cost and limits: they now check cost-to-performance before each run and say they have had to scale back usage because the expense is no longer sustainable.
    Try it yourself
    with
    Codex
    Copy prompt
    I'm researching [scientific question or topic]. Using the data and code in [folder path], reproduce [analysis or result], then run [next experiment or analysis] and summarize the findings with plots saved to [output folder]. Keep a log of assumptions and anything you couldn't verify. You're done when the scripts run end to end and I have a short write-up of the results and open questions.
    Original source: https://www.reddit.com/r/OpenaiCodex/comments/1xae775/codex_used_to_supercharge_my_scientific_research

</details>

## 方法摘要（目录转述，非作者原文）

目录转述称，分析、最终审查与日常计算操作由不同模型承担。
The directory reports separate models for analysis, final review, and routine calculation operations.

由研究人员决定何时需要更复杂推理，并衡量成本与性能。
The researcher decides when harder reasoning is needed and checks cost against performance.

## 结论

缺少原作者可复跑工程、数据、模型版本、用量账单及成果验收；周边论文不能补作本案实测。
让研究员掌握科学判断，把重复操作交给可追踪流程

## 原案能说明什么，缺什么

目录描述的是理论化学家对研究辅助工具的使用经验。对象包括分子在化学环境中的行为、激发和自旋计算；流程中有人决定复杂推理的升级。它没有提供模型确切版本、模拟程序、输入文件、实验编号、错误率或可复现成果。所谓一天完成一周工作是个人评价，不应换算成七倍准确率、工资节省或已到账收入。额度补偿也是作者转述的服务处理结果，不是收入，更不代表其他用户可以获得同样补偿。由于核心工程和账单无法核对，本篇是有依据简报，不用旁边几篇论文补成这个人的完整深研。

来源：Sdirectory

## 谁需要，谁可能付钱

自用人群是懂得判断计算结果的研究人员；潜在付款人是掌握软件或算力预算的课题组负责人、机构平台团队。需要买的可能是可靠的数据解析、批量计算管理和复现记录，而非一个声称会发现新科学的聊天框。把科研产出转为商业服务还要解决机构数据政策、采购、已有计算集群接入及学科验收。研究者个人喜欢一个工具不等于实验室存在外包预算，能使用免费软件也不等于没有维护成本。当前没有客户价格、采购意愿或合同证据。

来源：Sdirectory, Saiida

## 把自动操作和科学判断分开

建议先固定已有可信基线、软件环境、输入数据哈希和预期误差，再让助手生成或检查分析脚本。每次运行保存计算任务编号、参数、退出状态、日志和输出对应关系；额度或连接中断后从已完成步骤恢复，不能盲目重启昂贵计算。启动停止作业和复制文件是操作权限，接受一个科学结论是研究判断，两者不应混在同一条“完成”状态。脚本退出码为零只表示程序跑完；单位、边界条件、收敛性和结果对照仍需领域人员检查。这是研究者建议，不声称作者已经按此执行。

来源：Saiida, Ssessions

## 为什么不直接用现成流程

AiiDA已经提供工作流、输入输出溯源及集群调度接入，适合流程结构稳定的计算任务。智能体可以作为规划或脚本辅助层，而不必替换每一个确定性调度步骤。对于可重复的解析与提交，先比较普通脚本或现成插件，避免为简单动作反复调用昂贵推理。ERA采用明确评分指标的专门搜索策略；它说明科学软件优化可能需要任务设计，而不是证明通用助手随意探索就能得到同样结果。任何替代都要比较迁移、维护和人员学习成本，本轮没有安装或实测。

来源：Saiida, Sera

## 成本按一次可接受分析计

以下均为研究者假设，非作者账单或当前产品报价。轻量流程：模型摊销5美元、人工1小时按50美元计50、算力和存储10、获客摊销5，合计70美元；每月10份，加固定维护40，为740美元。高返工流程：模型20、人工4小时计200、算力存储80、获客20，合计320美元；每月10份加固定维护100，为3300美元。收入未知所以不算利润。科研软件许可、机构安全审核等未取得的费用另计，已列成本不是完整报价。自用不需要获客项，但不能把研究员审核时间当免费；订阅额度变化可能使流程停滞，应测的是每份验收结果的成本而非每条消息。

来源：Sdirectory, Saiida

## 获客、交付和复制条件

若将来验证服务机会，先限制在一种模拟软件及一种重复数据处理任务，交付可重跑脚本、环境说明、输入输出清单和人工验收记录。只能在机构明确授权后接触数据和计算账户；本任务不联系研究者、不注册、不提交表单、不启动实验。第一批客户的合理来源假设是既有科研软件合作关系，而不是对泛研究人员群发“自动发现”承诺。持续价值应体现在稳定插件、领域测试集和故障恢复，不在于简单模型分工容易复制。没有这些能力时，直接使用现成工作流更合理。

来源：Saiida, Srepo

## 隐私与错误风险影响真实收益

未发表数据、合作单位资料和运行日志可能有保密义务，不能为了排错把整个工作目录交给外部模型。还要防止误删原始数据、重复提交作业、错误终止别人的任务和无上限尝试消耗预算。来源可追溯不等于研究结果一定正确，但没有环境和参数记录几乎无法追责。OpenAI4S预印本对完整重跑仍弱的披露是重要反证；FrontierScience也明确限定测量范围，因此不把基准分数用作科学正确性的担保。

来源：Ssessions, Sfrontier

## 怎样进行最小验证

挑一个公开、非敏感、已有参考结果的分析任务，在隔离副本中比较原方法和辅助方法。人工先定义正确性容差、最高算力预算和停止规则；分别记录总人时、模型费、计算费、失败和重跑次数。必须由另一次干净环境重跑核对，不只检查一次漂亮图表。如果关键参数无法解释、数字不能复现、费用超出授权或人工修正抵消收益，就停止扩大流程。这里没有四周或200美元的统一门槛，也不以更换更多模型作为默认解决办法。

来源：Saiida, Ssessions

## 自用与试用

- 判断：领域专家可能受益，但无净省时对照。
- 适用人群：已有量子化学与计算基础的科研人员。
- 用途：分析脚本、数据解析及可追踪计算协调。
- 预期收益：预期减少重复操作，不保证正确发现或节省金额。
- 设置：公开样例、可信结果、环境与权限边界。
- 维护：版本、数据格式、队列及中断恢复维护。
- 频率：随项目高频运行，依研究阶段变化。
- 隐私：未发表数据、机构资料、凭据和日志外传。
- 错误风险：单位或收敛条件错误、重复计算、误删及误停。

已授权公开数据副本、可信基线、预算和停止条件。
脚本、参数、运行日志、图表与未决问题；须另做科学验收。

## 来源

- [Sdirectory · 许可目录科研流程](https://agentusecases.ai/use-case/accelerate-scientific-research-with-codex)：保留归档称理论化学研究者用Codex与ChatGPT做分子模拟分析及协调。效能、500美元补偿和3000美元消耗均为转述自述，未见账单、数据或可复跑产物。
- [Saiida · AiiDA官方简介](https://aiida.readthedocs.io/projects/aiida-core/en/stable/intro/index.html)：MIT开源计算科学工作流支持输入输出与元数据溯源、检查点和HPC调度器；是可核对的现成流程基础，不证明本案作者采用。
- [Sfrontier · FrontierScience官方研究](https://openai.com/index/frontierscience/)：2025年12月16日介绍专家编写的物理化学生物约束任务，Research金标准集60题；页面明确并不覆盖研究人员所有日常工作，不能替代此案例真实效率。
- [Ssessions · OpenAI4S预印本](https://arxiv.org/abs/2609.15096)：2026年9月14日社区预印本采用持久计算会话、逐单元执行记录、版本产物与检查点；作者承认所有被测系统的环境描述和完整重跑仍弱。不是OpenAI官方产品，也不是本案例部署。
- [Sera · ERA科研软件研究](https://www.nature.com/articles/s41586-026-10658-6)：2026年5月19日论文研究以明确质量指标和树搜索改进科学软件；受控任务结果不等于任何Codex工作流都有效，本文没有重跑论文。
- [Srepo · AiiDA公开仓库](https://github.com/aiidateam/aiida-core)：官方仓库警告不要直接使用快速变化的main分支，以免影响数据存储；部署稳定版本与迁移验证是成本。

## 核验边界

此前Reddit浏览限制未绕过；本轮没有完整读取原帖，未查私人通信或账单。云端/new导航超时，顺序用支持的公开网页阅读器核实。案例页普通网页读取失败，使用已有获许可归档。没有应用或科学计算实测。

搜索见相似自述但不计独立样本；公开仓库资料用于替代方案，未证明本案用户满意度。
