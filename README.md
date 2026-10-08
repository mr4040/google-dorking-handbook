# 🔍 Google Dorking Handbook

> A practical, defense-first guide to advanced Google search operators for **OSINT, threat hunting, and attack-surface auditing**, with a small stdlib-only CLI to generate dorks scoped to domains **you own or are authorized to assess**.

![license](https://img.shields.io/badge/license-MIT-blue) ![python](https://img.shields.io/badge/python-3.8%2B-green) ![use](https://img.shields.io/badge/use-authorized%20only-red)

## Why this exists

Search engines index what servers expose, not what owners *intend* to expose. Misconfigured buckets, forgotten backups, staging sites, and leaked docs are routinely discoverable with nothing but a search box. Attackers know it. Defenders should check first.

This repo treats dorking as a **detection and hygiene** discipline:

1. Learn the operators (`docs/01-operators.md`)
2. Apply a repeatable methodology (`docs/02-methodology.md`)
3. Audit your own exposure (`docs/03-defensive-self-audit.md`)
4. Fix and verify (`docs/06-remediation.md`)

## ⚠️ Scope & ethics

Use this only against assets you own or have **written authorization** to test. Viewing a publicly indexed result is generally lawful in many jurisdictions, but accessing, downloading, or using exposed credentials/data is not. Read [`ETHICS.md`](ETHICS.md) before anything else. If you find someone else's exposure, report it responsibly.

## Repo layout

```
.
├── docs/
│   ├── 01-operators.md             # operator reference + gotchas
│   ├── 02-methodology.md           # how to dork systematically
│   ├── 03-defensive-self-audit.md  # step-by-step exposure audit
│   ├── 04-osint-use-cases.md       # threat intel / brand / leak monitoring
│   ├── 05-other-engines.md         # Bing, DuckDuckGo, Yandex, Shodan/Censys pivots
│   └── 06-remediation.md           # fixing + de-indexing
├── dorks/library.json              # curated, templated dork library ({domain})
├── tools/dorkgen.py                # generator: text / markdown / csv / URLs
├── templates/audit-report.md       # reporting template
├── tests/test_dorkgen.py
└── .github/workflows/ci.yml
```

## Quick start

```bash
git clone https://github.com/<you>/google-dorking-handbook.git
cd google-dorking-handbook

# Browse the library
python3 tools/dorkgen.py list

# Generate dorks for a domain you own (explicit confirmation required)
python3 tools/dorkgen.py generate --domain example.com --authorized

# Only one category, as a markdown checklist
python3 tools/dorkgen.py generate -d example.com --authorized -c exposed-files -f md

# Clickable search URLs (you run them manually, no scraping)
python3 tools/dorkgen.py generate -d example.com --authorized -f urls
```

The tool **never queries Google**. Automated scraping violates Google's ToS and gets you CAPTCHA'd or blocked. It builds queries; you run them by hand, or via the official [Programmable Search / Custom Search JSON API](https://developers.google.com/custom-search/v1/overview) if you need automation.

## Operator cheat sheet

| Operator | Purpose | Example |
|---|---|---|
| `site:` | Restrict to domain/TLD | `site:example.com` |
| `inurl:` | Term in URL | `inurl:admin` |
| `intitle:` | Term in page title | `intitle:"index of"` |
| `intext:` | Term in body | `intext:"internal use only"` |
| `filetype:` / `ext:` | File extension | `ext:sql` |
| `"..."` | Exact phrase | `"confidential"` |
| `-` | Exclude | `-www` |
| `OR` / `\|` | Boolean OR | `ext:bak OR ext:old` |
| `*` | Wildcard word | `"password is *"` |
| `before:` / `after:` | Date range | `after:2025-01-01` |
| `AROUND(n)` | Proximity | `admin AROUND(3) password` |

Full details and deprecated operators (`cache:`, `link:`, `related:`) in [`docs/01-operators.md`](docs/01-operators.md).

## Contributing

PRs welcome: new defensive dorks, other-engine equivalents, remediation guidance. See [`CONTRIBUTING.md`](CONTRIBUTING.md). Dorks that target specific third parties, or that are only useful for locating credentials of unknown victims, will be declined.

## References

- Exploit-DB Google Hacking Database (GHDB)
- OWASP Web Security Testing Guide, *Conduct Search Engine Discovery Reconnaissance for Information Leakage* (WSTG-INFO-01)
- MITRE ATT&CK: T1593 (Search Open Websites/Domains), T1596 (Search Open Technical Databases)

## License

MIT, see [`LICENSE`](LICENSE).
