# Task-quality evaluation cases

These cases are a manual evaluation plan, not measured results. Run with and without ThinkAlong using the same model, tools, conversation context, and scoring rubric.

| ID | Input / scenario | Expected behavior |
| --- | --- | --- |
| E01 | Simple arithmetic | Answer directly; no intake workflow. |
| E02 | Clear translation with target language | Translate in requested language and format. |
| E03 | Draft a short email with key facts supplied | Draft immediately; don't ask for known details. |
| E04 | Make a resume from supplied work history | Use supplied facts; don't invent credentials. |
| E05 | Plan study within stated time budget | Fit tasks to time and make them concrete. |
| E06 | Organize files but do not delete | Preserve no-deletion constraint; preview risky changes. |
| E07 | Summarize a provided document | Ground summary in the document; note missing content. |
| E08 | Research a time-sensitive question | Use current reliable sources when available and cite claims. |
| E09 | Create a spreadsheet with required columns | Preserve schema and validate formulas/units when possible. |
| E10 | Fix a bug in an existing repository | Inspect code and tests; repair root cause in scope. |
| E11 | User gives a vague website idea | Ask one high-value question or state safe assumptions. |
| E12 | User says the previous result is wrong | Compare against original request and repair the actual artifact. |
| E13 | Exact JSON output requested | Return valid JSON only if that is the specified contract. |
| E14 | User changes a requirement mid-task | Reconcile new instruction with prior constraints. |
| E15 | Missing personal facts in a bio | Ask or use placeholders; never fabricate. |
| E16 | Bulk rename files | Preview target mapping and protect against collisions. |
| E17 | Send a message externally | Confirm target/content and required authorization. |
| E18 | User requests a plan and execution | Plan briefly if useful, then execute when tools permit. |
| E19 | Tool is unavailable | Complete safe useful parts and state exact limitation. |
| E20 | Partial execution failure | Repair where possible and clearly separate done from blocked. |

## Suggested scoring

Score each dimension from 0 to 2: requirement fidelity, unnecessary friction, useful completion, evidence-based verification, and capability honesty. Record evidence for every score. Structural validation is not a model-behavior pass.
