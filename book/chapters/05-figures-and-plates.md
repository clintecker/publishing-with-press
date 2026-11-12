# Figures, plates, and illustrations

::: {.in-this-chapter}
> **In this chapter:**
>
> - Two kinds of picture
> - The image line and its four fields
> - Numbered figures and cross-references
> - The two lists
> - Placement
> - Measures and the runaround
> - What each edition does with a placement
> - The height cap
> - Files, formats, and resolution
> - Print-safe images
:::

A book of prose can carry two kinds of picture, and press holds each kind to its own law. The laws are short, but a slip against them costs real work. The checker refuses an image line, a citation prints as a raw `@fig:` in the proof, or a plate changes sides when a chapter grows by a page. This chapter shows how to type an illustration, how press numbers and lists it, where it sits on the printed page, and what each edition does with it. It ends with the image files and the pass that makes them safe for a printer. The examples use the Alice book, the full novel that user `alice` keeps on the workstation `hatter`, and none of them comes from the press's own three-chapter Alice example.

## Two kinds of picture

In this book an *illustration* is any picture in a chapter file, and press sorts every illustration into one of two kinds. A *plate* is an unnumbered illustration in the idiom of the literary woodcut, one that keeps the story company and asks nothing of the reader. A *figure* is a numbered informative illustration, such as a map, a chart, or a diagram, that the text cites by number. Press numbers figures by chapter, so the third figure in Chapter 7 prints as "Figure 7.3", and it never numbers a plate. The two kinds also go into two separate lists, which the section "The two lists" later in this chapter describes.

Press 3.0.0 introduced the split between plates and numbered figures. A novel such as *Alice's Adventures in Wonderland* wants plates: its pictures carry no numbers, and no sentence in the Mad Tea-Party sends the reader to "Plate 12". A manual such as this one wants figures, because the prose says "as Figure 5.2 shows" and the reader must find Figure 5.2. Most books need only one kind. Press lets a book mix the two, and this book does.

The first class on the image line decides the kind. Table 5.1 lists every class press knows, whether press numbers it, and what it means. Four of the kinds are *generatable*: `press illustrate` can commission them from an image model. The other two, `.chart` and `.diagram`, are *data kinds*. Press routes a data kind away from the image model, and `press illustrate` refuses to commission one.

| Class | Numbered | Meaning |
|------------|----------|---------------------------------------------------------|
| (none) | No | A bare image with no class is a plate. |
| `.plate` | No | The image is a plate, stated outright. Press can commission it. |
| `.figure` | Yes | The image is a general informative figure. Press can commission it. |
| `.map` | Yes | The image is a map. Press can commission it. |
| `.photo` | Yes | The image is a photograph. Press can commission it. |
| `.chart` | Yes | The image is a chart. It is a data kind, and `press illustrate` refuses it. |
| `.diagram` | Yes | The image is a diagram. It is a data kind, and `press illustrate` refuses it. |

Table: Table 5.1. The kind classes

Press knows all seven classes, but a book can hold itself to fewer. The numbered figures in this book use only `.diagram` and `.photo`. The `.chart` in Example 5.2 belongs to the Alice book. One attribute overrides the numbering: press never numbers an illustration that carries `decorative=true`, as the next section shows.

## The image line and its four fields

Every illustration begins as one Markdown image: an exclamation point, a caption in square brackets, and a path in parentheses. Attributes in curly braces may follow the path, and a comment may follow the whole line. Example 5.1 shows how you might type a plate for the first chapter of the Alice book. It has no class, so it is a plate.

**Example 5.1. A plate and its art directive**

```text
![Alice and the White Rabbit](assets/woodcuts/white-rabbit.png)

<!-- art: a small girl in a pinafore running across a meadow
     after a white rabbit in a waistcoat who holds a pocket
     watch; a hedge and the mouth of a rabbit-hole ahead of
     them; wood engraving, single black ink, no lettering -->
```

An illustration has four fields, each with its own reader. The *caption*, the text in the square brackets, is a label for the person who reads the book. The *directive*, the comment after the image, is art direction for the illustrator or the image model. The `fig-alt` attribute is the accessible alt text, a description for the reader who cannot see the picture. A credit line is the fourth, and press has no field for it: if an illustration needs a credit, write it into the caption. Press keeps the other three apart, and it never takes art direction from the caption.

