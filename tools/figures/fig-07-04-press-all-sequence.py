"""Figure 7.4: the press all sequence (archetype 8, state machine)."""
import look
from matplotlib.patches import Ellipse

c = look.Canvas(170)
CY, EH = 62, 28
states = [("check", 30), ("formats", 36), ("source", 32), ("pages", 30), ("verify", 30),
          ("commerce\ngate", 46), ("done", 32)]
G = 10
x = 22
cx = []
for i, (n, w) in enumerate(states):
    cx.append((x + w / 2, w))
    x += w + G
def ell(xc, w, dbl=False):
    c.ax.add_patch(Ellipse((xc, CY), w, EH, facecolor="white", edgecolor="black",
                           linewidth=look.BOX_PT, zorder=c._zo()))
    if dbl:
        c.ax.add_patch(Ellipse((xc, CY), w - 5, EH - 5, facecolor="none", edgecolor="black",
                               linewidth=look.BOX_PT, zorder=c._zo()))
for (n, w), (xc, _) in zip(states, cx):
    ell(xc, w, dbl=(n == "done"))
    c.text(xc, CY, n, mono=True, size=7, align="center")
# start dot and pass arcs
c.dot(10, CY, r=2.8)
c.arrow(13, CY, cx[0][0] - cx[0][1] / 2, CY)
for i in range(6):
    xa = cx[i][0] + cx[i][1] / 2
    xb = cx[i + 1][0] - cx[i + 1][1] / 2
    c.arrow(xa, CY, xb, CY)
    c.text((xa + xb) / 2, CY - 10, "pass", italic=True, size=7, align="center", va="bottom")
# stop box and fail arcs
SX0, SW, SY, SH = 112, 90, 140, 22
c.box(SX0, SY, SW, SH, "stop", kind="plain", shadow=True, mono=True, size=7)
for i in range(6):
    x0, y0 = cx[i][0], CY + EH / 2
    x1 = SX0 + 10 + i * (SW - 20) / 5
    y1 = SY
    pts = []
    for k in range(25):
        t = k / 24
        b = [(x0, y0), (x0, y0 + 36), (x1, y1 - 36), (x1, y1)]
        px = sum(w_ * p[0] for w_, p in zip(((1-t)**3, 3*t*(1-t)**2, 3*t*t*(1-t), t**3), b))
        py = sum(w_ * p[1] for w_, p in zip(((1-t)**3, 3*t*(1-t)**2, 3*t*t*(1-t), t**3), b))
        pts.append((px, py))
    c.path(pts)
    lab = "fail, under\nPRESS_RELEASE" if i == 5 else "fail"
    mid = pts[10]
    c.text(mid[0] + 8, mid[1], lab, italic=True, size=7, align="left")
# notes above the row, with leaders
def note(xc, s, align="center", left=None, right=None):
    y1 = 8
    n = s.count("\n") + 1
    if align == "left":
        c.text(left, y1, s, size=7, align="left", va="top")
    elif align == "right":
        c.text(right, y1, s, size=7, align="right", va="top")
    else:
        c.text(xc, y1, s, size=7, align="center", va="top")
    c.leader(xc, y1 + n * 8.6 + 2, xc, CY - EH / 2 - 0.5)
note(cx[0][0], "source, self-test,\nstyle, jargon", "left", left=9)
note(cx[4][0], "pages, pdf,\nformats, archives")
note(cx[5][0], "advisory unless\nPRESS_RELEASE,\nabsent without ordering", "right", right=318)
c.save(look.figures_dir() / "07-04-press-all-sequence.png")
