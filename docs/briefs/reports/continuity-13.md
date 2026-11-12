# Continuity report: Chapter 13, *Registrations*

Desk: continuity editor. Chapter read as it stands after its desks and its
re-review, with the re-review's three one-line edits (N1 l.315, N2 l.273,
N3 l.204) in place: 323 lines. Cross-checked against Chapters 3, 6, 7, 8,
10, and 12 (committed), Appendixes A, B, C, and E, the Preface,
`docs/vocabulary.md`, `docs/design.md` section 5, and the press source the
shared facts rest on (*registrations.py*, *gen_front_matter.py*,
*build.py*).

Status: **PASS WITH FIXES.** One block, one should (in Chapters 3 and 6,
not in this chapter), four may. The block is the ISSN on the copyright
page: the chapter and its figure brief put an ISSN line there, and neither
Chapter 10 nor the press prints one.

What holds:

- **Chapter 10's flag is closed (continuity-10, finding 1).** Example 13.5
  is now labeled a fresh scaffold "before the changes of Chapters 3 and
  10, and before you set any registration" (l.165), and l.192 says that
  Chapters 3 and 10 replace the title, subtitle, publisher, and place
  with the Alice book's own (full title, double subtitle, Wonderland
  Press, Oxford). The scaffold values shown (`alice`, "A subtitle",
  publisher = author, "Earth", 2026, en-US) match the shared fact
  "Scaffold metadata values". The omitted `--owner` changes no PCN field.
- **Continuity-10, finding 2 is closed in substance.** The chapter says
  "copyright page" throughout and glosses the press's word once (l.269);
  see finding 3 for the gloss's wording.
- **Chapter 10 agrees on the copyright page otherwise.** One line per
  registration with the labels of Table 10.4 (l.172), `pending` printed
  as `[pending]` (l.33, 273; Ch. 10 l.182), the same block feeding the
  EPUB identifier and the barcode (l.273; Ch. 10 l.182), and the
  hand-authored *tex/title-page.tex* replacing the generated front matter
  (l.317).
- **Chapter 12 agrees on the barcode.** The barcode carries only
  `registrations.isbn.print` as an EAN-13 (l.269, 273; Ch. 12 l.225); the
  check digit "Chapter 12 works through by hand" is Example 12.4 (l.92,
  123; Ch. 12 l.231); the placeholder box reads `[ISBN pending]` (sidebar
  l.150; Ch. 12 l.251).
- **Chapter 8 agrees on the EPUB identifier.** `urn:isbn:` and the number
  (l.271); the verifier checks it in the package file (Ch. 8 Table 8.3
  l.243, message l.257; App. C l.517). Chapter 7 l.236 agrees, and the
  code writes it only for a real (not pending) EPUB ISBN, as l.226 implies.
- **Appendix B's `registrations` entries agree** (l.141 to 164): the
  never-over-the-network rule, `pending` as `[pending]`, the print ISBN to
  the colophon and the barcode, the EPUB ISBN to the identifier, the LCCN
  shape check and PCN, the ISSN mod-11 with `X`, the retail rule (two real
  ISBNs; a declared LCCN or ISSN must be real; a missing one is no fault),
  the block's 978/979 prefix, sizes 10, 100, 1000 named and 10 to
  1,000,000 accepted, validated only when both keys are set.
- **Appendix A agrees** on `press isbn`, `press lookup`, `press onix`,
  `press pcn`: synopses, the status-line form, *dist/alice.onix.xml* and
  *dist/alice-pcn.txt*, no price, exit 0 only on `found`, Example A.7's
  scaffold values. Appendix E's CIP, LCCN, ONIX 3.0, and PCN entries agree.
- **Earlier promises to Chapter 13 are kept**: the registration numbers
  (Ch. 3 l.269; Ch. 6 l.62; Ch. 16 l.42); how a book gets an EPUB ISBN
  and the files the registration targets add (Ch. 7 l.236, 484; Ch. 3
  l.625: *alice-pcn.txt*, *alice.onix.xml*); the numbers and the `retail`
  switch (Ch. 10 l.182, kept at "The retail flag", l.132); the print ISBN
  and the paperwork (Ch. 12 l.225, 493); the ISBN under `registrations`
  (App. C l.520).
- **Cross-references out are right.** Chapter 3, *The shape of a book
  repository* (l.31); Chapter 12, *The print pack* (l.92; l.123 by
  number); Chapter 8, *Verifying the artifacts* (l.271); Chapter 10,
  *Front matter, the index, and the table of authorities* (l.273; l.165,
  192, 317 by number). Titles match design.md section 5 and the files.
  Both "later in this chapter" references are later ("The retail flag",
  l.44 to l.132; "Preassigned control numbers", l.130 to l.161).
- **Cast.** `alice`, `hatter`, `wonderland-press` only; every other
  number is the press's own (the example block 978-1-960780, the selftest
  ISSN 0378-5955 and its invalid cases) and is labeled as such (l.56,
  102, 115). Bowker, KDP, PrePub Book Link are real.
- **Numbering.** Figure 13.1 `13-01-where-numbers-land`, cited (l.263)
  before it appears (l.265), one blank line before the `art:` comment,
  matches design.md section 5. Tables 13.1 to 13.4, Examples 13.1 to 13.5,
  no gap, no repeat, each cited before it appears. Eight uncaptioned
  fences (l.138, 155, 235, 283, 291, 297, 304, 310), none referred to by
  number; all 13 fences `text`, none over 64 columns. Footnotes
  `13-earth`, `13-agent`, prefixed and unique.
