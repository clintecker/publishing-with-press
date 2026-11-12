#!/usr/bin/env python3
"""ste-ratchet: the book's structural prose gate, built on tools/ste_check.py.

It runs the vendored STE80 linter over the manuscript with the prose
contract's thresholds (docs/prose-contract.md) and compares the per-file
counts with tools/ste-baseline.json. A file whose count rises fails the
run. The count may only fall.

    python3 tools/ste-ratchet.py            # gate: exit 1 if any file rose
    python3 tools/ste-ratchet.py --report   # list every finding
    python3 tools/ste-ratchet.py --update   # write the baseline from the tree
    python3 tools/ste-ratchet.py --update --ref <commit>   # ... from a commit

What the contract relaxes, this wrapper drops before counting:
- HTML comments (the art briefs are not prose)
- "however", "therefore", "whether" (period-correct, kept by the contract)
- "verify", "landscape", "enhance" (press's own command names and a page
  orientation), and "identical"
- the sentence cap is 30 words, the contract's hard ceiling, not STE's 25
- an "-ing" word in title case (a chapter title in a cross-reference)
- image lines, and anything inside double quotes (a quotation is verbatim)
- footnote markers, which otherwise glue a sentence to the next
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import ste_check  # noqa: E402  (vendored, MIT; see THIRD_PARTY_NOTICES.md)

BASELINE = HERE / "ste-baseline.json"
FILES = sorted((ROOT / "book" / "chapters").glob("*.md")) + sorted(
    (ROOT / "book" / "appendices").glob("*.md")
)
ALLOWED_WORDS = {"however", "therefore", "whether", "verify", "landscape",
                 "enhance", "identical"}
HARD_CEILING = 30


def prose_only(text: str) -> str:
    """Drop what the contract does not count as the book's own prose."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)       # art briefs
    text = re.sub(r"^!\[.*$", "", text, flags=re.M)           # image lines
    text = re.sub(r"^>[ \t]?", "", text, flags=re.M)          # unwrap sidebars
    text = re.sub(r'"[^"\n]*"', "QUOTE", text)                # quotations
    text = re.sub(r"\[\^[^\]]+\]", "", text)                  # footnote markers
    return text


def keep(f: ste_check.Finding) -> bool:
    if f.rule == "word":
        word = re.match(r"'([^']+)'", f.message)
        return not (word and word.group(1) in ALLOWED_WORDS)
    if f.rule == "sentence-length":
        return int(f.message.split()[0]) > HARD_CEILING
    if f.rule == "ing-form":
        word = re.findall(r"'([^']+)'", f.message)[-1]
        return not word[:1].isupper()
    return True


def read_source(path: Path, ref: str | None) -> str:
    if ref is None:
        return path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT).as_posix()
    return subprocess.run(["git", "-C", str(ROOT), "show", f"{ref}:{rel}"],
                          check=True, capture_output=True, text=True).stdout


def findings_for(path: Path, ref: str | None = None) -> list[ste_check.Finding]:
    text = prose_only(read_source(path, ref))
    return [f for f in ste_check.check(text, strict=False) if keep(f)]


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--report", action="store_true", help="print every finding")
    ap.add_argument("--update", action="store_true", help="rewrite the baseline")
    ap.add_argument("--ref", help="with --update: measure this git commit, not the tree")
    args = ap.parse_args(argv)
    if args.ref and not args.update:
        ap.error("--ref needs --update")

    counts: dict[str, int] = {}
    total = 0
    for path in FILES:
        rel = str(path.relative_to(ROOT))
        found = findings_for(path, args.ref)
        counts[rel] = len(found)
        total += len(found)
        if args.report:
            print(f"{rel}: {len(found)}")
            for f in found:
                print(f"  {f.line:>4}  {f.rule:<16} {f.message}  | {f.excerpt[:70]}")

    if args.update:
        BASELINE.write_text(json.dumps(counts, indent=2) + "\n", encoding="utf-8")
        print(f"baseline written: {total} findings in {len(counts)} files")
        return 0

    if not BASELINE.exists():
        print("no baseline; run with --update first", file=sys.stderr)
        return 2
    base = json.loads(BASELINE.read_text(encoding="utf-8"))
    rose = {k: (base.get(k), v) for k, v in counts.items() if v > base.get(k, 0)}
    fell = sum(1 for k, v in counts.items() if v < base.get(k, 0))
    print(f"ste-ratchet: {total} findings (baseline {sum(base.values())})")
    for k, (b, v) in sorted(rose.items()):
        print(f"  ROSE {k}: {b} -> {v}")
    if fell and not rose:
        print(f"  {fell} file(s) fell below baseline; run --update to lower it")
    return 1 if rose else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
