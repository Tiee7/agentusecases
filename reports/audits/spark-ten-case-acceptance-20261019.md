# Spark 十案复核、修正与导入验收

研究日期：2026-10-19。检查和修改在助手自己的原生云端工作区完成，未使用用户的 Codex 云环境、保存的 agentusecases 编码环境或用户电脑。GitHub 现有 CI 仅用于发布回归验证。

## 结果与范围

本批十案经逐案重核和修正，按 **10 份简报、0 份新增完整深研** 导入。独立只读终审未发现新的实质内容阻塞。全部两轨总分保持 null；没有用缺证零分、搜索摘要、作者成功样本或源站试用模板补造完整深研。

当前基线目录 **1,427 案**；完整深研 **47 篇**；简报由 **28 增至 38 篇**；完整中文译文由 **53 增至 63 份**。README 原来的 1,381 案已过时，本次按当前登记表更正，未覆盖每日爬虫新增目录。

输入为 FINAL_COMPLETE_CASES_PACKAGE.zip，628,710 字节，SHA-256：62242bb6feda5e777772b68236c1e962bfdf8b37991a860eca9e1f58a8458401。本轮重新列出批次及 results 目录，results 共 59 项，未发现晚于该 09:50 上传总包的新返修；包哈希与保存的原始输入一致。开始时 main 为 676e4af56a7f5ba4fdb74be31ea984265c956f61。

## 实际修正

下表的贡献均是给定假设的已列项算式，未扣未知费用；现金也只是已列项，不是实际完整账单。

| 案例 | 关键修正 | 四周现金 / USD | 月贡献 / USD |
|---|---|---:|---:|
| [Make 入职](../brief/automate-customer-onboarding-with-a-make-scenario.md) | 删无据 AWS 地域/2FA、历史损坏原数与回本期限；年费预付和未知现金分开 | 116 条件成立；644 已超预算 | 109 / 888 |
| [n8n 求职](../brief/automate-daily-job-applications-with-tailored-cvs-and-cover-.md) | 只保留归档可支持的方法；不造模型版本、评论或录用效果，保留人工投递 | 335 / 290，均超预算 | −260 / −90 |
| [航班交接](../brief/book-a-munich-to-london-flight-didn-t-finish.md) | 方法止于返回链接，不写已完成购买；不由一次受阻外推全行业不可出票 | 92 / 104，均条件成立 | 13 / −4 |
| [运营看板](../brief/build-and-maintain-a-local-ops-dashboard-with-agents.md) | 恢复归档步骤；改混合架构，分清商用许可、每席与支付周期，删完全本地/净回本保证 | 150 / 95，均条件成立 | 150 / −5 |
| [资助清单](../brief/collect-international-grant-listings-into-airtable.md) | 区分独立 Agents activities、迁后 tasks 与年费；选有限 Free 验证及明确月付预算假设 | 120 / 120，均条件成立 | 130 / 30 |
| [Cloudflare 发布](../brief/deploy-agent-built-static-pages-to-your-own-cloudflare-domai.md) | 区分静态资源、Worker、KV 与缓存计费；删私有/免维护/SLA保证，年约销量与全年履约分开 | 130 / 114，均条件成立 | 320 / 171 |
| [个人 CRM](../brief/enrich-and-store-contacts-in-a-personal-crm.md) | 重新核当前产品；标记候选不升级为自动建档，供应商价格未知，不从职业推采购特权 | 130 / 75，均条件成立 | 220 / 22.5 |
| [线索富集](../brief/enrich-new-crm-leads-for-personalized-outreach.md) | 泛 API 目录不背书具体单价；身份歧义待人工，置信度不能绕过写入/发送确认 | 126 / 72，均条件成立 | 184 / 33 |
| [发票提取](../brief/extract-supplier-invoice-pdfs-into-a-monday-com-board.md) | 具体发票模块按 operation 10 credits；未知税额为 null，绿勾不等于准确，金额等式有适用条件 | 112 / 60，均条件成立 | 208 / 30 |
| [球馆预约](../brief/handle-padel-club-bookings-through-a-conversational-ai-agent.md) | 实读作者帖；150 成功对话没有总分母；补创建/修改/取消明确确认与身份核对，拆流程不等于原子防重 | 130 / 66，均条件成立 | 260 / 54 |

“条件成立”统一指：已列现金加全部遗漏现金不超过 USD 200。每案列出了具体余量、付款归属、未核许可/税费/超额及预付条件。未知 other_variable_cost 保留 null，未当作已证零成本；Cloudflare 第二情景的 12 美元域名预算仍是明确情景值。自用均按固定普通知识工作者画像，不借专业用户高频抬分。

