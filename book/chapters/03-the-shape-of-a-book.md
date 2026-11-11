# The shape of a book repository

::: {.in-this-chapter}
> **In this chapter:**
>
> - Scaffolding a book
> - The tree, file by file
> - The metadata file
> - Reading and writing config from the shell
> - Chapters, appendixes, and how they sort
> - Adding a chapter
> - The Makefile and local builds
> - What git has to do with it
> - Where things go: build and dist
:::

Every book that press builds lives in a *book repository*, a directory with *config/metadata.yaml* at its top and the manuscript under *book/*. The press creates that directory for you, names every file in it, and refuses to build in a directory without that file. You will spend most of your working hours inside this one directory, so it pays to know what each file does and which program reads it. The running sample is the Alice book, slug `alice`, which the user `alice` writes on the workstation `hatter`.

## Scaffolding a book

The target that creates a book repository is `press new`. It takes one argument, the directory to create, and four options that fill in the identity of the book. The synopsis is:

```
press new <directory> [--author A] [--publisher P]
          [--place PLACE] [--owner GH]
```

Table 3.1 lists the options and the value each one takes when you leave it out.

| Option | Meaning |
|--------------|------------------------------------------------------------------|
| `--author` | The byline. Without it, press reads `git config user.name`, and if git has no name either, it writes "The Author". |
| `--publisher` | The imprint. It defaults to the author, which suits a book you publish yourself. |
| `--place` | The place of the imprint. It defaults to "Earth". |
| `--owner` | The GitHub account that will own the repository. With it, press writes live `repository` and `site-url` lines into the metadata file. Without it, those two lines stay commented out, with the word `OWNER` where the account belongs. |

Table: Table 3.1. press new options

The Alice book belongs to the GitHub account `wonderland-press`, and its author is Lewis Carroll, so `alice` gives both on the command line. Example 3.1 shows the whole session. The second line of output gives the absolute path of the new directory, which we shorten here.

**Example 3.1. Scaffolding the Alice book**

```
$ press new alice --author "Lewis Carroll" --owner wonderland-press
scaffolded alice -> /.../alice
next: edit config/metadata.yaml, write book/chapters/, run `press all`
```

The command looks trivial, and most of the time it is. Behind those two lines of output, press does six things in a fixed order:

1. It refuses a path that already exists, so it can never overwrite a book.
2. It checks the directory name as a slug before it copies a single file.
3. It copies the book template from its own package data.
4. It renames every template file called `dot-` something to the matching dotfile.
5. It stamps its four agent workflows into *.claude/workflows/*.
6. It substitutes the slug, author, publisher, place, repository line, and site-url line into the copied files.

The order matters for the second step. Because press checks the name before it copies anything, a refused name leaves no half-built directory behind for you to delete.

The directory name becomes the book's *slug*, the basename of every artifact the press produces. A slug must match the pattern `[a-z0-9][a-z0-9-]*`: lowercase letters, digits, and hyphens, starting with a letter or a digit. The Alice PDF is therefore *alice.pdf*, its EPUB is *alice.epub*, and so on through every edition. Neither `Alice` nor `my book` passes the slug test, and press refuses both.

::: {.tip}
> **Tip:** Choose the slug as if it were permanent. It names every file a reader downloads, and the scaffold writes it into the repository and Pages addresses as well.
:::

One step that press does not take is `git init`. The new directory is a plain directory, with no repository inside it yet. The section "What git has to do with it" later in this chapter explains why you want one before your first full build.

## The tree, file by file

@fig:scaffold-tree shows the tree that `press new alice` leaves behind with press 3.0.2, the current version at the time of this writing. Every file in it has a single job.

<!-- art: ARCHETYPE tree. A vertical trunk with horizontal stubs, names in monospace, rooted at "alice/". Stubs in order: ".claude/workflows/" with children "aesthetic-brief.js", "art-direction.js", "authorities-research.js", "editorial-passes.js"; ".github/workflows/book.yml"; ".gitignore"; "book/chapters/00-preface.md"; "CHANGELOG.md"; "CLAUDE.md"; "config/" with children "front-matter.yaml", "house-rules.yaml", "metadata.yaml"; "Makefile"; "requirements.txt". Three italic sans annotations, right-aligned, each on a thin straight leader ending in a dot: at "book.yml", "the whole CI: calls the press's build.yml at v3"; at "metadata.yaml", "identity, press facts, verification knobs"; at "book/chapters/", "your chapters go here". Put "metadata.yaml" in a box with a 20% gray fill so the eye finds it first. Black and white, no icons. -->
![The tree that press new lays down](assets/woodcuts/03-01-scaffold-tree.png){#fig:scaffold-tree .diagram width=full-measure fig-alt="A directory tree rooted at alice, with the workflows, the CI file, the preface, the changelog, the agent guide, three config files, the Makefile, and requirements.txt. Leader lines label the CI file, the metadata file, and the chapters directory."}

Table 3.2 gives each file in the tree and what it does, in the order the tree lists them.

| Path | Meaning |
|-------------------------------|------------------------------------------------------------|
| *.claude/workflows/* | Four agent workflows. *aesthetic-brief.js* drafts *config/aesthetic.yaml* from a one-line brief, *art-direction.js* writes *art/commissions.md*, *authorities-research.js* builds *config/authorities.yaml*, and *editorial-passes.js* runs the iterative editorial machine. Each file begins with a comment that names the press version that wrote it. |
| *.github/workflows/book.yml* | The whole CI for the book. It calls the press's reusable workflow at the floating tag `v3`. |
| *.gitignore* | It keeps `build/`, `dist/`, `__pycache__/`, and `.DS_Store` out of git. |
| *book/chapters/00-preface.md* | A one-paragraph preface. It exists so that an empty book builds and verifies. |
| *CHANGELOG.md* | A changelog in the Keep a Changelog form. CI extracts the section for a tag and uses it as the release notes. |
| *CLAUDE.md* | The book's own guide for authors and agents, 79 lines on the layout, the commands, and the house laws. |
| *config/front-matter.yaml* | Every key in it starts commented out. The presence of the file alone turns on generated front matter. |
| *config/house-rules.yaml* | The book's own house rules, empty at first: `banned-patterns: {}`, `jargon-allow: []`, and `audit-dirs: []`. |
| *config/metadata.yaml* | The identity of the book, the press facts, and the verification knobs. |
| *Makefile* | A wrapper that hands every target to `python3 -m press`. |
| *requirements.txt* | The press requirement for local builds. CI never reads it. |

Table: Table 3.2. The files of a fresh book repository

The workflows deserve one more word. The first line of each one reads `// scaffolded by press 3.0.2; source of truth: press data/workflows`. When you upgrade press later, that stamp tells you which version laid the file down, and a mismatch shows that your copy is older than the press you run. Chapter 15, *The operator's desk and the editorial machines*, describes what the workflows do.

### The preface stub

The only manuscript file in a new book is the preface. Example 3.2 reproduces it exactly as the scaffold writes it.

**Example 3.2. The scaffolded book/chapters/00-preface.md**

```
# Preface {.unnumbered}

Why this book exists, in your own voice, with no throat-clearing. Delete
this sentence and the one before it; keep the heading. This paragraph only
exists so a freshly scaffolded book builds and verifies before the first
real word lands.
```

The paragraph tells you to replace it, and you should. Keep the heading line. The `{.unnumbered}` attribute keeps the preface out of the chapter numbering, as the section "Chapters, appendixes, and how they sort" later in this chapter explains.

### How press finds the book

Every press target starts by finding the *book root*. The press takes the directory named in the environment variable `BOOK_ROOT`, or else the current directory. That directory must contain *config/metadata.yaml*, and if it does not, press refuses with the message that the directory "is not a book". The press does not search upward through parent directories the way git does. If `alice` runs `press check` from inside *book/chapters/*, the press refuses, because that directory holds no metadata file.

::: {.tip}
> **Tip:** Run every press target from the top of the book repository. If a script must run from somewhere else, set `BOOK_ROOT` to the book's directory first.
:::

### Files you add later

The scaffold writes only the files that every book needs. A book grows other files as its author asks more of the press, and each consumer of an optional file builds without it. The ones you are most likely to meet are these:

- The files *config/index-terms.yaml*, *config/authorities.yaml*, and *config/aesthetic.yaml* hold the subject index terms, the table of authorities, and the book's visual identity.
- The files *config/cover-styles.yaml* and *config/illustration-styles.yaml* merge over the house style libraries, and *config/qualification.yaml* holds inspection records.
- The files *tex/title-page.tex* and *tex/title-page-print.tex* override the generated front matter.
- The directory *assets/* holds *cover.jpg*, *press-logo.png*, *author.jpg*, the plates under *woodcuts/*, and the Web stylesheets *web/reader.css* and *web/extra.css*.
- The directory *art/* holds *author-photo.jpg*, *commissions.md*, and the *candidates/* directory.
- The directory *tests/known-bad/* holds fixtures that prove the book's own house rules still fire.

Chapter 9, *The house design*, Chapter 10, *Front matter, the index, and the table of authorities*, and Chapter 11, *The art department*, take these up in turn.

## The metadata file

The file *config/metadata.yaml* is the one file that makes a directory a book. It holds the book's identity, the facts the press needs to name and publish the artifacts, and the knobs that tell the verifiers how hard to look. The press reads it through a typed model, and pandoc reads the raw file as well. Every pandoc defaults file names the metadata file as its `metadata-file`, so a standard pandoc key that you add here passes through to every edition.

Example 3.3 shows the file as `press new alice` writes it, with the placeholders filled. The real file continues past the last line shown with a long commented block for direct print ordering, which Chapter 12, *The print pack*, covers.

**Example 3.3. The scaffolded config/metadata.yaml**

```
title: "alice"
subtitle: "A subtitle"
author:
  - "Lewis Carroll"
date: "First edition, 2026"
lang: en-US
copyright: "Copyright 2026."
publisher: "Lewis Carroll"
publisher-place: "Earth"
description: >-
  One honest paragraph on what this book is.
keywords:
  - writing

# Press facts: artifact basename, canonical repo, and the public Pages URL
# release notes link to (omit site-url to skip public download links).
slug: "alice"
repository: "https://github.com/wonderland-press/alice"
site-url: "https://wonderland-press.github.io/alice"

# Verification knobs. Sentinels are prose fragments every rendered
# format must contain: pick 2-4 phrases from your actual manuscript,
# each distinctive enough to appear exactly once (a whole memorable
# clause, not a common word). Empty sentinels and a one-page floor are
# DRAFT settings; a release build (CI on a tag) refuses them until at
# least 2 sentinels and verify-min-pages >= 24 are set.
verify-sentinels: []
verify-min-pages: 1
# trim: {width: 6, height: 9}

# The print pack reads these when building the interior and cover wrap.
# print: {paper: cream}          # or white; or {page-thickness: 0.0025}

# Registrations: validated by press check, injected into the colophon,
# EPUB metadata, and the wrap barcode. "pending" is the one honest
# placeholder; retail: true refuses to pass check while any placeholder
# remains. See the registrations skill for the actual processes.
# registrations:
#   isbn:
#     print: "pending"           # check digit validated when real
#     epub: "pending"
#   lccn: "pending"
#   retail: false
...
```

Notice what the scaffold could not know. The title is the slug, the subtitle is a placeholder, and the description says what a description should say. A new book builds with all three as they stand, so nothing forces you to fix them on the first day. They do appear on the title page and the landing page, however, and the first person you show the book to will notice them before you do.

### Identity

The first block of the file names the book. Table 3.3 gives each field, its type, and what the press does with it. The title, the author, and the slug are the three fields the model insists on.

| Field | Type | Meaning |
|-------------------|------------|----------------------------------------------------|
| `title` | string | The book's title. The model needs it. |
| `subtitle` | string | The subtitle. If it holds "or," clauses, the title page and the landing page stack them on separate lines. |
| `author` | string or list | The byline, one name per list item. A single string becomes a one-item list. The model needs it. |
| `date` | string | Free text. The press takes the first four-digit year in it for the EPUB date and for the lowercase roman numerals on the title page. |
| `lang` | string | A BCP-47 language tag, which press passes through to pandoc. The template sets `en-US`. |
| `copyright` | string | The copyright line. Once *config/front-matter.yaml* exists, the model needs it. |
| `publisher` | string | The imprint. The model needs it with front matter. The press also exports it to TeX as the environment variable `BOOK_PUBLISHER`. |
| `publisher-place` | string | The place of the imprint. The model needs it with front matter. |
| `description` | string | A one-sentence blurb for the landing page and the stores. The `press check` target refuses a book without one. |
| `keywords` | list | Subject keywords, which press passes to the editions. |
| `rights` | string | A rights statement, which press passes through to pandoc. |

Table: Table 3.3. Identity fields in metadata.yaml

The date field explains a small mystery in the EPUB. Pandoc writes an empty date into the EPUB, and epubcheck rejects an empty date. The press therefore pulls the year out of your free-text date and writes it into the EPUB metadata itself.[^epubdate] A date such as "First edition, 2026" gives the EPUB the year 2026 and gives the title page its roman numerals, and you never type the year twice.

Because the scaffold writes *config/front-matter.yaml*, a new book has front matter switched on from the first build. The scaffold fills `copyright`, `publisher`, and `publisher-place` for that reason. If you delete any of the three while the front-matter file exists, the model refuses the metadata.

### Press facts

The second block holds three facts the press needs to publish: the slug, the repository, and the public address. Table 3.4 lists them with the verification knobs that follow them in the file.

| Field | Type | Meaning |
|--------------------|-----------|---------------------------------------------------|
| `slug` | string | The basename of every artifact. It must match `[a-z0-9][a-z0-9-]*`, and the model needs it. |
| `repository` | string | The canonical repository URL. Without it, the landing page leaves out its paragraph about the source. |
| `site-url` | string | The public GitHub Pages URL. It is the one authority for every absolute URL the press writes: canonical links, the `og:image`, and the sitemap. Without it, the press writes nothing shaped like a URL. |
| `verify-sentinels` | list | Phrases the verifiers must find in the manuscript and in every artifact. The default is an empty list. A release needs at least two. |
| `verify-min-pages` | integer | The floor for the PDF page count. The model defaults to 40, but the template writes 1. A release needs at least 24. |

Table: Table 3.4. Press facts and verification knobs

The rule for `site-url` follows from the first law of the press: "Facts are stated once." A book that tells the press its address in one place cannot publish a sitemap that disagrees with its canonical links. A book that leaves the field out gets no sitemap, no canonical links, and no absolute download links.

### Verification knobs

A *sentinel* is a phrase from your manuscript that the verifiers must find, character for character, in the source and in every artifact. If the PDF, the EPUB, or the plain-text edition lost a chapter on the way out, a sentinel from that chapter would go missing, and the verifier would fail. Matching uses exact case. The verifiers treat curly and straight quotes as equal, because pandoc curls the quotes you type.

The template's own advice for choosing them is good: "pick 2-4 phrases from your actual manuscript, each distinctive enough to appear exactly once (a whole memorable clause, not a common word)". For Alice we chose two lines of verse from the middle of their chapters, "Twinkle, twinkle, little bat" and "she made some tarts".

::: {.warning}
> **Warning:** Never take a sentinel from the first words of a chapter. A chapter opening can split the first word into a large initial and small capitals, and then the PDF no longer contains the phrase as you typed it.
:::

The page floor is the second knob. The PDF verifier fails a PDF with fewer pages than `verify-min-pages`. The model's default of 40 suits a finished book. The template writes 1 so that a new book with nothing but its preface stub passes on the first day.

Both settings of the template are draft settings. When CI builds a tag whose name starts with `v`, it sets the environment variable `PRESS_RELEASE=1`. The press then refuses *vacuous witnesses*, which are sentinels and a page floor too weak to prove anything. Example 3.4 shows the refusal a fresh Alice book would draw at its first tagged release.

**Example 3.4. The release refusal for draft knobs**

```
this is a release build (PRESS_RELEASE=1) and its witnesses are vacuous:
verify-sentinels has 0 entries; a release needs at least 2 distinctive prose fragments
verify-min-pages is 1; a release needs at least 24
```

### Print, chapter openings, and registrations

The rest of the fields gather under four mappings, `print`, `chapter-opening`, `registrations`, and `commerce`. A new book needs none of them. Table 3.5 gives the ones you will reach for first, with their defaults.

| Field | Default | Meaning |
|-----------------------------------|-----------------|-----------------------------------------------|
| `print.profile` | `house-6x9` | The design profile, which sets the trim and the interior geometry. |
| `print.provider` | `house` | The provider spec, which sets the spine and cover geometry. |
| `print.binding` | `perfect-bound` | The binding: `perfect-bound`, `saddle-stitch`, `coil`, `casewrap`, or `dust-jacket`. |
| `print.material` | `paperback` | The cover material: `paperback`, `casewrap`, or `linen`. |
| `print.paper` | `cream` | The interior stock: `white` or `cream`. |
| `print.page-thickness` | none | Inches per page. When you set it, it overrides the paper. |
| `chapter-opening.style` | the profile's | The chapter opening: `none`, `drop-cap`, `raised-cap`, or `ornate`. The house profile uses `none`. |
| `chapter-opening.lines` | 3 | The number of text lines the initial spans. |
| `registrations.isbn.print` | none | The print ISBN, as 13 digits or the word `pending`. The EPUB ISBN goes in `registrations.isbn.epub`. |
| `registrations.retail` | false | When true, `press check` refuses any missing or pending registration. |

Table: Table 3.5. The first print and registration fields

One field in this part of the model looks settable and is not. The press derives `trim` from the profile. The press refuses a direct write with the message "trim is not set directly; choose it with print.profile". An older book that still carries a `trim` mapping keeps it, but the press only checks it against the profile and refuses the metadata when the two disagree. Chapter 9, *The house design*, covers the profiles and chapter openings, Chapter 12 covers the print fields, and Chapter 13, *Registrations*, covers the numbers.

## Reading and writing config from the shell

You can edit the metadata file in any text editor, and many authors do. The press also gives you a target, `press config`, that reads and writes every field from the shell. It has five subcommands:

```
press config get|set|unset|list|validate
```

The reason to prefer it is validation. Before `press config set` touches a byte on disk, it runs the new value through the same typed model that validates a build. A value that would break the build never reaches the file. For the metadata file, that model includes the commerce and registration rules, and for the house rules, it compiles each regular expression.

Example 3.5 shows `alice` giving the book its real identity. The title contains an apostrophe, so the shell needs double quotes around it.

**Example 3.5. Setting the Alice book's identity**

```
$ press config set title "Alice's Adventures in Wonderland"
$ press config unset subtitle
$ press config set description \
    "A girl follows a rabbit underground and argues with everyone."
$ press config set verify-sentinels \
    '["Twinkle, twinkle, little bat", "she made some tarts"]' --json
$ press config set verify-min-pages 24
$ press config set print.paper white
```

Two rules govern the values you type. A list or a mapping must be JSON, with the `--json` option, as the sentinel line shows. A boolean accepts `true`, `yes`, `on`, or `1`, and `false`, `no`, `off`, or `0`. Some fields, such as `print.paper` and `print.binding`, have a fixed set of choices, which Table 3.5 lists.

### Where each field lives

The `press config` target knows which file holds each field, so you name the field and not the file. Table 3.6 shows the routing.

| Fields | File |
|----------------------------------------------|---------------------------------------|
| Identity, verification, and every `print`, `chapter-opening`, `registrations`, and `commerce` field | *config/metadata.yaml* |
| `banned-patterns`, `jargon-allow`, and `audit-dirs` | *config/house-rules.yaml* |
| `edition-note` through `motto`: dedication, epigraph, acknowledgements, and the colophon lines | *config/front-matter.yaml* |
| `name` through `book-colors`: the cover, plates, logomark, portrait, typography, and palettes | *config/aesthetic.yaml* |

Table: Table 3.6. Where press config writes each field

### Kinds of field

Each field has one of four kinds. A *writable* field takes `set` and `unset`. An *immutable* field, such as `trim`, refuses writes and says what to change instead. A *structured* field holds a list that is too rich for one command line: the index terms, the authorities ledger, and the qualification records. The press sends you to the file or the workflow that maintains it. A *file* field is a whole file, such as *tex/title-page.tex* or the assets, and the press tells you where to put it.

The `press config list` target prints every field with its type and a one-line description, which makes it the quickest reference while you work. For a field you cannot set from the shell, it adds a second line, starting with an arrow, that says where to go instead.

### Validating after a hand edit

If you edit the YAML by hand, run `press config validate` afterward. It checks every config file the book has against its model and prints one line per file. Example 3.6 shows its output for a book that has all six.

**Example 3.6. press config validate**

```
$ press config validate
config/metadata.yaml: ok
config/house-rules.yaml: ok
config/front-matter.yaml: ok
config/aesthetic.yaml: ok
config/index-terms.yaml: ok
config/authorities.yaml: ok
```

The desk offers a third way in. Run `press desk` and type `w` for the setup wizard, which asks for the title, the subtitle, the author, and the description. For any other field, use `press config` or an editor.

## Chapters, appendixes, and how they sort

The press finds the manuscript by filename, and it never reads a table of contents. Two lines of the press source decide which files are chapters and which are appendixes:

```
chapters = sorted((root() / "book" / "chapters").glob("[0-9]*.md"))
appendices = sorted((root() / "book" / "appendices").glob("[a-z]-*.md"))
```

A *chapter file* is a file in *book/chapters/* whose name starts with a digit and ends in `.md`. An *appendix file* is a file in *book/appendices/* whose name is a single lowercase letter, a hyphen, and anything ending in `.md`. The press sorts each list by filename, and it merges them in a fixed order: chapters, then appendixes, then the generated subject index.

::: {.warning}
> **Warning:** The press skips any other Markdown file in those two directories, and it says nothing about it. A chapter saved as *chapter-two.md* or *2.md.txt* never reaches the book.
:::

If neither directory yields a single file, the press refuses with `FileNotFoundError("no manuscript files found under book/")`. The scaffold's preface keeps a new book clear of this refusal.

### Lexical order and zero padding

The sort compares filenames character by character, and it knows nothing about numbers. @fig:how-files-sort shows the consequence. A chapter named *10-the-lobster-quadrille.md* sorts before *2-the-pool-of-tears.md*, because the character `1` comes before `2`. With zero padding the problem disappears: *02-* sorts before *10-*, and the book reads in order.

The appendix row of the figure shows the second rule, the letters. The `press add appendix` target takes the next unused letter, counting down from `z`. The first appendix you add becomes *z-*, the second *y-*, and the third *x-*. The generated subject index takes the first free letter counting up from `a`, and the press never assigns it `z`. In a book with three appendixes added the ordinary way, the index therefore takes the letter A, and the authored back matter takes X, Y, and Z. By filename, *a-* sorts ahead of all three. If you add back matter with `press add appendix --front`, the letters count up from `a` instead, and the index takes the next free letter after them.

<!-- art: ARCHETYPE before/after, two rows of paired frames, (a) and (b) above (c) and (d), each label under its frame. Each plain rectangle holds a monospace listing, with the order beneath in small sans. (a) "1-down.md", "10-lobster.md", "2-pool.md", order "1, 10, 2", with an italic callout "sorts too early" on the "10" line. (b) "01-down.md", "02-pool.md", "10-lobster.md", order "1, 2, 10". (c) italic label "press add appendix": "x-glossary.md", "y-also-by.md", "z-about.md", plus a dashed box "build/generated/" with "a-index.md"; beneath, "index A, authored X Y Z". (d) italic label "press add appendix --front": "a-glossary.md", "b-also-by.md", dashed box with "c-index.md"; beneath, "authored A B, index C". The reader should see first that frame (a) puts 10 before 2. -->
![How press sorts chapter and appendix files](assets/woodcuts/03-02-how-files-sort.png){#fig:how-files-sort .diagram width=full-measure fig-alt="Four directory listings. Unpadded chapters sort 1, 10, 2 and padded ones 01, 02, 10. Appendixes added from z leave the index at a, and appendixes added with front take a and b and leave the index at c."}

::: {.tip}
> **Tip:** Pad chapter numbers to two digits from the first chapter. If you expect more than 99 chapters, pad to three, and rename the whole set at once.
:::

### Front parts and unnumbered headings

A preface, a foreword, or an introduction is a chapter whose filename starts with `00-`. The scaffold's preface is one. What keeps such a chapter out of the numbering is its heading. A level-one heading with the attribute `{.unnumbered}`, or its short form `{-}`, gets no chapter number and no chapter opening. The preface heading in Example 3.2 uses the long form.

The press has no parts. It sets pandoc's `top-level-division` to `chapter`, so every level-one heading (`#`) in the manuscript starts a chapter, and nothing groups chapters above that level. A book that wants "Part One" and "Part Two" pages cannot have them at the time of this writing.

## Adding a chapter

You can create a chapter file in any editor, as long as you get the name right. The press offers a target that gets it right for you:

```
press add chapter|appendix <name> [--front]
```

The `press add` target turns the name into a filename slug. It lowercases the name and replaces each run of characters that are not letters or digits with one hyphen. For the heading, it keeps a human title exactly as you typed it, and it sentence-cases a bare slug. A chapter gets the number one past the highest existing chapter, zero-padded to at least two digits, and the first chapter of a book is `01`.

Example 3.7 shows `alice` adding the first two chapters and three pieces of back matter, then listing the two directories.

**Example 3.7. Adding chapters and appendixes to the Alice book**

```
$ press add chapter "Down the rabbit-hole"
$ press add chapter the-pool-of-tears
$ press add appendix about-the-author
$ press add appendix also-by
$ press add appendix glossary
$ ls -1 book/chapters book/appendices
book/appendices:
x-glossary.md
y-also-by.md
z-about-the-author.md

book/chapters:
00-preface.md
01-down-the-rabbit-hole.md
02-the-pool-of-tears.md
```

The first chapter gets its heading verbatim, `# Down the rabbit-hole`. The second gets `# The pool of tears`, sentence-cased from the bare slug. Each new file holds a placeholder paragraph under its heading: "Write this part here. This placeholder paragraph only exists so the file is valid Markdown that builds; delete it and begin."

The `--front` option changes where the new file goes. With `chapter`, it creates a `00-` file with an `{.unnumbered}` heading, the way the scaffold's preface works, so `press add chapter preface --front` gives you *book/chapters/00-preface.md*. With `appendix`, it counts up from `a` instead of down from `z`. When all 26 letters are in use, `press add appendix` refuses with "the appendices are full".

::: {.warning}
> **Warning:** Do not expect `press add` to replace a file. It refuses to overwrite an existing file and exits with status 1, and a usage mistake exits with status 2.
:::

The refusal to overwrite is an *invariant*, a named entry in the press's ledger of properties that its tests prove, in this case `INV-add-no-clobber`. The target exists so that no author has to build a chapter file by hand with shell redirection.[^printf]

## The Makefile and local builds

Some authors type `make` before they think. The scaffold respects that habit with a *Makefile* that does nothing on its own. Example 3.8 shows the whole file.

**Example 3.8. The scaffolded Makefile**

```
# Muscle-memory wrapper; the pipeline itself lives in the press package.
PRESS ?= python3 -m press

.PHONY: all check pdf epub html markdown site txt docx pages source verify verify-formats render wordcount clean

all check pdf epub html markdown site txt docx pages source verify verify-formats render wordcount clean:
	$(PRESS) $@
```

Every target in the file runs the same recipe. The automatic variable `$@` holds the name of the target, so `make pdf` runs `python3 -m press pdf` and `make all` runs `python3 -m press all`. The press does all the work, and the dependencies between targets live in the press, not in the Makefile. That is why the file declares every target `.PHONY`: make(1) has no files to compare, and it must always hand the request on.

The `?=` assignment lets you replace the command. If `press` is on your path as a program, `make pdf PRESS=press` uses it directly. The Makefile names sixteen targets. The press has more, such as `print` and `coverwrap` for the print pack, and for those you call `press` itself.

### The requirements file

The second file for local builds is *requirements.txt*. Example 3.9 shows it.

**Example 3.9. The scaffolded requirements.txt**

```
# Local builds. CI does not read this file; the press action installs itself
# from its own checkout. For day-to-day work prefer an editable install of
# your press clone: pip install -e ~/path/to/press
press @ git+https://github.com/clintecker/press@v3
```

The last line installs press from its repository at the floating tag `v3`. The comment above it gives the better advice for an author who also works on press: install your own clone in editable mode, so that a change to the press takes effect in the book without a reinstall. Chapter 2, *Installing press*, covers installation in full.

::: {.sidebar}
> **Why CI does not install press from git**
>
> The requirements file installs press from git, but CI never reads that file. The composite action checks out the press at the exact ref the book's workflow names, and it installs the press from that checkout.
>
> The first reason is privacy. A book repository is often private while its author drafts. Because the action installs the press from its own checkout, a private book needs no token that reaches from one repository into another. The book's CI needs no secret for the press at all.
>
> The second reason is the pin. The installed press comes from the same checkout as the action, so the two always match the ref the workflow names. When a book pins `v3.0.2`, the press that builds it is the press at `v3.0.2`, and no separate install line can name some other version behind the action's back.
>
> The press records both reasons in its own *CLAUDE.md*, the guide for anyone who works on the press, and it forbids replacing the self-checkout install with pip from git.
:::

### A first local build

With the Alice book scaffolded, `alice` can run the checker before writing a word. Example 3.10 shows the result on a fresh scaffold. Two long lines of notes about the known-bad fixtures appear in the real output, and we elide them.

**Example 3.10. press check on a fresh scaffold**

```
$ press check
Source checks passed: 1 ordered Markdown files
...
Checker self-test passed: 19 known-bad fixtures each tripped their declared rule, known-good fixture accepted, 2 extra diagnostics noted
Editorial checks passed: 1 Markdown files
Jargon check passed: no rewrite-status terms (full audit in build/jargon-report.txt)
```

The "1 ordered Markdown files" is the preface. The self-test line says that every known-bad fixture the press ships still trips the rule it declares, which proves the checker still works before it judges your manuscript. The press runs those fixtures in `press check` and in `press all`, and not in a bare `press pdf`. Chapter 6, *Checking the manuscript*, takes the four passes apart.

The `press wordcount` target is the other one you will run daily. It prints one line per manuscript file and a total:

```
$ press wordcount
    42  book/chapters/00-preface.md
    42  TOTAL
```

It strips fenced and inline code before it counts. It does not strip HTML comments, so the art directions you write as comments count as words.[^wordcount]

The first time LuaLaTeX runs on a new machine, it scans the system fonts, and that scan takes several minutes. It looks like a hang. It is not one, although it is a convincing imitation.

## What git has to do with it

The scaffold leaves git to you. The press README gives the sequence as `cd my-book && git init && make all`, and the quick start in the press documentation ends with a first commit and a push. Example 3.11 shows that sequence for the Alice book.

**Example 3.11. Putting the Alice book under git**

```
$ cd alice
$ git init && git add -A && git commit -m "First book" && \
    git remote add origin https://github.com/wonderland-press/alice && \
    git push -u origin main
```

### What git gives the press

The reason to do this early is the Source edition. The artifact *alice-source.zip* contains the files git tracks and nothing else. A file you created but never added is missing from the zip, even though every other edition includes it. The `.gitignore` the scaffold writes works with this rule, because git never tracks *build/* or *dist/*, so a Source edition cannot contain an old build.

::: {.tip}
> **Tip:** Run `git add` on every new chapter file before a full build. The Source edition takes the manuscript from git, and it holds only what git tracks.
:::

### The CI file

The other reason is CI, which runs only on a repository that GitHub hosts. Example 3.12 shows the CI file the scaffold writes.

**Example 3.12. The scaffolded .github/workflows/book.yml**

```
name: Build book

on:
  push:
    branches: ["**"]
    tags: ["v*"]
  pull_request:
  workflow_dispatch:

permissions:
  contents: write
  packages: read
  pages: write
  id-token: write

jobs:
  book:
    uses: clintecker/press/.github/workflows/build.yml@v3
```

The file builds the book on a push to any branch, on any tag that starts with `v`, on every pull request, and on demand from the GitHub interface. It grants the job four permissions, and it hands all the work to one line: the press's reusable workflow at `v3`. That reusable workflow pins the composite action and the toolchain image, so the book never names either one. On the CI host, which in our examples is `printshop`, the job runs inside the toolchain image, pinned by digest to the bytes the release contract proved.

A tag push does two more things. It sets `PRESS_RELEASE=1`, which turns on the release refusal of Example 3.4, and it makes CI take the tag's section of *CHANGELOG.md* as the release notes. Chapter 14, *Continuous integration and the release contract*, covers the rest.

GitHub Pages needs one setting by hand. In the repository's settings, open Pages and set its Source to GitHub Actions. You do this once per book repository.

## Where things go: build and dist

A full build writes into two directories at the top of the book repository. The directory *dist/* holds every artifact the press publishes, and *build/* holds the intermediate files the press makes on the way. Git ignores both, and `press clean` deletes both.

@fig:dist-after-all shows *dist/* after `press all` for the Alice book. The registry in the press names every file in it, so the names are the same in every book except for the slug.

<!-- art: ARCHETYPE tree. A vertical trunk, names in monospace, rooted at "dist/", each stub with a right-aligned italic sans annotation on a thin leader ending in a dot. In order: "alice.pdf" Print edition; "alice.epub" Circulating edition; "alice.html" Single-leaf edition; "alice.md" Manuscript edition; "alice.txt" Telegraphic edition; "alice.docx" Office edition; "alice-site.zip" Chapter edition; "alice-source.zip" Source edition; "alice-sources.md" in a dashed outline, table of authorities; "site/" the reader; "pages/" the Pages bundle, with children "index.html" landing page, "read/" copy of site, "downloads/" every download, and "sitemap.xml" in a dashed outline. A 10% gray band groups the eight edition files. A 20% gray box around "pages/" makes the eye find first the part that goes public. Black and white. -->
![The dist directory after press all](assets/woodcuts/03-03-dist-after-all.png){#fig:dist-after-all .diagram width=full-measure fig-alt="A directory tree rooted at dist: eight edition files named alice, the optional table of authorities, the reader directory, and the Pages bundle with its landing page, reader copy, downloads, and sitemap."}

### The editions in dist

Each file at the top of *dist/* is one edition, and the registry gives each edition a name. The PDF is the Print edition, and the EPUB is the Circulating edition. The single HTML file is the Single-leaf edition, and it carries everything it needs inside itself. The Markdown file is the Manuscript edition, which press stitches together from your source files without running them through pandoc. The plain-text file is the Telegraphic edition, set at 80 columns, and the DOCX file is the Office edition.

The two zip files box the rest. The file *alice-site.zip* is the Chapter edition, the per-chapter reader in one download, and *alice-source.zip* is the Source edition. A book with *config/authorities.yaml* also gets *alice-sources.md*, the table of authorities, which the press publishes beside the book and never inside it.

The two directories are for the Web. The directory *site/* holds the per-chapter reader: an index page, the reader stylesheet, one page per chapter, and its assets.

The directory *pages/* is the bundle that GitHub Pages serves. It holds the landing page, a copy of the reader under *read/*, and every download under *downloads/*, each linked exactly once. It also carries the cover, the logo, and the plates when the book has them. A book with `site-url` gets *sitemap.xml* and *robots.txt*. A book with print ordering turned on and no policy URLs of its own gets generated support, privacy, and refund pages.

### Files press all does not make

The print pack builds only when you ask for it. Between them, the `press print`, `press verify-print`, and `press coverwrap` targets add *alice-interior.pdf* and *alice-coverwrap.pdf* to *dist/*. The registration targets add their own files: `press pcn` writes *alice-pcn.txt*, and `press onix` writes *alice.onix.xml*. The `press all` target makes none of these.

::: {.warning}
> **Warning:** Do not run a verifier over *dist/* and trust the result without a fresh build. Run `press all`, which rebuilds each artifact before it verifies it.
:::

The press learned that rule the hard way. Verifying an old *dist/* without rebuilding it proves only that last week's files were good, and a verifier that passes them blesses artifacts that no longer match the manuscript. The press now wires its targets to their dependencies so that a build target runs before the verifier that inspects its output. The invariant `INV-graph-no-stale` records the rule.

### The build directory

The directory *build/* is the press's workbench. You rarely need to open it, but when a build goes wrong, the evidence is here. The entries most worth knowing are these:

- The directory *build/defaults/* holds the pandoc defaults files the press renders.
- The directory *build/generated/* holds the generated subject index under its letter, such as *a-index-of-subjects.md*.
- The files *front-matter.tex*, *aesthetic.tex*, *profile-geometry.tex*, and *profile-dropcap.tex* hold the TeX the press generates from your config.
- The directory *build/print-assets/* holds flattened, print-safe copies of your images.
- The file *build/epub-metadata.xml* carries the year for the EPUB date, and *build/cover-fragment.html* sits beside it.
- The file *build/jargon-report.txt* holds the full jargon audit, and *build/verify-text.txt* sits beside it.
- The directory *build/rendered-book/* holds the page images that `press render` writes at 160 dpi.
- The files *build/editorial-report.md* and *build/editorial-rejections.md* come from the workflows.
- The file *build/cover/cover.png* and the directory *build/illustrations/* hold the art the art commands produce.

Two more places hold generated state outside *build/*. The `press migrate` target writes *.press/migration-receipt.json*, and the art commission writes candidate images under *art/candidates/*. Neither is an artifact.

The next chapter, *Writing the manuscript*, opens the chapter files themselves.

[^epubdate]: Pandoc emits an empty `dc:date` element, and epubcheck, the validator the retail channels run, rejects it under its rule RSC-005. The press writes the year it extracts into *build/epub-metadata.xml*.

[^printf]: The press documentation states the purpose in so many words: the target exists "so authors never printf > file".

[^wordcount]: The counter matches words with the pattern `\b[\w'-]+\b`, so a hyphenated compound counts as one word and a contraction counts as one.

<!-- index: press new; slug; book repository; book root; BOOK_ROOT; metadata.yaml; press config; sentinel; verify-sentinels; verify-min-pages; PRESS_RELEASE; vacuous witness; chapter file; appendix file; zero padding; press add; unnumbered heading; Makefile; requirements.txt; Source edition; book.yml; dist; build; press clean; press wordcount -->
