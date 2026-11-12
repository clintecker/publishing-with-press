# The house design

::: {.in-this-chapter}
> **In this chapter:**
>
> - The page in numbers
> - Type
> - Running heads and folios
> - Six profiles
> - The reader site
> - The landing page
> - The aesthetic file
> - Extra CSS and the reader sheet
> - Why a design change is a new major
:::

Every book that press builds wears the same design unless its author asks for another one. The press calls that design *the house*: the page, the type, the running heads, and the Web sheets that come with the package. This chapter gives the house in numbers, shows what the six *design profiles* (sealed page geometries) change, and follows the design onto the reader site and the landing page. It then shows how a book changes its own appearance, and it ends with the reason a design change waits for a new major version.

## The page in numbers

Open the reading PDF of the Alice book, the Print edition, and you see a page 6 inches wide and 9 inches tall. The text block inside it is about 4.54 by 7.5 inches. That page belongs to the default profile, `house-6x9`, and the numbers in this section are its numbers. The section "Six profiles" later in this chapter gives the other five.

@fig:page-geometry draws the house page to scale, with a dimension line for each measurement in Table 9.1.

![The house 6 by 9 page drawn to scale](assets/woodcuts/09-01-page-geometry.png){#fig:page-geometry .diagram width=half-measure fig-alt="A 6 by 9 inch page in outline around a gray text block. Dimension lines give the four margins, the 4.54 by 7.5 inch block, the gaps to the running head and page number, and the 6.3 inch height cap."}

<!-- art: ARCHETYPE page anatomy, portrait, to scale, drawn narrow for a half-measure figure. A 6 by 9 page outline. Inside, a 10% gray text block with dimension lines to the edges: left "inner 0.78in", right "outer 0.68in", top "head 0.72in", bottom "foot 0.78in". Above the block a line of small type (the running head), dimension "headsep 0.20in". Below it a centered page number, dimension "footskip 0.38in" from the last baseline to the page number's baseline. Outside: "6in" across the top, "9in" down the right. Inside the block: "4.54in" across, "7.5in" down. Left of the block, a dashed bracket "height cap 6.3in" from its top. The reader sees first the gray block. -->

Table 9.1 gives every measurement the house TeX header sets on that page. The inner margin and the bottom margin are the widest, at 0.78 inches each.

| Setting | Value | Meaning |
|-------------------|-------------|-----------------------------------------------------------|
| Trim | 6in by 9in | It is the size of the finished page. |
| Inner margin | 0.78in | It is the margin at the binding side of the page. |
| Outer margin | 0.68in | It is the margin at the open edge of the page. |
| Top margin | 0.72in | It runs from the top of the page to the top of the text block. |
| Bottom margin | 0.78in | It runs from the foot of the text block to the foot of the page. |
| `headsep` | 0.20in | It is the gap between the running head and the text block. |
| `footskip` | 0.38in | It runs from the baseline of the last line of text to the baseline of the page number. |
| Text block | about 4.54in by 7.5in | It is what remains when the four margins come off the trim. |
| Height cap | 6.3in | No image on the house page prints taller than this. |

Table: Table 9.1. The house 6 by 9 page

The last row is the height cap from Chapter 5, *Figures, plates, and illustrations*, and each profile sets its own value with the key `figure-cap`. Every figure prints where the manuscript puts it, because the header places figures with the option `[H]`.

### The print interior

The print pack changes the house page twice. Its interior is two-sided: left and right pages mirror each other, as in a bound book. The reading PDF is one-sided, and every page has the same layout. The header loads the KOMA-Script class `scrbook` with `oneside`, `openany`, and `headings=small` for the reading PDF, and with `twoside`, `open=any`, and `headings=small` for print.

The second change is in the margins. A second header, *print-header.tex*, resets the side margins of the house page to 0.88 inches inner and 0.58 inches outer. The total is the same 1.46 inches, so the text block keeps its width. The extra space moves toward the gutter. Chapter 12, *The print pack*, describes the rest of the print interior.

::: {.sidebar}
> **The KOMA spelling trap**
>
> LaTeX has two spellings for the same wish. The standard classes write `openany` for "a chapter may start on any page", and KOMA-Script writes `open=any`. The house reading PDF is one-sided, and its header loads the class with `openany`. The print interior is two-sided, and there the short spelling fails without a word.
>
> The comment in the press's print defaults states the cost exactly: "the standard-class spelling openany is silently ignored under twoside". The other obvious choice is worse. With `open=right`, the press would "ship genuinely blank versos", a white left-hand page before every chapter that would otherwise start on one. The first mistake is silent, and the second costs paper. The print defaults therefore spell the option the KOMA way, and the comment beside it gives the reason.
:::

## Type

The house sets its body text in Libertinus at 10 points. Table 9.2 lists the settings.

| Setting | Value | Meaning |
|-------------------|------------------------|---------------------------------------------------|
| Body face | Libertinus | The header loads it with `\usepackage{libertinus}` unless the book names another face. |
| Body size | 10pt | Every profile keeps this size. |
| Leading | `\linespread{1.045}` | It opens the lines slightly beyond the face's own spacing. |
| Indent | 1.1em | The first line of a paragraph moves in by this much. |
| Paragraph space | 0pt | No extra space separates two paragraphs. |
| Monospace | Source Code Pro, scaled 0.86 | It sets code, commands, and file contents. |

Table: Table 9.2. The house type

A book can choose another body face in its *aesthetic*, the visual identity in *config/aesthetic.yaml*, through the key `typography.pdf-family`. When that key is empty, the header uses the packaged Libertinus. When it names a family, the header writes `\setmainfont{<family>}[Numbers=OldStyle]` instead, so the chosen face sets its numerals in the old style, with descenders like lowercase letters.[^9-libertine]

[^9-libertine]: The face has its own scar. Ubuntu has no `fonts-libertinus` package, and an install with `--no-install-recommends` drops the Libertine keyboard face. The toolchain image therefore names `fonts-linuxlibertine` explicitly. Chapter 2, *Installing press*, lists the packages.

### Line breaking

Version 3.0.0 of press added rules for how the lines break. The `microtype` package runs with `protrusion=true,expansion=true,final=true`. Protrusion lets punctuation hang slightly past the margin, so the edge of the text looks straight to the eye. Expansion lets the face widen or narrow a little on a line, which gives the paragraph builder more ways to avoid a loose line. The `selnolig` package stops a ligature across the seam of a compound word, so "shelfful" keeps its two letters f apart at `shelf|ful`.

The header also sets six values to 10000. They are `\clubpenalty`, `\widowpenalty`, `\displaywidowpenalty`, `\brokenpenalty`, `\finalhyphendemerits`, and `\doublehyphendemerits`. For the four penalties, 10000 is the value TeX treats as infinite. A paragraph therefore never leaves its first line alone at the foot of a page or its last line alone at the head of the next. No page ends on a hyphenated line. The two demerits make TeX avoid a hyphen at the end of the next-to-last line and hyphens on two lines in a row.

Four more values control the shape of the paragraph. The value `\parfillskip=0pt plus 0.8\hsize` makes the last line of a paragraph fill at least a fifth of the line. No paragraph then ends on a *runt*, a last line of one short word. Hyphenation needs three letters on each side of a break, through `\lefthyphenmin=3` and `\righthyphenmin=3`. The value `\hyphenpenalty=150` raises the cost of every hyphen.

### Headings and captions

The header sets every heading in bold, in the ink color, and ragged on the right. A chapter title has 1.25 lines of space after it. A section heading has 1.6 lines before it and 0.55 after it, and a subsection heading has 1.2 before and 0.35 after. Each heading also reserves room for the text that follows it: five lines for a section and four for a subsection. A heading therefore never sits alone at the foot of a page.

The contents page goes one level deep: it lists the chapters. The plates and the figures have separate lists, the List of Plates and the List of Figures. A scar lives here. The setting `toc-depth: 1` sets the TeX counter `tocdepth` to 0, and that silently empties the List of Plates. The header now raises the depth inside the plates list itself, so a shallow contents page and a full List of Plates live together.

One package sets every caption. The header gives the `caption` package the options `font={small,it}`, `labelformat=empty`, `justification=centering`, and `hypcap=true`. Captions are therefore small, italic, and centered. The last option sends a link in the List of Plates to the top of the plate instead of to its caption.[^9-hypcap]

[^9-hypcap]: Earlier versions of press loaded a separate `hypcap` package for this. The `caption` package now does the work alone, and it is the single authority over captions in the house header.

### Color and links

The house PDF names six colors, and the aesthetic can override four of them through `book-colors`. Table 9.3 lists the defaults. The interior is single ink in every profile except `house-6x9-color`. That rule is a *craft law*, a law of the house that no configuration can change, and Chapter 11, *The art department*, names the others.

| Name | Value | Meaning |
|-------------|-------------|--------------------------------------------------------|
| `ink` | `#171717` | The headings take this color. `book-colors.ink` overrides it. |
| `muted` | `#5C5C5C` | It sets the book title in the running head. `book-colors.muted` overrides it. |
| `rulegray` | `#C8C8C8` | The header defines it, and no setting in the aesthetic touches it. |
| `papergray` | `#F4F4F1` | It fills the box behind a blockquote. |
| `accent` | `#4B3E8A` | It is defined by the header and used nowhere. `book-colors.accent` overrides it. |
| `linkgreen` | `#46621F` | It colors a URL in the reading PDF. `book-colors.link` overrides it. |

Table: Table 9.3. The house PDF colors

Links are live, with `colorlinks: true`. An internal link stays black through `linkcolor: black`, and a URL takes `linkgreen` in the reading PDF and black in print. A book with no front matter still gets a plain fallback title page. Chapter 10, *Front matter, the index, and the table of authorities*, describes the generated front matter that usually takes its place.

### Chapter openings

No shipped profile sets a drop cap. A book asks for one, as Chapter 4, *Writing the manuscript*, shows. In the PDF the `drop-cap` style becomes a call to the LaTeX package `lettrine`, wrapped in the house macro `\PressDropCap`. The drop cap is three lines deep, with `findent=2pt` between the letter and the text. The rest of the first word follows in small caps, and the macro reserves four lines first, so the drop cap never starts at the foot of a page.

A chapter that opens with speech puts a quotation mark before the drop cap. Since version 3.0.0 the house sets that mark at body size and hangs it into the left margin. The drop cap keeps its place at the left edge of the text. This is Bringhurst's rule for hanging punctuation. On the reader site the same mark takes a margin of minus 0.52 em.

## Running heads and folios

The house header sets the head and the foot of each page with three KOMA-Script commands. The command `\ihead` puts the book title in the inner head, in italic, at footnote size, in the `muted` color. The command `\ohead` puts the chapter title in the outer head. The command `\cfoot` puts the page number, the *folio*, in the center of the foot. The folio appears on plain pages too, so a chapter's opening page carries its number.

In a one-sided document, KOMA-Script puts the inner head at the left. A page of the reading PDF therefore carries the book title at its top left and the chapter title at its top right. The header takes the chapter title from the chapter heading, and the manuscript holds no markup for any of this.

The print interior is two-sided, so its inner and outer heads change sides from page to page. The book title sits next to the binding on both pages of a spread, and the chapter title sits at the open edge.

::: {.tip}
> **Tip:** Keep chapter titles short enough to fit the outer head. A long title in the manuscript becomes a long running head on every page of the chapter.
:::

## Six profiles

A design profile fixes a trim, four margins, a height cap, an indent and leading, and a column width for the Web. At the time of this writing, press 3.0.2 has six of them. A book chooses one with the field `print.profile` in *config/metadata.yaml*, and the default is `house-6x9`. The documentation divides the labor in one sentence: "choosing a profile changes the design's proportions; choosing an aesthetic changes its voice." The font family and the palette belong to the aesthetic, and everything that depends on the size of the page belongs to the profile.

To move the Alice book to the novella page, user `alice` runs one command on `hatter`:

```text
$ press config set print.profile novella-5x8
...
```

The command checks the value, writes it, and prints a diff of the change, as Chapter 3, *The shape of a book repository*, shows. The trim follows the profile. You never set it directly, and Chapter 3 gives the message press prints if you try.

@fig:profiles-compared sets the six side by side. The intended uses come from the profile descriptions in the press's fact base, which Table 12.2 in Chapter 12 also gives. The house text width is stated, and the other four are derived from Table 9.4: the trim width less the inner and outer margins. The figure leaves out the body size, because it is 10 points in every profile.

![The six design profiles compared](assets/woodcuts/09-02-profiles-compared.png){#fig:profiles-compared .diagram width=full-measure fig-alt="A grid with six profiles down the side and four columns across: trim, text width, height cap, and intended use. Every cell is filled, and the height cap falls and rises with the trim."}

<!-- art: ARCHETYPE matrix. Six rows, four columns, thin rules, no fills except a 10% gray header row. Column heads in small sans: "trim", "text width", "height cap", "intended use". Row heads in small monospace, top to bottom, with values left to right. house-6x9: "6 x 9", "4.54in", "6.3in", "default". house-6x9-color: "6 x 9", "4.54in", "6.3in", "color interior". novella-5x8: "5 x 8", "3.75in*", "5.6in", "novella". digest-5.5x8.5: "5.5 x 8.5", "4.14in*", "6.0in", "genre trade paperback". large-print-7x10: "7 x 10", "5.35in*", "7.2in", "large print". mass-market-4.25x6.87: "4.25 x 6.87", "3.17in*", "4.8in", "rack-size paperback". Under the grid, small italic: "* derived: trim width less inner and outer margins". The reader sees first the height cap column. -->

Table 9.4 gives the rest of each profile: its margins, its indent and leading, and the width of its *paper column*, the framed column that holds the text on the reader site. The margins run inner, outer, top, and bottom, in inches.

| Profile | Margins | Indent, leading, and column width |
|--------------------------|-------------------------|------------------------------------------------|
| `house-6x9` | 0.78, 0.68, 0.72, 0.78 | The indent is 1.1em at a leading of 1.045. The column is 48rem wide, with 1.25rem type on a 1.62 line. |
| `house-6x9-color` | 0.78, 0.68, 0.72, 0.78 | Every value matches `house-6x9`. |
| `novella-5x8` | 0.70, 0.55, 0.62, 0.68 | The indent is 1.0em at a leading of 1.08. The column is 40rem wide, with 1.2rem type on a 1.66 line. |
| `digest-5.5x8.5` | 0.74, 0.62, 0.66, 0.72 | The indent is 1.05em at a leading of 1.06. The column is 44rem wide, with 1.2rem type on a 1.64 line. |
| `large-print-7x10` | 0.90, 0.75, 0.85, 0.95 | The indent is 1.1em at a leading of 1.2. The column is 54rem wide, with 1.4rem type on a 1.8 line. |
| `mass-market-4.25x6.87` | 0.62, 0.46, 0.56, 0.62 | The indent is 0.9em at a leading of 1.02. The column is 34rem wide, with 1.15rem type on a 1.6 line. |

Table: Table 9.4. Margins and column widths by profile

The PDF body stays at 10 points in every profile, and the indent and the leading change with the page. The large-print profile earns its name through its page and its spacing. It has a 7 by 10 trim, the widest margins, the tallest height cap, and a leading of 1.2, and on the Web it sets 1.4 rem type. The mass-market profile is the smallest page, with the tightest margins and the narrowest paper column.

The color profile is the one exception to the single-ink law. A book that needs color plates or figures inside chooses `house-6x9-color`. It accepts a cost, and Chapter 12 explains why some providers refuse a color interior.

The list has a limit, which *NON-GOALS.md* states: "Press is a prose engine." Another trim, a color interior, or large print is a new profile and core press work. A fixed-layout picture book or a magazine is a new engine, and press does not take it on.

::: {.tip}
> **Tip:** Choose the profile before you commission art. The height cap and the text width set the largest size a plate can print at, and a plate drawn for one page may look cramped on a smaller one.
:::

## The reader site

In a browser, a reader opens the Chapter edition, the reader site: one chapter to a page, with links between them. Press builds it into *dist/site* from the house files in its own package data. One stylesheet, *reader.css*, sets its appearance, and one template, *chunked-template.html*, sets its structure. To look at a change, run `press site` and open *dist/site/index.html* in your browser.

The sheet works from named colors, which CSS calls custom properties and the press calls *tokens*. Table 9.5 gives each token's values and what it paints. A token marked "dark unchanged" keeps its light value in the dark theme.

| Token | Light and dark | Meaning |
|-----------------|-----------------------|------------------------------------------------------|
| `--cloth` | `#5a7d2a`, `#141a0e` | It paints the green book cloth behind the paper column. |
| `--cloth-deep` | `#46621f`, dark unchanged | It is the source of `--link`. |
| `--link` | `var(--cloth-deep)`, dark `var(--foil-bright)` | It colors the links. |
| `--foil` | `#b8963f`, dark unchanged | It paints the border of the paper column and of each figure mat, and it is the light-theme source of `--hairline`. |
| `--hairline` | `var(--foil)`, dark `var(--foil-deep)` | It underlines the links and borders the table cards. |
| `--foil-bright` | `#c9a961`, dark unchanged | It colors the links in the dark theme. |
| `--foil-deep` | `#8f7226`, dark unchanged | It is the light-theme source of `--ornament` and the dark-theme source of `--hairline`. |
| `--ornament` | `var(--foil-deep)`, dark `var(--foil)` | It colors the ornaments: the diamond rules, the scene breaks, the list markers, and the ornate drop cap. |
| `--paper` | `#f4efe3`, `#1d1b15` | It paints the paper column. |
| `--paper-warm` | `#ece5d3`, `#26231b` | It paints the mat behind each figure. |
| `--ink` | `#23201a`, `#e8e0cc` | It colors the text. |
| `--ink-soft` | `#4d463a`, `#b5ab93` | It is the softer of the two inks. |

Table: Table 9.5. The reader sheet's tokens

The page background is green book cloth, and the paper column sits in the middle of it with a foil border and a shadow. On a narrow screen the frame drops away, and the paper column stands alone. The body face is a stack of book faces, from Iowan Old Style down to Georgia. In the dark theme the sheet swaps in the dark values and dims every image to 87 percent of its brightness.

An `h1` sits in the center, with a small-caps line "Chapter N" and a diamond rule. A scene break becomes a small diamond ornament between two fading hairlines. On a narrow screen each table becomes a stack of cards.

### The chapter page

@fig:reader-site shows a chapter page from the press's own three-chapter Alice example as a reader sees it. Each chapter page opens with a masthead that carries the book title. Below it sits a contents drawer, built from the HTML `<details>` element. The drawer starts closed, and when the reader opens it, it lists the chapters with the current one expanded.

![A chapter page of the three-chapter example on the reader site](assets/woodcuts/09-03-reader-site.png){#fig:reader-site .photo width=full-measure fig-alt="A browser window shows a paper column on a cloth background. The column holds a masthead, a closed contents drawer, and a centered chapter heading over a diamond rule. Below them are a paragraph with a drop cap, a framed plate, and links to the previous and next chapters."}

<!-- art: ARCHETYPE screenshot. Capture from a real reader-site build of the three-chapter example, light theme, desktop width (wide enough that the cloth frame shows), with the drop-cap chapter opening set. Page: a chapter that opens with a plate. Crop tight to the browser content area, no browser chrome, grayscale, 0.5pt box. Visible top to bottom: the cloth background at both sides; the masthead with the book title; the contents drawer in its starting state, closed; the small-caps "Chapter N" line, the centered chapter heading, and the diamond rule; the first paragraph with its drop cap and small-caps first line; one plate on its mat with a foil border and caption; the previous and next pager cards at the foot. The reader sees first the paper column on its cloth. -->

The page works from the keyboard. The left and right arrow keys turn the pages. The page ignores them when a modifier key is down or the cursor sits in a form field. Access keys reach the masthead (`u`), the previous page (`p`), and the next page (`n`), and the template also gives a "Skip to chapter" link.

The index page of the reader site holds the title block and the cover, if the book has one. Below them are a lede that begins "This is the reading edition" and a "Start reading" button with the access key `s`.

### Metadata in the head

Each page carries the metadata that search engines and social sites read: a canonical link, Open Graph fields, a Twitter card of the type `summary_large_image`, and a JSON-LD block. In JSON-LD a chapter page is an `Article` that `isPartOf` the book, with a `BreadcrumbList`. The landing page is a `Book`, with a `workExample` entry for each edition the book offers.

The description of a chapter page comes from the chapter itself. Press takes the first paragraph of at least 20 characters and cuts it to 157 characters plus three periods.

All of this depends on the field `site-url`. The rule is short: "when there is no public base URL, nothing URL-shaped is emitted." A book without it gets no canonical link, no `og:url` or `og:image`, and no sitemap.

::: {.tip}
> **Tip:** Set `site-url` in *config/metadata.yaml* before you publish the reader site. Without it the pages still read correctly, but search engines and social sites get no address to show.
:::

### The other sheets

The Single-leaf edition, the self-contained HTML, uses *book.css*. That sheet takes the same ink, muted, and accent values as the PDF, and it sets the text on a near-white paper. Its face is Charter, then Bitstream Charter, then Georgia, at 19 pixels on a 1.58 line, in a column at most 42 rem wide. It has no dark theme.

The Circulating edition, the EPUB, uses *epub.css*. That sheet sets a serif face on a 1.45 line, a drop cap at 3 em, and a rule that keeps a figure inside the screen. It sets no colors at all, and the press gives the reason in five words: "the reader owns the theme."

## The landing page

On the Web, the front door of the book is the landing page, *dist/pages/index.html*. It shares the tokens of the reader sheet, but it sets a narrower paper column, at most 44 rem wide, and it has no dark theme. The template is *index-template.html*, and it lays the page out in four parts.

The first part is a "Read the Book" invitation that leads to the reader site, with the line "one chapter to a page, as is proper". The second part is a "Table of Editions" that lists every edition the book offers. The third part is "How This Book Was Built". A footer closes the page with the line "Printed on paper, electrons, or both."

The table of editions names each artifact in the manner of an old publisher's catalog. Its first row is always the "Chapter edition", which links to *read/index.html*, the reader site. Table 9.6 gives the label for each of the other files, by the end of its filename.

| File ends with | Label | Meaning |
|-----------------|-------------------------------|--------------------------------------------|
| `.pdf` | Print edition | It is the reading PDF. |
| `.epub` | Circulating edition | It is the EPUB. |
| `.html` | Single-leaf edition | It is the whole book as one HTML file. |
| `.md` | Manuscript edition | It is the stitched Markdown. |
| `.txt` | Telegraphic edition | It is the plain text. |
| `.docx` | Office edition | It is the DOCX file. |
| `-site.zip` | Chapter edition, boxed | It is the reader site in one archive. |
| `-source.zip` | Source edition | It is the archive of the book repository. |
| `-sources.md` | Table of authorities | It is the sources companion. |

Table: Table 9.6. Edition labels on the landing page

The PDF row adds a description: the edition is "typeset by LuaLaTeX, suitable for paper."

A subtitle in the old style joins its clauses with "or". The landing page sets each clause that begins "or," on a line of its own, as a Victorian title page would.

## The aesthetic file

A book keeps its visual identity in *config/aesthetic.yaml*, and press merges that file over the house aesthetic. The file holds the art direction for the cover, the plates, the logomark, and the portrait, which Chapter 11 describes. It also holds the few design values that a book can change. Table 9.7 lists the keys that touch the design.

| Key | Meaning |
|--------------------------|---------------------------------------------------------------|
| `web-palette` | It replaces tokens in the reader sheet's light theme. |
| `web-palette-dark` | It replaces tokens in the dark theme, after the dark-mode seam in the sheet. |
| `typography.web-family` | It names the font stack for the reader site. |
| `typography.pdf-family` | It names the body face for the PDF. If it is empty, the header uses Libertinus. |
| `book-colors` | It overrides `ink`, `muted`, `accent`, and `link` in the PDF, as hex values without a `#`. |
| `scene-break` | It chooses the ornament for a scene break: `rule` (the default), `asterism`, or `fairy-dust`. |
| `cover.style` | It chooses a cover style for the art commissions. |
| `plates.style` | It chooses a style for the plates. |

Table: Table 9.7. The aesthetic keys that touch the design

The tokens a palette can name are `paper`, `paper-warm`, `ink`, `ink-soft`, `cloth`, `cloth-deep`, `foil`, `foil-bright`, `foil-deep`, `hairline`, `link`, and `ornament`. Press rewrites the light palette into the sheet before the dark-mode seam and the dark palette after it, so the two themes stay separate.

Suppose `alice` wants a red cloth in the manner of a Victorian gift book. She writes the file in Example 9.1. It keeps the house foil, paper, and ink tones, and it changes the two cloth tokens. In the PDF it sets the links to the deep cloth red and restates the accent in the cloth red, though the header uses the accent nowhere, and it asks for the fairy-dust scene break.

**Example 9.1. An aesthetic file for the Alice book**

```text
web-palette:
  cloth: '#7b2d26'
  cloth-deep: '#5c1f1a'
  foil: '#b8963f'
  foil-bright: '#c9a961'
  foil-deep: '#8f7226'
  paper: '#f4efe3'
  paper-warm: '#ece5d3'
  ink: '#23201a'
  ink-soft: '#4d463a'
web-palette-dark:
  cloth: '#1c0b0b'
  paper: '#1d1b15'
  paper-warm: '#26231b'
  ink: '#e8e0cc'
  ink-soft: '#b5ab93'
book-colors:
  ink: '171717'
  muted: 5C5C5C
  accent: 7B2D26
  link: 5C1F1A
scene-break: fairy-dust
```

The dark palette names five tokens because the house dark palette names those five. Its only change is a darker red cloth. In the light theme, the links on the reader site follow the new deep cloth, because the sheet's `--link` takes its value from `--cloth-deep`.

A Web palette value is a CSS color, so it keeps its `#`. A `book-colors` value goes into TeX, so it is six hex digits with no `#`. Press writes each one as a `\definecolor` line in *build/aesthetic.tex*, and the `link` value becomes the house color `linkgreen`. In Example 9.1 the URLs in the reading PDF therefore print in the deep red, under the name of a green.

::: {.warning}
> **Warning:** Do not put a `#` before a `book-colors` value. Those values go into TeX, which wants the six hex digits alone.
:::

The merge works at the top level, and that surprises authors once. When the book's file names a section, such as `web-palette` or `book-colors`, the whole section replaces the house section of the same name. Nothing from the house section survives inside it. The house documentation gives the rule in eight words: "restate a whole section when you touch it." Example 9.1 follows it. It writes nine tokens of the light palette and all four book colors, including the values it keeps.

::: {.tip}
> **Tip:** When you change one field of an aesthetic section, copy the whole section into your file first and edit the copy. The merge replaces the section as a whole.
:::

To see the merged result, run `press aesthetic` with no argument. It prints a comment line that names the source, then the effective aesthetic as YAML. Example 9.2 shows the design part of that output in a fresh book with no aesthetic file. Those are the house values that Example 9.1 restates.

**Example 9.2. press aesthetic in a fresh book (excerpt)**

```text
$ press aesthetic
...
web-palette:
  cloth: '#5a7d2a'
  cloth-deep: '#46621f'
  foil: '#b8963f'
  foil-bright: '#c9a961'
  foil-deep: '#8f7226'
  paper: '#f4efe3'
  paper-warm: '#ece5d3'
  ink: '#23201a'
  ink-soft: '#4d463a'
web-palette-dark:
  cloth: '#141a0e'
  paper: '#1d1b15'
  paper-warm: '#26231b'
  ink: '#e8e0cc'
  ink-soft: '#b5ab93'
...
book-colors:
  ink: '171717'
  muted: 5C5C5C
  accent: 4B3E8A
  link: 46621F
```

## Extra CSS and the reader sheet

The aesthetic changes colors and a font stack. For anything more, a book supplies CSS of its own, as an addition or as a replacement.

The file *assets/web/extra.css* is the addition. Press appends it to the end of the house reader sheet, after a comment line that reads `/* assets/web/extra.css */`. Because it comes last, its rules win the cascade over any house rule of the same weight. Press also injects it into the landing page as a `<style>` element, so one file adjusts both.

The chapbook example that comes with press uses *extra.css* in the plainest way. It is a book of verse. Its *extra.css* sets a line height of 1.85 for room between the lines, and it narrows the paper column with this rule:

```text
.reader main {max-width: 30rem}
```

The file *assets/web/reader.css* is the replacement. If it exists, press uses it instead of the house reader sheet, entirely. The aesthetic palette still applies to either sheet. A book that supplies neither file gets the house sheet, and the press promises that such a book "renders byte-identically to before".

We suggest you start with *extra.css* and stay with it as long as you can. An appended file keeps every fix the house sheet gets in later releases, and a replacement sheet keeps none of them.

::: {.warning}
> **Warning:** If you supply *assets/web/reader.css*, set the width of the paper column in it yourself. Press does not add the profile's column width to a replacement sheet.
:::

## Why a design change is a new major

Press makes a promise about design, and *ARCHITECTURE.md* states it:

> Within a major version, a fix may correct broken output ... but must not change the typography or layout of a book that was already valid. A book that rebuilt cleanly yesterday must produce the same design today.

The press repository states the same rule from the other side: "design and template changes require a new major." The promise follows from how books use press. A book pins a release tag, as Chapter 14, *Continuous integration and the release contract*, describes. A *floating tag* such as `v3` moves to each new compatible release, and an *immutable tag* such as `v3.0.2` never moves. An author on the floating tag takes every fix in the major without reading the release notes. If a fix moved a line break, that author would find a different book after a routine rebuild.

A change of design moves more than one line. A different hyphenation penalty breaks a paragraph in a new place, and the paragraph may then gain or lose a line. One extra line can push a heading to the next page. Across a whole book the page count changes, and the page count sets the width of the spine on the cover wrap (Chapter 12 shows the arithmetic). An author proofs those exact pages.

### Version 3.0.0 as an example

The changes in 3.0.0, a design major, show what the rule covers. That release added the line-breaking rules from the section "Type" earlier in this chapter, and it hung the quotation mark of a chapter that opens with speech into the margin. A book that was valid under version 2 rebuilds under version 3 with different line breaks, and some of its pages change.

None of those changes corrects broken output. A widow is legal TeX, and a page that begins with one is a valid page. The changes make the book better and also different, so they waited for a new major. A book pinned to `v2` kept its old pages until its author chose to move.

The move itself left one more scar. The `press migrate` command once told an author moving from version 2 to version 3 that the geometry would stay byte for byte the same. That promise held for the move from version 1 to version 2, and it did not hold for this one. Release 3.0.1 corrected the message.[^9-migrate]

[^9-migrate]: The correction was number 262 in the press's tracker. It came in the first patch release after the major.

### The machinery behind the promise

Each profile carries a `design-major`, and the file *profile-seals.yaml* in the press's package data seals each profile with a digest of its contents. A check named `check_profile_seals` turns red when a profile's contents no longer match its seal.

The press also keeps visual regression baselines, rendered pages that its tests compare against. The rule for the baselines matches the rule for the design. A maintainer may record new baselines only "with a reason", and only in a new major. A patch that changes a page therefore shows up as a failed comparison in the press's own tests.

For your own pin, the rule means this: on `v3`, your book keeps the design it has today through every release of version 3. On `v3.0.2`, it keeps the same press code, the same composite action, and the same toolchain bytes forever. A new design reaches your book only when you change the major in your pin.

::: {.tip}
> **Tip:** Before you move a book to a new major, build the PDF on the old pin and keep it. Compare it with the new build page by page, and proof again any page that moved.
:::

Chapter 10, *Front matter, the index, and the table of authorities*, turns from the design of the page to the pages that press generates from configuration.

<!-- index: house design; design profile; house-6x9; print.profile; text block; height cap; scrbook; print interior; running head; folio; Libertinus; microtype; selnolig; widow; runt; craft law; book-colors; reader site; reader.css; extra.css; landing page; aesthetic; press aesthetic; site-url; design major -->
