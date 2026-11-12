# Copyedit: Chapter 12, The print pack

File: `book/chapters/12-the-print-pack.md`

## Status

REVISE. Seven blocks (six watchlist sightings and two meta-narration
sightings, in seven items), 43 should, 19 may, and one sentence sent to
the fact checker. `press check` names no finding in this file. Its one
finding is the unreferenced plate `assets/woodcuts/croquet-ground.png`,
which is outside this chapter. The watchlist blocks follow the Chapter 8
precedent: `jargon-allow` lets "shipped", "canonical", "proves", and
"stale" through, but none of the four is press's own name for a thing
here, and the contract puts the watchlist on the one-sighting list.
"harmless" is on the watchlist and is not allow-listed.

Counts by severity: blocks 7, should 43, may 19, fact 1.

Most frequent rules broken: wrong term (15), two ideas (14), era
spelling (11, almost all British "colour").

Line numbers are `cat -n` line numbers in the file as it stands.

## The ste_check findings, judged

ste_check reports 46 findings (461 sentences, average 11.6 words, max 55).

- Sentence and paragraph length at 6 (the In-this-chapter list), 113 and
  294 (alt text), 115, 132, and 296 (`art:` directives), and 509 (the index
  comment): accepted. None of them is prose.
- Sentence length at 134: accepted. The footnote marker merges two short
  sentences. At 501 the length is a verbatim quotation. At 111, 166, 202,
  and 280 each sentence is at or under 30 words. 278 is a real finding
  (item 39).
- Semicolons: accepted. The hits are the art directives (132, 296), the
  quoted transparency message (315), the quoted footnote (503 counts the
  footnote block), and the index comment (509). The semicolons at 70 and
  484 are inside code. No prose semicolon.
- Perfect tense at 176 ("has mirrored margins"): accepted. "mirrored" is
  an adjective. At 334 the perfect tense is real (item 46).
- Passives at 330, 453, and 504: accepted. All are verbatim quotations.
  At 420 ("is unverified") the word is an adjective, but the sentence
  breaks condition-first (item 55). At 499 the checker flags the wrong
  words, but the sentence has a real hidden actor (item 66).
- `-ing` forms in headings and chapter titles (178, 192, 290, 422, 426),
  in the art directive (296), and in the quoted gate message (499):
  accepted. At 246 the `-ing` form is a rider (item 32).
- "therefore" (76, 82, 168), "verify" (432), "whether" (490), and "look
  at" (420): accepted under the 80 percent rule.
- "landscape" (115): accepted. It names the orientation in an art
  directive, as in Chapter 8.

Also accepted on reading:

- "centred" (359) and "colour" (80, inside the quotation from the
  profile documentation) are inside verbatim quotations.
- "honest placeholder" (266, 268, 325) is press's own name for the box,
  in its source and its verifier output. "canonical bytes" (117) is the
  phrase *docs/PROVIDER-DATA.md* uses. "commerce gate", "spine",
  `scaffold`, and the EAN-13 "parity" are literal names.
- "golden-copy geometry test" (103) is press's name for the test in
  *docs/PROFILE-LIFECYCLE.md*. It shares a name with the physical golden
  copy. Item 49 defines the physical sense, and the two read apart.
- The opener's "This chapter follows the Alice example..." (19) is within
  the style guide 8.1 allowance for an opener.
- Cross-references of the form "as the section ... later in this chapter
  explains" are accepted.
- Dry understatement appears at 51, 70, and 273, never in a heading.
  There is no "I", and no "we" in prose (the "We keep no reader data" at
  484 is inside the example). Admonitions are all imperative and under
  four sentences.

## Findings

1. "The press builds both from the same manuscript that gives you the PDF
   and the EPUB, and it inspects both before you upload them." (19)
   Rule: wrong term (the editions have names, glossed once per chapter),
   and two ideas. Severity: should.
   Fix: "The press builds both from the same manuscript that gives you the
   Print edition (PDF) and the Circulating edition (EPUB). It inspects
   both before you upload them."

2. "This chapter follows the Alice example from the first print setting
   to a copy in the post." (19)
   Rule: era spelling (British idiom). Severity: may.
   Fix: "This chapter follows the Alice example from the first print
   setting to a copy in the mail."

3. "The house geometry with a colour interior. Only KDP cuts it in
   colour." (62, Table 12.2)
   Rule: era spelling (American "color"; the book's code, tables 12.7 and
   12.9, and "grayscale" at 280 are all American). Severity: should.
   Fix: "The house geometry with a color interior. Only KDP cuts it in
   color."

