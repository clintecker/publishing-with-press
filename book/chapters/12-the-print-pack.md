# The print pack

::: {.in-this-chapter}
> **In this chapter:**
>
> - Four orthogonal choices
> - Design profiles
> - Providers and their numbers
> - Building the interior
> - The cover wrap
> - The barcode
> - Print-safe images
> - Verifying the print pack
> - Qualification and the golden copy
> - Publish checklists
> - Ordering a copy
:::

A print shop wants two files from you: an interior and a cover, each built to the shop's own numbers. The shop runs its own checks on both, as Lulu once did when it flagged a press logomark for transparency. A mistake that gets past those checks arrives in a box of books. The press builds both files from the manuscript that gives you the Print edition (the reading PDF), and it inspects both before you upload them. The Alice book here is a 6 by 9 paperback with cover art in *assets/cover.jpg*. This chapter follows user `alice` as she takes it from the first print setting to a copy in the mail.

## Four orthogonal choices

*The print pack* is the set of artifacts a print shop needs: the print interior, the cover wrap, and the checklists for the retail channels. The *print interior* is the PDF that goes inside the covers. The *cover wrap* is the whole printed cover, back, spine, and front, set as one PDF page. Before the press builds either one, it needs four answers from you. Each answer has its own configuration key, and each key changes one thing only.

Table 12.1 lists the four choices with their keys and defaults.

| Choice | Key and default | Meaning |
|------------------|------------------------------|-----------------------------------------------------|
| Trim and interior | `print.profile`, `house-6x9` | The design profile sets the page size and the interior geometry. |
| Binding | `print.binding`, `perfect-bound` | The binding sets the topology of the cover: whether it has a spine, and whether it has flaps. |
| Cover material | `print.material`, `paperback` | The material sets the cover treatment, printed or cloth. |
| Provider | `print.provider`, `house` | The provider supplies the spine arithmetic, the hardcover margins and hinges, and the list of what the shop will make. |

Table: Table 12.1. The four print choices

The choices are *orthogonal*: you can change any one of them and leave the other three as they were. A new trim does not change the binding, and a new provider does not change the trim. The provider changes the arithmetic of the cover and the list of things the shop will make. Example 12.1 shows the four keys set for a 5 by 8 hardcover printed on the board at Lulu. It is a sample of the syntax, and the Alice book stays a `house-6x9` paperback.

**Example 12.1. Four print settings for a Lulu hardcover**

```text
$ press config set print.profile novella-5x8 && \
  press config set print.provider lulu && \
  press config set print.binding casewrap && \
  press config set print.material casewrap
```

The binding decides the shape of the cover. A `perfect-bound` book has a back, a spine, and a front, in that order. A `saddle-stitch` book and a `coil` book have no spine at all. A `casewrap` book is a hardcover printed on the board itself, with a turn-in where the paper folds over the board and a hinge beside the spine. A `dust-jacket` book wears a printed jacket with flaps that tuck inside the boards.

The material decides what the press prints on that shape. The press prints a `paperback` cover or a `casewrap` cover all over. A `linen` cover is cloth, so the press suppresses the printed field and prints only the dust jacket that goes over it. The documentation states the reason plainly: "Press never bakes a simulated cloth texture into a real linen cover."

Not every provider makes every combination, and the press knows which ones each provider offers. `press check` refuses an unsupported trim, binding, or ink combination before any render begins. The message comes from the provider spec itself, through `ProviderSpec.check_selection`. You learn that KDP makes no dust jacket before LuaLaTeX sets a single page.

## Design profiles

A *design profile* is a sealed interior geometry: a trim size, the margins and type block inside it, and the Web settings that go with it. Chapter 9, *The house design*, describes the geometry of each profile. Here the question is narrower. You need to know which trims exist and which providers cut each one.

At the time of this writing, press 3.0.2 carries six profiles. Table 12.2 lists them, with the providers that cut each trim.

| Profile | Trim | Meaning |
|----------------------------|-------------|------------------------------------------------------|
| `house-6x9` | 6 by 9 | It is the sealed house default. Lulu, KDP, and IngramSpark cut it. |
| `house-6x9-color` | 6 by 9 | It is the house geometry with a color interior. Only KDP cuts it in color. |
| `novella-5x8` | 5 by 8 | It suits a short novel or a novella. Lulu, KDP, and IngramSpark cut it. |
| `digest-5.5x8.5` | 5.5 by 8.5 | It suits trade-paperback genre fiction. Lulu, KDP, and IngramSpark cut it. |
| `mass-market-4.25x6.87` | 4.25 by 6.87 | It is a rack-sized genre paperback. Only Lulu cuts it. |
| `large-print-7x10` | 7 by 10 | It is large print, for accessibility. Lulu, KDP, and IngramSpark cut it. |

Table: Table 12.2. The six design profiles and the providers that cut them

Each profile declares its ink as `single` or `color`. An unknown id fails with `unknown print profile '<id>'; available: ...`, and the six ids take the place of the dots.

