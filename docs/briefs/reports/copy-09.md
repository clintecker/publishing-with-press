# Copyedit: Chapter 9, The house design

File: `book/chapters/09-the-house-design.md`

## Status

REVISE. Six blocks (all "a heading repeated as the first sentence", from
the one-sighting list), 26 should, 11 may, and six sentences referred to
the fact checker. `press check` names no finding in this file. Its seven
findings are all in Chapters 5, 6, and 12.

Counts by severity: blocks 6, should 26, may 11.

Most frequent rules broken: wrong term (20), then heading repeated (6) and
era spelling (5, every one of them "centre" or "centred").

Line numbers are `grep -n` line numbers in the file as it stands.

## The ste_check findings, judged

- Semicolons at 135, 202, and 379: accepted. 135 is inside the quoted
  profile sentence, 202 is the art directive, and 379 is the index
  comment. The chapter has no prose semicolon.
- Passives at 54 and 216: accepted. Both are verbatim quotations. "is
  filled" (139) is alt text describing a grid, "is green" (186) and "is
  centred" (192) are adjectives, not passives. 192 still has a spelling
  problem (item 23).
- Sentence length: 6 is the In-this-chapter box; 139 and 202 are the alt
  text and the art directive; 250 runs long only because the checker
  joins it to the next sentence at the closing quotation mark; 379 is
  the index comment. The others (65, 84, 156, 162, 192, 212) are at or
  under 30 words. Real overruns are 208 and 226 (items 26 and 28), and
  the alt text at 200 (item 25).
- Paragraph length at 27 and 141 (art directives): accepted. The sidebar
  at 54 (10 sentences) is item 34. The paragraph at 357 (seven
  sentences) is item 43.
- "therefore", "identical" (art directive), and the `-ing` forms in
  headings, chapter titles, and gerunds ("Installing press", "Writing the
  manuscript", "choosing a profile" inside a quotation): accepted under
  the 80 percent rule.

The checker does not catch the items below. They come from reading every
sentence.

## Findings

1. "The print interior changes the page twice." (49, under "### The print
   interior")
   Rule: heading repeated (a heading repeated as the first sentence,
   one-sighting list). Severity: blocks.
   Fix: "The print pack changes the house page twice."

2. "The reader site is the edition a reader opens in a browser: one
   chapter to a page, with links between them." (168, under "## The
   reader site")
   Rule: heading repeated. Severity: blocks. (The fix also glosses the
   edition name once, as the vocabulary asks.)
   Fix: "In a browser, a reader opens the Chapter edition (the reader
   site): one chapter to a page, with links between them."

3. "The landing page, *dist/pages/index.html*, is the front door of the
   book on the Web." (230, under "## The landing page")
   Rule: heading repeated. Severity: blocks.
   Fix: "On the Web, the front door of the book is the landing page,
   *dist/pages/index.html*."

4. "The *aesthetic* is the book's visual identity, kept in
   *config/aesthetic.yaml* and merged over the house values." (256, under
   "## The aesthetic file")
   Rule: heading repeated. Severity: blocks. (The participles "kept" and
   "merged" also hide the actor. If item 15 moves the definition of
   *aesthetic* to line 84, set it roman here.)
   Fix: "A book keeps its visual identity in *config/aesthetic.yaml*, and
   press merges that file over the house values."

5. "Version 3.0.0 is a design major, and its changes show what the rule
   covers." (357, under "### Version 3.0.0 as an example")
   Rule: heading repeated. Severity: blocks.
   Fix: "The changes in 3.0.0, a design major, show what the rule covers."

