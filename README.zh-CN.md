# ThinkAlong

**一起想清楚，少走弯路，把事情做好。**

[English](README.md) · [平台兼容指南](docs/platform-compatibility.md) · [使用示例](skills/think-along/references/examples.md) · [参与贡献](CONTRIBUTING.md)

![许可证：MIT](https://img.shields.io/badge/license-MIT-blue.svg)
![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-6f42c1.svg)
![CI 状态](https://github.com/koajsj/ThinkAlong/actions/workflows/validate.yml/badge.svg)

ThinkAlong 是一套可移植的 AI 协作 Skill，帮助普通人不必学习复杂的提示词技巧，也能更可靠地获得结果。它把模糊需求转化为可执行的**结果约定**，只追问真正重要的信息，在多轮任务中保留约束，并检查实际交付成果。

> **项目状态：实验性原型，v0.4.0。** 仓库包含结构验证和人工评测案例，但尚未完成全面的真实模型行为评测与跨平台安装验收。我们不宣称任务成功率已经获得实测提升。

## 问题不只是提示词

AI 可能误解目标、在多轮任务中忘记限制、让用户决定自己不懂的技术细节，或者没有检查结果就宣称完成。单纯改写提示词无法可靠避免这些问题。

ThinkAlong 采用五个具体机制：

1. **结果约定**：识别目标、交付物、硬性约束、验收标准、未知信息和风险。
2. **不确定性分级**：只有答案会实质改变结果或影响安全时才追问；其他情况优先采用合理、可逆的默认值。
3. **约束清单**：在多轮执行中持续保留排除项和要求，而不是只顾最新一句话。
4. **证据门槛**：根据验收标准检查真实成果，区分已验证、部分完成、未测试和受阻。
5. **修复闭环**：识别差异的根因，修复具体问题，再检查受影响的标准。

这是一套自适应流程，不是强制清单。简单任务仍然直接处理。

## 使用示例

**需求：**“我想做一份实习简历，但我什么都不懂。”

普通流程可能反复追问格式偏好，也可能为了填满简历而编造经历。

ThinkAlong 应当先复用用户提供的事实；只有岗位方向会实质改变简历时才追问；缺失信息使用占位符；宿主具备文件工具时直接生成实际文件；最后根据真实经历和指定格式检查成果。

更多[完整示例](skills/think-along/references/examples.md)。

## 安装

### Codex

将 `skills/think-along/` 复制到：

- 个人目录：`~/.agents/skills/think-along/`
- 项目目录：`.agents/skills/think-along/`

然后使用 `$think-along` 显式调用。参阅 [Codex Skills 文档](https://developers.openai.com/codex/skills)。

### Claude Code 与 Claude 网页端

Claude Code 可将技能目录放在 `~/.claude/skills/think-along/` 或项目的 `.claude/skills/think-along/`。Claude 网页端只有在账号开放自定义 Skills 时才能上传。参阅 [Claude Skills 文档](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)。

### ChatGPT 网页端

如果账号或工作区已经启用 Skills，可从 Skills 界面上传生成的 ZIP。可用性受套餐、工作区设置和产品开放范围影响。参阅 [ChatGPT Skills 文档](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)。

### DeepSeek 与其他模型

模型和宿主是两回事。通过支持 Skill 的宿主使用 DeepSeek 模型时，可以由宿主加载 Skill；不支持原生 Skill 的普通聊天网站，可使用[通用指令](adapters/portable-instructions.md)。粘贴指令不会自动赋予文件访问、工具、记忆或自动触发能力。

详见[平台兼容指南](docs/platform-compatibility.md)。遵循开放的 [Agent Skills 规范](https://agentskills.io/specification)，不代表所有 AI 产品都原生支持 Skill。

## 评测

项目将任务质量、触发准确性和评分标准分开维护：

- [任务质量案例](evals/task-cases.md)
- [触发准确性案例](evals/trigger-cases.md)
- [评分标准与基线对照方法](evals/scoring-rubric.md)

本地运行结构验证、验证器回归测试和打包：

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_skill.py
python -m unittest discover -s tests -v
python scripts/package_skill.py
```

这些检查只验证仓库文件与安装包结构，不会模拟大模型。要评估实际效果，应在相同模型、宿主、工具和上下文条件下，对比启用与未启用 ThinkAlong 的结果，并记录失败案例。

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

欢迎提交可复现的误触发、漏触发、约束遗漏、无效追问、验证不足和平台安装问题。请提供输入、预期行为、实际行为、宿主/模型和回归案例。不要在公开 Issue 中发布私人数据。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

如果 ThinkAlong 确实解决了你的问题，欢迎给仓库点 Star，并分享具体案例。成功与失败都能帮助改进。

## 许可证

MIT，详见 [LICENSE](LICENSE)。
