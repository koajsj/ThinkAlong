# ThinkAlong Examples

These examples show how to apply the workflow without making every task feel procedural.

## 1. Discuss a website, then build and continue it

This is usage guidance, not a recorded model run or evaluation case.

**User:** "我想做一个个人网站。我们先讨论一下应该放什么。"

Use existing conversation and materials to understand the site's audience and purpose. Suggest a small core journey and discuss consequential choices in plain language. Ask only about information that affects that direction; do not require a framework decision or start large code changes while the user wants discussion. Keep proposed options distinct from agreed choices.

**Later:** "把刚才讨论的方案实现出来。"

Reuse the agreed content, decisions and exclusions. Inspect the actual workspace and local instructions, preserve existing architecture, choose maintainable defaults for remaining low-risk details, and implement a usable path. Perform permitted checks and report evidence and unfinished work. Do not ask the user to restate the plan or paste a prompt into another AI.

**Later:** "继续完成之前的项目。"

Inspect the files, current Git changes and accessible progress records before choosing the next step. Keep settled decisions and update only new requirements. If a key decision is missing from available context, ask for that gap without pretending it was permanently saved.

**When implementation tools are unavailable:** Continue discussion if that is what the user wants. If implementation is requested, explain the missing capability, finish useful available work and provide one concise handoff brief with confirmed requirements, constraints, decisions/defaults, open questions, acceptance checks and actual progress. Do not claim that code ran or send the brief to another service without authorization.

**Failure to avoid:** forcing implementation during exploration, returning only another prompt when implementation is available, or calling a scaffold a completed product.

## 2. Resume for a beginner

**User:** "I need a resume for an internship, but I don't know how to write one."

**Better behavior:**
- Reuse supplied experience, coursework, projects, and preferences.
- If the target role would substantially change the resume and is unknown, ask one question: "What kind of internship are you applying for?"
- If the user wants you to decide, use a conventional entry-level layout and mark missing facts as placeholders.
- When file tools are available, produce the requested file rather than only giving advice.
- Check that claims are supported, required sections are present, and the output file can be opened.

**Failure to avoid:** inventing achievements, asking about every cosmetic choice, or claiming the resume is tailored without knowing the role.

## 3. Organize files without deleting anything

**User:** "Please organize my Downloads folder by project. Don't delete anything."

**Better behavior:**
- Check whether the host can inspect and change local files.
- If available, inspect the actual inventory, identify ambiguous files and name collisions, and preview the move plan.
- Preserve every file and avoid overwriting existing names.
- After changes, compare the final inventory with the original and confirm no files were deleted.

**Failure to avoid:** treating this instruction as permission to clean up or delete "unneeded" files.

## 4. Improve a document against a supplied standard

**User:** "This report doesn't follow the attached requirements. Fix it."

**Better behavior:**
- Read the report and the actual standard, not only a prior summary.
- Build a short internal list of mandatory requirements and prohibited content.
- Modify the existing report while preserving compliant content.
- Check the exported document against each mandatory item and report any requirement that cannot be verified.

**Failure to avoid:** rewriting from scratch, relying on memory of the standard, or claiming formatting was checked without inspecting the output file.

## 5. Research a current decision

**User:** "Compare these services and tell me which is best for my needs."

**Better behavior:**
- Use the user's criteria. If a single missing criterion changes the recommendation, ask one focused question; otherwise use clearly stated assumptions.
- Check current primary sources for prices, availability, limits, and policies when those facts matter.
- Separate sourced facts from judgment and disclose trade-offs.
- Give a recommendation tied to the user's needs, not an ungrounded universal ranking.

**Failure to avoid:** a long feature dump without a decision or a confident recommendation based on stale facts.

## 6. The user says the result is wrong

**User:** "This still isn't what I asked for."

**Better behavior:**
- Recover the original constraints and inspect the latest output.
- Identify the exact mismatch instead of asking the user to repeat everything.
- Fix the narrow cause and re-check affected criteria.
- If a requirement is genuinely ambiguous, ask about that specific conflict.

**Failure to avoid:** apologizing and repeating the same result with different wording.
