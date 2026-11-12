# Figures, chapter 16

Rendered with `tools/render-figures.sh`; the whole set passes its checks
(45 figures, grayscale, 1362 px wide, 300 dpi).

## 16-01 module map
- Path: `assets/woodcuts/16-01-module-map.png` (script `tools/figures/fig-16-01-module-map.py`), 1362 x 967.
- Archetype: 4, layered stack, inside a 2.6 pt ruled frame.
- Shortened labels: none. Added the module-file names only where the brief gave them (`__main__.py`, `catalog.py`, `registry.py`, `bookmodel.py, booklib.py`); the other bands carry no file names because the brief gave none.
- Changes from the brief: the trust column is white (not gray) so the frame stays the heaviest element. The three adapter arrows start in the gap beside the trust column and leave through the frame; their labels sit above the outside part. The `adapters/` label is on the top frame edge.
- Not drawn: nothing omitted.

## 16-02 end-to-end data flow
- Path: `assets/woodcuts/16-02-end-to-end-data-flow.png` (script `fig-16-02-end-to-end-data-flow.py`), 1362 x 1726 (under the 1740 cap).
- Archetype: 2, data-flow, top to bottom, drawn on the Canvas.
- Shortened labels: "profiles + aesthetic + front matter" and "book/chapters + book/appendices" and "booklib.chapter_files" and "gen_authorities -> dist/alice-sources.md" are broken across lines, not reworded. Row 3 is three boxes, each two or three lines of monospace.
- Additions the brief implies: `gen_authorities` has a side path to the `dist/alice.*` cylinder (it writes `dist/alice-sources.md` directly); `gen_index` and `render_defaults` feed pandoc. The bypass arrow on the left edge carries the label "markdown, source (no pandoc)", set on two lines. The CI band is one box, per the typesetter fold.
- "pages, verify_pages" is drawn as one rounded box (the brief gave one label for the step).
- Not drawn: the print interior branch (prose only, per report-16).

## 16-03 trust tiers
- Path: `assets/woodcuts/16-03-trust-tiers.png` (script `fig-16-03-trust-tiers.py`), 1362 x 1250.
- Archetype: 4, layered stack, plus a small flow on the right.
- Shortened labels: none. "quality tier", "integration tier", "release tier" are broken across two lines.
- Twelve bands alternate 10 and 20 percent gray, bottom to top, each joined to the next by a two-ring chain glyph. The italic note sits under the stack. The 2 pt shadow is on `press.receipts assemble`. "release tier" has no arrow, as the brief gives it none.
- Not drawn: nothing omitted.
