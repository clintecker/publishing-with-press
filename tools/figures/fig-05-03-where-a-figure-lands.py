"""05-03 where an image line lands in each edition (data-flow, top to bottom)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import look
from look import Canvas

c = Canvas(222)
BW, BG, X0 = 62, 4, 6
cx = [X0 + BW / 2 + k * (BW + BG) for k in range(4)]
mid = (cx[0] + cx[3]) / 2

src = c.box(mid - 60, 8, 120, 32, "image line", kind="file",
            sub=["#fig:alice-heights .chart"])
lua = c.box(mid - 55, 66, 110, 24, "figure-numbering.lua", kind="process",
            mono=True, size=7)
c.arrow(mid, 40, mid, 66)
BUS = 116
c.path([(mid, 90), (mid, BUS)], arrow=False)
c.text(mid + 5, 103, "Figure 5.1", mono=True, size=7, va="center")
c.rule(cx[0], BUS, cx[3], BUS, weight=look.ARROW_PT)
TOP, H = 132, 80
cards = [("PDF", 20, ["caption\nFigure 5.1", "List of\nFigures entry", "link target"]),
         ("EPUB / HTML", 0, ["in-flow,\nFigure 5.1", "link target"]),
         ("reader site", 0, ["in-flow,\nFigure 5.1", "link target"]),
         ("text / DOCX", 0, ["in-flow,\nFigure 5.1"])]
for x, (title, fill, items) in zip(cx, cards):
    c.arrow(x, BUS, x, TOP)
    c.box(x - BW / 2, TOP, BW, H, kind="plain", fill=fill)
    c.text(x, TOP + 9, title, size=8, align="center", bold=True)
    c.rule(x - BW / 2, TOP + 17, x + BW / 2, TOP + 17)
    y = TOP + 24
    for it in items:
        c.text(x, y, it, size=7, align="center", va="top")
        y += 8.6 * (it.count("\n") + 1) + 5

# bare image: its own route to the List of Plates
RX = 297
c.box(RX - 25, 8, 50, 32, "bare image", kind="file", size=7)
c.arrow(RX, 40, RX, TOP, label="no number", side="on")
c.box(RX - 25, TOP, 50, 36, "List of\nPlates", kind="plain", size=8)
c.save(look.figures_dir() / "05-03-where-a-figure-lands.png")
