# Acceptance Checks by Deliverable

Select only checks that match the task. These are prompts for verification, not a demand to show a checklist to the user.

## Discussion, implementation and handoff

- Does the output fit the user's current intent: useful exploration, actual implementation or a requested/necessary handoff? A discussion request must not trigger large code changes.
- Were confirmed decisions and constraints reused, with only material unresolved questions raised? For continuation, was actual progress inspected rather than inferred from an old summary?
- Does discussion clarify the problem, audience, core workflow or a material trade-off without forcing a questionnaire or technical specification?
- If handoff is necessary or requested, is there one copyable brief with the goal, confirmed requirements, constraints, defaults/decisions, open questions and acceptance checks, plus an accurate execution status?

## Project implementation

- Does the implementation solve the stated user problem and support the essential end-to-end journey, rather than merely presenting a scaffold?
- Were existing repository instructions, architecture, and working behavior inspected and preserved?
- Are must-have behaviors and hard constraints reflected in the actual implementation?
- Are user-facing controls connected to real behavior, or clearly marked as unavailable rather than implied to work?
- Are empty, loading, failure, and success states handled where relevant?
- Were permitted build, type, test, lint, or static checks actually run, and are their results accurately reported?
- Are unfinished features, mock data, placeholders, and untested runtime paths disclosed?
- Was the change set inspected for accidental scope expansion, secrets, generated artifacts, and unrelated edits?
- If the host cannot execute code, is the deliverable explicitly described as a handoff/specification rather than a completed implementation?

## Subjective quality

- Derive a few concrete criteria from the user's references, intended audience and purpose; distinguish explicit requirements from inferred preferences.
- Assess the actual result against those criteria and explain material trade-offs. Compliance with format or a successful build alone does not establish writing, visual or decision quality.
- When no reference is supplied, use a conventional, reversible default. Clarify taste only if it materially changes the outcome; do not present an inferred preference as user approval or a universal quality judgment.

## Documents and writing

- Does the result answer the intended audience and purpose?
- Are all required sections, facts, sources, tone, length, and format present?
- Are excluded elements absent?
- Are names, dates, quotations, citations, and numbers grounded in supplied or verified sources?
- If a file was requested, inspect the actual exported file for content and formatting; do not stop at a draft in chat.

## Resumes, bios, applications, and personal statements

- Is every factual claim supported by user-provided material?
- Are missing achievements, dates, skills, and credentials represented as questions or placeholders rather than invented?
- Does the result fit the target role or purpose?
- Are wording improvements truthful rather than inflated?

## Research and recommendations

- Are key claims supported by reliable sources appropriate to the claim?
- Are time-sensitive facts current and dated where relevant?
- Are facts separated from estimates, assumptions, and opinions?
- Are competing options evaluated against the user's criteria, with trade-offs and uncertainties made visible?
- Are source limitations or inaccessible documents disclosed?

## Plans, schedules, and learning

- Does the plan fit the stated time budget, deadlines, available resources, and current skill level?
- Are tasks specific enough to start, prioritized, and sized realistically?
- Are milestones or feedback loops included when they materially improve follow-through?
- Does the plan adapt to stated preferences instead of imposing a generic routine?

## Spreadsheets and structured data

- Are columns, types, units, formulas, and output schema correct?
- Do totals and representative rows reconcile?
- Are blanks, duplicates, outliers, and edge cases handled according to the request?
- Does exported CSV/JSON/XLSX open and parse as expected?
- Are original data and formulas preserved when required?

## Files and local workspace changes

- Is the target directory and scope correct?
- Have collisions, ambiguous matches, hidden files, and existing outputs been considered?
- Were destructive changes avoided unless specifically requested and authorized?
- Is there a preview or recoverable copy for risky bulk operations when practical?
- Does the final inventory match the requested change?

## Software and technical work

- Was the existing repository and its instructions inspected first?
- Are changes limited to the requested scope and compatible with existing conventions?
- Did relevant tests, type checks, builds, linters, or static checks actually run?
- Were failures fixed and affected checks rerun?
- Are runtime, visual, integration, security, and deployment checks distinguished from static evidence?

## Creative and visual deliverables

- Does the result match the requested subject, style, audience, dimensions, and exclusions?
- Are any claims about visual inspection based on an actual rendered output?
- Is the output usable in the requested format, not just a description of what to make?

## Communication and external actions

- Is the recipient, target, content, timing, and channel correct?
- Is the draft clearly distinguished from a sent/published message?
- Has required user authorization been obtained before the external action?
- Is success based on the host's actual confirmation rather than the intent to execute?

## Exact-format output

- Is the output parseable and compliant with the required schema?
- Are forbidden wrappers, explanations, Markdown fences, or extra fields absent?
- If exact syntax cannot be verified, is that limitation stated rather than hidden?
