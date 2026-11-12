# Figures, chapter 12 (illustrator)

All three render at 1362 px wide, 8-bit grayscale, 300 dpi; `look.py` margin and overlap checks pass.

## 12-01 cover wrap anatomy
- Path: `assets/woodcuts/12-01-cover-wrap-anatomy.png` (1362 x 1263). Script: `tools/figures/fig-12-01-cover-wrap-anatomy.py`.
- Archetype: page anatomy (Canvas), to scale at 22.4 pt per inch, so the wrap rectangle is about 286 x 207 pt. The directive's 1362 px wrap width cannot hold the dimension lines inside a 1362 px figure, so the wrap itself is about 1190 px wide.
- Drawn: 10% bleed band, trim line, back / 20% spine / front, all dimension lines, `wrap_w`, `wrap_h`, spine formula on a leader, barcode box with "EAN-13" inside and its two offset measures.
- Moved: bleed and trim labels sit below the rectangle on vertical leaders, not at the left. The left margin was too narrow for "bleed 0.125in".
- Omitted: the spine-text rule note (report-12 allows it "if room allows"; it is text the directive did not give).
- The two offset callouts ("0.5in from spine fold", "0.5in up") are leader labels onto tick measures, since the gaps are only about 11 pt.

## 12-02 spine math by provider
- Path: `assets/woodcuts/12-02-spine-math.png` (1362 x 901). Script: `tools/figures/fig-12-02-spine-math.py`.
- Archetype: matrix (Canvas), header row 10% gray. Row labels in the first column are monospace and unheaded. Column widths are 20 / 55 / 25 percent of the space right of the label column.
- Cell text is verbatim; long formulas are line-broken by hand after each slash. Lulu hardcover and IngramSpark allowance cells are empty, as briefed.
- Departures: the header text is 7 pt regular, since bold at 8 pt did not fit the narrow first column.

## 12-03 print pack graph
- Path: `assets/woodcuts/12-03-print-pack-graph.png` (1362 x 908). Script: `tools/figures/fig-12-03-print-pack-graph.py`.
- Archetype: pipeline (Canvas instead of Graphviz, for the stacked files, the cover input, and the elbow back to row 2).
- Shortened labels: `gen_coverwrap` is set `gen_` / `coverwrap` and `verify_coverwrap` is set `verify_` / `coverwrap` (broken at the underscore to fit four boxes plus the file column). File paths are broken after `dist/`, `build/`, and `config/`. "edition manifest" carries `edition_id` as a sub-line.
- Departures: the two verifier boxes (`verify_pdf --profile print`, `verify_coverwrap`) are double-ruled per the desk rule, where the directive says rounded. Press publish branches from verify_coverwrap straight down; the main chain leaves it by an elbow to the second row. Commerce gate carries the only drop shadow.

## Note
`assets/woodcuts/` also holds `12-01-spine-math.png` and `12-02-cover-wrap-anatomy.png`, stale placeholders that no chapter references. They were left in place, and the build refuses unreferenced files there, so they should be deleted.
