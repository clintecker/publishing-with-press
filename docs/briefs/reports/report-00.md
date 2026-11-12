# Report 00: Preface

Status: DONE_WITH_CONCERNS. Word count 2,401 (`press wordcount`, target
about 2,500, inside 15 percent). No figures, tables, or examples; no
footnotes; no "In this chapter" box.

## Structure

Four untitled opening paragraphs (why a book about press; *Mostly Done.*,
the scars, *Make Ready*; the history and the version described; the book
as a press book). The failing-check example was cut to keep each
paragraph at six sentences or fewer. Then the six A-heads
in the brief's order. In Organization, each entry is a bold "Chapter N,
*Title*" line, then a pandoc hard break (trailing backslash), then a blurb
that starts with a verb. Titles come from the chapter files' own `#` lines
and match design.md section 5. Appendix F is *Index of subjects* (the
generated appendix takes the first free letter, F, after a to e). One
sentence mentions the Colophon.

## Conventions list

Italic; constant width; constant width italic, plus angle brackets in
syntax lines (Appendix A and markup.md both use `<name>`); `$` and `#`
(Ch. 2 uses `sudo` at a `$` prompt and no chapter shows a `#` prompt, so the
entry says so and warns that `#` inside YAML and Makefiles is a comment);
`[ ]`, `|`, `...`, plus the elided-output line from Ch. 1; Tip, Warning, and
Sidebar described in words; "Figure 2.1" numbering for figures, tables,
and examples (figures by press, the other two by hand), plates unnumbered;
the eight edition names. No constant-width-bold entry, per design.md
("no bold-in-code claim"). There is also a paragraph on hand-typed
chapter references as "the weakest kind of guard" (agrees with Ch. 1 l.305) and
"at the time of this writing". The cast paragraph matches the bible's
Fixed cast and the vocabulary ruling on the Alice book versus the
three-chapter example.

## Facts used

History from facts-01 1.2 and the bible's "Press history dates" and
"Earlier books": first commit 2026-07-17, 2.0.0 four days later
(2026-07-21), 3.0.0 2026-11-10 as a design release, 3.0.2 2026-11-11.
The docstring quotation is verbatim. Maintainer, MIT, and both README
quotations are from 1.3. Contact URLs: the repository from
*config/metadata.yaml* plus `/issues`, the docs site, and the book's
`site-url`. The press repository is named as `clintecker/press` with no
URL typed. There is no postal address and no phone.

## Concerns

1. The issue tracker URL is `repository` + `/issues`. metadata.yaml gives
   no issues URL of its own.
2. I added the book's `site-url` to "How to contact us" as the place
   where every edition lives. It states something that holds only after
   step 10 (ship). Cut it if the Pages site will not be live at
   publication.
3. "The press built every edition of it ... It verified each edition"
   (opening) and "the press refused the book each time it broke a rule"
   (Acknowledgments) state what the production plan requires, and they
   come true only once the final build passes.
4. Acknowledgments names no model or agent by name. design.md's model
   seats are a plan, so I left them out. "Clint Ecker ... directed the
   work" rests on the colophon brief's "under direction".
5. "Using code examples" grants permission to reuse the examples, adapted
   from the style guide skeleton, while metadata says "All rights
   reserved". The editor should confirm the author wants that grant.

## ste_check residuals (defended)

- l.5 is 31 words: the title *Mostly Done.* ends in its own period, so the
  counter joins two sentences.
- Organization blurbs of 29 to 30 words: the counter joins the bold title
  line to its blurb across the hard break, and each blurb alone is under 25.
- The edition list in the conventions (35 words) is a list of eight names.
- "is untested" is the predicate adjective from Appendix D's heading.
- The semicolons and -ing forms are in the index comment and in chapter
  titles ("Installing press", "Checking the manuscript").

`press check` draws no finding in the Preface. The last run failed only on
two unreferenced Chapter 14 plates (*assets/woodcuts/14-02-resolving-v3.png*,
*14-03-release-state-machine.png*), which belong to another writer, and an earlier run
failed only on *book/appendices/e-glossary.md:300*. I did not commit.

## Revision after review (facts-00, copy-00, type-00, coordinator rulings)

Word count after revision: 2,440. Every blocks and should finding is applied:

- Facts: the docs-site sentence now says only "built from the press
  repository by its own CI" (U1). "Using code examples" now repeats the
  `rights-notice` and grants nothing more (quote the text, reuse the
  examples in your own books and build scripts, and get the publisher's
  consent for a substantial part). The "documentation" grant and the
  collections sentence are cut (U2, C2, D5). The Chapter 12 blurb ends
  with ordering a copy (C1). The Chapter 1 blurb has no "ten minutes" (D1).
  The Chapter 13 blurb lists where the numbers go: the copyright page,
  the EPUB metadata, the wrap barcode, the ONIX file, and the PCN listing
  (D2). Appendixes number by letter (D3). The 3.0.2 claim in examples
  carries "at the time of this writing" (D4). Contact and
  Acknowledgments both say "the fact base" (D6). The Appendix F blurb
  names the Preface (D7).
- Copy: *edition* is italic and glossed at first use, with "this book's
  repository" (1, 2). The figure sentence is split (3). "refuses your
  build" (4), and the Appendix C blurb says "refuses a build" too. Ch. 7
  "what the press tells pandoc" (5). App. D "which platforms the press
  does not test" (6). "new major version" (7). *the press's own
  three-chapter Alice example* (8) and *Alice book* (9) are italic. The
  edition list is split in two (10). The license sentence is split (11).
  The fact-base actor is named (12). The *Pages site* replaces the Web
  site (13). `press selftest` (14). The may items 19 and 22 are applied,
  the epubcheck joke is cut (21, per the ruling), and 20 and 24 stay as
  they are by ruling.
- Tip and Warning are described as set-off paragraphs that open with the
  word Tip or Warning, with no bold label and no icon (ruling 7).
- Type: every `##` heading carries ` {-}`, so the PDF no longer numbers
  them 0.1 to 0.6.

`press check` passes on the whole book: all four passes are green. The
ste_check residuals are the same kinds defended above: blurb lines joined
to their headings, the ceiling-length list sentences at 30 words, and the
index comment.

## Continuity revision

- The Chapter 14 blurb now has two verb-first sentences. They name the
  composite action, receipts, tags, release builds, the Pages deploy, and
  `press migrate`, following the chapter's `##` lines.
- The Chapter 15 blurb now names the operator commands (`press improve`,
  `press research`, `press aesthetic`) beside the desk and the workflows.
- `press check` passes. The word count is 2,463.
