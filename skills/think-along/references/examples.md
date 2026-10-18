# ThinkAlong Examples

These examples show how to apply the workflow without making every task feel procedural.

## 1. Resume for a beginner

**User:** "I need a resume for an internship, but I don't know how to write one."

**Better behavior:**
- Reuse any supplied experience, coursework, projects, and preferences.
- If the target role would substantially change the resume and is unknown, ask one question: "What kind of internship are you applying for?"
- If the user wants you to decide, use a conventional entry-level layout and mark missing facts as placeholders.
- When file tools are available, produce the requested file rather than only giving advice.
- Check that claims are supported, required sections are present, and the output file can be opened.

**Failure to avoid:** inventing achievements, asking about every cosmetic choice, or claiming the resume is tailored without knowing the role.

## 2. Organize files without deleting anything

**User:** "Please organize my Downloads folder by project. Don't delete anything."

**Better behavior:**
- Check whether the host can inspect and change local files.
- If available, inspect the actual inventory, identify ambiguous files and name collisions, and preview the move plan.
- Preserve every file and avoid overwriting existing names.
- After changes, compare the final inventory with the original and confirm no files were deleted.

**Failure to avoid:** treating this instruction as permission to clean up or delete "unneeded" files.

## 3. Improve a document against a supplied standard

**User:** "This report doesn't follow the attached requirements. Fix it."

**Better behavior:**
- Read the report and the actual standard, not only a prior summary.
- Build a short internal list of mandatory requirements and prohibited content.
- Modify the existing report while preserving compliant content.
- Check the exported document against each mandatory item and report any requirement that cannot be verified.

**Failure to avoid:** rewriting from scratch, relying on memory of the standard, or claiming formatting was checked without inspecting the output file.

## 4. Research a current decision

**User:** "Compare these services and tell me which is best for my needs."

**Better behavior:**
- Use the user's criteria. If a single missing criterion changes the recommendation, ask one focused question; otherwise use clearly stated assumptions.
- Check current primary sources for prices, availability, limits, and policies when those facts matter.
- Separate sourced facts from judgment and disclose trade-offs.
- Give a recommendation tied to the user's needs, not an ungrounded universal ranking.

**Failure to avoid:** a long feature dump without a decision or a confident recommendation based on stale facts.

## 5. A vague idea for a website

**User:** "I want a personal website, but I don't know anything about coding."

**Better behavior:**
- Do not force the user to choose frameworks, databases, hosting providers, or architecture.
- Establish the website's purpose and essential content; ask only if the missing purpose materially changes the design.
- Choose a sensible, maintainable default and state it briefly.
- If coding tools and a workspace are available, implement and verify the site; otherwise provide a concrete starter artifact and explain what cannot be executed.

**Failure to avoid:** dumping technical decisions on the user or returning only a prompt when the user asked for a website.

## 6. The user says the result is wrong

**User:** "This still isn't what I asked for."

**Better behavior:**
- Recover the original constraints and inspect the latest output.
- Identify the exact mismatch instead of asking the user to repeat everything.
- Fix the narrow cause and re-check affected criteria.
- If a requirement is genuinely ambiguous, ask about that specific conflict.

**Failure to avoid:** apologizing and repeating the same result with different wording.
