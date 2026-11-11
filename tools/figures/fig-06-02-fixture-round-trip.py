"""Figure 6.2: a known-bad fixture's round trip (archetype 10, flowchart)."""
import look
from _parts import file_icon

c = look.Canvas(250)
CX = 120
# the fixture file, with its first line inside
fx = c.box(CX - 74, 8, 148, 30, kind="file")
c.text(CX - 68, 17, "tests/known-bad/very-unique.md", mono=True, size=7)
c.text(CX - 68, 29, "<!-- expect: very unique -->", mono=True, size=7)
c.arrow(CX, 38, CX, 52)
c.box(CX - 62, 52, 124, 22, "style audit and jargon lint")
c.arrow(CX, 74, CX, 90)
# diamond
DW, DH, DY = 150, 54, 90
dc = DY + DH / 2
c._poly([(CX, DY), (CX + DW / 2, dc), (CX, DY + DH), (CX - DW / 2, dc)], 0)
c.text(CX, dc, "did the declared\nrule fire?", size=8, align="center")
# yes branch
c.arrow(CX + DW / 2, dc, 262, dc)
c.text(CX + DW / 2 + 3, dc - 3, "Yes", italic=True, size=7, align="left", va="bottom")
c.box(262, dc - 11, 58, 22, "fixture\npasses", kind="plain", size=7)
# no branch
c.arrow(CX, DY + DH, CX, 190)
c.text(CX + 4, 175, "No", italic=True, size=7, align="left")
c.box(10, 190, 220, 40, kind="plain", shadow=True)
c.text(120, 203, "very-unique.md: expected rule 'very unique'", mono=True, size=7, align="center")
c.text(120, 217, "did not fire (no diagnostics at all)", mono=True, size=7, align="center")
c.save(look.figures_dir() / "06-02-fixture-round-trip.png")
