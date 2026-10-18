# Public Release Checklist

## Repository quality

- [ ] English and Simplified Chinese READMEs match in purpose, installation scope, and limitations.
- [ ] License, changelog, contribution guidance, security guidance, and issue templates are present.
- [ ] No secrets, private data, local machine paths, or unrelated generated files are included.
- [ ] Run validator, unit tests, and package script.
- [ ] Verify ZIP integrity and exact contents.

## Behavior evidence

- [ ] Record exact model/provider, host/version, Skill version, input, and observed result.
- [ ] Run task cases with and without ThinkAlong under comparable conditions.
- [ ] Run trigger cases separately and record false positives and false negatives.
- [ ] Test each platform before describing it as tested.
- [ ] Publish only measured results and disclose limitations.

## GitHub discoverability

Suggested description:

> A portable Agent Skill for clearer AI collaboration: clarify intent, do useful work, and verify results—with less back-and-forth.

Suggested topics: `agent-skills`, `ai-agents`, `codex`, `claude`, `deepseek`, `chatgpt`, `prompt-engineering`, `open-source`.

Promote one real, reproducible before/after example. Do not invent user counts, benchmark scores, stars, or compatibility claims.

## Release assets

- [ ] Update CHANGELOG and tag the release.
- [ ] Attach the generated Skill ZIP and portable instructions.
- [ ] Confirm README does not imply that a release or remote CI run exists before it does.
