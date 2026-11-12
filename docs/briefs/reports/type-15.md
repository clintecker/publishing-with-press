# Typesetter report: Chapter 15, The operator's desk and the editorial machines

Status: clean of blocks findings; 0 blocks, 6 should.

Builds
- `press check`: passed (23 Markdown files; checker self-test, editorial and
  jargon checks all passed).
- `press pdf`: exit 0, `dist/publishing-with-press.pdf`, 298 pages; Chapter 15
  is PDF pages 260 to 275 (printed 251 to 266). The log shows two "Latexmk:
  Maximum runs of lualatex reached without getting stable files" notices
  before pandoc finished; not specific to this chapter (other desks were
  building in the same tree). No missing-figure errors: the two figure PNGs
  (`15-01-the-desk.png`, `15-02-editorial-passes-machine.png`) already existed
  as placeholders when I built (not mine; I created and deleted none).
- Page review (text and page images): no heading stranded at a page foot (15.2.1
  "Keys" and 15.9 "Running a workflow headless" each carry three lines of
  text under them); no table wider than the measure; no code line wraps; no
  blockquote box breaks over a page; every example caption sits with its
  fence (15.2 and 15.4 at the page top with the fence under them).

Construct audit: all present and correct. In-this-chapter list matches the ten
A-heads exactly; six tips/warnings (limit 8) and one sidebar (about 150
words); all four examples tagged `text` with `**Example 15.N. Title**`
captions; no code line over 64 columns; no trailing whitespace; no non-ASCII,
no dashes; footnote labels `15-pipe`, `15-popen`, `15-counsel` unique and
defined; six tables with header, proportioned separator and `Table: Table
15.N.` captions; headings sentence case with no two in a row; index comment
last. Figures 15.1 and 15.2: path, `#fig:` id, kind class, `full-measure`,
distinct `fig-alt`, sentence-case caption without period, `@fig:` reference
earlier in the prose, image / one blank line / `art:` comment, comment plus
image line 159 and 170 words (under 190). The plate
(`the-proofreaders-bench.png`) is identical to the stub's two lines
(`git show HEAD`) apart from the added blank line between them.

## Findings (should)

1. Quote: `<!-- index: ... maxim quota; ... -->`
   Rule: "A term must appear in prose (not only in code) somewhere in the
   book." "maxim quota" appears nowhere in the book's prose (the chapter says
   "the quota for coined maxims" and "The quota"); it is not found in the PDF text.
   Severity: should.
   Fix: write the phrase once in prose (for example "the *maxim quota*, two
   coined maxims per chapter by default") or drop the term.

2. Quote: `A typical session on hatter takes counsel first and applies afterwards:` (the fence of eight lines, `$ press improve` ... `$ git diff --stat`)
   Rule: only "Fragments under six lines that are not referred to again need
   no caption"; this fence is eight lines, uncaptioned.
   Severity: should.
   Fix: add `**Example 15.4. A counsel-then-apply session**` above it (the
   later Example 15.4 then becomes 15.5; renumber the prose reference "Example
   15.4 quotes them" and the caption), or cut the session to five lines or fewer.

3. Quote: `1. *Extract.* A scout states ...` (also *Research.*, *Verify.*,
   *Ledger.* in the same list)
   Rule: italics are assigned to filenames, directories, URLs and a new term
   at its definition; step labels are not among them.
   Severity: should.
   Fix: drop the asterisks and keep the label as plain words ("Extract. A
   scout states ...") or make each a plain sentence opener.

4. Quote (Figure 15.2 brief): `ARCHETYPE flowchart, top to bottom. ... "Scout" ...
   "synthesizer" ... "press check" ... diamond ... diamond ... "stop"`
   Rule: the figure is capped at 1740 px tall; a tall figure that is taller
   than wide wants `place=plate`, and a matrix or tree over about 14 rows is
   flagged. This is about eight stacked tiers (scout, two parallel groups,
   suggestions, synthesizers, law, two diamonds), on a width of full measure:
   it will likely come out taller than wide.
   Severity: should.
   Fix: ask the illustrator to lay the tiers out left to right, or to keep the
   composition landscape by running the two diamonds side by side; if it
   stays tall, add `place=plate`. Also the brief shows "(01, 02, ... 12)"
   chapter passes where the book has 23 files; say "one per chapter file" and
   draw three boxes with an ellipsis.

5. Quote (Figure 15.1 brief): `then press p and capture the target picker with its
   argument box. The reader should see first the state column of the artifact table,
   then the toolchain line.`
   Rule: the directive must let one frame show what the caption and fig-alt
   promise. `fig-alt` says the picker is "open over" the tables; an overlay
   will cover the state column the brief wants seen first. The directive
   (screenshot, `.photo`, 100 columns by 36 rows, grayscale, `full-measure`,
   no wrap) is otherwise sound.
   Severity: should.
   Fix: say the picker is to be drawn at the right or bottom, leaving the
   artifact table's state column and the toolchain line unobstructed, or
   split into two captures.

6. Quote: Table 15.5 (`The skills press ships`, eleven rows)
   Rule: a table should not strand its rows; in the PDF it breaks across
   pages 270 and 271 of the PDF (three rows on the second, header repeats).
   Severity: should (print layout only, may move as chapters above change).
   Fix: none needed unless the final pagination leaves one row alone; if so,
   shorten the Meaning sentences of `book-aesthetics` and `humanizer`.
