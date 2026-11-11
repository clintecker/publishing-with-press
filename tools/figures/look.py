"""The house look for every figure in *Publishing with Press*.

Every fig-*.py script and terminal.py imports this module and nothing else
decides how a figure looks.  See tools/figures/README.md for the API.

FONT CHOICE (recorded here on purpose)
    Sans:  Helvetica  (/System/Library/Fonts/Helvetica.ttc, faces extracted
           to tools/figures/.fontcache so matplotlib can address the
           regular, bold, and oblique faces individually)
    Mono:  Menlo      (/System/Library/Fonts/Menlo.ttc, same treatment)
    Fallbacks, in order: Arial / Courier New, then DejaVu Sans / DejaVu
    Sans Mono (matplotlib ships DejaVu).  The chosen files are printed by
    `python3 tools/figures/look.py`.

UNITS
    Canvas coordinates are typographic points at FINAL PRINT SIZE, origin at
    the top left, y growing downward.  The house text block is 4.54 in, so a full-measure
    figure is 326.9 pt wide (1362 px), half 163.4 pt (680 px), third 109 pt
    (455 px); height is capped at 1740 px; at 300 dpi one point is 4.1667 px,
    so a 0.5 pt stroke is 2 px and 8 pt text is 33 px high.  Nothing is ever
    scaled after rendering.
"""
from __future__ import annotations

import math
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
from matplotlib import font_manager as fm  # noqa: E402
from matplotlib.figure import Figure  # noqa: E402
from matplotlib.backends.backend_agg import FigureCanvasAgg  # noqa: E402
from matplotlib.patches import Ellipse, FancyBboxPatch, Polygon, Rectangle  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from PIL import Image  # noqa: E402

# ---------------------------------------------------------------- constants
DPI = 300
PX_PER_PT = DPI / 72.0
FULL_PX, HALF_PX, THIRD_PX = 1362, 680, 455   # 4.54 in text block
MAX_H_PX = 1740
MARGIN_PX = 12
MEASURE_PX = {"full": FULL_PX, "half": HALF_PX, "third": THIRD_PX}
MEASURE_PT = {k: v / PX_PER_PT for k, v in MEASURE_PX.items()}

BLACK = "#000000"
WHITE = "#ffffff"
GRAY = {0: "#ffffff", 10: "#e6e6e6", 20: "#cccccc", 40: "#999999"}

BOX_PT = 0.5      # box strokes
ARROW_PT = 0.75   # arrow strokes
LEADER_PT = 0.5   # callout leaders
ARROW_LEN = 5.0   # arrowhead length, pt
ARROW_WID = 3.4   # arrowhead width, pt
SANS_PT = 8.0
SMALL_PT = 7.0    # smallest sanctioned size
MONO_PT = 7.0
LINE_SPACING = 1.22

_HERE = Path(__file__).resolve().parent
_CACHE = _HERE / ".fontcache"

# ------------------------------------------------------------------- fonts
_TTC = {
    "Helvetica": ("/System/Library/Fonts/Helvetica.ttc",
                  {"regular": "Helvetica", "bold": "Helvetica Bold",
                   "italic": "Helvetica Oblique"}),
    "Menlo": ("/System/Library/Fonts/Menlo.ttc",
              {"regular": "Menlo Regular", "bold": "Menlo Bold",
               "italic": "Menlo Italic"}),
}


def _extract(family: str, style: str):
    path, names = _TTC[family]
    if not os.path.exists(path):
        return None
    out = _CACHE / f"{family}-{style}.ttf"
    if not out.exists():
        from fontTools.ttLib import TTCollection
        _CACHE.mkdir(exist_ok=True)
        for f in TTCollection(path).fonts:
            if f["name"].getDebugName(4) == names[style]:
                f.save(str(out))
                break
        else:
            return None
    return str(out)


def _plain(candidates, style):
    """Fallback: a plain .ttf found by family name."""
    weight = "bold" if style == "bold" else "normal"
    fstyle = "italic" if style == "italic" else "normal"
    for fam in candidates:
        try:
            return fm.findfont(fm.FontProperties(family=fam, weight=weight,
                                                 style=fstyle),
                               fallback_to_default=False)
        except Exception:
            continue
    return fm.findfont("DejaVu Sans")


def _font_files(family, style, fallbacks):
    return _extract(family, style) or _plain(fallbacks, style)


SANS = {s: _font_files("Helvetica", s, ["Arial", "DejaVu Sans"])
        for s in ("regular", "bold", "italic")}
MONO = {s: _font_files("Menlo", s, ["Courier New", "DejaVu Sans Mono"])
        for s in ("regular", "bold", "italic")}
