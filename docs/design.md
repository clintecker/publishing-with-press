# Publishing with Press: book design

Status: design, 2026-11-11. This is the spec every chapter brief, figure
brief, and reviewer works from. The research it rests on lives in the
session scratchpad under `research/` (the O'Reilly-era style guide, the
press fact base, the production handbook, the prose contract); the parts
of those files a writer needs are quoted into each brief.

## 1. What this book is

*Publishing with Press: Building Books from Plain Text* is a technical
manual explaining the `press` book pipeline (version 3.0.2) to someone who
has a manuscript in Markdown and wants a finished, verified book in print,
EPUB, and on the Web. It is written and designed in the idiom of a technical
publisher's "animal book" of about 1999 to 2002: second person, present
tense, dry, exact, with numbered figures, tables, and examples, a preface
in the canonical shape, lettered appendixes, a glossary, an index, and a
colophon that describes the animal on the cover.

It is itself a press book, built by press from its own `book/` directory,
and every claim in it comes from the fact base, which came from the press
source and its documentation at commit `fee8e42`.

The book is honest about what it is: the copyright page and colophon name
the real author, the real imprint (LGTM Publishing, Chicago), and the real
toolchain. The design is an homage to a tradition, not an imitation of a
particular publisher: no publisher's trademarks, series names, logos, or
sentences.

## 2. Reader and purpose

- **Reader:** an author or small-press operator who can use a Unix shell
  and a text editor, knows git at the clone-commit-push level, and does
  not know TeX or pandoc. A second reader is a developer asked to keep a
  group's book builds running; Chapters 14 to 16 are for them.
- **Purpose:** after reading, they can scaffold a book, write a manuscript
  that passes `press check`, build and verify every edition, commission
  art, prepare a print edition, register it, and understand what the CI
  release contract promises. They can also read a press refusal and know
  what to do.
- **Not the purpose:** selling press, comparing it with other tools at
  length, or teaching Markdown from zero.

## 3. Identity

| Fact | Value |
|---|---|
| Title | Publishing with Press |
| Subtitle | Building Books from Plain Text |
| Author | Clint Ecker |
| Publisher, place | LGTM Publishing, Chicago, Illinois |
| Edition line | First edition, 2026 |
| Slug | publishing-with-press |
| Covers press version | 3.0.2 ("at the time of this writing") |
| Cover animal | the common cuttlefish, *Sepia officinalis* |
| Cover band colour | deep sepia brown (`#4a2e1a`), so the band is the animal's ink |
| Sample book used in examples | *Alice's Adventures in Wonderland*, slug `alice`, the press's own example |
| Fixed cast | user `alice`, workstation `hatter`, CI host `printshop`, repo owner `wonderland-press` |

Why the cuttlefish: it is an animal made of ink (sepia is named for it), it
is a single creature that renders itself onto any surface in one ink, and
Victorian natural-history engravings of it are plentiful. The private
resonance stays private; the colophon describes the animal and draws no
link to the software.

## 4. The two laws the book obeys at once

The book follows the period idiom wherever press law allows, and press law
where the two differ. The rulings:

1. **Headings are sentence case.** The style audit refuses title-case
   headings with three or more capitalised words, and a book that is half
   one case and half the other looks careless. Chapter titles, A-heads,
   and B-heads are all sentence case. This is the one visible departure
   from the period's Title Case heads.
2. **Numbering is press's `Figure 2.1`, not the period's `Figure 2-1`.**
   The figure-numbering filter bakes `Figure C.N` into every edition and
   builds the List of Figures from it. Tables and examples are numbered by
   hand in the same form (`Table 2.1`, `Example 2.1`) so the three systems
   agree.
3. **No em or en dashes, straight quotes in source, ASCII plus accented
   Latin.** This is press law and also the prose contract.
4. **Paragraphs under 190 words; the 80-word average the prose contract
   wants is well inside it.**
5. **Chapters open with a drop cap in the PDF.** The house does this; a
   technical book of the period did not. The Preface is `{.unnumbered}`
   and gets none. Sentinels are therefore mid-chapter phrases.
6. **The front colophon the press generates stays** (title page, imprint,
   rights, edition note, production note, motto). The period's
   back-of-book colophon with the animal paragraph is an authored
   appendix, `z-colophon.md`, headed "Colophon".
7. **Parts are not used.** Press has no `\part`. Sixteen chapters sit
   under the period's threshold anyway.
