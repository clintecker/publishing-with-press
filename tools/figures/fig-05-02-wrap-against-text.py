"""05-02 wrap against text: an open book, verso and recto (page anatomy)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import look
from look import Canvas, GRAY
from matplotlib.patches import Rectangle

c = Canvas(236)
PW, PH = 112, 168                       # 6 x 9 page
SP = c.W / 2 - 8                        # spine x (leaves room for "guard")
PY = 34
TW, TH = PW * 4.54 / 6, PH * 7.5 / 9    # text block
INNER, TOP = 13, (PH - TH) / 2
PITCH, BAR = 5.2, 1.8
NL = int(TH / PITCH)
BW, BROWS, GAPW = 32, 9, 16              # block width, rows, outset (drawn large)


def rect(x, y, w, h, fill, edge=False):
    c.ax.add_patch(Rectangle((x, y), w, h, facecolor=GRAY[fill],
                             edgecolor="black" if edge else "none",
                             linewidth=0.5, zorder=c._zo()))


def side(px, recto):
    """Draw one page whose left edge is px; return block geometry."""
    c.box(px, PY, PW, PH, kind="plain")
    tx = px + (INNER if recto else PW - INNER - TW)
    ty = PY + TOP
    bx = tx if recto else tx + TW - BW
    rect(bx, ty, BW, BROWS * PITCH - 1.4, 20, edge=True)
    for i in range(NL):
        x1, x2 = tx, tx + TW
        if i < BROWS:
            if recto:
                x1 = tx + BW + GAPW
            else:
                x2 = bx - GAPW
        elif i in (11, 18, NL - 1):
            x2 -= 0.4 * TW
        rect(x1, ty + i * PITCH + PITCH / 2 - BAR / 2, x2 - x1, BAR, 40)
    return tx, ty, bx


vx, vy, vbx = side(SP - PW, recto=False)
rx, ry, rbx = side(SP, recto=True)
c.rule(SP, PY, SP, PY + PH, weight=2.2)

# wrap-inner labels
LY = 10
vc, rc = vbx + BW / 2, rbx + BW / 2
c.text(vc, LY, "wrap-inner", size=8, align="center")
c.leader(vc, LY + 6, vc, ry + 10)
c.text(rc, LY, "wrap-inner", size=8, align="center")
c.leader(rc, LY + 6, rc, ry + 10)
# outset: the white gap beside the recto block
gx = rbx + BW + GAPW / 2
c.text(gx + 30, LY, "outset", size=8, align="center")
c.leader(gx + 26, LY + 6, gx, ry + 22)
ay = ry + 34
c.arrow(gx, ay, gx - GAPW / 2 + .5, ay)
c.arrow(gx, ay, gx + GAPW / 2 - .5, ay)
# spine
c.text(SP, PY + PH + 16, "spine", size=8, align="center")
c.leader(SP, PY + PH + 10, SP, PY + PH - 14)
# guard bracket in the recto's outer margin, covering block and side lines
bx2 = SP + PW - 6.5
top, bot = ry, ry + BROWS * PITCH
c.rule(bx2, top, bx2, bot)
c.rule(bx2 - 3, top, bx2, top)
c.rule(bx2 - 3, bot, bx2, bot)
c.text(SP + PW + 5, (top + bot) / 2, "guard", size=8, align="left")
c.save(look.figures_dir() / "05-02-wrap-against-text.png")
