# Figures report: chapter 15

## Figure 15.2, the editorial-passes machine

- Script: `tools/figures/fig-15-02-editorial-passes-machine.py`
- PNG: `assets/woodcuts/15-02-editorial-passes-machine.png` (1362 x 1042 px, mode L, 300 dpi; passes `tools/render-figures.sh`)
- Archetype: 10, flowchart, drawn on the Canvas (not Graphviz) so the columns follow the directive. It is wider than tall, as the directive asks.
- Labels shortened: none. Three labels are wrapped across lines to fit the columns: `book/chapters/*.md` (three lines), `press check` (two), and `build/editorial-rejections.md` (broken after `editorial-`).
- Brief elements not drawn as written:
  - The directive puts the stop-rule diamond in column 4. The diamond needs about 104 pt of width for its three-line label, and column 4 is 50 pt wide, so both diamonds sit in a bottom band under the columns. `press check` still stands alone at far right, with its arrow dropping into the first diamond.
  - The three chapter-pass boxes and the three synthesizer boxes each end in a "..." ellipsis, set in 10 pt type.
  - The three whole-book boxes join the chapter passes at one shared bus into `suggestions`.
  - "stop" is drawn once, as a single box that both "Yes" and the "No" from `rounds left?` reach.
  - The "Yes" loop returns to the bottom of column 2 (the `arc` box), because the whole-book group is the nearest drawn target. It reads as returning to the readers.
  - The directive's reader "should see the loop first". With the shadow on `press check`, the eye lands there first, then follows the arrow down and around; the loop is the long path at the bottom. I did not give the loop extra weight, since the house look allows one emphasis (the shadow) and uniform strokes.