The comment's keyword may be `art:`, `data:`, or `source:`. Press looks for the comment only after the image. The rule for its place is exact: image line, one blank line, then the comment. Press reads a comment on the very next line too, but that comment joins the image's paragraph, and pandoc then makes no figure of the image. The illustration loses its caption, its number, its entry in the list, and its cross-reference target. The `press figures` report still shows the directive, so nothing warns you.

::: {.warning}
> **Warning:** Always leave one blank line between the image line and its comment. A comment on the very next line breaks the figure without a message.
:::

A comment above the image, or two blank lines below it, belongs to no illustration at all. The directive may run over several lines, and it ends at the first `-->`.

Suppose you run `press illustrate` with the name of a plate and no `--subject`. Press then finds the illustration whose image file stem matches the name, and it sends that illustration's `art:` directive to the image model. For Example 5.1 the name is `white-rabbit`, the stem of *white-rabbit.png*. Press refuses in three cases: no illustration in the manuscript has that stem, the illustration is a data kind, or it has no `art:` directive. The third refusal says "A caption is a label, not art direction (#225)".[^5-silly-plates] Chapter 11, *The art department*, follows the commission from the directive to the finished plate.

Write the directive for an artist who does not know the book. Name the subject, the moment, and what sits around it, then the medium. If the picture must carry no lettering, say "no lettering". `press illustrate` adds a guard of its own to every commission, and it always appends this text to the prompt. The prompt receives it as one line, and the breaks here are only for the width of the page.

```text
Single ink only, no colour wash. No text, no words, no
lettering, no caption, no page border, no watermark, no
signature.
```

The image line can also name a style for the commission. Press takes the style from the `--style` option first, then from the illustration's own `style=` attribute, then from `plates.style` in the *aesthetic*, the book's visual identity in *config/aesthetic.yaml*. Last comes the house style `wood-engraving`. A book can therefore set one style for all its plates and still ask for an engraved map in one chapter.

The `fig-alt` text belongs on every illustration that carries information. Write it for a listener: one or two sentences that say what the picture shows. Never copy the caption into it. A screen reader reads the caption already, and a second reading of the same words tells the listener nothing new.

A *decoration* is an illustration that holds no information, such as a tailpiece, a rule, or a small vignette at the end of a chapter. Mark it with `decorative=true` and leave the caption empty:

```text
![](assets/woodcuts/rule.png){decorative=true}
```

Press gives a decoration an empty alt text, never numbers it, and never lists it, whatever its class. Because its alt text is empty by definition, the checker refuses `decorative=true` together with a `fig-alt`.

Press reads all of this in one place, and you can see what it read. The `press figures` target prints every declared illustration as JSON, with the fields `file`, `src`, `caption`, `kind`, `style`, `directive`, `description`, `generatable`, `identifier`, `width`, `place`, `outset`, `alt`, `decorative`, and `numbered`. The report gives a bare image the kind `figure`, although the numbering treats it as an unnumbered plate. Press treats this report as the one reading of the manuscript, and both `press illustrate` and the art-direction workflow use it.

::: {.tip}
> **Tip:** Run `press figures` after you edit an image line. If a directive does not appear in the report, press did not find it. The report cannot catch a comment on the very next line, so check the blank line by eye.
:::

## Numbered figures and cross-references

To cite a figure, give it an identifier with `#` in its attributes and cite the identifier with `@` in the prose. Any identifier works, but the common convention starts each one with `fig:`. Example 5.2 shows a numbered chart that the Alice book might put in its own fifth chapter, "Advice from a Caterpillar", with the sentence that cites it. Pandoc lets the attributes run over several lines, and the example breaks them only to fit the width of this page.

**Example 5.2. A numbered figure and its citation**

```text
As @fig:alice-heights shows, Alice is never the right height
for long.

![Alice's height](assets/woodcuts/heights.png){
    #fig:alice-heights .chart width=half-measure
    fig-alt="A stepped line that rises and falls, marking
    Alice's height at each bite of the mushroom."}

<!-- data: her height in inches at each change in the
     chapter, from three inches upward -->
```

The `.chart` class makes this a numbered figure. It is the first figure in that chapter, so press numbers it Figure 5.1, and the citation prints as "Figure 5.1" with a link to the figure. In the PDF, press keeps the word and the number together on one line, so a line break never separates "Figure" from "5.1". In the other rendered editions the citation is an ordinary link whose text is "Figure 5.1" and whose target is the figure's identifier.

