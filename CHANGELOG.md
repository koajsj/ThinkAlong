# Changelog

## Unreleased

- Added a source-pinned research summary for six reference projects, with per-directory license boundaries and explicit design decisions.
- Preserved the canonical Skill and runtime references without new behavior rules or dependencies.
- Separated task quality, activation, unnecessary questions, constraint violations, unsupported claims, repair quality and safety measures in the retained rubric/protocol.
- At the user's request, removed all automated test code and task/trigger/regression cases, and switched CI and contributor guidance to static review only. Historical entries below describe earlier versions, not the current tree.
- Tightened static YAML/metadata and runtime package reference/symlink checks; clarified license inclusion for folder installation.
- Parse Python syntax and actual CI step definitions during static validation, instead of accepting command text in comments.
- Share the six-file package allowlist; stage and verify archives before atomic replacement, with fixed timestamps/permissions and portable ZIP paths.
- No behavior/model evaluation or compatibility improvement is claimed. Runtime Skill version remains 0.4.0; a source push does not create a tagged release.

## 0.4.0 — 2026-10-18

- Added an outcome contract, uncertainty triage, cross-turn constraint ledger, evidence gate, and root-cause repair loop.
- Added deliverable-specific acceptance checks and worked examples.
- Expanded task-quality and trigger evaluation plans to 30 cases each and added a consistent scoring rubric.
- Strengthened metadata validation, exact case checks, package-content checks, and validator regression tests.
- Kept repository documentation and test tooling outside the installable Skill ZIP.
- Improved English/Chinese README content and clarified platform limitations.
- No live model-behavior improvement is claimed; controlled evaluations remain pending.

## 0.3.0

- Established the canonical portable Agent Skill source.
- Added platform guidance, portable instructions, task and trigger evaluation plans, validator tests, packaging, and CI.

## 0.2.0

- Tightened adaptive behavior, output-format fidelity, context reuse, and repair guidance.

## 0.1.0

- Initial prototype for adaptive clarification, execution, verification, and manual evaluation.
