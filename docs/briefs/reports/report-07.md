# Report: Chapter 7, Building the editions

File: `book/chapters/07-building-the-editions.md`

## Status

DONE_WITH_CONCERNS (small; listed below).

## Word count

`press wordcount`: 5,798 (target 6,000; inside 15 percent). Prose-only
estimate is about 4,150 words, average sentence about 15 words by my
splitter (it joins footnotes and admonitions, so the true prose average
is a little higher). The rest is tables, examples, captions, and the
four art directives (103 to 118 words each, under 165 with the image line).

## Gates

- `press check` (real repository): fails only on
  `book/chapters/02-installing-press.md:315` (assistant vocabulary) and
  `:317` (staging: run-up), another writer's file. An earlier run failed on
  unreferenced plates `02-01`/`02-02`, also chapter 2. Because the check
  stops at the first failing pass, I ran it in a scratch copy with chapter 2
  removed: source checks, self-test, and editorial checks passed, and the
  jargon lint named nothing in chapter 7 (its remaining findings are in 05,
  06, 08).
- `tools/ste_check.py`: no semicolons or passives in prose. Residuals:
  sentence and paragraph length on tables, numbered lists, the In-this-
  chapter box, art comments, and the dist tree (counted as one sentence);
  `-ing` on headings and chapter titles (Rendering, Checking, Installing);
  "therefore" and "whether" (period-correct per the prose contract);
  "verify" (a target name); semicolons only in quoted press output and the
  index comment; "are cleaned" is inside a quotation from ARCHITECTURE.md.
- No non-ASCII, no trailing whitespace, no dashes.

## Figures

- 7.1 `@fig:build-graph` (pipeline): eight prerequisite-free artifact boxes
  plus sources fed by markdown; nine arrows into a shadowed pages box at
  right; print to coverwrap in a separate bottom row marked "not built by
  press all".
- 7.2 `@fig:filter-chain` (layered stack): three columns (pdf/epub/html/
  chunked, print, portable) of filter names in the fact file's order;
  print-safe-images only in the print column, in 40 percent gray.
- 7.3 `@fig:defaults-templating` (before/after): template with `@press/`,
  `@book/`, and a `?optional` line; rendered copy with absolute paths and
  the optional line struck out. The three paths are schematic: the fact
  file gives the prefix rules but no real defaults-file lines, so I chose
  `@press/tex/book-header.tex`, `@book/config/metadata.yaml`, and
  `@book/assets/web/extra.css?optional` and told the illustrator they are
  schematic. The prose makes no claim about the real file contents.
- 7.4 `@fig:press-all-sequence` (state machine): check, formats, source,
  pages, verify, commerce gate, each with a fail arc to one stop box.

Figure order: to make the filter numbers match the brief (7.2 before 7.3),
Figure 7.2 sits in "What pandoc is told" under "The defaults files" (the
defaults declare the chains); "The filter chain" refers back to it.

Tables 7.1 to 7.5 (7.4 and 7.5 are the REFERENCE.md tables reproduced
verbatim, four columns each, per the controller), Examples 7.1 and 7.2,
one sidebar (war story 4, about 125 words), war story 6 as a body scar
paragraph, three tips, three warnings, three footnotes. Every numbered
item is referred to before it appears.

## Facts I needed and left out, or took from elsewhere

- `press wordcount` behavior and captured output come from facts-C (shared
  fact base), since facts-07 has none.
- No captured `press all` or `+ pandoc` output exists; the session shows
  the fact file's command form with `<root>` and `...`, and timing lines
  use the literal `N.Ns`.
- What `press html`'s "table-cell labels" are: stated only as labels
  added to table cells.
- Which edition targets the FORMATS list holds: step 2 says "each edition
  target" without listing them.
- What the commerce gate checks: not described.
- Exact `press render` filenames: given as `page-*.png` only.

## Contradictions and bug-list items avoided

- B.13: `press all` builds neither print nor coverwrap; stated plainly. I
  did not say the release commerce gate builds them.
- B.11 (verify-formats reads a possibly stale PDF) and B.12 (verify-print
  builds the interior twice): omitted.
- B.9/B.10 (raw Markdown edition, no drop cap or scene break in txt/docx):
  stated neutrally as mechanism, not as features.

## Revision (after facts, dev, copy, and type desks)

`press wordcount`: 6,199 (target 6,000). Prose without code, tables,
captions, and comments: about 4,850 words, 78 percent.

Gates: `press check` names nothing in chapter 7. It exits 1 on the jargon lint in
another writer's file,
`05-figures-and-plates.md` (rewrite: "authoritative"). `ste_check` residuals
are the same kinds as before: the In-this-chapter box, art comments and
image lines, numbered lists, the index comment, and "however",
"therefore", "whether", and "verify" (a target name). The passive "are
cleaned" sits inside a quotation. No prose semicolons. Every prose
paragraph runs six sentences or fewer.

What changed, by ruling:

