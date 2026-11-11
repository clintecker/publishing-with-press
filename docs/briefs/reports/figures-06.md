# Figures report: chapter 6

## 06-01 The checker guards every build
- Path: assets/woodcuts/06-01-checker-guards-the-build.png (script tools/figures/fig-06-01-checker-guards-the-build.py, Canvas)
- Archetype: 1, pipeline.
- Shortened: "book/chapters/*.md" is folded to two lines ("book/chapters/" / "*.md") to fit the left column. Inner labels stack to two or three lines ("checking / the / checkers"); text is unchanged.
- Not drawn: nothing. Small type (7 pt) is used inside the four inner boxes and the three edition boxes; "stop (nonzero exit)" is 7 pt on one line.

## 06-02 Known-bad fixture round trip
- Path: assets/woodcuts/06-02-fixture-round-trip.png (script tools/figures/fig-06-02-fixture-round-trip.py, Canvas)
- Archetype: 10, flowchart.
- Shortened: none. The fixture's first line is shown as `<!-- expect: very unique -->`. The brief says the HTML comment holds "expect: very unique".
- Not drawn: nothing. The failure box carries the 40% gray shadow.

## 06-03 `press check` output
- Path: assets/woodcuts/06-03-check-output.png (tools/figures/06-03-check-output.txt, .title, .cols = 72)
- Archetype: terminal.
- Text copied from Example 6.12 character for character, with the chapter's own wrap points kept (72 columns; the renderer would rewrap identically). Mono type is 7.15 pt.
- Title bar is `alice@hatter:~/alice`, as the assignment specified. The `art:` comment says "alice@hatter: ~/alice-in-wonderland"; the assignment and the fig-alt ("alice at hatter") were followed. The chapter's art comment may want updating.

## Notes
- `tools/render-figures.sh` currently aborts at another desk's fig-08-02-rebuild-edges.py (Graphviz shrinks the layout to 74%), so the 06 figures were rendered by running their scripts and terminal.py directly with the same arguments the script uses. Re-run the full script once 08-02 is fixed.
