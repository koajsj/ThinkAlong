# ThinkAlong Examples

These examples show how to apply the workflow without making every task feel procedural.

## 1. Start a project directly in Codex — no prompt relay

**User:** "我想做一个个人网站，帮我直接做出来。我不懂技术，你来决定合理的实现方案。"

**Better behavior in a coding workspace:**
- Recognize this as a project-to-delivery request even if the first sentence is broad.
- Inspect the current workspace, project instructions, existing files, and available checks before choosing a stack.
- If this is an existing project, preserve its architecture and working behavior. If it is empty, choose a simple maintainable default suitable for the stated goal.
- Internally define the essential user journey, must-have content, exclusions, and acceptance checks. Mention only assumptions that materially affect the result.
- Ask only if a missing decision would substantially change the site or introduce a meaningful risk. Do not make the user choose a framework, package manager, or hosting architecture without a real need.
- Implement a coherent usable slice in the current workspace, run relevant checks, inspect the diff, and report actual results.
- Do not output a prompt for the user to copy into another AI unless they asked for a prompt.

**Fallback in a chat-only host:** If no project workspace or code execution is available, say so. Provide one concise handoff bundle with the goal, decisions/defaults, constraints, acceptance checks, and one consolidated implementation prompt. Clearly state that no code was executed.

**Failure to avoid:** producing a long project plan and stopping, creating only a scaffold, or forcing the user to act as a message bridge between ChatGPT and Codex.

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
