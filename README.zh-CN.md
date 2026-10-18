# ThinkAlong

**想法直接落地，少做提示词搬运工。**

[English](README.md) · [平台兼容指南](docs/platform-compatibility.md) · [使用示例](skills/think-along/references/examples.md) · [参与贡献](CONTRIBUTING.md)

![许可证：MIT](https://img.shields.io/badge/license-MIT-blue.svg)
![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-6f42c1.svg)
![CI 状态](https://github.com/koajsj/ThinkAlong/actions/workflows/validate.yml/badge.svg)

ThinkAlong 是一套可移植的 AI 协作 Skill，帮助普通人不必学习复杂的提示词技巧，也能更可靠地获得结果。它尤其希望解决 **ChatGPT 规划 → 生成提示词 → 复制给 Codex → 再解释一遍** 的重复流程：在具备项目访问能力的编程环境中，让 AI 直接从项目想法走向实现和验收。

> **项目状态：实验性原型，元数据版本 v0.4.0，包含尚未正式发布的指令改动。** 当前可进行静态验证和打包，但尚未全面测试真实模型行为或各平台安装效果，不宣称成功率已经获得实测提升。

## 你不应该一直充当两个 AI 之间的信息搬运工

常见流程是：先在 ChatGPT 中讨论项目，让它生成一大段提示词，再复制给 Codex。执行时一旦有遗漏，就得重新解释需求、补充约束，规划与实现也容易脱节。

ThinkAlong 希望减少这次中转：

1. **理解目标**：识别真正想实现的结果、交付物、硬性约束、假设和验收标准。
2. **采用合理默认值**：只询问会实质改变结果的选择，不让零基础用户承担不必要的技术决策。
3. **在当前工作区直接做**：检查现有项目，进行必要规划，并在工具允许时实际实现。
4. **持续保留约束**：避免执行到一半遗忘要求或擅自扩大范围。
5. **检查并修复**：核对实际成果、修复具体问题，并如实说明哪些已验证、哪些尚未测试。

这是一套自适应流程，不是强制清单。简单任务仍然直接处理。

## 在 Codex 中直接开始项目

安装 Skill 后，打开项目工作区，直接用自然语言描述你的想法：

```text
$think-along 我想做一个实用的个人网站，但我不懂技术。请检查当前工作区，选择合理的默认方案；只有会实质影响结果的选择才询问我。在当前工作区直接实现一个可用版本并验证，不要只给我一段交给另一个 AI 的提示词。
```

ThinkAlong 应先检查现有项目，再决定技术方案。如果目录已有代码，就保留有效功能并遵循项目指引；如果是空目录，则采用易维护的默认方案并开始实现。发布、部署等外部操作仍须遵循必要的授权流程。

**注意：** Skill 无法凭空赋予宿主不存在的工具或项目访问权限。如果当前只是无法执行代码的聊天界面，它应改为提供一份简洁完整的交接说明，并明确说明尚未实际执行代码。

## 它与普通提示词优化有什么区别？

- **从项目想法到实际交付：** 在编程环境中直接做项目，而不是把提示词交给用户中转。
- **结果约定：** 持续对齐目标、交付物、硬性约束、假设和验收标准。
- **低摩擦澄清：** 只问真正重要的问题；相关问题可以合并，有依赖的问题按顺序处理。
- **跨轮次约束管理：** 防止多步骤执行中悄悄丢掉要求。
- **证据与修复闭环：** 检查实际结果、修复根因，不虚报未执行的检查。
- **按宿主能力适配：** 优先使用原生 Agent Skills；不支持时提供通用指令，不宣称所有平台能力相同。

## 安装

### Codex

将 `skills/think-along/` 复制到：

- 个人目录：`~/.agents/skills/think-along/`
- 项目目录：`.agents/skills/think-along/`

然后使用 `$think-along` 显式调用。参阅 [Codex Skills 文档](https://developers.openai.com/codex/skills)。

### Claude Code 与 Claude 网页端

Claude Code 可将技能目录安装到 `~/.claude/skills/think-along/` 或项目的 `.claude/skills/think-along/`。Claude 网页端只有在账号开放自定义 Skills 时才能上传。参阅 [Claude Skills 文档](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)。

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

这些是开发工具，不是 Skill 的运行时依赖。命令不会执行 Skill、模拟大模型或证明实际行为效果。真实模型评测仍未运行，付费 API 调用还需单独授权。

## 参与贡献

欢迎提交 ThinkAlong 仍然要求用户中转提示词、遗漏约束、无效追问、没有实际实现或虚报验收的可复现案例。请提供输入、预期行为、实际行为、宿主/模型和证据。不要在公开 Issue 中发布私人数据。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

如果 ThinkAlong 确实解决了你的问题，欢迎给仓库点 Star，并分享具体案例。成功与失败都能帮助改进。

## 许可证

MIT，详见 [LICENSE](LICENSE)。