Each profile also carries a *seal*: a short digest of its contents, recorded in *profile-seals.yaml* in the press's package data. The check `check_profile_seals` recomputes every digest and turns red when one disagrees, so a profile's geometry cannot change inside a release without a visible reseal. Contributors who add a profile follow *docs/PROFILE-LIFECYCLE.md* and the `profile-lifecycle` skill, which scaffold it, prove it at its trim, and seal it.

### The color profile

The documentation describes `house-6x9-color` as "the 6x9 house geometry, byte-for-byte, with one difference: the interior prints in colour". The profile lifts the print verifier's single-ink rule. It also keeps plates in color at intake instead of graying them. The key `print.color-grade` takes `standard-color`, the default, or `premium-color`.

A color interior has one more requirement, and it comes from the spine. The spine width rests on a *caliper*, the thickness of one page of the stock. A color interior therefore needs a caliper for color stock, from a provider that documents one. At the time of this writing, only KDP does. At Lulu and at IngramSpark, the press refuses a color interior. The ledger holds no sourced color caliper for either provider, and the press will not guess a thickness.

::: {.warning}
> **Warning:** Do not plan a color interior for Lulu or IngramSpark. A guessed spine is a cover that does not fit.
:::

## Providers and their numbers

A *provider* is a print shop's specification as the press records it: `house`, `kdp`, `lulu`, or `ingramspark`. The profile decides what the pages look like. The provider decides how wide the spine is, how far a hardcover's board and hinge extend, and which trims, bindings, and page counts the shop accepts. The default is `house`, a set of numbers that belongs to no shop in particular. The section "The layout" later in this chapter shows how these numbers place the bands of the cover wrap.

The provider data comes from one reviewed ledger, *quality/providers.yaml*, in the press repository. The press generates its installed copy from it, and *docs/PROVIDER-DATA.md* gives the rule plainly: "Never edit it by hand."

### Four spine shapes

The spine is the hard number, and the providers compute it in four different ways. The press names each way a *spine shape*. Two of the shapes add an *allowance*, a fixed amount added on top of the thickness of the pages.

- `constant` multiplies the page count by a caliper for the stock and adds an allowance: `pages * caliper[stock] + allowance`. KDP and the house provider use it.
- `divisor` divides the page count by a fixed number and adds an allowance: `pages / divisor + allowance`. Lulu paperbacks use it, and the stock does not enter into it.
- `ppi-table` divides the page count by a pages-per-inch figure for the stock: `pages / ppi[stock]`. IngramSpark uses it.
- `lookup` reads a stepped table keyed by bands of page count. Lulu hardcovers use it.

@fig:spine-math sets the four shapes side by side with each provider's own figures.

