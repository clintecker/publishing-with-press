# Figures, chapter 8

## 08-01 What each verifier inspects
- PNG: assets/woodcuts/08-01-what-each-verifier-inspects.png
- Script: tools/figures/fig-08-01-what-each-verifier-inspects.py
- Archetype: matrix (Canvas), 13 rows by 5 columns, filled dots, sentinels row at 10% gray.
- Shortened/changed labels: column heads are broken across two lines to fit the column width at 7 pt: "verify_" / "formats", "verify_" / "archives", "verify_" / "pages"; "verify_pdf print profile" is "verify_pdf" over italic "print profile". No text added or dropped.
- Not drawn: nothing omitted.

## 08-02 The rebuild edges
- PNG: assets/woodcuts/08-02-rebuild-edges.png
- Script: tools/figures/fig-08-02-rebuild-edges.py
- Archetype: data-flow, left to right (Canvas, straight fans; Graphviz was tried first and abandoned for control of the crossings).
- Labels: none shortened. The "pages" bundle is a 10% gray dog-eared file one step past "sources", with a solid arrow.
- Drawing choices: the "coverwrap" file icon sits above "print" in the column so the dashed arrow ("if assets/cover.jpg") from press verify-print stays clear of the solid ones. The dotted arrow ("reads, does not rebuild") runs from press verify-formats along the top into "pdf". Solid, dashed and dotted are three distinct line styles.
- Not drawn: nothing omitted.

## 08-03 A verify run
- PNG: assets/woodcuts/08-03-verify-run.png
- Script: tools/figures/fig-08-03-verify-run.py (not the .txt route: terminal.py cannot gray single lines and bolds prompt lines, and the brief asks for 40% gray on the first two lines, full black on the last, no bold).
- Archetype: terminal panel.
- Text: the three lines exactly as the art brief gives them. The title bar reads "alice@hatter" as the art brief and fig-alt say, not "alice@hatter:~/alice" as the batch note said; change one string in the script if the longer title is preferred. Examples 8.1/8.2 are not used: this figure is the failure message, not a passing run.
- Not drawn: nothing omitted.

## Checks
tools/render-figures.sh renders all three: mode L, width 1362, 300 dpi, no margin violations. Viewed each PNG. The script's final table check exits nonzero only because other chapters' placeholder PNGs (07, 09 to 16) are still RGB; none of the three chapter 8 figures is flagged.
