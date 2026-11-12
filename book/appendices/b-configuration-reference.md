# Appendix B: Configuration reference {.unnumbered}

This appendix lists every configuration key a book repository can hold, file by file. The files live in *config/*, and the press requires only *config/metadata.yaml*. What `press config list` prints decides each key's type and purpose. Where the press documentation and the code disagree, the entry follows the code and says so.

Each entry gives the key, its type, its default, what it does, and the chapter that explains it. Dots join a nested key, so `print.profile` is the `profile` key inside the `print:` mapping. The types are the ones `press config list` prints: `str`, `int`, `float`, `bool`, `list[str]`, and `mapping`. The default applies when the key is absent. Where `press new` writes a different value, the entry gives both.

You can read and write most keys with `press config get`, `set`, `unset`, `list`, and `validate`, as Chapter 3, *The shape of a book repository*, describes. A list or a mapping needs the `--json` option. A boolean accepts `true`, `yes`, `on`, or `1`, and `false`, `no`, `off`, or `0`. The `--dry-run` option prints the diff and then `(dry run: nothing written)`. Neither option appears in `--help`.

Before `press config set` writes a byte, it checks the new value with the typed model that a build uses. No typed model checks *config/aesthetic.yaml*. After a hand edit, run `press config validate`, which reports an absent file as `ok`.

Every field in `press config list` has one of four kinds. A *writable* field takes `set` and `unset`. The one *immutable* field, `trim`, refuses writes and names the field to change instead. A *structured* field holds data too rich for one command line, such as the index terms. A *file* field is a whole file, such as *tex/title-page.tex*.

The two style libraries at the end of this appendix are not in `press config list`. You edit them by hand.

Table B.1 maps each file to the chapter that treats it at length.

| File | Chapter |
|------------------------------|------------------------------------------------|
| *config/metadata.yaml* | 3, *The shape of a book repository*, with 4, 8, 12, and 13 for its groups |
| *config/front-matter.yaml* | 10, *Front matter, the index, and the table of authorities* |
| *config/house-rules.yaml* | 6, *Checking the manuscript* |
| *config/aesthetic.yaml* | 9, *The house design*, and 11, *The art department* |
| *config/index-terms.yaml* | 10, *Front matter, the index, and the table of authorities* |
| *config/authorities.yaml* | 10, *Front matter, the index, and the table of authorities* |
| *config/cover-styles.yaml* | 11, *The art department* |
| *config/illustration-styles.yaml* | 11, *The art department* |

Table: Table B.1. The configuration files and the chapters that explain them

## *config/metadata.yaml* {-}

The metadata file holds the book's identity, the press facts, the verification knobs, and four groups of nested keys: `print`, `chapter-opening`, `registrations`, and `commerce`. The typed model requires `title`, `author`, and `slug`. The checker also refuses a book without `description`, with the message `metadata missing <key>:`. Pandoc reads the same file, so a standard pandoc key passes through.

### Identity {-}

**`title`**
: Type `str`, required. The book's title. The generated title page sets it in capitals and adds a period unless the title already ends in a period, an exclamation mark, or a question mark. See Chapter 3.

**`subtitle`**
: Type `str`, default none. The subtitle. If you write it as clauses joined by "or," (for example `"OR, ...; OR, ..."`), it stacks on the title page, one clause to a line. It also stacks on the landing page. The scaffold writes `"A subtitle"`. See Chapters 3 and 10.

**`author`**
: Type `list[str]`, required. The byline, one name per list item. The model also accepts a single string and makes it a list of one. The scaffold writes the name given to `press new --author`, else the name in `git config user.name`, else "The Author". See Chapter 3.

**`date`**
: Type `str`, default none. Free text. The press takes the first four-digit year in it that begins with 1 or 2. It uses that year for the EPUB date and for the lowercase roman numerals on the title page. Unless you set `edition-note`, the colophon's edition line comes from the text before the first comma, lowercased. The scaffold writes `"First edition, 2026"`. See Chapters 3 and 10.

**`copyright`**
: Type `str`, default none. The copyright line. The press requires it once *config/front-matter.yaml* exists. The scaffold writes `"Copyright 2026."`. See Chapter 10.

**`publisher`**
: Type `str`, default none. The imprint, required with front matter. The press also exports it to TeX as the environment variable `BOOK_PUBLISHER`, which the plain title page reads when the press generates no front matter. The cover prompt's `{imprint}` field comes from this key. The scaffold writes the author's name, or the value of `press new --publisher`. See Chapter 10.

**`publisher-place`**
: Type `str`, default none. The imprint's place, required with front matter. The title page sets it lowercased. The scaffold writes `"Earth"`, or the value of `press new --place`. See Chapter 10.

**`description`**
: Type `str`, default none, required by `press check`. A one-sentence blurb for the landing page and the stores. `press cover` uses it as the subject when neither `--subject` nor `cover.subject` names one. See Chapter 3.

**`keywords`**
: Type `list[str]`, default none. Subject keywords, passed to the editions. The scaffold writes one keyword, `writing`. See Chapter 3.

**`lang`**
: Type `str`, default none. A BCP-47 language tag, passed through to pandoc. The scaffold writes `en-US`. See Chapter 3.

**`rights`**
: Type `str`, default none. A rights statement, passed through to pandoc. It is a separate key from the colophon's `rights-notice` in *config/front-matter.yaml*. See Chapter 3.

### Press facts {-}

**`slug`**
: Type `str`, required. The basename of every artifact, so the PDF is `dist/<slug>.pdf` and the sources companion is `dist/<slug>-sources.md`. It must match `[a-z0-9][a-z0-9-]*`: a lowercase letter or digit, then lowercase letters, digits, and hyphens. The scaffold writes the directory name given to `press new`. See Chapter 3.

**`repository`**
: Type `str`, default none. The URL of the book's own repository. When the key is absent, the landing page leaves out its paragraph about the source. The scaffold writes it only when `press new` has `--owner`, and otherwise leaves it as a comment with `OWNER` in the URL. See Chapter 3.

**`site-url`**
: Type `str`, default none. The public URL of the book's Pages site. It is the one source for every absolute URL the press writes: the canonical link, the `og:image` link, and the sitemap. When it is absent, the press writes nothing that needs an absolute URL. The scaffold treats it as it treats `repository`. See Chapters 3 and 9.

### Verification knobs {-}

**`verify-sentinels`**
: Type `list[str]`, default `[]`. The sentinels: phrases that must appear in the manuscript and in every edition. Case must match, and curly and straight quotes count as equal. Pick two to four distinctive phrases from the middle of a chapter. A chapter opening (any `chapter-opening.style` other than `none`) splits a chapter's first word and sets it in small caps, which breaks an exact match in the Print edition (the PDF). A phrase missing from the manuscript stops `press check` with `sentinel not found in the manuscript: <s>`. A release needs at least two. See Chapters 3, 6, and 8.

**`verify-min-pages`**
: Type `int`, default `40`. The page floor: the smallest page count the PDF verifier accepts. The press documentation also gives 40. The scaffold writes `1`, so a new book's floor is 1 until you raise it. A release needs at least 24. See Chapters 3, 6, and 8.

**`trim`**
: Immutable. The page trim, which the profile supplies. `press config list` says "trim is not set directly; choose it with print.profile". The press compares a legacy `trim:` mapping with the profile's trim and refuses the book if the two disagree. See Chapter 12.

Under `PRESS_RELEASE=1`, which CI sets on a tag that begins with `v`, the press refuses sentinels and a page floor that are too weak. Its message names "vacuous witnesses" and states both floors, as Example B.1 shows.

**Example B.1. The release refusal of weak sentinels and a weak page floor**

```text
this is a release build (PRESS_RELEASE=1) and its ...
verify-sentinels has N entries; a release needs at least 2 ...
verify-min-pages is N; a release needs at least 24
```

The first line ends "its witnesses are vacuous:", and the second ends "distinctive prose fragments".

### The print group {-}

The `print` keys choose the print interior and the cover wrap. The profile, the binding, the material, and the provider are independent choices. `press check` refuses a trim, binding, or ink that the provider does not offer, so the refusal comes before any build. Chapter 12, *The print pack*, explains the whole group.

**`print.profile`**
: Type `str`, default `house-6x9`. The design profile, which seals the trim and the interior geometry. The six house profiles are `house-6x9`, `house-6x9-color`, `novella-5x8`, `digest-5.5x8.5`, `mass-market-4.25x6.87`, and `large-print-7x10`. The press refuses an unknown id with `unknown print profile '<id>'; available: ...`. See Chapters 9 and 12.

**`print.provider`**
: Type `str`, default `house`. The provider whose numbers decide the spine, the bleed, and the cover wrap: `house`, `kdp`, `lulu`, or `ingramspark`. The `house` numbers are KDP-like page calipers with no spine allowance, the press's v1 values. Before you design the cover, set this key to the shop that will print the book. For a Lulu paperback, set it to `lulu`. See Chapter 12.

**`print.binding`**
: Type `str`, default `perfect-bound`. The binding style, one of `perfect-bound`, `saddle-stitch`, `coil`, `casewrap`, or `dust-jacket`. It decides the cover's shape: a spine for `perfect-bound`, no spine for `saddle-stitch` and `coil`, a printed board with turn-in and hinge for `casewrap`, and flaps for `dust-jacket`. See Chapter 12.

**`print.material`**
: Type `str`, default `paperback`. The cover material, one of `paperback`, `casewrap`, or `linen`. `paperback` and `casewrap` are printed covers. With `linen`, the press prints only the jacket and suppresses the printed field. It never prints a simulated cloth texture. See Chapter 12.

**`print.paper`**
: Type `str`, default `cream`. The interior stock, `white` or `cream`. The `house`, `kdp`, and `ingramspark` providers read it for the spine width. Lulu computes its paperback spine from the page count alone. See Chapter 12.

**`print.page-thickness`**
: Type `float`, default none. Inches per page. When you set it, the press uses it in place of the paper's thickness, except for a Lulu hardcover, whose spine comes from Lulu's table of page-count bands. See Chapter 12.

**`print.color-grade`**
: Type `str`, default `standard-color`. The stock grade for a color interior, `standard-color` or `premium-color`. Only the `house-6x9-color` profile reads it. That profile needs a provider with a documented color caliper, which at the time of this writing means `kdp`. See Chapter 12.

### The chapter-opening group {-}

The press merges the book's chapter opening over the design profile's setting. Every house profile sets `none`. Chapter 4, *Writing the manuscript*, explains the opening, and Chapter 9 shows it on the page.

**`chapter-opening.style`**
: Type `str`, default the profile's (`none`). The chapter-opening style: `none`, `drop-cap`, `raised-cap`, or `ornate`. The `ornate` style sets a foliate capital in the Print edition and a styled display capital on the Web and in the Circulating edition (the EPUB). See Chapter 4.

**`chapter-opening.lines`**
: Type `int`, default `3`. The number of text lines the chapter opening spans. See Chapter 4.

**`chapter-opening.small-caps-remainder`**
: Type `bool`, default `true`. Whether the rest of the first word is set in small caps. See Chapter 4.

### The registrations group {-}

The registrations hold the book's numbers. The press never issues a number over the network: you buy it, and the press validates and places it. The value `pending` stands for a number you do not have yet and prints as `[pending]`. Chapter 13, *Registrations*, explains the group.

**`registrations.isbn.print`**
: Type `str`, default none. The print ISBN, 13 digits, or `pending`. The press validates the check digit of a real number. The print ISBN goes into the colophon and becomes the EAN-13 barcode on the cover wrap. See Chapters 12 and 13.

**`registrations.isbn.epub`**
: Type `str`, default none. The EPUB ISBN, or `pending`. It becomes the EPUB's identifier, which the EPUB verifier checks in the package file. See Chapter 13.

**`registrations.lccn`**
: Type `str`, default none. The Library of Congress Control Number, or `pending`. An LCCN has no check digit, so the press checks only its shape. A self-publisher gets one through the Library of Congress's Preassigned Control Number (PCN) program, PrePub Book Link. See Chapter 13.

**`registrations.issn`**
: Type `str`, default none. The ISSN, or `pending`. The press checks its mod-11 check digit, where a check value of 10 is written `X`. See Chapter 13.

**`registrations.retail`**
: Type `bool`, default `false`. When it is `true`, `press check` requires two real ISBNs, `registrations.isbn.print` and `registrations.isbn.epub`. A missing or pending ISBN fails the check with `retail edition declared while registrations are absent or pending: ...`. Any LCCN or ISSN the book declares must also be real, and a declared `pending` one joins the refusal's list. A missing LCCN or ISSN is not a retail fault. When it is `false`, missing numbers are advice only. See Chapter 13.

**`registrations.isbn-block.prefix`**
: Type `str`, default none. The ISBN registrant prefix you own, such as `978-1-960780`. `press isbn assign` mints numbers from it. The prefix begins with 978 or 979, and its digit count must fit the block size. See Chapter 13.

**`registrations.isbn-block.size`**
: Type `int`, default none. The size of the block the agency sold. `press config list` names 10, 100, or 1000, the sizes the agency sells, and the code accepts any size from 10 through 1,000,000. The press validates the block only when both the prefix and the size are set. See Chapter 13.

### The commerce group {-}

The commerce keys control direct print ordering: a link on the landing page to a storefront where a provider sells a printed copy. The press takes no payment and runs no store. `press check` refuses an unknown key under `commerce.print-ordering`, a URL that is not HTTPS, a seller that is not named, and any value shaped like a secret. Chapter 12 explains the group under "Ordering a copy".

**`commerce.print-ordering.enabled`**
: Type `bool`, default `false`, so ordering is off. Setting it to `true` turns the order link on. With ordering on, the release gate at the end of `press all` builds the print pack and requires a passed inspection for the current edition in *config/qualification.yaml*. Unless CI or you set `PRESS_RELEASE=1`, the gate only advises. See Chapter 12.

**`commerce.print-ordering.edition`**
: Type `str`, default none. The edition sold, such as `paperback`. See Chapter 12.

**`commerce.print-ordering.storefront-url`**
: Type `str`, default none. The storefront the link opens. It must be an HTTPS URL. See Chapter 12.

**`commerce.print-ordering.seller-of-record`**
: Type `str`, default none. The party the reader buys from, named on the landing page before the reader leaves it. The press's model has the provider as the seller. You must confirm who the legal seller is. See Chapter 12.

**`commerce.print-ordering.support-url`**
: Type `str`, default none. A support page, which must be an HTTPS URL. If you omit it, the press generates *support.html*, which names the seller. See Chapter 12.

**`commerce.print-ordering.privacy-url`**
: Type `str`, default none. A privacy page, which must be an HTTPS URL. If you omit it, the press generates *privacy.html*. See Chapter 12.

**`commerce.print-ordering.refund-url`**
: Type `str`, default none. A returns page, which must be an HTTPS URL. If you omit it, the press generates *refunds.html*. See Chapter 12.

**`commerce.print-ordering.policies.support`**
: Type `str`, default none. Your own text, appended to the generated support page. The press writes no legal terms of its own. See Chapter 12.

**`commerce.print-ordering.policies.privacy`**
: Type `str`, default none. Your own text, appended to the generated privacy page. See Chapter 12.

**`commerce.print-ordering.policies.refund`**
: Type `str`, default none. Your own text, appended to the generated returns page. See Chapter 12.

## *config/front-matter.yaml* {-}

The presence of this file asks the press to generate the PDF's front matter: the title page, the copyright page, and the dedication, epigraph, and acknowledgments pages. The press calls the copyright page the colophon. The identity facts come from *config/metadata.yaml*. An absent key does not print. The scaffold writes the file with every key commented out. If the file is missing, `press config set` creates it. A file at *tex/title-page.tex* overrides all of it. Chapter 10, *Front matter, the index, and the table of authorities*, explains every key.

**`edition-note`**
: Type `str`, default the date's text before its first comma, lowercased. The edition line at the top of the colophon, such as `"first edition, second printing"`. See Chapter 10.

**`dedication`**
: Type `str`, default none. The text of the dedication page, set in italic in a narrow box. See Chapter 10.

**`epigraph.quote`**
: Type `str`, default none. The epigraph's text. The epigraph page prints only when you set this key. The `epigraph` key must be a mapping with `quote` and `attribution`, and the checker refuses any other shape. See Chapter 10.

**`epigraph.attribution`**
: Type `str`, default none. The epigraph's attribution, set below the quotation in the muted color. See Chapter 10.

**`acknowledgements`**
: Type `str`, default none. The text of the acknowledgments page. See Chapter 10.

**`rights-notice`**
: Type `str`, default none. The colophon's rights line, printed after the edition line and above a rule. See Chapter 10.

**`manufacture`**
: Type `str`, default none. The colophon's manufacture line, the classic origin line, such as `"Published in the United States of America"`. See Chapter 10.

**`colophon-note`**
: Type `str`, default none. The colophon's production note, which names the type and the method, set in italic. See Chapter 10.

**`contact`**
: Type `str`, default none. The colophon's contact line. See Chapter 10.

**`motto`**
: Type `str`, default none. A line of the press, set in italic at the foot of the colophon, above the logomark. See Chapter 10.

Once this file exists, the metadata must hold `title`, `author`, `copyright`, `publisher`, and `publisher-place`. A missing one stops the build with `front matter needs these config/metadata.yaml keys: ...`, followed by the names.

## *config/house-rules.yaml* {-}

The house rules are the book's own additions to the checker. The scaffold writes all three keys empty: `banned-patterns: {}`, `jargon-allow: []`, and `audit-dirs: []`. Chapter 6, *Checking the manuscript*, explains the three keys.

**`banned-patterns`**
: Type `mapping`, default empty. Each entry maps a regular expression to a label. The style audit applies each pattern to book prose as written, case and all, and prints `<file>:<line>: <label>` for a match. A pattern skips fenced code but reads inline code on a prose line. Inside a double-quoted YAML string, double each backslash, as in `"\\bvery unique\\b"`. The press refuses a pattern that does not compile with `config/house-rules.yaml: banned pattern '<p>' is not a valid regex (<exc>)`. See Chapter 6.

**`jargon-allow`**
: Type `list[str]`, default empty. Watchlist terms this book can use. The press folds the case of each entry and passes it to the jargon lint with `--allow`. The allowance holds for the whole manuscript. See Chapter 6.

**`audit-dirs`**
: Type `list[str]`, default empty. Extra directories, beyond *book/*, for the style audit to read. Files there meet the dash and phrase rules but not the curly-quote rule, the glyph law, or the banned patterns. A heading fault or a long paragraph there draws a warning and does not fail the check. The jargon lint does not read these directories. See Chapter 6.

## *config/aesthetic.yaml* {-}

The aesthetic is the book's visual identity. Press merges the book's file over the house aesthetic, named "Victorian treatise". The merge works at the top level only: a section the book names, such as `cover`, replaces the whole house section. Restate a whole section when you touch it. `press aesthetic` with no argument prints the merged result. The defaults below are the house values. Chapter 9, *The house design*, explains the keys that change the design, and Chapter 11, *The art department*, explains the keys that direct the art.

Most keys in this file are prose that the art commissions quote to an image model. The build itself reads only `scene-break`, the `typography` keys, the two palettes, and `book-colors`. Intake and `press art enhance` also read `plates.medium`. Certain craft laws hold whatever the aesthetic says. The exact title and author appear verbatim on the art, cover plates are flat, and the trim is the trim. Print interiors are single ink, except under the `house-6x9-color` profile.

### Direction for the art {-}

**`name`**
: Type `str`, default `Victorian treatise`. The aesthetic's name. See Chapter 11.

**`register`**
: Type `str`, default the house register, an earnest nineteenth-century trade manual. The voice of the design. See Chapter 11.

**`cover.style`**
: Type `str`, default `penguin-tri-band`. The cover style id from the style library. `press cover --style` overrides it for one run. The house library holds ten styles. See Chapter 11.

**`cover.subject`**
: Type `str`, default none. The subject of the cover illustration, in one phrase. The cover prompt takes the subject from `--subject`, then this key, then the metadata `description`, then `cover.emblem`, then the literal words "the book's subject". See Chapter 11.

**`cover.medium`**
: Type `str`, default the house text, Victorian publisher's bookcloth stamped as if by a brass die. The cover's medium, as prompt material. See Chapter 11.

**`cover.field`**
: Type `str`, default the house text, a solid cloth-colored field with a fine woven grain. The cover's field and composition. See Chapter 11.

**`cover.ink`**
: Type `str`, default `gilt: metallic gold stamping`. The cover's ink treatment. See Chapter 11.

**`cover.type-treatment`**
: Type `str`, default the house text, stacked centered letterpress capitals. How the cover sets its type. See Chapter 11.

**`cover.ornament`**
: Type `str`, default the house text, a border of two concentric thin rules with a small fleuron at each inner corner. The cover's ornament. See Chapter 11.

**`cover.emblem`**
: Type `str`, default the house text, one central engraved medallion drawn from the book's strongest image. Where the cover's emblem goes and how it is cut. See Chapter 11.

**`plates.style`**
: Type `str`, default `wood-engraving`. The default illustration style id for interior plates. A figure's `style=` attribute and `press illustrate --style` both override it. The house library holds seven styles. See Chapters 5 and 11.

**`plates.medium`**
: Type `str`, default the house text, wood engraving with dense hatching in a single black ink. The interior plate medium. When this text contains both the words "single" and "ink" and the design profile is not a color profile, intake grays a plate to the single interior ink. `press art enhance` chooses its upscaling model and its number of grays from words in this text, such as `engrav` or `wash`. See Chapter 11.

**`plates.composition`**
: Type `str`, default the house text, one idea per plate, composed landscape or portrait. How a plate is composed. See Chapter 11.

**`logomark.tradition`**
: Type `str`, default the house text, a printer's mark in flat single-ink line art on transparency. The tradition the logomark follows. See Chapter 11.

**`portrait.style`**
: Type `str`, default the house text, an engraved oval trade-journal portrait. The style of the author portrait. See Chapter 11.

### Values the build reads {-}

**`scene-break`**
: Type `str`, default `rule`. The ornament for a scene break: `rule`, `asterism`, or `fairy-dust`. See Chapters 4 and 9.

**`typography.web-family`**
: Type `str`, default `"Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif`. The CSS font stack for the reader site. See Chapter 9.

**`typography.pdf-family`**
: Type `str`, default `''`. The LaTeX main font. The empty string keeps Libertinus. The press sets a named family with oldstyle numerals. See Chapter 9.

**`web-palette`**
: Type `mapping`, default the house light palette. Each entry maps a token to a `#hex` color. Press writes the palette into the light theme of the reader stylesheet. The tokens are `paper`, `paper-warm`, `ink`, `ink-soft`, `cloth`, `cloth-deep`, `foil`, `foil-bright`, `foil-deep`, `hairline`, `link`, and `ornament`. The cover prompts also read `paper` and `accent`. The house palette defines no `accent`, so the cover prompt uses `#7a2325` unless the book sets one. See Chapters 9 and 11.

**`web-palette-dark`**
: Type `mapping`, default the house dark palette, which sets `cloth`, `paper`, `paper-warm`, `ink`, and `ink-soft`. Token to `#hex` for the dark theme, written into the reader stylesheet after its dark-mode media query. See Chapter 9.

**`book-colors.ink`**
: Type `str`, default `171717`. The PDF's ink color, as six hex digits without a `#`. Press writes each book color as a `\definecolor` line in *build/aesthetic.tex*. When the book sets no override, press removes that file. See Chapter 9.

**`book-colors.muted`**
: Type `str`, default `5C5C5C`. The PDF's muted color, hex without `#`. See Chapter 9.

**`book-colors.accent`**
: Type `str`, default `4B3E8A`. The PDF's accent color, hex without `#`. See Chapter 9.

**`book-colors.link`**
: Type `str`, default `46621F`. The PDF's link color, hex without `#`. TeX knows it by the house name `linkgreen`, whatever its color. See Chapter 9.

To draft the file, run `press aesthetic "<brief>"`, which runs the `aesthetic-brief` workflow and then tells you to review the result with `press aesthetic`. The command also takes an `--overwrite` option, which `--help` does not list.

## *config/index-terms.yaml* {-}

This file holds the curated terms of the subject index. In `press config list` it is the structured field `index-terms`. The press's help text names an "index workflow", but at the time of this writing none ships, so edit the file by hand. With no file, the book has no index. Chapter 10 explains the index.

The file is a list, not a mapping, and each entry has two keys. Example B.2 shows two entries.

**Example B.2. Two entries in config/index-terms.yaml**

```text
- term: Margins
  match: [margin, margins]
- term: Spine width
  match: [spine width, spine arithmetic]
```

**`term`**
: Type `str`, required. The heading the index prints for the entry. See Chapter 10.

**`match`**
: Type `list[str]`, required, not empty. The words and phrases that count as a mention of the term. Matching ignores case and requires a boundary at each end that is neither a word character nor a hyphen. The press removes fenced code, inline code, and image lines before it matches. The index locates each mention by chapter number, appendix letter, or `Preface`, never by page. See Chapter 10.

A term that matches nothing fails the build with `gen_index: curated terms match nothing in the text: <terms>`, followed by the advice to fix the patterns or remove the terms. The press also refuses a `terms:` wrapper around the list, an entry with an empty `term`, and a `match` that is not a list of strings. `press check`, `press config validate`, and every build apply the same shape rules.

## *config/authorities.yaml* {-}

This file is the table of authorities: a list of claims of fact in the manuscript and the sources that warrant them. In `press config list` it is the structured field `authorities`, which the `authorities-research` workflow populates. Every build checks every entry, and the press renders the ledger as the sources companion, `dist/<slug>-sources.md`, beside the book. Chapter 10 explains the ledger and its refusals.

**`claim`**
: Type `str`, required. An exact fragment of the manuscript's prose. The press matches it as a case-sensitive substring after it normalizes whitespace. Rewording the sentence in the chapter fails the build until you update the claim. See Chapter 10.

**`authority`**
: Type `str`, required. The source that warrants the claim. See Chapter 10.

**`file`**
: Type `str`, preferred. The chapter file that holds the claim, such as *book/chapters/00-preface.md*. With a declared file, the claim must appear exactly once in that file. The press allows copies elsewhere. Without one, the claim must appear exactly once in the whole book. See Chapter 10.

**`url`**
: Type `str`, optional. A URL for the source. See Chapter 10.

**`note`**
: Type `str`, optional. A short aside printed after the entry in the sources companion. See Chapter 10.

The press collects every problem under `gen_authorities: the ledger does not hold:` and numbers the entries from 1. It refuses a malformed entry, a duplicate claim, and an unknown declared file. It also refuses a claim that matches nothing, a claim that matches more than once, and a claim that moved to another file. The ledger does not format citations, so use footnotes for citations in the text.

## *config/cover-styles.yaml* {-}

The cover styles are the prompt templates for `press cover`. The house library lives inside the press. A book's *config/cover-styles.yaml* merges over it, key by key, so a book can add a style or replace one by its id. The file is not in `press config list`, and `press config validate` does not list it. Chapter 11 explains the covers.

The file holds one top-level key, `styles`, a mapping from a style id to the style's fields. Example B.3 shows the shape.

**Example B.3. A book's own cover style**

```text
styles:
  my-house-style:
    name: "My house style"
    era: "your imprint"
    note: "what it looks like, in a line"
    text: baked
    prompt: |
      A book cover, portrait, on {paper}. ...
      The title "{title}" and author "{author}" set ...
```

**`styles.<id>.name`**
: Type `str`. The style's display name. See Chapter 11.

**`styles.<id>.era`**
: Type `str`. The period or tradition the style comes from. The house styles name theirs, such as 1935 onward for `penguin-tri-band`. See Chapter 11.

**`styles.<id>.note`**
: Type `str`. A one-line description, which `press cover --list` prints beside the id. See Chapter 11.

**`styles.<id>.text`**
: Type `str`, default `baked`. With `baked`, the image model letters the title. Press appends a guard that names the exact title, author, and imprint and forbids other words. Every house style is `baked`. The press documentation describes a `composited` value in which the press sets the type, but no code does so. Any other value only leaves the guard off. See Chapter 11.

**`styles.<id>.prompt`**
: Type `str`. The prompt template. It can use the fields `{title}`, `{author}` (the first author), `{imprint}` (the publisher), `{initials}` (up to three capitals from the publisher's name), `{accent}`, `{paper}`, and `{subject}`. See Chapter 11.

The ten house styles are `art-deco`, `bold-typographic`, `collage-mixed-media`, `midcentury-modern`, `minimalist-literary`, `penguin-tri-band`, `photographic`, `pulp-paperback`, `swiss-international`, and `victorian-clothbound`. `press cover --list` prints each with its note.

## *config/illustration-styles.yaml* {-}

The illustration styles are the prompt templates for `press illustrate`. A book's *config/illustration-styles.yaml* can add styles, under one top-level key, `styles`, which maps an id to the style's fields. Like the cover styles, the file is not in `press config list`. Chapter 11 explains the plates.

**`styles.<id>.name`**
: Type `str`. The style's display name. See Chapter 11.

**`styles.<id>.note`**
: Type `str`. A one-line description, printed by `press illustrate --list`. See Chapter 11.

**`styles.<id>.source`**
: Type `str`, optional. With `required`, the style needs an image to redraw, given with `--from`. The house style `figure-from-photo` is the one that requires it. Without `--from`, the press refuses such a style with `the <style> style needs source material: --from <image>`. See Chapter 11.

**`styles.<id>.prompt`**
: Type `str`. The prompt template. It can use `{subject}`, `{ink}`, and `{paper}`. The `{ink}` field reads `book-colors.ink`, then `web-palette.ink`, then `#1b1b1b`. The house `book-colors.ink` is `171717` with no `#`, so a house prompt reads "in 171717 ink". The `{paper}` field reads `web-palette.paper`, then `#f4f1e6`. Press always appends its own guard: a single ink, and no words, caption, border, watermark, or signature. See Chapter 11.

The seven house styles are `botanical-plate`, `engraved-map`, `figure-from-photo`, `line-diagram`, `ornament`, `technical-cutaway`, and `wood-engraving`. A plate's style comes from `--style`, then the figure's `style=` attribute, then `plates.style` in the aesthetic, then `wood-engraving`.

## Fields kept outside these files {-}

`press config list` names three more fields that are neither writable nor in the files above. It prints, for each one, where to go instead.

**`qualification`**
: Structured. The physical-inspection records, in *config/qualification.yaml*: a `schema_version` and a list of `inspections`. Each inspection names a provider, a product, a region, the `edition_id` of the copy, the inspector, and a result for each of eleven points. Every point must pass. An inspection covers one `edition_id`, so a change to the manuscript, the cover, or the print spec makes it out of date. You write the record by hand. See Chapter 12.

**`tex/title-page.tex`**
: File. Hand-authored front matter. When it exists, the press never generates front matter and ignores *config/front-matter.yaml*. A separate *tex/title-page-print.tex* replaces the title page in the print interior. See Chapter 10.

**`assets`**
: File. The cover (*assets/cover.jpg*), the logomark (*assets/press-logo.png*), the plates (*assets/woodcuts/*), the author photograph, and the Web stylesheets (*assets/web/reader.css* and *assets/web/extra.css*), with the art records under *art/*. Each one is optional, and every consumer works without it, except `press coverwrap`, which needs *assets/cover.jpg*. See Chapters 9 and 11.
