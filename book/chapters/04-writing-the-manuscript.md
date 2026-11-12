# Writing the manuscript

::: {.in-this-chapter}
> **In this chapter:**
>
> - The dialect
> - Headings and chapters
> - Characters you may and may not type
> - Paragraphs, footnotes, and quotations
> - Tables
> - Code
> - Chapter openings and drop caps
> - Scene breaks
> - The set pieces
> - The fine work press does for you
:::

A *chapter file*, one Markdown file in *book/chapters/*, is plain Markdown, and most of what you type in one is Markdown you already know. Press reads every chapter in one fixed dialect, holds it to a short list of laws, and does a good deal of typesetting on your behalf. This chapter describes the dialect, the laws, and the few constructs that belong to press alone. The examples come from the press's own three-chapter Alice example, the gallery book that holds the opening of Carroll's novel. The Alice book, which `alice` keeps on the workstation `hatter`, is the whole novel. It sets these constructs the same way.

## The dialect

Pandoc reads Markdown in many dialects. You build a dialect from a base format and a list of extensions, each switched on with a plus sign. Press fixes the dialect for every build of every book. Every pandoc build in press reads the manuscript in the dialect that follows, with `standalone: true` and `number-sections: true`.

```text
markdown+smart+yaml_metadata_block+fenced_divs+footnotes
```

Table 4.1 lists the parts of the dialect and what each one gives you.

| Setting | Meaning |
|---------------|-------------------------------------------------------------|
| `markdown` | Pandoc's own Markdown is the base. Pipe tables, fenced code, line blocks, and definition lists all come from it. |
| `+smart` | Pandoc turns straight quotes into curly ones and three periods into an ellipsis. It also turns runs of hyphens into dashes, which the house forbids. |
| `+yaml_metadata_block` | Pandoc accepts a block of YAML metadata. A press book keeps its metadata in *config/metadata.yaml* instead, as Chapter 3 describes. |
| `+fenced_divs` | Pandoc reads the lines between two fences of three colons as one classed block. The set pieces, described later in this chapter, use this extension. |
| `+footnotes` | Pandoc reads a note label in square brackets with a caret, and sets the note in the form each edition needs. |
| `standalone: true` | Pandoc writes a complete document, never a fragment. |
| `number-sections: true` | Pandoc numbers every chapter and every section heading. |

Table: Table 4.1. The pandoc dialect press reads

The same settings appear in all six of the pandoc defaults files that press keeps inside its own package. Your book repository has no copy of them, so pandoc parses a chapter the same way for every edition it builds.

The `+smart` extension explains most of the character rules later in this chapter. Because pandoc curls quotes for you, you type the straight ones and let pandoc choose the direction. Because pandoc turns hyphens into dashes, a sentence with two hyphens in it comes out with a dash in it. The house does not set dashes in prose. The `number-sections` setting explains the heading rules. Pandoc numbers your headings itself, so you type no numbers.

One edition stands apart from all of this. The Manuscript edition (the stitched Markdown) is the raw manuscript, stitched together from your chapter files. No filter runs on it. It keeps your straight quotes, your three periods, and every construct exactly as you typed it. Everything this chapter says about pandoc and the press filters applies to the rendered editions. They are the Print edition (PDF), the Circulating edition (EPUB), the Single-leaf edition (the self-contained HTML), the Chapter edition (the reader site), the Telegraphic edition (plain text), and the Office edition (DOCX).

## Headings and chapters

@fig:page-anatomy shows where the parts of a chapter end up on a printed page, here the opening page of the first chapter of the three-chapter example. The first callouts are (1) the folio, (2) the chapter title, and (3) the drop cap. Then come (4) the body text, (5) a section heading, and (6) a blockquote in its box. The last three are (7) a scene break, (8) a numbered figure with its caption, and (9) a footnote.

An opening page carries no running head, and every later page of the chapter does. The house sets the running head and the folio with no markup from you (Chapter 9, *The house design*, describes both). The drop cap comes from configuration. You type the rest, and Chapter 5 covers the figure.

![The parts of a printed page in the three-chapter example](assets/woodcuts/04-01-page-anatomy.png){#fig:page-anatomy .diagram place=plate fig-alt="A miniature book page in outline with nine numbered callouts pointing to its folio, chapter title, drop cap, body text, section heading, blockquote, scene break, figure, and footnote."}

<!-- art: ARCHETYPE page anatomy, portrait. One 6 by 9 chapter opening page in thin outline, with no running head. Top to bottom: a large flush-left chapter title, "Down the rabbit-hole"; a first paragraph opening with a three-line drop cap "A"; gray text lines; a bold section heading; a gray hairline box of italic lines; a staggered field of asterisks; a framed shape captioned "Figure 1.1"; a short rule over two small lines; a small page number centered at the foot. Thin callouts lead to numbered margin circles: 1 folio, 2 chapter title, 3 drop cap, 4 body text, 5 section heading, 6 blockquote box, 7 scene break, 8 numbered figure and caption, 9 footnote. The reader sees the whole page first. -->

A `#` heading is a chapter. Press sets pandoc's `top-level-division: chapter` for the PDF and the EPUB, and in every rendered edition one `#` at the start of a line starts a new chapter. A `##` heading is a section, and a `###` heading is a subsection. Pandoc numbers all three.

A chapter file's name starts with a digit, and Chapter 3 gives the sorting rules.

```text
$ press add chapter "The rabbit sends in a little Bill"
```

`press add chapter` names the file and writes the heading word for word (Chapter 3).

### Unnumbered chapters

A preface, a foreword, or an introduction is a chapter with no number. Mark its heading with `{.unnumbered}` or the short form `{-}`, and pandoc skips it when it counts. The command `press add chapter preface --front` creates *book/chapters/00-preface.md* with the heading `# Preface {.unnumbered}`. The `00-` prefix sorts the file ahead of chapter one. An unnumbered chapter also gets no drop cap or other special first letter, as the section "Chapter openings and drop caps" later in this chapter describes.

Press has no support for parts. A book cannot group its chapters into Part One and Part Two, because the top-level division is the chapter and `#` always means a chapter. If your book needs parts, put the grouping in the chapter titles or in the preface.

### Numbers and capitals in headings

You never type a number in a heading. The *checker*, `press check`, refuses a heading such as `# 3. The pool of tears` with the message `manual number in heading`, because pandoc numbers the heading itself. The same goes for section headings. Write `## Who stole the tarts` and let pandoc number it.

Headings are in sentence case: a capital on the first word and on proper names, and lowercase everywhere else. The checker refuses a title-case heading with the message `title-case heading:` followed by the heading text. The test is mechanical. The checker sets aside the first word, the words on a fixed list of 21 small words, and any word in all capitals. If at least three candidate words remain, and 80 percent or more of them start with a capital, the checker calls the heading title case.

Example 4.1 shows the test at work on the heading of Carroll's fourth chapter.

**Example 4.1. Two headings for the same chapter**

```text
# The Rabbit Sends In A Little Bill
# The rabbit sends in a little Bill
```

In the first heading, the candidates are at least Rabbit, Sends, Little, and Bill. Every one of them starts with a capital, so the checker refuses it. In the second, only Bill keeps its capital, because Bill is the lizard's name. One capital in four or five candidates is well under the line, and the checker accepts it.

A short heading can pass the test in title case. `# Down the Rabbit-Hole` has too few candidates, or too few capitals among them, so it passes. The house would still write it in sentence case.

::: {.tip}
> **Tip:** Type the title in sentence case when you run `press add chapter`. Press keeps the title word for word, so a title-case title becomes a title-case heading. The next `press check` refuses it.
:::

### Referring to other parts of the book

Press numbers figures and lets you cite them by name. Give a figure an identifier in its attributes, such as `{#fig:page-anatomy}` at the end of its image line, and cite it in prose as `@fig:page-anatomy`. Press then prints "Figure 4.1" with a link. A citation of an identifier press does not know stays in the text as a raw citation, which you will see at once in a proof. Chapter 5, *Figures, plates, and illustrations*, covers figure identifiers in full.

Press has no machinery for citing chapters or sections. Write a reference to a chapter or a section in words: "see Chapter 6, *Checking the manuscript*".

![The compositor at the frame, setting a chapter by hand](assets/woodcuts/the-compositor-at-the-frame.png)

<!-- art: a compositor in shirtsleeves standing at a sloped composing frame, seen three-quarter from the left at eye level, the upper and lower type cases angled before him, his left hand holding a brass composing stick with a line of type in it, his right hand lifting one sort from the case, the manuscript copy pinned to a small stand at eye height, a galley with set lines resting on the frame's ledge, a gas lamp bracket above; portrait composition; wood engraving with dense hatching and crosshatching, single black ink, no gray washes, no lettering anywhere -->

## Characters you may and may not type

The checker holds every chapter file to a *glyph law*: a short list of the characters that may appear in book prose. The law exists for the print interior, as the checker's message says: a character outside the law is outside the print-font set. `press check` refuses such a character wherever it finds one in prose.

Table 4.2 gives the law exactly.

| Characters | Meaning |
|---------------|-------------------------------------------------------------|
| Tab, line feed, carriage return | These are the only control characters the law allows. They hold a text file together. |
| U+0020 through U+007E | This is printable ASCII: the space, the letters, the digits, and the punctuation on a US keyboard. |
| U+00C0 through U+017F | These are the accented Latin letters, such as the e in "café" or the c in "façade". The multiplication and division signs also fall inside this range. |

Table: Table 4.2. The characters the glyph law allows in book prose

Nothing else passes, and the gap between the two ranges is the surprising part. The block from U+00A0 through U+00BF holds the copyright, degree, section, and pound signs. It also holds the guillemets, the fractions, the inverted question mark, and the non-breaking space. The checker refuses every one of them. It refuses Greek letters, mathematical symbols, and emoji too. For each one, the checker prints `glyph U+XXXX is outside the print-font set`, with the character's code point in place of the four X's.

Example 4.2 shows a few of the characters the law refuses. They appear here inside a code block, because the checker skips fenced code.

**Example 4.2. Characters the checker refuses in prose**

```text
U+00A3  £   pound sign
U+00A7  §   section sign
U+00A9  ©   copyright sign
U+2014  —   em dash
U+201C  “   left double quotation mark
U+201D  ”   right double quotation mark
```

In practice you write the word: "thirty degrees", "five pounds", "section 4". A book's copyright line belongs to the generated front matter, which Chapter 10 describes.

::: {.warning}
> **Warning:** Run `press check` after every paste from a word processor or a Web page. Pasted text arrives full of curly quotes, dashes, and non-breaking spaces, and the non-breaking space is invisible on screen. Only the checker will find it.
:::

### The dash law

The house sets no em dash and no en dash in prose. The checker refuses the em dash (U+2014), the en dash (U+2013), and the four curly quotation marks in the prose of a chapter. You type straight quotes and apostrophes, and pandoc curls them in every rendered edition.

The two hyphens are a quieter case. Because of `+smart`, pandoc turns two hyphens into an en dash and three into an em dash. The checker does not refuse the hyphens in source, so a sentence with two hyphens in it passes `press check` and then prints with a dash. The house law says what to do instead: rewrite the sentence. A comma, a colon, a period, or a pair of parentheses carries almost every job a dash does, and the rewrite is usually the better sentence. Example 4.3 shows one such rewrite.

**Example 4.3. A sentence with a dash and its rewrite**

```text
The Hatter's watch told the day of the month -- not the hour.
The Hatter's watch told the day of the month, never the hour.
```

The ellipsis is the third conversion. You type three periods, and pandoc sets the single ellipsis character in the output. The ellipsis character, U+2026, lies outside the glyph law, so you could not type it in prose if you tried.

### The book's own rules

A book can list extra directories for the checker under `audit-dirs` in *config/house-rules.yaml*. The files there get a lighter battery than the manuscript. The same file can add refusals of the book's own under `banned-patterns`. Chapter 6, *Checking the manuscript*, covers both.

## Paragraphs, footnotes, and quotations

A paragraph is any run of lines with no blank line inside it, as in all Markdown. Press adds one law of its own: a paragraph must be under 190 words. The checker refuses a paragraph that breaks the law.[^4-paragraph-law] The message is `paragraph N has W words (the law is under 190; split it)`, where N numbers the paragraph and W counts its words. In an audit directory the same paragraph draws a warning.

The law is a typesetting law as much as a prose law. A very long paragraph turns a page into one gray block and gives the eye nowhere to rest. Split the paragraph at the point where its subject turns.

In our experience the split is rarely hard to find. A paragraph that runs long usually holds two topics: a rule and its history, or a command and what to do when it refuses. Give each topic its own paragraph and its own first sentence. If the paragraph is a single list of things, such as the options of a command, it probably wants to be a table.

Press forbids trailing whitespace everywhere: in prose, in headings, and inside code blocks too. Trailing whitespace is invisible, and a line ending in two spaces is a hard line break in Markdown. A stray pair of spaces can change the page and leave your editor's screen unchanged.

::: {.tip}
> **Tip:** Set your editor to strip trailing whitespace when it saves a file.
:::

### Footnote markup

Footnotes use pandoc's standard syntax: you put a label in square brackets with a caret at the point of reference. The note itself goes on a line of its own that starts with the same label and a colon. The PDF sets each note at the foot of its page, and the EPUB and the reader site collect the notes as linked notes. Press has no separate setting for endnotes. Because the PDF prints every note at the foot of its page, a long note pushes text onto the next page. Keep notes for asides and history, and put anything the reader needs to follow the argument into the body.

```text
Alice had not a moment to think about stopping
herself.[^2-well]

[^2-well]: Either the well was very deep, or she fell slowly.
```

A label must be unique across the whole book. Pandoc merges every chapter file into one document before it resolves footnotes, so two chapters that both use `[^2-well]` collide. A short, descriptive label is easier to find again than a number, and pandoc numbers the notes for you in each edition. We start every label with its chapter number, as in `2-well`, so it never collides with another chapter's notes.

### Quotations and epigraphs

A blockquote is a paragraph whose lines start with `>`. In the PDF, the house sets each one in a framed box with a light paper-gray ground, a 0.4-point rule in gray, and small italic type. The *jargon lint*, the pass of the checker that looks for overused words, skips quotations, so a quoted passage does not trip it. Chapter 6 describes the jargon lint and its watchlist.

A chapter epigraph is an ordinary blockquote that you place right after the chapter heading. Press has no special syntax for one and no attribution field. If an epigraph needs a source line, write it as the last line of the blockquote. The drop cap, if the book has one, skips the blockquote and goes on the first real paragraph after it. The book's own epigraph, the one on a front-matter page of its own, comes from `epigraph.quote` and `epigraph.attribution` in *config/front-matter.yaml* instead. Chapter 10 describes it.

```text
# Down the rabbit-hole

> "And what is the use of a book," thought Alice,
> "without pictures or conversations?"
```

### Line blocks and definition lists

Pandoc's line block keeps every line break you type. Start each line with a vertical bar and a space, and pandoc sets the lines exactly as you broke them. A short verse, an address, or a list of signatures can go in a plain line block. The set pieces later in this chapter take a line block as their input and give it a shape. When the breaks matter and the shape does not, use a plain line block, as in a postal address inside a letter. Reach for a set piece only when the shape is part of what the passage says.

A definition list is standard pandoc too: a term on one line, then a line starting with a colon and a space that holds the definition. We recommend it for a glossary appendix, where each term needs a sentence or two after it.

### Sentences that other files name

Three kinds of configuration point into your prose, and each one constrains how you revise. Press matches the terms in *config/index-terms.yaml* against the manuscript by pattern, so you never mark up the manuscript for the index. A claim in *config/authorities.yaml* is an exact fragment of your manuscript. If you reword its sentence, the claim no longer matches and press refuses the build. Chapter 10 covers the index and the authorities.

A *sentinel* is a phrase in `verify-sentinels` in *config/metadata.yaml* that the verifiers look for in each finished edition. A sentinel must survive every revision word for word. Chapter 6, *Checking the manuscript*, explains sentinels, and Chapter 8, *Verifying the artifacts*, proves them in the finished editions.

## Tables

Press uses pandoc's pipe tables. Each row is a line, and a vertical bar separates the cells. A row of hyphens under the first row marks it as the header. A line that starts with `Table:` after the table gives it a caption. Example 4.4 shows a small table drawn from the first two chapters of the three-chapter example.

**Example 4.4. A pipe table with a header row and a caption**

```text
| Item | What it does |
|------------|------------------------------------------------|
| The bottle | Alice shrinks until she is ten inches high. |
| The cake | Alice grows until her head strikes the roof. |

Table: Table 2.1. What Alice swallows
```

Press has no filter that numbers tables. In the PDF, the caption prints above the table, centered, in small italic type, with no automatic label in front of it. The house sets the caption package so that LaTeX adds no "Table 1:" of its own. In the Single-leaf edition and the EPUB, the caption becomes the table's own caption element. The book has no List of Tables. A book that wants its tables numbered types the number into the caption, as Example 4.4 does with "Table 2.1." and as this book does throughout.

Pandoc decides the column widths from the source. If every line of a table fits within pandoc's 72 columns, pandoc sets the table at its natural width, each column as wide as its contents need. If any line runs past 72 columns, pandoc reads the relative widths from the separator row instead. A column whose run of hyphens is three times as long as its neighbor's gets three times the width. A table with long sentences in one column therefore needs a separator row drawn in proportion, as the tables in this chapter have.

Give every table a header row. In the Single-leaf edition and on the reader site, press labels each cell of a headed table with the name of its column, in a `data-label` attribute. Below a width of 34rem, the reader site's stylesheet turns each row of the table into a card.

Keep tables small. Two or three columns read well at every width, on a 6 by 9 page and on a small screen alike. A table of seven columns crowds a 6 by 9 page, and each of its cards runs to seven lines on a narrow screen. If a table needs that many columns, it is usually two tables.

## Code

Code goes in a fenced block: a line of three backticks, the code, and another line of three backticks. In the PDF, the house sets fenced code in Source Code Pro, a little smaller than the body type. In a fence tagged `text`, a line too long for the measure wraps onto the next line, with a hooked mark to show the continuation. An untagged fence is set verbatim, and a long line in it runs off the page. Even a wrapped line is harder to read than one you broke yourself.

Pandoc highlights fenced code in color, in the PDF, the EPUB, the Single-leaf edition, and the reader site, with its default `pygments` style. A book cannot change the style. Highlighting matters most at the opening fence. If you name a language after the three backticks, such as `python` or `yaml`, pandoc colors the code by that language's rules. If you write `text`, the code prints in black.

That choice reaches the printer. A language-tagged fence puts colored ink on the page, and `press verify-print` refuses the print interior with the message `print profile: colored ink on pages [N]`. The verifier of the reading PDF does not check the color of the ink, so the problem appears only when you build the print pack. Chapter 12, *The print pack*, describes that build. We tag every fence in this book `text`, so it prints in black and wraps.

::: {.warning}
> **Warning:** Do not put a language name on a fence in a book that goes to print. The highlighted code prints in colored ink, and the print verifier refuses the whole interior.
:::

The prose rules skip fenced code, with one exception. The checker reads no glyphs, dashes, banned patterns, or paragraph lengths inside a code block. You can show a session with real output there, or the characters from Example 4.2. The exception is trailing whitespace, which the checker refuses in code exactly as it does in prose.

Inline code, a word or a phrase between single backticks, prints in the same monospace face as a fenced block. The glyph law and the jargon lint skip inline code too. A book's banned patterns do not: they skip fenced code blocks only, so a pattern fires on a backticked span inside a prose line. Pandoc's smart typography leaves inline code alone, so `--front` in backticks keeps its two hyphens. Use inline code for anything a reader could type: a command, an option, a key, a value.

A short session looks like this:

```text
$ press check
...
```

Show the prompt, then the command, then the output, and show what the reader will really see. A session that you typed from memory, rather than copied from a terminal, is the first thing a careful reader catches out. Elide long or boring output with a line holding three periods. We use the `$` prompt throughout this book, on the workstation `hatter` and on the CI host `printshop` alike.

::: {.tip}
> **Tip:** Keep code lines to 63 characters or fewer. A `text` fence wraps a longer line for you, but at the measure, which is rarely where a reader expects the break.
:::

## Chapter openings and drop caps

A *chapter opening* is the treatment of the first letter of each chapter. The book sets it with `chapter-opening` in *config/metadata.yaml*, and press merges that setting over the design profile's default. Every profile that comes with press defaults to `none`, so a new book opens its chapters with a plain paragraph. The three-chapter example sets a three-line drop cap with small caps for the rest of the first word.

Table 4.3 lists the three settings.

| Setting | Default | Meaning |
|-----------------|-------------------|---------------------------------------------|
| `style` | the profile's (`none`) | The value `none` sets a plain first paragraph. The value `drop-cap` sets a large initial that sinks into the text. The value `ornate` sets a foliate initial in print. |
| `lines` | 3 | The default initial is three text lines deep. |
| `small-caps-remainder` | true | When this is true, press sets the rest of the first word in small caps. |

Table: Table 4.3. The chapter-opening settings in config/metadata.yaml

Press also accepts the style `raised-cap`, which renders the same as `drop-cap`. You can set the style with `press config set`, which checks each value before it writes the file:

```text
$ press config set chapter-opening.style drop-cap
```

In *config/metadata.yaml* the same settings form one block, as Example 4.5 shows.

**Example 4.5. The three-chapter example's chapter opening**

```text
chapter-opening:
  style: drop-cap
  lines: 3
  small-caps-remainder: true
```

### Where the drop cap goes

The *chapter-dropcap.lua* filter finds the first eligible paragraph after each `#` heading. It skips any chapter marked `{.unnumbered}`, so a preface opens with a plain paragraph. On its way down the chapter it passes over blockquotes, code blocks, lists, tables, rules, and figures. A chapter that opens with an epigraph therefore gets its drop cap on the first paragraph of prose, where the reader expects it.

In the PDF, press keeps a drop cap from starting at the foot of a page that has no room for its lines. The initial is always one grapheme, so an accented capital or a letter with a combining mark stays whole. We suggest opening each chapter with a paragraph of at least four or five lines. A three-line initial beside a one-line paragraph has nothing to sink into, and the page looks unfinished. The Telegraphic and Office editions carry no drop cap.

### Dialogue openers

The second chapter of the three-chapter example opens with speech:

```text
"Curiouser and curiouser!" cried Alice (she was so much
surprised, that for the moment she quite forgot how to speak
good English).
```

The first character of that paragraph is a quotation mark, and the letter after it is the one that should drop. Press calls the quotation mark the *lead*, and it sets the capital C as the drop cap. It hangs the lead into the left margin at body size, so the C stays square with the text below it.[^4-hung-quote] On the reader site, the lead carries the class `.drop-cap-lead` and a negative left margin of .52em, which gives the same effect.

### The ornate style

The `ornate` style sets the initial in the yinit foliate font, from the `yfonts` package in the TeX Live fonts-extra collection. That font exists only in print. The EPUB and the reader site set a styled display capital instead, at 3.6em in the ornament color. It uses a script face such as Luminari, Apple Chancery, or Zapfino, if the reader's machine has one.

## Scene breaks

A *scene break* is a pause inside a chapter, a change of time or place that needs more than a new paragraph. In the manuscript you type it as a Markdown thematic break: a line holding three asterisks with spaces between them, `* * *`. The key `scene-break` in *config/aesthetic.yaml* chooses how press draws it, and the *scene-break.lua* filter draws it.

Table 4.4 lists the three values.

| Value | Meaning |
|---------------|-------------------------------------------------------------|
| `rule` | This is the default. The PDF has a plain horizontal rule, and the reader site has a small diamond between two hairlines that fade at their ends. |
| `asterism` | Press sets three asterisks, centered and spaced a quad apart in the PDF, and as a paragraph of class `asterism` on the reader site. |
| `fairy-dust` | Press sets a staggered array of eleven asterisks in three rows of four, three, and four. Press describes it as Tenniel's 1866 array. |

Table: Table 4.4. The scene-break ornaments

@fig:scene-break-ornaments shows each ornament as it appears in the PDF and on the reader site. The three-chapter example uses `fairy-dust`, as Example 4.6 shows.

![The three scene-break ornaments in the PDF and on the reader site](assets/woodcuts/04-02-scene-break-ornaments.png){#fig:scene-break-ornaments .diagram width=full-measure fig-alt="A grid of three rows and two columns. A plain rule, three spaced asterisks, and a staggered field of eleven asterisks each appear once as printed in the PDF and once as shown on the reader site, where the rule becomes a diamond between fading hairlines."}

<!-- art: ARCHETYPE matrix. A grid of three rows by two columns, thin rules between cells. Column heads in small sans: "PDF" left, "Reader" right. Row labels down the left in small monospace: "rule", "asterism", "fairy-dust". Each cell shows the ornament in black between gray text lines. Rule, PDF: a plain thin horizontal rule. Rule, Reader: a small solid diamond centered between two hairlines that taper away at their outer ends. Asterism, both cells: three centered asterisks with wide even spaces. Fairy-dust, both cells: eleven small asterisks in three centered staggered rows of four, three, and four. The reader sees the three ornaments down the rows first, then that only the rule differs between the columns. -->

**Example 4.6. The three-chapter example's scene break**

```text
scene-break: fairy-dust
```

On the reader site, the fairy dust is a division of class `fairy-dust`. The division carries the role of a separator, and press hides it from screen readers, which have no use for eleven asterisks. The Telegraphic and Office editions keep a plain rule whatever the book chooses.

You type the same `* * *` in every case. If the aesthetic changes later, every scene break in the book changes with it, and no chapter file needs an edit. A book can therefore try all three ornaments, one build each, and keep the one that suits its pages.

## The set pieces

Some passages need a shape of their own: an address that steps down the page, a poem on its own measure, a poem shaped like its subject. Press calls these the *set pieces*, and it has three: `cascade`, `verse`, and `tail`. Each one is a fenced div, a block between two lines of three colons, with the set piece's name after the first fence. Inside it you normally put a line block, and the *set-pieces.lua* filter lays out the form. If the div holds plain paragraphs instead of a line block, the filter counts each paragraph as one line.

@fig:set-pieces shows what each of the three does to the same four lines: the address Alice imagines writing to her own right foot.

![What cascade, verse, and tail do to the same four lines](assets/woodcuts/04-03-set-pieces.png){#fig:set-pieces .diagram width=full-measure fig-alt="Three small frames side by side, each holding the same four-line address. In the first the lines step to the right one indent at a time, in the second they share one indented left edge, and in the third they swing in a curve and shrink line by line."}

<!-- art: ARCHETYPE before/after, three frames. Three identical small page frames side by side, no arrows. Each frame holds the same four short serif lines: "Alice's Right Foot, Esq.", "Hearthrug,", "near the Fender,", "(with Alice's love)." Frame (a): each line starts one equal indent further right than the line above. Frame (b): all four lines share one left edge set well in from the frame. Frame (c): the lines swing right, left, then right in a gentle curve, and the type shrinks line by line. Under each frame a small sans label: "(a) cascade", "(b) verse", "(c) tail". The reader sees first that the words are the same in all three frames. -->

### Cascade

A cascade suits an address or an inscription. It indents each line by 2.4em times one less than its line number, so the first line sits at the left edge. Example 4.7 shows the address in Carroll's second chapter as a cascade.

**Example 4.7. A cascade in the three-chapter example**

```text
::: cascade
| Alice's Right Foot, Esq.
| Hearthrug,
| near the Fender,
| (with Alice's love).
:::
```

### Verse

A verse block suits a poem or a song, and it sets its lines to the house stanza measure. Example 4.8 holds the start of the crocodile poem in Carroll's second chapter.

**Example 4.8. A verse block**

```text
::: verse
| How doth the little crocodile
| Improve his shining tail,
| And pour the waters of the Nile
| On every golden scale!
:::
```

Every line starts 3em in from the left, with no paragraph indent, and the block has 0.7em of space above and below it. An opening quotation mark at the start of a line hangs into the margin, so the letters of every line align. A blank line between groups of lines gives a stanza gap. On the reader site, the block carries the class `.verse`, with a left margin of 2.4em.

### Tail

The tail is the most elaborate of the three. It exists for the Mouse's Tale, which Carroll printed as a poem that winds down the page in the shape of a mouse's tail. The filter swings each line out from the left edge and back along a sine curve, as much as 3.0em at its widest.

The type also shrinks as the tail goes down. In the PDF it starts at body size and ends at the smallest size LaTeX offers. On the reader site it shrinks from 1em to .68em. Example 4.9 shows the opening lines of the Mouse's Tale in a tail.

**Example 4.9. The opening of the Mouse's Tale as a tail**

```text
::: tail
| "Fury said to a
| mouse, That he
| met in the
| house,
| 'Let us
| both go to
| law: I will
| prosecute
| you.
:::
```

### What the set pieces leave alone

The set pieces change the layout of the lines and nothing else. The words stay live text in every rendered edition, so a reader can search for them, copy them, and hear them from a screen reader. The Telegraphic and Office editions get a native line block, with the line breaks kept and no shape.

## The fine work press does for you

Some typesetting is too fine to ask of an author. Press does it in a Lua filter, *typographic-spacing.lua*, which runs in every rendered edition. The filter puts a *tie*, a non-breaking space, between a word and the word it must never leave at the end of a line. In the PDF the tie is LaTeX's `~`. In the other rendered editions it is the non-breaking space character, U+00A0, which the glyph law forbids you to type yourself.

The filter ties in three places, and none of them asks anything of you. After an honorific, it ties the honorific to a following capitalized word. The honorifics are Mr., Mrs., Ms., Dr., Prof., St., Mt., Sr., Jr., Rev., Hon., Capt., Sgt., Gen., Col., Lt., and Fr. After a reference form, it ties the form to a following digit. The reference forms include p., pp., No., Nos., Fig., Figs., Ch., Vol., Pt., and Eq. Between chained initials, it ties each initial to the next, as in "C. L. Dodgson".[^4-ties]

Each tie prevents a misreading. A line that ends on "Rev." with the name at the start of the next line reads, for an instant, as the end of a sentence. A page reference split after "p." leaves the number stranded on a line of its own. A name broken between its initials stops looking like a name. None of these is an error a checker could catch in the manuscript, because the line breaks do not exist until the page does.

The manuscript stays plain prose, and the house does the fine work. The filter leaves ordinary sentences exactly as you typed them, every period included. You type "Rev. Dodgson" and "p. 42" with ordinary spaces. The filter keeps each pair on one line in the PDF, the EPUB, and the reader site alike.

Figures get the same treatment. The *figure-numbering.lua* filter numbers each figure once, by chapter, and turns every `@fig:` citation into "Figure 4.1" with a link. Press therefore needs no pandoc-crossref.

::: {.sidebar}
> **A stray asterisk and Fig-ure**
>
> An author cannot fix the fine work from the manuscript, so it has to be right. Two small faults in the placed figures of the PDF show what that means. In figures with a placement, the float package's `\caption*` printed a stray asterisk above the figure. Nothing in the manuscript had an asterisk in it. The author could only look at the proof and wonder.
>
> The second fault came with the wraps. A figure with text running around it has a narrow caption. In a narrow enough wrap, LaTeX hyphenated the label itself, and the caption began "Fig-" on one line and "ure" on the next.
>
> The fixes went into the house design. The caption package became the single authority for every caption in the book. The label went inside an `\mbox`, which LaTeX never breaks. An author who writes a figure today types a caption and nothing else.
:::

The next chapter, *Figures, plates, and illustrations*, takes up the plates, the numbered figures, and the placements that put them on the page.

[^4-paragraph-law]: According to the press's change log, the checker began to enforce the paragraph law in press 1.7.0.

[^4-hung-quote]: Press calls this Bringhurst's rule. The capital aligns with the text, and the quotation mark sits outside the measure.

[^4-ties]: Pandoc ties Mr. on its own, and the filter covers the rest. Chapter 16 tells what that once did to a test.
