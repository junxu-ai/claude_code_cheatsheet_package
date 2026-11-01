# Research references - Claude Code, checked 2026-11-01

Primary source: the user-supplied pasted document **Claude Code Ultimate Reference and Engineering Cheatsheet** (~31.6 KB), used as the starting point. The original upload is **not** redistributed in this package; its information is synthesized and checked below.

## Official Anthropic references

1. Best practices: https://code.claude.com/docs/en/best-practices
2. Overview: https://code.claude.com/docs/en/overview
3. Advanced setup: https://code.claude.com/docs/en/setup
4. CLI: https://code.claude.com/docs/en/cli-reference
5. Slash commands: https://code.claude.com/docs/en/commands
6. Skills: https://code.claude.com/docs/en/skills
7. Permissions: https://code.claude.com/docs/en/permissions
8. Interactive shortcuts: https://code.claude.com/docs/en/interactive-mode
9. Prompt library: https://code.claude.com/docs/en/prompt-library
10. Memory and rules: https://code.claude.com/docs/en/memory
11. Subagents: https://code.claude.com/docs/en/sub-agents
12. Hooks reference: https://code.claude.com/docs/en/hooks
13. Hook examples: https://code.claude.com/docs/en/hooks-guide
14. Sandbox: https://code.claude.com/docs/en/sandboxing
15. MCP: https://code.claude.com/docs/en/mcp
16. Plugins: https://code.claude.com/docs/en/plugins
17. Costs: https://code.claude.com/docs/en/costs
18. GitHub Actions: https://code.claude.com/docs/en/github-actions
19. Agent teams: https://code.claude.com/docs/en/agent-teams
20. Security: https://code.claude.com/docs/en/security

## Research synthesis and feature corrections

- Official CLI docs distinguish `--allowedTools` (permission pre-approval), `--tools` (available built-in tool restriction), and `--disallowedTools` (denials including MCP). Verified against CLI reference.
- The official setup guide states that the npm distribution installs the same native Claude Code binary as the standalone installer. Verified against advanced setup.
- The best-practices guidance recommends short CLAUDE.md instructions, path-specific rules, skills for procedures, executable test feedback and deterministic hooks/permissions for mandatory restrictions. Verified against official best practices/memory/skills.
- `PreToolUse` command hooks receive JSON on stdin and can return exit code 2 with a stderr reason to block. Verified against official hook guide.
- Some command names and features vary by version, plan or deployment, so this cheatsheet avoids asserting exact active model IDs or universal defaults.

## Note on examples

The configuration snippets are illustrative, not executed by Claude Code in this environment. The Python blocking hook was tested locally against six representative events; integration testing with Claude Code and your repository policy is still required.
