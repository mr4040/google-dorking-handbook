# 02 · Methodology

Dorking without structure produces noise. Treat it like any other collection discipline.

## 1. Define scope
- Domains, subdomains, brand names, product names, known IP ranges
- Written authorization and out-of-scope list
- A reporting contact on the owner's side

## 2. Build a hypothesis
Examples:
- "Staging environments are indexed."
- "Employees uploaded internal spreadsheets to public paths."
- "Third parties are pasting our domain next to secrets."

## 3. Start broad, narrow fast
```
site:example.com                      # baseline index size
site:example.com ext:pdf              # by type
site:example.com ext:pdf after:2026-01-01
site:example.com ext:pdf intext:"internal"
```

## 4. Record everything
For each finding keep: **dork, timestamp, URL, why it matters, severity, redacted evidence**. Use `templates/audit-report.md`.

## 5. Pivot
- Subdomain found → dork it separately
- Technology fingerprint (`Powered by X`) → check version advisories
- Username/email pattern → check breach exposure via official services (e.g. HIBP) for *your own* org
- Cloud storage hostname → verify bucket permissions with the provider's own tooling, from your own account

## 6. Verify without exploiting
Open the result. Confirm what it is. Stop. Never authenticate with discovered credentials.

## 7. Report, fix, re-test
After remediation, re-run the dork **and** request re-indexing/removal (see `06-remediation.md`).

## Mapping to frameworks
- OWASP WSTG-INFO-01: Search Engine Discovery
- MITRE ATT&CK T1593.002 (Search Engines), T1594 (Search Victim-Owned Websites)
- PTES: Intelligence Gathering