6. "The press holds this promise with machinery." (367, under "### The
   machinery behind the promise")
   Rule: heading repeated. Severity: blocks.
   Fix: delete the sentence, and open the paragraph with "Each profile
   carries a `design-major`, and the file *profile-seals.yaml* in the
   press's package data seals each profile with a digest of its
   contents."

7. "This chapter gives the house in numbers, shows what the six design
   profiles change, and follows the design onto the reader site and the
   landing page." (17)
   Rule: wrong term (first use of a term is italic and defined in the
   same sentence; the chapter defines *design profile* only at 135, after
   using it at 17 and 21). Severity: should.
   Fix: "This chapter gives the house in numbers, shows what the six
   *design profiles* (sealed page geometries) change, and follows the
   design onto the reader site and the landing page." Then set "design
   profile" roman at 135.

8. "The reading PDF is a KOMA-Script book." (21)
   Rule: wrong term (the editions take press's names, glossed once per
   chapter; the Print edition is first named only in Table 9.6).
   Severity: should.
   Fix: "The reading PDF, the Print edition, is a KOMA-Script book."

9. "The inner margin and the foot margin are the widest, at 0.78 inches
   each." (29)
   Rule: synonym rotation (Table 9.1 calls it the "Bottom margin").
   Severity: should.
   Fix: "The inner margin and the bottom margin are the widest, at 0.78
   inches each."

10. "It runs from the last line of text to the baseline of the folio."
    (39, Table 9.1)
    Rule: wrong term (*folio* is defined at 123; here it is used before
    the definition). Severity: should.
    Fix: "It runs from the last line of text to the baseline of the page
    number."

11. "The List of plates reads the standard `lof` file. The List of Figures
    reads a second file ..." (61; also "List of plates" twice at 63)
    Rule: wrong term (the vocabulary writes "List of Plates", and the
    same paragraph capitalizes "List of Figures"). Severity: should.
    Fix: "The List of Plates reads the standard `lof` file." At 63: "...
    and that silently empties the List of Plates." and "... so a shallow
    contents page and a full List of Plates live together."

12. "Captions are therefore small, italic, and centred." (65)
    Rule: era spelling (American spelling). Severity: should.
    Fix: "Captions are therefore small, italic, and centered."

13. "The last option sends a link in either list to the top of the
    picture instead of to its caption, which is where the reader wants
    to land." (65)
    Rule: wrong term ("picture" is on the vocabulary's never list for a
    plate or a figure; "land" is the watchlist's status shorthand in
    its base form). Severity: should.
    Fix: "The last option sends a link in either list to the top of the
    figure instead of to its caption, which is where the reader wants to
    arrive."

14. "When it names a family, the header writes
    `\setmainfont{<family>}[Numbers=OldStyle]` instead, so the chosen face
    sets its figures in the old style, with descenders like lowercase
    letters." (84)
    Rule: wrong term (*figure* is the book's word for a numbered
    illustration; here it means numerals). Severity: should.
    Fix: "When it names a family, the header writes
    `\setmainfont{<family>}[Numbers=OldStyle]` instead, so the chosen
    face sets its numerals in the old style, with descenders like
    lowercase letters."

15. "A book can choose another body face with the aesthetic key
    `typography.pdf-family`." (84; "the aesthetic" also at 75, 98, and
    135)
    Rule: wrong term (the chapter uses *aesthetic* from line 75 but
    defines it only at 256). Severity: should.
    Fix: "A book can choose another body face in its *aesthetic*, the
    visual identity in *config/aesthetic.yaml*, through the key
    `typography.pdf-family`." In Table 9.2 (75): "The header loads it
    with `\usepackage{libertinus}` unless the book names another face."

16. "The value `\parfillskip=0pt plus 0.8\hsize` makes the last line of a
    paragraph fill at least a fifth of the measure." (94)
    Rule: wrong term (*measure* is the vocabulary's word for the width
    class of a figure). Severity: should.
    Fix: "The value `\parfillskip=0pt plus 0.8\hsize` makes the last line
    of a paragraph fill at least a fifth of the line."

17. "In the PDF the `drop-cap` style becomes a call to the LaTeX package
    lettrine, wrapped in the house macro `\PressDropCap`." (117)
    Rule: code typography (style guide 4: every other package in the
    chapter, `microtype`, `selnolig`, `caption`, `mdframed`, is in
    constant width). Severity: should.
    Fix: "In the PDF the `drop-cap` style becomes a call to the LaTeX
    package `lettrine`, wrapped in the house macro `\PressDropCap`."

18. "The initial is three lines deep, with `findent=2pt` between the
    initial and the text, and the rest of the first word follows in
    small caps." (117; "the initial" again at 117 and twice at 119)
    Rule: wrong term ("initial" is on the never list for the chapter
    opening; the vocabulary keeps "drop cap" for the `drop-cap` style)
    and two ideas. Severity: should.
    Fix: "The drop cap is three lines deep, with `findent=2pt` between
    the letter and the text. The rest of the first word follows in small
    caps." At 117 and 119, "the initial" becomes "the drop cap".

