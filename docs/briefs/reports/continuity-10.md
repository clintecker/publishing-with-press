# Continuity report: Chapter 10, *Front matter, the index, and the table of authorities*

Desk: continuity editor. Chapter read as it stands after its desks, its
re-review, and the final small revision (424 lines). Cross-checked against
Chapters 1 to 4 (committed), the drafts of 5, 7, 8, 9, 12, 13, 15 that
Chapter 10 cites or that cite it, `docs/vocabulary.md`, and `docs/design.md`
section 5.

Status: **PASS.** No blocks and no should in Chapter 10; two may. One block
raised against Chapter 13 (finding 1), one against Chapter 12 already logged by the Chapter 5 pass (finding 4),
one should against committed Chapter 3 (finding 3).

Both cross-reference titles the bible held open are now right: l.141 cites
Chapter 3, *The shape of a book repository* (the file's heading and design.md
row 3), and l.211 cites Chapter 5, *Figures, plates, and illustrations* (the
file's heading and design.md row 5). The old "seven editions at once" is now
"eight editions at once" (l.301), matching shared fact "The editions". Every
other title the chapter cites (7, 8, 12, 13, 15) matches its file and
design.md. "Table 10.4, later in this chapter" (l.65) is later (l.178); "as
the next section explains" (l.133) is the next section (l.143).

Numbering is clean: Figures 10.1 `10-01-config-to-front-matter` and 10.2
`10-02-index-entry-path`, design.md order, each cited before it appears
(l.121, 259), each image followed by one blank line and its `art:` comment;
Tables 10.1 to 10.7 and Examples 10.1 to 10.7, no gap, no repeat; three
uncaptioned message fences (l.109, 149, 248), none referred to by number.
Every fence is tagged `text`.

Every promise earlier chapters made to Chapter 10 is kept: the generated
subject index (Ch. 4 l.66; Ch. 3 l.392), the copyright line and the
`epigraph.quote`/`epigraph.attribution` keys (Ch. 4 l.132, 187), the index
and the authorities (Ch. 4 l.204; Ch. 3 l.118, 360), *tex/title-page.tex*
(Ch. 3 l.120; Ch. 13 l.296), the generated front matter that replaces the
fallback title (Ch. 9 l.113), *alice-sources.md* (Ch. 1 l.277; Ch. 7 l.369;
Ch. 8 l.357), the registration lines (Ch. 13 l.256), and the ledger the
`authorities-research` workflow fills (Ch. 15 l.236). Chapter 10's own
promises out (3, 5, 7, 8, 12, 13, 15) are kept by their targets.

Terms defined here agree with the bible where the bible already had them
(*artifact* l.386, *verifier* l.410). The cast is clean: `alice`, `hatter`,
"the Alice book" throughout; the only other names are real (Alice Liddell,
John Tenniel, Macmillan and Co.) or the scaffold's placeholder
(`you@example.com`).

## Findings

### 1. Chapter 13's PCN capture contradicts the Alice book's identity (blocks, for Chapter 13)

Quotes (Ch. 13): l.150 "Example 13.5 shows the target in a fresh copy of the
Alice book ... The author and the publisher are both Lewis Carroll, because
the scaffold uses the author as the publisher by default." Example 13.5
l.160 to 164: `Title alice`, `Subtitle A subtitle`, `Publisher name Lewis
Carroll`, `Place of publication Earth`. l.177 "The Alice book shows a
different gap. Its subtitle still reads "A subtitle", and its place of
publication is still "Earth", the scaffold's default." Footnote
`[^13-earth]`.

Against: Ch. 10 Example 10.2 (l.89 to 100) sets `publisher "Wonderland
Press"`, `publisher-place "Oxford"`, `copyright "Copyright 2026 Wonderland
Press"`; l.150 sets the subtitle "A Tale for Children; or, Alice's Adventures
Under Ground"; l.141 sets the title page from the title "Alice's Adventures
in Wonderland". Ch. 3 Examples 3.1 and 3.4 already set that title and unset
the scaffold subtitle.

Rule: shared facts (sample book's identity; sample book's front-matter
values). The chapters follow the order in which you make a book, so by
Chapter 13 the Alice book's publisher is Wonderland Press, its place Oxford,
and "still" (l.177) asserts a state no earlier chapter leaves it in.

Fix (Chapter 13's pass): recapture Example 13.5 on the Alice book as
Chapters 3 and 10 leave it (title "Alice's Adventures in Wonderland",
subtitle as Ch. 10 l.150, publisher Wonderland Press, place Oxford), drop
l.150's "fresh copy" and Lewis-Carroll-as-publisher sentences and l.177's
"still" sentences and the footnote; or keep a fresh-scaffold capture, label
it so in the caption, and say that the Alice book, after Chapter 10, prints
Wonderland Press and Oxford in those fields. The first is better: it shows
the stacked subtitle as the form receives it.

### 2. "Colophon" and "copyright page" for one page (may)

Quote: l.162 "The press calls the page after the title page the *colophon*,
although most readers know it as the copyright page." The chapter then says
"copyright page" throughout (A-head, Table 10.4, l.180 to 188).

Rule: one thing, one name. The chapter glosses the press's word once and
keeps one name after it, so this passes; but Chapter 13 (l.252, 256) says
"colophon" for the same page, and this book has its own Colophon appendix
(*z-colophon.md*), the classical sense. Recorded in the term table.

Fix: none in Chapter 10. For Chapter 13's pass: say "copyright page" for the
page (keep "colophon" only in the `colophon-note` key and the press's
quoted words), so "the Colophon" stays the appendix.

### 3. Chapter 3 calls *alice-sources.md* "the table of authorities" (should, for Chapter 3 errata)

Quotes (Ch. 3): l.617 "*alice-sources.md*, the table of authorities"; Figure
3.3 alt (l.609) "the optional table of authorities"; art comment (l.611)
"table of authorities, only with config/authorities.yaml".

Rule: `docs/vocabulary.md` now rules the bible's open question (shared fact
"Name of *alice-sources.md*"): the table of authorities is the ledger,
*config/authorities.yaml*; the sources companion is the generated file.
Chapter 10 obeys (l.22, 306, 386, 408), as do Ch. 1 l.277, 7 l.369, 8 l.357,
9 l.250 (the download label "Table of authorities", glossed as the
companion), and 15 l.236. Chapter 3 is committed.

Fix: in an errata pass on Chapter 3, "*alice-sources.md*, the sources
companion" at l.617, and "the optional sources companion" in the Figure 3.3
alt and art comment.

### 4. Chapter 12 gives Chapter 5 the wrong title (blocks, for Chapter 12)

Quote (Ch. 12): l.259 "Chapter 5, *Figures and plates*, describes the pass
for the interior."

Rule: cross-references match design.md section 5 and the file. The title is
*Figures, plates, and illustrations*. Chapter 10 had the same fault and has
fixed it.

Fix (Chapter 12's pass): "Chapter 5, *Figures, plates, and illustrations*". Already logged by the Chapter 5 pass (continuity-05, finding A); confirmed here, not a new entry.

### 5. The Alice book's preface already exists (may)

Quote: l.308 "Suppose user `alice` adds a preface with the sentence ..."

Rule: shared facts (`press wordcount`; scaffold): the scaffold writes
*book/chapters/00-preface.md* into every book (42 words on a fresh
scaffold), and Example 10.5 names that same file.

Fix: "Suppose user `alice` writes into her preface the sentence ..." (or
"adds to the preface").

## Bible entries added

30: nine terms (front matter, title page, colophon, subject index, locator,
table of authorities, claim, authority, sources companion), ten shared
facts, ten cross-reference rows, one numbering row; plus confirmations and
line-number updates to existing rows (editions count, the two cited titles,
the companion's name, sample identity, required keys, year, image cap, and
the Ch. 4 and Ch. 1 promises to Chapter 10).
