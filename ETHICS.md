# Ethics & Legal Use

Google dorking is passive reconnaissance: you query an index, not the target. But what you do with results matters.

## Rules of engagement

1. **Authorization first.** Only run target-specific dorks against domains you own or have written permission to assess (scope letter, bug bounty policy, internal engagement).
2. **Look, don't touch.** Confirming that something is exposed is enough. Do not log in with found credentials, download bulk data, or pivot into systems.
3. **Minimize data handling.** If you see PII or secrets, don't copy them. Record the URL, the dork, a timestamp, and a redacted screenshot.
4. **Report responsibly.** Check for `/.well-known/security.txt`, a bug bounty page, or a CERT contact. Give owners reasonable time to fix.
5. **Respect laws.** CFAA (US), Computer Misuse Act (UK), and equivalents elsewhere can apply to access beyond viewing public results. When unsure, stop and ask counsel.
6. **No scraping Google.** It violates their Terms of Service. Use the official API for automation.

## Not in scope for this repo

- Lists targeting specific companies or individuals
- Dorks whose only purpose is harvesting credentials, cards, or personal data of unknown victims
- Anything intended to facilitate unauthorized access
