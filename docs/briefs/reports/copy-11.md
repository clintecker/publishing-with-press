# Copyedit: Chapter 11, The art department

File: `book/chapters/11-the-art-department.md`

## Status

REVISE. 8 blocks (watchlist jargon and one "not X but Y" in the
sidebar), 33 should, 10 may. Six sentences go to the fact checker.
`press check` passes the whole book (source, self-test, editorial, and
jargon checks) and names nothing in this file. The watchlist blocks are
"ships", "lands", and "surface". The house `jargon-allow` list lets
them through, but none of them is press's own name for a thing here.
The Chapter 4 and Chapter 8 precedent treats that as a block.

Counts by severity: blocks 8, should 33, may 10.

Most frequent rules broken: era spelling (15, all British "colour",
"grey", "centre" forms in prose), wrong term (11), watchlist jargon (7).

Line numbers are `grep -n` line numbers in the file as it stands.

## The ste_check findings, judged

- Semicolons (43, 59, 78, 160, 244, 292, 363, 439, 464, 525): accepted.
  Every hit is in an `art:` or index comment, a YAML or session example,
  or a verbatim quotation (the house register at 59, the refusals at 363
  and 439). No prose semicolon.
- Sentence and paragraph length at 6, 41, 43, 59, 244, 248, 280, 292,
  333, 525: accepted. The hits are the In-this-chapter list, figure
  lines, `art:` and index comments, and quoted text. 333 counts the
  footnote marker with the next sentence. No prose sentence exceeds 30
  words.
- Passives at 61 ("is gilt", an adjective), 82 ("are prompt material",
  a noun), and 523 (quoted code comment): accepted.
- "is glaring" (301): accepted. It is a verbatim quotation of the code.
- "landscape" (61, 244, 382, 506, 517, 520): accepted. Every use names
  an orientation, not the assistant word's sense.
- "enhance" (41, 43, 525): accepted. It is the command name
  `press art enhance`.
- "therefore", "identical", "look at", `-ing` forms in headings
  ("Finishing a plate", "Commissioning and accepting"): accepted under
  the 80 percent rule.

The checker misses the findings below. They come from reading every
sentence.

## Findings

1. "It upscales, quantizes, and compresses the plates so that each one
   ships as a small PNG." (35, Table 11.1)
   Rule: watchlist jargon ("ship", one-sighting list). Severity: blocks.
   Fix: "It upscales, quantizes, and compresses the plates so that each
   one is a small PNG."

2. "A book without the file gets the house aesthetic, which ships in the
   press as *src/press/data/aesthetic-house.yaml* under the name
   "Victorian treatise"." (59)
   Rule: watchlist jargon ("ship"). Severity: blocks.
   Fix: "A book without the file gets the house aesthetic, which the
   press carries as *src/press/data/aesthetic-house.yaml* under the name
   "Victorian treatise"."

3. "The press ships ten of them in *src/press/data/cover-styles.yaml*,
   and `press cover --list` prints each with a one-line note." (109)
   Rule: watchlist jargon ("ship"). Severity: blocks.
   Fix: "The press carries ten of them in
   *src/press/data/cover-styles.yaml*, and `press cover --list` prints
   each with a one-line note."

4. "The press ships seven illustration styles, which Table 11.4 lists,
   and a book can add its own in *config/illustration-styles.yaml*."
   (200)
   Rule: watchlist jargon ("ship"). Severity: blocks.
   Fix: "The press carries seven illustration styles, which Table 11.4
   lists, and a book can add its own in
   *config/illustration-styles.yaml*."

5. "At the time of this writing, the press ships none." (294)
   Rule: watchlist jargon ("ship"). Severity: blocks.
   Fix: "At the time of this writing, the press has none."

6. "The first OpenAI candidate for the rabbit lands in
   *art/candidates/plate-white-rabbit/openai-1.png*." (405)
   Rule: watchlist jargon ("lands"). Severity: blocks.
   Fix: "The command writes the first OpenAI candidate for the rabbit to
   *art/candidates/plate-white-rabbit/openai-1.png*."

