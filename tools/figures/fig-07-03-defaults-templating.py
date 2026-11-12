"""Figure 7.3: a defaults file before and after rendering (archetype 6, before/after)."""
import look

c = look.Canvas(122)
FW, FH, FY = 156, 62, 22
ax_, bx_ = 6, 165
LH = 9.6
A = ["metadata-file:", "  @book/config/metadata.yaml", "- @press/tex/book-header.tex",
     "- @book/tex/title-page.tex?optional"]
B = ["metadata-file:", "  ~/alice/config/metadata.yaml", "- .../data/tex/book-header.tex",
     "- ~/alice/tex/title-page.tex"]
def frame(x, head, lines, strike):
    c.text(x, 11, head, mono=True, size=7, align="left")
    c.box(x, FY, FW, FH, kind="file")
    for i, s in enumerate(lines):
        y = FY + 9 + i * LH
        t = c.text(x + 4, y, s, mono=True, size=7, align="left")
        if strike and i == 3:
            t.set_color(look.GRAY[40])
            w = len(s) * look.mono_advance_pt(7)
            c.rule(x + 4, y, x + 4 + w, y, weight=look.ARROW_PT)
            c.ax.lines[-1].set_color(look.GRAY[40])
    return FY + 9 + 3 * LH
y3 = frame(ax_, "src/press/data/defaults/pdf.yaml", A, False)
frame(bx_, "build/defaults/pdf.yaml", B, True)
for x, s in ((ax_, "file absent"), (bx_, "dropped")):
    c.text(x + FW - 6, FY + FH - 8, s, italic=True, size=7, align="right")
    c.leader(x + FW - 14, FY + FH - 13, x + FW - 14, y3 + 3)
# one arrow from (a) to (b), below the frames
RY = FY + FH + 16
c.path([(ax_ + 110, FY + FH), (ax_ + 110, RY), (bx_ + 44, RY), (bx_ + 44, FY + FH)])
c.text((ax_ + 110 + bx_ + 44) / 2, RY - 2.5, "render_defaults", mono=True, size=7,
       align="center", va="bottom")
c.text(ax_ + FW / 2, RY + 14, "(a)", size=8, align="center")
c.text(bx_ + FW / 2, RY + 14, "(b)", size=8, align="center")
c.save(look.figures_dir() / "07-03-defaults-templating.png")
