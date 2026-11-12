# Appendix C: Messages and refusals {.unnumbered}

When press stops, it prints a message and exits with a nonzero status. This appendix lists the messages by the command that prints them, so you can look one up before you read the code. Each entry quotes the message as press prints it, then gives its cause and its remedy. Words in angle brackets, such as `<path>`, stand for a value press fills in. A letter such as `N` or `M` stands for a number, and `[...]` stands for a list of page numbers or names. Elsewhere in a message, `...` stands for text that press prints there and this appendix leaves out, such as the diagnostics after a colon.

A long message appears under a short entry that gives its first words. The message itself follows in a block, broken at a space to fit the page. Press prints it as one line, and an indented line in the block continues the line above it.

When a check or a verifier fails, press exits with status 1. When an external tool such as `pandoc` or `latexmk` fails, press exits with that tool's status. A status of 43 from the tool is therefore a status of 43 from press. Appendix A, *Command reference*, lists every exit status.

To find a message, search this appendix for a fixed word in it, such as "sentinel" or "trim". The values on your terminal will differ from the values in this appendix.

This appendix holds the checker's and the verifiers' messages. Table C.1 points to the chapters that quote the messages of the generators, intake, `press config`, the retail flag, and the commerce gate.

| Messages from | Quoted in |
|------------------------------------------|----------------------------------|
| `gen_index`, the subject index | Chapter 10 |
| `gen_authorities`, the table of authorities | Chapter 10 |
| `front matter needs`, the generated front matter | Chapter 10 |
| `press art accept`, intake | Chapter 11 |
| `press config` | Chapter 3 |
| `registrations.retail`, the retail flag | Chapter 13 |
| The commerce gate | Chapter 7 and Chapter 12 |

Table: Table C.1. Messages quoted outside this appendix

## press check {-}

The checker runs four passes in order: the source checks, the checker self-test, the style audit, and the jargon lint. It stops at the first pass that fails, so the passes after it do not read your manuscript on that run. Fix the fault behind every message before you run the check again. Chapter 6, *Checking the manuscript*, describes each pass.

### Source checks {-}

The first pass reads the chapter files and *config/metadata.yaml*. It passes with `Source checks passed: N ordered Markdown files`. On a failure, press prints each message as a bulleted line under the pass's failure header.

`missing source file: <path>`
:   **Cause.** A chapter file that press expects is not on disk.

    **Remedy.** Restore the file from Git, or write it.

`suspiciously short source: <path>`
:   **Cause.** The body of the chapter file runs under 80 characters.

    **Remedy.** Write the chapter, or remove the file until you do.

`no level-1 heading: <path>`
:   **Cause.** The chapter file has no level-1 heading, so the chapter has no title.

    **Remedy.** Make the first line of the file the chapter title, as in `# Writing the manuscript`.

`unfinished marker '<phrase>': <path>`
:   **Cause.** The file still holds one of three unfinished markers. Two are placeholder abbreviations followed by the verb "write", and the third is the Latin dummy copy of the typesetter. Press quotes the marker it found. The check reads fenced code too.

    **Remedy.** Replace the marker with the text it held a place for.

`metadata missing <field>:`
:   **Cause.** One of the four keys the checker requires is absent from *config/metadata.yaml*: `title`, `author`, `description`, or `slug`.

    **Remedy.** Set it, for example `press config set description "One paragraph."`, then run the check again.

`sentinel not found in the manuscript: <sentinel>`
:   **Cause.** A phrase under `verify-sentinels` no longer appears in any chapter file. A revision usually removed it.

    **Remedy.** Restore the phrase, or choose another phrase from the middle of a chapter. The setting is a list, so set it with `press config set verify-sentinels '[...]' --json`. Avoid the first words of a chapter, because a chapter opening splits the first word in the PDF.

