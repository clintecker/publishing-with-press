"""Figure 3.2: how press sorts chapter and appendix files (archetype 6)."""
import look
from _tree import tw

FW, FH, G, X0, Y0 = 150, 66, 9, 8, 10
LH = 12.0
frames = {
    "a": dict(head=None, rows=["1-down-the-rabbit-hole.md", "10-the-lobster-quadrille.md",
                                "2-the-pool-of-tears.md"], order="order: 1, 10, 2"),
    "b": dict(head=None, rows=["01-down-the-rabbit-hole.md", "02-the-pool-of-tears.md",
                                "10-the-lobster-quadrille.md"], order="order: 1, 2, 10"),
    "c": dict(head="press add appendix", rows=["a-index-of-subjects.md", "y-glossary.md",
                                               "z-about-the-author.md"], order="index A first"),
    "d": dict(head="press add appendix --front", rows=["a-about-the-author.md", "b-glossary.md",
                                                       "c-index-of-subjects.md"], order="index C last"),
}
c = look.Canvas(Y0 + 2 * (FH + 17) + 2)
for k, (key, f) in enumerate(frames.items()):
    x = X0 + (k % 2) * (FW + G)
    y = Y0 + (k // 2) * (FH + 17)
    c.box(x, y, FW, FH, kind="plain")
    if f["head"]:
        c.text(x + 6, y + 9, f["head"], italic=True, size=7)
    ly = [y + 21 + i * LH for i in range(3)]
    for i, r in enumerate(f["rows"]):
        generated = (key == "c" and i == 0) or (key == "d" and i == 2)
        if key == "a" and i == 1:
            hw = tw("10", mono=True)
            c.box(x + 5.2, ly[i] - 5, hw + 2.2, 10, kind="plain", fill=20)
        if generated:
            w = tw(r, mono=True)
            x0, x1, y0, y1 = x + 4, x + 8 + w, ly[i] - 5.4, ly[i] + 5.4
            for a, b, d, e in ((x0, y0, x1, y0), (x1, y0, x1, y1),
                               (x1, y1, x0, y1), (x0, y1, x0, y0)):
                c.rule(a, b, d, e, dashed=True)
            c.text(x1 + 4, ly[i], "generated", italic=True, size=7)
        c.text(x + 6.5, ly[i], r, mono=True, size=7)
    c.text(x + 6, y + FH - 8, f["order"], size=7)
    if key == "a":
        ex = x + 6.5 + tw(frames["a"]["rows"][1], mono=True) + 4
        c.text(x + 112, ly[2], "sorts too\nearly", italic=True, size=7, va="center")
        c.leader(x + 119, ly[2] - 6, ex + 1, ly[1] + 1)
    c.text(x + FW / 2, y + FH + 3.5, "(" + key + ")", size=8, align="center", va="top")
c.save(look.figures_dir() / "03-02-how-files-sort.png")
