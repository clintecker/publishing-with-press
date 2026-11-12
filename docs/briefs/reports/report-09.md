# Report: Chapter 9, The house design

File: `book/chapters/09-the-house-design.md`

## Status

DONE_WITH_CONCERNS (small; listed below).

## Word count

`press wordcount`: 5,708 (target 5,000; inside 15 percent, near the upper
edge). Cut from a 6,377 first draft. `ste_check.py` reports 377 sentences,
average 13.3 words (its counter treats identifiers as one word and counts
table rows and the In-this-chapter box as sentences).

## Gates

- `press check`: source checks, checker self-test, and editorial checks all
  pass. The run exits 1 only on the jargon lint, on
  `book/chapters/05-figures-and-plates.md:75` ('authoritative'), another
  writer's file. Nothing in chapter 9 is named.
- No non-ASCII, no trailing whitespace, no dashes, every fence `text`, no
  code line over 64 columns.
- 7 tips and warnings (5 tips, 2 warnings), 1 sidebar (134 words),
  3 footnotes, 7 tables, 2 examples, 3 figures, 25 index terms.

## Figures

- 9.1 `@fig:page-geometry` (page anatomy, to scale): the 6 by 9 page with
  dimension lines for inner 0.78, outer 0.68, head 0.72, foot 0.78, headsep
  0.20, footskip 0.38, the 4.54 by 7.5 text block, and a bracket for the
  6.3in figure cap.
- 9.2 `@fig:profiles-compared` (matrix): six profiles by trim, text width,
  figure cap, body size, intended use. Text width is filled only for the two
  house profiles (4.54in, stated in the fact file); intended use only for
  house (default), color (color interior), and large print. Every other
  such cell is blank by instruction. Body size is 10pt in every row.
- 9.3 `@fig:reader-site` (screenshot): a real light-theme reader-site
  chapter page of the Alice example at desktop width, showing the cloth
  frame, masthead, closed contents drawer, Chapter N line and heading with
  diamond rule, drop-cap paragraph, a plate on its mat, and pager cards.
  The illustrator should pick a chapter that opens with a plate.

## Facts I needed and left out

- Text width for the four non-house profiles. Trim minus margins would give
  3.75, 4.14, 5.35, and 3.17in, but the fact file states only the house
  value, so the cells are blank.
- An intended use for novella, digest, and mass-market. The fact file gives
  none beyond the names.
- The exact `extra.css` of the chapbook example. The fact file gives only
  `.reader main {max-width: 30rem}` and "line-height 1.85", so the prose
  describes it and Example 9.2 is an Alice file instead. Its dark-mode plate
  panel copies the pattern of this book's own `assets/web/extra.css`.
- The value syntax of `web-palette` (quoted `#rrggbb`) comes from this
  book's own `config/aesthetic.yaml`, not the fact file.
- `press aesthetic` printing the effective merge (CLAUDE.md says so; the
  fact file does not). Not used.
- What happens to unnamed palette tokens after a top-level replace. Not
  stated; the chapter says only that the whole section replaces the house
  section and tells the reader to restate it in full.

## Contradictions and hazards in the fact file

- 7.2 quotes PRINT-FORMATS: large print "sets a larger base face", and in
  the next sentence says every profile's font size stays 10pt. I followed
  the 10pt statement (code) and did not quote "larger base face".
- 7.1 gives print margins 0.88/0.58 as a fact; 20.B.1 says they may apply
  to every profile regardless of geometry. The chapter states them for the
  house page only.
- Left out as bug-like per section 20: `raised-cap`, the fixed `lang="en"`
  on the landing page, the landing page's trim text (B.3), and txt/docx
  having no drop cap or ornament.
- 7.1's six "penalties" include two demerits (`\finalhyphendemerits`,
  `\doublehyphendemerits`), for which 10000 is not infinite. The chapter
  says "six values" and gives the two demerits their real meaning.
- Chapter 5 says an alpha-master plate "reads on a light page or a dark
  one"; Example 9.2 adds a light panel in the dark theme. I framed it as the
  Alice author's choice, not as a fix.

## ste_check residuals and defence

- Sentence/paragraph length at lines 6, 25, 140-141, 200-201 and in tables:
  the In-this-chapter box, figure image lines with art comments, and table
  rows.
- Paragraph length at 53: the sidebar, which the markup counts as one
  paragraph (134 words).
- Passive 'is silently ignored' (53) and 'is emitted' (215): quotations
  from press source. 'is green', 'is centred', 'is 10pt', 'is filled':
  adjectives or table text, not passives.
- Semicolons at 136 (inside a quotation from PRINT-FORMATS.md) and the
  index comment.
- 'therefore' (period-correct per the prose contract), 'identical' (in the
  figure alt text), '-ing' on chapter titles in cross-references
  (Installing, Writing) and on 'choosing' inside a quotation.

## Revision (after facts, dev, copy, and type desks)

Word count: `press wordcount` 5,694 (was 5,708). `press check` exits 0 (all
four passes, including the jargon lint). No non-ASCII, no trailing
whitespace, no code line over 64 columns. Sidebar 133 words. Footnotes
prefixed with `tools/prefix-footnotes.py` (`9-libertine`, `9-hypcap`,
`9-migrate`). All three `art:` comments sit after their image line with one
blank line (confirmed).

### Coordinator rulings

