#!/usr/bin/env python3
"""Demonstration PreToolUse hook; read JSON tool input from stdin.

This is an Edit/Write safeguard, not comprehensive filesystem protection:
Bash, MCP tools and external scripts need independent controls.
"""
import json
import sys
from pathlib import Path


def denied(path_string: str) -> bool:
    if not path_string:
        return False
    path = Path(path_string).expanduser().resolve(strict=False)
    parts = path.parts
    name = path.name.lower()
    sensitive_names = {'.env', '.env.local', 'credentials.json', 'secrets.json'}
    # pathlib handles path normalization; clear trusted policy boundaries.
    return (
        name in sensitive_names
        or name.startswith('.env.')
        or '.git' in parts
        or 'secrets' in parts
    )


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except (ValueError, UnicodeDecodeError):
        # Fail closed for this protected Edit/Write hook on bad input.
        print('Blocked: invalid JSON hook input', file=sys.stderr)
        return 2
    tool_name = event.get('tool_name', '')
    if tool_name not in {'Edit', 'Write'}:
        return 0
    target = event.get('tool_input', {}).get('file_path', '')
    if not isinstance(target, str) or not target:
        print('Blocked: missing file_path for an Edit/Write action', file=sys.stderr)
        return 2
    if denied(target):
        print(f'Blocked: protected path {target!r}', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    sys.exit(main())
