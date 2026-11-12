# Report: Chapter 13, Registrations

Status: DONE_WITH_CONCERNS. File: `book/chapters/13-registrations.md`.

## Word count

`press wordcount`: 3,299 (target 3,500; within 15 percent). `press check`
exits 0 from the repository root.

## Figures

- Figure 13.1 `@fig:where-numbers-land`, `assets/woodcuts/13-01-where-numbers-land.png`,
  data-flow drawn left to right: metadata.yaml with a gray `registrations:`
  excerpt (isbn.print, isbn.epub, lccn, issn) at left; five stacked
  destinations at right (colophon page, EPUB metadata/content.opf, wrap
  barcode, ONIX file dist/alice.onix.xml, PCN text dist/alice-pcn.txt),
  each arrow labelled with the field it carries. Reader sees first that one
  block feeds all five.

## Tables and examples

Tables 13.1 (three activities), 13.2 (checks per number), 13.3 (ONIX
elements), 13.4 (lookup limits). Examples 13.1 (pending ISBNs), 13.2 (the
fact file's ISBN block), 13.3 (`press isbn status` with no block), 13.4
(ISSN check worked for 0378-5955), 13.5 (`press pcn`). Each is referenced
before it appears. One sidebar ("Pending, not a guess", about 165 words),
and three footnotes.

Admonitions: warnings on KDP's free ISBN, unsetting a printed ISBN, and the
deposit date; tips on setting prefix and size together, assigning before
`press pcn`, and looking a number up before storing it. Six in all.

## Decisions and facts not found

- Example 13.5 (PCN output): slug `demo` -> `alice` as the brief says. I
  also changed "Clint Ecker" (author and publisher) to "Lewis Carroll",
  because Chapter 3 scaffolds the Alice book with `--author "Lewis Carroll"`
  and the publisher defaults to the author; printing the maintainer's name
  as Alice's author would contradict Chapter 3 and the scaffold-neutrality
  rule. Every other character kept. Two over-64-column lines were broken
  (said so in prose), and the two long closing lines were elided with `...`
  and quoted verbatim in the following paragraph.
- Example 13.3 (`press isbn status`) wrapped to three lines to fit 64
  columns; said so in prose.
- No ISBN, LCCN, or ISSN value is invented. No `press isbn assign`, `press
  onix`, or `press lookup` output is shown (the fact file quotes none).
  The retail refusal is quoted only by its fixed opening, in prose.
- The ISSN worked example (Example 13.4) is arithmetic on the selftest's
  own valid number; the sum (160, remainder 6, check 5) agrees with the
  number. I stated the check as 11 minus the remainder, which is the
  standard ISSN rule and matches; the fact file gives only "mod 11, weights
  8 to 2, 10 written X".
- Not found, left out: what each lookup outcome other than `found` means
  (only the names are given); which metadata fields feed each PCN line;
  whether `lccn`/`issn` accept `pending`; whether ISSN prints on the
  colophon (the figure's colophon arrow lists issn on the strength of
  "one line for each registration number the book declares", Chapter 10);
  the ISO code that `en-US` maps to; the `{label}` values in
  RecordReference; what happens to `press lookup` with no number and none
  configured.
- Avoided as section 20.B items: ISBN minting starting at publication
  number 0 (I say only "lowest unused"), and ONIX NotificationType 03
  (omitted).

## Contradictions in the fact file

None internal. Docs vs code on block size (docs 10/100/1000, code 10
through 1,000,000) is stated as both, as the fact file does.

## Residual ste_check findings (18) and defence

- Semicolons (lines 46, 175, 221): all inside verbatim quotations from
  press documentation and output; prose has none.
- `must be deposited` (175): inside the quoted PCN obligations line.
- `verify` (42): press's own target vocabulary ("build, check, and verify").
- `-ing` forms: "Cataloging in Publication" (proper name); A-heads
  "Looking numbers up" (mandated by the brief) and the cross-referenced
  chapter title "Verifying the artifacts".
- `are stated` (246): inside the quoted first law, "Facts are stated once."
- Sentence-length and paragraph-length hits: the fig-alt and `art:` comment
  (248, 250), the sidebar counted as one paragraph (141), the index comment
  (302), and two places where a footnote marker joins two sentences for
  the counter (98, 177).

## Revision (after the fact, developmental, copy, and type desks)

Word count after revision: 3,256 (`press wordcount`; target 3,500, 7 percent
under). `press check` exits 0. ste_check: 17 findings, all of the kinds
defended above (quoted semicolons and passive at the PCN and documentation
quotations, the quoted first law, `verify`, the -ing names and headings,
the alt text, the `art:` comment, the index comment).

Coordinator rulings applied:

1. Retail section states S1: two real ISBNs (print and epub), the
   `isbn print missing` / `isbn epub missing` entries, pending ones listed
   as pending, the LCCN and ISSN outside the retail check and validated
   separately only when declared, and the refusal wording with `<list>` (in
   a `text` fence, broken to fit). It ends with `press config set
   registrations.retail true`, `press check`, `press all`. Chapter 14
   pointer removed. Note: ruling 1's phrase "an LCCN or ISSN only fails if
   present and still pending" goes slightly beyond S1, which says only
   "validated separately when present"; I followed S1's wording.
2. Example 13.5 is captioned and introduced as a fresh scaffold made with
   `press new alice --author "Lewis Carroll"`, before Chapters 3 and 10;
   the lead-in says the values come from the book's metadata and the labels
   and layout are the press's. The gap paragraph now describes the
   scaffold's placeholders and says Chapters 3 and 10 replace them with the
   full title, the double subtitle, Wonderland Press, and Oxford. Example
   13.3 likewise says "fresh scaffold". No Wonderland Press output invented.
3. The copyright-page sentence now says what each route carries (barcode
   print only, EPUB identifier EPUB only). Cut: "names the numbers at
   fault", "no artifact gets built", "Neither refusal changes the file",
   the 123X-5678 reason, "in the order the form asks", the
   look-up-before-storing workflow (tip now says only that a held record
   ends `found`), the "each step needs a number" rationale, "and none can",
   "as the place to start", "power of ten", "the model would refuse",
   "time of the build", "cannot go on sale". ISBN-10 footnote and its body
   paragraph removed; Table 13.2's ISBN-10 row keeps only the fact file's
   "returns none for 979". Example 13.3 lead-in now says three lines.
4. "Where each number goes" in heading and box; sidebar closer cut,
   sidebar split into two paragraphs (156 words), retitled "Why pending is
   a word"; "When the LCCN comes back"; "The checker refuses a malformed
   block"; "mod-11 check" throughout (table "Mod-11 check"); "PCN listing"
   in alt text and figure label; "the book model" phrase removed (now "the
   validated path of `press config`"); "copyright page" throughout, with
   one parenthetical "(the press calls it the colophon page)"; figure box
   relabelled "copyright page"; "labeled".
5. No `press isbn assign` capture exists, so its effect is described, not
   shown (and minting from 0 stays unstated, per 20.B.20).
   `registrations.issn` named in the ISSN section with its `press config
   set` command. Outcomes named, only `found` explained. Chapter 3 cited as
   *The shape of a book repository*. Trimmed: the DOCTYPE paragraph is one
   sentence in Table 13.4's cell; the invalid-ISSN paragraph is one
   sentence and the ISSN prose no longer restates the table; the
   placeholder rationale lives in the sidebar only (cut at the old lines 42
   and 256).
6. Table 13.3's Element column widened (32 dashes) and Value narrowed;
   `dist/alice.onix.xml` and `registrations.isbn.epub` moved to mid-sentence
   positions ("... in the book's dist directory", "... beside it"). I did
   not rebuild the PDF, so the line breaks are unverified; the typesetter
   should recheck, along with the Table 13.2 page split and the figure gap
   (both depend on final layout and art). Footnotes remain `13-` prefixed
   (two left: `13-earth`, `13-agent`). Every fence is `text`.

Fact-check items carried out: Drifted 1 to 10 all applied as the checker
proposed (or cut). Missing 1 (may) accepted: `ProductComposition 00` and
`TitleType 01` rows added; `NotificationType` still omitted.

Developmental: P1 (S1), P2, P3 (described), P4 (step 1 split into buy and
record; no `press config set` for the nested block key, since the fact desk
did not confirm the form; final step adds `press check` and `press all`;
the ISSN gap stated as "The skill's order names no step for an ISSN"; no
lookup step, per ruling 3), P5, P6, P7 (label not defined in the fact file;
the Value cell keeps the press's pattern and the Meaning cell explains the
base only), P8, P9 (KDP rule attributed to the skill with no reason; the
ISBN-10 line cut), P10, R1, R2, R3, N1.

Copy mays: accepted 10, 11, 12, 14, 18, 21, 25, 27, 29, 36, 37, 40, 41,
42 (partly), 43, 45, 46, 47, 48. Declined 15 (the sentence is cut), 39
(ruling 4 makes "copyright page" the term), 44 (the angle brackets are the
press's own synopsis and listing text, which the PCN quotation shows
verbatim). Copy 34 superseded by ruling 3/4 wording. Copy 16 moot (the
"checker refuses both" sentence is cut).

## Revision 2

Retail rule corrected to the fixed S1 (`registrations.py:350-355`): two real ISBNs (print and epub) are required, and any LCCN or ISSN the book declares must be real, since a declared `pending` one joins the refusal list; an undeclared one is not a retail fault. Changed the retail paragraph, the `<list>` sentence ("the entries at fault"), the sidebar's last sentence ("a pending number"), and the order-of-operations rationale. `press check` passes for this file; it fails only on `book/chapters/16-inside-the-press.md:232` (assistant vocabulary), another writer's file.

## Revision 3

Re-review items applied: the order-of-operations sentence split after "The retail flag comes last."; the copyright-page sentences joined with "so"; "in the book's dist directory" dropped from the ONIX paragraph.
