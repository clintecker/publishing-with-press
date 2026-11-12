"""Figure 10.2: the path of an index term (archetype 10, flowchart)."""
import look

c = look.Canvas(262)
CX = 100
BW = 150
L = CX - BW / 2
c.box(L, 8, BW, 22, "config/index-terms.yaml", kind="file", mono=True, size=7)
c.leader(196, 19, L + BW - 2, 19)
c.text(200, 19, "term: Mock Turtle", mono=True, size=7, align="left")
c.arrow(CX, 30, CX, 44)
c.box(L, 44, BW, 30, "strip fenced code, inline\ncode, image lines", kind="plain")
c.arrow(CX, 74, CX, 88)
c.box(L, 88, BW, 30, "match whole words, any case,\nin every chapter and appendix",
      kind="plain")
c.arrow(CX, 118, CX, 132)
DW, DH, DY = 100, 44, 132
dc = DY + DH / 2
c._poly([(CX, DY), (CX + DW / 2, dc), (CX, DY + DH), (CX - DW / 2, dc)], 0)
c.text(CX, dc, "Any hits?", size=8, align="center")
# No: right
c.arrow(CX + DW / 2, dc, 205, dc)
c.text(CX + DW / 2 + 4, dc - 3, "No", italic=True, size=7, align="left", va="bottom")
c.box(205, dc - 11, 110, 22, "build stops", shadow=True)
c.text(260, dc + 21, "gen_index: curated\nterms match nothing\nin the text", mono=True,
       size=7, align="center", va="top")
# Yes: down
c.arrow(CX, DY + DH, CX, 192)
c.text(CX + 4, 184, "Yes", italic=True, size=7, align="left")
c.box(L, 192, BW, 30, "entry: term in bold,\nthen locators 1, 3, A", kind="plain")
c.arrow(CX, 222, CX, 234)
c.box(L, 234, BW, 22, "Appendix A: Index of subjects", kind="file")
c.save(look.figures_dir() / "10-02-index-entry-path.png")
