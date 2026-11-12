# Figures, chapter 10

Both rendered with `tools/render-figures.sh`; all checks pass (1362 px wide, mode L, 300 dpi, nothing in the margin). Judged at 50 percent zoom.

## 10-01 How the two configuration files become the front matter

- Path: `assets/woodcuts/10-01-config-to-front-matter.png` (script `tools/figures/fig-10-01-config-to-front-matter.py`)
- Archetype: 2, data-flow, left to right (Canvas, not Graphviz, so the arrow labels and the gray band sit exactly where the brief puts them)
- Labels shortened: none. Line breaks added to the key lists and to the two file labels ("config/" over the file name) to fit the measure.
- Notes: the five generated pages carry a "generated" heading above them; "title page" has the 20% fill; the second group is a 10% band headed "from elsewhere" with dashed arrows from "pandoc toc" (to Contents) and "TeX header" (to both lists). Each config file uses a trunk line with dots at the branches, so the arrows do not cross. Height is 1709 px, just under the 1740 px cap.
- Not drawn: nothing omitted.

## 10-02 The path of an index term

- Path: `assets/woodcuts/10-02-index-entry-path.png` (script `tools/figures/fig-10-02-index-entry-path.py`)
- Archetype: 10, flowchart with a diamond, top to bottom (Canvas, because the brief wants a drop shadow on "build stops", which Graphviz cannot draw)
- Labels shortened: none; the text of the rectangles and of the `gen_index` message is wrapped onto two or three lines.
- Notes: "No" runs right to a rounded box with a 40% gray shadow, with the monospace message below it; "Yes" runs down to the entry box and the dog-eared appendix page. The "term: Mock Turtle" callout is a monospace note on a leader ending in a dot on the file icon.
- Not drawn: nothing omitted.