Press computes each number once, in its own Lua filter, *figure-numbering.lua*. It has no dependency on pandoc-crossref, the filter that many pandoc users install for numbered figures. Because press computes each number once, the PDF, the EPUB, and the reader site can never disagree about which figure is Figure 5.1.

A citation of an identifier that press does not know stays in the text as a raw citation. If `alice` mistypes `@fig:alice-hieghts`, the proof prints the mistyped identifier, at sign and all, in the middle of the sentence. The fault is easy to see in a proof and easy to miss in a hurry.

Press numbers and cites only figures. A plate has no number, so a sentence that needs to point at a plate names its caption.

Press has no cross-reference mechanism for chapters or sections either, and no `@` form reaches a chapter or a section. Write those references in words: "see Chapter 6, *Checking the manuscript*", or "the section 'Placement' later in this chapter". Tables and examples in this book carry hand-typed numbers for the same reason.

::: {.tip}
> **Tip:** Before you send a proof to anyone, search the PDF text for `@fig:`. Every hit is a citation of an identifier that press did not recognize.
:::

## The two lists

Press keeps two lists of illustrations in the PDF, and both follow the Contents. The *List of Figures* holds every numbered figure with its number and its caption. It appears when the manuscript declares at least one numbered figure, which means a kind class without `decorative=true`. The *List of Plates* holds every plate with its caption and no number. It appears when *assets/woodcuts/* holds any image file. A book with no plate directory therefore never prints an empty List of Plates.

The plate directory and the manuscript must agree. If a plate on disk under *assets/woodcuts/* has no reference in the manuscript, the checker refuses the book and prints the path:

```text
plate never referenced by the manuscript: assets/woodcuts/<name>
```

The rule catches a plate that lost its image line in an edit, and it catches a plate that someone accepted and nobody placed. In both cases the file sits on disk and never reaches a page.

::: {.warning}
> **Warning:** When you delete an image line, delete its file from *assets/woodcuts/* in the same commit. Otherwise the next `press check` refuses the book.
:::

Both lists need several passes of LuaLaTeX before their page numbers come out right. Plain LuaLaTeX under pandoc does not run enough passes for the lists to converge. Press therefore builds the PDF through latexmk, which runs LuaLaTeX until the output stops changing. A second scar sits in the same place. A shallow table of contents once emptied the List of Plates without a message. The house TeX header now prevents that, so a book with a one-level Contents still gets a full List of Plates.[^5-tocdepth]

The links in the lists had a fault of their own. A reader who clicked an entry in the List of Plates once arrived at the caption, with the plate above it and off the screen. The house now anchors each entry at the top of the illustration, so a click shows the whole plate.[^5-hypcap] The PDF verifier now checks the link destinations with pypdf.

## Placement

The `place` attribute says where an illustration sits on the printed page. It takes one of seven values, and Table 5.2 lists them with what each one does in the PDF. Each of the seven values names a *placement*. Two terms in the table come from the trade. A *leaf* is one sheet of the book, two pages back to back, and a *cleared leaf* is a fresh page that holds nothing but the illustration.

| Placement | Meaning |
|----------------|-------------------------------------------------------------|
| `inline` | The illustration sits in the run of the text, where you typed it. The PDF holds it in place. |
| `wrap-inner` | Text runs around the illustration, which sits on the spine side of the page. |
| `wrap-outer` | Text runs around the illustration, which sits on the fore-edge side of the page. |
| `margin` | The illustration sets the same as `wrap-outer`, inside the text column. It does not sit in the true margin. |
| `plate` | The illustration sits in place like `inline`. The placement takes no measure. |
| `full-bleed` | The illustration takes a cleared leaf of its own, inside the margins. It does not ink the trim. |
| `frontispiece` | The illustration takes a cleared leaf of its own on an even page, so it faces the chapter that follows. |

Table: Table 5.2. The seven placements

@fig:placement-vocabulary draws the seven side by side, each on a miniature page. In the drawing and in the PDF, `inline` and `plate` look the same: both hold the illustration in place in the run of the text. They differ in one rule. A `plate` placement takes no measure, so the illustration prints at its own size, within the height cap and the line.

![The seven placements on a miniature page](assets/woodcuts/05-01-placement-vocabulary.png){#fig:placement-vocabulary .diagram width=full-measure fig-alt="Seven small book pages, each with ruled text lines and one gray block. The block sits in the text, by the spine, by the fore-edge, at the outer edge of the column, alone on a page, filling a page, and on a left-hand page before a chapter."}

<!-- art: ARCHETYPE matrix. Seven equal miniature pages in thin outline, two rows: four above, three below, centered. Each page has gray ruled text lines and one solid 20% gray block. Page 1: block across the column. Page 2: narrow block against the spine edge, lines shortened beside it. Page 3: the same against the fore-edge. Page 4: as page 3. Page 5: block alone, space above and below. Page 6: block filling the area inside the margins. Page 7: a left-hand page, block alone, a ghost right-hand page beside it with a chapter heading. Mark each spine edge with a short heavy rule. Under each page a monospace label: inline, wrap-inner, wrap-outer, margin, plate, full-bleed, frontispiece. The reader sees first where each block sits. -->

The word *plate* now does two jobs, and they are independent. The class `.plate`, or no class at all, makes an illustration a plate: unnumbered and in the List of Plates. The placement `place=plate` says only where it sits. A plate needs no `place=plate`, and a numbered figure can take `place=plate`. Type the placement for an illustration that must print at its own size. The checker will then refuse any measure that someone adds to it later.

The two wraps name a side of the page by its relation to the spine, because the spine changes sides from page to page. A printed book has two kinds of page: a *recto* is a right-hand page with an odd number, and its spine edge is on the left. A *verso* is a left-hand page with an even number, and its spine edge is on the right. An illustration at the left of the page sits by the spine on a recto and at the fore-edge on a verso. When a chapter grows by one page, every illustration after that page changes sides.

A `wrap-inner` illustration stays by the spine on every page, whatever the parity, and a `wrap-outer` illustration stays by the fore-edge. Press calls such a placement *parity-aware*. The checker refuses the values `left`, `right`, `wrap-left`, and `wrap-right`, and it refuses the bare `inner` and `outer` too. It refuses a value that press does not know at all as an unknown placement.

::: {.warning}
> **Warning:** Type `wrap-inner` or `wrap-outer` from the first draft. The checker refuses `left`, `right`, and the bare `inner` and `outer`.
:::

The `margin` placement promises more than it does. A true margin figure sits outside the text block, in the space beside it. The house sets `margin` as an outer-side wrap inside the text column, and in the PDF it looks the same as `wrap-outer`. Prefer `wrap-outer`, which names what the PDF does.

In the trade, a bleed runs the ink past the trim, so the picture reaches the edge of the paper. The house `full-bleed` takes a cleared leaf of its own and stays inside the margins, the same as the `frontispiece`. Neither one floats, so LaTeX never moves them away from where you typed them.

The `frontispiece` adds one step: it clears to an even page. On an even page it sits on the verso of an opening and faces the chapter title on the recto. Example 5.3 shows how the Alice book might give Chapter 7, "A Mad Tea-Party", a frontispiece.

**Example 5.3. A frontispiece before a chapter**

```text
![The Mad Tea-Party](assets/woodcuts/tea-party.png){
    place=frontispiece}

<!-- art: a long table set out under a tree in front of a
     house; the March Hare, the Hatter, and a sleeping
     Dormouse at one end; Alice in a large arm-chair; wood
     engraving, single black ink, no lettering -->
```

The image has no class, so it is a plate, and it goes into the List of Plates. A numbered figure can take the same placement. A `.map` at `place=frontispiece` gets a full leaf and a number.

## Measures and the runaround

The `width` attribute takes a *measure*, a width stated against the line of text. Press knows three, `full-measure`, `half-measure`, and `third-measure`, and a measure applies only to an in-flow placement, one that sits among the lines of text: `inline`, `wrap-inner`, `wrap-outer`, and `margin`. The checker refuses a measure on the other three placements, `plate`, `full-bleed`, and `frontispiece`. Table 5.3 lists that rule with the others the checker applies to an image line. Each row names a value that you might type and gives the reason the checker refuses it.

| What you type | Meaning |
|------------------------------------|-----------------------------------------------------|
| `place=left`, `place=right`, `place=inner`, `place=outer`, `place=wrap-left`, `place=wrap-right` | The checker refuses the side because it is not parity-aware. |
| `place=` with an unknown value | The checker refuses any placement outside the seven. |
| `width=quarter-measure` | The checker refuses any measure outside the three. |
| `width=half-measure` with `place=plate`, `full-bleed`, or `frontispiece` | The checker refuses a measure on a placement that is not in-flow. |
| `width=3in` with an in-flow placement | The checker refuses an absolute length in `pt`, `px`, `in`, `cm`, `mm`, or `%`. |
| `outset=6pt` | The checker refuses an outset in any unit except the em. |
| `decorative=true` with `fig-alt` | The checker refuses alt text on a decoration. |

Table: Table 5.3. What the checker refuses on an image line

A measure is relative for a reason. Each *design profile* is a sealed page geometry, a trim with its own margins and line, and the line is a different length in each profile. A figure set at half the measure stays at half the measure when the book moves to another profile. An absolute width ties the figure to one page design and says nothing about its relation to the text beside it. Chapter 9, *The house design*, describes the profiles.

A *wrap* is an illustration with text running around it, set with `wrap-inner`, `wrap-outer`, or `margin`. The *outset* is the gap between a wrap and the text beside it. The book trade calls the whole arrangement the *runaround*, and press uses the trade's term for the gap. The `outset` attribute takes a length in ems, and its default is `1em`. An em is the size of the type, so the gap grows and shrinks with the type and keeps its proportion in a large-print profile. The checker refuses any other unit.

@fig:wrap-against-text shows a wrap on each page of an opening. Before press starts a wrap, it asks for a number of free lines on the page, called the *guard*. If fewer lines remain, the wrap moves to the top of the next page. A wrap therefore never begins at the foot of a page with no room beside it. The side follows the parity of each page, as the section "Placement" earlier in this chapter describes.

![A wrap against running text on a verso and a recto](assets/woodcuts/05-02-wrap-against-text.png){#fig:wrap-against-text .diagram width=full-measure fig-alt="An open book with a figure on each page, both beside the spine, text running around them. A mark shows the small gap between figure and text, and a bracket spans one figure and the lines beside it."}

<!-- art: ARCHETYPE page anatomy. An open book drawn flat: verso left, recto right, a heavy vertical rule for the spine. Gray ruled text lines on both pages. On each page a 20% gray block against the spine edge of the text column, with text lines stopping short beside it. Callouts in small sans on thin leaders ending in dots: "wrap-inner" at each block; "outset" at the white gap beside the recto block, with a small double-headed arrow across it; "spine" at the center rule. In the recto's outer margin, a square bracket spans the block and the lines beside it, labeled "guard". The reader sees first that both blocks hug the spine. -->

A wrap with no `width` takes four tenths of the line. Table 5.4 gives the guard for each measure.

| Measure | Meaning |
|-------------------|-------------------------------------------------------------|
| `full-measure` | The page must have 20 free lines before the wrap begins. |
| `half-measure` | The page must have 13 free lines before the wrap begins. |
| `third-measure` | The page must have 9 free lines before the wrap begins. |
| (none) | The page must have 11 free lines before the wrap begins. |

Table: Table 5.4. The guard for each measure

Press's Lua filter fuses the wrap onto the head of the next paragraph, so the text runs around the illustration. In the chapter file, type the image line, one blank line, and then the paragraph that wraps, with nothing between them. Example 5.4 shows how the Alice book might put the Cheshire Cat on the fore-edge of a page in Chapter 6, "Pig and Pepper".

**Example 5.4. A wrap at a third of the measure**

```text
![The Cheshire Cat](assets/woodcuts/cheshire-cat.png){
    place=wrap-outer width=third-measure outset=1.5em}

The Cat only grinned when it saw Alice. It looked
good-natured, she thought: still it had very long claws
and a great many teeth...
```

Example 5.4 carries no `art:` directive, and that is deliberate. A wrapped illustration cannot carry an `art:` comment without losing its wrap. A comment between the wrap and its paragraph stops the fusion, and the text no longer runs around the illustration. A comment after the paragraph is too far from the image for press to read. Commission a wrapped plate with `press illustrate <name> --subject "..."` instead, as Example 5.5 shows:

**Example 5.5. Commissioning a wrapped plate**

```text
$ press illustrate cheshire-cat --subject "a large grinning cat
    on the bough of a tree, seen from below; wood engraving,
    single black ink, no lettering"
...
```

Choose the measure by what the reader must make out. A plate that keeps the story company can sit at a third of the measure beside the text. A map that the reader must study wants the full measure and an `inline` placement, so nothing competes with it for the width of the page. A half-measure figure is the usual compromise for a small map or a portrait.

A full-measure wrap is legal, but it fills the line and leaves no text beside it. For a wrap, use half or a third of the measure. This book wraps no diagrams, because a narrow figure shrinks its lettering below what a reader can use.

## What each edition does with a placement

Placement is print-only: the PDF honors every placement in Table 5.2. A reflowable edition has no fixed page, no verso and recto, and no leaf to clear. Press therefore ignores the placement in five editions. They are the Circulating edition (EPUB), the Single-leaf edition (the self-contained HTML), the Chapter edition (the reader site and its zip), the Telegraphic edition (plain text), and the Office edition (DOCX). In each of them a placed illustration becomes an ordinary figure: the image and its caption in the run of the text.

Press computes the number once and writes it into every rendered edition. A numbered figure's caption carries its "Figure 5.1" label in the PDF and in the Circulating, Single-leaf, Chapter, Telegraphic, and Office editions. The link changes form from one edition to the next: in the PDF, the citation links to the figure, and the figure has an entry in the List of Figures. The Circulating, Single-leaf, and Chapter editions get an ordinary link to the figure's identifier. A plate gets no number anywhere, and in the PDF its entry goes into the List of Plates. @fig:where-a-figure-lands traces the image line of Example 5.2 into each rendered edition.

![Where an image line goes in each rendered edition](assets/woodcuts/05-03-where-a-figure-lands.png){#fig:where-a-figure-lands .diagram width=full-measure fig-alt="One image line branches to six editions in four groups. The PDF gets a numbered caption, a List of Figures entry, and a link target. The EPUB, HTML, and reader site get an in-flow figure with its number and a link target. The plain-text and DOCX editions get an in-flow figure with its number. A bare image goes to the List of Plates."}

<!-- art: ARCHETYPE data-flow, top to bottom. At top, a dog-eared file box labeled "image line", holding "#fig:alice-heights .chart" in monospace. Below it a rounded box "figure-numbering.lua", its outgoing arrow labeled "Figure 5.1". Four arrows fan down to square boxes. "PDF" (20% gray fill): "caption Figure 5.1", "List of Figures entry", "link target". "EPUB / HTML": "in-flow, Figure 5.1", "link target". "reader site": "in-flow, Figure 5.1", "link target". "text / DOCX": "in-flow, Figure 5.1". At far right, a second dog-eared box "bare image" with its own arrow to a box "List of Plates", labeled "no number". The reader sees first that one line feeds every edition. -->

The Manuscript edition (the stitched Markdown) is the one exception. It is the raw stitched source, and no filter runs over it. Its image lines appear as you typed them, with their attributes and their `art:` comments, so that edition publishes every directive verbatim. Write each directive as though a reader will see it.

A plate also changes ground between editions. The house keeps each plate as an *alpha master*, ink on transparency, and each edition composites it onto its own page. The reader site serves the transparent PNG itself, so a plate reads on a light page or a dark one. The print interior flattens the master onto white at build time, as the section "Print-safe images" later in this chapter describes.

Write the prose so that it holds in every rendered edition. A sentence such as "the cat at the right of this page" is true on one page of one PDF. The EPUB has no right of the page, and the next revision of the PDF may have a different page. Cite a figure by its identifier and a plate by its caption, and describe what the picture shows instead of where it sits.

::: {.tip}
> **Tip:** Never write "the figure below" or "the picture at left". Cite a figure with `@fig:`, which every rendered edition resolves to the right number and link, and name a plate by its caption.
:::

## The height cap

Press scales every image to fit two limits. The height must fit the *height cap*, a maximum height that each design profile sets in its `figure-cap` key, 6.3 inches on the house profile. The width must fit the line. Press only ever scales down, so a small image prints at its own size and never grows to fill the line. The house header applies the two limits to every image that pandoc writes, whatever its kind or placement.

The two limits act together, and the limit that binds first sets the size. A wide, shallow image meets the line before it meets the cap, so it prints at the full width of the line and well under the cap. A tall, narrow image meets the cap first and prints narrower than the line. On most pages a square plate meets the line first. The same file can therefore print at different sizes in different profiles, and you change nothing in the manuscript to make that happen.

Each design profile sets its own cap. Table 5.5 lists the cap in five profiles, the ones whose caps differ from one another. The house 6 by 9 profile sets 6.3 inches, and that is the number you will most often see quoted. The cover-design and plates skills give 7.1 inches, but the cap that the PDF applies is the profile's value in Table 5.5.

| Profile | Meaning |
|---------------|-------------------------------------------------------------|
| house | No image prints taller than 6.3 inches. |
| novella | No image prints taller than 5.6 inches. |
| digest | No image prints taller than 6.0 inches. |
| large-print | No image prints taller than 7.2 inches. |
| mass-market | No image prints taller than 4.8 inches. |

Table: Table 5.5. The height cap by profile

The cap exists because of a failure that looked like nothing at all.

::: {.sidebar}
> **The infinite empty pages**
>
> A book built with press once had a figure taller than its text block. A figure that tall fits on no page at all. LuaLaTeX did not stop, and it did not report an error. It emitted empty pages, one after another, forever, at 100 percent of a CPU. Nothing reported a failure. The run never finished, so there was no PDF to inspect.
>
> The fix capped every included image below the height of the text block. The cap was 6.3 inches on the 6 by 9 page, and each profile now sets its own. The cap sits in the house TeX header, and the scars list in the press repository keeps it there. Every image now passes through the cap, so no manuscript can bring the failure back, however tall the picture its author supplies.
:::

::: {.warning}
> **Warning:** Do not try to defeat the height cap with a custom TeX header or a raw LaTeX include. A figure taller than the text block makes LuaLaTeX emit empty pages forever, silently, at full CPU.
:::

## Files, formats, and resolution

The cover is *assets/cover.jpg*, the logomark is *assets/press-logo.png*, the author portrait is *assets/author.jpg*, and the plates are PNG files under *assets/woodcuts/*. This book keeps its numbered figures in *assets/woodcuts/* as well, and you should do the same with every interior image, for a reason the section "Print-safe images" gives. The path in the image line is relative to the book repository, as every example in this chapter shows.

You can copy a file into *assets/woodcuts/* by hand, but the house way is *intake*. The command `press art accept build/illustrations/white-rabbit.png --as plate:white-rabbit` converts the delivered image to house form and writes it to *assets/woodcuts/white-rabbit.png*. The plate name must match the pattern `[a-z0-9][a-z0-9-]*`. A single-ink plate becomes an alpha master: its color channels are black everywhere, and all of its tone lives in the alpha channel. Chapter 11, *The art department*, describes the luminance key that intake applies and the refusals that protect it.

Plates are PNG files because of a scar. Truecolor PNG barely compresses the grain of an engraving, so the house once kept plates as JPEG files baked onto white. A JPEG master cannot carry transparency, and a plate baked onto white shows a white box on cream paper or on a dark reader page. The house now quantizes the grain to a few grays, which a PNG compresses well, and keeps the transparency. The scars list says it plainly: "Do not reintroduce a baked-white JPEG master."

Example 5.6 shows the whole path for one plate: the commission, intake, and the finishing pass. `press illustrate` sends the directive to an image model, so it needs that service's account and key, which Chapter 11 sets up. It writes each delivery to *build/illustrations/*. Each `...` line stands for the output of a command.

**Example 5.6. From commission to finished plate**

```text
$ press illustrate white-rabbit
...
$ press art accept build/illustrations/white-rabbit.png \
    --as plate:white-rabbit
...
$ press art enhance assets/woodcuts/white-rabbit.png
...
```

The finishing pass, `press art enhance`, does four things in order. If it finds an upscaler, it upscales the image by a factor of four with Real-ESRGAN. It then resamples downward to a long edge of 2400 pixels by default. It quantizes the image to a few tones, 16 grays for an engraving. Last, it compresses the PNG with whichever of oxipng or pngcrush it finds first. With no file argument, it finishes every JPEG and PNG under *assets/woodcuts/*, and its output always goes to *`<stem>`.png*.

Intake does not check resolution. It checks no minimum pixel count and no resolution metadata, and the only shape it checks is the cover's aspect ratio. Press leaves the size of the image to the height cap at typeset time, and it leaves the sharpness of the image to you. Press can scale an image down to fit the page, but it never scales one up. An image with too few pixels therefore prints soft at its own size.

A printer wants about 300 pixels per inch, abbreviated *PPI*, at the size the image prints. A plate at the full 6.3-inch cap of the house profile needs 6.3 times 300, or 1890 pixels, on its tall side. The 2400-pixel default of `press art enhance` covers a full-page plate on a 6 by 9 interior at 300 PPI, with room to spare. A delivery from `press illustrate` is always a 1024-pixel square, which is why the finishing pass upscales before it resamples.[^5-square]

The toolchain image carries Real-ESRGAN and its models on amd64 only. The arm64 image has no upstream binary, so it resamples and quantizes without the upscale, and resampling only ever goes down. On Apple Silicon inside the toolchain image, a 1024-pixel delivery therefore stays at 1024 pixels, about 162 PPI at the 6.3-inch cap. Outside the image, `press art enhance` uses an upscaler installed on the host if it finds one. It looks for `realesrgan-ncnn-vulkan` or `upscayl-bin` on the PATH, then in */usr/local/bin/*, then inside */Applications/Upscayl.app*. With none, it says so and goes on without the upscale.

