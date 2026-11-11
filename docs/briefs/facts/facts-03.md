### 3.1 `press new <directory> [--author A] [--publisher P] [--place PLACE] [--owner GH]`

Source: `src/press/scaffold.py`.

- **Flags:**
  - `--author`: defaults to `git config user.name`, else "The Author".
  - `--publisher`: defaults to the author.
  - `--place`: defaults to "Earth".
  - `--owner`: when given, uncomments `repository: "https://github.com/<owner>/<slug>"` and `site-url: "https://<owner>.github.io/<slug>"`. When omitted, those lines stay commented with `OWNER`.
- **Steps:**
  1. Refuses an existing path.
  2. Validates the directory name as a slug *before* copying anything.
  3. Copies `src/press/data/template`.
  4. Renames `dot-*` to `.*`.
  5. Stamps the four workflows into `.claude/workflows/`.
  6. Substitutes `{{SLUG}} {{AUTHOR}} {{PUBLISHER}} {{PLACE}} {{REPOSITORY_LINE}} {{SITE_URL_LINE}}`.
- **It does NOT run `git init`.** The README says `cd my-book && git init && make all`.
- Captured output:

  ```text
  scaffolded demo -> /…/demo
  next: edit config/metadata.yaml, write book/chapters/, run `press all`
  ```

**The exact tree** of a fresh `press new demo` (3.0.2), with notes:

```text
demo/
├── .claude/workflows/
│   ├── aesthetic-brief.js       # agent workflow: drafts config/aesthetic.yaml from a brief
│   ├── art-direction.js         # agent workflow: writes art/commissions.md
│   ├── authorities-research.js  # agent workflow: builds config/authorities.yaml
│   └── editorial-passes.js      # agent workflow: the iterative editorial machine
│                                #  (each starts "// scaffolded by press 3.0.2; source of truth: press data/workflows")
├── .github/workflows/book.yml   # the whole CI: calls clintecker/press/.github/workflows/build.yml@v3
├── .gitignore                   # build/ dist/ __pycache__/ .DS_Store
├── book/chapters/00-preface.md  # a one-paragraph preface so the empty book builds and verifies
├── CHANGELOG.md                 # Keep a Changelog; CI extracts the tagged section as release notes
├── CLAUDE.md                    # 79 lines: the book's own agent/author guide (layout, commands, house laws)
├── config/
│   ├── front-matter.yaml        # all keys commented out; its PRESENCE turns on generated front matter
│   ├── house-rules.yaml         # banned-patterns: {}, jargon-allow: [], audit-dirs: []
│   └── metadata.yaml            # identity + press facts + verification knobs (see 3.3)
├── Makefile                     # muscle-memory wrapper: every target -> python3 -m press $@
└── requirements.txt             # press @ git+https://github.com/clintecker/press@v3 (local builds only)
```

**The scaffolded files, verbatim** (slug `demo`; author is the git user):

`Makefile`:

```make
# Muscle-memory wrapper; the pipeline itself lives in the press package.
PRESS ?= python3 -m press

.PHONY: all check pdf epub html markdown site txt docx pages source verify verify-formats render wordcount clean

all check pdf epub html markdown site txt docx pages source verify verify-formats render wordcount clean:
	$(PRESS) $@
```

`requirements.txt`:

```text
# Local builds. CI does not read this file; the press action installs itself
# from its own checkout. For day-to-day work prefer an editable install of
# your press clone: pip install -e ~/path/to/press
press @ git+https://github.com/clintecker/press@v3
```

`.github/workflows/book.yml`:

```yaml
name: Build book

on:
  push:
    branches: ["**"]
    tags: ["v*"]
  pull_request:
  workflow_dispatch:

permissions:
  contents: write
  packages: read
  pages: write
  id-token: write

jobs:
  book:
    uses: clintecker/press/.github/workflows/build.yml@v3
```

`book/chapters/00-preface.md`:

```markdown
# Preface {.unnumbered}

Why this book exists, in your own voice, with no throat-clearing. Delete
this sentence and the one before it; keep the heading. This paragraph only
exists so a freshly scaffolded book builds and verifies before the first
real word lands.
```

The scaffolded `CLAUDE.md` lists these house laws, verbatim:

```text
- No em or en dashes anywhere; rewrite the sentence instead.
- Straight quotes only; sentence-case headings; no manual heading
  numbers.
- ASCII plus accented latin only; paragraphs under 190 words; no
  trailing whitespace.
- Sentinel strings in `config/metadata.yaml` must survive every
  revision verbatim; they are how the verifiers prove the book is in
  the artifacts.
- Fixtures under `tests/known-bad/` must stay rejected; they are the
  proof the checkers still work.
```


### 3.2 Manuscript layout rules

Source: `src/press/booklib.py:181-189`.

```python
chapters = sorted((root() / "book" / "chapters").glob("[0-9]*.md"))
appendices = sorted((root() / "book" / "appendices").glob("[a-z]-*.md"))
```

**Discovery.**

- **The book root** is `$BOOK_ROOT`, or else the current directory. It must contain `config/metadata.yaml`, otherwise you get "is not a book". There is no upward search.
- **Chapters** are `book/chapters/` files that start with a digit and end in `.md`. They sort lexically, so use zero-padded prefixes (`00-`, `01-` … `10-`).
- **Appendices** are `book/appendices/` files named with a single lowercase letter, a hyphen, and `.md`. They sort by filename.
- **Ignored files.** Any other `.md` in those folders is silently ignored. If none are found you get `FileNotFoundError("no manuscript files found under book/")`.
- **Merge order** is chapters, then appendices, then the generated subject index.
- **Generated appendices.** The index takes the first free appendix letter from `a`; `z` is never assigned. Note that `press add appendix` hands out letters downward from `z-`, so the generated index usually sorts *before* authored back matter. See §20.

**Preface and front parts.**

- A preface, foreword, or introduction is a `00-` chapter. `press add chapter preface --front` creates `00-preface.md` with heading `# Preface {.unnumbered}`.
- `{.unnumbered}` or `{-}` headings get no number and no drop cap.
- There is **no "part" (`\part`) support**. `top-level-division: chapter` is set, and `#` is a chapter.

**`press add chapter|appendix <name> [--front]`** (`src/press/add.py`):

