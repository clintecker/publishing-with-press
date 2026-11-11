#!/usr/bin/env python3
"""Render a captured text file as a boxed, light terminal panel.

Usage: python3 tools/figures/terminal.py in.txt out.png --title "hatter:~/alice$"

Lines beginning "$ " are prompt lines and are set in bold (the only bold in
the book's figures); everything else is regular.  Lines longer than --cols
(default 80) are word-wrapped at the column limit, continuation lines indented two spaces.
"""
import argparse
import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import look  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402


def wrap(lines, cols):
    out = []
    for ln in lines:
        ln = ln.expandtabs(8).rstrip("\n")
        prompt = ln.startswith("$ ")
        if len(ln) <= cols:
            out.append((ln, prompt))
            continue
        indent = len(ln) - len(ln.lstrip(" "))
        for k, piece in enumerate(textwrap.wrap(
                ln, cols, subsequent_indent=" " * (indent + 2),
                drop_whitespace=True, replace_whitespace=False,
                break_long_words=True, break_on_hyphens=False)):
            out.append((piece, prompt))
    return out


def render(text, out_path, title="", cols=80, measure="full"):
    rows = wrap(text.splitlines(), cols)
    W = look.MEASURE_PT[measure]
    m = look.MARGIN_PX / look.PX_PER_PT + 1.0     # outer clear space, pt
    pad = 6.0                                      # text inset inside frame
    inner = W - 2 * m - 2 * pad
    longest = max([cols] + [len(r) for r, _ in rows])
    adv_em = look.mono_advance_pt(1.0)
    size = min(look.SANS_PT, inner / (longest * adv_em))
    size = int(size * 20) / 20.0
    lh = size * 1.32
    bar = 15.0
    H = m + bar + pad + len(rows) * lh + pad + m
    c = look.Canvas(H, measure)
    x0, y0, fw = m, m, W - 2 * m
    fh = H - 2 * m
    # title strip, then frame on top
    c.ax.add_patch(Rectangle((x0, y0), fw, bar, facecolor=look.GRAY[10],
                             edgecolor="none", zorder=2))
    c.rule(x0, y0 + bar, x0 + fw, y0 + bar)
    c.ax.add_patch(Rectangle((x0, y0), fw, fh, facecolor="none",
                             edgecolor=look.BLACK, linewidth=look.BOX_PT,
                             zorder=3))
    if title:
        c.text(x0 + pad, y0 + bar / 2 + 0.2, title, mono=False,
               size=look.SANS_PT - 0.5)
    for i, (ln, prompt) in enumerate(rows):
        c.text(x0 + pad, y0 + bar + pad + i * lh, ln, mono=True, size=size,
               bold=prompt, va="top")
    c._texts = []          # monospace rows may legitimately touch; skip check
    return c.save(out_path, measure), size


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("input")
    ap.add_argument("output")
    ap.add_argument("--title", default="")
    ap.add_argument("--cols", type=int, default=80)
    ap.add_argument("--measure", choices=["full", "half"], default="full")
    a = ap.parse_args()
    _, size = render(Path(a.input).read_text(encoding="utf-8"), a.output,
                     a.title, a.cols, a.measure)
    print(f"{a.output}: mono {size:.2f} pt at {a.cols} columns")


if __name__ == "__main__":
    main()