![Spine math by provider](assets/woodcuts/12-01-spine-math.png){#fig:spine-math .diagram width=full-measure fig-alt="A grid with five provider rows and three columns. Each row gives the provider's spine shape, its formula or table of figures, and its allowance, with two allowance cells left empty."}

<!-- art: ARCHETYPE matrix. Thin rules, header row at 10% gray. Column heads in small sans, widths about 20, 55, and 25 percent: "spine shape", "formula or table", "allowance". Long cells wrap to two or three lines inside the cell. Row labels in small monospace, top to bottom. "house": "constant"; "pages x caliper / white 0.002252 / cream 0.0025"; "0.0". "kdp": "constant"; "pages x caliper / white 0.002252, cream 0.0025 / std-color 0.002252, prem-color 0.002347"; "0.06". "lulu paperback": "divisor"; "pages / 444"; "0.06". "lulu hardcover": "lookup"; "26 bands / 24-84 pp 0.25in ... 779-800 pp 2.0625in"; empty. "ingramspark": "ppi-table"; "pages / ppi / cream 444, white 512 / white-70 377, groundwood 400"; empty. Numbers in small monospace. The reader sees first that the four shapes differ, row by row. -->

The house provider looks like KDP with the allowance set to zero.[^12-allowance] Its calipers are KDP's white and cream figures. That makes it a sound default for a book with no shop chosen yet, and it also means the house spine is no real provider's spine.

Example 12.2 gives the widths that the four shapes produce for three page counts, in inches. The columns are the house provider, KDP on cream and white (`KDP`, `KDP-w`), and a Lulu paperback (`Lulu-PB`). Then come IngramSpark on cream and white (`Ing-c`, `Ing-w`) and a Lulu hardcover (`Lulu-HC`).

**Example 12.2. Computed spine widths, in inches**

```text
pages  house  KDP   KDP-w   Lulu-PB  Ing-c   Ing-w   Lulu-HC
100    0.25   0.31  0.2852  0.2852   0.2252  0.1953  0.5
200    0.5    0.56  0.5104  0.5105   0.4505  0.3906  0.75
400    1.0    1.06  0.9608  0.9609   0.9009  0.7812  1.1875
```

At 200 pages on cream stock, the KDP spine is more than a tenth of an inch wider than the IngramSpark spine.

### What each provider makes

The providers also differ in what they will make. Table 12.3 gives the bindings, trims, page bounds, and hardcover figures that the ledger records for each one.[^12-kdpdate]

| Provider | Meaning |
|---------------|-----------------------------------------------------------------|
| `house` | The ledger lists `perfect-bound`, `saddle-stitch`, and `coil`. The house provider keeps no list of trims or page counts, so it refuses none. |
| `kdp` | KDP makes `perfect-bound` from 24 to 828 pages and `casewrap` from 75 to 550 pages, on six trims from 5 by 8 (paperback only) to 8.25 by 11. Its casewrap takes a margin of 0.5906in (a "15mm wrap") and a hinge of 0.3937in (a "10mm hinge"). It makes no dust jacket, linen, saddle-stitch, or coil binding. |
| `lulu` | Lulu makes `perfect-bound` (32 to 800 pages), `saddle-stitch` (4 to 88), `coil` (2 to 470), and hardcovers (24 to 800), on 13 trims from Pocketbook 4.25 by 6.875 to US Letter 8.5 by 11. Its casewrap takes a margin of 0.75in and a hinge of 0.25in. Its dust jacket takes a flap of 3.25in and a strip of 0.25in. |
| `ingramspark` | IngramSpark makes `perfect-bound` from 18 to 1200 pages and hardcovers from 18 to 1050, as `casewrap` or `dust-jacket`, on nine trims. Its casewrap takes a margin of 0.625in and a hinge of 0.5in. |

Table: Table 12.3. What each provider makes

The ledger marks Lulu's two dust-jacket figures UNCONFIRMED, and it marks IngramSpark's casewrap formula "OFFICIAL".[^12-ingram] An unconfirmed figure is the press's best reading of the shop's guide. If your book uses one, order a proof before you trust the jacket.

### Paper and the Lulu paperback

The paper setting matters for two of the four shapes. The `constant` shape and the `ppi-table` shape both read `print.paper`, so a white book and a cream book get different spines at KDP, at IngramSpark, and on the house provider. The key takes `white` or `cream`, and the default is `cream`:

```text
$ press config set print.paper white
```

The `divisor` shape does not read the paper. A Lulu paperback of 200 pages has a spine of 0.5105in on either stock. The Lulu guide in the press documentation tells you to set the paper first so that the spine math is right. That advice applies only when the provider reads the paper, and the default provider is `house`, not `lulu`. For a Lulu paperback, you should therefore set `print.provider` to `lulu`. The guide does not say so.

::: {.tip}
> **Tip:** Set `print.provider` to the shop that will print the book before you design the cover. The house numbers fit no real shop, and the spine you design against is the spine the provider computes.
:::

## Building the interior

The print interior and the Print edition come from the same manuscript, but they are different artifacts. The Print edition, *dist/alice.pdf*, is for reading. The print interior, *dist/alice-interior.pdf*, is for a printing press. It is set two-sided, with mirrored margins. It prints in a single ink unless the profile says `color`. Its images come from the print-safe copies in *build/print-assets/*, which the section "Print-safe images" later in this chapter describes.

`press print` builds the interior and nothing else. Pandoc and latexmk set it with the `print.yaml` defaults, two-sided, with the print-safe filter added to the chain. Run it when you want to look at the interior before any verifier reads it, for example after you move a figure. The target writes *dist/alice-interior.pdf*. It runs no verifier, so treat that file as a draft.

The `print.yaml` defaults carry one scar of their own. A two-sided KOMA document must spell "open chapters on any page" as `open=any`. The standard-class spelling `openany` "is silently ignored under twoside", and `open=right` would leave a blank verso after every chapter that ends on a recto. The defaults use the KOMA spelling.

`press verify-print` is the target you upload from. It builds the interior, runs the print verifier on it, and then builds and verifies the cover wrap, because the Alice book has *assets/cover.jpg*. Without a cover, the target prints `no assets/cover.jpg; interior verified, wrap not built` and stops there. Chapter 8, *Verifying the artifacts*, gives the checks of the print verifier in full.

`press all` builds neither the print interior nor the cover wrap. It builds and verifies every edition a reader downloads. The print pack has its own targets. The one exception is the *commerce gate*, the last step of `press all`, which guards print ordering. In a book that enables print ordering, that gate builds the interior and the wrap, as the section "Ordering a copy" later in this chapter explains.

::: {.tip}
> **Tip:** Run `press verify-print` before every upload to a print shop.
:::

The print verifier fails a single-ink interior that carries color. One source of color is code. A code block with a language tag gets syntax highlighting, and the highlighting prints in colored ink. The verifier then fails the whole interior with `print profile: colored ink on pages [N]`. Tag the block `text` instead, as Chapter 4, *Writing the manuscript*, advises. Another source is a colored cover plate in a hand-written *tex/title-page.tex*. That plate belongs on the wrap, and you can supply *tex/title-page-print.tex* without it for the print interior.

## The cover wrap

`press coverwrap` builds the cover wrap, *dist/alice-coverwrap.pdf*. It builds the `print` target first, because the spine depends on the page count. The press reads that count from the finished interior with pypdf, so the spine always matches the pages you actually have.

The wrap needs more from the book than the interior. It needs the cover art at *assets/cover.jpg*, and without it the press refuses the target with `coverwrap needs assets/cover.jpg`. It needs the title, the author, the publisher, and the place of publication from the metadata. With those in place, the press lays out the page and sets it with LuaLaTeX.

### The layout

Four print terms name the edges of the wrap. The *trim* is the line where the shop cuts the cover to size. The *bleed* is the band of art that runs past the trim, so that the cut leaves no white sliver at the edge. The press fixes the bleed at `BLEED_IN = 0.125`, which the source calls "universal across print vendors", and every provider in the ledger declares the same 0.125in.

The *safety* is a line inside the trim that a shop asks you to keep type within. The ledger records 0.25in for KDP and IngramSpark and 0.5in for Lulu, and none for the house provider. The press does not draw or check a safety line, so keeping the type inside it is your job.

The wrap runs left to right in seven bands: a margin, an inner offset, the back panel, the spine, the front panel, a second inner offset, and a second margin. Example 12.3 gives the arithmetic that places them.

**Example 12.3. The cover wrap layout, from `gen_coverwrap`**

```text
panel_w = trim_w + width_delta
wrap_w = 2 * margin + 2 * inner + 2 * panel_w + spine
wrap_h = 2 * margin + trim_h + height_delta
back_x = margin + inner
front_x = back_x + panel_w + spine
```

The *inner offset* is the sum of the binding's own extra widths: `inner = hinge + flap + strip`. The flap folds inside the board of a dust jacket, and the strip is the narrow band that joins it to the panel. A paperback has none of the three, so its inner offset is zero. The margin of a paperback is the bleed. A casewrap takes its margin, the turn-in, from the provider.

The two deltas adjust a panel from the trim to the board or jacket size, and the provider's spec sets them. For the house and KDP soft covers, both are zero. For a hardcover, they depend on the provider. The Lulu casewrap in Table 12.4 comes out 0.25in taller and 0.25in wider than its margins, hinges, trim, and spine alone give, and that difference is the two deltas. IngramSpark sets deltas of its own: 0.4375in wide and 0.25in high for its dust jacket, and -0.185in wide for its casewrap. A negative delta is why the IngramSpark casewrap comes out narrower than the same sum.

@fig:cover-wrap-anatomy draws the house example: a 6 by 9 perfect-bound book of 200 pages on cream stock. The panel is the 6-inch trim. The spine is 200 pages times 0.0025in, or 0.5in. The width is 2 times 0.125, plus 2 times 6, plus 0.5, which is 12.75in. The height is 2 times 0.125 plus 9, or 9.25in.

![The cover wrap of a house perfect-bound 6 by 9 book of 200 pages](assets/woodcuts/12-02-cover-wrap-anatomy.png){#fig:cover-wrap-anatomy .diagram width=full-measure fig-alt="A wide rectangle divided into a back panel, a narrow spine, and a front panel, with a thin bleed band around the outside and a barcode box near the lower right of the back panel. Dimension lines outside the rectangle give each width and height in inches."}

<!-- art: ARCHETYPE page anatomy, to scale, landscape. One outlined rectangle 12.75 by 9.25 units: "back" panel (6in), a 20% gray "spine" strip (0.5in), "front" panel (6in). A 10% gray outer band for the bleed, a solid trim line inside it. No safety line. Every spine and bleed label sits outside the rectangle on a thin leader. Above: "back 6in", "front 6in", and a staggered second row "spine = 200 x 0.0025 = 0.5in". Across the top: "wrap_w = 12.75in". At right: "wrap_h = 9.25in". Left: "bleed 0.125in", "trim". Lower right of the back panel, a white box labelled inside "EAN-13", with callouts "0.5in from spine fold" and "0.5in up". The reader sees first how narrow the spine is. -->

Table 12.4 gives the wrap for the same book, 6 by 9 with 200 pages on cream stock, under other providers and bindings.

| Provider and binding | Spine (in) | Meaning |
|-------------------------|------------|-------------------------------------------------------|
| `house`, perfect-bound | 0.5 | The wrap is 12.75 by 9.25 inches. |
| `kdp`, perfect-bound | 0.56 | The wrap is 12.81 by 9.25 inches. |
| `lulu`, perfect-bound | 0.5105 | The wrap is 12.7605 by 9.25 inches. |
| `lulu`, casewrap | 0.75 | The wrap is 15.0 by 10.75 inches. The margin adds to both the width and the height, and the hinge adds to the width. |
| `lulu`, dust-jacket | 0.75 | The wrap is 20.0 by 9.25 inches, because the two flaps and their strips add 7 inches to the width. |
| `ingramspark`, casewrap | 0.4505 | The wrap is 14.3305 by 10.5 inches. |
| `house`, saddle-stitch | 0 | The wrap is 12.25 by 9.25 inches, because the book has no spine. |

Table: Table 12.4. One book's cover wrap under seven settings

### What goes on the wrap

The cover art fills the front panel at the full height of the wrap, from bleed to bleed. On a soft cover it also runs out through the bleed on the outer edge, so for the house example *assets/cover.jpg* fills 6.125 by 9.25 inches. On a hardcover or a jacket, with a hinge or a flap beside the panel, the art keeps to the panel width alone. The wrap verifier looks for the art on the front panel and fails a wrap whose front panel is nearly flat.

The press sets its own type on the back panel, and it puts the logomark there at 1.1in wide. The barcode sits at the lower right of the same panel. Any lettering on the front, the title included, belongs in *assets/cover.jpg* itself. On a printed cover, the press lays down a cloth-colored field, RGB (201,191,191), and for a `linen` cover it drops that field, since the cloth is real. The press draws spine text only when the spine is at least 0.25in wide. Chapter 11, *The art department*, covers the making of the cover art itself.

The press compiles the wrap with `latexmk -lualatex` in *build/coverwrap*. When LuaLaTeX finishes, the press checks the page's mediabox against the computed layout within 0.01in.

## The barcode

A cover with an ISBN carries the number as an EAN-13 barcode, and the press draws the bars itself. You set the number as `registrations.isbn.print`, which Chapter 13, *Registrations*, covers. The barcode sits at the lower right of the back panel, on a white card. The press anchors the card by its south-east corner, 0.5in in from the spine fold and 0.5in up.

The bars follow the standard size. One *module*, the narrowest bar or space, is 0.0130in wide, from the rule that "100% EAN magnification is 0.33mm". An EAN-13 has 95 modules, so the barcode comes to about 1.235in across. The bars are 0.9in tall.

### The check digit

The thirteenth digit of an ISBN is a check digit. The press computes it from the first twelve digits. It weights them 1, 3, 1, 3, and so on from the left, sums the products, and takes `(10 - total % 10) % 10`. Example 12.4 works the ISBN that the press's selftest checks, 978-0-306-40615-7, through the formula.

**Example 12.4. The check digit of 978-0-306-40615-7**

```text
digits   9  7  8  0  3  0  6  4  0  6  1  5
weights  1  3  1  3  1  3  1  3  1  3  1  3
product  9 21  8  0  3  0  6 12  0 18  1 15
total    93
check    (10 - 93 % 10) % 10 = 7
```

The press then draws the bars from the fixed 95-module pattern that the EAN-13 standard defines. If the check digit does not match, the press refuses the ISBN, because "a mistyped ISBN on a cover is unrecoverable". The check digit catches most typing errors. It does not catch a valid number that belongs to some other book.

::: {.warning}
> **Warning:** Read the ISBN on the proof against your registration record before you approve a printing. The check digit shows only that the number is well formed, and nobody can correct a cover printed with the wrong book's ISBN.
:::

### The placeholder that says pending

A book with no ISBN yet still gets a wrap. In place of the bars, the press draws a white box 2in wide and 1.2in tall that reads `[ISBN pending]`. It holds the space that the barcode will need, and nobody can mistake it for a real number.

::: {.sidebar}
> **The barcode that crowded its quiet zone**
>
> An EAN-13 needs a *quiet zone*, blank space on either side of the bars, before a scanner will read it. The press draws its barcode as a TikZ node, and a TikZ node puts a little padding around its contents unless you tell it otherwise.
>
> In the releases before 2.3.1, that default padding shifted the bars, and the first guard bar crossed into the left quiet zone. The barcode was correct, but it no longer stood where it should. The wrap verifier measured the quiet zones and failed the wrap, so `press verify-print` failed on a correct cover. The verifier was right about the pixels. The fix, in 2.3.1 (#210), was `inner sep=0` on the node, which removes the padding. The verifier still measures both quiet zones on every wrap with an ISBN, so the padding cannot come back without a red build.
:::

## Print-safe images

A provider runs a *preflight* over every file it receives. The preflight flags two things that the reading editions do not care about: transparency, and more pixels than the page can use. The press therefore passes each interior image, from the directories Chapter 5 names, through a *print-safe* pass before the image goes onto paper. The pass flattens each image onto white and caps its resolution. Chapter 5, *Figures, plates, and illustrations*, describes the pass for the interior. The cover goes through the same pass, with its own caps.

For the interior, the pass caps the logomark at 1000 pixels on its long edge and each figure and plate at 1900 pixels, which is about 300 PPI at 6.3 inches. It keeps a grayscale image grayscale. It writes a JPEG source as a JPEG at quality 88, and every other image as a PNG. The results go to *build/print-assets/*, and the Lua filter *print-safe-images.lua* points the interior's image paths there. Your masters in *assets/* never change.

For the cover, `print_safe.prepare_cover` does the same work into *build/coverwrap-assets/*. It caps the cover art at 590 pixels for every inch of the wrap's height, `590 x wrap_h` pixels, and the logomark at 649 pixels. The logomark prints 1.1in wide, so 649 pixels comes to 590 PPI. Both caps sit under the 600 PPI line that the wrap verifier enforces.

The caps exist because of a preflight report. Lulu once flagged a press interior for transparency, since the logomark is ink on transparency. It also flagged an image over 600 PPI: a 1024-pixel logomark printed 1.7in wide comes to about 602 PPI. *docs/LULU.md* now reports that "a current `press verify-print` interior triggers **neither** warning".

::: {.tip}
> **Tip:** If your book supplies *tex/title-page-print.tex*, point its logomark at *build/print-assets/*. The filter `print-safe-images.lua` points the manuscript's images there, and a hand-written TeX file names its own paths.
:::

## Verifying the print pack

@fig:print-pack-graph shows the print pack from the print profile to the commerce gate. The interior and the wrap each pass through their verifier before anything downstream reads them. `press publish` branches off after the wrap verifier. The commerce gate builds the interior and the wrap itself, computes the *edition manifest*, the JSON file the gate writes with the production facts and their hash, and then looks for a qualification.

![The print pack, from the profile to the commerce gate](assets/woodcuts/12-03-print-pack-graph.png){#fig:print-pack-graph .diagram width=full-measure fig-alt="A left-to-right chain of rounded boxes from the print profile and print-safe assets through the print interior, its verifier, the cover wrap generator, and the wrap verifier to the edition manifest, qualification, and the commerce gate. A side branch leads from the wrap verifier to the publish checklist."}

<!-- art: ARCHETYPE pipeline, left to right, wrapping to a second row after the fourth box. Far left, two dog-eared file icons stacked: "print profile" and "build/print-assets/". Arrow to rounded box "print interior", file icon "dist/alice-interior.pdf" under it. Arrow to rounded box "verify_pdf --profile print". Arrow to rounded box "gen_coverwrap", file icon "dist/alice-coverwrap.pdf" under it, a thin input line from "assets/cover.jpg". Arrow to rounded box "verify_coverwrap". From it, a side branch going down to rounded box "press publish" with file icon "dist/publish-kdp.md". Second row, main chain: box "edition manifest", labelled "edition_id"; arrow to box "qualification", file icon "config/qualification.yaml"; arrow to a drop-shadowed box "commerce gate". The reader sees first that the commerce gate comes last and that press publish is a side branch. -->

The interior goes through `verify_pdf` with the print profile, which Chapter 8 describes. The wrap goes through `verify_coverwrap`, which runs ten checks in the order Table 12.5 gives.

| Check | Meaning |
|----------------------|-------------------------------------------------------------|
| One page | The wrap must be a single page. |
| Size | The page must equal the generator's own layout for this page count within 0.01in either way. |
| Fonts | Every font must be embedded. |
| Transparency | No image may carry a soft mask (`/SMask`). |
| Resolution | No image may exceed 600 PPI, as `pdfimages` reports it. |
| Title | The title must survive as extractable text. |
| Not blank | A render at 150dpi with `pdftoppm` must show something. |
| Front art | The front panel's pixels must have a standard deviation of at least 8. |
| Barcode card | The barcode area must hold a white card (some pixel above 245) and marks (some pixel below 70). |
| Bars | With an ISBN, the scanline must cross at least 25 transitions and find both quiet zones blank. |

Table: Table 12.5. The `verify_coverwrap` checks, in order

The size check compares the wrap with the arithmetic that built it, so the generator and the verifier cannot disagree about the spine. The transparency message names the reason for the rule: "coverwrap embeds N image(s) with transparency (a soft mask); a print preflight flags it...". If the front panel has almost no variation, the verifier says that "the cover art did not survive". An EAN-13 has 59 transitions across its bars, and the check asks for at least 25. `verify_coverwrap` reports each fault by name, so the message tells you which check to look at.

When every check passes, the verifier prints one line. Example 12.5 gives its form, broken here across lines to fit the page. The last clause reads one way for a wrap with an ISBN and the other way for a placeholder.

**Example 12.5. The `verify_coverwrap` success line**

```text
Verified <wrap>: one page, W x H in (N-page spine),
embedded fonts, no transparency, images under 600 PPI,
front art present, title survives, barcode: EAN-13
readable with quiet zones | honest placeholder present
```

## Qualification and the golden copy

A verified PDF tells you that the files are right. It cannot tell you that the shop prints them right. The press keeps that second question apart from the first. Its *docs/PROVIDER-QUALIFICATION.md* begins with a plain statement: "A provider here is *researched*, not *qualified*."

### The researched providers

The ledger keeps a second list of shops, the candidates for print ordering. It is separate from the four values of `print.provider`, and you cannot set `print.provider` to a name that appears only here. The ledger gives each researched shop a *disposition*, one of `primary`, `secondary`, `hosted-candidate`, `candidate`, or `not-fit`, and it scores each one on 11 capabilities, such as `api` and `one_copy_pod`. Table 12.6 gives the dispositions.

| Provider | Meaning |
|--------------------|-------------------------------------------------------------------|
| lulu | Lulu is the `primary` provider. |
| bookvault | Bookvault is the `secondary` provider. |
| peecho | Peecho is a `hosted-candidate`, and it is the only provider that the ledger marks `supported` for `seller_of_record`. |
| mixam, cloudprinter, prodigi | Each of these is a `candidate`. |
| onpress, print-bind-ship | Each of these is `not-fit`. |
| 48-hour-books | It is `not-fit`, because it has a 10-copy minimum. |

Table: Table 12.6. The researched providers and their dispositions

One capability, `seller_of_record`, matters for the last section of this chapter. The ledger records Lulu as `unsupported` for it, with the note that "the publisher is the seller in the custom route".

### The eleven points

*Qualification* means one physical copy in your hands, inspected against a fixed list. The press calls that copy the *golden copy*: the first copy of an exact edition, ordered from the shop and checked point by point. Table 12.7 gives the list as the press states it.

| Point | Meaning |
|---------------|-------------------------------------------------------------------|
| content | the interior text matches the release-approved manuscript |
| pagination | page count and page order match the manifest |
| trim | the cut size matches the declared trim within tolerance |
| bleed | full-bleed art reaches the trimmed edge without white slivers |
| spine | spine text is centred and square for the page count |
| barcode | the EAN-13 scans and matches the declared ISBN |
| color | single-ink interior and cover reproduce as specified |
| paper | stock weight and shade match the declared paper |
| binding | the binding is square, tight, and opens flat enough to read |
| packaging | the copy arrives undamaged and appropriately protected |
| tracking | the tracking link resolves and matches the destination |

Table: Table 12.7. The eleven-point physical checklist, verbatim

Every point must pass. "A single failure does not qualify." You record the inspection by hand in *config/qualification.yaml*. A comment in the metadata template mentions a `press qualify` command, but no such command exists. Example 12.6 shows the record for a Lulu paperback of the Alice book, with the results set out one to a line. The `product_id` is the shop's own name for the product you ordered.

**Example 12.6. A passed inspection in *config/qualification.yaml***

```text
schema_version: 1
inspections:
  - provider: lulu
    product_id: "PB-BW-6x9"
    region: US
    edition_id: "<the edition_id of the copy>"
    inspector: "alice"
    results:
      content: pass
      pagination: pass
      trim: pass
      bleed: pass
      spine: pass
      barcode: pass
      color: pass
      paper: pass
      binding: pass
      packaging: pass
      tracking: pass
```

### Edition identity

An inspection holds for one exact edition, named by its `edition_id`. You do not choose the id. The press computes it, and the commerce gate computes it each time it builds the edition manifest. The press shows only the first twelve characters of the id: the gate prints `edition <first 12 characters> (<edition>)`, and `python3 -m press.edition verify` prints `identity` followed by the same twelve. The full value lives in the manifest file that the gate writes, and that is where you copy it from for the record. The id is a sha256 hash over the production facts only: the interior bytes, the cover bytes, the print spec, the ISBN, and the toolchain digest. The source commit, the state of the tree, the receipts, and the qualifications themselves stay out of the hash.

The choice of inputs decides when an inspection stops holding. A new commit that changes no printed byte keeps the same id, so the old inspection still applies. A change to the manuscript, the cover, or the print spec mints a new id. You then order and inspect a new copy. The manifest itself must not carry money or personal details, and the press forbids keys such as `price` and `email` anywhere in it. To check a manifest file, run `python3 -m press.edition verify <manifest.json> [<book-root>]`.

## Publish checklists

KDP and IngramSpark each want the same files in their own forms, plus a set of answers that only you can give. For both shops, the press's route is `press publish`. It builds and verifies the files and writes a checklist, and you do the uploads and the account work at the shop. The synopsis is:

```text
press publish kdp|ingram [--report-only]
```

The target rebuilds and verifies four artifacts. It then writes the checklist to *dist/publish-kdp.md* or *dist/publish-ingram.md*. Table 12.8 shows the checklist's shape, its three sections in order.

| Section | Meaning |
|-----------------------------|-----------------------------------------------------------|
| Files the channel needs | It lists "Print interior PDF (mirrored margins, black ink)", "Cover wrap PDF (trim + bleed, spine computed)", "EPUB (KDP eBook / Ingram ebook program)", and "Marketing cover image (front board only)". |
| Identity the channel will ask for | It gives the print ISBN, the title, the subtitle, the author, the description, and the keywords. |
| Only a person can do these | It lists the work no program can do for you, which Table 12.9 gives for each channel. |

Table: Table 12.8. The three sections of a publish checklist

| Channel | Meaning |
|-----------|-------------------------------------------------------------------|
| `kdp` | "KDP account with tax interview completed"; "Category selections (2 allowed; note 10 keyword slots)"; "Pricing per marketplace and royalty option (60% print)"; "Order a physical proof before approving publication". |
| `ingram` | "IngramSpark account and title setup fee"; "BISAC subject codes (3 allowed)"; "Wholesale discount and returns policy decisions"; "Order a physical proof before enabling distribution". |

Table: Table 12.9. The items only a person can do, by channel

If any artifact fails its verifier, the target exits with status 1. With `--report-only`, it writes the checklist and marks each file "present but NOT verified (report-only)". The option suits a first look at what a channel will ask. Run the full target before an upload.

## Ordering a copy

A press book meets two kinds of order. You order one golden copy for yourself, to qualify the edition. Later, if you choose, your readers order copies through a link on the book's landing page.

### Printing at Lulu

*docs/LULU.md* gives the procedure for a Lulu paperback. It is the route to the golden copy. Set `print.provider` to `lulu` first, as the tip in "Paper and the Lulu paperback" advises. For a hardcover, also set `print.binding` to `casewrap` or `dust-jacket`.

::: {.warning}
> **Warning:** Do not let Lulu add its own barcode to a cover that already carries one. The press draws the EAN-13 from `registrations.isbn.print`, and a second barcode on the back panel is a defect on every copy.
:::

To print the Alice book at Lulu:

1. Build and verify the print pack with `press verify-print`. The target writes *dist/alice-interior.pdf* and, from *assets/cover.jpg*, *dist/alice-coverwrap.pdf* with 0.125in bleed.
2. At Lulu, choose **Print Your Book**, then the product **Paperback, Perfect Bound**.
3. Match Lulu's settings to the book's, as Table 12.10 gives them.
4. Upload the interior, then the one-piece cover PDF.
5. If you set `registrations.isbn.print`, leave Lulu's own barcode off.
6. Order one copy and inspect it against the eleven points.
7. Record the result in *config/qualification.yaml*.

| Lulu setting | Meaning |
|------------------------|-------------------------------------------------------|
| Page size or trim | Set it to the trim of your `print.profile`. |
| Binding | Set it to match `print.binding`. |
| Interior color | Set it to **Black and white**. |
| Paper | Set it to match `print.paper`. |
| Cover finish | Choose **Glossy** or **Matte**, as you prefer. |

Table: Table 12.10. Lulu's settings for a press book

Lulu may report that "a white bleed margin was added". You can ignore that note. Table 12.11 gives the other problems the guide lists, with their fixes.

| Problem | Meaning |
|------------------------|-------------------------------------------------------|
| Cover is the wrong size | The Lulu product does not match your `print.binding`. Match the binding, or set `print.binding`, and rebuild. |
| Transparency detected | The upload is an old one, from before the print-safe pass flattened images. Rebuild with `press verify-print` and upload again. |
| Images over 600 PPI | The upload is an old one, from before the print-safe pass capped resolution. Rebuild with `press verify-print` and upload again. |
| No cover was built | The book has no *assets/cover.jpg*. Add the cover art, then run `press coverwrap`. |
| Fonts not embedded | The file did not come from a press build. Rebuild with `press verify-print`. |

Table: Table 12.11. Lulu troubleshooting

The guide also lists an off-center spine and gives the cause as a Lulu stock that does not match your `print.paper`. That cause applies to a provider that reads the paper. For a Lulu paperback with `print.provider` set to `lulu`, the press computes the same spine on either stock. Check the provider setting before you check the paper.

### Print ordering for readers

The press can put an "Order a print copy" link on the book's landing page. It is off by default. You turn it on with a `commerce` block in *config/metadata.yaml*, which Example 12.7 shows for the Alice book. The `storefront-url` is the shop's page for the published title. The policy texts are your own words, which the press appends to the pages it generates.

**Example 12.7. Print ordering for the Alice paperback**

```text
commerce:
  print-ordering:
    enabled: true
    edition: paperback
    storefront-url: "https://www.lulu.com/shop/..."
    seller-of-record: "<the seller you have confirmed>"
    # optional; omit to generate
    support-url: "https://example.test/support"
    policies:
      privacy: >-
        We keep no reader data; the provider handles
        your order.
```

The `seller-of-record` value names who the reader buys from, and only you can establish it. The press's model is that the provider sells the copy, and the documentation's own sample writes `"Lulu"` in this field. The ledger, the reviewed source, records Lulu as `unsupported` for `seller_of_record`. Whether a provider is legally the seller is a question for you and the provider's own terms, so confirm it before you publish the link.

The landing page then shows an accessible, script-free `<aside class="print-order">` headed "Order a print copy". The link carries `rel="noopener noreferrer"`. Before the reader leaves the page, the aside names the seller. For each policy URL you leave out, the press generates a page, *support.html*, *privacy.html*, or *refunds.html*, that discloses the seller. The documentation is firm about the limit: "press never invents legal terms."

`press check` refuses the block in each of these cases:

- a URL that is not HTTPS
- a key the press does not know
- a value shaped like a secret, such as `sk_live`, `bearer` followed by 16 or more characters, or `?token=`
- an unnamed seller, because "a hosted checkout does not imply who the legal seller is"

`press all` ends with the commerce gate. In a book with print ordering on, the gate builds `print` and `coverwrap`, computes the edition manifest, and looks for a passed inspection of that `edition_id`. Without one, it fails with "order and inspect a copy and record it in config/qualification.yaml before advertising ordering". The gate is advisory unless the environment sets `PRESS_RELEASE=1`, as CI does when it builds a release tag.

The press stops at the link. It does not "process or store payment, calculate tax, hold provider credentials, receive a reader's name or address, or operate a store." A checkout of the press's own sits in the roadmap's Icebox, its list of deferred work.[^12-adapter] The barcode, the checklist, and the manifest all carry the ISBN from your registrations. Chapter 13, *Registrations*, covers that paperwork.

[^12-allowance]: The comment beside the house allowance in the provider ledger reads "v1 value; real specs use 0.06".
[^12-ingram]: The ledger notes that "Ingram is the one vendor whose casewrap and jacket TOTAL formulas are officially published".
[^12-kdpdate]: At the time of this writing, the ledger records the KDP spec as verified on 2026-07-21. Provider specifications change, and the ledger date tells you how old the numbers are.
[^12-adapter]: The press repository does contain a provider-neutral order contract and an adapter for Lulu's Print API, under *src/press/providers/*. The adapter defaults to Lulu's sandbox, and at the time of this writing only the tests reach it. No command uses it.
