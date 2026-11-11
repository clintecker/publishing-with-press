# Typesetter report, Chapter 7: Building the editions

File: `book/chapters/07-building-the-editions.md`.

Builds: `press check` FAILED, but only on another file (see Note 1); the
chapter itself is clean in the checker's output. `press pdf` PASSED; the
chapter is PDF pages 116 to 133 (printed 107 to 124). The four 07-NN
figure PNGs were already present (5 KB placeholders made by another desk,
17:35); I created none and deleted none.

Counts: blocks 4, should 15.

## Blocks

1. Quote (line 51, 83, 92, 325; images at 52, 84, 93, 326): the `<!-- art: ARCHETYPE ... -->`
   comment sits on the line BEFORE each image line, in all four figures.
   Rule: markup.md "Figures": the `art:` comment goes on the line
   immediately after the image line; a comment before the image belongs to
   nothing. Severity: blocks (x4, one per figure: 7.1 build-graph, 7.2
   filter-chain, 7.3 defaults-templating, 7.4 press-all-sequence). Fix:
   move each comment to directly under its image line. Comment plus image
   line are 148, 147, 127, and 158 words, so each stays under 190 once
   paired.

## Should

2. Quote: eight untagged fences (opening lines 60, 69, 182, 188, 305, 341,
   371, 407): e.g. "```" above `pandoc --defaults=<root>/build/...`.
   Rule: every fence is tagged `text`. Severity: should (x8). Fix: run
   `tools/tag-fences.py`.
3. Quote (line 183): `--metadata rights="<copyright> Published by
   <publisher>, <place>."` is 66 columns. Rule: code lines at most 64.
   Severity: should. Fix: break after `rights=` with a trailing backslash
   continuation, or shorten the placeholders (`<publisher>, <place>` ->
   `<name>, <place>`).
4. Quote (line 342): `(commerce gate is advisory here; a release build
   (PRESS_RELEASE=1) enforces it)` is 79 columns (under the 80 block
   line). Because the fence is untagged it cannot wrap, and in the PDF
   (p. 121) the line is clipped at the right margin after "enforc".
   Severity: should (becomes a visible truncation until tagged; once
   tagged it wraps with a hook). Fix: tag the fence; since the line is the
   press's real output, either accept the hook or lead with "..." and quote
   the first half in prose.
5. Quote: Table 7.1 (lines 26 to 41), first-column separator is 17
   dashes. Rule: separator proportioned to steer widths. In the PDF
   (pp. 107 to 108) the first column is too narrow: `press html`,
   `press markdown`, `press site`, `press docx`, `press source`, `press
   pages`, `press print`, `press coverwrap`, `press render`, `press clean`
   all break between "press" and the subcommand, so a command reads as two
   lines. Severity: should. Fix: widen column 1 to about 20 percent and
   narrow Meaning, e.g. separator `|--------------------|----------------------|-----------------------------------------|`.
6. Quote: Table 7.2, `SOURCE_DATE_EPOCH` (line 103). First column
   separator (20 dashes) is shorter than the longest cell; in the PDF
   (p. 112) the code word touches and runs into the Meaning text ("EPOCH"
   abuts "The press sets"). Severity: should. Fix: widen column 1 to at
   least 28 dashes and shorten column 2 accordingly.
7. Quote: Table 7.3 first column (line 120): `typographic-spacing.lua`,
   `print-safe-images.lua` hyphen-break in the first column (p. 112).
   Severity: should. Fix: widen column 1 to about 30 dashes.
8. Quote: Tables 7.4 and 7.5 (lines 249 to 287), header "artifact" renders
   as "arti-/fact" on every page of both tables (pp. 117 to 119); the
   first column (12 dashes) is too narrow. The four-column form is allowed
   and both tables fit the measure. Severity: should. Fix: widen column 1
   to 14 dashes, taking 2 from the final column. Table 7.5 column 2 also
   wraps "build (pandoc + latexmk)" into two lines; acceptable.
9. Quote: "When `alice` builds the EPUB on `hatter`, the first lines of output
   look like this:" (line 68) falls at the foot of PDF p. 118 and its fence
   (`$ press epub` ... `...`) starts p. 119. Rule: lead line kept with its
   fence. Severity: should. Fix: unfixable by markup alone; shorten
   preceding prose by a line or reorder so the pair does not straddle, then
   re-render (page flow shifts anyway as the figures replace placeholders,
   so recheck after the real PNGs land).
10. Quote: Example 7.2 "The dist directory after press all" (lines 369
    to 389). The caption and first 7 lines of the 17-line fence fall on
    p. 122 and the rest on p. 123. Rule: caption not separated from its
    fence. Severity: should. Fix: shrink the fence (the six lines under
    `pages/` could be cut to `...`) so it is about 12 lines, or let the
    page flow settle once figures are real, and recheck.
11. Quote: Table 7.1 caption "Table 7.1. The build targets" appears at the
    foot-then-split on pp. 107 to 108, so the table is broken across a
    page after four rows. Severity: should. Fix: none needed in markup; it
    will shift when the layout settles. Recheck after figures land.

## Checked and clean

- Chapter title, "In this chapter" box (ten entries match the A-heads
  exactly), orientation paragraph with no heading above.
- Headings: sentence case, no leading digit, none consecutive, none typed
  numbers. No heading at a page foot in the render.
- Captions: Example 7.1 and 7.2 are bold, directly above their fences,
  no period. Tables 7.1 to 7.5 have `Table: Table 7.N. ...` after the
  table, no period. All five are introduced in prose before they appear.
- Figures: path `assets/woodcuts/07-NN-slug.png`, `#fig:slug`, `.diagram`,
  `width=full-measure`, `fig-alt` differs from caption, captions sentence
  case without period, every figure referenced by `@fig:` earlier (7.1 at
  line 49, 7.2 at 81, 7.3 at 90, 7.4 at 323). No wrap or plate placement.
  Figure briefs: all four are archetype-named diagrams; the state machine
  (7.4) has six states in a row and the stack (7.2) has at most six bands,
  so none is near the 14-row cap; no terminal panel; no wrap.
- Callouts: two tips and three warnings (five of eight allowed) and one
  sidebar ("The lists that would not converge"), all in the blockquote-in-Div
  form with a bold lead; tip and warning lengths are within one to four
  sentences.
- No non-ASCII glyphs, no dash or em-dash, no trailing whitespace, no
  paragraph at 190 words (longest prose paragraph 181 words, line 39;
  line 94 is 183 words), footnote labels `epoch`, `figure`, `rsc`,
  `render` unique, index comment last.

## Notes

1. `press check` failure belongs to another file: `book/chapters/02-installing-press.md:322`
   (assistant vocabulary) and `:324` (staging: run-up).
2. Paragraph at line 94 is 183 words, under the 190 limit but near it;
   same for line 39 at 181. No action needed unless they grow.
3. The PDF builds with placeholders; a stray "latexmk -f" advisory
   appeared in the log tail from a concurrent build in the shared
   `build/`, but the PDF at `dist/publishing-with-press.pdf` completed
   (17:37) and was read.