4. "Table 12.2 lists the six profiles that press 3.0.2 carries, with the
   providers that cut each trim." (57)
   Rule: era touch ("At the time of this writing" before a version
   claim, style guide 8.2). Severity: may.
   Fix: "At the time of this writing, press 3.0.2 carries six profiles.
   Table 12.2 lists them, with the providers that cut each trim."

5. "The sealed house default." / "A short novel or a novella." /
   "Trade-paperback genre fiction." / "A rack-sized genre paperback." /
   "Large print, for accessibility." (61 to 66, Table 12.2)
   Rule: rhythm (style guide 3.7: Meaning cells hold sentences, not
   fragments). Severity: may.
   Fix, for example: "It is the sealed house default." / "It suits a
   short novel or a novella." / "It suits trade-paperback genre
   fiction." / "It is a rack-sized genre paperback." / "It is large
   print, for accessibility."

6. "It also keeps plates in colour at intake instead of greying them."
   (80)
   Rule: era spelling. Severity: should.
   Fix: "It also keeps plates in color at intake instead of graying them."

7. "A colour interior has one more requirement, ..." and the paragraph
   after it (82: "colour" five times)
   Rule: era spelling. Severity: should.
   Fix: "A color interior has one more requirement, and it comes from the
   spine. The spine width rests on a *caliper*, the thickness of one page
   of the stock, and a color interior needs a caliper for color stock.
   The color profile must therefore pair with a provider that documents a
   color caliper, and at the time of this writing only KDP does. At Lulu
   and at IngramSpark, the press refuses a color interior. The ledger
   holds no sourced color caliper for either provider, and the press will
   not guess a thickness."

8. "Do not plan a colour interior for Lulu or IngramSpark. The press
   refuses the combination because it has no sourced colour caliper for
   either provider, and a guessed spine is a cover that does not fit."
   (85, Warning)
   Rule: era spelling, and an admonition that repeats the paragraph above
   it (style guide 8.1). Severity: should.
   Fix: "Do not plan a color interior for Lulu or IngramSpark. A guessed
   spine is a cover that does not fit."

9. "Authors choose among the six profiles." (90)
   Rule: second person (brief). Severity: should.
   Fix: "You choose among the six profiles."

10. "The tool takes four subcommands:" (90)
    Rule: wrong term (no tool has been named; the block is the
    `press.profile_lifecycle` module). Severity: should.
    Fix: "The `press.profile_lifecycle` module takes four subcommands:"

11. "Scaffold it from geometry that is already proven." (102)
    Rule: hidden actor. Severity: may.
    Fix: "Scaffold it from an existing profile whose geometry the press
    has already sealed." If that adds a fact, then: "Scaffold it from an
    existing profile."

12. "The test renders every shipped profile at its declared trim." (103)
    Rule: watchlist jargon ("ship", one-sighting list). Severity: blocks.
    Fix: "The test renders every profile that the press carries at its
    declared trim."

13. "The provider decides how wide the spine is, how far the bleed runs,
    and how the wrap is laid out around the boards." (109)
    Rule: hidden actor. Severity: should.
    Fix: "The provider decides how wide the spine is, how far the bleed
    runs, and how the press lays out the wrap around the boards."

14. "...with a thin bleed border round the outside..." (113, alt text)
    Rule: era spelling (British "round"). Severity: may.
    Fix: "...with a thin bleed border around the outside..."

15. "*docs/PROVIDER-DATA.md* gives the rule in four words: "Never edit it
    by hand."" (117)
    fact: see fact checker (the quotation has five words).

16. "Its calipers are KDP's white and cream figures, and it refuses
    nothing, because it has no catalog of trims or bindings to check
    against." (134)
    Rule: two ideas, and wrong term ("the catalog" is reserved for the
    typed command table). Severity: should.
    Fix: "Its calipers are KDP's white and cream figures. It refuses
    nothing, because it keeps no list of trims or bindings to check
    against."

17. "The house provider takes `perfect-bound`, `saddle-stitch`, and
    `coil`, and it has no catalog, so it refuses no trim or page count."
    (155, Table 12.3)
    Rule: wrong term ("catalog"), and two ideas. Severity: should.
    Fix: "The house provider takes `perfect-bound`, `saddle-stitch`, and
    `coil`. It keeps no list of trims or page counts, so it refuses
    none."

18. "...as `casewrap` or `dust-jacket`, on 9 trims." (158, Table 12.3)
    Rule: numbers under ten spelled out (brief). Severity: should.
    Fix: "...as `casewrap` or `dust-jacket`, on nine trims."

