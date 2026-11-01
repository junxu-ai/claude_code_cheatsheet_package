---
name: fix-issue
description: Reproduce and fix a specific tracked software bug using a regression test and a minimal patch.
disable-model-invocation: true
allowed-tools: Read Grep Glob Bash Edit
---

Task/issue: $ARGUMENTS

1. Identify the behavior, existing tests and observable failure.
2. Reproduce the problem; preserve the failing test output.
3. Trace to the smallest responsible function, data path and state transition.
4. Add a regression test that fails for the right reason before changing the implementation.
5. Implement the smallest safe fix; keep existing API and data contracts stable.
6. Run relevant tests, lint, type checks and a final diff review.
7. Report: root cause, files changed, command results, residual risks and rollback procedure.

Do not silently modify authentication, authorization, data retention or deployment controls.
A skill is advisory; required restrictions must be implemented separately with permissions/hooks.
