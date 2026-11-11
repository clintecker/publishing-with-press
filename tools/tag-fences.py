#!/usr/bin/env python3
"""Tag every untagged opening code fence as ```text (the book's rule: a
text fence prints black and wraps; an untagged one is verbatim and does
not). Usage: tools/tag-fences.py FILE..."""
import re, sys
for path in sys.argv[1:]:
    lines = open(path, encoding="utf-8").read().split("\n")
    out, inside, changed = [], False, 0
    for line in lines:
        m = re.match(r"^(\s*)```(.*)$", line)
        if m:
            if not inside:
                inside = True
                if m.group(2).strip() == "":
                    line = m.group(1) + "```text"; changed += 1
            else:
                inside = False
        out.append(line)
    if changed:
        open(path, "w", encoding="utf-8").write("\n".join(out))
    print(f"{path}: {changed} fence(s) tagged")
