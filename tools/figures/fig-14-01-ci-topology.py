"""14-01 CI topology: workstation, repository, runner, registry (archetype 5)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import look
from look import Canvas
from matplotlib.patches import Rectangle

c = Canvas(214)
YC = 112

# GitHub boundary, dotted
c.ax.add_patch(Rectangle((100, 8), 220, 198, facecolor="none", edgecolor="black",
                         linewidth=look.BOX_PT, linestyle=(0, (1, 2.5)),
                         zorder=1))
c.text(108, 17, "GitHub", size=8, va="center")

# workstation: monitor with stand
m = c.box(8, YC - 20, 54, 38, "hatter", kind="plain", sub=["alice"])
c.rule(35, YC + 18, 35, YC + 24)
c.rule(25, YC + 24, 45, YC + 24)

# repository cylinder
r = c.box(110, YC - 26, 86, 52, "wonderland-press/\nalice", kind="store", mono=True, size=7)

# runner
run = c.box(248, YC - 20, 66, 40, "printshop", kind="process", sub=["CI runner"])

# registry crate above the runner
reg = c.box(184, 28, 130, 38, "container registry (ghcr.io)", kind="plain",
            sub=["press-toolchain@sha256:..."])

# outputs below
pg = c.box(176, 176, 54, 24, "GitHub\nPages", kind="plain")
rl = c.box(262, 176, 52, 24, "GitHub\nRelease", kind="plain")

# arrows with italic sans labels
c.arrow(m.right[0], YC, r.left[0], YC)
c.text(86, YC - 3, "git push", italic=True, size=7, align="center", va="bottom")
c.arrow(r.right[0], YC, run.left[0], YC)
c.text((r.right[0] + run.left[0]) / 2, YC - 3, "uses\nbuild.yml@v3", italic=True,
       size=7, align="center", va="bottom")
c.arrow(281, reg.y + reg.h, 281, run.y)
c.text(277, (reg.y + reg.h + run.y) / 2, "pull image\nby digest", italic=True,
       size=7, align="right", va="center")
# runner to Pages: down, left, down
c.path([(264, run.y + run.h), (264, 152), (pg.top[0], 152), (pg.top[0], pg.y)])
c.text(222, 149, "deploy pages (main)", italic=True, size=7, align="center",
       va="bottom")
# runner to Release, dashed
c.path([(rl.top[0], run.y + run.h), (rl.top[0], rl.y)], dashed=True)
c.text(rl.top[0] - 4, 164, "publish release\n(tags)", italic=True, size=7,
       align="right", va="center")

c.save(look.figures_dir() / "14-01-ci-topology.png")
