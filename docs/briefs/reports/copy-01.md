# Copyedit report: Chapter 1, Introduction

Desk: copyeditor. File: `book/chapters/01-introduction.md`. Read against
`docs/prose-contract.md`, `docs/style-guide.md` sections 3, 4, and 8, and
`docs/vocabulary.md`. Line numbers refer to the file as it stands.

## Checker leads

`python3 tools/ste_check.py book/chapters/01-introduction.md` reports 61
findings (341 sentences, average 13.8 words). Nearly all are noise:

- The 132-word sentence and the semicolons at lines 4, 37, 42, 196 are
  inside `<!-- art: -->` directives, not prose.
- The long sentences at 19, 37, 40, 45, 263, 265, 267, 295 come from the
  splitter merging two sentences where the second begins with a lowercase
  `press`, or where a footnote marker sits before the period. No prose
  sentence in the chapter runs over 30 words.
- The passives at 69, 71, 85, 96 are inside quotations of the laws and of
  CONTRIBUTING.md. "whether" and "therefore" are period-correct under the
  80% rule. The `-ing` flags are headings, gerunds, and output.

No prose semicolon, em or en dash, perfect tense, stacked hedge,
assistant-vocabulary word, or meta-narration appears in the chapter. There
is no "we" and no "I". Second person and present tense hold throughout,
with past tense only for history.

## Findings

1. "The image now ships a plain `java -jar` wrapper." (line 103)
   Rule: wrong term (watchlist jargon, "ship"; `jargon-allow` admits it
   only as press's own name for a thing, which this is not). Severity:
   blocks. Fix: "The image now carries a plain `java -jar` wrapper."

2. "It checks the manuscript, builds every edition, and then opens each file
   it built to confirm that the file holds what it should." (line 19)
   Rule: wrong term (first use of *edition* is roman; the definition waits
   until line 218). Severity: should. Fix: "It checks the manuscript, builds
   every *edition* (one published form of the book, such as the PDF or the
   EPUB), and then opens each file it built to confirm that the file holds
   what it should." Line 218 then drops the italic and the definition.

3. Same sentence, "the manuscript" (line 19), used before the italic
   definition at line 23. Rule: wrong term (first use not defined).
   Severity: should. Fix: "It checks the chapters, builds every *edition*
   (...), and then opens each file it built to confirm that the file holds
   what it should."

4. "A *profile* is a sealed interior geometry, and the house 6 by 9 is one
   profile among the six." (line 27) Rule: wrong term (*the house* is
   defined at line 45). Severity: should. Fix: "A *profile* is a sealed
   interior geometry, and the default 6 by 9 is one profile among the six."

5. "It reads every chapter file before anything builds, and it refuses a
   manuscript that breaks the house rules." (line 31) Rule: wrong term
   ("house rules" is *config/house-rules.yaml*; the em dash, curly quote,
   glyph, and paragraph rules belong to press itself). Severity: should.
   Fix: "It reads every chapter file before anything builds, and it refuses
   a manuscript that breaks one of its rules."

6. "One edition skips pandoc altogether: the Markdown edition is the
   manuscript stitched into one file." (line 33) Rule: synonym rotation
   (Table 1.2 names it the Manuscript edition). Severity: should. Fix: "One
   edition skips pandoc altogether: the Manuscript edition is the manuscript
   stitched into one file."

