"""12-03 the print pack as a pipeline (two rows, press publish a side branch)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import look
from look import Canvas

c = Canvas(218)
BY, BH = 29, 28
YC = BY + BH / 2


def file_under(cx, top, label, w=16, h=14):
    c.box(cx - w / 2, top, w, h, label, kind="file", label_below=True, mono=True, size=7)


# far left: two stacked file icons merging into the first box
fx = 36
c.box(fx - 11, 8, 22, 14, "print\nprofile", kind="file", label_below=True, size=7)
c.box(fx - 11, 46, 22, 14, "build/\nprint-assets/", kind="file", label_below=True, mono=True, size=7)
c.path([(fx + 11, 15), (56, 15), (56, YC)], arrow=False)
c.path([(fx + 11, 53), (56, 53), (56, YC)], arrow=False)

b1 = c.box(68, BY, 44, BH, "print\ninterior", kind="process")
c.arrow(56, YC, 68, YC)
b2 = c.box(126, BY, 69, BH, "verify_pdf\n--profile print", kind="verifier", mono=True, size=7)
c.arrow(b1.right[0], YC, b2.left[0], YC)
b3 = c.box(207, BY, 46, BH, "gen_\ncoverwrap", kind="process", mono=True, size=7)
c.arrow(b2.right[0], YC, b3.left[0], YC)
b4 = c.box(265, BY, 46, BH, "verify_\ncoverwrap", kind="verifier", mono=True, size=7)
c.arrow(b3.right[0], YC, b4.left[0], YC)

# files under the boxes
for b, name in ((b1, "dist/\nalice-interior.pdf"), (b3, "dist/\nalice-coverwrap.pdf")):
    cx = (b.left[0] + b.right[0]) / 2
    c.rule(cx, BY + BH, cx, 66, weight=look.LEADER_PT)
    file_under(cx, 66, name)
# cover input from above
cx3 = (b3.left[0] + b3.right[0]) / 2
c.text(cx3, 10, "assets/cover.jpg", mono=True, size=7, align="center", va="center")
c.arrow(cx3, 15, cx3, BY)

# row 2: edition manifest -> qualification -> commerce gate; press publish aside
R2, RH = 126, 34
R2C = R2 + RH / 2
m = c.box(10, R2, 72, RH, "edition manifest", kind="process", sub=["edition_id"])
q = c.box(96, R2, 62, RH, "qualification", kind="process")
g = c.box(172, R2, 56, RH, "commerce\ngate", kind="process", shadow=True)
c.arrow(m.right[0], R2C, q.left[0], R2C)
c.arrow(q.right[0], R2C, g.left[0], R2C)
qcx = (q.left[0] + q.right[0]) / 2
c.rule(qcx, R2 + RH, qcx, 168, weight=look.LEADER_PT)
file_under(qcx, 168, "config/\nqualification.yaml")

# wrap from verify_coverwrap to the manifest: down, left, down
BUS = 114
c.path([(276, BY + BH), (276, BUS), ((m.left[0] + m.right[0]) / 2, BUS),
        ((m.left[0] + m.right[0]) / 2, R2)])
# side branch: press publish
pp = c.box(266, R2, 44, RH, "press\npublish", kind="process", mono=True, size=7)
c.arrow((pp.left[0] + pp.right[0]) / 2 + 11, BY + BH, (pp.left[0] + pp.right[0]) / 2 + 11, R2)
pcx = (pp.left[0] + pp.right[0]) / 2
c.rule(pcx, R2 + RH, pcx, 168, weight=look.LEADER_PT)
file_under(pcx, 168, "dist/\npublish-kdp.md")

c.save(look.figures_dir() / "12-03-print-pack-graph.png")
