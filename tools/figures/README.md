# Figure toolkit

Every diagram in the book is code. `look.py` fixes the house look; each
`fig-*.py` script imports it and writes one PNG into `assets/woodcuts/`.
`tools/render-figures.sh` renders everything and checks the result.

Fonts: **Helvetica** (labels) and **Menlo** (code), both from macOS. They ship
as `.ttc` collections, so `look.py` extracts the faces it needs into
`tools/figures/.fontcache/` (git-ignored). If they are missing it falls back
to Arial / Courier New, then DejaVu. Run `python3 tools/figures/look.py` to
see which files were chosen. Needs Graphviz `dot`, Python 3 with matplotlib
and Pillow (or a `.venv-tools/` holding them; the script prefers it).

## Adding a figure

1. Copy the proof nearest your archetype (below).
2. Name it `tools/figures/fig-CC-NN-slug.py`, CC the chapter number, NN the
   figure's order in the chapter.
3. Write to `look.figures_dir() / "CC-NN-slug.png"`.
4. `tools/render-figures.sh`, then open the PNG and look at it. At 50 percent
   zoom the labels must still read.

A captured terminal session is not a script: put the verbatim output in
`tools/figures/NAME.txt` (first line `$ command`), optionally the window title
in `NAME.title`, and the script renders `assets/woodcuts/NAME.png`. At 80 columns the type is about 6.5 pt (80 columns of Menlo cannot be larger inside 4.54 in). Lines over
80 columns are word-wrapped with a two-space continuation indent.

## look.py

Constants: `GRAY` (0/10/20/40 percent), `BOX_PT` 0.5, `ARROW_PT` 0.75,
`SANS_PT` 8, `MONO_PT` 7, `SMALL_PT` 7 (floor), `FULL_PX` 1362, `HALF_PX` 680, `THIRD_PX` 455, `MAX_H_PX` 1740.

`Canvas(height_pt, measure="full"|"half"|"third")`: coordinates are points at final
size (326.9 pt wide full, 163.4 half, 109 third; the house text block is 4.54 in), origin top left, y down. Keep content at
least 6 pt from every edge; `save` refuses a figure whose ink enters the 12 px
margin and warns on overlapping labels.

| Method | Purpose |
|---|---|
| `box(x, y, w, h, label, kind, fill, shadow, mono, sub, label_below)` | kind `process` (rounded), `file` (dog-ear), `store` (cylinder), `verifier` (double rule), `plain`; returns a `Box` with `.left .right .top .bottom .center` |
| `arrow(x1, y1, x2, y2, label=None, dashed=False, side="above"/"below"/"on")` | straight arrow, label in monospace |
| `path(points, arrow=True, dashed=False)` | elbow connector |
| `text(x, y, s, mono, italic, size, align, va, bold)` | free text |
| `callout(n, x, y, tx, ty)` | numbered circle with a leader ending in a dot |
| `leader(x1, y1, x2, y2)` / `rule(...)` / `dot(x, y)` | annotation leaders, rules |
| `save(path)` | 300 dpi, 8-bit grayscale, exact width |

Graphviz: `render_dot(name, body, out_path, measure, rankdir, nodesep,
ranksep, splines)` wraps `body` in the house `graph/node/edge` defaults, writes
`.build/NAME.dot`, runs `dot -Tpng:cairo` at 300 dpi, and post-processes. Use
`PROCESS`, `FILE`, `STORE`, `VERIFIER` as node-attribute fragments, `FILLS`
for fill colours, and `dot_label(title, mono_lines, mono_title)` for labels.
Graphviz shrinks a layout wider than the measure, which shrinks the text;
`render_dot` errors on any shrinkage (graph sized to 4.45 in), so stack labels,
split ranks, or use `rankdir=TB` rather than accept small type. Narrow figures are padded, never
enlarged.

## Archetype to helper

| Archetype (style guide 5.2) | Back end | Start from |
|---|---|---|
| 1 Pipeline, 2 Data-flow, 8 State machine, 10 Flowchart | Graphviz | `fig-00-proof-pipeline.py` (`rankdir=TB` for top-down) |
| 3 Directory tree | Canvas | `fig-00-proof-tree.py` |
| 4 Layered stack | Canvas | `fig-00-proof-stack.py` |
| 5 Client/CI topology | Graphviz (`STORE`, `FILE`) or Canvas | the pipeline proof |
| 6 Before/after, 7 Page anatomy | Canvas (`box`, `callout`) | the stack proof |
| 9 Filmstrip | Canvas, or PNGs boxed by hand | |
| 11 Timeline | Canvas (`rule`, `text`, `dot`) | the tree proof |
| Terminal figure | `terminal.py` | `proof-check.txt` |

## What render-figures.sh enforces

It runs every `fig-*.py`, renders every `*.txt`, then checks each PNG in
`assets/woodcuts/`: mode `L` (8-bit grayscale, no alpha), width 1362, 680 or 455 (4.54, 2.27, 1.52 in),
dpi metadata 300 x 300, and that nothing but `.png` figures (no hidden or `._*` files) sits in the directory, since press refuses unreferenced files there. Height over 1740 px is refused by `look.py`. It prints a table (file, width, height, mode, dpi,
bytes) and exits nonzero on any violation. `look.py` itself additionally
refuses ink inside the 12 px margin.