8. **"Unix", "e-mail", "Web site", "filename", "manpage", "appendixes",
   "toward".** American spelling throughout.

## 5. Structure

Target: about 95,000 words, roughly 320 pages on the house 6 by 9 trim.

### Front matter (generated by press from config, plus one authored file)

- Title page, copyright and colophon page, dedication, epigraph: from
  `config/front-matter.yaml` and `config/metadata.yaml`.
- Contents, List of Figures, List of Plates: generated.
- `00-preface.md`, "Preface" (unnumbered): two untitled opening paragraphs
  on why the book exists and where press came from, then "Who should read
  this book", "Organization of this book" (one blurb per chapter and
  appendix, verb-first), "Conventions used in this book" (the full
  definition list from the style guide, adapted to press numbering and
  with no bold-in-code claim), "Using code examples", "How to contact us"
  (the repository's issue tracker and the docs site, no postal address or
  phone), "Acknowledgments" (brisk; names the machines).

### Chapters (`book/chapters/NN-*.md`)

Each chapter opens with an "In this chapter" box (a fenced Div, class
`in-this-chapter`, holding a bulleted list of the A-heads), then the
orientation paragraph with no heading before it. Word targets are for the
prose; tables, examples, and captions are extra.

| N | File | Title | Words | Core content (fact base sections) | Figures | Plates |
|---|---|---|---|---|---|---|
| 1 | 01-introduction.md | Introduction | 5,000 | what press is; extracted from one book; the four laws; what it is not; a ten-minute tour from `press new` to `ls dist/`; the editions it produces; versions and the pinned contract in one paragraph (§1, §3.4, §3.5) | 1.1 pipeline overview (manuscript to editions); 1.2 the layered stack (OS, Python, pandoc, TeX, press, your book); 1.3 the ten-minute tour as a filmstrip of three terminal frames | frontispiece (the shop) |
| 2 | 02-installing-press.md | Installing press | 5,000 | pip and editable installs; the system toolchain (pandoc, LuaLaTeX and TeX Live, latexmk, fonts, epubcheck and java, poppler); `press doctor` and its report; the toolchain image and `scripts/dev-render.sh`; Apple Silicon; the first-run font scan; what is not tested (§2) | 2.1 `press doctor` report, boxed terminal; 2.2 where each tool sits in the build (a data-flow with tools on the arrows); 2.3 local versus container builds | |
| 3 | 03-the-shape-of-a-book.md | The shape of a book repository | 6,000 | `press new` and its flags; the tree file by file; `metadata.yaml` field by field with types and defaults; `press config get/set/unset/list/validate`; slugs; chapter and appendix discovery and sorting; `press add`; `00-` front parts; the Makefile; `.gitignore`; `git init` and why the source zip needs it; `build/` and `dist/` (§3.1 to 3.5) | 3.1 the scaffold tree (directory-tree archetype); 3.2 how chapters and appendices sort (before/after pair); 3.3 `dist/` after `press all` (tree) | |
| 4 | 04-writing-the-manuscript.md | Writing the manuscript | 6,000 | the pandoc dialect and smart punctuation; headings and numbering; the glyph law; footnotes; tables and captions; code blocks; epigraphs; scene breaks and ornaments; chapter openings and drop caps; the set pieces; typographic spacing; the 190-word paragraph; the Alice example as running sample (§4) | 4.1 anatomy of a chapter page (annotated page with callouts: running head, folio, drop cap, scene break, footnote); 4.2 the three set pieces side by side; 4.3 scene-break ornaments | plate: the compositor at the frame |
| 5 | 05-figures-and-plates.md | Figures, plates, and illustrations | 6,000 | image syntax; plates versus informative figures; kinds; numbering and `@id` cross-references; the List of Figures and List of Plates; every placement with its measure rules and what each edition does with it; `outset`; `fig-alt` and `decorative`; the `art:` directive; the height cap per profile; print-safe flattening; file formats and resolution (§4.2, §10.7) | 5.1 the placement vocabulary (a grid of miniature pages, one per placement); 5.2 how a wrap behaves against running text; 5.3 the two lists and where a figure appears in each | |
| 6 | 06-checking-the-manuscript.md | Checking the manuscript | 5,500 | `press check` in order: source checks, check-the-checkers, style audit, jargon lint; each rule and its message; `house-rules.yaml` (banned patterns, jargon allow, audit dirs); the watchlist and its statuses; known-bad and known-good fixtures; sentinels and min pages; exit codes; the scar of the red check that shipped green (§6.4 to 6.6) | 6.1 the checker guards every build (pipeline with pass/fail); 6.2 a known-bad fixture round-trip (flow) | |
| 7 | 07-building-the-editions.md | Building the editions | 6,000 | every target and what runs; the pandoc command; defaults templating (`@press/`, `@book/`, `?optional`); the Lua filter chain in order and what each filter does; latexmk and why; EPUB specifics; the chunked reader; the Markdown and text editions; the registry graph; `press all` in sequence; timings and logs; `press render`, `wordcount`, `clean` (§5) | 7.1 the build graph (registry: artifacts, prerequisites); 7.2 the filter chain per format (layered); 7.3 defaults templating (before/after of a defaults file); 7.4 `press all` as a state machine | |
| 8 | 08-verifying-the-artifacts.md | Verifying the artifacts | 6,000 | the philosophy (artifacts as objects); every `verify_pdf` check; every `verify_formats` check; epubcheck and the binfmt scar; archives; pages; cross-edition agreement; manuscript and chapter witnesses; the no-stale law and which command rebuilds what; reading a failure (§6.1 to 6.3, §5.3) | 8.1 what each verifier inspects (matrix figure); 8.2 the rebuild edges (which verify command rebuilds what); 8.3 a verify_pdf run, boxed terminal | plate: the witness that could say no |
| 9 | 09-the-house-design.md | The house design | 5,000 | the house 6 by 9 in numbers (fonts, sizes, leading, margins, drop cap, running heads, figure cap); the six profiles and what changes; the reader site and landing page; `aesthetic.yaml` palettes, typography, book colours; `extra.css` and `reader.css`; design as part of the contract and why a change needs a new major (§7) | 9.1 the page geometry with dimensions; 9.2 the six profiles compared (table-as-figure); 9.3 the reader site, boxed screenshot | |
| 10 | 10-front-matter-index-authorities.md | Front matter, the index, and the table of authorities | 4,500 | `front-matter.yaml` key by key and what each renders; the stacked OR subtitle; `tex/title-page.tex` override; `index-terms.yaml` and the chapter-label index; the zero-hit rule; `authorities.yaml`, the claim check, and the sources companion; what is not generated (§9) | 10.1 how config becomes the front matter (data flow); 10.2 an index entry's path from term to appendix | |
| 11 | 11-the-art-department.md | The art department | 5,500 | the aesthetic and its schema; cover styles and `press cover`; `press illustrate` and the `art:` directive; `press art accept` (cover, plate, logomark, portrait) and what intake enforces; the luminance key and alpha masters; `press art enhance`; `art/commissions.md`; the art-direction workflow; image models, keys, and what spends money; the logomark and portrait (§8) | 11.1 the art-direction loop (flow); 11.2 one master onto every surface (the alpha-master composite); 11.3 what intake does to a delivered plate (before/after) | plate: the engraver's bench |
| 12 | 12-the-print-pack.md | The print pack | 6,000 | the four orthogonal choices; design profiles and the lifecycle; provider specs and spine math; `press print` and `verify-print`; the cover wrap, bleed, and the EAN-13; print-safe images; qualification and the golden copy; `press publish` checklists; Lulu, KDP, IngramSpark as the docs and ledger state them; ordering links (§10) | 12.1 the cover wrap with every dimension labelled; 12.2 spine math by provider (table-as-figure); 12.3 the print pack graph (print, coverwrap, verify) | |
| 13 | 13-registrations.md | Registrations | 3,500 | the governing rule; ISBN blocks and `press isbn`; ISSN and LCCN; `retail`; `press pcn`; `press onix`; `press lookup`; where each number lands (colophon, EPUB, barcode); order of operations (§11) | 13.1 where each registration number lands (data flow) | |
| 14 | 14-continuous-integration.md | Continuous integration and the release contract | 5,500 | `book.yml`; the reusable workflow and the composite action; self-checkout install and the hash lock; the toolchain image pinned by digest; Pages deploy; receipts; tags, floating and immutable; the release contract workflow; what `PRESS_RELEASE` enforces; `press migrate` between majors (§12) | 14.1 the CI topology (workstation, repository, runner, registry); 14.2 the release state machine (pushed, built, verified, tagged, proved, floated, published); 14.3 how a book resolves `@v3` | |
| 15 | 15-the-desk-and-the-machines.md | The operator's desk and the editorial machines | 5,000 | `press desk`: screens, keys, evidence glyphs, the wizard; the four workflows and their phases; the skills; `press skills` and `press workflows`; `press improve` counsel mode and `--apply`; `press research`; `press aesthetic`; the named diseases and why they are hard-coded (§13, §14) | 15.1 the desk, boxed screenshot; 15.2 the editorial-passes machine (flow with rounds) | plate: the proofreaders' bench |
| 16 | 16-inside-the-press.md | Inside the press | 5,000 | the module map; the data flow end to end; the catalog and the registry as single statements; the typed book model; the adapters boundary; invariants and the ledger; `press selftest`; the quality gate in brief; receipts; the extension contract; how to contribute and what a scar must earn (§15, §16) | 16.1 the module map (layered); 16.2 the end-to-end data flow; 16.3 the trust tiers (stack) | |

