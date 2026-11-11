# Chapter brief: Chapter 10, Front matter, the index, and the table of authorities

You are writing one chapter of *Publishing with Press: Building Books from
Plain Text*, a technical manual about the `press` book pipeline (version
3.0.2), written in the idiom of a technical publisher's animal book of about
1999. You write this chapter only. You do not have the press source; you
have a fact file, and every claim you make comes from it.

Read, in this order, before writing a word:

1. This brief.
2. `docs/briefs/facts/facts-10.md`: your facts. Everything technical in
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

- File: `book/chapters/10-front-matter-index-authorities.md`. It exists as a stub; replace its
  body, keep the first line (`# Front matter, the index, and the table of authorities`) exactly.
- Target length: 4,500 words of prose, plus examples, tables, and
  captions. Under 190 words per paragraph (press refuses more). Sentences
  16 to 22 words on average, never over 30.
- A-heads (the `##` headings), in this order, sentence case:
  1. What press generates and what it does not
  2. The front-matter file, key by key
  3. The title page and the stacked subtitle
  4. The copyright page
  5. Overriding the front matter
  6. The subject index
  7. The table of authorities
  8. The sources companion
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

- **Figure 10.1** `@fig:config-to-front-matter`, file `assets/woodcuts/10-01-config-to-front-matter.png`, archetype *data-flow*: metadata.yaml and front-matter.yaml at the left; arrows to each generated page in order (title page, copyright page, dedication, epigraph, acknowledgements, contents, lists); each arrow labelled with the keys it carries.
- **Figure 10.2** `@fig:index-entry-path`, file `assets/woodcuts/10-02-index-entry-path.png`, archetype *flowchart*: a term in index-terms.yaml; the matcher strips code and images; whole-word match across chapters; zero hits leads to the build failure quoted from the fact file; hits lead to an entry with chapter-number locators in the generated appendix.

## Plates

This chapter has no plate.

## Tables and examples

Number them by hand in the chapter's sequence: `Table 10.1`, `Example
10.1`. Every table is two or three columns with a header row and sentences
in its Meaning column. Every example over six lines, and every one you
refer to again, gets a number and a caption. Sessions use the `$` prompt
and elide output with `...`.

## Sidebars and admonitions

Suggested sidebar material: design rationale: why the index uses chapter labels rather than page numbers.

One sidebar of 120 to 180 words, from the war stories in your fact file's
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
2. `python3 tools/ste_check.py book/chapters/10-front-matter-index-authorities.md` reports no
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
6. Write your report to `docs/briefs/reports/report-10.md`: the word
   count, the figure list with one line each on what the directive asks
   for, any fact you needed and could not find (you left it out; say so),
   any place the fact file contradicted itself, and the checker's residual
   findings with your defence. Return only: status (DONE, DONE_WITH_CONCERNS,
   NEEDS_CONTEXT, or BLOCKED), the word count, and concerns in at most
   five lines.

You never dispatch subagents. Review comes from the controller after your
report.
