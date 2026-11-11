# Continuity report: Chapter 1, *Introduction*

Desk: continuity editor. Chapter read: `book/chapters/01-introduction.md`
as it stands after its desks and two re-review rounds (315 lines; line
numbers below are to that text). Cross-checked against Chapter 2 (final),
Chapters 3 and 4 (final revision), the drafts of 5 to 12 where they share a
fact or make a promise, the stubs of 13 to 16 and Appendixes A to E,
`docs/vocabulary.md`, `docs/markup.md`, `docs/design.md` section 5, and
reports continuity-02 and continuity-04. The chapter was not edited.

Status: **PASS WITH FIXES.** No blocks, one should, six mays. Every
cross-reference names the right chapter number and title; every "later in
this chapter" and "earlier" points the right way; numbering is clean; cast
is clean. Every promise other chapters make about Chapter 1 is kept. The
three markup conflicts continuity-04 raised against Chapter 1 (image, blank
line, `art:` comment; fence tags; 64 columns) are all fixed in this text.

## Findings

### 1. The reusable workflow called by a second name (should)

- Quote (l.236): "a short workflow that calls the press's own build
  workflow, so a push is all that CI needs."
- Quote (l.291): "it requires the press's reusable workflow to pin the
  toolchain image"
- Rule: one name per thing (vocabulary: *the reusable workflow*, `build.yml`;
  "the pipeline, the CI config" forbidden). The same file appears under two
  names fifty lines apart, and the reader cannot tell they are one.
  Substance agrees with the shared fact "Who a book's CI calls" (Ch. 3).
- Fix (l.236): "a short workflow that calls the press's reusable workflow,
  *build.yml*, so a push is all that CI needs."

### 2. "in the source" for the manuscript (may)

- Quote (l.283): "that the verifiers must find in the source and in every
  artifact."
- Rule: vocabulary, *the manuscript* ("the source" is not used for the
  files). The phrase is the fact base's, not a quotation in the text.
  Chapters 3 and 6 say "the manuscript".
- Fix: "that the verifiers must find in the manuscript and in every
  artifact."

### 3. "the Libertine fonts" (may; carried from continuity-02, finding 6)

- Quote (l.48): "pandoc, LuaLaTeX, latexmk, the Libertine fonts,[^libertine]
  epubcheck ..."
- Rule: shared fact (house PDF typeface). Chapter 2 l.186: "TeX Live
  includes Libertinus, the typeface of the house PDF." Chapter 1's own
  footnote names Libertinus correctly; only the body word is off, and it
  reads as though the house face were Libertine.
- Fix: "the fonts (Libertinus for the PDF, and the Libertine keyboard
  face),[^libertine]". Still open after both re-reviews.

### 4. Figure 1.2 brackets two layers as "the toolchain" (may)

- Quote (l.52, art brief): "A thin bracket at the right spans the "pandoc"
  and "TeX Live and LuaLaTeX" bands, labeled "the toolchain""; fig-alt
  (l.50): "with the pandoc and TeX bands bracketed as the toolchain."
- Rule: one gist per term. l.48 defines the toolchain as pandoc, LuaLaTeX,
  latexmk, the fonts, epubcheck with Java, and poppler. The figure as
  briefed says the toolchain is two of them.
- Fix: the PNG is a 5 KB placeholder, so this costs nothing. In the brief,
  label the bracket "the toolchain" and add under it, in small italic,
  "with the fonts, epubcheck, and poppler"; in fig-alt, "bracketed as the
  toolchain, which also holds the fonts, epubcheck, and poppler".

### 5. Edition names used before their gloss (may)

- Quote (l.201, Table 1.1): "The PDF, the EPUB, the Single-leaf and Chapter
  editions, the text, and the DOCX all built."
- Rule: vocabulary, edition names glossed once per chapter with the format.
  The gloss comes in Table 1.2 (l.264 to 271), sixty lines later, so here
  the reader meets "Single-leaf" and "Chapter" cold.
- Fix: "The PDF, the EPUB, the Single-leaf edition (the HTML file), the
  Chapter edition (the reader site), the text, and the DOCX all built." Or
  add "which the section "The editions" names" after the row.

### 6. Appendix A gives "every target" (may)

- Quote (l.303): "Appendix A, *Command reference*, gives every target in
  manual-page form"
