# 01 · Operators Reference

Google changes operator behavior without notice. Test each operator before relying on it.

## Core operators

| Operator | Behavior | Notes |
|---|---|---|
| `site:` | Limits results to a domain, subdomain or TLD | `site:example.com`, `site:*.example.com`, `site:gov.tn` |
| `inurl:` | Term must appear in URL | Only the next term; use `allinurl:` for several |
| `intitle:` | Term in `<title>` | `intitle:"index of"` finds directory listings |
| `intext:` | Term in page body | Often noisy, combine with `site:` |
| `filetype:` / `ext:` | File extension | Aliases. Google indexes PDF, DOC(X), XLS(X), PPT(X), TXT, XML, CSV, and more, but not everything |
| `"phrase"` | Exact match | Also disables stemming and synonyms |
| `-term` | Exclude | `site:example.com -www` |
| `OR` / `\|` | Either term | `OR` must be uppercase |
| `*` | Wildcard for one or more words | `"default password is *"` |
| `( )` | Grouping | `site:example.com (ext:bak OR ext:old)` |
| `before:` / `after:` | Date filters | `after:2025-06-01` |
| `AROUND(n)` | Words within n of each other | `admin AROUND(4) password` |
| `define:` | Dictionary definition | Not for recon |

## Removed / unreliable

- `cache:` was retired by Google in 2024. Use the Wayback Machine (`web.archive.org`) or `archive.ph` instead.
- `link:` and `related:` are deprecated/unreliable. Use backlink tools or Bing's `linkfromdomain:`.
- `inanchor:` still works but results are inconsistent.

## Behavior gotchas

- **No space after the colon**: `site:example.com`, not `site: example.com`.
- **Result cap**: Google rarely returns more than a few hundred results per query. Split queries by filetype, path, or date to get deeper coverage.
- **Personalization**: use a private window or logged-out session for reproducible results.
- **Quoting**: unquoted terms may be treated loosely. Quote anything you need literally.
- **Rate limiting**: repeated queries trigger CAPTCHAs. Slow down; don't script it.
- **Indexing lag**: absence from results doesn't mean absence of exposure.

## Composition patterns

```
# Scope + type + signal
site:example.com ext:xlsx (confidential OR "internal use only")

# Exclude noise
site:example.com ext:log -inurl:blog -inurl:docs

# Subdomain discovery by elimination
site:*.example.com -www -site:blog.example.com

# Time-boxed recency
site:example.com ext:pdf after:2026-01-01
```