### Appendixes (`book/appendices/`)

| Letter | File | Title | Words | Content |
|---|---|---|---|---|
| A | a-command-reference.md | Command reference | 6,000 | every command in manual-page shape: synopsis, description, options, examples, see also; from §17.1 and §17.2 |
| B | b-configuration-reference.md | Configuration reference | 4,000 | every key of every config file, alphabetical within file: type, default, meaning; from §17.3 and §3.3 |
| C | c-messages.md | Messages and refusals | 3,000 | the message in constant width, then Cause and Remedy; from §6, §17.4, §19 |
| D | d-the-toolchain.md | The toolchain, platform by platform | 2,000 | Debian and Ubuntu, macOS with Homebrew and MacTeX, the container image; versions stated only where the fact base states them |
| E | e-glossary.md | Glossary | 3,000 | the 75 terms of §18, alphabetical, term in bold |
| (F) | generated | Index of subjects | | from `config/index-terms.yaml`; the press assigns the next free letter |
| | z-colophon.md | Colophon | 400 | the animal paragraph in museum-label register; production credits naming the real toolchain (Markdown, pandoc, LuaLaTeX, press 3.0.2) and the real drafting method; fonts |

### Sentinels

Three mid-chapter clauses, chosen after the prose is final, each appearing
exactly once in the manuscript and never in a heading, caption, code block,
or drop-cap line. `verify-min-pages: 240`.

