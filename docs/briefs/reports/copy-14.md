# Copyedit: Chapter 14, Continuous integration and the release contract

File: `book/chapters/14-continuous-integration.md`

## Status

REVISE. One block: the five-step list in "The release contract" puts a
bold label on every item (the one-sighting list). `press check` passes
the whole book (source, checker self-test, editorial, jargon), and its
jargon audit names no term in this file. No prose semicolon, no dash, no
assistant vocabulary, no watchlist term.

Counts by severity: blocks 1, should 23, may 21, fact 5 (items 30, 35,
39, 46, and 47; items 30, 35, and 39 also carry a may).

Most frequent rules broken: wrong term (8), synonym rotation (4), then a
four-way tie at 3 each: perfect tense, two ideas, era spelling, and
second person.

Line numbers are `cat -n` line numbers in the file as it stands.

## The ste_check findings, judged

ste_check reports 29 findings (434 sentences, average 11.7 words, max 49).

- Semicolons at 44, 66, 105, and 248: accepted. All four sit inside
  verbatim quotations of press's comments and *CLAUDE.md*. 448 is the
  index comment. The three in code blocks (145, 360, 438) are program output.
- Passive "is refused" (157) and "is enforced" (228): accepted. Both are
  verbatim quotations of the press's contract text.
- Vague association at 214 ("linked to its predecessor"): accepted,
  a verbatim quotation.
- Paragraph length at 36, 236, 307: accepted. These are `art:` directives,
  not prose. 323 is a real finding (item 24).
- Sentence length at 448 (49 words): the index comment. Accepted.
- "therefore" at 42, 119, 139, 181, 248, 374: accepted under the 80
  percent rule (the contract keeps "therefore"). Six in one chapter is
  near the limit of taste, but none is wrong.
- `-ing` forms at 11, 64, 226, 448 ("floating", the term), 36
  ("holding", art directive), 117 ("Installing press", a chapter title),
  330, 372 ("Checking the manuscript", "Verifying the artifacts", chapter
  titles), 380 (heading), 395 ("migrating", a quoted refusal): accepted.

Also accepted on reading:

