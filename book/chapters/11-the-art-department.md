# The art department

::: {.in-this-chapter}
> **In this chapter:**
>
> - What the art department is
> - The aesthetic
> - Covers
> - Interior plates
> - Intake: what acceptance enforces
> - One master, every surface
> - Finishing a plate
> - The commission record
> - Logomark and portrait
> - Keys, models, and what spends money
:::

A book needs pictures as well as words: a cover, the plates inside it, the *logomark* (the printer's mark of the imprint), and sometimes a portrait of the author. Press commissions each of these from an image model, takes the result into the book repository in a fixed house format, and refuses a delivery that would print badly. The path runs from an `art:` directive in a chapter file to a committed image under *assets/*. Some of the commands send work to a paid image service, and Table 11.7, in the last section, names them with the keys they read. The examples use the Alice book, which the user `alice` keeps on the workstation `hatter`.

## What the art department is

The *art department* is the set of press commands that commission, accept, and finish the book's art. Each picture starts as a *commission*, a prompt for an image model that the book keeps in *art/commissions.md*, and press runs each commission once. You generate each image on your own machine, with your own API keys, and you commit the result to the book repository as an asset. The CI build never generates art. The toolchain image holds no keys, and the press never stores them, so a build on `printshop` can only use the files that `alice` committed from `hatter`.

This arrangement keeps the build deterministic. A cover that an image model drew last Tuesday stays the same cover in every later build. The build reads the committed file and never asks the model again. It also keeps the cost in your hands. Every request to an image model costs money, and only a command that you run on your own machine can make one.

Table 11.1 lists the commands of the art department and what each one does.

| Command | Meaning |
|------------------------|-------------------------------------------------------------|
| `press aesthetic` | It prints the book's visual identity, the house aesthetic merged with the book's own file. Given a brief in quotes, it drafts that file. |
| `press cover` | It commissions one cover from a named cover style. It uses OpenAI only. |
| `press illustrate` | It commissions one interior plate from a named illustration style. It uses OpenAI only. |
| `press art commission` | It sends the prompts in *art/commissions.md* to OpenAI, to Gemini, or to both. |
| `press art accept` | It takes one delivered image into the book in house format and records the acceptance. |
| `press art enhance` | It upscales, quantizes, and compresses the plates so that each one is a small PNG. |

Table: Table 11.1. The commands of the art department

The commands fit together in a loop, which @fig:art-direction-loop shows. A picture starts as an `art:` directive in a chapter file and ends as a committed file under *assets/* that the next build reads.

![The art-direction loop, from directive to committed asset](assets/woodcuts/11-01-art-direction-loop.png){#fig:art-direction-loop .diagram width=full-measure fig-alt="A flowchart: a chapter file with art directives feeds press figures and the art-direction workflow, which writes art/commissions.md. Image commands write candidates into build/, press art accept moves one into assets/, press art enhance finishes it, and an arrow returns to the build."}

<!-- art: ARCHETYPE flowchart in two rows, so the lettering stays full size. Top row, left to right: dog-eared file "book/chapters/*.md" noted "art: directives"; rounded box "press figures"; rounded box "art-direction workflow"; dog-eared file "art/commissions.md"; rounded box "press art commission | press cover | press illustrate", its incoming arrow labeled "your API keys". An arrow drops to the bottom row, which runs right to left: folder "build/ and art/candidates/"; arrow labeled "you choose one" to rounded box "press art accept"; folder "assets/"; rounded box "press art enhance"; rounded box "the build" under the first file, with a short arrow up to it closing the loop. The reader should see first that the loop starts at the manuscript and returns to the build. -->

To take a picture through the loop:

1. If the book wants something other than the house aesthetic, draft its own. Use `press aesthetic "<brief>"` or the book-aesthetics *skill*, a packaged authoring guide that an agent reads.
2. Declare each illustration in the manuscript with an `art:` directive. Run `press figures` to see them all as JSON. A wrapped plate is the exception. It carries no directive, because the comment would break the wrap (Chapter 5, *Figures, plates, and illustrations*), so commission it with `press illustrate <name> --subject "..."`.
3. Run the `art-direction` *workflow*, a packaged agent procedure, by name with the Workflow tool, the Claude Code tool that runs a workflow. It writes *art/commissions.md*.
4. Generate candidates with `press art commission`, or with the one-off commands `press cover` and `press illustrate`.
5. Accept one candidate with `press art accept` *`file`* `--as` *`art-target`*. The *art target* names what the image becomes: `cover`, `plate:<name>`, `logomark`, or `portrait`.
6. Finish the plates with `press art enhance`.
7. Commit the assets.

Skills and workflows run in Claude Code, an agent program whose command is `claude`. Chapter 15, *The operator's desk and the editorial machines*, describes them.

Step 7 matters more than it looks. The CI build on `printshop` reads only committed files, so an image that stays on `hatter` never reaches an edition. Step 2 carries a rule of its own. A plate that sits on disk and that no image line in the manuscript references is an orphan, and `press check` refuses the book over it.

## The aesthetic

The aesthetic comes first, because the commission prompts draw on it. The *aesthetic* is the book's visual identity: its cover grammar, its plate medium, its logomark tradition, its portrait style, and its register. It lives in *config/aesthetic.yaml*, which is optional.

A book without the file gets the house aesthetic, which the press carries as *src/press/data/aesthetic-house.yaml* under the name "Victorian treatise". Its register gives the idea in three sentences: "Earnest nineteenth-century trade manual. The joke lives in the subject; the style stays dead serious. A ridiculous scene rendered earnestly is the voice."

The house aesthetic writes its art direction in plain sentences, one key at a time. Its cover is Victorian publisher's bookcloth, with "everything stamped as if by a brass die", on a solid cloth-colored field with a fine woven grain. The ink is gilt, a metallic gold stamping. The title and subtitle stand in stacked, centered letterpress capitals inside a border of two thin rules, with a small fleuron at each inner corner. One central engraved medallion carries the book's strongest image, "cut as a woodcut with hatching, never a gradient". The plates are wood engravings in single black ink, one idea to a plate, composed deliberately landscape or portrait.

To see the aesthetic that a book actually gets, run `press aesthetic` with no arguments. It prints one comment line, `# effective aesthetic (<source path>)`, and then the merged YAML. The merge is shallow at the top level. The press copies the house file and lays each top-level section of the book's file over it, whole.

Suppose the Alice book writes a `cover:` section with only a `style:` key in it. The house `cover:` section then disappears, and its medium, field, ink, and emblem go with it. The rule in the press's own words is "restate a whole section when you touch it".

Example 11.1 adds a `plates:` section to the Alice book's *config/aesthetic.yaml*, the file of Chapter 9's Example 9.1, and restates every key in it.

**Example 11.1. The plates section of the Alice book's config/aesthetic.yaml**

```text
plates:
  medium: >-
    Wood engraving after Tenniel, single black ink,
    dense hatching, no gray washes.
  composition: >-
    One scene per plate, composed deliberately landscape
    or portrait; a square plate wastes the trim.
  style: wood-engraving
```

Most of the keys in the aesthetic are prompt material. The `name`, `register`, `cover.*`, `plates.*`, `logomark.tradition`, and `portrait.style` keys go into the text of each commission, and the build machinery does not read them. A few keys do reach the build: the Web palettes, the typography, the book colors, and the scene-break ornament. Chapter 9, *The house design*, describes those keys.

Three keys in the prose sections also steer commands. `plates.medium` decides how intake treats a plate and which model finishes it. `cover.style` and `plates.style` pick the default cover and illustration styles.

The medium in Example 11.1 contains the words "single" and "ink". Intake looks for both words, as the section "Intake: what acceptance enforces" later in this chapter explains. If your plates are single ink, keep both words in your own medium.

To draft the file from a one-line brief, run `press aesthetic` with the brief in quotes:

```text
$ press aesthetic "a Victorian nursery book, gilt on red cloth"
...
review it: press aesthetic
```

The command runs the `aesthetic-brief` workflow headlessly through `claude`, writes *config/aesthetic.yaml*, and tells you to review the result. The command also takes an `--overwrite` option. The press's config validation does not cover *config/aesthetic.yaml*, so nothing catches a misspelled key. Read the merged output of `press aesthetic` after every change.

Some things in the art department are law and are not configurable. The press states them as four craft laws: "the exact title and author text appear verbatim on art, cover plates are flat (no mockups), print interiors are single ink, and the trim is the trim." The single-ink law has one sanctioned exception, the `house-6x9-color` design profile, which Chapter 12, *The print pack*, describes.

## Covers

`press cover` commissions one cover. Its synopsis is:

```text
press cover [--style <id>] [--subject <text>] [--print]
press cover --list
```

A *cover style* is a named prompt template for a whole genre of cover. The press carries ten of them in *src/press/data/cover-styles.yaml*, and `press cover --list` prints each with a one-line note. The command picks the style from `--style`, then from `cover.style` in the aesthetic, and then falls back to `penguin-tri-band`. Table 11.2 describes the ten styles.

| Style | Meaning |
|------------------------|-------------------------------------------------------------|
| `art-deco` | It draws symmetric stepped forms and sunbursts in the accent and gold on a deep field, in the manner of the 1920s and 1930s. |
| `bold-typographic` | It makes the title the image, with oversized letters that fill the cover. |
| `collage-mixed-media` | It layers torn paper, tape, stitching, and image scraps, and sets the type among the layers. |
| `midcentury-modern` | It draws one abstract symbolic mark in a limited palette, after Lustig and Rand. |
| `minimalist-literary` | It sets one small off-center motif and a small refined serif in vast negative space. |
| `penguin-tri-band` | It sets horizontal color bands around a cream center, with Gill Sans and a woodcut vignette of the subject. |
| `photographic` | It uses a full-bleed photograph graded toward the accent, with large sans capitals over it. |
| `pulp-paperback` | It paints a dramatic full-bleed scene under a bold condensed title. |
| `swiss-international` | It sets flush-left grotesque type on an asymmetric grid with one bold accent field and no illustration. |
| `victorian-clothbound` | It fills the cloth with a repeating engraved pattern of the subject's motifs around a central cartouche. |

Table: Table 11.2. The ten cover styles

The default style follows the Penguin paperback grid.[^11-penguin] It prints a single color on cream in three horizontal bands, with the title, the author, and a woodcut of the subject in the wide cream band. Ovals in the accent bands above and below hold the imprint and the publisher's initials.

Each template has fields that the command fills from the book, and Table 11.3 lists them.

| Field | Meaning |
|------------------|-------------------------------------------------------------|
| `{title}` | The command takes the title from the metadata. |
| `{author}` | The command takes the first author from the metadata. |
| `{imprint}` | The command takes the publisher from the metadata. |
| `{initials}` | The command takes up to three capitals from the publisher's name and skips "and", "the", "of", "for", "&", and "a". |
| `{accent}` | The command reads `web-palette.accent` and uses `#7a2325` when the palette does not set it. |
| `{paper}` | The command reads `web-palette.paper` and uses `#f4f1e6` when the palette does not set it. |
| `{subject}` | The command follows the precedence that the next paragraph gives. |

Table: Table 11.3. The cover template fields

The house palette defines no `accent`, so every book on the house palette gets `#7a2325` in its cover prompt.

The subject comes from the first of five sources that has a value. In order, they are the `--subject` option, `cover.subject` in the aesthetic, the `description` in the metadata, `cover.emblem` in the aesthetic, and finally the literal words "the book's subject". The chain dates from press 2.3.1. Before that release, a book that named its subject only in its `description` sent the model the literal words "the book's subject". The model then invented generic motifs to fill the space. Write the subject as you would caption a woodcut: three to eight nouns and a place.

Every one of the ten styles lets the model letter the cover itself, which the style file records as `text: baked`. For such a style the command appends a guardrail to the prompt. The guardrail lists the exact title, author, and imprint to render verbatim, and it ends with this line:

```text
Do NOT add: any other text, a price, a barcode, a watermark,
or extra logos.
```

Check the lettering on every candidate yourself, as the press's cover documentation advises.

`press cover` sends one request to `gpt-image-2` at 1024 by 1536 pixels and high quality. It writes the result to *build/cover/cover.png* and prints the next step, `press art accept build/cover/cover.png --as cover`. With no `OPENAI_API_KEY` in the environment, or with `--print`, the command spends nothing and prints the prompt instead:

```text
$ press cover --style victorian-clothbound \
    --subject "a rabbit, a pocket watch, a rabbit-hole"
# no OPENAI_API_KEY set; emitting the prompt to run elsewhere.
...
```

::: {.tip}
> **Tip:** Run `press cover --print` for each style you consider before you spend anything. Read the prompts side by side, then commission the one or two that suit the book.
:::

A book can add its own styles in *config/cover-styles.yaml*, under a `styles:` key. The press merges that file over its own library, style by style, so a book can add a style or replace one of the ten. Each style takes a `name`, an `era`, a one-line `note`, a `text` setting, and a `prompt` that may use the fields in Table 11.3. Example 11.2 shows a style that the Alice book adds for a gift edition.

**Example 11.2. A cover style of the Alice book's own**

```text
styles:
  nursery-gilt:
    name: "Nursery gilt"
    era: "the Alice book's imprint"
    note: "red cloth, a gilt oval vignette, centered capitals"
    text: baked
    prompt: |
      A book cover, portrait, on {paper}. Red bookcloth
      with a gilt engraved vignette of {subject} in an
      oval. The title "{title}" and author "{author}"
      in stacked centered capitals, stamped in gold.
```

With the file in place, `press cover --style nursery-gilt` fills the template and appends the text guardrail, because the style keeps `text: baked`. A style with any other `text` value only skips the guardrail. The cover documentation also advises a deep, saturated accent and a style that matches the genre. A field guide suits `penguin-tri-band` or a woodcut, and essays suit `minimalist-literary` or `swiss-international`. A thriller suits `pulp-paperback` or `photographic`, and a gift edition suits `victorian-clothbound`.

[^11-penguin]: The style file credits the grid to Edward Young and Jan Tschichold and dates it from 1935.

## Interior plates

`press illustrate` commissions one interior plate. Its synopsis is:

```text
press illustrate <name> [--style <id>] [--subject <text>]
    [--from <image>] [--print]
press illustrate --list
```

The *name* is the stem of the plate's image file. For the Alice plate at *assets/woodcuts/white-rabbit.png*, the name is `white-rabbit`. The press carries seven illustration styles, which Table 11.4 lists, and a book can add its own in *config/illustration-styles.yaml*.

| Style | Meaning |
|------------------------|-------------------------------------------------------------|
| `botanical-plate` | It draws a precise natural-history engraving of a specimen. |
| `engraved-map` | It draws an antique cartographic engraving and works best from a real map to redraw. |
| `figure-from-photo` | It redraws a photograph that you supply into a wood engraving, and it needs `--from`. |
| `line-diagram` | It draws a spare technical diagram that puts clarity before beauty. |
| `ornament` | It draws a small engraved vignette, rule, or device. |
| `technical-cutaway` | It draws an engraving-style cutaway of an object's internal structure. |
| `wood-engraving` | It draws the house interior plate, with bold engraved linework in one ink. |

Table: Table 11.4. The seven illustration styles

The command picks the style from `--style`, then from the illustration's own `style=` attribute, then from `plates.style` in the aesthetic, and falls back to `wood-engraving`.

Without `--subject`, the command finds the subject in the manuscript. It looks for the illustration whose image file stem equals the name, and it takes the `art:` directive that follows its image line. Chapter 5, *Figures, plates, and illustrations*, shows how to write the directive, and its Example 5.1 declares the Alice plate `white-rabbit` that this section commissions. The command refuses in three cases: when no image line in the manuscript declares the illustration, when the illustration is a data kind (`.chart` or `.diagram`), and when it has no `art:` directive.

The last refusal carries a reason with an issue number: "A caption is a label, not art direction (#225)." Commissions once drew from captions, which produced what the press documentation calls "literal, silly plates". A directive describes the picture an engraver would cut.

The `--from` option sends a source image along with the prompt, through OpenAI's image-edit endpoint. The `figure-from-photo` style requires it. Without a source, that style refuses with "the figure-from-photo style needs source material: --from <image>". Use `--from` with `engraved-map` too, when you have a real map for the engraver to redraw.

The templates take three fields. `{subject}` is the directive or the `--subject` text. `{ink}` comes from `book-colors.ink`, then `web-palette.ink`, then `#1b1b1b`. `{paper}` comes from `web-palette.paper`, then `#f4f1e6`. The house `book-colors.ink` is `171717`, without a hash sign, so a house prompt asks for its plate "in 171717 ink".[^11-ink] The command always appends a guardrail:

```text
Single ink only, no colour wash. No text, no words, no
lettering, no caption, no page border, no watermark, no
signature.
```

At the time of this writing, `press illustrate` sends one request to `gpt-image-2` at 1024 by 1024 pixels. Its plate is therefore square whatever the prompt says about composition (press issue #278). It writes `build/illustrations/<name>.png` and prints the next step, `press art accept build/illustrations/<name>.png --as plate:<name>`. The command suits a single plate that you want to try again. For a full set of plates, in the shape the aesthetic asks for, use `press art commission`, which the section "The commission record" later in this chapter describes.

To commission and accept one plate for the Alice book:

1. Confirm that the plate from Example 5.1 has an `art:` directive. Run `press figures` and find `white-rabbit` in the report.
2. Read the prompt before you pay for it. Run `press illustrate white-rabbit --print`.
3. Commission the plate. Run `press illustrate white-rabbit`.
4. Accept the result. Run `press art accept build/illustrations/white-rabbit.png --as plate:white-rabbit`.
5. Finish the plate. Run `press art enhance assets/woodcuts/white-rabbit.png`.

[^11-ink]: The `book-colors` keys take hex without the hash sign because they become `\definecolor` values for LuaLaTeX. The illustration template reads the same key and passes it on unchanged.

![The engraver's bench, a plate half cut](assets/woodcuts/the-engravers-bench.png)

<!-- art: an engraver's bench by a north window, seen from slightly above and in front: a boxwood block held on a leather sandbag, a graver in the engraver's right hand, a spray of burins and scorpers in a rack, a magnifying glass on a stand, a proof pulled from the half-cut block pinned to the wall showing a cuttlefish, a small brass press for proofing at the bench's end, shavings on the bench; landscape composition; wood engraving with dense hatching and crosshatching, single black ink, no gray washes, no lettering anywhere -->

## Intake: what acceptance enforces

*Intake* is what `press art accept` does to a delivered image: it converts the file to house format, checks what it can, places the result under *assets/*, and records the acceptance. Its synopsis is:

```text
press art accept <file>
    --as cover|plate:<name>|logomark|portrait
```

The art target after `--as` decides where the image goes and what happens to it. Before anything else, intake applies the EXIF orientation of every input, so a photograph that a camera stored on its side arrives upright. Table 11.5 gives the four art targets.

| Art target | Destination | Meaning |
|----------------|--------------------------|----------------------------------------------|
| `cover` | *assets/cover.jpg* | Intake checks the aspect against the trim, flattens any alpha onto white (never onto black), and writes an optimized JPEG at quality 88. |
| `plate:<name>` | *assets/woodcuts/<name>.png* | Intake writes an alpha master, which the next subsection defines. The name must match `[a-z0-9][a-z0-9-]*`. |
| `logomark` | *assets/press-logo.png* | Intake keeps the logomark as ink on transparency. |
| `portrait` | *assets/author.jpg* | Intake flattens the image onto white and writes a JPEG at quality 88. |

Table: Table 11.5. The art targets

The only geometry check at intake is the cover's aspect ratio. The ratio of height to width must fall within 3 percent of the trim's ratio. Intake refuses a cover outside that tolerance with "crop the source, do not stretch it".

Intake reads the trim from `trim` in *config/metadata.yaml* and takes it as 6 by 9 when the key is absent. It does not read the design profile. A book made by a current press has no `trim` key, because the press refuses a direct write to it (Chapter 3, *The shape of a book repository*). A 5 by 8 book therefore has its cover checked against 6 by 9. A hand-written `trim` mapping that agrees with the profile corrects the check. Intake checks no minimum pixel count and no DPI. The TeX header enforces the figure height cap when LuaLaTeX sets the book, and intake leaves that work to it.

::: {.warning}
> **Warning:** Do not stretch a cover to make it pass the aspect check. Crop the source to the trim's proportions, as the refusal says, or commission it again in the right shape.
:::

### The plate master

A plate goes through the most work. Intake treats a plate as single ink when two conditions hold. The design profile's ink must not be `color`, and `plates.medium` in the aesthetic must contain both the word "single" and the word "ink". The house medium meets both. A plate that meets them comes out as an *alpha master*: black ink on transparency, with all of the tone in the alpha channel. Every pixel of the master has the color (0,0,0), and only its opacity varies.

@fig:one-master-every-surface shows why the press wants a master of this kind. One file composites onto every ground the plate meets, and the section "One master, every surface" later in this chapter follows it to each one.

![One alpha master composited onto three grounds](assets/woodcuts/11-02-one-master-every-surface.png){#fig:one-master-every-surface .diagram width=full-measure fig-alt="At the left, an engraved rabbit in black ink on a checkered transparency. Three arrows lead right to the same rabbit on a white page, on a dark cloth cover, and on a Web panel."}

<!-- art: ARCHETYPE before/after, one source at the left and three results stacked at the right. Left: a square frame on a gray-and-white checkerboard holding an engraved rabbit in black ink, labeled "alpha master" and, in small monospace, "assets/woodcuts/white-rabbit.png". Three thin arrows fan right. Top result: a page outline on white, labeled "print interior, flattened onto white". Middle result: a small book cover in dark green cloth with woven grain, the rabbit stamped at its center, labeled "cloth cover, flattened onto the field color". Bottom result: a rounded Web panel on cream, labeled "Chapter edition, transparent PNG". The rabbit is identical in all three. The reader should see first that one file feeds all three. -->

A delivery that already has transparency keeps its mask, and intake grays it to the single ink. Intake counts a delivery as opaque when its minimum alpha is 250 or more. A file with an alpha channel but no real transparency therefore takes the opaque path.

An opaque delivery first meets the *flat-ground test*. Intake measures a band around the border of the image, one twenty-fifth of the shorter side wide and never under 3 pixels.[^11-band] At least 82 percent of the border pixels must have a luminance of 200 or more. The mean luminance of the top edge and the bottom edge may differ by at most 45, and the same limit holds for the left and right edges.

A gradient or a textured ground fails that test with "the luminance key would leave a ghost on the page". The refusal offers two remedies: commission the plate again on a plain near-white ground, or move to a color interior, which keeps the plate's exact pixels. The test arrived in press 3.0.0. Before that release, intake keyed every opaque plate. The key read every dark pixel of a gradient as ink, so the gradient survived as a smudge on the page.

A delivery that passes the test goes through the *luminance key*, which turns brightness into opacity. @fig:intake-before-after shows a delivered plate before and after intake. The key has two thresholds. A pixel with a luminance of 225 or more becomes fully transparent, with alpha 0. A pixel with a luminance of 45 or less becomes fully opaque, with alpha 255. Between the two, the alpha falls in a straight line from 255 at a luminance of 45 to 0 at a luminance of 225.

![What intake does to a delivered plate](assets/woodcuts/11-03-intake-before-after.png){#fig:intake-before-after .diagram width=full-measure fig-alt="Two frames side by side. The left frame shows an engraved rabbit on a slightly gray ground with a faint box edge. The right frame shows the same rabbit as black ink on a checkered transparency with no ground at all."}

<!-- art: ARCHETYPE before/after pair, two equal frames labeled (a) and (b) beneath. (a) "delivered": a small engraved white rabbit in a waistcoat on a ground of 5 percent gray, with a faint rectangle where the gray ends just inside the frame; a callout "ground near #f1f2f3". (b) "after intake": the same rabbit in black ink on a gray-and-white checkerboard meaning transparency, no ground, no box. Under the frames, a horizontal luminance scale from 0 to 255 with ticks at 45 and 225: left of 45 labeled "alpha 255, ink", right of 225 labeled "alpha 0, clear", the span between labeled "linear ramp". One thin arrow from (a) to (b). The reader should see first that the box vanishes in (b). -->

A color plate follows a simpler path. It keeps any alpha it arrives with. Intake flattens an opaque color plate onto white and leaves its colors unchanged. The intake code names a matting model as future work for color plates. At the time of this writing, the press has none.

::: {.sidebar}
> **The five-percent box**
>
> The white threshold of 225 looks low until you see where it came from. The gpt-image models lay their ground near `#f1f2f3`, a luminance of about 241, which reads as white on a screen.
>
> A naive key that maps luminance straight to opacity, alpha `255 - L`, gives that ground an alpha of about 14. On cream paper that residue shows as a pale gray rectangle around every plate, which the comment in the intake code calls "a five-percent box that is glaring on cream paper". The press set the white threshold below the ground instead. Anything at 225 or brighter becomes fully clear, and the box goes with it. A flat ground was the easy case. A gradient still defeated the threshold, and that failure produced the flat-ground test of press 3.0.0.
:::

[^11-band]: In the code, the band is `max(3, min(w,h)//25)` pixels wide, and the ramp is `round(255*(225-v)/180)` for a luminance `v`.

## One master, every surface

The alpha master exists so that one file can serve every place a plate appears, as @fig:one-master-every-surface in the previous section shows. Each edition composites the same ink onto its own ground.

The print interior flattens the master onto white when the book builds. The print-safe pass, which Chapter 5, *Figures, plates, and illustrations*, describes, does this for every plate, figure, and logomark in the print interior. The print vendors are the reason. Lulu once flagged a book's logomark for its transparency, and for its resolution of over 600 PPI, so the pass now flattens each of those images and caps its resolution.

The Chapter edition (the reader site) serves the alpha master as it is, so a plate reads correctly on a light page and on a dark one. For the cloth cover, the press documentation describes the same treatment. A cloth cover would flatten the master onto the field color, which is how the logomark already works.

The rule against baking a plate onto white is a scar. Plates were once baked JPEGs, because truecolor PNG barely compresses the grain of an engraving. A baked plate carries its white ground onto cream paper and onto a dark page alike. The press now keeps the master as ink on transparency and solves the size problem in `press art enhance`. The scars list puts it plainly: "Do not reintroduce a baked-white JPEG master."

::: {.warning}
> **Warning:** Do not convert a plate in *assets/woodcuts/* to JPEG to save space. A JPEG has no alpha channel, so the plate loses its transparency for good. Run `press art enhance` instead.
:::

## Finishing a plate

`press art enhance` finishes plates for publication. Its synopsis is:

```text
press art enhance [file] [--colors N] [--max-edge PX]
```

Without a file argument, the command finishes every *.jpg* and *.png* file in *assets/woodcuts/*. Its output is always a PNG with the same stem. The work runs in four steps, in this order:

1. It upscales the plate with Real-ESRGAN.
2. It resamples the plate downward to the chosen long edge.
3. It quantizes the plate to a few gray levels.
4. It compresses the PNG.

For the upscale, the command looks for `realesrgan-ncnn-vulkan` or `upscayl-bin` on the `PATH`, then for */usr/local/bin/realesrgan-ncnn-vulkan*, and then for the binary inside *Upscayl.app* in */Applications*.[^11-upscayl] It looks for the models in */usr/local/share/realesrgan/models*, then in Upscayl's models directory, and then in a *models* directory beside the binary. It runs the upscaler at a scale of 4, with a timeout of 600 seconds. The medium in `plates.medium` chooses the model and the default number of colors, by substring, as Table 11.6 shows.

| Medium contains | Model and colors | Meaning |
|------------------------------|----------------------|----------------------------------------|
| `engrav`, `woodcut`, `wood engraving`, or `line` | remacri-4x, 16 | The command treats the plate as line work and keeps 16 gray levels. |
| `pen` or `etch` | remacri-4x, 24 | The command keeps 24 levels for the finer tone of pen and etching. |
| `wash`, `watercolour`, or `watercolor` | ultrasharp-4x, 64 | The command keeps 64 levels for continuous washes. |
| anything else | remacri-4x, 16 | The command uses the line-work defaults. |

Table: Table 11.6. How the plate medium chooses the upscaler model

If the chosen model is missing, the command tries remacri-4x, ultrasharp-4x, realesrgan-x4plus, and upscayl-standard-4x, in that order. If it finds no upscaler at all, it prints a note that it will quantize and compress without an AI upscale, and it carries on.

The resample uses a Lanczos filter and only ever shrinks the image. The default long edge is 2400 pixels, which the code comment explains: it "covers a full-page plate on a 6x9 interior at 300 DPI". The `--max-edge` option changes it.

The quantize step uses median cut to reduce the plate to the number of colors that Table 11.6 gives, or to the number in `--colors`. It quantizes in grayscale unless the design profile is color. It keeps the alpha channel and reattaches it afterward. The last step saves the PNG with optimization on and then runs `oxipng -o 4` or `pngcrush -ow`, whichever it finds first.

The toolchain image bakes in `realesrgan-ncnn-vulkan` with the remacri and ultrasharp models, and the *Dockerfile* pins the download by its sha256. The upscale in the image works on amd64 only, with CPU inference against a software Vulkan device. No upstream binary exists for arm64, so the arm64 image resamples instead of upscaling. On `hatter`, `alice` can finish one plate, or all of them:

```text
$ press art enhance assets/woodcuts/white-rabbit.png
$ press art enhance --colors 24
```

::: {.tip}
> **Tip:** Run `press art enhance` after every intake and before you commit. The quantize step reduces the grain to a few grays, and that keeps each plate a small lossless PNG.
:::

[^11-upscayl]: Upscayl is a desktop application for upscaling images. The press looks inside its application bundle, so an installed copy can do the upscale.

## The commission record

The file *art/commissions.md* holds the book's commissions, the prompts for the image models, and the record of what the book accepted. The `art-direction` workflow writes it.

You run the workflow by name with the Workflow tool, after the two steps that feed it. Those steps are the book's own aesthetic, if it has one, and an `art:` directive on every illustration that `press figures` reports, except a wrapped plate. What comes back is *art/commissions.md*, in the fixed headings that Example 11.3 shows. Read each prompt before you commission anything. `press art commission` sends the first fenced block of each section as the prompt, with a style preamble on a plate and a likeness preamble on a portrait. Chapter 15, *The operator's desk and the editorial machines*, describes how a workflow runs.

`press art commission` reads the file back. If the file is missing, the command refuses with "no commissions.md; run the art-direction workflow first".

The file uses fixed headings, and Example 11.3 shows its shape for the Alice book. A heading that begins `## Cover` holds the cover. A `## Plates` heading holds one `###` subheading for each plate, and the subheading gives the plate's name. `## Logomark` and `## Author portrait` hold the last two. The command takes the first fenced block in each section as the prompt for that art target.

**Example 11.3. The shape of art/commissions.md**

````text
## Cover

```
A Victorian publisher's bookcloth cover ...
```text

## Plates

### white-rabbit

```
A small girl in a pinafore runs after a white rabbit
... landscape composition ...
```text

## Logomark

```
A printer's mark ...
```text

## Author portrait

```
An engraved oval trade-journal portrait ...
```text
````

At the time of this writing, the command reads a plate's shape from the words of its prompt. The phrase "landscape composition" selects the landscape size, and "portrait composition" selects the portrait size, as in the rabbit's prompt in Example 11.3. Any other prompt gets the square size, which the house aesthetic warns against: "a square plate wastes the trim."

::: {.tip}
> **Tip:** Search *art/commissions.md* for the word "composition" before you commission anything. Add the phrase to any plate prompt that lacks it.
:::

The headings map to the art targets that `press art commission` accepts: `cover`, `plate:<name>`, `logomark`, and `portrait`. The synopsis is:

```text
press art commission [targets] [--model openai|gemini]...
    [--count N] [--photo PATH]
```

With no art targets, the command commissions all of them. The `--count` option sets the number of images per art target per model and defaults to 1. The command writes each candidate to `art/candidates/<art-target>/<model>-<n>.png`, with the colon in a plate's art target changed to a hyphen. The command writes the first OpenAI candidate for the rabbit to *art/candidates/plate-white-rabbit/openai-1.png*. Candidates number upward and never overwrite. A second run adds *openai-2.png* beside the first.

Example 11.4 commissions two rabbit candidates from OpenAI alone, from the prompt under `### white-rabbit` in Example 11.3. It then accepts the second into *assets/woodcuts/white-rabbit.png*.

**Example 11.4. Commissioning and accepting one plate**

```text
$ press art commission plate:white-rabbit --model openai \
    --count 2
...
$ ls art/candidates/plate-white-rabbit
openai-1.png  openai-2.png
$ press art accept \
    art/candidates/plate-white-rabbit/openai-2.png \
    --as plate:white-rabbit
```

A plate commission also carries style. The command attaches up to two plates that the book already accepted from *assets/woodcuts/* as reference images, never the plate it redraws. It adds a preamble that asks the model to "Match their hand exactly" and says "The new plate must look cut by the same engraver." Each new plate in the Alice book therefore has its predecessors to match.

When you accept a candidate, intake writes a line under a `## Acceptance record` heading in *art/commissions.md*. Each art target has one line, and a later acceptance replaces the earlier line for that art target. The line has the form ``- Accepted {date}: `{target}` <- {source.name}, {w}x{h}px, placed at {dest}``. A year later, the record still tells the maintainer which candidate became each plate and at what size.

## Logomark and portrait

The house aesthetic states the logomark's tradition: "A printer's mark: it certifies the maker, it does not advertise. Flat single-ink line art on transparency." Intake writes it to *assets/press-logo.png* as ink on transparency.

A logomark that arrives opaque goes through a hard threshold. Every pixel with a luminance below 96 becomes ink, painted as (23,23,23) on transparency, and every other pixel becomes clear. Intake then prints "logomark arrived opaque; ink extracted to transparency".

`press art commission` requests the logomark from `gpt-image-1` at 1024 by 1024 pixels with a transparent background. The logomark stays on the older model because `gpt-image-2` dropped transparent backgrounds. On Gemini, the command requests the logomark at 1:1 and 1K. At the time of this writing, OpenAI rejects requests for `gpt-image-1` (press issue #277), so the OpenAI logomark request fails. Commission the logomark with `--model gemini`, and intake extracts the ink of the opaque delivery onto transparency.

The *author portrait* goes to *assets/author.jpg*, flattened onto white as a JPEG at quality 88. The house aesthetic's portrait style is "An engraved oval trade-journal portrait of a valued tradesman, dense hatching, single ink, solemn and respectful." An author photograph makes the portrait commission engrave the actual author. The `--photo` option of `press art commission` names the photograph. Without it, the command looks for `art/author-photo.*` and ignores case in the match. It accepts *.jpg*, *.jpeg*, and *.png* files. It refuses an empty file, with a hint that the file may be an interrupted copy.

The command normalizes some photographs before it sends them. A photograph qualifies when it is over 2048 pixels or about 4 MB, or when it is not a JPEG. The command applies its EXIF orientation, shrinks it to 2048 pixels, and re-encodes it as a JPEG at quality 90. The work happens in memory, and the press never modifies your file. The command then prefixes the portrait prompt with a likeness preamble, which begins:

```text
The attached photograph is the author: the person facing
the camera. Ignore every other face in the frame,
including faces printed on clothing...
```

The preamble also asks the model to say so in text when a feature is hidden, so that it does not invent one. The book template's *CLAUDE.md* gives the advice for the photograph: "head and shoulders filling the frame, no hat, no sunglasses, even light, and no other face in the shot (including faces printed on clothing)."

::: {.tip}
> **Tip:** Try more than one photograph with `--photo` *`path`*. The candidates number upward and never overwrite, so you can compare them side by side.
:::

## Keys, models, and what spends money

The press reads API keys from the environment and nowhere else, and a key is all the setup it needs from each service. It reads `OPENAI_API_KEY` for OpenAI and `GEMINI_API_KEY` for Gemini. A command that needs a missing key refuses with this message, where the variable's name replaces `{var}`:

```text
{var} is not set; the press does not store keys
```

The press records the rule as an invariant, `INV-art-key-never-stored`, and it never stores a key. Set the keys in your shell on `hatter` for the session in which you commission art, and nowhere that CI can read.

Three commands send requests to a paid image service, and Table 11.7 names them with the keys they read.

| Command | Keys | Meaning |
|------------------------|------------------|-----------------------------------------------|
| `press art commission` | `OPENAI_API_KEY`, `GEMINI_API_KEY` | It sends every art target to both OpenAI and Gemini unless you name a model with `--model`. |
| `press cover` | `OPENAI_API_KEY` | It sends one cover request to OpenAI. With no key, or with `--print`, it prints the prompt and spends nothing. |
| `press illustrate` | `OPENAI_API_KEY` | It sends one plate request to OpenAI. With `--print`, it prints the prompt. |

Table: Table 11.7. The commands that spend money

`press art accept` and `press art enhance` work on files on your own machine and send nothing to a paid image service. The Real-ESRGAN upscale in `press art enhance` runs locally. `press aesthetic` with no arguments only prints the merge. `press aesthetic` with a brief and the `art-direction` workflow run an agent through `claude` under your own Claude Code setup, and Table 11.7 does not list them.

`press art commission` asks for no confirmation before it spends. It prints a plan line such as `submitting N commissions ... cover -> openai+gemini` and proceeds. The `--model` option is repeatable, and its default is both models. At the time of this writing, a missing `GEMINI_API_KEY` stops the run only after the OpenAI images are paid for.

::: {.warning}
> **Warning:** Name the model every time you run `press art commission`. Without `--model`, the command pays both OpenAI and Gemini for every art target, and it does not stop to ask.
:::

To commission the whole set of art for the Alice book from OpenAI alone:

1. Export `OPENAI_API_KEY` in the shell on `hatter`.
2. Read *art/commissions.md* and confirm that every plate prompt names its composition.
3. Name every art target except `logomark`, because of press issue #277. Run `press art commission cover portrait plate:white-rabbit --model openai`, with one `plate:` for each plate.
4. Commission the logomark from Gemini. Export `GEMINI_API_KEY`, then run `press art commission logomark --model gemini`.
5. Look at each candidate under *art/candidates/* and choose one per art target.
6. Accept each choice with `press art accept` *`file`* `--as` *`art-target`*.
7. Run `press art enhance`, then commit *assets/* and *art/commissions.md* together.

The press uses four models, which its code fixes as constants: `gpt-image-2` as the OpenAI flagship, `gpt-image-1` for transparency, `gemini-3-pro-image` as the Gemini flagship, and `gemini-3.1-flash-image` as the Gemini workhorse. A comment in the code calls the choice "print-driven, researched 2026-07".

A 6 by 9 cover at 300 DPI needs about 1800 by 2700 pixels. `gpt-image-2` takes sizes in multiples of 16, with a maximum edge of 3840 pixels and a maximum area of about 8.3 megapixels. On Gemini, the pro model draws covers because it renders text best, and the flash model draws plates and portraits. Table 11.8 gives the shape that `press art commission` asks for, by art target.

| Art target | Meaning |
|--------------------|-------------------------------------------------------------|
| `cover` | OpenAI's `gpt-image-2` draws it at 2304x3456, high quality and opaque. Gemini's `gemini-3-pro-image` draws it at 2:3 and 4K. |
| portrait plate | `gpt-image-2` draws it at 2304x3456. Gemini's `gemini-3.1-flash-image` draws it at 2:3 and 2K. |
| landscape plate | `gpt-image-2` draws it at 3456x2304. The flash model draws it at 3:2 and 2K. |
| square plate | `gpt-image-2` draws it at 2048x2048. The flash model draws it at 1:1 and 2K. |
| `logomark` | `gpt-image-1` draws it at 1024x1024 on a transparent background (press issue #277). The flash model draws it at 1:1 and 1K. |
| `portrait` | `gpt-image-2` draws it at 2304x3456. The flash model draws it at 2:3 and 2K. |

Table: Table 11.8. The shapes that press art commission requests

Each request goes from your machine straight to OpenAI or Google, and Gemini takes one request per image.[^11-imagen] The cover size in Table 11.8 differs from the size that `press cover` requests, which is 1024 by 1536. Both have the 2:3 shape, and intake checks only the shape. When Gemini refuses a prompt, the press prints the `finishReason` and up to 300 characters of the model's explanation.

[^11-imagen]: OpenAI requests go to *https://api.openai.com/v1/images/generations*, or to *https://api.openai.com/v1/images/edits* as a multipart form when they carry reference images. A transparent request adds `background: "transparent"`. Gemini requests go to the `generateContent` endpoint of *https://generativelanguage.googleapis.com/v1beta/*, with the key in the `x-goog-api-key` header. A comment in the code explains that the Imagen predict endpoint "is closed to new API users".

<!-- index: art department; aesthetic.yaml; press aesthetic; cover style; press cover; press illustrate; art directive; press art accept; intake; alpha master; luminance key; flat-ground test; press art enhance; Real-ESRGAN; commissions.md; acceptance record; art-direction workflow; press art commission; logomark; author portrait; OPENAI_API_KEY; GEMINI_API_KEY; gpt-image-2 -->
