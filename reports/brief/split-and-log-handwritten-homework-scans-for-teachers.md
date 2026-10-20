# 用Claude Code拆分手写作业扫描件并登记提交情况

## 中文

    为教师拆分手写作业扫描件并登记提交情况
    一个Claude Code技能读取批量扫描件上的手写姓名，将其与花名册匹配，为每位学生拆分出PDF，更新完成情况表，并标出未交作业。
    使用的是
    CC
    Claude Code
    他们做了什么
    这个技能接收一份批量扫描的作业PDF，通过视觉识别每页上的手写姓名。它将这些姓名与学生花名册进行模糊匹配，因此不同的拼写形式也能匹配。随后，它把PDF拆分为每位学生一份文件，并更新Excel完成情况表。对于超过99页的批次，它可以恢复会话继续处理。它要求进行人工核验。
    进展与成效
    该介绍没有给出实测结果或耗时。它说，人工核验步骤旨在让学生归属判断完全准确，并把在大型花名册中识别未交作业列为一种用途。
    值得了解
    要准备好人工检查姓名匹配，因为这个技能要求人工核验。超过99页的批次需要使用它的会话恢复功能。
    亲自尝试
    使用
    Claude Code
    复制提示词
    创建一个可复用的技能，处理[文件夹路径]中成批的手写作业扫描PDF。它应读取每页上手写的学生姓名，与[花名册文件]中的名单匹配，将扫描件拆成每位学生一份PDF，并更新[完成情况表]，标记谁提交了作业。最后列出未交作业的学生，以及任何无法有把握匹配的姓名。写入任何内容之前，先向我展示计划如何拆分以及如何修改表格，并且绝不要删除原始扫描件。
    原始来源：https://mcpmarket.com/tools/skills/homework-grading-workflow

<details><summary>English original</summary>

    Split and log handwritten homework scans for teachers
    A Claude Code skill reads handwritten names on batched scans, matches them to a roster, splits PDFs per student, updates the completion spreadsheet and flags missing work.
    Done with
    CC
    Claude Code
    What they did
    The skill takes a batched PDF of scanned homework and uses vision to read the handwritten name on each page. It fuzzy-matches those names to the student roster, so spelling variations still match. It then splits the PDF into one file per student and updates the Excel completion spreadsheet. For batches over 99 pages it can resume a session. It requires a manual verification step.
    How it went
    The listing gives no measured results or timings. It says the manual verification step is meant to make student attribution fully accurate, and it describes missing-assignment identification across large rosters as a use case.
    Worth knowing
    Expect to check the name matches by hand, because the skill requires manual verification. Batches over 99 pages need its session-resume feature.
    Try it yourself
    with
    Claude Code
    Copy prompt
    Create a reusable skill that processes batches of scanned handwritten homework PDFs in [folder path]. It should read the handwritten student name on each page, match it against the roster in [roster file], split the scans into one PDF per student, and update [completion spreadsheet] to mark who turned the work in. Finish with a list of students with missing work and any names you couldn't match confidently. Show me the planned splits and spreadsheet changes before writing anything, and never delete the original scans.
    Original source: https://mcpmarket.com/tools/skills/homework-grading-workflow

</details>

## 原作者的方法与来源

https://mcpmarket.com/tools/skills/homework-grading-workflow
方法来自第三方托管技能文本，源仓库404，未核验作者代码或运行。
Load a roster, inspect scanned pages, group by student, and record submission status.
读取花名册，检查扫描页，按学生分组并登记提交状态。

## 简要分析

商业分数未评定。

### 作业归档与提交登记，不是批改成绩

目录描述识别姓名、按学生拆PDF、在Excel登记提交和列出缺交。托管技能还描述增加作业列、标X并更新Total公式；这里没有对答案评分、判定学习质量的证据。标题中的grading不能扩展成自动批改。代码仓库两次404，不能核验实现、依赖或许可；原介绍没有准确率样本、批次耗时或真实学校采用结果，因此本篇按简报计数。

