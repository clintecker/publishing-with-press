# Typesetter report: Preface (book/chapters/00-preface.md)

Builds: `press check` FAILED on other files only; `press pdf` PASSED
(exit 0, dist/publishing-with-press.pdf, 389 s pandoc). No placeholder
PNGs were needed or created (the one missing figure at the first
attempt, 14-03-resolving-v3.png, appeared from another desk before my
retry).

## Findings

1. Quote: `## Who should read this book` (and the five other `##`
   headings: "Organization of this book", "Conventions used in this
   book", "Using code examples", "How to contact us", "Acknowledgments").
   Rule: markup guide, the Preface's A-heads should not carry numbers;
   the brief says to report it. Observed: the PDF numbers them 0.1
   through 0.6 (heading "0.1 Who should read this book", and so on, in
   the body; the TOC lists only the Preface). Severity: should.
   Fix: append ` {-}` to each of the six `##` headings, for example
   `## Who should read this book {-}`.

2. Quote: the "Organization of this book" list (`**Chapter 1,
   *Introduction***\` then a line). Rule: bold-and-italic form. Observed:
   renders correctly (bold lead, italic title, description on the next
   line, hanging layout); entries have no gap between them, so the page
   is dense but legible. Severity: none (observation only).

3. Quote: the "Conventions" definition list. Observed: sets cleanly;
   terms run in with hanging indent, no overflow, no wrapping with a
   hook, "[ ], |, and ..." and the constant width italic term both
   render. Severity: none.

## Checked and clean

- Heading `# Preface {.unnumbered}`; no "In this chapter" box; no
  figures, tables, fences, tips, warnings, or sidebars in the file (so
  no example captions, code lines, or `text` fences to check).
- No heading at a page foot, no blockquote box, nothing wider than the
  measure in the Preface pages (PDF pages 11 to 18).
- No trailing whitespace; no paragraph near 190 words (longest about
  95); no dashes or curly quotes typed.
- Footnotes: none in the file, so the `0-` label rule has no cases.
- Index comment present and last (line 169).

## Other files (not mine)

`press check` fails with: plate never referenced by the manuscript:
assets/woodcuts/12-01-cover-wrap-anatomy.png, 14-02-resolving-v3.png,
14-03-release-state-machine.png. The PDF build also logged one
"libpng error: Read Error" for an image outside this chapter.

## Counts

blocks 0; should 1; observations 2.
