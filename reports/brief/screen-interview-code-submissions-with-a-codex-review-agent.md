# 用 Codex 按预设规则初审面试代码提交

## 中文

    用 Codex 审查智能体初筛面试代码提交
    一位评论者使用 Codex 和有针对性的 agents.md 进行第一轮代码审查，拒绝修改或新增文件过多的提交。
    使用工具
    CX
    Codex
    GP
    ChatGPT
    做了什么
    一位评论者说，自己配置了 ChatGPT Codex 和一份有针对性的 agents.md 文件，用于编码提交的初步审查。智能体按简单的准入规则审查每份提交，并自动拒绝修改或新增文件过多的提交；规则仍由人选择，智能体作为第一道筛查工具。
    结果如何
    帖子没有提供指标、示例或与人工审查的比较。它只声称，这种做法用于在招聘流程较早阶段应对低质量、AI 辅助完成的提交。
    值得了解
    值得注意的是筛选器范围很窄：他们围绕文件数量、新增或修改文件上限等明显的审查启发式规则进行调整，而不是完整的自主招聘决策。
    亲自试用
    使用
    Codex
    复制提示词
    为[仓库或带回家完成的项目]编写一份 agents.md，告诉你如何筛查候选人的提交：标记任何修改或新增超过[数量]个文件、不遵守[要求]或缺少测试的提交。然后按该文件审查[文件夹路径]中的提交，并给我一份通过或拒绝的建议及理由。当我拿到可以使用的简短审查意见时，任务就完成；不要联系候选人，也不要在任何地方发布内容。
    原始来源：https://www.reddit.com/r/ExperiencedDevs/comments/1qbw1t3/dealing_with_the_flood_of_incompetent_aitethered

<details><summary>English original</summary>

    Screen interview code submissions with a Codex review agent
    A commenter uses Codex with a targeted agents.md for front-line code reviews, rejecting submissions with too many files changed or added.
    Done with
    CX
    Codex
    GP
    ChatGPT
    What they did
    A commenter said they set up ChatGPT Codex with a targeted agents.md file to handle first-pass reviews of coding submissions. The agent reviewed each submission against simple gate rules and automatically rejected ones with too many files changed or added; the human still chose the rules and used the agent as the front-line screener.
    How it went
    The post gives no metrics, examples, or comparison to manual review. It only claims this was being used to fight low-quality, AI-assisted submissions earlier in the hiring funnel.
    Worth knowing
    The useful catch is how narrow the filter was: they tuned it around obvious review heuristics like file-count and added/changed-file limits, not a full autonomous hiring decision.
    Try it yourself
    with
    Codex
    Copy prompt
    Write an agents.md for [repo or take-home project] that tells you how to screen candidate submissions: flag any submission that changes or adds more than [number] files, doesn't follow [requirement], or lacks tests. Then review the submission in [folder path] against it and give me a pass or reject recommendation with reasons. You're done when I have a short review I can use; don't contact the candidate or post anything anywhere.
    Original source: https://www.reddit.com/r/ExperiencedDevs/comments/1qbw1t3/dealing_with_the_flood_of_incompetent_aitethered

</details>

## 原作者方法

原Reddit全文未读取，不绕既有访问限制；目录模板不是作者实际agents.md。

## 结论

保留目录完整原文及翻译，并分析具体规则和替代方案；原案没有样本、指标或独立效果验证，交付有依据简报。

## 文件数量筛查不是能力评估

目录明确说有人实际使用自动拒绝，但没有给出规则阈值、样本、误拒率或招聘结果。原文翻译保留这种表述，不等于认可其效果。文件改动多可能来自重命名、项目结构或生成物，少也可能只是把大量改动塞进一个文件。由数量推断能力或是否使用AI没有本案证据。源站试用模板写的是给人建议，又不同于摘要里自动拒绝的行为，不能把两种流程混为一谈。

来源：Sdirectory, Sgit

## 需求是减轻审阅负担，付款尚未验证

可能使用者是技术面试官或工程负责人，付款预算可能来自招聘评估或工程管理。但案例没有说明公司、提交量、人工成本或采购意愿。需求假设是让人尽早看到不符合明确作业规范的位置，而不是把候选人排序交给黑箱。低频招聘或作业很短的团队，直接人工检查或CI规则更省事；只有大量同题提交且规则明确，整理证据的工具才可能降低重复劳动。

来源：Sdirectory, Sreview

## 先规范输入，再输出可核对证据

研究者建议固定作业模板与基准提交，记录提交SHA，确认比较的是候选人的有效改动而非仓库历史。文件数量、禁止路径和是否存在测试可以用确定性检查完成；代理再解释具体违规位置、缺失上下文和不确定项。候选人提供的README、注释或agents.md属于待审内容，不应成为覆盖评估规则的指令。输出应有规则编号、文件行号和支持证据，并让人复核；本轮没有处理任何真实候选资料，也没有给出招聘决定。

来源：Sgit, Sreview, Sdirectory

## 评价工具也需要被评价

