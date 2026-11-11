# Copyedit: Chapter 6, Checking the manuscript

File: `book/chapters/06-checking-the-manuscript.md`

## Status

REVISE. Ten blocks, all of them the watchlist word "ship" ("ships",
"shipped") in prose, captions, a footnote, and the sidebar title. That
word is on the contract's one-sighting list even though the book's
`jargon-allow` lets it through. `press style` reports nothing in this
file. The repository's check fails only on Chapter 2, at lines 322 and
324. The jargon lint reports `ship`/`shipped` as inspect sightings (118,
260, 263, 267, 269). The blocks come from the contract, not from the
checker.

Counts by severity: blocks 10, should 33, may 12.

Most frequent rules broken: wrong term (11), watchlist jargon "ship"
(10), two ideas (7). Next come meta-narration and synonym rotation (5
each).

## ste_check findings, judged

- Sentence length (6, 38, 72, 97, 112, 142, 211, 221, 241, 353, 454,
  534): accepted. These are the In-this-chapter list, the art comments,
  the index comment, footnote fusions (142, 241), or sentences at or
  under 30 words. No prose sentence goes over 30 words.
- Paragraph length: accepted for 38, 97, 454 (art comments). **Rejected
  for 51 and 211.** Both are prose paragraphs of eight sentences (items
  27 and 28).
- Semicolons (519, 534): accepted. 519 is the verbatim scars-list quote,
  and 534 is the index comment. There is no semicolon in prose.
- Passive "be determined" (51) and "is malformed" (318): accepted. The
  first is a quoted phrase, and the second is adjectival.
- `-ing` forms (1, 70, 89, 279, 316, 382, 390, 431, 457, 534): accepted,
  except 89 (item 45). The rest are headings, chapter titles, the term
  "wiring", "including case", and "trailing".
- "therefore" (21, 89, 221), "however" (229), "whether" (98, 254):
  accepted. The contract allows them.

## Voice and era checks (no finding)

Second person and present tense hold throughout. The chapter has no "we"
and no "I". It shows three dry understatements (213 copyright sign, 374
bridge spine, 429 "print Example 6.11 at you"), and none is in a heading.
Three tips and three warnings: all imperative, all under four sentences.
Four footnotes. Spelling is American. "filename" is correct throughout.
"appendices" appears only as the literal directory name in Example 6.8
and line 378. Headings are in sentence case.

## Findings

### Blocks

