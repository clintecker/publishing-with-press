# Copyedit: Appendix A, Command reference

File: `book/appendices/a-command-reference.md`

## Status

REVISE. Two blocks, both watchlist sightings that are not press's own
names: "the EPUB gate" (1186) and "the fallback title" (1332). This
follows the Chapter 15 and Appendix C precedent: `jargon-allow` lets
"gate" and "fallback" through, but here neither word names anything press
has. "The commerce gate" (86, 90, 98, 1327) is press's name and is
accepted. "scaffold" (371, 876, 1262) is press's name for what `press new`
writes, and "spine" (464) is the bound edge. Both are accepted. "clean" is
the command's name. "verified" and "canonical" occur only inside quoted
output (96, 859, 953, 1041, 1171, 1201). `press style` passes the whole
manuscript ("Editorial checks passed: 23 Markdown files"). `press check`
stops today at the source checks on two unreferenced Chapter 14 plates,
which do not concern this file.

Counts by severity: blocks 2, should 40, may 20, fact 4 (items 4, 14,
33, and 58 carry a note for the fact checker).

Most frequent rules broken: wrong term (20 items, counting both blocks:
the edition names, "the sample book", "the logo", "validator", the
sentence-initial lowercase "press"), two ideas (16, counting items where
it rides beside another rule), and hidden actor (9). Synonym rotation
(6) and era spelling ("colour", five lines) follow.

