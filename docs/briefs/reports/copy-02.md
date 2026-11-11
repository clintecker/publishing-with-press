# Copyedit report: Chapter 2, Installing press

File: `book/chapters/02-installing-press.md`. Read against
`docs/prose-contract.md`, `docs/style-guide.md` sections 3, 4, and 8, and
`docs/vocabulary.md`.

## Checker run

`python3 tools/ste_check.py book/chapters/02-installing-press.md`: 52
findings, 371 sentences, average 13.1 words, maximum 118. Triage:

- Every semicolon finding (lines 115, 158, 202, 213, 220, 221, 311, 380)
  sits in an art directive, a quotation from the press's own docs, or the
  index comment. The prose has no semicolons and no em or en dashes.
- The long-sentence findings at 115, 202, 220, 311, and 380 are art
  directives, doctor output, or the index comment. The ones at 35 and 88
  are counter artifacts (a footnote marker joins two sentences).
- The `-ing` findings on headings ("Installing", "Running", "Reading",
  "Pulling", "Verifying") are period-correct gerund headings, not riders.
- "therefore", "whether", "verify", "attempt" are kept by the contract's
  80% rule. "check out" (line 82) is the Git verb.
- The real findings the checker missed are below. `press check`'s banned
  patterns match nothing in the chapter.

## Findings

1. Line 19: "You can skip the toolchain entirely if you would rather not
   install it." Rule: condition first. Severity: may. Fix: "If you would
   rather not install the toolchain, you can skip it entirely."

2. Line 21: "The rest of the chapter takes them in the order you install
   them." Rule: meta-narration. Severity: may (style guide 8.1 allows an
   opener's look ahead). Fix: delete the sentence.

3. Line 33: "At the time of this writing, the continuous integration runs
   all five Python releases from 3.10 to 3.14 on Ubuntu, plus Python 3.12
   on macOS 15." Rule: synonym rotation (the chapter alternates
   "continuous integration" and "CI" without defining the short form).
   Severity: may. Fix: "At the time of this writing, the project's
   continuous integration (CI) runs all five Python releases from 3.10 to
   3.14 on Ubuntu, plus Python 3.12 on macOS 15." Use "CI" after this.

4. Line 33: "The Python requirement is a floor, and the tested range is a
   fact about the project's own testing." Rule: two ideas. Severity:
   should. Fix: "The Python requirement is a floor. The tested range
   records only what the project's own tests run."

5. Line 33: "A newer Python may work, but no test proves it yet, and
   `press doctor` will say so when you run it." Rule: two ideas.
   Severity: should. Fix: "A newer Python may work, but no test proves it
   yet. When you run `press doctor`, it says so."

6. Line 37: "...which is an honest label for a tool that still changes
   from one major version to the next." Rule: wrong term (watchlist:
   "honest"). Severity: may. Fix: "Its package metadata classifies it as
   "Development Status :: 4 - Beta", which fits a tool that still changes
   from one major version to the next."

7. Line 70: "Example 2.2 shows the form, with `alice` keeping her clone of
   press under her home directory on `hatter`." Rule: -ing rider.
   Severity: may. Fix: "In Example 2.2, `alice` keeps her clone of press
   under her home directory on `hatter`."

8. Line 82: "An editable install trades stability for reach." Rule: a
   saying dressed as depth. Severity: may. Fix: "An editable install
   follows whatever branch you check out."

9. Line 86: "The `tui` extra adds Textual, the library behind the desk,
   press's full-screen operator console." Rule: wrong term ("operator" is
   reserved for `press improve`, `press research`, `press aesthetic`) and
   a stacked appositive. First use of "the desk" is not italic. Severity:
   should. Fix: "The `tui` extra adds Textual, the library behind *the
   desk*, press's full-screen console."

10. Line 86: "The install documentation spells the command
    `pip install 'press[tui]'`." Rule: synonym rotation (everywhere else
    it is "the install guide"). Severity: may. Fix: "The install guide
    spells the command `pip install 'press[tui]'`."

11. Line 86: "Put the `[tui]` after the name `press` in whichever form of
    the requirement you use, the Git URL or a clone." fact: see fact
    checker (a clone install names no `press`; the PyPI spelling quoted
    just before it cannot work, as report-02 already flags).

12. Line 103: "Other Python installers may well work, since press is an
    ordinary command-line package, but the project does not test them and
    this book does not describe them." Rule: meta-narration ("text about
    the document itself", one-sighting list), plus two ideas. Severity:
    blocks. Fix: "Other Python installers may work, because press is an
    ordinary command-line package. The project does not test them."

