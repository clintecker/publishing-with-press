"""Figure 3.1: the tree that press new lays down (archetype 3, tree)."""
import look
from _tree import row

P = 15.0
rows = [  # (depth, name, note, box)
    (0, "alice/", None, 0),
    (1, ".claude/workflows/ (four files)", None, 0),
    (1, ".github/workflows/book.yml", "the whole CI: calls the press's build.yml at v3", 0),
    (1, ".gitignore", None, 0),
    (1, "book/chapters/00-preface.md", "your chapters go here", 0),
    (1, "CHANGELOG.md", None, 0),
    (1, "CLAUDE.md", None, 0),
    (1, "config/", None, 0),
    (2, "front-matter.yaml", None, 0),
    (2, "house-rules.yaml", None, 0),
    (2, "metadata.yaml", "identity, press facts, verification knobs", 20),
    (1, "Makefile", None, 0),
    (1, "requirements.txt", None, 0),
]
top = 14
c = look.Canvas(top + P * len(rows) + 4)
X0, TR, IND = 12, 18, 14
ys = [top + i * P for i in range(len(rows))]
c.text(X0, ys[0], rows[0][1], mono=True, size=7, bold=True)
# trunk
c.rule(TR, ys[0] + 6, TR, ys[-1])
cfg = 7
c.rule(TR + IND, ys[cfg] + 6, TR + IND, ys[cfg + 3])
for i, (d, name, note, box) in enumerate(rows[1:], 1):
    tx = TR if d == 1 else TR + IND
    c.rule(tx, ys[i], tx + 7, ys[i])
    row(c, tx + 10, ys[i], name, note, box=box)
c.save(look.figures_dir() / "03-01-scaffold-tree.png")