The entries are manpage entries. Per the desk instruction, the entry form
is not counted: the subjectless Description fragments ("Creates a chapter
file..."), the bold run-in labels, the "Not listed by `--help`" fragments
in the option tables, and the terse reference rhythm are accepted.
Synopsis lines and sessions are not touched. The Example lead-in prose is
judged with the Description, Options, and See also prose.

Every cross-reference is in the `Chapter N, *Title*` form, and every title
matches the chapter or appendix heading word for word (18 distinct
references checked). Second person and present tense hold throughout.
"We" appears only for the authors' editorial acts (15, 215, 803), and "I"
never appears. The one Warning (158) is imperative and two sentences
long. The appendix has no footnotes. The dry understatement appears once,
at 902 ("which looks like a hang and is not one"), and never in a
heading. Numbers under ten are spelled out in prose except values,
statuses, and measurements.

Line numbers are `cat -n` line numbers in the file as it stands.

## The ste_check findings, judged

ste_check reports 26 findings (704 sentences, average 6.8 words, max 41).

- Sentence length at 25, 112, 432, 560, and 790: mostly artifacts. The
  counter does not break a sentence before a lowercase "press", so it
  joins two sentences into one. Read as written, each sentence is under
  30 words. Line 790 still holds two ideas (item 30), and the lowercase
  starts are item 3.
- Sentence length at 1186 (33 words): the counter joins the first two
  sentences of the entry. The real sentences are under 30 words, but the
  entry carries a block, a hidden actor, and two wrong terms (items 1,
  6, 7, and 8).
- Sentence length at 1341 and the semicolon at 1341: accepted. It is the
  index comment.
- `-ing` forms at 44, 101, 231, 500, 529, 571, 862, 1131, 1176, 1204, and
  1227: accepted. Each is a chapter title in a See also line.
- `-ing` form at 1162 ("clipping"): accepted. It is a noun.
- "enhance" (173, 190): accepted. It is the command's name.
- "verify" (1154): accepted. It is the command's name.
- Perfect tense at 1075 ("has eleven"): accepted. "has" is the main verb.
- "whether" (1280): accepted. The contract keeps "whether" for this voice.
- The checker does not see: one real perfect tense at 1337 (item 43) and
  one "would" at 161 (item 36).
- Prose semicolons: none. The semicolon at 145 is inside press's quoted
  refusal. No em or en dash appears.

## Findings

1. "The EPUB gate softens to a warning." (1186, in "Without epubcheck on
   a local machine, the EPUB gate softens to a warning.")
   Rule: wrong term (watchlist "gate", one-sighting list; the vocabulary
   reserves "gate" for the commerce gate and the quality gate).
   Severity: blocks.
   Fix: "Without epubcheck on a local machine, press reports the missing
   check as a warning instead of a failure."

2. "press sets this for the fallback title in TeX." (1332)
   Rule: wrong term (watchlist "fallback", one-sighting list; Appendix B
   calls the same page "the plain title page"). Also item 3's lowercase
   start. Severity: blocks.
   Fix: "Press sets this for the plain title page in TeX."

3. Sentence-initial lowercase "press" in prose at 25 ("press refuses to
   overwrite"), 35 ("press lowercases the name"), 112 ("press refuses an
   opaque plate"), 120 ("press extracts the ink"), 181 ("press upscales
   the image"), 432 ("press writes the image"), 560 ("press writes the
   year"), 769 ("press refuses a pin"), 790 ("press refuses a path"),
   and 1328 ("press reads them"). Also 1332 (item 2).
   Rule: wrong term (*docs/vocabulary.md*: "Press (except at a sentence
   start)"; the chapters capitalize it 73 times at a sentence start and
   leave it lowercase 6 times; Appendixes B and C capitalize it).
   Severity: should.
   Fix: capitalize each: "Press refuses to overwrite a file that exists,
   with exit status 1." and likewise at each line. Captions such as
   "Table A.1. press add options" name the command and stay lowercase.
   (Copy 01, item 44, put the same question to the editor. If the editor
   rules for lowercase, no change.)

4. "...a short session on the sample book `alice`, and the chapter that
   explains the command in full." (3)
   Rule: wrong term (the vocabulary's term is "the Alice book"; "the
   sample book" is allowed only at first use, and the appendix uses it
   five more times). Severity: should.
   Fix: "...a short session on the Alice book (the book's sample, slug
   `alice`), and the chapter that explains the command in full."
   (fact: see fact checker. Example A.3, Example A.7, and the
   `press wordcount` session show a fresh scaffold, not the full novel.)

5. "the sample book" at 64 ("because the sample book has no
   *config/aesthetic.yaml* yet"), 90 ("The sample book has no print
   ordering"), 408 ("shows the sample book with every file in order"),
   769 ("the status of the sample book"), and 832 ("The sample book has
   no ISBN yet").
   Rule: wrong term ("the sample book (after first use)" is on the never
   list). Severity: should.
   Fix: "the Alice book" at each: "The first command shows the house
   aesthetic, because the Alice book has no *config/aesthetic.yaml* yet."

6. "Rebuilds the editions other than the PDF, then verifies each of them
   and the two archives." (1186)
   Rule: wrong term (press's edition name). Severity: should.
   Fix: "Rebuilds the editions other than the Print edition (PDF), then
   verifies each of them and the two archives."

7. "epubcheck validates the EPUB, and a further check confirms that the
   editions agree on the chapter witnesses." (1186)
   Rule: two ideas, hidden actor ("a further check"), wrong term ("the
   EPUB"). Severity: should.
   Fix: "epubcheck validates the Circulating edition (EPUB). Press then
   confirms that the editions agree on the chapter witnesses."
   (Sentence starts with the program name epubcheck, which stays
   lowercase as the program is spelled.)

8. "In the toolchain image a missing epubcheck is fatal." (1190)
   Rule: rhythm (the condition is first but the comma after the
   opening phrase is missing, and the sentence restates item 1's
   contrast). Severity: may.
   Fix: "In the toolchain image, a missing epubcheck fails the run."

9. "Builds the PDF, then renders every page with `pdftoppm` to a PNG file
   at 160 dpi in *build/rendered-book/*. Because the target builds the
   PDF first, the images always show the current manuscript." (975)
   Rule: wrong term (press's edition name). Severity: should.
   Fix: "Builds the Print edition (PDF), then renders every page with
   `pdftoppm` to a PNG file at 160 dpi in *build/rendered-book/*.
   Because the target builds the Print edition first, the images always
   show the current manuscript."

10. "Rebuilds the PDF and verifies it as an object." (1162)
    Rule: wrong term. Severity: should.
    Fix: "Rebuilds the Print edition, *dist/alice.pdf*, and verifies it
    as an object."

11. "The EPUB takes its rights line from the metadata `copyright`,
    `publisher`, and `publisher-place`." (564)
    Rule: wrong term (the entry has just glossed the Circulating
    edition). Severity: should.
    Fix: "The Circulating edition takes its rights line from the metadata
    `copyright`, `publisher`, and `publisher-place`."

12. "...the print interior, the cover wrap, the EPUB, and the marketing
    cover image." (947)
    Rule: wrong term. Severity: should.
    Fix: "...the print interior, the cover wrap, the Circulating edition
    (EPUB), and the marketing cover image."

13. "This capture comes from the press's own Alice example, which has 23
    pages and two sentinels." (1166)
    Rule: wrong term ("the Alice example" is on the never list; the term
    is "the press's own three-chapter Alice example"). Severity: should.
    Fix: "This capture comes from the press's own three-chapter Alice
    example, which has 23 pages and two sentinels."

14. "At the time of this writing, the print-safe pass copies only the
    JPEG files at the top of *assets/*, the images in *assets/woodcuts/*,
    and the logo." (929)
    Rule: wrong term ("the logo" is on the never list for the
    logomark). Severity: should.
    Fix: "At the time of this writing, the print-safe pass copies only
    the JPEG files at the top of *assets/*, the images in
    *assets/woodcuts/*, and the logomark."
    (fact: see fact checker. Line 925 says "Every image goes through the
    print-safe pass", and 929 says it copies only three places.)

15. "This sets the number of grays or colours after quantizing. The
    default comes from `plates.medium` in the aesthetic: 16 for
    engraving, woodcut, and line work, 24 for pen and etching, and 64 for
    wash and watercolour." (187)
    Rule: era spelling (American spelling). Severity: should.
    Fix: "This sets the number of grays or colors after quantizing. The
    default comes from `plates.medium` in the aesthetic: 16 for
    engraving, woodcut, and line work, 24 for pen and etching, and 64 for
    wash and watercolor."

16. "On a colour profile the quantizing keeps colours instead of grays."
    (192)
    Rule: era spelling. Severity: should.
    Fix: "On a color profile, the quantizing keeps colors instead of
    grays."

17. "The interior must be single ink except on a colour profile, so a
    code block in colour makes the verifier refuse it with `print
    profile: colored ink on pages [N]`." (1237)
    Rule: era spelling, two ideas. Severity: should.
    Fix: "The interior must be single ink except on a color profile. On
    any other profile, a code block in color makes the verifier refuse
    the interior with `print profile: colored ink on pages [N]`."

18. "The colour refusal names the pages at fault, so you can find them in
    the interior." (1241)
    Rule: era spelling. Severity: should.
    Fix: "The color refusal names the pages at fault, so you can find
    them in the interior."

19. "These turn colour in the terminal output off or on." (1330)
    Rule: era spelling. Severity: should.
    Fix: "These turn color in the terminal output off or on."

20. "On the way it generates the front matter and the subject index and
    checks the table of authorities, and the index or the ledger can
    refuse the build." (902)
    Rule: two ideas, synonym rotation ("the ledger" for the table of
    authorities named in the same sentence). Severity: should.
    Fix: "On the way, it generates the front matter and the subject index
    and checks the table of authorities. The index or the table of
    authorities can refuse the build."

21. "It reports the claims it could not source instead of putting them in
    the ledger." (998)
    Rule: synonym rotation (the previous sentence calls it "the table of
    authorities"). Severity: should.
    Fix: "It reports the claims it could not source instead of adding
    them to the table of authorities."

22. "Runs every config validator and reports each config file on its own
    line, the absent optional files included, as `ok` or with its
    problems." (398)
    Rule: wrong term ("validator" is on the never list). Severity:
    should.
    Fix: "Checks every config file against the book model and reports
    each file on its own line, the absent optional files included, as
    `ok` or with its problems."

23. "The file is a header followed by the source as written, with the
    attribute blocks removed from the headings." (744)
    Rule: wrong term ("the source" is on the never list for the
    manuscript), hidden actor ("removed"). Severity: should.
    Fix: "The file is a header followed by the manuscript as you wrote
    it. Press removes only the attribute blocks from the headings."

24. "Runs the whole build: the checker, every edition, the source
    archive, the Pages bundle, every verifier, and then the commerce
    gate." (86)
    Rule: synonym rotation ("the source archive" is the Source edition,
    which "every edition" already includes; Chapter 1 uses the same
    phrase, so the editor may let it stand). Severity: may.
    Fix: "Runs the whole build: the checker, every edition (the Source
    edition among them), the Pages bundle, every verifier, and then the
    commerce gate."

25. "The commerce gate is advisory unless `PRESS_RELEASE` is set and
    print ordering is on." (90)
    Rule: hidden actor, and the condition comes last. Severity: should.
    Fix: "Unless you set `PRESS_RELEASE` and turn on print ordering, the
    commerce gate only advises."

26. "Finishes a plate, and the whole subcommand is not listed by
    `--help`." (181)
    Rule: two ideas, hidden actor. Severity: should.
    Fix: "Finishes a plate. `--help` does not list the subcommand."

27. "The first pass that fails stops the run with exit status 1, and the
    jargon lint writes its full audit to *build/jargon-report.txt*."
    (211)
    Rule: two ideas (the failure rule and the jargon report are
    unrelated). Severity: should.
    Fix: "The first pass that fails stops the run with exit status 1. The
    jargon lint writes its full audit to *build/jargon-report.txt*."

28. "A field that is not set prints `<path>: not set` and exits with
    status 5." (263) and "An unknown or unwritable field exits with
    status 3, and a value the model refuses exits with status 4." (324)
    Rule: hidden actor (a field does not exit; the command does).
    Severity: should.
    Fix: "For a field that is not set, the command prints `<path>: not
    set` and exits with status 5." and "The command exits with status 3
    for an unknown or unwritable field and with status 4 for a value the
    model refuses."

29. "| `press config` | 0 for success, 2 for a usage error, 3 for an
    unknown or unwritable field, 4 for a refused value or a failed
    validation, 5 for a key that is not set on a read |" (1308)
    Rule: synonym rotation ("key" for the "field" of 263, 292, and 324).
    Severity: should.
    Fix: "... 5 for a read of a field that is not set |"

30. "press refuses a path that exists, copies the template, stamps the
    four workflows into *.claude/workflows/*, and fills in the identity,
    but it does not run `git init`." (790)
    Rule: two ideas (a refusal, three actions, and an omission in one
    sentence). Severity: should.
    Fix: "Press refuses a path that exists. Otherwise it copies the
    template, stamps the four workflows into *.claude/workflows/*, and
    fills in the identity. It does not run `git init`."

31. "The wrap is one page with the back, the spine, and the front, and
    press computes the width of the spine." (464)
    Rule: two ideas. Severity: should.
    Fix: "The wrap is one page with the back, the spine, and the front.
    Press computes the width of the spine."

32. "The desk needs the `tui` extra and a terminal, and without either it
    exits with status 2, because it never draws into a pipe." (486)
    Rule: two ideas ("without either" also reads as "without both").
    Severity: should.
    Fix: "The desk needs the `tui` extra and a terminal. If either is
    missing, it exits with status 2, because it never draws into a
    pipe."

33. "It is the one command that reaches the network, and it never issues
    a number. Without a number, it uses `registrations.lccn` or
    `registrations.issn` from the config, and it exits with status 0
    only when the outcome is `found`." (722)
    Rule: two ideas (second sentence). Severity: should.
    Fix (second sentence): "Without a number, it uses
    `registrations.lccn` or `registrations.issn` from the config. It
    exits with status 0 only when the outcome is `found`."
    (fact: see fact checker. `press cover`, `press illustrate`, and
    `press art commission` also reach the network.)

34. "A value the book lacks prints as `(needed on the form)`, and the
    print ISBN points you to `press isbn assign print`." (872)
    Rule: two ideas, and "the print ISBN points you" names the wrong
    actor (the line for a missing ISBN points you). Severity: should.
    Fix: "A value the book lacks prints as `(needed on the form)`. When
    the print ISBN is missing, its line points you to
    `press isbn assign print`."

35. "A book with no Git repository still gets an archive, but it holds no
    files, so commit the manuscript before you rely on it." (1098)
    Rule: two ideas (a description and a command in one sentence; two
    "it"s with different referents). Severity: should.
    Fix: "A book with no Git repository still gets an archive, but the
    archive holds no files. Commit the manuscript before you rely on the
    Source edition."

36. "A second run would add *openai-3.png* and *openai-4.png*, because
    candidates never overwrite." (161)
    Rule: perfect tense (simple tenses only: "would" is not one).
    Severity: should.
    Fix: "A second run adds *openai-3.png* and *openai-4.png*, because
    candidates never overwrite."

37. "It reads the manuscript and any directories named in `audit-dirs`,
    where heading and paragraph problems are warnings instead of
    errors." (1120)
    Rule: two ideas (the "where" clause carries the second fact).
    Severity: should.
    Fix: "It reads the manuscript and any directories named in
    `audit-dirs`. In an audit directory, heading and paragraph problems
    are warnings instead of errors."

38. "The bundle holds the landing page, a *read/* copy of the reader, and
    *downloads/*, plus *sitemap.xml* and *robots.txt* when `site-url` is
    set." (849)
    Rule: hidden actor ("is set"), and synonym rotation ("the reader"
    for the reader site). Severity: should.
    Fix: "The bundle holds the landing page, a *read/* copy of the reader
    site, and *downloads/*, plus *sitemap.xml* and *robots.txt* when you
    set `site-url`."

39. "| `press publish` | 1 when anything is unverified, unless
    `--report-only` is given |" (1314)
    Rule: hidden actor. Severity: should.
    Fix: "| `press publish` | 1 when anything is unverified, unless you
    give `--report-only` |"

40. "A chain such as `press check && git commit` stops on a failure, and
    a pipe into `grep` before the `&&` hides the failure behind `grep`'s
    own status." (1318)
    Rule: two ideas (the rule and the scar it protects against).
    Severity: should.
    Fix: "A chain such as `press check && git commit` stops on a failure.
    A pipe into `grep` before the `&&` hides the failure behind `grep`'s
    own status."

41. "This turns on release mode: a build demands the release witnesses,
    at least two sentinels and a page floor of at least 24, and the
    commerce gate fails closed." (1327)
    Rule: two ideas (and the appositive reads as a list of three items).
    Severity: should.
    Fix: "This turns on release mode. A build demands the release
    witnesses (at least two sentinels and a page floor of at least 24),
    and the commerce gate fails closed."

42. "Example A.3 previews the removal of the scaffold's placeholder
    subtitle." (371)
    Rule: the action in the verb ("the removal"). Severity: should.
    Fix: "Example A.3 previews how the diff looks when you remove the
    scaffold's placeholder subtitle."

43. "This is a secret in the press repository's CI, for the check that
    the security controls have not changed." (1337)
    Rule: perfect tense. Severity: should.
    Fix: "This is a secret in the press repository's CI, for the check
    that the security controls still match their record."

44. "press refuses a pin it finds anywhere else." (769)
    Rule: wrong term ("anywhere else" points back across a paragraph
    break to the two places at 765). Also item 3. Severity: should.
    Fix: "Press refuses a pin it finds outside *requirements.txt* and
    *.github/workflows/*."

45. "Prints every figure the manuscript declares as a JSON array, one
    object per image." (581)
    Rule: rhythm ("as a JSON array" attaches to "declares"). Severity:
    may.
    Fix: "Prints, as a JSON array, every figure the manuscript declares,
    one object per image."

46. "With a brief in quotes, press runs the `aesthetic-brief` workflow
    through the `claude` command to draft *config/aesthetic.yaml*, and
    then prints `review it: press aesthetic`." (54)
    Rule: two ideas. Severity: may.
    Fix: "With a brief in quotes, press runs the `aesthetic-brief`
    workflow through the `claude` command to draft
    *config/aesthetic.yaml*. It then prints `review it: press
    aesthetic`."

47. "A line that starts with `+` echoes a program press runs, and we
    shorten the long ones." and "The module command lines for
    contributors, such as `python3 -m press.receipts`, are not `press`
    commands, and this appendix leaves them out." (15)
    Rule: two ideas. Severity: may.
    Fix: "A line that starts with `+` echoes a program press runs. We
    shorten the long ones." and "The module command lines for
    contributors, such as `python3 -m press.receipts`, are not `press`
    commands. This appendix leaves them out."

48. "press lowercases the name for the filename and turns each run of
    other characters into one hyphen." (35)
    Rule: rhythm ("other" than what is not said). Severity: may.
    Fix: "Press lowercases the name for the filename and turns each run
    of characters other than letters and digits into one hyphen."

49. "We cut the two notes that report extra diagnostics from the dash
    fixtures, which the checker expects." (215)
    Rule: rhythm ("which" can attach to the fixtures or the
    diagnostics). Severity: may.
    Fix: "We cut the two notes about extra diagnostics from the dash
    fixtures. The checker expects those diagnostics."

50. "Run it when you doubt a leftover file in *build/*. The next target
    writes the directory again." (245), "It is the press checking
    itself, and a passing run prints one line." (1036), and "A first run
    with `--report-only` shows the list without the verification."
    (957)
    Rule: rhythm (each closing sentence repeats its own entry's
    Description). Severity: may.
    Fix: cut the repeated sentence: "Run it when you doubt a leftover
    file in *build/*." / "An author rarely needs this command." / end
    the paragraph at "...such as ordering a physical proof."

51. "Without `OPENAI_API_KEY`, it prints the prompt instead, so that you
    can run it elsewhere." (432)
    Rule: wrong term ("run" is what you do with a command, not a
    prompt). Severity: may.
    Fix: "Without `OPENAI_API_KEY`, it prints the prompt instead, so that
    you can give it to an image model elsewhere."

52. "Without it, press reads `git config user.name`, and failing that it
    writes "The Author"." (796)
    Rule: rhythm ("failing that" is an -ing form; "fail" is reserved for
    checks). Severity: may.
    Fix: "Without it, press reads `git config user.name`. If that is
    empty, it writes "The Author"."

53. "...changes nothing, and fingerprints *book/* and *config/* before
    and after to prove it." (666)
    Rule: wrong term ("fingerprint" is on the never list beside
    "witness"; here it means a hash). Severity: may.
    Fix: "...changes nothing, and hashes *book/* and *config/* before and
    after to prove it."

54. "This lets the workflow apply its suggestions, and grants the agent
    the full Bash tool instead of `press` and `python3` alone." (672)
    and "This sets the most rounds the workflow runs." (673)
    Rule: synonym rotation ("the agent" for the workflow), rhythm ("the
    most rounds"). Severity: may.
    Fix: "This lets the workflow apply its suggestions and gives it the
    full Bash tool instead of `press` and `python3` alone." and "This
    sets the largest number of rounds the workflow runs."

55. "A positive cap samples, and the workflow's accounting reports what
    it left out." (1004)
    Rule: rhythm ("samples" has no object). Severity: may.
    Fix: "A positive cap takes a sample of the claims, and the workflow's
    accounting reports the claims it left out."

56. "Builds the Telegraphic edition, plain text at 80 columns,
    *dist/alice.txt*, with pandoc and the portable defaults." (1141)
    Rule: rhythm (three appositives in a row; the gloss belongs in
    parentheses as at 539 and 560). Severity: may.
    Fix: "Builds the Telegraphic edition (plain text at 80 columns),
    *dist/alice.txt*, with pandoc and the portable defaults."

57. "The style comes from `--style`, then the figure's `style=`
    attribute, then `plates.style` in the aesthetic, then
    `wood-engraving`." (646)
    Rule: rhythm (the `press cover` entry at 445 says "then from the
    default `penguin-tri-band`"; this one drops "the default").
    Severity: may.
    Fix: "The style comes from `--style`, then the figure's `style=`
    attribute, then `plates.style` in the aesthetic, then the default
    `wood-engraving`."

58. "The receipts read this in CI." (1333)
    Rule: wrong term ("the receipts" is not defined in the book and is
    not in the vocabulary). Severity: may.
    Fix: "Press's build receipts record this in CI." (fact: see fact
    checker for what reads `GITHUB_SHA`.)

59. "...matched without regard to case." (153)
    Rule: hidden actor. Severity: may.
    Fix: "...and press matches the extension without regard to case."

60. "| The composite action's refusal of a command it does not accept |
    2 |" (1312)
    Rule: the action in the verb ("refusal of"). Severity: may.
    Fix: "| The composite action, when it refuses a command | 2 |"

61. "Keys run a target (`p`), open the setup wizard (`w`), refresh (`r`),
    and quit (`q`)." (486)
    Rule: rhythm (the keys do not quit; the desk does). Severity: may.
    Fix: "The keys run a target (`p`), open the setup wizard (`w`),
    refresh the screen (`r`), and quit the desk (`q`)."

62. "*`--as portrait`* ... flattened onto white." (121)
    Rule: hidden actor. Severity: may.
    Fix: "The image becomes *assets/author.jpg*, and press flattens it
    onto white."