1. S1 to S3 are in, with the slug changed to `alice` and the source named
   as "the press's own three-chapter Alice example". Example 7.1 is now the
   real HTML echo line, broken at 64 columns. Examples 7.2 and 7.3 are
   excerpts from S2 (the template, and the rendered copy with `lof: true`
   and the `metadata:` block). Figure 7.3's directive uses the real lines,
   and `@book/tex/title-page.tex?optional` is the dropped entry. "What press
   all does, in order" is now built on Example 7.4 (S1, elided to 64
   columns). It walks the six steps against the phase lines in a plain
   numbered list, names the step 2 order (PDF, EPUB, HTML, Markdown, text,
   Word, site), and shows Alice's real commerce-gate line. The advisory
   line follows as what an ordering-enabled book prints. "Reading the log"
   and "What the build leaves behind" moved into that section. The
   wordcount example is S3. No `<root>` or `N.Ns` is left (the time is
   `pandoc took 26.7s`, framed as one run on one machine).
2. Contradictions fixed: plus-sign lines are described as steps, and the
   two status lines are named as non-commands. The source zip does not
   call pandoc (Table 7.1 and the Markdown paragraph). The `press all` row
   no longer covers `render`, and the prose says so. The print-pack
   paragraph and warning now say an *ordinary* `press all` builds neither,
   with the commerce-gate exception. "Mr." is gone from Table 7.3. The
   input order follows facts-03 S3. The Source-edition tip is advice ("We
   suggest"). The prose says the EPUB echo needs quotes before you paste
   it.
3. Copy blocks: "ships" and "shipped" are gone. The closer is cut. The
   `press all` list has no bold labels. "Cover wrap" is used throughout,
   with "cover-wrap verifier". "Refuses" is used for press stops.
   "Invariant" is defined at first use, "aesthetic" replaces "look", and
   "Source edition" is used consistently. *Edition* and *artifact* are
   italic and defined at first use. Should items 5 to 32 are applied.
4. Dev: the TeX macros, `\directlua`, the Lua-coverage warning and its
   test story, `dirs_exist_ok`, the press-util internals, and the
   documentation-timing sentence are cut. The CI test fact is now one
   sentence with an "at the time of this writing" footnote. The sidebar
   carries the history and the body carries only the mechanism. Each tip
   holds only its action. The sources companion is described once, under
   "Generated inputs". GitHub Release and the Pages site are defined. The
   press-repository paths are labeled as such.
5. Markup: each `art:` comment now follows its image line after one blank
   line (`space-art-comments.py` reports 0 inserted, since the comments
   were written that way). Every fence is tagged `text`. No code line is
   over 64 columns: the rights placeholder moved to prose, and the two
   long press messages are broken with a note that the log prints each on
   one line. The table separators are re-proportioned (column 1 is 24, 30,
   32, and 16 dashes). The old line-88 and line-90 paragraphs are split.

Declined (may):

- Copy 40 (man-page references): applied to latexmk(1) and pdftoppm(1).
- Copy 38 (comma inside the quotation mark): applied to the two places in
  this chapter. The book-wide ruling belongs to the managing editor.
- Fact U10, last sentence: I kept the line about what the count strips
  and that it counts HTML comments. It comes from facts-C, the shared fact
  base, and the managing editor has not ruled on it. Cut it if facts-C
  does not govern.
- Dev P6 (table-cell labels, reader metadata): kept as bare clauses,
  because no fact explains either step further.
- Fact M7 (policy pages in Example 7.5): left out. Alice does not enable
  ordering, and the tree is now shorter for the page flow (type desk
  item 10).
- Type 9 and 11 (page breaks): depend on the final figures, so recheck
  after the PNGs land.

## Revision 2

All three footnote labels (`[^7-epoch]`, `[^7-lua]`, `[^7-rsc]`) are confirmed at both the reference and the definition. Edition names are glossed once after Table 7.1, and the portable editions carry their landing-page names at first mention in "The portable editions". The repeated cover sentence (244) is cut, "every pandoc build" is no longer said twice (359), and the verify-step list item is split. `press check` names nothing in chapter 7.

## Revision 3

Added the `press verify-formats` exception after "Every verify target rebuilds the artifacts it verifies": it reads an existing *dist/alice.pdf* into its agreement check without rebuilding it. "Page bundle" is now "the Pages bundle" throughout, and line 316 now separates the bundle (*dist/pages/*) from the Pages site. "The Alice book" covers the sample-book uses (the opener, the slug, the dist tree). The captures use "the press's own three-chapter Alice example" at first mention (and again before S3), then "the three-chapter example", because the vocabulary forbids a bare "the Alice example". `press check` exits 0 and names nothing in chapter 7.

## Revision 4

Past the gloss, the chapter now calls three editions by the press's names: the Manuscript, Telegraphic, and Office editions. That covers both B-heads, the `press all` step list, the `verify-formats` list, and the dist tree, and the format words appear only in parentheses or where the sentence is about the file. The gloss's closing sentence now says which editions keep their format names (PDF, EPUB, single-file HTML, reader site). The old line 59 is split: the three-chapter example lives under *examples/alice-in-wonderland* in a press checkout, the Alice book (the full novel) lives in *~/alice*, and the captures print *~/alice* so their paths match. The dist tree says "the Pages bundle". The registry is "the one statement of the artifact graph". `press check` exits 0 and names nothing in chapter 7.
