# Report: Chapter 5, Figures, plates, and illustrations

File: `book/chapters/05-figures-and-plates.md`

## Status

DONE_WITH_CONCERNS (one is a likely press defect worth checking before the
plates are drawn; see "Concerns").

## Word count

`press wordcount`: 5,772 (target 6,000; inside 15 percent). Prose-only
estimate (code, tables, comments stripped): about 280 sentences, average
about 15.5 to 16 words by my counter; no prose sentence over 29 words.

## Gates

- `press check`: no finding names this file. The run fails on
  `02-installing-press.md:315` (assistant vocabulary) and `:317` (staging:
  run-up), another writer's file; an earlier run also showed unreferenced
  plates `02-01`, `02-02`, `04-02`, `04-03`.
- Every table, example, and figure is referred to before it appears.
- Tables 5.1 to 5.6, Examples 5.1 to 5.5, one sidebar (war story 1, 143
  words), three warnings and five tips (eight in all), four footnotes
  (war story 17 is one).

## Figures

Each directive follows its image line after ONE BLANK LINE, the form the
chapter itself teaches (press reads the comment only after the image).
This departs from `docs/markup.md`, which puts the comment before the
image; the brief asked that the chapter's own figures obey its own rules.
`press figures` confirms it reads all three directives.

- 5.1 `@fig:placement-vocabulary` (matrix): seven equal miniature pages,
  4 + 3, gray text lines and one 20% gray block per page placed as inline,
  wrap-inner, wrap-outer, margin, plate, full-bleed, frontispiece (the
  last as a verso facing a ghost recto); monospace label under each; spine
  edge marked. 152 words.
- 5.2 `@fig:wrap-against-text` (page anatomy): an open spread, a
  wrap-inner block hugging the spine on both pages, callouts for
  wrap-inner, outset (with a double arrow across the gap), spine, and a
  bracket labeled "Needspace guard". 137 words.
- 5.3 `@fig:where-a-figure-lands` (data-flow): an image line through
  figure-numbering.lua fanning to PDF (caption Figure 8.1, List of Figures
  entry, \hyperref target; gray fill), EPUB/HTML, reader site (in-flow
  figure, number, link target), text/DOCX (in-flow figure), and a side
  branch from a bare image to the List of Plates ("no number"). 125
  words. I dropped the brief's "bold Figure label" and "strong label":
  the fact file does not say how the label is styled.

## Facts I needed and left out

- The sixth design profile's height cap: the fact file gives five (house,
  novella, digest, large-print, mass-market). Table 5.5 says "the profiles
  that the header names". Exact profile ids were not given either; I used
  the names as the fact file writes them.
- How a credit line is typed: not stated; I say only that it is separate.
- What the checker's refusals print (only "not parity-aware" and the
  orphan-plate message are quoted); I quoted no other message.
- Where the List of Figures appears and whether it, like the List of
  Plates, is conditional: not stated; left out.
- What `decorative` does to the lists: not stated; left out.
- The Markdown edition: section 4.2 says it gets a clean in-flow figure,
  bug B9 says it is raw source with attributes and comments as written. I
  left the Markdown edition out of "What each edition does".

## Contradictions handled (section 20.A.11 and others)

- ILLUSTRATIONS.md "full-bleed and frontispiece ignore width": the chapter
  says the docs say so, then states the validator refuses a measure on any
  non-in-flow place (plate, full-bleed, frontispiece).
- `margin` stated as an outer wrap inside the column; `full-bleed` stated
  as a cleared leaf inside the margins that does not ink the trim.
- Height cap: "per profile; 6.3in on the house 6 by 9" (A.5).
- hypcap: stated as caption's `hypcap=true`, with the old package in a
  footnote (A.4).
- markup.md vs the fact file on directive position: followed the fact
  file (comment after the image), with the blank-line form.

## Concerns (please check)

