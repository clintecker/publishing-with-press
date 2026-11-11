# Front matter, the index, and the table of authorities

::: {.in-this-chapter}
> **In this chapter:**
>
> - What press generates and what it does not
> - The front-matter file, key by key
> - The title page and the stacked subtitle
> - The copyright page
> - Overriding the front matter
> - The subject index
> - The table of authorities
> - The sources companion
:::

A book has pages before its first chapter, and most of them restate facts the book already holds. Press builds those pages from configuration, so the title on the title page cannot disagree with the title in the metadata. After the last chapter, it builds a subject index from a list of terms. It also checks a ledger of sources against the prose on every build and publishes that ledger as a separate document. The examples continue with the Alice book, which user `alice` keeps on the workstation `hatter`.

## What press generates and what it does not

The first law of the press reads "Facts are stated once." The title, the author, the copyright line, and the imprint already live in *config/metadata.yaml*. The press projects them onto the front pages and never asks you to type them again. The pages that hold new facts, such as a dedication or an epigraph, get their own small file, *config/front-matter.yaml*. Between them, the two files give the press everything it needs to set the opening pages of the Print edition, the PDF.

The press generates two parts inside the book and one document beside it. The first part is the *front matter*, the run of pages from the cover plate through the acknowledgments. The second is the *subject index*, an appendix built from *config/index-terms.yaml*. The document beside the book is the *table of authorities*, a ledger of claims and sources in *config/authorities.yaml*. The press checks the ledger against the manuscript and publishes it as a companion file, never as a page of the book.

Some book parts look as if a machine should write them, and the press leaves them to you. Table 10.1 lists them.

| Book part | Meaning |
|---------------------|--------------------------------------------------------------|
| Glossary | You write it as an appendix of definition lists. The press neither generates it nor checks it, and the press calls a generated glossary "a feature to ask for". |
| Also by, or further reading | You write it. A catalog that spans several books is planned work, and nothing generates the page today. |
| About the author | You write it as an appendix. Run `press add appendix about-the-author` and the press creates *z-about-the-author.md* for you to fill. |
| Half-title | The press sets a cover plate and a title page, but it has no separate half-title leaf. Do not plan one for a book that uses generated front matter. |

Table: Table 10.1. Book parts the press does not generate

## The front-matter file, key by key

The scaffold writes *config/front-matter.yaml* into every new book, with every key commented out. The file matters even while it is empty, so a new book gets generated front matter from its first build.

The file opens with a comment of eight lines. It says that the file's presence asks the press "to generate the PDF's title page, colophon, and surrounding pages from config", and that you opt out if you delete the file or supply *tex/title-page.tex*. It adds that "absent sections simply do not render", and that the identity facts "come from metadata.yaml and are never restated here." Example 10.1 shows the keys that follow the comment. The excerpt leaves out that opening comment, a three-line comment on the colophon keys, the sample text under the three folded keys, and the sample `motto` line.

**Example 10.1. The keys of the scaffolded config/front-matter.yaml**

```text
...
# dedication: "For the night shift."

# epigraph:
#   quote: "The devil did it."
#   attribution: "Every printer, since printing began"

# acknowledgements: >-
...
# edition-note: "first edition, second printing"
# manufacture: "Published in the United States of America"
# colophon-note: >-
...
# rights-notice: >-
...
# contact: "you@example.com"
...
```

Every key is optional, and a key you leave out produces nothing, not even a blank line. The identity facts stay in *config/metadata.yaml*, and the file never repeats them.[^10-devil]

Table 10.2 gives each key and what it holds. Six of the keys fill lines of the copyright page, and Table 10.4, later in this chapter, gives those lines in order.

| Key | Meaning |
|-------------------|----------------------------------------------------------------|
| `dedication` | It holds a short line, and the press sets it on a page of its own. |
| `epigraph` | It holds a mapping with two keys, `quote` and `attribution`. The press refuses an epigraph of any other shape. |
| `acknowledgements` | It holds a paragraph or more, and the press sets it on a page of its own. |
| `edition-note` | It holds the edition line, the first line of the copyright page. Without it, the press takes the edition line from the `date` field in the metadata. |
| `manufacture` | It holds the classic origin line, such as "Published in the United States of America". |
| `colophon-note` | It holds the production note that names the type and the method. |
| `rights-notice` | It holds the rights paragraph near the top of the copyright page. |
| `contact` | It holds an address for the publisher. |
| `motto` | It holds a line of the press for the foot of the copyright page. |

