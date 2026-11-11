# House Style Guide: The 1995-2003 Animal-Book Idiom

A guide for writers and an illustrator producing a technical book about a
Python command-line publishing pipeline ("press") that reads as if it came
off the shelf of a Unix bookstore around 1999. It describes the idiom
O'Reilly & Associates established in that period and how to reproduce it
without using their trademarks, their sentences, or their logo.

**Sources consulted.** The prefaces and chapters of *Using Samba* (samba.org
mirror), *TCP/IP Network Administration* and *Mac OS X for Unix Geeks* (CD
Bookshelf HTML editions), an Oracle web-applications title (owl/turkey icon
convention), the colophons of *Programming Perl*, 3rd ed. (2000), *Perl &
LWP* (2002), and *Information Architecture for the World Wide Web*, and Edie
Freedman's essay "A short history of the O'Reilly animals" (oreilly.com).
Where this guide states a convention from general knowledge of the books and
not from a page fetched for it, it says "typically".

**One correction to the brief.** In this period the interior headings were
not Franklin Gothic. The 1990s colophons say "The text and heading fonts
are ITC Garamond Light and Garamond Book" (*Programming Perl*, 3rd ed.).
From about 2002 the interior moved to Linotype Birka for text, Adobe Myriad
Condensed for headings, and TheSans Mono Condensed for code. Franklin Gothic
belongs to the later Hacks series. Pick one of the two systems and use it
throughout. Section 1.8 recommends the earlier one.

---

## 1. Book Architecture

### 1.1 Front matter, in order