19. "...and the ledger marks that formula as "OFFICIAL"." (162)
    Rule: wrong term (no formula is named in the sentence; the reader
    must infer it). Severity: may.
    Fix: "IngramSpark's casewrap takes a margin of 0.625in and a hinge of
    0.5in, and the ledger marks IngramSpark's casewrap formula as
    "OFFICIAL"."

20. "The stock matters for two of the four shapes." (166) beside "a Lulu
    paper that does not match your `print.paper`" (465)
    Rule: synonym rotation ("stock" and "paper" for one thing). Severity:
    may.
    Fix: keep "stock" for the physical sheet and "paper" only for the
    `print.paper` key, as at 166: "The paper setting matters for two of
    the four shapes." At 465: "a Lulu stock that does not match your
    `print.paper`".

21. "A book bound for a Lulu paperback should therefore set
    `print.provider` to `lulu`, and the guide does not say so." (168)
    Rule: two ideas, and second person. Severity: should.
    Fix: "For a Lulu paperback, you should therefore set `print.provider`
    to `lulu`. The guide does not say so."

22. "The print interior and the reading PDF come from the same
    manuscript, but they are different artifacts. The reading PDF is for
    a screen. The print interior, *dist/alice-interior.pdf*, is for a
    press." (176)
    Rule: wrong term ("the reading PDF" is the Print edition; "a press"
    collides with the press). Severity: should.
    Fix: "The print interior and the Print edition come from the same
    manuscript, but they are different artifacts. The Print edition is
    for a screen. The print interior, *dist/alice-interior.pdf*, is for a
    printing press."

