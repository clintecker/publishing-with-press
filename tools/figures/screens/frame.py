"""Grayscale, scale to 1362 px wide (2 px = 0.5 pt rule included), 300 dpi, mode L.
Usage: frame.py site IN OUT
       frame.py desk DESK.png PICKER.png OUT
       frame.py stack FULLPAGE.png OUT CSS_W TOP_Y0 TOP_Y1 BOT_Y0 BOT_Y1
  stack: two crops of one full-page capture (y in CSS px; the capture may be
  at any device scale), the top over the bottom, with a 40 px torn-edge
  gap band between them, so a long page shows its head and its foot."""
import sys
from PIL import Image, ImageOps
W, RULE = 1362, 2
def darkest(im):
    # Grayscale as the darkest channel: neutral grays are unchanged, while
    # coloured terminal text (the green toolchain line, the blue cursor
    # bar) keeps its contrast instead of washing out to a pale luminance.
    r, g, b = im.convert("RGB").split()
    from PIL import ImageChops
    return ImageChops.darker(ImageChops.darker(r, g), b)
def finish(im, out, mode="luma"):
    inner = W - 2 * RULE
    im = darkest(im) if mode == "darkest" else im.convert("L")
    im = im.resize((inner, round(im.height * inner / im.width)), Image.LANCZOS)
    im = ImageOps.expand(im, border=RULE, fill=0)
    assert im.width == W and im.height <= 1740, im.size
    im.save(out, dpi=(300, 300), optimize=True)
    print(out, im.size, im.mode)
def torn(im, edge, amp=5, period=14):
    """White out past a zigzag along the top or bottom edge."""
    from PIL import ImageDraw
    im = im.copy(); d = ImageDraw.Draw(im)
    pts = []
    for i, x in enumerate(range(0, im.width + period, period // 2)):
        off = amp if i % 2 else 0
        pts.append((x, im.height - 1 - amp + off if edge == "bottom" else amp - off))
    if edge == "bottom":
        poly = pts + [(im.width, im.height), (0, im.height)]
    else:
        poly = pts + [(im.width, 0), (0, 0)]
    d.polygon(poly, fill=255)
    return im
if sys.argv[1] == "stack":
    full = Image.open(sys.argv[2]); out = sys.argv[3]
    css_w, ty0, ty1, by0, by1 = (int(a) for a in sys.argv[4:9])
    k = full.width / css_w
    inner = W - 2 * RULE
    def crop(y0, y1):
        c = full.crop((0, round(y0 * k), full.width, round(y1 * k))).convert("L")
        return c.resize((inner, round(c.height * inner / c.width)), Image.LANCZOS)
    top, bot = torn(crop(ty0, ty1), "bottom"), torn(crop(by0, by1), "top")
    GAP = 40
    im = Image.new("L", (inner, top.height + GAP + bot.height), 255)
    im.paste(top, (0, 0)); im.paste(bot, (0, top.height + GAP))
    im = ImageOps.expand(im, border=RULE, fill=0)
    assert im.width == W and im.height <= 1740, im.size
    im.save(out, dpi=(300, 300), optimize=True)
    print(out, im.size, im.mode)
elif sys.argv[1] == "site":
    finish(Image.open(sys.argv[2]), sys.argv[3])
else:
    desk = Image.open(sys.argv[2]).convert("RGB")
    pick = Image.open(sys.argv[3]).convert("RGB")
    # Both rsvg renders share one cell scale (-z 1.5), so the inset keeps
    # the desk's type size. It goes at the right of the artifact table:
    # clear of the published column (ends x~800) and above the toolchain
    # line (y~1080).
    x = desk.width - pick.width - 40
    y = 230
    assert x > 830 and y + pick.height < 1060, (x, y)
    pad = ImageOps.expand(pick, border=8, fill="white")
    desk.paste(pad, (x - 8, y - 8))
    finish(desk, sys.argv[4], mode="darkest")
