"""04-01 page anatomy: a 6 x 9 chapter opening page with nine callouts."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import look
from look import Canvas, GRAY
from matplotlib.patches import Rectangle

c = Canvas(405)
PX, PY, PW, PH = 32, 6, 262, 393          # 6 x 9 page, aspect 2:3
c.box(PX, PY, PW, PH, kind="plain")
L, R = PX + 32, PX + PW - 32              # text block 4.54 in of 6 in

def bar(x1, x2, y, h=2.2, fill=20):
    c.ax.add_patch(Rectangle((x1, y - h / 2), x2 - x1, h, facecolor=GRAY[fill],
                             edgecolor="none", zorder=c._zo()))

# chapter title (no running head above it)
c.text(L, 62, "Down the rabbit-hole", size=10, bold=True, va="center")
# first paragraph: three-line drop cap
c.text(L - 0.5, 99, "A", size=24, bold=True, va="baseline")
for i in range(6):
    y = 83 + i * 6.6
    bar(L + 21 if i < 3 else L, R if i < 5 else R - 60, y)
# section heading
bar(L, L + 78, 129, h=3.6, fill=0)
c.ax.patches[-1].set_facecolor("black")
# body text
for i in range(3):
    bar(L, R if i < 2 else R - 40, 143 + i * 6.6)
# blockquote box
c.box(L + 12, 167, R - L - 24, 40, kind="plain")
for i in range(4):
    bar(L + 20, R - 22 - (i % 2) * 22 - (14 if i == 3 else 0), 176 + i * 7.6)
# body
for i in range(2):
    bar(L, R if i < 1 else R - 70, 218 + i * 6.6)
# scene break: staggered field of asterisks 4 / 3 / 4
cx = (L + R) / 2
for row, (n, y) in enumerate([(4, 241), (3, 248.5), (4, 256)]):
    for k in range(n):
        c.text(cx + (k - (n - 1) / 2) * 9, y, "*", size=8, bold=True,
               align="center", va="center")
# body
for i in range(2):
    bar(L, R if i < 1 else R - 50, 272 + i * 6.6)
# numbered figure with caption
c.box(L + 40, 290, R - L - 80, 46, kind="plain")
c.box(L + 62, 298, R - L - 124, 30, kind="plain", fill=20)
c.text(cx, 345, "Figure 1.1", size=7, align="center", va="center")
# body, then footnote rule and two small lines
for i in range(2):
    bar(L, R if i < 1 else R - 60, 358 + i * 6.6)
c.rule(L, 374, L + 36, 374)
bar(L, R - 24, 380, h=1.8)
bar(L, R - 90, 385, h=1.8)
# folio, centred at the foot
c.text(cx, 391, "1", size=7, align="center", va="center")

# callouts
LX, RX = 14, 313
c.callout(2, LX, 62, L - 2, 62)
c.callout(3, LX, 86, L + 5, 90)
c.callout(5, LX, 129, L - 2, 129)
c.callout(9, LX, 378, L - 2, 380)
c.callout(1, LX, 391, cx - 5, 391)
c.callout(4, RX, 112, R - 3, 109.5)
c.callout(6, RX, 186, R - 14, 186)
c.callout(7, RX, 249, cx + 27, 249)
c.callout(8, RX, 313, R - 38, 313)

c.save(look.figures_dir() / "04-01-page-anatomy.png")
