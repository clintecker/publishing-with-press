"""Figure 15.2: the editorial-passes machine (archetype 10, flowchart, left to right)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import look

c = look.Canvas(250)
S = 7
# ---- column 1: scout and its inputs
c.box(28, 8, 20, 16, kind="file", label="book/\nchapters/\n*.md", label_below=True, mono=True, size=S)
c.box(6, 70, 44, 24, "Scout", size=S)
c.box(2 + 4, 118, 44, 22, "press\nskills", mono=True, size=S)
c.arrow(38, 57, 38, 70)
c.arrow(28, 118, 28, 94)
# ---- column 2: the readers
X2, W2 = 66, 56
for y in (8, 24, 40):
    c.box(X2, y, W2, 13, "chapter pass", size=S)
c.text(X2 + W2 / 2, 55, "...", size=10, align="center", va="top")
c.text(X2 + W2 / 2, 66, "one pass per\nchapter file", italic=True, size=S, align="center", va="top")
c.text(X2 + W2 / 2, 98, "whole book", italic=True, size=S, align="center", va="top")
for y, t in ((110, "cadence"), (125, "repetition"), (140, "arc")):
    c.box(X2, y, W2, 13, t, size=S)
# scout -> readers
c.rule(50, 82, 58, 82)
c.path([(58, 82), (58, 30.5), (X2, 30.5)])
c.path([(58, 82), (58, 131.5), (X2, 131.5)])
# readers -> suggestions
BUS = 132
for y in (14.5, 30.5, 46.5, 116.5, 131.5, 146.5):
    c.rule(X2 + W2, y, BUS, y)
c.rule(BUS, 14.5, BUS, 146.5)
c.box(148, 70, 22, 24, kind="file")
c.text(159, 97, "suggestions", mono=True, size=S, align="center", va="top")
c.arrow(BUS, 82, 148, 82)
# ---- column 3: synthesizers
X3 = 196
for y in (8, 24, 40):
    c.box(X3, y, W2, 13, "synthesizer", size=S)
c.text(X3 + W2 / 2, 55, "...", size=10, align="center", va="top")
c.text(X3 + W2 / 2, 66, "one per\nchapter file", italic=True, size=S, align="center", va="top")
c.path([(170, 82), (184, 82), (184, 30.5), (X3, 30.5)])
c.box(212, 108, 24, 18, kind="file")
c.text(224, 129, "build/\neditorial-\nrejections.md", mono=True, size=S, align="center", va="top")
c.arrow(224, 84, 224, 108)
# ---- column 4: the law
c.text(295, 28, "Law", italic=True, size=S, align="center", va="bottom")
c.box(270, 34, 50, 26, "press\ncheck", mono=True, size=S, shadow=True)
c.path([(X3 + W2, 30.5), (261, 30.5), (261, 47), (270, 47)])
# ---- decisions, bottom band
AX, AY, AW, AH = 268, 158, 104, 62
ac = AY + AH / 2
c._poly([(AX, AY), (AX + AW / 2, ac), (AX, AY + AH), (AX - AW / 2, ac)], 0)
c.text(AX, ac, "zero suggestions,\nor fewer than\n5 applied?", size=S, align="center")
ex = 295
ey = AY + (AX + AW / 2 - ex) / (AW / 2) * (AH / 2) * -1 + AH / 2
ey = AY + (ex - AX) / (AW / 2) * (AH / 2)
c.arrow(295, 60, ex, ey)
BX, BW, BH = 150, 84, 46
bc = ac
c._poly([(BX, bc - BH / 2), (BX + BW / 2, bc), (BX, bc + BH / 2), (BX - BW / 2, bc)], 0)
c.text(BX, bc, "rounds left?\n(default 2)", size=S, align="center")
c.arrow(AX - AW / 2, ac, BX + BW / 2, ac)
c.text((AX - AW / 2 + BX + BW / 2) / 2, ac - 3, "No", italic=True, size=S, align="center", va="bottom")
# stop
c.box(192, 232, 34, 14, "stop", kind="plain", size=S)
c.path([(AX, AY + AH), (AX, 239), (226, 239)])
c.text(AX + 3, 223, "Yes", italic=True, size=S, align="left", va="top")
c.path([(BX, bc + BH / 2), (BX, 239), (192, 239)])
c.text(BX + 3, bc + BH / 2 + 2, "No", italic=True, size=S, align="left", va="top")
# the loop
c.path([(BX - BW / 2, bc), (X2 + W2 / 2, bc), (X2 + W2 / 2, 153.5)])
c.text(X2 + W2 / 2 + 3, 168, "Yes", italic=True, size=S, align="left", va="top")
c.save(look.figures_dir() / "15-02-editorial-passes-machine.png")