7. "## One master, every surface" (304; also the In-this-chapter item at
   11 and the cross-reference at 276)
   Rule: watchlist jargon ("surface"). Severity: blocks. The section
   itself calls these places grounds (276: "every ground the plate
   meets"), so the heading can use that word. The figure id
   `fig:one-master-every-surface` is never printed and can stay.
   Fix: "## One master, every ground" (and change "One master, every
   surface" to "One master, every ground" at 11 and 276).

8. "The gpt-image models do not lay their ground at pure white. They lay
   it near `#f1f2f3`, a luminance of about 241, which reads as white on a
   screen." (299, sidebar)
   Rule: "not X but Y" (one-sighting list). Severity: blocks.
   Fix: "The gpt-image models lay their ground near `#f1f2f3`, a
   luminance of about 241, which reads as white on a screen."

9. "Every request to an image model costs money, and only a command that
   you run at your own desk can make one." (24)
   Rule: wrong term (vocabulary: "the desk" is `press desk`). Severity:
   should.
   Fix: "Every request to an image model costs money, and only a command
   that you run on your own machine can make one."

10. "Draft the book's aesthetic, if the book wants something other than
    the house idiom." (47, step 1)
    Rule: synonym rotation ("house idiom" for "house aesthetic"), and the
    condition comes after the command. Severity: should.
    Fix: "If the book wants something other than the house aesthetic,
    draft its own."

11. "A plate that sits on disk and that no chapter references is an
    orphan, and `press check` fails the book over it." (55)
    Rule: wrong term (vocabulary: the press refuses; "fail" is for a
    verifier result). Severity: should. Also fact: see fact checker.
    The paragraph ties the orphan rule to step 7 (commit), but an
    orphan is an unreferenced plate, which is a step 2 matter.
    Fix: "A plate that sits on disk and that no chapter references is an
    orphan, and `press check` refuses the book over it."

12. "Suppose the Alice book writes a `cover:` section with only a
    `style:` key in it." (65)
    Rule: synonym rotation ("the Alice book" for "the Alice example").
    Severity: should.
    Fix: "Suppose the Alice example writes a `cover:` section with only a
    `style:` key in it."

13. "Intake looks for both words, as the section "Intake: what
    acceptance enforces" later in this chapter explains, so keep them in
    your own medium if your plates are single ink." (86)
    Rule: two ideas (a description and a command, with the condition
    last). Severity: should.
    Fix: "Intake looks for both words, as the section "What intake
    enforces" later in this chapter explains. If your plates are single
    ink, keep both words in your own medium."

14. "No config validator checks *config/aesthetic.yaml*, so a misspelled
    key simply does nothing." (96)
    Rule: wrong term (vocabulary: "validator" is never used). Severity:
    should. Also fact: see fact checker (`press config validate` claims
    to cover every config field).
    Fix: "Nothing in the press checks the keys in *config/aesthetic.yaml*,
    so a misspelled key does nothing."

15. "## Intake: what acceptance enforces" (246; also the
    In-this-chapter item at 10 and the cross-reference at 86)
    Rule: wrong term (vocabulary: "acceptance" is reserved for the
    record; the act is intake). Severity: should.
    Fix: "## What intake enforces" (and the same words at 10 and 86).

16. "The *target* after `--as` decides where the image goes and what
    happens to it." (255; also *`target`* at 51 and 493, and "targets"
    at 365, 398, 405, 426, 473)
    Rule: wrong term (vocabulary: a target is a `press` command that
    builds, checks, or verifies). Severity: should. The press's own
    synopsis says `[targets]`, so the word cannot leave the chapter.
    Define a distinct term once and flag it to the editor for
    *docs/vocabulary.md*.
    Fix: "The *art target* after `--as` decides where the image goes and
    what happens to it." (Then "art target" in prose throughout the
    chapter. Leave `[targets]` in the synopsis as it is.)

17. "A cover outside that tolerance fails with "crop the source, do not
    stretch it"." (266)
    Rule: wrong term (refuse, not fail). Severity: should.
    Fix: "Intake refuses a cover outside that tolerance with "crop the
    source, do not stretch it"."

18. "The TeX header enforces the figure height cap when the book is
    typeset, and intake leaves that work to it." (266)
    Rule: hidden actor. Severity: should.
    Fix: "The TeX header enforces the figure height cap when LuaLaTeX
    sets the book, and intake leaves that work to it."

