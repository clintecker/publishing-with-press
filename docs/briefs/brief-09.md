# Chapter brief: Chapter 9, The house design

You are writing one chapter of *Publishing with Press: Building Books from
Plain Text*, a technical manual about the `press` book pipeline (version
3.0.2), written in the idiom of a technical publisher's animal book of about
1999. You write this chapter only. You do not have the press source; you
have a fact file, and every claim you make comes from it.

Read, in this order, before writing a word:

1. This brief.
2. `docs/briefs/facts/facts-09.md`: your facts. Everything technical in
   the chapter comes from here. The last part, "Shared context", holds the
   philosophy, the thirty war stories, and the list of contradictions you
   must not assert.
3. `docs/prose-contract.md`: how every sentence is built. The one-sighting
   tells are defects.
4. `docs/vocabulary.md`: the one word for each thing.
5. `docs/style-guide.md` sections 2, 3, 4, and 9: chapter anatomy, voice,
   code typography, and a calibration page.
6. `docs/markup.md`: exactly what to type for an "In this chapter" box, a
   tip, a warning, a sidebar, an example, a table, a figure, a plate, a
   footnote, a cross-reference, and the index comment.

## The chapter

- File: `book/chapters/09-the-house-design.md`. It exists as a stub; replace its
  body, keep the first line (`# The house design`) exactly.
- Target length: 5,000 words of prose, plus examples, tables, and
  captions. Under 190 words per paragraph (press refuses more). Sentences
  16 to 22 words on average, never over 30.
- A-heads (the `##` headings), in this order, sentence case:
  1. The page in numbers
  2. Type
  3. Running heads and folios
  4. Six profiles
  5. The reader site
  6. The landing page
  7. The aesthetic file
  8. Extra CSS and the reader sheet
  9. Why a design change is a new major
  You may add B-heads (`###`) under them. Never two headings in a row
  without prose between them.
- Opening: the "In this chapter" box listing the A-heads, then two to five
  sentences of orientation with no heading above them.
- Closing: end on the last technical point or a one-sentence forward
  pointer to the next chapter. No summary, no recap, no pep.
- The running sample is the press's own Alice example: a book with slug
  `alice`, user `alice` on workstation `hatter`, CI host `printshop`,
  repository owner `wonderland-press`. Hang every example on it. Where the
  fact file quotes real output captured from a scaffolded book called
  `demo`, change the slug to `alice` and keep every other character.

## Figures (write the directive; do not draw)

Each figure below is referenced in prose before it appears, placed with the
image line and the `art:` directive from `docs/markup.md`, captioned in
sentence case with no period. The `art:` directive is the illustrator's
brief: name the archetype from the style guide (section 5.2), list every
box, label, and arrow in reading order, and say what the reader should see
first. An illustrator who has not read your chapter will draw from it.

- **Figure 9.1** `@fig:page-geometry`, file `assets/woodcuts/09-01-page-geometry.png`, archetype *page-anatomy*: a 6 by 9 page drawn to scale with dimension lines for trim, text block width and height, inner and outer margins, head and foot, the figure cap, each with its value from the fact file.
- **Figure 9.2** `@fig:profiles-compared`, file `assets/woodcuts/09-02-profiles-compared.png`, archetype *matrix*: rows: the six profiles; columns: trim, text width, figure cap, body size, intended use; values from the fact file; leave a cell blank rather than invent.
- **Figure 9.3** `@fig:reader-site`, file `assets/woodcuts/09-03-reader-site.png`, archetype *screenshot*: a screenshot of the reader site chapter page (the illustrator captures it from a real build; describe what should be visible: the sheet, the chapter heading, a figure, the chapter navigation).

## Plates

This chapter has no plate.

## Tables and examples

Number them by hand in the chapter's sequence: `Table 9.1`, `Example
9.1`. Every table is two or three columns with a header row and sentences
in its Meaning column. Every example over six lines, and every one you
refer to again, gets a number and a caption. Sessions use the `$` prompt
and elide output with `...`.

## Sidebars and admonitions

Suggested sidebar material: design rationale: design is part of the contract (CLAUDE.md), with the v3.0.0 design major as the example.

One sidebar of 150 to 250 words, from the war stories in your fact file's
shared context (pick one that belongs to this chapter's subject; the
chapter's row in `docs/design.md` may name it). Three to eight tips and
warnings, one to four sentences each, imperative.

## Footnotes

Two to six, for asides and history.

## Index

End the file with one HTML comment listing index candidates for this
chapter, 10 to 25 terms, semicolon separated, in the form the reader would
look up (`metadata.yaml`; `sentinel`; `drop cap`; `press check`):
`<!-- index: term; term; ... -->`. It is removed before the final build.

## What you must not do

- State anything the fact file marks as a contradiction, a bug, or
  undocumented (its "Shared context" section 20). Where the docs and code
  disagree, follow the code or stay silent.
- Invent a timing, a version number, a platform, a URL, a person, or a
  quotation. "At the time of this writing" introduces any version claim.
- Use em or en dashes, curly quotes, semicolons in prose, or any character
  outside ASCII and accented Latin (no ©, §, °, non-breaking space).
- Write a title-case heading, a manual heading number, trailing whitespace,
  or a paragraph of 190 words or more.
- Write about the document ("in this section we will"), close a paragraph
  on a maxim, stage a contrast ("not X but Y"), or use any word on the
  prose contract's lists. `press check` enforces most of these; the
  reviewer enforces the rest.
- Put bold or Markdown syntax inside a code block to mark what the user
  types. Prompt lines (`$ `) are the only marker.
- Touch any other file.

## Done means

1. `~/code/.pwp-venv/bin/press check` passes from the repository root with
   no error naming your file (run it from `/Users/clint/code/publishing-with-press`).
2. `python3 tools/ste_check.py book/chapters/09-the-house-design.md` reports no
   finding you cannot defend in your report (quoted output and tables will
   trip the sentence counter; those are fine; a semicolon or a passive
   construction in prose is not).
3. `~/code/.pwp-venv/bin/press wordcount` shows your file within 15 percent
   of target.
4. You have reread the chapter once as the reader, cut every sentence that
   adds nothing, and checked each numbered figure, table, and example is
   referenced before it appears.
5. Do not commit. Other writers work in this repository at the same time
   on other files; the managing editor commits each chapter. If `press
   check` fails naming another writer's file, that is not yours: rerun
   once, then report it in one line and proceed.
6. Write your report to `docs/briefs/reports/report-09.md`: the word
   count, the figure list with one line each on what the directive asks
   for, any fact you needed and could not find (you left it out; say so),
   any place the fact file contradicted itself, and the checker's residual
   findings with your defence. Return only: status (DONE, DONE_WITH_CONCERNS,
   NEEDS_CONTEXT, or BLOCKED), the word count, and concerns in at most
   five lines.

You never dispatch subagents. Review comes from the controller after your
report.
