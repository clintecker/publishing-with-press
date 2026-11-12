# Verifying the artifacts

::: {.in-this-chapter}
> **In this chapter:**
>
> - Artifacts as objects
> - What the PDF verifier checks
> - What the formats verifier checks
> - epubcheck
> - Archives and the Source edition
> - The pages verifier
> - Witnesses and cross-edition agreement
> - The no-stale law
> - Reading a failure
:::

Press opens every artifact it makes, renders or unpacks it, and compares it with the manuscript before it calls the build good. This chapter describes the programs that do that work, the checks each one runs, and the exact message each one prints when a check fails. The examples come from the Alice book, the full novel that user `alice` builds on the workstation `hatter` and that CI builds on the host `printshop`. The real runs in Examples 8.1 and 8.2 come from the press's own three-chapter Alice example.

## Artifacts as objects

The press works under four laws, which its *docs/ARCHITECTURE.md* states and Chapter 1, *Introduction*, describes. The third law governs this chapter: "Artifacts are verified as objects." The text of the law continues: "A green build means the actual PDF was rendered and inspected, the actual EPUB was validated by the tool retail channels run, the actual site was crawled." Its last sentence reads: "Verifying without rebuilding is forbidden by construction." The press ROADMAP says the same: verifiers prove artifacts as objects "rather than trusting command exit status".

The press learned this law from the cover that passed at 11.5 percent coverage (Chapter 1), and drew a rule from it: "A producer is only proven by a verifier that rejects a broken artifact." The cover check later in this chapter is that rule at work.

A *verifier* is a `verify_*` module in the press, together with the check it runs on a finished artifact. This chapter follows five verifier runs. `verify_pdf` reads the Print edition (the reading PDF). `verify_formats` reads the Circulating edition (EPUB), the Single-leaf edition (the self-contained HTML), and the Manuscript edition (the stitched Markdown). It also reads the Telegraphic edition (plain text), the Office edition (DOCX), and the Chapter edition (the reader site and its zip). `verify_archives` reads the zip files, among them the Source edition (the source zip), and `verify_pages` crawls the Pages bundle. The fifth run is `verify_pdf` again, with its print profile, on the print interior.

![The witness that could say no, inspecting a finished sheet](assets/woodcuts/the-witness-that-could-say-no.png)

<!-- art: a solemn press reader seated at a high desk inspecting a freshly printed sheet held up to a window, a brass magnifying lens on an articulated arm swung over the page, a tray of rejected sheets at the left with one sheet torn across, a tray of approved sheets at the right under a small brass weight, a rubber stamp and an inkpad on the desk, behind the reader a compact brass apparatus of gears and a lens mounted on a stand, also pointed at the sheet, as if a second inspector; landscape composition; wood engraving with dense hatching and crosshatching, single black ink, no gray washes, no lettering anywhere -->

A sixth verifier, `verify_coverwrap`, reads the cover wrap, and Chapter 12, *The print pack*, covers it. Each verifier ends with a line that begins with `Verified`, or stops the target with a message that names what it found.

The verifiers do their reading with outside tools. Poppler supplies `pdfinfo`, `pdftotext`, `pdffonts`, and `pdftoppm`. The pypdf library reads the link annotations inside the PDF, and epubcheck, the tool retail channels run, validates the EPUB. None of these tools knows anything about press, so none of them can share a mistake with the program that built the file. The ARCHITECTURE document draws the line this way: "generation makes a fact true, verification proves it stayed true all the way into the object a reader receives."

Table 8.1 lists each artifact of the Alice book with the verifier that reads it.

| Artifact | Verifier | Meaning |
|------------|------------------------|---------------------------------------------------|
| `pdf` | `verify_pdf` | The verifier reads *dist/alice.pdf*, the reading PDF. |
| `epub` | `verify_formats` and epubcheck | The verifier checks *dist/alice.epub* itself, then hands it to epubcheck. |
| `html`, `markdown`, `txt`, `docx` | `verify_formats` | The verifier reads the Single-leaf, Manuscript, Telegraphic, and Office editions for the title, the sentinels, and a plain line that press picks from the manuscript. |
| `site` | `verify_formats` and `verify_archives` | The first verifier reads the reader site, and the second compares *dist/alice-site.zip* with it. |
| `source` | `verify_archives` | The verifier recomputes *dist/alice-source.zip* from its policy. |
| `sources` | `verify_archives` | The verifier reads *dist/alice-sources.md* when the book has a table of authorities. |
| `pages` | `verify_pages` | The verifier crawls *dist/pages*, the Pages bundle that the deploy publishes as the Pages site. |
| `print` | `verify_pdf` (print profile) | The verifier reads *dist/alice-interior.pdf* with the stricter print checks. |
| `coverwrap` | `verify_coverwrap` | The verifier reads *dist/alice-coverwrap.pdf*, the whole printed cover on one page. |

Table: Table 8.1. The artifacts of the Alice book and their verifiers