- **The slug** is lowercased, with non-alphanumeric runs turned into `-`.
- **The heading.** A human title is kept verbatim; a bare slug is sentence-cased.
- **`chapter`** creates `book/chapters/NN-<slug>.md`, with NN one past the highest existing chapter. It is zero-padded to at least two digits, and the first is `01`.
- **`chapter --front`** creates `00-<slug>.md` with `{.unnumbered}`.
- **`appendix`** takes the next unused letter counting down from `z` (`z-`, then `y-`, …). **`appendix --front`** counts up from `a`. When all 26 letters are taken: "the appendices are full".
- **Stub body:** "Write this part here. This placeholder paragraph only exists so the file is valid Markdown that builds; delete it and begin."
- **Exit codes.** It refuses to overwrite (exit 1; invariant `INV-add-no-clobber`). A usage error exits 2.
- It exists so authors never `printf > file`.

**Examples** from `docs/BOOK-PARTS.md`:

```sh
press add appendix about-the-author     # -> book/appendices/z-about-the-author.md
press add appendix also-by              # -> book/appendices/y-also-by.md
press add appendix glossary             # -> book/appendices/x-glossary.md
press add chapter preface --front       # -> book/chapters/00-preface.md
press add chapter "The Long Winter"     # -> the next NN- chapter
```


### 3.3 `config/metadata.yaml`, field by field

There are two sources. The typed model lives in `src/press/bookmodel.py` and `booklib.py`. The CLI registry lives in `src/press/config_schema.py`; `press config list` output is verbatim in §17.

Pandoc also reads the raw file (`metadata-file: "@book/config/metadata.yaml"` in every defaults file), so standard pandoc keys pass through.

| Field | Type | Default | Meaning / rules |
|---|---|---|---|
| `title` | str | required | The book's title. |
| `subtitle` | str | none | Its `or,` clauses stack on the title page and the landing page. |
| `author` | str or list[str] | required | Byline. A single string is normalized to a tuple. `press config set` needs `--json` for lists. |
| `date` | str | none | Free text. The first `1xxx`/`2xxx` year becomes the EPUB `dc:date` and the title page's lowercase roman numerals. |
| `copyright` | str | none | Required once `config/front-matter.yaml` exists. |
| `publisher` | str | none | Imprint. Required with front matter. Also exported to TeX as the env var `BOOK_PUBLISHER`. |
| `publisher-place` | str | none | Required with front matter. |
| `description` | str | none | One-sentence blurb. **`press check` requires it** (`check_source.py:45-51`). |
| `slug` | str | required | Must match `[a-z0-9][a-z0-9-]*`. It is every artifact's basename. |
| `repository` | str | none | Canonical repo URL. Absent: the landing page omits its source paragraph. |
| `site-url` | str | none | Public Pages URL. The one authority for every absolute URL, canonical link, `og:image`, and sitemap. Absent: nothing URL-shaped is emitted. |
| `keywords` | list[str] | none | Passed to the formats. |
| `lang` | str | none | BCP-47 tag passed through to pandoc. The template sets `en-US`. |
| `rights` | str | none | Passed through to pandoc. |
| `verify-sentinels` | list[str] | `[]` | Phrases proven present in the source and in every artifact. Exact case; curly and straight quotes are equated. A release needs at least 2. |
| `verify-min-pages` | int | 40 in the model; **the template sets 1** | PDF page floor. A release needs at least 24. |
| `trim` | IMMUTABLE | derived | "trim is not set directly; choose it with print.profile". A legacy mapping is only cross-checked, and refused on disagreement. |
| `print.profile` | str | `house-6x9` | Design profile: trim and interior geometry (§10). |
| `print.provider` | str | `house` | Provider spec: spine and cover geometry. |
| `print.binding` | str | `perfect-bound` | Or `saddle-stitch`, `coil`, `casewrap`, `dust-jacket`. |
| `print.material` | str | `paperback` | Or `casewrap`, `linen`. |
| `print.paper` | str | `cream` | `white` or `cream`. |
| `print.page-thickness` | float | none | Inches per page. Overrides paper. |
| `print.color-grade` | str | standard | e.g. `standard-color`, `premium-color`. Colour profiles only. |
| `chapter-opening.style` | str | the profile's (house: `none`) | `none`, `drop-cap`, `raised-cap`, `ornate`. |
| `chapter-opening.lines` | int | 3 | Text lines the initial spans. |
| `chapter-opening.small-caps-remainder` | bool | true | Small caps for the rest of the first word. |
| `registrations.isbn.print` / `.epub` | str | none | ISBN-13 or `pending`. |
| `registrations.lccn` / `.issn` | str | none | Or `pending`. |
| `registrations.retail` | bool | false | `true` makes missing or pending numbers fail `check`. |
| `registrations.isbn-block.prefix` / `.size` | str / int | none | Owned registrant prefix. Size is 10, 100, or 1000. |
| `commerce.print-ordering.*` | various | off | See §10.9. |

**The release rule.** With `PRESS_RELEASE=1` (CI sets it on `refs/tags/v*`), `booklib.require_release_witnesses()` refuses vacuous witnesses:

```text
this is a release build (PRESS_RELEASE=1) and its witnesses are vacuous:
verify-sentinels has N entries; a release needs at least 2 distinctive prose fragments
verify-min-pages is N; a release needs at least 24
```

**Choosing sentinels.**

- Pick them mid-chapter. The drop cap splits and small-caps a chapter's opening word, which breaks exact PDF matching. This comes from the maintainer's own practice notes.
- The template's own advice: "pick 2-4 phrases from your actual manuscript, each distinctive enough to appear exactly once (a whole memorable clause, not a common word)".

**The scaffolded `config/metadata.yaml`**, verbatim with `{{…}}` filled:

