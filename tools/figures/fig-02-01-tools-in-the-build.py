"""Figure 2.1: where each tool sits in the build (archetype 2, data flow)."""
import look
from _parts import file_icon

c = look.Canvas(292)
PX, EX, HX = 70, 163, 256
file_icon(c, 163, 22, "book/chapters/*.md", w=24, h=18)
c.arrow(163, 46, 163, 76)
c.text(169, 61, "Lua filters", mono=True, size=7)
c.box(133, 76, 60, 22, "pandoc")
# fan-out
c.path([(163, 98), (163, 114)], arrow=False)
c.rule(PX, 114, HX, 114, weight=look.ARROW_PT)
c.box(PX - 30, 134, 60, 22, "LuaLaTeX")
c.arrow(PX, 114, PX, 134)
c.text(PX + 5, 124, "latexmk", mono=True, size=7)
file_icon(c, EX, 142, "alice.epub")
c.arrow(EX, 114, EX, 132)
c.text(EX + 5, 123, "pandoc", mono=True, size=7)
file_icon(c, HX, 142, "reader site", mono=False)
c.arrow(HX, 114, HX, 132)
c.text(HX + 5, 123, "pandoc", mono=True, size=7)
# pdf
c.arrow(PX, 156, PX, 182)
file_icon(c, PX, 190, "alice.pdf")
# converge
c.box(123, 246, 80, 30, "verify", kind="verifier", shadow=True)
c.path([(60, 212), (60, 268), (123, 268)])
c.text(86, 266, "pdftoppm", mono=True, size=7, align="center", va="bottom")
c.path([(82, 212), (82, 256), (123, 256)])
c.text(103, 254, "pdffonts", mono=True, size=7, align="center", va="bottom")
c.path([(EX, 162), (EX, 246)])
c.text(EX + 5, 205, "epubcheck", mono=True, size=7)
c.path([(HX, 162), (HX, 261), (203, 261)])
c.save(look.figures_dir() / "02-01-tools-in-the-build.png")