7. "Each *verifier* opens a finished artifact and inspects it as an object."
   (line 35) Rule: wrong term (first use of *artifact*; defined at line
   218). Severity: should. Fix: "Each *verifier* opens a finished
   *artifact*, a file or directory in *dist/* that the registry names, and
   inspects it as an object." Line 218 then drops the italic.

8. "Verifying is the part a home-made build script usually leaves out."
   (line 35) Rule: era spelling (American "homemade"). Severity: should.
   Fix: "Verifying is the part a homemade build script usually leaves out."

9. Paragraph at line 45, "You can install the toolchain on your own
   machine. ... A book changes the house through its own config files and
   never by editing press." Rule: two ideas (eight sentences, two topics:
   the toolchain image and the house; contract limit six). Severity:
   should. Fix: end the paragraph after "...as the section "Versions and the
   pinned contract" explains later in this chapter." and start a new
   paragraph at "Above the toolchain, press carries *the house*, its
   default design and law."

10. "Everything earlier lives only in the tags, and the CHANGELOG lists it in
    one sentence:" (line 51) Rule: two ideas (and the two halves read as a
    contradiction). Severity: should. Fix: "Everything earlier lives only in
    the tags. The CHANGELOG sums it up in one sentence:"

11. "Version 2.0.0 followed on 2026-07-21 as the "composable press", with
    print profiles, print providers, and an extension contract." (line 55;
    again in Table 1.3, line 254, "added print profiles, providers")
    Rule: synonym rotation (line 25 says "design profiles"; vocabulary is
    "profile / design profile"). Severity: should. Fix: "Version 2.0.0
    followed on 2026-07-21 as the "composable press", with design profiles,
    print providers, and an extension contract." Table 1.3: "The
    "composable press" added design profiles, providers, and the extension
    contract."

12. "press has one maintainer, Clint Ecker of LGTM Systems, LLC, and books
    from that shop appear under the LGTM Publishing imprint." (line 59)
    Rule: two ideas. Severity: should. Fix: "press has one maintainer, Clint
    Ecker of LGTM Systems, LLC. Books from that shop appear under the LGTM
    Publishing imprint."

13. "The license is MIT, "code and bundled content alike", and the README is
    plain about ownership: "A book you make with the press is yours
    entirely."" (line 59) Rule: two ideas. Severity: should. Fix: "The
    license is MIT, "code and bundled content alike". The README is plain
    about ownership: "A book you make with the press is yours entirely.""

14. "It is a book repository and not a scaffold, so the rule does not reach
    it." (line 61) Rule: not X but Y (near-variant: "X and not Y" staging).
    Severity: should (the contrast carries the logic, so not blocks, but
    the shape is the one the contract names). Fix: "The rule covers a fresh
    scaffold, and this book is a book repository, so the rule does not
    reach it."

15. "ARCHITECTURE.md then gives each kind of fact one home." (line 69; also
    "Its CLAUDE.md" line 73, "CONTRIBUTING.md records" line 92, "ARCHITECTURE.md
    draws" line 87, "NON-GOALS.md calls" line 115) Rule: code typography
    (filenames are italic, per style guide 2.5; lines 65 and 111 set
    *docs/ARCHITECTURE.md* and *docs/NON-GOALS.md* italic, the later
    mentions set them roman). Severity: should. Fix: "*ARCHITECTURE.md* then
    gives each kind of fact one home." and the same italic for every later
    filename mention (CLAUDE.md, CONTRIBUTING.md, NON-GOALS.md). The
    CHANGELOG, README, ROADMAP, and QUICKSTART, used as document names, may
    stay roman if the Preface conventions say so.

16. "The registry derives every filename from it, so the PDF becomes
    *alice.pdf* and the EPUB becomes *alice.epub*, and nobody types either
    name." (line 71) Rule: two ideas. Severity: should. Fix: "The registry
    derives every filename from it, so the PDF becomes *alice.pdf* and the
    EPUB becomes *alice.epub*. Nobody types either name."

17. "The tallest scar in press shows the order at work." (line 79) Rule:
    wrong term (first use of *scar*; defined at line 101). Severity: should.
    Fix: "The tallest *scar* in press, a production failure turned into a
    guard, shows the order at work." Line 101 then drops "A *scar* is a
    production failure turned into a guard."

18. "The commands in press carry dependency edges for that reason, and an
    invariant called `INV-graph-no-stale` guards them." (line 87) Rule:
    wrong term ("target", defined at line 29, is the word for a press
    command). Severity: should. Fix: "The targets carry dependency edges for
    that reason, and an *invariant*, an entry in the press's `INV-` ledger,
    called `INV-graph-no-stale` guards them."

19. Same sentence (line 87), "an invariant": first use of a vocabulary term,
    roman and undefined. Rule: wrong term (first use not defined). Severity:
    should. Fix: as in item 18. If the editor prefers shorter sentences:
    "The targets carry dependency edges for that reason. An *invariant*, an
    entry in the press's `INV-` ledger, guards them: `INV-graph-no-stale`."

20. "A new generator counts as proven only when some verifier would refuse
    its broken output." (line 96) Rule: wrong term ("refuse" is what press
    does when it stops with a message; a verifier result is "fail"; "output"
    is not a vocabulary word for an artifact). Severity: should. Fix: "A new
    generator counts as proven only when some verifier fails on its broken
    artifact."

21. "It says a scar becomes an executable invariant, a named proof, or an
    explicit public contract, and that a warning in prose is not enough by
    itself." (line 101) Rule: two ideas. Severity: should. Fix: "It says a
    scar becomes an executable invariant, a named proof, or an explicit
    public contract. A warning in prose is not enough by itself."

22. "The 3.0.2 release met that case in its own Lua filters.[^vacuous]"
    (line 105) Rule: footnote carries a fact the body needs (the body
    sentence means nothing until the reader reads the note). Severity:
    should. Fix: move the substance into the body: "The 3.0.2 release met
    that case in its own Lua filters. In CI the Lua filter tests skipped
    silently until the variable `PRESS_REQUIRE_LUA=1` forbade the skip." and
    keep the title-tie test in the footnote as the aside. (Release number:
    see item 61.)

23. "It does not build interactive or rich-media ebooks either." (line 113)
    Rule: era spelling ("e-book", like "e-mail"). Severity: should. Fix: "It
    does not build interactive or rich-media e-books either."

24. "Another trim, a colour interior, or large print is a new profile of the
    prose engine, and NON-GOALS.md calls that core press work." (line 115)
    Rule: era spelling (American "color"). Severity: should. Fix: "Another
    trim, a color interior, or large print is a new profile of the prose
    engine, and *NON-GOALS.md* calls that core press work."

25. "The build order, the verification pipeline, the file names, and the
    formats belong to the press." (line 121) Rule: era spelling ("filename")
    and wrong term ("edition", not "format", except for a file format).
    Severity: should. Fix: "The build order, the verification pipeline, the
    filenames, and the editions belong to the press."

26. "All 19 known-bad fixtures tripped their declared rule, and the
    known-good fixture passed." (Table 1.1, line 160) Rule: wrong term
    (*known-bad fixture* is defined at line 166, after this use). Severity:
    should. Fix: move the definition ahead of the table, so the paragraph at
    line 155 ends "...the preface. A *known-bad fixture* is a file that every
    check must reject." and line 166 opens "The second line shows press
    running every one of its fixtures through its own rules on each check."

27. "A *known-bad fixture* is a file that every check must reject, and press
    runs every one of its fixtures through its own rules on each check."
    (line 166) Rule: two ideas. Severity: should. Fix: "A *known-bad
    fixture* is a file that every check must reject. On each check, press
    runs every one of its fixtures through its own rules."

28. "It strips fenced and inline code, and it counts HTML comments, so an
    `art:` directive adds to the total." (line 168) Rule: two ideas.
    Severity: should. Fix: "It strips fenced and inline code. It counts HTML
    comments, so an `art:` directive adds to the total."

29. "**Warning:** The first LuaLaTeX run on a fresh machine starts a font
    scan that takes several minutes. It looks like a hang. Leave it alone,
    because it is not one, although it gives a very convincing imitation of
    one." (line 179) Rule: two ideas, and the admonition is not imperative
    (style guide 3.4: imperative and specific; the command arrives in the
    third sentence). Severity: should. Fix: "**Warning:** Leave the first
    LuaLaTeX run on a fresh machine alone. Its font scan takes several
    minutes and looks like a hang. It is not a hang, although it gives a very
    convincing imitation of one."

30. "That example sets Tenniel's 1865 wood engravings as plates." (line 213)
    Rule: wrong term (first use of *plate*, roman and undefined). Severity:
    should. Fix: "That example sets Tenniel's 1865 wood engravings as
    *plates*, the unnumbered illustrations in the List of Plates."

31. "It is the raw source, and pandoc does not render it." (Table 1.2, line
    226) Rule: wrong term ("the manuscript", never "the source"; "source"
    also collides with the Source edition two rows down). Severity: should.
    Fix: "It is the manuscript itself, and pandoc does not render it."

32. "It is a companion document published beside the book, and Chapter 10
    covers it." (line 235) Rule: two ideas (and the chapter title is
    missing, style guide 2.4). Severity: should. Fix: "It is a companion
    document published beside the book. Chapter 10, *Front matter and the
    index*, covers it." (Use the chapter's real title; chapter number: see
    item 65.)

33. "It holds a print-profile interior, a cover wrap with a computed spine
    and an EAN-13 barcode, and the retail channel checklists." (line 237)
    Rule: wrong term (first use of *cover wrap*, roman and undefined).
    Severity: should. Fix: "It holds a print-profile interior, a *cover
    wrap* (the back, spine, and front as one PDF) with a computed spine and
    an EAN-13 barcode, and the retail channel checklists."

34. "A book pins a tag of press, and the tags follow the GitHub Actions
    convention." (line 261) Rule: two ideas. Severity: should. Fix: "A book
    pins a tag of press. The tags follow the GitHub Actions convention."

35. "The press repository describes that immutability as "enforced, not
    promised", and *the release contract*, the workflow that proves a tag,
    does the enforcing." (line 261) Rule: two ideas. Severity: should. Fix:
    "The press repository describes that immutability as "enforced, not
    promised". *The release contract*, the workflow that proves a tag, does
    the enforcing."

36. Paragraph at line 263, "The contract covers the look of a book ... Its
    craft pass changed the page." Rule: two ideas (seven sentences; limit
    six). Severity: should. Fix: join the last two: "That rule is why v3.0.0
    had to be a major, because its craft pass changed the page."

37. "Release 3.0.1 keys that first note to the target major, so a v2 book
    moving to v3 no longer hears that nothing on its pages will move
    (#262)." (line 265) Rule: wrong term ("target" is a press command).
    Severity: should. Fix: "Release 3.0.1 keys that first note to the major
    the book moves to, so a v2 book moving to v3 no longer hears that
    nothing on its pages will move (#262)."

38. "A private book then needs no token for a second repository, and the
    installed press matches the exact action ref." (line 267) Rule: two
    ideas (two reasons, announced as two, in one sentence). Severity:
    should. Fix: "First, a private book needs no token for a second
    repository. Second, the installed press matches the exact action ref."

39. "Pin a three-part tag such as `v3.0.2` when a book must rebuild from the
    same press and toolchain years from now, and move that pin on purpose."
    (Tip, line 270) Rule: condition first (Pass 2). Severity: should. Fix:
    "When a book must rebuild from the same press and toolchain years from
    now, pin a three-part tag such as `v3.0.2` and move that pin on
    purpose."

40. "The chapters follow the order in which a book gets made." (line 275)
    Rule: hidden actor. Severity: should. Fix: "The chapters follow the
    order in which you make a book."

41. "They cover continuous integration and the release contract, the
    operator's desk and the editorial machines, and the internals." (line
    277) Rule: wrong term ("the desk" is `press desk`; "operator" is reserved
    for `press improve`, `press research`, `press aesthetic`). Severity:
    should. Fix: "They cover continuous integration and the release
    contract, the desk and the editorial workflows, and the internals."

42. Same sentence (line 277), "the editorial machines". Rule: synonym
    rotation (vocabulary: "workflow", never "pipeline, automation,
    playbook"; "machine" is a fourth name). Severity: should. Fix: as in
    item 41.

43. "Sessions show the `$` prompt followed by what you type, and a line that
    holds only `...` marks output left out." (line 281) Rule: two ideas (two
    conventions in one sentence; "left out" also hides the actor). Severity:
    should. Fix: "Sessions show the `$` prompt followed by what you type. A
    line that holds only `...` marks output that the example leaves out."

44. Sentence-initial lowercase "press" (lines 19, 35, 41, 45, 59, 113, 115,
    117, 121, 218, and others). Rule: wrong term (query for the editor:
    *docs/vocabulary.md* lists "Press (except at a sentence start)", which
    permits a capital at a sentence start, while line 23 and the house
    practice keep it lowercase; style guide 2.5 still shows "Press" as the
    roman program name). Severity: may. Fix: decide once and record it in
    the Preface conventions. If lowercase stays, no change; if not, "Press
    is a program that does that work for a book written in plain Markdown."

45. "...and a set of fixtures that every check must reject.[^mark]" (line
    45) Rule: rhythm (the footnote about the pilcrow mark hangs from the
    fixtures, which it does not concern). Severity: may. Fix: anchor it to
    the house: "Above the toolchain, press carries *the house*, its default
    design and law.[^mark]"

46. "A selftest named `scaffold_neutrality` checks that..." (line 61) beside
    "Checker self-test" and "the self-test fails" (lines 160, 166). Rule:
    synonym rotation (spelling). Severity: may. Fix: "A self-test named
    `scaffold_neutrality` checks that..." (or set `press selftest` in
    constant width if the command is meant).

47. "Each law fits in a line, and the ROADMAP restates most of them as
    product rules." (line 65) followed by "The ROADMAP states the same law
    as a product rule: facts are stated once and projected mechanically."
    (line 71) Rule: rhythm (the point is made twice in five sentences).
    Severity: may. Fix at line 65: "Each law fits in a line." and keep the
    line 71 sentence, which carries the specific wording.

48. "The cap varies by profile, and on the house 6 by 9 it is 6.3in."
    (line 79) Rule: code typography (a measurement in prose; the style guide
    writes "6.3 inches"). Severity: may. Fix: "The cap varies by profile,
    and on the house 6 by 9 it is 6.3 inches."

49. "The generator had tests, and they covered 11.5% of its lines." (line
    92) against the sidebar title "The cover that passed at 11.5 percent".
    Rule: rhythm (one form per book). Severity: may. Fix: "The generator had
    tests, and they covered 11.5 percent of its lines."

50. "On a fresh scaffold it passes, and its output names its passes in
    order." (line 147) Rule: rhythm (verb "passes" and noun "passes" in one
    clause). Severity: may. Fix: "On a fresh scaffold it succeeds, and its
    output names its four passes in order."

51. "The full output has four summary lines, one for each pass, and Table
    1.1 reads them." (line 155) Rule: rhythm (a table does not read). 
    Severity: may. Fix: "The full output has four summary lines, one for
    each pass, and Table 1.1 explains them."

52. "The count is 1 because the scaffold holds a single chapter file, the
    preface." (line 155) Rule: numbers (under ten, in prose). Severity: may.
    Fix: "The count is one because the scaffold holds a single chapter file,
    the preface." (Keep the numeral if the sentence is read as quoting the
    output.)

53. "The second line deserves a moment." (line 166) Rule: rhythm (a small
    staged run-up before the definition). Severity: may. Fix: delete it; the
    definition in item 27 can open the paragraph.

54. "If a rule stops catching the thing it exists to catch, the self-test
    fails before your manuscript can pass a broken rule." (line 166) Rule:
    rhythm (the logic is inverted: a rule passes a manuscript, not the other
    way round). Severity: may. Fix: "If a rule stops catching the thing it
    exists to catch, the self-test fails before that broken rule can pass
    your manuscript."

55. "Each file in Example 1.2 is an edition or holds one, and the section
    "The editions" later in this chapter names them." (line 194) Rule:
    rhythm (*pages* and *site* are directories). Severity: may. Fix: "Each
    entry in Example 1.2 is an edition or holds one. The section "The
    editions" later in this chapter names them."

56. "Chapter 14 follows that build step by step." (line 208) Rule: rhythm
    (style guide 2.4 gives the title with the number). Severity: may. Fix:
    "Chapter 14, *Continuous integration and the release contract*, follows
    that build step by step."

57. "The first is `pandoc is required`, ... The fifth is a CI build that dies
    at "Initialize containers", and the cure for that one is to run it
    again, because the toolchain image is public." (line 210) Rule: rhythm
    (five sentences in the same "The Nth is" mold; the causes are parallel
    items and the style guide allows a list for them). Severity: may. Fix:
    a numbered list of the five causes, each a sentence, introduced by
    "When the tour goes wrong, the QUICKSTART lists the five usual causes:".
    (The causal "because" in the fifth: see item 62.)

58. Dry understatement frequency: "with some care" (61), "and hopes" (77),
    "so nobody spends an afternoon looking for a defect in a sound EPUB"
    (103), "Nobody tests press on Windows." (117), "a very convincing
    imitation of one" (179), "the matching degree of trust" (281), and the
    footnote at 289. Rule: rhythm (seven in roughly nine pages; the voice
    asks for one every few pages). None is in a heading. Severity: may. Fix:
    cut two. "The press guards the neutrality of its scaffold." (line 61)
    and "The verifier also reports a present but unrunnable tool as a fault
    in the toolchain, not in the EPUB." (line 103). Keep the font-scan line,
    which is the calibration sample, and the closing one at 281.

59. "It adds that "A higher layer cannot erase missing proof below it.""
    (line 105) Rule: rhythm (punctuation: a quotation run into the sentence
    after "that" starts lowercase). Severity: may. Fix: "It adds: "A higher
    layer cannot erase missing proof below it.""

60. "That makes thirteen tags in one day, a pace the CHANGELOG did not
    attempt to record." (footnote, line 289) Fact: see fact checker (line 51
    names v1.0.0 through v1.6.0, seven tags, unless patch tags are counted).

61. "The 3.0.2 release met that case in its own Lua filters." (line 105)
    Fact: see fact checker (which release made the Lua suite run in CI).

62. "...and the cure for that one is to run it again, because the toolchain
    image is public." (line 210) Fact: see fact checker (the causal link
    between rerunning and the image being public).

63. "Two further artifacts gather the editions for readers. *dist/site/* is
    the reader site itself..." (line 233) Fact: see fact checker (Table 1.2
    already lists `site/` as the Chapter edition, so it is not a further
    artifact).

64. "Pillow 13 needs Python 3.11, so an install on Python 3.10 still
    resolves Pillow 12.x." (footnote, line 293) Fact: see fact checker
    (against a hash lock that pins 13.0.0, and press's stated floor of
    Python 3.10 at line 41).

65. "Chapter 10 covers it." (line 235) Fact: see fact checker (line 277
    gives Chapter 10 as the front matter and index; confirm the table of
    authorities lives there).

## Counts

- blocks: 1
- should: 42
- may: 16
- fact (referred to the fact checker, no severity): 6

Most frequent rules broken:

1. wrong term: 18 (items 1-5, 7, 17-20, 25, 26, 30, 31, 33, 37, 41, and
   the query in 44; nine of them a vocabulary term used before its italic
   definition)
2. two ideas: 15 (items 9, 10, 12, 13, 16, 21, 27, 28, 32, 34, 35, 36, 38,
   43, and the warning in 29)
3. synonym rotation and era spelling, tied at 4 each (items 6, 11, 42, 46;
   items 8, 23, 24, 25)
