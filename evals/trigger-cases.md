# Trigger-accuracy evaluation cases

These cases assess whether ThinkAlong should activate. They are manual test prompts; no model-level trigger accuracy is claimed. Test implicit activation separately from explicit calls.

| ID | Prompt | Expected activation | Reason |
| --- | --- | --- | --- |
| T01 | Explicitly call `$think-along` to plan a trip | Yes | Explicit invocation |
| T02 | "Make me a resume from these notes." | Yes | Multi-step deliverable |
| T03 | "The report doesn't follow the attached rules; fix it." | Yes | Repair and acceptance criteria |
| T04 | "Organize these files by project without deleting any." | Yes | Constraints and file safety |
| T05 | "Research the latest policy and cite sources." | Yes | Current facts and source checking |
| T06 | "Build a website from this rough idea." | Yes | Ambiguous, multi-step work |
| T07 | "Check this spreadsheet for formula errors." | Yes | Inspection and verification |
| T08 | "Create a study plan that fits my deadline and schedule." | Yes | Multiple constraints |
| T09 | "Compare these services against my needs." | Yes | Criteria-based decision |
| T10 | "Turn these notes into a polished report and check it." | Yes | Transformation plus acceptance |
| T11 | "What is 15% of 80?" | No implicit trigger | Simple bounded answer |
| T12 | "Translate 'good morning' into Chinese." | No implicit trigger | Direct transformation |
| T13 | "What does this word mean?" | No implicit trigger | Simple explanation |
| T14 | "Give me three names for a cat." | No implicit trigger | Lightweight creative task |
| T15 | "Thanks!" | No | Social response |
| T16 | "What is the capital of France?" | No implicit trigger | Direct factual question |
| T17 | "Rewrite this sentence more politely." | Usually no | Bounded editing |
| T18 | Explicit `$think-along` for simple arithmetic | Yes, answer directly | Explicit call must not force ceremony |
| T19 | "Continue the plan we discussed earlier." | Yes if relevant context exists | Context continuity |
| T20 | "Publish this post now." | Yes | Consequential action needs target/authority checks |
| T21 | "What's a synonym for 'helpful'?" | No implicit trigger | Simple lookup |
| T22 | "Create a seven-day meal plan under my budget and dietary restrictions." | Yes | Multiple constraints and deliverable |
| T23 | "Explain this error and fix the project if you can." | Yes | Diagnose and execute |
| T24 | "Make this spreadsheet look nicer." | Yes if file editing is requested | Artifact modification and acceptance |
| T25 | "Summarize the attached PDF in five bullets." | Usually no special workflow; direct task | Clear bounded summarization |
| T26 | "Compare the attached PDF with the policy and fix all mismatches." | Yes | Cross-document audit and repair |
| T27 | "I don't know which laptop to buy; ask me only what matters." | Yes | Decision support and minimal clarification |
| T28 | "Tell me a joke." | No implicit trigger | Simple creative request |
| T29 | "Check whether this claim is true using reliable sources." | Yes | Evidence verification |
| T30 | "Improve the previous result without changing its meaning or format." | Yes | Context-preserving repair |

## Reporting

For each run, record model/provider, host/version, Skill version, prompt, whether it activated, output, false-positive/false-negative classification, and notes.