## 6. The prose

Every writer and reviser receives the prose contract verbatim (scratchpad
`research/prose-contract.md`): the period voice, the Pass 1 tells that are
defects on one sighting, the Pass 2 sentence rules at 80%, and the
fidelity rules. The short form:

- You, present tense, plain words; explain the why and the history; one
  understatement every few pages, never a pun in a heading.
- One idea per sentence, 16 to 22 words on average, never over 30; active
  voice with a named actor; simple tenses; condition before command; the
  action in the verb; one term per thing for the whole book; no
  semicolons, no dashes.
- No "not X but Y", no one-line closers, no staged run-ups, no forced
  triads, no stacked hedges, no -ing riders, no "serves as", no assistant
  vocabulary, no engineering jargon from press's watchlist, no "Let's".
- Every fact from the fact base at its stated strength. Where the fact base
  says the docs and the code disagree, the book follows the code or stays
  silent. Nothing in §20.C is stated. Nothing is invented: no timings, no
  tool versions, no platforms the fact base does not name.
- Cross-references in the period's forms: "see Chapter 7, *Building the
  editions*"; "as described in the section "Reading a failure" later in
  this chapter"; "Figure 8.2 shows"; "Table 3.1 lists".
- Every numbered figure, table, and example is referred to in the text
  before it appears.
- Admonitions: a Tip or a Warning, one to four sentences, imperative, at
  most eight per chapter. A sidebar is 150 to 400 words with a bold title,
  about one per chapter, for history, a war story, or a rationale (the 30
  scars of §19 are the stock).
- Footnotes two to six per chapter, for asides and history.
- Code: wrapped at 72 columns, the `$` prompt, `#` only for root, output
  elided with `...`, syntax lines with `[ ]`, `|`, and `...`.

