# Appendix E: Glossary {.unnumbered}

Each entry gives the meaning a term has in this book and the chapter that treats it. A term in italic inside an entry has its own entry. Filenames and directories are also in italic and have none.

**acceptance record**
: The section of *art/commissions.md* where `press art accept` writes one line for each *art target* it accepts (Chapter 11).

**aesthetic**
: The book's visual identity in *config/aesthetic.yaml*, which press merges over the house aesthetic. It cannot repeal a *craft law* (Chapters 5, 9, and 11).

**alpha master**
: A plate kept as ink on transparency: black color channels, with all the tone in the alpha channel. Press composites it onto the ground of each edition (Chapters 5 and 11).

**appendix file**
: A file in *book/appendices/* whose name is one lowercase letter, a hyphen, and the rest, ending in `.md` (Chapter 3).

**art department**
: The commands that commission, accept, and finish the book's art, from `press aesthetic` to `press art enhance`. You make the art once on your own machine and commit it. CI never generates art (Chapter 11).

**art target**
: The `--as` value of `press art accept`: `cover`, `plate:<name>`, `logomark`, or `portrait` (Chapter 11).

**artifact**
: A file or directory in *dist/* that the *registry* names, with its outputs, prerequisites, and publication role (Chapters 1 and 7).

**asterism**
: A scene-break *ornament* of three asterisks spaced a quad apart (Chapter 4).

**audit directory**
: A directory outside the manuscript, named under `audit-dirs`. Its files meet only the *universal battery*. The checker reports heading and paragraph faults there as warnings (Chapter 6).

**authority**
: The source that warrants a *claim* in the *table of authorities* (Chapter 10).

**banned pattern**
: A `banned-patterns` entry in the *house rules*, a regular expression mapped to a label. The checker applies it, case-sensitive, to book prose (Chapter 6).

**book model**
: The press's typed rules for every config field: kind, requirement, and default. Every build and every `press config set` checks against it (Chapters 3 and 16).

**book repository**
: A directory that holds *config/metadata.yaml* and the manuscript under *book/*, with the config and accepted art, and nothing else (Chapters 1 and 3).

**book root**
: The directory a *target* works in: `BOOK_ROOT` if set, otherwise the current directory. Press does not search upward (Chapter 3).

**build/**
: The directory of intermediate files, none of them published (Chapters 1, 3, and 7).

**caliper**
: The thickness of one page of a paper stock, in inches (Chapter 12).

**caption**
: The text in the square brackets of an image line, for the reader. Press never takes art direction from it (Chapter 5).

**catalog**
: The one typed table of commands in *catalog.py*. Press renders the usage text, `press --help`, and the *desk* picker from it (Chapter 16).

**celebrimbor**
: The framework that runs the press's development checks. It is a development and CI dependency only (Chapters 2 and 16).

**chapter file**
: A file in *book/chapters/* whose name starts with a digit and ends in `.md` (Chapter 3).

**chapter opening**
: The treatment of each chapter's first letter, set by `chapter-opening`. The *drop cap* is one style of it. The initial is the large letter itself (Chapter 4).

**chapter witness**
: The *manuscript witness* rule applied to one chapter file. Its line must appear on exactly one reader-site page and in every edition (Chapter 8).

**checker**
: `press check`, which reads every chapter file before anything builds and refuses a manuscript that breaks a rule. Its four passes are the *source checks*, the *checker self-test*, the *style audit*, and the *jargon lint* (Chapters 1 and 6).

**checker self-test**
: The checker's second pass. Each *known-bad fixture* must draw its declared rule, and the *known-good fixture* must draw nothing. It is not the `press selftest` target (Chapter 6).

**CIP**
: Cataloging in Publication, a Library of Congress program not open to self-publishers. See *PCN* (Chapter 13).

**claim**
: An exact fragment of prose that the *table of authorities* cites. Every build confirms it appears exactly once in its declared file (Chapter 10).

**colophon**
: The press's name for the copyright page, not this book's closing Colophon (Chapter 10).

**commerce gate**
: The gate that guards *print ordering*. It computes the *edition manifest* and looks for a *qualification* (Chapters 7, 8, and 12).

**commission**
: A prompt for an image model, kept in *art/commissions.md* (Chapter 11).

**composite action**
: The file *action.yml*, which installs press in CI from the action's own checkout, never with pip from Git (Chapters 2 and 14).

**counsel mode**
: `press improve` without `--apply`. It writes a report and touches nothing. Press compares fingerprints of *book/* and *config/* to prove it (Chapter 15).

**cover wrap**
: The whole printed cover (back, spine, and front) as one PDF page with bleed, a computed spine, and the *EAN-13* barcode (Chapters 1 and 12).

**craft law**
: A house law no configuration can change. The four are verbatim text, flat plates, single-ink interiors (`house-6x9-color` excepted), and "the trim is the trim" (Chapters 9 and 11).

**decoration**
: An illustration that holds no information, marked `decorative=true`. Press gives it empty alt text and never numbers or lists it (Chapter 5).

**defaults file**
: A YAML file of pandoc settings. The templates in *data/defaults/* name paths with `@press/` and `@book/` and mark a file that may be absent with `?optional`. Press renders them into *build/defaults/* (Chapter 7).

**design major**
: A major release that changes how a valid book looks, as 3.0.0 did. Each *design profile* also carries a `design-major` that must rise when its appearance changes (Chapters 1 and 9).

**design profile**
: One of six sealed interior geometries, selected with `print.profile`: trim, margins, *height cap*, indent and leading, and the width of the *paper column*. The font family belongs to the *aesthetic*. See *seal* (Chapters 1, 9, and 12).

**desk**
: `press desk`, the press's full-screen console in the terminal. Every action it runs is a target you could type (Chapters 1 and 15).

**directive**
: The `art:` comment after an image line, written for the illustrator or image model. It is distinct from the *caption* and the *fig-alt* (Chapters 5 and 11).

**dist/**
: The directory of published *artifacts* (Chapters 1 and 3).

**drop cap**
: The `drop-cap` style of *chapter opening*. It splits the first word, so a *sentinel* there fails exact matching in the Print edition (the PDF) (Chapter 4).

**EAN-13**
: The barcode symbology for an ISBN-13, drawn by press on the *cover wrap* (Chapters 12 and 13).

**editable install**
: An install that points Python at a clone's files, so a `git pull` changes the installed press (Chapter 2).

**edition**
: One published form of the book. Press names eight, from the Print edition to the Source edition (Chapters 1 and 7).

**edition manifest**
: The record of one printed edition's production facts. Its `edition_id` is a sha256 hash over the interior, the cover, the print spec, the ISBN, and the toolchain digest (Chapter 12).

**editorial law**
: The rules `press check` enforces. See *checker* (Chapter 6).

**evidence state**
: The desk's glyph for an artifact, derived from content digests and never from a timestamp. The live desk shows `-`, `o`, and `/` (Chapter 15).

**expect comment**
: The line `<!-- expect: <rule> -->` that names the rule a *known-bad fixture* must draw (Chapter 6).

**extension manifest**
: A declaration of the exact names an extension claims in one of press's data registries. Press "extends by declaration, not by code" (Chapter 16).

**extras**
: pip's optional dependency groups. Press has `tui`, for the *desk*, and `dev`, for work on the press itself (Chapter 2).

**fairy-dust**
: A scene-break *ornament* of eleven asterisks in rows of four, three, and four, which press describes as Tenniel's 1866 array (Chapter 4).

**fig-alt**
: The alt text of an illustration, for a reader who cannot see it. It never copies the *caption* (Chapter 5).

**figure**
: A numbered informative illustration that the text cites by number ("Figure 7.3"), listed in the List of Figures. Its class is `.figure`, `.chart`, `.map`, `.photo`, or `.diagram` (Chapter 5).

**finisher**
: A planned source mode for designed interiors, `interior: path/to/interior.pdf`. At the time of this writing, it is not part of press 3.0.2 (Chapter 1).

**float**
: LaTeX's word for a block it may move to a better spot on the page (Chapter 8).

**floating tag**
: A tag such as `v3` that moves to the newest compatible release within its major (Chapters 1 and 14).

**front matter**
: The pages from the cover plate through the acknowledgments, generated from *config/metadata.yaml* and *config/front-matter.yaml* (Chapter 10).

**frontispiece**
: The *placement* that gives an illustration a cleared leaf (see *leaf*) on an even page, facing the chapter that follows (Chapter 5).

**generatable kind**
: A class `press illustrate` can commission: `.plate`, `.figure`, `.map`, or `.photo`. `press illustrate` refuses the data kinds `.chart` and `.diagram` (Chapter 5).

**generator**
: Machinery that makes the right thing. The second law ranks it above a check and a convention (Chapter 1).

**glyph law**
: The checker's list of characters allowed in book prose: printable ASCII with tab and line ends, and the accented Latin letters, U+00C0 to U+017F (Chapters 4 and 6).

**golden copy**
: The first physical copy of an exact edition, inspected against the eleven-point checklist. Every point must pass (Chapter 12).

**guard**
: The free lines a page must have before press starts a *wrap*. With fewer, the wrap moves to the next page (Chapter 5).

**height cap**
: The tallest an image may be, set per *design profile*: 6.3 inches on the house 6 by 9 (Chapter 5).

**house**
: Press's default design and law. A book changes it through its own config, never by editing press (Chapters 1 and 9).

**house rules**
: The optional *config/house-rules.yaml*: `banned-patterns`, `jargon-allow`, and `audit-dirs` (Chapter 6).

**illustration**
: Any picture in a chapter file, sorted into *plate* or *figure* (Chapter 5).

**immutable tag**
: A three-part tag such as `v3.0.2` that names one release forever and pins its own action and toolchain digest (Chapters 1 and 14).

**in-flow placement**
: A *placement* among the lines of text: `inline`, `wrap-inner`, `wrap-outer`, or `margin`. Only these take a *measure* (Chapter 5).

**informative figure**
: See *figure*.

**intake**
: What `press art accept` does: it converts a delivered image to house form and writes it into *assets/* (Chapters 5 and 11).

**invariant**
: A named `INV-` entry in the press's ledger, *.celebrimbor/invariants.yaml*, with its enforcer, proof, and limits (Chapters 7 and 16).

**jargon allowance**
: A `jargon-allow` entry, which permits a watchlist word everywhere in the book (Chapter 6).

**jargon lint**
: The checker's fourth pass, which looks for words from the *watchlist* outside quotations and code (Chapters 4 and 6).

**known-bad fixture**
: A Markdown file that a check must reject. The press carries 19, and a book adds its own in *tests/known-bad/* (Chapters 1 and 6).

**known-good fixture**
: The file *clean.md*, which must draw no diagnostic (Chapter 6).

**LCCN**
: A Library of Congress Control Number, which a self-publisher gets through the *PCN* program (Chapter 13).

**lead**
: The quotation mark that opens a dialogue paragraph at a *chapter opening*, hung into the margin (Chapter 4).

**leaf**
: One sheet of the book, two pages back to back. A cleared leaf is a fresh page that holds one illustration (Chapters 5 and 10).

**locator**
: Where a reader finds an index term: a chapter number, an appendix letter, or "Preface", never a page (Chapter 10).

**Lua filter**
: A small program that pandoc runs over the document between reading and writing it (Chapters 1 and 7).

**luminance key**
: The intake step that turns brightness into opacity: luminance 225 and above becomes clear, 45 and below opaque (Chapter 11).

**manuscript**
: The chapter files and appendix files under *book/* (Chapter 1).

**manuscript witness**
: The longest markup-free line of 40 or more characters in the manuscript. Every edition but the Print edition must carry it (Chapter 8).

**measure**
: A width stated against the line: `full-measure`, `half-measure`, or `third-measure` (Chapter 5).

**migration**
: The move of a book to the next major with `press migrate`, which rewrites only the press pins. It first writes an exact backup and afterward a receipt under *.press/*, and it leaves the manuscript, the config, and the art alone (Chapter 14).

**ONIX 3.0**
: The book trade's XML format for product records, written by `press onix` (Chapter 13).

**operator**
: The commands `press improve`, `press research`, and `press aesthetic`, which hand work to an agent through `claude`. They are not *targets* (Chapters 2 and 15).

**ornament**
: The glyph of a *scene break*: a rule, an *asterism*, or *fairy-dust* (Chapter 4).

**outset**
: The gap between a *wrap* and its text, in ems only (Chapter 5).

**page floor**
: The value of `verify-min-pages`, the fewest pages the PDF verifier accepts (Chapters 6 and 8).

**Pages bundle**
: The directory *dist/pages/*, which `press pages` assembles and from which GitHub Pages serves the *Pages site* (Chapters 1 and 7).

**Pages site**
: What GitHub Pages serves from the *Pages bundle*: the book's public Web site (Preface, Chapters 7 and 14).

**paper column**
: The reader site's framed column that holds the text, styled as a sheet (Chapter 9).

**paragraph law**
: The checker's rule that a paragraph must be under 190 words (Chapter 6).

**parity-aware**
: Said of a placement that names its side by the spine, such as `wrap-inner` (Chapter 5).

**PCN**
: The Library of Congress Preassigned Control Number program. Press prepares its field values, and you submit them through PrePub Book Link (Chapter 13).

**placement**
: The value of `place`: `inline`, `wrap-inner`, `wrap-outer`, `margin`, `plate`, `full-bleed`, or `frontispiece` (Chapter 5).

**plate**
: An unnumbered illustration in the idiom of the literary woodcut, listed in the List of Plates. It is distinct from `place=plate` (Chapters 1 and 5).

**PPI**
: Pixels per inch at the printed size. A printer wants about 300. In the `ppi-table` *spine shape*, PPI means pages per inch (Chapters 5 and 12).

**preflight**
: The program a print shop runs over every file it receives (Chapters 5 and 12).

**press**
: The pip-installable Python package and its command, `press <target>` or `python -m press`, lowercase by convention (Chapter 1).

**print interior**
: The PDF that goes inside the covers, built by `press print` (Chapters 5 and 12).

**print ordering**
: The optional ordering of printed copies from the book's *Pages site* (Chapters 8 and 12).

**print pack**
: The *print interior*, the *cover wrap*, and the retail channel checklists (Chapters 1 and 12).

**print-safe pass**
: The pass that flattens each image onto white and caps its resolution for print (Chapters 5 and 12).

**provider**
: A print shop's specification, selected with `print.provider`. It decides the spine, the hardcover boards, and the trims and page counts a shop accepts (Chapter 12).

**qualification**
: A passed inspection of a *golden copy*, recorded by hand in *config/qualification.yaml* for one `edition_id` (Chapter 12).

**quality gate**
: The *celebrimbor* gate as the press configures it. It holds the press's domain checks and *ratchets* (Chapter 16).

**ratchet**
: A floor that may only rise, such as coverage, mutation score, or Lua coverage. The gate fails below it (Chapter 16).

**recto, verso**
: The right-hand odd page and the left-hand even page (Chapter 5).

**registry**
: The artifact graph in *registry.py*. It names every *artifact* and its dependencies, and the build order comes from those edges (Chapters 1, 7, and 16).

**release contract**
: The workflow that proves each press tag pins itself and a resolvable `@sha256:` image, with a complete *trust receipt* chain (Chapters 1 and 14).

**release witnesses**
: The release floor under `PRESS_RELEASE=1`: at least two sentinels and a *page floor* of at least 24 (Chapters 3 and 6).

**reusable workflow**
: The file *build.yml* that a book's CI calls. It pins the *composite action* and the *toolchain image* (Chapters 2 and 14).

**runaround**
: The trade's name for a *wrap* (Chapter 5).

**runt**
: A paragraph's last line of one short word, prevented by a finite `\parfillskip` (Chapter 9).

**scar**
: A production failure turned into a mechanical guard and an entry in the press's *CLAUDE.md* (Chapters 1 and 16).

**scene break**
: A pause inside a chapter, typed `* * *` and drawn as an *ornament* (Chapter 4).

**seal**
: A digest of a *design profile* in *profile-seals.yaml*. A check turns red when the profile no longer matches it (Chapters 9 and 12).

**sealed capability**
: One of five guarantees an extension may depend on but never claim, such as `release-gate` (Chapter 16).

**seller of record**
: The party that legally sells to the reader. Press's model takes the provider as the seller. The publisher must confirm it (Chapters 3 and 12).

**sentinel**
: A `verify-sentinels` phrase that must appear in the manuscript and in every edition (Chapter 6).

**set piece**
: A shaped passage, `::: cascade`, `::: verse`, or `::: tail`, whose words stay live text (Chapter 4).

**skill**
: A packaged authoring guide that an agent reads before it writes. `press skills` lists the eleven (Chapters 11 and 15).

**slug**
: The basename of every artifact. It matches `[a-z0-9][a-z0-9-]*` and defaults to the directory given to `press new` (Chapter 3).

**source checks**
: The checker's first pass: files, headings, required metadata, and configuration (Chapter 6).

**sources companion**
: The file *dist/<slug>-sources.md*, written from the *table of authorities* and published beside the book (Chapters 1 and 10).

**spine shape**
: One of four ways a provider computes the spine: `constant`, `divisor`, `ppi-table`, or `lookup` (Chapter 12).

**stale artifact**
: An artifact not rebuilt in this run. The registry's edges make every verify target rebuild what it reads. The one exception is `press verify-formats`, which reads an existing PDF into its agreement check without rebuilding it (Chapters 8 and 16).

**structured field**
: A config field too rich for one command line, such as the index terms. The other kinds are writable, immutable, and file fields (Chapter 3).

**style audit**
: The checker's third pass, also run alone as `press style` (Chapter 6).

**subject index**
: The appendix press writes on every build from *config/index-terms.yaml*. See *locator* (Chapter 10).

**table of authorities**
: The ledger in *config/authorities.yaml* of *claims* and their *authorities*, never a page of the book (Chapter 10).

**target**
: A `press` command that builds, checks, or verifies, such as `press pdf` (Chapter 1).

**tie**
: A non-breaking space between two words that must not part at a line end (Chapter 4).

**title page**
: The first page that carries type (Chapter 10).

**toolchain**
: The outside programs press runs: pandoc, LuaLaTeX, latexmk, the fonts, epubcheck, and poppler (Chapter 1).

**toolchain image**
: `ghcr.io/clintecker/press-toolchain`, a public image built on Ubuntu 24.04 and pinned by digest. Every CI build runs in it (Chapters 1, 2, and 14).

**trust receipt**
: The record that one layer of proof ran. There are twelve layers in three tiers. A release must present the complete chain (Chapters 14 and 16).

**universal battery**
: The rules every audited file meets, such as no em dash and no trailing whitespace (Chapter 6).

**vacuous witnesses**
: Press's phrase, in its release refusal, for knobs too weak to prove anything (Chapter 3).

**verifier**
: The check that opens a finished artifact and inspects it as an object, and its `verify_*` module (Chapters 1 and 8).

**watchlist**
: The list of 53 overused words in the `overused-jargon` skill, each marked `allow`, `inspect`, `rewrite`, or `ban` (Chapters 1 and 6).

**witness**
: Any evidence a verifier requires of an edition: a *sentinel*, the title, the *manuscript witness* line, a *chapter witness* line, or the page floor. The Print edition carries the title and the sentinels but no manuscript witness line. See also *release witnesses* (Chapter 8).

**workflow**
: A packaged agent procedure that dispatches agents and runs press targets to check their work. The press carries four (Chapters 11 and 15).

**wrap**
: An illustration with text running around it: `wrap-inner`, `wrap-outer`, or `margin` (Chapter 5).
