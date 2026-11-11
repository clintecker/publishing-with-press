# Introduction

![The shop at morning: a small press at the start of a build](assets/woodcuts/the-shop-at-morning.png){place=frontispiece}

<!-- art: a small nineteenth-century print shop at the start of the working day, seen from the doorway at eye level with correct one-point perspective and a level floor: a row of type cases on the left, a compact brass hand press with a lever and a platen in the centre, a long proofing table on the right under a tall window, morning light in parallel hatched rays, one apprentice in an apron carrying a chase of locked type toward the press, a second figure at the far table reading a sheet, shelves of bound volumes along the back wall; landscape composition; wood engraving with dense hatching and crosshatching, single black ink, no gray washes, no lettering anywhere -->

::: {.in-this-chapter}
> **In this chapter:**
>
> - What press is
> - Where it came from
> - The four laws
> - What press is not
> - A ten-minute tour
> - The editions
> - Versions and the pinned contract
> - How to read this book
:::

The press is a program that does the work of an old print shop, from compositor to proofreader, for a book written in plain Markdown. You give it a directory of chapters, and it gives back every *edition* of the book. An edition is one published form, such as a print-ready PDF, an EPUB, or a Web site. You never write a line of TeX, the typesetting language behind the print PDF, or type a pandoc command to get them. Before the press calls the book finished, it opens each file it built and checks what is inside.

## What press is

The press README describes the program in one plain sentence:

> A complete small press: everything required to turn a directory of Markdown chapters into a publishable book.

Its next sentence lists what a single command produces:

> One `press all` produces a verified 6 x 9 PDF, EPUB, single-file HTML, per-chapter reader site, stitched Markdown, plain text, DOCX, a GitHub Pages site with public downloads, and gated GitHub releases ...