SANS_NAME = "Helvetica" if "Helvetica" in SANS["regular"] else "fallback"
MONO_NAME = "Menlo" if "Menlo" in MONO["regular"] else "fallback"


def fontprops(mono=False, italic=False, bold=False, size=SANS_PT):
    table = MONO if mono else SANS
    style = "bold" if bold else ("italic" if italic else "regular")
    return fm.FontProperties(fname=table[style], size=size)


def mono_advance_pt(size):
    """Advance width of one monospace character at `size` pt."""
    from fontTools.ttLib import TTFont
    f = TTFont(MONO["regular"])
    return f["hmtx"]["M"][0] / f["head"].unitsPerEm * size


# --------------------------------------------------------------- post-process
def finish_png(img: Image.Image, path, measure="full"):
    """Force the house output format: 8-bit grayscale, exact width, 300 dpi.

    Narrower images are padded with white (never enlarged); wider ones are an
    error, because rescaling would break the stroke weights.
    """
    target = MEASURE_PX[measure]
    if img.mode in ("RGBA", "LA", "P"):
        bg = Image.new("RGBA", img.size, "white")
        img = Image.alpha_composite(bg, img.convert("RGBA"))
    img = img.convert("L")
    if img.width > target:
        raise ValueError(f"image is {img.width} px wide, over the {target} px "
                         f"{measure} measure; redraw it narrower")
    if img.width < target:
        canvas = Image.new("L", (target, img.height), 255)
        canvas.paste(img, ((target - img.width) // 2, 0))
        img = canvas
    if img.height > MAX_H_PX:
        raise ValueError(f"image is {img.height} px tall, over the "
                         f"{MAX_H_PX} px maximum")
    _check_margin(img, str(path))
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    img.save(path, format="PNG", dpi=(DPI, DPI), optimize=True)
    return img


def _check_margin(img, name):
    """Nothing touches the frame: ink must stay MARGIN_PX from every edge."""
    inv = img.point(lambda v: 255 if v < 250 else 0)
    box = inv.getbbox()
    if box is None:
        return
    l, t, r, b = box
    w, h = img.size
    if l < MARGIN_PX or t < MARGIN_PX or w - r < MARGIN_PX or h - b < MARGIN_PX:
        raise ValueError(
            f"{name}: ink touches the {MARGIN_PX}px margin "
            f"(left {l}, top {t}, right {w - r}, bottom {h - b})")


# ------------------------------------------------------------------ Canvas
class Box:
    """A drawn shape with named anchors, all in canvas points."""

    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h

    left = property(lambda s: (s.x, s.y + s.h / 2))
    right = property(lambda s: (s.x + s.w, s.y + s.h / 2))
    top = property(lambda s: (s.x + s.w / 2, s.y))
    bottom = property(lambda s: (s.x + s.w / 2, s.y + s.h))
    center = property(lambda s: (s.x + s.w / 2, s.y + s.h / 2))


class Canvas:
    """A matplotlib drawing surface in points at final print size."""

    def __init__(self, height_pt, measure="full"):
        self.measure = measure
        self.W = MEASURE_PT[measure]
        self.H = float(height_pt)
        px_h = math.ceil(self.H * PX_PER_PT)
        self.fig = Figure(figsize=(MEASURE_PX[measure] / DPI, px_h / DPI),
                          dpi=DPI, facecolor=WHITE)
        self.canvas = FigureCanvasAgg(self.fig)
        self.H = px_h / PX_PER_PT
        self.ax = self.fig.add_axes([0, 0, 1, 1])
        self.ax.set_xlim(0, self.W)
        self.ax.set_ylim(self.H, 0)
        self.ax.axis("off")
        self._texts = []
        self._z = 1

    def _zo(self):
        self._z += 1
        return self._z

    # ---- shapes
    def _poly(self, pts, fill, lw=BOX_PT, closed=True, z=None):
        p = Polygon(pts, closed=closed, facecolor=GRAY[fill], edgecolor=BLACK,
                    linewidth=lw, joinstyle="miter", zorder=z or self._zo())
        self.ax.add_patch(p)

    def box(self, x, y, w, h, label="", kind="process", fill=0, shadow=False,
            mono=False, sub=None, label_below=False, size=None, bold=False):
        """Draw a labelled shape and return its Box (for anchors).

        kind: process  rounded rectangle (programs, processes)
              file     square, dog-eared corner (files, artifacts)
              store    cylinder (a repository, a disk)
              verifier square with a thin double rule
              plain    square, single rule (generic data / layers)
        fill: 0, 10, 20 or 40 percent gray.
        sub:  list of small monospace lines under the label.
        label_below: put the label under the shape (file icons).
        """
        if fill not in GRAY:
            raise ValueError("fill must be 0, 10, 20 or 40")
        if shadow:
            self._shape(kind, x + 2, y + 2, w, h, 40 if fill != 40 else 0,
                        shadow_pass=True)
        self._shape(kind, x, y, w, h, fill)
        size = size or SANS_PT
        cx = x + w / 2
        if label_below:
            self.text(cx, y + h + 3, label, mono=mono, size=size,
                      align="center", va="top")
        elif label or sub:
            lines_h = 0
            n_main = label.count("\n") + 1 if label else 0
            main_h = n_main * size * LINE_SPACING if label else 0
            sub_h = len(sub or []) * MONO_PT * LINE_SPACING
            total = main_h + sub_h
            ty = y + h / 2 - total / 2
            if kind == "store":
                ty += 3
            if label:
                self.text(cx, ty, label, mono=mono, size=size, align="center",
                          va="top", bold=bold)
            for i, line in enumerate(sub or []):
                self.text(cx, ty + main_h + i * MONO_PT * LINE_SPACING + 0.5,
                          line, mono=True, size=MONO_PT, align="center",
                          va="top")
        return Box(x, y, w, h)

    def _shape(self, kind, x, y, w, h, fill, shadow_pass=False):
        z = self._zo()
        fc, lw = GRAY[fill], BOX_PT
        if kind == "process":
            r = min(4.5, h / 3, w / 3)
            self.ax.add_patch(FancyBboxPatch(
                (x + r, y + r), w - 2 * r, h - 2 * r,
                boxstyle=f"round,pad={r},rounding_size={r}", facecolor=fc,
                edgecolor=BLACK, linewidth=lw, zorder=z))
        elif kind in ("plain", "verifier"):
            self.ax.add_patch(Rectangle((x, y), w, h, facecolor=fc,
                                        edgecolor=BLACK, linewidth=lw,
                                        zorder=z))
            if kind == "verifier" and not shadow_pass:
                g = 2.2
                self.ax.add_patch(Rectangle((x + g, y + g), w - 2 * g,
                                            h - 2 * g, facecolor="none",
                                            edgecolor=BLACK, linewidth=lw,
                                            zorder=z))
        elif kind == "file":
            d = min(7.0, w / 3, h / 3)   # dog-ear size
            self._poly([(x, y), (x + w - d, y), (x + w, y + d), (x + w, y + h),
                        (x, y + h)], fill, z=z)
            if not shadow_pass:
                self._poly([(x + w - d, y), (x + w - d, y + d), (x + w, y + d)],
                           20 if fill < 20 else 40, z=z)
        elif kind == "store":
            e = min(5.0, h / 4)          # ellipse half-height
            cx = x + w / 2
            kw = dict(edgecolor=BLACK, linewidth=lw)
            self.ax.add_patch(Ellipse((cx, y + h - e), w, 2 * e, facecolor=fc,
                                      zorder=z, **kw))
            self.ax.add_patch(Rectangle((x, y + e), w, h - 2 * e, facecolor=fc,
                                        edgecolor="none", zorder=z + 0.1))
            for xx in (x, x + w):
                self.ax.add_line(Line2D([xx, xx], [y + e, y + h - e],
                                        color=BLACK, linewidth=lw,
                                        zorder=z + 0.2, solid_capstyle="butt"))
            self.ax.add_patch(Ellipse((cx, y + e), w, 2 * e, facecolor=fc,
                                      zorder=z + 0.3, **kw))
        else:
            raise ValueError(f"unknown kind {kind!r}")

    # ---- lines
    def rule(self, x1, y1, x2, y2, weight=BOX_PT, dashed=False, fill=None):
        self.ax.add_line(Line2D(
            [x1, x2], [y1, y2], color=BLACK, linewidth=weight,
            linestyle=(0, (4, 3)) if dashed else "-",
            solid_capstyle="butt", dash_capstyle="butt", zorder=self._zo()))

    def path(self, pts, arrow=True, dashed=False, weight=ARROW_PT):
        """A polyline (elbow connector) with an optional arrowhead at the end."""
        pts = [tuple(map(float, p)) for p in pts]
        if arrow:
            (xa, ya), (xb, yb) = pts[-2], pts[-1]
            L = math.hypot(xb - xa, yb - ya)
            ux, uy = (xb - xa) / L, (yb - ya) / L
            base = (xb - ux * ARROW_LEN, yb - uy * ARROW_LEN)
            line = pts[:-1] + [base]
        else:
            line = pts
        self.ax.add_line(Line2D(
            [p[0] for p in line], [p[1] for p in line], color=BLACK,
            linewidth=weight, linestyle=(0, (4, 3)) if dashed else "-",
            solid_capstyle="butt", solid_joinstyle="miter",
            dash_capstyle="butt", zorder=self._zo()))
        if arrow:
            px, py = -uy, ux
            hw = ARROW_WID / 2
            self.ax.add_patch(Polygon(
                [(xb, yb), (base[0] + px * hw, base[1] + py * hw),
                 (base[0] - px * hw, base[1] - py * hw)], closed=True,
                facecolor=BLACK, edgecolor=BLACK, linewidth=0.3,
                zorder=self._zo()))

    def arrow(self, x1, y1, x2, y2, label=None, dashed=False, mono=True,
              side="above", size=None):
        """A straight arrow, tip at (x2, y2), optionally labelled.

        side: 'above' | 'below' | 'on' (label centred on the line over a
        white patch).  Labels are monospace by default (tool names).
        """
        self.path([(x1, y1), (x2, y2)], arrow=True, dashed=dashed)
        if label:
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            size = size or MONO_PT
            if side == "on":
                self.text(mx, my, label, mono=mono, size=size, align="center",
                          va="center", bg=True)
            else:
                off = 2.5 if side == "above" else -2.5
                self.text(mx, my - off, label, mono=mono, size=size,
                          align="center", va="bottom" if side == "above"
                          else "top")

    def dot(self, x, y, r=1.3):
        self.ax.add_patch(Ellipse((x, y), 2 * r, 2 * r, facecolor=BLACK,
                                  edgecolor=BLACK, linewidth=0.3,
                                  zorder=self._zo()))

    # ---- text
    def text(self, x, y, s, mono=False, italic=False, size=SANS_PT,
             align="left", va="center", bold=False, bg=False,
             allow_small=False):
        """Place text.  (x, y) is the anchor selected by align / va."""
        if size < SMALL_PT - 1e-6 and not allow_small:
            print(f"look: warning, {size} pt text is under the {SMALL_PT} pt "
                  f"floor", file=sys.stderr)
        t = self.ax.text(
            x, y, s, fontproperties=fontprops(mono, italic, bold, size),
            color=BLACK, ha=align, va=va, linespacing=LINE_SPACING,
            zorder=self._zo() + 5,
            bbox=dict(facecolor="white", edgecolor="none", pad=1.2)
            if bg else None)
        self._texts.append(t)
        return t

    def callout(self, number, x, y, tx, ty, r=5.2):
        """A numbered circle at (x, y) with a thin leader to (tx, ty)."""
        d = math.hypot(tx - x, ty - y) or 1.0
        sx, sy = x + (tx - x) / d * r, y + (ty - y) / d * r
        self.rule(sx, sy, tx, ty, weight=LEADER_PT)
        self.dot(tx, ty)
        self.ax.add_patch(Ellipse((x, y), 2 * r, 2 * r, facecolor=WHITE,
                                  edgecolor=BLACK, linewidth=BOX_PT,
                                  zorder=self._zo()))
        self.text(x, y + 0.3, str(number), size=SMALL_PT, align="center")

    def leader(self, x1, y1, x2, y2):
        """A thin annotation leader ending in a dot at (x2, y2)."""
        self.rule(x1, y1, x2, y2, weight=LEADER_PT)
        self.dot(x2, y2)

    # ---- output
    def _check_overlaps(self):
        self.canvas.draw()
        r = self.canvas.get_renderer()
        boxes = [(t, t.get_window_extent(r)) for t in self._texts if t.get_text()]
        for i, (a, ba) in enumerate(boxes):
            for b, bb in boxes[i + 1:]:
                if ba.overlaps(bb):
                    ox = min(ba.x1, bb.x1) - max(ba.x0, bb.x0)
                    oy = min(ba.y1, bb.y1) - max(ba.y0, bb.y0)
                    if ox > 1.5 and oy > 1.5:
                        print(f"look: WARNING labels overlap: "
                              f"{a.get_text()!r} / {b.get_text()!r}",
                              file=sys.stderr)

    def save(self, path, measure=None):
        """Render at 300 dpi and write the house PNG."""
        if measure not in (None, self.measure):
            raise ValueError("measure is fixed when the Canvas is created")
        self._check_overlaps()
        self.canvas.draw()
        buf = self.canvas.buffer_rgba()
        img = Image.frombytes("RGBA", self.canvas.get_width_height(),
                              bytes(buf))
        return finish_png(img, path, self.measure)


# ------------------------------------------------------------------ Graphviz
HOUSE_DOT = """\
digraph G {{
  graph [fontname="{sans}", fontsize=8, dpi=300, rankdir={rankdir},
         size="{size_in:.3f},5.8", pad=0.0, nodesep={nodesep}, ranksep={ranksep},
         splines={splines}, bgcolor="white", color="black", penwidth=0.5,
         labeljust=l{graph_extra}];
  node  [fontname="{sans}", fontsize=8, shape=box, style="rounded,filled",
         fillcolor="#ffffff", color="black", penwidth=0.5, margin="0.10,0.06",
         height=0.0, width=0.0];
  edge  [fontname="{mono}", fontsize=7, penwidth=0.75, arrowsize=0.42,
         arrowhead=normal, color="black", fontcolor="black"];
{body}
}}
"""

# node-style fragments for use inside a .dot body
PROCESS = 'shape=box, style="rounded,filled"'
FILE = 'shape=note, style="filled"'
STORE = 'shape=cylinder, style="filled"'
VERIFIER = 'shape=box, style="filled", peripheries=2'
FILLS = {0: "#ffffff", 10: "#e6e6e6", 20: "#cccccc", 40: "#999999"}


def dot_label(title="", mono_lines=(), mono_title=False):
    """An HTML-like label: a sans title over small monospace lines."""
    def esc(s):
        return (s.replace("&", "&amp;").replace("<", "&lt;")
                .replace(">", "&gt;"))
    parts = []
    if title:
        face = MONO_NAME if mono_title else SANS_NAME
        size = 7 if mono_title else 8
        parts.append(f'<FONT FACE="{face}" POINT-SIZE="{size}">{esc(title)}</FONT>')
    for m in mono_lines:
        parts.append(f'<FONT FACE="{MONO_NAME}" POINT-SIZE="7">{esc(m)}</FONT>')
    return "<" + "<BR/>".join(parts) + ">"


def _png_dpi_scale(path, size_in):
    return 1.0


def render_dot(name, body, out_path, measure="full", rankdir="LR",
               nodesep=0.18, ranksep=0.3, splines="ortho", graph_extra="",
               keep_dir=None):
    """Write <name>.dot with the house defaults, render, post-process.

    `body` is the node/edge statements.  Graphviz shrinks a layout that is
    wider than the measure; since that would shrink the text, the effective
    scale is checked and any shrinkage is an error.
    Returns the final PIL image.
    """
    size_in = (MEASURE_PX[measure] - 2 * MARGIN_PX - 4) / DPI
    build = Path(keep_dir or _HERE / ".build")
    build.mkdir(parents=True, exist_ok=True)
    dot_path = build / f"{name}.dot"
    raw_png = build / f"{name}.raw.png"
    dot_path.write_text(HOUSE_DOT.format(
        sans=SANS_NAME, mono=MONO_NAME, rankdir=rankdir, size_in=size_in,
        nodesep=nodesep, ranksep=ranksep, splines=splines,
        graph_extra=graph_extra, body=body))
    # natural size first, to detect shrinkage
    nat = subprocess.run(["dot", "-Tplain", str(dot_path)], capture_output=True,
                         text=True, check=True).stdout.splitlines()[0].split()
    # plain reports the (already shrunk) size and the scale factor
    scale = float(nat[1])
    if scale < 0.999:
        raise ValueError(
            f"{name}: Graphviz shrank the layout to {scale:.0%} to fit the "
            f"{size_in:.2f} in measure; labels would fall under 8 pt.  Stack "
            f"labels, split ranks, or use rankdir=TB.")
    subprocess.run(["dot", "-Tpng:cairo", str(dot_path), "-o", str(raw_png)],
                   check=True)
    img = Image.open(raw_png)
    # add the 12 px frame margin around the drawing, then pad to measure
    img = img.convert("RGBA")
    pad = MARGIN_PX + 2
    framed = Image.new("RGBA", (img.width + 2 * pad, img.height + 2 * pad),
                       "white")
    framed.alpha_composite(img, (pad, pad))
    return finish_png(framed, out_path, measure)


def repo_root():
    return _HERE.parent.parent


def figures_dir():
    d = repo_root() / "assets" / "woodcuts"
    d.mkdir(parents=True, exist_ok=True)
    return d


if __name__ == "__main__":
    print(f"sans: {SANS_NAME} -> {SANS['regular']}")
    print(f"mono: {MONO_NAME} -> {MONO['regular']}")
