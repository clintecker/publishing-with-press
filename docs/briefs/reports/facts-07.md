# Fact check: Chapter 7, Building the editions

I checked `book/chapters/07-building-the-editions.md` against `docs/briefs/facts/facts-07.md`: sections 5.1 to 5.5 and 3.5, the Shared context (1.4, 19, 20), and the managing editor's supplement (S1 the full `press all` capture, S2 a defaults template and its rendered copy, S3 `press wordcount`). The writer did not have the supplement. Where the chapter uses placeholders, the fix below gives the real text. Line numbers refer to the chapter. U, C, D, and M refer to the items in lists 1 to 4, so C2 is item 2 of Contradicted.

**Slug.** The real captures use the press example's slug, `alice-in-wonderland`. The book's sample uses `alice` (brief-07, and the facts-01 note "replace `alice-in-wonderland` with `alice` and keep everything else"). So `dist/alice.*` throughout the chapter is correct house practice, not an error. Every capture quoted below has that substitution made and nothing else changed.

**Captured output and verbatim tables.**

- Table 7.4 and Table 7.5 match the fact file's REFERENCE.md tables cell for cell. I compared them mechanically after normalising the column padding.
- These quoted messages match: `pandoc is required`, `defaults reference a missing file`, `no assets/cover.jpg; interior verified, wrap not built`, and `(commerce gate is advisory here; a release build (PRESS_RELEASE=1) enforces it)`. The last one is real, but see C2 for when it appears.
- Every quotation is accurate: "the tool retail channels run", "the generated appendices are cleaned first so stale copies cannot survive", and "Keep that fallback working."
- `SOURCE_DATE_EPOCH` `1784160000` is 2026-07-16 00:00 UTC, so the footnote's date is right.
- The two captures that fail this check are the EPUB echo (D1) and the word count (U10).

## 1. Unsupported

1. **`sh -x`.** Line 67: "This is the same convention that `sh -x` uses for a traced shell script." I searched for sh, trace, and shell. The file says only "It runs from the book root and prints `+ <command>`." Fix: cut the sentence.
2. **How latexmk works.** Line 162: "A book has several lists that depend on an earlier pass: the table of contents, the List of Figures, the List of Plates, and the cross-references. ... latexmk watches the auxiliary files and runs again until they stop changing." I searched for latexmk, pass, aux, and converge. The file says only "Plain lualatex under pandoc does not run enough passes, so the build goes through latexmk" (war story 4). It also says that `figure-numbering.lua` "resolves `@id` cross-references", so cross-references may not depend on a TeX pass at all. Fix: cut "and the cross-references" and the sentence about auxiliary files. Keep: "Plain LuaLaTeX under pandoc does not run enough passes for the lists to converge, so the press builds through latexmk."
3. **The font scan.** Line 170: "LuaLaTeX scans every font on the system and caches what it finds ... During that time the build prints nothing new and uses a full CPU ... Later runs read the cache and start without the wait." I searched for font, cache, CPU, and scan. The file says only "The first LuaLaTeX run spends several minutes on a font scan" (war story 10) and "The first LuaLaTeX run takes several minutes for the font scan" (5.4). Fix: "The first LuaLaTeX run on a new machine spends several minutes on a font scan, and it looks like a hang. It is not one." Cut the claims about caching, CPU use, and silence.
4. **"The first book built its PDF the simple way."** Line 167, the sidebar. I searched for "first book" and found nothing about this scar's origin. The file says: "Plain lualatex under pandoc does not run enough passes, so the build goes through latexmk." Fix: open the sidebar with "Plain LuaLaTeX under pandoc does not run enough passes for a book."
5. **The `SOURCE_DATE_EPOCH` rationale.** Line 111, the footnote: "Tools that honor `SOURCE_DATE_EPOCH` use it in place of the current time. A fixed value therefore keeps a changing date out of the build." The file gives only the value, the date, and "unless the caller set it". Fix: keep "The value falls on 16 July 2026." and cut the rest, or have the editor accept it as general knowledge.
6. **"a book repository does not carry its own copy."** Line 79. I searched for defaults, copy, and override. The nearest thing the file says is "Book repositories contain book facts only" (1.4). Fix: cut the sentence, or write "The defaults files ship with the press."
7. **The single-file HTML and the reader stylesheet.** Line 200: "Both use the house reader stylesheet". The file says that `press site` adds "reader CSS" (5.1) and that `dist/site/` holds `reader.css` (3.5). It says nothing about the CSS in `html.yaml`. Fix: "The reader site uses the house reader stylesheet, which Chapter 9 describes."
8. **"the press writes every file in it again on demand."** Line 393. Section 3.5 lists `build/` entries that no build target writes: `build/editorial-report.md` and `build/editorial-rejections.md` (workflows), `build/cover/cover.png` and `build/illustrations/<name>.png` (art), and `build/dev-render/`. Fix: "Nothing in *build/* is a source file, and `press clean` deletes all of it."
9. **"`press all` ... stops at the first failure."** Line 323. The file says this only of the check step: "stopping at the first failure" (5.3, step 1). The commerce gate step is "advisory" on an ordinary run. Figure 7.4's directive draws a fail arc from every state, including the commerce gate, and that arc has the same problem. Fix: "`press all` runs ... in six steps. The check step stops at the first pass that fails." In the directive, label the commerce gate's fail arc "under PRESS_RELEASE".
10. **The `press wordcount` example, lines 405 to 413.** It is not in facts-07. The writer took it from facts-C (report-07 says so). It also leaves the Alice sample, which the rest of the chapter follows. Facts-C supports the stripping claim on line 413 ("It strips fenced and inline code ... It does not strip HTML comments"), but facts-07 does not. Fix: replace the example with S3, verbatim:

    ```
    $ press wordcount
      2160  book/chapters/01-down-the-rabbit-hole.md
      2136  book/chapters/02-the-pool-of-tears.md
      1721  book/chapters/03-a-caucus-race-and-a-long-tale.md
       228  book/appendices/z-about-this-edition.md
      6245  TOTAL
    ```

    Change the lead-in to "On the Alice example, it prints one line per file". Line 413 can stay only if the managing editor confirms facts-C's description for this chapter. Otherwise cut it.
