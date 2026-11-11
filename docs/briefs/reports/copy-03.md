# Copyedit report: Chapter 3, "The shape of a book repository"

File: `book/chapters/03-the-shape-of-a-book.md`. Read against
`docs/prose-contract.md`, `docs/style-guide.md` sections 3, 4, and 8, and
`docs/vocabulary.md`. Line numbers refer to the file as it stands.

## Checker leads

`python3 tools/ste_check.py book/chapters/03-the-shape-of-a-book.md`: 38
findings, 439 sentences, average 11.9 words, maximum 46. After a reading,
most of them are false positives:

- The sentence-length and paragraph-length hits at lines 6, 72, 361, 552,
  and 599 are the in-this-chapter box, the art-direction comments, and the
  index comment. None of them is prose.
- The semicolons at lines 272, 406, and 599 are inside quoted press messages
  (the trim refusal, the placeholder paragraph) or the index comment. None
  is a semicolon in prose.
- The passive at 229 ("Facts are stated once") is a quotation. The passive
  at 63 ("as if it were permanent") is a subjunctive.
- The `-ing` hits are headings, captions, and gerunds ("Scaffolding a
  book", "by finding", "starting with a letter"). None of them is an
  -ing rider.
- "therefore" and "however" are period-correct (contract, the 80% rule).
- The hits that hold up (lines 233, 359, 540, 573) appear below as items.

No sentence of prose runs past 30 words. Prose has no semicolons, no dashes,
and no hedges. The press's `banned-patterns` set finds nothing in the
chapter. The real findings are about vocabulary and sentence structure.

## Findings

1. Line 478: "The self-test line says that every known-bad fixture the press
   ships still trips the rule it declares, ..."
   Rule: assistant vocabulary ("ship" is engineering jargon on press's
   watchlist and on the contract's one-sighting list. The book's
   `jargon-allow` admits it only as a press name, and this sentence uses it
   as a verb of delivery.) Severity: blocks.
   Fix: "The self-test line says that every known-bad fixture that comes with the press still trips the rule it declares."

2. Line 478: "..., which proves the checker still works before it judges
   your manuscript."
   Rule: two ideas. Severity: should.
   Fix: "That line proves the checker works before it judges your manuscript."

3. Line 17: "The press creates that directory for you, names every file in
   it, and refuses to build in a directory without that file."
   Rule: two ideas (three actions in one sentence, and "that file" has no
   clear antecedent). Severity: should.
   Fix: "The press creates that directory for you and names every file in it. It refuses to build in a directory that has no *config/metadata.yaml*."

4. Line 66: "The new directory is a plain directory, with no repository
   inside it yet."
   Rule: wrong term ("repository" alone collides with *book repository*,
   which the chapter defines eight lines up). Severity: should.
   Fix: "The new directory is a plain directory, with no git repository inside it yet."

5. Line 122: "A book grows other files as its author asks more of the
   press, and each consumer of an optional file builds without it."
   Rule: two ideas (and "each consumer ... builds without it" is unclear).
   Severity: should.
   Fix: "A book grows other files as its author asks more of the press. Every target that reads one of these optional files still builds when the file is absent."

6. Line 129: "The directory *tests/known-bad/* holds fixtures that prove the
   book's own house rules still fire."
   Rule: wrong term (the term is *known-bad fixture*, and "fire" is on the
   never-list beside "run"). Severity: should.
   Fix: "The directory *tests/known-bad/* holds known-bad fixtures, which prove that the book's own house rules still reject what they should."

7. Line 192: "The title, the author, and the slug are the three fields the
   model insists on."
   Rule: synonym rotation (Tables 3.3 and 3.4 say "The model needs it"
   every time). Severity: should.
   Fix: "The model needs three fields: the title, the author, and the slug."

8. Line 233: "...must find, character for character, in the source and in
   every artifact."
   Rule: wrong term ("the source" is on the never-list for the manuscript.
   Table 3.4 says "in the manuscript"). Severity: should.
   Fix: "A *sentinel* is a phrase from your manuscript that the verifiers must find, character for character, in the manuscript and in every artifact."

9. Line 233: "If the PDF, the EPUB, or the plain-text edition lost a chapter
   on the way out, a sentinel from that chapter would go missing, and the
   verifier would fail."
   Rule: two ideas (29 words, the conditional "would" where the contract
   allows only simple tenses, and "plain-text edition" against the
   registry's name, the Telegraphic edition). Severity: should.
   Fix: "If the PDF, the EPUB, or the Telegraphic edition loses a chapter on the way out, a sentinel from that chapter goes missing. The verifier then fails."

10. Line 238 (Warning): "A chapter opening can split the first word into a
    large initial and small capitals, and then the PDF no longer contains
    the phrase as you typed it."
    Rule: wrong term ("initial" is on the never-list under *chapter
    opening*) and two ideas. Severity: should.
    Fix: "A chapter opening can set the first word as one large capital followed by small capitals. The PDF then no longer contains the phrase as you typed it."

11. Line 266 (Table 3.5): "The number of text lines the initial spans."
    Rule: wrong term (as in item 10). Severity: should.
    Fix: "The number of text lines the large first letter spans."

12. Line 243: "The press then refuses *vacuous witnesses*, which are
    sentinels and a page floor too weak to prove anything."
    Rule: wrong term (the vocabulary reserves *witness* for the manuscript
    and chapter witness line. The press's own message in Example 3.4 says
    "its witnesses are vacuous", so the term cannot leave the text). Severity:
    should. Resolve it in `docs/vocabulary.md` with a "vacuous witness" entry
    rather than by rewording the press's message.
    Fix: "The press then refuses *vacuous witnesses*: sentinels and a page floor too weak to prove anything."

13. Line 272: "An older book that still carries a `trim` mapping keeps it,
    but the press only checks it against the profile and refuses the
    metadata when the two disagree."
    Rule: two ideas. Severity: should.
    Fix: "An older book that still carries a `trim` mapping keeps it. The press checks that mapping against the profile and refuses the metadata when the two disagree."

14. Line 309 (Table 3.6): "dedication, epigraph, acknowledgements, and the
    colophon lines"
    Rule: era spelling (American "acknowledgments", as style guide 7 spells
    the heading. If the YAML key is meant, set it in code.) Severity: should.
    Fix: "`edition-note` through `motto`: the dedication, the epigraph, the acknowledgments, and the colophon lines"

15. Line 350 (Warning): "The press skips any other Markdown file in those
    two directories, and it says nothing about it."
    Rule: admonition tone (style guide 3.4: imperative and specific. This
    warning gives no instruction) and two ideas. Severity: should.
    Fix: "Start every chapter filename with a digit and every appendix filename with a letter and a hyphen. The press skips any other Markdown file in those two directories without a message, so a chapter saved as *chapter-two.md* or *2.md.txt* never reaches the book."

16. Line 382: "The `press add` target turns the name into a filename slug."
    and "...and it sentence-cases a bare slug." (also line 406, "sentence-cased
    from the bare slug")
    Rule: wrong term (*slug* is defined at line 60 as the book's slug, the
    basename of every artifact. One term per thing.) Severity: should.
    Fix: "The `press add` target turns the name into a filename." / "For the heading, it keeps a human title exactly as you typed it, and it sentence-cases a name typed in filename form, such as `the-pool-of-tears`." / "The second gets `# The pool of tears`, sentence-cased from the filename form."

17. Line 411 (Warning): "It refuses to overwrite an existing file and exits
    with status 1, and a usage mistake exits with status 2."
    Rule: two ideas. Severity: should.
    Fix: "It refuses to overwrite an existing file and exits with status 1. A usage mistake exits with status 2."

18. Line 434: "...and for those you call `press` itself."
    Rule: wrong term (the vocabulary uses *run*, never execute or invoke.
    "call" is a synonym of invoke). Severity: should.
    Fix: "The press has more, such as `print` and `coverwrap` for the print pack, and for those you run `press` itself."

19. Lines 454 and 458 (sidebar): "...at the exact ref the book's workflow
    names" and "...match the ref the workflow names."
    Rule: wrong term (*workflow* is a packaged agent procedure. The book's
    GitHub file is "the CI file" at line 513, and *build.yml* is "the
    reusable workflow"). Severity: should. Also fact: see fact checker. The
    book's CI file names *build.yml* at `v3`, and *build.yml* pins the
    composite action, so the ref the action checks out may be the one the
    reusable workflow names.
    Fix: "The composite action checks out the press at the exact ref that the reusable workflow pins, and it installs the press from that checkout." / "...so the two always match that ref."

20. Line 507: "The `.gitignore` the scaffold writes works with this rule,
    because git never tracks *build/* or *dist/*, so a Source edition cannot
    contain an old build."
    Rule: two ideas (a because-so chain). "an old build" is also a wrong term
    because *artifact* never appears as "build". Severity: should.
    Fix: "The `.gitignore` the scaffold writes keeps *build/* and *dist/* out of git. A Source edition therefore cannot contain old artifacts."

21. Line 510 (Tip): "The Source edition takes the manuscript from git, and it
    holds only what git tracks."
    Rule: admonition repeats the paragraph above it (style guide 8.1).
    Severity: should.
    Fix: "**Tip:** Run `git add` on every new chapter file before a full build."

22. Line 540: "On the CI host, which in our examples is `printshop`, the job
    runs inside the toolchain image, pinned by digest to the bytes the
    release contract proved."
    Rule: hidden actor (who pins the image) and two ideas. Severity: should.
    Fix: "On the CI host, which in our examples is `printshop`, the job runs inside the toolchain image. The reusable workflow pins that image by digest to the bytes the release contract proved."

23. Line 542: "A tag push does two more things. It sets `PRESS_RELEASE=1`,
    which turns on the release refusal of Example 3.4, and it makes CI take
    the tag's section of *CHANGELOG.md* as the release notes."
    Rule: hidden actor (line 243 says CI sets the variable, but here the tag
    push sets it) and two ideas. Severity: should.
    Fix: "On a tag push, CI does two more things. It sets `PRESS_RELEASE=1`, which turns on the release refusal of Example 3.4. It also takes the tag's section of *CHANGELOG.md* as the release notes."

24. Line 557: "The Markdown file is the Manuscript edition, which press
    stitches together from your source files without running them through
    pandoc."
    Rule: wrong term ("source" for the manuscript files). Severity: should.
    Fix: "The Markdown file is the Manuscript edition, which press stitches together from your chapter files and appendix files without running them through pandoc."

25. Line 557: "Each file at the top of *dist/* is one edition, and the
    registry gives each edition a name."
    Rule: fact: see fact checker. Line 559 puts *alice-sources.md* at the top
    of *dist/* and does not call it an edition. Severity: should (as an
    internal contradiction).
    Fix: left to the fact checker.

26. Line 573: "Verifying an old *dist/* without rebuilding it proves only
    that last week's files were good, and a verifier that passes them
    blesses artifacts that no longer match the manuscript."
    Rule: two ideas (29 words). Severity: should.
    Fix: "A verifier run over an old *dist/* proves only that last week's files were good. When it passes them, it blesses artifacts that no longer match the manuscript."

27. Line 573: "...so that a build target runs before the verifier that inspects
    its output."
    Rule: wrong term ("output" is on the never-list for *artifact*).
    Severity: should.
    Fix: "The press now wires its targets to their dependencies so that a build target runs before the verifier that inspects its artifact."

28. Line 589: "...and the art commission writes candidate images under
    *art/candidates/*."
    Rule: wrong term (a *commission* is a prompt in *art/commissions.md*.
    A prompt writes nothing). Severity: should. Also fact: see fact checker
    for which command writes the candidates.
    Fix: "The `press migrate` target writes *.press/migration-receipt.json*, and the art commands write candidate images under *art/candidates/*."

29. Line 58: "The order matters for the second step."
    Rule: synonym rotation (the list was introduced as "six things", and
    "step" is on the never-list near *target*). Severity: may.
    Fix: "The order matters most for the second of the six."

30. Line 21: "...and four options that fill in the identity of the book."
    Rule: phrasal verb in place of a plain verb (S-rule, "the action in the
    verb"). Severity: may.
    Fix: "It takes one argument, the directory to create, and four options that set the identity of the book."

31. Line 93: "A mismatch shows that your copy came from an older or newer
    press."
    Rule: hidden actor (it does not say what the stamp mismatches).
    Severity: may.
    Fix: "A stamp that names a different version from the press you run shows that your copy came from an older or newer press."

32. Line 137: "Example 3.3 shows the file as `press new alice` writes it,
    with the placeholders filled. The real file continues past the last
    line shown with a long commented block..."
    Rule: hidden actor ("filled" by whom). "shown with" is also a
    misplaced modifier that reads as "the line shown with a block".
    Severity: may.
    Fix: "Example 3.3 shows the file as `press new alice` writes it, after the scaffold fills the placeholders. Past the last line shown, the real file continues with a long commented block for direct print ordering, which Chapter 12, *The print pack*, covers."

33. Line 197 (Table 3.3): "If it holds "or," clauses, the title page and the
    landing page stack them on separate lines."
    Rule: noun stack ("or," used as a modifier, which is hard to read).
    Severity: may. Fact: see fact checker for the exact separator press
    splits on.
    Fix: "If it joins clauses with "or," the title page and the landing page stack them on separate lines."

34. Line 222 (Table 3.4): "...the landing page leaves out its paragraph
    about the source."
    Rule: wrong term ("the source" is ambiguous beside the Source edition and
    the manuscript). Severity: may.
    Fix: "Without it, the landing page leaves out its paragraph about the source repository."

35. Line 272: "Chapter 9, *The house design*, covers the profiles and chapter
    openings, Chapter 12 covers the print fields, and Chapter 13,
    *Registrations*, covers the numbers."
    Rule: two ideas (three clauses). Severity: may.
    Fix: "Chapter 9, *The house design*, covers the profiles and chapter openings. Chapter 12 covers the print fields, and Chapter 13, *Registrations*, covers the numbers."

36. Line 282: "For the metadata file, that model includes the commerce and
    registration rules, and for the house rules, it compiles each regular
    expression."
    Rule: two ideas. Severity: may.
    Fix: "For the metadata file, that model includes the commerce and registration rules. For the house rules, it compiles each regular expression."

37. Line 299: "Two rules govern the values you type." The paragraph then
    gives three (lists and mappings, booleans, fixed choices).
    Rule: wrong term (the count does not match). Severity: may.
    Fix: "Three rules govern the values you type."

38. Line 316: "...the index terms, the authorities ledger, and the
    qualification records."
    Rule: synonym rotation (the chapter says "the table of authorities" at
    lines 124 and 559). Severity: may.
    Fix: "A *structured* field holds a list that is too rich for one command line: the index terms, the table of authorities, and the qualification records."

39. Line 318: "...and a one-line description, which makes it the quickest
    reference while you work."
    Rule: two ideas (a ", which makes" tail clause). Severity: may.
    Fix: "The `press config list` target prints every field with its type and a one-line description. It is the quickest reference while you work."

40. Line 359: "The `press add appendix` target takes the next unused letter,
    ..." / "The generated subject index takes the first free letter ..."
    Rule: synonym rotation (unused / free). Severity: may.
    Fix: "The `press add appendix` target takes the next free letter, counting down from `z`."

41. Line 370: "What keeps such a chapter out of the numbering is its
    heading."
    Rule: staged run-up (a cleft that delays the subject). Severity: may.
    Fix: "Its heading keeps such a chapter out of the numbering."

42. Line 382: "A chapter gets the number one past the highest existing
    chapter, zero-padded to at least two digits, and the first chapter of a
    book is `01`."
    Rule: two ideas. Severity: may.
    Fix: "A chapter gets the number one past the highest existing chapter, zero-padded to at least two digits. The first chapter of a book is `01`."

43. Line 434: "The Makefile names sixteen targets."
    Rule: number style (the brief allows numerals for ten and up, and the
    chapter writes "26 letters" and "79 lines"). Severity: may.
    Fix: "The Makefile names 16 targets."

44. Line 490: "It looks like a hang. It is not one, although it is a
    convincing imitation."
    Rule: scar paragraph without its rule (style guide 3.3: a short story
    with a cost, then the rule). It is also the style guide's own
    calibration line, nearly word for word. Severity: may.
    Fix: "The first time LuaLaTeX runs on a new machine, it scans the system fonts, and that scan takes several minutes. It is not a hang, although it is a convincing imitation of one. Let it finish."

45. Line 540: "The file builds the book on a push to any branch, ..."
    Rule: hidden actor (the file does not build anything. CI builds).
    Severity: may.
    Fix: "With this file, CI builds the book on a push to any branch, on any tag that starts with `v`, on every pull request, and on demand from the GitHub interface."

46. Line 563: "...and every download under *downloads/*, each linked
    exactly once."
    Rule: hidden actor. Severity: may.
    Fix: "It holds the landing page, a copy of the reader under *read/*, and every download under *downloads/*. The landing page links each download exactly once."

47. Lines 581, 583, and 584: "The files *front-matter.tex*, *aesthetic.tex*,
    ..." and "...and *build/cover-fragment.html* sits beside it." / "...and
    *build/verify-text.txt* sits beside it."
    Rule: code typography (line 581 drops the *build/* prefix that every
    other item carries), and "sits beside it" says nothing about the file.
    Severity: may. Fact: see fact checker for what each of the two files
    holds.
    Fix: "The files *build/front-matter.tex*, *build/aesthetic.tex*, *build/profile-geometry.tex*, and *build/profile-dropcap.tex* hold the TeX the press generates from your config." (Give the other two files their own clauses once the fact checker supplies what they hold.)

48. Line 593 (footnote): "Pandoc emits an empty `dc:date` element, and
    epubcheck, the validator the retail channels run, rejects it under its
    rule RSC-005."
    Rule: synonym rotation (the body at line 210 says "writes", and the
    vocabulary never uses "validator"). The footnote also repeats the
    body. Severity: may.
    Fix: "Epubcheck, the tool the retail channels run, rejects the empty `dc:date` element under its rule RSC-005. The press writes the year it extracts into *build/epub-metadata.xml*."

49. Lines 546 and 565 (headings): "Where things go: build and dist" and
    "Files press all does not make".
    Rule: code typography (style guide 4: literal names in constant width,
    with directories in italic as the body sets them). Severity: may.
    Fix: "Where things go: *build/* and *dist/*" / "Files `press all` does not make"

50. Tables 3.2 and 3.3, Meaning column: "Four agent workflows.", "The whole
    CI for the book.", "A one-paragraph preface.", "Subject keywords, which
    press passes to the editions.", and others.
    Rule: table cells (style guide 3.7: "Cells hold sentences, not
    fragments, in the Meaning column"). Severity: may.
    Fix (two examples): "It is the whole CI for the book. It calls the press's reusable workflow at the floating tag `v3`." / "It holds subject keywords, which press passes to the editions."

## Other checks

- Second person and present tense: these hold throughout, except for the
  conditional in item 9.
- "We": lines 39, 235, 465, and 540 use it for the authors' editorial acts
  (shortening, choosing, eliding, the sample network). That use is
  acceptable. The chapter has no "I".
- Dry understatement: it appears at lines 49, 110, 188, 418, 465 ("runs
  happily"), and 490, which is about six in roughly a dozen pages. That is
  at the dense end of "one every few pages". We suggest cutting "happily"
  at line 465. No heading carries a joke.
- Admonitions: there are eight (four Tips, four Warnings), all under four
  sentences. The exceptions are items 15 (not imperative) and 21 (repeats
  the paragraph).
- Footnotes: there are three, and each carries an aside. The body does not
  depend on any of them. Item 48 covers the duplicate in [^epubdate].
- Spelling: the chapter uses "appendixes" in prose ("appendices" only in
  code and quoted messages), "filename", "Web", and "afterward". The one
  British spelling is "acknowledgements" (item 14). The chapter does not use
  "Unix", "e-mail", "manpage", or "toward".
- Numbers: the chapter spells out numbers under ten in prose. Item 43 is
  the only inconsistency. Sentinels and messages quoted with the period
  outside the quotation marks (lines 235, 408) follow logical punctuation
  for literal strings. We leave them as they are.
- Title case: headings and captions are sentence case throughout.

## Counts

- blocks: 1
- should: 27
- may: 22

Most frequent rules broken: two ideas (16 items), wrong term (15), hidden
actor (6).
