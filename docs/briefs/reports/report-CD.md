# Report: Appendixes C and D

## Word counts (press wordcount)

- *book/appendices/c-messages.md*: 2,814 (target about 3,000; within 15 percent). Message text is inline code and is not counted.
- *book/appendices/d-the-toolchain.md*: 2,007 (target about 2,000).

## Figures, tables, examples

No figures (appendix rule). Appendix C has none. Appendix D: Table D.1 (the tools press doctor checks), Examples D.1 (apt line), D.2 (venv on Ubuntu), D.3 (Homebrew), D.4 (the epubcheck wrapper), D.5 (docker run). Each is referred to before it appears. Every fence is tagged `text`, no code line over 64 columns. Footnotes: `c-ellipsis`, `d-runner`, `d-colima`.

## Appendix C: grouping and sources

Groups: press check (source checks, self-test, style audit, jargon lint), the command line, press doctor, the PDF verifier, the formats verifier (including epubcheck and the EPUB ISBN message), the pages and archives verifiers, the print pack. 81 definition terms.

Messages taken from outside facts-C (verbatim, flag for the reviewer):
- `paragraph N has W words (the law is under 190; split it)` and the release-witness refusal (`this is a release build (PRESS_RELEASE=1) and its witnesses are vacuous:` with its two follow-on lines) are quoted from the continuity bible's shared facts, not facts-C. Chapter 6 promises Appendix C holds "the full list", so I included them. Cut if the rule is facts-C only.
- The press doctor messages come from facts-D (my other fact file).
- `manual number in heading` and `title-case heading` are the fixture expect strings from facts-C's fixture table; they are substrings of the real diagnostics (Ch. 6 shows `title-case heading: <text>`).
- `glyph U+2014 is outside the print-font set` is the fact file's captured instance.

Deviation from "exactly as quoted": facts-C ends `note: <fixture> also drew: ...` and the known-good message with U+2026. The glyph law refuses it, so I typed three periods and said so in footnote `c-ellipsis`.

Not covered for lack of quoted messages: intake (`press art accept`), registrations beyond the EPUB ISBN line, cover wrap verification (facts-C 6.7 lists checks, no messages), verify_pages commerce and metadata checks, the jargon lint's malformed-watchlist message (only exit 2 is stated). The print-pack section points to Chapters 11 and 12. The unfinished markers and the universal-battery trigger phrases are described, not typed, because the checker reads inline code (two fixture filenames also tripped the book's banned patterns and were rephrased).

