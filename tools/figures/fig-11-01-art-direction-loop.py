"""Figure 11.1: the art-direction loop (archetype 10, flowchart in two rows)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import look
from _parts import folder

c = look.Canvas(168)
T, B = 52, 122           # row centers
# ---- top row, left to right
c.text(38, 6, "book/chapters/\n*.md", mono=True, size=7, align="center", va="top")
c.text(38, 28, "art: directives", italic=True, size=7, align="center", va="top")
f1 = c.box(26, T - 9, 24, 18, kind="file", shadow=True)
c.box(66, T - 14, 46, 28, "press\nfigures")
c.box(124, T - 14, 52, 28, "art-direction\nworkflow")
c.text(212, 12, "art/\ncommissions.md", mono=True, size=7, align="center", va="top")
c.box(200, T - 9, 24, 18, kind="file")
c.box(232, T - 18, 88, 36, "press art commission\npress cover\npress illustrate",
      mono=True, size=7)
c.arrow(50, T, 66, T)
c.arrow(112, T, 124, T)
c.arrow(176, T, 200, T)
c.arrow(224, T, 232, T)
c.text(276, 22, "your API keys", italic=True, size=7, align="center", va="top")
c.arrow(276, 32, 276, T - 18)
# ---- drop and bottom row, right to left
folder(c, 268, B - 10, 24, 20, "build/ and\nart/candidates/")
c.path([(292, T + 18), (292, B - 10)])
c.box(168, B - 14, 46, 28, "press art\naccept")
c.arrow(268, B, 214, B)
c.text(241, B - 2.5, "you choose one", italic=True, size=7, align="center", va="bottom")
folder(c, 124, B - 10, 24, 20, "assets/")
c.arrow(168, B, 148, B)
c.box(66, B - 14, 46, 28, "press art\nenhance")
c.arrow(124, B, 112, B)
c.box(21, B - 14, 34, 28, "the\nbuild")
c.arrow(66, B, 55, B)
c.arrow(38, B - 14, 38, T + 9 + 1)
c.save(look.figures_dir() / "11-01-art-direction-loop.png")
