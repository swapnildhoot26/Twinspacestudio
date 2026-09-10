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
            ("services/", "0.9"), ("areas/", "0.8"), ("guides.html", "0.8"),
            ("guides/", "0.7"), ("projects/", "0.7")]
SKIP_DIRS = {".git", "assets", "node_modules", "scripts", "tools"}

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
    """Every .html file in the tree, so a new section needs no change here."""
    found = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
        for fn in filenames:
            if fn.endswith(".html"):
                found.append(os.path.relpath(os.path.join(dirpath, fn), ROOT))
    found = [f for f in found if os.path.basename(f) not in EXCLUDE]
    # index first, then by priority, then alphabetically
    return sorted(found, key=lambda f: (f != "index.html", priority_for(f) != "1.0",
                                        -float(priority_for(f)), f))

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