The one term per thing list (the book's controlled vocabulary) is in
`docs/vocabulary.md` and every brief carries it.

## 7. Markup conventions (what a writer types)

These are fixed here so sixteen writers produce one book. The production
handbook confirms each mechanism renders in PDF, EPUB, HTML, and the
reader; where it cannot, the handbook names the fallback.

- Chapter: `# Title` as the first line; the next block is the
  "In this chapter" Div:

  ```markdown
  ::: {.in-this-chapter}
  - First A-head
  - Second A-head
  :::
  ```

- Tip: `::: {.tip}` ... `:::`. Warning: `::: {.warning}` ... `:::`.
  Sidebar: `::: {.sidebar}` with a bold first paragraph as its title.
- Example: a bold caption paragraph `**Example 3.1. A minimal
  metadata.yaml**` immediately above a fenced block with a language tag
  (`yaml`, `sh`, `text`, `markdown`, `lua`, `python`, `tex`). Sessions
  use `text` with `$ ` prompts.
- Table: a pipe table with `Table: Table 3.1. press check options`
  beneath it.
- Figure: `![Caption](assets/figures/NN-name.png){#fig:name .diagram}`
  with a preceding `<!-- art: ... -->` directive holding the figure brief.
  Placement attributes per Chapter 5's own rules (most diagrams are
  `inline` at `full-measure`; a tall one is `place=plate`).
- Plate: `![Caption in the quiet plate-legend register](assets/woodcuts/name.png)`
  with no kind class, so it stays an unnumbered plate in the List of
  Plates.
- Footnote: `[^n]` with the text at the end of the section.
- Cross-reference to a figure: `@fig:name` (renders as "Figure C.N").
  Chapters, sections, tables, and examples are referred to by number and
  title in prose, since press cross-references only figures.
- Index terms: writers do not mark text. The index is built from
  `config/index-terms.yaml`, which the index pass assembles from each
  chapter's "Index candidates" comment block at the end of the file
  (`<!-- index: term; term; ... -->`), removed before the final build.

## 8. Figures and plates

About 42 numbered figures and 6 plates, plus the cover.

- **Diagrams** are drawn as code (Graphviz `dot` for graphs and flows,
  Python with Pillow or matplotlib for page anatomies, trees, matrices,
  and timelines) in `tools/figures/NN-name.py` or `.dot`, rendered to
  grayscale PNG at 300 dpi, 1800 px wide for a full-measure figure, by
  `tools/render-figures.sh`. The look: black on white, 10 and 20 percent
  gray fills, 0.5 pt boxes and 0.75 pt arrows, small filled arrowheads,
  Helvetica-style labels at 7 to 8 pt with code in a monospace, rounded
  boxes for programs and square boxes with a dog-ear for files, a cylinder
  for a store, nothing touching the frame. The twelve archetypes of the
  style guide are the menu.
- **Terminal figures** are real press output rendered to a boxed, light,
  monospace panel by `tools/figures/terminal.py` from a captured text
  file, so every character is genuine.
- **Screenshots** of the reader site, the landing page, and the desk are
  taken from real builds (headless Chrome for the pages; the desk through
  its own headless proof), converted to grayscale, and boxed.
- **Plates** are commissioned with `press illustrate` in the
  `wood-engraving` style from `art:` directives written in the
  plates-and-woodcuts register: the house's earnest nineteenth-century
  trade-manual scene, one idea per plate, compact brass apparatus and
  never a robot. Six subjects: the shop at morning (frontispiece), the
  compositor at the frame, the witness that could say no, the engraver's
  bench, the proofreaders' bench, and the cuttlefish at its inkwell (the
  colophon). Each goes through `press art accept --as plate:<name>` and
  `press art enhance`.
- **The cover** is composed, not lettered by a model: the cuttlefish
  engraving is commissioned as an alpha master; `tools/cover.py` lays it
  on a white ground with the sepia band, the title in a condensed
  Garamond-class face, the subtitle in italic, the author bottom right,
  and the imprint bottom left, then `press art accept --as cover` enforces
  the geometry. A custom style entry in `config/cover-styles.yaml` records
  the same brief so `press cover` can regenerate it.
- Every figure's source is committed under `tools/`, so a reviewer can
  regenerate any image from its code.

## 9. Config decisions

- `config/metadata.yaml`: identity above; `keywords` publishing, book
  production, pandoc, LaTeX, Markdown, verification; `lang: en-US`;
  `verify-min-pages: 240`; `print: {paper: cream, profile: house-6x9}`;
  no registrations block (no ISBN is assigned; the colophon says so
  honestly by omission).