11. **"Without that file, the press names no cover image and still builds the EPUB."** Line 194. The file says only "`epub-cover-image` is `assets/cover.jpg` when present." Fix: cut the sentence, or soften it to "The press names the cover only when that file is present."
12. **"A caption once came out as 'Fig-ure'."** Line 137. The file says the risk, not that it happened: "A narrow wrap could hyphenate 'Figure'" (war story 22), and "so a narrow column can never hyphenate it into 'Fig-ure'" (5.2). Fix: "Without the box, a narrow column could hyphenate the word into 'Fig-ure'."

## 2. Contradicted

1. **Plus-sign lines are not always commands.** Line 359: "A line that starts with a plus sign and a space is a command that the press is about to run." Line 67 implies the same. S1 contains two `+ ` lines that are status reports:

    ```
    + stitched 4 files -> dist/alice.md
    + assembled pages site -> dist/pages
    ```

    Section 5.4 calls these lines "tool invocations" only for the desk's parser. Fix: "A line that starts with a plus sign and a space marks a step the press runs. For pandoc it is the full command line, and for the steps that do not call pandoc it is a short report, such as `+ stitched 4 files -> dist/alice.md`."
2. **The commerce gate on the Alice example.** Lines 339 to 343 say that on an ordinary run on `hatter` the gate is advisory, "and it says so in a line of its own", and then show the advisory line. The Alice example does not enable ordering, so S1 ends the gate step with this line instead:

    ```
    commerce release gate: print ordering is not enabled; no commerce release gate
    ```

    The bug list ties the gate to "ordering-enabled books only" (20.B.13). Fix: show the S1 line for the Alice example. Then add: "A book that enables print ordering gets the gate. On an ordinary run it is advisory and prints `(commerce gate is advisory here; a release build (PRESS_RELEASE=1) enforces it)`; under `PRESS_RELEASE` it enforces." Figure 7.4's caption under the commerce gate should then read "advisory unless PRESS_RELEASE; absent without ordering".
