"""Figure 7.2: the filter chain per family of editions (archetype 4, layered stack)."""
import look

c = look.Canvas(172)
cols = [
    ("pdf, epub, html,\nchunked", ["typographic-spacing", "set-pieces", "chapter-dropcap",
                                   "scene-break", "figure-numbering"]),
    ("print", ["typographic-spacing", "set-pieces", "print-safe-images", "chapter-dropcap",
               "scene-break", "figure-numbering"]),
    ("portable\n(txt, docx)", ["typographic-spacing", "set-pieces", "figure-numbering"]),
]
X0, W, GAP, H, Y0 = 32, 88, 6, 22, 34
for ci, (head, items) in enumerate(cols):
    x = X0 + ci * (W + GAP)
    c.text(x + W / 2, 8, head, size=8, align="center", va="top")
    for i, n in enumerate(items):
        fill = 40 if n == "print-safe-images" else (10 if i % 2 == 0 else 20)
        c.box(x, Y0 + i * H, W, H, n, kind="plain", fill=fill, mono=True, size=7)
# downward arrow at the left of the first column
AX = 16
yb = Y0 + 5 * H
c.arrow(AX, Y0, AX, yb)
t = c.ax.text(AX - 4.5, (Y0 + yb) / 2, "pandoc runs in this order", rotation=90,
              fontproperties=look.fontprops(False, True, False, 7), ha="center", va="center",
              color="black", zorder=20)
c.save(look.figures_dir() / "07-02-filter-chain.png")