19. "The command `\cfoot` puts the page number, the *folio*, in the
    centre of the foot." (123)
    Rule: era spelling. Severity: should.
    Fix: "The command `\cfoot` puts the page number, the *folio*, in the
    center of the foot."

20. "Its outer head reads "Down the rabbit-hole", and its folio sits in
    the centre of its foot." (125)
    Rule: era spelling. Severity: should.
    Fix: "Its outer head reads "Down the rabbit-hole", and its folio sits
    in the center of its foot."

21. "Table 9.4 gives the rest of each profile: its margins, its indent and
    leading, and its measure on the Web." (143; "a set of measures for
    the Web" at 135, the column head "Web measure" at 145, the "Web
    leaf" in every row of Table 9.4, and "the profile's Web measure" at
    326 and 342)
    Rule: wrong term ("measure" is reserved for the width class, and
    *leaf* is used in Table 9.4 before its definition at 186).
    Severity: should. (The profile key is `web: {measure: ...}`. If the
    authors want to keep the word, name the key in code once and say so.)
    Fix: "Table 9.4 gives the rest of each profile: its margins, its
    indent and leading, and the width of its *leaf*, the paper column
    that holds the text on the reader site." Then set "leaf" roman at
    186. Column head: "Indent, leading, and leaf width". At 135: "and a
    leaf width for the Web". At 326 and 342: "the profile's leaf width".

22. "A book that needs color pictures inside chooses `house-6x9-color`,
    and it accepts the cost: Chapter 12 explains why some providers
    refuse a color interior." (158)
    Rule: wrong term ("picture") and two ideas. Severity: should.
    Fix: "A book that needs color plates or figures inside chooses
    `house-6x9-color`. It accepts a cost, and Chapter 12 explains why
    some providers refuse a color interior."

23. "An `h1` is centred, between 1.9 and 2.5 rem depending on the width
    of the screen, with a small-caps line "Chapter N" above it and a
    diamond rule below it." (192)
    Rule: era spelling and two ideas (29 words). Severity: should.
    Fix: "An `h1` is centered, between 1.9 and 2.5 rem depending on the
    width of the screen. A small-caps line "Chapter N" sits above it and
    a diamond rule below it."

24. "A horizontal rule becomes a small diamond between two hairlines that
    fade toward their ends." (194)
    Rule: wrong term (the manuscript's `***` is a *scene break*; the
    vocabulary keeps "ornament" for the glyph). Severity: should.
    Fix: "A scene break becomes a small diamond ornament between two
    hairlines that fade toward their ends."

25. "The leaf holds a masthead, a closed contents drawer, a centred
    chapter heading over a diamond rule, a paragraph with a drop cap, a
    framed engraving, and links to the previous and next chapters." (200,
    fig-alt, read aloud by a screen reader)
    Rule: era spelling, wrong term ("engraving" for a plate), and
    sentence over 30 words (34). Severity: should.
    Fix: "The leaf holds a masthead, a closed contents drawer, and a
    centered chapter heading over a diamond rule. Below them are a
    paragraph with a drop cap, a framed plate, and links to the previous
    and next chapters."
    (The art directives at 27 and 202 also say "centred". They are the
    illustrator's text; the art desk may want "centered" for
    consistency.)

26. "The index page of the reader site holds the title block, the cover if
    the book has one, a lede that begins "This is the reading edition",
    and a "Start reading" button with the access key `s`." (208)
    Rule: sentence over 30 words (32). Severity: should.
    Fix: "The index page of the reader site holds the title block and the
    cover, if the book has one. Below them are a lede that begins "This
    is the reading edition" and a "Start reading" button with the access
    key `s`."