1. Likely press defect, found while testing pandoc 3.9 locally: an image
   followed by its comment on the NEXT line (the form ILLUSTRATIONS.md and
   the fact file show, and the form Chapter 4's plates use) parses as one
   paragraph of Image + SoftBreak + RawInline. It is no longer alone in
   its paragraph, so pandoc makes no Figure of it, and the image would get
   no caption, number, or List of Plates entry. The blank-line form parses
   as a Figure. Worth a build check of Chapter 4's plates.
2. A wrap cannot carry a directive between it and its paragraph: a
   comment block there stops the filter from fusing the wrap onto the
   next paragraph. Example 5.4 therefore shows a wrap with no directive,
   and the prose says "nothing between them". This rests on the filter's
   behaviour, not on the fact file.
3. `press figures` also reports the image lines inside this chapter's
   code examples (white-rabbit, croquet-ground, tea-party, cheshire-cat)
   as declared figures. Harmless to the build; a `press illustrate
   white-rabbit` in this repository would find it.

## ste_check residuals, with defence

- sentence-length: tables, captions, the in-this-chapter list, art
  comments, and fusions across footnote markers; no prose sentence over
  29 words by my own count.
- paragraph-length over 6: the three art directives only.
- semicolon: inside art directives and the index comment; none in prose.
- passive "is print-only": adjective, false positive.
- -ing forms: the chapter title "Checking the manuscript", table cells
  and directives ("filling").
- "whether", "therefore": allowed by the prose contract. "enhance": the
  command name `press art enhance`.

## Revision (after the four desks)

Status: DONE_WITH_CONCERNS. `press wordcount`: 6,237 (target 6,000).

### Gates

- `press check`: nothing names the chapter file. One source check fails:
  `plate never referenced by the manuscript: assets/woodcuts/croquet-ground.png`.
  That PNG is an untracked placeholder that someone made for my old
  Example 5.2. Ruling 3 replaced that example (see below), so the
  placeholder now has no reference. I did not delete it because it is
  not my file. Please remove it, or create `assets/woodcuts/heights.png`
  for the new example. This also confirms the fact checker's note: the
  orphan check counts image lines inside code fences as references.
- ste_check: what remains is sentence length in tables, fig-alt text,
  comments, and the in-this-chapter list. Paragraph length and
  semicolons occur only in the three art directives and the index
  comment. "is print-only" is an adjective. "however" here means "no
  matter how". "therefore" and "whether" are allowed. "enhance" is the
  command name. No prose sentence runs over 30 words.
- All 18 fences are now tagged `text`. Each figure's image line plus
  comment is under 190 words: 182, 164, and 180 by `wc`.
- Footnote labels now carry the chapter number: `5-silly-plates`,
  `5-tocdepth`, `5-hypcap`, `5-square`, `5-lulu`.

### Rulings applied

1. S1: the chapter states the rule as image line, one blank line,
   comment, and adds a warning that a next-line comment breaks the
   figure silently. The tip now says `press figures` cannot catch that
   fault. S2: Example 5.4 now says it carries no directive, gives the
   reason in the ruling's words, and shows `press illustrate
   cheshire-cat --subject "..."` as a new Example 5.5. The old Example
   5.5 is now Example 5.6. S3: a new paragraph in "Print-safe images"
   says what the pass copies today, reports the "file not found"
   failure, and advises keeping images in `assets/woodcuts/`. S4: the
   chapter now covers the credit line (no field, write it in the
   caption), when each list appears, `margin` rendering the same as
   `wrap-outer`, the text and DOCX editions keeping their numbered
   caption, the Manuscript edition being raw source (named once as the
   exception), and the ornament markup with an example.
2. "every rendered edition" replaces "every edition" throughout.
3. The guardrail is now one line, exactly as given, and attributed to
   `press illustrate` only. The numbered example now has the Alice book
   put a `.chart`, `#fig:alice-heights`, in its own fifth chapter, so it
   numbers as Figure 5.1. The prose and the Figure 5.3 directive both
   say Figure 5.1. Figure 5.3's fig-alt now says "six editions in four
   groups" and gives the text and DOCX editions their number.
4. Copyedit blocks: "shipped" (2), "settle", "wins", "authoritative",
   "clean", "surface", and the meta-narration all fixed. "spine" stays
   (jargon-allow). "fails press check" is now "the checker refuses".
   I made the figure/illustration/plate terms consistent.
5. The TeX passages are cut to what the reader sees: no `\hyperref`,
   `\Needspace`, `wrapfigure`, `\captionof`, `\cleardoubleevenpage`,
   `\pandocbounded`, or `0.4\linewidth` in the prose. The tocdepth
   mechanism moved to a footnote marked for the Chapter 16 reader. The
   words went to the ornament example, commissioning a wrapped plate,
   and a paragraph on Apple Silicon: the arm64 image has no upscaler,
   so a 1024 px delivery stays at 1024 px (about 162 PPI at 6.3 in). On
   the host, press uses an installed Real-ESRGAN or Upscayl if it finds
   one. The tip is rewritten so that it holds on arm64.
6. Markup: fences tagged, directives trimmed, footnote labels renamed,
   and Example 5.4 states why it has no directive. The prose says the
   attribute line breaks are only for page width.

### Other desk items

- Fact checker: Alice claims are now framed as "how you might type".
  The sidebar opens "A book built with press". The default `place`
  sentence, the section-numbers claim, and "the print interior follows
  the same rules" are cut. "On most pages a square plate". The logomark
  points at "its copy in build/print-assets/". `.photo` now says only
  "photograph". "now checks ... with pypdf". "printed at 1.7 inches".
  The cap/enlargement bridge is cut. Added the 7.1 in skills clause and
  the `press art enhance` no-argument form with its `<stem>.png` output.
- Developmental: C1 to C3, P1 to P10 (P8 defines the print interior
  and points to Chapter 12; P9 defines aesthetic, leaf, cleared leaf,
  profile, and "Press's Lua filter"), R1 to R4, O1 (the orientation now
  says what goes wrong), N1 (the bracket now spans the figure and the
  lines beside it), and N2 are all applied.
- Typesetter: 1 to 7 applied. Item 5 is handled as S2 rules: there is
  no comment, with a stated reason. Item 7 adds a sentence saying the
  book uses only `.diagram` and `.photo`. Item 8 declined: the Meaning
  column already gives the value in a sentence, and a third column
  would repeat it. Item 9 kept at 25 terms. "Needspace" left the index
  and "ornament" joined it.

### Copyedit mays

- Accepted: 37, 38, 39, 40, 41, 42, 44, 45, 46, 47 ("ordinary
  figure"), 48 ("center"), 49 ("logomark" throughout).
- Declined: 43. The warning stands before the risky act, which is
  editing the TeX. That is a different moment from the sidebar's
  history, and the house wants a warning there.
- Sidebar: 140 words, inside 120 to 180.

### Figure notes (detail moved out of the directives)

- 5.1: pages 3 and 4 are drawn alike on purpose, because `margin` sets
  as `wrap-outer`. Keep the four-over-three grid and equal page sizes.
- 5.2: show no folios. The bracket labeled "guard" must cover the
  block and its side lines, not the lines above it.
- 5.3: the identifier in the top box is the Alice example's
  `#fig:alice-heights .chart`. Every "Figure 5.1" in the drawing is
  that example's number, not this chapter's Figure 5.1.

## Revision 2 (after the re-review)

Status: DONE. `press check` passes in full (source, self-test,
editorial, and jargon). `press wordcount`: 6,282.

- O1: code lines. The plate caption is now "Alice and the White
  Rabbit" (63 columns). The chart caption is now "Alice's height". The
  guardrail is broken over three lines, and its lead-in now says "The
  prompt receives it as one line, and the breaks here are only for the
  width of the page." No fenced line runs over 64 columns.
- O2: edition names. The chapter glosses the five names once, in their
  own sentence ("They are the Circulating edition (EPUB), the
  Single-leaf edition (the self-contained HTML), the Chapter edition
  (the reader site), the Telegraphic edition (plain text), and the Office
  edition (DOCX)"). Later lines use the short names. The Manuscript
  edition now carries "(the stitched Markdown)". In Figure 5.3's
  fig-alt, "text and DOCX" is now "plain-text and DOCX". The box labels
  in the drawing still name formats, as the reviewer allowed.
- O3: Figure 5.3's caption now reads "Where an image line goes in each
  rendered edition". The sentence that cites it now reads "traces the
  image line of Example 5.2 into each rendered edition", which ties the
  drawn "Figure 5.1" to that example.
- Notes: "A wrapped illustration" replaces "A wrapped figure". The
  print-safe sentence now says the pass works on "each interior image in
  the directories it copies, listed later in this section". "A figure
  taller than the text block" stays, because those are the scar's own
  words.
- Each figure's image line plus directive: 182, 165, and 181 words.

## Revision 3 (after continuity)

The continuity pass found five things. All are applied:

- Every "the Alice example" that meant the full novel now says "the
  Alice book" (lines 18, 44, 184, 237). Line 18 now keeps the two books
  apart: it calls the Alice book user `alice`'s full novel on `hatter`,
  and it says no example comes from the press's own three-chapter
  example.
- An image marked `decorative=true` is now a *decoration*, in the body,
  in Table 5.3, and in the index. "Ornament" no longer appears in the
  chapter.
- "Runaround" now appears only as the trade name, in the A-head and its
  gloss. Line 250 now says "without losing its wrap". The continuity may
  is also taken: *wrap* now has its own definition in italics.
- The closing pointer to Chapter 6 now promises less. It says Chapter 6
  "describes the checker, which applies the rules in Table 5.3 whenever
  it runs".
- Table 5.5: the fact file gives no cap for the color 6 by 9 profile.
  The lead-in therefore says the table lists "five profiles, the ones
  whose caps differ from one another".

`press check` exits 0. `press wordcount`: 6,310.
