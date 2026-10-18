# ThinkAlong

**一起想清楚，少走弯路，把事情做好。**

[English](README.md) · [平台兼容指南](docs/platform-compatibility.md) · [参与贡献](CONTRIBUTING.md) · [审计汇总](docs/audit-summary.md)

![许可证：MIT](https://img.shields.io/badge/license-MIT-blue.svg)
![格式：Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-6f42c1.svg)
![CI 状态](https://github.com/koajsj/ThinkAlong/actions/workflows/validate.yml/badge.svg)

ThinkAlong 是一套轻量、可移植的 AI 协作流程，帮助普通人不必学习复杂的提示词技巧，也能更高效地获得有用结果。它引导 AI 理解目标、只询问关键问题、在能力允许时完成实际工作，并检查最终成果。

> **项目状态：实验性原型，v0.3.0。** 仓库包含可重复的测试案例和验证工具，但尚未声称任务成功率或用户满意度已经获得实测提升。不同平台的原生 Skill 支持也不相同。

## 为什么做 ThinkAlong？

AI 协作经常在两个地方出错：AI 没理解用户真正想要什么，或者虽然理解了，却交付了不完整、不合要求的结果。单纯改写提示词并不能可靠地解决这两个问题。

ThinkAlong 聚焦四个动作：

1. **理解**：识别真实目标、限制条件和已有上下文。
2. **澄清**：只询问会实质影响结果或避免重大风险的信息。
3. **执行**：采用足够简单的流程，尽可能完成实际工作。
4. **验收**：检查真实成果、修复具体缺口，并如实报告已验证和未验证的部分。

## 安装

### Codex
将 `skills/think-along/` 复制到 `~/.agents/skills/think-along/`（个人）或项目的 `.agents/skills/think-along/`，然后使用 `$think-along` 显式调用。

### Claude
Claude Code 可安装到 `~/.claude/skills/think-along/` 或项目的 `.claude/skills/think-along/`。Claude 网页端仅在账号开放自定义 Skills 时支持上传 ZIP。

### ChatGPT 网页端
若账号或工作区已启用 Skills，可在 Skills 页面上传由脚本生成的 ZIP。可用性取决于产品开放范围和工作区设置。

### DeepSeek 与其他 AI
如果宿主支持 Agent Skills，按宿主规定安装；普通聊天界面可复制 `adapters/portable-instructions.md` 中的指令。手动粘贴不会增加工具、文件访问或自动触发能力。

详见[平台兼容指南](docs/platform-compatibility.md)。遵循开放的 [Agent Skills 格式](https://agentskills.io/specification) 不代表所有 AI 产品都原生支持安装。

## 评测

- [任务质量案例](evals/task-cases.md)：Skill 激活后是否按预期工作。
- [触发准确性案例](evals/trigger-cases.md)：请求是否应该触发 Skill。

运行：

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_skill.py
python -m unittest discover -s tests -v
python scripts/package_skill.py
```

这些检查验证结构与文件，不会模拟大模型，也不能证明实际行为改善。若要声称效果提升，需在相同模型、工具、上下文和评分标准下比较启用与未启用 Skill 的结果。

## 设计原则

- 关注最终结果，而不是为了优化提示词而优化提示词。
- 先利用已有上下文，不重复询问已知信息。
- 不设固定追问次数；每个问题都必须值得它带来的沟通成本。
- 简单任务保持简单，复杂度与任务风险相匹配。
- 不编造个人事实或绕过关键授权。
- 使用实际证据验收，不声称执行过未运行的检查。
- 核心指令尽量跨平台，平台专属安装方式单独说明。

## 参与贡献

欢迎提交真实失败案例、触发遗漏、误触发、平台安装问题和可复现测试。请提供输入、预期行为、实际行为和回归检查。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

MIT，详见 [LICENSE](LICENSE)。
