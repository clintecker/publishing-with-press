"""14-03 the release state machine in two snaking rows (archetype 8)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import look
from look import Canvas
from matplotlib.patches import Ellipse

c = Canvas(268)
R = 24
Y1, Y2 = 56, 160
XS = [70, 142, 214, 286]


def circle(x, y, name, double=False, fill=0):
    c.ax.add_patch(Ellipse((x, y), 2 * R, 2 * R, facecolor=look.GRAY[fill],
                           edgecolor="black", linewidth=look.BOX_PT, zorder=c._zo()))
    if double:
        c.ax.add_patch(Ellipse((x, y), 2 * R - 5, 2 * R - 5, facecolor="none",
                               edgecolor="black", linewidth=look.BOX_PT, zorder=c._zo()))
    c.text(x, y, name, mono=True, size=7, align="center", va="center")


def hpass(xa, xb, y):
    d = 1 if xb > xa else -1
    c.arrow(xa + d * R, y, xb - d * R, y)
    c.text((xa + xb) / 2, y - 3, "pass", italic=True, size=7, align="center", va="bottom")


# row 1
c.dot(18, Y1, r=2.6)
c.arrow(21, Y1, XS[0] - R, Y1)
for x, n in zip(XS, ["pushed", "tagged", "built", "verified"]):
    circle(x, Y1, n)
glosses = ["release commit\non main", "v3.0.2", "checks run on\nrelease commit",
           "newest run of\neach passes"]
for x, g in zip(XS, glosses):
    c.text(x, Y1 - R - 3, g, italic=True, size=7, align="center", va="bottom")
for a, b in zip(XS, XS[1:]):
    hpass(a, b, Y1)

# bend down at the right, then row 2 right to left
c.arrow(XS[3], Y1 + R, XS[3], Y2 - R)
c.text(XS[3] + 4, 108, "pass", italic=True, size=7, align="left")
names2 = ["contract\nproved", "floating\ntag moved", "release\npublished", "done"]
for x, n in zip(XS[::-1], names2):
    circle(x, Y2, n, double=(n == "done"), fill=10 if n.startswith("floating") else 0)
for a, b in zip(XS[::-1], XS[::-1][1:]):
    hpass(a, b, Y2)
c.text(XS[3], Y2 + R + 4, "pins, digest,\nreceipts", italic=True, size=7, align="center", va="top")
c.text(XS[2], Y2 + R + 4, "v3", mono=True, size=7, align="center", va="top")

# stopped
st = c.box(18, 222, 60, 28, "stopped", kind="plain", shadow=True)
BUS = 236
# fail from built: down, left, down into stopped
c.path([(XS[2], Y1 + R), (XS[2], 112), (34, 112), (34, st.y)])
c.text(176, 109, "fail", italic=True, size=7, align="center", va="bottom")
# fail from verified via the right edge, then the bus; contract proved's
# fail joins that edge with its own arrowhead
c.path([(XS[3] + R, Y1), (318, Y1), (318, BUS), (st.x + st.w, BUS)])
c.arrow(XS[3] + R, Y2, 316, Y2)
c.text(315, 130, "fail", italic=True, size=7, align="right", va="center")
c.text(316, Y2 + 17, "fail", italic=True, size=7, align="right", va="top")
# fail from release published: straight down to the bus
c.arrow(XS[1], Y2 + R, XS[1], BUS - 2)
c.text(XS[1] + 4, 214, "fail", italic=True, size=7, align="left", va="center")
# rerun: dashed, up the left edge, over, into tagged from below
c.path([(st.x, 238), (8, 238), (8, 96), (XS[1], 96), (XS[1], Y1 + R)], dashed=True)
c.text(14, 93, "rerun release.sh", mono=True, size=7, align="left", va="bottom")

c.save(look.figures_dir() / "14-03-release-state-machine.png")
