# ThinkAlong Workflow

Use these checkpoints when a mode transition or execution decision is unclear. Core contract, uncertainty, evidence and safety rules remain in [SKILL.md](../SKILL.md); this is not a mandatory sequence.

## Continue from the user's current intent

| Intent or transition | Useful next move | Avoid |
| --- | --- | --- |
| Discuss an idea, compare or assess feasibility | Clarify the problem and audience; propose a direction and explain material trade-offs | Demanding a full specification or starting large code changes |
| Implement the discussed plan | Reuse confirmed decisions and exclusions; inspect the workspace and start the next usable slice | Repeating intake or generating another AI prompt |
| Create, extend, improve or repair a project | Inspect the existing implementation and choose scoped work that meets the outcome contract | Replacing working architecture or stopping at a scaffold |
| Continue earlier work | Compare conversation/project records with actual files, Git changes and available evidence; identify the real next step | Assuming a previous completion claim is current progress |
| Discuss while implementing | Advance authorized work independent of open decisions; ask before dependent or irreversible choices | Blocking all work on cosmetic details or treating ideas as decisions |
| Requested transfer or missing implementation capability | Update one consolidated brief with actual progress, remaining questions and the precise blocker | Sending messages without authority or requiring repeated prompt relays |
| Clear question or bounded transformation | Answer or transform directly | Intake questions or a formal plan |

## Check at useful boundaries

- Before changing files, distinguish existing work from a new project and inspect the actual sources behind summaries. Preserve local edits and working behavior.
- Choose one core user journey and connect its entry point, essential behavior, result and relevant failure states. Expand toward the requested scope after checking this slice; placeholders and disconnected controls are not a usable path.
- Before dependent work, resolve unknowns that would invalidate it. After a requirement changes, update only the affected decisions and checks.
- At a handoff or final delivery, recover constraints from accessible records. If essential context is missing, ask for that specific gap rather than restarting intake. Do not create mandatory progress files or imply cross-host memory.
- Connect each important acceptance criterion to actual output evidence using [acceptance-checks.md](acceptance-checks.md). Execute only checks permitted by the repository, host and user; disclose missing runtime or visual evidence.

## Diagnose a mismatch

Locate the cause: misunderstood intent or mode, omitted constraint, factual/source error, format/schema violation, subjective quality gap, execution failure, scope drift, or unsupported completion claim. For quality gaps, compare the result with the supplied reference, audience and purpose before choosing what to change.

Apply the repair loop in SKILL.md. If the cause remains blocked, name the missing input, permission or capability and a useful next step.
