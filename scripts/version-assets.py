#!/usr/bin/env python3
"""Stamp styles.css and app.js references with a content hash.

Static assets are served with a one-year immutable cache. Fonts and images are
safe under that because their filenames never change meaning, but the CSS and JS
do change, so their references carry ?v=<hash> and a new build busts the cache.
"""
import hashlib, glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGETS = {"assets/css/styles.css": "css", "assets/js/app.js": "js"}

def digest(rel):
    with open(os.path.join(ROOT, rel), "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()[:10]

def main():
    hashes = {rel: digest(rel) for rel in TARGETS if os.path.exists(os.path.join(ROOT, rel))}
    pages = ["index.html", "areas-we-serve.html", "404.html"]
    for d in ("services", "areas", "projects"):
        pages += [os.path.relpath(p, ROOT) for p in sorted(glob.glob(os.path.join(ROOT, d, "*.html")))]
    changed = 0
    for page in pages:
        path = os.path.join(ROOT, page)
        if not os.path.exists(path):
            continue
        src = open(path, encoding="utf-8").read()
        new = src
        for rel, h in hashes.items():
            name = os.path.basename(rel)
            # match the reference with or without an existing ?v=
            new = re.sub(r'(["\'])((?:/|\.\./)?[^"\']*?%s)(?:\?v=[0-9a-f]+)?\1' % re.escape(name),
                         lambda m: '%s%s?v=%s%s' % (m.group(1), m.group(2), h, m.group(1)), new)
        if new != src:
            open(path, "w", encoding="utf-8").write(new)
            changed += 1
    print("versioned %d pages (%s)" % (changed, ", ".join("%s=%s" % (os.path.basename(k), v) for k, v in hashes.items())))
    return 0

if __name__ == "__main__":
    sys.exit(main())