1. Examples. Example 9.1 is now "An aesthetic file for the Alice example",
   introduced as what `alice` writes. Every key and value form follows the
   house aesthetic captured verbatim in facts-11 section 8.8 (quoted
   `'#rrggbb'` palettes, bare hex `book-colors`). The `extra.css` dark-panel
   example is cut. "Extra CSS" now shows the chapbook's fact-file rule
   `.reader main {max-width: 30rem}` as an uncaptioned fragment. The Chapter 5
   conflict is gone with it. The running-head strings are gone. The
   paragraph gives the mechanism only: book title inner (left on the
   one-sided PDF), chapter title outer.
2. The contents page "lists the chapters". Line about Example 9.1 counts
   what it writes: nine light tokens and all four book colors. The two reds
   are named as two values (accent = cloth red, link = deep cloth red).
3. Developmental. "Six profiles" names `print.profile` in
   *config/metadata.yaml* (facts-03) and shows
   `press config set print.profile novella-5x8` for alice on hatter, with
   the diff elided and a pointer to Chapter 3 for the trim refusal. "The
   aesthetic file" ends with `press aesthetic` and Example 9.2, an excerpt of
   the facts-11 capture in a fresh book. "The reader site" says to run
   `press site` and open *dist/site/index.html*. The first A-head opens on
   the page the reader sees. The class options moved to "The print
   interior" with one-sided and two-sided glossed. *Craft law* is glossed at
   first use, with a pointer to Chapter 11. The drawer "starts closed" and,
   when opened, lists the chapters with the current one expanded. The prose,
   directive, and alt text now agree. The CSS measures (clamp, 4px outline,
   3.1em drop cap, rel links, card rows) are cut. Table 9.3 and Table 9.5
   now say what each color or token paints. Where the fact file gives no
   use (`rulegray`, `accent`, `--ink-soft`), the row says so plainly.
   Table 9.5 now also lists the three derived tokens. Figure 9.2 drops the
   body-size column, and the prose says it is 10pt in every profile. The
   blank cells stay blank.
4. Copyeditor. The six heading-restating openers are rewritten. "numerals"
   replaces "figures" twice. "List of Plates" is capitalized. Each edition
   name is glossed once (Print, Chapter, Single-leaf, Circulating).
   "centre/centred" is now "center/centered", in alt text and directives
   too. *design profile* (17), *aesthetic* (76), *folio*, and *leaf* (Table
   9.4 intro) are defined at first use. "measure" now means only the figure
   classes, and the Web value is the "leaf width". The two long sentences
   are split. The fact notes are fixed: four values, four of six colors,
   "the indent and the leading change with the page", "five words", two
   reds, and the token count.
5. Markup. Figure 9.1 is `half-measure`, and its directive says to draw it
   narrow. Chapters 10 and 12 now have titles at first mention. Tables 9.5
   and 9.6 have a Meaning column.

### Fact-desk items also applied

The figure-cap purpose clause is cut. The `web-palette` syntax now rests on
the facts-11 capture. The tip now says only that "the merge replaces the
section as a whole". The replacement-sheet warning drops "no longer" and the
unset-width consequence. Logomark and portrait art direction are supported
by the facts-11 house aesthetic. "Where the binding takes up paper", "a
printer bills", "although many designs leave it off", and the per-row Table
9.1 glosses are softened or cut. The `hypcap` link is limited to the List of
Plates. "Issue 262" is now "number 262". Unsupported placements ("above",
"below the masthead", "one per row") are cut. Added: no shipped profile sets
a drop cap, large print's 1.4rem Web type, the landing page's `Book` with
`workExample`, and `rule` as the default scene break.

### Declined or deferred

- Copy 40 (italic *alpha masters*): moot, because that sentence went with
  the cut example.
- Type 4 (Table 9.5 splits across folios) and type 5 (Example 9.1 caption
  at a page foot): layout changed since the desk's build. I did not rebuild
  the PDF, so the managing editor should check both on the next `press pdf`.
- Dev N3 (fill text width by arithmetic): declined per the coordinator's
  ruling. The cells stay blank.
- Dev R1 "keep Metadata in the head": kept as is.

## Revision 2

"The Alice example" now reads "the Alice book" at lines 21, 137, and 279
(the Example 9.1 caption). Around Figure 9.3 (204 to 208), the prose now
says "the press's own three-chapter Alice example", and the caption and
directive say "the three-chapter example". The links sentence at 306 now
begins "In the light theme,". `press check` exits 0, and the word count is
5,701.

## Revision 3 (continuity)

- *Leaf* now keeps its trade sense. The reader site's framed column is the
  *paper column*, defined at the Table 9.4 lead-in, and "column width"
  replaces "leaf width".
- "Height cap" is the term throughout, with the `figure-cap` key named
  once.
- Figure 9.2 is now fully filled. The intended uses come from the fact
  base's profile descriptions, as in Table 12.2. The four non-house text
  widths are derived from Table 9.4 (3.75, 4.14, 5.35, 3.17in), and the
  prose and the art directive both say so. The "blank cell" sentence is
  gone.
- Table 9.5 now gives `--hairline` and `--ornament` with their dark-theme
  swap and their full uses. In Table 9.3, `accent` is "defined by the
  header and used nowhere", and the Example 9.1 lead-in says so too.
- I cut four low-value sentences to stay in the band. `press wordcount`:
  5,725. `press check`: the editorial pass fails only on
  `book/chapters/16-inside-the-press.md:232`, another writer's file.
  Nothing in chapter 9 is named.
