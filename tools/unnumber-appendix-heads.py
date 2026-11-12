#!/usr/bin/env python3
"""Mark every ## and ### heading in an appendix file {-} so it carries no
section number (an unnumbered chapter's sections otherwise inherit the last
numbered chapter's counter). Idempotent. Usage: FILE..."""
import re, sys, pathlib
for path in sys.argv[1:]:
    p = pathlib.Path(path); lines = p.read_text(encoding="utf-8").split("\n")
    out, inside, n = [], False, 0
    for line in lines:
        if line.startswith("```"): inside = not inside
        if not inside and re.match(r"^#{2,3} ", line) and not re.search(r"\{[^}]*(-|\.unnumbered)[^}]*\}\s*$", line):
            line = line.rstrip() + " {-}"; n += 1
        out.append(line)
    if n: p.write_text("\n".join(out), encoding="utf-8")
    print(f"{path}: {n} heading(s) marked")
