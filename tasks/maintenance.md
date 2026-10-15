# 仓库维护说明

README 面向案例研究的读者，描述实际可读产物及研究方法。调度、运行状态和提交身份等维护信息放在任务文档，不写入读者介绍。

## 提交身份与认证核验

2026-10-15 本环境检查结果：

- 修改前，Git 的提交身份继承自 `/home/agent/.gitconfig` 中的全局配置，显示名称为“云先生”。提交身份配置不代表 GitHub 登录账号。
- 当前仓库 `.git/config` 已设置 `user.name=Tiee`、`user.email=tieetheai@gmail.com`，优先于上述全局配置。`git var GIT_AUTHOR_IDENT` 与 `git var GIT_COMMITTER_IDENT` 均确认有效身份为 `Tiee <tieetheai@gmail.com>`。
- `gh auth status` 显示当前环境可见的 GitHub 活跃账号为 `Tiee7`，来自已有环境认证；只显示一个账号。`gh api user` 返回 `login=Tiee7`、`name=Tiee`。未据此推断其他设备、浏览器或环境是否登录其他账号。
- 本次没有修改全局配置、历史提交、认证材料或授权范围。仓库本地 Git 配置不会随 clone 传播；后续新环境须复核有效身份，不能仅凭本文假定已经配置。

后续提交在本仓库继续使用上述身份，检查时只读取身份字段与认证状态，不输出、复制或提交密钥和令牌。新提交推送后，通过 GitHub commit API 核对 `commit.author`、`commit.committer` 的姓名和邮箱，并确认 `author.login`、`committer.login` 均映射为 `Tiee7`。若映射缺失，不把配置姓名相同称为已绑定账号。

## 内容与发布检查

1. 保持工作区原有修改，确认远端为 `Tiee7/agentusecases` 并同步 main。
2. 文档修改在独立分支完成；核对相对链接、真实案例计数和 README 中的产物描述。
3. 运行仓库测试与 `git diff --check`，审查差异后合并 main，不强推或重写历史。
4. 推送后重新读取远端文件，核对报告或文档、索引及结构化记录的一致性；提交身份映射也需实际检查。

案例研究的质量要求见[研究标准](../RESEARCH_STANDARD.md)，逐轮运行流程见[研究任务](hourly-business-research.md)。原始网页缓存与运行数据库不入 Git；公开报告、结构化记录、来源元数据及必要非敏感验证结果保留在仓库。
