"""Figure 6.1: the checker guards every build (archetype 1, pipeline)."""
import look
from _parts import file_icon

c = look.Canvas(172)
# inputs
file_icon(c, 36, 56, "book/chapters/\n*.md", w=22, h=18)
file_icon(c, 36, 104, "config/*.yaml", w=22, h=18)
# the large box
BX, BY, BW, BH = 86, 30, 158, 84
c.text(BX + 3, BY - 7, "press all", italic=True, size=8)
c.box(BX, BY, BW, BH, kind="plain")
c.text(BX + BW / 2, BY + 9, "press check", mono=True, size=7, align="center")
labels = ["source\nchecks", "checking\nthe\ncheckers", "style\naudit",
          "jargon\nlint"]
IW, IG, IY, IH = 33, 5, 50, 46
x = BX + 6
boxes = []
for lab in labels:
    boxes.append(c.box(x, IY, IW, IH, lab, size=7))
    x += IW + IG
for a, b in zip(boxes, boxes[1:]):
    c.arrow(a.right[0], IY + IH / 2, b.left[0], IY + IH / 2)
# inputs into the large box
c.path([(47, 56), (72, 56), (72, 72)], arrow=False)
c.path([(47, 104), (72, 104), (72, 72)], arrow=False)
c.arrow(72, 72, BX, 72)
# pass: to the three editions
SX, SW, SH = 274, 44, 24
ys = [BY + 12, BY + 42, BY + 72]
for y, n in zip(ys, ["Print\nedition", "Circulating\nedition", "Chapter\nedition"]):
    c.box(SX, y - SH / 2 + 0, SW, SH, n, size=7)
    c.arrow(262, y, SX, y)
c.rule(262, ys[0], 262, ys[-1], weight=look.ARROW_PT)
c.arrow(BX + BW, 72, 262, 72)
c.text(253, 69, "pass", italic=True, size=7, align="center", va="bottom")
# fail: drop to the stop box
FX = BX + BW / 2
stop = c.box(FX - 46, 140, 92, 22, "stop (nonzero exit)", shadow=True, size=7)
c.arrow(FX, BY + BH, FX, 140)
c.text(FX + 4, 127, "fail", italic=True, size=7, align="left")
c.save(look.figures_dir() / "06-01-checker-guards-the-build.png")
