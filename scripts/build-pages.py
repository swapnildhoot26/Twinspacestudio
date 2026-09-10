#!/usr/bin/env python3
"""Generate the area and guide pages from their content modules."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pagegen import write  # noqa: E402

MODULES = [
    "content_areas_a", "content_areas_b", "content_areas_c",
    "content_areas_d", "content_areas_e",
    "content_guides_a", "content_guides_b", "content_guides_c",
]


def main():
    total = 0
    for name in MODULES:
        try:
            mod = __import__(name)
        except ImportError:
            print(f"  (skipping {name} — not present yet)")
            continue
        for page in mod.PAGES:
            path, words = write(page)
            rel = os.path.relpath(path, os.path.dirname(os.path.dirname(path)))
            print(f"  {rel:<44} {words:>5} words")
            total += 1
    print(f"\n{total} pages written")


if __name__ == "__main__":
    main()
