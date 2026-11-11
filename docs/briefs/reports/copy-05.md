# Copyedit: Chapter 5, Figures, plates, and illustrations

File: `book/chapters/05-figures-and-plates.md`

## Status

REVISE. Nine blocks, 27 should, 13 may.

`press check` exits 1, and Chapter 5 carries 18 of its 23 findings:
`authoritative` (75, rewrite), `settle` (128), `wins` (260), and fifteen
sightings of `spine` (139 to 208). Four further one-sighting terms pass
the checker but break the contract: "shipped" twice, "clean" (in
`jargon-allow`), and "surface" (in `jargon-allow`).

Counts by severity: blocks 9, should 27, may 13.

Most frequent rules broken: wrong term (12), two ideas (9 at should,
2 more at may), watchlist jargon (8, all blocks).

## The ste_check findings, judged

`python3 tools/ste_check.py` reports 30 findings: 383 sentences, average
13.9 words, longest 41.

- Sentence length (6, 71, 73, 77, 128, 130, 150, 200, 204, 206, 208, 314,
  353): accepted for 6 (the In-this-chapter list), 130 (a fusion across
  the `[^hypcap]` marker), 150 and 206 (fig-alt text), 208 (art comment),
  and 353 (index comment). No prose sentence runs over 30 words. The ones
  at 25 to 29 words that also carry two ideas are items 3, 16, 17, 20,
  21, and 22.
- Semicolons (208, 353): accepted. Both sit in comments that never print.
  No prose semicolon.
- Passive "is print" (240): false positive ("is print-only").
- `-ing` forms (106, 150, 343): accepted. Two are the chapter title
  *Checking the manuscript*. The third is "filling" in the fig-alt.
- "therefore" (71, 240, 260, 324) and "whether" (26): accepted. The
  contract allows both.
- "enhance" (353): accepted. It is the command `press art enhance`.
- Paragraph length (152, 208, 246): accepted. All three are art comments.

## Findings

1. "It shipped empty pages, one after another, forever, at 100 percent of
   a CPU." (279, sidebar)
   Rule: watchlist jargon ("ship", one-sighting list). Severity: blocks.
   Fix: "It emitted empty pages, one after another, forever, at 100
   percent of a CPU."

2. "Truecolor PNG barely compresses the grain of an engraving, so plates
   once shipped as JPEG files baked onto white." (296)
   Rule: watchlist jargon ("shipped", one-sighting list). Severity:
   blocks.
   Fix: "Truecolor PNG barely compresses the grain of an engraving, so the
   house once kept plates as JPEG files baked onto white."

3. "Plain LuaLaTeX under pandoc does not run enough passes for the lists
   to settle, so press builds the PDF through latexmk, which runs
   LuaLaTeX until the output stops changing." (128)
   Rule: watchlist jargon ("settle", which `press check` refuses), and
   two ideas in 29 words. Severity: blocks.
   Fix: "Plain LuaLaTeX under pandoc does not run enough passes for the lists
   to converge. Press therefore builds the PDF through latexmk, which runs
   LuaLaTeX until the output stops changing."

4. "The two limits act together, and whichever binds first wins." (260)
   Rule: watchlist jargon ("wins", which `press check` refuses).
   Severity: blocks.
   Fix: "The two limits act together, and the limit that binds first sets
   the size."

5. "The press documentation calls this report "the authoritative reading"
   of the manuscript, and both `press illustrate` and the art-direction
   workflow use it." (75)
   Rule: watchlist jargon ("authoritative", which `press check` refuses
   as `rewrite` even inside a quotation). Severity: blocks.
   Fix: "The press documentation treats this report as the one reading of
   the manuscript, and both `press illustrate` and the art-direction
   workflow use it."

6. "In each of them a placed figure becomes a clean in-flow figure: the
   picture and its caption in the run of the text." (240)
   Rule: watchlist jargon ("clean", one-sighting list). `press check`
   passes it only because `clean` is in `jargon-allow`. That entry is
   for press's own names, and this "clean" is not one. Severity: blocks.
   Fix: "In each of them a placed figure becomes a plain in-flow figure:
   the image and its caption in the run of the text."

7. "The house keeps each plate as an *alpha master*, ink on transparency,
   and each edition composites it onto its own surface." (248)
   Rule: watchlist jargon ("surface", one-sighting list). `press check`
   passes it through `jargon-allow`. Here it is a metaphor for the page
   ground, not a press name. Severity: blocks.
   Fix: "The house keeps each plate as an *alpha master*, ink on
   transparency, and each edition composites it onto its own page."

