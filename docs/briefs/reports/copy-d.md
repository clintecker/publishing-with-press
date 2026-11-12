# Copyedit: Appendix D, The toolchain, platform by platform

File: `book/appendices/d-the-toolchain.md`

## Status

REVISE. Two blocks, both watchlist sightings in prose ("proves" at 177,
"shipped" at 181). `press check` passes the whole book (exit 0), and its
jargon audit names no term in this file. The two blocks follow the Chapter
15 precedent: `jargon-allow` lets "proves" and "shipped" through, but in
these two sentences neither is press's own name for anything, and the
contract puts the watchlist on the one-sighting list.

Counts by severity: blocks 2, should 29, may 12, fact 1.

Most frequent rules broken: wrong term (11 items, counting the two
watchlist blocks), two ideas (9 as the primary rule, 11 counting items 9
and 14), rhythm (8, all may). Hidden actor follows with 5.

Line numbers are `cat -n` line numbers in the file as it stands.

## The ste_check findings, judged

ste_check reports 12 findings (180 sentences, average 10.9 words, max 32).

- `-ing` forms at 3 (the chapter title *Installing press*), 65 and 149
  (headings): accepted.
- Sentence length at 3 (29 words) is under the ceiling. 188 (32 words) is
  the index comment. Accepted.
- Semicolons at 100 (inside the guide's quoted sentence) and 188 (index
  comment): accepted. The semicolon at 63 is inside the quoted message in
  code. No prose semicolon.
- "whether" (28) and "therefore" (55, 100, 145): accepted under the
  80 percent rule. Item 5 rewrites 28 on other grounds.
- Passive at 175 ("is untested"): accepted. It is a heading, and
  "untested" is a predicate adjective.
- The checker misses one real passive with a hidden actor at 80 (item 17).

Also accepted on reading:

- "canonical" (38) is the install guide's own word ("The Dockerfile is the
  canonical package list", `docs/INSTALL.md`). "scaffolding" and "gate" in
  Table D.1 are the doctor's own words. "the retail EPUB gate" in Example
  D.3 is the guide's own comment. "shipped" at 84 is inside a quotation.
- "edit-render-look" (171) replaces the press notes' en dashes with
  hyphens. That is the dash law, not a misquotation.
