"""Figure 8.1: what each verifier inspects (a matrix of filled dots)."""
import look
from matplotlib.patches import Rectangle

ROWS = [("fonts embedded", (1, 5)), ("no blank page", (1, 5)),
        ("no edge ink", (1, 5)), ("trim", (1, 5)),
        ("sentinels", (1, 2, 4, 5)), ("cover on page one", (1,)),
        ("witnesses", (2,)), ("figure labels", (2,)), ("epubcheck", (2,)),
        ("link resolution", (1, 4, 5)), ("archive contents", (3,)),
        ("black ink", (5,)), ("mirrored margins", (5,))]
HEADS = [("verify_pdf", ""), ("verify_", "formats"), ("verify_", "archives"),
         ("verify_", "pages"), ("verify_pdf", "print profile")]
LX, CW, RH = 8.0, 47.0, 13.0
GX = LX + 80.0                       # grid left
HH = 26.0                            # header height
Y0 = 8.0
GY = Y0 + HH
H = GY + RH * len(ROWS) + 8.0
c = look.Canvas(H)
GW = CW * 5
# sentinels row shading first (under everything)
si = [r[0] for r in ROWS].index("sentinels")
c.ax.add_patch(Rectangle((LX, GY + si * RH), GX + GW - LX, RH,
                         facecolor=look.GRAY[10], edgecolor="none", zorder=1.5))
# rules
for i in range(len(ROWS) + 1):
    c.rule(LX, GY + i * RH, GX + GW, GY + i * RH,
           weight=look.BOX_PT if i in (0, len(ROWS)) else 0.3)
c.rule(LX, Y0, GX + GW, Y0)
for j in range(6):
    xx = GX + j * CW
    c.rule(xx, Y0, xx, GY + RH * len(ROWS), weight=look.BOX_PT if j in (0, 5) else 0.3)
c.rule(LX, Y0, LX, GY + RH * len(ROWS))
for j, (a, b) in enumerate(HEADS):
    cx = GX + j * CW + CW / 2
    c.text(cx, Y0 + 4.5 if b else Y0 + 10, a, mono=True, size=7, align="center",
           va="top")
    if b:
        c.text(cx, Y0 + 14.5, b, mono=(j != 4), size=7, align="center", va="top",
               italic=(j == 4))
for i, (name, cols) in enumerate(ROWS):
    cy = GY + i * RH + RH / 2
    c.text(LX + 4, cy, name, size=8)
    for k in cols:
        c.dot(GX + (k - 1) * CW + CW / 2, cy, r=2.4)
c.save(look.figures_dir() / "08-01-what-each-verifier-inspects.png")
