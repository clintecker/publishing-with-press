"""09-01 page geometry: the 6 x 9 house page to scale (13 pt per inch), half measure."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import look
from look import Canvas, GRAY
from matplotlib.patches import Rectangle

S = 13.0                     # points per inch
c = Canvas(168, measure="half")
X0, Y0 = 40.0, 28.0
PW, PH = 6 * S, 9 * S
X1, Y1 = X0 + PW, Y0 + PH
BL, BR = X0 + 0.78 * S, X1 - 0.68 * S
BT, BB = Y0 + 0.72 * S, Y1 - 0.78 * S
CAP = BT + 6.3 * S
CX = (BL + BR) / 2


def bar(x1, x2, y, h=1.6, fill=40):
    c.ax.add_patch(Rectangle((x1, y - h / 2), x2 - x1, h, facecolor=look.GRAY[fill],
                             edgecolor="none", zorder=c._zo()))


def dim_h(xa, xb, y, text=None, tx=None, size=7):
    m = (xa + xb) / 2
    c.arrow(m, y, xa, y)
    c.arrow(m, y, xb, y)
    if text:
        c.text(tx if tx is not None else m, y, text, size=size, align="center", bg=True)


def dim_v(x, ya, yb, text=None, ty=None):
    m = (ya + yb) / 2
    c.arrow(x, m, x, ya)
    c.arrow(x, m, x, yb)
    if text:
        c.text(x, ty if ty is not None else m, text, size=7, align="center", bg=True)


# page, then the text block (10% gray)
c.box(X0, Y0, PW, PH, kind="plain")
c.box(BL, BT, BR - BL, BB - BT, kind="plain", fill=10)
# running head (two runs of small type) and page number
HB = BT - 0.20 * S
bar(BL, BL + 22, HB)
bar(BR - 16, BR, HB)
FB = BB + 0.38 * S
c.text(CX, FB, "12", size=7, align="center", va="baseline")

# 6in across the top, 9in down the right
yt = 17
c.rule(X0, Y0 - 1, X0, yt - 4, weight=0.5)
c.rule(X1, Y0 - 1, X1, yt - 4, weight=0.5)
dim_h(X0, X1, yt, "6in")
xr = 155
c.rule(X1 + 1, Y0, xr + 3, Y0)
c.rule(X1 + 1, Y1, xr + 3, Y1)
dim_v(xr, Y0, Y1, "9in")

# inside the block
dim_h(BL, BR, BT + 14, "4.54in")
dim_v(CX + 14, BT, BB, "7.5in", ty=(BT + BB) / 2 + 4)

# left gutter: head, height cap, inner, foot
LR = 33
xm = X0 + 5          # dimension lines sit inside the left margin
dim_v(xm + 1, Y0, BT)
c.text(LR, 31, "head\n0.72in", size=7, align="right")
c.leader(LR + 2, 31, xm + 1, (Y0 + BT) / 2)
# height cap bracket: dashed, from the top of the block
xb = BL - 4
c.rule(xb, BT, xb, CAP, dashed=True, weight=0.75)
c.rule(xb - 2, BT, xb + 2, BT, weight=0.75)
c.rule(xb - 2, CAP, xb + 2, CAP, weight=0.75)
c.text(LR, 68, "height\ncap\n6.3in", size=7, align="right")
c.leader(LR + 2, 68, xb, 68)
yi = 126
dim_h(X0, BL, yi)
c.text(LR, yi, "inner\n0.78in", size=7, align="right")
c.leader(LR + 2, yi, X0 + (BL - X0) / 2, yi)
c.text(LR, 150, "foot\n0.78in", size=7, align="right")
c.leader(LR + 2, 150, xm + 1, (BB + Y1) / 2 + 0)
dim_v(xm + 1, BB, Y1)

# right gutter: headsep, outer, footskip
RL = 120
xa = X1 + 3
for y in (HB, BT):
    c.rule(BR - 8 if y == BT else BR + 1, y, xa + 4, y, weight=0.5)
c.arrow(xa, HB - 5, xa, HB)
c.arrow(xa, BT + 5, xa, BT)
c.text(RL + 6, 38, "headsep\n0.20in", size=7, align="left")
c.leader(RL + 2, 38, xa + 1.5, (HB + BT) / 2)
yo = 74
dim_h(BR, X1, yo)
c.text(RL, yo, "outer\n0.68in", size=7, align="left")
c.leader(RL - 1.5, yo, (BR + X1) / 2, yo)
for y in (BB, FB):
    c.rule(CX + 11 if y == FB else BR + 1, y, xa + 4, y, weight=0.5)
c.arrow(xa, BB - 5, xa, BB)
c.arrow(xa, FB + 5, xa, FB)
c.text(RL + 6, 152, "footskip\n0.38in", size=7, align="left")
c.leader(RL + 2, 152, xa + 1.5, (BB + FB) / 2)

c.save(look.figures_dir() / "09-01-page-geometry.png")
