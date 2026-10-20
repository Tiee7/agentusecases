# 用本地Codex辅导纸笔练习并保存学习记录

## 中文

    用本地智能体辅导纸笔数学练习
    一个开源辅导应用在本地运行Codex，使用TUTOR.md教学说明和用户的订阅额度，指导纸笔数学学习。
    使用的是
    Codex
    他们做了什么
    作者开发并开源了名为ari的辅导应用。它在本地运行Codex，因此使用用户现有订阅额度，而不是API密钥。TUTOR.md借鉴openclaw中SOUL.md的思路，存放把智能体设定为纸笔数学导师的教学说明。
    进展与成效
    作者说它很有趣，也说自己制作一个版本很容易。这条评论没有提供结果、数字或限制。
    值得了解
    本地运行Codex意味着使用订阅额度而不是API密钥，因此无需另外支付API账单。
    亲自尝试
    使用Codex
    复制提示词
    在这个文件夹里为我搭建一个本地数学导师。编写TUTOR.md教学说明，让你以[我的水平]教授[主题，例如代数或微积分]：每次给我一道题让我在纸上解答，再要求我输入或描述答案和步骤，先给提示，再给解答。当我能开始一个会话、收到第一道题，并获得对我尝试的反馈时，搭建才算完成。不要在未先展示给我的情况下删除或覆盖任何现有文件。
    原始来源：https://news.ycombinator.com/item?id=50147872

<details>
<summary>English original</summary>


    Tutor you through pen-and-paper math with a local agent
    An open-sourced tutor app runs Codex locally with a TUTOR.md brief to teach math with pen and paper using the user's subscription credits.
    Done with
    CX
    Codex
    What they did
    The author built a tutor app called ari and open-sourced it. It runs Codex locally, so it draws on the user's existing subscription credits instead of an API key. A TUTOR.md file, adapted from the SOUL.md idea in openclaw, holds the brief that sets up the agent as a math tutor for pen-and-paper work.
    How it went
    The author calls it very fun and says a version of your own is trivial to make. The comment gives no results, numbers, or limitations.
    Worth knowing
    Running Codex locally means it uses subscription credits rather than an API key, so no separate API billing is needed.
    Try it yourself
    with
    Codex
    Copy prompt
    Set up a local math tutor for me in this folder. Write a TUTOR.md brief telling you to teach [topic, e.g. algebra or calculus] at [my level] by giving me one problem at a time to work out on paper, then asking me to type or describe my answer and steps, and giving hints before solutions. The setup is done when I can start a session, receive a first problem, and get feedback on my attempt. Don't delete or overwrite any existing files without showing me first.
    Original source: https://news.ycombinator.com/item?id=50147872


</details>

## 原作者的方法与来源

