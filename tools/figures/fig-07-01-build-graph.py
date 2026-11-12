"""Figure 7.1: the artifact graph the registry declares (archetype 1, pipeline)."""
import look

c = look.Canvas(236)
names = ["pdf", "epub", "html", "markdown", "txt", "docx", "site", "source"]
X, W, H, Y0, STEP = 14, 58, 15, 16, 21
ys = [Y0 + i * STEP + H / 2 for i in range(8)]
PX, PW = 248, 66
top, bot = ys[0] - 10, ys[-1] + 10
pages = c.box(PX, top, PW, bot - top, "pages", kind="plain", shadow=True, mono=True, size=7)
for n, y in zip(names, ys):
    c.box(X, y - H / 2, W, H, n, kind="plain", mono=True, size=7)
    if n == "markdown":
        ym = y
        continue
    c.arrow(X + W, y, PX, y)
# markdown row: its own arrow, and the feed into sources
ys_src = ym + STEP / 2
c.arrow(X + W, ym, PX, ym)
c.box(100, ys_src - H / 2, W, H, "sources", kind="plain", mono=True, size=7)
c.path([(X + W - 8, ym + H / 2), (X + W - 8, ys_src), (100, ys_src)])
c.arrow(100 + W, ys_src, PX, ys_src)
# separate bottom row
RY = bot + 22
c.rule(14, RY - 10, 314, RY - 10, weight=look.BOX_PT)
c.box(X, RY, W, H, "print", kind="plain", mono=True, size=7)
c.box(100, RY, W, H, "coverwrap", kind="plain", mono=True, size=7)
c.arrow(X + W, RY + H / 2, 100, RY + H / 2)
c.text(100 + W / 2, RY + H + 5, "not built by press all", italic=True, size=7,
       align="center", va="top")
c.save(look.figures_dir() / "07-01-build-graph.png")