- The opener at 3 ("This appendix gives the toolchain for each
  platform...") is the period opener the style guide allows (8.1, "keep it
  to the opener").
- "..., not in your EPUB" (63) and "..., not from press" (67) are factual
  contrasts, not the staged "not X but Y".
- "job" at 112 is a GitHub Actions job, the platform's own word.
- Second person and present tense hold throughout. "We" appears only for
  the authors' recommendations (67, 106) and "our addition" (67). There is
  no "I". No perfect tense.
- Dry understatement appears at 30 ("A few programs escape the doctor"),
  116 ("The run looks hung, and it is not"), 130 ("the whole repair"), and
  186 ("trust CI"), never in a heading. Headings are sentence case.
- Admonitions: the Tip (33) has three sentences and opens with an
  imperative; the Warning (60) has two and opens with a condition and a
  command. Both are under four sentences.
- Footnotes: d-runner carries history, d-colima an issue number and an
  aside. Neither holds a fact the body needs.
- American spelling throughout ("canceled" at 112). No "website",
  "email", "file name", "man page", "appendices", "towards", or "folder".
- Numbers: "two", "three", "four", "five" are spelled out. "status 0",
  versions, and "#276" keep numerals correctly.

## Findings

### Blocks

1. "The press states what it proves, and the rest of this appendix covers
   that ground." (177)
   Rule: wrong term (watchlist jargon, "proves", one-sighting list), and
   meta-narration ("the rest of this appendix" sits at the end of the
   appendix and points backward). Severity: blocks.
   Fix: "The press states what it tests, and the earlier sections of this
   appendix cover that ground."

2. "The press tests the pandoc and TeX Live that Ubuntu 24.04 shipped, as
   frozen in the image." (181)
   Rule: wrong term (watchlist jargon, "shipped", outside a quotation).
   Severity: blocks.
   Fix: "The press tests the pandoc and TeX Live that came with Ubuntu
   24.04, as the image freezes them."

### Should

3. "...the toolchain image that carries all of it..." (3), with the
   definition "*The toolchain image* is `ghcr.io/clintecker/press-toolchain`..."
   at 120.
   Rule: wrong term (first use is not italic and defined; the term
   appears at 3, 5, 38, and 57 before its definition). Severity: should.
   Fix at 3: "This appendix gives the toolchain for each platform the press
   supports, then *the toolchain image* that carries all of it, then what
   the press does not test." At 120, set "The toolchain image" in roman.

4. "A required tool that is absent makes the doctor report `MISSING`, and
   an optional one reports `absent`." (11)
   Rule: hidden actor (the second clause makes the tool report; the
   doctor reports). Severity: should.
   Fix: "If a required tool is absent, the doctor reports `MISSING`. If an
   optional tool is absent, the doctor reports `absent`."

5. "The doctor also reports `realesrgan`, which `press art enhance` uses
   for plate upscaling, and whether `OPENAI_API_KEY` and `GEMINI_API_KEY`
   are set." (28)
   Rule: two ideas. Severity: should.
   Fix: "The doctor also reports `realesrgan`, which `press art enhance`
   uses to upscale plates. It reports if `OPENAI_API_KEY` and
   `GEMINI_API_KEY` are set."

6. "The container's epubcheck wrapper needs `java`." (30)
   Rule: wrong term (the toolchain image, not "the container").
   Severity: should.
   Fix: "The toolchain image's epubcheck wrapper needs `java`."

7. "The press's own documentation site drives a headless Chrome for its
   layout check, and no book needs it." (30)
   Rule: two ideas (unrelated facts), and era spelling ("site" for Web
   site). Severity: should.
   Fix: "The press's own documentation Web site drives a headless Chrome
   for its layout check. No book needs Chrome."

8. "It exits with status 0 and prints `this machine can make books` when
   the machine is ready." (33, in the Tip)
   Rule: condition first. Severity: should.
   Fix: "When the machine is ready, it exits with status 0 and prints
   `this machine can make books`."

9. "The press's *Dockerfile* builds the toolchain image from Ubuntu 24.04,
   and its package list is the canonical list for Debian and Ubuntu." (38)
   Rule: hidden actor (the press builds the image from the Dockerfile, as
   120 says), and two ideas. Severity: should.
   Fix: "The press builds the toolchain image from Ubuntu 24.04 with its
   own *Dockerfile*. That file's package list is the canonical list for
   Debian and Ubuntu."

10. "The packages divide by job." (49)
    Rule: wrong term ("job" is on the never list for target, and 112 uses
    it for a CI job; this is a third sense). Severity: should.
    Fix: "Each package has its own work."

11. "`texlive-luatex` and `latexmk` set the PDF, and `texlive-latex-extra`
    brings lettrine, the package behind the drop cap." (49)
    Rule: two ideas, and wrong term (the Print edition is never named or
    glossed in the appendix, while the Circulating edition is glossed in
    the same paragraph). Severity: should.
    Fix: "`texlive-luatex` and `latexmk` set the Print edition (the PDF).
    `texlive-latex-extra` brings lettrine, the package behind the drop
    cap."

12. "Ubuntu has no `fonts-libertinus` package, and `--no-install-recommends`
    drops the Libertine keyboard face." (55)
    Rule: two ideas. Severity: should.
    Fix: "Ubuntu has no `fonts-libertinus` package. Also,
    `--no-install-recommends` drops the Libertine keyboard face."

13. "Keep that package in your own list if you copy the flag." (55)
    Rule: condition first. Severity: should.
    Fix: "If you copy the flag, keep that package in your own list."

14. "The system manages Ubuntu 24.04's Python, and that Python refuses a
    bare `pip install` into its own site-packages directory." (67)
    Rule: hidden actor ("the system"), and two ideas. Severity: should.
    Fix: "Ubuntu 24.04 manages its own Python. That Python refuses a bare
    `pip install` into its site-packages directory."

15. "That rule comes from Python's packaging standards (PEP 668), not from
    press, and the press's install guide does not mention it." (67)
    Rule: two ideas. Severity: should.
    Fix: "That rule comes from Python's packaging standards (PEP 668), not
    from press. The press's install guide does not mention it."

16. "Example D.2 adds that package, which is our addition, and installs
    press from Git at the floating tag `v3`." (67)
    Rule: two ideas ("which is our addition" repeats "adds"), and wrong
    term ("floating tag" is not italic or defined at its first use in the
    appendix). Severity: should.
    Fix: "Example D.2 adds that package to the press's list. It then
    installs press from Git at the *floating tag* `v3`, the tag that moves
    to each compatible v3 release."

17. "Press is not published to PyPI." (80)
    Rule: hidden actor (passive; ste_check misses it). Severity: should.
    Fix: "The press does not publish press to PyPI." (Or: "Press is not on
    PyPI.")

18. "For the desk, install the `tui` extra with ..." (80)
    Rule: wrong term (first use of "the desk" in the appendix is not
    italic or glossed). Severity: should.
    Fix: "For *the desk* (`press desk`), install the `tui` extra with
    `"press[tui] @ git+https://github.com/clintecker/press@v3"`."

19. "In its compatibility notes, "the exact tool versions are whatever
    Ubuntu 24.04 shipped, frozen by the image digest"." (84)
    Rule: hidden actor (the sentence has no verb and no actor; it is a
    fragment). Severity: should.
    Fix: "Its compatibility notes say that "the exact tool versions are
    whatever Ubuntu 24.04 shipped, frozen by the image digest"."

20. "On macOS, Homebrew supplies the toolchain and a TeX distribution."
    (88)
    Rule: wrong term (the toolchain already includes LuaLaTeX and TeX
    Live, so "and a TeX distribution" counts it twice). Severity: should.
    Fix: "On macOS, Homebrew supplies the whole toolchain, TeX
    distribution included."

21. "The strict EPUB gate runs in CI whatever your workstation lacks."
    (102)
    Rule: synonym rotation (Table D.1 and Example D.3 call it "the retail
    EPUB gate"). Severity: should.
    Fix: "The retail EPUB gate runs in CI whatever your workstation lacks."

22. "Install it locally if you want to see epubcheck's faults before you
    push." (102)
    Rule: condition first. Severity: should.
    Fix: "If you want to see epubcheck's faults before you push, install
    the formula locally."

23. "The variable `PRESS_TOOLCHAIN` tells press that it runs in the
    reference environment, and press keys its strictness on it." (139)
    Rule: two ideas (and three "it"s with two referents). Severity: should.
    Fix: "The variable `PRESS_TOOLCHAIN` tells press that it runs in the
    reference environment. Press sets its strictness from that variable."

24. "The release contract refuses a three-part press tag whose workflow
    names only a `sha-` tag." (145)
    Rule: wrong term ("immutable tag" is the vocabulary's term for
    `v3.0.2`; "workflow" should be the reusable workflow). Severity: should.
    Fix: "The release contract refuses an immutable tag whose reusable
    workflow names only a `sha-` tag."

25. "In CI the reusable workflow authenticates the pull with the
    workflow's own `GITHUB_TOKEN`, which works for a public image on fork
    and Dependabot pull requests too." (147)
    Rule: two ideas (28 words). Severity: should.
    Fix: "In CI, the reusable workflow authenticates the pull with its own
    `GITHUB_TOKEN`. That token works for a public image on fork and
    Dependabot pull requests too."

26. "Inside the image, `pip install` needs `--break-system-packages`,
    because Debian manages the image's Python." (165)
    Rule: synonym rotation (67 says Ubuntu 24.04 manages its Python; the
    image is Ubuntu). Severity: should. Fact: see fact checker, if
    "Debian" is meant as the packaging lineage.
    Fix: "Inside the image, `pip install` needs `--break-system-packages`,
    because Ubuntu manages the image's Python."

27. "Then install that same three-part press tag." (167)
    Rule: wrong term (immutable tag). Severity: should.
    Fix: "Then install press at that same immutable tag."

28. "It reads the image from *build.yml*, so it runs the image the release
    contract pins." (171)
    Rule: wrong term (the reusable workflow pins the image, as 145 says;
    the release contract proves a tag). Severity: should.
    Fix: "It reads the image from *build.yml*, so it runs the image that
    the reusable workflow pins."

29. The list at 179 to 184 ("**Windows.** ...", "**Other Linux
    distributions.** ...", and four more).
    Rule: bold labels on every list item (the contract's tell is "bold
    labels with colons on every list item"; these use periods, which is
    the same pattern). Severity: should.
    Fix: Make it a two-column table, "Area | What the press says", with
    the labels as plain first-column cells, or drop the bold and keep each
    item as one plain sentence ("The press does not test Windows.").

30. "Other installers, such as pipx, may work, because press is an ordinary
    command-line package, but the press does not document or test them."
    (183)
    Rule: two ideas. Severity: should.
    Fix: "Other installers, such as pipx, may work, because press is an
    ordinary command-line package. The press does not document or test
    them."

31. "It states no figure for how long a build takes." (184)
    Rule: wrong term ("figure" is the numbered illustration). Severity:
    should.
    Fix: "It states no number for how long a build takes."

### May

32. "`press art enhance` uses `oxipng` or `pngcrush` when either is
    present." (30)
    Rule: condition first. Severity: may.
    Fix: "When `oxipng` or `pngcrush` is present, `press art enhance` uses
    it."

33. "Two packages in the list carry a *scar*, ..." (53), under the heading
    "Two Ubuntu scars".
    Rule: heading repeated as the first sentence. Severity: may.
    Fix: "Each of two packages in the list carries a *scar*, the press's
    word for a production failure turned into a guard."

34. "The command exists, and `which` finds it, but it dies with "Exec
    format error" only when it runs." (57)
    Rule: rhythm (three clauses, three "it"s). Severity: may.
    Fix: "The command exists and `which` finds it. It dies with "Exec
    format error" only when it runs."

35. "We recommend a virtual environment of its own for press." (67)
    Rule: rhythm. Severity: may.
    Fix: "We recommend that you give press a virtual environment of its
    own."

36. "Of fonts, the guide says: ..." (100)
    Rule: rhythm (inverted opener). Severity: may.
    Fix: "About fonts, the guide says: ..."

37. "...because the press publishes an arm64 build of the toolchain
    image." (110)
    Rule: synonym rotation ("build" here means an image variant; the
    appendix uses "build" for a book build everywhere else). Severity: may.
    Fix: "...because the press publishes the toolchain image for arm64."

38. "stylua v2.5.2, and selene 0.31.0 on amd64, the Lua tools the press
    runs over its own filters" (128)
    Rule: rhythm (the scope of "on amd64" is unclear). Severity: may.
    Fact: see fact checker for which tool is amd64-only.
    Fix: "stylua v2.5.2 on both architectures and selene 0.31.0 on amd64
    only: the Lua tools the press runs over its own filters"

39. "...because `CI=false` would read as truthy." (139)
    Rule: era spelling (modern programmer's idiom). Severity: may.
    Fix: "...because a check for any value would read `CI=false` as true."

40. "...so `press art enhance` there resamples a plate instead of upscaling
    it." (143)
    Rule: rhythm. Severity: may.
    Fix: "...so on arm64 `press art enhance` resamples a plate instead of
    upscaling it."

41. "On macOS with Colima it can mount a book only under `$HOME`." (171)
    Rule: rhythm (comma after the introductory phrase). Severity: may.
    Fix: "On macOS with Colima, it can mount a book only under `$HOME`."

42. "...so a Mac may carry other releases than the image does." (181)
    Rule: rhythm. Severity: may.
    Fix: "...so a Mac may carry different releases from the image."

43. "Then run the same target in the toolchain image on your own machine,
    pinned by the same digest, to see the reference result locally." (186)
    Rule: rhythm ("on your own machine" and "locally" say the same thing).
    Severity: may.
    Fix: "Then run the same target in the toolchain image, pinned by the
    same digest, to see the reference result on your own machine."

### Fact

44. "It names the same packages as Example D.3 in one line." (104)
    Fact: see fact checker. Example D.3 also installs `epubcheck`, and the
    quoted hint `brew install pandoc mactex-no-gui poppler` does not.
