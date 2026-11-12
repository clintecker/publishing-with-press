"""Figure 11.3: what intake does to a delivered plate (archetype 6, before/after)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np
import look
from _plate import *

c = look.Canvas(246)
FW, FY = 128, 24
AX, BX = 12, 187
n = px(104)
ink, al = plate_rgba(n)
# (a) delivered: white frame, a 5 percent gray ground ending just inside it
c.box(AX, FY, FW, FW, kind="plain")
GX, GY, GS = AX + 6, FY + 6, FW - 12
c.rule(GX, GY, GX + GS, GY, weight=0.3)
gn = px(GS)
gnd = flat(gn, gn, 241)
off = (gn - n) // 2
show(c, over(gnd, ink, al, (off, off)), GX, GY, GS, GS)
outline(c, GX, GY, GS, GS, lw=0.5, edge=look.GRAY[20])
c.text(AX + FW, 10, "ground near #f1f2f3", mono=True, size=7, align="right", va="center")
c.leader(AX + FW - 20, 15, GX + GS - 1, GY + 12)
# (b) after intake: checker, no ground
c.box(BX, FY, FW, FW, kind="plain")
show(c, over(checker(px(FW - 12), px(FW - 12), px(4)), ink, al,
             ((px(FW - 12) - n) // 2, (px(FW - 12) - n) // 2)), BX + 6, FY + 6, FW - 12, FW - 12)
c.text(AX + FW / 2, FY + FW + 8, "(a) delivered", size=8, align="center", va="top")
c.text(BX + FW / 2, FY + FW + 8, "(b) after intake", size=8, align="center", va="top")
c.arrow(AX + FW + 8, FY + FW / 2, BX - 8, FY + FW / 2)
# luminance scale
X0, X1, SY = 12, 315, 214
sx = lambda v: X0 + v / 255 * (X1 - X0)
AH = 24
c.text((X0 + X1) / 2, SY + 16, "luminance", italic=True, size=7, align="center", va="top")
c.path([(sx(0), SY - AH), (sx(45), SY - AH), (sx(225), SY), (sx(255), SY)], arrow=False)
c.rule(X0, SY, X1, SY)
for v in (0, 45, 225, 255):
    c.rule(sx(v), SY, sx(v), SY + 3)
    c.text(sx(v), SY + 5, str(v), mono=True, size=7, align="center", va="top")
c.text((sx(0) + sx(45)) / 2 + 2, SY - AH - 3, "alpha 255,\nink", size=7, align="center", va="bottom")
c.text((sx(45) + sx(225)) / 2 - 8, SY - AH / 2 - 6, "linear ramp", size=7, align="center", va="bottom")
c.text(sx(255) - 2, SY - 3, "alpha 0,\nclear", size=7, align="right", va="bottom")
c.save(look.figures_dir() / "11-03-intake-before-after.png")