- Opener meta-narration at 18 ("This chapter follows ...", "The later
  sections turn to ..."): the style guide allows it in the opener.
- Cross-references "The section ... later in this chapter explains" (64,
  183) are accepted, as in Chapters 12 and 13.
- Dry understatement appears at 117 ("whatever Pillow PyPI served that
  day"), 243 ("a book pinned two ways builds two ways"), 411 ("That was
  true only of the step from v1 to v2."), and 417 ("the plan proposes it
  anyway"), never in a heading. The sidebar title is plain, not a pun.
- There is no "I". The five "we" sentences are editorial acts (item 25).
- Admonitions (107, 206, 242, 268, 344, 366, 413): seven, within the
  three-to-eight range. All are imperative and run two or three
  sentences. Item 21 and item 26 concern placement and repetition.
- Four footnotes, each an aside (Pillow, `main`, macOS, the 3.0.1 fix).
- Numbers: "status 2", "60 times 30 seconds", "87 sha256 hashes", "64
  hexadecimal digits", versions, and step numbers are measurements,
  codes, or references. "twelve layers" and "forty-one advisories" are
  spelled out, which is allowed. No small number appears as a numeral in
  prose.
- The chapter uses "Web site" (372) correctly and none of the other era
  words, so none is misspelled.
- Heading and caption case is sentence case throughout.

## Findings

1. "1. **Pin check.** The tag's *build.yml* must contain ... 2. **Image
   resolves.** ... 3. **Check runs pass.** ... 4. **Receipt chain.** ...
   5. **Upload.** The workflow uploads `release-receipt`." (278 to 282)
   Rule: bold labels on every list item (one-sighting list; the period
   in place of a colon does not change the device). Severity: blocks.
   Fix: drop the labels and let each step lead with its actor:
   "1. The tag's *build.yml* must contain `uses: clintecker/press@${tag}`,
   and its image must match ... 2. `docker manifest inspect` must succeed
   on that image. 3. The workflow waits up to 60 times 30 seconds ...
   4. The workflow builds the wheel, ... 5. The workflow uploads
   `release-receipt`."

2. "This chapter follows the Alice example through that machinery." (18)
   Rule: wrong term (vocabulary: "the Alice example" is a never-word; the
   chapter means the Alice book, which it names at 232 and 330).
   Severity: should.
   Fix: "This chapter follows the Alice book through that machinery."

3. "The press's own guide puts the rule in one clause" (30); "Its
   *CLAUDE.md* says" (105); "The press's contract says so in a
   parenthesis" (157); "In the press's words" (248)
   Rule: synonym rotation (one document, the press's *CLAUDE.md*, under
   four names). Severity: should.
   Fix (30): "The press's own *CLAUDE.md* puts the rule in one clause:
   ..." and name it *CLAUDE.md* at 157, 228, 230, and 248 as well (see
   item 4).

4. "The press's contract says so in a parenthesis" (157); "The press's
   contract adds that" (228); "The contract ends with the result" (230);
   "Design is part of the contract." (248)
   Rule: wrong term (vocabulary reserves "contract" for the release
   contract and the extension contract; here it means a section of the
   press's *CLAUDE.md*, and 284 and 303 use "the contract" for the
   workflow). Severity: should.
   Fix: "The press's *CLAUDE.md* says so in a parenthesis: ..." (157);
   "The press's *CLAUDE.md* adds that ..." (228); "The same passage ends
   with the result: ..." (230); "Design is part of what a tag promises."
   (248). If the book wants the section's own name, quote it once:
   "the section of the press's *CLAUDE.md* titled "The contract"".

5. "The runner pulls the toolchain image from the registry by its
   digest" (32); "The registry accepts a new image under an old tag"
   (157); "The first line names the image in the registry." (181); "a
   digest in the right form that names no image in the registry" (284)
   Rule: wrong term (vocabulary: "the registry" is the artifact graph in
   *registry.py*). Severity: should.
   Fix: "the container registry" at each place, glossed once at 32:
   "The runner pulls the toolchain image by its digest from the container
   registry, *ghcr.io*." The art directive (36) and `fig-alt` (34) need
   the same word.

6. "It deploys the Pages artifact that the build job uploaded." (50);
   "it uploads the Pages artifact" (62); "travels in its own artifact"
   (68); "downloads the artifacts `receipt-quality` and
   `receipt-integration`" (216); "uploads the Pages artifact" (374)
   Rule: wrong term (vocabulary: an *artifact* is a file or directory in
   *dist/* that the registry names; these are GitHub's upload bundles).
   Severity: should.
   Fix: name GitHub's sense once and keep it distinct: "It deploys the
   Pages upload, the GitHub artifact that the build job made." Then
   "GitHub artifact" at 62, 68, 216, and 374. The house sense at 48, 49,
   and 68 ("no artifacts") stays.

7. "The release contract assembles this receipt." (216)
   Rule: wrong term (define a term once, in italic, at first use; the
   term appears at 207 and 216 and is defined only at 276).
   Severity: should.
   Fix: "The *release contract*, the workflow that proves a press tag,
   assembles this receipt." At 276: "The release contract is
   *.github/workflows/release-contract.yml* in the press repository."

8. "its self-test proves the grammar" (252); "runs the self-test" (295,
   Table 14.3); "The self-test check `check_migration`" (407)
   Rule: wrong term (vocabulary: "self-test" belongs to the checker
   self-test; press's own suite is `press selftest`). Severity: should.
   Fix: "and `press selftest` proves the grammar against the cases in
   Table 14.2." Same at 295 and 407 ("The `press selftest` check
   `check_migration` proves both ..."), if `press selftest` is the suite
   meant (fact checker to confirm).

9. "The floating major moves only through *scripts/release.sh*." (266);
   "The script moves the major only after the release contract proves
   the new tag." (269)
   Rule: synonym rotation (the term is "floating tag"; "the major" names
   the version line at 248 and 382). Severity: should.
   Fix: "The floating tag moves only through *scripts/release.sh*." and
   "The script moves the floating tag only after the release contract
   proves the new tag." ("Float the major" in Table 14.3 is the script's
   own step name and stays.)

10. "Two steps on `printshop` publish the bundle." (374)
    Rule: wrong term (the next two sentences name a job and a job, not
    steps). Severity: should.
    Fix: "Two jobs on `printshop` publish the bundle."

11. "A shell line could have read the slug straight from
    *config/metadata.yaml*. It would then have held a second copy of the
    slug law, and the first law of the press forbids that." (66)
    Rule: perfect tense. Severity: should.
    Fix: "A shell line could read the slug straight from
    *config/metadata.yaml*. It would then hold a second copy of the slug
    law, and the first law of the press forbids that."

12. "Before the step starts, GitHub has already checked out the press at
    the action's ref." (101)
    Rule: perfect tense. Severity: should.
    Fix: "Before the step starts, GitHub checks out the press at the
    action's ref."

13. "It reports the major the book pins and any migration it has
    recorded." (388, Table 14.4)
    Rule: perfect tense. Severity: should.
    Fix: "It reports the major the book pins and any migration it
    recorded."

14. "The reader site already travels in *dist/* as *alice-site.zip*, the
    Chapter edition (the reader site and its zip), and the Pages bundle
    travels in its own artifact in step 5." (68)
    Rule: two ideas (30 words, two directories, two reasons).
    Severity: should.
    Fix: "The reader site already travels in *dist/* as *alice-site.zip*,
    part of the Chapter edition (the reader site and its zip). The Pages
    bundle travels in its own GitHub artifact in step 5."

15. "The credentials block authenticates the pull with the workflow's own
    token. The image is public, and that token works for it on fork and
    Dependabot pull requests too, so no book configures a secret." (181)
    Rule: two ideas (the last sentence carries three clauses), and the
    paragraph changes topic from the pin to the credentials.
    Severity: should.
    Fix: start a new paragraph at "The credentials block", then: "The
    image is public, and that token works for it on fork and Dependabot
    pull requests too. No book configures a secret."

16. "The `consumer` run comes from the press's integration gate, which in
    the press's words must "build the wheel, scaffold a stranger's book,
    run the whole `press all`, and prove tampering turns the verifier
    red"." (286)
    Rule: sentence over 30 words (33). Severity: should.
    Fix: "The `consumer` run comes from the press's integration gate. In
    the press's words, that gate must "build the wheel, scaffold a
    stranger's book, run the whole `press all`, and prove tampering turns
    the verifier red"."

17. "The runner installs press from the composite action, builds inside
    the toolchain image, and throws the machine away at the end." (38)
    Rule: hidden actor (GitHub discards the machine, as the sentence
    before says it supplies one; the runner is the machine).
    Severity: should.
    Fix: "The runner installs press from the composite action and builds
    inside the toolchain image. At the end, GitHub throws the machine
    away."

18. "A book author does not need them, and opens a receipt only to answer
    a question such as which toolchain digest a release used." (224)
    Rule: second person. Severity: should.
    Fix: "You do not need them. You open a receipt only to answer a
    question such as which toolchain digest a release used."

19. "A change of design waits for `v4`, and a book reaches it only when
    its owner moves the pin." (248)
    Rule: second person. Severity: should.
    Fix: "A change of design waits for `v4`, and your book reaches it
    only when you move the pin."

20. "A book stays on its major until its owner moves the pin." and "When
    the owner does want the next major, `press migrate` moves the pin."
    (382)
    Rule: second person. Severity: should.
    Fix: "A book stays on its major until you move the pin." and "When
    you want the next major, `press migrate` moves the pin."

21. "Tip: Set two sentinels and a page floor of 24 or more before your
    first release tag." (345)
    Rule: warning before the step (the tip follows the procedure it
    protects; a reader who follows steps 1 to 3 meets it after the tag
    has failed). Severity: should.
    Fix: move the tip above "To release the Alice book as version
    1.0.0:" unchanged.

22. "even when a release run stopped half way" (269)
    Rule: era spelling (American "halfway"). Severity: should.
    Fix: "Never move a floating tag by hand, even when a release run
    stopped halfway."

23. "GitHub cancelled the job that asked for it within a second" (326,
    footnote)
    Rule: era spelling (American "canceled"). Severity: should.
    Fix: "GitHub canceled the job that asked for it within a second, with
    "configuration not supported"." If "cancelled" is GitHub's own
    status word, set it in code instead.

24. The sidebar "The release script that rewrote mypy" (323)
    Rule: paragraph over six sentences (ten in one paragraph).
    Severity: should.
    Fix: break before "The repair has two parts." The first paragraph
    tells the failure (six sentences), the second the repair (four).

25. "We replaced the long description, ... with `...`" (76); "We elided
    the comment above the variable and the validation block" (123); "We
    cut the image line after `sha-`" (161); "which we folded to fit the
    page" (357); "We folded the long lines to fit the page." (417)
    Rule: "we" outside the authors' judgment (the Chapter 13 precedent).
    Severity: may.
    Fix: "Example 14.1 replaces the long description, ... with `...`,
    and every line that remains is verbatim." / "Example 14.2 elides the
    comment above the variable and the validation block, which the text
    describes." / "Example 14.3 cuts the image line after `sha-`,
    because ..." / "the job stops with this message, folded here to fit
    the page:" / "Example 14.5 folds the long lines to fit the page."

26. "Warning: ... The self-checkout keeps a private book working with no
    token for a second repository, and it pins the installed press to
    the action's exact ref." (108)
    Rule: repetition (style guide 8.1: an admonition that repeats the
    paragraph above it; 105 says the same thing twice already).
    Severity: may.
    Fix: keep the imperative and drop the restatement: "Do not replace
    the install step with a `pip install` from a Git URL, in the press or
    in a fork of it."

27. "The input reaches the script as the environment variable
    `PRESS_COMMAND`. The elided comment says why: "The input reaches the
    script as an environment value, ..."" (139)
    Rule: repetition (the prose sentence and the quotation open with the
    same words). Severity: may.
    Fix: "The elided comment says why the input reaches the script as the
    environment variable `PRESS_COMMAND`: "... never interpolated into
    shell text, so metacharacters are data."" or cut the prose sentence.

28. "The subject here is the pin." (155)
    Rule: meta-narration. Severity: may.
    Fix: cut the sentence. The paragraph reads "Chapter 2 describes what
    the toolchain image holds and how to pull it. The press's workflow
    *toolchain.yml* builds ...".

29. "A book pinned to `v3.0.2` directly enters the chart one box later and
    reaches the same bytes." (232)
    Rule: synonym rotation ("chart" for the figure) and a misplaced
    modifier. Severity: may.
    Fix: "A book pinned directly to `v3.0.2` enters the figure one box
    later and reaches the same bytes."

30. "*The release contract* is the workflow that proves a press tag, ...
    It runs on every tag that matches ... and proves five things in
    order:" (276)
    Rule: definition typography (only the term is italic, not "The"),
    and step 5 is an upload, not a proof. Severity: may.
    Fix: "The *release contract* is ..." (or roman, per item 7), and
    "... and runs five steps in order:". Also fact: see fact checker.

31. "The script then takes a preflight and five steps, which Table 14.3
    lists." (290)
    Rule: the action in the verb ("takes" a preflight). Severity: may.
    Fix: "The script then runs a preflight and five steps, which Table
    14.3 lists."

32. "The order of the arcs carries the safety." (303)
    Rule: noun stack in spirit (an abstraction does the acting).
    Severity: may.
    Fix: "The order of the arcs keeps every book safe." or cut it, since
    the next two sentences say what the order does.

33. "The commerce gate also stops advising and enforces its findings, for
    a book with print ordering turned on, as Chapter 7, *Building the
    editions*, explains." (330)
    Rule: condition first. Severity: may.
    Fix: "For a book with print ordering turned on, the commerce gate
    also stops advising and enforces its findings, as Chapter 7,
    *Building the editions*, explains."

34. "It has the landing page, a copy of the reader under *read/*, and
    every download under *downloads/*." (372)
    Rule: wrong term ("the reader" reads as the person; the chapter says
    "reader site" at 68). Severity: may.
    Fix: "It has the landing page, a copy of the reader site under
    *read/*, and every download under *downloads/*."

35. "The release notes and the Pages site depend on each other." (378)
    Rule: the paragraph describes a one-way dependence (the notes link
    into the site). Severity: may.
    Fix: "The release notes depend on the Pages site." Also fact: see
    fact checker.

36. "From v1 to v2" / "From v2 to v3" / "Before version 3.0.1, the plan
    told v2 users" (411); "a move from v2 to v3" / "on v3" (414); "v4
    does not exist" (417)
    Rule: code typography (style guide 4: tags are literals; 248 and 444
    set `v3` and `v4` in constant width). Also "v2 users" is third
    person. Severity: may.
    Fix: set each tag in code, and "Before version 3.0.1, the plan told
    you, on `v2`, that your geometry would not change."

37. "At the time of this writing, v4 does not exist, and the plan
    proposes it anyway, because it always proposes the current major plus
    one." (417)
    Rule: two ideas. Severity: may.
    Fix: "At the time of this writing, `v4` does not exist. The plan
    proposes it anyway, because it always proposes the current major plus
    one."

38. "The expression yields 1 on a tag whose name starts with `v`" (64)
    Rule: code typography (the value is a literal string). Severity: may.
    Fix: "The expression yields `1` on a tag whose name starts with `v`,
    and an empty string on every other run."

39. "The workflow pins the checkout action and every other outside action
    to a 40-hex commit SHA." and "A commit SHA names one tree forever."
    (72)
    Rule: shorthand in prose ("40-hex"). Severity: may.
    Fix: "... to a commit SHA of 40 hexadecimal digits." Also fact: see
    fact checker (a SHA names one commit; "tree" is a narrower git
    object).

40. "the default branch" (32, 50, 62, 352, 374, 378) against "`main`"
    (266, 334, 345, 366, 374, 378)
    Rule: synonym rotation (both inside 378). Severity: may.
    Fix: name it once, "the default branch, `main`", at 32, then use
    `main` for the Alice book and keep "the default branch" only where
    the text quotes the workflow's condition.

41. "Centre: a repository cylinder" (36, art directive)
    Rule: era spelling (American "Center"). Severity: may (the directive
    does not print).
    Fix: "Center: a repository cylinder, ..."

42. Table 14.1, header "Runs on" (47)
    Rule: wrong term (the cells say when a job runs, but GitHub's
    `runs-on` names the machine, and the `build` row then says "It runs
    on `ubuntu-24.04`"). Severity: may.
    Fix: retitle the column "When it runs".

43. "The pattern is now anchored, so it matches only a line that begins
    with `version`." and "in a file that every later release commit
    touched again" (323, sidebar)
    Rule: hidden actor; and an unclear clause. Severity: may.
    Fix: "The maintainer anchored the pattern, so it now matches only a
    line that begins with `version`." For the second, say what the
    reader should learn, for example "... changed the Python version that
    mypy assumed, and every later release commit carried the change
    forward." (fact checker to confirm).

44. "In the repository's settings, open Pages and set Source to GitHub
    Actions, once per book repository, as Chapter 1 explains." (376)
    Rule: procedure apart from description. Severity: may.
    Fix: "Chapter 1 gives the one-time step: in the repository's
    settings, open Pages and set Source to GitHub Actions."

45. "The press's migration guide puts it plainly: "Old pins keep
    working", and a book that never repins stays on its major forever."
    (382)
    Rule: repetition (restates the sentence before it). Severity: may.
    Fix: "The press's migration guide puts it plainly: "Old pins keep
    working"."

46. "The digest appears in one place that you can read: the `image:` line
    of the press's *build.yml*" (161) against "The release receipt also
    names the digest" (183)
    Rule: fact: see fact checker (the two sentences contradict each
    other). No copy fix proposed.

47. "The script's notes say that "rerunning after any failure is the
    recovery procedure"." (311)
    Rule: fact: see fact checker (the phrase is in the press's
    *CLAUDE.md*; confirm the script carries it too before attributing
    it).