Table: Table 10.2. The keys of config/front-matter.yaml

The press escapes every value before TeX sees it. A backslash, an ampersand, a percent sign, a dollar sign, a hash, the `_` character, braces, a tilde, or a caret in your dedication comes out as the character itself.

### Setting the keys from the command line

You can edit the file by hand, but `press config` is the shorter path. Example 10.2 shows user `alice` replacing the scaffold's placeholder identity facts and filling in the Alice front matter in one sitting.

**Example 10.2. Setting the Alice front matter**

```text
$ press config set copyright \
    "Copyright 2026 Wonderland Press" && \
  press config set publisher "Wonderland Press" && \
  press config set publisher-place "Oxford" && \
  press config set date "First edition, 2026"
$ press config set dedication "For Alice Liddell"
$ press config set epigraph.quote \
    "Curiouser and curiouser!" && \
  press config set epigraph.attribution "Alice"
$ press config set edition-note "First edition" && \
  press config set motto "Made slowly."
```

The four commands on the first line write to *config/metadata.yaml*, and the rest write to *config/front-matter.yaml*. The `press config` command knows which file owns each key, so you name the key and never the file. The `date` command repeats the value the scaffold wrote. The epigraph takes two commands because its value is a mapping, and the dotted names reach into it. If the front-matter file does not exist, the first front-matter key you set creates it.

### What the metadata must hold

Once front matter is on, five keys in *config/metadata.yaml* become mandatory: `title`, `author`, `copyright`, `publisher`, and `publisher-place`. The scaffold fills all five, so a new book passes. If you later delete one, the press refuses to generate the front matter and names the missing keys:

```text
front matter needs these config/metadata.yaml keys: ...
```

The list after the colon holds the key names, and the fix is to set them. The `date` field is not on the list, but the copyright page reads it for the edition line.

::: {.tip}
> **Tip:** If you trim *config/metadata.yaml* by hand, or adopt a metadata file from another book, keep the five mandatory keys in it. A missing one stops the next build that generates front matter.
:::

## The title page and the stacked subtitle

The press always sets the generated pages in one fixed order, and @fig:config-to-front-matter shows that order. It also shows which configuration file feeds each page and which keys travel along each path. The pages after the acknowledgments form a second group that comes from elsewhere.

