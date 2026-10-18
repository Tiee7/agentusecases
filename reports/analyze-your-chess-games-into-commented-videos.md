# 用 Claude Code 将国际象棋对局制作成解说视频

## 中文

    将你的国际象棋对局制作成带解说的分析视频
    一个 Claude Code skill 将 Claude 的视觉能力、Stockfish 和你的语音笔记结合起来，把一盘 Lichess 对局制作成带解说的视频分析。
    实际使用
    Claude Code
    他们做了什么
    作者在一盘 15+10 快棋对局中录下了自己边下边说的思考过程，然后把 Lichess 链接和 mp3 交给 Claude Code。Claude 使用 whisper.cpp 在本地转录音频，并利用 PGN 中的棋钟时间，将每句话与对应的走子对齐。它用 Stockfish 逐步扫描对局，再由子代理针对每个失误向引擎提问。之后，一轮核验检查结果，再将分镜脚本制作成带旁白的视频。
    结果如何
    它为作者的真实对局生成了带注释的 PGN、一个 HTML 棋盘，以及一段 6 分 49 秒、带字幕和旁白的视频。作者说错误很少，但 AI 仍可能出错。
    需要知道的事
    完整运行大约需要一小时处理时间，因此应把它用于你花时间认真思考过的慢棋对局，而不是超快棋。
    自己试试
    推荐工具
    Claude Code
    复制提示词
    请获取我在 Lichess 上的这盘对局：[对局 URL]，用 Stockfish 分析，找出最大的失误和最佳走法。结合我在[音频文件或文本文件]中的笔记，制作一个带解说的对局讲解视频。视频文件保存后停止，并给我一份简短清单，列出讲解涵盖的关键时刻。
    原始来源：https://github.com/brumar/chess-postmortem-skills

<details>
<summary>英文原文</summary>

    Analyze your chess games into commented videos
    A Claude Code skill uses Claude vision plus Stockfish and your audio notes to turn a Lichess game into a commented video analysis.
    Done with
    CC
    Claude Code
    What they did
    The author recorded themselves thinking aloud during a 15+10 rapid game, then gave Claude Code the Lichess link and the mp3. Claude transcribed it locally with whisper.cpp and matched sentences to moves using PGN clock times. It ran a Stockfish sweep, and subagents questioned the engine about each mistake. A verifier pass checked the result, then a storyboard became a narrated video.
    How it went
    It produced an annotated PGN, an HTML board and a 6:49 narrated video with subtitles for the author's real game. The author says errors are rare but the AI can still get things wrong.
    Worth knowing
    A full run takes about an hour of processing, so use it on slow games where you took time to think, not on blitz.
    Try it yourself
    with
    Claude Code
    Copy prompt
    Take my chess game from Lichess at [game URL] and analyze it with Stockfish to find the biggest mistakes and best moves. Combine that with my notes in [audio file or text file] and produce a commented video walkthrough of the game. Stop when the video file is saved and give me a short list of the key moments covered.
    Original source: https://github.com/brumar/chess-postmortem-skills

</details>

## 原作者的方法与来源

