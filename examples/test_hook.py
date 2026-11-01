"""Simple offline smoke tests: python3 test_hook.py (no Claude installation needed)."""
import json
import subprocess
import sys
from pathlib import Path

script = Path(__file__).parent / '.claude/hooks/block_protected.py'
checks = [
    ('Edit', 'src/app.py', 0),
    ('Write', 'src/api/test.ts', 0),
    ('Edit', '.env', 2),
    ('Write', 'secrets/tokens.txt', 2),
    ('Edit', '.git/config', 2),
    ('Read', '.env', 0), # hook does NOT protect Reads: use deny rules
    ('Write', '', 2),
]
for tool, path, expected in checks:
    event = {'tool_name': tool, 'tool_input': {'file_path': path}}
    proc = subprocess.run([sys.executable, str(script)], input=json.dumps(event),
                          text=True, capture_output=True)
    assert proc.returncode == expected, (tool, path, proc.returncode, proc.stderr)
print(f'{len(checks)} hook smoke tests passed')
