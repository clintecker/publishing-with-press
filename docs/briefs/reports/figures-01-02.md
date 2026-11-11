# Figures, chapters 1 and 2

All six render through `tools/render-figures.sh` (1362 px wide, mode L, 300 dpi, no margin or overlap warnings). The script's final FAIL list names only other desks' placeholder PNGs (RGB, no dpi), none of this batch. I opened each PNG and judged it at reduced size.

Toolkit change: `tools/render-figures.sh` now reads an optional `tools/figures/NAME.cols` sidecar and passes it to `terminal.py --cols` (default stays 80). `tools/figures/_parts.py` holds the shared folder and file-icon helpers.

| Figure | PNG | Script | Archetype |
|---|---|---|---|
| 1.1 | `assets/woodcuts/01-01-pipeline-overview.png` | `tools/figures/fig-01-01-pipeline-overview.py` | 1 pipeline (Canvas) |
| 1.2 | `assets/woodcuts/01-02-the-stack.png` | `tools/figures/fig-01-02-the-stack.py` | 4 layered stack |
| 1.3 | `assets/woodcuts/01-03-ten-minute-tour.png` | `tools/figures/fig-01-03-ten-minute-tour.py` | 9 filmstrip, three terminal panels (6.85 pt mono) |
| 2.1 | `assets/woodcuts/02-01-tools-in-the-build.png` | `tools/figures/fig-02-01-tools-in-the-build.py` | 2 data-flow |
| 2.2 | `assets/woodcuts/02-02-doctor-report.png` | `tools/figures/02-02-doctor-report.txt` (+ `.title`, `.cols` = 72) | terminal (7.15 pt mono) |
| 2.3 | `assets/woodcuts/02-03-local-versus-container.png` | `tools/figures/fig-02-03-local-versus-container.py` | 5 topology |

## Deviations and judgment calls

- Verifier boxes ("verifiers" in 1.1, "verify" in 2.1) are double-ruled with the drop shadow, per the desk rule for verifiers, not the plain rounded box the briefs name.
- Folder icon for `dist/` (1.1) is drawn from the toolkit's polygon primitive (rectangle with a tab); the toolkit has no folder helper.
- 1.1: the label "book/chapters/*.md" is broken onto two lines (no words changed). The stitch arrow starts at a dot under the input labels, since the two inputs are one manuscript. Arrowheads from the output files run through one bus to the verifiers, with ticks rather than arrowheads on the file side.
- 1.1: "pandoc writers" is stacked on two lines beside the trunk; "+ Lua filters" is set in monospace inside the pandoc box.
- 1.3: the panels are drawn by the figure script (numbered 1, 2, 3 in circles at the left of each frame), not by `terminal.py`, which cannot number or stack; the transcripts are the brief's lines exactly, at 72 columns. Title bar `alice@hatter:~/alice` on each.
- 2.2: the capture is verbatim from report-02, with the `$ press doctor` prompt before it and a fresh `$` after. At 72 columns the epubcheck and claude lines and the `not ready:` line wrap with a two-space continuation indent. The blank line before `not ready:` is kept.
- 2.3: the image line `ghcr.io/clintecker/press-toolchain@sha256:...` is wrapped onto four lines inside the box (no text changed); "Ubuntu 24.04, amd64 and arm64" is on two lines. Arrow labels "chapters and config" and "mounted at /book" are on two lines. The crate icon is a small slatted box; the dashed docker pull arrow ends at the image box at the crate. The two-headed mount arrow is two overlaid arrows.
- 2.1: no label on the HTML-to-verify arrow, as the brief gives it none. The HTML branch is labeled "reader site" in sans (it is a name, not a file name).
- No label text added or dropped otherwise. Nothing in the briefs was left undrawn.
