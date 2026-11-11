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

A chapter file is plain Markdown, and most of what you type in one is Markdown you already know. Press reads every chapter in one fixed dialect, holds it to a short list of laws, and does a good deal of typesetting on your behalf. This chapter describes the dialect, the laws, and the few constructs that belong to press alone. The examples come from the Alice example, the sample book that ships with press, which user `alice` keeps on the workstation `hatter`.

## The dialect

Pandoc reads Markdown in many dialects. You build a dialect from a base format and a list of extensions, each one switched on with a plus sign. Press fixes the dialect for every build of every book. Every pandoc build in press reads the manuscript as `markdown+smart+yaml_metadata_block+fenced_divs+footnotes`, with `standalone: true` and `number-sections: true`. The same settings appear in all six defaults files under *src/press/data/defaults/*. A chapter that renders one way in the PDF therefore reads the same way in the EPUB and on the Web.

Table 4.1 lists the parts of the dialect and what each one gives you.

| Setting | Meaning |
|---------------|-------------------------------------------------------------|
| `markdown` | Pandoc's own Markdown is the base. Pipe tables, fenced code, line blocks, and definition lists all come from it. |
| `+smart` | Pandoc turns straight quotes into curly ones and three periods into an ellipsis. It also turns runs of hyphens into dashes, which the house forbids. |
| `+yaml_metadata_block` | Pandoc accepts a block of YAML metadata. |
| `+fenced_divs` | Pandoc reads the lines between two fences of three colons as one classed block. The set pieces use this extension. |
| `+footnotes` | Pandoc reads a note label in square brackets with a caret, and sets the note in the form each edition needs. |
| `standalone: true` | Pandoc writes a complete document, never a fragment. |
| `number-sections: true` | Pandoc numbers every chapter and every section heading. |

Table: Table 4.1. The pandoc dialect press reads

The `+smart` extension explains most of the character rules later in this chapter. Because pandoc curls quotes for you, you type the straight ones and let the machine choose the direction. Because pandoc turns hyphens into dashes, a sentence with two hyphens in it comes out with a dash in it, and the house does not set dashes in prose. The `number-sections` setting explains the heading rules. Pandoc already numbers your headings, so a number you type yourself prints twice.

@fig:page-anatomy shows where each construct in this chapter ends up on a printed page of the Alice example. The first four callouts are (1) the running head, (2) the folio, (3) the chapter title, and (4) a section heading. The other four are (5) the body text, (6) a footnote, (7) a blockquote in its box, and (8) a numbered figure with its caption. Two of the eight, the running head and the folio, have no markup at all. The house design sets them, and Chapter 9, *The house design*, describes them. You type the other six, and the rest of this chapter takes them in turn.

<!-- art: ARCHETYPE page anatomy. One miniature 6 by 9 page in thin outline, centred. Inside, top to bottom: small type at the top outer corner; a large flush-left chapter title, "Down the rabbit-hole"; a bold section heading; grey text lines; a light grey hairline box of grey italic lines; a framed shape with a caption line "Figure 1.1"; a short rule with two small lines under it; a page number at the bottom outer corner. Thin callout lines end in dots and lead to numbered margin circles: 1 running head, 2 folio, 3 chapter title, 4 section heading, 5 body text, 6 footnote, 7 blockquote box, 8 numbered figure and caption. The reader sees the whole page first. -->
![The parts of a printed page in the Alice example](assets/woodcuts/04-01-page-anatomy.png){#fig:page-anatomy .diagram width=full-measure fig-alt="A miniature book page in outline with eight numbered callouts pointing to the running head, the folio, the chapter title, a section heading, the body text, a footnote, a boxed blockquote, and a numbered figure with its caption."}

## Headings and chapters

A `#` heading is a chapter. Press sets pandoc's `top-level-division: chapter`, so one `#` at the start of a line starts a new chapter in every edition. A `##` heading is a section, and a `###` heading is a subsection. Pandoc numbers all three. In the PDF of the Alice example, the first section of the second chapter prints as 2.1, and its first subsection prints as 2.1.1.

Press finds chapters by their filenames. A *chapter file* is a file in *book/chapters/* whose name starts with a digit and ends in `.md`. An *appendix file* is a file in *book/appendices/* whose name is a single lowercase letter, a hyphen, and the rest of the name. Press sorts each group by filename and merges the chapters first, then the appendixes, then the generated subject index. The sort is lexical, so a file named `10-the-lobster-quadrille.md` sorts before `4-the-rabbit-sends-in-a-little-bill.md`. Press pads the numbers it hands out to two digits for that reason.

::: {.warning}
> **Warning:** Press silently ignores any other `.md` file in *book/chapters/* or *book/appendices/*. A file named `notes.md` or `chapter-four.md` never reaches the book, and no target tells you so.
:::

The simplest way to start a chapter is to let press create the file. The Alice example holds the first three chapters of Carroll's book. If its highest chapter file starts with `03-`, the next `press add chapter` creates a file starting with `04-`:

```
$ press add chapter "The rabbit sends in a little Bill"
```

Press lowercases the title and turns each run of characters that are not letters or digits into one hyphen, so the new file is *book/chapters/04-the-rabbit-sends-in-a-little-bill.md*. Press keeps a title you type verbatim as the heading. If you give a bare slug instead, such as `pool-of-tears`, press writes a sentence-case heading for you, `Pool of tears`. The new file holds a one-paragraph placeholder that says to delete it and begin. Press refuses to overwrite a file that already exists, and exits with status 1.

### Unnumbered chapters

A preface, a foreword, or an introduction is a chapter with no number. Mark its heading with `{.unnumbered}` or the short form `{-}`, and pandoc skips it when it counts. The command `press add chapter preface --front` creates *book/chapters/00-preface.md* with the heading `# Preface {.unnumbered}`. The `00-` prefix sorts the file ahead of chapter one. An unnumbered chapter also gets no chapter opening, which the section "Chapter openings and drop caps" later in this chapter describes.

Press has no support for parts. A book cannot group its chapters into Part One and Part Two, because the top-level division is the chapter and `#` always means a chapter. If your book needs parts, put the grouping in the chapter titles or in the preface.

### Numbers and capitals in headings

You never type a number in a heading. The checker refuses a heading such as `# 3. The pool of tears` with the message `manual number in heading`, because pandoc would print the number a second time beside its own. The same goes for section headings. Write `## Who stole the tarts` and let pandoc number it.

Headings are in sentence case: a capital on the first word and on proper names, and lowercase everywhere else. The checker refuses a title-case heading with the message `title-case heading:` followed by the heading text. The test is mechanical. The checker sets aside the first word, the words on a fixed list of 21 small words, and any word in all capitals. If at least three candidate words remain, and 80 percent or more of them start with a capital, the checker calls the heading title case.

Example 4.1 shows the test at work on the heading of Carroll's fourth chapter.

**Example 4.1. Two headings for the same chapter**

```
# The Rabbit Sends In A Little Bill
# The rabbit sends in a little Bill
```

In the first heading, the candidates are at least Rabbit, Sends, Little, and Bill, and every one of them starts with a capital, so the checker refuses it. In the second, only Bill keeps its capital, because Bill is the lizard's name. One capital in four or five candidates is well under the line, and the checker accepts it. A short heading escapes the test entirely. `# Down the Rabbit-Hole` has too few candidates after the first word and the small words, so the checker lets it pass, although the house would still write it in sentence case.

::: {.tip}
> **Tip:** Type the title in sentence case when you run `press add chapter`. Press keeps the title verbatim, so a title-case title becomes a title-case heading, and the next `press check` refuses it.
:::

### Referring to other parts of the book

Press numbers figures and lets you cite them by name, but it has no machinery for citing chapters or sections. Give a figure an identifier and cite it as `@fig:page-anatomy`, and press prints "Figure 4.1" with a link. A citation of an identifier press does not know stays in the text as a raw citation, which you will see at once in a proof. For a chapter or a section, write the reference in words: "see Chapter 6, *Checking the manuscript*". Chapter 5, *Figures, plates, and illustrations*, covers figure identifiers in full.

![The compositor at the frame, setting a chapter by hand](assets/woodcuts/the-compositor-at-the-frame.png)
<!-- art: a compositor in shirtsleeves standing at a sloped composing frame, seen three-quarter from the left at eye level, the upper and lower type cases angled before him, his left hand holding a brass composing stick with a line of type in it, his right hand lifting one sort from the case, the manuscript copy pinned to a small stand at eye height, a galley with set lines resting on the frame's ledge, a gas lamp bracket above; portrait composition; wood engraving with dense hatching and crosshatching, single black ink, no gray washes, no lettering anywhere -->

## Characters you may and may not type

The checker holds every chapter file to a *glyph law*: a short list of the characters that may appear in book prose. The law exists for the print interior, as the checker's message says: a character outside the law is outside the print-font set. The checker refuses such a character before any build begins.

Table 4.2 gives the law exactly.

| Characters | Meaning |
|---------------|-------------------------------------------------------------|
| Tab, line feed, carriage return | These are the only control characters the law allows. They hold a text file together. |
| U+0020 through U+007E | This is printable ASCII: the space, the letters, the digits, and the punctuation on a US keyboard. |
| U+00C0 through U+017F | These are the accented Latin letters, such as the e in "café" or the c in "façade". The multiplication and division signs also fall inside this range. |

Table: Table 4.2. The characters the glyph law allows in book prose

Nothing else passes, and the gap between the two ranges is the surprising part. The block from U+00A0 through U+00BF holds the copyright, degree, section, and pound signs. It also holds the guillemets, the fractions, the inverted question mark, and the non-breaking space. Every one of them fails. Greek letters, mathematical symbols, and emoji fail too. For each one, the checker prints `glyph U+XXXX is outside the print-font set`, with the character's code point in place of the four X's.

Example 4.2 shows some of the characters the law refuses. They appear here inside a code block, because the checker reads prose and skips fenced code.

**Example 4.2. Characters the checker refuses in prose**

```
U+00A0      no-break space (invisible)
U+00A3  £   pound sign
U+00A7  §   section sign
U+00A9  ©   copyright sign
U+00B0  °   degree sign
U+00BD  ½   vulgar fraction one half
U+2013  –   en dash
U+2014  —   em dash
U+2018  ‘   left single quotation mark
U+2019  ’   right single quotation mark
U+201C  “   left double quotation mark
U+201D  ”   right double quotation mark
```

In practice you write the word: "thirty degrees", "five pounds", "section 4". A book's copyright line belongs to the generated front matter, which Chapter 10, *Front matter, the index, and the table of authorities*, describes. You never need the sign in a chapter.

::: {.warning}
> **Warning:** Text pasted from a word processor or a Web page arrives full of curly quotes, dashes, and non-breaking spaces. Run `press check` after every paste. The non-breaking space is invisible on screen, and only the checker will find it.
:::

### The dash law

The house sets no em dash and no en dash in prose. The checker refuses the em dash (U+2014), the en dash (U+2013), and the four curly quotation marks in the prose of a chapter. You type straight quotes and apostrophes, and pandoc curls them in every edition.

The two hyphens are a quieter case. Because of `+smart`, pandoc turns two hyphens into an en dash and three into an em dash. The checker does not refuse the hyphens in source, so a sentence with two hyphens in it passes `press check` and then prints with a dash. The house law is plain about what to do instead: rewrite the sentence. A comma, a colon, a period, or a pair of parentheses carries almost every job a dash does, and the rewrite is usually the better sentence. Example 4.3 shows one such rewrite.

**Example 4.3. A sentence with a dash and its rewrite**

```
The Hatter's watch told the day of the month -- not the hour.
The Hatter's watch told the day of the month, and never the hour.
```

The ellipsis is the third conversion. You type three periods, and pandoc sets the single ellipsis character in the output. The ellipsis character, U+2026, lies outside the glyph law, so you could not type it in prose if you tried.

### What the audit directories get

A book can name extra directories for the checker to read in `audit-dirs` in *config/house-rules.yaml*. Files there get a lighter battery than the manuscript. The checker applies the dash rules and the banned-phrase rules, but not the curly-quote rule, the glyph law, or the book's own banned patterns. A heading or paragraph problem in an audit directory is a warning, where the same problem in a chapter is an error. Chapter 6, *Checking the manuscript*, covers house rules and the audit directories in full.

A book adds its own refusals in the same file, under `banned-patterns`. Each pattern is a case-sensitive regular expression, matched as written, with a label that the checker prints as `<file>:<line>: <label>`. The checker refuses a pattern that is not a valid regular expression, and its message quotes the pattern.

## Paragraphs, footnotes, and quotations

A paragraph is any run of lines with no blank line inside it, as in all Markdown. Press adds one law of its own: a paragraph must be under 190 words. A paragraph of 190 words or more fails `press check`.[^paragraph-law] The message is `paragraph N has W words (the law is under 190; split it)`, where N numbers the paragraph and W counts its words. In an audit directory the same paragraph draws a warning.

The law is a typesetting law as much as a prose law. A very long paragraph turns a page into one grey block and gives the eye nowhere to rest. Split the paragraph at the point where its subject turns.

Press forbids trailing whitespace everywhere: in prose, in headings, and inside code blocks too. Trailing whitespace is invisible, and a line ending in two spaces is a hard line break in Markdown. A stray pair of spaces can change the page and leave your editor's screen unchanged.

::: {.tip}
> **Tip:** Set your editor to strip trailing whitespace when it saves a file. The checker refuses trailing whitespace even inside code blocks, where it reads nothing else.
:::

### Footnotes

Footnotes use pandoc's standard syntax. You put a label in square brackets with a caret at the point of reference. The note itself goes on a line of its own that starts with the same label and a colon. The PDF sets each note at the foot of its page. The EPUB and the Web reader collect the notes as linked notes. Press has no separate setting for endnotes.

```
Alice had not a moment to think about stopping herself.[^well]

[^well]: Either the well was very deep, or she fell very slowly.
```

A label must be unique within its chapter file. A short, descriptive label such as `well` is easier to find again than a number, and pandoc numbers the notes for you in each edition.

### Quotations and epigraphs

A blockquote is a paragraph whose lines start with `>`. In the PDF, the house sets each one in a framed box with a light paper-grey ground, a 0.4-point rule in grey, and small italic type. The jargon lint skips blockquotes by default, so a quoted passage that uses a word on the watchlist does not trip it.

A chapter epigraph is an ordinary blockquote placed right after the chapter heading. Press has no special syntax for one. The drop cap, if the book has one, skips the blockquote and lands on the first real paragraph after it. The book's own epigraph, the one on a front-matter page of its own, comes from `epigraph.quote` and `epigraph.attribution` in *config/front-matter.yaml* instead, and Chapter 10 describes it.

```
# Down the rabbit-hole

> "And what is the use of a book," thought Alice,
> "without pictures or conversations?"

Alice was beginning to get very tired of sitting by her sister...
```

### Line blocks and definition lists

Pandoc's line block keeps every line break you type. Start each line with a vertical bar and a space, and pandoc sets the lines exactly as you broke them. A short verse, an address, or a list of signatures can go in a plain line block. The set pieces later in this chapter take a line block as their input and give it a shape.

A definition list is standard pandoc too: a term on one line, then a line starting with a colon and a space that holds the definition. We recommend it for a glossary appendix, where each term needs a sentence or two after it.

### Sentences that other files name

Three kinds of configuration point into your prose, and each one constrains how you revise. Press matches the terms in *config/index-terms.yaml* against the text by pattern, so you never mark up the manuscript for the index. A claim in *config/authorities.yaml* is an exact fragment of a sentence in your manuscript. If you reword that sentence, the claim no longer matches, and the build fails. A *sentinel* is a phrase in `verify-sentinels` in *config/metadata.yaml* that the PDF verifier looks for in the finished book, so it must survive every revision word for word. Chapter 10 covers the index and the authorities, and Chapter 8, *Verifying the artifacts*, covers sentinels.

## Tables

Press uses pandoc's pipe tables. Each row is a line, a vertical bar separates the cells, and a row of hyphens under the first row marks it as the header. A line that starts with `Table:` after the table gives it a caption. Example 4.4 shows a small table drawn from the first two chapters of the Alice example.

**Example 4.4. A pipe table with a header row and a caption**

```
| Item | What it does |
|------------|-------------------------------------------------|
| The bottle | Alice shrinks until she is ten inches high. |
| The cake | Alice grows until her head strikes the roof. |

Table: What Alice swallows
```

Give every table a header row. In the HTML edition and on the reader site, press labels each cell of a headed table with the name of its column, in a `data-label` attribute. The reader stylesheet uses those labels on a narrow screen. Below a width of 34rem, it turns each row of the table into a card, with each cell set under its column's name.

Keep tables small. Two or three columns read well at every width, on a 6 by 9 page and on a small screen alike. A table of seven columns crowds a 6 by 9 page, and each of its cards runs to seven lines on a narrow screen. If a table needs that many columns, it is usually two tables.

## Code

Code goes in a fenced block: a line of three backticks, the code, and another line of three backticks. In the PDF, the house sets fenced code in Source Code Pro scaled to 0.86. The `fvextra` package breaks a long line wherever it must, with the options `breaklines` and `breakanywhere`. Nothing runs off the page, but a broken line is harder to read than one you broke yourself.

The prose rules skip fenced code, with one exception. The checker reads no glyphs, dashes, or paragraph lengths inside a code block. You can show a session with real output there, or the characters from Example 4.2. The exception is trailing whitespace, which the checker refuses in code exactly as it does in prose.

A short session looks like this:

```
$ press check
...
```

Show the prompt, then the command, then the output. Elide long or boring output with a line holding three periods. We use the `$` prompt throughout this book, on the workstation `hatter` and on the CI host `printshop` alike.

::: {.tip}
> **Tip:** Keep code lines to 72 characters or fewer. The PDF will break a longer line for you, but it breaks it at the measure, which is rarely where a reader expects the break.
:::

## Chapter openings and drop caps

A *chapter opening* is the treatment of the first letter of each chapter. The book sets it with `chapter-opening` in *config/metadata.yaml*, and press merges that setting over the design profile's default. Every profile that ships with press defaults to `none`, so a new book opens its chapters with a plain paragraph. The Alice example sets a three-line drop cap with small caps for the rest of the first word.

Table 4.3 lists the three settings.

| Setting | Default | Meaning |
|-----------------|-------------------|---------------------------------------------|
| `style` | the profile's (`none`) | The value `none` sets a plain first paragraph. The value `drop-cap` sets a large initial that sinks into the text. The value `ornate` sets a foliate initial in print. |
| `lines` | 3 | This is the number of text lines the initial spans. |
| `small-caps-remainder` | true | When this is true, press sets the rest of the first word in small caps. |

Table: Table 4.3. The chapter-opening settings in config/metadata.yaml

You can set them from the command line, which checks each value before it writes the file:

```
$ press config set chapter-opening.style drop-cap
```

In *config/metadata.yaml* the same settings form one block, as Example 4.5 shows.

**Example 4.5. The Alice example's chapter opening**

```
chapter-opening:
  style: drop-cap
  lines: 3
  small-caps-remainder: true
```

### Where the drop cap lands

The `chapter-dropcap.lua` filter finds the first eligible paragraph after each `#` heading. It skips any heading marked `{.unnumbered}` or `{.unlisted}`, so a preface opens plainly. On its way down the chapter it passes over blockquotes, code blocks, lists, tables, rules, and figures. A chapter that opens with an epigraph therefore gets its drop cap on the first paragraph of prose, where the reader expects it.

In the PDF, the filter wraps the LaTeX `lettrine` package. Press guards the initial with `\Needspace*{4\baselineskip}`, so a drop cap never starts at the foot of a page with no room for its lines. The settings it passes are `lines=3,depth=0,findent=2pt,nindent=0pt`, and the rest of the first word goes in `\scshape`. The initial is always one grapheme, so an accented capital or a letter with a combining mark stays whole.

### Dialogue openers

The second chapter of the Alice example opens with speech:

```
"Curiouser and curiouser!" cried Alice (she was so much
surprised, that for the moment she quite forgot how to speak
good English).
```

The first character of that paragraph is a quotation mark, and the letter after it is the one that should drop. Press calls the quotation mark the *lead*, and it sets the capital C as the drop cap. It hangs the lead into the left margin at body size, so the C stays square with the text below it.[^hung-quote] On the Web, the lead carries the class `.drop-cap-lead` and a negative left margin of .52em, which gives the same effect.

### The ornate style

The `ornate` style sets the initial in the yinit foliate font, from the `yfonts` package in the TeX Live fonts-extra collection. That font exists only in print. The Web and EPUB editions set a styled display capital instead, at 3.6em in the ornament colour. It uses a script face such as Luminari, Apple Chancery, or Zapfino, if the reader's machine has one.

::: {.warning}
> **Warning:** Never choose a sentinel from the first words of a chapter. The drop cap splits the first word and sets its remainder in small caps, so the opening phrase no longer matches exactly in the PDF, and the verifier fails it. Pick a phrase from the middle of the chapter.
:::

## Scene breaks

A *scene break* is a pause inside a chapter, a change of time or place that needs more than a new paragraph. In the manuscript you type it as a Markdown thematic break: a line holding three asterisks with spaces between them, `* * *`. The key `scene-break` in *config/aesthetic.yaml* chooses how press draws it, and the `scene-break.lua` filter does the drawing.

Table 4.4 lists the three values.

| Value | Meaning |
|---------------|-------------------------------------------------------------|
| `rule` | This is the default. The PDF sets a plain horizontal rule, and the reader sets a small diamond between two hairlines that fade at their ends. |
| `asterism` | Press sets three asterisks, centred and spaced a quad apart in the PDF, and as a paragraph of class `asterism` on the Web. |
| `fairy-dust` | Press sets a staggered array of eleven asterisks in three rows of four, three, and four. It follows Tenniel's 1866 Alice. |

Table: Table 4.4. The scene-break ornaments

@fig:scene-break-ornaments shows each ornament as it appears in the PDF and on the reader site. The Alice example uses `fairy-dust`, as Example 4.6 shows.

<!-- art: ARCHETYPE matrix. A grid of three rows by two columns, thin rules between cells. Column heads in small sans: "PDF" left, "Reader" right. Row labels down the left in small monospace: "rule", "asterism", "fairy-dust". Each cell shows the ornament in black between grey text lines. Rule, PDF: a plain thin horizontal rule. Rule, Reader: a small solid diamond centred between two hairlines that taper away at their outer ends. Asterism, both cells: three centred asterisks with wide even spaces. Fairy-dust, both cells: eleven small asterisks in three centred staggered rows of four, three, and four. The reader sees the three ornaments down the rows first, then that only the rule differs between the columns. -->
![The three scene-break ornaments in the PDF and on the reader site](assets/woodcuts/04-03-scene-break-ornaments.png){#fig:scene-break-ornaments .diagram width=full-measure fig-alt="A grid of three rows and two columns. A plain rule, three spaced asterisks, and a staggered field of eleven asterisks each appear once as printed in the PDF and once as shown on the reader site, where the rule becomes a diamond between fading hairlines."}

**Example 4.6. The Alice example's scene break**

```
scene-break: fairy-dust
```

In the PDF, the fairy dust is the LaTeX macro `\PressFairyDust`, with a step of 1.9em between its asterisks. On the Web it is a division of class `fairy-dust`. The division carries the role of a separator and is hidden from screen readers, which have no use for eleven asterisks. You type the same `* * *` whatever the book chooses. If the aesthetic changes later, every scene break in the book changes with it, and no chapter file needs an edit.

## The set pieces

Some passages need a shape of their own: an address that steps down the page, a poem on its own measure, a poem shaped like its subject. Press calls these the *set pieces*, and it has three: `cascade`, `verse`, and `tail`. Each one is a fenced div, a block between two lines of three colons, with the set piece's name after the first fence. Inside it you normally put a line block, and the `set-pieces.lua` filter lays out the form. If the div holds plain paragraphs instead of a line block, the filter counts each paragraph as one line.

@fig:set-pieces shows what each of the three does to the same four lines. They are the address Alice imagines writing to her own right foot, when she grows too tall to reach it.

<!-- art: ARCHETYPE before/after, three frames. Three identical small page frames side by side, no arrows. Each frame holds the same four short serif lines: "Alice's Right Foot, Esq.", "Hearthrug,", "near the Fender,", "(with Alice's love)." Frame (a): each line starts one equal indent further right than the line above. Frame (b): all four lines share one left edge set well in from the frame. Frame (c): the lines swing right, left, then right in a gentle curve, and the type shrinks line by line. Under each frame a small sans label: "(a) cascade", "(b) verse", "(c) tail". The reader sees first that the words are the same in all three frames. -->
![What cascade, verse, and tail do to the same four lines](assets/woodcuts/04-02-set-pieces.png){#fig:set-pieces .diagram width=full-measure fig-alt="Three small frames side by side, each holding the same four-line address. In the first the lines step to the right one indent at a time, in the second they share one indented left edge, and in the third they swing in a curve and shrink line by line."}

Table 4.5 summarizes the three.

| Set piece | Meaning |
|---------------|-------------------------------------------------------------|
| `cascade` | Each line steps one indent further in than the line above it. It suits an address or an inscription. |
| `verse` | The lines take the house stanza measure, indented from the left, with space above and below. It suits a poem or a song. |
| `tail` | The lines wind from side to side and shrink as they go. It exists for the Mouse's Tale. |

Table: Table 4.5. The three set pieces

### Cascade

A cascade indents each line by 2.4em times one less than its line number. The first line sits at the left edge, the second at 2.4em, the third at 4.8em, and so on down. The Alice example uses a cascade for the address in Carroll's second chapter, as Example 4.7 shows.

**Example 4.7. A cascade in the Alice example**

```
::: cascade
| Alice's Right Foot, Esq.
| Hearthrug,
| near the Fender,
| (with Alice's love).
:::
```

### Verse

A verse block sets its lines to the house stanza measure, which the PDF calls `\PressVerse`. Every line starts 3em in from the left, with no paragraph indent, and the block has 0.7em of space above and below it. A blank line between groups of lines gives a stanza gap. An opening quotation mark at the start of a line hangs into the margin by protrusion, so the letters of every line align. On the reader site, the block carries the class `.verse`, with a left margin of 2.4em. Example 4.8 shows a verse block holding the start of the Lobster's song.

**Example 4.8. A verse block**

```
::: verse
| 'Tis the voice of the Lobster;
| I heard him declare,
| "You have baked me too brown,
| I must sugar my hair."
:::
```

### Tail

The tail is the most elaborate of the three. It exists for the Mouse's Tale, which Carroll printed as a poem that winds down the page in the shape of a mouse's tail. The filter offsets each line from the left by 3.0em times the sine of 2 pi t, where t is the line's position along the tail. The lines therefore swing out and back, and the type tapers as the tail goes down. In the PDF the lines run from `\normalsize` through `\small`, `\footnotesize`, and `\scriptsize` to `\tiny`. On the Web they shrink from 1em to .68em.

**Example 4.9. The opening of the Mouse's Tale as a tail**

```
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

The set pieces change the layout of the lines and nothing else. The words stay live text in every edition, so a reader can search for them, copy them, and hear them from a screen reader. The plain-text and DOCX editions get a native line block, with the line breaks kept and no shape. A book that uses no set pieces renders byte for byte as it did before press added them.

## The fine work press does for you

Some typesetting is too fine to ask of an author. Press does it in a Lua filter, `typographic-spacing.lua`, which runs in every edition. The filter puts a *tie*, a non-breaking space, between a word and the word it must never leave at the end of a line. In the PDF the tie is LaTeX's `~`. In the other editions it is the non-breaking space character, U+00A0, which the glyph law forbids you to type yourself.

The filter ties in three places, and none of them asks anything of you. After a title, it ties the title to a following capitalized word, for Mr., Mrs., Ms., Dr., Prof., St., Mt., Sr., Jr., Rev., Hon., Capt., Sgt., Gen., Col., Lt., and Fr. After a reference form, it ties the form to a following digit, for p., pp., No., Nos., Fig., Figs., Ch., Vol., Pt., and Eq. Between chained initials, it ties each initial to the next, as in "C. L. Dodgson".[^ties]

The press states the principle plainly. The manuscript stays plain prose, the house does the fine work, and the filter leaves ordinary sentences exactly as you typed them, every full stop included. You never type a tie of your own. You type "Dr. Dodgson" and "p. 42", and the filter keeps each pair on one line in the PDF, the EPUB, and the reader alike.

The same principle runs through this whole chapter. You type straight quotes and three periods, and pandoc sets curly quotes and an ellipsis. You type `* * *`, and the aesthetic chooses the ornament. You type a bare heading, and pandoc numbers it. You give a figure an identifier, and the `figure-numbering.lua` filter numbers it once, by chapter, and turns every `@fig:` citation into "Figure 4.1" with a link. Press needs no pandoc-crossref for this.

::: {.sidebar}
> **A stray asterisk and Fig-ure**
>
> The fine work has to be right, because an author cannot fix it from the manuscript. Two small faults in the placed figures of the PDF show what that means. The first was an asterisk. In figures with a placement, the float package's starred command `\caption*` printed a stray asterisk above the figure. Nothing in the manuscript had an asterisk in it. The author could only look at the proof and wonder.
>
> The second fault came with the wraps. A figure with text running around it has a narrow caption. In a narrow enough wrap, LaTeX hyphenated the label itself, and the caption began "Fig-" on one line and "ure" on the next. Again, nothing in the manuscript caused it, and nothing in the manuscript could stop it.
>
> The fixes went into the house design. The caption package became the single authority for every caption in the book. The label went inside an `\mbox`, which LaTeX never breaks. An author who writes a figure today types a caption and nothing else, and the label prints whole.
:::

The next chapter, *Figures, plates, and illustrations*, takes up the plates, the numbered figures, and the placements that put them on the page.

[^paragraph-law]: According to the press's change log, the checker began to enforce the paragraph law in press 1.7.0.

[^hung-quote]: The press's notes call this Bringhurst's rule. The capital aligns with the text, and the quotation mark sits outside the measure.

[^ties]: Pandoc ties Mr. on its own. For that reason, the press's test for the tie once passed with no filter in place at all. The Lua coverage work for press 3.0.2 found the empty test. It also found that the Lua tests skipped silently in CI until CI set `PRESS_REQUIRE_LUA=1`.

<!-- index: glyph law; dash law; em dash; ellipsis; title-case heading; press add chapter; unnumbered chapter; paragraph law; trailing whitespace; footnote; blockquote; epigraph; line block; pipe table; fenced code; chapter-opening; drop cap; dialogue opener; scene break; fairy-dust; set piece; cascade; verse; tail; tie -->
