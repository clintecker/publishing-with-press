#!/usr/bin/env python3
"""Proof: the layered-stack archetype (style guide 5.2 #4), half measure."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import look  # noqa: E402

BANDS = [  # top to bottom
    ("your book", None),
    ("press", None),
    ("TeX Live and LuaLaTeX", None),
    ("pandoc", None),
    ("Python 3.10+", None),
    ("Operating system", None),
]

band_h, gap = 27.0, 0.0
top = 12.0
c = look.Canvas(top * 2 + band_h * len(BANDS), "half")
x, w = 14.0, c.W - 28.0
for i, (label, _) in enumerate(BANDS):
    fill = 10 if i % 2 == 0 else 20
    c.box(x, top + i * band_h, w, band_h, label, kind="plain", fill=fill,
          mono=(label == "pandoc"),
          size=look.SANS_PT if label != "pandoc" else look.MONO_PT + 0.5)
c.save(look.figures_dir() / "00-proof-stack.png")
