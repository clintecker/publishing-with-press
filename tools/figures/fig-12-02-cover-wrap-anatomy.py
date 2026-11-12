"""12-01 cover wrap anatomy: 6 x 9 book, 200 pages, cream; drawn to scale (page anatomy)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import look
from look import Canvas

S = 22.4                      # points per inch
X0, YT = 18.0, 66.0
B = 0.125 * S
PW, SW = 6 * S, 0.5 * S
W, H = 12.75 * S, 9.25 * S
c = Canvas(YT + H + 30)

# bleed band (10% gray), then the three panels inside the trim line
c.box(X0, YT, W, H, kind="plain", fill=10)
c.box(X0 + B, YT + B, PW, 9 * S, "back", kind="plain")
c.box(X0 + B + PW, YT + B, SW, 9 * S, kind="plain", fill=20)
c.box(X0 + B + PW + SW, YT + B, PW, 9 * S, "front", kind="plain")
sx1, sx2 = X0 + B + PW, X0 + B + PW + SW


def hdim(x1, x2, y, label, ext_from, mono=False, label_on=True):
    mid = (x1 + x2) / 2
    c.arrow(mid, y, x1, y)
    c.arrow(mid, y, x2, y)
    for x in (x1, x2):
        c.rule(x, ext_from, x, y - 3, weight=look.LEADER_PT)
    if label_on:
        c.text(mid, y, label, mono=mono, size=7, align="center", va="center", bg=True)


# top: overall width
hdim(X0, X0 + W, 14, "wrap_w = 12.75in", YT, mono=True)
# back and front widths (row A); the spine segment is labelled one row up
hdim(X0 + B, sx1, 48, "back 6in", YT + B)
hdim(sx2, X0 + B + 2 * PW + SW, 48, "front 6in", YT + B)
hdim(sx1, sx2, 48, "", YT + B, label_on=False)
c.leader(X0 + B + PW + SW / 2, 45, X0 + B + PW + SW / 2, 36)
c.text(X0 + B + PW + SW / 2, 31, "spine = 200 x 0.0025 = 0.5in", mono=True, size=7,
       align="center", va="center")

# right: overall height
rx = X0 + W + 10
c.arrow(rx, YT + H / 2, rx, YT)
c.arrow(rx, YT + H / 2, rx, YT + H)
for y in (YT, YT + H):
    c.rule(X0 + W + 2, y, rx + 3, y, weight=look.LEADER_PT)
c.text(rx, YT + H / 2, "wrap_h = 9.25in", mono=True, size=7, align="center",
       va="center", bg=True).set_rotation(90)

# below: bleed and trim labels on leaders
LY = YT + H + 17
c.text(X0 + 4, LY, "bleed 0.125in", size=7, align="left", va="center")
c.leader(X0 + 20, LY - 5, X0 + 20, YT + H - B / 2)
c.text(X0 + 98, LY, "trim", size=7, align="left", va="center")
c.leader(X0 + 100, LY - 5, X0 + 100, YT + H - B)

# barcode on the back panel: 1.235 x 0.9in, 0.5in off the spine fold, 0.5in up
bw, bh = 1.235 * S, 0.9 * S
bx2 = sx1 - 0.5 * S
by2 = YT + B + 9 * S - 0.5 * S
c.box(bx2 - bw, by2 - bh, bw, bh, "EAN-13", kind="plain", size=7)
def tick_gap(horizontal, a, b, at):
    """A thin measure across a small gap: a rule with a short tick at each end."""
    t = 2.5
    if horizontal:
        c.rule(a, at, b, at, weight=look.LEADER_PT)
        for x in (a, b):
            c.rule(x, at - t, x, at + t, weight=look.LEADER_PT)
    else:
        c.rule(at, a, at, b, weight=look.LEADER_PT)
        for y in (a, b):
            c.rule(at - t, y, at + t, y, weight=look.LEADER_PT)


gy = by2 - bh / 2
tick_gap(True, bx2, sx1, gy)
mx = (bx2 + sx1) / 2
c.text(sx1 - 3, by2 - bh - 26, "0.5in from spine fold", size=7, align="right", va="center")
c.leader(mx, by2 - bh - 21, mx, gy)
trim_b = YT + B + 9 * S
gx = bx2 - bw / 2
tick_gap(False, by2, trim_b, gx)
ym = (by2 + trim_b) / 2
c.text(bx2 - bw - 6, ym, "0.5in up", size=7, align="right", va="center")
c.leader(bx2 - bw - 4, ym, gx, ym)

c.save(look.figures_dir() / "12-02-cover-wrap-anatomy.png")
