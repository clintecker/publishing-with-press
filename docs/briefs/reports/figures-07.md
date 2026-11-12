# Figures, batch 07

Scripts are in `tools/figures/`; all four render at 1362 px wide, mode L, 300 dpi.
`tools/render-figures.sh` renders them cleanly; its final check currently fails
only on other batches' RGB placeholders (09-* onward), not on these four.

## 7.1 `assets/woodcuts/07-01-build-graph.png` (fig-07-01-build-graph.py)
Archetype 1, pipeline (Canvas). Nine horizontal arrows enter the shadowed
"pages" box, one per artifact box; markdown also feeds sources through an
elbow; print to coverwrap sits below a rule with "not built by press all".
Labels: "source" kept as given. Nothing shortened. Nothing undrawn.
Choice: the nine arrows are drawn horizontal, entering a tall pages box, to
avoid crossings; sources sits in a second column between the markdown and txt
rows.

## 7.2 `assets/woodcuts/07-02-filter-chain.png` (fig-07-02-filter-chain.py)
Archetype 4, layered stack, three columns. print-safe-images in 40 percent
gray, only in the print column; rotated italic arrow label "pandoc runs in
this order" beside the first column. Nothing shortened. Same-named bands line
up for the first two rows only; later bands shift up in the shorter columns
(stacks are top-aligned and gapless).

## 7.3 `assets/woodcuts/07-03-defaults-templating.png` (fig-07-03-defaults-templating.py)
Archetype 6, before/after, two dog-eared file boxes labeled (a) and (b).
Shortened or changed labels (a 7 pt monospace line cannot fit the half-width
frame):
- the `metadata-file:` line is wrapped onto two lines (key, then indented path),
  and the quotation marks around values are dropped;
- (b) line 2 reads `.../data/tex/book-header.tex` (brief: `.../press/data/tex/...`);
- (b) line 3 is the struck-through gray rendition `~/alice/tex/title-page.tex`
  (the brief gives no text for it; it is the resolved form of the (a) line).
The arrow from (a) to (b) is an elbow under the frames, labeled
`render_defaults`, because the gap between frames is too narrow for the label.

## 7.4 `assets/woodcuts/07-04-press-all-sequence.png` (fig-07-04-press-all-sequence.py)
Archetype 8, state machine (Canvas, not Graphviz, for control of the arcs).
Start dot, six states, double-circle "done", shadowed "stop" box, six "fail"
arcs (the gate's labeled "fail, under PRESS_RELEASE").
Deviations: "commerce gate" is set on two lines inside its ellipse; the three
small-sans notes sit above the row with leaders, not under the states, so the
fail arcs have a clear path down; "advisory unless PRESS_RELEASE, absent
without ordering" is broken over three lines. Circles are wide ellipses to
fit the labels in one 4.54 in row.
