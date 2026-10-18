# ThinkAlong

**Discuss naturally. Build when ready. Verify actual results.**

[简体中文](README.zh-CN.md) · [Platform guide](docs/platform-compatibility.md) · [Examples](skills/think-along/references/examples.md) · [Contributing](CONTRIBUTING.md)

![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)
![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-6f42c1.svg)
![CI](https://github.com/koajsj/ThinkAlong/actions/workflows/validate.yml/badge.svg)

ThinkAlong is a portable AI collaboration skill for people who want better outcomes without learning prompt engineering. It is especially designed to remove the **ChatGPT → prompt → Codex relay**: keep discussion, confirmed decisions and implementation connected; when the user wants execution and workspace tools are available, work on the actual project.

> **Status: experimental, v0.4.0 with unreleased instruction changes.** Static validation and packaging are available. Natural-language activation, model behavior and cross-platform installation have not been exercised in this review; no measured success-rate improvement is claimed.

## The problem: you shouldn't have to be the message bridge

A common workflow is: discuss a project in ChatGPT, ask it to write a detailed prompt, copy that prompt to Codex, then explain missing details again when implementation differs from the plan.

ThinkAlong aims to reduce that handoff:

1. **Explore when wanted** — discuss the problem, audience and options; keep the goal, constraints, decisions and acceptance checks aligned.
2. **Choose sensible defaults** — ask only about decisions that materially change the result; do not make non-experts choose technical details unnecessarily.
3. **Work in the current workspace** — inspect the existing repository, plan just enough, and implement when tools permit.
4. **Keep constraints alive** — preserve exclusions and decisions across steps and turns.
5. **Verify and repair** — check the actual result, fix concrete gaps, and report what is verified versus untested.

This is an adaptive workflow, not a mandatory checklist. Simple requests stay simple.

## From discussion to implementation

Install the Skill in a supported host and open your project workspace. Use ordinary language, without memorizing a command:

```text
I want a personal website. Let's discuss what it should do first.
Implement the plan we just discussed.
Continue the project from its current state.
```

These are usage illustrations, not measured activation results. The first request stays in discussion. The next reuses agreed requirements and implements in the accessible workspace. Continuation starts by inspecting actual files and progress. Direct requests to add a feature, improve or repair a project should also lead to implementation; technical details with safe defaults do not require repeated confirmation. Ordinary questions, translations, local text edits and basic code explanations stay direct.

The host controls discovery/loading and tools; the model controls adherence. The description makes natural-language matching possible, and `policy.allow_implicit_invocation: true` permits it in Codex (already the host default). This does not force activation. `$think-along` remains an optional explicit fallback, not a required project-development ritual. See [official Skill guidance](https://learn.chatgpt.com/docs/build-skills).

If you want discussion alongside implementation, independent authorized work can continue while consequential choices are discussed. A prompt/handoff is the main deliverable only when you request it, request another tool, or implementation needs unavailable capabilities. It should be one brief with the goal, confirmed requirements, constraints, decisions/defaults, open questions, acceptance checks and actual progress. The Skill does not transfer chats, grant tools, permanently save context, or authorize publishing/deployment.

## What makes it different?

- **Project-to-delivery, not prompt-only:** in a coding host, work on the project instead of handing the user another prompt.
- **Outcome contract:** keep goal, deliverable, hard constraints, assumptions, and acceptance checks aligned.
- **Low-friction clarification:** ask only about material unknowns; combine related questions when useful and sequence dependent questions.
- **Cross-turn constraint tracking:** avoid silently dropping requirements halfway through the task.
- **Evidence gate and repair loop:** inspect real outputs, fix causes, and never claim checks that were not performed.
- **Host-aware portability:** use native Agent Skills where available and portable instructions elsewhere, without claiming every platform has the same capabilities.

## Install

### Codex

Copy `skills/think-along/` to a location below and include the root `LICENSE` in the installed `think-along/` folder. The generated ZIP includes it. Inspect existing destinations before upgrading and preserve local edits:

- Personal: `~/.agents/skills/think-along/`
- Project: `.agents/skills/think-along/`

Describe the project naturally; explicit `$think-along` remains available if needed. Loading still depends on host discovery, configuration and matching. See [Codex Skills](https://learn.chatgpt.com/docs/build-skills).

### Claude Code and Claude web

Install the folder with `LICENSE` for Claude Code under `~/.claude/skills/think-along/` or a project-level `.claude/skills/think-along/`. Claude Code can select from descriptions or use `/think-along`. Claude web ZIP upload requires custom Skills and code execution to be enabled; it does not grant access to your local repository. See [Claude Code Skills](https://code.claude.com/docs/en/skills) and [Claude custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

### ChatGPT web

Use the Skill installation/upload controls actually enabled for your account or workspace; if custom Skills are unavailable, use the portable instructions. Files, execution and repository access depend on the current tools and permissions. Continue discussion without tools; offer an implementation handoff only when requested or needed. See [ChatGPT Skills](https://learn.chatgpt.com/docs/skills-and-plugins) and [ChatGPT capabilities](https://learn.chatgpt.com/docs/use-chatgpt).

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
