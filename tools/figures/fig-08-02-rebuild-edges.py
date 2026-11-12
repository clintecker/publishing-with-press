"""Figure 8.2: what each verify target rebuilds first (archetype 2, data flow)."""
import look
from matplotlib.lines import Line2D

arts = ["pdf", "epub", "html", "markdown", "txt", "docx", "site", "source",
        "sources", "coverwrap", "print"]
Y0, P = 38.0, 18.0
IX, IW, IH = 212.0, 14.0, 12.0
row = {n: Y0 + i * P for i, n in enumerate(arts)}
row["coverwrap"] = row["sources"] + 26
row["print"] = row["coverwrap"] + 36
CMD_X, CMD_W, CMD_H = 8.0, 100.0, 22.0
cmds = [("press verify", 38), ("press verify-formats", 76),
        ("press pages", 124), ("press verify-print", 224),
        ("press coverwrap", 268)]

c = look.Canvas(row["print"] + 48)
for n in arts:
    c.box(IX, row[n] - IH / 2, IW, IH, kind="file")
    c.text(IX + IW + 4, row[n], n, mono=True, size=7)
# the Pages bundle, one step past "sources"
ys = row["sources"]
c.arrow(IX + IW + 4 + 7 * 4.22 + 4, ys, 290, ys)
c.box(290, ys - IH / 2, IW, IH, kind="file", fill=10)
c.text(290 + IW / 2, ys + IH / 2 + 3, "pages", mono=True, size=7,
       align="center", va="top")

cy = {}
for label, y in cmds:
    c.box(CMD_X, y - CMD_H / 2, CMD_W, CMD_H, label, mono=True, size=7)
    cy[label] = y
R = CMD_X + CMD_W


def fan(cmd, targets, **kw):
    for t in targets:
        c.arrow(R, cy[cmd], IX - 2, row[t], **kw)


fan("press verify", ["pdf"])
fan("press verify-formats",
    ["epub", "html", "markdown", "site", "txt", "docx", "source"])
fan("press pages", ["pdf", "epub", "html", "markdown", "txt", "docx", "site",
                    "source", "sources"])
fan("press verify-print", ["print"])
c.arrow(R, cy["press verify-print"], IX - 2, row["coverwrap"], dashed=True)
fan("press coverwrap", ["print", "coverwrap"])
c.text(114, 204, "if assets/cover.jpg", mono=True, size=7, va="bottom")

# dotted: formats reads the PDF without rebuilding it
fy = cy["press verify-formats"] - 6
x1, ytop = 128.0, 18.0
pdf_x = IX + IW / 2
for pts in [[(R, fy), (x1, fy), (x1, ytop), (pdf_x, ytop)]]:
    c.ax.add_line(Line2D([p[0] for p in pts], [p[1] for p in pts], color="black",
                         linewidth=look.ARROW_PT, linestyle=(0, (1, 2)),
                         solid_capstyle="butt", zorder=20))
c.path([(pdf_x, ytop), (pdf_x, row["pdf"] - IH / 2 - 1)])
c.text(x1 + 4, ytop - 3, "reads, does not rebuild", mono=True, size=7,
       va="bottom")
c.save(look.figures_dir() / "08-02-rebuild-edges.png")