19. "The reader edition serves the transparent PNG itself, so a plate
    reads correctly on a light page and on a dark one." (308; also the
    drawn label "reader edition, transparent PNG" in the `art:` comment
    at 280)
    Rule: wrong term (vocabulary: the editions have names). Severity:
    should.
    Fix: "The Chapter edition (the reader site) serves the transparent
    PNG itself, so a plate reads correctly on a light page and on a dark
    one." (Label at 280: "Chapter edition, transparent PNG".)

20. "1. Upscale the plate with Real-ESRGAN. 2. Resample it downward to
    the target long edge. 3. Quantize it to a few grey levels. 4.
    Compress the PNG." (328 to 331)
    Rule: procedure apart from description. The list describes what the
    command does, but its imperatives read as steps for the reader.
    Severity: should.
    Fix: "1. It upscales the plate with Real-ESRGAN. 2. It resamples the
    plate downward to the target long edge. 3. It quantizes the plate to
    a few gray levels. 4. It compresses the PNG."

21. "It quantizes in greyscale unless the design profile is colour, and
    it keeps the alpha channel and reattaches it afterward." (346)
    Rule: two ideas, and era spelling. Severity: should.
    Fix: "It quantizes in grayscale unless the design profile is color.
    It keeps the alpha channel and reattaches it afterward."

22. "On `hatter`, the Alice example can finish one plate, or all of
    them:" (348)
    Rule: hidden actor (an example does not run commands). Severity:
    should.
    Fix: "On `hatter`, `alice` can finish one plate, or all of them:"

23. "`press art commission` reads the file back, and it fails with "no
    commissions.md; run the art-direction workflow first" when the file
    is missing." (363)
    Rule: wrong term (refuse, not fail), and the condition comes last.
    Severity: should.
    Fix: "`press art commission` reads the file back. If the file is
    missing, the command refuses with "no commissions.md; run the
    art-direction workflow first"."

24. "The `--photo` option of `press art commission` names the
    photograph, and by default the command looks for
    `art/author-photo.*`, matched without regard to case." (443)
    Rule: two ideas, and hidden actor ("matched"). Severity: should.
    Fix: "The `--photo` option of `press art commission` names the
    photograph. Without it, the command looks for `art/author-photo.*`
    and ignores case in the match."

25. "The command normalizes a large photograph before it sends it."
    (445)
    Rule: wrong term ("large" is wrong for one of the three cases: the
    next sentence says a small PNG qualifies too). Severity: should.
    Also fact: see fact checker ("over 2048 pixels" does not say which
    edge).
    Fix: "The command normalizes some photographs before it sends them."

26. "A command that needs a missing key stops with this message, where
    the variable's name replaces `{var}`:" (461)
    Rule: wrong term (refuse, not stop). Severity: should.
    Fix: "A command that needs a missing key refuses with this message,
    where the variable's name replaces `{var}`:"

27. "Each request goes from your machine straight to the provider."
    (513)
    Rule: wrong term (vocabulary: a provider is a print vendor spec).
    Severity: should.
    Fix: "Each request goes from your machine straight to OpenAI or
    Google."

28. "Put the exact words "landscape composition" or "portrait
    composition" in every plate prompt in *art/commissions.md*. Without
    one of them, `press art commission` requests a square plate." (520,
    Tip)
    Rule: admonition repeats the paragraph above it (style guide 8.1).
    Severity: should.
    Fix: keep the Tip and cut the paragraph's restatement. At 517: "The
    command reads a plate's shape from the words of its prompt. The
    house aesthetic warns against the square default: "a square plate
    wastes the trim."" The Tip then carries the two phrases and the
    rule.

29. "Its cover is Victorian publisher's bookcloth, with "everything
    stamped as if by a brass die", on a solid cloth-coloured field with
    a fine woven grain." and "The title and subtitle stand in stacked,
    centred letterpress capitals..." (61)
    Rule: era spelling (American spelling outside quotations). Severity:
    should.
    Fix: "...on a solid cloth-colored field with a fine woven grain."
    and "The title and subtitle stand in stacked, centered letterpress
    capitals..."

