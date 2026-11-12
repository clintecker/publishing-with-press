# Building the editions

::: {.in-this-chapter}
> **In this chapter:**
>
> - Targets
> - What pandoc is told
> - The filter chain
> - The PDF through latexmk
> - The EPUB
> - The single-file HTML and the reader site
> - The portable editions
> - The registry and the order of work
> - What press all does, in order
> - Rendering, counting, and cleaning
:::

A checked manuscript is still only a directory of Markdown files. This chapter follows the Alice book from that directory to a full *dist/*, one *edition*, or published form of the book, at a time. It names the program that does each piece of the work, the files press writes along the way, and the order in which press runs them. The last sections explain the registry, which decides that order, and the single command that runs all of it.

## Targets

A *target* is a `press` command that builds, checks, or verifies something. Chapter 6, *Checking the manuscript*, covered the targets that read the manuscript. The targets in this chapter write files. Each one has a fixed name, a fixed mechanism, and a fixed place for its result, and none of the three is yours to configure. You decide the title, the author, the words, and the aesthetic. The press decides the build order, the verifiers, the filenames, and the editions.

Table 7.1 lists the build targets in the order the press lists them. The slug is the `slug` field from *config/metadata.yaml*, so for the Alice book every `<slug>` below reads `alice`.

| Target | Result | Meaning |
|------------------------|------------------------------|------------------------------------------------------|
| `press pdf` | *dist/alice.pdf* | Pandoc writes LaTeX with the `pdf.yaml` defaults, and latexmk runs LuaLaTeX over it. This is the reading PDF. |
| `press epub` | *dist/alice.epub* | Pandoc writes the EPUB directly with the `epub.yaml` defaults. |
| `press html` | *dist/alice.html* | Pandoc writes one self-contained HTML file with the `html.yaml` defaults. A second pass then labels the table cells. |
| `press markdown` | *dist/alice.md* | Press writes a header and the stitched raw manuscript, with heading attribute blocks removed. Pandoc takes no part. |
| `press site` | *dist/site/* and *dist/alice-site.zip* | Pandoc writes chunked HTML with the `chunked.yaml` defaults. Press then adds the reader CSS, the assets, and the reader metadata, and zips the result. |
| `press txt` | *dist/alice.txt* | Pandoc writes plain text at 80 columns with the `portable.yaml` defaults. |
| `press docx` | *dist/alice.docx* | Pandoc writes a Word file with the `portable.yaml` defaults. |
| `press source` | *dist/alice-source.zip* | Press packs the files that Git tracks into a zip, or the whole book when it sits outside any Git repository. Pandoc takes no part. |
| `press pages` | *dist/pages/* | Press assembles the landing page, the reader, the downloads, and the sitemap, and then verifies the result. |
| `press print` | *dist/alice-interior.pdf* | Pandoc and latexmk build the two-sided print interior with the `print.yaml` defaults and print-safe images. |
| `press coverwrap` | *dist/alice-coverwrap.pdf* | Press builds the print interior, generates the cover wrap, runs latexmk on it, and verifies it. |
| `press render` | *build/rendered-book/* | Press builds the PDF and turns every page into a PNG. |
| `press all` | every published artifact and *dist/pages/* | Press checks the manuscript, builds every edition, assembles the pages, and runs every verifier for them. |
| `press clean` | nothing | Press deletes *build/* and *dist/*. |

Table: Table 7.1. The build targets

The rest of this chapter calls the PDF, the EPUB, the single-file HTML, and the reader site by their formats, as the targets do. It uses the press's names for the Manuscript, Telegraphic, Office, and Source editions.

Every target in the table that calls pandoc needs it on your `PATH`. If pandoc is missing, the press refuses the build at once with the message `pandoc is required`. Chapter 2, *Installing press*, describes how to install it.

The build targets take no options. Each one accepts `--help` and `-h`, and nothing more. You cannot pass an option through to pandoc, because no target has a passthrough. The press does hand pandoc extra arguments of its own for some editions, such as the EPUB rights line. Those arguments are internal, and no option of yours changes them.

The targets are not independent, because some *artifacts*, the files and directories in *dist/* that the registry names, need others before they can exist. The Pages bundle needs every other published artifact, and the cover wrap needs the print interior. @fig:build-graph shows these edges for every artifact. The section "The registry and the order of work" later in this chapter explains where the edges come from and why the press refuses to skip them.

![The artifact graph the registry declares](assets/woodcuts/07-01-build-graph.png){#fig:build-graph .diagram width=full-measure fig-alt="A graph of twelve boxes. Nine artifacts, from pdf to sources, each send one arrow into a pages box at the right, markdown also feeds sources, and a separate bottom row joins print to coverwrap."}

<!-- art: ARCHETYPE pipeline, left to right. Left column, top to bottom, square boxes in small monospace: "pdf", "epub", "html", "markdown", "txt", "docx", "site", "source". Beside "markdown", a box "sources", with one arrow from "markdown" into it. At far right, a larger box "pages" with a 2 pt offset shadow. Nine arrows enter "pages", one from each of the nine boxes. Below a thin horizontal rule, a second row: "print", an arrow, "coverwrap", with small italic sans beneath: "not built by press all". No other arrows. The reader should see first the nine arrows converging on pages, then that the bottom row stands apart. -->

## What pandoc is told

Every edition except the Manuscript edition and the Source edition comes out of pandoc. The press builds a pandoc command line for each one, always in the same shape, and runs it from the root of the book repository. It prints each command before it runs it, with a plus sign and a space in front.

The captures in this chapter come from the press's own three-chapter Alice example, which lives under *examples/alice-in-wonderland* in a press checkout. The Alice book itself, the full novel, lives in *\~/alice* on `hatter`. The captures print the example's directory as *\~/alice* too, so that their paths match the rest of the chapter. Example 7.1 shows the line for the single-file HTML.

**Example 7.1. The pandoc command for the single-file HTML**

```text
+ pandoc --defaults=~/alice/build/defaults/html.yaml \
    book/chapters/01-down-the-rabbit-hole.md \
    book/chapters/02-the-pool-of-tears.md \
    book/chapters/03-a-caucus-race-and-a-long-tale.md \
    book/appendices/z-about-this-edition.md \
    --output dist/alice.html
```

The command has four parts. The `--defaults` option names a rendered defaults file. Extra arguments of the press's own come next, and the HTML command has none. The input files follow in book order: the chapter files, then the appendix files sorted by letter. The press sorts any generated appendix, such as the subject index, among them, and the Alice command carries no generated file. The last part names the file that pandoc writes.

The echo has a practical use. If pandoc refuses the manuscript, you can copy the command from the log and run it yourself from the book root, outside the press, with the same inputs. The echo does not quote values that contain spaces, however. The EPUB command passes its rights line bare, so put quotes around that value before you paste the EPUB command into a shell.

When a pandoc run takes one second or more, the press prints the time on the next line, indented two spaces. On one run of the three-chapter example on `hatter`, only the PDF reached that mark, and the line read `pandoc took 26.7s`. Treat the number as one run on one machine, not as a guide to your own book.

### The defaults files

Pandoc reads most of its settings from a *defaults file*, a YAML file that holds the same settings you could give on the command line. The defaults files come with the press. The installed package carries one for each family of editions in its *data/defaults/* directory: `pdf.yaml`, `epub.yaml`, `html.yaml`, `chunked.yaml`, `portable.yaml`, and `print.yaml`. In the press repository, that directory is *src/press/data/defaults/*. The Telegraphic and Office editions share `portable.yaml`.

A defaults file also names the Lua filters that pandoc runs over the manuscript, in order. The six files declare three different chains. The PDF, EPUB, HTML, and chunked defaults share one chain of five filters. The print defaults add a sixth filter, `print-safe-images`, in the middle of that chain. The portable defaults keep only three of the five. @fig:filter-chain sets the three chains side by side, and Table 7.3 in the next section describes each filter.

![The Lua filter chain for each family of editions](assets/woodcuts/07-02-filter-chain.png){#fig:filter-chain .diagram width=full-measure fig-alt="Three vertical stacks of filter names. The first has five filters, the print stack adds print-safe-images in the middle, and the portable stack has only typographic-spacing, set-pieces, and figure-numbering."}

<!-- art: ARCHETYPE layered stack, three columns side by side, each a vertical stack of equal horizontal bands, labels centered in small monospace, alternating 10 and 20 percent gray. Headings in small sans: "pdf, epub, html, chunked", "print", "portable (txt, docx)". First column, top to bottom: typographic-spacing, set-pieces, chapter-dropcap, scene-break, figure-numbering. Second column: typographic-spacing, set-pieces, print-safe-images (in 40 percent gray), chapter-dropcap, scene-break, figure-numbering. Third column: typographic-spacing, set-pieces, figure-numbering. Same-named bands line up across columns where they can. A small downward arrow at the left of the first column, labeled "pandoc runs in this order". The reader should see first that print-safe-images appears in one column only. -->

### Templating the defaults

The defaults files in the package cannot name absolute paths, because the press does not know where you installed it or where your book repository is. Instead, they name paths with two prefixes. A path that starts with `@press/` points into the package's own *data/* directory, where the TeX header and the filters live. A path that starts with `@book/` points into the book repository. A path that ends in `?optional` names a file that a book repository can leave out.

Example 7.2 shows part of the package's `pdf.yaml`. It names latexmk as the PDF engine, five filters from the package, and a list of TeX files for the header, most of them optional.

**Example 7.2. Part of the pdf.yaml template**

```text
toc-depth: 1
pdf-engine: latexmk
pdf-engine-opts:
  - -lualatex
metadata-file: "@book/config/metadata.yaml"
filters:
  - "@press/lua/typographic-spacing.lua"
  ...
include-in-header:
  - "@press/tex/book-header.tex"
  - "@book/build/profile-geometry.tex?optional"
  - "@book/build/profile-dropcap.tex?optional"
  - "@book/build/aesthetic.tex?optional"
  - "@book/build/front-matter.tex?optional"
  - "@book/tex/title-page.tex?optional"
```

Before each pandoc run, the press renders the defaults file. It replaces each prefix with a real directory and checks that every named file exists. If an optional file is absent, the press drops that entry from the rendered copy. If any other file is absent, the press refuses the build with the message `defaults reference a missing file`. The press writes the rendered copies to *build/defaults/*, one per defaults file, and the pandoc command names that copy.

@fig:defaults-templating shows three lines of the template before and after this step. The three-chapter example supplies no *tex/title-page.tex*, so its entry is the one that disappears.

![A defaults file before and after rendering](assets/woodcuts/07-03-defaults-templating.png){#fig:defaults-templating .diagram width=full-measure fig-alt="Two file boxes. The template holds prefixed paths and one optional entry, and the rendered copy holds absolute paths with the optional entry struck out."}

<!-- art: ARCHETYPE before/after, two frames side by side, labeled (a) and (b) beneath. Each is a dog-eared file box holding three lines in small monospace. (a), headed "src/press/data/defaults/pdf.yaml": line 1 metadata-file: "@book/config/metadata.yaml". Line 2 - "@press/tex/book-header.tex". Line 3 - "@book/tex/title-page.tex?optional", with a small italic callout "file absent". (b), headed "build/defaults/pdf.yaml": line 1 metadata-file: ~/alice/config/metadata.yaml. Line 2 - .../press/data/tex/book-header.tex. Line 3 struck through in 40 percent gray, callout "dropped". One thin arrow from (a) to (b), labeled "render_defaults". The reader should see first that line 3 has gone from (b). -->

The rendered copy carries more than resolved paths. Example 7.3 shows the end of the rendered *build/defaults/pdf.yaml* for the three-chapter example, after `press pdf`. The press adds `lof: true` to the variables, because *assets/woodcuts/* holds files. It also adds a `metadata:` block of four values, which the next section explains.

**Example 7.3. The end of the rendered pdf.yaml**

```text
include-in-header:
- .../press/data/tex/book-header.tex
- ~/alice/build/profile-geometry.tex
- ~/alice/build/profile-dropcap.tex
- ~/alice/build/aesthetic.tex
- ~/alice/build/front-matter.tex
variables:
  ...
  lof: true
metadata:
  chapter-opening-style: drop-cap
  chapter-opening-lines: 3
  chapter-opening-smallcaps: 'true'
  scene-break-ornament: fairy-dust
```

The rendered copies are worth reading when a build goes wrong. They show exactly what pandoc saw, with every path resolved. If you suspect that pandoc read the wrong header, open the matching file in *build/defaults/* before you look anywhere else.

### Environment and metadata

The press also sets three environment variables for the build, and Table 7.2 lists them.

| Variable | Meaning |
|------------------------------|---------------------------------------------------------|
| `SOURCE_DATE_EPOCH` | The press sets this to `1784160000` unless you already set it yourself.[^7-epoch] |
| `BOOK_ROOT` | The press sets this to the root of the book repository. |
| `BOOK_PUBLISHER` | The press sets this to the book's publisher. The fallback title page reads it. |

Table: Table 7.2. Environment variables the press sets for a build

Of the three, `SOURCE_DATE_EPOCH` is the one you can set. If you export your own value before a build, the press keeps it and does not substitute its default. The other two come from the book repository and its configuration.

The four values in the `metadata:` block of Example 7.3 are `chapter-opening-style`, `chapter-opening-lines`, `chapter-opening-smallcaps`, and `scene-break-ornament`. They carry the book's choices for the chapter opening and the scene break from its configuration into the filters. In the three-chapter example, the chapter opening is a three-line drop cap in small capitals, and the scene break is the fairy-dust ornament. Chapter 4, *Writing the manuscript*, describes what the two features look like on the page.

[^7-epoch]: The value falls on 2026-07-16.

## The filter chain

A Lua filter is a small program that pandoc runs over the document after it reads the Markdown and before it writes the edition. The filter sees the document as a tree of headings, paragraphs, images, and spans, and it can change any part of the tree. Much of the press's fine typesetting happens in filters. A filter in a shared chain acts on every edition that runs that chain. Pandoc runs the filters in the order that the defaults file lists them, so a filter sees the document as the filters before it left it.

Table 7.3 describes the filters in chain order and then the shared helper file. Chapter 4 covers the set pieces (the cascade, the verse, and the tail), the chapter openings, and the scene breaks from the author's side. Chapter 5, *Figures, plates, and illustrations*, covers placements and cross-references.

| Filter | Meaning |
|--------------------------------|------------------------------------------------------|
| `typographic-spacing.lua` | This filter puts non-breaking spaces after titles, reference forms, and initials. |
| `set-pieces.lua` | This filter sets the cascade, the verse, and the tail. |
| `print-safe-images.lua` | In print only, this filter points every `assets/` image path at the flattened white-ground copy under *build/print-assets/assets/*. |
| `chapter-dropcap.lua` | This filter splits a chapter's first paragraph into the lead, the initial, the rest of the first word, and the rest of the text. It sets the chapter opening in the PDF and the HTML. |
| `scene-break.lua` | This filter turns a thematic break into a rule, an asterism, or the fairy-dust ornament. |
| `figure-numbering.lua` | This filter numbers the informative figures, writes their captions, lays out wraps, leaves, and frontispieces, and resolves `@id` cross-references. |
| `press-util.lua` | This file holds shared helpers that the other filters use. |

Table: Table 7.3. The Lua filters in chain order

In every chain, typographic spacing runs first and figure numbering runs last. In the print chain, the print-safe filter sits after the set pieces and before the chapter opening. The filters after it therefore see images that already point at the print copies.

### What figure numbering does

The last filter in the chain does the most work that a reader can see. It numbers each informative figure by chapter and sequence, so the first figure in this chapter is 7.1. In the PDF, it sets the label in bold ahead of the caption and adds an entry to the List of Figures. It also removes the press's own image attributes, so `place`, `outset`, `fig-alt`, and `decorative` never leak into the HTML as `data-*` attributes.

The filter also locks each label together as one unit, so a narrow column beside a wrapped figure can never hyphenate the word into "Fig-ure". The filters have tests of their own in CI.[^7-lua] Chapter 16, *Inside the press*, describes them.

[^7-lua]: At the time of this writing, CI requires those tests to run from version 3.0.2 on and holds a coverage floor for each filter.

## The PDF through latexmk

The reading PDF takes more preparation than the other reading editions. Before pandoc runs, the press does six things, in a fixed order:

1. It writes *build/profile-dropcap.tex*, the chapter-opening settings.
2. It sets pandoc's `lof` variable if *assets/woodcuts/* holds any files.
3. It generates *build/front-matter.tex*, the front matter.
4. It writes *build/aesthetic.tex*, the book's aesthetic.
5. It writes *build/profile-geometry.tex*, the page geometry of the design profile.
6. For the print interior only, it writes the flattened images to *build/print-assets/*.

Example 7.3 shows the results of four of these steps as entries in the rendered defaults, and step 2 as `lof: true`. Chapter 9, *The house design*, describes what the profile and aesthetic files contain. Chapter 10, *Front matter, the index, and the table of authorities*, describes the front matter. The press generates each of these files on every build. None of them is a file you edit, and none of them survives `press clean`.

Pandoc then writes the LaTeX and hands it to latexmk(1), the PDF engine that Example 7.2 names. The latexmk program runs LuaLaTeX with the `-lualatex` option, as many times as the document needs. The sidebar explains why the press does not let pandoc run LuaLaTeX itself.

::: {.sidebar}
> **The lists that would not converge**
>
> Plain LuaLaTeX under pandoc does not run enough passes for a book. A book's table of contents, List of Figures, and List of Plates each take more than one pass to settle. With too few passes, the lists did not converge. The press therefore builds every PDF through latexmk.
>
> A second trap sat in the same lists. The `pdf.yaml` defaults ask for `toc-depth: 1`, a table of contents that lists chapters only. That setting sets the TeX tocdepth counter to 0, and at that depth the List of Plates comes out empty, with no error to say so. The house TeX header now raises the depth inside the list file itself, so a shallow table of contents can no longer empty the List of Plates.
:::

The print interior follows the same road with different defaults. `press print` uses `print.yaml`, sets the page two-sided, and adds the print-safe filter to the chain. Chapter 12, *The print pack*, covers it in full. The registry treats the print interior and the cover wrap as a branch of their own, which @fig:build-graph draws in its bottom row.

## The EPUB

Pandoc writes the EPUB directly, with no second program. The press adds two arguments of its own to the command, and both show in the echo line from the three-chapter example:

```text
+ pandoc --defaults=~/alice/build/defaults/epub.yaml \
    --metadata rights=The text and illustrations ... \
    --epub-metadata=~/alice/build/epub-metadata.xml \
    book/chapters/01-down-the-rabbit-hole.md ... \
    --output dist/alice.epub
```

The first argument is the rights line. The press builds it in the form `<copyright> Published by <publisher>, <place>.`, from the book's `copyright` and `publisher` fields and its place of publication. Chapter 3, *The shape of a book repository*, lists those fields. For the three-chapter example, the whole value reads "The text and illustrations are in the public domain. Published by The Press (gallery example), Oxford." The echo prints it without quotes, which is why a pasted EPUB command needs them added.

If the book has an ISBN registered for its EPUB, the press also passes `identifier=urn:isbn:` followed by that number. Chapter 13, *Registrations*, explains how a book gets one.

The second argument, `--epub-metadata`, names a small XML file, *build/epub-metadata.xml*, that carries one element:

```text
<dc:date>YEAR</dc:date>
```

The press writes the year from the book's date into that element. The file exists because pandoc writes an empty `dc:date` element, and epubcheck rejects an EPUB with an empty date.[^7-rsc] In the words of the press's architecture notes, epubcheck is "the tool retail channels run," so the press writes the date itself.

If the book supplies *assets/cover.jpg*, the press names it as the `epub-cover-image`. Chapter 11, *The art department*, explains how a book gets its cover.

[^7-rsc]: epubcheck reports the problem under the code RSC-005. If an EPUB that you built some other way fails with that code, an empty date is the first thing to look for.

## The single-file HTML and the reader site

The press builds two HTML editions, and they serve different readers. The single-file HTML is one page that holds the whole book. The reader site is a small Web site with one page per chapter. The reader site uses the house reader stylesheet, which Chapter 9 describes.

### The single-file HTML

`press html` runs pandoc with the `html.yaml` defaults and the `self-contained` setting. Pandoc then embeds every image and stylesheet in the one file, so *dist/alice.html* has no companion directory. You can send it by e-mail or copy it to another machine, and it still shows its figures. After pandoc finishes, the press runs one more pass over the file to add labels to the table cells.

### The reader site

`press site` runs pandoc with the `chunked.yaml` defaults and `--to=chunkedhtml`. The chunked writer splits the book into one HTML page per chapter, because the defaults set `split-level: 1`. Pandoc writes the pages into *dist/site/* with an *index.html* at the top. The press then does four more things to the directory:

1. It adds *reader.css*, the reader stylesheet.
2. It copies the book's assets in, and re-saves each JPEG at quality 70.
3. It adds the reader metadata.
4. It zips the whole directory into *dist/alice-site.zip*.

The re-save touches only the copies in *dist/site/*. The images in your book repository keep their full quality.

The asset step carries a scar from the first book. Pandoc's chunked writer copies the media that the pages reference into the output directory on its own. Some directories therefore already exist when the press copies the assets in. The press now writes into directories that already exist, where it once stopped.

The reader site is also the `read/` directory of the Pages bundle. `press pages` copies *dist/site/* into *dist/pages/read/*, as Example 7.5 later in this chapter shows.

## The portable editions

The press builds three editions for readers who need something other than a typeset book: the Manuscript edition (the stitched Markdown), the Telegraphic edition (plain text), and the Office edition (DOCX). It also packs the book repository itself into the Source edition, a zip of the files that Git tracks. Each of the four carries less of the house design than the PDF, the EPUB, or the HTML.

### The Manuscript edition

`press markdown` is one of two edition targets that do not call pandoc, and the Source edition is the other. The press writes a short header and then the raw manuscript. It stitches every chapter and appendix together in book order. It removes the attribute blocks from the headings, such as `{.unnumbered}`, and changes nothing else. In the log, the step reports itself with a plus-sign line that is not a command: `+ stitched 4 files -> dist/alice.md`.

### The Telegraphic and Office editions

`press txt` runs pandoc with `--to=plain` and `--columns=80`, and writes *dist/alice.txt*. `press docx` runs pandoc with `--to=docx`, and writes *dist/alice.docx*. Both use the `portable.yaml` defaults and the shorter filter chain from @fig:filter-chain. That chain runs typographic spacing, the set pieces, and figure numbering. It does not run the chapter-opening filter or the scene-break filter.

### The Source edition

`press source` writes *dist/alice-source.zip* through the `package_source` module. The zip holds the files that Git tracks in the book repository, and only those. If the book sits outside any Git repository, the press archives all of it. If the book sits untracked inside a parent repository, the press archives nothing. The step prints the path of the zip and then one line of report. For the three-chapter example, that line reads `archived 12 files; excluded dirs ['.git', '__pycache__', 'build', 'dist']`.

::: {.tip}
> **Tip:** We suggest that you add each new chapter file to Git before you build the Source edition. A file that Git does not track stays out of the zip.
:::

## The registry and the order of work

Every artifact that the press can build has one entry in *the registry*, the one statement of the artifact graph. The registry lives in *src/press/registry.py* in the press repository. The entry names the artifact's files, the artifacts it needs first, and whether the press publishes it. The press generates the artifact table in its *docs/REFERENCE.md* from the registry, so the documentation and the code state the same facts. Table 7.4 reproduces that table exactly, cell for cell.

| artifact | outputs | prerequisites | published |
|----------------|--------------------------|------------------------------------------------------------|---------------------------------|
| pdf | {slug}.pdf | - | yes |
| epub | {slug}.epub | - | yes |
| html | {slug}.html | - | yes |
| markdown | {slug}.md | - | yes |
| txt | {slug}.txt | - | yes |
| docx | {slug}.docx | - | yes |
| site | site, {slug}-site.zip | - | yes |
| source | {slug}-source.zip | - | yes |
| sources | {slug}-sources.md | markdown | yes (when authorities configured) |
| pages | pages | pdf, epub, html, markdown, txt, docx, site, source, sources | no |
| print | {slug}-interior.pdf | - | no |
| coverwrap | {slug}-coverwrap.pdf | print | no |

Table: Table 7.4. The registry's artifact table, from docs/REFERENCE.md

Read the prerequisites column against @fig:build-graph, and notice two things: the Pages bundle waits on nine artifacts, and the print branch stands apart from all of them.

The registry marks both the Pages bundle and the print pack "no" in the published column, for different reasons. The Pages bundle, *dist/pages/*, becomes the Pages site, the Web site that GitHub Pages serves. The Pages site holds the downloads, so the bundle is never a download itself. The print pack goes to the GitHub Release when you build it, as Table 7.5 shows. A GitHub Release is the set of files that GitHub keeps beside a tagged version of the book repository. Chapter 14, *Continuous integration and the release contract*, covers the Pages site and the release.

The same reference file holds a second table, which Table 7.5 reproduces exactly. It names the code that builds each artifact, the verifier that inspects it, and where the artifact goes when the press publishes the book.

| artifact | builder | verifier | publication destination |
|----------------|----------------------------|----------------------------------|------------------------------------------------------|
| pdf | build (pandoc + latexmk) | verify_pdf | Pages downloads + GitHub Release |
| epub | build | verify_formats + epubcheck | Pages downloads + GitHub Release |
| html | build | verify_formats | Pages downloads + GitHub Release |
| markdown | build | verify_formats | Pages downloads + GitHub Release |
| txt | build | verify_formats | Pages downloads + GitHub Release |
| docx | build | verify_formats | Pages downloads + GitHub Release |
| site | build | verify_formats + verify_archives | Pages downloads + GitHub Release |
| source | package_source | verify_archives | Pages downloads + GitHub Release |
| sources | gen_authorities | verify_archives | Pages downloads + GitHub Release (when authorities configured) |
| pages | build | verify_pages | deployed as the Pages site |
| print | build (print profile) | verify_pdf (print profile) | GitHub Release when built (print pack) |
| coverwrap | gen_coverwrap | verify_coverwrap | GitHub Release when built (print pack) |

Table: Table 7.5. Builders, verifiers, and destinations, from docs/REFERENCE.md

### No stale artifact

The prerequisite edges exist because a verifier that reads *dist/* but does not rebuild it can bless an artifact that no longer matches the manuscript. Suppose `alice` fixes a sentence in her second chapter and then runs a verifier over last week's PDF. The verifier finds nothing wrong, because last week's PDF was fine. The fix never reached the file, and a green result now covers a stale book. Every verify target rebuilds the artifacts it verifies before it verifies them (one exception, Chapter 8), and the command line offers no way around that.

The press records this as an *invariant*, an entry in its ledger of guarded behavior, under the name `INV-graph-no-stale` at the critical level. The ledger also states its limit: the invariant holds on the command-line path only. Code that imports a verifier module directly skips the rebuild.

### Which target rebuilds what

Each verify target names its own rebuilds, and the list is short. `press verify` builds the PDF and then runs the PDF verifier. `press verify-formats` builds the EPUB, the HTML, the Manuscript, Telegraphic, and Office editions, the reader site, and the Source edition, and then runs the format and archive verifiers. `press pages` asks the registry for the Pages bundle. The registry builds all nine prerequisites, assembles the bundle, and runs the page verifier. The press also accepts `press verify-pages` as another name for `press pages`.

The print branch of the registry has targets of its own. `press verify-print` builds the print interior and runs the PDF verifier with the print profile. If *assets/cover.jpg* exists, it then builds the cover wrap and runs the cover-wrap verifier. Without a cover, it stops after the interior and says so.

`press coverwrap` builds the print interior, then the cover wrap, and then runs the cover-wrap verifier. Chapter 8, *Verifying the artifacts*, describes what each verifier inspects.

### Generated inputs

Some of the files that pandoc reads are not in your manuscript. Before every pandoc build, the press calls the same function to generate them again. That function does three things in order:

1. It deletes *build/generated/*.
2. It generates the subject index again.
3. If the book has *config/authorities.yaml*, it writes *dist/alice-sources.md* from that ledger.

In the words of the press's architecture notes, "the generated appendices are cleaned first so stale copies cannot survive." An index file left over from an earlier build cannot slip into a new edition, because no earlier copy exists when pandoc runs.

The third step produces the sources companion, the one artifact in Table 7.4 that waits on the Manuscript edition. It is a standalone document of the claims in the book and the sources that warrant them. The press publishes it beside the book. The three-chapter example has no ledger, so it gets no companion. Chapter 10 describes the ledger and what the companion contains.

## What press all does, in order

`press all` runs the checker, the edition targets, and the verifiers for the published artifacts, in six steps. @fig:press-all-sequence draws the sequence as a state machine. Example 7.4 shows one real run on the three-chapter example on `hatter`, with long lines cut short.

![The press all sequence](assets/woodcuts/07-04-press-all-sequence.png){#fig:press-all-sequence .diagram width=full-measure fig-alt="A row of six states from check to the commerce gate, each joined to the next by a pass arc, with a fail arc from every state down to a single stop box."}

<!-- art: ARCHETYPE state machine, left to right. A filled start dot, then six circles in a row, each labeled in small monospace: "check", "formats", "source", "pages", "verify", "commerce gate". An arc labeled "pass" in small italic joins each circle to the next, and a last "pass" arc ends in a double circle "done". Below the row, one square box "stop", with a 2 pt offset shadow. From each of the first five circles, a thin arc labeled "fail" curves down into "stop". From "commerce gate", the arc is labeled "fail, under PRESS_RELEASE". In small sans under "check": "source, self-test, style, jargon". Under "verify": "pages, pdf, formats, archives". Under "commerce gate": "advisory unless PRESS_RELEASE, absent without ordering". The reader should see first that every state has its own way down to stop. -->

**Example 7.4. A press all run on the three-chapter example**

```text
$ press all
Source checks passed: 4 ordered Markdown files
...
Checker self-test passed: 19 known-bad fixtures each ...
Editorial checks passed: 4 Markdown files
Jargon check passed: no rewrite-status terms ...
  ¶ check      ✓ style, source, jargon
+ pandoc --defaults=~/alice/build/defaults/pdf.yaml ...
  pandoc took 26.7s
+ pandoc --defaults=~/alice/build/defaults/epub.yaml ...
+ pandoc --defaults=~/alice/build/defaults/html.yaml ...
+ stitched 4 files -> dist/alice.md
+ pandoc --defaults=~/alice/build/defaults/portable.yaml ...
+ pandoc --defaults=~/alice/build/defaults/portable.yaml ...
+ pandoc --defaults=~/alice/build/defaults/chunked.yaml ...
~/alice/dist/alice-source.zip
archived 12 files; excluded dirs ['.git', ...]
+ assembled pages site -> dist/pages
  ¶ typeset    ✓ PDF · EPUB · web · text · DOCX
Verified dist/pages: every local reference resolves ...
Verified alice.pdf: 23 pages, 6 x 9 trim, embedded fonts, ...
...
Verified archives: alice-site.zip, alice-source.zip
  ¶ verify     ✓ 7 editions match source
commerce release gate: print ordering is not enabled; ...

  press. your book is ready → dist/
```

Walk the six steps against the example:

1. The check step runs the four passes of the checker in order: the source checks, the self-test against the known-bad fixtures, the style audit, and the jargon lint. Each pass reports one line, and the step ends with the `check` phase line. The checker stops at the first pass that refuses the manuscript.
2. The formats step builds the editions in this order: the PDF, the EPUB, the single-file HTML, the Manuscript edition, the Telegraphic edition, the Office edition, and the reader site. Each pandoc edition has its plus-sign command line, and the Manuscript edition has its `stitched` report.
3. The source step builds the Source edition and prints its path and its `archived` report.
4. The pages step assembles *dist/pages/*, reports it with `assembled pages site`, and then prints the `typeset` phase line for the whole build.
5. The verify step runs the page, PDF, format, and archive verifiers in that order. Each prints one `Verified` line, and the step ends with the `verify` phase line.
6. The commerce gate runs last.

The known-bad fixtures run in `press check` and `press all`, and not in a bare `press pdf`. Under `press all`, a manuscript that the checker refuses never reaches pandoc.

The elided lines in the verify step include a warning on any machine without epubcheck. On `hatter`, the run says that it validated the EPUB "structurally only" and that the toolchain image runs the full check in CI. Chapter 8 explains what that difference costs.

### The commerce gate

The commerce gate concerns print ordering, the optional feature that puts an "Order a print copy" link on the book's landing page. Print ordering is off by default, and Chapter 12 describes it. The three-chapter example does not enable it, so its gate has nothing to check and says so in the last line before the closing:

```text
commerce release gate: print ordering is not enabled; no
commerce release gate
```

A book that enables print ordering gets the gate. On an ordinary run on `hatter`, the gate is advisory. It reports what it finds, does not stop the run, and prints this line:

```text
(commerce gate is advisory here; a release build
(PRESS_RELEASE=1) enforces it)
```

When the release build sets `PRESS_RELEASE=1`, the gate enforces its findings and the press refuses the run on a finding. Chapter 14 describes the release build that sets it.

### What press all leaves out

An ordinary `press all` does not build the print interior, and it does not build the cover wrap. The print pack is a separate branch of the registry with its own targets, as @fig:build-graph shows. To build it, run `press print`, `press verify-print`, or `press coverwrap`, which Chapter 12, *The print pack*, describes. The one exception is the commerce gate in a book that enables print ordering, which does build them. `press all` also does not run `press render`.

::: {.warning}
> **Warning:** Do not take a green `press all` as proof that the print pack is ready. Run `press verify-print` before you send anything to a printer.
:::

### Reading the log

The press marks its own lines in the log with a few fixed forms, and Example 7.4 shows each of them. A line that starts with a plus sign and a space marks a step that the press runs. For pandoc, the line is the full command. For a step that does not call pandoc, the line is a short report, such as `+ stitched 4 files -> dist/alice.md` or `+ assembled pages site -> dist/pages`. Only the pandoc lines are commands that you can copy and run.

A time line, indented two spaces, follows any pandoc run of one second or more, as `pandoc took 26.7s` does in Example 7.4. When a target times more than one step, the registry also prints a summary line that starts with `press timings:`. The run on the three-chapter example timed only the PDF, so it printed no summary.

The three phase lines start with a pilcrow, the paragraph sign, followed by the phase name: check, typeset, or verify. They appear in every run in your own terminal. The desk reads the same stream, and it uses the phase lines, the plus-sign lines, and the time lines to show its progress. Chapter 15, *The operator's desk and the editorial machines*, describes how the desk shows them. The run's last line begins `press. your book is ready`.

The jargon lint and the PDF verifier leave reports in *build/* for you to read. The lint writes its full audit to *build/jargon-report.txt*. The PDF verifier writes *build/verify-text.txt*. When the lint refuses the book or the PDF verifier fails it, open the matching file.

### What the build leaves behind

After `press all`, the *dist/* directory of the Alice book holds every published artifact under the names from the registry. Example 7.5 shows the directory, with the role of each file in a comment.

**Example 7.5. The dist directory after press all**

```text
dist/
    alice.pdf           # the reading PDF
    alice.epub          # the EPUB
    alice.html          # the single-file HTML
    alice.md            # the stitched raw manuscript
    alice.txt           # plain text at 80 columns
    alice.docx          # the Office edition
    alice-site.zip      # the reader site, zipped
    alice-source.zip    # the Source edition
    site/               # the per-chapter reader
    pages/              # the Pages bundle
        index.html      # the landing page
        read/           # a copy of dist/site
        downloads/      # every published download, once
        ...
```

A book with *config/authorities.yaml* also gets *alice-sources.md* at the top of *dist/*. The Pages bundle takes the cover, the logomark, and the plates when the book has them, and a *sitemap.xml* and *robots.txt* when the book sets `site-url`. The print pack adds *dist/alice-interior.pdf* and *dist/alice-coverwrap.pdf* when you build it. The registration targets add files of their own, which Chapter 13 describes.

The *build/* directory holds the intermediate files that the targets write on the way to *dist/*. Most of them appear earlier in this chapter: the rendered defaults, the generated index in *build/generated/*, and the TeX files from the PDF build. It also holds *build/print-assets/*, *build/epub-metadata.xml*, *build/cover-fragment.html*, and the two report files. Nothing in *build/* is a source file, and `press clean` deletes all of it.

## Rendering, counting, and cleaning

Three targets produce no edition. `press render` shows you the pages, `press wordcount` counts the words, and `press clean` throws *build/* and *dist/* away.

### Rendering the pages

`press render` builds the PDF and then runs pdftoppm(1) over it with the options `-png -r 160`. The result is one PNG for each page, at 160 dots per inch, in *build/rendered-book/*. The files match the pattern *page-\*.png*. Because the target builds the PDF first, the images always show the current manuscript. Use them to examine the book a page at a time, at a fixed resolution.

### Counting the words

`press wordcount` counts the words in the manuscript, file by file, and ends with a total. On the three-chapter example, it prints one line per file:

```text
$ press wordcount
  2160  book/chapters/01-down-the-rabbit-hole.md
  2136  book/chapters/02-the-pool-of-tears.md
  1721  book/chapters/03-a-caucus-race-and-a-long-tale.md
   228  book/appendices/z-about-this-edition.md
  6245  TOTAL
```

The count strips fenced code blocks and inline code before it counts. It does not strip HTML comments, so the `art:` comment beside every figure counts toward the total.[^7-wordcount] If you write to a fixed length, remember that your `art:` comments are in the number.

[^7-wordcount]: The counter matches words with the pattern `\b[\w'-]+\b`, so a hyphenated compound or a contraction counts as one word.

### Cleaning up

`press clean` deletes *build/* and *dist/*, and nothing else. Your manuscript, your configuration, and your assets stay where they are. Because every target rebuilds what it needs, the next build after a clean starts from nothing and writes everything again. The next chapter, Chapter 8, *Verifying the artifacts*, opens those artifacts and inspects each one.
