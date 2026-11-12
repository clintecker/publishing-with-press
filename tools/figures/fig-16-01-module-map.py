"""Figure 16.1: the module areas of the press package (archetype 4, layered stack)."""
import look
from matplotlib.patches import Polygon

c = look.Canvas(232)
FX0, FY0, FX1, FY1 = 8, 10, 262, 222
c._poly([(FX0, FY0), (FX1, FY0), (FX1, FY1), (FX0, FY1)], 0, lw=2.6)
c.text(FX0 + 10, FY0, "adapters/", mono=True, size=7, bg=True, allow_small=True)

BX, BW = 16, 190
bands = [
    (30, [("entry and CLI", ["__main__.py", "catalog.py"], BW)]),
    (28, [("desk", None, 56), ("operator and instruments", None, BW - 56)]),
    (28, [("build", None, 42), ("generators", None, 54), ("editorial\nlaw", None, 48),
          ("verifiers", None, 46)]),
    (34, [("print and\ncommerce", None, 52), ("registrations", None, 60), ("art", None, 30),
          ("scaffolding", None, 48)]),
    (30, [("registry", ["registry.py"], BW)]),
    (34, [("book model", ["bookmodel.py, booklib.py"], 126), ("config", None, 64)]),
]
y = 28
for i, (h, cells) in enumerate(bands):
    x = BX
    fill = 10 if i % 2 == 0 else 20
    for label, sub, w in cells:
        c.box(x, y, w, h, label, kind="plain", fill=fill, sub=sub)
        x += w
    y += h
bottom = y
c.box(208, 28, 46, bottom - 28, "trust", kind="plain", fill=0,
      sub=["selftest", "invariants", "receipts"], bold=True)
for ay, lab in [(70, "subprocess"), (120, "os.environ"), (170, "urllib")]:
    c.arrow(256, ay, 316, ay)
    c.text(270, ay - 3, lab, mono=True, size=7, align="left", va="bottom")
c.save(look.figures_dir() / "16-01-module-map.png")