- Rule: term gist. l.34 defines a target as a command that builds, checks,
  or verifies; Chapter 2 (continuity-02, finding 5) rules that the operator
  commands are not targets. design.md section 5 gives Appendix A "every
  command".
- Fix: "gives every command in manual-page form".

### 7. *alice-sources.md*: "the table of authorities" or "the sources companion" (may; needs a ruling)

- Quote (l.277): "one more file, *alice-sources.md*, the table of
  authorities. It is a companion document published beside the book."
- Against: Chapter 3 l.617 and Chapter 9 l.246 agree with Chapter 1;
  Chapter 10 l.401 defines the file as "the *sources companion*" and keeps
  "table of authorities" for the ledger in *config/authorities.yaml*;
  Chapter 8 l.327 says "the sources companion". Not a fault inside
  Chapter 1, which uses one name, but the book uses two.
- Rule: one name per thing, book-wide.
- Recommended ruling: the *table of authorities* is the ledger; the file is
  the *sources companion*. Then l.277: "one more file, *alice-sources.md*,
  the sources companion, which publishes the book's table of authorities
  beside the book." Chapters 3 and 9 follow at their passes.

## Promises

Outgoing, kept: Ch. 2 (both install routes, l.54; the installed toolchain,
l.124; the toolchain on `hatter`, l.307); Ch. 3 (the scaffold file by file,
l.142); Ch. 6 (every rule and its message, l.36: kept in draft, Ch. 6
l.457); Ch. 9 (compares the six profiles, l.32: Ch. 9 l.135, Figure 9.2);
Ch. 10 (the authorities companion, l.277: Ch. 10 l.399); Ch. 12 (the print
pack in full, l.279). Internal: "later in this chapter" at l.60 (scars:
l.84, l.108, footnote), l.62 (l.289), l.228 and l.250 ("The editions",
l.258 and l.283); "earlier" at l.208 (the sidebar, l.94) and l.251 (the
warning at l.173, same A-head). All point the right way.

Outgoing, open (targets are stubs): Ch. 14 follows the CI build step by
step (l.244) and takes the pin mechanism apart (l.294); Ch. 16 describes
the extension contract (l.118); Appendixes A to E as l.303 describes them;
the Preface lists the typographic conventions (l.305). The Preface entry in
the bible records what Chapter 1 tells the reader about the book's plan.

Incoming, all kept: Ch. 4 l.204 (Chapter 1 introduces sentinels: l.283);
Ch. 8 l.25 (Chapter 1 describes the four laws: l.68 to 108); Ch. 8 l.447
(Example 1.2 shows the summary lines of a full run: l.176 to 192).

## Numbering

Figures 1.1 `01-01-pipeline-overview`, 1.2 `01-02-the-stack`, 1.3
`01-03-ten-minute-tour`: design.md order, no gap, no repeat, slugs match,
each `@fig:` cited before or at its figure. PNGs are placeholders. The
frontispiece plate *the-shop-at-morning.png* is unnumbered and present.
Tables 1.1 and 1.2; Examples 1.1 to 1.3; three short uncaptioned fences
(l.148, 162, 238), none referred to again. Every fence is tagged `text`, no
code line is over 64 columns, and every image line is followed by one blank
line and then its comment.

## Cast

Clean: `alice`, `hatter`, `printshop`, `wonderland-press`; the press's own
Alice example labeled as such at every capture (l.170, 208, 277); real names
only otherwise (Clint Ecker, LGTM Systems, *Mostly Done.*, *Make Ready*,
Tenniel).

## Conflicts in other chapters found on the way

Not Chapter 1 faults; for those chapters' passes.

- **Ch. 10 l.317** (sidebar): "A press book appears in seven editions at
  once." Chapter 1 Table 1.2 and Chapter 3 l.615 list eight. The seven in
  `7 editions match source` (Ch. 1 Table 1.1, Ch. 7 l.403, Ch. 8 l.294) is
  the count that the agreement check compares, not the number of editions.
  Blocks at Chapter 10's pass (contradicted shared fact).
- **Ch. 10 l.233**: "Chapter 5, *Figures and plates*". The title is
  *Figures, plates, and illustrations*. Blocks (wrong cross-reference).
- **Ch. 11 l.255**: "The *target* after `--as` decides where the image
  goes". This redefines *target*, which Chapters 1, 2, and 7 define as a
  `press` command. Should: call it "the destination" or "the `--as`
  value".
