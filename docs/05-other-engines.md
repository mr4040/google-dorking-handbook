# 05 · Beyond Google

Different engines index different content. Cover several.

| Engine | Useful operators | Notes |
|---|---|---|
| **Bing** | `site:`, `inurl:`, `intitle:`, `filetype:`, `ip:`, `linkfromdomain:` | `ip:` lists sites sharing an IP |
| **DuckDuckGo** | `site:`, `inurl:`, `intitle:`, `filetype:` | Fewer operators; bangs (`!g`) |
| **Yandex** | `site:`, `inurl:`, `title:`, `mime:`, `host:` | Strong on some Eastern European content |
| **Brave Search** | `site:`, `inurl:`, `intitle:`, `filetype:` | Independent index |

## Device and service search (not dorking, same mindset)
- **Shodan**: `hostname:example.com`, `ssl.cert.subject.cn:example.com`
- **Censys**: `services.tls.certificates.leaf_data.subject.common_name: example.com`
- **FOFA / ZoomEye**: similar certificate/hostname pivots
- **crt.sh**: certificate transparency for subdomain discovery
- **Wayback Machine**: historical versions of pages you thought were removed
- **GitHub code search**: `org:yourorg password`, or `"yourcompany.com" filename:.env`

Run these for **your own** assets or authorized scope only.
