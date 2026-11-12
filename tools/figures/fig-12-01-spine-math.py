"""12-02 spine math by provider (matrix)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import look
from look import Canvas

ROWS = [
    ("house", "constant", "pages x caliper / white 0.002252 / cream 0.0025", "0.0"),
    ("kdp", "constant", "pages x caliper / white 0.002252, cream 0.0025 / std-color 0.002252, prem-color 0.002347", "0.06"),
    ("lulu paperback", "divisor", "pages / 444", "0.06"),
    ("lulu hardcover", "lookup", "26 bands / 24-84 pp 0.25in ... 779-800 pp 2.0625in", ""),
    ("ingramspark", "ppi-table", "pages / ppi / cream 444, white 512 / white-70 377, groundwood 400", ""),
]
BREAKS = {
    "house": ["pages x caliper /", "white 0.002252 /", "cream 0.0025"],
    "kdp": ["pages x caliper /", "white 0.002252,", "cream 0.0025 /", "std-color 0.002252,", "prem-color 0.002347"],
    "lulu paperback": ["pages / 444"],
    "lulu hardcover": ["26 bands /", "24-84 pp 0.25in ...", "779-800 pp 2.0625in"],
    "ingramspark": ["pages / ppi /", "cream 444, white 512 /", "white-70 377, groundwood 400"],
}
X0, X1 = 10, 317
LABW = 70
rest = X1 - X0 - LABW
cw = [rest * 0.20, rest * 0.55, rest * 0.25]
xs = [X0, X0 + LABW]
for w in cw:
    xs.append(xs[-1] + w)
adv = look.mono_advance_pt(7)
PAD, LH = 5, 7 * look.LINE_SPACING


def wrap(text, width):
    lines, cur = [], ""
    for tok in text.split(" "):
        t = (cur + " " + tok).strip()
        if len(t) * adv <= width - 2 * PAD + 6 or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = tok
    lines.append(cur)
    return lines


# the formula column breaks after a slash when it can
def wrap_formula(text, width):
    segs = text.split(" / ")
    units = [sg + " /" for sg in segs[:-1]] + [segs[-1]]
    lines, cur = [], ""
    for u in units:
        parts = wrap(u, width) if len(u) * adv > width - 2 * PAD + 6 else [u]
        for k, part in enumerate(parts):
            t = (cur + " " + part).strip() if k == 0 else part
            if k == 0 and cur and len(t) * adv <= width - 2 * PAD + 6:
                cur = t
            else:
                if cur:
                    lines.append(cur)
                cur = part
    lines.append(cur)
    return lines


HEAD = 17
heights = []
cells = []
for r in ROWS:
    f = BREAKS[r[0]]
    cells.append(f)
    heights.append(max(len(f), 1) * LH + 2 * PAD + 1)
Y0 = 8
H = HEAD + sum(heights)
c = Canvas(Y0 + H + 8)
c.box(xs[0], Y0, xs[-1] - xs[0], HEAD, kind="plain", fill=10)
for i, t in enumerate(["spine shape", "formula or table", "allowance"]):
    c.text(xs[i + 1] + PAD, Y0 + HEAD / 2, t, size=7)
c.box(xs[0], Y0, xs[-1] - xs[0], H, kind="plain")
for x in xs[1:-1]:
    c.rule(x, Y0, x, Y0 + H)
y = Y0 + HEAD
for r, f, h in zip(ROWS, cells, heights):
    c.rule(xs[0], y, xs[-1], y)
    cy = y + h / 2
    c.text(xs[0] + PAD, cy, r[0], mono=True, size=7)
    c.text(xs[1] + PAD, cy, r[1], size=8)
    top = cy - len(f) * LH / 2
    for k, ln in enumerate(f):
        c.text(xs[2] + PAD, top + k * LH, ln, mono=True, size=7, va="top")
    if r[3]:
        c.text(xs[3] + PAD, cy, r[3], mono=True, size=7)
    y += h
c.save(look.figures_dir() / "12-01-spine-math.png")
