# Report: Chapter 4, Writing the manuscript

File: `book/chapters/04-writing-the-manuscript.md`

## Status

DONE_WITH_CONCERNS (concerns are small; listed below).

## Word count

`press wordcount`: 5,718 (target 6,000; inside 15 percent). Prose-only
estimate (code, tables, comments stripped): about 4,450 words in about
270 sentences, average about 16.3 words. The rest is examples, tables,
captions, and art directives.

## Gates

- `press check`: no finding names this file. The run still fails on
  paragraph-length errors in 01, 02, and 03 (other writers' files; rerun
  once, same result).
- Paragraphs: the three figure `art:` comments plus their image lines
  count as one paragraph each to the checker; first drafts of the
  directives tripped the 190-word law and were cut to fit (about 110 to
  130 words each). The same failure is what currently breaks 01 to 03.
- Plate: the two plate lines are byte-identical to the stub, moved to the
  end of "Headings and chapters".
- Note: at the time I finished, HEAD (`d3a3c72` or an earlier commit by
  another hand) already contained an intermediate version of this file.
  I did not commit; the working tree holds the final version.

## Figures

- 4.1 `@fig:page-anatomy` (page anatomy): one 6 by 9 page in outline with
  eight numbered margin circles (running head, folio, chapter title,
  section heading, body text, footnote, blockquote box, numbered figure
  and caption); key given in the prose.
- 4.2 `@fig:scene-break-ornaments`, *04-02-scene-break-ornaments.png*
  (matrix): rows rule, asterism, fairy-dust by columns PDF, Reader; only
  the rule differs (diamond between tapering hairlines on the reader site).
- 4.3 `@fig:set-pieces`, *04-03-set-pieces.png* (before/after, three
  frames): the same four lines of "Alice's Right Foot, Esq." as cascade
  (stepped), verse (one indented edge), and tail (S-curve, shrinking
  type), labelled (a) to (c) beneath.
- (Corrected in revision: the first report numbered these the wrong way
  round. Scene breaks precede set pieces, so they print as 4.2.)

Tables 4.1 to 4.5, Examples 4.1 to 4.9, one sidebar (war story 22),
three warnings, three tips, three footnotes. Every numbered item is
referred to before it appears.

## Facts I needed and left out

- The checker's exact message for em dash, en dash, and curly quotes in
  prose (the known-bad output suggests the glyph message fires for
  dashes, but the fact file does not say); I named no message.
- Whether prose rules skip inline code spans (only fenced code is
  stated); I made no claim.
- The 21 small words of the title-case test; the example is built to
  hold whether or not "In" is on the list.
- The `config set` dotted-key form `chapter-opening.style` comes from the
  key listing in facts-03/B, not from a captured session.
- Which chapter covers sentinels: I pointed to Chapter 8, *Verifying the
  artifacts*; the fact file says "§3.3 and §6" of the fact base. Please
  check against the final 03 and 08.
- `raised-cap` left out (renders as `drop-cap`, listed as bug B7). The
  txt/docx lack of drop caps and scene-break ornaments, and the Markdown
  edition's raw `:::` source, left out (B9, B10).

## Contradictions

- The glyph law range U+00C0 to U+017F includes the multiplication and
  division signs (the fact file says so); `docs/markup.md` lists the
  multiplication sign as forbidden. The chapter states the press law.
- `typographic-spacing.lua` ties after the section sign and the pilcrow,
  but the glyph law forbids both in book prose. I listed only the
  typable reference forms.
- `docs/markup.md` puts the `art:` comment before the image line; the
  fact file (4.2) describes it after the image. I followed markup.md.

## ste_check residuals (36 findings), with defence

- sentence-length over 25: tables, the In-this-chapter list, art
  comments, abbreviation lists (Mr., Dr., p.), and sentences the tool
  fuses across a colon before a code block or across a footnote marker.
  By my own count no prose sentence exceeds 30 words except where those
  fusions occur.
- semicolon: in the plate and figure `art:` comments, in the quoted
  checker message `(the law is under 190; split it)` inside a code span,
  and in the index comment. None in prose.
- passive "is Markdown", progressive "is trailing": false positives
  (copula plus noun; "trailing whitespace").
- `-ing` forms: headings and chapter titles (Checking, Verifying,
  Writing, Referring) and the term "trailing whitespace".
- "therefore" (allowed by the prose contract), "identical" (art comment),
  phrasal verb "look at" (sidebar, "look at the proof").
- paragraph-length over 6 sentences: the art comments only.

## Revision (after the fact, developmental, copy, and type desks)

