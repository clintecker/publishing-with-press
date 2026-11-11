# Continuity report: Chapter 4, *Writing the manuscript*

Desk: continuity editor. Chapter read as it stands after Revision 2 and the
second re-review (`docs/briefs/reports/rereview-04.md`). Cross-checked
against Chapters 1, 2, 3 (final or near-final), the later drafts where they
make promises to or share facts with Chapter 4 (5, 6, 7, 8, 9), the press
source (`src/press/data/defaults/*.yaml`, `src/press/data/tex/book-header.tex`,
`examples/alice-in-wonderland/`), `docs/vocabulary.md`, `docs/markup.md`,
`docs/design.md` section 5, and `docs/production-ledger.md`.

Status: **PASS WITH FIXES.** One blocks, two should, five may. The chapter
obeys the three shared markup rules (every fence `text`, no code line over
64 columns, image then blank line then `art:` comment) without exception,
keeps every promise earlier and later chapters make about it, and its
numbering is clean. The block is in the Figure 4.1 brief, which is not yet
drawn (the PNG is a 5 KB placeholder), so it costs nothing to fix now.

## Findings

### 1. The opening page of a chapter has no running head (blocks)

Quote, l.44: "@fig:page-anatomy shows where the parts of a chapter end up on
a printed page, here the opening page of the first chapter of the Alice
example. The first callouts are (1) the running head, (2) the folio, ..."
Art brief, l.48: "small type at the top outer corner; ... a page number at
the bottom outer corner."

Rule: shared fact (running heads and folio). The house header sets
`\renewcommand*{\chapterpagestyle}{plain.scrheadings}` and gives `\ihead`
and `\ohead` no optional argument, so a chapter's opening page carries no
running head; `\cfoot[\footnotesize\thepage]{...}` puts the folio in the
centre of the foot on every page, opening pages included. Chapter 9 states
both (l.122: "`\cfoot` puts the page number, the *folio*, in the centre of
the foot"; l.124: "The folio appears on plain pages too, so a chapter's
opening page carries its number"). Figure 4.1 as briefed would draw a
running head that the house never sets on that page and a folio in the
wrong place.

Fix (choose one; the second keeps all ten callouts design.md asks for):

- Keep the opening page, drop the running head. l.44: "The callouts are (1)
  the folio, (2) the chapter title, (3) the drop cap, ..." renumbered to
  nine, plus a sentence: "An opening page carries no running head; every
  later page of the chapter does (Chapter 9, *The house design*, describes
  both)." Brief: delete "small type at the top outer corner"; "a centred
  page number at the foot". fig-alt: "nine numbered callouts", drop
  "running head".
- Or draw a page from inside the chapter, not its opening: l.44 "here a
  page from the first chapter of the Alice example", and the brief loses
  the chapter title and drop cap, which then need a second, opening-page
  frame. More art; only if the writer wants the ten callouts.

Either way the brief's folio becomes "a centred page number at the foot".

### 2. The two Alices are merged in the orientation paragraph (should)

Quote, l.18: "The examples come from the Alice example, the sample book that
comes with press, which user `alice` keeps on the workstation `hatter`."

Rule: cast, and the ledger ruling "the book's sample `alice` is the full
novel; captures from press's gallery example (three chapters, 23 pages) are
quoted as such". Chapter 1 l.121 makes "the sample book" the full novel that
`alice` builds on `hatter`; Chapter 4 l.58 correctly says "The Alice example
holds the first three chapters of Carroll's book". l.18 gives the gallery
example the bible's name for the sample book and puts it on `hatter`, so a
reader cannot tell which book a later sentence means. (l.52's
*10-the-lobster-quadrille.md* is a filename illustration and is fine with
either book.)

Fix, l.18: "The examples come from the press's own Alice example, the
three-chapter book in the press's gallery that holds the first three
chapters of Carroll's novel. The book `alice` keeps on the workstation
`hatter` is the whole novel, and this chapter shows the same constructs as
the gallery example sets them."  (Or, shorter: end the sentence at "the
three-chapter sample that comes with press" and drop the `hatter` clause;
l.252 already places the `$` prompt on `hatter` and `printshop`.)

### 3. Editions called by second names and never glossed (should)

Quotes: l.40 "The Markdown edition is the raw manuscript ... They are the
PDF, the EPUB, the HTML edition, the reader site, the plain text, and the
DOCX."; l.221, 225, 233 "the HTML edition"; l.293, 341, 409 "The plain-text
and DOCX editions".

Rule: vocabulary ("the Markdown edition", "the text edition" are forbidden;
use press's names, glossed once per chapter with the format in
parentheses) and the ledger ruling on edition names. Chapters 1 and 3 use
the names (Ch. 1 l.259 to 266; Ch. 3 l.575 to 581).

