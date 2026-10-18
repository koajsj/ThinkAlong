# Public Release Checklist

## Repository quality

- [ ] English and Simplified Chinese READMEs agree on features, installation scope, and limitations.
- [ ] License, changelog, contribution/security guidance, issue templates, and CI are present.
- [ ] No secrets, private data, local machine paths, or unrelated generated files are included.
- [ ] Run validator, unit tests, and package script.
- [ ] Verify ZIP integrity and exact package contents.
- [ ] Inspect the actual remote Actions run before describing CI as passing.

## Behavior evidence

- [ ] Record model/provider, host/version, Skill version, input, and observed result.
- [ ] Run task cases with and without ThinkAlong under comparable conditions.
- [ ] Run trigger cases separately; record false positives and false negatives.
- [ ] Test each platform before describing it as tested.
- [ ] Publish only measured results and disclose limitations.

## GitHub discoverability

Copy-ready About description and Topics are maintained in [github-metadata.md](github-metadata.md). Set them in the repository's About settings; repository file edits do not change GitHub's About metadata.

Promote one real, reproducible before/after example. Do not invent user counts, benchmark scores, stars, or compatibility claims.

## Release assets

- [ ] Update CHANGELOG and tag the release.
- [ ] Attach the generated Skill ZIP and portable instructions.
- [ ] Confirm README does not imply that a release or remote CI run exists before it does.