来源：[nichochar on ari](https://news.ycombinator.com/item?id=50147872)

作者方法摘要

1. 作者公开本地Codex辅导应用，用Markdown教学说明指导纸笔练习。
   English summary: The author publishes a local Codex tutor and adapts a Markdown brief to guide paper-based practice.

## 我们的分析

**商业结论：仅建议受控试点。先验证纸笔反馈与独立解题，再判断是否值得包装服务**

ari有可追溯的开源实现、可编辑教学与用户文档，以及照片反馈和记录恢复设计，复制条件比短评论清楚。但本地界面仍会把提交内容发给模型，现有订阅有额度成本，设备和版本需要维护。公开讨论没有独立成效证据，成熟替代已提供低价家庭辅导。先限定成年自用和合成作答验收，验证总工时与撤掉AI后的表现，再判断商业投入。

案例ID：`tutor-you-through-pen-and-paper-math-with-a-local-agent` · 案例来源：https://agentusecases.ai/use-case/tutor-you-through-pen-and-paper-math-with-a-local-agent
研究时间：2026-10-20T01:24:22.548256+00:00

**商业评分：35.0/100。用户反馈信号占5%。**

| 维度 | 权重 | 分数 /5 | 商业依据 |
|---|---:|---:|---|
| 付费需求 | 20% | 2 | 具体纸笔自用场景存在，但仅作者自述，尚无目标成人付费需求或长期留存验证。 [Sauthor, Skhan] |
| 业务价值与效果证据 | 20% | 2 | 代码和上游CI支持工程流程存在，未实测教学反馈或独立解题收益，不能计作效果证明。 [Scode, Sci, Sstudy] |
| 单位经济与利润 | 20% | 2 | 两种假设对支持工时高度敏感，缺真实账单与成交；自有订阅不是总成本为零。 [Sreadme, Sauth] |
| 获客与市场进入 | 15% | 1 | 作者有HN和开源入口，但没有可核验转化或独立用户复用，渠道价值尚待验证。 [Sauthor, Sissues] |
| 竞争壁垒 | 10% | 2 | 可积累验收内容和恢复工程，但MIT实现可复制，教学优势缺独立检验。 [Spersonal, Slicense] |
| 交付与经营风险 | 10% | 2 | 本地回环与校验有设计，设备兼容、模型错误和数据提交仍有维护责任，未运行验收。 [Scode, Sprovider, Sreadme] |
| 独立用户反馈信号 | 5% | 0 | 没有独立ari使用效果反馈，记为证据信号不足，不表示用户不满或产品无效。 [Sdiscussion, Sissues] |

## 自用价值：中

已有订阅且能审核反馈的成年人可验证自用，学习收益与净省时待测。

依据：Sreadme, Scode, Sstudy

- 适用人群：有纸笔练习习惯、能自行安装和审核的成年学习者。
- 用途：按需提示、照片或文字反馈、课程与反思记录。
- 预期收益：流程组织有源码支持，不能承诺提高成绩或替代真人辅导。
- 设置成本：电脑、Node/Codex环境、账号额度、拍摄或照片工作流。
- 维护成本：版本、设备权限、反馈复核、档案纠错和备份恢复。
- 使用频率：按个人练习安排使用，实际长期留存未知。
- 隐私风险：提交作答与相关上下文会发给模型；本地文件也需妥善保护。
- 错误风险：手写误读、错误量规、过早给答案、把AI分数当掌握。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/tutor-you-through-pen-and-paper-math-with-a-local-agent

建议工具：Codex

    Set up a local math tutor for me in this folder. Write a TUTOR.md brief telling you to teach [topic, e.g. algebra or calculus] at [my level] by giving me one problem at a time to work out on paper, then asking me to type or describe my answer and steps, and giving hints before solutions. The setup is done when I can start a session, receive a first problem, and get feedback on my attempt. Don't delete or overwrite any existing files without showing me first.

自编试用模板

准备条件：原创题、无身份合成作答、人工标准答案与量规。

工具：先文档评审；软件运行、账号和资料提交另按授权，不使用额外付费API。

预期结果：一组可复核的提示与评分验收标准；本轮无真实教学试用。

### 源站Copy prompt

原文模板

出处：https://agentusecases.ai/use-case/tutor-you-through-pen-and-paper-math-with-a-local-agent

依据：Sdirectory

    Set up a local math tutor for me in this folder. Write a TUTOR.md brief telling you to teach [topic, e.g. algebra or calculus] at [my level] by giving me one problem at a time to work out on paper, then asking me to type or describe my answer and steps, and giving hints before solutions. The setup is done when I can start a session, receive a first problem, and get feedback on my attempt. Don't delete or overwrite any existing files without showing me first.

### 纸笔反馈验收设计

自编模板

出处：研究团队自编

依据：Scode, Sstudy

    仅用这些原创题和合成作答设计测试。区分提示、解释和检查，不因最终答案正确而推断步骤正确；看不清或只有题面时不评分。列重复页、更正页、错题页、版本变化和撤掉AI后独立解题的验收标准。不安装软件、不登录账户、不开启摄像头、不上传真实学生数据。

## 已核验事实

- 作者HN评论直接链接ari仓库并说明采用TUTOR.md教学文件。 [Sauthor]
- 固定ari提交使用MIT许可证，复制实质代码需保留版权与许可声明。 [Slicense]
- README要求Node24及Codex账号，内置摄像头桥有Mac平台限制。 [Sreadme]
- 本地保存不等于离线推理，主动提交的作答与上下文仍发送OpenAI。 [Sreadme]
- 固定代码区分提示、解释和检查，无法可靠识别的作答不得评分。 [Scode, Sprompt]
- 个性化文件的更新包含哈希检查和路径约束，但不证明学会了知识。 [Spersonal]
- 上游固定提交CI的隐私检查、测试和构建均显示成功，本轮未运行应用。 [Sci]
- 官方登录文档区分ChatGPT订阅访问和API按量访问，仍受实际额度限制。 [Sauth]
- Khanmigo官方家庭价税前4美元每月或44每年，开通有美国等条件。 [Skhan]
- 公开HN上下文仅作者自己的评论，问题列表空，不构成独立效果验证。 [Sdiscussion, Sissues]

## 先服务能自己安装的成年学习者

事实是ari定位个人纸笔学习，本地单用户程序要求Node、Codex账号和设备配置。最贴近的首批使用者是已有订阅、愿意自己练数学或物理的技术型成年人，而不是默认把儿童和学校当容易成交的客户。前者可以自己判断安装、拍摄和额度是否值得，后者还涉及监护、课程匹配、采购、设备维护和学生数据处理。研究者判断应先把“即时提示”“检查过程”和“安排学习”拆开，找出使用者最常卡住的一步，不能把完整导师人格当所有人都会购买的功能。付款人若是本人，比较的是现有订阅加个人时间；若是家长，比较的是可信内容、监督与孩子独立解题，而不只是一款能聊天的软件。目前没有本案付费用户、留存或客单价，下面的经营情景仅检验假设，不声称作者正在经营这些服务。对已有编程能力的人，复制安装可能较容易，但这也会降低他们为通用部署付费的意愿。应验证是否存在持续的教学检查需求，而非只问是否觉得演示有趣。

依据：Sreadme, Skhan

## 把纸面练习、主动提交和反馈拆成可审查步骤

代码与README呈现的流程是讨论目标、形成课程或单课、在学习桌上练习、提交照片或文字、请求提示或检查，并保存反思。服务器按模式处理反馈，缺少相关且可辨认的作答时不应评分；评分还要对应量规。多张照片可按顺序作为同一道题的不同视图，重复页面不应重复得分。这个设计比“拍一张图直接报分”更完整，但静态分支和提示词存在不等于真实手写识别每次正确。研究者建议为一次提交绑定练习ID、照片顺序、题目版本和反馈版本，测模糊字、擦改、错页、缺步和只拍题面等情况。学生得到下一步提示后继续纸面尝试，而不是把答案复制回来作为掌握证据。实时摄像头画面与实际发送给模型的作答也要区别，界面应清楚显示正在预览还是已提交。本轮没有启动应用、开启摄像头、调用模型或上传作业，所以这里只描述固定源码支持的设计和必须验证的路径。

依据：Scode, Sprompt, Sreadme

## 已有学习产品与现有订阅共同限制收费空间

可核验的市场参照是Khanmigo官方家庭页税前每月4美元或每年44美元，并有美国居住和账单等开通条件。它提供课程和家长功能，但并不等同ari的本地文档、摄像头与可编辑个性化流程，也不能把地区限制外推成某个地区一定有空白市场。ari作者公开表达自己的使用兴趣，HN讨论没有独立学习者的效果数据；搜索发现的介绍文章也不能作为真实使用和付费证明。研究者的可检验需求假设是：已有模型订阅的人仍需要把纸笔作业、课程和反馈记录放在一个清楚的界面里。市场大小不能由GitHub星数、评论赞同或模型用户总数推算。下一步需要观察人在不用辅导工具时是否仍能独立完成相似题，并了解维护和复核是否增加负担。如果用户只是偶尔问一道题，现有聊天工具足以替代，安装本地应用反而提高进入成本。

依据：Skhan, Sauth, Sauthor

## 原生学习工具、直接对话和开源自装各有替代边界

与直接上传照片聊天相比，ari的差别主要是把课程、练习、提示、反思和可编辑学习档案串起来；这属于可用性和持续状态组织，不能直接称为教学效果优势。与Khanmigo相比，ari可查看和修改源码、保存本地数据，却缺已核实的同等家长管理、课程覆盖和学校服务能力。与人工辅导相比，异步提示有时间灵活性，但错误诊断、鼓励和学习动机仍可能需要真人。本案MIT许可降低复制技术的门槛，同时削弱仅靠封装开源界面的独占性；若分发实质源码需保留许可证，品牌和素材另按实际权利处理。比较时应固定一道题、同样的作答照片和同样的“先提示后解答”标准，计入安装、拍照、等待、澄清与教师核验总时间。不能拿最快的一次模型回答与老师完整辅导课比较。若现成工具已覆盖用户最常用需求，合理选择可能是继续使用现成方案，而不新增软件订阅。

依据：Skhan, Sreadme, Slicense

## 把软件服务收入与学习者模型支出分开

以下两组是研究者为“成年人的一次本地设置与限定验收服务”设定的假设，非作者报价、成交或市场承诺。基础情景每单99美元，服务方不代付模型API，人工按1小时30美元，其他变量4美元，获客摊销12美元，每月10单，固定维护300美元：每单贡献53美元，月贡献扣固定成本230美元。压力情景仍99美元，人工增至3小时90美元，其他变量6美元，获客25美元，每月5单、固定300美元：每单贡献负22美元，月结果负410美元。两者均未含税、退款和额外保修，不是净利润预测。学习者已有订阅额度、摄像头和电脑不在服务商成本内，却是客户总成本，不能因api_cost填0就称整套免费；若使用API模式，必须另按实际用量核算。99美元高于现成工具月费，能否成立取决于明确的安装或验收价值，目前没有愿付证据。最敏感变量是人工支持时间与获客，而不是代码生成速度；任何“无限维护”都会改变该交付单位。

依据：Sreadme, Sauth, Skhan

## 先用可复核的演示解释价值，再讨论收费

作者已有HN和公开代码作为分发入口，但可读讨论主要是作者自己的介绍，不能称作自然增长或成熟销售渠道。研究者建议若验证需求，应面向自愿的成年纸笔学习者，展示同一道题从作答、逐步提示到关掉AI后迁移练习的过程，并明确哪些步骤是真实完成、哪些仅演示。演示材料应是原创题与无个人身份的合成作答，不收集学生姓名、学校或健康信息。潜在合作对象可包括愿意审核题库的成人教育教师，但本轮没有联系任何第三方或招募用户。获取一名愿意反馈的使用者与获取一名续费客户是不同阶段，要分别记录入口、安装完成、练习完成、返工次数和付费意愿。不要把开源星标换算成交，也不把竞品网站上的精选家长评价移植为本产品口碑。一个短期试点只有在复核负担可控、学习者确实愿意持续使用时，才值得继续投入包装和销售。

依据：Sauthor, Sissues, Sreadme

## 可积累的是经审核内容与恢复质量

可编辑的TUTOR.md和用户档案使偏好能够被检查与修正，源码还为记忆路径、内容大小、哈希冲突和恢复标识设边界。持续学习代理保存工具回执并处理会话中断，这些是减少重复动作和历史丢失的工程基础。它们不自动构成教育护城河，因为开源实现可复制，且错误的学习档案可能在后续会话反复影响反馈。研究者认为更难积累的是明确适用范围的题目、经过人工核验的评分量规、常见误解分类、可重放的失败样本和跨版本兼容测试。更新学习者档案时应区分本人陈述、一次错误和多次证据，不能因一道题错了就给人贴固定标签；也不能把AI评分当真正掌握。若产品只新增人格文本和聊天外观，其价值很容易被现有模型功能吸收。若能减少恢复和内容审核时间，则可形成服务交付优势，但仍需要实际使用数据来证明，不能由源码结构推断成本已经下降。

依据：Spersonal, Sagent, Slicense

## 本地界面不等于离线模型或零隐私成本

README说明聊天、作业与进度保存在本地，主动提交的作答和相关上下文会发送到OpenAI；因此“本地运行”不能被宣传为所有信息不离开电脑。短请求适配器禁用多类工具并使用read-only，主学习会话另有应用提供的工作区工具，不能拿一个路径的限制概括整个应用。服务器限制回环地址，现成程序应保持单用户localhost，不把它直接改为面向学校的公网服务。摄像头桥有Mac与设备适配条件，浏览器摄像头和照片上传是不同路径；不能保证所有设备即装即用。固定提交的上游CI显示隐私检查、测试和构建成功，但本轮没有运行它，也没有实测手写识别、浏览器权限或教学对话。复制前仍需明确安装来源、模型额度、所提交资料和恢复步骤，未成年人资料需要相应授权与保护。产品交付若跨账号、多人或公网，权限与数据边界都发生实质变化，必须另行设计和验证，不能沿用本地演示的结论。

依据：Sreadme, Sprovider, Scode, Sci

## 学习成效要在撤掉AI后测

暂无直接用户反馈。

依据：Sstudy, Sdiscussion, Sissues

## 限定个人效率试点，暂不承诺教学收益

结论是仅建议受控试点。源码、许可证和数据路径提供了比单条评论更明确的复制基础，值得验证“纸笔尝试—按需提示—可审查反馈—反思”是否减少个人学习摩擦。但订阅额度不免费、设备与版本有维护负担，独立学习收益和商业愿付仍未知。第一步不必安装或调用额外付费模型：先用原创题和合成作答制定验收表，覆盖正确过程、正确答案但步骤错、看不清、只拍题目、重复页与更正页，人工标注应答。取得需要的软件运行及资料授权后，再在隔离目录做实际测试，并记录全部失败与总工时。初始范围限定成年自用，不接学校成绩、不上传孩子作业、不承诺长期托管。若可靠反馈需要比原先更多人工，用户离开AI后无法完成相似题，或现有工具已满足需求，就停止商业投入；若验证有益，再分开讨论资源包、安装服务或长期辅导，不能把三种不同责任混成一个无限订阅。

依据：Sreadme, Sprompt, Skhan, Sstudy

## 单位经济测算：情景假设，不是项目已实现的财务结果

| 情景 / 交付单位 | 收入 | 可变成本（含获客） | 单位贡献 | 月交付量 | 月固定成本 | 月经营贡献 |
|---|---:|---:|---:|---:|---:|---:|
| 基础假设：限定成人本地安装与验收 / 一次安装及限定验收服务 (USD) | 99.00 | 46.00 | 53.00 | 10 | 300.00 | 230.00 |
| 压力假设：支持时间升至三小时 / 一次安装及限定验收服务 (USD) | 99.00 | 121.00 | -22.00 | 5 | 300.00 | -410.00 |

基础假设：限定成人本地安装与验收假设：全部为研究假设，非作者报价。10×(99-0-30-4-12)-300=230。用户自有模型订阅及设备另付，不含税退款或无限维护。；API成本 0，人工成本 30，其他可变成本 4，分摊获客成本 12。依据：Sreadme, Sauth

压力假设：支持时间升至三小时假设：全部为研究假设，非实绩。5×(99-0-90-6-25)-300=-410。服务商不代付API不代表用户模型免费；未计税退款。；API成本 0，人工成本 90，其他可变成本 6，分摊获客成本 25。依据：Sreadme, Skhan

## 反证与未核实信息

无独立ari学习效果或付费证据；本地不等于离线；订阅额度与安装维护成本；低价成熟替代；练习表现不等于独立掌握。

仅公开只读源码和来源研究；未安装运行ari、登录Codex、开启摄像头或调用模型；上游CI不是本轮测试，PNAS不是ari评测；没有使用私人学生材料。

## 具体动作与止损条件

准备原创题与合成作答验收集，先人工核量规；经运行授权后再做隔离实测。

停止投入条件：反馈不可靠、维护大于收益、独立后测无改善或需要未经授权的学生数据。

## 来源与对应关系

- [Sdirectory] [许可目录案例](https://agentusecases.ai/use-case/tutor-you-through-pen-and-paper-math-with-a-local-agent)：保留许可正文和原试用模板；目录只描述短评论，不提供效果测量。
- [Sauthor] [nichochar作者评论](https://news.ycombinator.com/item?id=50147872)：作者直接给出ari仓库与TUTOR.md思路，主张有趣而非提供学习成效数据。
- [Sdiscussion] [HN完整讨论上下文](https://news.ycombinator.com/item?id=50147861)：可读讨论仅作者自己一条评论，无独立复制用户；不能把投票数当学习验证。
- [Sreadme] [ari固定版本README](https://github.com/nichochar/ari/blob/b0c63994c3df49222efc2289f2c1d49145f3396f/README.md)：本地单用户、摄像头与主动提交、数据备份、订阅登录和安装条件。
- [Slicense] [ari MIT许可证](https://github.com/nichochar/ari/blob/b0c63994c3df49222efc2289f2c1d49145f3396f/LICENSE)：允许按MIT条件复制和修改，需保留版权与许可声明，不承诺教育效果。
- [Scode] [请求与评分校验代码](https://github.com/nichochar/ari/blob/b0c63994c3df49222efc2289f2c1d49145f3396f/server/app.ts)：可读性、相关性、评分量规和来源限制；只读代码审查，不是运行验收。
- [Sprompt] [辅导与验证提示逻辑](https://github.com/nichochar/ari/blob/b0c63994c3df49222efc2289f2c1d49145f3396f/server/ai.ts)：提示/问答/检查模式区分，生成与再验证调用；提示约束不等于稳定效果证明。
- [Sprovider] [Codex短请求适配器](https://github.com/nichochar/ari/blob/b0c63994c3df49222efc2289f2c1d49145f3396f/server/codex-provider.ts)：read-only与工具禁用、图像输入、额度错误处理；本地启动仍调用模型服务。
- [Spersonal] [个性化文档实现](https://github.com/nichochar/ari/blob/b0c63994c3df49222efc2289f2c1d49145f3396f/server/personalization.ts)：教学与用户文档及记忆的范围、哈希更新和恢复标识，不是已证明学习掌握。
- [Sagent] [会话与工具恢复实现](https://github.com/nichochar/ari/blob/b0c63994c3df49222efc2289f2c1d49145f3396f/server/codex-learning-provider.ts)：原生会话、工具回执及不自动换模型逻辑；区别短请求路径与持续学习代理。
- [Sci] [上游固定提交CI](https://github.com/nichochar/ari/actions/runs/39198839019)：固定提交上游privacy/test/build步骤成功；不是研究者实测或学习效果试验。
- [Sissues] [公开问题与PR检索](https://github.com/nichochar/ari/issues)：state=all列表空，本轮未取得独立用户问题；零问题不是零缺陷。
- [Skhan] [Khanmigo家庭替代](https://www.khanmigo.ai/parents)：官方4美元每月/44每年税前和美国开通条件，提供课程与家长功能；不是同等本地摄影流程。
- [Sstudy] [2025年数学辅导随机试验](https://www.pnas.org/doi/10.1073/pnas.2422633122)：相邻GPT4课堂研究区分练习表现与撤掉AI后的测验，不能迁移为ari有效性证明。
- [Sauth] [官方订阅与API登录区别](https://learn.chatgpt.com/docs/auth)：订阅登录与API按量登录分开，额度与权限按实际账户，不能称无限免费。

结构化记录：[research/tutor-you-through-pen-and-paper-math-with-a-local-agent.json](../research/tutor-you-through-pen-and-paper-math-with-a-local-agent.json)
