"""Figure 10.1: how config becomes the front matter (archetype 2, data-flow)."""
import look
from _parts import file_icon

c = look.Canvas(410)
PX, PW, PH = 246, 68, 24
TX = 96          # arrow start
TR = 90          # trunk
c.text(PX + PW / 2, 14, "generated", italic=True, size=7, align="center")


def lab(y, s):
    c.text((TX + PX) / 2 + 4, y - 2, s, mono=True, size=7, align="center",
           va="bottom")


# sources
file_icon(c, 46, 44, "config/\nmetadata.yaml", w=22, h=18)
file_icon(c, 46, 140, "config/\nfront-matter.yaml", w=22, h=18)
# row 1 title page
c.box(PX, 44 - PH / 2, PW, PH, "title page", kind="plain", fill=20)
c.arrow(57, 44, PX, 44)
lab(44, "title, subtitle, author,\npublisher-place, date")
# row 2 copyright page (two inputs)
c.box(PX, 90, PW, 58, "copyright page", kind="plain")
c.path([(TR, 44), (TR, 104)], arrow=False)
c.dot(TR, 44)
c.arrow(TR, 104, PX, 104)
lab(104, "copyright, publisher,\npublisher-place, date")
c.arrow(57, 140, PX, 140)
lab(140, "edition-note, rights-notice,\nmanufacture, contact,\ncolophon-note, motto")
# rows 3-5
rows = [(176, "dedication", "dedication"),
        (222, "epigraph", "epigraph.quote,\nepigraph.attribution"),
        (262, "acknowledgments", "acknowledgements")]
c.path([(TR, 140), (TR, 262)], arrow=False)
c.dot(TR, 140)
for y, name, keys in rows:
    c.box(PX, y - PH / 2, PW, PH, name, kind="plain", size=7.5 if len(name) > 12 else 8)
    c.arrow(TR, y, PX, y)
    lab(y, keys)
    c.dot(TR, y)
# second group
BY0, BY1 = 292, 400
c.box(240, BY0, 80, BY1 - BY0, kind="plain", fill=10)
c.text(280, BY0 + 9, "from elsewhere", italic=True, size=7, align="center")
ys = [322, 352, 382]
for y, n in zip(ys, ["Contents", "List of Plates", "List of Figures"]):
    c.box(PX, y - 11, PW, 22, n, kind="plain", size=7.5 if len(n) > 12 else 8)
c.box(100, ys[0] - 11, 62, 22, "pandoc toc")
c.arrow(162, ys[0], PX, ys[0], dashed=True)
c.box(100, 367 - 11, 62, 22, "TeX header")
JX = 200
c.path([(162, 367), (JX, 367)], arrow=False, dashed=True)
c.path([(JX, ys[1]), (JX, ys[2])], arrow=False, dashed=True)
c.arrow(JX, ys[1], PX, ys[1], dashed=True)
c.arrow(JX, ys[2], PX, ys[2], dashed=True)
c.save(look.figures_dir() / "10-01-config-to-front-matter.png")
