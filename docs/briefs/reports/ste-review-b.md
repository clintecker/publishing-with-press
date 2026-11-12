# STE80 review: Appendix B, Configuration reference

File: `book/appendices/b-configuration-reference.md`, reviewed against
`git diff HEAD` and the editor's report `docs/briefs/reports/ste-b.md`.

Status: **REVISE**. Blocks 1, should 0.

The diff holds the twelve edits the report lists and nothing else. No code
span, path, flag, key, message, identifier, number, or heading changed.
The three sentinels do not occur in this file, before or after. No
paragraph is over 190 words, and no blockquote was touched. `press check`
exits 0. `tools/ste-ratchet.py` puts the file at 21 (baseline 23). The 21
are the paragraph-length leads the editor declined, and the key-line
artifact the report describes accounts for them.

## Findings

1. **Line 202, the opening of *config/front-matter.yaml* (edit 6).**
   Old: "The presence of this file asks the press to generate the PDF's
   front matter: the title page, the copyright page, and the dedication,
   epigraph, and acknowledgments pages. ... An absent key does not print.
   The scaffold writes the file with every key commented out. ... A file
   at *tex/title-page.tex* overrides all of it. ..."
   New: "When this file exists, the press generates the PDF's front
   matter: ..." The paragraph now ends at "An absent key does not print."
   "A file at *tex/title-page.tex* overrides all of it" moves to the next
   paragraph.
   What went wrong: two changes act together and make the claim stronger.
   "Asks the press to generate" was a request that something else can
   overrule. "Generates" says it always happens. The one exception was in
   the same paragraph, and now it is after a paragraph break, behind two
   sentences about the scaffold. Table 10.5 lists *tex/title-page.tex*
   first: when that file exists, "the press generates no front matter at
   all", even with *config/front-matter.yaml* present. Chapter 10, line
   211, says the press then "reads no key from
   *config/front-matter.yaml*". As written, the new first sentence is
   false for a book that has both files. This is the "may became does"
   case with the condition moved after the command. The cover case
   (Table 10.5, row 3) is not a problem. Neither version says "only", and
   "When this file exists" gives a sufficient condition, not an exclusive
   one, so a cover-only book still agrees with the text. The editor's
   alternative ("it asks the press to generate", 26 words) fixes the verb
   but is over the length limit. Moving the override back fixes it at
   full strength with no new words.
   Severity: blocks.
   Corrected: keep the new first sentence and the split, and move the
   override sentence up so that it comes straight after the claim it
   limits:
   > When this file exists, the press generates the PDF's front matter:
   > the title page, the copyright page, and the dedication, epigraph, and
   > acknowledgments pages. A file at *tex/title-page.tex* overrides all
   > of it. The press calls the copyright page the colophon. The identity
   > facts come from *config/metadata.yaml*. An absent key does not print.
   >
   > The scaffold writes the file with every key commented out. If the
   > file is missing, `press config set` creates it. Chapter 10, *Front
   > matter, the index, and the table of authorities*, explains every key.

## The hard cases, checked

- **`print.provider`, line 111 (edit 3).** "set this key to the shop that
  will print the book, such as `lulu` for a Lulu paperback" (23 words).
  The instruction still gives the exact value (`lulu`) for the exact case
  (a Lulu paperback). Facts-B discrepancy 13 is the reason the sentence
  exists ("the doc never says so for paperbacks"), and the merged sentence
  still says it. The general rule already tells the reader to set the key,
  so the example keeps the force of a command. The paperback qualifier is
  the original's, and so is the claim that the default `house` is not
  Lulu. No finding.
- **`date`, line 46 (edit 2).** "The press reads this free text for the
  first four-digit year that begins with 1 or 2." The type note "free
  text" survives as "this free text". "Reads ... for" says what the next
  sentence ("It uses that year ...") needs. The 1/2 rule and "first" are
  exact (facts-B 3.3: the first `1xxx`/`2xxx` year). No finding.
- **`seller-of-record`, line 180 (edit 5).** "which the press names on
  the landing page". The press generates the landing page and its
  `print-order` aside, and Chapter 12, line 490, says the aside names the
  seller. The entry still says that the press's model has the provider as
  seller and that you must confirm the legal seller (facts-B discrepancy
  12). No finding.
- **`web-palette-dark`, line 323 (edit 9).** Both new sentences use the
  wording of the `web-palette` entry two lines above, and "Press" opens a
  sentence, as `docs/vocabulary.md` allows. "After its dark-mode media
  query" is unchanged and agrees with `substitute_web()` (facts-B: it
  rewrites declarations after the `prefers-color-scheme: dark` split).
  No finding.
- **`styles.<id>.source`, line 431 (edit 12).** "which you give with
  `--from`". `--from` is a command-line flag that the author passes, so
  the actor is correct. The refusal message is verbatim. No finding.
- **Edits 1, 4, 7, 10, and 11.** Each split or reorder keeps every
  qualifier: "unless the title already ends in ...", "The exception is a
  Lulu hardcover", "at the time of this writing", "until you update the
  claim". No finding.

## A note on the editor's report

Edit 8 says that the craft-laws text "opens a new paragraph with 'Print
interiors are single ink ...'". In the file, the new paragraph opens with
"Certain craft laws hold whatever the aesthetic says:" and "Print
interiors ..." is its second sentence. That is the right split (from
which keys the build reads, to the craft laws). Only the report's
description is wrong. The text needs no change.