Fix, l.40: "One edition stands apart from all of this. The Manuscript
edition (the stitched Markdown) is the raw manuscript ... applies to the
rendered editions: the Print edition (PDF), the Circulating edition (EPUB),
the Single-leaf edition (the self-contained HTML), the Chapter edition (the
reader site), the Telegraphic edition (plain text), and the Office edition
(DOCX)." Then l.221, 225, 233 "the Single-leaf edition"; l.293, 341, 409
"The Telegraphic and Office editions". "The PDF", "the EPUB", and "the
reader site" as short references after the gloss are what Chapters 1 to 3
do and may stay.

### 4. "Chapter 6 ... introduces sentinels" (may)

Quote, l.204: "Chapter 6, *Checking the manuscript*, introduces sentinels,
and Chapter 8, *Verifying the artifacts*, proves them in the finished
editions."

Rule: promise accuracy. Sentinels are introduced in Chapter 1 (l.278) and
again in Chapter 3 (l.219); Chapter 4 itself defines the term in this
sentence. Chapter 6 l.380 to 386 does cover them, so the promise is kept;
only the verb is wrong.

Fix: "Chapter 6, *Checking the manuscript*, covers how the checker finds
sentinels in the manuscript, and Chapter 8, ..."

### 5. `top-level-division: chapter` is not in every defaults file (may; route to facts)

Quote, l.50: "Press sets pandoc's `top-level-division: chapter`, so one `#`
at the start of a line starts a new chapter in every rendered edition."

Rule: shared fact with Chapter 7 (the defaults files). Only *pdf.yaml*,
*epub.yaml*, and *print.yaml* set it; *html.yaml*, *chunked.yaml*, and
*portable.yaml* do not. The effect (a `#` is a chapter everywhere) holds;
the stated cause does not.

Fix: "Press sets pandoc's `top-level-division: chapter` for the PDF and
the EPUB, and in every rendered edition one `#` at the start of a line
starts a new chapter."

### 6. "the output", "in source" for the manuscript (may)

Quotes: l.151 "pandoc sets the single ellipsis character in the output";
l.142 "The checker does not refuse the hyphens in source"; l.223 "Pandoc
decides the column widths from the source."

Rule: vocabulary ("output" is not an edition; "the source" is not the
manuscript).

Fix: l.151 "in every rendered edition"; l.142 "in the manuscript"; l.223
"from the table as you type it".

### 7. Figure order differs from design.md section 5 (may; design.md, not the chapter)

The chapter numbers 4.2 scene-break ornaments and 4.3 set pieces, in
reading order; design.md lists them the other way round. Same precedent as
Chapter 2 (dev ruling 4). Fix: update design.md section 5, row 4.

### 8. "initial" for the letter (may; no change required)

l.266, 267, 293 use "initial" for the large letter itself. The vocabulary
forbids "initial" as a name for the chapter opening; here it names the
glyph, which the vocabulary does not cover. Recorded so the next chapters
(7, 9) use it the same way: the *chapter opening* is the treatment, the
*drop cap* is the `drop-cap` style, the *initial* is the letter.

## Promises checked

Earlier and later chapters promise Chapter 4 five things; all are kept:
Ch. 3 l.605 (opens the chapter files), Ch. 7 l.109 (what the chapter-opening
and scene-break features look like on the page), Ch. 7 l.131 (set pieces,
chapter openings, scene breaks from the author's side), Ch. 8 l.466 (the
chapter opening splits the first word: l.312 warning), Ch. 9 l.114 (how a
book chooses its chapter opening: l.260 to 287).

## Conflicts with earlier (and later) chapters found on the way

These are not Chapter 4 faults; Chapter 4 obeys every rule below.

- **Image, blank line, comment.** Chapter 1 l.3 to 4 (frontispiece plate),
  l.43 to 44, l.48 to 49, l.227 to 228, and Chapter 3 l.76 to 77, l.360 to
  361, l.574 to 575 put the `art:` comment on the line directly after the
  image. Per the ledger, pandoc then makes a paragraph, not a figure: no
  caption, no List of Figures entry. Run `tools/space-art-comments.py` on
  01 and 03 (the ledger says their writers were instructed; the drafts
  still have it).
- **Chapter 5 l.59** says the comment "may sit on the next line or after
  one blank line". That is true of press's directive reader but omits that
  pandoc demotes the figure; it contradicts markup.md and the ledger
  correction. For Chapter 5's continuity pass.
- **64 columns.** Chapter 1 l.134 and l.235 are 65 characters inside
  fences.
- **Fence tags.** Chapters 1 and 3 still have untagged fences in the
  working draft (the ledger says `tools/tag-fences.py` tags them at
  commit). design.md 5c still reads "Code fences are untagged", superseded
  by the ledger ruling; update design.md.
- **Running head and folio** (finding 1) is a conflict with Chapter 9, a
  later chapter, and with the house header.
