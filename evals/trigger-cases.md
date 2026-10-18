# Trigger-accuracy evaluation cases

These cases assess whether ThinkAlong should activate. They are prompts to test manually; no model-level trigger accuracy is claimed.

| ID | Input / context | Expected activation | Reason |
| --- | --- | --- | --- |
| T01 | Explicitly call `$think-along` to plan a trip | Yes | Explicit invocation. |
| T02 | "Help me make a resume from these notes." | Yes | Multi-step deliverable. |
| T03 | "The previous document doesn't follow the attached rules; fix it." | Yes | Repair and acceptance criteria. |
| T04 | "Help me organize these files without deleting any." | Yes | Constraints and file safety. |
| T05 | "Research the latest policy and cite sources." | Yes | Current facts and source checking. |
| T06 | "Make a website from this rough idea." | Yes | Ambiguous, multi-step work. |
| T07 | "Check this spreadsheet for formula errors." | Yes | Inspection and verification. |
| T08 | "Create a study plan for my deadline." | Yes | Planning with constraints. |
| T09 | "Compare these products against my needs." | Yes | Criteria-based comparison. |
| T10 | "Turn these notes into a polished report." | Yes | Transformation with quality criteria. |
| T11 | "What is 15 percent of 80?" | No implicit trigger | Clear, bounded, low-risk. |
| T12 | "Translate 'good morning' into Chinese." | No implicit trigger | Direct task. |
| T13 | "What does this word mean?" | No implicit trigger | Simple explanation. |
| T14 | "Give me three names for a cat." | No implicit trigger | Lightweight creative request. |
| T15 | "Thanks!" | No | Social response only. |
| T16 | "What is the capital of France?" | No implicit trigger | Direct factual question. |
| T17 | "Rewrite this one sentence more politely." | Usually no | Bounded editing request. |
| T18 | Explicit `$think-along` for simple arithmetic | Yes, but answer directly | Explicit call must not force ceremony. |
| T19 | "Continue the plan we discussed earlier." | Yes if context supports it | Prior context and continuity. |
| T20 | "Publish this public post now." | Yes | Consequential action still requires host authorization rules. |

## Reporting

For each run record model/provider, host/version, Skill version, input, activation, output, false-positive/false-negative classification, and notes. Evaluate implicit activation separately from explicit calls.
