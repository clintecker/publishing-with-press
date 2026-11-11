"""04-03 set pieces: the same four lines as cascade, verse, and tail."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import look
from look import Canvas
from matplotlib.font_manager import FontProperties, findfont

LINES = ["Alice's Right Foot, Esq.", "Hearthrug,", "near the Fender,",
         "(with Alice's love)."]
SERIF = ["Times New Roman", "Georgia", "DejaVu Serif"]

def serif(c, x, y, s, size):
    t = c.ax.text(x, y, s, fontproperties=FontProperties(family=SERIF, size=size),
                  color="black", ha="left", va="center", zorder=c._zo() + 5)
    c._texts.append(t)
    return t

FW, FH, GAP, X0 = 98, 92, 9, 8
c = Canvas(8 + FH + 8 + 14 + 6)
top = 8
specs = [
    ("(a) cascade", [(8 + 5 * i, 8.0) for i in range(4)]),
    ("(b) verse",   [(12, 8.0)] * 4),
    ("(c) tail",    [(12, 8.0), (6, 7.6), (14, 7.3), (5, 7.0)]),
]
for i, (label, pos) in enumerate(specs):
    x = X0 + i * (FW + GAP)
    c.box(x, top, FW, FH, kind="plain")
    for j, (s, (dx, size)) in enumerate(zip(LINES, pos)):
        serif(c, x + dx, top + 18 + j * 19, s, size)
    c.text(x + FW / 2, top + FH + 8, label, align="center", va="top")
c.save(look.figures_dir() / "04-03-set-pieces.png")