1. "Press ships 19 of them in its package data, under
   *src/press/data/known-bad/*, and it also reads every Markdown file in
   your book's *tests/known-bad/* directory." (74)
   Rule: watchlist jargon ("ships"). Severity: blocks.
   Fix: "Press carries 19 of them in its package data, under
   *src/press/data/known-bad/*, and it also reads every Markdown file in
   your book's *tests/known-bad/* directory."

2. "The press also ships one *known-good fixture*,
   *src/press/data/known-good/clean.md*." (91)
   Rule: watchlist jargon ("ships"). Severity: blocks.
   Fix: "The press package also holds one *known-good fixture*,
   *src/press/data/known-good/clean.md*."

3. "Table 6.3 lists 17 of the 19 fixtures that ship with press, with the
   rule each one declares." (118)
   Rule: watchlist jargon ("ship"). Severity: blocks.
   Fix: "Table 6.3 lists 17 of the 19 packaged fixtures, with the rule each
   one declares."

4. "Table: Table 6.3. Seventeen of the known-bad fixtures press ships"
   (140)
   Rule: watchlist jargon ("ships"), in a caption. Severity: blocks.
   Fix: "Table: Table 6.3. Seventeen of the packaged known-bad fixtures"

5. "No rule in the shipped watchlist has this status." (260, Table 6.5)
   Rule: watchlist jargon ("shipped"). Severity: blocks.
   Fix: "No rule in the packaged watchlist has this status."

6. "No shipped rule has this status." (263, Table 6.5)
   Rule: watchlist jargon ("shipped"). Severity: blocks.
   Fix: "No packaged rule has this status."

7. "The shipped watchlist has 39 `inspect` rules and 14 `rewrite` rules."
   (267)
   Rule: watchlist jargon ("shipped"). Severity: blocks.
   Fix: "The packaged watchlist has 39 `inspect` rules and 14 `rewrite`
   rules."

8. "**Example 6.5. The rewrite terms in the shipped watchlist**" (269)
   Rule: watchlist jargon ("shipped"), in a caption. Severity: blocks.
   Fix: "**Example 6.5. The rewrite terms in the packaged watchlist**"

9. "One copy lives in the press package, and a portable copy ships inside
   the overused-jargon skill, so that the skill works without press
   installed." (324, footnote)
   Rule: watchlist jargon ("ships"). Severity: blocks.
   Fix: "One copy lives in the press package, and a portable copy lives
   inside the overused-jargon skill, so that the skill works without
   press installed."

10. "**The red check that shipped green**" (517, sidebar title)
    Rule: watchlist jargon ("shipped"), in a title. The scars-list quote
    at 519 is verbatim and stays. Severity: blocks.
    Fix: "**The red check that went out green**"

### Should

11. "It reads source and configuration only, and it runs four passes in a
    fixed order, and it stops at the first pass that fails." (21)
    Rule: two ideas (three clauses joined by "and"), and wrong term
    ("source" for the manuscript). Severity: should.
    Fix: "It reads only the manuscript and its configuration. It runs four
    passes in a fixed order and stops at the first pass that fails."

12. "Everything to the left of the large box is source." (36)
    Rule: wrong term ("source"). Severity: should.
    Fix: "Everything to the left of the large box is the manuscript and its
    configuration."

13. "A curly quote in the source is usually a paste from a word processor."
    (209)
    Rule: wrong term ("the source"). Severity: should.
    Fix: "A curly quote in a chapter file is usually a paste from a word
    processor."

14. "Keep sidebars and art directives short for that reason, or the
    checker will refuse a block that looks innocent in the source." (229)
    Rule: wrong term ("the source"), plus synonym rotation ("art
    directives" after "`art:` comment" in the sentence before).
    Severity: should.
    Fix: "Keep sidebars and art comments short for that reason, or the
    checker will refuse a block that looks innocent in the chapter file."

15. "The self-test comes second, because a rule that cannot fail would let
    a broken manuscript through." (34)
    Rule: synonym rotation. The second pass goes by "Checking the
    checkers" (Table 6.1, heading), `check_the_checkers` (72), and
    "the self-test" (34, 89, 100, 114, 151, 452). "Self-test" appears
    before anything defines it, and nothing ties it to the pass.
    Severity: should.
    Fix (at 72): "The second pass, `check_the_checkers`, is the *self-test*,
    and it tests that claim on every run." (At 34 use "The second pass
    comes second, because a rule that cannot fail would let a broken
    manuscript through." or move the term's first use to 72.)

16. "A file in the package data, *src/press/data/known-bad/expected.yaml*,
    maps each fixture to its checker and its diagnostic." (142)
    Rule: wrong term ("checker" is reserved for `press check`).
    Severity: should.
    Fix: "A file in the package data,
    *src/press/data/known-bad/expected.yaml*, maps each fixture to the
    rule that must refuse it and to that rule's diagnostic."

17. "A note count that rises after you add a rule means your rule overlaps
    a house rule." (148)
    Rule: wrong term ("house rules" means *config/house-rules.yaml*,
    which is the reader's own rule here. The packaged rule belongs to
    "the house"). Severity: should.
    Fix: "A note count that rises after you add a rule means your rule
    overlaps one of the house's own rules."

18. "If the regex is wrong, the self-test tells you before the pattern
    reads a single chapter." (151, tip)
    Rule: synonym rotation ("regex" beside "pattern" and "regular
    expression"). Severity: should.
    Fix: "If the pattern is wrong, the self-test tells you before it reads
    a single chapter."

19. "Its word boundaries refuse a match against a neighboring word
    character or hyphen, so the term "gate" never matches the word
    "gateway"." (314)
    Rule: wrong term ("refuse" is reserved for press stopping with a
    message). Severity: should.
    Fix: "Its word boundaries allow no match next to a word character or a
    hyphen, so the term "gate" never matches the word "gateway"."

20. "A test in the press's own self-test requires the two copies to match
    byte for byte, function by function, except for the function that
    parses the command line." (324, footnote)
    Rule: wrong term ("self-test" is this chapter's name for the second
    pass of `press check`). Severity: should.
    Fix: "A test in the press's own test suite requires the two copies to
    match byte for byte, function by function, except for the function
    that parses the command line." (If the test is in `press selftest`,
    name the command in code type. Fact: see fact checker.)

21. "The CI build sets `PRESS_RELEASE=1` when it builds a tag that begins
    with `v`." (417)
    Rule: wrong term (the vocabulary's name is "the reusable workflow").
    Severity: should.
    Fix: "The reusable workflow sets `PRESS_RELEASE=1` when it builds a tag
    that begins with `v`."

22. "It refuses vacuous witnesses with the message in Example 6.11." (417)
    Rule: undefined term ("witnesses" is never defined. The vocabulary
    term is "release witnesses"). Severity: should.
    Fix: "Press calls the two settings the *release witnesses*, and it
    refuses vacuous ones with the message in Example 6.11."

23. "The command line declares dependency edges between its targets, and
    the same edges keep a verifier from blessing an edition that the
    current manuscript did not produce." (496)
    Rule: wrong term ("the command line" is the shell. The actor is
    press), and two ideas. Severity: should.
    Fix: "Press declares dependency edges between its targets. The same
    edges keep a verifier from blessing an edition that the current
    manuscript did not produce."

24. "A paragraph must run under 190 words, and for a longer one the audit
    prints a message of this form." (223)
    Rule: undefined term ("paragraph law" appears in footnote 237 and the
    index but is never defined), and wrong term ("longer" for "190 words
    or more", as Table 6.7 states it). Severity: should.
    Fix: "The *paragraph law* requires every paragraph to run under 190
    words. For a paragraph of 190 words or more, the audit prints a
    message of this form."

25. "`verify-min-pages` is the PDF's page floor, the fewest pages the PDF
    verifier accepts." (411)
    Rule: undefined term (an index term, defined here but not in
    italic). Severity: should.
    Fix: "`verify-min-pages` is the PDF's *page floor*, the fewest pages
    the PDF verifier accepts."

26. "Example 6.15 shows the chain that the press's scars list warns
    about." (506)
    Rule: undefined term ("scars list" appears here and the sidebar
    defines "scars" after it). Severity: should.
    Fix: "Example 6.15 shows the chain that the press's list of *scars*,
    the production failures it turned into guards, warns about." (Then
    the sidebar at 519 can drop its own definition.)

27. Paragraph at 51 ("For each chapter file, the source checks look for
    four faults. ... because the checker reads examples for them too.")
    Rule: paragraph over six sentences (eight). Severity: should.
    Fix: end the paragraph after "...and quotes the marker." Start a new
    paragraph with "Two of the markers are placeholders: ..."

28. Paragraph at 211 ("The second is the *glyph law*, ... with the code
    point in place of the four letters.")
    Rule: paragraph over six sentences (eight). Severity: should.
    Fix: end the paragraph after "...and also the multiplication and
    division signs." Start a new paragraph with "The audit refuses
    everything from U+00A0 to U+00BF."

29. "This chapter cannot show the three markers, even in an example,
    because the checker reads examples for them too." (51)
    Rule: meta-narration (text about the document itself). Graded should,
    not blocks. The sentence carries a fact about the checker, and the
    fix keeps that fact. Severity: should.
    Fix: "The source checks read fenced code for the markers too, so not
    even an example can hold one."

30. "Their filenames repeat the phrases they hold, and this book's own
    house rules refuse those words even in a filename, so the table
    leaves them out." (118)
    Rule: meta-narration, and two ideas. Severity: should.
    Fix: "Their filenames repeat the phrases they hold. A book whose banned
    patterns refuse those words cannot name the files even in inline
    code, and this book has such patterns."

31. "The table describes the phrases instead of quoting them, because this
    chapter is itself audited." (166)
    Rule: meta-narration. Severity: should.
    Fix: "The audit would refuse a chapter that quoted these phrases in
    prose, so Table 6.4 describes them and Example 6.3 gives them in
    fenced code."

32. "They sit in a code block because the lint would refuse this
    paragraph if they did not." (267)
    Rule: meta-narration. Severity: should.
    Fix: "The lint skips fenced code, so Example 6.5 can list the terms
    and a paragraph cannot."

33. "You set them before any edition exists, and this chapter introduces
    them because the checker reads one of them." (382)
    Rule: meta-narration, and two ideas. Severity: should.
    Fix: "You set them before any edition exists, and the checker reads
    one of them."

34. "The default is `rewrite`, and press check uses it, so an inspect term
    appears in the report and does not fail the check." (267)
    Rule: code typography (the command in roman). Severity: should.
    Fix: "The default is `rewrite`, and `press check` uses it, so an
    inspect term appears in the report and does not fail the check."

35. "The checker's part is the cheap one: it catches a sentinel that a
    revision has already removed, before you spend a build on it." (388)
    Rule: perfect tense. Severity: should.
    Fix: "The checker's part is the cheap one: it catches a sentinel that a
    revision removed, before you spend a build on it."

36. "The press keeps a list of scars, the production failures it has paid
    for once." (519, sidebar)
    Rule: perfect tense. Severity: should.
    Fix: "The press keeps a list of scars, the production failures it paid
    for once."

37. "The YAML file doubles each backslash because YAML reads the string
    first, so `\\b` in the file reaches the regular expression as `\b`, a
    word boundary." (353)
    Rule: hidden actor (the file does not double anything. You do), and
    two ideas. Severity: should.
    Fix: "Double each backslash in the YAML file, because YAML reads the
    string first. The `\\b` in the file reaches the regular expression as
    `\b`, a word boundary."

38. "When a shell runs a pipeline, the pipeline's status is the status of
    its last command, and every earlier status is lost." (506)
    Rule: hidden actor. Severity: should.
    Fix: "When a shell runs a pipeline, the pipeline's status is the status
    of its last command, and the shell discards every earlier status."

39. "A fresh scaffold prints 1, for the preface alone." (68)
    Rule: hidden actor (the check prints, not the scaffold). Severity:
    should.
    Fix: "In a fresh scaffold, the line reports 1, for the preface alone."

40. "The negative parallelism rule allows up to 120 characters between its
    two halves, and the dash rules match single characters." (183)
    Rule: two ideas (two unrelated facts). Severity: should.
    Fix: "The negative parallelism rule allows up to 120 characters between
    its two halves. The dash rules match single characters."

41. "Files there meet the dash rules and the phrase rules, and their
    heading and paragraph faults print as warnings, but the jargon lint
    does not read them." (378)
    Rule: two ideas (three clauses). Severity: should.
    Fix: "Files there meet the dash rules and the phrase rules, and their
    heading and paragraph faults print as warnings. The jargon lint does
    not read them."

42. "The chain depends on one thing: the status that reaches `&&` must be
    the checker's status, and a pipe breaks that." (506)
    Rule: two ideas, with a staged run-up ("depends on one thing:").
    Severity: should.
    Fix: "The chain works only if the checker's own status reaches the
    `&&`. A pipe breaks that."

43. "The scars list exists so that nobody has to learn this a second
    time." (523, last line of the sidebar)
    Rule: one-line closer (a moral at the end of a section, style guide
    8.1). Severity: should.
    Fix: delete it. The sidebar can end on "...and read its output when it
    fails."

### May

44. "If the fixture draws other diagnostics as well, press prints each one
    as a note and does not fail." (89)
    Rule: hidden actor (press does not "fail". The self-test passes).
    Severity: may.
    Fix: "If the fixture draws other diagnostics as well, press prints each
    one as a note, and the self-test still passes."

45. "The expected text must appear, ignoring case, as a substring of at
    least one diagnostic that the fixture draws." (89)
    Rule: -ing rider. Severity: may.
    Fix: "The expected text must appear as a substring of at least one
    diagnostic that the fixture draws, and case does not count."

46. "The title-case test is a count, and it is worth knowing exactly."
    (221)
    Rule: meta-narration (filler next to the throat-clearing form).
    Severity: may.
    Fix: "The title-case test is an exact count."

47. "Of the 53 rules, 45 match as words and 8 as phrases." (254)
    Rule: number style (under ten, in prose). Severity: may.
    Fix: "Of the 53 rules, 45 match as words and eight as phrases."

48. "The jargon pass never ran in Example 6.13." (474)
    Rule: synonym rotation ("jargon pass" beside "jargon lint" and "the
    fourth pass"). Severity: may.
    Fix: "The jargon lint never ran in Example 6.13."

49. "...labeled in order "source checks", "check the checkers", "style
    audit", "jargon lint"." (38, art comment)
    Rule: synonym rotation (the pass is "Checking the checkers" in Table
    6.1 and the heading). Severity: may.
    Fix: "...labeled in order "source checks", "checking the checkers",
    "style audit", "jargon lint"."

50. "The code reads the first expect comment it finds, so give each
    fixture exactly one." (156, footnote)
    Rule: footnote carries a fact the body needs (an instruction).
    Severity: may.
    Fix: move it into the body at 78: "Give each fixture exactly one
    expect comment. Press reads the first one it finds." Keep the
    footnote for the documentation discrepancy alone.

51. "The cure is a habit of the hands." (523, sidebar)
    Rule: saying dressed as depth. Severity: may.
    Fix: "The cure is a habit."

52. "**Warning:** Never pipe `press check` into another command before
    `&&` in a commit chain." (527)
    Rule: repetition (style guide 8.1: an admonition that repeats the
    text above it). The sidebar and Example 6.15 have already made the
    point twice. Severity: may.
    Fix: keep the warning, cut the sidebar's last paragraph to "Let the
    checker's own status reach the `&&`, and read its output when it
    fails.", or move the warning ahead of Example 6.15, where it protects
    the step.

53. "This book, for example, carries banned patterns for the stock phrases
    its editors refuse, and a fixture in *tests/known-bad/* for each
    family of patterns." (366)
    Rule: wrong term ("refuse" is reserved for press). Severity: may.
    Fix: "This book, for example, carries banned patterns for the stock
    phrases its editors will not print, and a fixture in
    *tests/known-bad/* for each family of patterns."

54. "The scaffold calls an empty sentinel list and a one-page floor draft
    settings." (417)
    Rule: rhythm (the predicate noun comes late, and the reader parses
    "floor draft" as a noun stack). Severity: may.
    Fix: "The scaffold's template calls two settings draft settings: an
    empty sentinel list and a one-page floor."

55. "At the time of this writing it holds 53 rules." / "Example 6.5 lists
    the 14 rewrite terms." (254, 267)
    Rule: synonym rotation (watchlist "rules", "terms", and "rows" for
    one thing, where "rule" also names the checker's rules). Severity:
    may.
    Fix: "At the time of this writing it holds 53 terms." Use "terms" for
    the watchlist entries throughout 254 to 279, and "rows" only for the
    CSV lines of Example 6.6.

## Fact: see fact checker

- 17 ("Every book that press builds passes through one command first")
  and 36 ("none of it exists until all four passes succeed") against 154
  ("a bare `press pdf` does not run them"). Does `press pdf` run the
  checker at all?
- 233 and 378: the audit directories meet "the dash rules and the phrase
  rules". The universal battery also holds trailing whitespace. Does that
  rule apply there?
- 386: the four places ("the PDF text" and "every edition") overlap,
  because the PDF is an edition.
- 439, 447: does the Alice example really report "1 ordered Markdown
  files" and "Editorial checks passed: 1"? Example 6.13 names a chapter
  01, Example 6.8 names an `appendices` audit directory, and 235 says the
  editorial count includes the audit directories.
- 514: "The failed audit two lines later" depends on how many note lines
  print between the summaries.
- 324: which suite holds the byte-for-byte copy test (item 20).
