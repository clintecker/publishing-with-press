# Typesetter report: Chapter 5, Figures, plates, and illustrations

Status: `press check` fails, but only on another file (Chapter 10).
`press pdf` passed (with temporary placeholder PNGs, since deleted).

Counts: blocks 0 (in this file), should 9.

## press check

- Failures name only `book/chapters/10-front-matter-index-authorities.md`
  (lines 99 and 285 "assistant vocabulary"; paragraph 86 has 206 words).
  Not this desk's. Nothing names the Chapter 5 file.

## press pdf

- Passed after 20 missing figure PNGs were created as 1362 by 800
  white placeholders (the 05-01, 05-02, 05-03 figures among them) and
  then deleted. Pandoc duplicate-footnote warnings name Chapter 9
  (`hypcap`, `libertine`), not this file.
- Pages 82 to 96 read: no heading at a page foot, no table wider than
  the measure, no code line wrapped with a hook, the sidebar and tips stay
  on one page, and each example caption sits with its fence (Example 5.5
  moves whole to the next page).

## Findings

1. Quote: ```` ``` ```` (seven fences: lines 48, 65, 87, 118, 170, 225, 302,
   each untagged)
   Rule: every fence tagged `text`; untagged is plain verbatim and cannot
   wrap.
   Severity: should.
   Fix: run `tools/tag-fences.py`, or type `text` after each opening fence.
   All code lines are within 64 columns (longest is 64, line 118), so
   nothing else in the fences needs change. This chapter teaches the markup,
   so it is the one that must obey it.

2. Quote (line 100): "it is the first figure in Chapter 8, so press numbers it
   Figure 8.1"
   Rule: the example's number must agree with where it is shown; this is
   Chapter 5 and the prose names a Chapter 8 the reader has not met.
   Severity: should.
   Fix: say "the first figure in this example's chapter, Chapter 8" or,
   better, make the example chapter 5 and say "Figure 5.1", then match the
   same number in the figure 5.3 brief (below) and in the
   "Figure 8.1" at the close of the section "Numbered figures..." (page 85
   reads "which figure is Figure 8.1"). Nothing contradicts it if the
   chapter is stated as an invented one; at present it reads as a slip.

3. Quote (line 246, art comment of `#fig:where-a-figure-lands`):
   "label "Figure 8.1" on its outgoing arrow ... "caption: Figure 8.1""
   Rule: same as 2; the lettering the illustrator draws must match the
   fix chosen for 2.
   Severity: should.
   Fix: change all "Figure 8.1" in that comment to the number chosen above.

4. Quote (lines 244 and 246): image line plus `art:` comment, 219 words by
   `wc -w`.
   Rule: the checker counts the comment and image line as one paragraph,
   under 190 words.
   Severity: should (press check passed, so its count, which likely skips
   the attribute block, is under 190; the margin is thin).
   Fix: trim the brief to under about 150 words by `wc`, or move extra
   detail to the report file. Figure 5.1 (197) and 5.2 (191) are also near
   the line; trim lightly.

5. Quote (Example 5.4, lines 225-232): the example shows an image line with
   no `art:` comment after it.
   Rule: the art comment follows the image line with one blank line between;
   a reader copying the example gets a plate with no brief.
   Severity: should.
   Fix: put a blank line after the image line, then a one-line comment, e.g.
   `<!-- art: a grinning cat in a tree; wood engraving, single ink -->`,
   before the prose (and tag the fence). The prose line that follows is
   the wrapped paragraph, so keep it after the comment.

6. Quote (Example 5.3, line 171): `![The Mad Tea-Party](...){` newline
   `    place=frontispiece}`
   Rule: attributes on one logical line; a brace block broken across lines
   is legal pandoc but is not the form the markup guide shows.
   Severity: should (also lines 91-95 and 226-227).
   Fix: acceptable only because of the 64-column limit; keep, but say in
   prose that the break is for width. No change required if the author
   accepts.

7. Quote (Example 5.2, line 92): `.map`; (Table 5.1) `.map`, `.figure`,
   `.plate`
   Rule: the guide's kind classes are `.diagram` and `.photo`; this chapter
   documents press's own full class list, which is a different claim.
   Severity: should (informational).
   Fix: add one sentence that the book's own figures use only `.diagram`
   and `.photo`, so a reader does not copy `.map` into this book.

8. Quote (Table 5.5): header "Profile | Meaning", every row "No image prints
   taller than N inches."
   Rule: the Meaning column holds sentences (met); but the cap value is
   the datum and sits only inside the sentence.
   Severity: should (style only).
   Fix: none needed; optionally add a "Cap" column (three columns are
   allowed).

9. Quote (index comment): 25 terms.
   Rule: 10 to 25 flat terms.
   Severity: should (at the ceiling).
   Fix: none required; do not add terms.

## Checked and clean

- "In this chapter" box form, tips (3), warning (2), one sidebar (about 150
  words), no heading, table, or figure inside a sidebar.
- Example captions `**Example 5.N. Title**`, numbered 5.1 to 5.5 in order,
  each directly above its fence, no trailing period.
- Tables 5.1 to 5.6: header row, proportioned separator, `Table: Table 5.N.`
  caption after the table with a blank line, no final period, sentences in
  the Meaning column.
- Figures: `art:` after the image with one blank line (all three), paths
  `assets/woodcuts/05-NN-slug.png`, `#fig:slug`, `.diagram`,
  `width=full-measure`, `fig-alt` differs from caption, captions in
  sentence case with no period, each cited with `@fig:` before it appears,
  no wrap on a diagram. Briefs: Figure 5.1 is a matrix of seven pages
  (two rows, under 14 rows); none is a terminal panel or tall tree.
- Plate lines in the examples show a blank line between image and comment.
- Headings: sentence case, no digits, never adjacent, no typed numbers.
- No trailing whitespace, no non-ASCII, no dashes; footnotes `silly-plates`,
  `hypcap`, `square`, `lulu` unique in this file (the duplicate-note
  warnings are Chapter 9's `hypcap`, which is a collision across files, so
  rename one of the two).
- Index comment present and last.
