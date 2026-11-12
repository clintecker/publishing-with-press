"""Figure 13.1: where each registration number goes (archetype 2, data-flow)."""
import look
from _parts import file_icon

c = look.Canvas(318)
BX, BW, BH = 232, 90, 40
TR = 112
ys = [40, 100, 160, 220, 280]

file_icon(c, 52, 30, "config/\nmetadata.yaml", w=22, h=18)
EX0, EY0, EW, EH = 10, 96, 92, 76
c.box(EX0, EY0, EW, EH, kind="plain", fill=20)
c.text(EX0 + 6, EY0 + 6, "registrations:", mono=True, size=7, va="top")
for i, s in enumerate(["isbn.print", "isbn.epub", "lccn", "issn"]):
    c.text(EX0 + 14, EY0 + 21 + i * 12, s, mono=True, size=7, va="top")
c.arrow(52, 66, 52, EY0 - 0.5)  # file to excerpt
mid = EY0 + EH / 2

names = [("copyright page", None), ("EPUB metadata", "content.opf"),
         ("wrap barcode", None), ("ONIX file", "dist/alice.onix.xml"),
         ("PCN listing", "dist/alice-pcn.txt")]
labels = ["isbn.print, isbn.epub,\nlccn, issn",
          "isbn.epub as\nurn:isbn:",
          "isbn.print as\nEAN-13",
          "isbn.print, isbn.epub\nas ProductIDType 15",
          "isbn.print"]
c.path([(EX0 + EW, mid), (TR, mid)], arrow=False)
c.path([(TR, ys[0]), (TR, ys[-1])], arrow=False)
c.dot(TR, mid)
for y, (n, sub), lab in zip(ys, names, labels):
    kind = "file" if sub else "plain"
    c.box(BX, y - BH / 2, BW, BH, n if not sub else n, kind=kind,
          sub=[sub] if sub else None)
    c.arrow(TR, y, BX, y)
    c.dot(TR, y)
    c.text((TR + BX) / 2, y - 3, lab, mono=True, size=7, align="center",
           va="bottom")
# barcode bars inside the wrap barcode box
by = ys[2]
bars = [0, 1.5, 3, 5.5, 7, 9.5, 11, 12.5, 15, 16.5, 19, 20.5, 22, 24.5, 26]
cx0 = BX + BW / 2 - 13
for b in bars:
    c.rule(cx0 + b, by + 4, cx0 + b, by + 15, weight=0.8)
c.save(look.figures_dir() / "13-01-where-numbers-land.png")
