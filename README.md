# ThinkAlong

**Think clearly together. Build directly. Verify what actually works.**

[简体中文](README.zh-CN.md) · [Platform guide](docs/platform-compatibility.md) · [Examples](skills/think-along/references/examples.md) · [Contributing](CONTRIBUTING.md)

![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)
![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-6f42c1.svg)
![CI](https://github.com/koajsj/ThinkAlong/actions/workflows/validate.yml/badge.svg)

ThinkAlong is a portable AI collaboration skill for people who want better outcomes without learning prompt engineering. It is especially designed to remove the **ChatGPT → prompt → Codex relay**: when used in a coding workspace, it helps turn a rough project idea into a practical brief, implementation, and verified deliverable in the same workflow.

> **Status: experimental, v0.4.0 with unreleased instruction changes.** Static validation and packaging are available. Live model behavior and cross-platform installation are not comprehensively benchmarked; no measured success-rate improvement is claimed.

## The problem: you shouldn't have to be the message bridge

A common workflow is: discuss a project in ChatGPT, ask it to write a detailed prompt, copy that prompt to Codex, then explain missing details again when implementation differs from the plan.

ThinkAlong aims to reduce that handoff:

1. **Understand the outcome** — identify the goal, deliverable, hard constraints, assumptions, and acceptance checks.
2. **Choose sensible defaults** — ask only about decisions that materially change the result; do not make non-experts choose technical details unnecessarily.
3. **Work in the current workspace** — inspect the existing repository, plan just enough, and implement when tools permit.
4. **Keep constraints alive** — preserve exclusions and decisions across steps and turns.
5. **Verify and repair** — check the actual result, fix concrete gaps, and report what is verified versus untested.

This is an adaptive workflow, not a mandatory checklist. Simple requests stay simple.

## Try it in Codex

Install the Skill, open the project workspace, and start with your idea in natural language:

```text
$think-along I want to build a useful personal website, but I don't know the technical details. Inspect this workspace, choose sensible defaults, ask only if a decision would materially change the result, implement a working version here, and verify it. Don't just give me a prompt for another AI.
```

ThinkAlong should inspect the existing project before choosing a stack. If the workspace already contains code, it should preserve working behavior and follow project instructions. If the workspace is empty, it should choose a maintainable default and start building. It should not publish or deploy externally without the required authorization.

**Important:** the Skill cannot create tools or workspace access the host does not provide. In a chat-only interface, it should instead provide one concise handoff brief and clearly state that implementation was not executed.

## What makes it different?

- **Project-to-delivery, not prompt-only:** in a coding host, work on the project instead of handing the user another prompt.
- **Outcome contract:** keep goal, deliverable, hard constraints, assumptions, and acceptance checks aligned.
- **Low-friction clarification:** ask only about material unknowns; combine related questions when useful and sequence dependent questions.
- **Cross-turn constraint tracking:** avoid silently dropping requirements halfway through the task.
- **Evidence gate and repair loop:** inspect real outputs, fix causes, and never claim checks that were not performed.
- **Host-aware portability:** use native Agent Skills where available and portable instructions elsewhere, without claiming every platform has the same capabilities.

## Install

### Codex

Copy `skills/think-along/` to:

- Personal: `~/.agents/skills/think-along/`
- Project: `.agents/skills/think-along/`

Invoke explicitly with `$think-along`. See [Codex Skills](https://developers.openai.com/codex/skills).

### Claude Code and Claude web

Claude Code can use the skill folder under `~/.claude/skills/think-along/` or a project-level `.claude/skills/think-along/`. Claude web upload is available only where custom Skills are enabled. See [Claude Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

### ChatGPT web

If Skills are enabled for your account/workspace, upload the generated ZIP from the Skills interface. Availability varies by plan, workspace settings, and rollout. See [ChatGPT Skills](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

### DeepSeek and other models

A model and a host are different things. DeepSeek through a compatible host can use the host's Skill mechanism; a plain chat website without native Skill support can use [portable instructions](adapters/portable-instructions.md). Pasting instructions does not grant file access, tools, memory, or automatic activation.

See the [platform compatibility guide](docs/platform-compatibility.md). The open [Agent Skills specification](https://agentskills.io/specification) does not mean every AI product supports native Skills.

## Static review and evaluation methodology

The current policy permits static review only. Test code and task/trigger/regression case catalogues have been removed. Do not run unit, runtime, behavioral or model tests. Retained methodology documents require separate authorization before future execution:

- [Seven independent measures and scoring rubric](evals/scoring-rubric.md)
- [Static review and evaluation protocol](evals/protocol.md)
- [Research sources and design decisions](docs/research-summary.md)
- [Audit results and limitations](docs/audit-summary.md)

Check metadata, file references and package structure locally:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_skill.py
python scripts/package_skill.py
```

These are development tools, not Skill runtime dependencies. The commands do not execute the Skill, simulate an LLM or establish installation/behavior quality. Model evaluation remains unrun; paid API calls require separate authorization.

Validation also parses Python source and active CI step definitions. Packaging uses a shared six-file allowlist, fixed ZIP timestamps/permissions and portable paths; it checks the staged archive before replacing an existing ZIP. Generated archives stay in ignored `dist/` and are not committed.

## Contribute

Useful contributions include reproducible cases where the Skill still asks the user to relay prompts, drops constraints, asks unnecessary questions, skips implementation, or overstates verification. Include the input, expected behavior, observed behavior, host/model, and evidence. Keep private data out of public issues. See [CONTRIBUTING.md](CONTRIBUTING.md).

If this solves a real problem for you, star the repository and share a concrete case—successes and failures both help improve it.

## License

MIT. See [LICENSE](LICENSE).