27. "The single-file HTML edition uses *book.css*, which uses the same ink,
    muted, and accent values as the PDF and sets the text on a near-white
    paper." (224)
    Rule: wrong term (the vocabulary's name is the Single-leaf edition)
    and two ideas. Severity: should.
    Fix: "The Single-leaf edition (the self-contained HTML) uses
    *book.css*. That sheet takes the same ink, muted, and accent values
    as the PDF, and it sets the text on a near-white paper."

28. "The EPUB sheet, *epub.css*, sets a serif face on a 1.45 line, a drop
    cap at 3 em, and a rule that keeps a figure inside the width of the
    screen." (226)
    Rule: sentence over 30 words (32 by the checker's count). Severity:
    should. (The fix also glosses the Circulating edition once.)
    Fix: "The Circulating edition (EPUB) uses *epub.css*. That sheet sets
    a serif face on a 1.45 line, a drop cap at 3 em, and a rule that
    keeps a figure inside the width of the screen."

29. "It is a book of verse, and it sets `.reader main {max-width: 30rem}`
    for a narrow column and a line height of 1.85 for room between the
    lines." (328)
    Rule: two ideas (29 words). Severity: should.
    Fix: "It is a book of verse. Its *extra.css* sets
    `.reader main {max-width: 30rem}` for a narrow column and a line
    height of 1.85 for room between the lines."

30. "They are `microtype` protrusion and expansion, the `selnolig` ligature
    rule, and old-style figures for the aesthetic font." (357)
    Rule: wrong term ("figures" for numerals, as in item 14) and synonym
    rotation ("font" where the chapter otherwise says "face").
    Severity: should.
    Fix: "They are `microtype` protrusion and expansion, the `selnolig`
    ligature rule, and old-style numerals for the aesthetic's face."

31. "The move itself produced one more lesson." (361)
    Rule: wrong term (the vocabulary's word is *scar*, never "lesson").
    Severity: should.
    Fix: "The move itself left one more scar."

32. "On an immutable tag such as `v3.0.2`, it keeps the same pipeline, the
    same composite action, and the same toolchain bytes forever." (371)
    Rule: wrong term ("pipeline" is on the never list). Severity: should.
    Fix: "On an immutable tag such as `v3.0.2`, it keeps the same press
    code, the same composite action, and the same toolchain bytes
    forever."

33. "The total is the same 1.46 inches, so the text block keeps its width,
    and the extra space moves toward the gutter, where the binding takes
    up paper." (49)
    Rule: two ideas. Severity: may.
    Fix: "The total is the same 1.46 inches, so the text block keeps its
    width. The extra space moves toward the gutter, where the binding
    takes up paper."

34. The sidebar "The KOMA spelling trap" (54) is one paragraph of ten
    sentences.
    Rule: paragraph over six sentences (rhythm). Severity: may.
    Fix: break the paragraph after "... and there the short spelling
    fails without a word." The second paragraph opens "The comment in
    the press's print defaults states the cost exactly: ..."

35. "The house reading PDF is one-sided, and it loads the class with
    `openany`." (54, sidebar)
    Rule: hidden actor (a PDF does not load a class; the house header
    does). Severity: may.
    Fix: "The house reading PDF is one-sided, and its header loads the
    class with `openany`."

36. "The left and right arrow keys turn the pages, and the page ignores
    them when a modifier key is down or the cursor sits in a form
    field." (204)
    Rule: two ideas (28 words). Severity: may.
    Fix: "The left and right arrow keys turn the pages. The page ignores
    them when a modifier key is down or the cursor sits in a form field."

37. "The first part is a "Read the Book" invitation, with the line "one
    chapter to a page, as is proper", which leads to the reader site."
    (232)
    Rule: two ideas ("which" can attach to the line or the invitation).
    Severity: may.
    Fix: "The first part is a "Read the Book" invitation that leads to the
    reader site, with the line "one chapter to a page, as is proper"."

38. "It also holds the few design values that a book may change." (256)
    Rule: honest modals ("may" for permission; the contract keeps "may"
    for real uncertainty). Severity: may. (Same at 271, "The tokens a
    palette may name".)
    Fix: "It also holds the few design values that a book can change."

39. "A palette changes colors and a font stack." (322)
    Rule: wrong term (the font stack is `typography.web-family`, not part
    of a palette; the subject is the aesthetic). Severity: may.
    Fix: "The aesthetic changes colors and a font stack."

40. "Its plates are alpha masters, black ink on transparency, and in the
    dark theme they sit on the dark `--paper-warm` mat." (328)
    Rule: wrong term (first use of *alpha master* in the chapter is not
    italic) and two ideas. Severity: may.
    Fix: "Its plates are *alpha masters*, black ink on transparency. In
    the dark theme they sit on the dark `--paper-warm` mat."

41. "Press makes a promise about design, and *ARCHITECTURE.md* states it
    in full:" (347)
    Rule: two ideas ("in full" introduces a quotation that carries an
    ellipsis). Severity: may.
    Fix: "Press makes a promise about design, and *ARCHITECTURE.md*
    states it:"

42. "A floating tag such as `v3` moves to each new compatible release, and
    an immutable tag such as `v3.0.2` never moves." (351)
    Rule: wrong term (first use in the chapter of *floating tag* and
    *immutable tag* is not italic). Severity: may.
    Fix: "A *floating tag* such as `v3` moves to each new compatible
    release, and an *immutable tag* such as `v3.0.2` never moves."

43. The paragraph at 357 runs seven sentences, and "It also hung the
    quotation mark of a dialogue opener into the margin." renames what
    119 calls "a chapter that opens with speech".
    Rule: paragraph over six sentences and synonym rotation. Severity:
    may.
    Fix: "It also hung the quotation mark of a chapter that opens with
    speech into the margin." Fold the "They are" and "They also include"
    sentences into one list: "They are `microtype` protrusion and
    expansion, the `selnolig` ligature rule, old-style numerals for the
    aesthetic's face, the six settings against widows, orphans, and
    stray hyphens, the runt rule, and the hyphenation minimums." (That
    sentence is about 30 words; if the fact checker keeps every item,
    the authors may prefer a short list.)

## Referred to the fact checker

Not edited. Each sentence may be wrong in fact.

- "Two more settings control the shape of the paragraph." (94) The
  paragraph then gives four values: `\parfillskip`, `\lefthyphenmin`,
  `\righthyphenmin`, and `\hyphenpenalty`. fact: see fact checker.
- "The house PDF uses six named colors, and the aesthetic can override
  them through `book-colors`." (98) Table 9.7 says `book-colors`
  overrides four (`ink`, `muted`, `accent`, `link`). fact: see fact
  checker.
- "The PDF body stays at 10 points in every profile, and only the leading
  changes." (156) Table 9.4 also gives a different indent per profile.
  fact: see fact checker.
- "... the press gives the reason in four words: "the reader owns the
  theme."" (226) The quotation has five words. fact: see fact checker.
- "... and moves the PDF accent and links to the same red." (273) Example
  9.1 sets `accent` to `7B2D26` and `link` to `5C1F1A`, two reds. fact:
  see fact checker.
- "Example 9.1 follows it, and it writes out every token of the light
  palette, including the ones it keeps." (314) Example 9.1 names ten of
  the twelve tokens that 271 lists; `hairline` and `ornament` are
  absent. fact: see fact checker.

## Also checked

- Second person and present tense throughout. Past tense appears only
  for history (90, 357 to 361, the footnotes), which the contract allows.
- "we" appears once, at 339 ("We suggest"), for the authors' judgment. No
  "I".
- Dry understatement: 54 ("a printer bills for every page"), 308 ("under
  the name of a green"), and 314 ("that surprises authors once"). They
  are spaced through the chapter, and none is in a heading.
- Admonitions: five tips and two warnings. All are imperative, and all
  run to three sentences or fewer.
- Footnotes: three (the `hypcap` history, the Libertine scar, the issue
  number for 3.0.1). All are asides. The body does not depend on any.
- Spellings: "Web" and "filename" (234) are correct. No "website",
  "email", "file name", "man page", "UNIX", "appendices", or "towards"
  ("toward" at 49 and 194). "centre" and "centred" are items 12, 19, 20,
  23, and 25.
- Numbers under ten: spelled out in prose ("five lines", "four parts",
  "six profiles", "three letters"). The numerals that remain are
  measurements ("4 pixels", "3 em"), versions, or code.
- Headings: sentence case throughout. No title case. The quoted landing
  page labels at 232 ("Read the Book", "Table of Editions", "How This
  Book Was Built") are verbatim template text and stay.
- No em or en dashes, no assistant vocabulary, no -ing riders, no "not X
  but Y", no hedge stacks, no perfect tense in prose. "ship" (54) and
  "cleanly" (349) are inside quotations. "seam" (90, 261, 271),
  "canonical" (212, 216), "fallback" (103), and "spine" (353) are on the
  book's `jargon-allow` list and carry their literal or press-named
  sense.
- The opener's "This chapter gives ..." (17) is the period opener that
  style guide 8.1 allows. It stays.
