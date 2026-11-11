"""Figure 1.3: three stacked terminal panels (archetype 9, filmstrip)."""
import look
from matplotlib.patches import Rectangle

TITLE = "alice@hatter:~/alice"
COLS = 72
PANELS = [
    ["$ press new alice", "$ cd alice", "$"],
    ["$ press check", "Source checks passed: 1 ordered Markdown files", "...",
     "Editorial checks passed: 1 Markdown files", "..."],
    ["$ ls dist/", "alice-site.zip", "alice-source.zip", "alice.docx",
     "alice.epub", "alice.html", "alice.md", "alice.pdf", "alice.txt",
     "pages", "site"],
]
W = look.MEASURE_PT["full"]
m = look.MARGIN_PX / look.PX_PER_PT + 1.0
gut = 14.0                      # number gutter
pad, bar, gap = 4.0, 15.0, 10.0
fx = m + gut
fw = W - m - fx
adv = look.mono_advance_pt(1.0)
size = min(look.SANS_PT, (fw - 2 * pad) / (COLS * adv))
size = int(size * 20) / 20.0
lh = size * 1.32
hs = [bar + pad + len(p) * lh + pad for p in PANELS]
H = 2 * m + sum(hs) + gap * (len(PANELS) - 1)
c = look.Canvas(H)
y = m
for n, (lines, h) in enumerate(zip(PANELS, hs), 1):
    c.ax.add_patch(Rectangle((fx, y), fw, bar, facecolor=look.GRAY[10],
                             edgecolor="none", zorder=2))
    c.rule(fx, y + bar, fx + fw, y + bar)
    c.ax.add_patch(Rectangle((fx, y), fw, h, facecolor="none",
                             edgecolor=look.BLACK, linewidth=look.BOX_PT,
                             zorder=3))
    c.text(fx + pad, y + bar / 2 + 0.2, TITLE, size=look.SANS_PT - 0.5)
    for i, ln in enumerate(lines):
        c.text(fx + pad, y + bar + pad + i * lh, ln, mono=True, size=size,
               bold=ln.startswith("$"), va="top", allow_small=True)
    # number at the left of the frame
    r = 5.2
    cx = m + gut / 2 - 1
    from matplotlib.patches import Ellipse
    c.ax.add_patch(Ellipse((cx, y + bar / 2), 2 * r, 2 * r, facecolor="white",
                           edgecolor=look.BLACK, linewidth=look.BOX_PT,
                           zorder=4))
    c.text(cx, y + bar / 2 + 0.3, str(n), size=look.SMALL_PT, align="center")
    y += h + gap
c._texts = []
c.save(look.figures_dir() / "01-03-ten-minute-tour.png")
print(f"01-03: mono {size:.2f} pt")
