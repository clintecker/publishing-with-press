"""Figure 8.3: a press verify run that fails on a missing sentinel (terminal).

terminal.py cannot grey individual lines or drop the bold prompt, so this
draws the same panel on the Canvas.
"""
import look
from matplotlib.patches import Rectangle

LINES = [("$ press verify", 40), ("...", 40),
         ("missing text sentinel in PDF: Twinkle, twinkle, little bat", 0)]
W = look.MEASURE_PT["full"]
m = look.MARGIN_PX / look.PX_PER_PT + 1.0
pad, bar, size = 6.0, 15.0, look.SANS_PT
lh = size * 1.6
H = m + bar + pad + len(LINES) * lh + pad + m
c = look.Canvas(H)
x0, y0, fw, fh = m, m, W - 2 * m, H - 2 * m
c.ax.add_patch(Rectangle((x0, y0), fw, bar, facecolor=look.GRAY[10],
                         edgecolor="none", zorder=2))
c.rule(x0, y0 + bar, x0 + fw, y0 + bar)
c.ax.add_patch(Rectangle((x0, y0), fw, fh, facecolor="none",
                         edgecolor=look.BLACK, linewidth=look.BOX_PT, zorder=3))
c.text(x0 + pad, y0 + bar / 2 + 0.2, "alice@hatter", size=look.SANS_PT - 0.5)
for i, (s, g) in enumerate(LINES):
    t = c.text(x0 + pad, y0 + bar + pad + i * lh, s, mono=True, size=size,
               va="top")
    if g:
        t.set_color(look.GRAY[g])
c._texts = []
c.save(look.figures_dir() / "08-03-verify-run.png")
