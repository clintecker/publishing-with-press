"""Figure 16.3: the trust receipt chain (archetype 4, layered stack)."""
import look

c = look.Canvas(300)
names = ["collection", "unit", "property", "component", "damage", "graph",
         "scenario", "integration", "distribution", "container", "boundary",
         "release"]
BX, BW, BH, GAP, Y0 = 12, 70, 15, 8, 10
n = len(names)
for i, name in enumerate(names):          # i = 0 is the bottom band
    y = Y0 + (n - 1 - i) * (BH + GAP)
    c.box(BX, y, BW, BH, name, kind="plain", fill=10 if i % 2 == 0 else 20)
    if i < n - 1:                          # one unbroken stroke joins each band to the next
        cx = BX + BW / 2
        c.rule(cx, y - GAP, cx, y, weight=look.ARROW_PT)
c.text(BX, Y0 + n * (BH + GAP) - GAP + 8, "a gap anywhere breaks the chain",
       italic=True, size=8, align="left", va="top")
# right column
TX, TW, TH = 92, 62, 24
tiers = [("quality\ntier", 214), ("integration\ntier", 144), ("release\ntier", 74)]
for lab, cy in tiers:
    c.box(TX, cy - TH / 2, TW, TH, lab, kind="process")
AX, AW, AH = 238, 76, 28
asm = c.box(AX, 126, AW, AH, "press.receipts\nassemble", kind="process", mono=True,
            size=7, shadow=True)
c.arrow(TX + TW, 144, AX, 144, "receipt-integration", side="above")
c.path([(TX + TW, 214), (AX + AW / 2, 214), (AX + AW / 2, 126 + AH + 2)])
c.text((TX + TW + AX + AW / 2) / 2, 211, "receipt-quality", mono=True, size=7,
       align="center", va="bottom")
f = c.box(AX, 40, AW, 50, "release-receipt", kind="file", mono=True, size=7,
          sub=["wheel digest", "toolchain digest"])
c.arrow(AX + AW / 2, 126, AX + AW / 2, 92)
c.save(look.figures_dir() / "16-03-trust-tiers.png")
