# 06 · Remediation & De-indexing

Finding an exposure is half the job. Fix the source, then clean the index.

## 1. Fix the root cause
| Finding | Fix |
|---|---|
| Directory listing | Disable autoindex (`Options -Indexes` Apache, `autoindex off;` nginx) |
| `.git` / `.env` exposed | Block dotfiles at the web server; never deploy repo dirs to webroot |
| Backups / dumps | Remove from webroot; store off-box; add CI check for stray `*.bak`, `*.sql` |
| Secrets in config | Rotate immediately; use a secrets manager |
| Admin panels | Restrict by IP/VPN/SSO; add MFA |
| Staging indexed | Put behind auth. `noindex` alone is *not* access control |
| Verbose errors | Disable debug mode in production; use generic error pages |
| Sensitive docs | Remove, move behind auth, rotate links |
| Metadata leaks | Strip with `exiftool -all= file`, or export without metadata |
| Open cloud storage | Block public access at account level; audit bucket policies/ACLs |

## 2. Prevent re-indexing
- `X-Robots-Tag: noindex, nofollow` header (works for non-HTML such as PDFs)
- `<meta name="robots" content="noindex">` for HTML
- **robots.txt does not secure anything** and can advertise sensitive paths. Don't list secrets there.

## 3. Remove from Google
- **Search Console → Removals** (verified owners): temporary hide (~6 months) plus cache clear
- Return **404/410** so the URL drops permanently
- For content on sites you don't own: Google's "Remove personal or sensitive info" request forms

## 4. Verify
Re-run the original dork after a few days. Keep the before/after in your report.

## 5. Add guardrails
- Pre-deploy CI check for risky file types in build artifacts
- Secret scanning (gitleaks, trufflehog) on repos
- Scheduled quarterly dork audit using this repo
