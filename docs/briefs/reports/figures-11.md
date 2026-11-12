# Figures, chapter 11

Rendered with `tools/render-figures.sh`; all three PNGs pass the format
checks (1362 px wide, mode L, 300 dpi). Shared helper: `tools/figures/_plate.py`
(composites the alpha master onto a ground).

## 11-01 the art-direction loop

- Path: `assets/woodcuts/11-01-art-direction-loop.png`
- Script: `tools/figures/fig-11-01-art-direction-loop.py`
- Archetype: 10, flowchart in two rows (Canvas).
- Shortened labels: none. Long text is wrapped: `book/chapters/*.md`,
  `art/commissions.md`, "build/ and art/candidates/", and the command box
  (three lines in place of the `|` separators).
- Departures: file labels sit above their icons, so the closing arrow from
  "the build" can land on the first file's icon. "your API keys" is a separate
  arrow dropping into the command box from above, because the file-to-command
  arrow is too short to carry a label; the file-to-command arrow is drawn
  unlabeled. "you choose one" and "your API keys" are in italic sans, not
  monospace, to fit. The one drop shadow is on the manuscript file, where the
  loop starts.

## 11-02 one master onto every surface

- Path: `assets/woodcuts/11-02-one-master-every-surface.png`
- Script: `tools/figures/fig-11-02-one-master-every-surface.py`
- Archetype: 6, before/after (one source, three results; Canvas).
- Uses the real plate `the-engravers-bench.png` (reduced), not a rabbit: the
  monospace path label reads `assets/woodcuts/the-engravers-bench.png`, which
  differs from the brief's `white-rabbit.png` so the figure shows a file that
  exists. The chapter's `fig-alt` still says "engraved rabbit" and needs
  updating to match (chapter not edited).
- Left: master on a 20 percent/white checkerboard. Right: page outline on
  white; cover as a 40 percent gray cloth field with a woven grain of 20 percent
  and darker lines, spine rule at the left, plate centered; rounded panel
  on 10 percent gray standing for cream.
- Shortened labels: none. Gray is used for "dark green" (grays only at the
  house levels) and for "cream"; the brief's color names cannot be drawn.

## 11-03 what intake does to a delivered plate

- Path: `assets/woodcuts/11-03-intake-before-after.png`
- Script: `tools/figures/fig-11-03-intake-before-after.py`
- Archetype: 6, before/after pair, plus a luminance scale (Canvas).
- Uses the bench plate instead of a rabbit in a waistcoat. (a) is the plate
  over a #f1f1f1 ground (the grayscale of #f1f2f3) that ends just inside the
  frame, its edge a 10-20 percent hairline, with the callout
  "ground near #f1f2f3". (b) is the same plate on a checkerboard, no ground.
  One thin arrow from (a) to (b).
- Scale: drawn as the alpha curve (255 flat to 45, a straight ramp to 225,
  0 beyond) over a ruled axis with ticks 0, 45, 225, 255, rather than a shaded
  bar, because gradients are barred. Added text beyond the brief: the tick
  numbers and the word "luminance" naming the axis. The end labels are
  wrapped to two lines ("alpha 255, / ink", "alpha 0, / clear").
- Unsatisfied: the brief asks for an "engraved white rabbit in a waistcoat";
  not drawn (using the supplied plate).
