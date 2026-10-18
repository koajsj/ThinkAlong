# ThinkAlong 研究依据与设计决策

调研日期：2026-10-18。下列提交来自本次只读获取的各仓库默认分支 HEAD；链接固定提交，便于复查。调研范围为 README、列出的实现/规范及相应许可证，并非六个仓库的全面审计。未执行第三方项目、模型调用或其测试。

## 参考机制与适用边界

| 项目与本次提交 | 实际依据 | 可复用机制 | ThinkAlong 决策与边界 |
| --- | --- | --- | --- |
| claude-quickstarts · `9ec32b9` | [README](https://github.com/anthropics/claude-quickstarts/blob/9ec32b91df50b0d4906cae64b13c6298055ff40d/README.md)、[autonomous-coding/README](https://github.com/anthropics/claude-quickstarts/blob/9ec32b91df50b0d4906cae64b13c6298055ff40d/autonomous-coding/README.md)、[coding_prompt](https://github.com/anthropics/claude-quickstarts/blob/9ec32b91df50b0d4906cae64b13c6298055ff40d/autonomous-coding/prompts/coding_prompt.md) | 将需求拆成可检查的功能，后续会话读取真实进度，验证后再标记完成。 | 已有结果契约、约束清单和证据门槛足以承接思想；评分标准要求区分当前证据与旧进度。两智能体、浏览器操作、固定功能数量和持续运行服务不适合通用协作 Skill，不引入。 |
| anthropics/skills · `dbd4588` | [README](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/README.md)、[run_eval.py](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/scripts/run_eval.py)、[aggregate_benchmark.py](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/scripts/aggregate_benchmark.py) | 任务输出评估与 description 触发评估分开；重复运行、保留原始证据和汇总差异。 | 为触发记录宿主加载证据，单列误触发/漏触发；保留现有按需 references。其 Claude 专用命令探测方式不能证明其他宿主的加载行为，不复制评测运行器。 |
| obra/superpowers · `bb92a77` | [README](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/README.md)、[verification-before-completion](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/verification-before-completion/SKILL.md) | 完成声明需要相应检查的实际输出；修复应有回归证据。 | 保留已有证据门槛和根因修复；将未经核验声明、修复质量独立计量。固定全流程、强制子智能体、对小任务增加仪式均不采用。 |
| huggingface/upskill · `eec8ab4` | [README](https://github.com/huggingface/upskill/blob/eec8ab46f970a880e4d21cfd41dff50ac08c6847/README.md)、[evaluate.py](https://github.com/huggingface/upskill/blob/eec8ab46f970a880e4d21cfd41dff50ac08c6847/src/upskill/evaluate.py) | 同一任务分别运行 baseline/with-skill，保存单例输出、验证结果和资源统计。 | 固定环境与输入、隔离两组上下文，报告成对差异、失败与样本量；工具故障和缺失记录不记作成功。该项目的执行后端、模型配置、依赖和自动优化服务不引入。 |
| agentskills/agentskills · `69ef37e` | [README](https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/README.md)、[specification](https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/docs/specification.mdx)、[validator.py](https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/skills-ref/src/skills_ref/validator.py) | 标准前置元数据、目录同名、渐进加载、相对文件引用；规范与参考验证器是两个证据层。 | 本地验证补齐 compatibility 长度、字符串 metadata、allowed-tools 字符串；检查运行包内引用。未安装或运行 skills-ref，不宣称获得官方认证。500 行是本仓库采用的预算，并非所有宿主的硬限制。 |
| openai/plugins · `0722921` | [README](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/README.md)、[build-ios-apps manifest](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/build-ios-apps/.codex-plugin/plugin.json)、[figma manifest](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/figma/.codex-plugin/plugin.json)、[figma MCP 配置](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/figma/.mcp.json) | 插件清单、Skill 指令与连接器配置分层，元数据声明并不等于工具已连接。 | 保持 ThinkAlong 为独立 Skill；ZIP 不添加插件清单、OAuth、MCP 或权限。方法上区分工具可用性与任务完成程度，不把插件与 Skill 安装兼容性混为一谈。 |

## 许可证核对

- claude-quickstarts：[根 LICENSE 为 MIT](https://github.com/anthropics/claude-quickstarts/blob/9ec32b91df50b0d4906cae64b13c6298055ff40d/LICENSE)。superpowers：[MIT](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/LICENSE)。
- anthropics/skills 按目录授权：[skill-creator 为 Apache-2.0](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/LICENSE.txt)；[docx 的条款不同](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/docx/LICENSE.txt)。不能把整库视为同一开放许可证。
- upskill：[Apache-2.0](https://github.com/huggingface/upskill/blob/eec8ab46f970a880e4d21cfd41dff50ac08c6847/LICENSE)。agentskills：[代码 Apache-2.0](https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/LICENSE)，[文档 CC-BY-4.0](https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/docs/LICENSE)。
- openai/plugins 本次 HEAD 根目录没有统一 LICENSE；build-ios-apps 清单声明 MIT，而 [Figma LICENSE](https://github.com/openai/plugins/blob/0722921d5542fc593105c27bd52630babd8b8c2a/plugins/figma/LICENSE.txt) 对应开发者条款。清单声明不能替代完整授权核对，不推断整库可重许可。

本次只以独立表述总结机制，没有引入第三方实现、素材或大段文本。ThinkAlong 继续使用自己的 MIT 许可证；目录安装也应携带它。未来如复制具体文件，应先逐文件核对授权及通知要求。

## 从现状到改动

已有能力：结果契约、按信息影响决定追问、跨轮约束管理、按交付物选择检查、根因修复和安全信任边界。首轮调研保留核心 Skill；后续经用户授权，针对静态易用性审查发现的缺口，收窄触发描述、允许合并少量必要问题、去除重复工作流规则，并补充以用户参考、受众和用途判断主观质量。保留现有架构，不新增依赖。原有任务/触发案例和首轮暂增的回归案例已按用户要求全部删除；保留评分标准与协议，后续仅做静态审查。

实际缺口与处理：

1. 原评分将约束、安全和核验混合，总分不足以诊断失败。保留历史五维分数，新增独立事件指标、修复评分和不可被总分抵消的失败门槛。
2. 原案例多为场景摘要；条件触发的上下文与观测方法未固定。将冻结输入、加载证据、隔离基线和计量分母要求保留在方法协议中，不保留案例、不执行评测。
3. 验证器会漏检部分元数据、重复 YAML 键、运行包外引用及符号链接。收紧静态检查；移除已删除案例及单元测试的存在性要求和 CI 入口。
4. 文件夹安装说明遗漏仓库 LICENSE。修订双语安装与发布说明；研究、评测和工具仍在运行包外。

执行结果与限制见 [audit-summary.md](audit-summary.md)，方法见 [评测协议](../evals/protocol.md)。这些设计决策是调研判断，不是模型效果证据。

## 本轮深化：降低误操作、无效修复和虚假完成

2026-10-18 再次读取 anthropics/skills、obra/superpowers、agentskills/agentskills 默认分支 HEAD；提交仍分别为上表的 `dbd4588`、`bb92a77`、`69ef37e`。本轮补读了以下具体材料，许可证依据仍为上文对应目录条款。仅提炼机制并独立表述，没有运行其工具或复制实现。

| 来源 | 可复用思想 | ThinkAlong 的具体取舍 |
| --- | --- | --- |
| [Anthropic skill-creator](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/SKILL.md)、[grader](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/skills/skill-creator/agents/grader.md) | 关注真实成果而非表面满足；检查评分条件本身是否有区分力；保持规则简洁，避免为少数输入堆积特例。 | 在现有证据门槛中要求检查能识别实质错误，不能仅凭文件存在或自报成功；不能削弱原标准来制造通过。仅把必要决策规则加入主 Skill，详细诊断留在原 references；不采用其子智能体或评测运行流程。 |
| [Superpowers systematic-debugging](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/systematic-debugging/SKILL.md)、上表 verification-before-completion | 从症状定位原因，用新证据修正判断；重复失败时重新检查假设；完成声明依赖实际检查结果。 | 增补“重复尝试不产生新信息时改变调查或明确阻碍”，避免盲目叠加补丁。不照搬固定次数阈值、强制测试/审批或架构重构；检查方式仍受当前任务权限限制。证据须对应当前成果、完成状态和相关范围。 |
| [Agent Skills 规范](https://agentskills.io/specification) | 元数据发现、主体加载与资源按需读取分层。 | 保持独立 Skill 与原三份 references；主文件只补跨任务共用的边界，不能把优化请求扩张成无关功能清单或全能专业工具。规范符合性不等于实际模型遵循或宿主安全保证。 |

静态工具另依据 [GitHub Actions workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) 核对条件跳过和 `continue-on-error` 语义。原验证器只查步骤含有命令，未检查 job 条件、失败容忍，并把多行 Shell 中出现的命令视为执行依据。本轮采用保守的本仓库约定：必要 job/步骤无附加条件、不忽略失败，必要检查为独立完整命令。不实现表达式或 Shell 解释器，不把结构验证描述为远程执行证明。

只读审查、讨论不授权写入、中途追问保留主任务、宽泛优化按用户影响收敛、外部操作结果不明先查状态等改动，来自对 ThinkAlong 现有规则的静态缺口分析。它们是本项目的设计判断，尚无行为复现或模型增益测量，不将潜在风险写成已发生事故。
