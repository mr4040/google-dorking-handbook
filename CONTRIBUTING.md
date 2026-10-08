# Contributing

## Adding a dork to `dorks/library.json`

Each entry needs:

```json
{
  "id": "unique-kebab-id",
  "category": "exposed-files",
  "title": "Short description",
  "template": "site:{domain} ext:bak",
  "risk": "low | medium | high",
  "why": "What exposure this detects",
  "fix": "How owners remediate it"
}
```

Rules:
- Template must be scoped with `{domain}` (no hardcoded third parties).
- Must have a defensive purpose and a `fix`.
- Run `python3 -m unittest discover tests` before opening a PR.

## Docs
Keep it practical. Prefer examples over theory, and cite sources when making claims about operator behavior (Google changes it often).
