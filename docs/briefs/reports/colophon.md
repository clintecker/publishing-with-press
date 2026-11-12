# Colophon report: "the colophon is a blank page in the pdf"

Desk: production editor. Builds examined: `build/docker6/dist/` (current,
after the STE80 pass), `build/docker5/dist/` (fifth build, before STE80),
and the stray `dist/publishing-with-press.pdf` (12 Nov 10:07, 380 pp).
Renders (72 dpi) are in the session scratchpad under `colophon/`.
No file under `book/` or `config/` was changed.

## What the author is seeing

Neither colophon is blank. The only page that names the colophon and is
otherwise blank is a **one-line overflow page of the table of contents**.
The contents run one line longer than a page holds, so the last entry,
`Colophon .... 372`, wraps alone onto a page of its own: running head
("Publishing with Press / Contents"), that single line, folio, and nothing
else. A reader flipping the front matter sees a bare page whose only word
is "Colophon", which reads as "the colophon is blank".

| PDF | TOC overflow page (the "blank colophon") | Copyright page (press "colophon") | Back colophon (cuttlefish) |
|---|---|---|---|
| reading `publishing-with-press.pdf` (381 pp, cover = p1) | **p7** (folio vii), only "Colophon 372" | p3, full | p380 (plate + 2 paras), p381 (3 paras) |
| interior `publishing-with-press-interior.pdf` (381 pp) | **p6** (folio vi), only "Colophon 372" | p2, full | p380, p381 |
| docker5 reading (379 pp) | p7, only "Colophon 370" | p3, full | p378, p379 |
| docker5 interior (379 pp) | p6, only "Colophon 370" | p2, full | p378, p379 |
| `dist/` reading (380 pp, 10:07) | p7, only "Colophon 371" | p3, full | p379-380 |

Surroundings (docker6 reading): p6 Contents (Preface through Appendix F,
23 entries, folio vi) -> **p7 overflow** -> p8 List of plates -> p9 List of
Figures. Interior: p5 Contents -> **p6 overflow** -> p7 List of plates ->
p8 genuinely empty verso (openright before the List of Figures; expected
recto-opening blank, no head or folio) -> p9 List of Figures.

Whole-PDF scan for empty or head-and-folio-only pages (text extraction plus
an ink measure of the body area, top and bottom 12% excluded):

- reading: p1 (the cover, image only: expected), p4 (dedication, one short
  line: expected), **p7 (TOC overflow)**. Nothing else.
- interior: p3 (dedication), **p6 (TOC overflow)**, p8 (openright blank
  verso: expected).

## Each colophon, checked by eye

- **Copyright page** (reading p3, interior p2): edition line, rights
  notice, rule, copyright, publisher, place, manufacture line, contact URL,
  italic colophon-note, motto, LGTM logomark. Every key in
  `config/front-matter.yaml` renders; nothing white, clipped, or pushed
  over a break.
- **Back colophon** (reading/interior p380-381): heading "Colophon", the
  cuttlefish plate with caption, two paragraphs on p380, the production
  paragraphs on p381, which then has white space below (a normal chapter
  end). Running head on p381 reads "16 Inside the press", the known
  #287/#288 defect, not a blank.

## Cause

1. The Contents page holds 23 entries. The book has 24 level-1 entries:
   Preface, 16 chapters, Appendices A-E, the generated Appendix F (index),
   and the back colophon. `book/appendices/z-colophon.md:1` is
   `# Colophon {.unnumbered}`, which pandoc writes to the TOC, and it sorts
   last, so it is the line that spills. Contents is chapters-only
   (`toc-depth: 1`, `src/press/data/defaults/pdf.yaml:4`, print.yaml:11);
   the press has no TOC-fitting logic, so a single overflow line gets its
   own page with a running head and folio. verify-print passes it because
   the page has ink.
2. Not the config. `src/press/data/tex/front-matter.tex:48-89` draws the
   copyright page unconditionally (only its individual lines are gated:
   rights-notice 52-58, manufacture 65-68, contact 73-76, colophon-note
   76-79, motto 80-83, logo 84-87). Acknowledgements is a separate page
   gated at `front-matter.tex:108-117` / `src/press/gen_front_matter.py:191`;
   `press config unset acknowledgements` removes only that page and cannot
   empty the colophon. No key's absence leaves the copyright page blank.

## New or pre-existing

Pre-existing. docker5 (built 23:09 on 11 Nov, before the STE80 pass
`54f2f99`) has the identical overflow page with "Colophon 370". STE80 only
moved the page number (370 -> 372).

## Press or book

Primarily a book matter (the colophon's TOC entry is a book heading), with
a press weakness underneath: the press neither fits a one-line TOC
overflow nor flags a page carrying only a running head, folio, and one TOC
line. Worth a press issue: verify-print should treat a front-matter page
with a single TOC entry as a widow page, and the colophon heading should
not need hand marking to stay out of the contents.

## Smallest fix

Book, one token: change `book/appendices/z-colophon.md:1` to

    # Colophon {.unnumbered .unlisted}

so the closing colophon leaves the Contents (pandoc 3.9 honours
`unlisted`; the press's drop-cap filter already treats it like
`unnumbered`, `src/press/data/lua/chapter-dropcap.lua:304`). Contents
returns to 23 lines on one page and the overflow page goes (later
pagination may shift by a page or two with the openright blanks; recheck). A colophon at the end of a book
customarily goes unlisted, so nothing is lost. Rebuild and confirm the
reading PDF p6 is followed directly by the List of plates.

Alternative if the author wants it listed: tighten the TOC so 24 lines fit
(a press design change, so a new major), or shorten nothing and accept the
page. Do not move the colophon into the appendix sequence to fix this.
