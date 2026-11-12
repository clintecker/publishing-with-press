"""09-02 the six design profiles as a matrix, full measure."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import look
from look import Canvas
from matplotlib.patches import Rectangle

ROWS = [
    ("house-6x9", "6 x 9", "4.54in", "6.3in", "default"),
    ("house-6x9-color", "6 x 9", "4.54in", "6.3in", "color interior"),
    ("novella-5x8", "5 x 8", "3.75in*", "5.6in", "novella"),
    ("digest-5.5x8.5", "5.5 x 8.5", "4.14in*", "6.0in", "genre trade paperback"),
    ("large-print-7x10", "7 x 10", "5.35in*", "7.2in", "large print"),
    ("mass-market-4.25x6.87", "4.25 x 6.87", "3.17in*", "4.8in", "rack-size paperback"),
]
HEADS = ["trim", "text width", "height cap", "intended use"]
RH = 17.0
c = Canvas(158)
X0, X1 = 5.0, 321.0
Y0 = 8.0
cols = [X0, 103.0, 148.0, 195.0, 243.0, X1]
n = len(ROWS) + 1
Y1 = Y0 + n * RH
# header fill (10%)
c.ax.add_patch(Rectangle((X0, Y0), X1 - X0, RH, facecolor=look.GRAY[10],
                         edgecolor="none", zorder=c._zo()))
# frame and horizontal rules
c.rule(X0, Y0, X1, Y0)
c.rule(X0, Y1, X1, Y1)
for i in range(1, n):
    c.rule(X0, Y0 + i * RH, X1, Y0 + i * RH)
c.rule(X0, Y0, X0, Y1)
c.rule(X1, Y0, X1, Y1)
for x in cols[1:-1]:
    c.rule(x, Y0, x, Y1)
# heads: columns 1..4 (the first column has no head)
for j, h in enumerate(HEADS):
    c.text(cols[j + 1] + 4, Y0 + RH / 2, h, size=8, bold=True)
for i, row in enumerate(ROWS):
    y = Y0 + (i + 1.5) * RH
    c.text(cols[0] + 4, y, row[0], mono=True, size=7)
    for j in range(1, 5):
        c.text(cols[j] + 4, y, row[j], size=7, bold=(j == 3))
# the height cap column carries the eye: a heavier frame
c.rule(cols[3], Y0, cols[3], Y1, weight=1.5)
c.rule(cols[4], Y0, cols[4], Y1, weight=1.5)
c.rule(cols[3], Y0, cols[4], Y0, weight=1.5)
c.rule(cols[3], Y1, cols[4], Y1, weight=1.5)
c.text(X0 + 1, Y1 + 10, "* derived: trim width less inner and outer margins",
       italic=True, size=7)
c.save(look.figures_dir() / "09-02-profiles-compared.png")
