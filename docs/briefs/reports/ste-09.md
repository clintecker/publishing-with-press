# STE80 editor report: Chapter 9, The house design

File: `book/chapters/09-the-house-design.md`

Ratchet count: 4 before under the ratchet as it stood when I started, 3 for
the unchanged file under the current ratchet (the baseline in
`tools/ste-baseline.json` now reads 3; `tools/ste-ratchet.py` and the
baseline changed at 09:59 while I worked, and the sidebar unwrap rule
removed the sidebar lead). After: 1. `press check` passes (exit 0).
`python3 tools/ste-ratchet.py` passes.

Sentinels: none of the three stands in this chapter. Index terms: every
match string in `config/index-terms.yaml` occurs in the file the same
number of times before and after. No code span, fence, quotation, heading,
figure line, art comment, or footnote changed. The sidebar is untouched.

## Edits (23, line numbers in the edited file)

1. L17, S1 and S2 (29 words, three ideas). Old: "This chapter gives the
   house in numbers, shows what the six *design profiles* (sealed page
   geometries) change, and follows the design onto the reader site and the
   landing page. It then shows how a book changes its own appearance, and
   it ends with the reason a design change waits for a new major version."
   New: "This chapter gives the house in numbers and shows what the six
   *design profiles* (sealed page geometries) change. Then it follows the
   design onto the reader site and the landing page. It shows how a book
   changes its own appearance, and it ends with the reason a design change
   waits for a new major version."
2. L45, S1 (25 words, two ideas). Old: "The last row is the height cap from
   Chapter 5, *Figures, plates, and illustrations*, and each profile sets
   its own value with the key `figure-cap`." New: "The last row is the
   height cap from Chapter 5, *Figures, plates, and illustrations*. Each
   profile sets its own value with the key `figure-cap`."
3. L76, S1 and S6 (26 words). Old: "When it names a family, the header
   writes `\setmainfont{<family>}[Numbers=OldStyle]` instead, so the chosen
   face sets its numerals in the old style, with descenders like lowercase
   letters." New: "When it names a family, the header writes
   `\setmainfont{<family>}[Numbers=OldStyle]` instead. That option makes
   the chosen face set its numerals in the old style, with descenders like
   lowercase letters."
4. L80, S1 (which-clause as second idea). Old: "Expansion lets the face
   widen or narrow a little on a line, which gives the paragraph builder
   more ways to avoid a loose line." New: "Expansion lets the face widen or
   narrow a little on a line. That gives the paragraph builder more ways to
   avoid a loose line." (Paragraph now six sentences.)
5. L90, S1, S2, S4 (31 words with a parenthetical second idea). Old: "The
   plates and the figures have separate lists, the List of Plates and the
   List of Figures (a scar Chapter 7 tells kept the List of Plates full at
   that depth)." New: "The plates and the figures have separate lists, the
   List of Plates and the List of Figures. A scar that Chapter 7 tells kept
   the List of Plates full at that depth."
6. L96, S1 (25 words, two ideas). Old: "That rule is a *craft law*, a law
   of the house that no configuration can change, and Chapter 11, *The art
   department*, names the others." New: "That rule is a *craft law*, a law
   of the house that no configuration can change. Chapter 11, *The art
   department*, names the others."
7. L104 (table cell), S6. Old: "It is defined by the header and used
   nowhere." New: "The header defines it and uses it nowhere."
8. L109/111, S13 (one topic per paragraph). Split the links paragraph
   before "A book with no front matter still gets a plain fallback title
   page." The fallback title page and Chapter 10's generated front matter
   are a second topic. No words changed.
9. L115, S1 (29 words, three ideas). Old: "The rest of the first word
   follows in small caps, and the macro reserves four lines first, so the
   drop cap never starts at the foot of a page." New: "The rest of the
   first word follows in small caps. The macro reserves four lines first,
   so the drop cap never starts at the foot of a page." (Paragraph now six
   sentences.)
10. L144, S1 (26 words). Old: "The figure takes the house text width as
    stated and derives the other four from Table 9.4: the trim width less
    the inner and outer margins." New: "The figure takes the house text
    width as stated. It derives the other four from Table 9.4: the trim
    width less the inner and outer margins."