```yaml
title: "demo"
subtitle: "A subtitle"
author:
  - "Clint Ecker"
date: "First edition, 2026"
lang: en-US
copyright: "Copyright 2026."
publisher: "Clint Ecker"
publisher-place: "Earth"
description: >-
  One honest paragraph on what this book is.
keywords:
  - writing

# Press facts: artifact basename, canonical repo, and the public Pages URL
# release notes link to (omit site-url to skip public download links).
slug: "demo"
# repository: "https://github.com/OWNER/demo"
# site-url: "https://OWNER.github.io/demo"

# Verification knobs. Sentinels are prose fragments every rendered
# format must contain: pick 2-4 phrases from your actual manuscript,
# each distinctive enough to appear exactly once (a whole memorable
# clause, not a common word). Empty sentinels and a one-page floor are
# DRAFT settings; a release build (CI on a tag) refuses them until at
# least 2 sentinels and verify-min-pages >= 24 are set.
verify-sentinels: []
verify-min-pages: 1
# trim: {width: 6, height: 9}

# The print pack reads these when building the interior and cover wrap.
# print: {paper: cream}          # or white; or {page-thickness: 0.0025}

# Registrations: validated by press check, injected into the colophon,
# EPUB metadata, and the wrap barcode. "pending" is the one honest
# placeholder; retail: true refuses to pass check while any placeholder
# remains. See the registrations skill for the actual processes.
# registrations:
#   isbn:
#     print: "pending"           # check digit validated when real
#     epub: "pending"
#   lccn: "pending"
#   retail: false

# Direct print ordering: ... (commerce block, commented; see 10.9)
```

The real file contains the full commented commerce block. It mentions "press qualify", **which is not a command**.

The other two scaffolded configs, `config/house-rules.yaml` and `config/front-matter.yaml`, are quoted verbatim in §6.4 and §9.1.


### 3.4 The first-run loop

From `docs/QUICKSTART.md`:

```sh
press new my-first-book
cd my-first-book
press config set title "My First Book" && \
  press config set subtitle "And how it came to be" && \
  press config set author '["Your Name"]' --json && \
  press config set description "One honest paragraph on what this book is."
press check
press all
ls dist/
press pages      # then open dist/pages/index.html
git init && git add -A && git commit -m "First book" && \
  git remote add origin https://github.com/OWNER/my-first-book && git push -u origin main
```

Then enable GitHub Pages once: Settings → Pages → Source: GitHub Actions.

**`press check` on a fresh scaffold** (captured, exit 0):

```text
Source checks passed: 1 ordered Markdown files
  note: em-dash.md also drew: - /…/src/press/data/known-bad/em-dash.md:4: glyph U+2014 is outside the print-font set
  note: en-dash.md also drew: - /…/src/press/data/known-bad/en-dash.md:4: glyph U+2013 is outside the print-font set
Checker self-test passed: 19 known-bad fixtures each tripped their declared rule, known-good fixture accepted, 2 extra diagnostics noted
Editorial checks passed: 1 Markdown files
Jargon check passed: no rewrite-status terms (full audit in build/jargon-report.txt)
```

**`press wordcount`** (captured):

```text
    42  book/chapters/00-preface.md
    42  TOTAL
```

It strips fenced and inline code and counts `\b[\w'-]+\b`. It does not strip HTML comments, so `art:` directives are counted.

**`press figures`** on a fresh book prints `[]`.

**Common first-run refusals** (`docs/QUICKSTART.md` §6):

- `pandoc is required`
- a style or jargon failure
- `sentinel ... not found`
- a first-run font-scan "hang"
- CI dying at "Initialize containers" (retry; the image is public)


### 3.5 `dist/` and `build/` layout after `press all`

`dist/` holds every published artifact, named from the registry (`src/press/registry.py:28-72`):

```text
dist/
├── <slug>.pdf             # reading PDF (Print edition on the landing page)
├── <slug>.epub            # Circulating edition
├── <slug>.html            # Single-leaf edition (self-contained)
├── <slug>.md              # Manuscript edition (stitched raw source, not pandoc-rendered)
├── <slug>.txt             # Telegraphic edition (80 columns)
├── <slug>.docx            # Office edition
├── <slug>-site.zip        # Chapter edition, boxed
├── <slug>-source.zip      # Source edition (git-tracked files only)
├── <slug>-sources.md      # Table of authorities (only with config/authorities.yaml)
├── site/                  # the per-chapter reader (index.html, reader.css, chapter pages, assets/)
└── pages/                 # the GitHub Pages bundle
    ├── index.html         # landing page
    ├── read/              # copy of dist/site
    ├── downloads/         # every published download, linked exactly once
    ├── cover.jpg, press-logo.png, woodcuts/   # when present
    ├── support.html privacy.html refunds.html # only when ordering is enabled and policy URLs are omitted
    └── sitemap.xml, robots.txt                 # only when site-url is set
```

The print pack, built only by `press print`, `verify-print`, or `coverwrap`, adds:

- `dist/<slug>-interior.pdf`
- `dist/<slug>-coverwrap.pdf`

The registration commands add:

- `dist/<slug>-pcn.txt` (`press pcn`)
- `dist/<slug>.onix.xml` (`press onix`)
- the publish checklists (§10)

`build/` holds intermediates. Notable entries:

- `build/defaults/<name>.yaml`: rendered pandoc defaults
- `build/generated/<letter>-index-of-subjects.md`
- `build/front-matter.tex`
- `build/aesthetic.tex`
- `build/profile-geometry.tex`
- `build/profile-dropcap.tex`
- `build/print-assets/`: flattened print-safe images
- `build/cover-fragment.html`
- `build/epub-metadata.xml`
- `build/verify-text.txt`
- `build/jargon-report.txt`
- `build/rendered-book/page-*.png` (`press render`, 160 dpi)
- `build/editorial-report.md` and `build/editorial-rejections.md` (workflows)
- `build/cover/cover.png` and `build/illustrations/<name>.png` (art)
- `build/dev-render/` (the press-repo dev loop)

`press clean` deletes `build/` and `dist/`.

Other generated state:

- `.press/migration-receipt.json` (migrate)
- `art/candidates/…` (art commission)


### 17.3 Configuration reference: `press config list` (captured verbatim)

