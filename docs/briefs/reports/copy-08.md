# Copyedit: Chapter 8, Verifying the artifacts

File: `book/chapters/08-verifying-the-artifacts.md`

## Status

REVISE. Three blocks (watchlist jargon, one-sighting list), 19 should,
13 may, and two sentences referred to the fact checker. `press check`
names no finding in this file. Its 23 findings are all in other chapters.
The three blocks are watchlist terms that the house `jargon-allow` list
lets through ("lands", "ship", "surface"). They are on the contract's
one-sighting list, and none of the three is press's own name for a
thing, so the checker's silence does not clear them. This follows the
Chapter 4 precedent.

Counts by severity: blocks 3, should 19, may 13.

Most frequent rules broken: hidden actor (6), then two ideas (4) and
wrong term (4).

Line numbers are `grep -n` line numbers in the file as it stands.

## The writer's ste_check defences, judged

- Passives at 24 and 26 in ste numbering (the third law, CONTRIBUTING)
  and at 428 (ARCHITECTURE): accepted. All are verbatim quotations.
- Semicolons: accepted. The hits are the plate directive (20), the
  quoted CLAUDE.md scar (407), the quoted `INV-graph-no-stale` limit
  (430), and the index comment (496). The semicolon at 128 is inside a
  code span. No prose semicolon.
- Paragraph and sentence length on the `art:` directives and the index
  comment: accepted. ste_check misses one prose sentence over 30 words
  because it sits in an admonition (item 4). No other prose sentence
  exceeds 30 words. The quoted passages at 27 and 303 run long only
  because of their verbatim quotations.
- "therefore", "verify", "look at", "find out", and `-ing` forms in
  headings and gerunds: accepted under the 80 percent rule.
- "landscape" (20): accepted. It names the orientation in an art
  directive, which the reader never sees, and it is not the assistant
  word's sense.
- "appendices" (428): accepted. It is inside a verbatim quotation of
  *docs/ARCHITECTURE.md*.

The checker does not catch the items below. They come from reading
every sentence.

## Findings

1. "The second means that the links point at pages, but the pages hold
   no image, so the reader lands on the wrong leaf." (128)
   Rule: watchlist jargon ("lands", one-sighting list). Severity: blocks.
   Fix: "The second means that the links point at pages, but the pages
   hold no image, so the reader arrives on the wrong leaf."

2. "The toolchain image now ships a plain `java -jar` wrapper, and the
   verifier reports the case as `epubcheck is present but cannot run
   (<exc>); the toolchain image is broken`." (303)
   Rule: watchlist jargon ("ship", one-sighting list). Severity: blocks.
   Fix: "The toolchain image now carries a plain `java -jar` wrapper, and
   the verifier reports the case as `epubcheck is present but cannot run
   (<exc>); the toolchain image is broken`."