11. L163, S1 (28 words). Old: "It has a 7 by 10 trim, the widest margins,
    the tallest height cap, and a leading of 1.2, and on the Web it sets
    1.4 rem type." New: "It has a 7 by 10 trim, the widest margins, the
    tallest height cap, and a leading of 1.2. On the Web it sets 1.4 rem
    type."
12. L170 (tip), S1 (30 words). Old: "The height cap and the text width
    set the largest size a plate can print at, and a plate drawn for one
    page may look cramped on a smaller one." New: "The height cap and the
    text width set the largest size a plate can print at. A plate drawn for
    one page may look cramped on a smaller one." ("may" kept.)
13. L175, S10 (ratchet lead, phrasal verb). Old: "To look at a change, run
    `press site` ..." New: "To see a change, run `press site` ..."
14. L202, S1 and S3. Old: "The drawer starts closed, and when the reader
    opens it, it lists the chapters with the current one expanded." New:
    "The drawer starts closed. When the reader opens it, it lists the
    chapters with the current one expanded."
15. L208, S3 (condition first). Old: "The page ignores them when a
    modifier key is down or the cursor sits in a form field." New: "When a
    modifier key is down or the cursor sits in a form field, the page
    ignores them."
16. L208, S1. Old: "Access keys reach the masthead (`u`), the previous page
    (`p`), and the next page (`n`), and the template also gives a "Skip to
    chapter" link." New: "Access keys reach the masthead (`u`), the
    previous page (`p`), and the next page (`n`). The template also gives a
    "Skip to chapter" link."
17. L232, S1 (26 words, three ideas). Old: "It shares the tokens of the
    reader sheet, but it sets a narrower paper column, at most 44 rem wide,
    and it has no dark theme." New: "It shares the tokens of the reader
    sheet, but it sets a narrower paper column, at most 44 rem wide. It has
    no dark theme."
18. L273, S1 (27 words, a which-clause as second idea). Old: "...,
    `ornament`, and `accent`, which only the cover prompt reads." New:
    "..., `ornament`, and `accent`. Only the cover prompt reads `accent`."
19. L312, S8 (ratchet lead, "including"). Old: "It writes nine tokens of
    the light palette and all four book colors, including the values it
    keeps." New: "It writes nine tokens of the light palette and all four
    book colors, the values it keeps among them." (Kept as one sentence so
    the paragraph stays at six.)
20. L377, S1 (27 words). Old: "Across a whole book the page count
    changes, and the page count sets the width of the spine on the cover
    wrap (Chapter 12 shows the arithmetic)." New: "Across a whole book the
    page count changes. The page count sets the width of the spine on the
    cover wrap (Chapter 12 shows the arithmetic)." (Paragraph now six
    sentences.)
21. L381, S1 (30 words). Old: "That release added the line-breaking
    rules from the section "Type" earlier in this chapter, and it hung the
    quotation mark of a chapter that opens with speech into the margin."
    New: "That release added the line-breaking rules from the section
    "Type" earlier in this chapter. It also hung the quotation mark of a
    chapter that opens with speech into the margin."
22. L385, S8 (-ing form). Old: "...once told an author moving from
    version 2 to version 3..." New: "...once told an author who moved from
    version 2 to version 3..."
23. L391, S1. Old: "Each profile carries a `design-major`, and the file
    *profile-seals.yaml* in the press's package data seals each profile
    with a digest of its contents." New: "Each profile carries a
    `design-major`. The file *profile-seals.yaml* in the press's package
    data seals each profile with a digest of its contents."

## Leads declined

- L196, passive 'is green': "The page background is green book cloth" is a
  copula with an adjective, not a passive. False positive.
- (Old ratchet only) sidebar "The KOMA spelling trap", paragraph length:
  Light mode. Every sentence is under 30 words with one idea, it holds no
  semicolon, and it runs about 150 words, under the 190 ceiling. The
  current ratchet no longer flags it.
- Long sentences kept (24 to 29 words, one idea each, mostly lists):
  L49 (the two option sets for `scrbook`), L82 (widow and club rule), L133
  (the font family and palette sentence), L196 (cloth and paper column),
  L214 (the metadata list), L226 (Charter stack), L228 (EPUB sheet list),
  L304 (the `--link` because-clause), L401 (closing sentence). Splitting
  them would separate a list from its subject or a cause from its effect.

## Passives kept

- L373 (quotation from ARCHITECTURE.md, "a book that was already valid"):
  a quotation, never touched.
- No other passives remain in body prose that I could find.