1. **Half-title** (recto): the title alone, no subtitle.
2. **Series/also-by page** (verso, optional): "Other titles from [Press]".
3. **Title page** (recto): title; the edition line if not first ("Second
   Edition"); author names, one per line or joined with "and"; the
   publisher's name and a city list set small at the foot (the originals
   read like "Beijing · Cambridge · Köln · Paris · Sebastopol · Taipei ·
   Tokyo"). Use one or two plausible cities for our neutral press.
4. **Copyright page** (verso). It is dense, small, and laid out in this
   order:
   - `Title` by Author
   - Copyright © 2001 Holder. All rights reserved.
   - Printed in the United States of America.
   - Published by [Neutral Press], street address, city.
   - Editor: ...  Production Editor: ...  Cover Designer: ...
   - **Printing History:** a two-column list of dates and events:
     ```
     Printing History:
        March 1999:      First Edition.
        November 2001:   Second Edition.
     ```
   - The trademark notice, neutralized (do not copy the original's wording
     or name its marks). Use this:
     > The Workbench Series and the Workbench logo are trademarks of
     > Ferrule & Quire. Many of the designations used by manufacturers and
     > sellers to distinguish their products are claimed as trademarks.
     > Where those designations appear in this book and the publisher was
     > aware of a trademark claim, the designations have been printed in
     > caps or initial caps. The association between the image of a
     > [animal] and the topic of book publishing is a trademark of Ferrule
     > & Quire.
   - The disclaimer: "While every care has been taken in preparing this
     book, the publisher and authors accept no responsibility for errors or
     omissions, or for damages resulting from use of the information it
     contains."
   - ISBN line, and a print-run code (`[M]  [10/01]`) at the bottom.
5. **Table of Contents**: Preface, chapters (optionally grouped by Part),
   appendixes, Glossary, Index. Show chapter titles and A-heads, never
   B-heads.
6. **Preface** (section 1.2).

The originals have no foreword unless a famous person wrote one, no "Praise
for" pages before 2003, and no dedication page. A dedication, if any, is one
line on the copyright page or the half-title verso.

### 1.2 Preface

The heading is "Preface". It opens with two to four untitled paragraphs on
why the subject matters and why the book exists, often a short history ("When
we started running X in 1996..."). Then come the titled sections, in this
order:

| Order | Section | Typical length |
|---|---|---|
| 1 | Who Should Read This Book (variants: "Audience", "Audience for This Book") | 1-3 paragraphs |
| 2 | Organization of This Book (variants: "What's in This Book", "Organization") | one paragraph per chapter |
| 3 | Versions / "What's New in This Edition" (later editions only) | 1-2 paragraphs or a short list |
| 4 | Conventions Used in This Book | a definition list, 6-10 entries |
| 5 | Using Code Examples (2001 onward) | 1 paragraph |
| 6 | How to Contact Us (variants: "Comments and Questions", "We'd Like to Hear from You") | address block plus 2 paragraphs |
| 7 | Acknowledgments | 1-3 pages, often split by author with subheads |

A preface runs 6 to 12 pages. *Using Samba*'s preface has this shape:
Audience, Organization, Conventions, How to Contact Us, then Acknowledgments
split into one subsection per author.

### 1.3 Parts

Use Parts only when there are more than about twelve chapters. A Part divider
is a recto page reading "Part I" and then the Part title ("Getting Started"),
with an optional one-paragraph abstract under it. The verso is blank.
Reference sections typically become their own Part: "Part III, Reference".

### 1.4 Chapters

- **Count:** 8 to 16 chapters for a "Learning" or "Managing" book; 15 to 25
  for a "Definitive Guide".
- **Length:** a chapter is 15 to 40 printed pages, roughly 5,000 to 12,000
  words. Chapter 1 is shorter (8 to 15 pages), an overview with a
  "quick tour" or "a five-minute install". The longest chapter is typically
  the configuration-reference chapter.
- **Whole book:** 250 to 450 pages for a Learning, Managing, or Nutshell
  book; 500 to 900 for a Definitive Guide.

### 1.5 Appendixes

The spelling is *appendixes*, not appendices. They are lettered A, B, C. For
our subject, use these:

- **Appendix A, Command Reference**: one entry per subcommand in man-page
  shape (Name / Synopsis / Description / Options / Examples / See Also).
- **Appendix B, Configuration File Reference**: an alphabetical list of every
  key, with type, default, and a one-paragraph meaning.
- **Appendix C, Error Messages**: the message in constant width, then
  "Cause" and "Remedy" paragraphs.
- **Appendix D, Installing the Toolchain**: platform by platform.
- **Glossary**: about 40 to 80 terms, alphabetical, with the term in bold.
- An optional fold-out-style **Quick Reference** card: two pages of dense
  tables.

### 1.6 Index

The index is two-column and set small. Main entries are lowercase except
proper nouns. Commands and filenames keep their typography in the index:
constant width for `press check`, italic for *metadata.yaml*. Use
subentries generously, and "See also" cross-references in italic. Symbols
come first: `$` prompt, `--draft` option. The index is credited by name in
the colophon.

### 1.7 Colophon

The colophon is the last page and has a fixed form. Paraphrased to its
structure, from *Programming Perl*, 3rd ed. and *Perl & LWP*:

1. **A boilerplate opening sentence** about the look of the series coming
   from reader comments and experiment, and the animal giving "personality"
   to technical topics. Write our own version: "The look of Workbench books
   comes from listening to readers and from a good deal of trial and error."
2. **The animal paragraph** (the heart of it): "The animal on the cover of
   *[Title]* is a [common name] (*Latin binomial*)." Then 4 to 8 sentences of
   encyclopedic natural history: range, size, diet, habits, lifespan, and
   often a note on its conservation status. The register is a museum label,
   dry and specific ("They travel in single file and live about 13 years").
   There is no joke about the topic, and no link drawn between animal and
   software.
3. **Production credits**: "[Name] was the production editor and
   copyeditor for *[Title]*. [Name] proofread... [Name] provided quality
   control. [Name] wrote the index."
4. **Cover**: "[Name] designed the cover of this book, based on a series
   design by [Name]. The cover image is a 19th-century engraving from
   [source]. [Name] produced the cover layout with [tool] using [font]."
5. **Interior**: "[Name] designed the interior layout. The text and heading
   fonts are [X]; the code font is [Y]. This book was converted from
   [source format] to [output] by [tools]." The colophons name the actual
   toolchain: *Programming Perl*, 3rd ed. records POD converted to DocBook
   SGML, a Perl filter to gtroff, and groff generating PostScript.
6. **Illustrations**: "The illustrations that appear in the book were
   produced by [Name] using Macromedia FreeHand [n] and Adobe Photoshop [n]."
7. A closing credit line: "This colophon was written by [Name]."

For our book the toolchain sentence should describe the press pipeline
itself: Markdown through pandoc and LuaLaTeX. That is the self-referential
joke, and it is the only one the book is allowed.

### 1.8 Typography (interior)

Recommended system ("classic", about 1997-2001):

- Body: ITC Garamond Light, about 10.5/13, justified. A free stand-in is
  EB Garamond.
- Headings: Garamond Book or bold in the same family. Chapter titles are
  large, flush left, with the chapter number set large above or beside them.
- Code: a Courier-style constant width in the earliest books. Use one
  monospace with a true bold and italic (for example, a free Courier
  revival or Inconsolata).
- Running heads: verso carries the chapter title, recto the A-head, both
  small, with page numbers at the outer edge.

---

## 2. Chapter Anatomy

### 2.1 The opener

- The chapter page is "Chapter 4" and then the title ("Configuring the
  Build"), flush left, with nothing between the title and the first paragraph.
- **Older Nutshell style (to about 1998):** a small ruled box in the outer
  margin or at the top, headed **In this chapter:**, lists the A-heads:
  ```
  In this chapter:
  • Kernel Configuration
  • Linux Kernel Configuration
  • The Internet Daemon
  • Summary
  ```
  The CD Bookshelf HTML editions render this as a "Contents:" list. Use this
  device: it dates the book exactly.
- **First paragraph:** no heading precedes it. It is a short orientation of
  2 to 5 sentences that says what the subject is and why the reader is here.
  It is often followed by a second paragraph that names the chapter's scope
  in a sentence, or in a short bulleted list introduced by "This chapter
  covers:" or "In this chapter, we'll look at:". The opener of *TCP/IP
  Network Administration*, chapter 5, states a universal fact ("Every UNIX
  computer that runs TCP/IP has a technique for incorporating...") and then
  names the two files the chapter will examine.

### 2.2 Heading hierarchy

| Level | Name | Style | Capitalization |
|---|---|---|---|
| 0 | Chapter title | large, numbered | Title Case |
| 1 | A-head | bold, large | Title Case ("Running the Checker") |
| 2 | B-head | bold, smaller | Title Case |
| 3 | C-head | bold or italic run-in | Title Case, sometimes sentence case |

Rules:

- Never skip a level, and never put two headings in a row without text
  between them.
- Section numbers (5.1, 5.2) appear in the CD Bookshelf HTML and some
  Nutshell books. The Definitive Guides typically print unnumbered heads.
  Choose one style and keep to it. Recommended: unnumbered heads, numbered
  chapters.
- Headings are often gerunds or noun phrases ("Installing from Source",
  "The Configuration File", "Verifying the PDF"). They are never questions or
  clever.

### 2.3 Closing

- **Older books** end on the last technical point, or with a one-paragraph
  forward pointer: "In the next chapter, we'll put these files to work."
- **Some books (the TCP/IP book, for example) end with a short "Summary"
  A-head** of one or two paragraphs in prose, not bullets.
- There are no "Key Takeaways", "Exercises", or "What You Learned" boxes,
  except in Learning-series books, which may have numbered exercises with
  answers in an appendix (as *Learning Perl* does).

### 2.4 Cross-references

- Chapters: "see Chapter 4, *Configuring the Build*" (the title in italic in
  print; quoted titles also occur).
- Sections: "as described in the section "Verifying the PDF" in Chapter 7"
  or, within the chapter, "as described in the section "Verifying the PDF"
  later in this chapter." Write "earlier" and "later", not "above" and
  "below", except of an adjacent example.
- Numbered items: "Example 3-2 shows...", "as shown in Figure 3-1", "the
  options are listed in Table 3-1". Capitalize the noun.
- Appendixes: "see Appendix B, *Configuration File Reference*".
- Man pages: "see make(1)", "the crontab(5) manpage". Both "manpage" and
  "manual page" are period-correct.
- External: "the pandoc Web site at *http://pandoc.org/*". URLs are italic,
  with a trailing slash and the http:// shown.

### 2.5 Terms and in-text typography

- A **new term is italicized at first use**, defined in the same sentence,
  and never italicized again: "Press calls each of these steps a *target*."
- **Filenames, directories, URLs, commands named as programs, and options**
  are typically italic in 1990s books (*/etc/inetd.conf*, the *-f* option).
  2000s books moved commands and options into constant width. Recommended:
  italic for files, directories, and URLs; constant width for commands,
  options, config keys, environment variables, and anything you could type.
  Record the choice in the Conventions section and hold to it.
- Program names as proper nouns are roman: "Samba", "LuaLaTeX", "Press".
  The command is in constant width: `press`.

---

## 3. Voice and Prose

### 3.1 Stance

- **Second person, present tense**, "you" throughout ("You can override
  this in the configuration file"). Use first-person plural for the authors'
  judgments and history ("We recommend", "we found this out the hard way").
  Never "I" in a multi-author book, except in the Acknowledgments.
- **Plain and direct.** The register is a senior colleague at the next desk:
  someone who ran the thing in production, has been paged at 3 a.m. over it,
  and is not trying to sell it to you.
- **Dry humor**: one understatement every few pages, never a pun in a
  heading. "This is not a hang, although it is a very convincing imitation
  of one."
- **Opinions are allowed and labeled**: "In our experience, ..." or "We
  strongly suggest you ...".

### 3.2 Sentence texture

- Average sentences of 18 to 24 words, with real variation: a 6-word
  sentence after a 35-word one. Paragraphs run 3 to 7 sentences. One-line
  paragraphs are rare.
- Explain the **why** and the **history**. The books routinely stop to say
  how a thing got this way ("The name is a holdover from...", "Early
  versions of the program did not..."). A chapter on configuration will
  explain the defaults before it lets you change them.
- Concrete nouns: real hostnames (`toltec`, `crimson`), real paths, real
  numbers. *Using Samba* hangs its examples on a fixed fictional network. Do
  the same with a fixed sample book; we suggest a public-domain novel.

### 3.3 The scar paragraph

The scar paragraph is a warning drawn from experience, and it is the most
characteristic device in these books. It tells a short story with a cost and
then gives the rule:

> The first time we built a book with an oversized frontispiece, LuaLaTeX ran
> for forty minutes at full CPU and produced nothing. It had not crashed; it
> was emitting empty pages, one after another, forever. The house style now
> caps every image at 6.3 inches tall, and you should not raise that limit.

It is set in body text when it is part of the explanation, and as a Warning
when the reader is about to do the dangerous thing.

### 3.4 Admonitions

- There are two kinds, Note/Tip and Warning/Caution, each marked by an icon in
  the margin. In some books the icons were animals: "The owl icon indicates
  a tip, suggestion, or general note. The turkey icon indicates a warning or
  caution." Most books used generic TIP and WARNING icons with the same
  wording. Our homage: a **quill nib** for tips and a **broken type sort**
  (or an inverted "pi" sort) for warnings, drawn as small engravings.
- **Frequency:** at most one or two per section, three to eight per chapter.
- **Length:** one to four sentences. If it needs more, it is a sidebar or
  body text.
- **Tone:** imperative and specific. "Run `press check` before you commit;
  the CI build runs it anyway, and slower." Never "Note that..." inside a
  Note.

### 3.5 Sidebars

A sidebar is a ruled box (a thin rule all round, or a heavy rule top and
bottom), with a bold title, holding a self-contained aside of 150 to 400
words: history, a war story, or a comparison with a rival tool. Use about one
per chapter. Sidebars are not numbered.

### 3.6 Procedures

Introduce a procedure with an infinitive phrase and a colon, then give
numbered steps, each a single imperative, with the command on its own
display line:

> To install Press from source:
>
> 1. Unpack the distribution:
>    `$ tar xzf press-3.0.2.tar.gz`
> 2. Change into the new directory and install it:
>    `$ cd press-3.0.2`
>    `$ pip install .`
> 3. Verify the installation:
>    `$ press --version`

### 3.7 Captions and numbering

- **Examples:** the caption goes ABOVE the code: **Example 3-2. A minimal
  metadata.yaml**. Captions use sentence case or Title Case consistently,
  with no closing period.
- **Figures:** the caption goes BELOW the art: **Figure 3-2. The build
  pipeline**.
- **Tables:** the caption goes ABOVE the table: **Table 3-1. press check
  options**.
- Numbering is chapter-dash-sequence and restarts every chapter: 3-1, 3-2.
  Appendixes use letters (A-1). The Preface uses P-1 or none at all.
- Every numbered item is referenced in the text *before* it appears.
- **Table shape:** typically two or three columns, Option | Meaning or
  Parameter | Value | Description, with a header rule and no vertical rules.
  Cells hold sentences, not fragments, in the Meaning column.
- Code fragments of under about 6 lines may be informal (displayed without a
  caption). Anything longer, or anything referred to again, gets an Example
  number.

---

## 4. Code and Command Typography

| Convention | Meaning | Example |
|---|---|---|
| `constant width` | literal code, output, file contents, config keys | `verify-min-pages` |
| **`constant width bold`** | what the user types, in a session | `$ ` **`press check`** |
| *`constant width italic`* | replaceable text | `press art accept` *`file`* |
| `$` | normal user prompt (Bourne/bash) | |
| `%` | normal user prompt (csh/tcsh), common in the 1990s books | |
| `#` | root prompt | |
| `\` at line end | continuation of a long command | |
| `...` on its own line | output elided | |
| `[ ]` | optional | `press build [--draft]` |
| `\|` | choose one | `--paper white\|cream` |
| `...` after an item | may repeat | *`file ...`* |
| `{ }` | required choice group, in syntax lines | |

Rules:

- A session shows prompt and input in bold, then unbolded output:
  ```
  $ press check --strict
  checking chapters/01-arrival.md ... ok
  checking chapters/02-the-pool.md ... 2 warnings
  ...
  check: 0 errors, 7 warnings
  ```
  (In print, `press check --strict` is bold.) In Markdown, render the bold
  with the house filter; do not leave it to the reader.
- Pick one prompt for the book. Recommended: `$`, plus `#` only when root is
  genuinely required. Use `%` only if you want a 1996 flavor and will hold to
  it everywhere.
- Wrap code at 72 to 80 columns. Never let the page wrap code for you.
- Elide boring output with `...` rather than shrinking the type.
- Comments in examples are short and in the language's own comment syntax.
- Syntax lines (the synopsis form) go at the head of reference entries:
  ```
  press check [--strict] [--only chapter] [file ...]
  ```
  In print, `chapter` and `file` are italic.

---

## 5. Figures and Diagrams

### 5.1 The look

- **Black and white only.** Use gray fills (10%, 20%, 40%) for emphasis and
  no color anywhere in the interior.
- **Thin, uniform strokes**, about 0.5 pt for boxes and 0.75 pt for arrows.
  No hand-drawn wobble, no gradients, no 3-D bevels. A flat 2 pt offset drop
  shadow (solid black or 40% gray) on a box is permitted for the "important"
  node.
- **Labels in a small sans** (Helvetica or Frutiger style, 7 to 8 pt), with
  code names in a small monospace. Labels go inside boxes where possible.
  Callout lines are thin and straight, ending in a dot or a small arrowhead.
- **Arrowheads** are solid, small, and filled, and the same on every arrow.
- **Boxes**: square corners for data and files, rounded corners for
  processes and programs (or the reverse; pick one). A file is often a
  rectangle with a dog-eared corner. A disk or store is a cylinder.
- Generous white space; nothing touches the frame.
- **Screenshots:** grayscale, a thin 0.5 pt box around each, cropped tight
  to the relevant window, at actual size or reduced, never enlarged.
  Window chrome of the period (an X11 xterm, Netscape) is the ideal; for our
  book, a plain terminal window.

### 5.2 Archetypes (for the illustrator)

1. **Pipeline (left to right).** Rounded process boxes (`check`, `build`,
   `verify`) joined by arrows, with dog-eared file icons between them
   (*chapters/*.md*, *book.pdf*). The source files go at far left, the
   artifacts in a vertical stack at far right. Labels go under the file
   icons.
2. **Data-flow (top to bottom).** One input at the top fans out into three
   format branches (PDF, EPUB, HTML) and converges on a "verify" box. Arrows
   are labeled with the transforming tool in monospace (`pandoc`,
   `latexmk`).
3. **Directory tree.** A vertical trunk with horizontal stubs, folder icons
   (or plain names) in monospace, and annotations right-aligned in italic
   sans with a thin leader line ("your chapters go here"). It may be drawn
   as ASCII art inside an Example instead.
4. **Layered stack.** Horizontal bands stacked like a protocol stack: OS,
   Python, pandoc, TeX, press, and your book on top. Use alternating 10% and
   20% gray fills and centered labels.
5. **Client/CI topology.** An author workstation (a monitor icon), a
   repository (a cylinder), and a CI runner (a plain box with a small
   crate icon) joined by labeled arrows (`git push`, `pull
   image`).
6. **Before/after pair.** Two identical frames side by side labeled (a) and
   (b) under each, with one caption for both: a page with a widowed heading
   and the same page corrected. A single subtle arrow between them, or none.
7. **Annotated page anatomy.** A miniature book page in outline, with
   callouts naming the running head, folio, drop cap, block quote, and
   plate. Callout numbers in circles, keyed to a list in the caption or the
   text.
8. **State machine.** Circles for states, arcs for transitions labeled with
   the event; used for a release process (`tagged`, `proved`, `floated`,
   `published`). The start state has a filled dot.
9. **Filmstrip.** Three to five screenshots in a row (or a 2 x 2 grid),
   each boxed and numbered 1, 2, 3 under its frame, showing a sequence such
   as the setup wizard.
10. **Decision tree / flowchart.** Diamonds for questions ("Does
    *tex/title-page.tex* exist?"), rectangles for actions, and "Yes"/"No"
    labels on the arrows in small italic.
11. **Timeline.** A horizontal rule with tick marks and dated labels above
    and events below, for a history sidebar ("1984 TeX 1.0 ... 2006
    pandoc").

---

## 6. The Cover

### 6.1 Tradition and rationale

Edie Freedman found odd 19th-century animal engravings while looking for
cover images. She thought their quirkiness matched the strange-sounding
names of Unix tools (vi, sed, awk, uucp) and would appeal to programmers.
Some colleagues found them "weird, ugly, and a bit scary"; Tim O'Reilly
liked that they would stand out. The colophons consistently credit "a
19th-century engraving from the Dover Pictorial Archive", with cover type
"Adobe's ITC Garamond" laid out in QuarkXPress. The animal is chosen for a
loose, private resonance with the subject, never a literal pun. Freedman
notes that readers are quick to correct zoological errors, that some
readers avoid spiders and snakes, and that animals with readable faces sell.

### 6.2 Layout (homage spec)

Front cover, trimmed 7 x 9.19 in (the series trim; 7 x 9 is close enough):

- **White ground**, with the whole cover on white.
- **Top:** a solid, full-width **color band** about 1/8 of the cover height
  (the series color; e.g. a deep oxblood, or a slate teal), carrying a short
  reversed-out tagline or the series name at the right in small caps.
- **Title block** below the band, flush left, in large black condensed
  Garamond (horizontally scaled to about 80%, or use a true condensed cut).
  The subtitle sits under it in italic, smaller. The edition line ("Second
  Edition") goes top right or under the subtitle.
- **The engraving** sits center-to-lower right, about 45% of the cover
  height, unframed, black line on white. The animal faces into the cover
  (toward the spine side or the title), never off the edge.
- **Bottom right:** the authors' names, in Garamond, ragged right or flush
  right.
- **Bottom left:** the publisher's name and mark, small.
- Nothing else: no burst, no "Covers Python 3.12!" flash. In the 2000s an
  edition note sometimes appeared as a small line of italic. Allow one.

**Spine:** white, with the title in black condensed Garamond running top to
bottom, a small color block at the head matching the band, the author's
surname, and the publisher's mark at the foot. A tiny version of the animal
on the spine is permitted.

**Back cover:** white, with the band repeated at the top.

1. **A headline** in bold Garamond, one line, stating the book's promise
   ("The pipeline that turns a manuscript into a book").
2. **Two paragraphs** of plain description: the problem, then what the book
   does about it. No superlatives.
3. **A bulleted list** of 5 to 8 topics, introduced by "Topics include:" or
   "This book covers:".
4. **A pull quote** from a named reviewer or user, in italic, with attribution.
5. **An author biography**, two or three sentences, sometimes at the foot.
6. Category line at the top left ("Publishing/Unix"), a price, the ISBN and
   barcode at the bottom right, and the publisher's mark and Web address.

### 6.3 Candidate animals

1. **The common cuttlefish** (*Sepia officinalis*). It is an animal made of
   ink: sepia is named for it, and the whole subject is putting ink on
   paper. Victorian natural-history engravings of it are plentiful, and its
   W-shaped pupil gives it the readable face Freedman found that readers
   like. This is our first choice.
2. **The European hedgehog** (*Erinaceus europaeus*). Its spines look like
   type sorts standing in a case. It is small and methodical, has a friendly
   face, and stipple engraving suits it well.
3. **The Eurasian magpie** (*Pica pica*). Black and white like a printed
   page, it is a collector of small bright things, as a pipeline gathers
   chapters, fonts, and plates into one artifact. It is a striking engraving
   subject. The risk is its folk reputation as a thief, which a reviewer may
   take as a comment on the book.

Avoid the owl and the turkey, which were the admonition icons. Check the
publisher's animal list (oreilly.com/animals) for collisions before you
commit, so that the homage is not read as a copy of one particular title.

### 6.4 Title

| Title | Pros | Cons |
|---|---|---|
| *Press: The Definitive Guide* | The most recognizable pattern; it promises completeness. | It implies 700 pages and a reference section we must then deliver; "Press" alone is ambiguous on a spine. |
| *Managing Books with Press* | Echoes *Managing Projects with make*, the exact cousin of our subject; it says what the reader does. | "Managing" reads as sysadmin, not authoring. |
| *Press in a Nutshell* | Short; implies a desktop quick reference. | The Nutshell series implies a terse reference, not a narrative tutorial. "Nutshell" is a mark to avoid; use "in Brief" instead. |
| *Learning Press* | Signals a tutorial for newcomers. | Thin; it does not say what Press is. |
| *Publishing with Press* (recommended) | Period cadence ("Programming with Perl", "Managing Projects with make"); the subject is unambiguous; it allows tutorial and reference. | Less instantly iconic than "Definitive Guide". |

Recommended full form: ***Publishing with Press*** with the subtitle
*Building Books from Plain Text* on the second line.

---

## 7. Preface Boilerplate (original skeletons)

These are written fresh, in the period's cadence. Fill in the brackets.

### Who Should Read This Book

> This book is for anyone who has to turn a manuscript into a book and would
> rather not do it by hand twice. If you have written a long document in a
> text editor, kept it under version control, and then spent a weekend
> wrestling it into a PDF that a printer would accept, you are the reader we
> had in mind.
>
> We assume you are comfortable at a Unix shell prompt and can edit a text
> file without help. You do not need to know TeX, and you do not need to be a
> Python programmer, although Chapter 11 will make more sense if you are.
> System administrators who are asked to keep a build server running for a
> group of authors will find Part III written for them.

### Organization of This Book

> The book is divided into three parts. Part I teaches you to build a book;
> Part II explains how the pieces fit together; Part III is reference.
>
> **Chapter 1, *Getting Started***
> Installs Press, builds the sample book, and shows you where everything
> went.
>
> **Chapter 2, *The Shape of a Book Repository***
> Describes each file and directory a book contains, and which of them you
> are expected to edit.
>
> **Chapter 3, *Checking the Manuscript***
> Covers `press check`, the house rules it enforces, and how to add your own.
>
> **Appendix A, *Command Reference***
> Lists every command and option in manual-page form.

Each blurb is a single sentence fragment or one sentence beginning with a
verb ("Covers", "Describes", "Explains", "Shows"), or "This chapter...". The
chapter name is bold and the title italic.

### Conventions Used in This Book

> The following typographical conventions are used in this book:
>
> *Italic*
> : Used for filenames, directory names, URLs, and for new terms where
>   they are defined.
>
> `Constant width`
> : Used for commands, options, configuration keys, environment variables,
>   and the contents of files, and in examples to show the output of
>   commands.
>
> **`Constant width bold`**
> : Used in examples to show text that you type literally.
>
> *`Constant width italic`*
> : Used for text you should replace with a value of your own, such as
>   *`file`* in `press art accept` *`file`*.
>
> `$`
> : The shell prompt for an ordinary user. A `#` prompt means the command
>   must be run as root.
>
> [ ] and |
> : In syntax lines, square brackets enclose optional items, and a
>   vertical bar separates alternatives, of which you choose one.
>
> [quill icon]
> : This icon marks a tip, suggestion, or general note.
>
> [broken-sort icon]
> : This icon marks a warning or caution.

### Using Code Examples

> This book is here to help you get your books built. In general, you may use
> the code and configuration in this book in your own projects and
> documentation. You do not need to contact us for permission unless you are
> reproducing a significant portion of it; writing a build script that uses
> several fragments from this book does not require permission, but selling
> or redistributing a collection of examples from it does. We appreciate,
> but do not require, attribution. An attribution usually includes the title,
> author, publisher, and ISBN; for example: "*Publishing with Press*, by
> [Author]. Copyright 2002 [Holder], [ISBN]."

### How to Contact Us

> We have tested and verified the information in this book to the best of
> our ability, but you may find that features have changed, or even that we
> have made mistakes. Please let us know about any errors you find, as well
> as your suggestions for future editions, by writing to:
>
> Ferrule & Quire
> [street address]
> [city, state, postal code]
>
> You can also send us messages electronically. To be put on our mailing
> list, or to ask technical questions or comment on the book, send e-mail
> to: *[address]*
>
> We have a Web page for this book, where we list errata, examples, and
> plans for future editions. You can find it at: *[URL]*

(Do not use real addresses or phone numbers. If the book needs one, use the
555 exchange: 1-800-555-0100.)

### Acknowledgments

> A book about building books turns out to be mostly about the people who
> found the bugs. [Name] read every chapter in draft and returned them with
> more red ink than text. [Name] and [Name] ran Press on their own books long
> before it was ready, and their bug reports are the reason Chapter 9
> exists.
>
> Our technical reviewers, [Name], [Name], and [Name], caught errors that
> would have embarrassed us in print; any that remain are our own.
>
> At Ferrule & Quire, [Name] was the editor every author hopes for: patient
> about deadlines and impatient with vague sentences.
>
> **[Author 1]**
> I would like to thank ...

The period voice for acknowledgments: warm but brisk; family last; a joke
about coffee or the cat is permitted once.

---

## 8. Anti-Patterns and Era Touches

### 8.1 What breaks the illusion

- **Marketing voice:** "powerful", "seamless", "robust", "game-changing",
  "best-in-class", "leverage", "unlock", "supercharge", "journey".
- **Emoji, check-mark bullets, colored callouts**, or any color in the
  interior.
- **Meta-narration:** "In this section we will...", "Let's dive in",
  "Let's take a look", "As we've seen", "Without further ado". (Period books
  do say "we'll look at" occasionally in openers; keep it to the opener.)
  Do not open a sentence with "Let's", ever.
- **Bullet sprawl:** a page of bullets where paragraphs belong. These books
  argue in prose; lists hold genuinely parallel items: options, steps,
  files.
- **Hedging:** "you might want to consider possibly", "it's generally a good
  idea to". The house voice says "Do X" or "We recommend X, because Y".
- **Overlong admonitions** (more than four sentences), stacked admonitions,
  and admonitions that repeat the paragraph above them.
- **Inconsistent numbering**, captions on the wrong side, figures not
  referenced in the text, and examples referred to as "the code below".
- **Modern idiom:** "spin up", "out of the box" as an adjective, "ship it",
  "DX", "footgun", "TL;DR", "deep dive", "under the hood" more than once a
  book, "folks".
- **Anachronistic UI** in screenshots: dark-mode terminals, rounded
  macOS-style windows with traffic lights, emoji in prompts, powerline
  glyphs. Use a plain light terminal, a monospace font, and a `$` prompt.
- **Epigrams** at the end of sections, and chapter-ending pep talks.
- **Inline Markdown-isms visible in print**: backtick characters, `**`, and
  "Note:" in bold at the start of a paragraph instead of the icon.

### 8.2 Era-appropriate touches

- Spellings: **Unix** (or UNIX in the earliest books; pick one; we
  recommend "Unix"), **e-mail**, **Web site**, **Web page**, the **Web**,
  the **Net**, **online**, **filename** (one word), **manpage** or **manual
  page**, **appendixes**, **toward**, **setup** (noun) / **set up** (verb).
- "the Python community", "the TeX community", "comp.text.tex" as a place
  where people ask questions; "a mailing list archive".
- Man-page references with sections: make(1), latexmk(1), crontab(5).
- "Print out the manual and keep it by the terminal" style asides, used
  sparingly. A reference card "to photocopy and pin above your desk".
- "At the time of this writing" before any version claim. Version numbers
  stated exactly ("pandoc 3.1.11").
- References to FTP sites and CD-ROMs only where apt. A "the examples are
  available for download from the book's Web site" line is right; a bundled
  CD-ROM is not.
- Footnotes for asides and history, numbered per chapter, used two to six
  times a chapter. A footnote is a natural place for the dry joke.
- Hostnames and user names from a fixed cast (`alice`, `hatter`, a host
  called `printshop`).
- Bibliographic references in a short "For More Information" A-head or a
  Bibliography appendix that cites Knuth's *The TeXbook* and Bringhurst's
  *The Elements of Typographic Style* by title and publisher.

---

## 9. Calibration Sample

What follows is how a mid-chapter page should read. Bold in sessions is shown
with `**` here; in the book it is set by the house filter.

---

### Running the Checker

Before Press will build anything, it reads every chapter and compares it
against the house rules. The program that does this is `press check`, and in
most books it runs more often than any other command. It is fast, because
it never invokes TeX, and it is strict, because a mistake caught at this
stage costs a few seconds instead of a forty-minute build that fails on
page 212.

You can run the checker by itself at any time. From the top of your book's
repository, type:

**Example 6-1. A first run of the checker**

```
$ **press check**
reading config/house-rules.yaml ... 14 rules
checking chapters/01-down-the-rabbit-hole.md ... ok
checking chapters/02-the-pool-of-tears.md ... 1 error
  02-the-pool-of-tears.md:41: banned pattern "very unique" (redundancy)
...
check: 1 error, 0 warnings in 12 files
```

The output shows each file as it is read, followed by the problems found in
it. Each problem gives the filename, the line number, and the rule that
caught it, in the same form a compiler uses, so that Emacs and vi can jump
straight to the offending line.[^1] The final line is a summary. If the
error count is anything but zero, `press check` exits with a nonzero status,
and any build that depends on it stops there. That is deliberate: the
build targets described in Chapter 7, *Building the Formats*, all run the
checker first, so you cannot produce a PDF from a manuscript that has
failed it.

The checker's behavior can be adjusted with the options in Table 6-1.

**Table 6-1. press check options**

| Option | Meaning |
|---|---|
| `--strict` | Treat warnings as errors. This is what the CI build uses. |
| `--only` *`chapter`* | Check one chapter instead of the whole book. |
| `--rules` *`file`* | Read house rules from *`file`* instead of *config/house-rules.yaml*. |
| `--quiet` | Print only the problems and the summary line. |

> **[quill icon]** Run `press check --strict` before you commit. The CI build
> runs the same command, and it is much faster to find out at your desk than
> from an e-mail an hour later.

Figure 6-1 shows where the checker sits in the larger pipeline. Notice that
it reads only your source files; it never looks at *dist/*, which is why a
clean check says nothing about whether last week's PDF is current.

*[art: pipeline archetype. Left: dog-eared file icons labeled chapters/*.md
and config/. Center: a rounded, drop-shadowed box labeled press check. An
arrow labeled "pass" runs right to three boxes, build pdf, build epub, build
site; an arrow labeled "fail" drops down to a small box labeled "stop
(exit 1)".]*

**Figure 6-1. The checker guards every build target**

Most of the rules come from two places. The universal rules ship with Press
and catch the mistakes nearly every book makes: doubled words, straight
quotes where curly ones belong, a chapter heading at the wrong level. The
book's own rules live in *config/house-rules.yaml*, and they are the subject
of the next section.

[^1]: The format is older than either editor. It comes from the C compilers
of the 1970s, and nobody has yet found a reason to change it.

---

*End of guide.*