依据：[Sdirectory](https://agentusecases.ai/use-case/split-and-log-handwritten-homework-scans-for-teachers), [Sskill](https://mcpmarket.com/tools/skills/homework-grading-workflow)

### 可见技能流程中的两处落差

第三方托管SKILL先建立追踪文件再让用户确认计划，而许可目录模板要求写入任何内容之前展示计划。复用时需把预览与写入边界统一。技能把精确匹配列高置信度、模糊匹配列中置信度并继续，只有低置信度留人工处理；这不等于人工逐项确认所有学生。全准确的宣传不能代替独立测量。本文只阅读这些指令，没有执行、安装或发送任何扫描件。

依据：[Sskill](https://mcpmarket.com/tools/skills/homework-grading-workflow), [Sdirectory](https://agentusecases.ai/use-case/split-and-log-handwritten-homework-scans-for-teachers)

### 未知姓名要保留待核对区

技能一处要求所有页都归属学生，拆分阶段却跳过Unknown。研究者据此提出：未知页必须单独保留并计数，不能强行分给最像的姓名，更不能因为它未入个人PDF就认定某学生未交。每页需保留输入页号、候选、置信原因、人工结论和输出文件对应；同名同班、多页无姓名、换班、重复扫描、空白和旋转页都应进入测试。姓名相似不是身份相同。

依据：[Sskill](https://mcpmarket.com/tools/skills/homework-grading-workflow)

### 先减少扫描问题，再比较agent收益

Gradescope建议扫描前清点纸页，扫描后比较PDF页数，固定长度作业分组，异常长度另行处理并保持纸张格式一致。研究者将这些作为低成本对照：标准姓名栏、明确学生编号、固定页序与人工分组，可能先减少大部分错误。Gradescope现成流程也是替代，但本轮未核定机构报价或全部功能。不能只与最混乱的手工场景比较，然后将改进全归功于agent。

依据：[Sscan](https://guides.gradescope.com/hc/en-us/articles/21707758815245-Scanning-Tips)

### 99页是技能安排，不是统一平台上限

托管技能按每会话最多99张图像分批并保存逐页状态。当前Claude API文档按上下文给出PDF请求100页或600页的上限及32MB请求约束，还受内容密度影响。API整份PDF与Claude Code逐页图像流程不同，不能直接替换阈值或说99页已失效。可复制性需要核对实际工具版本、上下文、恢复文件和幂等性，验证续跑不会重复标记或漏页。

依据：[Sskill](https://mcpmarket.com/tools/skills/homework-grading-workflow), [Spdf](https://platform.claude.com/docs/en/build-with-claude/pdf-support)

### 先获学校批准，再考虑真实学生资料

学生姓名、作业和提交状态可能属于教育记录。美国教育部FAQ建议教师先核对学校或学区批准的工具，相关例外有学校控制及用途等条件；其他地区须另行核对，本文不认定该技能符合法律。托管技能提到困难页面可交另一模型协助，这会增加接收方和成本，不能默认启用。优先用虚构编号与合成页验证，实际使用前确认数据处理、保留、访问、删除和备份规则。

依据：[Sprivacy](https://studentprivacy.ed.gov/faq/i-want-use-online-tool-or-application-part-my-course-however-i-am-worried-it-violation-ferpa), [Sskill](https://mcpmarket.com/tools/skills/homework-grading-workflow)

### 买方可能是学校，收益尚未测出

商业需求假设是教师反复整理纸质作业，付款人可能是学校、教研组或教师本人。可设想按校交付配置、培训和维护，或按明确批次提供校内处理支持；目前没有价格、客户、收入或采购周期证据。获客假设是提供合成样本演示及可审阅差异清单，而不是先索取真实学生资料。与学校现有作业系统和标准化扫描比较后，只有复核后仍节约时间才有继续验证的理由。

依据：[Sdirectory](https://agentusecases.ai/use-case/split-and-log-handwritten-homework-scans-for-teachers), [Sskill](https://mcpmarket.com/tools/skills/homework-grading-workflow)

### 错误复核和维护可能吃掉节省

模型、已有订阅或API使用成本未知，不能声称免费。成本项还包括扫描准备、名单清理、姓名歧义处理、逐页核验、Excel公式和备份、版本更新、学校审查、培训及获客。关键指标应是每批总人工分钟和错分修复分钟，不只模型运行时间。没有这些数据不编造利润表或ROI；本简报保留待测成本，不冒称符合完整深研的经济测算门槛。

依据：[Sskill](https://mcpmarket.com/tools/skills/homework-grading-workflow), [Sscan](https://guides.gradescope.com/hc/en-us/articles/21707758815245-Scanning-Tips)

### 教师自用也需要独立核对

适合已获准处理作业、能够审核页码与表格差异的教师。可能收益是少做重命名、拆分和抄表，实际收益未知。首次需准备扫描规范、花名册字段、目录副本和Excel映射；每学期维护班级变化，每次检查缺页、同名和公式。频率跟随作业批次。隐私风险来自学生记录出机，错误风险是错分给同学、误报缺交和误改累计统计；不得直接据输出采取扣分或通知家长等后续行动。

依据：[Sdirectory](https://agentusecases.ai/use-case/split-and-log-handwritten-homework-scans-for-teachers), [Sskill](https://mcpmarket.com/tools/skills/homework-grading-workflow)

### 合成批次先验页数守恒与无覆盖

拟议演练使用虚构学生编号，设计同名、漏名、多页、重复和跨99页恢复，不使用真实学生内容。输出待审映射、每人PDF计划、未知页清单和表格差异；所有输入页都必须落在已确认输出或明确待核对区。确认后也只写副本，检查公式、原始扫描未变和重复运行不重复登记。对照人工标准答案，测总复核时间；若仍错分或比规范人工流程更慢，停止扩大使用。本轮未实际试用。

依据：[Sskill](https://mcpmarket.com/tools/skills/homework-grading-workflow), [Sscan](https://guides.gradescope.com/hc/en-us/articles/21707758815245-Scanning-Tips)

## 试用准备与预期结果

虚构学生编号、合成扫描、人工答案和表格副本。
可核对的页号映射、未知页清单与表格差异；未实际运行。
只用给定虚构编号和合成作业页，先输出逐页映射、歧义、未匹配页及表格拟改差异。每页必须可追溯，未知不得强配或用于认定缺交。未确认前不写文件，确认后仅写副本，保留原扫描和公式；不访问真实学生资料，不调用额外模型。

## 来源

- [许可目录案例](https://agentusecases.ai/use-case/split-and-log-handwritten-homework-scans-for-teachers)：目录明示无实测结果和耗时；保留完整原模板。
- [MCPMarket托管技能说明](https://mcpmarket.com/tools/skills/homework-grading-workflow)：实际读取列表和SKILL页签；第三方托管内容，不是已核验源仓库。
- [Gradescope扫描建议](https://guides.gradescope.com/hc/en-us/articles/21707758815245-Scanning-Tips)：扫描前后核对页数、固定页长分组，不规则作业分开处理。
- [Claude API PDF支持](https://platform.claude.com/docs/en/build-with-claude/pdf-support)：API页数和请求大小约束不同于本技能99张逐页图像的会话安排。
- [美国教育部课堂工具隐私FAQ](https://studentprivacy.ed.gov/faq/i-want-use-online-tool-or-application-part-my-course-however-i-am-worried-it-violation-ferpa)：教师应先确认学校批准工具及适用条件；不证明该技能合规。
- [列表指向的GitHub仓库](https://github.com/sallvainian/sallvain-marketplace)：无法核验代码、许可、测试或当前实现。