13. Line 107: "For now, remember that the press on `printshop` and the
    press on `hatter` arrive by different roads, and that both roads start
    at the same tag." Rule: one-line closer. Severity: may. Fix: "The
    press on `printshop` and the press on `hatter` arrive by different
    roads, but both roads start at the same tag."

14. Line 111: "Press calls each command that builds, checks, or verifies a
    *target*, and most targets call at least one of these programs."
    Rule: two ideas (and "press calls" collides with "programs that press
    calls" in the opener). Severity: should. Fix: "Each command that
    builds, checks, or verifies is a *target*. Most targets call at least
    one of these programs."

15. Line 137: "The epubcheck program is the validator that retail ebook
    channels run on an EPUB before they accept it." Rule: wrong term
    ("validator" is on the never list for verifier) and era spelling
    ("e-book", as "e-mail"; Chapter 1 line 113 has the same "ebook").
    Severity: should. Fix: "The epubcheck program is the program that
    retail e-book channels run on an EPUB before they accept it."

16. Line 139: "It looks for `realesrgan`, the upscaler behind
    `press art enhance`, which is optional." Rule: two ideas (the "which"
    can attach to either noun). Severity: may. Fix: "It looks for
    `realesrgan`, the optional upscaler behind `press art enhance`."

17. Line 141: "The `art enhance` target can use `oxipng` or `pngcrush` to
    shrink a PNG further, if either one is present." Rule: condition
    first. Severity: may. Fix: "If `oxipng` or `pngcrush` is present, the
    `art enhance` target can use it to shrink a PNG further."

18. Line 160: "The gate still runs strictly in the toolchain image, so you
    will learn about an EPUB fault eventually, but you will learn about it
    later and somewhere else." Rule: two ideas. Severity: may. Fix: "The
    gate still runs strictly in the toolchain image. You will learn about
    an EPUB fault eventually, but later and somewhere else."

19. Line 163 (Tip): "Install epubcheck on your own machine. An EPUB fault
    that you see at your desk costs you a minute, and the same fault that
    you first see in CI costs you a round trip." Rule: admonition repeats
    the paragraph above (style guide 8.1); "at your desk" collides with
    *the desk*. Severity: should. Fix: delete the Tip and end the line-160
    paragraph with "An EPUB fault that you see on your own machine costs
    you a minute, and the same fault that you first see in CI costs you a
    round trip."

20. Line 168: "On Debian and Ubuntu, the canonical package list is the
    press's own `Dockerfile`..." Rule: wrong term (watchlist "canonical";
    jargon-allow passes it, but here it is not press's own name).
    Severity: may. Fix: "On Debian and Ubuntu, the reference package list
    is the press's own `Dockerfile`, because that file builds the
    toolchain image that every CI build uses."

21. Line 180: "...holds lettrine, the LaTeX package behind the chapter
    opening's large initial." Rule: wrong term ("initial" is on the never
    list for chapter opening). Severity: may. Fix: "The package
    `texlive-latex-extra` holds lettrine, the LaTeX package that sets the
    large first letter of each chapter opening." (Keep "foliate initials"
    for `yinit`: it is the font's own description.)

22. Line 182 and Warning at line 185: the warning about
    `fonts-linuxlibertine` follows Example 2.4, the command it protects.
    Rule: warning before the step (prose contract, Pass 2). Severity:
    should. Fix: move the Warning to sit directly before Example 2.4, its
    text unchanged: "Do not drop `fonts-linuxlibertine` from the command
    because the TeX packages look like enough. With
    `--no-install-recommends`, nothing else in the list installs the
    Libertine keyboard face."

23. Lines 194, 307 (and 163, item 19): "to see the reference result at your
    own desk"; "which suits an experiment at your desk". Rule: wrong term
    (*the desk* is `press desk`). Severity: may. Fixes: "Then run the same
    build in the toolchain image on `hatter` to see the reference result
    on your own machine." / "The example uses `:latest`, which suits an
    experiment on your own machine."

24. Line 200: "The final line names what stands between this machine and
    readiness." Rule: noun stack (the action is in the noun; "readiness"
    is on the watchlist). Severity: may. Fix: "The final line names the
    tool that keeps this machine from being ready."

25. Line 253 (Warning): "The press shipped exactly that failure once, and
    the rule against it is now a scar." Rule: wrong term (watchlist
    "ship", on the one-sighting list; `config/house-rules.yaml`
    jargon-allow lists "shipped", so `press check` passes it). Severity:
    blocks. Fix: "The press once released exactly that failure, and the
    rule against it is now a scar."

