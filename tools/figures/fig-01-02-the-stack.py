"""Figure 1.2: the layers under a book (archetype 4, layered stack)."""
import look

c = look.Canvas(222)
names = ["your book", "press", "TeX Live and LuaLaTeX", "pandoc",
         "Python 3.10 or later", "operating system"]
x, w, h, y0 = 12, 205, 32, 12
for i, n in reversed(list(enumerate(names))):
    top = i == 0
    c.box(x, y0 + i * h, w, h, n, kind="plain",
          fill=10 if i % 2 == 0 else 20, shadow=top)
# bracket spanning TeX and pandoc bands
yt, yb = y0 + 2 * h + 3, y0 + 4 * h - 3
bx = x + w + 10
c.rule(bx, yt, bx, yb)
c.rule(bx - 5, yt, bx, yt)
c.rule(bx - 5, yb, bx, yb)
c.rule(bx, (yt + yb) / 2, bx + 6, (yt + yb) / 2)
c.text(bx + 10, (yt + yb) / 2,
       "the toolchain:\npandoc, LuaLaTeX,\nlatexmk, fonts,\nepubcheck, poppler",
       italic=True, size=7, align="left")
c.save(look.figures_dir() / "01-02-the-stack.png")