```text
  title                                     str       the book's title (required)
  subtitle                                  str       the subtitle; OR clauses stack on the title page
  author                                    list[str] byline, one name per list item (required)
  date                                      str       free text; the first year in it dates the EPUB
  copyright                                 str       copyright line (required once front-matter.yaml exists)
  publisher                                 str       imprint (required with front matter)
  publisher-place                           str       imprint place (required with front matter)
  description                               str       one-sentence blurb for the landing page and stores
  slug                                      str       artifact basename; [a-z0-9][a-z0-9-]* (required)
  repository                                str       canonical repo URL (optional)
  site-url                                  str       public Pages URL (optional)
  keywords                                  list[str] subject keywords for the formats
  lang                                      str       BCP-47 language tag passed through to pandoc
  rights                                    str       rights statement passed through to pandoc
  verify-sentinels                          list[str] phrases proven present in every artifact (release needs >=2)
  verify-min-pages                          int       PDF page floor (release needs >=24)
  trim                                      IMMUTABLE page trim; derived from print.profile
                                                      -> trim is not set directly; choose it with print.profile
  print.profile                             str       design profile id: trim and interior geometry (default house-6x9)
  print.provider                            str       provider spec for spine and cover geometry (default house)
  print.binding                             str       binding style
  print.material                            str       cover material
  print.paper                               str       interior stock
  print.page-thickness                      float     inches per page; overrides paper
  print.color-grade                         str       color-interior stock grade for the provider (e.g. standard-color, premium-color); used only by a color design profile
  chapter-opening.style                     str       chapter-opening initial
  chapter-opening.lines                     int       text lines the initial spans
  chapter-opening.small-caps-remainder      bool      set the rest of the first word in small caps
  registrations.isbn.print                  str       print ISBN (13 digits) or 'pending'
  registrations.isbn.epub                   str       EPUB ISBN or 'pending'
  registrations.lccn                        str       LCCN or 'pending'
  registrations.issn                        str       ISSN or 'pending'
  registrations.retail                      bool      true makes missing/pending registrations fail check
  registrations.isbn-block.prefix           str       owned ISBN registrant prefix (e.g. 978-1-960780); 'press isbn assign' mints from it
  registrations.isbn-block.size             int       block size Bowker sold: 10, 100, or 1000
  commerce.print-ordering.enabled           bool      turn the order CTA on
  commerce.print-ordering.edition           str       the edition sold (e.g. paperback)
  commerce.print-ordering.storefront-url    str       must be an https URL
  commerce.print-ordering.seller-of-record  str       who the reader buys from
  commerce.print-ordering.support-url       str       support page must be an https URL (optional; omit to generate)
  commerce.print-ordering.privacy-url       str       privacy page must be an https URL (optional; omit to generate)
  commerce.print-ordering.refund-url        str       returns page must be an https URL (optional; omit to generate)
  commerce.print-ordering.policies.support  str       your own text appended to the generated support page
  commerce.print-ordering.policies.privacy  str       your own text appended to the generated privacy page
  commerce.print-ordering.policies.refund   str       your own text appended to the generated returns page
  banned-patterns                           mapping   regex -> label; applied by the style audit
  jargon-allow                              list[str] watchlist terms this book may use
  audit-dirs                                list[str] extra directories to lint beyond book/
  edition-note                              str       edition line (falls back to the date)
  dedication                                str       dedication page text
  epigraph.quote                            str       epigraph text (gates the epigraph page)
  epigraph.attribution                      str       epigraph attribution
  acknowledgements                          str       acknowledgements page text
  rights-notice                             str       colophon rights line
  manufacture                               str       colophon manufacture line
  colophon-note                             str       colophon typography note
  contact                                   str       colophon contact line
  motto                                     str       colophon motto
  name                                      str       the aesthetic's name
  register                                  str       the register/voice of the design
  cover.style                               str       cover style id from the style library (default penguin-tri-band)
  cover.subject                             str       the subject of the cover illustration, one phrase
  cover.medium                              str       cover medium (prompt material)
  cover.field                               str       cover field/composition
  cover.ink                                 str       cover ink treatment
  cover.type-treatment                      str       cover type treatment
  cover.ornament                            str       cover ornament
  cover.emblem                              str       cover emblem placement
  plates.style                              str       default illustration style id (default wood-engraving)
  plates.medium                             str       interior plate medium
  plates.composition                        str       interior plate composition
  logomark.tradition                        str       logomark tradition
  portrait.style                            str       author portrait style
  scene-break                               str       thematic-break ornament (rule, asterism, or fairy-dust)
  typography.web-family                     str       CSS font stack for the web reader
  typography.pdf-family                     str       LaTeX main font ('' keeps Libertinus)
  web-palette                               mapping   light-theme token -> #hex
  web-palette-dark                          mapping   dark-theme token -> #hex
  book-colors.ink                           str       PDF ink color, hex without #
  book-colors.muted                         str       PDF muted color, hex without #
  book-colors.accent                        str       PDF accent color, hex without #
  book-colors.link                          str       PDF link color, hex without #
  index-terms                               STRUCTURED curated subject-index terms (a list)
                                                      -> edit config/index-terms.yaml or curate with the index workflow
  authorities                               STRUCTURED the table of authorities (a list)
                                                      -> populate with the authorities-research workflow
  qualification                             STRUCTURED physical-inspection records (schema_version + inspections)
                                                      -> record a physical qualification; edition_id comes from press
  tex/title-page.tex                        FILE      hand-authored front matter override
                                                      -> author the .tex file directly
  assets                                    FILE      cover, logo, plates, author photo, and web CSS
                                                      -> place the files under assets/ (and art/)
```

**File routing.** Fields map to files:

- `metadata.yaml`: identity, verification, `print.*`, `chapter-opening.*`, `registrations.*`, `commerce.*`.
- `house-rules.yaml`: banned-patterns, jargon-allow, audit-dirs.
- `front-matter.yaml`: edition-note through motto.
- `aesthetic.yaml`: name through book-colors.

**Kinds.** Each field is one of `writable`, `immutable`, `structured`, or `file`. Lists and mappings need `--json`. Booleans accept true/yes/on/1 and false/no/off/0.

**Choices:**

| Field | Values |
|---|---|
| `print.binding` | perfect-bound, saddle-stitch, coil, casewrap, dust-jacket |
| `print.material` | paperback, casewrap, linen |
| `print.paper` | white, cream |
| `chapter-opening.style` | none, drop-cap, raised-cap, ornate |
| `scene-break` | rule, asterism, fairy-dust |

**Validation.** Every write is validated by the real typed model for its file *before* writing: bookmodel plus commerce plus registrations for metadata, and the regex compiler for house rules. `aesthetic.yaml` has no validator.

`press config validate` (captured):

```text
config/metadata.yaml: ok
config/house-rules.yaml: ok
config/front-matter.yaml: ok
config/aesthetic.yaml: ok
config/index-terms.yaml: ok
config/authorities.yaml: ok
```

