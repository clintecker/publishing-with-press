"""05-01 placement vocabulary: seven miniature 6 x 9 pages (matrix)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import look
from look import Canvas, GRAY
from matplotlib.patches import Rectangle

c = Canvas(262)
PW, PH, GAP = 66, 99, 14            # 6 x 9 page at 11 pt per inch
TW, TH = PW * 4.54 / 6, PH * 7.5 / 9  # text block
MX, MY = (PW - TW) / 2, (PH - TH) / 2
PITCH, BAR = 3.7, 1.3
NLINES = int(TH / PITCH)


def rect(x, y, w, h, fill):
    c.ax.add_patch(Rectangle((x, y), w, h, facecolor=GRAY[fill],
                             edgecolor="black" if fill == 20 and h > 6 else "none",
                             linewidth=0.5, zorder=c._zo()))


def spine(x, y):                     # short heavy rule on the spine edge
    c.rule(x, y + PH / 2 - 11, x, y + PH / 2 + 11, weight=2.2)


def page(x, y, spine_left=True, lines=None, block=None, label="", ghost=False):
    """block = (row, rows, side, wfrac): side in 'spine', 'fore', 'across'."""
    c.box(x, y, PW, PH, kind="plain")
    tx = x + MX if spine_left else x + (PW - TW) - MX + MX  # same on both
    tx = x + (MX if spine_left else PW - MX - TW)
    ty = y + MY
    bx = bw = br = brows = None
    if block:
        br, brows, side, frac = block
        bw = TW if side == "across" else TW * frac
        on_left = (side == "spine") == spine_left
        bx = tx if (side == "across" or on_left) else tx + TW - bw
        rect(bx, ty + br * PITCH, bw, brows * PITCH - 1.2, 20)
    for i in range(NLINES):
        if lines is False:
            break
        y0 = ty + i * PITCH + PITCH / 2
        x1, x2 = tx, tx + TW
        if block and br <= i < br + brows:
            if block[2] == "across":
                continue
            if bx == tx:
                x1 = tx + bw + 3.5
            else:
                x2 = bx - 3.5
        if i in (12, 19, NLINES - 1):
            x2 -= 0.45 * TW if x2 == tx + TW else 0.3 * TW
        rect(x1, y0 - BAR / 2, x2 - x1, BAR, 40)
    spine(x + (0 if spine_left else PW), y)


x0 = (c.W - (4 * PW + 3 * GAP)) / 2
y1, y2 = 8, 8 + PH + 30
names = ["inline", "wrap-inner", "wrap-outer", "margin"]
specs = [dict(block=(8, 7, "across", 1)),
         dict(block=(0, 8, "spine", .42)),
         dict(block=(0, 8, "fore", .42)),
         dict(block=(0, 8, "fore", .42))]
for k in range(4):
    x = x0 + k * (PW + GAP)
    page(x, y1, **specs[k])
    c.text(x + PW / 2, y1 + PH + 6, names[k], mono=True, size=7,
           align="center", va="top")

row2 = 2 * PW + (2 * PW + 4) + 2 * GAP     # plate, full-bleed, pair
xs = (c.W - row2) / 2
# plate: block alone, space above and below
x = xs
c.box(x, y2, PW, PH, kind="plain")
rect(x + MX, y2 + PH / 2 - 17, TW, 34, 20)
spine(x, y2)
c.text(x + PW / 2, y2 + PH + 6, "plate", mono=True, size=7, align="center", va="top")
# full-bleed: fills the text area
x += PW + GAP
c.box(x, y2, PW, PH, kind="plain")
rect(x + MX, y2 + MY, TW, TH, 20)
spine(x, y2)
c.text(x + PW / 2, y2 + PH + 6, "full-bleed", mono=True, size=7, align="center", va="top")
# frontispiece: verso with block, ghost recto with chapter heading
x += PW + GAP
c.box(x, y2, PW, PH, kind="plain")
rect(x + MX, y2 + PH / 2 - 17, TW, 34, 20)
spine(x + PW + 0, y2)
gx = x + PW + 4
for (a, b, d, e) in [(gx, y2, gx + PW, y2), (gx + PW, y2, gx + PW, y2 + PH),
                     (gx + PW, y2 + PH, gx, y2 + PH), (gx, y2 + PH, gx, y2)]:
    c.rule(a, b, d, e, dashed=True)
spine(gx, y2)
c.ax.add_patch(Rectangle((gx + MX + 3, y2 + 26), TW * .5, 3.2,
                         facecolor="black", edgecolor="none", zorder=c._zo()))
for i in range(5):
    rect(gx + MX + 3, y2 + 38 + i * PITCH, TW - 6 - (14 if i == 4 else 0), BAR, 20)
c.text(x + PW + 3, y2 + PH + 6, "frontispiece", mono=True, size=7,
       align="center", va="top")
c.save(look.figures_dir() / "05-01-placement-vocabulary.png")