Word count after revision: `press wordcount` 6,455; prose only (code,
tables, captions, art and index comments stripped) about 5,240, inside 15
percent of 6,000. `press check`: no finding names this file. The live run
stops at source checks on two orphaned plates in Chapter 2
(`02-01-doctor-report.png`, `02-02-tools-in-the-build.png`), not mine; in
a scratch copy with those removed, source checks pass and editorial
failures name only 02 and 08. ste_check: residuals as before (art and
index comments, headings, "Figure 4.1" split as a sentence end, the
"trailing" false positive); no prose semicolon, passive, or perfect.

### Coordinator rulings

1. Applied. All three `art:` comments now follow their image lines.
2. Applied. Paths and ids: scene breaks `04-02-scene-break-ornaments`,
   set pieces `04-03-set-pieces`. The two untracked placeholder PNGs in
   *assets/woodcuts/* were swapped by `mv` to the new names (otherwise
   `press check` refused them as orphaned plates). No other file touched.
3. Applied. S1 now supports the Alice claims (three chapters, drop cap,
   fairy-dust, the Mouse's Tale, the dialogue opener); "2.1 / 2.1.1" cut.
   S2 gives Tables (no numbering filter, caption above, centered small
   italic, no automatic label, caption element on the Web, no List of
   Tables, widths from the separator row past 72 columns) and Code
   (pygments highlighting in color, unchangeable; language tags color the
   print interior and `press verify-print` refuses it with its message;
   untagged or `text` print black; inline code exempt; smart typography
   leaves code alone). Paid for by cutting `fvextra` options, the lettrine
   parameters, `\Needspace`, `\scshape`, `\PressFairyDust`,
   `\PressVerse`, the size ladder, Table 4.5, and the byte-for-byte line.
4. Applied, verbatim.
5. Applied. "every rendered edition" throughout; the Markdown exception is
   named once, at the end of "The dialect".
6. Applied. `{.unlisted}` cut. Defaults files: "inside its own package";
   path removed.
7. Applied. `lines` row now states only the default of 3.
8. Applied. Example 4.2 is a `text` fence of six lines (pound, section,
   copyright, em dash, two curly quotes); the invisible no-break space row
   is gone.
9. Applied. "Rev. Dodgson".
10. Applied. lands (2), ships (2) removed; checker "fails" now "refuses";
    gray, color, centered, period (for full stop); "the reader site"
    throughout prose. British spellings in art comments also changed.
11. Applied. Figure 4.1 has ten callouts (drop cap and scene break added,
    first paragraph opens with a three-line drop cap); `place=plate`, no
    measure (a measure on a plate is refused). Moved to the head of
    "Headings and chapters" (dev N2).
12. Applied. Directive plus image line: 169, 177, 175 words (my count;
    press check passes). Sidebar about 155 words. The tail paragraph is
    split in two.

### Fact desk

- 1.1 footnote scope: applied from S2 (unique across the whole book).
- 1.2 Alice claims: kept, now supported by S1; 2.1/2.1.1 cut.
- 1.3 "before any build begins": cut.
- 1.4 `press config set`: kept; supported by the key listing in facts-03
  and facts-B. Wording now names the command (copy 8).
- 1.5 glosses: "pandoc numbers the heading itself" applied; 72-column tip
  kept as house advice; card wording cut to "turns each row into a card";
  t definition cut; Lobster example replaced (see copy, fact notes).
- 2.1 sentinels: applied (ruling 4).
- 2.2 every edition: applied (ruling 5).
- 3.1 reference forms: "for forms such as". 3.2 190 boundary: "must be
  under 190 words ... refuses a paragraph that breaks the law". 3.3
  Down the Rabbit-Hole: applied. 3.4 "at least two digits": applied. 3.5
  "Press calls this Bringhurst's rule": applied. 3.6 Lua footnote:
  applied. 3.7 no-break space row: removed.
- 4.1 Markdown set pieces: covered by the single Markdown exception in
  "The dialect" (ruling 5 says name it once). 4.2 txt/docx: one sentence
  each in drop caps and scene breaks. 4.3 `raised-cap`: one flat sentence.
  4.4 appendix letters and index position: one paragraph, pointer to
  Chapter 10.

### Developmental desk

- C1 applied (ruling 11). C2, C3 applied from S2.
- P1 applied (ruling 6). P2 applied: the cell says a press book keeps its
  metadata in *config/metadata.yaml*. P3 applied (cut). P4 applied
  (ruling 7). P5 applied: jargon lint defined in a clause, pointer to
  Chapter 6. P6 applied: no attribution field; write the source as the
  last line of the blockquote. P7 applied. P8 declined per ruling 8 (the
  typesetter saw no missing glyphs). P9 applied.
- R1 applied (Table 4.5 cut; "suits" clauses folded into the B-heads).
  R2 applied (one paragraph, renamed "The book's own rules"). R3 applied.
  R4 applied (recap cut; figure-numbering fact kept in one sentence). R5
  applied. R6 applied.
- N1 applied (ruling 2). N2 applied.
- Length: to keep prose inside the band after the cuts I added short,
  advice-only paragraphs (splitting a long paragraph, plain line block
  versus set piece, length of a chapter's first paragraph, why the ties
  matter, footnote length, copying sessions from a terminal). None adds a
  press fact.

### Copy desk

- 1 to 4 (blocks): applied.
- 5 to 28 (should): all applied. 13 "honorific"; 14 *chapter file*
  defined at first use; 15 "described later in this chapter"; 16 "no drop
  cap or other special first letter"; 17 *checker* defined; 18 to 21
  "the reader site"; 27 warning made imperative; 28 recap cut.
- 29 to 39 (may): 29, 32, 33 (folded into the one-paragraph rewrite), 35,
  36 (superseded by the new callout paragraph), 37, 38 applied. 30, 31,
  39 moot: the macro names, the `fvextra` sentence, and the byte-for-byte
  sentence are cut. 34 moot: the banned-patterns paragraph is reduced to
  one sentence under "The book's own rules".
- Fact notes: Tenniel 1866 now "Press describes it as Tenniel's 1866
  array" (the fact file's wording; I have no other source). `\caption*`
  and the float package: kept as the fact file states (war story 22).
  Leading apostrophe in "'Tis": the verse example now uses "How doth the
  little crocodile" (Carroll ch. 2). Lua coverage release: kept as war
  story 21 states (3.0.2). Dr. Dodgson: ruling 9.

### Type desk

- 1 applied (ruling 2). 2 applied (`place=plate`, ruling 11).
- 3 (Table 4.2 split across pages) and 4 (sidebar split): not applied in
  source; page breaks move as chapters 1 to 3 change. The sidebar is
  shorter now, and a recheck after the other chapters settle is needed.
- 5 applied: filenames and filter files in italic (*notes.md*,
  *chapter-dropcap.lua*, and so on); commands, keys, and typed values
  stay in constant width.
- 6 applied: the epigraph fragment is four lines.

## Revision 2 (scoped re-review, `rereview-04.md`)

Gates: `press check` passes in full (source and editorial, 23 files).
`press wordcount` 6,458; prose about 5,250. ste_check residuals are the
accepted classes only (art and index comments, image lines with fig-alt,
headings, the honorific list, the "Figure 4.1" split, footnote fusions,
"trailing", "identical", "look at").

- O1 (blocks): applied. Code now says a `text` fence prints black and
  wraps a long line with a hooked mark; an untagged fence is verbatim and
  a long line runs off the page; a language tag colors the print
  interior and `press verify-print` refuses it. "We tag every fence in
  this book `text`, so it prints in black and wraps." Ran
  `tools/tag-fences.py`: 14 fences tagged; all 15 opening fences are now
  `text`.
- O2: applied. Tip says 64 characters and that a `text` fence wraps.
- O3: applied differently. "and never" to "but never" is the same
  length (65 characters both), so the line is now "The Hatter's watch
  told the day of the month, never the hour." (61). No code line in the
  chapter exceeds 64 characters.
- O4: applied. Split into two sentences ("...wants to be a table. The
  section "Tables" later in this chapter covers them.").
- New rule (blank line between image and comment): confirmed. All four
  read image line, blank line, `art:` comment (page anatomy 46/48, plate
  99/101, scene breaks 331/333, set pieces 351/353). The chapter teaches
  no `art:` example in prose (it defers figure markup to Chapter 5), so
  there is nothing else to change.
- Notes taken: line 22 split into two sentences as suggested; the
  sentinel sentence now says "the verifiers look for in each finished
  edition", agreeing with Chapter 8. Two other sentences that ste_check
  counted at 31 to 32 words (the file-name warning and the authorities
  sentence) were shortened.

## Revision 3 (continuity, `continuity-04.md`)

Applied: (1, blocks) Figure 4.1 is the chapter's opening page with no running head and the folio centered at the foot; nine callouts, a sentence saying later pages carry the running head, brief and fig-alt renumbered; (2) line 18 separates press's three-chapter gallery Alice from the full-novel sample `alice` on `hatter`; (3) press's edition names glossed once (Manuscript, Print, Circulating, Single-leaf, Chapter, Telegraphic, Office) and used after; (4) Chapter 6 "explains" sentinels; `top-level-division: chapter` limited to the PDF and EPUB builds; footnote labels renamed `[^4-paragraph-law]`, `[^4-hung-quote]`, `[^4-ties]`, the example label `[^2-well]`, and the advice now says to start each label with its chapter number (the example note was trimmed to 63 columns). Not taken: mays 6 to 8 (6 left for a later pass, 7 and 8 need no chapter change). `press check` passes in full; wordcount 6,510.

Also applied (coordinator, late item): inline code is exempt from the glyph law and the jargon lint, but a book's banned patterns skip fenced code only and fire on backticked spans in prose; line 243 now says so.