**Other book files** a writer should know:

- `config/cover-styles.yaml` and `config/illustration-styles.yaml`, which merge over the house style libraries;
- `config/qualification.yaml`;
- `tex/title-page.tex` and `tex/title-page-print.tex`;
- `assets/cover.jpg`, `assets/press-logo.png`, `assets/author.jpg`, `assets/woodcuts/*.png|*.jpg`, `assets/web/reader.css`, `assets/web/extra.css`;
- `art/author-photo.jpg`, `art/commissions.md`, `art/candidates/`;
- `tests/known-bad/*.md`.


---

# Shared context (every chapter)

### 1.4 Philosophy

**The four laws** (`docs/ARCHITECTURE.md`):

> 1. **Facts are stated once.** A book's identity lives in its config; the house design lives in press data; the artifact graph lives in the registry. If you find the same fact in two places, one of them is a bug already filed or a bug you should file.
> 2. **Generators over checkers over conventions.** Prefer machinery that produces the right thing to machinery that detects the wrong thing, and either to a sentence in a document asking people to behave.
> 3. **Artifacts are verified as objects.** A green build means the actual PDF was rendered and inspected, the actual EPUB was validated by the tool retail channels run, the actual site was crawled. Verifying without rebuilding is forbidden by construction.
> 4. **Scars become law.** Every production failure earns a mechanical guard and an entry in CLAUDE.md's scars list. Do not relearn them.

**Product laws** (`ROADMAP.md`):

- Facts are stated once and projected mechanically.
- Generators establish structure; verifiers prove artifacts as objects "rather than trusting command exit status".
- "A scar becomes an executable invariant, a named proof, or an explicit public contract—not merely a warning in prose."
- Valid output stays compatible within a major.
- Book repositories contain book facts only.
- "Trust accumulates from deterministic functions through compositions, real tools, complete workflows, consumer repositories, and release identity. A higher layer cannot erase missing proof below it."

**No book in the press.** From `CLAUDE.md`:

> There is no book in here. Every book-specific fact (title, slug, sentinels, banned vocabulary, front matter, art) lives in the book repository that consumes this package.

Also: "if a book needs machinery, the machinery belongs here". This is enforced. The integration gate requires that "no original-book identity may appear in a clean scaffold's public artifacts", and selftest `scaffold_neutrality` checks that a scaffolded book contains no "Clint Ecker" or "LGTM".

**Provenance vs verification** (`docs/ARCHITECTURE.md`):

> generation makes a fact true, verification proves it stayed true all the way into the object a reader receives.

**The pinned contract.** Books pin a tag. `vN` floats; three-part tags are immutable "and immutability is enforced, not promised". "Design is part of the contract: within a major, fixes may correct broken output but must not change typography or layout of a valid book; design and template changes require a new major." See §12.

**Non-goals** (`docs/NON-GOALS.md`). "Press is a prose engine." It is not:

- a page-layout or design application (it does not replace InDesign, Affinity, Scribus, or Quark);
- a fixed-layout picture-book, comic, or magazine designer;
- an interactive or rich-media ebook builder.

The heuristic: "a new profile of the prose engine -- another trim, a colour interior, large print -- is core press work; a new *engine* is not." The planned answer for designed interiors is the *finisher*, a supplied-interior source mode (`interior: path/to/interior.pdf`). It is planned work on the Book breadth milestone, not shipped.

**What the author owns and what the press owns** (`docs/QUICKSTART.md`):

- "Yours to decide": title, author, words, and the visual identity.
- "The press owns": build order, verification pipeline, file names, and formats.

---


## 19. War stories, scars, and design rationales (sidebar candidates)

Each entry names its source. Lines are 1-based.