`plate never referenced by the manuscript: assets/woodcuts/<name>`
:   **Cause.** A file under *assets/woodcuts/* has no image line in any chapter file.

    **Remedy.** Reference the plate from a chapter, or delete the file. When you remove a plate, delete its file and its image line in the same commit.

`fig-alt`
:   **Cause.** A figure carries `decorative=true` together with a `fig-alt` attribute, and the diagnostic names `fig-alt`. Press gives a decoration an empty alt text by definition.

    **Remedy.** Delete the `fig-alt`. If the image carries information, delete `decorative=true` instead and keep the alt text.

The first pass also refuses faults in registrations and commerce, figure placement, the shapes of the other config files, and print feasibility. Chapter 5, *Figures, plates, and illustrations*, Chapter 12, *The print pack*, and Chapter 13, *Registrations*, describe those rules.

### The checker self-test {-}

The second pass runs the style audit and the jargon lint over the 19 packaged known-bad fixtures and the book's own fixtures in *tests/known-bad/*. It passes with a line that begins `Checker self-test passed:`. Each message names the fixture.

`<fixture>: expected rule`

:   Press prints:

    ```text
    <fixture>: expected rule '<rule>' did not fire
      (<up to 3 others or "no diagnostics at all">)
    ```

    **Cause.** The fixture declares a rule in an `<!-- expect: ... -->` comment, and no diagnostic contains that rule's text. The parentheses show up to three diagnostics that did fire.

    **Remedy.** For a book fixture, compare the expected text with the label of your banned pattern in *config/house-rules.yaml*. The match ignores case and accepts a substring. If the label is right, the pattern no longer matches the fixture. Fix the pattern.

`<fixture>: no checker rejected`

:   Press prints:

    ```text
    <fixture>: no checker rejected a known-bad fixture
      (and it declares no expected rule)
    ```

    **Cause.** A fixture without an expect comment draws no diagnostic at all.

    **Remedy.** Make the fixture break the rule you wrote it for, or add a banned pattern for that rule to *config/house-rules.yaml*.

`<fixture>: a checker rejected the known-good fixture: ...`
:   **Cause.** The packaged known-good fixture draws a diagnostic.[^c-ellipsis] It must draw none, so a rule that rejects it is too broad.

    **Remedy.** Read the diagnostics after the colon, and narrow the rule they name.

`note: <fixture> also drew: ...`
:   **Cause.** A fixture draws a diagnostic beside the one it declares. On a fresh scaffold the dash fixtures also trip the glyph law, and the pass reports "2 extra diagnostics noted".

    **Remedy.** None. A note does not fail the check.

### The style audit {-}

The third pass reads every audited file: the manuscript and the files in any audit directory. It passes with `Editorial checks passed: N Markdown files`. In an audit directory, heading and paragraph faults print under `Editorial warnings:` and do not fail the check. The universal battery (the dash, phrase, parallelism, and whitespace rules) applies there as everywhere. Each diagnostic follows the filename and the line number.

`contains em dash`
:   **Cause.** The line holds the character U+2014.

    **Remedy.** Rewrite with a comma, a colon, a period, or parentheses. Two hyphens pass the audit, but pandoc prints them as a dash. Rewrite them as well.

`contains en dash`
:   **Cause.** The line holds the character U+2013, often in a range of numbers.

    **Remedy.** Write the range with "to", or rewrite as for an em dash.

`generic conclusion`
:   **Cause.** The line holds the stock two-word phrase that the fixture *in-conclusion.md* holds.

    **Remedy.** Delete the phrase and state the conclusion.

`throat-clearing phrase`
:   **Cause.** The line announces that a point is important or worth noting before it makes the point.

    **Remedy.** Delete the announcement and keep the point.

`fake-revelation phrase`
:   **Cause.** The line stages a revelation with one of the two phrases that the fixtures *at-its-core.md* and *real-question.md* hold.

    **Remedy.** State the claim plainly.

`chatbot signposting`
:   **Cause.** The line invites the reader to dive in, explore, or the like, or promises to proceed without further delay.

    **Remedy.** Delete the invitation and begin with the content.

`inflated significance`
:   **Cause.** The line claims that a thing proves its own importance, in the stock phrase that Chapter 6 quotes.

    **Remedy.** Say what the thing does.

`inflated AI phrase`
:   **Cause.** The line describes something as a bright woven fabric, in the stock two-word phrase that Chapter 6 quotes.

    **Remedy.** Name the actual things.

`formulaic negative parallelism`
:   **Cause.** The line holds "not only" and its usual partner within 120 characters, as the fixture *negative-parallelism.md* does.

    **Remedy.** Make the two claims in two sentences.

`trailing whitespace`
:   **Cause.** A line ends in a space or a tab. The rule reads fenced code too.

    **Remedy.** Delete the whitespace, and set your editor to strip it on save.

`glyph U+2014 is outside the print-font set`
:   **Cause.** Book prose holds a character outside the set the glyph law allows: tab, line feed, carriage return, U+0020 to U+007E, and U+00C0 to U+017F. Press names the code point. The glyph law skips fenced code.

    **Remedy.** Replace the character with its ASCII spelling, such as three periods for an ellipsis.

`paragraph N has W words (the law is under 190; split it)`
:   **Cause.** A paragraph of book prose reaches 190 words. In an audit directory this is a warning.

    **Remedy.** Split the paragraph at a change of topic, or cut it.

`manual number in heading`
:   **Cause.** A heading begins with a number you typed, such as `# 3. A numbered heading`.

    **Remedy.** Delete the number. Press numbers chapters and sections itself.

`title-case heading: <text>`
:   **Cause.** A heading capitalizes its words in title case.

    **Remedy.** Rewrite it in sentence case.

The curly-quote rule refuses a curly quotation mark in book prose. Its diagnostic contains the word `curly`, which the packaged fixture *curly-quotes.md* declares. Type straight quotes, and pandoc curls them in the editions.

When a line matches one of the book's banned patterns, press prints the label from *config/house-rules.yaml* in place of a packaged diagnostic, in the form `<file>:<line>: <label>`. The label is the book's own message, and its remedy is the rule the book wrote.

### The jargon lint {-}

The fourth pass runs the jargon lint over the chapter files and writes its full report to *build/jargon-report.txt*. It passes with `Jargon check passed: no rewrite-status terms (full audit in build/jargon-report.txt)`. Press prints each finding in three lines: the location, status, term, and category, then the line of context, then a question.

`path:line:col: rewrite: 'seam' [structural metaphor]`
:   **Cause.** A chapter holds a term the watchlist marks `rewrite`. The lint fails at `rewrite` by default.

    **Remedy.** Answer the question on the `Ask:` line and rewrite the sentence with the answer. If the book uses the term literally, add it to `jargon-allow` in *config/house-rules.yaml*.

The jargon lint exits with status 2 when the watchlist itself is malformed.

## The command line {-}

These messages come from press itself, before or at the start of a target, not from a checker. A bare `press` with no command prints its usage and exits with status 2.

`unknown target: X`
:   **Cause.** The command names no target in the catalog. Press exits with status 2 and prints a suggestion.

    **Remedy.** Run the suggested name, or run `press --help` for the catalog.

`pandoc is required`
:   **Cause.** A build target found no `pandoc` on the search path.

    **Remedy.** Install pandoc as Appendix D describes, then run `press doctor`.

`defaults reference a missing file`
:   **Cause.** Before each pandoc run, press renders a defaults file and checks that every file it names exists. A file that is absent and not marked optional stops the build.

    **Remedy.** Find the file the defaults name, in the book repository or the press package, and restore it.

## press doctor {-}

The doctor checks the toolchain on the machine and prints one line per tool. On a ready machine its last line reads `this machine can make books`, and it exits with status 0. Otherwise it exits with status 1.

`not ready:`

:   Press prints:

    ```text
    not ready: claude (macOS: brew install pandoc
      mactex-no-gui poppler; Debian/Ubuntu: see the
      Dockerfile's package list)
    ```

    **Cause.** At least one tool is `MISSING` (a required tool is absent) or `BROKEN`. The line names the tools, here `claude`. A broken optional tool also keeps the machine from being ready.

    **Remedy.** Install or repair each tool the line names. In the captured run, the line ends with install hints in parentheses.

`[ BROKEN]`

:   Press prints:

    ```text
      [ BROKEN] claude     present but cannot execute; the
        operator: press improve, research, aesthetic briefs
    ```

    **Cause.** The tool is on the search path, but it fails both `--version` and `-v` within 15 seconds. The doctor marks it `BROKEN` and puts "present but cannot execute" before the tool's purpose.

    **Remedy.** Run the tool by hand to see its own error, and reinstall it.

`X.Y is outside the tested range`

:   Press prints:

    ```text
    X.Y is outside the tested range 3.10 to 3.14
      (see docs/COMPATIBILITY.md)
    ```

    **Cause.** The Python that runs press is older or newer than the tested releases.

    **Remedy.** Install press under a Python from 3.10 to 3.14.

## The PDF verifier {-}

`press verify` rebuilds the Print edition (the PDF) and runs the PDF verifier over it. `press verify-print` runs the same verifier over the print interior with the print profile. A pass prints a line that begins `Verified <pdf>:` and lists what it proved.

`this is a release build`

:   Press prints:

    ```text
    this is a release build (PRESS_RELEASE=1) and its
      witnesses are vacuous:
    verify-sentinels has N entries; a release needs at
      least 2 distinctive prose fragments
    verify-min-pages is N; a release needs at least 24
    ```

    **Cause.** A release build demands its release witnesses: at least two sentinels and a page floor of at least 24. The lines after the first name each fault.

    **Remedy.** Set two sentinels and a floor of 24 or more with `press config set` before you push the tag.

`PDF not found: <path>`
:   **Cause.** The verifier found no PDF at the path it names.

    **Remedy.** Run `press verify`, which builds the PDF before it inspects it.

`blank-page detector failed to reject a blank fixture`
:   **Cause.** The verifier tests its own blank-page detector before it trusts it. Here the detector called a blank test image inked.

    **Remedy.** Report it to the press. The book is not at fault. The fault lies in the press or its image library.

`blank-page detector rejected a marked fixture`
:   **Cause.** The detector called a marked test image blank.

    **Remedy.** As for the message before it.

`required verification tool missing: <tool>`
:   **Cause.** A poppler tool, such as `pdfinfo`, is absent.

    **Remedy.** Install poppler (Appendix D).

`could not parse pdfinfo output`
:   **Cause.** `pdfinfo` printed something the verifier cannot read.

    **Remedy.** Run `pdfinfo` on the PDF by hand. A damaged PDF or a broken poppler shows itself there.

`unexpected trim size: W x H pt (expected 6 x 9 inches)`
:   **Cause.** The page size differs from the design profile's trim by more than one point.

    **Remedy.** Confirm that `print.profile` names the profile you mean, then rebuild with `press verify`.

`suspiciously short PDF: N pages (minimum M)`
:   **Cause.** The PDF has fewer pages than `verify-min-pages`.

    **Remedy.** If the book is that short, lower the floor. If not, look for lost chapters in the build log.

`missing text sentinel in PDF: <s>`
:   **Cause.** A sentinel is absent from the PDF's text. The match is case-sensitive, and straight and curly quotes count as equal.

    **Remedy.** Check that the phrase does not open a chapter, where a chapter opening splits it. Then check that no word in it breaks with a hyphen at the end of a line.

`missing title in PDF text: <title>`
:   **Cause.** The book's title does not appear anywhere in the PDF's text, even with case ignored.

    **Remedy.** Check the title page, especially a hand-authored *tex/title-page.tex*.

`pdffonts found no fonts`
:   **Cause.** The PDF carries no text fonts at all.

    **Remedy.** Rebuild, and read the LuaLaTeX log for a font failure.

`unembedded fonts: [...]`
:   **Cause.** The PDF uses the listed fonts and does not embed them.

    **Remedy.** Rebuild with `press verify`. If the list persists, check any TeX file the book supplies, such as *tex/title-page.tex*.

`<label> link <dest> resolves to no page`
:   **Cause.** A link in the List of Plates or the List of Figures points nowhere.

    **Remedy.** Run `press clean`, then rebuild with `press verify`.

`<label> links point at imageless pages: [n...]`
:   **Cause.** A list link points at a page without the image, often the caption's page.

    **Remedy.** As for the message before it. If it persists, report it with the page numbers.

`<label> present but contains no links`
:   **Cause.** The list prints without its links.

    **Remedy.** Report it to the press.

`pypdf unavailable; illustration-list destinations not verified`
:   **Cause.** Python cannot import the `pypdf` package, so press does not verify the list links.

    **Remedy.** Reinstall press, which declares `pypdf` as a dependency.

`rendered N pages, pdfinfo reports M`
:   **Cause.** The renderer produced a different number of page images than the PDF holds.

    **Remedy.** Rerun the verifier, then run `pdftoppm` on the PDF by hand.

`apparently blank rendered pages: [...]`
:   **Cause.** The listed pages carry no ink. The print profile forgives one isolated blank even page.

    **Remedy.** Open the PDF at the listed pages and find what left them empty.

`ink touches rendered page edge: [...]`
:   **Cause.** A pixel darker than the threshold lies within two pixels of the page edge.

    **Remedy.** Find the image or table that overruns the margins and reduce it.

`inconsistent rendered page dimensions: [...]`
:   **Cause.** Some pages differ in size from the rest.

    **Remedy.** Look for a hand-authored page that sets its own size.

`assets/cover.jpg exists but page 1`

:   Press prints:

    ```text
    assets/cover.jpg exists but page 1 of the reading PDF
      renders blank -- the cover plate was clipped off the
      page
    ```

    **Cause.** The book has a cover image, and the generated front matter lost it.

    **Remedy.** Report it to the press with the PDF. The press generates the front matter that places the cover, so the fault is in the press.

`... carries no cover image -- the generated front matter dropped it`
:   **Cause.** Page 1 has ink but no embedded image.

    **Remedy.** As for the message before it.

`note: pdfimages absent; cover-on-page-1 identity unverified`
:   **Cause.** `pdfimages`, part of poppler, is not installed, so press reports a note in place of the check. The doctor does not check for it.

    **Remedy.** Install the full poppler package.

## The formats verifier {-}

`press verify-formats` rebuilds the other editions and runs the formats verifier and the archives verifier over them. Each edition must carry the title, every sentinel, and the manuscript witness line.

`missing or suspicious artifact: <path>`
:   **Cause.** The HTML or EPUB file is missing or under 1000 bytes.

    **Remedy.** Rebuild and read the pandoc output above the message.

`<label> does not carry the book title: <title>`
:   **Cause.** The named edition lost the title.

    **Remedy.** Check the `title` key and any book stylesheet or template that replaces the house one.

`<label> lost the manuscript witness line: <first 60 chars>...`
:   **Cause.** The edition lacks the manuscript witness line, the longest markup-free line of 40 or more characters in the manuscript.

    **Remedy.** Find what breaks that line in the edition, often a filter or a stylesheet.

`no manuscript witness derivable; ... (write one honest plain sentence)`
:   **Cause.** No line in the manuscript runs 40 characters free of markup.

    **Remedy.** Write one such sentence, as the message says.

`HTML missing sentinel`
:   **Cause.** The Single-leaf edition (the self-contained HTML) lacks a sentinel.

    **Remedy.** As for the PDF sentinel message.

`HTML output has no html element`
:   **Cause.** The HTML file has no `<html>` element, so it is not an HTML document.

    **Remedy.** Rebuild, and check any book template.

`HTML carries N numbered-figure labels; the source declares M`
:   **Cause.** The edition numbers more or fewer figures than the manuscript declares.

    **Remedy.** Check each figure's image line and its attributes (Chapter 5, *Figures, plates, and illustrations*).

`EPUB has invalid mimetype`
:   **Cause.** The EPUB's container holds a wrong mimetype entry.

    **Remedy.** Rebuild with `press verify-formats`.

`EPUB missing container.xml`
:   **Cause.** The EPUB lacks the file that tells a reading system where the book's contents are.

    **Remedy.** As for the message before it.

`EPUB carries an empty dc:date`

:   Press prints:

    ```text
    EPUB carries an empty dc:date (retail validators reject
      it); the date field should contain a four-digit year
    ```

    **Cause.** The `date` key holds no four-digit year.

    **Remedy.** Put a year in `date`, as in `First edition, 2026`.

`epubcheck missing from the press toolchain image`

:   Press prints:

    ```text
    epubcheck missing from the press toolchain image; the
      retail-format gate cannot be skipped where releases
      are cut
    ```

    **Cause.** `PRESS_TOOLCHAIN` is set, and press finds no epubcheck.

    **Remedy.** The toolchain image is broken. Report it to the press.

`WARNING: epubcheck not installed`

:   Press prints:

    ```text
    WARNING: epubcheck not installed; EPUB validated
      structurally only. The press toolchain runs the full
      check in CI. (brew install epubcheck)
    ```

    **Cause.** epubcheck is absent on a machine without `PRESS_TOOLCHAIN`. This is a warning.

    **Remedy.** Install epubcheck, or let CI run it.

`epubcheck is present but cannot run`

:   Press prints:

    ```text
    epubcheck is present but cannot run (<exc>); the toolchain
      image is broken
    ```

    **Cause.** The command exists but fails to start. This is the binfmt scar that Appendix D describes.

    **Remedy.** Run the jar through `java -jar`.

`epubcheck failed on <path> (exit N):`
:   **Cause.** epubcheck found faults. Its own report follows. A pass prints `epubcheck passed: <name>`.

    **Remedy.** Fix each fault epubcheck names, then rebuild.

`docx embeds N images; expected at least M plates`
:   **Cause.** The Office edition (DOCX) lost plates.

    **Remedy.** Check each plate's image path.

`site missing index.html`
:   **Cause.** The Chapter edition (the reader site and its zip) has no index page. The messages `site missing reader.css` and `site has N chapter pages; expected at least M` read the same way.

    **Remedy.** Rebuild, and check any *assets/web/reader.css*.

`reader site is missing <chapter>: ...`
:   **Cause.** No page of the reader site carries the chapter witness line. The chapter lost its witness line. Its twin, `reader site duplicates <chapter>: ...`, means two pages share one.

    **Remedy.** Open the reader site at the chapter's page.

`site carries N plates; expected M`
:   **Cause.** The reader site lost or doubled plates.

    **Remedy.** Check the plate image paths.

`<label> disagrees with the manuscript`

:   Press prints:

    ```text
    <label> disagrees with the manuscript: it is missing
      content from N chapter(s) (...)...
    ```

    **Cause.** An edition lacks every eight-word window of a chapter witness line.

    **Remedy.** Open the named edition at that chapter.

`EPUB metadata is missing the registered ISBN <isbn>`
:   **Cause.** The book declares an ISBN, and the EPUB metadata does not carry it.

    **Remedy.** Check the ISBN under `registrations` (Chapter 13, *Registrations*).

## The pages and archives verifiers {-}

`press pages` builds the Pages bundle and crawls it. A pass prints `Verified dist/pages:`. The archives verifier runs under `press verify-formats`.

`dead fragment`
:   **Cause.** A link names an anchor that no page holds.

    **Remedy.** Fix the link.

`absolute reference`
:   **Cause.** A link or asset path begins at the root of a disk or a host.

    **Remedy.** Make it relative.

`broken reference`
:   **Cause.** A reference names a file the bundle lacks.

    **Remedy.** Add the file or fix the path.

`reference escapes the site`
:   **Cause.** A relative path climbs out of *dist/pages*.

    **Remedy.** Keep every asset inside the bundle.

`landing page links <name> N times (expected exactly once)`
:   **Cause.** The landing page links a download twice, or not at all.

    **Remedy.** Rebuild with `press pages`. If the count persists, report it to the press.

`sources companion looks empty of entries`
:   **Cause.** *config/authorities.yaml* exists, and the sources companion has no entries.

    **Remedy.** Populate the table of authorities (Chapter 10, *Front matter, the index, and the table of authorities*).

## The print pack {-}

The print pack's interior goes through the PDF verifier with the print profile, which adds two messages. Chapter 12, *The print pack*, lists the cover wrap checks. Intake refusals from `press art accept` belong to Chapter 11, *The art department*.

`print profile: margins do not mirror`

:   Press prints:

    ```text
    print profile: margins do not mirror (recto left edge
      Xpx, verso Ypx); the gutter is missing
    ```

    **Cause.** The median left ink edges of rectos and versos differ by under 18 pixels at 120 dpi.

    **Remedy.** Rebuild with `press verify-print`, and check any hand-authored TeX.

`print profile: colored ink on pages [...]`

:   Press prints:

    ```text
    print profile: colored ink on pages [...] (a colored
      cover plate in a hand-authored tex/title-page.tex
      belongs on the wrap; supply tex/title-page-print.tex
      without it)
    ```

    **Cause.** The listed pages carry color, in a profile without `ink: color`. A code fence with syntax highlighting also puts color on a page.

    **Remedy.** Do as the message says, and tag every fence `text`.

`no assets/cover.jpg; interior verified, wrap not built`
:   **Cause.** `press verify-print` found no *assets/cover.jpg*. It verified the print interior and did not build the cover wrap.

    **Remedy.** None if the book needs no wrap yet. To build and verify the wrap, supply *assets/cover.jpg* and run `press verify-print` again.

[^c-ellipsis]: Here `...` stands for the diagnostics that press prints after the colon.
