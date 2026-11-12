"""Figure 16.2: the data flow from book repository to release (archetype 2, data-flow)."""
import look

c = look.Canvas(414)
M = look.MONO_PT if hasattr(look, "MONO_PT") else 7
CX = 162


def bus(xs, y):
    c.rule(min(xs), y, max(xs), y, weight=look.ARROW_PT)


# row 1: input files
r1 = [("config/*.yaml", True), ("book/chapters +\nbook/appendices", True),
      ("profiles +\naesthetic +\nfront matter", False)]
bx = [24, 118, 212]
for x, (lab, mono) in zip(bx, r1):
    c.box(x, 8, 88, 34, lab, kind="file", mono=mono, size=7 if mono else 8)
# row 2
r2 = ["bookmodel", "booklib.\nchapter_files", "build/*.tex"]
for x, lab in zip(bx, r2):
    c.box(x, 52, 88, 22, lab, kind="process", mono=True, size=7)
    c.arrow(x + 44, 42, x + 44, 52)
bi = c.box(107, 92, 110, 20, "build.book_inputs", kind="process", mono=True, size=7,
           shadow=True)
tx = [126, 162, 198]
for x, t in zip(bx, tx):
    pts = [(x + 44, 74), (x + 44, 84)]
    if x + 44 != t:
        pts += [(t, 84)]
    pts += [(t, 92)]
    c.path(pts)
# row 3
r3 = [("gen_index", "-> build/generated/"), ("render_defaults", "-> build/defaults/"),
      ("gen_authorities", "-> dist/\nalice-sources.md")]
R3Y, R3H = 128, 34
trunk = (CX, 112)
c.rule(CX, 112, CX, 120, weight=look.ARROW_PT)
bus([68, 256], 120)
for x, (a, b) in zip(bx, r3):
    c.box(x, R3Y, 88, R3H, a + "\n" + b, kind="process", mono=True, size=7)
    c.arrow(x + 44, 120, x + 44, R3Y)
# pandoc
pan = c.box(112, 182, 100, 20, "pandoc + Lua filters", kind="process", mono=True, size=7)
c.path([(68, 162), (68, 172), (130, 172), (130, 182)])
c.path([(162, 162), (162, 182)])
# writers
ws = [("latexmk\n(pdf, print)", 54), ("epub", 28), ("html", 28), ("chunkedhtml", 58),
      ("plain", 32), ("docx", 30)]
x = 24
centers = []
WY, WH = 218, 24
for lab, w in ws:
    c.box(x, WY, w, WH, lab, kind="process", mono=True, size=7)
    centers.append(x + w / 2)
    x += w + 6
c.rule(162, 202, 162, 210, weight=look.ARROW_PT)
bus(centers + [162], 210)
for cx in centers:
    c.arrow(cx, 210, cx, WY)
# converge on dist
CY0 = 268
for cx in centers:
    c.rule(cx, WY + WH, cx, 252, weight=look.ARROW_PT)
bus(centers, 252)
c.rule(162, 252, 162, 252, weight=look.ARROW_PT)
dist = c.box(96, CY0 - 4, 132, 30, "dist/alice.*", kind="store", mono=True, size=7, fill=10)
c.arrow(162, 252, 162, CY0 - 4)
# bypass on the left edge
c.path([(107, 102), (12, 102), (12, CY0 + 11), (96, CY0 + 11)])
c.text(18, CY0 + 8, "markdown, source\n(no pandoc)", mono=True, size=7, align="left", va="bottom")
# sources companion straight to dist
c.path([(300, R3Y + R3H / 2), (314, R3Y + R3H / 2), (314, CY0 + 11), (228, CY0 + 11)])
# verifiers
VY, VH = 316, 22
c.rule(162, CY0 + 26, 162, 302, weight=look.ARROW_PT)
bus([68, 256], 302)
for x, lab in zip(bx, ["verify_pdf", "verify_formats", "verify_archives"]):
    c.arrow(x + 44, 302, x + 44, VY)
    c.box(x, VY, 88, VH, lab, kind="verifier", mono=True, size=7)
bus([68, 256], 348)
for x in bx:
    c.rule(x + 44, VY + VH, x + 44, 348, weight=look.ARROW_PT)
c.box(110, 356, 104, 18, "pages, verify_pages", kind="process", mono=True, size=7)
c.arrow(162, 348, 162, 356)
# CI
c.rule(14, 382, 312, 382, dashed=True)
c.text(14, 379, "CI", italic=True, size=8, align="left", va="bottom")
c.arrow(162, 374, 162, 388)
c.box(82, 388, 160, 20, "upload, tag: Release, main: Pages", kind="process", mono=True, size=7)
c.save(look.figures_dir() / "16-02-end-to-end-data-flow.png")