- **In this chapter** box matches the nine A-heads.
- **Vocabulary.** No barred word for a thing. "Product" (l.212 to 226) is
  ONIX's own term for a product record, not a name for an artifact;
  "target" for `press isbn`, `press pcn`, `press onix`, `press lookup`
  matches the catalog (group "print pack") and Ch. 3 l.625's "registration
  targets"; "selftest" is `press selftest`, as in Ch. 12 Example 12.4.

## Findings

**1. ISSN on the copyright page.** Rule 7 (shared fact "Copyright page,
in order"). Severity: **blocks**.
Quote (l.273): "The copyright page carries one line for each registration
that the book declares." With l.102, a declared ISSN is a registration,
and the figure brief (l.267) labels the arrow to the copyright page
"isbn.print, isbn.epub, lccn, issn".
The press prints only "ISBN (print)", "ISBN (ebook)", and "LCCN" there
(*gen_front_matter.py* `_registration_lines`, l.136 to 148); Chapter 10
Table 10.4 (l.172) lists those three. An ISSN reaches no artifact at all:
it is validated, checked for retail, and looked up.
Fix (l.273): "The copyright page carries a line for each ISBN and for an
LCCN that the book declares. An ISSN does not print there." Fix (l.267,
art brief): the copyright-page arrow reads "isbn.print, isbn.epub, lccn";
keep "issn" in the boxed excerpt and give it no arrow, or drop it.

**2. The retail rule overstated in Chapters 3 and 6.** Rule 7. Severity:
**should** (fix in the committed chapters; Chapter 13 is right).
Quotes: Ch. 3 l.265, "When it is true, `press check` refuses any missing
or pending registration."; Ch. 6 l.62, "it refuses a retail book with a
missing or pending number."
Chapter 13 (l.136, 315), Appendix B (l.158), and *registrations.py*
`_retail_failures` refuse a missing or pending ISBN and a declared
`pending` LCCN or ISSN; a book that declares no LCCN or ISSN passes.
Fix (Ch. 3 l.265): "When it is true, `press check` refuses a missing or
pending ISBN, and a pending LCCN or ISSN." Fix (Ch. 6 l.62): "...and it
refuses a retail book with a missing or pending ISBN, or a pending LCCN
or ISSN."

**3. "colophon page" against Chapter 10's "colophon".** Rule 2. Severity:
may.
Quote (l.269): "It prints on the copyright page (the press calls it the
colophon page)".
Chapter 10 l.162 defines the press's word as "the *colophon*"; Appendix B
l.146 says "the colophon".
Fix: "(the press calls it the colophon)".

**4. Which artifact the print ISBN identifies.** Rule 7. Severity: may.
Quote (l.48): "the Print edition (the PDF) and the Circulating edition
(the EPUB) each need their own."
Chapter 12 l.151 separates the Print edition, *dist/alice.pdf*, "for
reading", from the print interior that the shop prints. The print ISBN
belongs to the printed book (the interior and its wrap), and it also
prints on the Print edition's copyright page. The sentence is defensible;
a reader of Chapter 12 may stumble.
Fix (optional): "the printed book and the Circulating edition (the EPUB)
each need their own."

**5. The Alice book's registration state after this chapter.** Rule 7.
Severity: may.
Quotes: l.17, "The Alice book has no registrations yet"; l.33, "Example
13.1 shows the Alice book with both of its ISBNs still on order"; l.143,
"while Example 13.1 is still in place".
The chapter implies, without saying, that `alice` adds Example 13.1. If
she does, the Alice copyright page gains "ISBN (print) [pending]" and
"ISBN (ebook) [pending]", which Chapter 10 l.180 ("declares no ...
registrations") showed before this chapter. That is chronology, not a
contradiction, but a later chapter that shows the Alice copyright page or
the `registrations` block needs to know which state holds. The bible now
records it as: both ISBNs `pending`, no block, no LCCN, no ISSN, `retail`
false.
Fix (l.33, optional): "`alice` puts Example 13.1 in the Alice book while
both of its ISBNs are on order."

**6. Figure 13.1's file is absent at this pass.** Rule 6. Severity: may.
`assets/woodcuts/13-01-where-numbers-land.png` is tracked and deleted in
the working tree (`git status`: `D`). The `@fig:` reference and the image
line are right; the build needs the file back (or redrawn) before the
chapter is committed. Not a chapter edit.

## Bible updates

Added 27 entries to *docs/continuity.md*: 11 terms (registration; the
three registration activities; ISBN; ISBN block and publication number;
`pending`; ISSN; LCCN; PCN and PrePub Book Link; CIP; the retail flag;
ONIX and the ONIX product), 12 shared facts (the registrations block and
governing rule; ISBN block rules; `press isbn`; ISSN check; LCCN
normalization; ISBN-10; the retail refusal; the PCN
listing; the ONIX record; `press lookup`; where each number goes; the
sample book's registration state), 2 cross-reference rows, 1 numbering
row, 1 Preface entry. Updated in place: the pass status, the `colophon`
term row, the shared facts "Sample book's identity after setup", "Sample
book's front-matter values" (Ch. 13 conflict resolved), "Copyright page,
in order" (finding 1), "EPUB extras", "EAN-13 and the placeholder", and
the cross-reference rows from Chapters 3, 6, 7, 8, 10, and 12 into 13
(now kept).

Conflicts with earlier chapters: Chapter 10 (and the press) on the ISSN
line (finding 1, fix in Chapter 13); Chapters 3 and 6 on the retail rule
(finding 2, fix in those chapters).
