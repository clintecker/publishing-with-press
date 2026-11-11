#!/usr/bin/env python3
"""Ensure one blank line between an image line and the art: comment that
follows it; pandoc makes a figure only of an image alone in its paragraph.
Usage: tools/space-art-comments.py FILE..."""
import re, sys
for path in sys.argv[1:]:
    lines = open(path, encoding="utf-8").read().split("\n")
    out, n = [], 0
    for i, line in enumerate(lines):
        out.append(line)
        if re.match(r"^!\[", line) and i + 1 < len(lines) and lines[i+1].lstrip().startswith("<!--"):
            out.append(""); n += 1
    if n: open(path, "w", encoding="utf-8").write("\n".join(out))
    print(f"{path}: {n} blank line(s) inserted")
