#!/usr/bin/env python3
"""Compose the front cover of *Publishing with Press* (1800 x 2700, 2:3).

The image model draws only the animal (build/cover/cover.png, commissioned
with ``press cover --style engraved-animal``); this script sets everything
else, so no letter on the cover is ever a model's guess.

Layout (docs/style-guide.md section 6.2, config/aesthetic.yaml ``cover``):

- white ground, the whole cover;
- a deep sepia band (#4a2e1a) across the top eighth, carrying the series
  line "A Workbench Handbook" reversed out in small caps at the right;
- the title flush left under the band in Libertinus Serif condensed by
  horizontal scaling to 82 percent; the subtitle in Libertinus Serif
  Italic beneath it;
- the engraving keyed to transparency (a luminance key: ink stays, the
  white ground goes) and set centre-to-lower-right, facing into the title;
- "Clint Ecker" bottom right; "LGTM Publishing" small at bottom left.

Nothing else. Usage, from the repository root:

    python3 tools/cover.py [--engraving build/cover/cover.png] [--out build/cover/front.png]

then ``press art accept build/cover/front.png --as cover``.

Fonts: Libertinus Serif Regular and Italic (OFL), found via kpsewhich or
the paths below. Pillow on this machine has no raqm, so the OpenType smcp
feature is unavailable; the small caps are synthesized from capitals at
74 percent of the cap size, letterspaced, which is how a hand compositor
without a small-caps fount would set them.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1800, 2700
BAND_H = round(H / 8)          # 338 px, the top eighth
SEPIA = (0x4A, 0x2E, 0x1A)
INK = (0x1A, 0x1A, 0x1A)
WHITE = (255, 255, 255)
MARGIN = 120                   # left/right margin
CONDENSE = 0.82                # horizontal scale of the title face

TITLE = "Publishing with Press"
SUBTITLE = "Building Books from Plain Text"
SERIES = "A Workbench Handbook"
AUTHOR = "Clint Ecker"
IMPRINT = "LGTM Publishing"

FONT_DIRS = [
    Path.home() / "Library/texmf/fonts/opentype/public/libertinus-fonts",
    Path("/usr/share/fonts/opentype/libertinus"),
    Path("/usr/share/texlive/texmf-dist/fonts/opentype/public/libertinus-fonts"),
]


def font_path(name: str) -> Path:
    if shutil.which("kpsewhich"):
        out = subprocess.run(["kpsewhich", name], capture_output=True, text=True).stdout.strip()
        if out:
            return Path(out)
    for d in FONT_DIRS:
        if (d / name).exists():
            return d / name
    raise SystemExit(f"cover.py: font {name} not found (install Libertinus)")


def font(name: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(font_path(name)), size)


def text_layer(text: str, f: ImageFont.FreeTypeFont, fill, scale_x: float = 1.0) -> Image.Image:
    """Render text tightly to an RGBA layer whose top is the font's ascender
    line, optionally condensed horizontally."""
    asc, desc = f.getmetrics()
    w = int(f.getlength(text)) + 4
    layer = Image.new("RGBA", (w, asc + desc), (0, 0, 0, 0))
    ImageDraw.Draw(layer).text((0, 0), text, font=f, fill=fill)
    if scale_x != 1.0:
        layer = layer.resize((max(1, round(w * scale_x)), layer.height), Image.LANCZOS)
    return layer


def small_caps(text: str, f_cap: ImageFont.FreeTypeFont, f_sc: ImageFont.FreeTypeFont,
               fill, track: int) -> Image.Image:
    """Synthesized small caps: capitals stay full size, lowercase is set as
    capitals in the smaller face, all on one baseline, letterspaced."""
    asc_c, desc_c = f_cap.getmetrics()
    pieces = []
    for ch in text:
        f = f_cap if (ch.isupper() or not ch.isalpha()) else f_sc
        g = ch.upper()
        pieces.append((g, f, f.getlength(g)))
    width = int(sum(p[2] for p in pieces) + track * (len(pieces) - 1)) + 4
    layer = Image.new("RGBA", (width, asc_c + desc_c), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    x = 0.0
    for g, f, adv in pieces:
        d.text((x, asc_c), g, font=f, fill=fill, anchor="ls")
        x += adv + track
    return layer


def keyed_engraving(path: Path) -> Image.Image:
    """Luminance key: the engraving's light ground becomes transparent, its
    ink becomes black of matching opacity, so no box shows on the cover."""
    src = Image.open(path).convert("L")
    # Ground (>= 246) goes fully clear; ink ramps to opaque.
    alpha = src.point(lambda v: 0 if v >= 246 else min(255, round((246 - v) * 255 / 236)))
    ink = Image.new("RGBA", src.size, INK + (0,))
    ink.putalpha(alpha)
    bbox = alpha.getbbox()
    return ink.crop(bbox) if bbox else ink


def compose(engraving: Path, out: Path) -> None:
    cover = Image.new("RGBA", (W, H), WHITE + (255,))
    d = ImageDraw.Draw(cover)

    # Band, the top eighth, with the series line reversed out at the right.
    d.rectangle([0, 0, W, BAND_H], fill=SEPIA)
    series = small_caps(SERIES, font("LibertinusSerif-Regular.otf", 58),
                        font("LibertinusSerif-Regular.otf", 43), WHITE, track=6)
    cover.alpha_composite(series, (W - MARGIN - series.width, (BAND_H - series.height) // 2 + 6))

    # Title: one line, flush left, condensed to 82 percent, filling the measure.
    measure = W - 2 * MARGIN
    size = 300
    while True:
        tl = text_layer(TITLE, font("LibertinusSerif-Regular.otf", size), INK, CONDENSE)
        if tl.width <= measure or size <= 120:
            break
        size -= 2
    title_top = BAND_H + 110
    cover.alpha_composite(tl, (MARGIN - 6, title_top))

    # Subtitle in italic beneath.
    sub = text_layer(SUBTITLE, font("LibertinusSerif-Italic.otf", 104), INK)
    sub_top = title_top + tl.height - 10
    cover.alpha_composite(sub, (MARGIN, sub_top))

    # Engraving: centre-to-lower-right, facing left into the title.
    eng = keyed_engraving(engraving)
    target_w = 1560
    eng = eng.resize((target_w, round(eng.height * target_w / eng.width)), Image.LANCZOS)
    zone_top, zone_bot = sub_top + sub.height + 60, H - 300
    ey = zone_top + (zone_bot - zone_top - eng.height) // 2 + 60
    cover.alpha_composite(eng, (W - MARGIN + 40 - eng.width, ey))

    # Foot: author bottom right, imprint small bottom left, on one baseline.
    base = H - 150
    author = font("LibertinusSerif-Regular.otf", 92)
    d.text((W - MARGIN, base), AUTHOR, font=author, fill=INK, anchor="rs")
    imprint = small_caps(IMPRINT, font("LibertinusSerif-Regular.otf", 44),
                         font("LibertinusSerif-Regular.otf", 33), INK, track=4)
    asc, _ = font("LibertinusSerif-Regular.otf", 44).getmetrics()
    cover.alpha_composite(imprint, (MARGIN, base - asc))

    out.parent.mkdir(parents=True, exist_ok=True)
    cover.convert("RGB").save(out, dpi=(300, 300))
    print(f"wrote {out} ({W}x{H}); title {size}px at {CONDENSE:.0%}, "
          f"engraving {eng.width}x{eng.height} at y={ey}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--engraving", default="build/cover/cover.png", type=Path)
    ap.add_argument("--out", default="build/cover/front.png", type=Path)
    a = ap.parse_args()
    compose(a.engraving, a.out)


if __name__ == "__main__":
    main()
