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
> - What Git has to do with it
> - Where things go: build and dist
:::

Every book that press builds lives in a *book repository*, a directory with *config/metadata.yaml* at its top and the manuscript under *book/*. The press creates that directory for you and names every file in it. It refuses to build in a directory that has no *config/metadata.yaml*. You will spend most of your working hours inside this one directory, so it pays to know what each file does and which program reads it. The running sample is the Alice book, slug `alice`, which the user `alice` writes on the workstation `hatter`.

## Scaffolding a book

The target that creates a book repository is `press new`. It takes one argument, the directory to create, and four options that set the identity of the book. The synopsis is:

```text
press new <directory> [--author A] [--publisher P]
          [--place PLACE] [--owner GH]
```

Table 3.1 lists the options and the value each one takes when you leave it out.

| Option | Meaning |
|----------------------|------------------------------------------------------|
| `--author` | This option sets the byline. Without it, press reads `git config user.name`, and if Git has no name either, it writes "The Author". |
| `--publisher` | This option sets the imprint. It defaults to the author, which suits a book you publish yourself. |
| `--place` | This option sets the place of the imprint. It defaults to "Earth". |
| `--owner` | This option names the GitHub account that will own the repository. With it, press writes live `repository` and `site-url` lines into the metadata file. Without it, those two lines stay commented out, with the word `OWNER` where the account belongs. |

Table: Table 3.1. press new options

The Alice book belongs to the GitHub account `wonderland-press`, and its author is Lewis Carroll, so `alice` gives both on the command line. Example 3.1 shows the whole session. The first line of output ends with the absolute path of the new directory, which we shorten here. We also cut the end of the second line, which goes on to tell you to run `press all`.

**Example 3.1. Scaffolding the Alice book**

```text
$ press new alice --author "Lewis Carroll" \
    --owner wonderland-press
scaffolded alice -> /.../alice
next: edit config/metadata.yaml, write book/chapters/, ...
$ cd alice
```

Every press target runs from the top of the book repository, so every later example in this chapter runs from inside *alice/*.

Behind those two lines of output, press does six things in a fixed order:

1. It refuses a path that already exists, so it can never overwrite a book.
2. It checks the directory name as a slug before it copies a single file.
3. It copies the book template from its own package data.
4. It renames every template file called `dot-` something to the matching dotfile.
5. It stamps its four agent workflows into *.claude/workflows/*.
6. It substitutes the slug, author, publisher, place, repository line, and site-url line into the copied files.

Because press checks the name before it copies anything, a refused name leaves no half-built directory behind for you to delete.

The directory name becomes the book's *slug*, the basename of every artifact the press produces. A slug must match the pattern `[a-z0-9][a-z0-9-]*`: lowercase letters, digits, and hyphens, starting with a letter or a digit. The Alice PDF is therefore *alice.pdf*, its EPUB is *alice.epub*, and so on through every edition. Neither `Alice` nor `my book` passes the slug test, and press refuses both.

::: {.tip}
> **Tip:** Choose the slug as if it were permanent. It names every file a reader downloads, and the scaffold writes it into the repository and Pages addresses as well.
:::

One step that press does not take is `git init`. The new directory is a plain directory, with no Git repository inside it yet. The section "What Git has to do with it" later in this chapter explains what the Source edition (the source zip) needs from Git.

## The tree, file by file

@fig:scaffold-tree shows the tree that `press new alice` leaves behind with press 3.0.2, the current version at the time of this writing.

![The tree that press new lays down](assets/woodcuts/03-01-scaffold-tree.png){#fig:scaffold-tree .diagram width=full-measure fig-alt="A directory tree rooted at alice, with one row for the agent workflows, the CI file, the preface, the changelog, the agent guide, three config files, the Makefile, and requirements.txt. Leader lines label the CI file, the metadata file, and the chapters directory."}

<!-- art: ARCHETYPE tree. A vertical trunk with horizontal stubs, names in monospace, rooted at "alice/". Thirteen rows in order: "alice/". ".claude/workflows/ (four files)". ".github/workflows/book.yml". ".gitignore". "book/chapters/00-preface.md". "CHANGELOG.md". "CLAUDE.md". "config/" with three children "front-matter.yaml", "house-rules.yaml", "metadata.yaml". "Makefile". "requirements.txt". Three italic sans annotations, right-aligned, each on a thin straight leader ending in a dot. At "book.yml": "the whole CI: calls the press's build.yml at v3". At "metadata.yaml": "identity, press facts, verification knobs". At "book/chapters/": "your chapters go here". Put "metadata.yaml" in a box with a 20% gray fill so the eye finds it first. Black and white, no icons. -->

Table 3.2 gives each file in the tree and what it does, in the order the tree lists them.

| Path | Meaning |
|--------------------------------------------|------------------------------------------------|
| *.claude/workflows/* | It holds four agent workflows. *aesthetic-brief.js* drafts *config/aesthetic.yaml* from a one-line brief, *art-direction.js* writes *art/commissions.md*, *authorities-research.js* builds *config/authorities.yaml*, and *editorial-passes.js* runs the iterative editorial machine. |
| *.github/workflows/book.yml* | It is the whole CI for the book. It calls the reusable workflow of the press at the floating tag `v3`. |
| *.gitignore* | It keeps `build/`, `dist/`, `__pycache__/`, and `.DS_Store` out of Git. |
| *book/chapters/00-preface.md* | It is a one-paragraph preface. It exists so that an empty book builds and verifies. |
| *CHANGELOG.md* | It is a changelog in the Keep a Changelog form. CI extracts the section for a tag and uses it as the release notes. |
| *CLAUDE.md* | It is the book's own guide for authors and agents, 79 lines on the layout, the commands, and the house laws. |
| *config/front-matter.yaml* | Every key in it starts commented out. The presence of the file alone turns on generated front matter. |
| *config/house-rules.yaml* | It holds the book's own house rules, empty at first: `banned-patterns: {}`, `jargon-allow: []`, and `audit-dirs: []`. |
| *config/metadata.yaml* | It holds the identity of the book, the press facts, and the verification knobs. |
| *Makefile* | It hands every target to `python3 -m press`. |
| *requirements.txt* | It names the press requirement for local builds. CI never reads it. |

Table: Table 3.2. The files of a fresh book repository

The house laws in *CLAUDE.md* are short enough to keep in your head. Use no em or en dashes and only straight quotes. Write sentence-case headings with no manual numbers. Keep to ASCII plus accented Latin letters, keep paragraphs under 190 words, and leave no trailing whitespace. The sentinels in the metadata file must survive every revision verbatim, and the fixtures under *tests/known-bad/* must stay rejected.

The first line of each workflow reads `// scaffolded by press 3.0.2; source of truth: press data/workflows`. After you upgrade press, that stamp tells you which version laid each file down. A stamp that names a different version from the press you run shows that your copy came from an older or newer press. Chapter 15, *The operator's desk and the editorial machines*, describes what the workflows do.

### The preface stub

The only manuscript file in a new book is the preface. Its first line is the heading `# Preface {.unnumbered}`, and one paragraph follows it: "Why this book exists, in your own voice, with no throat-clearing. Delete this sentence and the one before it; keep the heading. This paragraph only exists so a freshly scaffolded book builds and verifies before the first real word lands."

The paragraph tells you to replace it, and you should. Keep the heading line. The `{.unnumbered}` attribute keeps the preface out of the chapter numbering, as the section "Chapters, appendixes, and how they sort" later in this chapter explains.

### How press finds the book

Every press target starts by finding the *book root*. The press takes the directory named in the environment variable `BOOK_ROOT`, or else the current directory. That directory must contain *config/metadata.yaml*, and if it does not, press refuses with the message that the directory "is not a book". The press does not search upward through parent directories the way Git does. If `alice` runs `press check` from inside *book/chapters/*, the press refuses, because that directory holds no metadata file.

::: {.tip}
> **Tip:** If a script must run a press target from outside the book repository, set `BOOK_ROOT` to the book's directory first.
:::

### Files you add later

The scaffold writes only the files that every book needs. A book grows other files as its author asks more of the press, and each of them is optional. Three more config files hold the subject index terms, the table of authorities, and the book's visual identity: *config/index-terms.yaml*, *config/authorities.yaml*, and *config/aesthetic.yaml*. Chapter 10, *Front matter, the index, and the table of authorities*, and Chapter 9, *The house design*, cover them.

A hand-written *tex/title-page.tex* replaces the generated front matter, which Chapter 10 also covers. The directory *assets/* takes the cover, the logomark, the plates, and any Web stylesheet you add. The directory *art/* holds the commissions and the candidate images of Chapter 11, *The art department*. The directory *tests/known-bad/* holds the book's own known-bad fixtures, which Chapter 6, *Checking the manuscript*, describes.

## The metadata file

The file *config/metadata.yaml* is the one file that makes a directory a book. It holds the book's identity, the facts the press needs to name and publish the artifacts, and the knobs that tell the verifiers how hard to look.

The press reads the file through its *book model*, the typed set of rules it holds for every field. For each field, the model records the kind of value, whether the field must be present, and its default. Every build checks the file against the model, and Chapter 16, *Inside the press*, shows how the model works. Pandoc reads the raw file as well. Every pandoc defaults file names the metadata file as its `metadata-file`, so a standard pandoc key that you add here passes through to every edition.

Example 3.2 shows the start of the file as `press new alice` writes it, after the scaffold fills the placeholders. We cut two comment lines above `slug`. After `site-url`, the real file goes on with the verification knobs, which the section "Verification knobs" later in this chapter shows, and with commented lines for print and registrations. It ends with a commented block for direct print ordering, the last part of Example 3.2. We wrapped that block's opening comment to fit the page and cut the ends of four long lines.

**Example 3.2. The scaffolded config/metadata.yaml, in part**

```text
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

...
slug: "alice"
repository: "https://github.com/wonderland-press/alice"
site-url: "https://wonderland-press.github.io/alice"
...
# Direct print ordering: a reader-facing "Order a print
# copy" link to a provider-hosted checkout (Lulu, Peecho, a
# Bookvault store, ...). The provider is the seller of record
# and owns payment, tax, fulfillment, and support; this block
# holds only URLs and a name, never a credential or a price.
# Enable it once the edition is qualified (press qualify).
# A policy link is optional: give a URL to link your own
# hosted page, or omit it and press generates an honest page
# on your book site. Add policies: {support,privacy,refund}
# text to append your own words.
# commerce:
#   print-ordering:
#     enabled: true
#     edition: paperback
#     storefront-url: "https://www.lulu.com/shop/..."
#     seller-of-record: "Lulu"     # who the reader ...
#     support-url: "https://example.test/support"   ...
#     # privacy-url / refund-url omitted -> press ...
#     policies:
#       privacy: "We keep no reader data; the provider ...
```

Two lines of that commerce comment need a gloss. It says to enable ordering "once the edition is qualified (press qualify)", but at the time of this writing press has no `press qualify` command. You record the qualification by hand in *config/qualification.yaml*. The comment also says that the provider is the seller of record. That is the model press builds on, provider as seller, and the publisher must confirm with the provider who sells to the reader. Chapter 12, *The print pack*, covers direct print ordering.

Notice what the scaffold could not know. The title is the slug, the subtitle is a placeholder, and the description says what a description should say. A new book builds with all three as they stand, but all three appear on the title page and the landing page.

### Identity

The first block of the file names the book. Table 3.3 gives each field, its default, and what the press does with it. The model needs three fields: the title, the author, and the slug.

| Field | Default | Meaning |
|---------------------|------------------|--------------------------------------------|
| `title` | none, required | It is a string that holds the book's title. |
| `subtitle` | none | It is a string. If it joins clauses with "or," the title page and the landing page stack them on separate lines. |
| `author` | none, required | It is the byline, one name per list item. A single string becomes a one-item list. |
| `date` | none | It is free text. The press takes the first year in it (a four-digit number beginning 1 or 2) for the EPUB date and for the lowercase roman numerals on the title page. |
| `lang` | none | It is a BCP-47 language tag, which press passes through to pandoc. The template sets `en-US`. |
| `copyright` | none | It is the copyright line. Once *config/front-matter.yaml* exists, the model needs it. |
| `publisher` | none | It is the imprint. The model needs it with front matter. The press also exports it to TeX as the environment variable `BOOK_PUBLISHER`. |
| `publisher-place` | none | It is the place of the imprint. The model needs it with front matter. |
| `description` | none | It is a one-sentence blurb for the landing page and the stores. The `press check` target refuses a book without one. |
| `keywords` | none | It is a list of subject keywords, which press passes to the editions. |
| `rights` | none | It is a rights statement, which press passes through to pandoc, except in the EPUB, where the press sets its own `--metadata rights=` value. |

Table: Table 3.3. Identity fields in metadata.yaml

The date field explains a small mystery in the EPUB. Pandoc writes an empty date into the EPUB, and epubcheck rejects an empty date. The press therefore pulls the year out of your free-text date and writes it into the EPUB metadata itself.[^3-epubdate] A date such as "First edition, 2026" gives the EPUB the year 2026 and gives the title page its roman numerals, so you never type the year twice.

Because the scaffold writes *config/front-matter.yaml*, a new book has front matter switched on from the first build. The scaffold fills `copyright`, `publisher`, and `publisher-place`, which the model needs once front matter is on. If you delete any of the three while the front-matter file exists, the model refuses the metadata.

### Press facts

The second block holds three facts the press needs to publish: the slug, the repository, and the public address. Table 3.4 lists them with the verification knobs that follow them in the file.

| Field | Default | Meaning |
|---------------------|-------------------|--------------------------------------------|
| `slug` | none, required | It is the basename of every artifact. It must match `[a-z0-9][a-z0-9-]*`. |
| `repository` | none | It is the canonical repository URL. Without it, the landing page leaves out its paragraph about the source repository. |
| `site-url` | none | It is the public GitHub Pages URL and the one authority for every absolute URL the press writes: canonical links, the `og:image`, and the sitemap. Without it, the press writes nothing shaped like a URL. |
| `verify-sentinels` | `[]` | It is a list of phrases that the verifiers must find in the manuscript and in every artifact. A release needs at least two. |
| `verify-min-pages` | 40 (template: 1) | It is the floor for the PDF page count. A release needs at least 24. |

Table: Table 3.4. Press facts and verification knobs

The rule for `site-url` follows from the first law of the press: "Facts are stated once." A book that leaves the field out gets no sitemap, no canonical links, and no absolute download links.

### Verification knobs

A *sentinel* is a phrase from your manuscript that the verifiers must find, character for character, in the manuscript and in every artifact. If the PDF, the EPUB, or the Telegraphic edition (the plain text) loses a chapter on the way out, a sentinel from that chapter goes missing. The verifier then fails. Matching uses exact case, and the verifiers treat curly and straight quotes as equal.

The template's own advice for choosing them is good: "pick 2-4 phrases from your actual manuscript, each distinctive enough to appear exactly once (a whole memorable clause, not a common word)". For Alice we will use two lines of verse from the middle of their chapters, "Twinkle, twinkle, little bat" and "she made some tarts".

::: {.warning}
> **Warning:** Never take a sentinel from the first words of a chapter. A chapter opening can set the first word as one large capital followed by small capitals. The PDF then no longer contains the phrase as you typed it.
:::

The *page floor*, the fewest pages the PDF may have, is the second knob. The PDF verifier fails a PDF with fewer pages than `verify-min-pages`. The model's default of 40 suits a finished book. The template writes 1 so that a new book with nothing but its preface stub passes on the first day.

Both settings of the template are draft settings. When CI builds a tag whose name starts with `v`, it sets the environment variable `PRESS_RELEASE=1`. The press then demands its *release witnesses*: at least two sentinels and a page floor of at least 24. It refuses draft knobs as *vacuous witnesses*, too weak to prove anything. Example 3.3 shows the refusal that a freshly scaffolded book draws at its first tagged release. We fold its first line to fit the page and cut the end of the second.

**Example 3.3. The release refusal for draft knobs**

```text
this is a release build (PRESS_RELEASE=1) and its witnesses
    are vacuous:
verify-sentinels has 0 entries; a release needs at least 2 ...
verify-min-pages is 1; a release needs at least 24
```

Do not set the real knobs on the first day. A sentinel must already appear in the manuscript, and the PDF must already reach the floor, or every build fails. Once the chapters hold both phrases and the PDF runs past 24 pages, `alice` sets them:

```text
$ press config set verify-sentinels \
    '["Twinkle, twinkle, little bat", "she made some tarts"]' \
    --json
$ press config set verify-min-pages 24
```

### Print, chapter openings, and registrations

The rest of the fields gather under four mappings, `print`, `chapter-opening`, `registrations`, and `commerce`. A new book needs none of them. Table 3.5 gives the ones you will reach for first, with their defaults.

| Field | Default | Meaning |
|------------------------------------|------------------|------------------------------------|
| `print.profile` | `house-6x9` | It names the design profile, which sets the trim and the interior geometry. |
| `print.provider` | `house` | It names the provider spec, which sets the spine and cover geometry. |
| `print.binding` | `perfect-bound` | It takes `perfect-bound`, `saddle-stitch`, `coil`, `casewrap`, or `dust-jacket`. |
| `print.material` | `paperback` | It names the cover material: `paperback`, `casewrap`, or `linen`. |
| `print.paper` | `cream` | It names the interior stock: `white` or `cream`. |
| `print.page-thickness` | none | It gives inches per page. When you set it, it overrides the paper. |
| `chapter-opening.style` | the profile's | It takes `none`, `drop-cap`, `raised-cap`, or `ornate`. The house profile uses `none`. |
| `chapter-opening.lines` | 3 | It gives the number of text lines the large first letter spans. |
| `registrations.isbn.print` | none | It holds the print ISBN, as 13 digits or the word `pending`. The EPUB ISBN goes in `registrations.isbn.epub`. |
| `registrations.retail` | false | When it is true, `press check` refuses a missing or pending ISBN and any declared LCCN or ISSN still pending. |

Table: Table 3.5. The first print and registration fields

One field in this part of the model looks settable and is not. The press derives `trim` from the profile, and it refuses a direct write with the message "trim is not set directly; choose it with print.profile". An older book that still carries a `trim` mapping keeps it. The press checks that mapping against the profile and refuses the metadata when the two disagree. Chapter 9 covers the profiles and chapter openings. Chapter 12 covers the print fields, and Chapter 13, *Registrations*, covers the numbers.

## Reading and writing config from the shell

You can edit the metadata file in any text editor, and many authors do. The press also gives you a target, `press config`, that reads and writes every field from the shell. It has five subcommands:

```text
press config get|set|unset|list|validate
```

The reason to prefer it is validation. Before `press config set` touches a byte on disk, it runs the new value through the book model, the same rules a build checks. A value the model refuses never reaches the file. For the metadata file, the check includes the commerce and registration rules. For the house rules, it compiles each regular expression. The one exception is *config/aesthetic.yaml*, which has no typed model of its own.

Example 3.4 is a captured session on a fresh scaffold. It reads two fields, changes the subtitle, tries a change with `--dry-run`, and removes the subtitle again. We cut the end of one long context line and the last three lines of the dry-run diff.

**Example 3.4. Reading and changing fields with press config**

```text
$ press config get author
["Lewis Carroll"]
$ press config get subtitle
A subtitle
$ press config set subtitle "A tale for a summer afternoon"
--- a/metadata.yaml
+++ b/metadata.yaml
@@ -1,5 +1,5 @@
 title: "alice"
-subtitle: "A subtitle"
+subtitle: "A tale for a summer afternoon"
 author:
   - "Lewis Carroll"
 date: "First edition, 2026"
$ press config get subtitle
A tale for a summer afternoon
$ press config set verify-min-pages 24 --dry-run
--- a/metadata.yaml
+++ b/metadata.yaml
@@ -25,7 +25,7 @@
 # DRAFT settings; a release build (CI on a tag) refuses ...
 # least 2 sentinels and verify-min-pages >= 24 are set.
 verify-sentinels: []
-verify-min-pages: 1
+verify-min-pages: 24
...
(dry run: nothing written)
$ press config unset subtitle
--- a/metadata.yaml
+++ b/metadata.yaml
@@ -1,5 +1,4 @@
 title: "alice"
-subtitle: "A tale for a summer afternoon"
 author:
   - "Lewis Carroll"
 date: "First edition, 2026"
```

The `press config get` subcommand prints the value of a field: a list as JSON, and anything else as the bare string. Every `set` and `unset` prints a unified diff of the change it made to the file. With `--dry-run`, the press prints the same diff and then "(dry run: nothing written)", and the file stays as it was.

Example 3.5 lists the commands `alice` runs next to give the book its real identity. The title contains an apostrophe, so the shell needs double quotes around it. We leave out the diff that each command prints.

**Example 3.5. Setting the Alice book's identity**

```text
$ press config set title "Alice's Adventures in Wonderland"
$ press config set description "A girl falls into Wonderland."
$ press config set keywords '["fantasy", "children"]' --json
$ press config set print.paper white
```

Three rules govern the values you type. A list or a mapping must be JSON, with the `--json` option, as the keywords line shows. A boolean accepts `true`, `yes`, `on`, or `1`, and `false`, `no`, `off`, or `0`. Some fields, such as `print.paper` and `print.binding`, take a fixed set of choices, which Table 3.5 lists.

### Where each field lives

The `press config` target knows which file holds each field, so you name the field and not the file. Table 3.6 shows the routing.

| Fields | File |
|--------------------------------------------------|---------------------------------|
| Identity, verification, and every `print`, `chapter-opening`, `registrations`, and `commerce` field | *config/metadata.yaml* |
| `banned-patterns`, `jargon-allow`, and `audit-dirs` | *config/house-rules.yaml* |
| `edition-note` through `motto`: the dedication, the epigraph, the acknowledgments, and the colophon lines | *config/front-matter.yaml* |
| `name` through `book-colors`: the cover, the plates, the logomark, the portrait, the typography, and the palettes | *config/aesthetic.yaml* |

Table: Table 3.6. Where press config writes each field

### Kinds of field

Each field has one of four kinds. A *writable* field takes `set` and `unset`. An *immutable* field, such as `trim`, refuses writes and says what to change instead. A *structured* field holds data too rich for one command line: the index terms, the table of authorities, and the qualification records. The press sends you to the file or the workflow that maintains it. A *file* field is a whole file, such as *tex/title-page.tex* or the assets, and the press tells you where to put it.

The `press config list` target prints every field with its type and a one-line description. It is the quickest reference while you work. For a field you cannot set from the shell, it adds a second line that begins with an arrow and says where to go instead.

### Validating after a hand edit

If you edit the YAML by hand, run `press config validate` afterward. It prints one line for every config file the press knows, including the optional ones the book does not have yet. It reports an absent file as `ok`. Example 3.6 shows the run on a fresh scaffold. Three of the six files do not exist yet: Chapters 9 and 10 add the aesthetic, the index terms, and the table of authorities.

**Example 3.6. press config validate**

```text
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

The press finds the manuscript by filename, and it never reads a table of contents. A *chapter file* is a file in *book/chapters/* whose name matches `[0-9]*.md`: it starts with a digit and ends in `.md`. An *appendix file* is a file in *book/appendices/* whose name matches `[a-z]-*.md`: a single lowercase letter, a hyphen, and anything ending in `.md`.

The press sorts each group by filename. It merges the chapters first, then the appendixes in the order of their letters, and the generated subject index takes its place among the appendixes by its own letter.

::: {.warning}
> **Warning:** Start every chapter filename with a digit and every appendix filename with a letter and a hyphen. The press skips any other Markdown file in those two directories without a message, so a chapter saved as *chapter-two.md* never reaches the book.
:::

If neither directory yields a single file, the press refuses with `FileNotFoundError("no manuscript files found under book/")`. The scaffold's preface keeps a new book clear of this refusal.

### Lexical order and zero padding

The sort compares filenames character by character, and it knows nothing about numbers. @fig:how-files-sort shows the consequence. A chapter named *10-the-lobster-quadrille.md* sorts before *2-the-pool-of-tears.md*, because the character `1` comes before `2`. With zero padding the problem disappears: *02-* sorts before *10-*, and the book reads in order. The appendix row of the figure shows the second rule, the letters.

The `press add appendix` target takes the next free letter, counting down from `z`. In the Alice book, *about-the-author* becomes *z-about-the-author.md*, and *glossary* becomes *y-glossary.md*. The generated subject index takes the first free letter counting up from `a`, and the press never assigns it `z`. The index file is therefore usually *a-index-of-subjects.md*, and by its letter it sorts first among the appendixes in the merged book. If you add the same back matter with `press add appendix --front`, the letters count up from `a` instead: *a-about-the-author.md*, then *b-glossary.md*, and the index takes `c`.

![How press sorts chapter and appendix files](assets/woodcuts/03-02-how-files-sort.png){#fig:how-files-sort .diagram width=full-measure fig-alt="Four directory listings. Unpadded chapters sort 1, 10, 2 and padded ones 01, 02, 10. Appendixes added from z leave the index at a, ahead of them. Appendixes added with front take a and b and leave the index at c."}

<!-- art: ARCHETYPE before/after, two rows of paired frames, (a) and (b) above (c) and (d), each label under its frame. Each plain rectangle holds a monospace listing, with the order beneath in small sans. (a) "1-down-the-rabbit-hole.md", "10-the-lobster-quadrille.md", "2-the-pool-of-tears.md", order "1, 10, 2", with an italic callout "sorts too early" on the "10" line. (b) "01-down-the-rabbit-hole.md", "02-the-pool-of-tears.md", "10-the-lobster-quadrille.md", order "1, 2, 10". (c) italic label "press add appendix": "a-index-of-subjects.md" in a dashed box marked "generated", then "y-glossary.md", "z-about-the-author.md". Beneath: "index A first". (d) italic label "press add appendix --front": "a-about-the-author.md", "b-glossary.md", then "c-index-of-subjects.md" in the dashed box. Beneath: "index C last". The reader should see first that frame (a) puts 10 before 2. -->

::: {.tip}
> **Tip:** Pad chapter numbers to two digits from the first chapter. If you expect more than 99 chapters, pad to three, and rename the whole set at once.
:::

### Front parts and unnumbered headings

A preface, a foreword, or an introduction is a chapter whose filename starts with `00-`. The scaffold's preface is one. Its heading keeps such a chapter out of the numbering. A level-one heading with the attribute `{.unnumbered}`, or its short form `{-}`, gets no chapter number and no chapter opening. The scaffold's preface heading uses the long form.

The press has no parts. In the PDF and the EPUB it sets pandoc's `top-level-division` to `chapter`. In every edition a level-one heading (`#`) starts a chapter, and nothing groups chapters above that level. A book that wants "Part One" and "Part Two" pages cannot have them at the time of this writing.

## Adding a chapter

You can create a chapter file in any editor, as long as you get the name right. The press offers a target that gets it right for you:[^3-printf]

```text
press add chapter|appendix <name> [--front]
```

The `press add` target turns the name into a filename. It lowercases the name and replaces each run of characters that are not letters or digits with one hyphen. For the heading, it keeps a human title exactly as you typed it. A chapter gets the number one past the highest existing chapter, zero-padded to at least two digits. The first chapter of a book is `01`.

Example 3.7 shows `alice` adding the first chapter and two pieces of back matter, then listing the two directories and the new chapter file. Each `press add` prints `created` and the path of the new file. We cut the end of the last line.

**Example 3.7. Adding a chapter and two appendixes to the Alice book**

```text
$ press add chapter "Down the rabbit-hole"
created book/chapters/01-down-the-rabbit-hole.md
$ press add appendix about-the-author
created book/appendices/z-about-the-author.md
$ press add appendix glossary
created book/appendices/y-glossary.md
$ ls -1 book/chapters book/appendices
book/chapters:
00-preface.md
01-down-the-rabbit-hole.md

book/appendices:
y-glossary.md
z-about-the-author.md
$ cat book/chapters/01-down-the-rabbit-hole.md
# Down the rabbit-hole

Write this part here. This placeholder paragraph only ...
```

The chapter's heading is the title exactly as `alice` typed it. A name typed in filename form gets a sentence-case heading, so `the-pool-of-tears` would become `# The pool of tears`. The placeholder paragraph reads in full: "Write this part here. This placeholder paragraph only exists so the file is valid Markdown that builds; delete it and begin."

The `--front` option changes where the new file goes. With `chapter`, it creates a `00-` file with an `{.unnumbered}` heading, like the scaffold's preface. In a book without a preface, `press add chapter preface --front` creates *book/chapters/00-preface.md*. With `appendix`, the option counts up from `a` instead of down from `z`. When all 26 letters are in use, `press add appendix` refuses with "the appendices are full".

::: {.warning}
> **Warning:** Do not expect `press add` to replace a file. It refuses to overwrite an existing file and exits with status 1. A usage mistake exits with status 2.
:::

## The Makefile and local builds

Some authors type `make` before they think. The scaffold respects that habit with a *Makefile* that does nothing on its own. Example 3.8 shows the file in part. The real file lists all 16 targets on both of its long lines, and we cut the end of the comment.

**Example 3.8. The scaffolded Makefile, in part**

```text
# Muscle-memory wrapper; the pipeline itself lives in ...
PRESS ?= python3 -m press

.PHONY: all check pdf epub html ...

all check pdf epub html ...:
	$(PRESS) $@
```

The 16 targets are `all`, `check`, `pdf`, `epub`, `html`, `markdown`, `site`, `txt`, `docx`, `pages`, `source`, `verify`, `verify-formats`, `render`, `wordcount`, and `clean`. Every one of them runs the same recipe. The automatic variable `$@` holds the name of the target, so `make pdf` runs `python3 -m press pdf` and `make all` runs `python3 -m press all`. The press does all the work, and the dependencies between targets live in the press, not in the Makefile. That is why the file declares every target `.PHONY`: make(1) has no files to compare, and it must always hand the request on.

The `?=` assignment lets you replace the command. If `press` is on your path as a program, `make pdf PRESS=press` uses it directly. The press has more targets than the Makefile names, such as `print` and `coverwrap` for the print pack, and for those you run `press` itself.

### The requirements file

The second file for local builds is *requirements.txt*. Example 3.9 shows it with the ends of its first two lines cut. In full, its comment reads: "Local builds. CI does not read this file; the press action installs itself from its own checkout. For day-to-day work prefer an editable install of your press clone: pip install -e ~/path/to/press".

**Example 3.9. The scaffolded requirements.txt**

```text
# Local builds. CI does not read this file; the press ...
# from its own checkout. For day-to-day work prefer an ...
# your press clone: pip install -e ~/path/to/press
press @ git+https://github.com/clintecker/press@v3
```

The last line installs press from its repository at the floating tag `v3`. The comment gives better advice for day-to-day work: install your own clone of press in editable mode. A change to that clone then takes effect in the book without a reinstall. Chapter 2, *Installing press*, covers installation in full.

::: {.sidebar}
> **Why CI does not install press from Git**
>
> The requirements file installs press from Git, but CI never reads that file. The composite action checks out the press at the action ref that the reusable workflow pins, and it installs the press from that checkout.
>
> The first reason is privacy. Because the action installs the press from its own checkout, a private book needs no cross-repository token.
>
> The second reason is the pin. The installed press comes from the same checkout as the action, so the two always match that ref. When a book pins `v3.0.2`, the press that builds it is the press at `v3.0.2`. No separate install line can name some other version behind the action's back.
>
> The press records both reasons in its own *CLAUDE.md*, the guide for anyone who works on the press. It forbids replacing the self-checkout install with pip from Git.
:::

### A first local build

A full build needs the toolchain from Chapter 2: pandoc, LuaLaTeX, latexmk, and the rest. With the toolchain in place, `alice` runs `press all` and then lists *dist/*. The build does not need Git, so it can run before `git init`. Example 3.10 shows the same run on the press's own three-chapter Alice example, which also has one appendix, with its slug changed to `alice`. We cut it to the lines that mark each stage and cut the ends of long lines.

**Example 3.10. press all on the three-chapter example, in part**

```text
$ press all
Source checks passed: 4 ordered Markdown files
...
Checker self-test passed: 19 known-bad fixtures ...
Editorial checks passed: 4 Markdown files
Jargon check passed: no rewrite-status terms ...
...
+ stitched 4 files -> dist/alice.md
...
+ assembled pages site -> dist/pages
...
Verified archives: alice-site.zip, alice-source.zip
...
commerce release gate: print ordering is not enabled; ...
...
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

The run follows a fixed order. First come the four passes of the checker: the source checks, the checker self-test, the style audit, and the jargon lint. The four files are its three chapters and its appendix. Next, pandoc builds each edition, and the press prints every pandoc command line with a leading `+`. The press then stitches the Manuscript edition (the raw Markdown), packs the Source edition, and assembles the Pages bundle. The verifiers run last, and the commerce release gate only reports, because print ordering is off.

The self-test line says that every known-bad fixture that comes with the press still trips the rule it declares. That line proves the checker works on known-bad input. The press runs those fixtures in `press check` and in `press all`, and not in a bare `press pdf`. Chapter 6 takes the four passes apart, and Chapter 8, *Verifying the artifacts*, covers the verifiers. On a machine without epubcheck, the run also prints a warning that it validated the EPUB structurally only, and the toolchain image runs the full check in CI.

The first time LuaLaTeX runs on a new machine, it scans the system fonts, and that scan takes several minutes. It is not a hang, although it is a convincing imitation of one. Let it finish.

The other refusals a first build is likely to meet are short and plain. The message `pandoc is required` means the toolchain is missing. A failure in the style audit or the jargon lint names the file and the rule. The checker prints `sentinel not found in the manuscript:` when a sentinel is missing from the manuscript. A verifier that cannot find a sentinel in an artifact prints its own form, such as `missing text sentinel in PDF:` or `<label> missing sentinel:`.

The `press wordcount` target is the one you will run daily. It prints one line per manuscript file and a total. On a fresh scaffold it looks like this, and yours now lists the new files too:

```text
$ press wordcount
    42  book/chapters/00-preface.md
    42  TOTAL
```

It strips fenced and inline code before it counts. It does not strip HTML comments, so the art directions you write as comments count as words.[^3-wordcount]

## What Git has to do with it

The scaffold leaves Git to you. The press README gives the sequence as `cd my-book && git init && make all`. The quick start in the press documentation ends with a first commit and a push. Before the push, create an empty repository named `alice` under the `wonderland-press` account on GitHub. Example 3.11 shows the rest for the Alice book.

**Example 3.11. Putting the Alice book under Git**

```text
$ git init && git add -A && git commit -m "First book" && \
    git remote add origin \
    https://github.com/wonderland-press/alice && \
    git push -u origin main
```

### What Git gives the press

The reason to do this early is the Source edition. The artifact *alice-source.zip* contains the files Git tracks and nothing else. A file you created but never added is missing from the zip, even though every other edition includes it. Before `git init`, `press all` still builds and verifies *alice-source.zip*. A book outside any repository is archived whole, less *build/*, *dist/*, and caches, but a book that sits untracked inside another repository archives nothing until Git tracks its files. The `.gitignore` the scaffold writes keeps *build/* and *dist/* out of Git. A Source edition therefore cannot contain old artifacts.

### The CI file

The other reason is CI, which runs only on a repository that GitHub hosts. Example 3.12 shows the CI file the scaffold writes.

**Example 3.12. The scaffolded .github/workflows/book.yml**

```text
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

With this file, CI builds the book on a push to any branch, on a tag that starts with `v`, on a pull request, or on demand. The file grants the job four permissions, and it hands all the work to one line: the reusable workflow at `v3`. The reusable workflow pins the composite action and the toolchain image, so the book never names either one.

On the CI host, which in our examples is `printshop`, the job runs inside the toolchain image. The reusable workflow pins that image by digest to the bytes the release contract proved. If a CI run dies at the step "Initialize containers", run it again. The image is public, and the step needs no secret.

On a tag push, CI does two more things. It sets `PRESS_RELEASE=1`, which turns on the release refusal of Example 3.3. It also takes the tag's section of *CHANGELOG.md* as the release notes. Chapter 14, *Continuous integration and the release contract*, covers the rest.

GitHub Pages needs one setting by hand. In the repository's settings, open Pages and set its Source to GitHub Actions. You do this once per book repository.

## Where things go: build and dist

A full build writes into two directories at the top of the book repository. The directory *dist/* holds every artifact the press publishes, and *build/* holds the intermediate files the press makes on the way. Git ignores both, and `press clean` deletes both.

@fig:dist-after-all shows *dist/* after `press all` for the Alice book. The registry in the press names every file in it, so the names are the same in every book except for the slug.

![The dist directory after press all](assets/woodcuts/03-03-dist-after-all.png){#fig:dist-after-all .diagram width=full-measure fig-alt="A directory tree rooted at dist: eight edition files named alice, the optional sources companion, the reader directory, and one row for the Pages bundle. Each edition file carries its edition name."}

<!-- art: ARCHETYPE tree. A vertical trunk with horizontal stubs, names in monospace, rooted at "dist/". Twelve rows, each but the root with a right-aligned italic sans annotation on a thin straight leader ending in a dot. In order: "dist/". "alice.pdf": Print edition. "alice.epub": Circulating edition. "alice.html": Single-leaf edition. "alice.md": Manuscript edition. "alice.txt": Telegraphic edition. "alice.docx": Office edition. "alice-site.zip": Chapter edition. "alice-source.zip": Source edition. "alice-sources.md" in a dashed outline: sources companion, only with config/authorities.yaml. "site/": the per-chapter reader. "pages/": the GitHub Pages bundle (see Chapter 14). A 10% gray band behind the eight edition rows groups them. A 20% gray box around "pages/" makes the eye find first the part that goes public. Black and white, no icons. -->

### The editions in dist

The first eight files in @fig:dist-after-all are the editions, and the registry gives each edition a name. The PDF is the Print edition, and the EPUB is the Circulating edition. The single HTML file is the Single-leaf edition, and it carries everything it needs inside itself. The Manuscript edition is the Markdown file, which press stitches together from your chapter files and appendix files without running them through pandoc. The Telegraphic edition is the plain-text file, set at 80 columns, and the DOCX file is the Office edition.

The two zip files box the rest. The file *alice-site.zip* is the Chapter edition, the per-chapter reader in one download, and *alice-source.zip* is the Source edition. A book with *config/authorities.yaml* also gets *alice-sources.md*, the sources companion, which the press publishes as a separate file in *dist/*.

The two directories are for the Web. The directory *site/* holds the per-chapter reader: an index page, the reader stylesheet, one page per chapter, and its assets.

The directory *pages/* is the Pages bundle, which GitHub Pages serves. It holds the landing page, a copy of the reader under *read/*, and every download under *downloads/*. The landing page links each download exactly once. The bundle also includes the cover, the logomark, and the plates when the book has them. A book with `site-url` gets *sitemap.xml* and *robots.txt*. A book with print ordering turned on and no policy URLs of its own gets generated support, privacy, and refund pages.

### Files `press all` does not make

The print pack builds only when you ask for it. Between them, the `press print`, `press verify-print`, and `press coverwrap` targets add *alice-interior.pdf* and *alice-coverwrap.pdf* to *dist/*. The registration targets add their own files: `press pcn` writes *alice-pcn.txt*, `press onix` writes *alice.onix.xml*, and other targets write the publish checklists that Chapter 12 describes. In a book without print ordering, `press all` makes none of these.

::: {.warning}
> **Warning:** Do not run a verifier over *dist/* and trust the result without a fresh build. Run `press all`, which rebuilds each artifact before it verifies it.
:::

A verifier run over an old *dist/* proves only that last week's files were good. When it passes them, it accepts artifacts that no longer match the manuscript. The press now wires its targets to their dependencies so that a build target runs before the verifier that inspects its artifact.

### The build directory

The directory *build/* is the press's workbench. You rarely need to open it, but when a build goes wrong, the evidence is here. If pandoc does something you did not expect, read the defaults file it used under *build/defaults/*, such as *pdf.yaml*. If the front matter or the page geometry looks wrong, read the TeX the press generated from your config. It lives in *build/front-matter.tex*, *build/aesthetic.tex*, *build/profile-geometry.tex*, and *build/profile-dropcap.tex*.

After a jargon failure, *build/jargon-report.txt* holds the full audit. To look at the PDF page by page, run `press render`, which writes page images at 160 dpi into *build/rendered-book/*. The generated subject index lives under *build/generated/*, with its letter in its name, and the flattened, print-safe copies of your images live under *build/print-assets/*. The EPUB date comes from *build/epub-metadata.xml*.

Two more places hold generated state outside *build/*. The `press migrate` target writes *.press/migration-receipt.json*, and `press art commission` writes candidate images under *art/candidates/*. Neither is an artifact.

Chapter 4, *Writing the manuscript*, opens the chapter files themselves.

[^3-epubdate]: Epubcheck, the tool the retail channels run, rejects the empty `dc:date` element under its rule RSC-005. The press writes the year it extracts into *build/epub-metadata.xml*.

[^3-printf]: The source of `press add` states the purpose plainly. It exists so that authors never `printf > file`.

[^3-wordcount]: The counter matches words with the pattern `\b[\w'-]+\b`, so a hyphenated compound or a contraction counts as one word.
