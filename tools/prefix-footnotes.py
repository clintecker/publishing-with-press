#!/usr/bin/env python3
"""Prefix every footnote label in a chapter/appendix file with its chapter
number (NN- from the filename, or the letter for an appendix), so labels
are unique across the merged book. Idempotent. Usage: FILE..."""
import re, sys, pathlib
for path in sys.argv[1:]:
    p = pathlib.Path(path); name = p.name
    m = re.match(r"^(\d+)-", name); pref = str(int(m.group(1))) if m else name[0]
    text = p.read_text(encoding="utf-8")
    def fix(mo):
        label = mo.group(1)
        if re.match(rf"^{re.escape(pref)}-", label): return mo.group(0)
        return mo.group(0).replace(f"[^{label}]", f"[^{pref}-{label}]")
    new = re.sub(r"\[\^([^\]\s]+)\]", fix, text)
    changed = sum(1 for a, b in zip(text.split("[^"), new.split("[^")) if a != b)
    if new != text: p.write_text(new, encoding="utf-8")
    print(f"{path}: {'changed' if new != text else 'unchanged'} (prefix {pref}-)")
