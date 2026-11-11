# Typesetter report: Chapter 8, Verifying the artifacts

Status: no blocks findings; 13 should findings.

- `press check`: this chapter passes. The run fails only on
  `book/chapters/02-installing-press.md:322` ("assistant vocabulary") and
  `:324` ("staging: run-up"), which belong to another desk.
- `press pdf`: passed (exit 0) once placeholder PNGs stood in for the 19
  figure files missing at build time (I deleted them afterwards). The
  chapter runs PDF pages 134 to 154. No Overfull box, no heading at a page
  foot, no table over the measure, no blockquote box over a page.

## Should

1. Quote: line 50, `<!-- art: ARCHETYPE matrix. A grid, thin rules ...`
   Rule: the `art:` comment follows its image line (markup guide, Figures).
   Severity: should. The comment sits on the line before the image (line 51),
   so it attaches to nothing and the illustrator never sees the brief.
   Fix: move line 50 to directly after line 51 (blank line between the
   preceding prose and the image).
2. Quote: line 410, `<!-- art: ARCHETYPE data-flow, drawn left to right...`
   Rule and severity as above; the image is line 411. Fix: move it below
   line 411. The brief is 173 words with the image line; keep it under 190.
3. Quote: line 462, `<!-- art: ARCHETYPE terminal. A plain light terminal...`
   Rule and severity as above; the image is line 463. Fix: move it below
   line 463.
4. Quote (line 454): `  [ absent] epubcheck  the retail EPUB gate (softens to a warning locally)`
   Rule: code lines at most 64 columns; a verbatim captured line that
   wraps in a `text` fence is a should. 74 columns; it hooks in the PDF
   (page 144), and the Example 8.4 fence also splits across PDF pages
   143 and 144, leaving the caption and half the report on one page.
   Fix: if the writer keeps the capture verbatim, accept the hook; better,
   shorten the sample to the fields that fit (cut the parenthetical) or
   drop the `[     ok]` rows between the `...` lines so the whole fence
   (about 9 lines) stays together.
5. Quote (lines 198 to 200), `plus the title as witnesses, every rendered page contains ink, no`
   / `edge clipping[, mirrored margins, black ink only | , cover on page 1]`
   Rule: 64-column limit. 65, 66, 69 columns (line 198 is 66 as well:
   `Verified <pdf>: N pages, 6 x 9 trim, embedded fonts, K sentinel(s),`
   hooks on page 142). Severity: should (a writer-composed form, not a
   capture). Fix: rewrap the form at 64 columns with explicit indented
   continuation lines instead of letting the fence hook.
6. Quote (line 171): `print profile: colored ink on pages [...] (a colored cover plate in a`
   (69 columns). Rule: 64-column limit. Fix: rewrap by hand at 64, or
   excerpt shorter.
7. Quote (line 183): `assets/cover.jpg exists but page 1 of the reading PDF renders blank`
   (67). Same rule and fix; hooks in PDF.
8. Quote (line 240): `EPUB carries an empty dc:date (retail validators reject it); the date`
   (69). Same rule and fix.
9. Quote (line 264): `Verified <files> (K sentinel(s), the title, and the manuscript line`
   (67). Same rule and fix; hooks on the page.
10. Quote (line 288): `epubcheck missing from the press toolchain image; the retail-format`
    (67). Same rule and fix.
11. Quote (line 291): `WARNING: epubcheck not installed; EPUB validated structurally only.`
    (67). Same rule; break after "installed;".
12. Quote (line 366): `Verified dist/pages: every local reference resolves (fragments and`
    (66). Same rule and fix.
13. Quote (line 398): `<label> disagrees with the manuscript: it is missing content from N`
    (67). Same rule and fix.

Items 6 to 13 are all lines of 65 to 69 columns inside `text` fences that
hook with a continuation arrow in the PDF; none exceeds 80, so none blocks.

14. Quote: `Table: Table 8.1 ...` area, line 48, "appear in
    @fig:what-each-verifier-inspects. With it, you can see at a glance..."
    Rule: the figure is referred to by `@fig:` before it appears. It is
    (line 48 precedes the image at line 51), so this passes; noted only
    because items 1 to 3 would move the comment, not the reference. No fix.
    (Not counted.)
15. Quote: fence at lines 287 to 294 (Example 8.3, 8 lines) is correctly
    captioned, but the "Example 8.3" caption at 285 is followed by a fence
    that carries two messages and a blank separator; the PDF kept caption
    and fence together. No fix. (Not counted.)

Revised count: 13 should findings (items 1 to 13); items 14 and 15 are
confirmations, not defects.

## Checked and clean

- First line is the chapter title in sentence case, no number; the "In this
  chapter" box is the blockquote-in-Div form and lists the nine A-heads
  exactly as they appear.
- Headings: all sentence case, no leading digit, none two in a row, no
  typed numbers.
- Every fence (21) is tagged `text`; four example captions (8.1 to 8.4)
  sit directly above their fences in the `**Example 8.N. Title**` form
  with no period; no trailing whitespace anywhere in the file; non-ASCII
  characters: none.
- Tables 8.1 to 8.7 have header rows, proportioned separators, and
  `Table: Table 8.N.` captions after the table with no final period.
- Figures 8.1 to 8.3: paths `assets/woodcuts/08-NN-slug.png`, `#fig:slug`,
  `.diagram`, `width=full-measure`, `fig-alt` differs from the caption,
  captions in sentence case without a period, each referred to by
  `@fig:` earlier. The plate (line 19) is untouched: no kind class,
  non-numbered path, `art:` comment on the following line.
- Footnote labels `ci-false`, `fallback`, `timestamp`, `window` are
  unique. The index comment is the last line.
- One tip (line ~450) and no warnings or sidebar: within limits.

## Figure briefs

- 8.1 matrix: 13 rows, under the roughly 14-row ceiling for the 1740 px
  cap; 5 columns; fine. Comment plus image line is 143 words.
- 8.2 data-flow: placement inline, left to right, not a wrap. Seven
  arrows leave `press verify-formats` and nine leave `press pages`;
  dense but the illustrator can lay out with the right column of file
  icons. The comment plus image line is 173 words, close to the 190
  ceiling; do not add detail to it.
- 8.3 terminal panel: 3 lines, longest 58 columns, fits 72. Fine.
