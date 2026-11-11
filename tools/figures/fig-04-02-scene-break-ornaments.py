"""04-02 scene-break ornaments: 3 rows (rule, asterism, fairy-dust) x PDF/Reader."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import look
from look import Canvas, GRAY
from matplotlib.patches import Rectangle, Polygon

X0, XL, XM, X1 = 8, 80, 199, 318
HEAD, ROW = 22, 58
H = 8 + HEAD + 3 * ROW + 8
c = Canvas(H)
top = 8
bot = top + HEAD + 3 * ROW

def bar(x1, x2, y, h=2.2):
    c.ax.add_patch(Rectangle((x1, y - h / 2), x2 - x1, h, facecolor=GRAY[20],
                             edgecolor="none", zorder=c._zo()))

# frame and rules
c.box(X0, top, X1 - X0, bot - top, kind="plain")
c.rule(X0, top + HEAD, X1, top + HEAD)
for i in (1, 2):
    c.rule(X0, top + HEAD + i * ROW, X1, top + HEAD + i * ROW)
c.rule(XL, top, XL, bot)
c.rule(XM, top, XM, bot)
c.text((XL + XM) / 2, top + HEAD / 2, "PDF", align="center", bold=True)
c.text((XM + X1) / 2, top + HEAD / 2, "Reader", align="center", bold=True)

def cell(col, row):
    x1, x2 = (XL, XM) if col == 0 else (XM, X1)
    y = top + HEAD + row * ROW
    cy = y + ROW / 2
    for dy in (-23, -18):
        bar(x1 + 10, x2 - 10 - (6 if dy == -18 else 0), cy + dy)
    for dy in (18, 23):
        bar(x1 + 10, x2 - 10 - (30 if dy == 23 else 0), cy + dy)
    return (x1 + x2) / 2, cy

for r, name in enumerate(["rule", "asterism", "fairy-dust"]):
    c.text(X0 + 6, top + HEAD + r * ROW + ROW / 2, name, mono=True, size=7,
           va="center")

# rule
cx, cy = cell(0, 0)
c.rule(cx - 36, cy, cx + 36, cy, weight=0.5)
cx, cy = cell(1, 0)
d = 3.4
c.ax.add_patch(Polygon([(cx - d, cy), (cx, cy - d), (cx + d, cy), (cx, cy + d)],
                       closed=True, facecolor="black", edgecolor="black",
                       linewidth=0.3, zorder=c._zo()))
for s in (-1, 1):                         # hairlines tapering to the outer ends
    xa, xb = cx + s * (d + 3), cx + s * 46
    c.ax.add_patch(Polygon([(xa, cy - 0.45), (xa, cy + 0.45), (xb, cy)],
                           closed=True, facecolor="black", edgecolor="none",
                           zorder=c._zo()))
# asterism, both columns
for col in (0, 1):
    cx, cy = cell(col, 1)
    for k in (-1, 0, 1):
        c.text(cx + k * 22, cy + 1.5, "*", size=10, bold=True, align="center")
# fairy-dust, both columns
for col in (0, 1):
    cx, cy = cell(col, 2)
    for n, dy in [(4, -7), (3, 0), (4, 7)]:
        for k in range(n):
            c.text(cx + (k - (n - 1) / 2) * 10, cy + dy + 1.2, "*", size=8,
                   bold=True, align="center")

c.save(look.figures_dir() / "04-02-scene-break-ornaments.png")
