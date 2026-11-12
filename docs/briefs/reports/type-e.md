# Typesetter report: Appendix E (Glossary) and Appendix Z (Colophon)

Files: `book/appendices/e-glossary.md`, `book/appendices/z-colophon.md`.

## Builds

- `press check`: fails, but not on these files. Message: "plate never
  referenced by the manuscript: assets/woodcuts/12-01-cover-wrap-anatomy.png"
  (another desk's stray file; not mine).
- `press pdf`: passes once every missing figure PNG exists (other desks'
  figures were absent; I made white 1362x800 placeholders for the 13 missing
  at build time and deleted exactly those). 375 pages. Other desks were
  building concurrently into the same `dist/`; one early run died on a
  placeholder deleted mid-build by another desk.

## Appendix E

Markup against `docs/markup.md`: no findings.
- Heading `# Appendix E: Glossary {.unnumbered}`, hand-lettered; no `##` or
  `###` (so no `{-}` needed); no footnotes (so no `e-` labels needed).
- 145 term/definition pairs (bold term, blank-free `: ` definition), counted
  by grep. No trailing whitespace, no em/en dash, no non-ASCII, no tables,
  fences, figures, or admonitions.
- Setting: each entry runs the term in bold into the definition on the same
  line with a hanging indent; no term is stranded from its definition at a
  page foot. Entries are not separated by blank space, only the hang.
  Glossary runs pdf pp. 366-373 (printed 357-364), ending a little over a
  half page down; the last entry (wrap) is on p. 373. One entry (chapter
  witness/chapter opening area, p. 367-368 and p. 368) splits across a page
  with two lines each side: acceptable.

## Appendix Z

Plate lines: image, blank line, `art:` comment (89 words, under 190): correct.
- The plate renders in the PDF at the colophon opening (p. 374, printed 365)
  with caption "The cuttlefish at its inkwell" centred beneath, and it
  appears in the List of Plates as "16.1 The cuttlefish at its inkwell ...
  365". No footnotes, no headings beyond the title. The colophon is the last
  pages: pp. 374-375, the final page (375, printed 366) holding the
  closing paragraph.

## Findings

1. Quote: running head "16 Inside the press" on every glossary page and on
   the colophon pages. Rule: a running head should name the section the page
   belongs to. Severity: should. Fix: a template/press matter (the head takes
   the last numbered chapter); not fixable in these files, report to the
   build owner.
2. Quote: List of Plates entry "16.1 The cuttlefish at its inkwell". Rule:
   the colophon plate is in an unnumbered appendix, so a chapter-16 number
   is misleading. Severity: should. Fix: same cause as 1 (the counter is the
   last chapter's); press behavior, not a manuscript edit. Other plates in
   the list use the same scheme (e.g. 15.1), so it is house behavior.
3. Quote: colophon text spans two pages (plate and three-quarters of the
   text on 374, remainder, 8 lines, on 375). Severity: should (cosmetic).
   Fix: none required; a shorter plate or paragraph would fit one page but
   the plate is the brief's.

Counts: blocks 0, should 3 (all outside these files' text).
Figure briefs: none in either file (the one plate is untouched).
