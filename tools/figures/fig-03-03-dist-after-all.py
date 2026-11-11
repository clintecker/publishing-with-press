"""Figure 3.3: the dist directory after press all (archetype 3, tree)."""
import look
from _tree import row

P = 16.0
rows = [
    ("dist/", None), ("alice.pdf", "Print edition"),
    ("alice.epub", "Circulating edition"), ("alice.html", "Single-leaf edition"),
    ("alice.md", "Manuscript edition"), ("alice.txt", "Telegraphic edition"),
    ("alice.docx", "Office edition"), ("alice-site.zip", "Chapter edition"),
    ("alice-source.zip", "Source edition"),
    ("alice-sources.md", "sources companion, only with config/authorities.yaml"),
    ("site/", "the per-chapter reader"), ("pages/", "the GitHub Pages bundle (see Chapter 14)"),
]
top = 14
c = look.Canvas(top + P * len(rows) + 2)
ys = [top + i * P for i in range(len(rows))]
TR = 18
# 10% band behind the eight edition rows
c.box(6, ys[1] - P / 2 + 1, 314.5, 8 * P - 4, kind="plain", fill=10)
c.text(12, ys[0], rows[0][0], mono=True, size=7, bold=True)
c.rule(TR, ys[0] + 6, TR, ys[-1])
for i, (name, note) in enumerate(rows[1:], 1):
    c.rule(TR, ys[i], TR + 7, ys[i])
    row(c, TR + 10, ys[i], name, note, right=314,
        box=20 if name == "pages/" else 0, dashed=name == "alice-sources.md")
c.save(look.figures_dir() / "03-03-dist-after-all.png")
