# Copyedit: Chapter 7, Building the editions

File: `book/chapters/07-building-the-editions.md`

## Status

REVISE. Four blocks (watchlist jargon twice, one one-line closer, bold
labels on every list item), 28 should, 15 may. No house-rules
`banned-patterns` regex matches the chapter, and it holds no dashes or
non-ASCII characters, so the checker would refuse nothing here. The four
blocks are on the contract's one-sighting list, and the checker's silence
does not clear them ("ship" and "shipped" pass the jargon lint only
because `jargon-allow` lists them as press's own names, and here they
name nothing of press's).

Counts by severity: blocks 4, should 28, may 15.

Most frequent rules broken: wrong term (15, including partial hits),
two ideas (6), hidden actor (5). Synonym rotation follows with 4.

## The writer's ste_check defences, judged

`python3 tools/ste_check.py` reports 40 findings (418 sentences, average
12.3 words, maximum 42).

- Sentence length (6, 51, 75, 83, 88, 95, 162, 192, 323, 419): accepted
  except 88. The others are the In-this-chapter box, art comments fused
  with their image lines, fusions across code blocks, and the index
  comment. Line 323 counts 24 words on its own. **Rejected for 88:** it
  is one prose sentence of 31 words (item 2).
- Semicolons (419): accepted. The index comment, plus the quoted press
  output at 306 and 342. No prose semicolon.
- Passive "are cleaned" (319): accepted, it sits inside a quotation.
  The writer's report says there are no passives in prose, but the
  checker misses "are both marked" at 268 (item 31).
- Perfect "has vanished" (92): accepted, an art comment.
- `-ing` forms (15, 22, 45, 75, 83, 86, 109, 219, 309, 353, 357, 403,
  415, 417): accepted. Headings, chapter titles, and section titles in
  cross-references.
- "therefore" (111, 131), "whether" (247): accepted, the contract allows
  them. "verify" (291, 301, 325, 361): accepted, target names and art
  comments.
- Paragraph length (51, 83, 92, 325): accepted, art comments. **Rejected
  for 167:** the sidebar's single paragraph is prose and runs eight
  sentences (item 15). The checker does not flag 90, which also runs
  seven sentences (item 8).

The checker does not catch most of the problems below. They come from
reading every sentence.

## Findings

1. "The press ships one for each family of editions in
   *src/press/data/defaults/*: ..." (79)
   Rule: watchlist jargon ("ship", one-sighting list).
   Severity: blocks.
   Fix: "The press carries one for each family of editions in
   *src/press/data/defaults/*: `pdf.yaml`, `epub.yaml`, `html.yaml`,
   `chunked.yaml`, `portable.yaml`, and `print.yaml`."

2. "The shipped defaults files cannot name absolute paths, because the
   press does not know where you installed it or where your book lives,
   so they name paths with two prefixes instead." (88)
   Rule: watchlist jargon ("shipped", one-sighting list), sentence over
   30 words (31), two ideas, wrong term ("your book" for the book
   repository). Severity: blocks.
   Fix: "The defaults files in the package cannot name absolute paths,
   because the press does not know where you installed it or where your
   book repository is. Instead, they name paths with two prefixes."

3. "Whatever you typed in a chapter file appears in it as typed." (227)
   Rule: one-line closer (it repeats "the manuscript as you wrote it, in
   one file" from the sentence before, and it overstates, because the
   attribute blocks are removed). Severity: blocks.
   Fix: delete the sentence. The paragraph ends at "The result,
   *dist/alice.md*, is the manuscript as you wrote it, in one file."

4. "1. **check.** The press runs the checker: ..." through "6. **The
   commerce gate.** The press runs the commerce gate." (330-335)
   Rule: bold labels on every list item (one-sighting list). The labels
   also disagree in case ("check." against "Every edition."), and item 6
   says the same thing twice. Severity: blocks.
   Fix: drop the labels and let each item start with its sentence:
   "1. The press runs the checker: the source checks, then ...
   2. The press builds each edition target in turn.
   3. The press builds *dist/alice-source.zip*.
   4. The press assembles *dist/pages/*.
   5. The press runs the page verifier, the PDF verifier, the format
   verifier, and the archive verifier, in that order.
   6. The press runs the commerce gate."

5. "The press decides the build order, the file names, and the
   editions." (22)
   Rule: era spelling ("filename"). Severity: should.
   Fix: "The press decides the build order, the filenames, and the
   editions."

6. "The book repository decides the words and the look." (22)
   Rule: wrong term ("look" is on the never list for the aesthetic).
   Severity: should.
   Fix: "The book repository decides the words and the aesthetic."

7. "If pandoc is missing, the build stops at once with the message
   `pandoc is required`." (45)
   Rule: wrong term (press stops with a message: refuse). Severity:
   should.
   Fix: "If pandoc is missing, the press refuses the build at once with
   the message `pandoc is required`."

8. "If any other file is absent, the build stops with the message
   `defaults reference a missing file`." (90)
   Rule: wrong term (refuse). Severity: should.
   Fix: "If any other file is absent, the press refuses the build with
   the message `defaults reference a missing file`."

9. "Before each pandoc run, the press renders the defaults file. ...
   @fig:defaults-templating shows a defaults file before and after this
   step." (90, seven sentences)
   Rule: paragraph over six sentences. Severity: should.
   Fix: join the last two sentences: "The press writes the rendered
   copies to *build/defaults/*, one per defaults file, and the pandoc
   command names that copy." Then begin a new paragraph:
   "@fig:defaults-templating shows a defaults file before and after this
   step."

10. "The page bundle needs every published edition, and the cover wrap
    needs the print interior." (49)
    Rule: wrong term (the page bundle also needs the sources companion,
    which is an artifact, not an edition; line 266 says "every other
    published artifact"). Severity: should.
    Fix: "The page bundle needs every other published artifact, and the
    cover wrap needs the print interior."

11. "This chapter follows the Alice example from that directory to a
    full *dist/*, one edition at a time." (18) and "The targets are not
    independent, because some artifacts need others before they can
    exist." (49)
    Rule: wrong term (the vocabulary wants the first use of each term in
    a chapter set in italic and defined in the same sentence; "edition"
    and "artifact" are neither). Severity: should.
    Fix: "This chapter follows the Alice example from that directory to a
    full *dist/*, one *edition* (one published form of the book) at a
    time." and "The targets are not independent, because some
    *artifacts*, the files and directories in *dist/* that the registry
    names, need others before they can exist."

12. "Chapter 6, *Checking the manuscript*, covered the targets that read
    the manuscript, and the targets in this chapter write files." (22)
    Rule: two ideas. Severity: should.
    Fix: "Chapter 6, *Checking the manuscript*, covered the targets that
    read the manuscript. The targets in this chapter write files."

13. "The `--defaults` option names a rendered defaults file, and the
    extra arguments are the press's own." (65)
    Rule: two ideas (two of the four parts in one sentence). Severity:
    should.
    Fix: "The `--defaults` option names a rendered defaults file. The
    extra arguments are the press's own."

14. "The six files declare three different chains, and the PDF, EPUB,
    HTML, and chunked defaults share one chain of five filters." (81)
    Rule: two ideas. Severity: should.
    Fix: "The six files declare three different chains. The PDF, EPUB,
    HTML, and chunked defaults share one chain of five filters."

15. "The first book built its PDF the simple way, ... A shallow table of
    contents can no longer empty the List of Plates." (167, eight
    sentences)
    Rule: paragraph over six sentences (the writer's defence covers lists
    and art comments, not the sidebar). Severity: should. The sidebar
    also runs 132 words, under the style guide's 150-word floor, so the
    split costs nothing.
    Fix: end the first paragraph at "The PDF now builds through latexmk,
    which runs as many passes as the lists need." Start a second
    paragraph at "A second trap sat in the same lists."

16. "Much of the press's fine typesetting happens in filters, and a
    filter in a shared chain acts on every edition that runs that
    chain." (115)
    Rule: two ideas. Severity: should.
    Fix: "Much of the press's fine typesetting happens in filters. A
    filter in a shared chain acts on every edition that runs that chain."

17. "It also packs the manuscript itself into the source edition." (223)
    Rule: wrong term ("the manuscript" is the chapters and appendices
    under *book/*, and the source zip holds every file that Git tracks in
    the book repository, as 235 says). Severity: should.
    Fix: "It also packs the book repository itself into the source
    edition."

18. "> **Tip:** Add and commit a new chapter file before you build the
    source edition. The source zip holds only the files that Git
    tracks." (238)
    Rule: admonition that repeats the paragraph above it (style guide
    8.1). Severity: should.
    Fix: "> **Tip:** Add and commit a new chapter file before you build
    the source edition, or the zip leaves it out."

19. "The rule carries the name `INV-graph-no-stale` in the press's ledger
    of invariants, at the critical level. The ledger also states its
    limit: the rule holds on the command-line path only." (293)
    Rule: wrong term ("rule" is on the never list for invariant), and
    "invariant" is not defined at first use. Severity: should.
    Fix: "The press records this as an *invariant*, an entry in its
    ledger of guarded behavior, under the name `INV-graph-no-stale` at
    the critical level. The ledger also states its limit: the invariant
    holds on the command-line path only."

20. "`press verify-formats` builds the EPUB, the HTML, the Markdown, the
    site, the text, the Word file, and the source zip, and then runs the
    format and archive verifiers." (301)
    Rule: synonym rotation ("the site" for the reader site, "the Word
    file" for the Word edition, bare "the Markdown" and "the text").
    Severity: should.
    Fix: "`press verify-formats` builds the EPUB, the HTML, the Markdown,
    text, and Word editions, the reader site, and the source zip, and
    then runs the format and archive verifiers."

21. "Press builds the print interior, generates the wrap, runs latexmk
    on it, and verifies it." (38); "it then builds the cover wrap and
    runs the wrap verifier" (303); "`press coverwrap` builds the print
    interior, then the wrap, and then runs the wrap verifier." (309)
    Rule: wrong term ("wrap" alone is the controlled term for text
    flowing beside a figure, and 126 uses it that way). Severity: should.
    Fix: "Press builds the print interior, generates the cover wrap,
    runs latexmk on it, and verifies it." / "it then builds the cover
    wrap and runs the cover-wrap verifier" / "`press coverwrap` builds
    the print interior, then the cover wrap, and then runs the
    cover-wrap verifier."

22. "Every pandoc build calls the same function first, and that function
    does three things in order:" (313)
    Rule: hidden actor (the press calls the function, not the build).
    Severity: should.
    Fix: "Before every pandoc build, the press calls the same function,
    which does three things in order:"

23. "The checker stops at the first pass that fails." (330)
    Rule: wrong term (the checker refuses; "fail" is for a verifier
    result). Severity: should.
    Fix: "The checker stops at the first pass that refuses the
    manuscript."

24. "Under `press all`, a manuscript that fails the checker never reaches
    pandoc." (337)
    Rule: wrong term (refuse). Severity: should.
    Fix: "Under `press all`, a manuscript that the checker refuses never
    reaches pandoc."

25. "When `PRESS_RELEASE` is set, the gate enforces its findings and
    fails the run." (345)
    Rule: hidden actor (who sets it), wrong term ("fails" for a stop
    with a message). Severity: should.
    Fix: "When the release build sets `PRESS_RELEASE=1`, the gate
    enforces its findings and the press refuses the run."

26. "The press documents no other timing, and the first LuaLaTeX run on
    a new machine is the one slow step that its documentation
    describes." (359)
    Rule: two ideas. Severity: should.
    Fix: "The press documents no other timing. The one slow step that its
    documentation describes is the first LuaLaTeX run on a new machine."

27. "Open the matching file when either one refuses the book." (363)
    Rule: condition first; wrong term (the lint refuses, the verifier
    fails). Severity: should.
    Fix: "When the lint refuses the book or the PDF verifier fails it,
    open the matching file."

28. "It does not strip HTML comments, so the `art:` directive above every
    figure counts toward the total. If you write to a fixed length,
    remember that your figure briefs are in the number." (413)
    Rule: synonym rotation ("`art:` directive", then "figure briefs",
    for one thing). Severity: should.
    Fix: "It does not strip HTML comments, so the `art:` comment above
    every figure counts toward the total. If you write to a fixed length,
    remember that your `art:` comments are in the number."

29. "the source zip" (56, 238, 301, 332) against "the source edition"
    (223, 233, 238)
    Rule: synonym rotation (two names for one artifact, both inside the
    Tip at 238). Severity: should.
    Fix: name it once as "the source edition, a zip of the files that Git
    tracks" at 223, and use "the source edition" in prose after that.
    Keep *dist/alice-source.zip* where the filename is the point.
    Example at 56: "Every edition except the Markdown edition and the
    source edition comes out of pandoc."

30. "The value falls on 16 July 2026." (111, footnote)
    Rule: era spelling (American date order). Severity: should.
    Fix: "The value falls on July 16, 2026."

31. "The page bundle and the print pack are both marked "no" in the
    published column, for different reasons." (268)
    Rule: hidden actor. Severity: should.
    Fix: "The registry marks both the page bundle and the print pack "no"
    in the published column, for different reasons."

32. "labels centred in small monospace" (83); "labelled" (83, 92, 325)
    Rule: era spelling (American spelling: "centered", "labeled").
    These are art comments and do not print, but the illustrator's
    captions may copy them. Severity: should.
    Fix: "labels centered in small monospace"; "labeled (a) and (b)
    beneath"; "labeled "pandoc runs in this order""; "an arc labeled
    "pass""; "a thin arc labeled "fail"".

33. "During that time the build prints nothing new and uses a full CPU,
    and it looks exactly like a hang." (170)
    Rule: rhythm (the Tip at 173 makes the same point as the dry
    understatement, so the body spends the joke first). Severity: may.
    Fix: "During that time the build prints nothing new and uses a full
    CPU."

34. "The box tells TeX that the label is one unbreakable unit." (137)
    Rule: one-line closer, weak (it restates "Without the box, a narrow
    column could hyphenate the word"). Severity: may.
    Fix: move the explanation forward and drop the closer: "The filter
    boxes each label in `\mbox`, which TeX treats as one unbreakable
    unit. Without the box, a narrow column could hyphenate the word. A
    caption once came out as "Fig-ure"."

35. "A shallow table of contents can no longer empty the List of
    Plates." (167)
    Rule: one-line closer, weak (it restates the fix in the sentence
    before). Severity: may.
    Fix: delete, or fold in: "The house TeX header now raises the depth
    inside the list file itself, so a shallow table of contents can no
    longer empty the List of Plates."

36. "The press generates them, and it generates them again for every
    pandoc build." (313)
    Rule: rhythm (says "generates" twice for one fact). Severity: may.
    Fix: "The press generates them again for every pandoc build."

37. "A verifier run on its own can pass a stale artifact." (296) and "It
    never built the print interior or the cover wrap." (350)
    Rule: admonition that repeats the paragraph above it (style guide
    8.1). Each Warning is otherwise sound. Severity: may.
    Fix: delete the last sentence of the Warning at 296. At 350: "Do not
    take a green `press all` as proof that the print pack is ready. Run
    `press verify-print` before you send anything to a printer."

38. "epubcheck is "the tool retail channels run", so the press writes the
    date itself." (192) and "cannot survive". An index file" (319)
    Rule: rhythm (punctuation: American style sets the comma and the
    period inside the closing quotation mark, and 401 already does).
    Severity: may. Follow whatever the book settles book-wide.
    Fix: "epubcheck is "the tool retail channels run," so the press
    writes the date itself." and "... so stale copies cannot survive.""

39. "Since version 3.0.2, CI requires those tests to run, ..." (143)
    Rule: era touch ("At the time of this writing" before any version
    claim, style guide 8.2). Severity: may.
    Fix: "At the time of this writing, CI requires those tests to run,
    starting with version 3.0.2, through the `PRESS_REQUIRE_LUA=1`
    setting, and it holds a line-coverage floor for each filter."

40. "latexmk runs LuaLaTeX as many times as the document needs." (162);
    "runs pdftoppm over it" (397)
    Rule: era touch (man-page references such as latexmk(1)). Severity:
    may.
    Fix: "latexmk(1) runs LuaLaTeX as many times as the document needs."
    and "runs pdftoppm(1) over it with the options `-png -r 160`."

41. "Because the target builds the PDF first, the pictures always show
    the current manuscript." (397)
    Rule: synonym rotation ("pictures" for the PNG files; "picture" is
    on the never list for plate, and "image" is the word for the file).
    Severity: may.
    Fix: "Because the target builds the PDF first, the images always show
    the current manuscript."

42. "Eight artifacts need nothing first, and the sources companion needs
    the Markdown edition." (266)
    Rule: rhythm (the table shows nine artifacts with no prerequisite;
    the sentence means the eight published ones, and the print interior
    comes two sentences later). Severity: may.
    Fix: "Eight published artifacts need nothing first, and the sources
    companion needs the Markdown edition."

43. "When a target times more than one step, the registry ends with a
    summary line that starts with `press timings:`." (359)
    Rule: hidden actor, weak (a registry does not "end with" a line; it
    prints one). Severity: may.
    Fix: "When a target times more than one step, the registry prints a
    summary line at the end that starts with `press timings:`."

44. "`press clean` throws the results away." (355)
    Rule: wrong term, weak ("results" for the artifacts and the
    intermediate files). Severity: may.
    Fix: "and `press clean` throws *build/* and *dist/* away."

45. "a file that a book may or may not supply" (88); "On a book fresh
    from `press new`, ..." (405)
    Rule: wrong term, weak ("book" for the book repository). Severity:
    may.
    Fix: "a file that a book repository can leave out" and "In a book
    repository fresh from `press new`, the only file is the placeholder
    preface:"

46. "The first is a rights line, passed as metadata in this form:" (180)
    Rule: hidden actor, weak. Severity: may.
    Fix: "The first is a rights line, which the press passes as metadata
    in this form:"

47. "The last step behaves differently on `hatter` and on a release
    build." (339)
    Rule: rhythm (a workstation set against a kind of build). Severity:
    may.
    Fix: "The last step behaves differently in an ordinary build on
    `hatter` and in a release build."

## Fact notes (for the fact checker; not edited)

- "`press markdown` is the only edition target that does not call
  pandoc." (227) Line 56 says the source zip also does not come out of
  pandoc, and line 223 calls it the source edition. Fact: see fact
  checker.
- "a stray asterisk that the float package's `\caption*` printed above
  placed figures" (139). The Chapter 4 copyedit raised the same doubt:
  `\caption*` usually comes from the caption package. Fact: see fact
  checker.

## Other checks

- Second person and present tense hold throughout. The chapter has no
  "we" and no "I".
- Dry understatement appears at 137 ("Fig-ure"), 143 ("without a word"),
  and 173 ("a very convincing imitation"), about once every few pages and
  never in a heading. Item 33 keeps the 173 line from being spent early.
- Admonitions: three Warnings (146, 296, 350) and two Tips (173, 238),
  each imperative and under four sentences. Items 18 and 37 cover the
  repetition.
- Footnotes (four: 111, 139, 196, 401) carry history and asides. The
  body needs none of them.
- Spelling: "e-mail" (204), "Web site" (200, 268), and "toward" (413) are
  correct. "file names" (item 5) is the one slip in prose. No "Unix",
  "manpage", or "appendixes" occasion arises in prose; "appendices" at 62
  is in code and at 319 is inside a quotation, so both stay. British
  forms appear only in the art comments (item 32), plus the date order in
  item 30.
- Numbers: under ten spelled out in prose throughout. Numerals appear
  only in versions, measurements (quality 70, 80 columns, 160 dots per
  inch, 2 pt), table and figure numbers, the date, and code.
- No semicolons, dashes, perfect tenses, hedge stacks, assistant
  vocabulary, "not X but Y", -ing riders, title-case headings, or noun
  stacks over three in prose.