3. "Every surface must carry an Open Graph title and a Twitter card, and
   the `og:image` must resolve." (356)
   Rule: watchlist jargon ("surface", one-sighting list). Severity:
   blocks. ("public reading surface" at 354 and 386 stays, because it is
   the phrase in the verifier's own success line.)
   Fix: "Every published page must carry an Open Graph title and a
   Twitter card, and the `og:image` must resolve."

4. "The house design caps every image at a height that depends on the
   profile (6.3in on the house 6 by 9) because a taller figure once made
   LuaLaTeX emit empty pages forever." (153, Warning)
   Rule: sentence over 30 words (32). Severity: should.
   Fix: "The house design caps every image at a height that depends on the
   profile (6.3in on the house 6 by 9). The cap exists because a taller
   figure once made LuaLaTeX emit empty pages forever."
   (The Warning stays at three sentences.)

5. "The self-test is an *invariant*, an entry in the press's ledger of
   named, enforced guarantees." (90)
   Rule: wrong term (vocabulary: invariant, never "guarantee").
   Severity: should.
   Fix: "The self-test is an *invariant*, a named entry in the press's
   ledger of properties that the press enforces."

6. "The press's CLAUDE.md kept the lesson as an instruction: "When
   touching PDF links, verify destinations with pypdf"." (135, sidebar)
   Rule: wrong term (vocabulary: scar, never "lesson"). Severity: should.
   Fix: "The press's CLAUDE.md kept the scar as an instruction: "When
   touching PDF links, verify destinations with pypdf"."

7. "The verifier skips the first 20 percent of the pages, where the front
   matter would confuse the measure." (162)
   Rule: wrong term ("measure" is the book's term for the width class).
   Severity: should.
   Fix: "The verifier skips the first 20 percent of the pages, where the
   front matter would confuse the measurement."

8. "The print interior must have mirrored margins and, unless the profile
   allows colour, black ink only." (70, Table 8.2)
   Rule: era spelling (American spelling). Severity: should.
   Fix: "The print interior must have mirrored margins and, unless the
   profile allows color, black ink only."

9. "The second check concerns colour. A page fails when more than 200 of
   its pixels have an RGB channel spread of 48 or more, which means that
   a reader sees colour in them." (169)
   Rule: era spelling (American spelling), twice. Severity: should.
   Fix: "The second check concerns color. A page fails when more than 200
   of its pixels have an RGB channel spread of 48 or more, which means
   that a reader sees color in them."
   (The art directive at 463, "No colour", is the illustrator's text; the
   art desk may want "No color" for consistency.)

10. "Under `PRESS_RELEASE`, the book must declare at least 2 sentinels
    and a page floor of at least 24." (60, Table 8.2)
    Rule: numbers under ten spelled out in prose. Severity: should.
    Fix: "Under `PRESS_RELEASE`, the book must declare at least two
    sentinels and a page floor of at least 24."

11. "It cuts the line into windows of 8 consecutive words, with a new
    window every 4 words." (394)
    Rule: numbers under ten spelled out in prose (footnote 494 already
    says "four words"). Severity: should.
    Fix: "It cuts the line into windows of eight consecutive words, with a
    new window every four words."

12. "The verifier folds its case, because the title page sets it in
    capitals, so `ALICE'S ADVENTURES IN WONDERLAND` on the title page
    satisfies the check." (114)
    Rule: two ideas (a cause and a consequence in one sentence).
    Severity: should.
    Fix: "The verifier folds its case, because the title page sets it in
    capitals. `ALICE'S ADVENTURES IN WONDERLAND` on the title page
    therefore satisfies the check."

13. "A chapter missing from every page fails with `reader site is missing
    <chapter>:` and a chapter on two pages fails with `reader site
    duplicates <chapter>:`, each followed by the details." (258)
    Rule: two ideas (two failures, two messages, and no comma at the
    join). Severity: should.
    Fix: "A chapter missing from every page fails with `reader site is
    missing <chapter>:` and the details. A chapter on two pages fails
    with `reader site duplicates <chapter>:` and the details."

14. "The configuration model defaults `verify-min-pages` to 40, but the
    template that `press new` writes sets it to 1, and the sentinel list
    starts empty." (388)
    Rule: two ideas (the page floor and the sentinel list). Severity:
    should.
    Fix: "The configuration model defaults `verify-min-pages` to 40, but
    the template that `press new` writes sets it to 1. The sentinel list
    starts empty."

15. "Search the manuscript for it, and if the checker also fails on it,
    the manuscript is the culprit." (466)
    Rule: two ideas (a command fused with a condition; procedure apart
    from description). Severity: should.
    Fix: "Search the manuscript for it. If the checker also fails on it,
    the manuscript is the culprit."

16. "When every edition passes, the verifier checks agreement across
    editions, as described in the section "Witnesses and cross-edition
    agreement" later in this chapter." (260)
    Rule: hidden actor ("as described"). Severity: should.
    Fix: "When every edition passes, the verifier checks agreement across
    editions, as the section "Witnesses and cross-edition agreement"
    later in this chapter describes."

17. "Inside the toolchain image, where releases are cut, a missing
    epubcheck is a fault in the image." (284)
    Rule: hidden actor ("are cut"). Severity: should. (The same words in
    the quoted message at 289 are verbatim and stay.)
    Fix: "Inside the toolchain image, where CI cuts releases, a missing
    epubcheck is a fault in the image."

18. "The canonical link must be present exactly when `site-url` is set in
    *config/metadata.yaml*. ... When `site-url` is set, the sitemap must
    exist, ..." (356)
    Rule: hidden actor ("is set", twice). Severity: should.
    Fix: "The canonical link must be present exactly when the book sets
    `site-url` in *config/metadata.yaml*. ... When the book sets
    `site-url`, the sitemap must exist, ..."

19. "When `pdftotext` exists, it still reads whatever *dist/alice.pdf* is
    present into the agreement check." (416)
    Rule: hidden actor ("it" could be `pdftotext` or the target).
    Severity: should.
    Fix: "When `pdftotext` exists, the target still reads whatever
    *dist/alice.pdf* is present into the agreement check."

20. "Under `PRESS_RELEASE` it enforces." (424)
    Rule: hidden actor ("enforces" with no object, and "it" is the
    gate, not the actor). Severity: should.
    Fix: "Under `PRESS_RELEASE`, the press enforces it."

21. "The source gives the reason: keying on `CI` would fail "because
    `CI=false` would read as truthy"." (297)
    Rule: wrong term (vocabulary: "the source" is never used for a set of
    files; here the reader may take it for the manuscript). Severity:
    should.
    Fix: "The press's own code gives the reason: keying on `CI` would fail
    "because `CI=false` would read as truthy"."

22. "Four messages can come back from this step:" (94)
    Rule: synonym rotation ("step" is a word the vocabulary keeps out;
    the chapter calls these "checks" everywhere else). Severity: should.
    Fix: "Four messages can come back from this check:"
    (The same holds for "the epubcheck step" at 282, Table 8.4's caption,
    and at 438. Fix: "Table: Table 8.4. The outcomes of the epubcheck
    run" and "A message that names `epubcheck` comes from the epubcheck
    run, and `landing page` comes from `verify_pages`.")

23. "Later on, the verifier must decide for every rendered page if it is
    blank." (81)
    Rule: rhythm ("whether" is period-correct and the precise word).
    Severity: may.
    Fix: "Later on, the verifier must decide for every rendered page
    whether it is blank."

24. "Next, decide if the fault lies in the book or in the machine." (440)
    Rule: rhythm (as item 23). Severity: may.
    Fix: "Next, decide whether the fault lies in the book or in the
    machine."

25. "A printed book has a wider margin at the gutter, so the text block
    sits further right on a recto than on a verso." (162)
    Rule: era spelling (American usage: "farther" for distance).
    Severity: may.
    Fix: "A printed book has a wider margin at the gutter, so the text
    block sits farther right on a recto than on a verso."

26. "That verifier checks one page whose size equals the generator's own
    layout within 0.01in, embedded fonts, the title as text, and the
    barcode, among other things." (177)
    Rule: rhythm (the list is not parallel, so "one page whose size
    equals ... embedded fonts" reads as one noun phrase). Severity: may.
    Fix: "Among other things, that verifier checks for a single page, a
    page size within 0.01in of the generator's own layout, embedded
    fonts, the title as text, and the barcode."

27. "The edge check looks at a border 2 pixels wide around each page and
    fails any page where one pixel there is darker than 245." (150)
    Rule: rhythm ("one pixel" can read as "exactly one"). Severity: may.
    Fix: "The edge check looks at a border 2 pixels wide around each page
    and fails any page where any pixel in that border is darker than
    245."

28. "An edition that lost it fails with this message, which quotes the
    first 60 characters of the line:" (214)
    Rule: present tense throughout. Severity: may.
    Fix: "An edition that loses it fails with this message, which quotes
    the first 60 characters of the line:"

29. "`verify_formats` checks every edition except the PDF, and it ends by
    checking that all the editions, the PDF included, agree with the
    manuscript." (206)
    Rule: rhythm (an -ing chain, "by checking"). Severity: may.
    Fix: "`verify_formats` checks every edition except the PDF. Its last
    check confirms that all the editions, the PDF included, agree with
    the manuscript."

30. "The EPUB check reports the same comparison for the EPUB." (236)
    Rule: rhythm ("EPUB" twice in eight words). Severity: may.
    Fix: "The EPUB message reports the same comparison."

31. "The ledger names this invariant `INV-archive-source-policy`, and
    marks it critical. ... a mode of 0o755 or 0o644, and deflate level
    9." (315, 319)
    Rule: synonym rotation ("DEFLATE" at 315, "deflate" at 319) and a
    stray comma before the second verb. Severity: may.
    Fix: "The ledger names this invariant `INV-archive-source-policy` and
    marks it critical." and "... a mode of 0o755 or 0o644, and DEFLATE
    level 9."

32. "The ledger enforces it as `INV-graph-no-stale`, marked critical."
    (407)
    Rule: hidden actor (the participle "marked"; 212 and 315 name the
    actor). Severity: may.
    Fix: "The ledger enforces it as `INV-graph-no-stale` and marks it
    critical."

33. "epubcheck is optional on a workstation, as the section "epubcheck"
    described, so its absence does not stop a local run." (459)
    Rule: rhythm (a sentence that opens on a lowercase tool name, set in
    roman, reads as a typo in print). Severity: may.
    Fix: "The epubcheck tool is optional on a workstation, as the section
    "epubcheck" described, so its absence does not stop a local run."

34. "When `PRESS_RELEASE=1`, the press requires at least two sentinels
    and a page floor of at least 24." (388)
    Rule: rhythm (an assignment used as a clause). Severity: may.
    Fix: "When `PRESS_RELEASE` is `1`, the press requires at least two
    sentinels and a page floor of at least 24."

35. "The witness that could say no, inspecting a finished sheet" (19,
    plate caption)
    Rule: -ing rider. Severity: may. The writer moved the plate line
    unchanged, so this one belongs to the art desk.
    Fix: "The witness that could say no, at a finished sheet" or leave as
    the plate's title.

## Referred to the fact checker

- "Without `pdfimages`, two checks soften to notes, and a note is easy to
  miss in a long run." (191, Tip) Fact: see fact checker. The body (188)
  describes one check that softens to a note. The writer's report says
  only the cover check softens.
- "It is the one target that rebuilds every edition and runs every
  verifier over the results, so its agreement check compares editions of
  the same manuscript." (419, Tip) Fact: see fact checker. Lines 424 and
  426 say `press all` runs four verifiers, not `verify_coverwrap`, and
  builds neither the print interior nor the cover wrap.

## Other checks

- Second person and present tense: held throughout, except item 28.
- "we": no use. "I": no use.
- Dry understatement: "an e-mail later" (300), "One more rule protects
  you from yourself" (324), "does not pretend it checked the links
  either" (128), "which a single book never should" (150). They are
  spaced through the chapter, and none is in a heading.
- Admonitions: four tips and three warnings. All are imperative, and all
  run to three sentences or fewer (the item 4 fix keeps the Warning at
  three).
- Footnotes: all four carry asides (a scar's history, shell semantics,
  why the timestamp is fixed, window arithmetic). The body does not
  depend on any of them.
- Spellings: "Web site" (341) and "e-mail" (300) are correct. No
  "website", "email", "file name", "man page", "UNIX", or "towards".
  "colour" is items 8 and 9.
- Headings: sentence case throughout. No title case.
- No em or en dashes. The `--` in the quoted cover messages (185, 188)
  is verbatim output.
- The opener's "This chapter describes ..." (17) is the period
  opener that style guide 8.1 allows. It stays.