30. "A few keys do reach the build: the Web palettes, the typography,
    the book colours, and the scene-break ornament." (82)
    Rule: era spelling. Severity: should.
    Fix: "A few keys do reach the build: the Web palettes, the
    typography, the book colors, and the scene-break ornament."

31. "It leaves vast negative space around one small off-centre motif and
    a small refined serif." and "It sets horizontal colour bands around
    a cream centre..." (117, 118, Table 11.2)
    Rule: era spelling. Severity: should. (At 117, "space around ... a
    small refined serif" also misparses: the serif is the type, not a
    second thing in the space.)
    Fix: "It sets one small off-center motif and a small refined serif in
    vast negative space." and "It sets horizontal color bands around a
    cream center, with Gill Sans and a woodcut vignette of the subject."

32. "The `penguin-tri-band` template prints a single colour on cream
    along a strict horizontal grid." (126)
    Rule: era spelling. Severity: should.
    Fix: "The `penguin-tri-band` template prints a single color on cream
    along a strict horizontal grid."

33. "Every pixel of the master has the colour (0,0,0), and only its
    opacity varies." (274)
    Rule: era spelling. Severity: should.
    Fix: "Every pixel of the master has the color (0,0,0), and only its
    opacity varies."

34. "A delivery that already has transparency keeps its mask, and intake
    greys it to the single ink." (282)
    Rule: era spelling. Severity: should.
    Fix: "A delivery that already has transparency keeps its mask, and
    intake grays it to the single ink."

35. "...or move to a colour interior, which keeps the plate's exact
    pixels." (286)
    Rule: era spelling. Severity: should.
    Fix: "...or move to a color interior, which keeps the plate's exact
    pixels."

36. "A colour plate follows a simpler path. ... Intake flattens an
    opaque colour plate onto white and leaves its colours unchanged. The
    intake code names a matting model as future work for colour plates."
    (294)
    Rule: era spelling (four times). Severity: should.
    Fix: "A color plate follows a simpler path. ... Intake flattens an
    opaque color plate onto white and leaves its colors unchanged. The
    intake code names a matting model as future work for color plates."

37. "On cream paper that residue shows as a pale grey rectangle around
    every plate, which the comment in the intake code calls "a
    five-percent box that is glaring on cream paper"." (301, sidebar)
    Rule: era spelling. Severity: should.
    Fix: "On cream paper that residue shows as a pale gray rectangle
    around every plate, which the comment in the intake code calls "a
    five-percent box that is glaring on cream paper"."

38. "...a cloth cover would flatten the master onto the field colour,
    which is how the imprint logo already works." (308)
    Rule: era spelling. Severity: should. Also fact: see fact checker
    ("would": whether the cloth-cover path exists or is only described).
    Fix: "...a cloth cover would flatten the master onto the field color,
    which is how the imprint logo already works."

39. "The medium in `plates.medium` chooses the model and the default
    number of colours, by substring, as Table 11.6 shows." (333)
    Rule: era spelling. Severity: should.
    Fix: "The medium in `plates.medium` chooses the model and the default
    number of colors, by substring, as Table 11.6 shows."

40. "Model and colours" (335, Table 11.6 header) and "keeps 16 grey
    levels" (337); "the number of colours that Table 11.6 gives" (346)
    Rule: era spelling. Severity: should. (`watercolour` at 339 is a
    matched substring in code and stays.)
    Fix: "Model and colors", "keeps 16 gray levels", "the number of
    colors that Table 11.6 gives".

41. "The quantize step reduces the grain to a few greys, and that keeps
    each plate a small lossless PNG." (356, Tip)
    Rule: era spelling. Severity: should.
    Fix: "The quantize step reduces the grain to a few grays, and that
    keeps each plate a small lossless PNG."

42. "The examples come from the Alice example, which user `alice` keeps
    on the workstation `hatter`." (18)
    Rule: rhythm ("examples ... example"). Severity: may.
    Fix: "The examples use the Alice example, which the user `alice`
    keeps on the workstation `hatter`."

43. "The aesthetic comes first, because every commission reads it."
    (55)
    Rule: one topic per paragraph (the sentence turns from the orphan
    rule to the next section). Severity: may.
    Fix: move it to open "The aesthetic" section: "The aesthetic comes
    first, because every commission reads it. The *aesthetic* is the
    book's visual identity: ..."