26. Line 271: "The variable `PRESS_TOOLCHAIN` tells press that it runs in
    the reference environment, and press keys its toolchain strictness on
    that variable." Rule: two ideas. Severity: may. Fix: "The variable
    `PRESS_TOOLCHAIN` tells press that it runs in the reference
    environment. Press decides how strict its toolchain checks are from
    that variable."

27. Line 273: "The epubcheck wrapper deserves its own warning, because it
    hides a failure that cost the first book real time." Rule: hidden
    actor (the wrapper does not hide the failure; the launcher it replaces
    does). Severity: should. Fix: "The epubcheck wrapper deserves its own
    warning, because the launcher it replaces hides a failure that cost
    the first book real time."

28. Line 276 (Warning): "It needs binfmt_misc, which containers do not
    register, so the command exists, `which` finds it, and it dies with
    "Exec format error" only when it runs." Rule: two ideas. Severity:
    should. Fix: "It needs binfmt_misc, which containers do not register.
    The command exists and `which` finds it, but it dies with "Exec format
    error" only when it runs."

29. Line 279: "A missing validator and a broken validator call for
    different repairs, and neither one tells you anything about the
    book." Rule: wrong term ("validator"). Severity: should. Fix: "A
    missing epubcheck and a broken epubcheck call for different repairs,
    and neither one tells you anything about the book."

30. Line 291: "Example 2.5 shows the form from the press's install guide,
    with `alice` building every edition of her book from its repository on
    `hatter`." Rule: -ing rider. Severity: may. Fix: "Example 2.5 shows the
    form from the press's install guide. In it, `alice` builds every
    edition of her book from its repository on `hatter`."

31. Line 305: "The artifacts stay behind in the *dist/* directory of your
    book repository..." Rule: code typography (style guide 4: a literal
    path is constant width; italic marks replaceable text). Severity:
    should. Fix: "The artifacts stay behind in the `dist/` directory of
    your book repository, because that directory lives on the mounted
    volume."

32. Line 316: "Apple Silicon is the maintainer's primary platform, and the
    Homebrew route in Example 2.3 is the one the install guide gives for
    it." Rule: two ideas. Severity: may. Fix: "Apple Silicon is the
    maintainer's primary platform. The install guide gives the Homebrew
    route in Example 2.3 for it."

33. Line 318: "The press's own full verification script,
    `scripts/verify.sh --full`, also runs natively on Apple Silicon for the
    same reason, so contributors to the press need no emulation either."
    Rule: two ideas. Severity: should. Fix: "The press's own full
    verification script, `scripts/verify.sh --full`, also runs natively on
    Apple Silicon for the same reason. Contributors to the press need no
    emulation either."

34. Line 322: "CI runs every tested Python release on Ubuntu, and the image
    itself is Ubuntu 24.04, so Ubuntu has the strongest record of any
    platform." Rule: two ideas. Severity: may. Fix: "CI runs every tested
    Python release on Ubuntu, and the image itself is Ubuntu 24.04. Ubuntu
    therefore has the strongest record of any platform."

35. Line 324: "Windows is not tested." Rule: hidden actor (also a rare
    one-line paragraph). Severity: should. Fix: "The project does not test
    Windows." (Better appended to the line-322 paragraph.)

36. Line 336 (step 3): "Create a book, or change into an existing book
    repository:" with only `$ cd ~/alice` beneath it. Rule: two ideas (a
    procedure step is a single imperative, style guide 3.6). Severity:
    may. Fix: "Change into the book repository:"

37. Line 341: "For this chapter, the interesting part is what happens
    during step 4 on a machine that has never run LuaLaTeX before." Rule:
    meta-narration (one-sighting list) and perfect tense. Severity:
    blocks. Fix: "On a machine where LuaLaTeX runs for the first time,
    step 4 holds a surprise."

38. Lines 341 and 370: both point to Chapter 3 for creating the `alice`
    book with `press new`; line 370 also "walks through every file it
    makes". Rule: synonym rotation (the same pointer twice in different
    words). Severity: may. Fix at 341: "Chapter 7, *Building the
    editions*, explains what `press all` builds." Fix at 370: "The next
    chapter, *The shape of a book repository*, creates the `alice` book
    with `press new` and describes every file it makes."

