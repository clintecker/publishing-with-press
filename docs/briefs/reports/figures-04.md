# Figures report, chapter 4

All three render clean (mode L, 1362 px wide, 300 dpi) via `tools/render-figures.sh`; judged at 50 percent zoom.

## 04-01 page anatomy
- Path: `assets/woodcuts/04-01-page-anatomy.png` (script `tools/figures/fig-04-01-page-anatomy.py`), 1362 x 1688 px.
- Archetype: 7, annotated page anatomy (Canvas).
- Drawn as one full-measure page at 2:3 (6 by 9), text block 4.54 in of 6 in, no running head, folio centred at the foot. It fits under 1740 px, so no verso-recto pair was needed; the chapter's `place=plate` stays as is.
- Gray bars stand in for body text and the blockquote's italic lines; the section heading is a solid black bar (the brief gave no heading text, so none is invented). The "Figure 1.1" label and "Down the rabbit-hole" are the only words on the page besides the folio "1".
- The drop cap is an "A" about three lines tall.
- Callouts 1 to 9 as briefed; circles sit in the left and right margins.

## 04-02 scene-break ornaments
- Path: `assets/woodcuts/04-02-scene-break-ornaments.png`, 1362 x 884 px.
- Archetype: matrix (Canvas). Rows labelled in monospace (rule, asterism, fairy-dust), column heads PDF and Reader.
- Rule/Reader is a solid diamond between hairlines tapered to a point at their outer ends. Fairy-dust is 4/3/4 staggered asterisks.
- Nothing shortened or omitted.

## 04-03 set pieces
- Path: `assets/woodcuts/04-03-set-pieces.png`, 1362 x 534 px.
- Archetype: before/after, three frames (Canvas), labels "(a) cascade", "(b) verse", "(c) tail".
- Text is a serif (Times New Roman, falling back to Georgia or DejaVu Serif), set in the script, because look.py offers no serif face; the brief asks for serif lines.
- Type is 8 pt in (a) and (b); in (c) it shrinks 8, 7.6, 7.3, 7.0 pt, staying at the 7 pt floor. The shrink is therefore modest. Tail offsets swing right, left, right, left in a gentle curve.
- Nothing shortened.

## Not satisfied
- Nothing missing. Other files in `assets/woodcuts/` (the 2400 px RGBA art and the 01-03 placeholders) make render-figures.sh report format violations; those are not mine.
