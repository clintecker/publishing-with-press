# Report: Chapter 1, Introduction

Status: DONE_WITH_CONCERNS

## Word count

`press wordcount`: 5,353 for `book/chapters/01-introduction.md` (target
5,000, within 15 percent). The count includes the three `art:` directives,
the frontispiece directive, and the tables, because wordcount does not strip
HTML comments. Prose alone is roughly 4,500 words.

## Figures

- Figure 1.1 `@fig:pipeline-overview` (pipeline): two manuscript file icons,
  press check, pandoc + Lua filters, fork into latexmk/LuaLaTeX to
  alice.pdf and pandoc writers to five edition icons, a "stitch" arrow
  straight to alice.md, all converging on a drop-shadowed "verifiers" box,
  then dist/.
- Figure 1.2 `@fig:the-stack` (stack): six bands bottom to top, OS, Python
  3.10 or later, pandoc, TeX Live and LuaLaTeX, press, your book (shadowed),
  with a bracket marking pandoc and TeX as "the toolchain".
- Figure 1.3 `@fig:ten-minute-tour` (filmstrip): three boxed 72-column
  terminal panels: press new alice / cd alice; the captured press check
  output (note lines elided as "..."); ls dist/ with the two-line listing.

Plate: frontispiece lines untouched.

## Facts I needed and could not find (left out or flagged)

- No captured output for `press new` or for `ls dist/`. The `ls dist/`
  listing in Example 1.2 and Figure 1.3 is constructed from the registry
  layout in facts section 3.5 (slug alice, without the authorities
  companion). The managing editor should replace it with a real capture.
- Whether `press all` itself writes `dist/pages/`: README says it does, but
  QUICKSTART runs `press pages` after `ls dist/`. I listed `pages` in the
  listing and kept the QUICKSTART's `press pages` step.
- Contradiction A26 (source zip and git): I moved `git init` and a commit
  before `press all` (as README's quick start does) instead of claiming the
  source zip needs it. The prose says only that the Source edition holds
  files Git tracks.
- `press new` output and what CI does on push were not in the fact file, so
  the tour defers CI to Chapter 14.

## Places the fact file contradicted itself or needed adapting

- The captured `press check` output contains a non-ASCII ellipsis
  (`/…/src/press/...`) and lines over 72 columns. The chapter shows only the
  first line in a session fragment and explains all four lines in Table 1.1;
  the full text (ellipsis as three periods) is in the Figure 1.3 directive.
- The README sentence with "6 x 9" is stale per A1; I quoted it and noted
  six profiles since v2. The 6.3in cap is given as per-profile (A5).
- The design-contract and four-laws quotes contain semicolons and em dashes;
  I quoted only the dash- and semicolon-free parts and paraphrased the rest.
- design.md row asks for the pinned contract "in one paragraph"; the brief
  gives it an A-head. I followed the brief at five paragraphs plus a table.

## Checker residuals and defence

`press check` reports no error naming this file (it fails on paragraph
length in chapters 02 and 03, other writers' files). Note: press counts an
`art:` comment plus its image line, and a whole sidebar, as one paragraph;
I trimmed the directives and the sidebar (170 words) to stay under 190.

`ste_check.py` residuals, all defensible:

- Lines 3-4 (sentence length, semicolon, "landscape"): the frontispiece
  directive, which the brief says to leave exactly as it is.
- Lines 37, 42, 196 (paragraph length, semicolons, long sentences): the
  three `art:` directives; they are illustrator briefs, not prose.
- Lines 25, 83-85, 96, 263 (passives, long sentences): verbatim quotations
  of the README, the third law, CONTRIBUTING.md, and the press repository.
- Lines 67, 69, 71: B-heads that quote the law names verbatim.
- Remaining sentence-length flags of 24-31: the checker merges a sentence
  with the following footnote or quote, or counts list items inside a
  sentence; no prose sentence is over 30 words by my count. Prose average is
  about 16 words per sentence.
- ing-form flags are heading gerunds and words such as "including".
- "verify", "whether", "therefore", "attempt": period-correct per the prose
  contract's 80 percent rule.
