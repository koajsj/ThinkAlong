# Contributing to ThinkAlong

Thanks for helping make AI collaboration more useful and less frustrating.

## Useful contributions

- Reproducible cases where the Skill asks an unnecessary question or misses a necessary one.
- False activations or missed activations, with the exact prompt and host/model.
- Cases where it misunderstands requirements, skips useful work, or overstates verification.
- Platform installation issues and focused improvements with regression tests.

## Before opening a pull request

1. Explain the user problem.
2. Include exact input/context, expected behavior, observed behavior, and why the difference matters.
3. Add or update a case in `evals/task-cases.md` or `evals/trigger-cases.md`.
4. Run validation, unit tests, and the package script described in README.
5. Keep changes focused and avoid mandatory steps that do not fix a demonstrated failure.
6. Do not claim measured improvement without a recorded baseline comparison.

Keep English and Chinese documentation aligned. Do not add credentials, private conversations, or sensitive personal data to fixtures.
