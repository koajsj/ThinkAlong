# Public Release Checklist

## Repository quality

- [ ] English and Simplified Chinese READMEs agree on features, installation scope, and limitations.
- [ ] License, changelog, contribution/security guidance, issue templates, and CI are present.
- [ ] No secrets, private data, local machine paths, or unrelated generated files are included.
- [ ] Run static validator and inspect source syntax, metadata, references and package structure.
- [ ] Keep test code/cases and unit/runtime/behavior/model runs absent under the current static-only policy.
- [ ] Verify ZIP integrity and exact package contents.
- [ ] Confirm the ZIP matches the six shared package entries and source bytes; keep `dist/` and temporary outputs out of Git.
- [ ] Inspect the actual remote Actions run before describing CI as passing.

For a source-only push, inspect repository identity, current remote head, changed paths and deletions; retain existing history and avoid force-push. Verify the remote commit/tree after pushing. A source push does not authorize tags, Release creation, repository-setting changes or asset uploads.

## Behavior evidence — not run under the current policy

The [retained protocol](../evals/protocol.md) and [rubric](../evals/scoring-rubric.md) describe future evidence requirements. They do not authorize evaluation. Do not execute them or incur model charges unless separately authorized.

- [ ] Label behavior, activation, model benchmarks and host installation as unrun in this iteration.
- [ ] Do not claim improvement or tested compatibility from static checks.
- [ ] If the policy changes later, record actual controlled results and host evidence before changing these claims.

## GitHub discoverability

Copy-ready About description and Topics are maintained in [github-metadata.md](github-metadata.md). Set them in the repository's About settings; repository file edits do not change GitHub's About metadata.

Promote one real, reproducible before/after example. Do not invent user counts, benchmark scores, stars, or compatibility claims.

## Release assets

- [ ] Update CHANGELOG and tag the release.
- [ ] Attach the generated Skill ZIP and portable instructions.
- [ ] Ensure folder installations and the ZIP carry the repository MIT LICENSE; keep research, methodology and tooling outside the runtime package.
- [ ] Confirm README does not imply that a release or remote CI run exists before it does.
