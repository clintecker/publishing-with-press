# Chapter brief: Chapter 14, Continuous integration and the release contract

You are writing one chapter of *Publishing with Press: Building Books from
Plain Text*, a technical manual about the `press` book pipeline (version
3.0.2), written in the idiom of a technical publisher's animal book of about
1999. You write this chapter only. You do not have the press source; you
have a fact file, and every claim you make comes from it.

Read, in this order, before writing a word:

1. This brief.
2. `docs/briefs/facts/facts-14.md`: your facts. Everything technical in
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

- File: `book/chapters/14-continuous-integration.md`. It exists as a stub; replace its
  body, keep the first line (`# Continuous integration and the release contract`) exactly.
- Target length: 5,500 words of prose, plus examples, tables, and
  captions. Under 190 words per paragraph (press refuses more). Sentences
  16 to 22 words on average, never over 30.
- A-heads (the `##` headings), in this order, sentence case:
  1. What a book's CI is
  2. The reusable workflow
  3. The composite action
  4. The toolchain image
  5. Receipts
  6. Tags: floating and immutable
  7. The release contract
  8. Release builds
  9. Pages
  10. Moving between majors
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

- **Figure 14.1** `@fig:ci-topology`, file `assets/woodcuts/14-01-ci-topology.png`, archetype *topology*: workstation hatter; repository cylinder at wonderland-press/alice; the CI runner printshop pulling the toolchain image from the registry; arrows labelled git push, uses build.yml@v3, pull image by digest, deploy pages, publish release.
- **Figure 14.2** `@fig:release-state-machine`, file `assets/woodcuts/14-02-release-state-machine.png`, archetype *state-machine*: states from the fact file's release contract: pushed, built, verified, tagged, contract proved, floating tag moved, release published; failure arcs.
- **Figure 14.3** `@fig:resolving-v3`, file `assets/woodcuts/14-03-resolving-v3.png`, archetype *flowchart*: a book pins @v3; the floating tag resolves to the latest v3.x.y; that tag's build.yml pins the action to itself and the image to a digest; the same bytes every time.

## Plates

This chapter has no plate.

## Tables and examples

Number them by hand in the chapter's sequence: `Table 14.1`, `Example
14.1`. Every table is two or three columns with a header row and sentences
in its Meaning column. Every example over six lines, and every one you
refer to again, gets a number and a caption. Sessions use the `$` prompt
and elide output with `...`.

## Sidebars and admonitions

Suggested sidebar material: war story 19 (release automation that rewrote mypy) and 26 (the macOS runner retired mid-release).

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
2. `python3 tools/ste_check.py book/chapters/14-continuous-integration.md` reports no
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
6. Write your report to `docs/briefs/reports/report-14.md`: the word
   count, the figure list with one line each on what the directive asks
   for, any fact you needed and could not find (you left it out; say so),
   any place the fact file contradicted itself, and the checker's residual
   findings with your defence. Return only: status (DONE, DONE_WITH_CONCERNS,
   NEEDS_CONTEXT, or BLOCKED), the word count, and concerns in at most
   five lines.

You never dispatch subagents. Review comes from the controller after your
report.