- `config/front-matter.yaml`: `dedication: "For everyone who has built a
  book twice."`; an epigraph from a public-domain printer's manual;
  `edition-note: "First edition, first printing"`; `colophon-note` naming
  the type and method; `motto` a plain line.
- `config/aesthetic.yaml`: name "Animal book, 1999"; cover grammar as in
  §8; plates medium wood engraving; web palette white paper, near-black
  ink, sepia cloth, no foil; typography stack Georgia-class serif on the
  Web, the packaged Libertinus in print; book colours black ink, dark gray
  muted, sepia accent.
- `config/house-rules.yaml`: the prose contract's one-sighting tells as
  `banned-patterns` (the regex set in the prose contract), `jargon-allow`
  for watchlist words the book must use as press's own terms (gate,
  gating, surface, surfaces, drift, parity, clean, verified, canonical,
  ship, shipped, lands, landed, round-trip, end-to-end, fallback, stale,
  scaffold, scaffolding), `audit-dirs: [docs]` off (docs is the design,
  not prose).
- `config/index-terms.yaml`: assembled from the chapters' index comments;
  150 to 250 terms.
- `tests/known-bad/`: one fixture per banned-pattern family, each with
  `<!-- expect: banned-pattern -->`.
- `assets/web/extra.css`: the tip, warning, sidebar, in-this-chapter, and
  example-caption styles for the reader and HTML editions.
- `config/metadata.yaml` `header-includes`: the LaTeX for the same
  constructs in the PDF (per the production handbook's confirmation that
  `header-includes` passes through, as Make Ready's does).

## 10. Production plan

Work runs in this repository on `main` (a new repository has nothing to
protect) with a ledger at `docs/production-ledger.md`. Each step is a
subagent dispatch with a brief file under `docs/briefs/`, a report file,
and a reviewer; the controller rules on conflicts and records them.

1. **Foundation.** Config, house rules, known-bad fixtures, extra.css,
   header-includes, tools skeleton, vocabulary, a stub chapter per entry
   in §5 so the book builds end to end from day one. Prove `press check`
   and `press all` pass locally. Commit.
2. **Chapters 1 to 16**, one dispatch each, in order, each with its brief
   (the chapter row of §5, the fact base sections it cites in full, the
   prose contract, the markup conventions, the vocabulary, the figure list
   with art directions to write). The writer writes the chapter and the
   `art:` directives for its figures, runs `press check`, and reports. A
   reviewer checks fact fidelity against the fact base, the prose
   contract, and the markup conventions, and runs the checker script.
3. **Preface and appendixes**, after the chapters, since the Organization
   section and the references depend on final titles and numbers.
4. **Figures**, in batches by archetype, from the `art:` directives: a
   figure agent writes the code, renders, and checks each image against
   the look rules; a reviewer compares image to directive.
5. **Plates and cover**, through `press illustrate`, `press art accept`,
   `press art enhance`, `tools/cover.py`.
6. **Index and sentinels.** Assemble `index-terms.yaml`; choose sentinels;
   set `verify-min-pages`.
7. **Editorial pass.** Run the humanizer checker over every chapter, then
   press's own editorial-passes workflow in report mode, apply what
   survives review.
8. **Full build and proof.** `press all` locally, `press render`, read
   the rendered pages for layout faults (widows, orphan headings, figure
   placement, table overflow), fix, rebuild. Then the print pack:
   `press verify-print` and the cover wrap.
9. **Final review** by a fresh reader on the most capable model: the
   whole PDF against the design, the fact base's §20 (nothing contradicted
   is asserted), and the prose contract.
10. **Ship.** Push to `github.com/clintecker/publishing-with-press`, let
    the book's own CI build and deploy the Pages site, and report the
    URLs.

Model seats: writers on the most capable general model available to
subagents (opus); figure code on a mid-tier model (sonnet); reviewers on
opus; the final whole-book review on the most capable model (fable).

## 11. Out of scope

- No ISBN, LCCN, or retail registration is performed; the chapter
  explains the flows with the fact base's examples.
- No image generation is run for diagrams; diagrams are code.
- No print order is placed. The cover wrap is built and verified only.
- Press itself is not modified for this book. Anything the book needed
  and press lacked is a press issue, not a book-side hack beyond the
  documented override hooks (`extra.css`, `header-includes`,
  `house-rules.yaml`, `cover-styles.yaml`).
