# 04 · OSINT & Threat Hunting Use Cases

Operators are the same, the intent differs. All examples assume your own organization or an authorized engagement.

## Brand and leak monitoring
```
"yourcompany" "internal use only" -site:yourcompany.com
"@yourcompany.com" site:pastebin.com
"yourcompany.com" (password OR secret OR token) site:github.com
```
Set these up as recurring manual checks, or use Google Alerts for low-noise coverage.

## Phishing & impersonation hunting
```
intitle:"Your Company" (login OR "sign in") -site:yourcompany.com
"yourcompany" inurl:login -site:yourcompany.com
```
Feed lookalike domains to your takedown workflow and mail gateway blocklists.

## Third-party risk
```
site:vendor.com inurl:status
"yourcompany" site:vendor-portal.example
```
Vendors that leak *your* data are your problem too. Notify them through their security contact.

## Document metadata review
Download **your own** published PDFs/Office files and inspect them:
```bash
exiftool report.pdf        # author, software, internal paths
```
Strip metadata before publishing (see remediation).

## Subdomain & asset discovery (complements passive DNS)
```
site:*.example.com -www
```
Cross-check with certificate transparency (crt.sh), passive DNS, and your asset inventory. Anything indexed but not inventoried is a finding.

## Threat-hunting angle
- Track when new sensitive paths appear in the index (`after:`) after each release.
- Alert on your staging hostnames appearing in search results.
- Correlate index appearances with WAF/server logs for crawler activity (Googlebot UA + reverse DNS check) to confirm what was fetched and when.