1. **The infinite empty pages.** "A figure taller than the text block makes LuaLaTeX ship empty pages forever, silently, at 100% CPU." The fix caps every image at 6.3in (now per profile), and "never stack a third `titlepage`". Sources: `CLAUDE.md:178-182`; `src/press/data/tex/book-header.tex:148-186`.
2. **The missing Libertine face.** "Ubuntu has no `fonts-libertinus` package, and `--no-install-recommends` drops the Libertine keyboard face; the Dockerfile states `fonts-linuxlibertine` explicitly." Source: `CLAUDE.md:183-185`.
3. **The epubcheck that exists but cannot run.** Ubuntu's launcher needs binfmt_misc, which containers do not register. "the command exists, `which` finds it, and it dies with 'Exec format error' only at execution." The fix is a `java -jar` wrapper, and a present-but-unrunnable tool is reported as a toolchain fault. Sources: `CLAUDE.md:186-190`; `Dockerfile:41-46`; `src/press/verify_formats.py:399-440`. The Real-ESRGAN comment in the Dockerfile calls the same trap "the epubcheck/binfmt scar".
4. **The lists that would not converge.** Plain lualatex under pandoc does not run enough passes, so the build goes through latexmk. Also, `toc-depth: 1` silently empties the List of Plates; the header raises tocdepth inside the lof file. Sources: `CLAUDE.md:191-194`; `book-header.tex:104-139`.
5. **Links that overshoot.** hyperref anchors floats at the caption, so list-of-plates links overshoot the image. The fix moved from the `hypcap` package to `caption`'s `hypcap=true`. "When touching PDF links, verify destinations with pypdf". The verifier now does so. Sources: `CLAUDE.md:195-197`; `src/press/verify_pdf.py:44-104`.
6. **The chunked writer copies media itself.** Site assembly must tolerate directories that already exist (`dirs_exist_ok=True`). Sources: `CLAUDE.md:198-199`; `src/press/build.py:319-341`.
7. **JPEG plates, then PNG masters.** "Truecolor PNG barely compresses engraving grain, which is why plates were once baked JPEGs". `press art enhance` quantizes to a few grays, and intake keeps alpha PNG masters. "Do not reintroduce a baked-white JPEG master." Sources: `CLAUDE.md:200-204`; CHANGELOG 3.0.0 (#226).
8. **Blessing stale artifacts.** "Verifying `dist/` without rebuilding blesses stale artifacts; the CLI's dependency edges exist so that cannot happen." This is enforced by `INV-graph-no-stale` (critical). Source: `CLAUDE.md:205-206`.
9. **The renderer fallback.** The verifier renders with `pdftoppm` when the authoring sandbox's renderer is absent. "Keep that fallback working." Sources: `CLAUDE.md:207-208`; `verify_pdf.py:21,336-355`.
10. **The hang that isn't.** The first LuaLaTeX run spends several minutes on a font scan. Sources: `CLAUDE.md:209-210`; also stated in QUICKSTART and INSTALL.
11. **A red check that shipped green.** "Never pipe a check command into grep before `&&` in a commit chain; the pipeline exit code is grep's, and a red check once shipped as green." Source: `CLAUDE.md:211-212`.
12. **The KOMA spelling trap.** In print, `open=any` must be spelled the KOMA way. "the standard-class spelling openany is silently ignored under twoside". `open=right` "would ship genuinely blank versos". Source: `src/press/data/defaults/print.yaml:3-7`.
13. **epubcheck versus pandoc's empty date.** pandoc emits an empty `dc:date`, which epubcheck rejects (RSC-005). The press therefore writes a year extracted from the prose date into `build/epub-metadata.xml`. Source: `src/press/build.py:594-623`.
14. **`CI=false` is truthy.** Toolchain strictness is keyed on `PRESS_TOOLCHAIN`, set in the image, "not the ambient CI variable". Source: `src/press/verify_formats.py:408-411`.
15. **The barcode that crowded its quiet zone.** A TikZ node's default padding shifted the EAN-13, so `verify-print` refused a correct wrap. The fix is `inner sep=0` on the node. Sources: CHANGELOG 2.3.1 (#210); `src/press/gen_coverwrap.py:393-400`.
16. **The five-percent box.** gpt-image lays its "white" ground near `#f1f2f3`. A naive inversion leaves "a five-percent box that is glaring on cream paper", so the luminance key starts at 225. Source: `src/press/art.py:67-73`.
17. **Literal, silly plates.** Commissions used to draw from captions, which produced "literal, silly plates". Now a figure with no `art:` description is refused: "A caption is a label, not art direction (#225)". Sources: `docs/ILLUSTRATIONS.md`; `src/press/illustrate.py:118-141`.
18. **The cover that invented its own subject.** Before v2.3.1, a book that named its subject only in `description` got "the book's subject" literally, and the model invented generic motifs. A fallback chain now applies. Sources: CHANGELOG 2.3.1; `src/press/cover.py:71-84`.
19. **Release automation that rewrote mypy.** An unanchored version regex in the release script "once rewrote [tool.mypy]'s python_version". It is now anchored, with `count=1`. Source: `scripts/release.sh:91-93`.
20. **11.5% coverage, broken covers.** "a title-page generator shipped a dropped and a clipped cover at 11.5% coverage: the lines ran, the artifact was never inspected." Hence "A producer is only proven by a verifier that rejects a broken artifact." This is also why the PDF verifier checks the cover on page 1. Source: `CONTRIBUTING.md:85-90`.
21. **The vacuous test.** A title-tie test passed with no filter, because pandoc ties `Mr.` itself. It was found by the 3.0.2 Lua coverage backfill, and the Lua tests had been silently skipping in CI until `PRESS_REQUIRE_LUA=1`. Source: `CHANGELOG.md:30-40`.
22. **A stray asterisk and "Fig-ure".** The float package's `\caption*` printed a stray asterisk above placed figures. A narrow wrap could hyphenate "Figure". The fixes were the caption package as the single caption authority and an `\mbox` around the label. Source: `CHANGELOG.md:140-150`.
23. **The 602-PPI logo.** Lulu flagged a 1024px logo printed at 1.7in as over 600 PPI, and flagged the logo's transparency. The print-safe pass now flattens every image and caps its resolution. Sources: `docs/LULU.md`; `src/press/print_safe.py`.
24. **An honest refusal beats a guessed thickness.** A colour interior is refused at Lulu and IngramSpark because no colour caliper is sourced: "the press will not guess a thickness". Sources: `docs/PRINT-FORMATS.md`; `src/press/provider_specs.py:87-101`.
25. **A migration that promised too much.** `press migrate` told v2→v3 users their geometry would be byte-for-byte unchanged. That was true only for v1→v2. Fixed in 3.0.1 (#262). Sources: `CHANGELOG.md:42-56`; `src/press/migrate.py:161-185`.
26. **The macOS runner retired mid-release.** GitHub retired `macos-14` ("configuration not supported", cancelled within a second), so the job moved to `macos-15`. Sources: CHANGELOG 3.0.0; `docs/COMPATIBILITY.md`.
27. **Forty-one Pillow advisories.** Five were critical. The hash lock made this a one-package bump: `scripts/lock-deps.sh --upgrade-package pillow`. Source: CHANGELOG 3.0.2.
28. **The subprocess gate's blind spot.** The adapters boundary gate missed `from subprocess import Popen`, and the desk launcher did exactly that. The gate now resolves aliases, and the launcher moved into `press.adapters`. Source: CHANGELOG 2.3.1.
29. **Sentinels on a drop cap.** The drop cap splits and small-caps a chapter's first word, so a sentinel placed there fails exact PDF matching. Choose mid-chapter phrases. Sources: the maintainer's notes; `src/press/data/lua/chapter-dropcap.lua`.
30. **The ghost of a gradient.** The luminance key reads every dark pixel as ink, so a gradient ground "survives as a smudge". Since 3.0.0, intake judges the border and refuses, naming the fix. Sources: CHANGELOG 3.0.0; `src/press/art.py:94-133`.

Design rationales that work as sidebars:

- **Why pip-from-git is not used in CI.** A private book needs no cross-repo token, and the installed press is pinned to the exact action ref (`CLAUDE.md:20-25`).
- **Why the index uses chapter labels rather than page numbers.** "both stay put across editions, which page numbers do not" (`src/press/gen_index.py:71-73`).
- **Why there is no plugin loader.** "Behavior cannot come from the accident of which package imported first" (`docs/ARCHITECTURE.md`).
- **Why the jargon checker exists twice.** The skill must work without the press installed, and a byte-parity contract keeps the two copies identical (`docs/WORKFLOWS.md`).
- **Why the hard-coded "diseases".** "'apply the skills' alone produces locally-obedient, globally-patterned prose" (`CLAUDE.md`).
- **Why the toolchain image is pinned by digest.** The `sha-` tag is mutable; a digest pins bytes (`CLAUDE.md` "The contract").
- **Why `main` takes direct pushes.** Trust is enforced at the release boundary, the tag (`SECURITY.md`, #153).

---


## 20. Open questions and contradictions (writers: avoid or hedge these)

### A. Docs contradict code. Follow the code.

1. **"In v1 the page trim is 6 x 9"** (`docs/QUICKSTART.md`, "What you are building"). This is stale. v2 and later have six profiles. The README still says "verified 6 x 9 PDF". That is the default, not the only option.
2. **The toolchain pin.** ARCHITECTURE.md ("Design versioning") and COMPATIBILITY.md say three-part tags pin "an existing immutable `sha-` tag". CLAUDE.md and `release-contract.yml` say a `sha-` tag alone is mutable and refused; an `@sha256:` digest is required. Use the digest wording.
3. **The invariant ledger's location.** ARCHITECTURE.md says `quality/invariants.yaml`. The real file is `.celebrimbor/invariants.yaml`. EXTENSION-CONTRACT.md likewise says `quality/surfaces.yaml`; the real file is `.celebrimbor/surfaces.yaml`.
4. **hypcap.** CLAUDE.md says the `hypcap` package is "loaded in the hyperref after-hook". Code: the package was removed, and `caption`'s `hypcap=true` does the job (`book-header.tex:134-139`).
5. **The 6.3in cap.** CLAUDE.md states it as universal. It is the house profile's value; other profiles use 4.8–7.2in. The cover-design and plates skills say 7.1in. Use "per profile; 6.3in on the house 6×9".
6. **"Page-accurate subject index" / "will not print a wrong page number"** (`docs/BOOK-PARTS.md`). The index lists chapter numbers and appendix letters, not pages.
7. **Index placement.** BOOK-PARTS shows the index last in the back matter. It takes the *first* free letter from `a`, while `press add appendix` assigns `z-`, `y-`… So the index usually sorts *before* authored appendices.
8. **Appendix lettering.** The scaffolded book `CLAUDE.md` says appendices order "by letter prefix (`a-`, `b-`, ...)". `press add appendix` counts down from `z-`. Both orderings are valid filenames; describe `press add`'s behavior.
9. **`verify-min-pages` default.** CONFIGURATION.md says "default 40", which is the model default. The scaffold template writes `1`.
10. **`tests/known-bad` "on every build"** (CLAUDE.md). The fixtures run in `press check` and `press all`, not in a bare `press pdf`.
11. **ILLUSTRATIONS.md widths.**
    - It says full-bleed and frontispiece "ignore width". The validator *refuses* a measure on a non-in-flow place.
    - It says a `plate` sits at its width, yet also that a measure on a plate is refused.
    - `place=margin` is an outer wrap inside the column, not a true margin figure.
    - "full-bleed" does not bleed: it is a cleared leaf inside the margins.
12. **"Seller of record: Lulu"** (PRINT-ORDERING, QUICKSTART). The provider ledger records Lulu `seller_of_record: unsupported` ("the publisher is the seller in the custom route"). Only Peecho is marked supported. Do not assert that Lulu is legally the seller of record. Say press's *model* is provider-as-seller and the publisher must confirm.
13. **LULU.md spine claims.** "Set the paper first so the spine math is right." With `print.provider: lulu`, the paperback spine is `pages/444 + 0.06`, independent of paper. The default provider is `house` (KDP-like calipers, 0 allowance), not Lulu. A Lulu-bound book should set `print.provider lulu`; the doc never says so for paperbacks.
14. **COMPATIBILITY.md** says "Each release records the toolchain image digest ... in its notes". Notes come from the CHANGELOG; the digest lives in the release receipt artifact.
15. **COVER-STYLES.md.**
    - `text: composited` "have the press set type": nothing implements compositing.
    - "Every style prints in your book's `accent`": the code reads `web-palette.accent`, which the house palette does not define, so the hard-coded `#7a2325` is used.
    - The doc says each card is a different book and later "the same book in each".
16. **Cover sizes.** `press cover` asks gpt-image-2 for 1024×1536. `press art commission` asks for 2304×3456. Intake checks only the aspect ratio (±3%), never resolution or DPI.
17. **Cover aspect check vs profile.** `art accept --as cover` reads `metadata.trim` (default 6×9), not the profile. A 5×8 book's cover is checked against 1.5, not 1.6.
18. **Plate greying.** "Intake greys it to the single interior ink." This happens only when `plates.medium` contains both the words "single" and "ink" (the house text does) and the profile is not colour.
19. **DESK.md.**
    - The evidence states `*` and `!` cannot appear in the live desk, because no evidence is passed and present artifacts show `o`.
    - The keymap omits `c` (cancel).
    - CLAUDE.md says every config field is settable from the wizard; only title, subtitle, author and description are.
20. **WORKFLOWS.md and CLAUDE.md skill lists** omit `book-aesthetics` and `profile-lifecycle`. `press skills` lists 11.
21. **Extension contract major 3 and `config/extensions.yaml`** are documented but not implemented. `SUPPORTED_CONTRACT_MAJORS = (2,)` even in v3.
22. **`press add` summary.** The catalog says "Add a chapter, appendix, or front-matter part". There is no front-matter part type: `--front` means a `00-` chapter or an `a-` appendix.
23. **Help grammar omissions.** `art enhance`, `cover --print`, `illustrate --subject/--print`, `improve --rounds`, `research --max-claims-per-file`, `aesthetic --overwrite`, `new --author/--publisher/--place/--owner`, `config --json/--dry-run/--file`, and `selftest --write-docs` all exist in code but not in `--help`.
24. **`verify-pages`** appears in README's "Checking" list and REFERENCE.md but not in `press --help`. It is an alias of `pages`.
25. **The metadata template comment** says "Enable it once the edition is qualified (press qualify)". There is no `press qualify` command. The qualification is recorded by hand in `config/qualification.yaml`.
26. **README's quick start** says `press new my-book; cd my-book && git init && make all`. That is accurate: `press new` does not `git init`, and the source zip needs git-tracked files, so `git init` plus an add/commit matters before `press source` and `press all`. This is inferred from the policy's "tracked files only" and should be verified before writers claim it.
27. **`docs/GALLERY.md`** says nine example cards lead with covers, but also says "the cards above are typographic rather than photographic". `build_examples.py` comments say "eight" examples; there are nine.

### B. Code behaviors that look like bugs. Do not document them as features.

1. **Print interior side margins.** `print-header.tex` re-sets `inner=0.88in,outer=0.58in` after the profile geometry. Every print interior may therefore get the house 6×9 side margins, regardless of profile. This comes from reading include order and was not verified by a build.
2. **Possibly missing print images.** `print-safe-images.lua` redirects *all* `assets/…` images to `build/print-assets/`. `print_safe` copies only the logo, top-level `assets/*.jpg` and `assets/woodcuts/*`. A figure at `assets/fig/x.jpg` (the docs' own example path) could be missing from the print interior. Unverified.
3. **Hard-coded 6×9 text.** The landing page's PDF row, the `publish` checklist trim, and the coverwrap back-text width all read the legacy `metadata.trim`, defaulting to 6×9, not the profile. Non-6×9 books show "6 by 9", and their back-cover text box may overrun into the spine.
4. **Unused provider minimums.** Spine-text minimums (KDP 79, Lulu 81, Ingram 48 pages) and provider `safety` values are declared but unused. Spine text is drawn whenever the spine is at least 0.25in. No even-page or saddle-stitch divisible-by-4 rule is enforced.
5. **`print.page-thickness`** is ignored for Lulu hardcovers. The IngramSpark dust-jacket spine uses the paperback PPI formula.
6. **Page-count bounds** are checked only inside cover-wrap generation, so a coverless book's page count is never bounded.
7. **`raised-cap`** renders identically to `drop-cap`.
8. **`lang="en"` is fixed** on the landing page, policy pages and JSON-LD `inLanguage`, ignoring metadata `lang`. The reader uses `$lang$`.
9. **The Markdown edition** is raw stitched source. `::: verse` divs, figure attributes and `<!-- art: -->` comments ship as written.
10. **The txt and docx editions** have no drop cap and no scene-break ornament.
11. **`press verify-formats`** includes an existing, possibly stale, `dist/<slug>.pdf` in the cross-edition agreement check without rebuilding it.
12. **`press verify-print`** builds the print interior twice when a cover exists.
13. **`press all`** builds neither `print` nor `coverwrap`, but the commerce release gate (ordering-enabled books only) does.
14. **The doctor and `pdfimages`.** Doctor does not check `pdfimages`, and its absence silently softens two checks to notes. A broken *optional* tool fails doctor.
15. **Gemini spends by default.** `press art commission` sends to both OpenAI and Gemini with no confirmation. Without `GEMINI_API_KEY` it exits after already paying for the OpenAI images.
16. **Plate shape keywords.** A plate prompt lacking the exact words "landscape composition" or "portrait composition" is generated square.
17. **`events.py`** (the child-event protocol) and the Lulu Print API adapter are not wired to any runtime path.
18. **Inconsistent check selection.** `release.sh` picks the `consumer` check with `first`; the release contract uses `sort_by(.started_at) | last`.
19. **The Dockerfile** installs PyYAML (unused) and unpinned Pillow. The action reinstalls from the hash lock anyway.
20. **ISBN minting** starts at publication number 0. ONIX always emits `NotificationType 03`, even with `--forthcoming`.
21. **`migrate plan`** on a v3 book proposes v4, which does not exist.

### C. Not documented anywhere. Do not invent.

- **pipx.** Not documented or proven.
- **Tool versions.** Pandoc and TeX Live versions are not pinned by number; they are "whatever Ubuntu 24.04 shipped".
- **Build timings.** Only the first-run font scan is described.
- **Windows.** Not tested.
- **Book-level `\part` divisions.** Unsupported.
- **Cross-references to chapters or sections.** None exist; only figures.
- **A generated glossary or "also by".** Planned, not built.
- **The finisher (supplied-interior PDF).** Planned on the Book breadth milestone, not shipped.
- **The custom merchant-of-record commerce stack.** Icebox.
- **Non-Latin and right-to-left scripts.** Icebox, "a major per script family".
---

# Supplement added by the managing editor (2026-11-11): real captures

## S1. `press add`, captured in a fresh `press new alice --author "Lewis Carroll" --owner wonderland-press` book

```text
$ press add chapter "Down the rabbit-hole"
created book/chapters/01-down-the-rabbit-hole.md
$ press add appendix about-the-author
created book/appendices/z-about-the-author.md
$ press add appendix glossary
created book/appendices/y-glossary.md
$ ls -1 book/chapters book/appendices
book/chapters:
00-preface.md
01-down-the-rabbit-hole.md

book/appendices:
y-glossary.md
z-about-the-author.md
$ cat book/chapters/01-down-the-rabbit-hole.md
# Down the rabbit-hole

Write this part here. This placeholder paragraph only exists so the file is valid Markdown that builds; delete it and begin.
```

The `metadata.yaml` that `--owner wonderland-press` and `--author "Lewis Carroll"` produce has these lines (verbatim):

```text
author:
  - "Lewis Carroll"
repository: "https://github.com/wonderland-press/alice"
site-url: "https://wonderland-press.github.io/alice"
```

## S2. The commerce block of the scaffolded metadata.yaml, verbatim

```text
# Direct print ordering: a reader-facing "Order a print copy" link to a
# provider-hosted checkout (Lulu, Peecho, a Bookvault store, ...). The
# provider is the seller of record and owns payment, tax, fulfillment,
# and support; this block holds only URLs and a name, never a credential
# or a price. Enable it once the edition is qualified (press qualify).
# A policy link is optional: give a URL to link your own hosted page, or
# omit it and press generates an honest page on your book site. Add
# policies: {support,privacy,refund} text to append your own words.
# commerce:
#   print-ordering:
#     enabled: true
#     edition: paperback
#     storefront-url: "https://www.lulu.com/shop/..."
#     seller-of-record: "Lulu"     # who the reader actually buys from
#     support-url: "https://example.test/support"   # optional; omit to generate
#     # privacy-url / refund-url omitted -> press generates those pages
#     policies:
#       privacy: "We keep no reader data; the provider handles your order."
```

## S3. Ruling on the index position

The merge order is chapters, then appendices sorted by filename letter, then the generated index, which is given the first free letter from `a`. Because `press add appendix` letters from `z` downward, the generated index file is usually lettered `a-` and therefore sorts first among the appendices in the merged book. State the mechanism; do not call it a bug.