8. "The cap exists because of a failure that looked like nothing at all,
   and the sidebar tells the story." (274)
   Rule: meta-narration (text about the document itself, one-sighting
   list). Severity: blocks.
   Fix: "The cap exists because of a failure that looked like nothing at
   all."

9. "spine" at 139, 150, 152 (twice), 154 (four times), 156, 206, and 208
   (five times). `press check` refuses every one as `inspect: 'spine'
   [structural metaphor]`. Each use is literal: the bound edge of a
   book. Rule: watchlist jargon (`press check` refuses). Severity:
   blocks.
   Fix: no change to the prose. This needs a house-rules decision, not a
   copyedit. Add `spine` to `jargon-allow` in `config/house-rules.yaml`,
   because Chapters 1, 3, and 6 also use it literally. The fix belongs
   to whoever owns house rules.

10. "The difference between `inline` and `plate` is not visible there,
    and in the PDF it does not exist: both are ordinary figures held in
    place. The difference is in the rules: a `plate` placement takes no
    measure, ..." (148)
    Rule: "not X but Y" (the "This doesn't mean X. It means Y." shape). It
    is close to the pattern, not a literal match. Severity: should.
    Fix: "In the drawing and in the PDF, `inline` and `plate` look the
    same: both are ordinary figures held in place. They differ in one
    rule: a `plate` placement takes no measure, so the figure prints at
    its own size, within the height cap and the line."

11. "One attribute overrides the numbering: a figure that carries
    `decorative=true` is an *ornament*, a picture that holds no
    information." (40)
    Rule: wrong term ("figure" is the numbered kind, and an ornament can
    be any illustration). Severity: should.
    Fix: "One attribute overrides the numbering: an illustration that
    carries `decorative=true` is an *ornament*, an image that holds no
    information."

12. "Press then finds the figure whose image file stem matches the name,
    and it sends that figure's `art:` directive to the image model. ...
    Press refuses in three cases: no figure in the manuscript has that
    stem, the figure is a data kind, or the figure has no `art:`
    directive." (61)
    Rule: wrong term (the name is a plate's, so "figure" is the wrong
    kind). Severity: should.
    Fix: "Press then finds the illustration whose image file stem matches
    the name, and it sends that illustration's `art:` directive to the
    image model. ... Press refuses in three cases: no illustration in the
    manuscript has that stem, the illustration is a data kind, or it has
    no `art:` directive."

13. "Press takes the style from the `--style` option first, then from the
    figure's own `style=` attribute, ..." (71)
    Rule: wrong term (the attribute belongs to any illustration).
    Severity: should.
    Fix: "Press takes the style from the `--style` option first, then from
    the illustration's own `style=` attribute, then from `plates.style`
    in the aesthetic, and last from the house style `wood-engraving`."

14. "Write `fig-alt` for every figure that carries information, ..." (73)
    Rule: wrong term (plates need alt text too). Severity: should.
    Fix: "Write `fig-alt` for every illustration that carries information,
    and write it for a listener: one or two sentences that say what the
    picture shows."

15. "The `place` attribute says where a figure sits on the printed page."
    (134)
    Rule: wrong term (Example 5.3 places a plate). Severity: should.
    Fix: "The `place` attribute says where an illustration sits on the
    printed page."

16. "Never copy the caption into it, because a screen reader reads the
    caption already, and a second reading of the same words tells the
    listener nothing new." (73)
    Rule: two ideas (a command, then two chained reasons, 28 words).
    Severity: should.
    Fix: "Never copy the caption into it. A screen reader reads the caption
    already, and a second reading of the same words tells the listener
    nothing new."

17. "If a directive does not appear in the report, press did not find it,
    and a common cause is a comment above the image instead of below it."
    (78, tip)
    Rule: two ideas (28 words). Severity: should.
    Fix: "If a directive does not appear in the report, press did not find
    it. A common cause is a comment above the image instead of below it."

18. "The `.map` class makes this a numbered figure, and it is the first
    figure in Chapter 8, so press numbers it Figure 8.1." (100)
    Rule: two ideas. Severity: should.
    Fix: "The `.map` class makes this a numbered figure. It is the first
    figure in Chapter 8, so press numbers it Figure 8.1."

19. "A plate has no number, so the prose cannot cite it by number, and a
    sentence that needs to point at one names its caption." (104)
    Rule: two ideas. Severity: should.
    Fix: "A plate has no number, so the prose cannot cite it by number. A
    sentence that needs to point at a plate names its caption."

