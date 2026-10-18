# ThinkAlong

**Think clearly together. Get useful results with less back-and-forth.**

[简体中文](README.zh-CN.md) · [Platform guide](docs/platform-compatibility.md) · [Examples](skills/think-along/references/examples.md) · [Contributing](CONTRIBUTING.md)

![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)
![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-6f42c1.svg)
![CI](https://github.com/koajsj/ThinkAlong/actions/workflows/validate.yml/badge.svg)

ThinkAlong is a portable AI collaboration skill for people who want better outcomes without learning prompt engineering. It turns vague requests into a practical **outcome contract**, asks only consequential questions, preserves constraints across multi-step work, and checks the actual deliverable.

> **Status: experimental, v0.4.0.** The repository has structural validation and manual evaluation cases. Live model behavior and cross-platform installation are not yet comprehensively benchmarked. No measured success-rate improvement is claimed.

## The problem is not just the prompt

AI can misunderstand the goal, forget constraints halfway through, make users decide technical details they do not understand, or claim a task is done without checking the result. Rewriting the prompt alone does not reliably prevent these failures.

ThinkAlong uses five practical mechanisms:

1. **Outcome contract** — identify the goal, deliverable, hard constraints, acceptance checks, unknowns, and risks.
2. **Uncertainty triage** — ask only when the answer materially changes the outcome or safety; otherwise use sensible reversible defaults.
3. **Constraint ledger** — preserve exclusions and requirements across turns instead of optimizing only for the latest message.
4. **Evidence gate** — inspect the actual result against acceptance checks; distinguish verified, partial, untested, and blocked work.
5. **Repair loop** — classify the mismatch, fix its cause, and re-check the affected criteria.

The process is adaptive, not a mandatory checklist. Simple requests stay simple.

## Example

**Request:** “I need an internship resume, but I don't know how to write one.”

A weak workflow may ask about every formatting preference—or invent achievements to fill gaps.

ThinkAlong should reuse supplied facts, ask about the target role only if it materially changes the resume, use placeholders for missing personal information, produce the actual file when the host can, and check the result against the supplied facts and requested format.

See more [worked examples](skills/think-along/references/examples.md).

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

## Evaluate it

The repository separates task quality, trigger accuracy, and scoring:

- [Task-quality cases](evals/task-cases.md)
- [Trigger-accuracy cases](evals/trigger-cases.md)
- [Scoring rubric and baseline method](evals/scoring-rubric.md)

Run structural validation, validator regression tests, and packaging locally:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_skill.py
python -m unittest discover -s tests -v
python scripts/package_skill.py
```

These checks validate repository files and package structure; they do not simulate an LLM. To assess actual benefit, run the same cases with and without ThinkAlong using comparable model, host, tools, and context. Record failures as well as successes.

## Design principles

- Outcome over prompt polish.
- Context before questions.
- Defaults for reversible choices; clarification for material uncertainty.
- Work before advice when execution is possible.
- Hard constraints survive the entire task.
- Evidence before completion claims.
- Repair causes, not just wording.
- Platform portability without pretending all hosts have identical capabilities.

## Contribute

Useful contributions include reproducible false activations, missed triggers, constraint drops, unnecessary questions, weak verification, and platform installation issues. Include the input, expected behavior, observed behavior, host/model, and a regression case. Keep private data out of public issues. See [CONTRIBUTING.md](CONTRIBUTING.md).

If this solves a real problem for you, star the repository and share a concrete case—successes and failures both help improve it.

## License

MIT. See [LICENSE](LICENSE).
