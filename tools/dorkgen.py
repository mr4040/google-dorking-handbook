#!/usr/bin/env python3
"""dorkgen: generate Google dorks scoped to a domain you own or are authorized to assess.

This tool only BUILDS queries. It never contacts Google or the target.
Stdlib only, Python 3.8+.
"""
import argparse
import csv
import json
import re
import sys
import urllib.parse
from pathlib import Path

LIB_PATH = Path(__file__).resolve().parent.parent / "dorks" / "library.json"
DOMAIN_RE = re.compile(r"^(?=.{1,253}$)([a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}$")
RISK_ORDER = {"high": 0, "medium": 1, "low": 2}
REQUIRED = {"id", "category", "title", "template", "risk", "why", "fix"}


def load_library(path=LIB_PATH):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    dorks = data["dorks"]
    seen = set()
    for d in dorks:
        missing = REQUIRED - d.keys()
        if missing:
            raise ValueError(f"{d.get('id', '?')}: missing {sorted(missing)}")
        if d["id"] in seen:
            raise ValueError(f"duplicate id {d['id']}")
        seen.add(d["id"])
        if "{domain}" not in d["template"]:
            raise ValueError(f"{d['id']}: template must contain {{domain}}")
        if d["risk"] not in RISK_ORDER:
            raise ValueError(f"{d['id']}: invalid risk {d['risk']}")
    return dorks


def validate_domain(domain):
    domain = domain.strip().lower()
    if not DOMAIN_RE.match(domain):
        raise ValueError(f"invalid domain: {domain!r}")
    return domain


def render(dork, domain):
    return dork["template"].replace("{domain}", domain)


def search_url(query):
    return "https://www.google.com/search?" + urllib.parse.urlencode({"q": query})


def select(dorks, category=None, min_risk=None):
    out = dorks
    if category:
        out = [d for d in out if d["category"] == category]
    if min_risk:
        limit = RISK_ORDER[min_risk]
        out = [d for d in out if RISK_ORDER[d["risk"]] <= limit]
    return sorted(out, key=lambda d: (RISK_ORDER[d["risk"]], d["category"], d["id"]))


def fmt_text(items, domain):
    return "\n".join(f"[{d['risk'].upper():6}] {d['id']:<20} {render(d, domain)}" for d in items)


def fmt_md(items, domain):
    lines = [f"# Dork audit checklist: `{domain}`", ""]
    cat = None
    for d in items:
        if d["category"] != cat:
            cat = d["category"]
            lines += ["", f"## {cat}", ""]
        lines += [
            f"- [ ] **{d['title']}** ({d['risk']})",
            f"  - Query: `{render(d, domain)}`",
            f"  - Why: {d['why']}",
            f"  - Fix: {d['fix']}",
        ]
    return "\n".join(lines)


def fmt_urls(items, domain):
    return "\n".join(search_url(render(d, domain)) for d in items)


def fmt_csv(items, domain):
    import io
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["id", "category", "risk", "title", "query", "url", "status", "notes"])
    for d in items:
        q = render(d, domain)
        w.writerow([d["id"], d["category"], d["risk"], d["title"], q, search_url(q), "", ""])
    return buf.getvalue()


FORMATS = {"text": fmt_text, "md": fmt_md, "urls": fmt_urls, "csv": fmt_csv}


def build_parser():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list", help="list library entries")

    g = sub.add_parser("generate", help="render dorks for a domain")
    g.add_argument("-d", "--domain", required=True)
    g.add_argument("-c", "--category")
    g.add_argument("--min-risk", choices=list(RISK_ORDER))
    g.add_argument("-f", "--format", choices=list(FORMATS), default="text")
    g.add_argument("--authorized", action="store_true",
                   help="confirm you own the domain or have written authorization to assess it")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    dorks = load_library()

    if args.cmd == "list":
        for d in select(dorks):
            print(f"{d['risk']:<6} {d['category']:<18} {d['id']:<20} {d['title']}")
        return 0

    if not args.authorized:
        print("Refusing: pass --authorized to confirm you own this domain or have written permission.\n"
              "See ETHICS.md.", file=sys.stderr)
        return 2
    try:
        domain = validate_domain(args.domain)
    except ValueError as e:
        print(e, file=sys.stderr)
        return 2

    items = select(dorks, args.category, args.min_risk)
    if not items:
        print("No dorks matched.", file=sys.stderr)
        return 1
    print(FORMATS[args.format](items, domain))
    return 0


if __name__ == "__main__":
    sys.exit(main())
