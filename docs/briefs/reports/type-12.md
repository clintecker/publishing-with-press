# Typesetter report: Chapter 12, The print pack

Status: builds; 3 blocks, 5 should. `press check` exit 1 (all three
blocks are this file's, from the jargon lint; every other finding names
another file). `press pdf` passed (exit 0) once placeholder PNGs stood in
for missing figures (see Notes).

## Blocks

1. Quote: `### The honest placeholder` (line 266) and "The source calls it
   "an honest placeholder"." (line 268, col 171).
   Rule: `press check` jargon lint, 'honest' [rhetorical reassurance];
   fails the check.
   Fix: heading "The placeholder box"; in the sentence, quote the source
   as "a placeholder" or drop the quotation ("The source calls it a
   placeholder."). Also drop "honest" from the Figure 12.3 and
   qualification text if it appears in prose elsewhere in the chapter.
2. Quote: "That note is harmless, and you can ignore it." (line 453).
   Rule: `press check` jargon lint, 'harmless' [risk verdict]; fails the
   check.
   Fix: state the fact: "That note changes nothing in the file, and you
   can ignore it."
3. Quote: `[^allowance]`, `[^ingram]`, `[^isbn]`, `[^kdpdate]`,
   `[^adapter]` (lines 134, 162, 246, 420, 501 and definitions 503-507).
   Rule: markup.md "Footnote labels ... every label begins with the
   chapter number"; unprefixed labels collide across the merged book.
   Fix: rename to `[^12-allowance]`, `[^12-ingram]`, `[^12-isbn]`,
   `[^12-kdpdate]`, `[^12-adapter]`, at both reference and definition.

## Should

1. Quote: line 323, `fonts, no transparency, images under 600 PPI,
   front art present,` (64 columns, in Example 12.5).
   Rule: code lines at most 64 columns, nothing may wrap. In the PDF this
   line wrapped with a hook (page 221, "present," on its own line).
   Fix: re-break the example to at most 60 columns (line 379 is 63;
   shorten to 60 as well).
2. Quote: Figure 12.1 image line (65 words) plus its `art:` comment (161
   words) = 226 words (line 113 and 115).
   Rule: markup.md "the comment and the image line ... stay under 190
   words". The checker did not refuse it, but the guide's literal count
   fails.
   Fix: trim the comment to about 110 words (see Figure 12.1 below); move
   the callout detail to the art report.
3. Quote: Figure 12.1 brief, "drawn to proportion ... a narrow 20% gray
   "spine" strip (0.5in)" with labels placed "On the spine".
   Rule: figure rules, legible labels at 1362 px.
   Fix: see Figure 12.1 below.
4. Quote: Example 12.7 caption (line 471), `**Example 12.7. Print
   ordering for the Alice paperback**`.
   Rule: an example caption must not be separated from its fence. In the
   placeholder build the caption stands at the foot of page 226 with the
   fence on page 227.
   Fix: depends on real figure heights; recheck after the real PNGs
   land. If it persists, move the introductory sentence so the caption
   falls earlier, or shorten the fence.
5. Quote: Figure 12.2 art comment cells, e.g. "26 bands: 24-84 pages
   0.25in, 85-140 0.5in, +0.0625 per band, 779-800 2.0625in" and the KDP
   caliper cell (about 90 characters).
   Rule: matrix cells must stay legible in small monospace.
   Fix: add "wrap long cells to two or three lines inside the cell" and
   "column widths about 20, 55, 25 percent".

## Figure 12.1 verdict (fits, with changes)

Geometry fits: 12.75 by 9.25 is 1.38:1, so at full measure (1362 px wide,
about 107 px per inch) the drawing is about 990 px tall, well under the
1740 px cap, and a dimensioned drawing needs another 200 to 250 px of
margin for the dimension lines, so about 1250 px tall in all. No plate or
wrap placement is used; `full-measure` and `.diagram` are correct.

Labels are the risk. At 107 px per inch the spine is 53 px wide and the
bleed band 13 px, so "spine text if spine >= 0.25in", the long spine
formula, and "bleed 0.125in" cannot sit inside their shapes. The brief
should say: keep shapes to scale, but put every spine and bleed label
outside the rectangle on a leader line (spine formula in a staggered second
row above the top dimension line; "spine text" below the page); minimum
label height 24 px (about 9 pt at print scale); the barcode box (about
132 by 96 px) may carry its own label inside. The brief also lists
about 14 labels; allow the illustrator to drop "safety" repetition by
labelling only one safety line.

## Figures 12.2 and 12.3

Figure 12.2 (matrix, 5 rows plus header) is under the 14-row ceiling;
see should 5. Figure 12.3 (pipeline, two rows of four boxes with file
icons) fits; no wrap placement; reading order is explicit. All three
figures: path form, `#fig:slug`, `.diagram`, `full-measure`, fig-alt
differs from caption, caption in sentence case without a period, and each
is referred to by `@fig:` before it appears (lines 111, 128, 292).

## Passed

In-this-chapter box matches the 11 A-heads; three tips, two warnings, one
sidebar (156 words) in the classed form; seven example captions each over
a `text` fence, three short fragments uncaptioned; all 10 fences tagged
`text`; no trailing whitespace; ASCII only; ten tables with header,
proportioned separator, and caption after the table; every table and
example referred to by number before it appears; headings sentence case,
none doubled, none numbered; index comment last with 25 terms; no
paragraph near 190 words; no heading stranded at a page foot (the "12.9.2
The eleven points" heading has two lines under it on page 222).

## Notes

- Other files: `press check` also lists jargon findings in
  *05-figures-and-plates.md* (lines 75, 128, 260) and
  *06-checking-the-manuscript.md* (line 256); not this chapter's.
  `press pdf` printed duplicate-note warnings for `hypcap` and `libertine`
  in *09-the-house-design.md* (not mine).
- The first `press pdf` failed on missing *02-01-tools-in-the-build.png*;
  all 30 referenced PNGs were missing at build time (the 12-0N files had
  vanished between two commands), so I wrote 1362 by 800 white
  placeholders at each, built, and removed every one that was still my
  placeholder. Page flow in the PDF check used 800 px figures, not the
  real drawings.
