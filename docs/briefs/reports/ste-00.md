# STE80 editor report: book/chapters/00-preface.md

Mode: Light throughout (the whole file is the Preface). Fixed only sentences
over 30 words, sentences with three ideas, and semicolons (none found).

## Ratchet count

- Baseline (`tools/ste-baseline.json`): 4
- Before: 4
- After: 3

`press check` passes (source, checker self-test, editorial, jargon).

## Edits (9)

| Line | Rule | Old | New |
|---|---|---|---|
| 26 | S1 (three ideas: explains, tours, lists) | Explains what press is, where it came from, and its four laws, then tours a build from `press new` to the finished editions and lists them. | Explains what press is, where it came from, and its four laws. Then tours a build from `press new` to the finished editions and lists them. |
| 29 | S1 (three ideas: installs, runs, shows) | Installs the Python package and the toolchain, runs `press doctor`, and shows how to build inside the toolchain image. | Installs the Python package and the toolchain, then runs `press doctor`. Shows how to build inside the toolchain image. |
| 32 | S1 (three ideas: scaffolds, describes, shows) | Scaffolds a book with `press new`, describes each file and the metadata fields, and shows how chapters and appendixes sort. | Scaffolds a book with `press new` and describes each file and the metadata fields. Shows how chapters and appendixes sort. |
| 59 | S1 (four ideas: builds, works through, covers, ends) | Builds the print interior and the cover wrap, works through providers and spine math, covers the publish checklists, and ends with ordering a copy. | Builds the print interior and the cover wrap, then works through providers and spine math. Covers the publish checklists and ends with ordering a copy. |
| 62 | S2 (33 words, real lead) + S1 | Explains ISBNs, the ISSN and LCCN, ONIX, and the retail flag, and shows where each number goes: the copyright page, the EPUB metadata, the wrap barcode, the ONIX file, and the PCN listing. | Explains ISBNs, the ISSN and LCCN, ONIX, and the retail flag. Shows where each number goes: the copyright page, the EPUB metadata, the wrap barcode, the ONIX file, and the PCN listing. |
| 71 | S1 (three ideas: maps, follows, covers) | Maps the package, follows the data from manuscript to edition, and covers invariants, `press selftest`, and what a contributed scar must earn. | Maps the package and follows the data from manuscript to edition. Covers invariants, `press selftest`, and what a contributed scar must earn. |
| 110 | S1 (three independent clauses, 28 words) | In syntax lines, square brackets enclose an optional item, a vertical bar separates alternatives of which you choose one, and three periods mark an item you may repeat. | In syntax lines, square brackets enclose an optional item. A vertical bar separates alternatives of which you choose one, and three periods mark an item you may repeat. |
| 143 | S1 (three ideas, 30 words) | We checked the information in this book against the fact base, which came from the press's source and its documentation, and the press checked the book against its own rules. | We checked the information in this book against the fact base, which came from the press's source and its documentation. The press checked the book against its own rules. |
| 153 | S1 (three ideas: press built, Pages serves, site carries) + S6 | The book's *Pages site*, which the press built from this manuscript and GitHub Pages serves, carries every edition of the book: | The press built the book's *Pages site* from this manuscript, and GitHub Pages serves it. The site carries every edition of the book: |

## Leads declined

- Line 5 (31 words): a counter artifact. The book title *Mostly Done.* ends in a
  period inside the italics, so the counter does not see the sentence end
  and merges two sentences. The real sentences are 13 and 18 words (the
  quotation counts as one). The title cannot change.
- Line 52 (34 words): a counter artifact. The counter joins the bold
  chapter label (`**Chapter 10, ...***\`) to its description because the
  hard line break is not a sentence end. The description alone is 23 words
  and holds one idea. The label is a chapter title and is not touched.
- Line 82 (31 words): the same label artifact. The description alone is
  24 words with one verb.

## Noted, not acted on (outside Light mode)

- Paragraph at line 5 has seven sentences (the counter sees six because of
  the *Mostly Done.* merge). Light mode does not cover paragraph length, so
  it stands for the Preface's voice. A later Humanize pass could split it
  after "...turned into a guard."

## Passives kept

None. The edits add no passive, and the edit at line 153 removes one hidden
actor (the relative clause now opens with "The press built"). Light mode
leaves the unedited sentences alone.