Remedies are mine, kept to what the facts support (rebuild through the target that rebuilds, the config key named, or "report it to the press" where the fault is the press's own, such as the blank-page detector self-test and the cover-on-page-1 messages).

## Appendix D: notes

- Versions named are only those the fact files state: Ubuntu 24.04, Python 3.10 to 3.14, 3.12 on macOS 15, stylua v2.5.2, selene 0.31.0. No pandoc or TeX number.
- The venv advice and `python3-venv` are labeled as the book's own, per the facts-02 S2/S3 ruling, consistent with Chapter 2.
- facts-D 2.2 (INSTALL list) omits `gh`; 12.4 (Dockerfile) includes it. I said the image adds `gh` to Example D.1's list, as Chapter 2 does.
- "Other Linux distributions" untested: inferred from INSTALL.md naming Ubuntu 24.04 as the reference and nothing else. Worded as "names no other distribution and tests none".

## Checker residuals

`press check` passes (23 files). ste_check findings, defended:
- C: `verify` (a target name), `therefore` (period-correct per the contract), "Checking" in a chapter title cross-reference (Chapter 6, *Checking the manuscript*), a semicolon and 37 words on the index comment line.
- D: "Installing"/"Running" in headings, `whether`/`therefore` (allowed), a semicolon inside the install guide's quoted sentence ("TeX Live carries Libertinus for the PDF; nothing else to install."), "is untested" in the heading "What is untested", a 29-word opening sentence (under the 30 ceiling), and the index comment line.

## Revision C

Word count after revision: 3,263 (target about 3,000; within 15 percent).

Applied from facts-C, copy-c, type-c, and facts-C S1:

- Footnote `c-ellipsis` now says only that `...` stands for the diagnostics press prints after the colon. The marker moved out of the term into the Cause sentence of the known-good entry. The conventions paragraph says what `...` stands for.
- Eleven long messages (the ten the typesetter listed, plus the release refusal with its follow-on lines) are now short terms with the full message in an indented `text` block, broken at spaces, continuation lines indented, no line over 64 columns. A convention paragraph says press prints each as one line. Each block is introduced by "Press prints:" so the opening fence line is indented only; a fence opened on the `:   ` line was invisible to *tools/tag-fences.py*, which then tagged the closing fences (I repaired that, and a rerun now tags 0). `title-case heading: <text>` in full; the doctor's `[ BROKEN]` line shown whole.
- Source-check terms use S1's exact forms (trailing colon and `<path>`, `<field>`, `<sentinel>`). New entries: the orphan-plate refusal, the `fig-alt` refusal on `decorative=true`, `defaults reference a missing file` (command-line section), and the `verify-print` no-cover line (print pack). The curly-quote rule is described in words, and the banned-pattern form `<file>:<line>: <label>`, bare `press` (exit 2), the malformed-watchlist exit 2, and the unlisted source checks (with chapter pointers) each get a sentence.
- Audit directories follow S1: only heading and paragraph faults soften. The missing-source, level-1-heading, known-good, pypdf, and doctor-hint claims are cut back to what the files say. The command-line intro and the rule wordings (conclusion, parallelism, signposting) follow the fact check. The sentinel remedy shows the `--json` list form.
- Copyedit: both watchlist blocks fixed ("lands", "from clean"). Named actors, filename, "a drop cap", edition names glossed once with their format, "the sources companion", "manuscript witness line", "chapter witness line", Chapter 10's full title, present-tense Causes, and the remaining should/may items applied.
- Tools run: unnumber-appendix-heads (11 headings), tag-fences (0 after repair), prefix-footnotes (unchanged).
- Left out: S1's `duplicate source file: <path>`. No admitted source gives its cause.

`press check`: the first run failed only on *book/chapters/16-inside-the-press.md:232* (assistant vocabulary), which is another writer's file. The rerun passed. ste_check residuals are the same kinds as before: chapter title, "therefore", "verify", the index comment, a 28-word instruction sentence under the 30 ceiling, and "is malformed" used as an adjective.

## Revision D

Word count after revision: 2,235 (target about 2,000; within 15 percent). The additions the fact checker listed as missing account for the growth.

Applied from facts-D, copy-d, type-d, and facts-D S1:

- The Tip now gives exit statuses 0 and 1. The broken-optional-tool behaviour moved out of the Tip into its own paragraph, stated "at the time of this writing". The `pdfimages` line says "silently softens two checks to notes, so install poppler in full".
- Cut or reduced: lettrine "behind the drop cap" (now "the *Dockerfile* names `texlive-latex-extra` for lettrine"), "both hide until a build runs", "every CI build of every book" (now: the reusable workflow runs book builds inside it, pinned by digest), the Homebrew route "serves" Apple Silicon (and the macOS 15 CI sentence left that subsection), and stylua/selene as tools run over the filters (now "the image's Lua tooling", with a time hedge). The binfmt repair now has two parts, the wrapper and the verifier's toolchain-fault report, in the scar section and at Example D.4.
- Install guide wording follows facts-02 S2: it never mentions a virtual environment, and its container recipe uses `--break-system-packages`. The doctor hint: shown after a not-ready result (in the captured run, after a broken optional tool), naming Example D.3's required packages and leaving out epubcheck.
- Copyedit blocks: "proves" is now "tests", and "shipped" (outside the quote) is now "came with". Terms: *the toolchain image* is defined at first use, and so are *floating tag*, *immutable tag* (with `v3.0.2`, per S1), the *reusable workflow*, and *the desk* (with a pointer to Chapter 15). Also "role" for "job", "number" for "figure", the Print edition glossed, the reusable workflow (not the release contract) pins the image, named actors, and the condition-first sentences. The bold-label list in "What is untested" is now Table D.2.
- Added from the Missing list: the `BROKEN` state, the three discovery commands, the editable install, and the clause that CI installs press from the composite action's own checkout.
- Also from the fact check: "In this appendix, Linux means...", the time hedge on the Python range, "comments wrapped to fit the page" for Example D.3, and the font-scan sentence cut back to the scar's words.
- Not applied: copy item 26 ("Ubuntu manages the image's Python"). S2 calls it Debian-managed, so I wrote "the image's Python belongs to the operating system", which is true under both names. The typesetter's two caption-at-page-foot breaks and the 16.x heading numbers: the headings now carry `{-}` (14 marked). Recheck the page breaks after the final build.
- Tools run: unnumber-appendix-heads (14), tag-fences (0), prefix-footnotes (unchanged).

`press check`: the source checks pass now fails on three orphan plates belonging to Chapters 12 and 14 (*12-01-cover-wrap-anatomy.png*, *14-02-resolving-v3.png*, *14-03-release-state-machine.png*), so its later passes did not run. I ran `press style` (passed, 23 files) and the jargon lint over C and D with the book's allow list (exit 0). ste_check residuals for D: the 29-word opener (under the ceiling), the semicolon inside the guide's quoted fonts sentence, "is untested" in the heading, and the index comment.
