#!/usr/bin/env python3
"""Proof: the directory-tree archetype (style guide 5.2 #3), full measure.

The tree is the exact tree of a fresh `press new demo`; the three italic
annotations are joined to their entries by thin leader lines.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import look  # noqa: E402

# (depth, name, annotation-key)
TREE = [
    (0, "demo/", None),
    (1, ".claude/workflows/", "wf"),
    (2, "aesthetic-brief.js", None),
    (2, "art-direction.js", None),
    (2, "authorities-research.js", None),
    (2, "editorial-passes.js", None),
    (1, ".github/workflows/book.yml", None),
    (1, ".gitignore", None),
    (1, "book/chapters/00-preface.md", "pre"),
    (1, "CHANGELOG.md", None),
    (1, "CLAUDE.md", None),
    (1, "config/", None),
    (2, "front-matter.yaml", None),
    (2, "house-rules.yaml", None),
    (2, "metadata.yaml", "meta"),
    (1, "Makefile", None),
    (1, "requirements.txt", None),
]
NOTES = {
    "wf": "agent workflows, stamped with the press version",
    "pre": "one paragraph, so an empty book builds and verifies",
    "meta": "identity, press facts, and verification knobs",
}

SIZE = 8.0
row = 12.5
top, left = 14.0, 20.0
indent = 15.0
adv = look.mono_advance_pt(SIZE)
c = look.Canvas(top * 2 + row * len(TREE), "full")
ax_note = c.W - 20.0                      # annotations right-aligned here
trunk_x = {}                              # depth -> x of its trunk
ys = [top + row * i + row / 2 for i in range(len(TREE))]
for i, (d, name, key) in enumerate(TREE):
    tx = left + d * indent
    c.text(tx, ys[i], name, mono=True, size=SIZE, va="center")
    if d > 0:
        # horizontal stub from the parent's trunk to this name
        px = left + (d - 1) * indent + 3.0
        c.rule(px, ys[i], tx - 2.5, ys[i])
# vertical trunks: from each directory row down to its last child
for i, (d, name, key) in enumerate(TREE):
    kids = [j for j in range(i + 1, len(TREE))]
    last = None
    for j in kids:
        if TREE[j][0] <= d:
            break
        if TREE[j][0] == d + 1:
            last = j
    if last is not None:
        px = left + d * indent + 3.0
        c.rule(px, ys[i] + SIZE * 0.55, px, ys[last])
for i, (d, name, key) in enumerate(TREE):
    if key:
        end = left + d * indent + len(name) * adv + 5.0
        txt = c.text(ax_note, ys[i], NOTES[key], italic=True, size=look.SANS_PT,
                     align="right")
        c.canvas.draw()
        r = c.canvas.get_renderer()
        bb = txt.get_window_extent(r).transformed(c.ax.transData.inverted())
        c.leader(min(bb.x0, bb.x1) - 4.0, ys[i], end, ys[i])
c.save(look.figures_dir() / "00-proof-tree.png")