## 来源与过程边界

- 重读十份已授权英文归档，逐句检查完整译文。原英文、来源字段和原有元数据不变，只新增独立 translation 字段；没有把损坏摘录补造为伪原文。
- 重新实读所需官方计量、定价或产品页面。只保存带归属的短摘要、其字符数/哈希和读取结果哈希；外链全文、HTML、运行数据库、秘密与私人通信不入 Git。
- 本轮公开页面的真实读取区间为 13:18–13:30 UTC。精确逐次秒值未保留，凭据明确将 fetched_at 标为区间上界，另列整理时间，不倒填历史精确时间。离线归档读取与旧站点观测时间分列。
- 第 1–9 案没有直接重读原始外链，author_method 保持 unavailable；已知步骤独立列为 reported_method/归档转述。第 10 案直接读取作者帖，author_summary 与对应来源凭据匹配。未将评论建议当独立项目效果验证。
- 新凭据替换了损坏来源字符串；未认证旧包“PASSED”或从合成 shell 实验推断历史实际命令、原金额。旧输入完整保留，旧审查时序冲突不被倒写修复。
- 未运行十个业务工作流、压力测试、真实招聘投递、预约、发票上传、付费 API、账户连接或外部沟通；没有恢复已暂停的旧研究调度。

## 导入映射与可复核文件

- 权威简报：[research/brief](../../research/brief/INDEX.md) 与 reports/brief，分别统计，不生成 completed v2 深研记录
- 独立双轨评分：research/scoring-v1，与旧七维分数分开，规则见[评分说明](../../research/scoring-v1/README.md)
- 完整译文：translations；阅读站通过各案原档的独立 translation 读取
- 来源凭据：research/evidence；每案保留范围、假设与未知项
- [批次清单与原始哈希](../../research/runs/spark-ten-case-repair-20261019/manifest.json)、[逐案修正记录](../../research/runs/spark-ten-case-repair-20261019/cases/)、[可重复只读校验器](../../research/runs/spark-ten-case-repair-20261019/verify.py)、[本轮数据校验结果](../../research/runs/spark-ten-case-repair-20261019/validation.json)

不复制 Spark 包里的共享索引、registry、代码、旧工作草稿或 pre-import pending 状态。本侧基于当前 main 重建简报索引与覆盖计数。registry/cases.json、当前目录观察和日常爬虫元数据不变。

## 验证与交付

本地已通过：十案原文/译文绑定、来源引用、author_method/personal_use、报告投影、评分空值规则、二十种情景贡献及现金重算；92 项 Python 单元测试；16 项网站内容测试；Astro 构建 2,905 页；输出检查 2,907 个文件，验证 1,427 份原文、63 份完整译文、47 篇深研及全部源站模板。

本地浏览器安全与端到端测试未通过启动阶段：浏览器下载返回不完整内容；已有 Chromium 在本原生沙箱内因进程 socket 权限拒绝退出，标准提权也遇环境内部只读目录错误。因此这些断言没有被冒称本地通过。独立分支内容提交 [695eebc](https://github.com/Tiee7/agentusecases/commit/695eebc17c9596fda840338d1f5dcd8543bd9c94) 的既有 [GitHub Reading site checks](https://github.com/Tiee7/agentusecases/actions/runs/39263173413) 已于 13:51 UTC 全部成功：92 项 Python 测试、16 项内容测试、构建与输出检查、桌面/手机真实 Chromium 提示词安全检查、69 项桌面/平板/手机端到端测试。此结果为 GitHub 发布验证，不能解释为本地浏览器启动成功，也不是十个业务工作流的实测。

提交继续使用已有 Tiee7 认证，author 与 committer 均为 Tiee <tieetheai@gmail.com>。已先用未挂引用、同 tree 的 commit 验证连接器身份；无新增凭据、强推、改历史或绕过保护。发布前复核远端 main，再以 expected-old、force=false 更新引用，最后回读报告、索引、记录与真实计数。

发布凭据见 [publication.json](../../research/runs/spark-ten-case-repair-20261019/publication.json)。13:49 UTC 再次列出 results，仍为 59 项，最新仍是同一 09:50 总包。交付凭据补充后，最终分支仍须通过相同 CI 才合并；最终 SHA、合并与检查状态以 [PR 2](https://github.com/Tiee7/agentusecases/pull/2) 和 main 的远端记录为准。
