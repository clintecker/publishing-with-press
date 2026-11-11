"""Figure 2.3: workstation versus toolchain image (archetype 5, topology)."""
import look
from _parts import folder

c = look.Canvas(196)
# monitor
c.ax.add_patch(look.Rectangle((26, 62), 52, 36, facecolor=look.GRAY[10],
                              edgecolor=look.BLACK, linewidth=look.BOX_PT,
                              zorder=3))
c.rule(52, 98, 52, 105)
c.rule(42, 106, 62, 106)
c.text(52, 80, "hatter", size=8, align="center")
c.text(52, 114, "native toolchain", size=8, align="center", va="top")
# may lack
c.box(14, 136, 76, 42, "", kind="plain")
c.text(52, 142, "may lack", italic=True, size=7, align="center", va="top")
c.text(52, 155, "epubcheck\njava", mono=True, size=7, align="center", va="top")
# repository
c.box(136, 56, 56, 66, "~/alice", kind="store", mono=True, size=7)
c.text(164, 128, "book repository", size=8, align="center", va="top")
# arrows
c.arrow(136, 74, 90, 74)
c.text(113, 71, "chapters\nand config", mono=True, size=7, align="center",
       va="bottom")
c.arrow(90, 94, 136, 94)
c.text(113, 97, "dist/", mono=True, size=7, align="center", va="top")
# image box
c.box(238, 62, 84, 86, "", kind="process")
cx = 280
c.box(cx - 8, 68, 16, 12, "", kind="plain")
c.rule(cx - 8, 72, cx + 8, 72)
c.rule(cx - 8, 76, cx + 8, 76)
c.text(cx, 86, "toolchain image", size=8, align="center", va="top")
c.text(cx, 100, "ghcr.io/\nclintecker/\npress-toolchain\n@sha256:...",
       mono=True, size=7, align="center", va="top")
c.text(cx, 154, "Ubuntu 24.04,\namd64 and arm64", size=8, align="center",
       va="top")
c.path([(192, 90), (238, 90)])
c.path([(238, 90), (192, 90)])
c.text(215, 87, "mounted\nat /book", mono=True, size=7, align="center",
       va="bottom")
c.path([(cx, 14), (cx, 62)], dashed=True)
c.text(cx - 6, 36, "docker pull\n(anonymous)", mono=True, size=7, align="right")
c.save(look.figures_dir() / "02-03-local-versus-container.png")
