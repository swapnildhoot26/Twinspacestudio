#!/usr/bin/env python3
"""Regenerate sitemap.xml with a real per-page <lastmod> taken from git history.

Google discounts <lastmod> when it cannot be trusted, so this uses the commit
date of each file rather than stamping everything with today's date. Pages are
discovered from the filesystem, so new pages are picked up automatically.

Run manually, or let .git/hooks/pre-commit run it (see scripts/install-hooks.sh).
"""
import os, re, subprocess, sys, glob
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://twinspacestudios.com"
EXCLUDE = {"404.html"}
PRIORITY = [("index.html", "1.0"), ("areas-we-serve.html", "0.9"),
            ("services/", "0.9"), ("areas/", "0.8"), ("projects/", "0.7")]

def url_for(rel):
    if rel == "index.html":
        return BASE + "/"
    return BASE + "/" + rel[:-5]            # cleanUrls: drop the .html

def priority_for(rel):
    for prefix, p in PRIORITY:
        if rel == prefix or rel.startswith(prefix):
            return p
    return "0.5"

def _staged():
    """Files staged in the commit being made. git log does not know about them yet,
    so they must be dated today rather than at their previous commit."""
    try:
        out = subprocess.run(["git", "diff", "--cached", "--name-only"],
                             cwd=ROOT, capture_output=True, text=True, timeout=20).stdout
        return set(out.split())
    except Exception:
        return set()

STAGED = _staged()
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")

def lastmod_for(rel):
    if rel in STAGED:
        return TODAY
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cI", "--", rel],
                             cwd=ROOT, capture_output=True, text=True, timeout=20).stdout.strip()
        if out:
            return out[:10]
    except Exception:
        pass
    ts = os.path.getmtime(os.path.join(ROOT, rel))   # fallback: file mtime
    return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%d")

def pages():
    found = []
    for rel in ["index.html", "areas-we-serve.html"]:
        if os.path.exists(os.path.join(ROOT, rel)):
            found.append(rel)
    for d in ("services", "areas", "projects"):
        for p in sorted(glob.glob(os.path.join(ROOT, d, "*.html"))):
            found.append(os.path.relpath(p, ROOT))
    return [f for f in found if os.path.basename(f) not in EXCLUDE]

def main():
    rows = []
    for rel in pages():
        rows.append('  <url><loc>%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>'
                    % (url_for(rel), lastmod_for(rel), priority_for(rel)))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    path = os.path.join(ROOT, "sitemap.xml")
    old = open(path).read() if os.path.exists(path) else ""
    if old != xml:
        open(path, "w").write(xml)
        print("sitemap.xml updated — %d URLs" % len(rows))
        return 1
    print("sitemap.xml already current — %d URLs" % len(rows))
    return 0

if __name__ == "__main__":
    changed = main()
    sys.exit(0)
