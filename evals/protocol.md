# Evaluation protocol

Current policy: **static review only**. Test code and task/trigger/regression case catalogues have been removed at the user's request. Retain this protocol and the [scoring rubric](scoring-rubric.md) as methodology; neither authorizes execution. Do not add or run unit, runtime, behavioral or model tests unless the user changes this policy. Do not incur model API costs without explicit budget authorization.

## Three evidence layers

| Layer | Evidence | Limits |
| --- | --- | --- |
| Static review — permitted | Source inspection, Python syntax, safe YAML parsing, metadata/schema checks, local links, package allowlist and ZIP integrity | Cannot establish model adherence, actual activation, runtime success or host installation |
| Human behavioral evaluation — not run | Human grading of actual model transcripts, tool results and artifacts against frozen criteria | Selected observations alone cannot establish broad improvement |
| Controlled model benchmark — not run | Repeated paired baseline/with-skill executions under recorded matching conditions with independent grading | Cannot establish universal benefit or untested host compatibility |

Reading expected behavior or discussing synthetic answers is not a behavioral run. Static CI must not report behavior scores. No case catalogue or benchmark output is retained in the repository.

## Current static review procedure

1. Inspect existing source, relevant instructions, dependencies and CI before editing. Identify user constraints and preserve valid work.
2. Parse source and metadata; inspect naming, field types/limits and canonical identity against the linked specification. Check that local references resolve inside the repository and runtime references stay inside the package allowlist.
3. Inspect package inputs, symlinks, license inclusion and exact ZIP members. Building an archive reads files; it does not execute the Skill or simulate a model.
4. Inspect the diff and changed-file inventory for scope drift, secrets, private data, duplicated rules and obsolete test entrypoints. With no `.git`, compare to a saved pre-edit snapshot and disclose the lack of branch/history evidence.
5. Record actual commands, outputs and exit codes. State which evidence is static and which checks were not run. Do not treat absent runtime/model evidence as a pass.

## Requirements if behavioral evaluation is authorized later

Before any future run, obtain authorization to change the static-only policy and separately confirm any billable budget. The following are design requirements, not current tasks or executable cases:

- Freeze exact prompts, input artifacts, context turns, tool permissions/responses and assertions before observing outputs. Snapshot or hash the Skill and fixtures. Use fictional data and isolated fake tools for external actions.
- Separate task quality (explicitly loaded Skill), implicit discovery (metadata only) and explicit invocation. Quoted identifiers in data are not invocation authority. Conditional trigger expectations must be fixed from the supplied context before grading.
- Match model/provider revision, host/version, other loaded instructions, sampling settings and tool access between arms. Reset conversations/workspaces; verify the baseline does not load ThinkAlong elsewhere.
- Predeclare repetitions, budget, timeout and stopping conditions. Randomize arm order, preserve all failures and set aside holdouts before tuning. Report per-case paired differences and sample size; small or uncontrolled samples do not establish causal improvement.
- Capture actual outputs, artifacts, calls/responses and host loading traces. Self-reported activation alone is unknown. A host that loads every Skill unconditionally cannot measure selection precision.
- Grade parseable structures mechanically and intent/question necessity/root-cause repair from full evidence. Blind graders to arms where practical and resolve disagreements from artifacts. A model judge requires separate cost authorization.
- Report attempted/completed/graded/planned counts, timeout/tool-error counts and exclusions. Timeouts are unsuccessful attempts; unknown activations and missing grades remain unknown/ungraded. Do not silently drop them or turn them into passes. A zero denominator is N/A.

## Record and release claims

A future run record requires run/pair/repetition IDs and timestamp, fixture and source hashes, exact input turns, model/provider revision, host/settings, Skill version and activation mode, tool availability, status and raw artifact/log references. Add the five historical scores, independent violation/question counts, repair score or N/A, grader and evidence per assertion. Record latency/tokens/cost only from host measurements; otherwise mark unavailable. `not_run` has no score or success claim.

Keep the seven measures separate: task quality, trigger accuracy, unnecessary questions, hard-constraint violations, unsupported completion claims, repair quality and safety boundaries. Any explicit-constraint violation, unsupported completion claim, unauthorized action or leak is a hard failure regardless of total score. Missing evidence prevents a pass claim. An honest host blocker can satisfy honesty while completion remains partial.

A documentation/tooling release may remain experimental with behavioral evaluation explicitly unrun. Claims of behavior gains require actual controlled evidence, and platform compatibility claims require installation/activation evidence. Both remain unavailable under the current static-only policy.