先用人工标注的合成或获授权样本检验规则，覆盖合理多文件实现、少文件但错误实现、重命名、缺测试和运行环境失败。记录错误标记、遗漏问题、人工复核时间及不同语言的表现，而不只记录处理速度。没有跑通依赖与业务测试时，应标为未验证，而不是直接判定代码不合格。MCR-Bench摘要研究多轮代码审查，不是本案筛选器，因此只用于提示上下文与缺陷状态问题，不能搬用为候选人识别准确率。

来源：Sbenchmark, Scopilot

## 无需模型的规则应先用脚本

若唯一标准是新增或修改文件不能超过某个数，Git差异统计配合固定规则脚本更容易解释、复现和测试，未必需要付出模型调用与提示维护成本。GitHub原生审查支持逐行证据及请求修改，Copilot则是已有的AI审查替代，但官方仍要求人工检查其误报和遗漏。采用代理的额外价值应体现在理解任务语义与整理证据，而不是把一个简单计数包装成AI招聘产品。

来源：Sgit, Sreview, Scopilot

## 按一份提交的辅助审查计算

下列是研究者假设，美元计价，不是本案报价或收入。规则稳定情景：模型0.10、人工5分钟按40/小时=3.33、其它0.07、获客摊销0.50，单位4.00；每月100份另加固定40，共440。复杂情景：模型0.80、人工20分钟按40/小时=13.33、其它0.37、获客1.50，单位16.00；每月100份加固定160，共1760。售价未知，不计算利润。规则设计、数据授权、人工标注和争议复核另计，不能用token费用冒充总成本。

来源：Scopilot, Sreview

## 可试点证据整理，不销售自动淘汰承诺

可探索为已有技术招聘客户提供规则配置、代码证据报告和审查留痕服务，但属于经营假设。获客可用虚构提交展示规则如何解释，不公开候选代码或姓名；本轮无外联。交付包括规则版本、基准、验证日志和未解决问题，最终评估仍交由负责的人。没有误拒与复核成本资料时，不应承诺更公平、更准确或自动辨别AI作弊。客户已有CI与审阅规范时，切换成本很可能大于一个计数筛选器的收益。

来源：Sdirectory, Sreview

## 自用更适合提交前自检

个人开发者可用同类规则检查自己的练习是否越界修改、是否缺测试，再人工理解具体原因。设置要定义文件范围、生成物例外、基准与测试命令；维护要跟随模板及依赖升级，频率按每次练习提交而非日常打卡。可能收益是少遗漏显式要求，但未实测省时。私密代码与身份资料不应随便放入外部提示，错误风险包括把环境问题当实现问题、把简洁风格当唯一正确风格。

来源：Sdirectory, Sgit, Scopilot

## 不建议据此投入自动筛人业务

当前仅建议受控的代码证据辅助试点，不支持把这个案例当可复制的自动淘汰商业机会。原作者方法全文未读取，真实样本和独立用户效果反馈都缺失。多次社区及问题库搜索主要命中工具权限或环境问题，未找到能验证本案招聘效果的反馈，不能拿不相干投诉凑数。若规则对同样合理的实现给出不同结论，或人工复核时间超过原流程，应停止扩大；先补明确定义、对照样本和可解释证据，再讨论收费。

来源：Sdirectory, Sbenchmark, Scopilot

## 自用与试用

- 开发者和负责人工复核的代码审阅者。
- 检查显式作业规范并整理代码级证据。
- 可能减少遗漏和重复检查，净省时与误报率未知。
- 固定基准、允许路径、生成物规则与验证命令。
- 随作业模板和依赖更新规则，复核误报。
- 每次提交或审阅时使用。
- 候选代码和个人资料可能私密，使用前需明确授权与最少输入。
- 文件数代理指标失真、上下文缺失、环境失败被误判、风格偏差。

合成或获授权代码样本、固定基准、公开明确的作业规范与人工复核。
可核对规则与代码证据的审查草稿，不联络候选人、不自动作招聘决定。

## 来源

- [Sdirectory · 许可目录案例](https://agentusecases.ai/use-case/screen-interview-code-submissions-with-a-codex-review-agent)：作者自述用定向agents.md和文件数规则初筛面试代码；没有指标、示例或人工对照。
- [Sgit · Git差异文档](https://git-scm.com/docs/git-diff)：差异取决于工作树、索引、提交端点或共同祖先，比较基础需要明确。
- [Sreview · GitHub代码审查流程](https://docs.github.com/en/pull-requests/get-started/reviewing-pull-requests-quickstart)：审查先理解上下文，再针对改动行评论；评论、批准与请求更改是不同结果。
- [Scopilot · Copilot审查应用说明](https://docs.github.com/en/copilot/responsible-use/agents)：另一产品Copilot结合代码、PR上下文和自定义指令生成意见；官方指出漏报、误报和语言或风格偏差。
- [Sbenchmark · MCR-Bench研究摘要](https://arxiv.org/abs/2608.27442)：2026年8月27日摘要描述2269个五语言多轮代码审查任务，报告跨轮状态跟踪与缺陷识别局限；不是招聘有效性或Codex专项实验。

## 核验边界

无真实候选数据处理、招聘决定、代码执行或收益实测。浏览器首次导航及5分钟后唯一恢复均超时，使用获许可存档；论文只读摘要。
