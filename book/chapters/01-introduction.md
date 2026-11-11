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

For most of the history of print, a book reached its readers through a shop full of people. A compositor set the type, a proofreader read it, a pressman printed it, and someone checked the pressman's work. press is a program that does that work for a book written in plain Markdown. It checks the manuscript, builds every edition, and then opens each file it built to confirm that the file holds what it should. The sample book throughout is Lewis Carroll's *Alice's Adventures in Wonderland*, which the user `alice` builds on a workstation called `hatter`.

## What press is

*press* is a Python package and the command it installs, and its name is lowercase like the command. You run it from inside a *book repository*, a directory that holds a *config/metadata.yaml* file and *the manuscript*, the chapter files and appendix files under *book/*. The press README states the whole claim in its first paragraph:

> One `press all` produces a verified 6 x 9 PDF, EPUB, single-file HTML, per-chapter reader site, stitched Markdown, plain text, DOCX, a GitHub Pages site with public downloads, and gated GitHub releases.

The 6 by 9 in that sentence is the default trim, and it is no longer the only one. Since version 2, press offers six design profiles. A *profile* is a sealed interior geometry, and the house 6 by 9 is one profile among the six. Chapter 9, *The house design*, compares them.

The package describes itself in fewer words. Its docstring begins "A small press: the build, check, and verify pipeline for books." Those three verbs name the three kinds of work press does, and press calls each command that does one of them a *target*. You will meet `press check`, `press pdf`, `press all`, and the rest of the targets one at a time in later chapters.

*The checker* is `press check`. It reads every chapter file before anything builds, and it refuses a manuscript that breaks the house rules. An em dash, a curly quote, a glyph outside the print fonts, or a paragraph of 190 words or more each stops it. Chapter 6, *Checking the manuscript*, lists every rule and its message.

Building is the work of pandoc. It reads the Markdown and passes the document through a chain of Lua filters that press supplies. For the PDF, pandoc writes LaTeX, and latexmk then drives LuaLaTeX through as many passes as the lists and cross-references need. For the other editions, pandoc's own writers produce the EPUB, the single HTML file, the chunked reader site, the plain text, and the DOCX. One edition skips pandoc altogether: the Markdown edition is the manuscript stitched into one file.

Verifying is the part a home-made build script usually leaves out. Each *verifier* opens a finished artifact and inspects it as an object. The PDF verifier renders pages and looks for the cover on page 1. The EPUB goes through epubcheck, the validator that retail channels run. press does not call a book built until every verifier passes. @fig:pipeline-overview shows the whole path. The manuscript sits at the left, and *dist/*, the directory that holds every published artifact, sits at the right.

<!-- art: ARCHETYPE pipeline, left to right. Far left: two stacked dog-eared file icons, "book/chapters/*.md" and "config/*.yaml". An arrow to a rounded box "press check", then to a rounded box "pandoc" with "+ Lua filters" inside in small monospace. From pandoc two arrows fork: the upper, labelled "latexmk", runs to a rounded box "LuaLaTeX" and on to a file icon "alice.pdf"; the lower, labelled "pandoc writers", runs to a vertical stack of file icons "alice.epub", "alice.html", "site/", "alice.txt", "alice.docx". A thin bottom arrow labelled "stitch" runs from the manuscript straight to a file icon "alice.md". All file icons feed one drop-shadowed rounded box "verifiers", then a folder icon "dist/" at far right. The reader should see first that every edition starts from the same two inputs and passes the verifiers before it reaches dist/. -->
![From the manuscript to dist/: the path every edition takes](assets/woodcuts/01-01-pipeline-overview.png){#fig:pipeline-overview .diagram width=full-measure fig-alt="Chapter and config files pass through press check and pandoc, fork into a LuaLaTeX branch and a writers branch, and meet at the verifiers before the dist directory."}

press sits on top of *the toolchain*, the programs it calls to do the work: pandoc, LuaLaTeX, latexmk, the fonts, epubcheck, and poppler. press itself needs Python 3.10 or later. @fig:the-stack shows how the layers rest on one another, with your book at the top and the operating system at the bottom.

<!-- art: ARCHETYPE layered stack. Six horizontal bands of equal size, bottom to top, alternating 10% and 20% gray fills, each with a centred label in small sans: "operating system"; "Python 3.10 or later"; "pandoc"; "TeX Live and LuaLaTeX"; "press"; "your book". The top band carries a flat 2 pt drop shadow. A thin bracket at the right spans the "pandoc" and "TeX Live and LuaLaTeX" bands, labelled "the toolchain" in small italic. The reader should see first that the book rests on press, and press rests on programs it does not contain. -->
![The layers under a book](assets/woodcuts/01-02-the-stack.png){#fig:the-stack .diagram width=full-measure fig-alt="Six stacked horizontal bands. From the bottom: operating system, Python, pandoc, TeX Live and LuaLaTeX, press, and your book on top, with the pandoc and TeX bands bracketed as the toolchain."}

You can install the toolchain on your own machine. You can also use *the toolchain image*, `ghcr.io/clintecker/press-toolchain`, a public container image that holds all of it. press does not pin pandoc or TeX Live by version number. The image carries whatever Ubuntu 24.04 packaged. A book's CI pins the image itself by digest, as the section "Versions and the pinned contract" explains later in this chapter. Above the toolchain, press carries *the house*, its default design and law. The house includes the TeX header, the reader stylesheet, the jargon watchlist, and a set of fixtures that every check must reject.[^mark] A book changes the house through its own config files and never by editing press.

## Where it came from

The maintainer extracted press from the production of an earlier book, *Mostly Done.*, so that the next book would not repeat the work. The package docstring gives the motive directly: "Extracted from the production of one book so the next book starts with the scars already paid for." The first commit, `6ee1498`, carries the date 2026-07-17, and its message describes the pipeline with the book taken out.[^first-commit] By 2026-11-11 the repository held 560 commits.

The early pace was quick. The tags v1.0.0 through v1.6.0 all carry the date 2026-07-18, the day after the first commit.[^tags] The CHANGELOG begins at v1.7.0. Everything earlier lives only in the tags, and the CHANGELOG lists it in one sentence:

> the packaged instruments, the art department, generated front matter, the print pack, registrations, the operator, the aesthetic system, and the public-readiness hardening of the P0/P1 audit

Version 2.0.0 followed on 2026-07-21 as the "composable press", with print profiles, print providers, and an extension contract. Version 3.0.0 arrived on 2026-11-10. It was a design major, and the section "Versions and the pinned contract" later in this chapter explains why design needs one.

A second book put the docstring's claim to the test. *Make Ready* was "taken end to end through the built-in facilities": a commissioned clothbound cover, fourteen engraved plates finished by `press art enhance`, a subject index, registered ISBNs, and a table of authorities. Neither book lives in the press repository. The repository holds the machinery, and each book keeps its own repository.

press has one maintainer, Clint Ecker of LGTM Systems, LLC, and books from that shop appear under the LGTM Publishing imprint. The license is MIT, "code and bundled content alike", and the README is plain about ownership: "A book you make with the press is yours entirely." The repository `clintecker/press` became public on 2026-07-19. The documentation site is at *https://clintecker.github.io/press/*.

The press guards the neutrality of its scaffold with some care. A selftest named `scaffold_neutrality` checks that a freshly scaffolded book contains neither "Clint Ecker" nor "LGTM". An integration gate goes further and requires that "no original-book identity may appear in a clean scaffold's public artifacts". This book carries both names on its title page. It is a book repository and not a scaffold, so the rule does not reach it.

## The four laws

The press repository sets out four laws in *docs/ARCHITECTURE.md*. They account for most of the decisions you will meet in later chapters, including several that look strange the first time a refusal stops your build. Each law fits in a line, and the ROADMAP restates most of them as product rules.

### Facts are stated once

The first law reads "Facts are stated once." ARCHITECTURE.md then gives each kind of fact one home. A book's identity lives in its config, the house design lives in press data, and the artifact graph lives in the registry. *The registry* is that artifact graph: the part of press that names every artifact and what each one depends on. The law ends with an instruction: "If you find the same fact in two places, one of them is a bug already filed or a bug you should file."

The Alice book shows the law at small scale. The slug `alice` appears once, in *config/metadata.yaml*. The registry derives every filename from it, so the PDF becomes *alice.pdf* and the EPUB becomes *alice.epub*, and nobody types either name. The ROADMAP states the same law as a product rule: facts are stated once and projected mechanically.

The law also runs in the other direction. The press repository contains no book. Its CLAUDE.md says so plainly: "Every book-specific fact (title, slug, sentinels, banned vocabulary, front matter, art) lives in the book repository that consumes this package." The same file adds "if a book needs machinery, the machinery belongs here". A book repository holds book facts only. When a book needs a new capability, the capability goes into press, where every other book can use it.

### Generators over checkers over conventions

The second law ranks three kinds of guard: "Prefer machinery that produces the right thing to machinery that detects the wrong thing, and either to a sentence in a document asking people to behave." A *generator* makes the right thing. A checker catches the wrong thing after someone makes it. A convention asks people to avoid it and hopes.

The tallest scar in press shows the order at work. "A figure taller than the text block makes LuaLaTeX ship empty pages forever, silently, at 100% CPU." One answer is a warning in the documentation. The press chose a generator instead: the TeX header caps the height of every included image, so no Markdown figure can reach the fault. The cap varies by profile, and on the house 6 by 9 it is 6.3in.

`press check` refusing an em dash is a checker. The style guide for this book is a convention, and the second law ranks it last. Most of that guide now also exists as regular expressions in this book's *config/house-rules.yaml*, where `press check` enforces them on every run. The guide remains in force for the rules that no regular expression can express.

### Artifacts are verified as objects

The third law sets the standard for a green build: "A green build means the actual PDF was rendered and inspected, the actual EPUB was validated by the tool retail channels run, the actual site was crawled." The ROADMAP adds that verifiers prove artifacts as objects "rather than trusting command exit status". An exit status of zero tells you that a program finished. It tells you nothing about whether the PDF has a cover.

ARCHITECTURE.md draws the line between the two halves of the work in one sentence: "generation makes a fact true, verification proves it stayed true all the way into the object a reader receives." The law also forbids verifying without rebuilding. A verifier that inspects last week's PDF blesses last week's PDF. The commands in press carry dependency edges for that reason, and an invariant called `INV-graph-no-stale` guards them.

::: {.sidebar}
> **The cover that passed at 11.5 percent**
>
> A title-page generator in press once went out with two broken covers: one dropped out of place, and one clipped. The generator had tests, and they covered 11.5% of its lines. CONTRIBUTING.md records the cause in one clause: "the lines ran, the artifact was never inspected."
>
> Nothing in the suite opened the PDF and looked at page 1. The tests asked whether the code executed, and it did. Nobody asked whether a reader would find a cover at the front of the book.
>
> The fix came in two parts. The first was a rule, which CONTRIBUTING.md now states without qualification: "A producer is only proven by a verifier that rejects a broken artifact." A new generator counts as proven only when some verifier would refuse its broken output. The second part was the verifier. The PDF verifier now checks for the cover on page 1 of every book it inspects, including books that never had a cover problem.
:::

### Scars become law

The fourth law turns history into code: "Every production failure earns a mechanical guard and an entry in CLAUDE.md's scars list. Do not relearn them." A *scar* is a production failure turned into a guard. The ROADMAP sets the bar higher than a list. It says a scar becomes an executable invariant, a named proof, or an explicit public contract, and that a warning in prose is not enough by itself.

The epubcheck scar shows what that means. Ubuntu's `epubcheck` launcher runs the Java archive through binfmt_misc, which containers do not register. Inside the toolchain image, "the command exists, `which` finds it, and it dies with 'Exec format error' only at execution." The image now ships a plain `java -jar` wrapper. The verifier also reports a present but unrunnable tool as a fault in the toolchain, so nobody spends an afternoon looking for a defect in a sound EPUB.

The ROADMAP explains why the laws stack the way they do. In its account, trust accumulates upward from deterministic functions through real tools, complete workflows, consumer repositories, and release identity. It adds that "A higher layer cannot erase missing proof below it." The 3.0.2 release met that case in its own Lua filters.[^vacuous]

::: {.warning}
> **Warning:** Never pipe a check command into `grep` before `&&` in a commit chain. The exit status of the pipeline is grep's, and a failing check once went through as a passing one that way.
:::

## What press is not

"Press is a prose engine," says *docs/NON-GOALS.md*. The rest of that file lists what follows from it. press is not a page-layout or design application, and it does not replace InDesign, Affinity, Scribus, or Quark. It does not design fixed-layout picture books, comics, or magazines. It does not build interactive or rich-media ebooks either.

The same file gives a test for new requests. Another trim, a colour interior, or large print is a new profile of the prose engine, and NON-GOALS.md calls that core press work. A new engine falls outside it. For books with designed interiors, the plan is the *finisher*, a supplied-interior source mode in which the book names a finished PDF with `interior: path/to/interior.pdf`. At the time of this writing, the finisher sits on the Book breadth milestone as planned work, and press 3.0.2 does not include it.

Some smaller limits follow from the same choice. press has no book-level `\part` divisions. Its cross-references point at figures and nothing else, so press does not number a reference to a chapter or a section for you. It does not generate a glossary or an "also by" page, although both appear in the plans. Non-Latin and right-to-left scripts sit in the icebox, at the stated price of "a major per script family". Nobody tests press on Windows.

press also has no plugin loader. ARCHITECTURE.md gives the reason in one line: "Behavior cannot come from the accident of which package imported first." Extensions go through a declared extension contract, which Chapter 16, *Inside the press*, describes.

The QUICKSTART draws the boundary from the author's side. The title, the author, the words, and the visual identity are "yours to decide". The build order, the verification pipeline, the file names, and the formats belong to the press. If you want to rename *alice.pdf* or skip epubcheck, you ask for something press does not offer, and it will tell you so.

## A ten-minute tour

The quickest way to understand press is to watch it make a book. The tour that follows takes `alice` from an empty directory on `hatter` to a full *dist/*. It uses the commands from the press QUICKSTART, with the Alice book's names in place. It assumes that you already installed press and the toolchain, as Chapter 2, *Installing press*, describes. @fig:ten-minute-tour collects three moments from the tour into one strip.

### Scaffolding the book

`press new` creates a book repository from the house template. Example 1.1 creates the Alice book, sets its title, author, and description, and puts the scaffold under Git.

**Example 1.1. Scaffolding the Alice book**

```
$ press new alice
$ cd alice
$ press config set title "Alice's Adventures in Wonderland" && \
  press config set author '["Lewis Carroll"]' --json && \
  press config set description "A girl falls down a rabbit hole."
$ git init && git add -A && git commit -m "First book"
...
```

The new directory holds a *config/metadata.yaml*, a *book/chapters/* directory with a 42-word preface stub, and the rest of the scaffold. Chapter 3, *The shape of a book repository*, walks through the scaffold file by file. Each `press config set` writes one field. The `--json` option tells press to read the value as JSON, which is how a list of authors goes in. The Source edition holds only the files Git tracks, so the tour commits the scaffold before the first build.

### Checking the manuscript

Next, run the checker. On a fresh scaffold it passes, and its output names its passes in order. The fragment below shows the first line and elides the rest:

```
$ press check
Source checks passed: 1 ordered Markdown files
...
```

The full output has four summary lines, one for each pass, and Table 1.1 reads them. The count is 1 because the scaffold holds a single chapter file, the preface.

| Line begins | Meaning |
|------------------|------------------------------------------------------------|
| `Source checks passed` | The source checks read every chapter file in order and found no fault. |
| `Checker self-test passed` | All 19 known-bad fixtures tripped their declared rule, and the known-good fixture passed. The em-dash and en-dash fixtures also drew a second complaint each, which press reports as notes. |
| `Editorial checks passed` | The style audit read every Markdown file and found no refused pattern. |
| `Jargon check passed` | The jargon lint found no term from the watchlist with the rewrite status. The full audit goes to *build/jargon-report.txt*. |

Table: Table 1.1. The four lines of a passing press check

The second line deserves a moment. A *known-bad fixture* is a file that every check must reject, and press runs every one of its fixtures through its own rules on each check. If a rule stops catching the thing it exists to catch, the self-test fails before your manuscript can pass a broken rule.

`press wordcount` counts the prose. It strips fenced and inline code, and it counts HTML comments, so an `art:` directive adds to the total.

```
$ press wordcount
    42  book/chapters/00-preface.md
    42  TOTAL
```

### Building everything

::: {.warning}
> **Warning:** The first LuaLaTeX run on a fresh machine starts a font scan that takes several minutes. It looks like a hang. Leave it alone, because it is not one, although it gives a very convincing imitation of one.
:::

With the check passing, run `press all`. It runs the checker again, builds each edition, and runs the verifiers against the result. When it finishes, *dist/* holds the artifacts in Example 1.2.

**Example 1.2. dist/ after press all**

```
$ press all
...
$ ls dist/
alice-site.zip    alice.docx  alice.html  alice.pdf  pages
alice-source.zip  alice.epub  alice.md    alice.txt  site
```

Each file in Example 1.2 is an edition or holds one, and the section "The editions" later in this chapter names them. To look at the landing page as a reader will see it, run `press pages` and open *dist/pages/index.html* in a Web browser. The page links every download exactly once.

<!-- art: ARCHETYPE filmstrip. Three boxed terminal panels in a row, black monospace on white, 72 columns wide, numbered 1, 2, 3 beneath. Panel 1: "$ press new alice", "$ cd alice", and a bare "$". Panel 2, each line exactly, long lines wrapped at 72 columns: "$ press check"; "Source checks passed: 1 ordered Markdown files"; "..."; "Checker self-test passed: 19 known-bad fixtures each tripped their declared rule, known-good fixture accepted, 2 extra diagnostics noted"; "Editorial checks passed: 1 Markdown files"; "Jargon check passed: no rewrite-status terms (full audit in build/jargon-report.txt)". Panel 3: "$ ls dist/", then "alice-site.zip    alice.docx  alice.html  alice.pdf  pages" and "alice-source.zip  alice.epub  alice.md    alice.txt  site". The reader should see first the progression from an empty book to a full dist/. -->
![Three moments of the tour: scaffold, check, and the finished dist/](assets/woodcuts/01-03-ten-minute-tour.png){#fig:ten-minute-tour .diagram width=full-measure fig-alt="Three terminal windows side by side. The first creates the alice book, the second shows press check passing all four of its passes, and the third lists the artifacts in the dist directory."}

### Publishing the book

The last step puts the book on the Web. Add the remote for the `wonderland-press` account and push:

```
$ git remote add origin https://github.com/wonderland-press/alice
$ git push -u origin main
```

Then enable GitHub Pages once, in the repository settings on GitHub: under Pages, set Source to GitHub Actions. On GitHub, the CI runner, which this book calls `printshop`, builds the book inside the toolchain image. Chapter 14 follows that build step by step.

When the tour goes wrong, the QUICKSTART lists the five usual causes. The first is `pandoc is required`, which means the toolchain is missing. The second is a style or jargon failure from the checker. The third is `sentinel ... not found` from a verifier, which the section "The editions" explains. The fourth is the font scan that looks like a hang. The fifth is a CI build that dies at "Initialize containers", and the cure for that one is to run it again, because the toolchain image is public.

::: {.tip}
> **Tip:** To see a finished book before you write one, build an example from the gallery. Clone the press repository, run `pip install -e .` in it, change into *examples/alice-in-wonderland/*, and run `press all`. That example sets Tenniel's 1865 wood engravings as plates.
:::

## The editions

An *edition* is one published form of the book, such as the PDF or the EPUB. An *artifact* is a file or directory in *dist/* that the registry names. Every edition is an artifact, and a few artifacts hold editions instead of being one. press gives each edition a name, and Table 1.2 lists them for the Alice book.

| Edition | Artifact | Meaning |
|-----------------|--------------------|------------------------------------------------------|
| Print edition | `alice.pdf` | The reading PDF, typeset by LuaLaTeX in the book's profile. |
| Circulating edition | `alice.epub` | The EPUB for e-readers and retail channels. press runs epubcheck over it. |
| Single-leaf edition | `alice.html` | The whole book in one self-contained HTML file. |
| Chapter edition | `site/` and `alice-site.zip` | The reader site, one Web page per chapter. The zip archive holds the same site, boxed. |
| Manuscript edition | `alice.md` | The chapters stitched into one Markdown file. It is the raw source, and pandoc does not render it. |
| Telegraphic edition | `alice.txt` | The book as plain text, 80 columns wide. |
| Office edition | `alice.docx` | A DOCX file for word processors. |
| Source edition | `alice-source.zip` | An archive of the files Git tracks in the book repository. |

Table: Table 1.2. The editions of the Alice book

Two further artifacts gather the editions for readers. *dist/site/* is the reader site itself, with its stylesheet, chapter pages, and images. *dist/pages/* is the GitHub Pages bundle. It holds the landing page, a *read/* copy of the reader site, and a *downloads/* directory that links every published download exactly once. When the metadata sets `site-url`, the bundle also gets a *sitemap.xml* and a *robots.txt*.

A book with a *config/authorities.yaml* gets one more file, *alice-sources.md*, the table of authorities. It is a companion document published beside the book, and Chapter 10 covers it. The Alice example has no authorities file, so its *dist/* has no companion.

*The print pack* is the set of artifacts a printer needs: a print-profile interior, a cover wrap with a computed spine and an EAN-13 barcode, and the retail channel checklists. The print pack has its own targets: `press print`, `press verify-print`, and `press coverwrap`. They add *alice-interior.pdf* and *alice-coverwrap.pdf* to *dist/*. Chapter 12, *The print pack*, covers it in full.

Everything press makes on the way to *dist/* stays in *build/*. That directory holds the rendered pandoc defaults, the generated subject index, the front matter as TeX, the jargon report, and the page images that `press render` draws at 160 dpi. `press clean` deletes both *build/* and *dist/*.

The verifiers look for the same evidence in every rendered edition. A *sentinel* is a phrase from the manuscript, listed under `verify-sentinels` in *config/metadata.yaml*, that each rendered edition must contain. If a sentinel goes missing from any edition, the build stops with `sentinel ... not found`. A second setting, `verify-min-pages`, sets the fewest pages the PDF may have. The scaffold writes 1, which suits a book that is one preface long.

::: {.warning}
> **Warning:** Do not choose a sentinel from the first words of a chapter. The house chapter opening sets a drop cap that splits the first word and small-caps the rest of it. A sentinel placed there fails the exact match in the PDF.
:::

## Versions and the pinned contract

At the time of this writing, the current release is press 3.0.2, dated 2026-11-11, and every example in this book comes from it. Table 1.3 lists the majors and the patch releases since the last one.

| Release | Date | Meaning |
|-----------|---------------------------|----------------------------------------------------|
| v1.x | 2026-07-18 to 2026-07-21 | The first major ran from v1.0.0 through v1.20.0. |
| v2.0.0 | 2026-07-21 | The "composable press" added print profiles, providers, and the extension contract. |
| v3.0.0 | 2026-11-10 | A design major brought a fine-press craft pass, numbered figures with a List of Figures, the placement vocabulary, set pieces, and the Alice gallery example. |
| v3.0.1 | 2026-11-10 | A fix corrected the first note that `press migrate` prints. |
| v3.0.2 | 2026-11-11 | A security release moved Pillow to 13.0.0 in the hash lock. |

Table: Table 1.3. The majors of press and the releases since v3.0.0

A book pins a tag of press, and the tags follow the GitHub Actions convention. A *floating tag* such as `v3` moves to the latest compatible release in its major. An *immutable tag* such as `v3.0.2` names one release forever. The press repository describes that immutability as "enforced, not promised", and *the release contract*, the workflow that proves a tag, does the enforcing. It requires *the reusable workflow*, *build.yml*, at that tag to pin the toolchain image by an `@sha256:` digest. A `sha-` tag on the image does not satisfy it, because a tag can move and a digest pins bytes.

The contract covers the look of a book as well as its machinery. In the words of the press repository, "Design is part of the contract." Within a major, fixes may correct broken output, but they must not change the typography or layout of a valid book. Design and template changes require a new major. A book that pins `v3` therefore gets every fix in the third major and no change in its typography. That rule is why v3.0.0 had to be a major. Its craft pass changed the page.

Crossing a major is a deliberate act, and `press migrate` plans it. The tool once promised too much. Its plans opened with a promise of byte-for-byte geometry. That promise held from v1 to v2, and it failed from v2 to v3. Release 3.0.1 keys that first note to the target major, so a v2 book moving to v3 no longer hears that nothing on its pages will move (#262).

In CI, *the composite action*, *action.yml*, installs press from its own checkout. It never installs press with pip from Git, for two reasons. A private book then needs no token for a second repository, and the installed press matches the exact action ref. The runtime dependencies come from a hash lock, which made the Pillow fix in 3.0.2 a change to one package.[^pillow] When `printshop` builds the Alice book, it runs the pinned press in the pinned image, the same pair the release contract proved. Chapter 14, *Continuous integration and the release contract*, takes the mechanism apart.

::: {.tip}
> **Tip:** Pin `v3` to receive fixes as they come. Pin a three-part tag such as `v3.0.2` when a book must rebuild from the same press and toolchain years from now, and move that pin on purpose.
:::

## How to read this book

The chapters follow the order in which a book gets made. Chapters 2 through 8 take a book from installation to verified artifacts. They cover installation, the shape of a book repository, the manuscript, figures and plates, checking, building, and verifying. Read them in order the first time.

Chapters 9 through 13 cover the work that follows a sound manuscript: the house design, the front matter and index, the art department, the print pack, and registrations. Read them when your book needs them. Chapters 14 through 16 are for the person who runs the press. They cover continuous integration and the release contract, the operator's desk and the editorial machines, and the internals.

The appendixes are for reference. Appendix A, *Command reference*, gives every target in manual-page form, and Appendix B, *Configuration reference*, gives every key of every config file. If press stops a build with a message you do not recognize, look it up in Appendix C, *Messages and refusals*, before you read the code. Appendix D covers the toolchain platform by platform, and Appendix E is the glossary.

The Preface lists the typographic conventions. Two of them matter at once. Sessions show the `$` prompt followed by what you type, and a line that holds only `...` marks output left out. Every example hangs on the Alice book: the user `alice` on `hatter`, the CI runner `printshop`, and the repository owner `wonderland-press`. The author typed the chapter references in this book by hand, because press cross-references figures and nothing else. By the terms of the second law they are a convention, the weakest kind of guard, and you should treat them with the matching degree of trust.

Chapter 2, *Installing press*, puts the toolchain on `hatter`.

[^mark]: The press uses the pilcrow, the paragraph sign, as its mark.

[^first-commit]: The message reads "Found the press: the book pipeline with no book inside".

[^tags]: That makes thirteen tags in one day, a pace the CHANGELOG did not attempt to record.

[^vacuous]: In CI the Lua filter tests skipped silently until the variable `PRESS_REQUIRE_LUA=1` forbade the skip. The backfill that followed found a title-tie test that passed with no filter at all, because pandoc ties `Mr.` itself.

[^pillow]: The bump from Pillow 12.3.0 to 13.0.0 closed 41 advisories against the lock, five of them critical. Pillow 13 needs Python 3.11, so an install on Python 3.10 still resolves Pillow 12.x.

<!-- index: press; book repository; manuscript; target; press check; checker; verifier; registry; four laws; scar; generator; toolchain; toolchain image; profile; edition; artifact; dist directory; build directory; known-bad fixture; sentinel; verify-min-pages; print pack; floating tag; immutable tag; release contract -->
