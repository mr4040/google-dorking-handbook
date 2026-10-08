# 03 · Defensive Self-Audit

A one-hour exposure review for a domain you own.

## Prep
- Private/incognito browser, logged out of Google
- `python3 tools/dorkgen.py generate -d yourdomain.tld --authorized -f md > audit-checklist.md`
- Copy `templates/audit-report.md`

## Checklist (work top-down by risk)

### 🔴 High
- [ ] Directory listings (`intitle:"index of"`)
- [ ] Exposed `.git`, `.env`, `.svn`
- [ ] Database dumps and backups (`ext:sql`, `ext:bak`)
- [ ] Config files with secret-like keys
- [ ] Documents marked confidential/internal
- [ ] Spreadsheets/CSVs with personal data

### 🟠 Medium
- [ ] Admin/login panels indexed
- [ ] Staging/dev/UAT hosts indexed
- [ ] Verbose error pages and stack traces
- [ ] `phpinfo()` pages
- [ ] API docs (Swagger/OpenAPI) not meant to be public
- [ ] DevOps dashboards (Jenkins, Grafana, Kibana)

### 🟡 Low / informational
- [ ] Subdomain inventory vs. your CMDB (find the ones you forgot)
- [ ] Document metadata (author names, internal paths, software versions)
- [ ] Log files

### 🌐 Off-site
- [ ] Your domain on paste sites
- [ ] Your domain/keys in public code repos
- [ ] Public cloud storage naming your org
- [ ] Public project-management boards (Trello, Jira) mentioning you

## Triage
| Severity | Criteria | SLA suggestion |
|---|---|---|
| Critical | Live credentials, PII, DB dumps | Hours; rotate secrets immediately |
| High | Internal docs, admin interfaces, source code | 1-3 days |
| Medium | Info disclosure aiding attackers | 2 weeks |
| Low | Metadata, banners | Next cycle |

**If credentials are exposed: rotate first, investigate second.** Assume they were already harvested.