23. "In every other book, a green `press all` says nothing about the
    print pack." (186) and the Tip's "Unless the book enables print
    ordering, a passing `press all` never opened the interior or the
    wrap." (189)
    Rule: one-line closer (repeats the paragraph's first sentence), and
    an admonition that repeats the paragraph above it (style guide 8.1).
    Severity: should.
    Fix: delete the closer at 186, and cut the Tip to "Run `press
    verify-print` before every upload to a print shop."

24. "It builds every edition a reader downloads, and it verifies them,
    but the print pack has its own targets." (186)
    Rule: two ideas. Severity: should.
    Fix: "It builds and verifies every edition a reader downloads. The
    print pack has its own targets."

25. "The print verifier fails a single-ink interior that carries colour,
    and one source of colour is code." (192)
    Rule: two ideas, and era spelling. Severity: should.
    Fix: "The print verifier fails a single-ink interior that carries
    color. One source of color is code."

26. "A fence with a language tag gets syntax highlighting, and the
    highlighting prints in coloured ink." (192)
    Rule: era spelling ("fence" is also modern Markdown slang).
    Severity: should.
    Fix: "A code block with a language tag gets syntax highlighting, and
    the highlighting prints in colored ink."

27. "Another source is a coloured cover plate in a hand-written
    *tex/title-page.tex*. That plate belongs on the wrap, and a book can
    supply *tex/title-page-print.tex* without it for the print interior."
    (192)
    Rule: era spelling, and second person. Severity: should.
    Fix: "Another source is a colored cover plate in a hand-written
    *tex/title-page.tex*. That plate belongs on the wrap, and you can
    supply *tex/title-page-print.tex* without it for the print interior."

28. "...and without it the target stops with `coverwrap needs
    assets/cover.jpg`." (198)
    Rule: wrong term (the press stopping with a message is a refusal).
    Severity: should.
    Fix: "It needs the cover art at *assets/cover.jpg*, and without it the
    press refuses the target with `coverwrap needs assets/cover.jpg`."

29. "**Example 12.3. The cover wrap layout, from gen_coverwrap**" (204);
    also "Table 12.5. The verify_coverwrap checks, in order" (313),
    "**Example 12.5. The verify_coverwrap success line**" (319), and
    "**Example 12.6. A passed inspection in config/qualification.yaml**"
    (371)
    Rule: code typography (style guide 4: literal code in constant width;
    the body sets these names in code and the path in italic). Severity:
    may.
    Fix: "The cover wrap layout, from `gen_coverwrap`"; "The
    `verify_coverwrap` checks, in order"; "The `verify_coverwrap` success
    line"; "A passed inspection in *config/qualification.yaml*".

30. "The margin of a paperback is the bleed, and the press fixes the
    bleed at `BLEED_IN = 0.125`, which the source calls "universal across
    print vendors"." (214)
    Rule: two ideas. Severity: should.
    Fix: "The margin of a paperback is the bleed. The press fixes the
    bleed at `BLEED_IN = 0.125`, which the source calls "universal across
    print vendors"."

31. "On a printed cover, the press lays down a cloth-coloured field..."
    (234)
    Rule: era spelling. Severity: should.
    Fix: "On a printed cover, the press lays down a cloth-colored field in
    `black!85!red!25!white`, which is RGB (201,191,191)."

32. "The press computes it from the first twelve digits, weighting them
    1, 3, 1, 3, and so on from the left." (246)
    Rule: -ing rider. Severity: should.
    Fix: "The press computes it from the first twelve digits. It weights
    them 1, 3, 1, 3, and so on from the left."

33. "Example 12.4 works the press's own canonical example, the ISBN
    978-0-306-40615-7, through the formula." (246) and the footnote "The
    number 978-0-306-40615-7 is the selftest's canonical example." (505)
    Rule: watchlist jargon ("canonical", one-sighting list; here it is
    not press's own name). The footnote also only repeats the body.
    Severity: blocks.
    Fix: "Example 12.4 works the ISBN that the press's selftest checks,
    978-0-306-40615-7, through the formula." Delete the `[^isbn]`
    footnote.

34. "The three guard groups make 11 modules, and each of the twelve
    encoded digits takes 7, which accounts for all 95." (258)
    Rule: numbers under ten spelled out (brief). Severity: should.
    Fix: "The three guard groups make 11 modules, and each of the twelve
    encoded digits takes seven, which accounts for all 95."

35. "The first digit is not drawn as bars." (258)
    Rule: hidden actor. Severity: should.
    Fix: "The press draws no bars for the first digit."

36. "The check digit proves only that the number is well formed, and
    nobody can correct a cover printed with the wrong book's ISBN." (263,
    Warning)
    Rule: watchlist jargon ("proves", one-sighting list). Severity:
    blocks.
    Fix: "The check digit shows only that the number is well formed, and
    nobody can correct a cover printed with the wrong book's ISBN."

37. "The wrap verifier measured the quiet zones and refused the wrap, so
    `press verify-print` failed on a correct cover." (273, sidebar)
    Rule: wrong term (a verifier result is "fail"; "refuse" is reserved
    for the press stopping with a message). Severity: should.
    Fix: "The wrap verifier measured the quiet zones and failed the wrap,
    so `press verify-print` failed on a correct cover."

38. The sidebar body (273) is one paragraph of nine sentences.
    Rule: rhythm (six sentences at most per paragraph). Severity: may.
    Fix: break the paragraph after "...unless you tell it otherwise." so
    the cause and the fix stand in two paragraphs.

39. "A provider runs a *preflight* over every file it receives, and a
    preflight flags two things that the reading editions do not care
    about: transparency, and more pixels than the page can use." (278)
    Rule: sentence over 30 words (33), and two ideas. Severity: should.
    Fix: "A provider runs a *preflight* over every file it receives. The
    preflight flags two things that the reading editions do not care
    about: transparency, and more pixels than the page can use."

40. "The print pack passes every image through a *print-safe* pass before
    it goes onto paper." (278)
    Rule: hidden actor (the print pack is a set of artifacts and cannot
    act; "it" is also ambiguous). Severity: should.
    Fix: "The press passes every image through a *print-safe* pass before
    the image goes onto paper."

41. "Chapter 5, *Figures and plates*, describes the pass for the
    interior, and this section adds the cover." (278)
    Rule: meta-narration. Graded should, not blocks, because the clause
    carries a cross-reference. Severity: should.
    Fix: "Chapter 5, *Figures and plates*, describes the pass for the
    interior. The cover goes through the same pass, with its own caps."

42. "It writes a JPEG at quality 88 and writes every other image as a
    PNG." (280)
    Rule: wrong term (ambiguous: a JPEG source, or a JPEG for some other
    class of image?). Severity: may. Confirm the meaning with the fact
    checker before you fix it.
    Fix, if the reading is "a JPEG source stays a JPEG": "It writes a
    JPEG source back as a JPEG at quality 88, and every other image as a
    PNG."

43. "Lulu once flagged a press interior for transparency, since the
    logomark is ink on transparency." (284)
    Rule: synonym rotation ("logo" everywhere else, including the next
    sentence). Severity: should.
    Fix: "Lulu once flagged a press interior for transparency, since the
    logo is ink on transparency."

44. "Each verifier in it reads the artifact that the stage before it
    built." (292)
    Rule: wrong term ("stage" is on the never list for target).
    Severity: should.
    Fix: "Each verifier in it reads the artifact that the box before it
    builds."

45. "The press keeps that second question apart from the first, and it
    starts with a plain statement in *docs/PROVIDER-QUALIFICATION.md*:
    ..." (330)
    Rule: two ideas. Severity: should.
    Fix: "The press keeps that second question apart from the first. It
    starts with a plain statement in *docs/PROVIDER-QUALIFICATION.md*: "A
    provider here is *researched*, not *qualified*.""

46. "The ledger gives every provider it has studied a *disposition*, ..."
    (334)
    Rule: perfect tense (and a ledger does not study). Severity: should.
    Fix: "The ledger gives each researched provider a *disposition*, one
    of `primary`, `secondary`, `hosted-candidate`, `candidate`, or
    `not-fit`."

47. "One capability matters for the last section of this chapter. The
    ledger records Lulu as `unsupported` there, ..." (347)
    Rule: wrong term (the capability is never named; "there" points at
    nothing). Severity: should.
    Fix: "One capability, `seller_of_record`, matters for the last section
    of this chapter. The ledger records Lulu as `unsupported` for it, with
    the note that "the publisher is the seller in the custom route"."

48. "The ledger is the reviewed source, and it does not support that
    claim, so this book does not repeat it." (347)
    Rule: meta-narration ("text about the document itself", one-sighting
    list), and two ideas. Severity: blocks.
    Fix: "The ledger is the reviewed source, and it does not support that
    claim. We do not repeat it."

49. "Qualification means one physical copy, in your hands, inspected
    against a fixed list." (351)
    Rule: wrong term ("golden copy" names the section and returns at 424
    and 428, but the chapter never defines it). Severity: should.
    Fix: "Qualification means one physical copy, the *golden copy*, in
    your hands, inspected against a fixed list."

50. "Each of these is a candidate." / "Each of these is not fit." /
    "It is not fit, because it has a 10-copy minimum." (341 to 343,
    Table 12.6)
    Rule: rhythm ("is not fit" reads as broken English; the disposition is
    a value). Severity: may.
    Fix: "Each of these is a `candidate`." / "Each of these is
    `not-fit`." / "It is `not-fit`, because it has a 10-copy minimum."

51. `inspector: "Your Name"` (380, Example 12.6)
    Rule: era touch (style guide 8.2: names from the fixed cast).
    Severity: may.
    Fix: `inspector: "alice"`, or set the placeholder as replaceable text
    if the house filter can italicize it.

52. "The choice of inputs decides when a copy goes stale." (399)
    Rule: watchlist jargon ("stale", one-sighting list; press uses it for
    artifacts, not for a physical copy). Severity: blocks.
    Fix: "The choice of inputs decides when an inspection stops holding."

53. "The edition manifest that carries the id may not hold anything that
    looks like money or a person." (401)
    Rule: honest modals ("may not" for a prohibition). Severity: should.
    Fix: "The edition manifest that carries the id must not hold anything
    that looks like money or a person."

54. "It then writes the checklist to *dist/publish-kdp.md* or
    *dist/publish-ingram.md*, in three sections." (411)
    Rule: wrong term ("It" follows "They", the artifacts). Severity: may.
    Fix: "The target then writes the checklist to *dist/publish-kdp.md*
    or *dist/publish-ingram.md*, in three sections."

55. "The target exits with status 1 if any artifact is unverified."
    (420); the `[^kdpdate]` footnote hangs on the unrelated sentence "It
    is not a substitute for the full run before an upload."
    Rule: rhythm (condition first), and a misplaced footnote. Severity:
    may.
    Fix: "If any artifact fails its verifier, the target exits with
    status 1." Move `[^kdpdate]` to the KDP row of Table 12.3 (156),
    where the KDP figures are.

56. "There are two kinds of order in this chapter." (424)
    Rule: meta-narration ("text about the document itself", one-sighting
    list). Severity: blocks.
    Fix: "A press book meets two kinds of order."

57. "*docs/LULU.md* gives the procedure for a Lulu paperback, and it is
    the route to the golden copy." (428)
    Rule: two ideas. Severity: may.
    Fix: "*docs/LULU.md* gives the procedure for a Lulu paperback. It is
    the route to the golden copy."

58. "Leave Lulu's own barcode off when `registrations.isbn.print` is
    set." (436, step 5)
    Rule: hidden actor, and condition first. Severity: should.
    Fix: "If you set `registrations.isbn.print`, leave Lulu's own barcode
    off."

59. The Warning at 449 to 451 ("Do not let Lulu add its own barcode...
    The press has drawn the EAN-13 from `registrations.isbn.print`, and a
    second barcode on the back panel is a defect on every copy.")
    Rule: perfect tense, and a warning after the step it protects (it
    follows the procedure and Table 12.9, and repeats step 5). Severity:
    should.
    Fix: move the Warning above "To print the Alice example at Lulu:"
    and write its second sentence as "The press draws the EAN-13 from
    `registrations.isbn.print`, and a second barcode on the back panel is
    a defect on every copy."

60. "Order one copy, inspect it against the eleven points, and record the
    result in *config/qualification.yaml*." (437, step 6)
    Rule: rhythm (style guide 3.6: each step a single imperative).
    Severity: may.
    Fix: split into "6. Order one copy and inspect it against the eleven
    points." and "7. Record the result in *config/qualification.yaml*."

61. "Set it to Black and white." / "Choose Glossy or Matte, as you
    prefer." (443, 445, Table 12.9)
    Rule: code typography (step 2 sets Lulu's interface labels in bold;
    these are not). Severity: may.
    Fix: "Set it to **Black and white**." / "Choose **Glossy** or
    **Matte**, as you prefer."

62. "That note is harmless, and you can ignore it." (453)
    Rule: watchlist jargon ("harmless", one-sighting list; not
    allow-listed). Severity: blocks.
    Fix: "You can ignore that note."

63. "The guide also lists an off-centre spine..." (465)
    Rule: era spelling. Severity: should.
    Fix: "The guide also lists an off-center spine and gives the cause as
    a Lulu paper that does not match your `print.paper`."

64. "A Lulu paperback with `print.provider` set to `lulu` computes the
    same spine on either stock, so check the provider setting before you
    check the paper." (465)
    Rule: hidden actor (a paperback computes nothing; the press does),
    and two ideas. Severity: should.
    Fix: "For a Lulu paperback with `print.provider` set to `lulu`, the
    press computes the same spine on either stock. Check the provider
    setting before you check the paper."

65. "a value shaped like a secret, such as `sk_live`, `bearer` followed by
    sixteen or more characters, or `?token=`" (496); also "the first
    twelve digits" (246) beside "11 modules" (258) and "11 capabilities"
    (334) beside "the eleven points" (349, 437)
    Rule: rhythm (numbers of ten and over appear both as words and as
    numerals; 74 has "16 hexadecimal characters"). Severity: may.
    Fix: "`bearer` followed by 16 or more characters". Pick numerals for
    ten and over, except where "eleven" is part of the checklist's name.

66. "The last stage of `press all` is the commerce gate." (499)
    Rule: wrong term ("stage"). Severity: should.
    Fix: "`press all` ends with the commerce gate."

67. "The gate is advisory unless `PRESS_RELEASE=1` is set, as it is when
    CI builds a release tag." (499)
    Rule: hidden actor. Severity: should.
    Fix: "The gate is advisory unless the environment sets
    `PRESS_RELEASE=1`, as CI does when it builds a release tag."

68. "A custom merchant-of-record stack, with a broker, checkout,
    webhooks, and reconciliation, sits in the Icebox, and
    *docs/DIRECT-ORDERING-PLAN.md* holds the plan." (501)
    Rule: two ideas, and wrong term ("the Icebox" is never defined; the
    reader meets a roadmap bucket by name only). Severity: should.
    Fix: "A custom merchant-of-record system, with a broker, checkout,
    webhooks, and reconciliation, sits in the Icebox of the press's
    roadmap, with no release planned. *docs/DIRECT-ORDERING-PLAN.md*
    holds the plan." (Confirm "with no release planned" with the fact
    checker, or gloss the Icebox in the press's own words.)

69. "The ISBN that the barcode, the checklist, and the manifest all carry
    comes from your registrations, and Chapter 13, *Registrations*,
    covers that paperwork." (501)
    Rule: two ideas. Severity: should.
    Fix: "The barcode, the checklist, and the manifest all carry the ISBN
    from your registrations. Chapter 13, *Registrations*, covers that
    paperwork."

70. "...a provider-neutral order contract and a Lulu Print API adapter
    under *src/press/providers/*." (507, footnote)
    Rule: noun stack (four nouns). Severity: may.
    Fix: "The press repository does contain a provider-neutral order
    contract and an adapter for Lulu's Print API, under
    *src/press/providers/*."
