# Example project instructions (adapt before adopting)

## Hard project facts
- Use the repository's locked toolchain and dependency versions.
- Preserve public API contracts unless a user-approved migration explicitly changes them.
- Business decisions must be implemented in deterministic code/rules and tested.

## Verification
- Run the repository's unit and integration test commands before claiming success.
- Present command outputs, changed file list, remaining risks and rollback notes.
- Do not deploy or push to protected branches without explicit authorization.

## Working procedure
- For high-impact changes, explore and plan first.
- Keep changes focused and review the final diff.
- Use .claude/skills/fix-issue/SKILL.md for repeatable defect resolution.
