# Typesetter report: Chapter 11, The art department

Status: no markup failures from the verifier; 4 blocks-level guide findings
(footnote labels), 3 should findings. `press check` exits 1, but only on
other files (see below). `press pdf` completed (exit 0); no placeholder
PNGs were needed or created (every figure and plate file existed when I
built).

## press check

Nothing names `book/chapters/11-the-art-department.md`. It reports 7
findings, all in other files: chapter 05 (3), chapter 06 (1), chapter 12
(3), which are watchlist "inspect/rewrite" terms. Not this desk's.

## Confirmed clean

- Every fence is tagged `text` (17 fences); no untagged or language-tagged
  fence. No code line over 64 columns (checked with fence-aware script,
  including the lines inside Example 11.4); no trailing whitespace.
- Figures: three, each with the `art:` comment AFTER the image line and ONE
  blank line between; plate (the-engravers-bench) untouched, same layout.
  Paths `11-NN-slug.png`, `#fig:` ids, `.diagram`, `width=full-measure`,
  `fig-alt` differs from caption, sentence-case captions without a period.
  Each `@fig:` reference precedes its figure (lines 39, 276, 288). Brief
  plus image line are 161, 146, 172 words (limit 190). No wrap placements.
- Example 11.4 (four-backtick outer fence, line 369): renders in the PDF as
  one block; the inner fences and headings print literally. Caption sits
  directly above it.
- Headings sentence case, no digits, never two in a row; the `## Cover`
  etc. lines are inside Example 11.4, not headings. Boxes: in-this-chapter
  form correct and matches the A-heads; 4 tips, 3 warnings (7, limit 8),
  one sidebar. Tables 11.1 to 11.8 have header rows, proportioned
  separators, captions after. Index comment is last. No non-ASCII, dashes,
  or paragraphs near 190 words.

## Findings

1. Quote: `[^penguin]` (line 126 and 188)
   Rule: markup.md, footnote labels begin with the chapter number.
   Severity: blocks (guide "labels are unique across the whole book").
   Fix: rename to `[^11-penguin]`. Unique today, but unprefixed.
2. Quote: `[^ink]` (lines 222, 240). Same rule and severity.
   Fix: `[^11-ink]`.
3. Quote: `[^upscayl]` (lines 333, 359). Same rule and severity.
   Fix: `[^11-upscayl]`.
4. Quote: `[^imagen]` (lines 515, 523). Same rule and severity.
   Fix: `[^11-imagen]`.
   (`press check` does not enforce this; the guide does.)
5. Quote: "**Example 11.1. The Alice example's config/aesthetic.yaml**" then
   `plates:` as the last line on PDF page 181 (book p. 181), the rest of the
   fence on p. 182.
   Rule: example caption not separated from its fence.
   Severity: should.
   Fix: the fence is about 28 lines; no markup change can keep it together
   (no raw LaTeX). Shorten the example to an excerpt ending in `...` so it
   fits, or move the paragraph of orientation after it so the page break
   falls earlier. Pagination will move again when the art is real; recheck.
6. Quote: "press art commission [targets] [--model openai|gemini]..." at the
   foot of book p. 194, with "[--count N] [--photo PATH]" on p. 195.
   Rule: a short synopsis fence split across pages.
   Severity: should.
   Fix: none in markup; will likely move. Optionally drop the trailing
   `...` after `]` (it reads as repetition of the option group and is
   unneeded).
7. Quote (figure brief, Example art 11.1): "In order: dog-eared file ...;
   rounded box ...; ... folder ...; rounded box "press art accept"; folder
   "assets/"; rounded box "press art enhance"; ... return arrow".
   Rule: figure rules, left-to-right flowchart must fit full measure.
   Severity: should.
   Fix: nine nodes in one row at 6.3in is tight (lettering shrinks). Ask
   the illustrator for two rows (manuscript to commissions on top, accept
   to build underneath) with the return arrow between them, or cut node
   text.

Figure briefs 11.2 and 11.3 are within the 1740 px cap (no matrix or tree).
No terminal panels in this chapter.

Note: pages after book p. 186 could not be viewed as images because another
desk rewrote `dist/publishing-with-press.pdf` while I was rendering; I read
those pages from `pdftotext -layout` output of my own build instead, and
found no heading at a page foot, no table wider than the measure, no hooked
code line, and no blockquote box crossing a page.
