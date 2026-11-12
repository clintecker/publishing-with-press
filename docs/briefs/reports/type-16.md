# Typesetter report: Chapter 16, Inside the press

Status: clean on the markup guide. `press check` PASSED (23 files; checker
self-test 29 fixtures; editorial and jargon checks passed). `press pdf`
PASSED (exit 0; chapter on PDF pages 276 to 292). Counts: blocks 0,
should 4.

Placeholders: `assets/woodcuts/16-01`, `16-02`, `16-03` already existed
(1362 by 800, made by another desk) when I built. I created none and
deleted none.

Construct audit, all passing: "In this chapter" box matches the list of
A-heads; headings sentence case, never adjacent, no typed numbers; 3
examples (16.1 to 16.3), every fence tagged `text`, longest code line 51
columns, no trailing whitespace; 6 tables, each with header, proportioned
separator, and `Table: Table 16.N.` caption after; 3 figures, each with
the `art:` comment after the image line with one blank line between,
paths `assets/woodcuts/16-NN-slug.png`, `#fig:`, `.diagram`,
`width=full-measure`, `fig-alt` differing from caption, referred to by
`@fig:` earlier (lines 48, 58, 281); art comment word counts 173, 187,
164 (all under 190; Figure 16.2 is 3 words from the limit); footnote
labels all `16-` and unique; ASCII only, no dashes; one warning, no
sidebar; index comment present and last.

## Findings

1. Quote: `**Example 16.1. The critical invariants**` (line 184).
   Rule: an example caption must not be separated from its fence (brief,
   step 2). Severity: should. Evidence: in the PDF the caption is the last
   line of page 285 (printed 276) and the fence begins on the next page.
   Fix: layout-dependent, so re-check after the figures are final; if it
   persists, add one sentence of prose before the caption (or move the
   warning at line ~176 after the example) so the caption moves with its
   fence.

2. Quote: `**Example 16.3. The reference extension manifest**` fence
   (lines 317 to 334). Rule: same. Severity: should. Evidence: the fence
   breaks across PDF pages 290 and 291 (ends `- INV-acme-quarto-geometry`
   / continues `invariants:` list). Fix: re-check after figures land; if it
   stays, trim the manifest excerpt with a `...` line to under about 12
   lines.

3. Quote: Table 16.1, column `Modules` (separator
   `|-------------------|------------------------------------|---...`).
   Rule: tables: proportioned separator, nothing wider than the measure.
   Severity: should. Evidence: the Modules column is narrow and breaks
   file names mid-word (`profile_lifecy-cle.py`, `check_the_check-ers.py`,
   `provider_specs.py` stacked), and the table runs 3 pages. Fix: widen the
   Modules dashes (for example 28 / 44 / 38) and shorten long Meaning cells.

4. Quote: Figure 16.2 brief, "`latexmk -lualatex (pdf, print)`", six-box
   fan-out, 12 or so stages. Rule: figure must fit 1362 by 1740 px with 8 pt
   labels. Severity: should. Fix: see verdicts.

## Figure fit verdicts

- Figure 16.1 (module map): FITS. No wrap placement, `full-measure`, six
  bands (about 16 area labels, 2 to 4 module names per box as the brief
  lists) plus a trust column, frame, and three arrows: well under 14 rows
  and 8 pt labels clear at 1362 px wide. Keep to the module names the
  brief lists; do not add the full Build list (11 modules) to band 3.
- Figure 16.2 (end-to-end data flow): FITS ONLY TIGHTLY. About 12 vertical
  stages (inputs, three typed boxes, `build.book_inputs` with two side
  branches, `render_defaults`, pandoc, six-writer fan-out, `dist`, three
  verifiers, pages assembly, CI split) at roughly 140 px each uses nearly
  all of 1740 px. The six fan-out boxes are about 215 px wide, so
  `latexmk -lualatex (pdf, print)` needs three lines at 8 pt. Fix: shorten
  that label to `latexmk (pdf, print)` and fold the two side branches into
  the same row as `render_defaults`, or the illustrator should drop the
  CI tail to one box. Art comment is 187 words, so any added detail must
  go in the report file.
- Figure 16.3 (trust chain, not asked but checked): FITS. Twelve bands is
  within the 14-row limit.

Other: no failure from `press check` or `press pdf` named another file.
The PDF log shows only a harmless hyperref warning (`unreferenced
destination Hfootnote.61`).
