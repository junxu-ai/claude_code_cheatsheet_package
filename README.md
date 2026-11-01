# Claude Code - Practical Engineering Cheatsheet

Research snapshot: **2026-11-01**. Two-column A4 reference distilled from the user-provided `Claude Code Ultimate Reference and Engineering Cheatsheet` and cross-checked against Anthropic's official Claude Code documentation.

## Contents

- `claude_code_cheatsheet.pdf` - compiled two-column PDF, searchable with hyperlinks to official references.
- `claude_code_cheatsheet.tex` - complete editable LaTeX source (XeLaTeX).
- `references.md` - source list and verification notes.
- `examples/` - editable example `CLAUDE.md`, path rules, custom skill, restricted review agent, settings and a tested blocking hook.

## Compile

On a LaTeX installation with `xelatex`, `fontspec`, `extarticle`, `multicol`, `hyperref`, `listings`, `tabularx`, `microtype` and the standard TeX Live package collection:

```sh
xelatex -interaction=nonstopmode -halt-on-error claude_code_cheatsheet.tex
xelatex -interaction=nonstopmode -halt-on-error claude_code_cheatsheet.tex
```

The document uses the open fonts **Arimo** and **DejaVu Sans Mono**. If missing, change the `\setmainfont`/`\setmonofont` lines to locally available fonts.

## Adopting examples

Copy selected files inside `examples/.claude/` into your **own** repository, after adapting the commands and policy. Example allow rules mention `pnpm`; omit these unless your repo really uses pnpm.

The `PreToolUse` hook only checks edits through Claude's `Edit` and `Write` tools; it does **not** cover mutations made by Bash scripts, arbitrary MCP tools, or other processes. Combine with sandbox, managed settings, filesystem permissions, credential isolation and CI controls.

Run the included smoke test:

```sh
python3 examples/test_hook.py
```

## Key corrections to the reference material

- `--allowedTools` **pre-approves** listed tools. `--tools` restricts the built-in tool set; deny rules, OS sandboxing and MCP restrictions are additional controls.
- `CLAUDE.md` and skills are **non-deterministic instructions**; permission rules and lifecycle hooks are enforceable **runtime** controls.
- `auto` is a classifier-based permission mode; `default` is labeled Manual, and new interactive session startup defaults may vary by plan/provider/version.
- The npm installer now distributes the same native binary as the standalone installer.
- Availability and behavior of commands/shortcuts can vary by release and environment. Re-check `/help` and the official documentation.

The package is a practical reference, **not** an audited enterprise security baseline; validate all examples in your environment before production use.