::: {.tip}
> **Tip:** On an Apple Silicon Mac, install Upscayl or Real-ESRGAN and run `press art enhance` on the host, outside the toolchain image. Then multiply each plate's printed height by 300 and check that the file has at least that many pixels on that side.
:::

## Print-safe images

The *print interior* is the PDF that press builds for a print provider with `press print`, and Chapter 12, *The print pack*, describes it in full. It has one more reader than the PDF: the provider's preflight, the program a print provider runs over every file it receives. A preflight flags transparency and flags images that carry far more pixels than print needs. The print pack therefore passes each interior image in the directories it copies, listed later in this section, through a *print-safe* pass. The pass flattens each image onto white and caps its resolution, so the preflight sees no transparency and no over-resolution. Table 5.6 gives the caps.

| Image | Meaning |
|------------|-------------------------------------------------------------|
| Logomark | The pass resamples the logomark to a long edge of no more than 1000 pixels. |
| Figures and plates | The pass resamples each interior figure and plate to no more than 1900 pixels, about 300 PPI at 6.3 inches. |

Table: Table 5.6. The print-safe resolution caps

The pass keeps a grayscale image grayscale. It writes a JPEG source as a JPEG at quality 88, and it writes every other image as a PNG. The results go into *build/print-assets/*, and a Lua filter, *print-safe-images.lua*, points the interior's image paths at that directory. Your masters in *assets/* stay as they are. The reader site still gets the transparent plate, and only the print interior gets the flattened copy.

The pass does not copy every image. At the time of this writing it copies the logomark, the JPEG files at the top of *assets/*, and everything in *assets/woodcuts/*. An image in any other directory, such as *assets/figures/*, is missing from the print interior, and `press print` stops with "file not found". Keep every interior image under *assets/woodcuts/*.

The pass came from a real preflight. Lulu flagged two problems in an early print interior: transparency, because the logomark is ink on transparency, and images over 600 PPI. A 1024-pixel logomark printed at 1.7 inches comes to about 602 PPI, just over the line.[^5-lulu] With the pass in place, the documentation reports that "a current `press verify-print` interior triggers **neither** warning".

A custom title page needs one change to stay inside the rules. If the book supplies its own *tex/title-page-print.tex*, the logomark in it must come from *build/print-assets/*, not from *assets/*. A hand-written TeX file names its own paths, and the Lua filter that redirects the manuscript's images never sees them.

::: {.tip}
> **Tip:** In *tex/title-page-print.tex*, point the logomark at its copy in *build/print-assets/*. The file in *assets/* still carries its transparency and its full resolution.
:::

The next chapter, *Checking the manuscript*, describes the checker, which applies the rules in Table 5.3 whenever it runs.

[^5-silly-plates]: The rule has a history. Commissions once drew their subject from the caption, and a caption written for a reader made a poor brief for an artist. The results were what the press documentation calls "literal, silly plates". Since press issue #225, a commission with no `--subject` takes its subject from the `art:` directive alone.

[^5-tocdepth]: For the reader who wants the mechanism: the pandoc setting `toc-depth: 1` sets the LaTeX counter `tocdepth` to 0, which empties the List of Plates. The house header raises the depth inside the list file itself.

[^5-hypcap]: The anchor comes from the caption package's `hypcap=true` option. An earlier house header loaded the separate hypcap package for the same purpose.

[^5-square]: The square shape comes from the request press makes to the image model, which asks for 1024 by 1024 pixels at high quality for every illustration.

[^5-lulu]: The arithmetic is simple division: 1024 pixels over 1.7 inches is 602 pixels per inch.