44. "note: "red cloth, a gilt oval vignette, centred capitals"" and "in
    stacked centred capitals, stamped in gold" (177, 183, Example 11.3)
    Rule: era spelling. Severity: may. This is the book's own invented
    style, not press code, so it can follow the book's spelling.
    Fix: "centered capitals" and "in stacked centered capitals, stamped
    in gold".

45. "Intake writes an alpha master." (260, Table 11.5)
    Rule: a term used before its italic definition at 274. Severity: may.
    Fix: "Intake writes an alpha master, which the next section
    defines."

46. "The rule in the other direction is a scar." (310)
    Rule: rhythm (the reader cannot tell which direction). Severity:
    may.
    Fix: "The rule against baking a plate onto white is a scar."

47. "A year later, the record still tells the maintainer which candidate
    became each plate and at what size." (433)
    Rule: one-line closer (a one-sentence paragraph that ends the
    section; it adds the reason, so it is weak alone). Severity: may.
    Fix: join it to the paragraph at 426: "...replaces the earlier line
    for that target. A year later, the record still tells the maintainer
    which candidate became each plate and at what size." Then the code
    block follows "The line has this form:" as its own short paragraph.

48. "The house style is "An engraved oval trade-journal portrait of a
    valued tradesman, ..."" (443)
    Rule: synonym rotation ("house style" for the house aesthetic's
    `portrait.style`). Severity: may.
    Fix: "The house aesthetic's portrait style is "An engraved oval
    trade-journal portrait of a valued tradesman, ...""

49. "A 6 by 9 cover at 300 dpi needs about 1800 by 2700 pixels." (500)
    Rule: synonym rotation ("dpi" here, "DPI" at 266 and 346).
    Severity: may.
    Fix: "A 6 by 9 cover at 300 DPI needs about 1800 by 2700 pixels."

50. "Gemini takes one request per image." (515)
    Rule: one topic per paragraph (the paragraph is about cover sizes).
    Severity: may.
    Fix: move it after the Gemini sentence at 513: "...asks for both
    text and image in the reply. Gemini takes one request per image."

51. The sidebar "The five-percent box" (296 to 302) runs about 130
    words, under the style guide's 150 to 400.
    Rule: rhythm (sidebar length, style guide 3.5). Severity: may.
    Fix: none required. If the writer wants it to reach length, the
    gradient failure in its last two sentences can take the one story
    from 286 ("The key read every dark pixel of a gradient as ink...").

## Fact-checker referrals (not copyedits)

- 55: whether an uncommitted plate is an orphan, and whether
  `press check` refuses orphan plates.
- 96: whether any `press config validate` path checks
  *config/aesthetic.yaml*.
- 308: whether the cloth-cover flattening exists or is only documented.
- 445: which dimension "over 2048 pixels" measures.
- 513: whether `--from` (a `press illustrate` option) applies to the
  `press art commission` requests this paragraph describes.
- 517: whether "a square plate wastes the trim" is the house
  aesthetic's text or only the Alice example's (it appears in Example
  11.1 at 78).

## The other checks

- Second person and present tense: held throughout. No "I". No "we"
  anywhere in the chapter, which is within the rule.
- Dry understatement: thin. "Step 7 matters more than it looks" (55) and
  "A flat ground was the easy case" (301) are the only candidates in
  about nine pages. Neither is in a heading. Not a defect, but the writer
  could add one in the commission or keys sections.
- Admonitions: seven (four Tips, three Warnings), all imperative, all
  one to three sentences. Only the Tip at 520 repeats its paragraph
  (item 28). The Warning at 484 restates 481 but adds the instruction.
  That is acceptable.
- Footnotes: four (penguin, ink, upscayl, imagen), all asides. The first
  sentence of the imagen footnote (523) repeats 513 and can go.
- Spellings: Web, toward, afterward, filename, and e-mail are correct
  where they occur. American spelling fails only on the
  colour/grey/centre family (items 29 to 41 and 44). "folder" appears
  only in the `art:` comment at 43 as a drawn icon shape.
- Numbers under ten: spelled out in prose. Numerals appear only for
  steps, measurements (3 percent, 6 by 9), code values, and versions.
- Headings and captions: sentence case throughout. No title case.