20. "The line is a different length in each profile, and a figure set at
    half the measure stays at half the measure when the book moves to
    another trim." (200)
    Rule: two ideas (29 words), and synonym rotation ("trim" for the
    profile that the sentence just named). Severity: should.
    Fix: "The line is a different length in each profile. A figure set at
    half the measure stays at half the measure when the book moves to
    another profile."

21. "The height must fit the *height cap*, which the house TeX header
    stores in the macro `\PressFigureCap`, and the width must fit
    `\linewidth`, the length of the line." (258)
    Rule: two ideas. Severity: should.
    Fix: "The height must fit the *height cap*, which the house TeX header
    stores in the macro `\PressFigureCap`. The width must fit
    `\linewidth`, the length of the line."

22. "Intake makes no check of resolution: it checks no minimum pixel count
    and no DPI, and the cover's aspect ratio is the only shape it checks."
    (314)
    Rule: two ideas (29 words), with the action in a noun ("makes no
    check"). Severity: should.
    Fix: "Intake does not check resolution. It checks no minimum pixel
    count and no DPI, and the only shape it checks is the cover's aspect
    ratio."

23. "Any plate on disk under *assets/woodcuts/* that
    the manuscript never references fails `press check`, and the checker
    prints the path:" (116)
    Rule: wrong term ("fail" is for a verifier result; the checker
    refuses). Severity: should.
    Fix: "If a plate on disk under *assets/woodcuts/* has no reference in
    the manuscript, the checker refuses the book and prints the path:"

24. "The values `left`, `right`, `wrap-left`, and `wrap-right` fail, and so
    do the bare `inner` and `outer`. A value that press does not know at
    all fails as an unknown placement." (156)
    Rule: wrong term ("fail" for a checker refusal). Severity: should.
    Fix: "The checker refuses the values `left`, `right`, `wrap-left`, and
    `wrap-right`, and it refuses the bare `inner` and `outer` too. It
    refuses a value that press does not know at all as an unknown
    placement."

25. "The print build therefore passes every image through a *print-safe*
    pass." (324)
    Rule: wrong term ("print build" is on the never list; the term is
    "the print pack"). Severity: should.
    Fix: "The print pack therefore passes every image through a
    *print-safe* pass."

26. "The print interior has one more reader than the PDF: the vendor's
    preflight, the program a print vendor runs over every file it
    receives." (324)
    Rule: wrong term ("vendor" is on the never list for provider).
    Severity: should.
    Fix: "The print interior has one more reader than the PDF: the
    provider's preflight, the program a print provider runs over every
    file it receives."

27. "A preflight flags transparency and flags images that carry far more
    pixels than the press needs." (324)
    Rule: wrong term ("the press" is press the institution in this book;
    here it means a printing press). Severity: should.
    Fix: "A preflight flags transparency and flags images that carry far
    more pixels than print needs."

28. "The house 6 by 9 profile sets 6.3 inches, and that is the figure you
    will most often see quoted." (262) Also "The figure is simple
    division: ..." (351, footnote)
    Rule: wrong term ("figure" means a numbered illustration in this
    book, and this chapter is about figures). Severity: should.
    Fix: "The house 6 by 9 profile sets 6.3 inches, and that is the number
    you will most often see quoted." and "The arithmetic is simple
    division: 1024 pixels over 1.7 inches is 602 pixels per inch."

29. "In the source, type the image line, one blank line, and then the
    paragraph that wraps, with nothing between them." (221)
    Rule: wrong term ("the source" is on the never list for the
    manuscript). Severity: should.
    Fix: "In the chapter file, type the image line, one blank line, and
    then the paragraph that wraps, with nothing between them."

30. "The filter fuses the wrap onto the head of the next paragraph, and
    the text really does run around the figure." (221)
    Rule: hidden actor ("The filter" has no antecedent; no filter has
    been named since line 102). Severity: should.
    Fix: "Press's Lua filter fuses the wrap onto the head of the next
    paragraph, so the text runs around the figure."

31. "The mechanism is a redefinition of pandoc's own `\pandocbounded`
    macro in the house header, so every image that pandoc writes passes
    through it, whatever its kind or placement." (258)
    Rule: hidden actor (the actor is buried in the noun "redefinition").
    Severity: should.
    Fix: "The house header redefines pandoc's own `\pandocbounded` macro,
    so every image that pandoc writes passes through it, whatever its
    kind or placement."

32. "The cap was 6.3 inches on the 6 by 9 page, and it is now set per
    profile." (281, sidebar)
    Rule: hidden actor. Severity: should.
    Fix: "The cap was 6.3 inches on the 6 by 9 page, and each profile now
    sets its own."

33. "Write the directive for an artist who has not read the book." (63)
    Rule: perfect tense. Severity: should.
    Fix: "Write the directive for an artist who does not know the book."

34. "Example 5.5 shows the whole path for one plate: the commission,
    intake, and the finishing pass, and we elide the output of each
    command." (298)
    Rule: "we" outside the authors' judgment, and two ideas. Severity:
    should.
    Fix: "Example 5.5 shows the whole path for one plate: the commission,
    intake, and the finishing pass. Each `...` line stands for the output
    of a command."

35. "A *plate* is an unnumbered illustration in the idiom of the literary
    woodcut, a picture that keeps the story company and asks nothing of
    the reader." (22) Also "the size of the picture", "the sharpness of
    the picture", "a picture with too few pixels" (314) and "at the size
    the picture prints" (316).
    Rule: synonym rotation (the vocabulary bars "picture" for a plate,
    and uses "image" for the file). Severity: should.
    Fix: "A *plate* is an unnumbered illustration in the idiom of the
    literary woodcut, one that keeps the story company and asks nothing
    of the reader." At 314 and 316, use "image" for "picture" each time.
    Example: "Press can scale an image down to fit the page, but it never
    scales one up, so an image with too few pixels prints soft at its own
    size." The general "picture" at 24, 57, 63, 73, and 250 is accepted.

36. "Write those references in words: "see Chapter 6, *Checking the
    manuscript*", or "the section "Placement" later in this chapter"."
    (106)
    Rule: punctuation (double quotes nested inside double quotes).
    Severity: should.
    Fix: "Write those references in words: "see Chapter 6, *Checking the
    manuscript*", or "the section 'Placement' later in this chapter"."

37. "Name the subject, the moment, and what sits around it, then the
    medium, and say "no lettering" if the picture must carry none." (63)
    Rule: condition first (rhythm). Severity: may.
    Fix: "Name the subject, the moment, and what sits around it, then the
    medium. If the picture must carry no lettering, say "no lettering"."

38. "An ornament has an empty alt text by definition, so `decorative=true`
    together with a `fig-alt` makes no sense, and the checker refuses
    the pair." (73)
    Rule: two ideas (rhythm). Severity: may.
    Fix: "An ornament has an empty alt text by definition, so the checker
    refuses `decorative=true` together with a `fig-alt`."

39. "The two wraps name a side of the page by its relation to the spine,
    and the reason is the book itself." (154) Also "Plates are PNG
    files, and the reason is a scar." (296)
    Rule: a saying dressed as depth (staged reason). Severity: may.
    Fix: "The two wraps name a side of the page by its relation to the
    spine, because the spine changes sides from page to page." and "Plates
    are PNG files because of a scar."

40. "One computation means one answer: the PDF, the EPUB, and the reader
    site can never disagree about which figure is Figure 8.1." (102)
    Rule: a saying dressed as depth (the maxim before the colon).
    Severity: may.
    Fix: "Because press computes each number once, the PDF, the EPUB, and
    the reader site can never disagree about which figure is Figure 8.1."

41. "Press numbers and cites only figures." (104)
    Rule: one topic per paragraph. The paragraph is about a mistyped
    citation, and this sentence starts a second topic about plates.
    Severity: may.
    Fix: start a new paragraph at "Press numbers and cites only figures."

42. "Do not type `place=left` or `place=right`, even in a draft. The
    checker refuses both, and the correct value is `wrap-inner` or
    `wrap-outer`, never the bare `inner` or `outer`." (159, warning)
    Rule: an admonition that repeats the paragraph above it (style guide
    8.1). Severity: may.
    Fix: "Type `wrap-inner` or `wrap-outer` from the first draft. The
    checker refuses `left`, `right`, and the bare `inner` and `outer`."

43. "Do not try to defeat the height cap with a custom TeX header or a raw
    LaTeX include. A figure taller than the text block makes LuaLaTeX
    emit empty pages forever, silently, at full CPU." (285, warning)
    Rule: an admonition that repeats the sidebar above it. Severity: may.
    Fix: "Do not try to defeat the height cap with a custom TeX header or a
    raw LaTeX include. The sidebar's failure comes back at once."

44. "It upscales the image four times with Real-ESRGAN when it finds an
    upscaler." (312)
    Rule: condition first, and "four times" reads as four passes.
    Severity: may.
    Fix: "If it finds an upscaler, it upscales the image by a factor of
    four with Real-ESRGAN."

45. "The toolchain image carries the upscaler on amd64 only, and the arm64
    image, which has no upstream binary, resamples and quantizes without
    it." (312)
    Rule: two ideas (rhythm). Severity: may.
    Fix: "The toolchain image carries the upscaler on amd64 only. The arm64
    image has no upstream binary, so it resamples and quantizes without
    the upscaler."

46. "it checks no minimum pixel count and no DPI" (314), then "300 pixels
    per inch, abbreviated *PPI*" (316)
    Rule: synonym rotation (DPI, then PPI, within two sentences).
    Severity: may. If intake means the DPI metadata field, say so: "no
    DPI field".
    Fix: "It checks no minimum pixel count and no resolution metadata, and
    the only shape it checks is the cover's aspect ratio."

47. "a clean in-flow figure" (240) against "an in-flow placement" (184)
    Rule: synonym rotation ("in-flow" names four placements at 184, then
    means "set in the run of the text" in a reflowable edition at 240).
    Severity: may.
    Fix at 240: "In each of them a placed figure becomes an ordinary
    figure: the image and its caption in the run of the text."

48. "callouts ... "spine" at the centre rule" (208, art comment)
    Rule: era spelling (British "centre"; the comment at 152 says
    "centered"). It does not print, but the illustrator reads it.
    Severity: may.
    Fix: "at the center rule".

49. "| Logomark | The pass resamples the logo to a long edge of no more
    than 1000 pixels. |" (328, Table 5.6)
    Rule: synonym rotation (logomark, then logo; the chapter uses both at
    292, 335, 337, and 340). Severity: may.
    Fix: "| Logomark | The pass resamples the logomark to a long edge of no
    more than 1000 pixels. |" and keep "logomark" throughout, or define
    "logo" once as the short form.

Item 47 and item 6 touch the same sentence at 240. Apply item 6 first,
then replace "plain in-flow" with "ordinary" if the desk accepts item 47.

## Fact notes (for the fact checker; not counted)

- 288: "The cap also explains why the house cannot enlarge a small
  image." The cap limits height. The no-enlarging rule comes from the
  `\pandocbounded` redefinition at 258 ("Press only ever scales down").
  fact: see fact checker.
- 319, tip: "Run `press art enhance` on any plate that falls short." On
  arm64, 312 says the image has no upscaler, so the pass cannot add
  pixels there. fact: see fact checker.
- 240: the list of reflowable editions leaves out the Markdown edition
  that the vocabulary names. fact: see fact checker.
- 253, tip: "Use the `@fig:` citation" fits a figure but not a plate,
  which 250 tells you to cite by caption. Wording question; the fact
  checker or the developmental editor decides.

## Other checks

- Second person and present tense hold throughout. The sidebar (279 to
  281), the hypcap story (130), and the Lulu story (335) use the past
  tense for history, and the contract allows that.
- "We" appears once, at 298, and it is not judgment (item 34). The
  authors' choices are stated as "this book does" (24, 236). No "I".
- Dry understatement appears at 104 ("easy to see in a proof and easy to
  miss in a hurry"), 162 and 164 ("promises more than it does", "promises
  more again"), 279 ("nothing came out that anyone could inspect"), and
  the 345 footnote. The two at 162 and 164 sit back to back, which is
  more than once every few pages there. None is in a heading.
- Admonitions: five tips and three warnings, eight in all, at the upper
  limit of the style guide's three to eight. Each is imperative and under
  four sentences. Two repeat the text above them (items 42 and 43).
- The sidebar runs about 130 words, under the style guide's 150-word
  floor. Severity may. One added sentence of history would bring it up
  to length.
- Footnotes (four) carry history and asides. The body does not need any
  of them.
- Spelling: American throughout the printed prose ("gray", "honors",
  "labeled"). "colour" at 66 sits in the verbatim guardrail text and
  stays. "centre" at 208 is item 48. No "Unix", "e-mail", "Web site",
  "manpage", "appendixes", or "toward" occasion arises. "filename" is not
  used.
- Numbers: under ten spelled out in prose ("seven", "four", "three",
  "two"). Numerals appear in versions, measurements, chapter and figure
  numbers, counter values (`tocdepth` 0), and code. Table 5.4 gives "9
  free lines" as a numeral in a series with 20, 13, and 11. That is
  accepted for the series.
- No semicolons, dashes, hedge stacks, or assistant vocabulary in prose.
  No noun stack runs over three. The one perfect tense is item 33.