The program is a Python package, and it installs a command of the same name.[^1-name] You run that command from inside a *book repository*, a directory that holds a *config/metadata.yaml* file and *the manuscript*. The manuscript is the chapter files and appendix files under *book/*. The 6 x 9 in the README is the default trim. It belongs to one of six *design profiles*, each a trim with its own interior geometry, and Chapter 9, *The house design*, compares them.

The package docstring names the work in three verbs: "A small press: the build, check, and verify pipeline for books." The press calls each command that does one of those jobs a *target*. You will meet `press check`, `press pdf`, `press all`, and the other targets one at a time in later chapters.

*The checker* is `press check`. It reads every chapter file before anything builds, and it refuses a manuscript that breaks one of its rules. An em dash, a curly quote, a glyph outside the print-font set, or a paragraph of 190 words or more stops it. Chapter 6, *Checking the manuscript*, lists every rule and its message.

The building falls to pandoc, a program that converts documents from one markup language to another. It reads your Markdown once and passes the document through a chain of Lua filters that the press supplies. A *Lua filter* is a small script, written in the Lua language, that pandoc runs over the document between reading it and writing it out. Apart from the PDF, pandoc's own writers produce the EPUB, the single HTML file, the chunked reader site, the plain text, and the DOCX. One edition skips pandoc altogether: the *Manuscript edition* is the chapters stitched into one Markdown file.

The PDF takes two more programs. Pandoc writes the book out as LaTeX, and LuaLaTeX, the TeX engine that sets the type, turns that LaTeX into pages. Then latexmk, a program that reruns LaTeX until the page references and the lists stop changing, drives it through as many passes as the book needs. You never see the LaTeX unless you go looking for it.

Verifying is the part a homemade build script usually leaves out. Each *verifier* opens a finished *artifact*, a file or directory in *dist/* that the press names and tracks, and inspects it as an object. The PDF verifier renders pages and checks the cover on page 1. The EPUB goes through epubcheck, the validator that retail channels run. The press does not call a book built until every verifier passes. @fig:pipeline-overview shows the whole path, from the manuscript at the left to the dist directory, *dist/*, at the right.

![From the manuscript to dist/: the path every edition takes](assets/woodcuts/01-01-pipeline-overview.png){#fig:pipeline-overview .diagram width=full-measure fig-alt="Chapter and config files pass through press check and pandoc, fork into a LuaLaTeX branch and a writers branch, and meet at the verifiers before the dist directory."}

<!-- art: ARCHETYPE pipeline, left to right. Far left: two stacked dog-eared file icons, "book/chapters/*.md" and "config/*.yaml". An arrow to a rounded box "press check", then to a rounded box "pandoc" with "+ Lua filters" inside. From pandoc two arrows fork: the upper, labeled "latexmk", runs to a rounded box "LuaLaTeX" and on to a file icon "alice.pdf"; the lower, labeled "pandoc writers", runs to a vertical stack of file icons "alice.epub", "alice.html", "site/", "alice.txt", "alice.docx". A thin bottom arrow labeled "stitch" runs from the manuscript straight to a file icon "alice.md". All file icons feed one drop-shadowed rounded box "verifiers", then a folder icon "dist/" at far right. The reader should see first that every edition starts from the same two inputs and passes the verifiers before it reaches dist/. -->

Under the press sits *the toolchain*, the programs it calls to do the work. They are pandoc, LuaLaTeX, latexmk, the Libertinus fonts,[^1-libertine] epubcheck with a Java to run it, and poppler, a set of PDF tools whose `pdftoppm` renders a page as an image for the verifier. The press itself needs Python 3.10 or later. @fig:the-stack shows how the layers rest on one another, with your book at the top and the operating system at the bottom.

![The layers under a book](assets/woodcuts/01-02-the-stack.png){#fig:the-stack .diagram width=full-measure fig-alt="Six stacked horizontal bands. From the bottom: operating system, Python, pandoc, TeX Live and LuaLaTeX, press, and your book on top, with the pandoc and TeX bands bracketed as the toolchain and its programs listed."}

<!-- art: ARCHETYPE layered stack. Six horizontal bands of equal size, bottom to top, alternating 10% and 20% gray fills, each with a centered label in small sans: "operating system"; "Python 3.10 or later"; "pandoc"; "TeX Live and LuaLaTeX"; "press"; "your book". The top band carries a flat 2 pt drop shadow. A thin bracket at the right spans the "pandoc" and "TeX Live and LuaLaTeX" bands, labeled "the toolchain: pandoc, LuaLaTeX, latexmk, fonts, epubcheck, poppler" in small italic. The reader should see first that the book rests on press, and press rests on programs it does not contain. -->

You can install the toolchain on your own machine. You can also use *the toolchain image*, `ghcr.io/clintecker/press-toolchain`, a public container image that holds all of it. The image carries Ubuntu 24.04's pandoc and TeX Live, and the press pins no tool by version number. Chapter 2, *Installing press*, covers both routes.

Above the toolchain, the press carries *the house*, its default design and law. The house includes the TeX header, the reader stylesheet, and the rules the checker applies. A book changes the house through its own config files and never by editing the press.

## Where it came from

The maintainer extracted the press from the production of an earlier book, *Mostly Done.*, so that the next book would not repeat the work. The package docstring gives the motive: "Extracted from the production of one book so the next book starts with the scars already paid for." A *scar*, in the press's vocabulary, is a production failure turned into a guard. Several of them appear later in this chapter. The first commit carries the date 2026-07-17.

The work moved quickly after that. Version 2.0.0 followed on 2026-07-21 as the "composable press", with design profiles, print providers, and an extension contract. Version 3.0.0 arrived on 2026-11-10. It was a design major, and the section "Versions and the pinned contract" later in this chapter explains why design needs one.

A second book put the docstring's claim to the test. *Make Ready* was "taken end to end through the built-in facilities". It had a commissioned clothbound cover, fourteen engraved plates finished by `press art enhance`, a subject index, registered ISBNs, and a table of authorities. Neither book lives in the press repository. The repository holds the machinery, and each book keeps its own repository.

One maintainer, Clint Ecker of LGTM Systems, LLC, looks after the press. Books from that shop appear under the LGTM Publishing imprint. The license is MIT, "code and bundled content alike". The README is plain about ownership: "A book you make with the press is yours entirely." The ROADMAP records the repository `clintecker/press` as public since 2026-07-19, and the documentation site is at *https://clintecker.github.io/press/*.

## The four laws

The press repository sets out four laws in *docs/ARCHITECTURE.md*. They account for most of the decisions you will meet in later chapters, including several that look strange the first time a refusal stops your build. Each law fits in a line.

### Facts are stated once

The first law reads "Facts are stated once." *ARCHITECTURE.md* then gives each kind of fact one home. A book's identity lives in its config, the house design lives in press data, and the artifact graph lives in the registry. *The registry* is that graph: the part of the press that names every artifact and records what each one depends on. The law ends with an instruction: "If you find the same fact in two places, one of them is a bug already filed or a bug you should file."

The Alice book shows the law at small scale. `press new alice` writes the slug `alice` once, into *config/metadata.yaml*. The registry derives every filename from it, so the PDF becomes *alice.pdf* and the EPUB becomes *alice.epub*. Nobody types either name. The ROADMAP states the same law as a product rule: facts are stated once and projected mechanically.

The law also runs in the other direction. The press repository contains no book. Its *CLAUDE.md* says so plainly: "Every book-specific fact (title, slug, sentinels, banned vocabulary, front matter, art) lives in the book repository that consumes this package." The same file adds "if a book needs machinery, the machinery belongs here". A book repository therefore holds book facts only, and a capability that one book needs goes into the press, where every other book can use it.

### Generators over checkers over conventions

The second law ranks three kinds of guard: "Prefer machinery that produces the right thing to machinery that detects the wrong thing, and either to a sentence in a document asking people to behave." A *generator* makes the right thing. A checker catches the wrong thing after someone makes it. A convention asks people to avoid it and hopes.

The tallest scar in the press shows the order at work. "A figure taller than the text block makes LuaLaTeX ship empty pages forever, silently, at 100% CPU." One answer is a warning in the documentation. The press chose a generator instead: the TeX header caps the height of every included image, so no Markdown figure can reach the fault. The cap varies by design profile, and on the house 6 by 9 it is 6.3 inches.

`press check` refusing an em dash is a checker. The style guide for this book is a convention, and the second law ranks it last. Most of that guide now also exists as regular expressions in this book's *config/house-rules.yaml*, where `press check` enforces them on every run. The guide remains in force for the rules that no regular expression can express.

### Artifacts are verified as objects

The third law sets the standard for a green build: "A green build means the actual PDF was rendered and inspected, the actual EPUB was validated by the tool retail channels run, the actual site was crawled." The ROADMAP adds that verifiers prove artifacts as objects "rather than trusting command exit status". An exit status of zero tells you that a program finished. It tells you nothing about whether the PDF has a cover.

*ARCHITECTURE.md* draws the line between the two halves of the work in one sentence: "generation makes a fact true, verification proves it stayed true all the way into the object a reader receives." The law also forbids verifying without rebuilding. A verifier that inspects last week's PDF blesses last week's PDF. The press's own notes say that "the CLI's dependency edges exist so that cannot happen".

::: {.sidebar}
> **The cover that passed at 11.5 percent**
>
> A title-page generator in the press once went out with a dropped cover and a clipped cover. The generator had tests, and they covered 11.5 percent of its lines. *CONTRIBUTING.md* records the cause in one clause: "the lines ran, the artifact was never inspected."
>
> Nothing in the suite opened the PDF and looked at page 1. The tests asked whether the code executed, and it did. Nobody asked whether a reader would find a cover at the front of the book.
>
> The fix came in two parts. The first was a rule, which *CONTRIBUTING.md* now states without qualification: "A producer is only proven by a verifier that rejects a broken artifact." A new generator counts as proven only when some verifier fails on its broken artifact. The second part was the verifier itself: the PDF verifier now checks the cover on page 1.
:::

### Scars become law

The fourth law turns history into code: "Every production failure earns a mechanical guard and an entry in CLAUDE.md's scars list. Do not relearn them." The ROADMAP sets the bar higher than a list. It says a scar becomes an executable invariant, a named proof, or an explicit public contract. A warning in prose is not enough by itself.

The epubcheck scar shows what that means. Ubuntu's `epubcheck` launcher runs the Java archive through binfmt_misc, a kernel feature that containers do not register. In a container, "the command exists, `which` finds it, and it dies with 'Exec format error' only at execution." The toolchain image now carries a plain `java -jar` wrapper. The verifier also reports a present but unrunnable tool as a toolchain fault, so the EPUB takes no blame for it.

## What press is not

"Press is a prose engine," says *docs/NON-GOALS.md*. The rest of that file lists what follows from it. The press is not a page-layout or design application, and it does not replace InDesign, Affinity, Scribus, or Quark. It does not design fixed-layout picture books, comics, or magazines. It does not build interactive or rich-media e-books either.

The same file gives a test for new requests. Another trim, a color interior, or large print is a new profile of the prose engine, and *NON-GOALS.md* calls that core press work. A new engine falls outside it. For books with designed interiors, the plan is the *finisher*, a supplied-interior source mode in which the book names a finished PDF with `interior: path/to/interior.pdf`. At the time of this writing, the finisher sits on the Book breadth milestone as planned work, and press 3.0.2 does not include it.

Some smaller limits follow from the same choice. The press has no book-level `\part` divisions. Its cross-references point at figures and nothing else, so it does not number a reference to a chapter or a section for you. It does not generate a glossary or an "also by" page, although both appear in the plans. Non-Latin and right-to-left scripts sit in the icebox, at the stated price of "a major per script family". Nobody tests the press on Windows.

The press also has no plugin loader. *ARCHITECTURE.md* gives the reason in one line: "Behavior cannot come from the accident of which package imported first." Extensions go through a declared extension contract, which Chapter 16, *Inside the press*, describes.

The QUICKSTART draws the boundary from the author's side. The title, the author, the words, and the visual identity are "yours to decide". The build order, the verification pipeline, the filenames, and the editions belong to the press. If you want to rename *alice.pdf* or skip epubcheck, you ask for something the press does not offer.

## A ten-minute tour

The quickest way to understand the press is to watch it make a book. The sample book throughout is Lewis Carroll's *Alice's Adventures in Wonderland*, which the user `alice` builds on a workstation called `hatter`. The tour takes it from an empty directory to a full dist directory, using the commands from the press QUICKSTART with the Alice book's names in place. It assumes that you already installed the press and the toolchain, as Chapter 2, *Installing press*, describes. @fig:ten-minute-tour, at the end of the build, collects three moments from the tour.

### Scaffolding the book

`press new` creates a book repository from the house template, and it takes the slug from the directory name. Example 1.1 creates the Alice book, sets its title, author, and description, and puts the scaffold under Git.

**Example 1.1. Scaffolding the Alice book**

```text
$ press new alice
$ cd alice
$ press config set title "Alice's Adventures in Wonderland" && \
  press config set author '["Lewis Carroll"]' --json && \
  press config set description "A girl falls into Wonderland."
$ git init && git add -A && git commit -m "First book"
...
```

The new directory holds a *config/metadata.yaml* with `slug: "alice"`, a *book/chapters/* directory with a one-paragraph preface, and the rest of the scaffold. Chapter 3, *The shape of a book repository*, walks through it file by file. Each `press config set` writes one field, and the `--json` option reads the value as JSON, which is how a list of authors goes in. The checker refuses a book without a description, so the tour sets one now. `press new` does not run `git init`, and the source archive holds only the files Git tracks, so the tour commits the scaffold before the first build.[^1-make]

### Checking the manuscript

Next, run the checker. On a fresh scaffold it succeeds, and its output names its four passes in order:

```text
$ press check
Source checks passed: 1 ordered Markdown files
...
Editorial checks passed: 1 Markdown files
...
```

The count is 1 because the scaffold holds a single chapter file, the preface. The first line reports the source checks, which read every chapter file in order. The `Editorial checks` line reports the style audit. The two elided lines report the other passes. One is a selftest of the checker's own rules. The other is the jargon lint, which looks for terms from the *watchlist*, the press's list of overused words.

The selftest is the unusual pass. A *known-bad fixture* is a file that every check must reject. On each check, the press runs all 19 of its known-bad fixtures through its own rules. If a rule stops catching the thing it exists to catch, the selftest fails before that broken rule can pass your manuscript.

`press wordcount` counts the prose. It strips fenced and inline code. It counts HTML comments, so a comment inside a chapter adds to the total.

```text
$ press wordcount
    42  book/chapters/00-preface.md
    42  TOTAL
```

### Building everything

With the check passing, run `press all`. It runs the checker again, builds every edition, packs the source archive, and assembles the Pages bundle. Then it runs the verifiers, and it finishes with an advisory commerce gate that applies only when a book enables print ordering. Example 1.2 shows the summary lines from a run on the press's own Alice example, which has three chapters and an appendix, and elides the rest.

::: {.warning}
> **Warning:** Leave the first LuaLaTeX run on a fresh machine alone. Its font scan takes several minutes and looks like a hang. It is not a hang, although it gives a very convincing imitation of one.
:::

**Example 1.2. The summary lines of press all**

```text
$ press all
...
  ¶ check      ✓ style, source, jargon
...
+ stitched 4 files -> dist/alice.md
...
+ assembled pages site -> dist/pages
  ¶ typeset    ✓ PDF · EPUB · web · text · DOCX
...
Verified archives: alice-site.zip, alice-source.zip
  ¶ verify     ✓ 7 editions match source
...
  press. your book is ready → dist/
```

Table 1.1 explains each line that Example 1.2 shows, by the words that identify it.

| Line | Meaning |
|---------------------------------|----------------------------------------------------|
| `check` | All four passes of the checker succeeded, the same passes that `press check` runs. |
| `stitched 4 files` | The press joined the chapter and appendix files into *alice.md*, the Manuscript edition, without pandoc. |
| `assembled pages site` | The press built the GitHub Pages bundle in *dist/pages/*. |
| `typeset` | The PDF, the EPUB, the Single-leaf edition (one HTML file), the Chapter edition (the reader site), the text, and the DOCX all built. |
| `Verified archives` | The verifier checked both zip archives. |
| `verify` | Seven editions agree with the manuscript. |
| `your book is ready` | The run finished, and the artifacts wait in *dist/*. |

Table: Table 1.1. The summary lines of a press all run

The elided verifier lines carry the detail. For the Alice example, the PDF line reports "23 pages, 6 x 9 trim, embedded fonts" and goes on to "every rendered page contains ink, no edge clipping, cover on page 1". That last check is the one the sidebar earlier in this chapter explains. On a machine without epubcheck, the run warns that it validated the EPUB "structurally only", and it notes that the toolchain image runs the full check in CI.

When the run finishes, *dist/* holds the artifacts in Example 1.3.

**Example 1.3. dist/ after press all**

```text
$ ls dist/
alice-site.zip
alice-source.zip
alice.docx
alice.epub
alice.html
alice.md
alice.pdf
alice.txt
pages
site
```

Each entry in Example 1.3 is an edition or holds one, and the section "The editions" later in this chapter names them. `press all` built the landing page too. Open *dist/pages/index.html* in a Web browser to see the book as a reader will. The separate `press pages` target rebuilds that bundle alone. @fig:ten-minute-tour gathers the tour so far into three frames.

![Three moments of the tour: scaffold, check, and the finished dist/](assets/woodcuts/01-03-ten-minute-tour.png){#fig:ten-minute-tour .diagram width=full-measure fig-alt="Three terminal windows stacked one above another. The first creates the alice book, the second shows press check passing, and the third lists the artifacts in the dist directory."}

<!-- art: ARCHETYPE filmstrip, stacked vertically. Three boxed terminal panels, one above another, each 72 columns wide, black monospace on white, numbered 1, 2, 3 at the left of each frame. Panel 1, three lines: "$ press new alice"; "$ cd alice"; "$". Panel 2, five lines exactly: "$ press check"; "Source checks passed: 1 ordered Markdown files"; "..."; "Editorial checks passed: 1 Markdown files"; "...". Panel 3, eleven lines exactly: "$ ls dist/"; "alice-site.zip"; "alice-source.zip"; "alice.docx"; "alice.epub"; "alice.html"; "alice.md"; "alice.pdf"; "alice.txt"; "pages"; "site". Each panel is only as tall as its lines. The reader should see first the progression down the page, from an empty book to a full dist/. -->

### Publishing the book

The last step puts the book on the Web. The scaffold already carries *.github/workflows/book.yml*, a short workflow that calls the press's reusable workflow, *build.yml*, so a push is all that CI needs. Add the remote for the `wonderland-press` account and push:

```text
$ git remote add origin \
  https://github.com/wonderland-press/alice
$ git push -u origin main
```

Then enable GitHub Pages once, in the repository settings on GitHub: under Pages, set Source to GitHub Actions. From then on, the CI runner, which this book calls `printshop`, builds the book inside the toolchain image on every push. Chapter 14, *Continuous integration and the release contract*, follows that build step by step.

When the tour goes wrong, the QUICKSTART lists five usual causes:

1. `pandoc is required`. The toolchain is missing, or pandoc is not on your path.
2. A style or jargon failure. The checker refused something in the manuscript.
3. `sentinel ... not found`. A verifier could not find a sentinel phrase, which the section "The editions" explains.
4. A font scan that looks like a hang. The warning earlier in this section covers it.
5. A CI build that dies at "Initialize containers". Run the build again. The image is public, so no permission is missing.

::: {.tip}
> **Tip:** To see a finished book before you write one, build an example from the gallery. Clone the press repository, run `pip install -e .` in it, change into *examples/alice-in-wonderland/*, and run `press all`. That example sets Tenniel's 1865 wood engravings as *plates*, the unnumbered illustrations in the List of Plates.
:::

## The editions

Every edition is an artifact, and a few artifacts hold editions instead of being one. The press gives each edition a name, and Table 1.2 lists them for the Alice book.

| Edition | Artifact | Meaning |
|----------------------|--------------------------------|--------------------------------------|
| Print edition | `alice.pdf` | The reading PDF, typeset by LuaLaTeX in the book's design profile. |
| Circulating edition | `alice.epub` | The EPUB for e-readers and retail channels. The press runs epubcheck over it. |
| Single-leaf edition | `alice.html` | The whole book in one self-contained HTML file. |
| Chapter edition | `site/` and `alice-site.zip` | The reader site, with one Web page per chapter, its stylesheet, and its images. The zip archive holds the same site, boxed. |
| Manuscript edition | `alice.md` | The chapters stitched into one Markdown file. It is the manuscript itself, and pandoc does not render it. |
| Telegraphic edition | `alice.txt` | The book as plain text, 80 columns wide. |
| Office edition | `alice.docx` | A DOCX file for word processors. |
| Source edition | `alice-source.zip` | An archive of the files Git tracks in the book repository. |

Table: Table 1.2. The editions of the Alice book

The GitHub Pages bundle, *dist/pages/*, gathers the editions for readers. It holds the landing page, a *read/* copy of the reader site, and a *downloads/* directory that links every published download exactly once. When the metadata sets `site-url`, the bundle also gets a *sitemap.xml* and a *robots.txt*.

A book with a *config/authorities.yaml*, its table of authorities, gets one more file. The press generates *alice-sources.md*, *the sources companion*, a document published beside the book. Chapter 10, *Front matter, the index, and the table of authorities*, covers it. The Alice example has no authorities file, so its *dist/* has no sources companion.

*The print pack* is the set of artifacts a printer needs. It holds a print-profile interior, a *cover wrap* (the whole cover, back to front, as one PDF) with a computed spine and an EAN-13 barcode, and the retail channel checklists. `press all` does not build the print pack. Its own targets do: `press print`, `press verify-print`, and `press coverwrap`, which add *alice-interior.pdf* and *alice-coverwrap.pdf* to *dist/*. Chapter 12, *The print pack*, covers it in full.

Everything the press makes on the way to *dist/* stays in the build directory, *build/*. That directory holds the rendered pandoc defaults, the generated subject index, the front matter as TeX, the jargon report, and the page images that `press render` draws at 160 dpi. `press clean` deletes both *build/* and *dist/*.

A *sentinel* is a phrase from the manuscript, listed under `verify-sentinels` in *config/metadata.yaml*, that the verifiers must find in the manuscript and in every artifact. If one goes missing, the build stops with `sentinel ... not found`. A second setting, `verify-min-pages`, sets the fewest pages the PDF may have. The scaffold writes 1, which suits a book that is one preface long. If you delete that line, the default of 40 applies, and a short book then fails. A release build refuses both draft values, and it needs at least 2 sentinels and a floor of at least 24 pages.

::: {.warning}
> **Warning:** If your book uses the drop-cap chapter opening, do not take a sentinel from the first words of a chapter. The drop cap splits the first word and sets the rest of it in small caps, so a sentinel placed there fails the exact match in the PDF. The house default is no drop cap at all.
:::

## Versions and the pinned contract

At the time of this writing, the current release is press 3.0.2, dated 2026-11-11. A *floating tag* such as `v3` moves forward within its major as new releases come out, and an *immutable tag* such as `v3.0.2` names one release forever. *The release contract* is the workflow that proves a tag. At each three-part tag, it requires the press's reusable workflow to pin the toolchain image by an `@sha256:` digest, which fixes the exact bytes. Design falls under the same contract: within a major, fixes may correct broken output, but they must not change the typography or layout of a valid book. A design change needs a new major, which is why v3.0.0 is one.

::: {.tip}
> **Tip:** Pin `v3` to receive fixes as they come. When a book must rebuild from the same press and toolchain years from now, pin a three-part tag such as `v3.0.2` and move that pin on purpose. Chapter 14, *Continuous integration and the release contract*, takes the mechanism apart.
:::

## How to read this book

The chapters follow the order in which you make a book. Chapters 2 through 8 take a book from installation to verified artifacts. They cover installation, the shape of a book repository, the manuscript, figures and plates, checking, building, and verifying. Read them in order the first time.

Chapters 9 through 13 cover the work that follows a sound manuscript: the house design, the front matter and index, the art department, the print pack, and registrations. Read them when your book needs them. Chapters 14 through 16 are for the person who runs the press. They cover continuous integration and the release contract, *the desk* (the terminal screen that `press desk` opens) and the editorial workflows, and the internals.

The appendixes are for reference. Appendix A, *Command reference*, gives every command in manual-page form, and Appendix B, *Configuration reference*, gives every key of every config file. If the press stops a build with a message you do not recognize, look it up in Appendix C, *Messages and refusals*, before you read the code. Appendix D, *The toolchain, platform by platform*, covers each operating system, and Appendix E, *Glossary*, defines the terms.

The Preface lists the typographic conventions, and two of them matter at once. Sessions show the `$` prompt followed by what you type. A line that holds only `...` marks output that the example leaves out. Every example hangs on the Alice book: the user `alice` on `hatter`, the CI runner `printshop`, and the repository owner `wonderland-press`. The author typed the chapter references in this book by hand, because the press cross-references figures and nothing else. By the terms of the second law they are a convention, the weakest kind of guard, and you should treat them with the matching degree of trust.

Chapter 2, *Installing press*, puts the toolchain on `hatter`.

[^1-name]: The program writes its name in lowercase, like the command, and it uses the pilcrow, the paragraph sign, as its mark.

[^1-libertine]: TeX Live carries Libertinus for the PDF. Ubuntu has no `fonts-libertinus` package, and `--no-install-recommends` drops the Libertine keyboard face, so the toolchain image names `fonts-linuxlibertine` explicitly. That is another scar.

[^1-make]: The press README's own quick start runs `git init` in the same place, with `make all` in place of `press all`. The scaffold's Makefile passes every target to `python3 -m press`.

<!-- index: press; book repository; manuscript; target; press check; checker; verifier; registry; four laws; scar; generator; Lua filter; toolchain; toolchain image; design profile; edition; artifact; dist directory; build directory; known-bad fixture; sentinel; verify-min-pages; print pack; floating tag; immutable tag; release contract -->
