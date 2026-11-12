"""14-02 how a book resolves @v3 (archetype 10, flowchart)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import look
from look import Canvas
from matplotlib.patches import Rectangle

c = Canvas(318)
CX = 190

b1 = c.box(CX - 62, 10, 124, 32, "book.yml", kind="process", sub=["uses: .../build.yml@v3"])
c.arrow(CX, b1.y + b1.h, CX, 76)
c.text(CX + 5, 59, "floating tag", italic=True, size=7, align="left")

b2 = c.box(CX - 80, 76, 160, 40, "", kind="process")
c.text(CX, 87, "v3 resolves to the newest v3.x.y", size=8, align="center", va="center")
c.text(CX, 103, "v3.0.2 at the time of writing", italic=True, size=7, align="center", va="center")
c.arrow(CX, b2.y + b2.h, CX, 142)

b3 = c.box(CX - 62, 142, 124, 30, "build.yml at v3.0.2", kind="plain", mono=True, size=7)
c.ax.add_patch(Rectangle((b3.x, b3.y), b3.w, b3.h, facecolor="none", edgecolor="black",
                         linewidth=1.6, zorder=40))

# the pinned-book side box, dashed arrow into build.yml
bk = c.box(8, 143, 76, 28, "a book pinned", kind="process", sub=["@v3.0.2"])
c.arrow(bk.right[0], 157, b3.left[0], 157, dashed=True)

ca = c.box(40, 206, 124, 38, "composite action", kind="process", sub=["clintecker/press@v3.0.2"])
ti = c.box(180, 206, 140, 38, "toolchain image", kind="process", sub=["@sha256:0d784ac0..."])
c.arrow(b3.bottom[0] - 20, b3.y + b3.h, ca.top[0] + 20, ca.y)
c.arrow(b3.bottom[0] + 20, b3.y + b3.h, ti.top[0] - 20, ti.y)

fin = c.box(CX - 66, 276, 132, 32, "the same bytes every time", kind="verifier")
c.arrow(ca.bottom[0] + 20, ca.y + ca.h, fin.top[0] - 30, fin.y)
c.arrow(ti.bottom[0] - 20, ti.y + ti.h, fin.top[0] + 30, fin.y)

c.save(look.figures_dir() / "14-02-resolving-v3.png")
