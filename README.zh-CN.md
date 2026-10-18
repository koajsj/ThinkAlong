# ThinkAlong

**自然讨论，准备好就实施，核验实际成果。**

[English](README.md) · [平台兼容指南](docs/platform-compatibility.md) · [使用示例](skills/think-along/references/examples.md) · [参与贡献](CONTRIBUTING.md)

![许可证：MIT](https://img.shields.io/badge/license-MIT-blue.svg)
![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-6f42c1.svg)
![CI 状态](https://github.com/koajsj/ThinkAlong/actions/workflows/validate.yml/badge.svg)

ThinkAlong 是一套可移植的 AI 协作 Skill，帮助普通人不必学习复杂的提示词技巧，也能更可靠地获得结果。它尤其希望解决 **ChatGPT 规划 → 生成提示词 → 复制给 Codex → 再解释一遍** 的重复流程：让讨论、已确认决定和实施保持衔接；当用户要求执行且工具可用时，直接处理实际项目。

> **项目状态：实验性原型，元数据版本 v0.4.0，包含尚未正式发布的指令改动。** 本次仅做静态验证与打包；自然语言加载、真实模型行为和跨平台安装均未运行验收，不宣称成功率已经获得实测提升。

## 你不应该一直充当两个 AI 之间的信息搬运工

常见流程是：先在 ChatGPT 中讨论项目，让它生成一大段提示词，再复制给 Codex。执行时一旦有遗漏，就得重新解释需求、补充约束，规划与实现也容易脱节。

ThinkAlong 希望减少这次中转：

1. **按需讨论**：帮助明确问题、受众和方案，持续对齐目标、约束、决定和验收标准。
2. **采用合理默认值**：只询问会实质改变结果的选择，不让零基础用户承担不必要的技术决策。
3. **在当前工作区直接做**：检查现有项目，进行必要规划，并在工具允许时实际实现。
4. **持续保留约束**：避免执行到一半遗忘要求或擅自扩大范围。
5. **检查并修复**：核对实际成果、修复具体问题，并如实说明哪些已验证、哪些尚未测试。

这是一套自适应流程，不是强制清单。简单任务仍然直接处理。

## 从讨论自然进入实施

在支持 Skill 的宿主安装后，打开项目工作区，直接使用普通语言，无需记住专门口令：

```text
我想做一个个人网站。我们先讨论一下应该放什么。
把刚才讨论的方案实现出来。
继续完成之前的项目。
```

这些是使用说明，不是已测得的触发结果。第一句保持讨论；下一句复用已确认需求，在可访问的工作区实施；继续项目时先检查真实文件和进度。直接要求增加功能、完善或修复项目时，也应推进实际工作，不因可采用默认值的技术细节重复确认。普通问答、翻译、局部文本修改和基础代码解释仍然直接处理。

仅要求审查时保持只读；宽泛优化聚焦现有用户流程中有依据的缺口。中途追问保留原任务目标，明确停止时及时遵守。修复应根据新证据推进，避免无效重试；完成声明须对应当前成果与允许的检查。外部操作结果不明时，先核对实际状态，避免重试造成重复执行。

宿主决定发现、加载和工具权限，模型决定如何遵循指令。description 为自然语言匹配提供依据，`policy.allow_implicit_invocation: true` 明确允许 Codex 隐式调用（这本来就是宿主默认值），但不会强制加载。`$think-along` 保留为可选的显式调用方式，不是开发项目的必要步骤。参阅[官方 Skill 文档](https://learn.chatgpt.com/docs/build-skills)。

如果要求边讨论边实现，可推进已授权且不依赖待定选择的工作，同时讨论关键决策。仅在用户要求提示词、要求交给其他工具，或实施缺少必要能力时，才以交接为主要交付物；交接是一份包含目标、已确认需求、约束、决定/默认值、待确认事项、验收标准和实际进度的精简说明。Skill 不会自动转移聊天、赋予工具、永久保存上下文或授权发布部署。

## 它与普通提示词优化有什么区别？

- **从项目想法到实际交付：** 在编程环境中直接做项目，而不是把提示词交给用户中转。
- **结果约定：** 持续对齐目标、交付物、硬性约束、假设和验收标准。
- **低摩擦澄清：** 只问真正重要的问题；相关问题可以合并，有依赖的问题按顺序处理。
- **跨轮次约束管理：** 防止多步骤执行中悄悄丢掉要求。
- **证据与修复闭环：** 检查实际结果、修复根因，不虚报未执行的检查。
- **按宿主能力适配：** 优先使用原生 Agent Skills；不支持时提供通用指令，不宣称所有平台能力相同。

## 安装

### Codex

将 `skills/think-along/` 复制到以下位置，并把仓库根目录 `LICENSE` 放入安装后的 `think-along/`。生成的 ZIP 已包含许可证；升级前先检查目标目录并保留本地修改：

- 个人目录：`~/.agents/skills/think-along/`
- 项目目录：`.agents/skills/think-along/`

直接描述项目即可；需要时可用 `$think-along` 显式调用。加载仍取决于宿主发现、配置和匹配。参阅 [Codex Skills 文档](https://learn.chatgpt.com/docs/build-skills)。

### Claude Code 与 Claude 网页端

Claude Code 可将含 `LICENSE` 的技能目录安装到 `~/.claude/skills/think-along/` 或项目的 `.claude/skills/think-along/`。Claude Code 可按描述选择 Skill，也可用 `/think-along` 显式调用。Claude 网页端上传 ZIP 需要启用自定义 Skills 和代码执行能力，并不因此获得本地仓库权限。参阅 [Claude Code Skills](https://code.claude.com/docs/en/skills) 和 [Claude 自定义 Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)。

### ChatGPT 网页端

使用账号或工作区实际开放的 Skill 安装/上传入口；自定义 Skills 不可用时使用通用指令。文件、执行和仓库访问能力取决于当前工具与权限。无工具时仍可继续讨论，只有要求实施且确有必要时才交接。参阅 [ChatGPT Skills](https://learn.chatgpt.com/docs/skills-and-plugins) 和 [ChatGPT 能力说明](https://learn.chatgpt.com/docs/use-chatgpt)。

### DeepSeek 与其他模型

模型和宿主是两回事。通过支持 Skill 的宿主使用 DeepSeek 模型时，可以由宿主加载 Skill；不支持原生 Skill 的普通聊天网站，可使用[通用指令](adapters/portable-instructions.md)。粘贴指令不会自动赋予文件访问、工具、记忆或自动触发能力。

详见[平台兼容指南](docs/platform-compatibility.md)。遵循开放的 [Agent Skills 规范](https://agentskills.io/specification)，不代表所有 AI 产品都原生支持 Skill。

## 静态审查与评测规范

当前仅做静态审查，不保留测试代码或任务/触发/回归案例，不运行单元、运行时、行为或模型测试。保留以下方法文档供日后另行授权时参考：

- [七项独立指标与评分标准](evals/scoring-rubric.md)
- [静态审查与评测协议](evals/protocol.md)
- [六个参考项目的研究依据与设计取舍](docs/research-summary.md)
- [本次审查结果及限制](docs/audit-summary.md)

本地检查元数据、文件引用和打包结构：

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_skill.py
python scripts/package_skill.py
```

这些是开发工具，不是 Skill 的运行时依赖。命令不会执行 Skill、模拟大模型或证明实际行为效果。真实模型评测仍未运行，付费 API 调用还需单独授权。

验证器同时解析 Python 源码和 CI 定义：必要步骤必须无附加条件且不能忽略失败，必要检查命令必须独立执行。这是本仓库的保守结构约定，不解析任意 GitHub 表达式或 Shell 程序，也不证明远程已执行。打包采用共享的六文件白名单、固定 ZIP 时间戳/权限和可移植路径，核对暂存归档后才替换原 ZIP。生成文件留在被忽略的 `dist/`，不提交到 Git。

## 参与贡献

欢迎提交 ThinkAlong 仍然要求用户中转提示词、遗漏约束、无效追问、没有实际实现或虚报验收的可复现案例。请提供输入、预期行为、实际行为、宿主/模型和证据。不要在公开 Issue 中发布私人数据。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

如果 ThinkAlong 确实解决了你的问题，欢迎给仓库点 Star，并分享具体案例。成功与失败都能帮助改进。

## 许可证

MIT，详见 [LICENSE](LICENSE)。
