# Copyedit: Appendix E, Glossary, and the Colophon

Files: `book/appendices/e-glossary.md`, `book/appendices/z-colophon.md`
(the colophon added to this desk by the controller).

## Status

REVISE. One block: "Press ships four" (glossary 435), a watchlist word
outside any quotation. The `jargon-allow` list admits "ship" and
"shipped" but not "ships". The jargon lint matches whole words, so it
would not catch this sighting. The prose contract still puts the
watchlist on the one-sighting list, and the Appendix D precedent grades
it as a block.

Counts by severity: blocks 1, should 24, may 18. Fact notes for the fact
checker: 4 (items 16, 27, 40, 41), with three more facts to confirm
inside items 23, 26, and 43. Items 16 and 27 are fact-only and have no
severity.

Most frequent rules broken: two ideas (13 items), hidden actor (11), wrong
term (10, counting the block). Synonym rotation follows with 3.

Line numbers are `cat -n` line numbers in each file as it stands.

## Gates run

- `python3 tools/ste_check.py` on both files: 14 findings (judged below).
- `press check`: the source checks fail on two plates that the manuscript
  never references, `assets/woodcuts/12-01-cover-wrap-anatomy.png` and
  `12-02-spine-math.png`. That is Chapter 12's problem and not in these
  files. Because the source pass failed, the checker stopped there and the
  jargon lint did not run.
- `press style` (the style audit run alone): "Editorial checks passed: 23
  Markdown files".
- A script applied every `banned-patterns` regex from
  `config/house-rules.yaml` to both files and found no match. Neither file
  has a non-ASCII character or a dash.
- Watchlist hits (whole word): gate (87, 323, 324, 327, 360), spine (99,
  285, 297, 318, 383, 384), clean (231, the filename *clean.md*), parity
  (284, the press term *parity-aware*), proves (336), stale (386). All are
  in `jargon-allow`, and each is press's own name or a literal use. "proves"
  at 336 is the vocabulary's own definition of the release contract ("the
  workflow that proves a tag"). Accepted. The one stem-only hit is "ships"
  (item 1).

## The ste_check findings, judged

