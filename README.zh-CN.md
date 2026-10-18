# ThinkAlong

**一起想清楚，少走弯路，把事情做好。**

[English](README.md) · [平台兼容指南](docs/platform-compatibility.md) · [使用示例](skills/think-along/references/examples.md) · [参与贡献](CONTRIBUTING.md)

![许可证：MIT](https://img.shields.io/badge/license-MIT-blue.svg)
![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-6f42c1.svg)
![CI 状态](https://github.com/koajsj/ThinkAlong/actions/workflows/validate.yml/badge.svg)

ThinkAlong 是一套可移植的 AI 协作 Skill，帮助普通人不必学习复杂的提示词技巧，也能更可靠地获得结果。它把模糊需求转化为可执行的**结果约定**，只追问真正重要的信息，在多轮任务中保留约束，并检查实际交付成果。

> **项目状态：实验性原型，元数据版本 v0.4.0，包含 Unreleased 指令改动。** 当前仅做静态审查，已删除测试代码与评测案例，保留评分标准和评测协议。真实模型行为评测与跨平台安装验收未运行。我们不宣称任务成功率已经获得实测提升。

## 问题不只是提示词

AI 可能误解目标、在多轮任务中忘记限制、让用户决定自己不懂的技术细节，或者没有检查结果就宣称完成。单纯改写提示词无法可靠避免这些问题。

ThinkAlong 采用五个具体机制：

1. **结果约定**：识别目标、交付物、硬性约束、验收标准、未知信息和风险。
2. **不确定性分级**：只有答案会实质改变结果或影响安全时才追问；其他情况优先采用合理、可逆的默认值。
3. **约束清单**：在多轮执行中持续保留排除项和要求，而不是只顾最新一句话。
4. **证据门槛**：根据验收标准检查真实成果，区分已验证、部分完成、未测试和受阻。
5. **修复闭环**：识别差异的根因，修复具体问题，再检查受影响的标准。

这是一套自适应流程，不是强制清单。简单任务仍然直接处理。

当歧义会改变结果、多步骤或多轮约束相互影响、已有成果需要修复时，适合使用 ThinkAlong。研究、文件/数据工作或步骤较多本身不是加载理由；日常问答和明确的转换任务直接处理，显式调用后也不增加流程。少量必要、相关的问题可以合并；主观质量按用户参考、受众和用途判断。这些是指令改进，尚无行为效果实测结论。

## 使用示例

**需求：**“我想做一份实习简历，但我什么都不懂。”

普通流程可能反复追问格式偏好，也可能为了填满简历而编造经历。

ThinkAlong 应当先复用用户提供的事实；只有岗位方向会实质改变简历时才追问；缺失信息使用占位符；宿主具备文件工具时直接生成实际文件；最后根据真实经历和指定格式检查成果。

更多[完整示例](skills/think-along/references/examples.md)。

## 安装

### Codex

将 `skills/think-along/` 复制到以下位置，并将仓库根目录的 `LICENSE` 复制到安装后的 `think-along/` 目录。生成的 ZIP 已包含许可证；升级前先检查目标目录，保留本地修改。

- 个人目录：`~/.agents/skills/think-along/`
- 项目目录：`.agents/skills/think-along/`

然后使用 `$think-along` 显式调用。参阅 [Codex Skills 文档](https://developers.openai.com/codex/skills)。

### Claude Code 与 Claude 网页端

Claude Code 可按上述方式连同 `LICENSE` 安装技能目录到 `~/.claude/skills/think-along/` 或项目的 `.claude/skills/think-along/`。Claude 网页端只有在账号开放自定义 Skills 时才能上传。参阅 [Claude Skills 文档](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)。

### ChatGPT 网页端

如果账号或工作区已经启用 Skills，可从 Skills 界面上传生成的 ZIP。可用性受套餐、工作区设置和产品开放范围影响。参阅 [ChatGPT Skills 文档](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)。

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

这只需要开发工具依赖，不增加 Skill 运行时依赖。应使用已安装 `requirements-dev.txt` 的同一 Python 环境。这些命令不会执行 Skill、模拟大模型或证明安装及行为效果。真实模型评测仍未运行，也不自动授权付费 API。

验证器同时解析 Python 源码和 CI 的有效步骤定义。打包共用六文件清单，固定 ZIP 时间戳和权限，统一使用 `/` 路径；临时包校验完成后才原子替换旧 ZIP。产物保存在已忽略的 `dist/`，不提交到仓库。不同 Python 或压缩库版本之间不保证产物字节完全一致。

## 设计原则

- 关注结果，而不是只润色提示词。
- 先利用上下文，再决定是否追问。
- 可逆选择采用合理默认值，重要不确定性才澄清。
- 能执行时优先完成实际工作，而不只给建议。
- 多轮任务始终保留硬性约束。
- 有证据后才宣称完成。
- 修复根因，而不只是换一种说法。
- 追求跨平台可移植性，但不假装不同宿主的能力完全相同。

## 参与贡献

欢迎提交可复现的误触发、漏触发、约束遗漏、无效追问、验证不足和平台安装问题。请提供输入、预期行为、实际行为、宿主/模型和静态证据。不要在公开 Issue 中发布私人数据。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

如果 ThinkAlong 确实解决了你的问题，欢迎给仓库点 Star，并分享具体案例。成功与失败都能帮助改进。

## 许可证

MIT，详见 [LICENSE](LICENSE)。