![How the two configuration files become the front matter](assets/woodcuts/10-01-config-to-front-matter.png){#fig:config-to-front-matter .diagram width=full-measure fig-alt="Two file icons at the left send labeled arrows to five generated pages stacked at the right. Below them, a second, gray group of three pages takes dashed arrows from pandoc and the TeX header instead."}

<!-- art: ARCHETYPE data-flow, left to right. Left: two dog-eared file icons, "config/metadata.yaml" above "config/front-matter.yaml", monospace labels. Right, a vertical stack of five page outlines headed "generated": "title page", "copyright page", "dedication", "epigraph", "acknowledgments". Labeled arrows, small monospace. From metadata.yaml: to title page "title, subtitle, author, publisher-place, date". To copyright page "copyright, publisher, publisher-place, date". From front-matter.yaml: to copyright page "edition-note, rights-notice, manufacture, contact, colophon-note, motto". To dedication "dedication". To epigraph "epigraph.quote, epigraph.attribution". To acknowledgments "acknowledgements". Below the stack, a second group in a 10% gray band headed "from elsewhere": "Contents", "List of Plates", "List of Figures". Dashed arrows into it from two small rounded boxes at the lower left: "pandoc toc" to Contents, "TeX header" to both lists. Give "title page" a 20% gray fill. The reader should see first that the two config files feed only the five upper pages. -->

The *title page* is the first page that carries type. If the book has a cover, the cover plate comes before it, scaled to fit the text block with its proportions kept. The title page then runs from top to bottom as Table 10.3 describes.

| Line | Meaning |
|-------------------|----------------------------------------------------------------|
| Title | The press uppercases the `title` and sets it in bold at 30 points on 34. It adds a period unless the title already ends in a period, an exclamation point, or a question mark. |
| Rule | A short ornamental rule, 0.9 inch long, in a muted color, sits below the title. |
| Subtitle | The press splits the `subtitle` into clauses and sets them in small capitals, as the next section explains. |
| Second rule | A second rule of the same kind follows. The press draws it only when the book has a subtitle. |
| Byline | The word "by" comes first, then each author in large small capitals. |
| Place | The press sets the `publisher-place` in lowercase. |
| Year | The press sets the year in lowercase roman numerals. |

Table: Table 10.3. The title page, top to bottom

For the Alice book, the title becomes ALICE'S ADVENTURES IN WONDERLAND with a period after it. The place reads "oxford". The date "First edition, 2026" gives the year as "mmxxvi".[^10-roman] Chapter 3, *The shape of a book repository*, explains how the press finds the year in that field. The publisher's name does not appear on this page. It waits for the copyright page.[^10-rules]

### The stacked subtitle

Victorian title pages often carried a double title, joined by "or". The press sets such a subtitle the old way, one clause to a line. It splits the `subtitle` wherever it finds a space and "or,", with an optional semicolon before them. The press sets every clause in small capitals and lowercases it. Above each clause after the first, it sets a line of its own that reads "or," in small capitals.

To try it, user `alice` gives the book a double subtitle:

```text
$ press config set subtitle \
    "A Tale for Children; or, Alice's Adventures Under Ground"
```

The title page then shows "a tale for children" in small capitals, then "or," on a line by itself, then "alice's adventures under ground". A subtitle with no "or," clause sets as one line in the same style.

::: {.tip}
> **Tip:** Write each break as in the Alice subtitle: a semicolon, a space, and "or,". The press splits at every space followed by "or,", so a stray "or," inside a clause starts a new line too.
:::

## The copyright page

The press calls the page after the title page the *colophon*, although most readers know it as the copyright page.[^10-colophon] It holds the legal and production facts, and every line comes from the book's own files. Table 10.4 lists the lines in the order the press sets them.

| Line | Meaning |
|-------------------|----------------------------------------------------------------|
| Edition line | The `edition-note` comes first. Without one, the press takes the `date` up to its first comma and lowercases it. |
| Rights notice | The `rights-notice` appears next, followed by a rule. |
| Copyright | The `copyright` line from the metadata follows the rule. |
| Publisher | The words "Published by" precede the `publisher`. |
| Place | The `publisher-place` appears on its own line. |
| Manufacture | The `manufacture` line appears here. |
| Registrations | The press sets one line for each registration number the book declares, such as "ISBN (print)", "ISBN (ebook)", and "LCCN". |
| Contact | The `contact` address appears here. |
| Colophon note | The press sets the `colophon-note` in italic. |
| Motto | The press sets the `motto` in italic. |
| Logo | The press sets its logo from *assets/press-logo.png*, at 1.7 inches. |

Table: Table 10.4. The lines of the copyright page, in order

The Alice settings from Example 10.2 produce a short page. The edition line reads "First edition", because the `edition-note` overrides the line from the date. Without that note, the date "First edition, 2026" would give "first edition" in lowercase. The copyright line, "Published by Wonderland Press", and "Oxford" follow. The Alice book declares no rights notice, manufacture line, registrations, contact, or colophon note, so none of those lines appears. It has no logo file either, so "Made slowly." is the last line on the page.

The registration lines come from the `registrations` block in *config/metadata.yaml*. A number you do not hold yet can stand as `pending`, and the press prints it as "[pending]" on the page. The same numbers flow into the EPUB identifier and the barcode on the cover wrap. The copyright page therefore cannot show an ISBN that the EPUB does not carry. Chapter 13, *Registrations*, covers the numbers themselves and the `retail` switch that refuses a pending number in a book for sale.

The print interior gets a flattened copy of every image, the logo included, as Chapter 12, *The print pack*, describes.

### The pages after the copyright page

Three pages follow the copyright page, each only when you set its key. The dedication sits 2.1 inches down the page, in an italic column 3.1 inches wide. The epigraph starts 1.7 inches down, with the quote large and italic and the attribution in a muted color. The acknowledgments start 1.2 inches down, in a column 3.6 inches wide. For each optional page, the press either keeps the page whole or drops it whole, and a dropped page leaves no trace.

The generated front matter ends with the acknowledgments. The Contents follows, and pandoc's table of contents produces it. The List of Plates and the List of Figures come next, and the house TeX header sets each one only when the book has plates or numbered figures. Neither configuration file feeds those three pages.

## Overriding the front matter

The generated front matter depends on three conditions, and the press tests them in a fixed order. Table 10.5 gives the decision the press makes on each build of the reading PDF.

| Condition | Meaning |
|-------------------------------|-------------------------------------------------------|
| *tex/title-page.tex* exists | The press generates no front matter at all. Your file is the whole front of the book. |
| *config/front-matter.yaml* exists | The press generates the front matter from the two configuration files. |
| *assets/cover.jpg* exists | The press generates the front matter so that the cover plate can appear. This applies to the reading PDF only. |
| None of these | The book builds with pandoc's plain title handling and no generated front matter. |

Table: Table 10.5. When the press generates the front matter

The press stops at the first condition that holds. The override file therefore beats everything below it, even a front-matter file full of keys.

### The whole-cloth override

The file *tex/title-page.tex* is what the press calls "the whole-cloth override". It replaces every generated page: the cover plate, the title page, the copyright page, the dedication, the epigraph, and the acknowledgments. You write the opening pages in LaTeX yourself, so the file must hold every one of those pages that you want the book to have. The press then reads no key from *config/front-matter.yaml*, so the file can stay in the book repository and has no effect.

A figure taller than the text block once made LuaLaTeX ship empty pages forever, as Chapter 5, *Figures, plates, and illustrations*, tells. The house design caps every image at a height per profile, 6.3 inches on the house 6 by 9 profile. Keep any image in your override, the cover plate above all, well inside the text block.

::: {.warning}
> **Warning:** Do not stack a third `titlepage` environment, the LaTeX block that sets a page of its own, in *tex/title-page.tex*. The house rule against it comes from the same scar as the image cap, a build that never finishes. The generated front matter keeps the rule by setting all its pages in one block.
:::

### The print interior

The print interior never shows the cover plate, because the cover belongs on the cover wrap. The press builds the interior's front matter with the cover turned off, and the title page becomes the first page with type on it. If you need a different title page in print, supply *tex/title-page-print.tex*. That file replaces the title page in the print interior only, and the press never sets both title pages in the same interior.

### No front matter at all

If you delete *config/front-matter.yaml* and supply neither the override nor a cover, the press generates nothing. The press describes the result as "no generated front matter; the formats build with pandoc's plain title handling." The house TeX header still defines a modest title for that case. It sets the title in bold at 25 points on 29, the subtitle large and muted, then the author, the date, and the publisher.

::: {.tip}
> **Tip:** Keep the front-matter file even when you set no key in it. An empty file still gives you the generated title page and copyright page. If you delete it, you get the plainer title that the house TeX header sets.
:::

## The subject index

The subject index is an appendix that the press writes on every build from *config/index-terms.yaml*. With no such file, the book has no index. You never mark up the manuscript for it. You list the terms a reader will look up, and the press finds them in the text.

The file is a list of entries. Each entry has a `term`, the heading the reader sees in the index, and a `match`, the list of strings the press looks for. Example 10.3 shows three entries for the Alice book.

**Example 10.3. An index-terms.yaml for the Alice book**

```text
- term: Cheshire Cat
  match: [cheshire cat, cheshire puss]
- term: Mock Turtle
  match: [mock turtle]
- term: Tarts
  match: [tart, tarts]
```

The file has no wrapper key. The press refuses a `terms:` key at the top with the list beneath it. The shape errors are short, and `press check`, `press config validate`, and every build print the same text:

```text
must be a list of {term, match} entries, not ...
(see docs/CONFIGURATION.md)
entry 3: term is missing or empty
entry 3: match must be a non-empty list of strings
```

The first message is one line in the press's output, broken here to fit the page. The other two name the entry by its position in the list.

### How the press finds a term

@fig:index-entry-path follows one term from the configuration file to the printed index. The path has two exits, and the build stops at one of them.

![The path of an index term from the configuration to the appendix](assets/woodcuts/10-02-index-entry-path.png){#fig:index-entry-path .diagram width=full-measure fig-alt="A top-to-bottom flowchart. A term passes a box that removes code and images, then a matching box, then a question about hits. No leads to a stopped build, and yes leads to an index entry."}

<!-- art: ARCHETYPE flowchart, top to bottom. Top: a dog-eared file icon, "config/index-terms.yaml", with a monospace callout "term: Mock Turtle". Arrow down to a rectangle "strip fenced code, inline code, image lines". Arrow down to a rectangle "match whole words, any case, in every chapter and appendix". Arrow down to a diamond "Any hits?". Arrow "No" (small italic) goes right to a rounded box with a 40% gray drop shadow, "build stops", above small monospace text "gen_index: curated terms match nothing in the text". Arrow labeled "Yes" goes down to a rectangle "entry: term in bold, then locators 1, 3, A". Arrow down to a dog-eared page "Appendix A: Index of subjects". Keep the drawing no taller than the house figure cap. The reader should see first that a term with no hits cannot reach the appendix. -->

Before it matches anything, the press removes fenced code blocks, inline code, and every image line. A term that appears only inside an example, a constant-width span, or a figure line therefore has no hits.

The match itself ignores case. A match must also stand alone: the character on either side of it cannot be a letter, a digit, the `_` character, or a hyphen. The string `tart` therefore misses "tarts", and that is why Example 10.3 lists both forms. The string `turtle` misses "mock-turtle" by the same rule, because the hyphen sits next to the match. The string `mock turtle` misses "mock-turtle" for a plainer reason: the pattern holds a space where the text holds a hyphen.

::: {.warning}
> **Warning:** Do not trust a term that appears only in code or in a figure line. The press strips both before it matches, and a term with no hits in prose stops the build.
:::

### The zero-hit rule

A term that matches nothing anywhere in the manuscript is a fault, and the press refuses the build. The message names every such term at once, as Example 10.4 shows.

**Example 10.4. A term that matches nothing**

```text
$ press pdf
...
gen_index: curated terms match nothing in the text: Jabberwock
(fix the patterns or remove the terms; silence is not allowed)
```

The press prints the message as one line. It appears here on two to fit the page. The rule exists because an index term with no locators is a promise the book does not keep. A reader who looks up "Jabberwock" and finds nothing after the word learns only that the index is wrong. A revision that cuts the last mention of a term would leave such an entry. The zero-hit rule turns the cut into a refusal you see at your desk.[^10-silence]

The fix is one of the two the message names. Either the pattern is wrong, and you correct the `match` list, or the subject no longer appears in the book, and you remove the entry.

### What the index prints

The press writes the index to *build/generated/*, under a filename made from the first free appendix letter and the words *index-of-subjects*. It looks for that letter from `a` to `y`. A book with no `a-` appendix gets *a-index-of-subjects.md*, headed "Appendix A: Index of subjects". The heading carries pandoc's `{-}` mark, so the index appendix takes no section number. Because `press add appendix` hands out letters from `z-` downward, the index usually sorts before the appendixes you write.

The appendix opens with a fixed explanatory paragraph and then lists the entries in alphabetical order. Each entry is the term in bold, a separator, and its locators, with commas between them. A *locator* is the place a reader goes to find the term. The press uses chapter and appendix labels as locators, not page numbers. A hit in the preface reads "Preface", a hit in a chapter reads the chapter's number, and a hit in an appendix reads its letter. An entry for the Mock Turtle in the Alice book reads its two chapter numbers, 9 and 10, if the creature appears in only those two chapters.

The press states its reason in its own code: "Numbers are chapters and letters are appendices; both stay put across editions, which page numbers do not."

::: {.sidebar}
> **Why the index has no page numbers**
>
> A press book appears in eight editions at once, and only the Print edition has fixed pages. The Circulating edition, the EPUB, reflows its text to each reader's screen and type size. The Single-leaf edition is one long HTML page, and the Telegraphic edition, the plain text, has no pages at all. An index that printed page numbers would be right in the PDF and wrong in every other edition. Chapter numbers and appendix letters belong to the manuscript, so they read the same in every edition that carries the index. The cost is precision: a reader who looks up the Cheshire Cat learns the chapter and must find the page, a short search in a book of a dozen chapters.
:::

## The table of authorities

A book that states facts can carry a ledger of where each fact came from. The press calls this ledger the table of authorities and keeps it in *config/authorities.yaml*. Each entry ties a *claim*, an exact fragment of your prose, to the *authority* that warrants it. On every build, the press checks that each claim still appears in the text, once, where the ledger says it does.

The Alice book has no ledger yet. Suppose user `alice` adds a preface with the sentence "The book first appeared in 1865, with forty-two illustrations by John Tenniel." Example 10.5 shows the ledger she writes for it, with one entry for the date and one for the artist.

**Example 10.5. An authorities.yaml for the Alice book**

```text
- claim: "The book first appeared in 1865"
  authority: "Macmillan and Co., first edition, 1865"
  file: book/chapters/00-preface.md
- claim: "illustrations by John Tenniel"
  authority: "Macmillan and Co., first edition, 1865"
  file: book/chapters/00-preface.md
  note: "the first printing was withdrawn at Tenniel's request"
```

Table 10.6 gives the keys an entry can hold.

| Key | Meaning |
|---------------|-----------------------------------------------------------------|
| `claim` | Required. It holds the exact fragment of prose. The press collapses runs of whitespace before it compares, and the comparison is case-sensitive. |
| `authority` | Required. It names the source that warrants the claim. |
| `file` | Preferred. It names the chapter file that holds the claim, which pins the claim to one place. |
| `url` | Optional. It holds an address for the source. |
| `note` | Optional. It holds a short remark that the companion prints after the source, in the press's phrase "a dry aside". |

Table: Table 10.6. The keys of an authorities entry

### The claim must match exactly

The claim is a string, and the press looks for that string in the manuscript. A paraphrase does not count, and neither does a synonym or a change of case. The match forgives only whitespace, so a claim that breaks across two lines in the chapter file still matches. That exactness is the purpose of the ledger: a claim that matches shows that the cited sentence still says what the source supports.

::: {.warning}
> **Warning:** Before you reword a sentence that a ledger entry cites, find its claim in *config/authorities.yaml*. If you change one word of the fragment, the claim matches nothing, and the press refuses the next build. Update the claim in the same commit as the prose.
:::

### Reading a refusal

The press checks the whole ledger before it reports, and it collects every problem under one heading. Example 10.6 shows the ledger from Example 10.5 after two edits to the preface. User `alice` changed "first appeared" to "was first published", and she added a second sentence that also mentions the "illustrations by John Tenniel".

**Example 10.6. A ledger that does not hold**

```text
$ press pdf
...
gen_authorities: the ledger does not hold:
entry 1: missing, "The book first appeared in 1865" matches
nothing in the book (the text moved out from under its
citation)
entry 2: ambiguous, "illustrations by John Tenniel" appears 2
times in book/chapters/00-preface.md; lengthen the fragment
```

Each message is one line in the press's output, broken here to fit the page. Table 10.7 lists every fault the press reports.

| Fault | Meaning |
|-------------|---------------------------------------------------------------------|
| malformed | The entry is not a mapping, or it lacks a `claim` or an `authority`. |
| duplicate claim | Two entries state the same claim. The message names the entry that stated it first. |
| missing | The claim matches nothing in the book. The text moved out from under its citation. |
| ambiguous | With no `file`, the claim matches more than once across the book. The message counts the matches in each file and asks you to lengthen the fragment or declare `file:`. With a `file`, the claim appears more than once in that file. |
| unknown file | The `file` names a file that is not in the book. |
| moved | The entry declares a `file`, and the claim is no longer in it but appears elsewhere. The message names where, and the fix is to update `file:`. |

Table: Table 10.7. The faults a ledger can have

The `file` key changes how strict the count is. Without it, the claim must appear exactly once in the whole book, wherever that is. With it, only the count in that file must be one, and the same words elsewhere do no harm. A short claim such as "in 1865" is likely to recur, so give each claim enough words to stand alone.

::: {.tip}
> **Tip:** Put a `file` on every entry. The press then notices when a claim leaves its chapter, and a common phrase in another chapter cannot make the entry ambiguous.
:::

### What the ledger is not

The press says plainly what the ledger does not do: "It verifies a sources ledger; it is not a BibTeX or CSL citation engine." The ledger prints no superscripts, numbers no notes, and formats no bibliography. For a citation the reader should see in the text, write a footnote. The ledger then records, out of the reader's sight, that the footnote's sentence still says what its source supports.

You need not build the ledger by hand. The `authorities-research` workflow populates it, and so does `press research`. Chapter 15, *The operator's desk and the editorial machines*, describes both.

## The sources companion

The ledger produces one *artifact*, a file in *dist/* that the registry names. That artifact is the *sources companion*, a standalone Markdown file that the press publishes beside the book and never inside it. For the Alice book with the ledger from Example 10.5, it is *dist/alice-sources.md*.

The companion opens with a heading made from the title. A line in italic follows with the title, the authors, and then the publisher and the date when the book has them. The entries come next, grouped by where each claim sits in the book. The groups read "In the preface", "In chapter N", and "In appendix X". Example 10.7 shows the shape of the file, with each field the press fills in angle brackets.

**Example 10.7. The shape of a sources companion**

```text
# <Title>: sources and authorities

*Companion to <Title> by <authors>, <publisher>, <date>.*

## In the preface

- "<claim>": <authority>. <url> <note>
```

The Alice companion has one group, "In the preface", with two entries, and the Tenniel entry ends with its note about the withdrawn printing.

Before it writes a field, the press rewrites a few characters. It turns each dash into a comma and a space, straightens curly quotes, and writes an ellipsis as three periods. It also turns a non-breaking space or a backslash into a plain space. The substitutions keep the companion plain, wherever you copied the ledger's sources from.

### Publication and proof

The press publishes the companion as a download, with the label "Table of authorities". Chapter 7, *Building the editions*, places it in the registry beside the editions.

A *verifier* is one of the press's `verify_*` checks, which inspect an artifact after the build. The archive verifier, `verify_archives`, requires the companion to name the book, to run to at least 200 characters, and to contain an entry marker. A companion that came out empty, or that belongs to some other title, fails the run. Chapter 8, *Verifying the artifacts*, describes the archive verifier and its other checks.

The next chapter turns from words to pictures and the art department that commissions them.

[^10-devil]: The sample epigraph is a printer's joke. A *printer's devil* was the apprentice in a print shop, and every misprint was his fault.

[^10-roman]: Printers set the year in roman numerals on title pages for centuries. The habit survives in film credits and on cornerstones.

[^10-rules]: Before version 3.0.0, a book without a subtitle got both ornamental rules anyway, with nothing between them. The fix removed the second rule when it has nothing to close.

[^10-colophon]: The word first named a note at the end of a book, where the printer recorded the type, the date, and the place. Modern books moved those facts to the back of the title leaf, and the press keeps the old name for them.

[^10-silence]: The press's message ends "silence is not allowed". An index that drops a term without a word would be the silence it means.

<!-- index: front matter; front-matter.yaml; title page; stacked subtitle; colophon; copyright page; dedication; epigraph; acknowledgments; tex/title-page.tex; whole-cloth override; subject index; index-terms.yaml; locator; zero-hit rule; table of authorities; authorities.yaml; claim; sources companion; verify_archives; registrations -->