- Glossary (8 findings, 369 sentences, average 7.6 words, max 26): the
  `-ing` forms at 15 ("ending"), 78 (*Cataloging in Publication*, a proper
  name), 170 (the term *floating tag*), 177 ("facing"), and 198 ("by
  editing press") are accepted. The forms at 324 ("holding", item 17) and
  375 ("matching", item 36) are real riders. "verify" at 387 names the
  verify targets. Accepted.
- Colophon (6 findings, 19 sentences, average 19.3, max 87): the
  semicolon, the 87-word "sentence", and "landscape" at 5 all sit in the
  `art:` comment, which is a directive for the illustrator and not prose.
  Accepted. The passives at 9 ("was written", "were commissioned") are
  real (items 22 and 23). "facing left" at 11 is an adjectival participle.
  Accepted.
- The checker misses the passive "were drawn" at colophon 9 (item 24).

## Also checked, and accepted

- The glossary is a definition list. Its definitions are noun-phrase
  fragments by design, so they were judged only on their full sentences
  and their clauses. The list form was not counted against them.
- Second person and present tense hold in both files. There is no "we",
  no "I", and no perfect tense. The only "you" sentences are 18, 117, and
  288. They are correct.
- The only dry turn is "the press it describes" (colophon 9). Style guide
  1.7 allows that one self-referential joke. No heading carries a joke,
  and both headings use sentence case.
- No admonitions and no footnotes in either file.
- The spellings are American. There is no "website", "email", "file name",
  "man page", "towards", "folder", or "UNIX". *book/appendices/* is a
  path. "reader site" (69, 240) is the vocabulary's own gloss for the
  Chapter edition.
- Numbers: "two", "three", "four", "five", "six", "eight", "eleven", and
  "twelve" are spelled out in prose. "19", "53", "190", "24", "225", "45",
  "300", "6.3 inches", "82 percent", "45 centimeters", versions, and
  code keep their numerals correctly. "6 by 9" is a trim measurement.
- The cross-references are italic, and each one resolves to an entry
  (plurals and possessives allowed), except *cleared leaf* (item 9).
  Filenames and directories are also italic, which is the house
  convention in style guide 2.5 (item 2).
- "not this book's closing Colophon" (84), "never with pip from Git" (93),
  and "never a page of the book" (399) are factual contrasts. They are not
  the staged "not X but Y" shape. The quoted "extends by declaration, not
  by code" (150) is press's own phrase.
- *diagrams* in colophon 9 is correct. The book's figures carry the
  `.diagram` class.
- The colophon has no link between animal and software, and its natural
  history uses the dry museum-label register, apart from items 25 and 41.

## Findings

### Blocks

1. "A packaged agent procedure that dispatches agents and runs press
   targets to check their work. Press ships four (Chapter 15)." (glossary
   435)
   Rule: wrong term (watchlist jargon "ship", one-sighting list, not in
   `jargon-allow` in this form). Severity: blocks.
   Fix: "Press carries four (Chapter 15)." This matches "The press
   carries 19" at 228.

### Should

2. "A word in italic inside an entry has its own entry." (glossary 3)
   Rule: wrong term. The sentence promises that every italic word has an
   entry, but the house sets filenames and directories in italic too
   (*art/commissions.md*, *config/aesthetic.yaml*, *dist/*, and about 30
   more), and none of them has an entry. Severity: should.
   Fix: "A term in italic inside an entry has its own entry. Filenames and
   directories are also in italic."

3. "Each edition composites it onto its own ground." (glossary 12)
   Rule: hidden actor (an edition does not act. Press does the compositing).
   Severity: should.
   Fix: "Press composites it onto the ground of each edition (Chapters 5
   and 11)."

4. "Its files meet only the *universal battery*, and heading and paragraph
   faults there are warnings." (glossary 30)
   Rule: two ideas, and hidden actor in the second clause. Severity:
   should.
   Fix: "Its files meet only the *universal battery*. The checker reports
   heading and paragraph faults there as warnings (Chapter 6)."

5. "The *drop cap* is one style of it, and the initial is the large letter
   itself." (glossary 66)
   Rule: two ideas. Severity: should.
   Fix: "The *drop cap* is one style of it. The initial is the large letter
   itself (Chapter 4)."

6. "It writes a report and touches nothing, and press compares
   fingerprints of *book/* and *config/* to prove it." (glossary 96)
   Rule: two ideas. Severity: should.
   Fix: "It writes a report and touches nothing. Press compares
   fingerprints of *book/* and *config/* to prove it (Chapter 15)."

7. "The templates in *data/defaults/* name paths with `@press/` and
   `@book/`, mark a file that may be absent with `?optional`, and render
   into *build/defaults/*." (glossary 108)
   Rule: two ideas (three verbs, two subjects), and hidden actor ("render
   into": press renders them). Severity: should.
   Fix: "The templates in *data/defaults/* name paths with `@press/` and
   `@book/` and mark a file that may be absent with `?optional`. Press
   renders them into *build/defaults/* (Chapter 7)."

8. "...trim, margins, *height cap*, typography, and Web measure." (glossary
   114)
   Rule: wrong term (the vocabulary reserves "measure" for a figure's width
   class. See its *paper column* row and the glossary's own entry at 257).
   Severity: should.
   Fix: "One of six sealed interior geometries, selected with
   `print.profile`: trim, margins, *height cap*, typography, and the width
   of the paper column. See *seal* (Chapters 1, 9, and 12)."

9. "The *placement* that gives an illustration a *cleared leaf* on an even
   page..." (glossary 177)
   Rule: wrong term. The italic says *cleared leaf* has an entry, but it
   is defined only inside *leaf* at 240. Severity: should.
   Fix: "The *placement* that gives an illustration a cleared leaf (see
   *leaf*) on an even page, facing the chapter that follows (Chapter 5)."

10. "It refuses the data kinds `.chart` and `.diagram`." (glossary 180)
    Rule: hidden actor ("It" could be the class or the command. The
    command refuses). Severity: should.
    Fix: "`press illustrate` refuses the data kinds `.chart` and
    `.diagram` (Chapter 5)."

11. "The second law ranks it above a checker and a convention." (glossary
    183)
    Rule: wrong term (the vocabulary reserves "checker" for `press check`,
    and the glossary defines it that way at 71). Severity: should.
    Fix: "The second law ranks it above a check and a convention (Chapter
    1)." If Chapter 1 quotes the law with the word "checker", keep the
    quoted word in quotation marks.

12. "On the reader site, the leaf is the paper column." (glossary 240)
    Rule: wrong term (the vocabulary's *paper column* row says never to
    call it "the leaf"). Severity: should.
    Fix: "On the reader site, the framed column of text is the paper
    column, not a leaf (Chapters 5 and 9)."

13. "Every edition but the PDF must carry it." (glossary 255)
    Rule: wrong term (use the edition's own name, glossed with its
    format). Severity: should.
    Fix: "Every edition but the Print edition (the PDF) must carry it
    (Chapter 8)."

14. "The program a print provider runs over every file it receives."
    (glossary 300)
    Rule: wrong term (*provider* is a print vendor's specification. The
    glossary says so at 318. A program is run by a print shop).
    Severity: should.
    Fix: "The program a print shop runs over every file it receives
    (Chapters 5 and 12)."

15. "The optional ordering of printed copies from the book's site."
    (glossary 309)
    Rule: era spelling ("site" for Web site). Severity: should.
    Fix: "The optional ordering of printed copies from the book's Web site
    (Chapters 8 and 12)." If the ordering lives on the Pages site, write
    "the book's Pages site".

16. "Its line must appear on exactly one reader-site page and in every
    edition" (glossary 69) against "Every edition but the PDF must carry
    it" (255).
    Fact: see fact checker. The two witness entries disagree about the
    Print edition. The writer's report-E notes the conflict for the
    manuscript witness only.

17. "*Celebrimbor's* gate as the press configures it, holding its domain
    checks and *ratchets*." (glossary 324)
    Rule: -ing rider. Severity: should.
    Fix: "The celebrimbor gate as the press configures it. It holds the
    press's domain checks and *ratchets* (Chapter 16)." This also matches
    the lowercase *celebrimbor* at 59 and the vocabulary's "the celebrimbor
    gate".

18. "Press's model takes the provider, and the publisher must confirm it."
    (glossary 363)
    Rule: two ideas. "takes the provider" is also unclear. Severity:
    should.
    Fix: "Press's model takes the provider as the seller of record. The
    publisher must confirm it (Chapter 3)."

19. "There are twelve layers in three tiers, and a release must present
    the chain complete." (glossary 417)
    Rule: two ideas. Severity: should.
    Fix: "There are twelve layers in three tiers. A release must present
    the complete chain (Chapters 14 and 16)."

20. "**edition**" (131) and "**edition manifest**" (134) come before
    "**editable install**" (137).
    Rule: alphabetical order (style guide 1.5, "alphabetical"; this rule
    is not in the contract's list). "editable" sorts before "edition" both
    letter by letter and word by word. The other 144 entries are in order.
    Severity: should.
    Fix: move the *editable install* entry (137 and 138) above *edition*
    (131).

21. "It lives in the coastal waters of the eastern Atlantic and the
    Mediterranean, and its mantle grows to about 45 centimeters."
    (colophon 7)
    Rule: two ideas (range and size). Severity: should.
    Fix: "It lives in the coastal waters of the eastern Atlantic and the
    Mediterranean. Its mantle grows to about 45 centimeters."

22. "The book was written in Markdown, and pandoc and LuaLaTeX set it
    under press 3.0.2, the press it describes." (colophon 9)
    Rule: hidden actor ("was written"), and two ideas. Severity: should.
    Fix: "The manuscript is Markdown. Pandoc and LuaLaTeX set it under
    press 3.0.2, the press it describes."

23. "The plates and the cover engraving were commissioned from an image
    model, the logomark from Gemini, and the press's own intake finished
    each one." (colophon 9)
    Rule: hidden actor ("were commissioned"), and two ideas (commission
    and intake, with a gapped middle clause). Severity: should.
    Fix: "The authors commissioned the plates and the cover engraving from
    an image model and the logomark from Gemini. The press's own intake
    finished each one." Who commissioned the art is a fact. If it was not
    the authors, see the fact checker.

24. "The diagrams were drawn with Graphviz and Pillow from scripts kept
    with the manuscript." (colophon 9)
    Rule: hidden actor (the passive ste_check missed). Severity: should.
    Fix: "Scripts kept with the manuscript drew the diagrams with Graphviz
    and Pillow."

25. "![The cuttlefish at its inkwell](...)" (colophon 3, the plate
    caption)
    Rule: register (style guide 1.7: the colophon is a museum label, with
    "no joke about the topic"). The inkwell turns the animal into a
    writer, which is a joke about the book. This rule is not in the
    contract's list. Severity: should.
    Fix: "![The common cuttlefish, *Sepia officinalis*](...)". The
    inkwell and quill in the `art:` comment and the filename are the art
    desk's call. Change them with the caption or leave them, but the
    caption should not point the joke out.

26. "...and the subtitle in Libertinus Italic." (colophon 11) after
    "Libertinus Serif" twice (9, 11).
    Rule: synonym rotation (one face, two names). Severity: should.
    Fix: "The title is set in Libertinus Serif condensed to 82 percent, and
    the subtitle in Libertinus Serif Italic." Fact: confirm the face name
    against the art report.

27. "A craft law ... The four are verbatim title and author text, flat
    covers, single-ink interiors..." (glossary 102)
    Fact: see fact checker. The press's own statement of the craft laws
    reads "verbatim text, flat plates, single-ink interiors". The
    glossary has "flat covers". This finding has no severity grade.

### May

28. "...merged over the house aesthetic." (glossary 9)
    Rule: hidden actor. Severity: may.
    Fix: "The book's visual identity in *config/aesthetic.yaml*, which
    press merges over the house aesthetic."

29. "The usage text, `press --help`, and the *desk* picker render from it."
    (glossary 57)
    Rule: hidden actor (press renders them). Severity: may.
    Fix: "Press renders the usage text, `press --help`, and the *desk*
    picker from it (Chapter 16)."

30. "must draw its declared rule" (75), "the rule a *known-bad fixture*
    must draw" (147), "must draw no diagnostic" (231).
    Rule: synonym rotation against the vocabulary, which says a fixture
    "trips its rule". "draw" is consistent inside the glossary, so this is
    rhythm, not a defect. Severity: may.
    Fix at 75: "Each *known-bad fixture* must trip its declared rule, and
    the *known-good fixture* must trip nothing." Make the same change at
    147 and 231.

31. "The whole printed cover, back, spine, and front, as one PDF page with
    bleed, a computed spine, and the *EAN-13* barcode." (glossary 99)
    Rule: rhythm (two lists in one sentence, and the comma-bounded
    apposition reads as one list). Severity: may.
    Fix: "The whole printed cover (back, spine, and front) as one PDF page
    with bleed, a computed spine, and the *EAN-13* barcode (Chapters 1 and
    12)."

32. "`press desk`, press's full-screen console" (117), "Press's default
    design" (198), "Press's model" (363) against "the press's" at 39, 60,
    84, 93, 219, 324, 351.
    Rule: synonym rotation. The vocabulary allows both forms, but one
    entry should not switch between them. Severity: may.
    Fix at 117: "`press desk`, the press's full-screen console in the
    terminal."

33. "It is not part of press 3.0.2." (glossary 165)
    Rule: era touch (style guide 8.2, "At the time of this writing" before
    any version claim). Severity: may.
    Fix: "At the time of this writing, it is not part of press 3.0.2
    (Chapter 1)."

34. "...6.3 inches on the house 6 by 9." (glossary 195)
    Rule: wrong term (the profile has a name, and the vocabulary asks for
    the `figure-cap` key to be named once). Severity: may.
    Fix: "The tallest an image may be, set per *design profile* by the
    `figure-cap` key: 6.3 inches on `house-6x9` (Chapter 5)."

35. "The workflow that proves each press tag pins itself and a resolvable
    `@sha256:` image, with a complete *trust receipt* chain." (glossary
    336)
    Rule: two ideas, and "pins itself and a resolvable image" makes the
    reader parse twice. Severity: may.
    Fix: "The workflow that proves each press tag pins itself and a
    resolvable `@sha256:` image. It also requires a complete *trust
    receipt* chain (Chapters 1 and 14)."

36. "The basename of every artifact, matching `[a-z0-9][a-z0-9-]*`, by
    default the directory given to `press new`." (glossary 375)
    Rule: -ing rider. Severity: may.
    Fix: "The basename of every artifact. It matches `[a-z0-9][a-z0-9-]*`
    and defaults to the directory given to `press new` (Chapter 3)."

37. "...so the command line never verifies one." (glossary 387)
    Rule: hidden actor (a command line does not verify). Severity: may.
    Fix: "The registry's edges make every verify target rebuild first, so
    no verify target that you run can check one (Chapters 7 and 16)."

38. "The check that opens a finished artifact and inspects it as an
    object, and its `verify_*` module." (glossary 426)
    Rule: two ideas (the check and the module, joined late). Severity:
    may.
    Fix: "A `verify_*` module, or the check it runs, which opens a finished
    artifact and inspects it as an object (Chapters 1 and 8)."

39. "The outside programs press runs: pandoc, LuaLaTeX, latexmk, the
    fonts, epubcheck, and poppler." (glossary 411)
    Rule: wrong term (fonts are not programs). Severity: may.
    Fix: "The outside programs and fonts press runs on: pandoc, LuaLaTeX,
    latexmk, the fonts, epubcheck, and poppler (Chapter 1)."

40. "A directory that holds *config/metadata.yaml* and the manuscript under
    *book/*, with the config and accepted art, and nothing else."
    (glossary 42)
    Rule: rhythm (three "and"s). Fact: see fact checker. The scaffold
    tree in Chapter 3 also lays down workflows, a CI file, a Makefile,
    and *requirements.txt*, so "nothing else" may be wrong. Severity:
    may.
    Fix (pending the fact): "A directory that holds
    *config/metadata.yaml*, the manuscript under *book/*, the rest of the
    config, and the accepted art (Chapters 1 and 3)."

41. "Under threat it releases a cloud of dark ink, and the brown pigment
    sepia takes its name from that ink." (colophon 7) together with "The
    band is sepia, and it carries the series line..." (colophon 11)
    Rule: two ideas in each sentence. Also, the two sepia sentences make
    a quiet echo between the animal and the cover. Both facts are dry and
    true, so the echo can stay. Fact: see fact checker. The pigment is
    made from the ink, but the word "sepia" is the Greek name for the
    cuttlefish itself, so "takes its name from that ink" may overstate.
    Severity: may.
    Fix: "Under threat, it releases a cloud of dark ink. The brown pigment
    sepia was first made from that ink." and "The band is sepia. It
    carries the series line, *A Workbench Handbook*, in white small
    capitals."

42. "It has eight arms and two longer feeding tentacles, and its eye has a
    W-shaped pupil." (colophon 7)
    Rule: two ideas (loosely linked anatomy). Severity: may.
    Fix: "It has eight arms and two longer feeding tentacles. Its eye has a
    W-shaped pupil."

43. "Language models drafted the text under direction from a fact base
    extracted from the press source and its documentation." (colophon 9)
    Rule: hidden actor (who directed, and who extracted). Severity: may.
    Fix: "Language models drafted the text from a fact base drawn from the
    press source and its documentation, under the authors' direction."
    Who gave the direction is a fact. Confirm it with the fact checker
    before naming an actor.

44. "A squad of editorial agents then checked the text against that fact
    base." (colophon 9)
    Rule: register ("squad" is modern and casual next to the museum-label
    paragraph above it). Severity: may.
    Fix: "A group of editorial agents then checked the text against that
    fact base."

45. The colophon as a whole (colophon 7 to 11).
    Rule: structure (style guide 1.7). The fixed form opens with the
    boilerplate sentence ("The look of Workbench books comes from
    listening to readers and from a good deal of trial and error.") and
    closes with a credit line. The colophon has the animal, interior, and
    cover paragraphs, but not the opener or the closing line. The brief
    asks for three paragraphs, so this is for the editor to decide.
    Severity: may.
    Fix: open the first paragraph with "The look of Workbench books comes
    from listening to readers and from a good deal of trial and error."

## Note for the editor

The glossary has 145 entries. Style guide 1.5 asks for about 40 to 80. The
writer reports that it was cut once already, from 4,400 words. A
copyeditor does not set length. This note is here so the editor can
decide.