The verifiers overlap on purpose. The checks of this chapter and the five verifier runs that apply them appear in @fig:what-each-verifier-inspects. With it, you can see at a glance which program to suspect when a check fails.

![What each verifier inspects](assets/woodcuts/08-01-what-each-verifier-inspects.png){#fig:what-each-verifier-inspects .diagram width=full-measure fig-alt="A grid with thirteen checks down the side and five verifier runs across the top. Filled dots mark which run applies each check, and the sentinels row has the most dots."}

<!-- art: ARCHETYPE matrix. A grid, thin rules between cells. Column heads in small monospace, left to right: "verify_pdf", "verify_formats", "verify_archives", "verify_pages", "verify_pdf print profile". Row labels in small sans, top to bottom, with filled dots: "fonts embedded" (columns 1, 5), "no blank page" (1, 5), "no edge ink" (1, 5), "trim" (1, 5), "sentinels" (1, 2, 4, 5), "cover on page one" (1), "witnesses" (2), "figure labels" (2), "epubcheck" (2), "link resolution" (1, 4, 5), "archive contents" (3), "black ink" (5), "mirrored margins" (5). Empty cells stay empty. Shade the "sentinels" row 10% gray. The reader sees first that the sentinels row is the fullest. -->

## What the PDF verifier checks

The `press verify` target builds *dist/alice.pdf* and then runs `verify_pdf` on it. The verifier works through its checks in a fixed order. Table 8.2 lists the checks in the order the verifier runs them.

| Check | Meaning |
|----------------------|-------------------------------------------------------------|
| Sentinel count and page floor | Under `PRESS_RELEASE`, the book must declare at least two sentinels and a *page floor* of at least 24. The page floor is the fewest pages the PDF may have, set by `verify-min-pages`. |
| Trim | The verifier takes the expected page size from the design profile and allows 1.0pt either way. |
| File exists | The verifier stops when the PDF is absent. |
| Detector self-test | The verifier tests its own blank-page detector on two synthetic images before it trusts it. |
| pdfinfo | The tool must run, its output must parse, the trim must match, and the page count must reach the floor. |
| Text | Every sentinel and the title must appear in the text that `pdftotext` extracts. |
| Fonts | `pdffonts` must find fonts, and every font must be embedded. |
| List links | Every link in the List of Plates and the List of Figures must lead to a page with an image on it. |
| Render | The verifier renders every page, and the rendered count must equal the count `pdfinfo` reports. |
| Ink | Every rendered page must carry ink, no ink may touch the page edge, and every page must have the same size. |
| Print profile | The print interior must have mirrored margins and, unless the profile allows color, black ink only. |
| Cover on page 1 | The reading PDF must show the cover image on page 1 when the book supplies one. |

Table: Table 8.2. The verify_pdf checks, in order

The print interior goes through the same verifier with the option `--profile print`. Both profiles run every row of Table 8.2 except the last two. The print profile row belongs to the print interior alone, and the cover row belongs to the reading PDF alone.

### Before the verifier opens the file

The first check runs only under `PRESS_RELEASE=1`, the variable that marks a release build. It refuses a book whose sentinels and page floor are too weak to prove anything. Chapter 3, *The shape of a book repository*, shows the refusal in Example 3.3, which opens `this is a release build (PRESS_RELEASE=1) and its witnesses are vacuous:`. The second check reads the trim from the design profile. The Alice book uses the house 6 by 9 profile, so the verifier expects a page 6 inches wide and 9 inches tall, within 1.0pt in each direction. The third check is the plain one: if the file is absent, the verifier prints `PDF not found:` and the path.

The fourth check tests the verifier itself. Later on, the verifier must decide for every rendered page whether it is blank. A detector that called every page inked would pass a book of empty pages, and nobody would know. So `verify_pdf` first shows its detector two synthetic images. One is blank, and the other carries the words "KNOWN INK".[^8-detector] If the detector gets either wrong, the verifier stops with one of these messages:

```text
blank-page detector failed to reject a blank fixture
blank-page detector rejected a marked fixture
```

The self-test is an *invariant*, a named entry in the press's ledger of properties that the press enforces. Its name is `INV-pdf-detector`, and the ledger marks it critical. Neither message concerns your book. The verifier failed its own test.

### Structure, text, and fonts

The verifier now asks `pdfinfo` for the page size and the page count. Four messages can come back from this check:

```text
required verification tool missing: <tool>
could not parse pdfinfo output
unexpected trim size: W x H pt (expected 6 x 9 inches)
suspiciously short PDF: N pages (minimum M)
```

The first concerns the toolchain. The second can mean a broken tool or a damaged PDF. The third means that the PDF came out at the wrong size. The fourth compares the page count with the page floor in *config/metadata.yaml*. It catches a PDF that built without error but lost most of its chapters.

Next, the verifier extracts the text with `pdftotext` and folds every run of whitespace into one space. It then looks for each sentinel by exact case. It treats straight and curly quotes as equal, because pandoc curls the quotes you type. The Alice book, the full novel in user `alice`'s repository, declares the two sentinels that Chapter 3 set with `press config set`:

```text
verify-sentinels:
  - "Twinkle, twinkle, little bat"
  - "she made some tarts"
```

If the first phrase goes missing from the PDF, the verifier prints `missing text sentinel in PDF: Twinkle, twinkle, little bat`. The title gets a softer match. The verifier folds its case, because title pages set the title in capitals. A title page in capital letters therefore satisfies the check. A PDF without the title anywhere fails with `missing title in PDF text:` and the title.

The font check runs `pdffonts` and reads its table. A PDF with no fonts at all fails with `pdffonts found no fonts`. A PDF with a font that is not embedded fails with `unembedded fonts: [...]` and the list of names.

### Links in the lists of illustrations

The PDF carries two lists of illustrations, the List of Plates and the List of Figures. Each entry is a link, and each link must take the reader to the illustration it names. The verifier opens the PDF with pypdf and follows every link in each list to its destination page. That page must carry an image XObject, the PDF's own record of a placed image. Three messages report a failure, with the list's label, `List of plates` or `List of Figures`, in place of `<label>`:

```text
<label> link <dest> resolves to no page
<label> links point at imageless pages: [n...]
<label> present but contains no links
```

The first means that a link points at nothing. The second means that the links point at pages, but the pages hold no image, so the reader arrives on the wrong page. The third means that the list printed, but LuaLaTeX made no links in it. If the pypdf library will not import, the verifier prints `pypdf unavailable; illustration-list destinations not verified` and goes on. It does not fail the build for a missing library, and it does not pretend it checked the links either.

::: {.sidebar}
> **Links that overshoot**
>
> The link check exists because the links in the PDF once went to the wrong place. LaTeX treats a figure as a *float*, a block it is free to move to a better spot on the page. Its link package, hyperref, set the anchor of each float at its caption. A plate's caption sits under the image, so a link from the List of Plates opened the page scrolled to the caption, with the plate itself above the reader's view.
>
> The first fix loaded the `hypcap` package, which moves the anchor to the top of the float. A later version of the house design dropped that package and set `hypcap=true` in the package that sets captions, which does the same job from one place. The press's CLAUDE.md kept the scar as an instruction: "When touching PDF links, verify destinations with pypdf".
:::

### Rendering and ink

The verifier renders every page to a PNG image with `pdftoppm -png -r 120`, at 120 dots per inch, unless a helper renderer is present.[^8-fallback] It then counts the images. If the count differs from the page count, it prints `rendered N pages, pdfinfo reports M`.

With the images in hand, the verifier looks at the ink on each page. Three messages can result:

```text
apparently blank rendered pages: [...]
ink touches rendered page edge: [...]
inconsistent rendered page dimensions: [...]
```

A blank page in the reading PDF is a defect, and the first message lists the page numbers. The edge check looks at a border two pixels wide around each page. It fails any page where any pixel in that border is darker than 245. Ink at the edge means that a figure or a line of type ran off the page, and a reader would see it cut. The third message means that the pages differ in size, which a single book never should.

::: {.warning}
> **Warning:** Do not treat a blank-page failure as cosmetic. The house design caps every image at a height that depends on the profile (6.3in on the house 6 by 9). The cap exists because a taller figure once made LuaLaTeX emit empty pages forever. Find the cause of a blank page before you go on.
:::

The print profile forgives exactly one blank page, and only on one condition. The main text of a printed book starts on a right-hand page, so the left-hand page before it can come out empty. The verifier forgives that one isolated blank even page. A second blank page, or a blank odd page, still fails.

### The print profile

The `press verify-print` target builds the print interior, *dist/alice-interior.pdf*, and runs `verify_pdf --profile print` on it. The print profile adds two checks that matter only on paper.

The first concerns the margins. A printed book has a wider margin at the gutter, so the text block sits farther right on a recto than on a verso. The verifier skips the first 20 percent of the pages. It then finds the median left edge of the ink on rectos and on versos. The two medians must differ by at least 18 pixels at 120 dots per inch. If they do not, the verifier prints:

```text
print profile: margins do not mirror (recto left edge Xpx,
verso Ypx); the gutter is missing
```

The second check concerns color. A page fails when more than 200 of its pixels have an RGB channel spread of 48 or more, which means that a reader sees color in them. The verifier skips the check when the profile declares `ink: color`. The message names a likely cause:

```text
print profile: colored ink on pages [...] (a colored cover
plate in a hand-authored tex/title-page.tex belongs on the
wrap; supply tex/title-page-print.tex without it)
```

After the interior passes, `press verify-print` looks for *assets/cover.jpg*. If the cover is there, the target builds the cover wrap and runs `verify_coverwrap` on it, as Chapter 12 describes. Without a cover, the target stops after the interior.

### The cover on page 1

The reading profile has one check of its own, the one that the 11.5 percent story produced. It applies when *assets/cover.jpg* exists and the book has no *tex/title-page.tex* of its own. In that case the press generates the front matter, and the cover plate belongs on page 1 of the reading PDF. The verifier looks at page 1 twice. If the page renders blank, it prints:

```text
assets/cover.jpg exists but page 1 of the reading PDF renders
blank -- the cover plate was clipped off the page
```

If page 1 has ink but no image, the message ends `carries no cover image -- the generated front matter dropped it`. The second test needs the `pdfimages` tool. Without it, the verifier prints `note: pdfimages absent; cover-on-page-1 identity unverified` and does not fail. The press's own notes record that a missing `pdfimages` softens two checks to notes in this way, and `press doctor` does not check for the tool.

::: {.tip}
> **Tip:** Install `pdfimages` on your workstation and confirm it runs. Without it, two checks soften to notes, `press doctor` does not warn you, and a note is easy to miss in a long run.
:::

When every check passes, the verifier prints one line. Example 8.1 shows a real run from the three-chapter example, which renders 23 pages. The slug reads `alice`. The tail of the line depends on the profile. The print profile ends `, mirrored margins, black ink only` in place of `, cover on page 1`.

**Example 8.1. A press verify run on the three-chapter example**

```text
$ press verify
...
Verified alice.pdf: 23 pages, 6 x 9 trim, embedded fonts,
2 sentinel(s) plus the title as witnesses, every rendered
page contains ink, no edge clipping, cover on page 1
```

That example sets its page floor at 1, which suits a gallery excerpt, and a release build would refuse it. The Alice book itself, the full novel, sets its floor at 24 once its twelve chapters exist.

## What the formats verifier checks

The `press verify-formats` target builds the Circulating, Single-leaf, Manuscript, Chapter, Telegraphic, and Office editions, and the Source edition. It then runs `verify_formats`, and after it `verify_archives`, which the section "Archives and the Source edition" later in this chapter covers. `verify_formats` checks every edition except the Print edition. Its last check confirms that all the editions, the Print edition included, agree with the manuscript.

The first check is a size floor. The HTML and the EPUB must each be at least 1000 bytes. A smaller file is almost certainly a stub or an error page, and the verifier fails it with `missing or suspicious artifact:` and the path.

### The three witnesses

Every edition must carry three pieces of evidence that it holds the book. The press calls the check `INV-format-witness`, and the ledger marks it critical. The first piece is the title. An edition without it fails with `<label> does not carry the book title: <title>`, where the label names the edition. The second is every sentinel. The third is the manuscript witness.

The *manuscript witness* is the longest markup-free line of 40 or more characters in the whole manuscript. A line counts as markup-free when it contains none of these characters:

```text
* _ ` [ ] ( ) < > " ' & # ! |
```

You do not choose the witness: the press finds it. The witness changes when you write a longer plain line. An edition that loses it fails with this message, which quotes the first 60 characters of the line:

```text
<label> lost the manuscript witness line: <first 60 chars>...
```

The sentinels and the witness do different jobs. You choose the sentinels, so they sit where you expect content to survive. The press chooses the witness, so it tests a line that you never thought to protect. A manuscript with no plain line of 40 characters cannot yield a witness at all. The verifier then fails with a message that begins `no manuscript witness derivable;` and ends with its advice, `(write one honest plain sentence)`.

::: {.warning}
> **Warning:** Keep long code lines from becoming witnesses. A raw line of 40 or more plain characters that is not prose, such as a long code line, can become a witness. If the HTML or the EPUB renders it differently, those editions then fail the check.
:::

### Edition by edition

Beyond the three witnesses, each edition has checks of its own. Table 8.3 lists them.

| Edition | Meaning |
|--------------|-------------------------------------------------------------|
| Single-leaf (HTML) | The file must have an `html` element and every sentinel. The count of numbered figure labels must equal the count the manuscript declares. |
| Circulating (EPUB) | The package must have a valid mimetype, a `container.xml`, a non-empty `dc:date`, and the registered ISBN, in the form `urn:isbn:` and the number, when the book has one. The sentinels, the witnesses, and the figure labels must all survive. |
| Manuscript and Telegraphic | The files must carry the sentinels and the witnesses. |
| Office (DOCX) | The verifier joins the text across the `w:t` runs of the document before it searches, and counts the embedded images against the plates. |
| Chapter (reader site) | The site must have an *index.html*, a *reader.css*, enough chapter pages, each chapter on exactly one page, and every plate. |

Table: Table 8.3. The checks each edition adds

The figure-label check catches a numbered figure that vanished in the HTML or the EPUB. The verifier counts the figures the manuscript declares and the labels the edition prints. If they differ, the HTML message reads `HTML carries N numbered-figure labels; the source declares M`. The EPUB message reports the same comparison.

The EPUB checks reach into the package. `EPUB has invalid mimetype` and `EPUB missing container.xml` mean that the zip is not an EPUB at all. Two more messages concern the metadata:

```text
EPUB carries an empty dc:date (retail validators reject it);
the date field should contain a four-digit year
EPUB metadata is missing the registered ISBN <isbn>
```

The date check has a history. Pandoc writes an empty `dc:date` element, and epubcheck rejects it with the code RSC-005. The press therefore extracts a year from the prose date in *config/metadata.yaml* and writes it into *build/epub-metadata.xml* for pandoc to use. A date line with no four-digit year in it would bring the message back.

The DOCX check joins text across runs because Word splits a paragraph into runs wherever the formatting changes, so a sentinel can span two runs. The image count fails with `docx embeds N images; expected at least M plates`.

The reader site has the most checks. Three messages concern its structure:

```text
site missing index.html
site missing reader.css
site has N chapter pages; expected at least M
```

The verifier then checks each chapter by its chapter witness. A *chapter witness* follows the same rule as the manuscript witness, applied to one chapter file: it is the longest markup-free line of 40 or more characters in that file. Each chapter's witness must appear on exactly one page of the site. A chapter missing from every page fails with `reader site is missing <chapter>:` and the details. A chapter on two pages fails with `reader site duplicates <chapter>:` and the details. The last message, `site carries N plates; expected M`, counts the plates.

When every edition passes, the verifier checks agreement across editions, as the section "Witnesses and cross-edition agreement" later in this chapter describes. It then prints one line. Example 8.2 shows a real run on the three-chapter example, with the slug changed to `alice`. The run also shows the source zip's report and the `verify_archives` line.

**Example 8.2. A press verify-formats run on the three-chapter example**

```text
$ press verify-formats
+ stitched 4 files -> dist/alice.md
~/alice/dist/alice-source.zip
archived 12 files; excluded dirs ['.git', '__pycache__',
'build', 'dist']
WARNING: epubcheck not installed; EPUB validated structurally
only. The press toolchain runs the full check in CI. (brew
install epubcheck)
Verified alice.html, alice.epub, alice.md, alice.txt,
alice.docx, site/ (2 sentinel(s), the title, and the
manuscript line 'and here alice began to get rather sleep...'
as witnesses); 7 editions agree on all 4 chapter witnesses
Verified archives: alice-site.zip, alice-source.zip
```

The message prints the manuscript witness in lower case and cuts it at 40 characters, so it is a pointer to the line and not a quotation of it. The seven editions are the six that the `Verified` line names plus the Print edition, which takes part because `pdftotext` was present on the machine that ran the example.

## epubcheck

Retail channels validate an EPUB with epubcheck, so the press runs the same tool. Its function in `verify_formats` is `epubcheck()`, and it has five outcomes. Table 8.4 lists them.

| Situation | Meaning |
|------------------------|-------------------------------------------------------------|
| Missing in the toolchain | When `PRESS_TOOLCHAIN` is set and epubcheck is absent, the verifier fails the build. |
| Missing locally | When `PRESS_TOOLCHAIN` is unset and epubcheck is absent, the verifier prints a warning and goes on. |
| Present but cannot run | The verifier fails and reports a broken toolchain image, not a broken EPUB. |
| Nonzero exit | The verifier fails and prints epubcheck's own output after `epubcheck failed on <path> (exit N):`. |
| Pass | The verifier prints `epubcheck passed:` and the EPUB's name. |

Table: Table 8.4. The outcomes of the epubcheck run

The two cases of a missing epubcheck print different messages, because they mean different things. Inside the toolchain image, where CI cuts releases, a missing epubcheck is a fault in the image. On `hatter`, where `alice` writes, it is a tool that she can install when she likes. Example 8.2 showed the local warning. Inside the image, the verifier prints instead:

```text
epubcheck missing from the press toolchain image; the
retail-format gate cannot be skipped where releases are cut
```

The press decides which case applies by looking at `PRESS_TOOLCHAIN`. It does not look at `CI`. The press's source gives the reason: keying on `CI` would fail "because `CI=false` would read as truthy".[^8-ci-false] The toolchain image sets `PRESS_TOOLCHAIN`, and an ordinary workstation does not.

::: {.tip}
> **Tip:** Install epubcheck on your workstation if you can, with the command the warning names. A local run without it validates the EPUB structurally only, and the first full check then happens in CI, an e-mail later.
:::

The third outcome, the tool that is present but cannot run, comes from one of the press's scars. Ubuntu's `epubcheck` launcher runs the jar through binfmt_misc, which containers do not register. In the press's CLAUDE.md, the scar reads: "the command exists, `which` finds it, and it dies with 'Exec format error' only at execution." Without a separate message, that fault would read as a bad EPUB. The toolchain image now carries a plain `java -jar` wrapper, and the verifier reports the case as `epubcheck is present but cannot run (<exc>); the toolchain image is broken`.

## Archives and the Source edition

The `verify_archives` verifier runs after `verify_formats` in `press verify-formats`. It covers three files: the reader zip, the source zip, and the sources companion when the book has one.

### The reader zip

The reader zip, *dist/alice-site.zip*, is the reader site packed for download. The verifier opens it and compares it with *dist/site/* file by file, by sha256 digest. Every file in the directory must be in the zip with the same bytes, and the zip must hold nothing else. The ledger names this invariant `INV-archive-site-bytes`. A reader who downloads the zip therefore gets exactly the reader site the press built and verified.

### The source zip

The source zip, *dist/alice-source.zip*, is the book's own source, published so that anyone can rebuild it. The verifier recomputes the member list from the same policy, `publication_members()`, and compares it with the zip the builder wrote. It also checks that every member uses DEFLATE compression. The ledger names this invariant `INV-archive-source-policy` and marks it critical. The policy has six rules:

- Members are files that Git tracks, and only those. A book outside any Git repository is archived whole, and one untracked inside a parent repository archives nothing. A file that you never added to Git is not a member.
- Every member sits under an `alice/` prefix, so the zip unpacks into one directory.
- Every member carries the fixed timestamp 2026-07-16 12:00, a mode of 0o755 or 0o644, and DEFLATE level 9.
- The press excludes the directories `build`, `dist`, `.git`, and `__pycache__`.
- The press skips junk files: `.DS_Store`, `Thumbs.db`, `*.swp`, and `*~`.
- The press never follows a symbolic link.

The builder reports its work as it goes. In Example 8.2 it printed `archived 12 files` and the four excluded directories. One more rule protects you from yourself. A file whose name matches a secret pattern aborts the archive. The patterns are these:

```text
.env  .env.*  *.pem  *.key  *.p12  *.pfx  id_rsa*  id_ed25519*
.netrc  *.keychain  credentials*  *.secret
```

::: {.warning}
> **Warning:** Never commit a key, a certificate, or an *.env* file to the book repository. The source zip refuses to build while Git tracks one, and Git keeps the file in its history after you delete it.
:::

### The sources companion

When *config/authorities.yaml* exists, the press writes a sources companion, *dist/alice-sources.md*, beside the book. The verifier checks three things about it. It must name the book, it must run to at least 200 characters, and it must contain at least one entry marker. A companion that fails the last test produces `sources companion looks empty of entries`. Chapter 10, *Front matter, the index, and the table of authorities*, describes the ledger that feeds it.

When all three files pass, the verifier prints its line. Example 8.2 shows it for the three-chapter example, which has no table of authorities: `Verified archives: alice-site.zip, alice-source.zip`.

## The pages verifier

The `press pages` target builds the Pages bundle in *dist/pages*, the directory from which GitHub Pages serves the Pages site. The registry lists nine prerequisites for it. The target builds all of them: the PDF, the EPUB, the HTML, the Markdown, the text, the DOCX, the reader site, and the source zip. The ninth, the sources companion, joins them only when the book has a ledger in *config/authorities.yaml*. It then runs `verify_pages`. The README and the reference also list `press verify-pages`, which runs the same target.

The verifier crawls the site the way a browser would. It reads every page and follows every `href` and `src` attribute, every CSS `url()`, and every `.css` file it finds. Each reference must resolve inside *dist/pages*. Table 8.5 lists the four ways a reference can fail.

| Failure | Meaning |
|----------------------------|-------------------------------------------------------------|
| `dead fragment` | The reference names an anchor with a `#`, and the target page has no such anchor. |
| `absolute reference` | The reference starts at a root or a host, so it would break when the site moves. |
| `broken reference` | The reference names a file that the site does not contain. |
| `reference escapes the site` | The reference climbs out of *dist/pages*, so it would point at nothing once the site deploys. |

Table: Table 8.5. The reference failures of verify_pages

The other checks fall into three groups by when they apply. Every book gets the first group. Every download that the site declares must exist, and the landing page must link each one exactly once. A second link to the same file, or no link at all, fails with `landing page links <name> N times (expected exactly once)`. The verifier looks for every sentinel on the public reading surface, the pages a visitor can read.

Every published page must carry an Open Graph title and a Twitter card, and the `og:image` must resolve. The JSON-LD must exist, must name the book, and must carry no foreign edition.

The second group depends on `site-url` in *config/metadata.yaml*. The canonical link must be present exactly when the book sets `site-url`. The sitemap follows the same rule. When the book sets `site-url`, the sitemap must exist, every `<loc>` in it must resolve, and every canonical URL must appear in it.

The third group concerns *print ordering*, the optional ordering of printed copies from the book's site, which Chapter 12 describes. A call to buy must appear exactly when the book enables print ordering, so a book without it must show none. The generated policy pages must disclose the seller, and no secret may appear anywhere on the site.

One check, in the first group, looks for leaks from the build machine. The head of each page must not match this pattern:

```text
/Users/|/home/|/dist/|/build/|file://
```

A head that contains */Users/alice/* picked up a path from `hatter`, and every visitor would see it in the page source. The check catches the mistake before the site deploys. When everything passes, the verifier prints:

```text
Verified dist/pages: every local reference resolves
(fragments and stylesheet assets included), N downloads
present and linked, sentinels on the public reading surface
```

## Witnesses and cross-edition agreement

The earlier sections named several kinds of evidence. The press calls them all witnesses, and each one answers a different question. Table 8.6 collects them.

| Witness | Where the press checks it | Meaning |
|-------------------|----------------------------|-------------------------------------------------|
| Sentinels | The manuscript, the PDF, every edition, and the Pages bundle | You choose these phrases, so they prove that the parts you care about survived. |
| Title | The PDF and every edition | The title proves that the file is this book and not another. |
| Manuscript witness | Every edition except the PDF | The press chooses this line, so it proves survival of text that you did not think to protect. |
| Chapter witnesses | The reader site and the agreement check | Each chapter's own line proves that the chapter arrived whole and only once. |
| Page floor | The PDF | The count `verify-min-pages` sets proves that the PDF is not a fragment of the book. |

Table: Table 8.6. The witnesses and what each proves

The checker also looks for the sentinels in the manuscript, as Chapter 6, *Checking the manuscript*, describes. A sentinel that passes the checker and fails `verify_pdf` therefore tells you that the manuscript is right and the PDF is wrong. The release rules for the sentinels and the page floor appear in the section "What the PDF verifier checks" earlier in this chapter.

### Agreement across the editions

The last check in `verify_formats` compares every edition with the manuscript, chapter by chapter. Every chapter's witness must appear in every edition. The PDF takes part too, when `pdftotext` is available to extract its text. The check catches a chapter that one edition dropped and the others kept, which no single sentinel would find unless it happened to sit in that chapter.

The match tolerates the ways an edition changes text. The PDF adds running heads in the middle of a paragraph, and text extraction sometimes glues two words together at a line end. So the check does not demand the whole witness line in one piece. It cuts the line into windows of eight consecutive words, with a new window every four words. The chapter passes when any one window appears in the edition.[^8-window]

When an edition fails, the message names the edition and counts the missing chapters:

```text
<label> disagrees with the manuscript: it is missing content
from N chapter(s) (...)...
```

In Example 8.2, the agreement reads `7 editions agree on all 4 chapter witnesses`. The three-chapter example stitches four files, its three chapters and an appendix, so it has four chapter witnesses. On a machine without `pdftotext`, the PDF drops out and the count of editions falls by one.

## The no-stale law

A verifier proves something only about the file it reads. If that file is last week's PDF, the proof is about last week's book. The press's CLAUDE.md lists this as a scar: "Verifying `dist/` without rebuilding blesses stale artifacts; the CLI's dependency edges exist so that cannot happen. Keep them." The ledger enforces it as `INV-graph-no-stale` and marks it critical.

The mechanism is the registry. Its table, `registry.ARTIFACTS`, records each artifact, its files, and its prerequisites. Every verify target builds the artifacts it verifies before it verifies them, and the build follows the registry. One edge has an exception: `press verify-formats` reads an existing PDF for the agreement check without rebuilding it. @fig:rebuild-edges shows what each verify target builds, and the exception.

![The artifacts each verify target rebuilds before it inspects them](assets/woodcuts/08-02-rebuild-edges.png){#fig:rebuild-edges .diagram width=full-measure fig-alt="Five verify commands on the left with arrows to the artifacts each one builds. press pages builds nine artifacts on the way to the Pages bundle, and a dotted arrow shows press verify-formats reading the PDF without building it."}

<!-- art: ARCHETYPE data-flow, left to right. Left column, five rounded boxes in small monospace, top to bottom: "press verify", "press verify-formats", "press pages", "press verify-print", "press coverwrap". Right side, dog-eared file icons in monospace. Solid arrows: "press verify" to "pdf". "press verify-formats" to "epub", "html", "markdown", "site", "txt", "docx", "source", plus one dotted arrow to "pdf" labeled "reads, does not rebuild". "press pages" to "pdf", "epub", "html", "markdown", "txt", "docx", "site", "source", "sources", then on to "pages". "press verify-print" to "print", then a dashed arrow labeled "if assets/cover.jpg" to "coverwrap". "press coverwrap" to "print", then "coverwrap". The reader sees first that solid arrows leave every command before any verifier runs. -->

The edges in @fig:rebuild-edges come straight from the press, and the earlier sections of this chapter gave each target's builds. The exception needs care. When `pdftotext` exists, the target still reads whatever *dist/alice.pdf* is present into the agreement check. If `alice` edits a chapter and runs only `press verify-formats`, the agreement check compares the new editions with the PDF from whatever last built it.

::: {.tip}
> **Tip:** Run `press all` before you push. It rebuilds every reading edition, the source zip, and the Pages bundle, then runs `verify_pages`, `verify_pdf`, `verify_formats`, and `verify_archives` over them. For the print interior and the cover wrap, run `press verify-print` as well.
:::

The `press all` target runs the checker first, then builds every edition, the source zip, and the Pages bundle. Last, it runs the verifiers in this order: `verify_pages`, `verify_pdf`, `verify_formats`, and `verify_archives`.

A commerce gate follows the verifiers (Chapter 7).

The law reaches the generated inputs too: every pandoc build regenerates them first (Chapter 7).

The invariant has a stated limit, and the ledger records it: "CLI-path only; importing a verifier module directly skips the rebuild." The edges live in the `press` command. A script that imports `press.verify_pdf` and calls it on *dist/alice.pdf* reads whatever file is there, fresh or not.

::: {.warning}
> **Warning:** Do not call a verifier module from your own script to save a build. It checks whatever is in *dist/*, and a pass then proves nothing about the manuscript you edit.
:::

## Reading a failure

Start with the command that ran. Each verify target runs a known set of verifiers. A failure under `press verify` comes from `verify_pdf`, and one under `press verify-formats` comes from `verify_formats` or `verify_archives`. A failure under `press pages` comes from `verify_pages`. Under `press verify-print`, it comes from the print profile of `verify_pdf` or from `verify_coverwrap`. Under `press all`, the verifiers run in the order the previous section gives.

Where a message names the artifact, such as `PDF`, `EPUB`, `HTML`, `site`, or an edition's label, Table 8.1 tells you which file to open.

Next, decide whether the fault lies in the book or in the machine. Some messages point at the machine: `required verification tool missing:`, both blank-page detector messages, and `epubcheck is present but cannot run`. The message `could not parse pdfinfo output` can point at a broken tool, though it can also mean a damaged PDF.

For a machine fault, run `press doctor`, which checks the tools the verifiers need, except `pdfimages`. Chapter 2, *Installing press*, describes the command. Example 8.3 shows part of its report from a Mac, with the epubcheck row cut short.

**Example 8.3. Part of a press doctor report**

```text
$ press doctor
press doctor
  [     ok] pandoc     every build target
  [     ok] lualatex   PDF and print builds
...
  [     ok] pdftoppm   PDF verification renders
...
  [ absent] epubcheck  the retail EPUB gate ...
...
```

The `absent` state marks an optional tool that is missing. A required tool that is missing shows `MISSING`, and a tool that is present but fails to run shows `BROKEN`. A `BROKEN` tool keeps the report from calling the machine ready, even when the tool is optional. When every tool is ready, the report ends with `this machine can make books`, and the command exits 0.

When the fault lies in the book, the message tells you what went missing, and your job is to find out why. The most common case is a missing sentinel. @fig:verify-run shows the run `alice` sees on `hatter` after a revision of the chapter that held her first sentinel.

![A press verify run that fails on a missing sentinel](assets/woodcuts/08-03-verify-run.png){#fig:verify-run .diagram width=full-measure fig-alt="A terminal window titled alice@hatter shows the command press verify, an elided line, and the message that the sentinel Twinkle, twinkle, little bat is missing from the PDF."}

<!-- art: ARCHETYPE terminal. A plain light terminal window with a thin 0.5 pt frame and a title bar reading "alice@hatter". Inside, in monospace, three lines, top to bottom: "$ press verify", then a line holding only "...", then "missing text sentinel in PDF: Twinkle, twinkle, little bat". No color, no bold. Draw the last line at full black and the first two in 40% gray. The reader sees the sentinel message first. -->

A missing sentinel has four usual causes. The first is a revision that reworded the phrase. Search the manuscript for it. If the checker also fails on it, the manuscript is the culprit. The second is a phrase at the start of a chapter, where the chapter opening splits the first word and small-caps the rest, as Chapter 4, *Writing the manuscript*, explains. The third is an edition that lost the chapter, so run `press verify-formats` too, because its agreement check counts the chapters that each edition lacks. The fourth is a word in the phrase that LuaLaTeX hyphenated at a line end. Choose shorter words or another phrase.

Table 8.7 lists failures that point at the book and where to look first. The next chapter, *The house design*, describes the typography and layout these verifiers inspect.

| Message begins | Meaning |
|------------------------------------|---------------------------------------------------------|
| `missing text sentinel in PDF` | A sentinel is not in the PDF text. Search the manuscript for the phrase, then check that it does not open a chapter. |
| `suspiciously short PDF` | The PDF has fewer pages than `verify-min-pages`. Check that the PDF holds every chapter you expect. |
| `apparently blank rendered pages` | The PDF has a page with no ink. Look first at the figure nearest the listed page. |
| `<label> lost the manuscript witness line` | One edition dropped the longest plain line of the manuscript. Find the line, then look at what the edition did to its chapter. |
| `<label> disagrees with the manuscript` | One edition lacks content from the chapters the message counts. Open that edition at those chapters. |

Table: Table 8.7. Verifier failures and where to look first

[^8-detector]: Each synthetic image is 300 by 450 pixels. The detector calls a page blank when its pixels have a standard deviation under 1.2. It also calls a page blank when its darkest pixel is lighter than 249 and its mean is above 252.5.

[^8-fallback]: The press's CLAUDE.md lists the `pdftoppm` fallback among its scars. Its instruction reads "Keep that fallback working." Without it, a machine that lacked the other renderer could not verify a PDF at all.

[^8-ci-false]: In most shells and most CI systems, an environment variable holds a string, and a check for its presence treats the string `false` as present.

[^8-window]: Because the windows overlap by four words, one break in the line, such as a running head, spoils at most two of them.
