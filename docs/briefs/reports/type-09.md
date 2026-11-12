# Typesetter report: Chapter 9, The house design

Status: 3 blocks, 6 should. `press check` exits 1 but no finding names
Chapter 9 (7 findings, all in 05, 06, and 12). `press pdf` completed
(exit 0, 238 pages; Chapter 9 is folios 147 to 162). Figure PNGs for
09-01..09-03 were already present (5.0k placeholders written by another
desk at 17:44); I created none and deleted none.

## Blocks

1. Quote: `[^hypcap]` (lines 65, 67)
   Rule: footnote labels begin with the chapter number; unique book-wide.
   pandoc warns: "Duplicate note reference 'hypcap' at
   book/chapters/09-the-house-design.md line 67". Chapter 5 line 347 also
   defines `hypcap`; the merged PDF then has two notes colliding.
   Severity: blocks.
   Fix: rename to `[^9-hypcap]` at both places (Chapter 5's owner should
   rename theirs to `[^5-hypcap]`).

2. Quote: `[^libertine]` (lines 84, 86)
   Rule: as above. pandoc warns "Duplicate note reference 'libertine' at
   ... line 86". Chapter 1 line 311 also defines `libertine`.
   Severity: blocks.
   Fix: `[^9-libertine]` (Chapter 1's owner: `[^1-libertine]`).

3. Quote: `[^migrate]` (lines 361, 363)
   Rule: label must begin with the chapter number. No collision today.
   Severity: blocks (markup guide "every label begins with the chapter
   number").
   Fix: `[^9-migrate]`.

## Should

4. Quote: Table 9.5 (lines 172-182), "Token | Light | Dark"
   Rule: PDF check, table split. The table breaks 4 rows / 5 rows across
   folios 154 and 155 (header repeats, so it is legible).
   Severity: should.
   Fix: none needed if tolerable; otherwise reorder the intro so the table
   falls earlier on the page. Not fixable by markup.

5. Quote: Example 9.1 caption, "The design part of the Alice example's
   aesthetic.yaml" (line 275 area)
   Rule: an example caption must not be separated from its fence. The
   caption and first 2 lines sit at the foot of folio 158 and the fence
   continues on folio 159.
   Severity: should.
   Fix: shorten the example (drop the `web-palette-dark` block to cut
   about 8 lines is not enough alone); better, move the sentence that
   introduces it up or trim prose above so the fence starts a page.
   The 64-column rule is met (no line over 64).

6. Quote: Figure 9.1 `.diagram width=full-measure` with brief "page
   anatomy, portrait, to scale" (lines 25-27)
   Rule: a figure taller than wide takes `place=plate`. A 6 by 9 portrait
   at full measure (4.54in wide) would be 6.8in tall, above the 6.3in
   cap; the figure is pushed whole to folio 148 and folio 147 ends with
   white space after the lead-in paragraph.
   Severity: should.
   Fix: keep inline but say `width=half-measure` in the brief (illustrator
   draws a narrower page), or add `place=plate`.

7. Quote: "Chapter 10 describes the generated front matter", "Chapter 12
   explains why", "(Chapter 12 shows the arithmetic)"
   Rule: cross-references use `Chapter N, *Title*`.
   Severity: should.
   Fix: add `, *Front matter, the index, and the table of authorities*`
   and `, *The print pack*` on first mention (Chapter 12's title:
   check against the file).

8. Quote: Tables 9.5 and 9.6 (columns Token/Light/Dark and File
   ends with/Label)
   Rule: sentences in the Meaning column. These tables have no Meaning
   column (values and labels only).
   Severity: should (data tables; acceptable if the editor agrees).
   Fix: none, or add a Meaning column to 9.5.

9. Quote: Fig 9.3 art comment, "grayscale, 0.5pt box" and "a chapter that
   opens with a plate"
   Rule: judge directive only. Directive is complete (archetype
   screenshot, kind `.photo`, full-measure, 178 words with image line,
   under 190, fig-alt differs from caption, referred to earlier by
   `@fig:`). One check: "Chapter 2" in the brief names the Alice chapter
   shown; fine. Cloth green in grayscale will read as mid gray, which is
   consistent with the single-ink interior.
   Severity: none. No fix.

## Passed

- Fences: 2, both tagged `text`; no line over 64 columns; no trailing
  whitespace; no non-ASCII; no dashes in prose.
- Figures: all three have the image line, one blank line, then the `art:`
  comment; paths `09-NN-slug.png`; `#fig:` ids; kind classes; fig-alt
  differs from caption; captions sentence case without period; each
  referred to by `@fig:` before it appears. Fig 9.2 matrix is 6 rows
  (under 14).
- Tables 9.1 to 9.7: header row, proportioned separators, `Table: Table
  9.N.` caption after, no period.
- Box forms: In-this-chapter list matches the 9 A-heads exactly; 7 tips
  and warnings (limit 8); one sidebar, 140 words; no paragraph near 190.
- Headings: sentence case, no digits, never two in a row.
- PDF: no heading at a page foot; no table wider than the measure; no
  code line hooked; blockquote box intact; plate lines n/a.
- Index comment present and last.
