"""Figure 11.2: one alpha master onto every surface (archetype 6, before/after)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np
import look
from _plate import *

c = look.Canvas(196)
# left: master on a checkerboard
LX, LY, LS = 14, 56, 76
n = px(LS)
ink, al = plate_rgba(n)
show(c, over(checker(n, n, px(4)), ink, al), LX, LY, LS, LS)
outline(c, LX, LY, LS, LS)
c.text(LX + LS / 2, LY + LS + 6, "alpha master", size=8, align="center", va="top")
c.text(LX + LS / 2, LY + LS + 17, "assets/woodcuts/\nthe-engravers-bench.png",
       mono=True, size=7, align="center", va="top")
# right: three results
TX, TS = 158, 46
ys = [12, 75, 138]
tn = px(TS)
pink, pal = plate_rgba(px(36))
m = pink.shape[0]
# print interior: a page outline on white
c.box(TX, ys[0], TS, TS, kind="plain")
show(c, over(flat(m, m, 255), pink, pal), TX + (TS - 36) / 2, ys[0] + (TS - 36) / 2, 36, 36)
# cloth cover: grain, plate stamped at center
cw, ch = 40, 50
gw, gh = px(cw), px(ch)
grain = flat(gh, gw, G[40])
grain[::5, :] = G[20]
grain[:, ::7] = np.minimum(grain[:, ::7], 170)
grain[2::5, 3::7] = G[20]
sn = px(30)
sink, sal = plate_rgba(sn)
cover = over(grain, sink, sal, ((gh - sn) // 2, (gw - sn) // 2))
cx0 = TX + (TS - cw) / 2
show(c, cover, cx0, ys[1] - 2, cw, ch)
outline(c, cx0, ys[1] - 2, cw, ch)
c.rule(cx0 + 4, ys[1] - 2, cx0 + 4, ys[1] + ch - 2)
# web panel on cream
c.box(TX - 3, ys[2], TS + 6, TS, kind="process", fill=10)
show(c, over(flat(m, m, G[10]), pink, pal), TX + (TS - 36) / 2, ys[2] + (TS - 36) / 2, 36, 36)
LXL = TX + TS + 14
labels = ["print interior,\nflattened onto white",
          "cloth cover, flattened\nonto the field color",
          "Chapter edition,\ntransparent PNG"]
cy = [ys[0] + TS / 2, ys[1] - 2 + ch / 2, ys[2] + TS / 2]
for l, y in zip(labels, cy):
    c.text(LXL, y, l, size=8, align="left", va="center")
for y in cy:
    c.arrow(LX + LS + 6, LY + LS / 2, TX - 8, y)
c.save(look.figures_dir() / "11-02-one-master-every-surface.png")