来源：[brumar 的 chess-postmortem-skills README](https://github.com/brumar/chess-postmortem-skills)

作者方法摘要

1. 在慢棋对局中记录思考，再把对局和可选的笔记或音频交给Claude Code。
   English summary: Record thoughts while playing a slow game, then provide Claude Code with the game and optional notes or audio.

2. 在本地转录音频，利用棋钟对齐，用Stockfish调查失误，并核验注释。
   English summary: Transcribe audio locally, align it using game clocks, investigate mistakes with Stockfish, and verify the annotations.

3. 保留带注释的PGN与HTML棋盘，请求生成旁白视频，再回看仍不明白的位置。作者提醒仍会出错，且处理耗时较长。
   English summary: Keep the annotated PGN and HTML board; request a narrated video, then revisit positions that remain unclear. The author warns about errors and substantial processing time.

## 我们的分析

**商业结论：适合内部效率工具。个人思考录音复盘有用途，教学效果与交付成本仍需验证**

公开代码和示例说明作者能把棋局、思考记录、引擎线路和视频串联，保留了可检查PGN与HTML。但全流程约一小时，作者估计某局API等价成本约15美元，还需要解释、笔记归属和字幕同步审核。Lichess免费分析已覆盖基础任务，未见本项目的独立教学验证、付费客户或持续使用证据。先限定自用复盘和人工核对，不据视频完整度投入独立自动教练业务。

案例ID：`analyze-your-chess-games-into-commented-videos` · 案例来源：https://agentusecases.ai/use-case/analyze-your-chess-games-into-commented-videos
研究时间：2026-10-18T02:41:29.568104+00:00

**商业评分：23.0/100。用户反馈信号占5%。**

| 维度 | 权重 | 分数 /5 | 商业依据 |
|---|---:|---:|---|
| 付费需求 | 20% | 1 | 慢棋爱好者有复盘用途，但没有付费客户、预算、频次或购买意愿证据。 [S4b894348badc, Sa65477dc17e5, Sa089efa83c5a] |
| 业务价值与效果证据 | 20% | 2 | 公开产物与代码支持可理解流程，尚无独立质量、学习效果或重生成验证。 [S4b894348badc, S47b21d022697, S68a9ec9b8f5f] |
| 单位经济与利润 | 20% | 1 | 作者自估约15美元API等价成本且未优化，两情景均对人工和返工敏感。 [Sa65477dc17e5, S58333316475e, S68a9ec9b8f5f] |
| 获客与市场进入 | 15% | 1 | 公开仓库与HN讨论提供曝光，未证明持续使用、销售或低成本获客。 [S4b894348badc, Sa65477dc17e5] |
| 竞争壁垒 | 10% | 0 | 开源流程依靠现成引擎与媒体组件，没有独占数据、渠道或验证的教学积累。 [S4b894348badc, Sfea32cda253b, Sa089efa83c5a] |
| 交付与经营风险 | 10% | 2 | 有明确代码、引擎线路与核验要求，但笔记错位已发生，教学和视频审核仍需人工。 [S47b21d022697, S68a9ec9b8f5f, Sceff1d5acd33, S59f1c523fe28] |
| 独立用户反馈信号 | 5% | 0 | 只取得作者自述、旁观讨论及相邻实现经验，没有本项目独立使用结果；不是零满意度。 [Sa65477dc17e5, S4b894348badc] |

## 自用价值：中

条件性推断：有完整思考记录、愿意等待并能检查棋盘的人，可用公开流程组织个人复盘；没有量化学习或节时证据。

依据：S4b894348badc, Sa65477dc17e5, S47b21d022697, S68a9ec9b8f5f

- 适用人群：会使用Claude Code、能核对走法及引擎线路的慢棋/快棋爱好者。
- 用途：把对局、自己的问题与可追溯引擎证据整理成PGN、HTML和可选视频。
- 预期收益：针对真实疑问组织复盘并便于回看；不声称提高棋力或替代主动练习。
- 设置成本：已有合法工具与足够额度、公开或获准PGN、可选笔记，及依赖审查与受众水平设定。
- 维护成本：处理对齐、错误解释、引擎/依赖版本、声音和字幕/画面同步，视频环节可另选。
- 使用频率：挑选值得认真思考的对局，非每盘超快棋；作者每局处理约一小时。
- 隐私风险：思考录音、身份与笔记是个人信息，不因示例公开就默认提交用户资料；本轮仅公开材料。
- 错误风险：合法线路不代表解释正确，笔记错位、分数视角和安静局面计划均需复核。

## Copy prompt · 动手试用

### 源站试用模板

出处：https://agentusecases.ai/use-case/analyze-your-chess-games-into-commented-videos

建议工具：Claude Code

    Take my chess game from Lichess at [game URL] and analyze it with Stockfish to find the biggest mistakes and best moves. Combine that with my notes in [audio file or text file] and produce a commented video walkthrough of the game. Stop when the video file is saved and give me a short list of the key moments covered.

自编试用模板

准备条件：公开或合成PGN、人工确认的关键位置、可选获准文字笔记、已有工具说明；无需私人录音或新凭据。

工具：实际与推荐均为Claude Code；作者使用Stockfish、whisper.cpp及视频组件，本轮不安装或调用这些组件。

预期结果：待检查的关键位置与证据表、笔记归属和制作计划；自编模板未实测，不声称视频已保存。

### 先核对棋局复盘的证据与制作范围

自编模板

出处：研究团队自编

依据：S47b21d022697, S68a9ec9b8f5f, Sc4e399d9bda2, Sceff1d5acd33

    仅检查[公开或合成PGN]、[明确走子索引的文字笔记]及[已有引擎结果]。先列出对局、受众水平、分数视角与缺失信息，不安装依赖、不下载模型、不创建凭据、不调用额外付费API。按关键位置给出PGN走子索引、FEN、原走法、引擎候选线路及不确定解释；没有引擎结果时不要冒充已验证。棋手想法只能来自该位置或笔记明确提及的走法，其他情况写未知，不挪用后一步笔记。将战术线路事实与局面计划推断分开，给人工复核清单。再提出可选PGN/HTML与视频分镜方案，逐镜标注走子、旁白、箭头和字幕核对点。先说明哪些步骤只是计划及预期成本边界，不运行陌生项目或声称已生成、保存视频。

### Check evidence before producing a chess review

自编模板

出处：研究团队自编

依据：S47b21d022697, S68a9ec9b8f5f, Sc4e399d9bda2, Sceff1d5acd33

    Inspect [public or synthetic PGN], [move-indexed text notes] and [existing engine results] only. Identify the game, audience level, score perspective and missing information without installing dependencies, downloading models, creating credentials or calling additional paid APIs. List key positions with ply, FEN, played move, engine lines and unresolved explanations. Never claim engine verification without results. Attribute player beliefs only to notes covering that position or explicitly named moves; mark other beliefs unknown. Separate tactical evidence from inferred positional plans. Propose optional PGN/HTML and video storyboards with move, narration, arrow and subtitle checks. Return a plan and human-review checklist, without running unknown code or claiming a saved video.

## 已核验事实

- 源站实际与推荐工具均为Claude Code，作者README也明确以Claude Code skills呈现项目。 [S46c2f995eb9b, S4b894348badc]
- 作者展示15+10快棋、法语思考录音与英文6:49视频的例子，并称全流程约需一小时；本轮未观看或重生成视频。 [S4b894348badc]
- 作者在HN按日志估算上一盘若按API价约15美元，并称尚未优化；不是实际已支付账单或稳定单局报价。 [Sa65477dc17e5]
- 分析说明要求按PGN棋钟对齐录音、核验注释，并记录了把后一步笔记错误用于较早位置的已发生缺陷。 [S47b21d022697, S68a9ec9b8f5f]
- 固定提交sweep.py默认深度22、失误阈值30厘兵并使用白方分数视角，这些是实现设置而非普遍棋理标准。 [Sc4e399d9bda2]
- 固定提交query.py支持限定根走法和保存候选线路，官方python-chess文档也提供相应分析参数。 [Sceff1d5acd33, Sb791f0d44020]
- 固定提交视频脚本读取分镜，以Piper或espeak生成语音，再用ffmpeg拼接视频并输出字幕；没有执行该代码。 [S59f1c523fe28]
- Lichess当前功能页提供免费棋盘分析、错误练习、研究和PGN导入导出，服务器深度分析列为每日40局。 [Sa089efa83c5a]
- Stockfish官方说明其为使用UCI的免费开源引擎，GPLv3；引擎强度不直接证明自然语言讲解正确。 [Sfea32cda253b]
- 当前Claude Pro月付20美元、包含Claude Code且有用量限制，不能换算为本流程的保证局数或免费无限运行。 [S58333316475e]
- 作者在HN承认对深层局面判断不应期待过高；相邻开发者经历和旁观评论不是本项目独立复现。 [Sa65477dc17e5]

## 慢棋复盘者与付款人

结论是适合内部效率工具，商业分数23/100。真正有区别的部分是把棋手当时的疑问与引擎线路对应，再整理成容易观看的复盘。作者公开了一盘真实快棋的多种产物，并表示自己喜欢看视频；这支持个人用途，不能推出学习效果、棋力提高或订阅购买意愿。

适用人群是愿意记录思考、能运行Claude Code并能核查棋盘的慢棋或快棋爱好者。作者不建议用于每盘超快棋。潜在付款人可以是棋手本人，也可以是代学生准备材料的教练，但后者只是经营假设，来源没有教练客户、学校采购、学生留存或预算证据。已经付费的工具用户和从零配置环境的人，设置成本不同。

自用价值为中，条件是允许等待、愿意核对关键局面，并把视频当复盘辅助。棋手自己的语音比猜测其想法更有针对性，却也增加记录与对齐负担。没有对照实验表明视频优于自己分析、做题或真人指导，不能把观看更舒服写成掌握更牢。

依据：S46c2f995eb9b, S4b894348badc, Sa65477dc17e5

## 引擎证据与视频是两段交付

公开流程先确定受众水平，读取PGN和可选思考录音；whisper.cpp在本地转录，利用棋钟及少数锚点将文字对齐到走子。随后逐步扫描，按失误分配调查，追问自然走法的反驳，再合并注释、复核和生成HTML。视频在已分析的PGN与分镜之上增加旁白、箭头和字幕，不应从一段解说直接反推棋局证据。

固定提交eca0edf的静态代码提供了可检查细节：sweep默认深度22、阈值30厘兵，保留白方视角；query支持限定候选根走法并保存线路。python-chess文档也明确深度、候选线路、分数视角与将杀分数是不同参数。30厘兵是作者工作流阈值，不是普遍教学定律；同深度、不同局面也不代表耗时相同。

make_video读取分镜，用Piper或espeak合成旁白，再用ffmpeg组合视频与字幕。分析说明要求合法走法校验和引擎抽查，视频说明另外要求抽帧与字幕位置核对。这些都是方法与实现证据；本轮没有安装作者项目、运行Stockfish、转录音频或生成视频，网站构建通过不等于棋局流程已复现。

依据：S47b21d022697, S68a9ec9b8f5f, Sc4e399d9bda2, Sceff1d5acd33, S59f1c523fe28, Sb791f0d44020

## 免费引擎分析已经覆盖什么

Lichess当前功能表列出免费的分析棋盘、从错误中学习、持久化研究以及PGN导入导出，服务器深度分析标示每日40局；这是读取时的公开额度，不代表作者当时使用的额度。Stockfish本身也是公开可获得的引擎。仅凭“找出坏棋并给出最佳走法”，新增服务很难说明收费理由。

尚需验证的缺口是解释棋手为什么会犯某种错误，以及把复杂线路整理成适合其水平的观看材料。拥有思考笔记可能让问题更明确，但输入者也要付出记录和回看时间。需求强度应按每月愿意认真复盘的对局数、当前人工负担和复盘后的使用行为衡量，不能按全体棋手、Github星数或论坛票数估计付费市场。

当前Claude Pro月付20美元且包含Claude Code，但存在额度限制。作者所说每局约15美元是按日志估出的API等价成本，不能把二者简单相除算出可交付局数，也不能把订阅包含工具视作免费无限算力。这里没有实际模型用量、客户月频次、服务报价或付费测试，市场规模与可销售套餐都未得到证明。

依据：Sa089efa83c5a, Sfea32cda253b, S58333316475e, Sa65477dc17e5

## 先与交互式复盘比较

最直接替代是Lichess分析棋盘和错误练习：棋手可以自己探索线路，而不必等待整套视频处理。它缺少本项目的思考录音讲解包装，但这不等于没有学习价值。比较应固定同一盘棋、同一组关键问题和相同使用时间，分别检查能否解释错误、是否主动推演及之后能否处理相似局面。

作者自己的反证是成本高、没有优化；HN讨论也区分了战术线路解释与安静局面的计划判断。强引擎给出的最佳着与自然语言解释正确，是两个验收对象。不能拿不使用工具的裸模型表现证明本系统失败，也不能凭引擎参与就证明其每句教学结论正确。

另一种实际选择是保留PGN及HTML交互产物，只在少数值得复盘的对局生成视频。这来自本项目已有多段输出，不需要先发明新产品。它能减少不必要的媒体制作，却仍需要验证是否降低模型调查和人工核对成本。真人教练可作为评审基准，本文没有读取报价，不虚构教练价格或声称能够替代指导。

依据：Sa089efa83c5a, S4b894348badc, Sa65477dc17e5, S47b21d022697, S68a9ec9b8f5f

## 约一小时等待与人工复核分开计费

作者报告约一小时处理，并估算某次会话按API计约15美元；前者是等待时间，后者是单次日志换算，两者都不是稳定服务成本。实际交付还包括音频准备、引擎计算、字幕检查、版本维护、返工、存储与支持。局面越复杂或解释越难确认，调查次数与审核时间越容易增加。

以下均为USD假设，不调用付费API。29美元单局视频，模型预算15美元、人工半小时乘40美元为20美元、其他2美元、获客5美元，可变成本42美元，单位贡献-13美元。每月20局、固定200美元，月贡献-460美元。15美元只是借作者估算设定的预算，并非我们的测量或现价保证。

另一假设为教练辅助的99美元限定复盘包，模型仍15美元、人工一小时乘40美元、其他5美元、获客10美元，可变70美元、贡献29美元；月20包减固定300美元，月贡献280美元。若每包再多一小时返工，贡献降到-11美元。该情景没有证明买家接受99美元，也不含税费与退款；用量受限的订阅不能代替总成本预算。

依据：Sa65477dc17e5, S58333316475e, S47b21d022697, S68a9ec9b8f5f, S59f1c523fe28

## 先验证是否有人反复使用

原项目在公开代码和Show HN中获得讨论，但讨论者对成本、解释质量和主动学习有分歧。公开曝光说明有人愿意讨论这个实验，没有证明能按可承担成本获取持续复盘的买家。作者自己使用和欣赏视频，与别人愿意每月付费是不同证据。

可检验的进入方式是假设一个已有教学关系的小范围复盘辅助：先由教练挑选问题明确、记录完整的慢棋，检查解说并决定哪些片段给学生。这个方案缩小了输入与复核范围，却把教练审核纳入成本，不能再声称完全自动化。没有授权和买家证据前，本文不联系任何棋手、机构或论坛用户。

获客阶段应记录愿意准备思考笔记、能完成首次复盘、再次主动使用和愿为下一包付费的比例，并把失败和返工算进去。观看次数、下载次数、代码星标和媒体转载都不能直接替代这些指标。若要靠逐局人工解释才能让客户认可，销售的实际上包含指导服务，成本不能只列视频渲染。

依据：S4b894348badc, Sa65477dc17e5, S47b21d022697, S68a9ec9b8f5f

## 记录与评审规范比包装更重要

代码公开，核心的棋局分析建立在Stockfish与python-chess上，旁白与视频也使用现成组件。README说明项目主体MIT并保留第三方资产的各自许可证；这不是所有依赖与声音资产都采用同一许可的结论。本轮没有打包分发项目或复制其完整文档，商业发布前应按实际交付组件单独核对。

可形成积累的是可回溯的解释审核集：原始位置、棋手问题、引擎线路、接受或修改的解释，以及学生后续能否解决相似问题。这是我们提出的经营资产假设，不是本项目已有的教学数据或效果证据。私人录音与对局身份不能因为能导出HTML就被默认公开，评审材料也不能未经许可跨用户复用。

当前没有专有数据、排他渠道、模型改进或客户迁移成本证据，壁垒维度0/5。个性化视频看起来更完整，不等于难以复制。若平台原生功能增加可解释反馈，额外服务必须靠可核验的教学工作和实际使用习惯说明价值，不能仅依赖多层agent的复杂度。

依据：S4b894348badc, Sfea32cda253b, Sb791f0d44020, S47b21d022697, S68a9ec9b8f5f

## 笔记错位是已知交付缺陷

分析与视频说明明确记载过去把某一步的笔记拿去解释更早走法的错误，导致反驳了棋手并未在那个位置表达的判断。因此“使用了本人录音”不能自动保证个性化正确；每条关于棋手想法的说法，都要能定位到同一走子或笔记明确提到的线路，缺失时保持未知。

其他验收对象包括PGN合法性、将杀与厘兵分数、分数视角、受众水平、分支返回、箭头及字幕画面同步。模型核验和引擎抽查能提供检查途径，但同一模型重复阅读不构成独立正确性证明，尤其安静局面的计划解释可能听起来合理却证据不足。用观众能复述一句结论代替棋力改善，也会夸大效果。

本轮只读公开资料与固定版本静态文件，没有执行依赖安装、引擎、语音模型或视频脚本。项目说明中的自动安装指令不在本轮执行范围，源码里的提交录音建议也不适用于本研究的私人资料。对外展示应另做明确发布决定，不能把公开仓库示例的做法推广成所有玩家的默认设置。

依据：S47b21d022697, S68a9ec9b8f5f, Sc4e399d9bda2, Sceff1d5acd33, S59f1c523fe28, Sa65477dc17e5

## 评论不等于项目独立复现

作者自述更愿意看针对自己思考的复盘，处理和成本高、尚未优化，承认局面判断局限。

相关体验：kuboble及Bootvis描述各自Claude/LLM与Stockfish实验的困难，jeremyjh讨论安静局面解释。

依据：Sa65477dc17e5, S4b894348badc

## 保留复盘辅助，先证明解释有效

适合内部效率工具的判断，承认公开流程和产物足以说明一个可理解的个人实验；不以此证明可经营的自动教练。最强反证是，有思考录音的人可能更愿意观看针对自己疑问的复盘，现成HTML也方便继续追问。这支持小范围验证，而不是否认个人收益；但观看便利尚未连接到重复使用、学习增益与支付意愿。

下一步应在已有获准环境中选少量公开或合成棋谱，先让人工评审核对一组战术与安静局面的问题、引擎线路和说法的归属，再比较交互PGN、视频及手动复盘。记录设置、调查、核验、返工和总等待时间；若有录音，逐条核对笔记映射。本文没有执行这个业务试验，不把计划写成已经通过。

若不能可靠标记不确定解释、持续错引棋手想法，或用视频替代主动思考却没有更好使用表现，应停止扩大。若99美元假设包频繁额外返工一小时，或买家只接受低于可变成本的价格，也不应靠扩大销量解释亏损。先保留PGN和HTML的可检查价值，能省去的制作环节应通过实测决定。

依据：S4b894348badc, Sa65477dc17e5, Sa089efa83c5a, S47b21d022697, S68a9ec9b8f5f

## 单位经济测算：情景假设，不是项目已实现的财务结果

| 情景 / 交付单位 | 收入 | 可变成本（含获客） | 单位贡献 | 月交付量 | 月固定成本 | 月经营贡献 |
|---|---:|---:|---:|---:|---:|---:|
| 全部假设：单局解说视频 / 一局限定范围视频 (USD) | 29.00 | 42.00 | -13.00 | 20 | 200.00 | -460.00 |
| 全部假设：教练辅助复盘包 / 一个限定范围复盘包 (USD) | 99.00 | 70.00 | 29.00 | 20 | 300.00 | 280.00 |

全部假设：单局解说视频假设：模型预算15借作者日志估算作假设，非账单或保证价；人工0.5小时×40美元，其他2、获客5均假设。可变42、贡献-13、月贡献-460，不含税费退款。；API成本 15，人工成本 20，其他可变成本 2，分摊获客成本 5。依据：Sa65477dc17e5, S58333316475e, S68a9ec9b8f5f

全部假设：教练辅助复盘包假设：收入99、模型预算15、人工1小时×40美元、其他5、获客10及月量固定成本均假设。可变70、贡献29、月贡献280；额外一小时返工使贡献-11。没有实际客户或报价，不含税费退款，不能用订阅额度承诺无限运行。；API成本 15，人工成本 40，其他可变成本 5，分摊获客成本 10。依据：Sa65477dc17e5, S58333316475e, S47b21d022697, S68a9ec9b8f5f

## 反证与未核实信息

作者公开完整流程和示例，认为针对本人疑问的视频更容易观看；项目同时保留交互式PGN/HTML。这支持限定自用的真实价值假设，不能因为缺少付费证据就说没有用途。反面是高处理量、作者自认成本未优化、局面解释和已发生笔记错位；尚无独立效果验证。

没有运行作者代码、引擎、转录、模型或视频，未观看示例视频或核对每句棋理；静态文件不是独立复现。15美元是作者按日志的API等价估算，非已付账单，当前价格与额度也不证明历史配置。没有客户、学习对照、留存、实际成本或独立本项目用户结果。Wanted未知，稳定目录第47不是热度排名。

## 具体动作与止损条件

在已有获准环境以少量公开或合成棋谱，比较PGN/HTML、视频和人工基线，核对战术、安静局面、笔记归属及全部工时；本轮不执行模型或引擎。

停止投入条件：持续错误解释或错引棋手想法、不能明确标出不确定项、没有重复使用，或返工使99美元假设包超出成本预算时停止扩大。

## 来源与对应关系

- [S46c2f995eb9b] [源站已提交案例全文](https://agentusecases.ai/use-case/analyze-your-chess-games-into-commented-videos)：支持案例描述、工具归属、作者成果自述和完整建议模板，不是运行质量或原作者实际提示词的独立验证。
- [S4b894348badc] [原作者 GitHub README](https://github.com/brumar/chess-postmortem-skills)：支持作者的思考录音、对齐、分析与视频流程、约一小时、6:49示例及幻觉警告；仅阅读说明和静态文件，未观看/重新生成视频，未验证教学效果。
- [Sa65477dc17e5] [原始 Show HN 讨论](https://news.ycombinator.com/item?id=49857528)：支持作者按日志估算每局约15美元API等价成本、未优化与局面解释局限；同帖旁观者及相邻实现体验并非本项目独立复现。
- [Sfea32cda253b] [Stockfish 官方介绍](https://stockfishchess.org/)：支持引擎、UCI、免费开源和GPLv3公开说明；不证明自然语言教学正确或本例的引擎版本。
- [Sa089efa83c5a] [Lichess 官方功能表](https://lichess.org/features)：支持当前免费分析棋盘、错误练习、研究及PGN导入导出，以及页面列出的每日服务器分析额度；不是本例历史额度或个性化视频功能。
- [Sb791f0d44020] [python-chess 官方引擎文档](https://python-chess.readthedocs.io/en/latest/engine.html)：实际阅读分析、Limit、MultiPV、root_moves、PovScore与mate相关条目，支持可限制候选走法和保留分数视角；不证明本例完成运行或深度等于棋力。
- [S58333316475e] [Claude 当前官方价格](https://claude.com/pricing)：支持Pro当前月付20美元、包含Claude Code且有用量限制；不是作者账单、每局固定价格或无限运行承诺。
- [S47b21d022697] [固定提交：chess-analysis 方法说明](https://github.com/brumar/chess-postmortem-skills/blob/eca0edfd55feba0b4bd87bbd4e93cf911b5ad5a7/skills/chess-analysis/SKILL.md)：支持受众等级、音频对齐、逐步扫描、引擎追问、一次安静局面分析、核验和笔记错位的已知缺陷；是作者要求，不等于每次执行通过。
- [S68a9ec9b8f5f] [固定提交：chess-video 方法说明](https://github.com/brumar/chess-postmortem-skills/blob/eca0edfd55feba0b4bd87bbd4e93cf911b5ad5a7/skills/chess-video/SKILL.md)：支持分镜、旁白、走子归属、字幕同步和人工抽帧复核要求；已知笔记错位不能被简化为理论风险。
- [Sc4e399d9bda2] [固定提交：sweep.py 静态代码](https://github.com/brumar/chess-postmortem-skills/blob/eca0edfd55feba0b4bd87bbd4e93cf911b5ad5a7/skills/chess-analysis/scripts/sweep.py)：支持默认深度22、30厘兵阈值、白方分数视角、逐步前后分析和JSON输出；没有执行此脚本或安装引擎。
- [Sceff1d5acd33] [固定提交：query.py 静态代码](https://github.com/brumar/chess-postmortem-skills/blob/eca0edfd55feba0b4bd87bbd4e93cf911b5ad5a7/skills/chess-analysis/scripts/query.py)：支持限定根走法、MultiPV查询和保存引擎线路到sidecar；它保存引擎证据，不能自动证明解说因果正确。
- [S59f1c523fe28] [固定提交：make_video.py 静态代码](https://github.com/brumar/chess-postmortem-skills/blob/eca0edfd55feba0b4bd87bbd4e93cf911b5ad5a7/skills/chess-video/scripts/make_video.py)：支持Piper或espeak旁白、按句生成字幕及ffmpeg组合本地视频的实现；未安装语音模型、调用模型服务或运行该代码。

结构化记录：[research/analyze-your-chess-games-into-commented-videos.json](../research/analyze-your-chess-games-into-commented-videos.json)