39. Lines 345 and 350: the body paragraph and the sidebar's first
    paragraph state the same facts in the same order ("The first time
    LuaLaTeX runs on a fresh machine, it scans the fonts..." / "The scan
    takes several minutes." twice). Rule: a sidebar that repeats the
    paragraph above (style guide 8.1). Severity: should. Fix: the sidebar's
    first paragraph becomes "During the scan, the build prints little, and
    the terminal sits still while the processor works."

40. Line 348: sidebar title "The hang that isn't". Rule: dry
    understatement in a heading (style guide 3.1), with a contraction.
    Severity: should. Fix: "The first-run font scan".

41. Line 356: "The remedy is patience." Rule: a saying dressed as depth.
    Severity: may. Fix: "Wait for the scan to finish."

42. Line 358: "The press's documentation describes no other build timing,
    and this book does not invent one." Rule: meta-narration ("text about
    the document itself", one-sighting list). Severity: blocks. Fix:
    delete the sentence.

43. Line 358: "A build that stays silent for several minutes on a fresh
    machine is almost certainly the scan, and the right response is to
    wait for it." Rule: one-line closer (repeats the sidebar's remedy and
    the paragraph). Severity: may. Fix: "If a build on a fresh machine
    stays silent for several minutes, wait: it is almost certainly the
    scan."

44. Line 362: "By the time `press all` finishes, the verifiers inspected
    each artifact as an object, the way a reader or a retailer will meet
    it." Rule: perfect tense (avoiding "have inspected" left a broken
    tense sequence). Severity: should. Fix: "Before `press all` finishes,
    the verifiers inspect each artifact as an object, the way a reader or
    a retailer will meet it."

45. Line 362: "A red result means one verifier refused an artifact, and
    Chapter 8, *Verifying the artifacts*, explains how to read the
    refusal." Rule: wrong term ("refuse" is what press does when it stops;
    a verifier result is "fail"). Severity: should. Fix: "A red result
    means that a verifier failed an artifact. Chapter 8, *Verifying the
    artifacts*, explains how to read the failure."

46. Lines 364 and 367: "Either way, rerun `press doctor` after you change
    the toolchain. The report on your screen then describes the machine
    you actually have." followed by the Tip "Run `press doctor` again
    after every change to the toolchain..." Rule: admonition repeats the
    paragraph above (style guide 8.1). Severity: should. Fix: end the
    paragraph at "...or accept the local warning and let the toolchain
    image run the strict gate." and keep the Tip.

47. Line 376 (footnote): "...so the lesson reached a second tool." Rule:
    wrong term ("lesson" is on the never list for scar). Severity: should.
    Fix: "The `Dockerfile`'s comment on Real-ESRGAN refers to the same trap
    as "the epubcheck/binfmt scar", so the scar reached a second tool."

48. Line 378 (footnote): "GitHub retired that runner partway through a
    release, and it cancelled every job there within a second with
    "configuration not supported"." Rule: era spelling (American
    "canceled"), with an ambiguous "it". Severity: should. Fix: "GitHub
    retired that runner partway through a release. GitHub then canceled
    every job on it within a second with "configuration not supported"."

49. Lines 115, 202, 221, 311: art directives spell "labelled", "Centre", "colour". Rule:
    era spelling (American spelling). Severity: may (directives do not
    print, but the art desk copies their words onto figures: "labelled
    "Lua filters"" is safe, a printed "colour" would not be). Fix:
    "labeled", "Center", "color".

## House-wide checks

- Second person and present tense: held throughout. History is in the
  past tense, as it should be.
- "We": once (line 160, "we recommend it anyway"), the authors' judgment.
  No "I".
- Dry understatement: lines 37 (removed by item 6), 345 ("a very
  convincing imitation"), 356 (cup of tea), 372 (footnote, "a poor fate
  for a word in a title"). About right for the length. One sits in a
  heading (item 40).
- Admonitions: six (three Tips, three Warnings), all imperative, all
  three sentences or fewer. Two repeat their paragraph (items 19, 46);
  one follows the step it protects (item 22).
- Footnotes: four, all asides. None carries a fact the body needs.
- Era spellings: "Web site" correct (line 141); no website, email, file
  name, man page, appendices, towards, or UNIX. "ebook" (item 15) and
  "cancelled" (item 48) are the exceptions.
- Numbers: every digit in prose is a version, measurement, exit status,
  step or chapter number, or code. "seven", "four", "eight", "two" are
  spelled out.
- Headings: sentence case throughout; none repeated as its first
  sentence.

## Note for the house (not counted)

- Style guide 3.7 numbers items chapter-dash-sequence ("Table 3-1"); the
  chapter and `docs/vocabulary.md` ("Figure 5.2") use a period. The
  chapter is consistent with the vocabulary. The two house documents
  contradict each other, and the house should pick one.

## Counts

- blocks: 4 (items 12, 25, 37, 42)
- should: 20
- may: 24
- fact: 1 (item 11)

Most frequent rules: two ideas (11), wrong term (10), meta-narration (4).
