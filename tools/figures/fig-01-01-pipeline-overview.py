"""Figure 1.1: from the manuscript to dist/ (archetype 1, pipeline)."""
import look
from _parts import file_icon, folder

c = look.Canvas(312)
FX = 244          # file column centre
# inputs
file_icon(c, 39, 118, "book/chapters/\n*.md", w=22, h=18)
file_icon(c, 39, 164, "config/*.yaml", w=22, h=18)
chk = c.box(84, 133, 52, 34, "press check")
pan = c.box(148, 133, 60, 34, "pandoc", sub=["+ Lua filters"])
c.path([(50, 118), (72, 118), (72, 150)], arrow=False)
c.path([(50, 164), (72, 164), (72, 150)], arrow=False)
c.arrow(72, 150, 84, 150)
c.arrow(136, 150, 148, 150)
# upper branch
lua = c.box(148, 42, 60, 22, "LuaLaTeX")
c.arrow(178, 133, 178, 64)
c.text(183, 98, "latexmk", mono=True, size=7)
file_icon(c, FX, 53, "alice.pdf")
c.arrow(208, 53, 234, 53)
# writers branch
ys = [108, 140, 172, 204, 236]
for y, n in zip(ys, ["alice.epub", "alice.html", "site/", "alice.txt",
                     "alice.docx"]):
    file_icon(c, FX, y, n)
    c.arrow(218, y, 234, y)
c.rule(218, ys[0], 218, ys[-1], weight=look.ARROW_PT)
c.path([(178, 167), (178, 190), (218, 190)], arrow=False)
c.text(173, 179, "pandoc\nwriters", mono=True, size=7, align="right")
# stitch
file_icon(c, FX, 276, "alice.md")
c.path([(39, 194), (39, 276), (234, 276)])
c.dot(39, 194)
c.text(135, 272, "stitch", mono=True, size=7, align="center", va="bottom")
# verifiers
ver = c.box(279, 144, 41, 32, "verifiers", kind="verifier", shadow=True)
c.rule(270, 53, 270, 276, weight=look.ARROW_PT)
for y in [53] + ys + [276]:
    c.rule(254, y, 270, y, weight=look.ARROW_PT)
c.arrow(270, 160, 279, 160)
c.arrow(299.5, 176, 299.5, 204)
folder(c, 289, 206, 22, 16, "dist/")
c.save(look.figures_dir() / "01-01-pipeline-overview.png")
