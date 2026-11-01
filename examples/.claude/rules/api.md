---
paths:
  - "src/api/**/*.ts"
  - "src/api/**/*.tsx"
---

# API rules
- Validate inputs at trust boundaries.
- Maintain backward-compatible contract behavior unless an API version increment is approved.
- Write unit and contract tests for new endpoints.
- Do not log bearer tokens, secrets or personal data.
