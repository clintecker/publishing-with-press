# Typesetter report: Chapter 4, Writing the manuscript

Status: no blocks findings; 6 should findings.

## Builds

- `press check`: FAILED, but only on another file: `book/chapters/02-installing-press.md`
  (paragraphs 40, 104, 118 run 264, 253, 223 words; the law is under 190).
  Nothing named Chapter 4. The checker self-test passed.
- `press pdf`: PASSED (97 pages, Chapter 4 is pages 62 to 79 of the PDF, folios
  53 to 70) after 12 white 1362 by 800 placeholder PNGs were created for every
  missing figure in the book (chapters 1 to 4); all 12 were deleted afterward.
  Without them LaTeX stops at the first missing figure (01-01). No missing-glyph
  warnings; the Example 4.2 glyphs (pound, section, copyright, degree, fraction,
  dashes, curly quotes) all render.

## Blocks

None. Verified clean: no trailing whitespace; no code line over 72 characters;
no language-tagged fences; no non-ASCII in prose (accents and glyph samples sit
only in a table and Example 4.2); no heading with a digit, none typed-numbered,
none two in a row; the "In this chapter" list equals the A-heads exactly;
tip, warning, and sidebar forms correct (tips and warnings 28 to 52 words, 2 to
3 sentences; one sidebar, 188 words; six tips and warnings); art comment plus
image under 190 words in all three figures (170, 177, 175); paragraphs all
under 190; footnote labels unique (`paragraph-law`, `hung-quote`, `ties`; `well`
appears only inside an example fence); all five tables have a header row,
proportioned separator, 2 or 3 columns, `Table: Table 4.N.` caption after the
table; every table, example, and figure is referred to in prose before it
appears; index comment present, last, 25 terms; the plate line and its
comment are untouched.

## Should

1. Quote: `![The three scene-break ornaments ...](assets/woodcuts/04-03-scene-break-ornaments.png){#fig:scene-break-ornaments` (line 320), then `.../04-02-set-pieces.png){#fig:set-pieces` (line 337).
   Rule: image path is `CC-NN-slug.png` in sequence. The scene-break figure
   prints as Figure 4.2 and the set-pieces figure as Figure 4.3, but the files
   are numbered 04-03 and 04-02, so the illustrator's file order contradicts
   the printed order. Severity: should.
   Fix: rename to `04-02-scene-break-ornaments.png` and `04-03-set-pieces.png`
   (path in both the markdown and the commissions), or reorder the sections.

2. Quote: `![The parts of a printed page in the Alice example](assets/woodcuts/04-01-page-anatomy.png){#fig:page-anatomy .diagram width=full-measure ...` (line 43).
   Rule: placement is inline unless a figure is taller than wide and long, then
   `place=plate`. The brief is a miniature 6 by 9 portrait page with eight
   margin callouts, so the picture is likely taller than wide at full measure
   and may meet the height cap. Severity: should.
   Fix: brief the illustrator to a landscape canvas (page centred, callouts
   spread left and right), or set `place=plate`.

3. Quote: the Table 4.2 block (lines 104 to 109), set on PDF pages 67 and 68.
   Rule: tables must not strand rows; the header and one row sit at the foot of
   page 67 and the other two rows continue on 68. Severity: should.
   Fix: shorten the intro or the preceding paragraph so the table stays whole,
   or accept it (the header repeats on the continuation page).

4. Quote: the sidebar `> **A stray asterisk and Fig-ure**` (lines 413 to 427).
   Rule: a blockquote box should not run over a page. It splits across PDF
   pages 78 and 79. Severity: should.
   Fix: none needed in the source if the box is allowed to break; the page
   break will move when chapters 1 and 3 change length, so recheck after the
   writers finish.

5. Quote: `` `10-the-lobster-quadrille.md` ``, `` `notes.md` ``, `` `chapter-four.md` `` (lines 49, 52) and `` `chapter-dropcap.lua` ``, `` `scene-break.lua` ``, `` `set-pieces.lua` ``, `` `typographic-spacing.lua` ``, `` `figure-numbering.lua` `` (lines 279 to 411).
   Rule: italic for a filename, constant width for anything the reader could
   type. The chapter italicizes config and chapter paths (`*book/chapters/...*`,
   `*config/...yaml*`) but sets these filenames in constant width. Severity:
   should.
   Fix: italicize the filenames (`*notes.md*`, `*scene-break.lua*`), or keep
   the example filenames in constant width as typed names and italicize only
   the filter files; choose one and apply it throughout.

6. Quote: the unlabeled epigraph fence at line 189 (`# Down the rabbit-hole` through `Alice was beginning ... sister...`).
   Rule: fragments under six lines that are not referred to again need no
   caption. This one is exactly six lines. Severity: should.
   Fix: drop the blank-line-bounded first line (start at the `>` quote) or
   caption it as an example.

Also noted, not a finding: Table 4.3's caption names `config/metadata.yaml` in
plain roman; the guide would italicize it, but captions are tolerated.
