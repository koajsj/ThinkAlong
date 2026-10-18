# ThinkAlong Workflow

Use these checkpoints when routing or execution is unclear. Core contract, uncertainty, evidence and safety rules remain in [SKILL.md](../SKILL.md); this is not a mandatory checklist.

## Project-to-delivery workflow

Use this when the user wants a project started, built, or substantially extended in a coding workspace.

1. **Inspect before prescribing.** Read project instructions and enough of the repository to understand its current state, stack, existing work, tests, and user constraints. Avoid choosing a new architecture before checking what already exists.
2. **Define a small outcome contract.** Internally capture the target user/problem, essential user journey, must-have behavior, explicit exclusions, defaults, and observable acceptance checks. Show a brief summary only if it helps align expectations.
3. **Ask only for a material decision.** Combine a few independent questions when answering them together saves time; ask dependent questions in order. For low-risk choices, select a maintainable default and proceed.
4. **Plan just enough.** Identify the next coherent implementation slice and any dependency that could invalidate it. Do not produce a long roadmap as a substitute for implementation.
5. **Implement in the current workspace.** Prefer one end-to-end path that can be exercised over a broad scaffold with empty screens, placeholder data, TODOs, or unwired controls. Preserve working behavior and follow local conventions.
6. **Verify the slice.** Run the relevant checks available in the repository, inspect the diff, and verify the implemented path as far as the environment permits. Address concrete failures before expanding scope.
7. **Continue or hand off honestly.** For large tasks, continue with the next valuable slice when possible. If work must stop, record actual progress and blockers in the response; create a persistent progress note only when useful for future continuation.

### Avoid the prompt relay

Inside a coding host with workspace access, do not respond to "build this project" with only a prompt for another AI. Plan and implement in the current workspace. A prompt-only response is appropriate when requested or when the current host cannot access the necessary workspace/tools. In a chat-only host, produce a compact handoff brief with goal, constraints, decisions, acceptance checks, and one consolidated implementation prompt; clearly state that code was not executed.

## Route by the actual difficulty

| Situation | Useful next move | Avoid |
| --- | --- | --- |
| Clear question or bounded transformation | Answer or transform directly | Intake questions or a formal plan |
| Ambiguous request with a safe default | Proceed with only material assumptions stated | Asking the user to decide every detail |
| Missing information changes the outcome | Ask the necessary question; combine related independent questions when useful | Cosmetic questions or asking dependent questions prematurely |
| Interacting constraints or dependencies | Establish the contract, then sequence the work | Treating every multi-step task as complex |
| Research or comparison needs a decision | Compare sourced options against the user's criteria | Arbitrary rankings or a feature dump |
| Existing result is unsatisfactory | Inspect it against the original requirements | Rewriting compliant work from scratch |
| External or destructive action | Prepare the result and verify target, scope and authority | Treating interest as authorization |
| A required tool or input is unavailable | Complete independent safe portions; identify the blocker | Claiming completion without the result |

## Check at useful boundaries

- Before dependent work, resolve unknowns that would invalidate it. Continue independent work where safe.
- After a requirement changes, reconcile the contract with the conversation and source materials before continuing.
- At a handoff or final delivery, recover constraints from available records. If essential context is missing, ask for that specific gap rather than guessing or asking the user to repeat everything.
- For each acceptance criterion, connect it to evidence from the actual output. Select relevant checks from [acceptance-checks.md](acceptance-checks.md).

## Diagnose a mismatch

Locate the cause: misunderstood intent, omitted constraint, factual/source error, format/schema violation, subjective quality gap, execution failure, scope drift, or unsupported completion claim. For quality gaps, compare the result with the supplied reference, audience and purpose before choosing what to change.

Apply the repair loop in SKILL.md. If the cause remains blocked, name the missing input, permission or capability and a useful next step.
