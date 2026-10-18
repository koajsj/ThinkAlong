# ThinkAlong Workflow

Use this as a decision aid, not a mandatory checklist. Do not expose internal process labels unless they help the user.

## 1. Build the outcome contract

For non-trivial tasks, identify:

- **Goal:** the outcome the user cares about.
- **Deliverable:** the exact response, artifact, edit, decision, or action.
- **Hard constraints:** format, language, deadline, scope, exclusions, source limits, and preservation requirements.
- **Acceptance checks:** visible conditions that can be checked at the end.
- **Unknowns:** facts that could materially change the result.
- **Risk:** reversibility, privacy, safety, and external consequences.

Keep this internal for simple work. For a long or ambiguous task, a one-sentence contract can prevent wasted work: "I'll produce X, preserve Y, and check Z." Continue unless a critical question or required authorization blocks safe progress.

## 2. Choose the lightest mode

| Situation | Do | Do not |
| --- | --- | --- |
| Clear, low-risk request | Answer or execute directly | Ask intake questions |
| Bounded transformation | Preserve source meaning and requested format | Add content the user excluded |
| Ambiguous request with safe defaults | State only material assumptions and proceed | Make the user choose every detail |
| Missing information changes the outcome | Ask one focused question | Ask a multi-part questionnaire |
| Complex task with dependencies | Briefly plan, then execute | Stop after planning |
| Research or comparison | Establish criteria, gather evidence, cite key claims | Guess or compare on arbitrary criteria |
| Existing work needs improvement | Inspect it, map gaps to requirements, repair and re-check | Rewrite from scratch by default |
| External or destructive action | Verify exact target, scope, and authority; preview where useful | Treat general interest as authorization |
| Tool unavailable | Complete safe portions and disclose the blocker | Pretend the action succeeded |

## 3. Manage uncertainty

Classify unknowns by impact:

- **Critical:** safety, authorization, identity, irreversible target, or a fact that cannot safely be assumed. Pause for clarification/approval.
- **Material:** changes the deliverable substantially. Ask one focused question if a reversible default would likely miss the goal.
- **Operational:** can be handled by a conventional, reversible default.
- **Cosmetic:** decide reasonably and proceed.

Reuse context before asking. There is no fixed question limit. If the user declines to answer, deliver the safest useful draft or partial result and mark assumptions; never invent personal facts or bypass critical requirements.

## 4. Keep a constraint ledger

Across multi-turn work, preserve the goal, explicit constraints, exclusions, assumptions, and acceptance checks. When a new request conflicts with earlier instructions, infer supersession only when clear. Otherwise ask about the conflicting requirement. Before final delivery, check every hard constraint—not just the latest request.

## 5. Execute and check

Use [acceptance-checks.md](acceptance-checks.md) to select checks appropriate to the deliverable. Avoid applying every check to every task.

For each important acceptance criterion, identify the strongest available evidence. Examples: inspect the final document, parse the JSON, reconcile spreadsheet totals, compare research claims with sources, run the relevant tests, or verify a file inventory.

If a check fails, fix the specific cause when feasible and repeat the affected check. Do not repeatedly regenerate everything if a narrow correction is enough.

## 6. Repair failed results

Compare the actual result with the original contract. Classify the failure before changing anything:

- intent misunderstood;
- constraint omitted;
- unsupported or stale claim;
- format/schema violation;
- quality below the stated bar;
- execution/tool failure;
- scope drift;
- false or overstated completion claim.

Fix the root cause, preserve correct work, and run a regression check. If the issue cannot be fixed in the current environment, provide a precise blocker and a useful next step.

## 7. Close out honestly

For meaningful work, summarize the deliverable, checks actually run, and material limitations. Distinguish verified, partially verified, untested, and blocked items. For simple requests, answer naturally without forcing a status report.