3. **"Mr." and the title tie.** Line 121, Table 7.3: `typographic-spacing.lua` puts in non-breaking spaces "so that 'Mr.' never ends a line apart from its name." War story 21: "A title-tie test passed with no filter, because pandoc ties `Mr.` itself". The chapter says the same thing itself on line 143. Fix: "This filter puts non-breaking spaces after titles, reference forms, and initials (§4.7)." Cut the "Mr." clause, or give an example that is not `Mr.`, such as an initial.
4. **Where the generated files go in the input order.** Line 65: "the chapter files, then the appendix files, then the generated files such as the subject index." The file gives the command as `<chapters...> <appendices + generated...>`, which is one group. 20.A.7 says the index "takes the *first* free letter from `a`" and so "usually sorts *before* authored appendices." Note also that S1's pandoc lines for Alice contain no generated file at all: the inputs are the three chapters and `book/appendices/z-about-this-edition.md`. Fix: "The input files follow in book order: the chapter files, then the appendices, with the generated appendices such as the subject index sorted among them by letter."
5. **`press all` in Table 7.1.** Line 40 gives the result as "everything above except print and coverwrap". The rows above include `press render` (*build/rendered-book/*), and `press all` does not render. The sequence in 5.3 and S1 contains no pdftoppm step. Fix: "every published artifact and *dist/pages/*". The fact table's own wording is "everything except print/coverwrap".
6. **"the only edition target that does not call pandoc."** Line 227. `press source` does not call pandoc either: its mechanism is "`package_source` (git-tracked files only)" (5.1), and 3.5 calls its result the "Source edition". The chapter itself says so on line 56. Fix: "`press markdown` is one of two edition targets that do not call pandoc, and the source zip is the other."
7. **"Add and commit."** Line 238, the tip, and line 235 ("so is anything that *.gitignore* excludes"). 20.A.26 says the add/commit requirement "is inferred from the policy's 'tracked files only' and should be verified before writers claim it." The file also never mentions *.gitignore*. S1 shows the source step's real report, `archived 12 files; excluded dirs ['.git', '__pycache__', 'build', 'dist']`. Fix: keep "The zip holds the files that Git tracks in the book repository, and only those." Soften the tip to "A chapter file that Git does not track is left out of the source zip, so add new files to Git before you build it." Cut the *.gitignore* clause, or replace it with the excluded-dirs line from S1.
8. **"It never built the print interior or the cover wrap."** Line 350, the warning. 20.B.13: "`press all` builds neither `print` nor `coverwrap`, but the commerce release gate (ordering-enabled books only) does." The commerce gate is step 6 of `press all`. Fix: "An ordinary `press all` never builds the print interior or the cover wrap." Keep the rest of the warning.

## 3. Drifted

1. **The EPUB echo, lines 69 to 73.** It is presented as output, but it uses `<root>` and elides the whole tail. S1 has the real line, captured under `press all` rather than `press epub`:

    ```
    + pandoc --defaults=~/alice/build/defaults/epub.yaml --metadata rights=The text and illustrations are in the public domain. Published by The Press (gallery example), Oxford. --epub-metadata=~/alice/build/epub-metadata.xml book/chapters/01-down-the-rabbit-hole.md book/chapters/02-the-pool-of-tears.md book/chapters/03-a-caucus-race-and-a-long-tale.md book/appendices/z-about-this-edition.md --output dist/alice.epub
    ```

    Fix: use this line, with elision by `...` if it is too long for the measure, for example after the first chapter file. Change the lead-in to "Under `press all`, the EPUB's line reads". The file gives no capture of a bare `press epub`, so do not claim these are "the first lines of output" of that command. The capture also shows the rights line and the XML file going into the command, which supports the next section.
2. **`pandoc took N.Ns`, lines 75 and 359.** The form is right (5.1 and 5.4). The real line is indented two spaces, and on the Alice example only the PDF reached one second: `  pandoc took 26.7s` (S1). Fix: give the real line as the example, "a line such as `pandoc took 26.7s`, indented two spaces". Line 359 says "the registry ends with a summary line". The file says "the registry prints `press timings: …`". Fix "ends with" to "prints". S1 has no `press timings:` line, because only one step was timed.
3. **Figure 7.3's directive, line 92.** The three paths are schematic, and `@book/assets/web/extra.css?optional` does not occur in any defaults file the supplement shows. S2 gives the real lines. Fix: replace the directive's lines as follows.
    - (a): head it with "src/press/data/defaults/pdf.yaml". Line 1 is `metadata-file: "@book/config/metadata.yaml"`. Line 2 is `- "@press/tex/book-header.tex"`. Line 3 is `- "@book/tex/title-page.tex?optional"`, with the callout "file absent".
    - (b): head it with "build/defaults/pdf.yaml". Line 1 is `metadata-file: ~/alice/config/metadata.yaml`. Line 2 is `- .../press/data/tex/book-header.tex`. Line 3 is struck through, with the callout "dropped".

    The Alice book supplies no `tex/title-page.tex`, and S2's rendered copy omits it, so this is the real dropped entry. Line 2 also shows that `@press/` resolves to the package's `data/` directory. Drop the sentence saying the angle brackets stand for absolute directories, or keep it for `.../press` and `~/alice`.
4. **The Lua coverage warning, line 146.** "The floor ... must come from the CI measurement." The file says: "Contributors must never `update` that floor from a macOS measurement." Fix: "Never update the Lua coverage floor in *.celebrimbor/baselines/lua-coverage.yaml* from a measurement taken on macOS."
5. **Who owns what, line 22.** "The press decides the build order, the file names, and the editions." QUICKSTART, as quoted in 1.4: "The press owns: build order, verification pipeline, file names, and formats." Fix: "The press decides the build order, the verification pipeline, the file names, and the formats." It is also worth saying that the author owns "title, author, words, and the visual identity".
6. **"in the order that the press documentation gives them,"** line 24. The fact file's target table cites the CLI (`src/press/__main__.py`), not a document. Fix: "in the order the press lists them".
7. **"Eight artifacts need nothing first,"** line 266. Nine rows of Table 7.4 have `-` in the prerequisites column, because `print` has none either. The sentence then mentions print separately, which makes the count read as an error. Fix: "Eight of the published artifacts need nothing first".
8. **Sources written unconditionally,** line 317, step 3: "It writes *dist/alice-sources.md* from the authorities ledger." The Alice example has no ledger. S1 reports "8 downloads present and linked" and archives only `alice-site.zip` and `alice-source.zip`, with no sources companion. The tree in 3.5 marks the file "(only with config/authorities.yaml)". Fix: "If the book has *config/authorities.yaml*, it writes *dist/alice-sources.md* from the ledger."
9. **"a set of small TeX files,"** line 151: "Before pandoc runs, the press writes a set of small TeX files into *build/*. Each one carries a fact from the book's configuration into the house TeX header." Step 2 sets a pandoc variable, and step 6 writes images, so neither is a TeX file. Fix: "Before pandoc runs, the press does six things, in a fixed order:" and drop "Each one carries ...". Alternatively, keep that sentence only for steps 1, 3, 4, and 5.
10. **"Every verify target rebuilds what it verifies first,"** line 291. This is true for the artifacts each target verifies. But `press verify-formats` "reads an existing `dist/<slug>.pdf` into the cross-edition agreement check" without rebuilding it (5.3; 20.B.11). The writer rightly avoided documenting that as a feature. The absolute sentence, though, invites a reader to trust a stale PDF there. Fix: "Every verify target rebuilds the artifacts it verifies before it verifies them." This narrows the claim without describing the bug.

## 4. Missing

1. **No real `press all` capture.** "What press all does, in order" describes the six steps but never shows them. S1 is the whole run on the Alice example. With the slug changed and nothing else changed, it reads:

    ```
    $ press all
    Source checks passed: 4 ordered Markdown files
      note: em-dash.md also drew: - .../known-bad/em-dash.md:4: glyph U+2014 is outside the print-font set
      note: en-dash.md also drew: - .../known-bad/en-dash.md:4: glyph U+2013 is outside the print-font set
    Checker self-test passed: 19 known-bad fixtures each tripped their declared rule, known-good fixture accepted, 2 extra diagnostics noted
    Editorial checks passed: 4 Markdown files
    Jargon check passed: no rewrite-status terms (full audit in build/jargon-report.txt)
      ¶ check      ✓ style, source, jargon
    + pandoc --defaults=~/alice/build/defaults/pdf.yaml book/chapters/01-down-the-rabbit-hole.md book/chapters/02-the-pool-of-tears.md book/chapters/03-a-caucus-race-and-a-long-tale.md book/appendices/z-about-this-edition.md --output dist/alice.pdf
      pandoc took 26.7s
    + pandoc --defaults=~/alice/build/defaults/epub.yaml --metadata rights=The text and illustrations are in the public domain. Published by The Press (gallery example), Oxford. --epub-metadata=~/alice/build/epub-metadata.xml book/chapters/01-down-the-rabbit-hole.md book/chapters/02-the-pool-of-tears.md book/chapters/03-a-caucus-race-and-a-long-tale.md book/appendices/z-about-this-edition.md --output dist/alice.epub
    + pandoc --defaults=~/alice/build/defaults/html.yaml book/chapters/01-down-the-rabbit-hole.md book/chapters/02-the-pool-of-tears.md book/chapters/03-a-caucus-race-and-a-long-tale.md book/appendices/z-about-this-edition.md --output dist/alice.html
    + stitched 4 files -> dist/alice.md
    + pandoc --defaults=~/alice/build/defaults/portable.yaml --to=plain --columns=80 book/chapters/01-down-the-rabbit-hole.md book/chapters/02-the-pool-of-tears.md book/chapters/03-a-caucus-race-and-a-long-tale.md book/appendices/z-about-this-edition.md --output dist/alice.txt
    + pandoc --defaults=~/alice/build/defaults/portable.yaml --to=docx book/chapters/01-down-the-rabbit-hole.md book/chapters/02-the-pool-of-tears.md book/chapters/03-a-caucus-race-and-a-long-tale.md book/appendices/z-about-this-edition.md --output dist/alice.docx
    + pandoc --defaults=~/alice/build/defaults/chunked.yaml --to=chunkedhtml book/chapters/01-down-the-rabbit-hole.md book/chapters/02-the-pool-of-tears.md book/chapters/03-a-caucus-race-and-a-long-tale.md book/appendices/z-about-this-edition.md --output dist/site
    ~/alice/dist/alice-source.zip
    archived 12 files; excluded dirs ['.git', '__pycache__', 'build', 'dist']
    + assembled pages site -> dist/pages
      ¶ typeset    ✓ PDF · EPUB · web · text · DOCX
    Verified dist/pages: every local reference resolves (fragments and stylesheet assets included), 8 downloads present and linked, sentinels on the public reading surface
    Verified alice.pdf: 23 pages, 6 x 9 trim, embedded fonts, 2 sentinel(s) plus the title as witnesses, every rendered page contains ink, no edge clipping, cover on page 1
    WARNING: epubcheck not installed; EPUB validated structurally only. The press toolchain runs the full check in CI. (brew install epubcheck)
    Verified alice.html, alice.epub, alice.md, alice.txt, alice.docx, site/ (2 sentinel(s), the title, and the manuscript line 'and here alice began to get rather sleep...' as witnesses); 7 editions agree on all 4 chapter witnesses
    Verified archives: alice-site.zip, alice-source.zip
      ¶ verify     ✓ 7 editions match source
    commerce release gate: print ordering is not enabled; no commerce release gate
    
      press. your book is ready → dist/
    ```

    It belongs in that section as an Example, with elision by `...` if needed. It shows the four check passes in order, and the build order of step 2: pdf, epub, html, markdown, txt, docx, site. It also shows the source zip, the pages, the four verifiers in the stated order, and the gate. The `WARNING: epubcheck not installed` line is Chapter 8's matter, and you can elide it with a forward reference.
2. **The order of the editions in step 2,** line 331: "The press builds each edition target in turn." The writer listed this as unknown. From S1, the order is PDF, EPUB, HTML, Markdown, text, Word, then the chunked site.
3. **The phase lines and the closing line.** Line 361 says the desk reads "a pilcrow followed by a phase name", but the chapter never shows one. S1 shows `  ¶ check      ✓ style, source, jargon`, `  ¶ typeset    ✓ PDF · EPUB · web · text · DOCX`, and `  ¶ verify     ✓ 7 editions match source`. It also shows the run's last line, `press. your book is ready → dist/`. Both are worth quoting in "Reading the log".
4. **What rendering adds to the defaults.** S2 shows that the rendered copy carries more than resolved paths. It gains `lof: true` under `variables:`, which is step 2 of the PDF pre-steps made visible. It also gains a `metadata:` block holding the four values from line 109 (`chapter-opening-style: drop-cap`, `chapter-opening-lines: 3`, `chapter-opening-smallcaps: 'true'`, `scene-break-ornament: fairy-dust`). The rendered copy is also written in normalised YAML (unquoted paths, `''` for the empty `thanks`). Lines 95 and 109 would be stronger for saying so: "Open *build/defaults/pdf.yaml* and you will find these four values in its `metadata:` block."
5. **The EPUB metadata flag.** Line 186 calls *build/epub-metadata.xml* the third piece but does not say how pandoc gets it. S1 shows the option, `--epub-metadata=~/alice/build/epub-metadata.xml`.
6. **The source zip's report.** The source step prints the zip's path and then `archived 12 files; excluded dirs ['.git', '__pycache__', 'build', 'dist']` (S1). That would serve "The source edition" better than the *.gitignore* clause (see C7).
7. **The policy pages in Example 7.2.** The 3.5 tree lists `support.html privacy.html refunds.html # only when ordering is enabled and policy URLs are omitted` under `pages/`. The example omits them, and the prose after it does not mention them. This is optional, because the Alice example does not enable ordering.
8. **The one real timing.** "The press documents no other timing" (line 359) is right for the documentation (20.C). S1 now gives one measured data point, `pandoc took 26.7s` for the Alice PDF. If the chapter uses it, frame it as one run on one machine, not as a guide.

## Counts

- Unsupported: 12
- Contradicted: 8
- Drifted: 10
- Missing: 8

**Worst finding:** C2. The chapter shows the advisory commerce-gate line as what an ordinary Alice run prints. The real run prints `commerce release gate: print ordering is not enabled; no commerce release gate`, because the gate exists only for ordering-enabled books. C1 is close behind: the chapter tells readers that every `+ ` line is a command they can copy and rerun, and two of them in a real `press all` are not commands.
