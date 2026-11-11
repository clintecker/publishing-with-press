## 1. What press is

### 1.1 One-sentence identity

`README.md` opens:

> A complete small press: everything required to turn a directory of Markdown chapters into a publishable book. One `press all` produces a verified 6 x 9 PDF, EPUB, single-file HTML, per-chapter reader site, stitched Markdown, plain text, DOCX, a GitHub Pages site with public downloads, and gated GitHub releases; the print pack adds a print-profile interior, a cover wrap with computed spine and EAN-13 barcode, and retail channel checklists.

The package docstring (`src/press/__init__.py`):

> A small press: the build, check, and verify pipeline for books. Extracted from the production of one book so the next book starts with the scars already paid for. Everything book-specific comes from the book repository's config; nothing in here names a title.

The `pyproject.toml` description is "Book production pipeline: pandoc/LuaLaTeX builds, editorial checks, and artifact verification". The terminal tagline is `markdown → a finished book` (`src/press/brand.py:62`). The press mark is the pilcrow `¶`.

### 1.2 Provenance and history

- **Extracted from one book.** press was extracted from the production of the book *Mostly Done.* (`README.md`). A second flagship, *Make Ready*, was "taken end to end through the built-in facilities": a commissioned clothbound cover, fourteen engraved plates finished by `press art enhance`, a subject index, registered ISBNs, and a table of authorities (CHANGELOG 2.3.1). Make Ready lives outside the press repo.
- **First commit.** `6ee1498`, 2026-07-17: "Found the press: the book pipeline with no book inside". There are 560 commits to 2026-11-11.
- **Tags.** v1.0.0 through v1.6.0 all landed on 2026-07-18. The CHANGELOG records releases from v1.7.0 onward. Earlier history lives in the tags: "the packaged instruments, the art department, generated front matter, the print pack, registrations, the operator, the aesthetic system, and the public-readiness hardening of the P0/P1 audit" (`CHANGELOG.md:3-8`).
- **Majors.**

  | Major | Date | What it brought |
  |---|---|---|
  | v1.x | 2026-07-18 to 2026-07-21 | v1.0.0 through v1.20.0 |
  | v2.0.0 | 2026-07-21 | "Composable press": print profiles, providers, extension contract |
  | v3.0.0 | 2026-11-10 | A design major (see below) |
  | v3.0.1 | 2026-11-10 | Migrate message fix |
  | v3.0.2 | 2026-11-11 | Security: Pillow 13 |

  v3.0.0 brought:
  - a fine-press craft pass: microtype, oldstyle figures, selnolig, widow/orphan/runt discipline, and the typographic-spacing filter;
  - numbered figures with cross-references and a List of Figures;
  - the placement vocabulary;
  - the set pieces `cascade`, `verse`, and `tail`;
  - the `ornate` chapter opening and aesthetic scene breaks (asterism, fairy-dust);
  - the print-profile lifecycle;
  - a provider support matrix enforced by `press check`;
  - the Alice gallery example.

- **Floating tags.** `v1`, `v2`, `v3`. All tags, in order:

  ```text
  v1.0.0 v1.0.1 v1.0.2 v1.0.3 v1.0.4 v1.1.0 v1.1.1 v1.1.2 v1.2.0 v1.3.0 v1.4.0 v1.5.0 v1.6.0 v1.7.0 v1.8.0 v1.8.1 v1.8.2 v1.9.0 v1.10.0 v1.11.0 v1.12.0 v1.13.0 v1.14.0 v1.15.0 v1.15.1 v1.15.2 v1.16.4 v1.17.0 v1.18.0 v1.19.1 v1.20.0 v2.0.0 v2.1.0 v2.2.0 v2.2.1 v2.3.0 v2.3.1 v3.0.0 v3.0.1 v3.0.2
  ```

- **The four most recent releases**, from `CHANGELOG.md`:
  - **3.0.2** (2026-11-11). Security release. The hash-locked runtime deps move Pillow 12.3.0 → 13.0.0, "closing the 41 advisories GitHub reported against the lock (five critical: heap overflows in the JPEG and FlashPix decoders and in TIFF writing, a stale-storage reuse in multi-frame loaders, and an argument injection in the Ghostscript call)". Pillow 13 needs Python 3.11; the package floor stays `Pillow>=10.0`, so 3.10 installs resolve 12.x. `scripts/lock-deps.sh` now passes extra args to pip-compile (`--upgrade-package pillow`). The Lua filter tests now run in CI (`PRESS_REQUIRE_LUA=1` forbids the silent skip). 31 backfilled Lua tests raised every filter to 83-100% line coverage. They also exposed that a previous title-tie test was vacuous, because pandoc ties `Mr.` itself.
  - **3.0.1** (2026-11-10). `press migrate` had opened every plan promising byte-for-byte geometry. That was true for v1→v2 and false for v2→v3. The first note is now keyed by the target major (#262).
  - **3.0.0** (2026-11-10). The design major described above. Notable fixes: EPUB figures fit and centre; a dialogue-opening chapter hangs its opening quote in the margin (Bringhurst); a subtitle-less title page shows one rule, not two; a plate on a gradient ground is refused at intake. Notable changes: plates are kept as alpha PNG masters (#226); the macOS selftest moves to `macos-15`.
  - **2.3.1** (2026-07-24). The EAN-13 barcode crowded its quiet zone because a TikZ node's default padding shifted it; fixed with `inner sep=0` (#210). Cover subject precedence was fixed. An adapters-boundary gate blind spot was closed (a from-import of `subprocess.Popen`).

### 1.3 Who maintains it

One maintainer: Clint Ecker, LGTM Systems, LLC. Books appear under the LGTM Publishing imprint (`SUPPORT.md`). Licence is MIT, "code and bundled content alike... A book you make with the press is yours entirely" (`README.md`). The roadmap describes the GitHub repo `clintecker/press` as public since 2026-07-19. Docs site: <https://clintecker.github.io/press/>.

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


### 3.6 The example books (`examples/*/`, the gallery)

Each of the nine examples is a complete book repository with the same layout:

- `config/metadata.yaml` and `config/aesthetic.yaml`
- `assets/cover.jpg`
- `book/chapters/` and `book/appendices/`
- `verify-min-pages: 1`

**What none of them has:** `config/authorities.yaml`, `tex/title-page.tex`, or a `registrations` block.

**Build any of them:**

```sh
git clone https://github.com/clintecker/press && cd press
pip install -e . && cd examples/tidepool-field-notes && press all
```

**How the gallery is published:**

- The docs site builds each example's PDF inside the pinned image (`scripts/build_examples.py`).
- `docs/GALLERY.md` shows each example's cover and two real pages.
- The covers are one-time Penguin tri-band commissions in each book's accent. They are committed assets, never regenerated in CI.

| Example | Genre | Title | Print config | Exercises |
|---|---|---|---|---|
| `alice-in-wonderland` | public-domain classic (Carroll, ch. 1–3) | "Alice's Adventures in Wonderland" (lang en-GB, Oxford) | `house-6x9`; drop-cap, 3 lines, small caps | Tenniel's 1865 wood engravings as plates; `art/commissions.md`; front matter (edition-note, epigraph, rights, manufacture, colophon-note); aesthetic "Wonderland engraving" with `scene-break: fairy-dust`; `::: verse`, `::: cascade`, `::: tail` (the Mouse's Tale); a dialogue opener ("Curiouser and curiouser!") with a hung quote; appendix `z-about-this-edition.md` |
| `field-days-almanac` | children's nature almanac | "Field Days: A young naturalist's almanac" | `binding: saddle-stitch` (no spine); drop-cap, 3 lines | four seasonal chapters |
| `hearthstone-cookbook` | cookbook | "The Hearthstone Table: Plain food for cold months" | `house-6x9-color`, `provider: kdp`, `paper: white` | **colour interior**; `index-terms.yaml`; dedication |
| `on-the-commons-monograph` | academic monograph | "The Reasonable Commons: Cooperation without coercion in small communities" | house | footnote citations; dedication and acknowledgements |
| `signal-and-noise-manual` | technical field manual (radio) | "Signal and Noise: A field manual for small radio" | house | every figure placement (`inline`, `wrap-inner`, `wrap-outer`, `plate`, `full-bleed`, `frontispiece`; full and half measure; `outset`; `fig-alt`) in `04-plates-and-placement.md`; tables; glossary appendix `x-glossary.md`; index; `house-rules.yaml` jargon-allow (gate, gating, clean, drift) |
| `small-hours-chapbook` | poetry chapbook | "Small Hours: Poems for the middle of the night" | `novella-5x8` | verse as hard line breaks; `assets/web/extra.css` (narrow 30rem measure, line-height 1.85); dedication and epigraph |
| `the-long-field-essays` | essay collection | "The Long Field: Essays on staying put" | house | footnotes; dedication, epigraph, acknowledgements; `y-also-by.md` |
| `the-tinsmith-novella` | literary novella | "The Tinsmith's Daughter: A novella" | `novella-5x8`; drop-cap | `house-rules.yaml` (jargon-allow seam, clean); aesthetic "Cold steel minimal"; `a-also-by.md` |
| `tidepool-field-notes` | natural-history field guide | "Between the Tides: A field guide to the rocky shore" | house | a preface plus four intertidal-zone chapters; footnotes; no front-matter file |

**What differs, and where it lives** (from `docs/GALLERY.md`):

| To change… | Set this | Seen in |
|---|---|---|
| Trim | `print: profile:` in `config/metadata.yaml` | the 5×8 chapbook and novella |
| Palette and register | `config/aesthetic.yaml` | every book |
| The initial that opens each chapter | `chapter-opening:` in `config/metadata.yaml` | the novella and the almanac |
| Binding | `print: binding:` in `config/metadata.yaml` | the saddle-stitched almanac |
| Dedication, epigraph, acknowledgements | `config/front-matter.yaml` | cookbook, monograph, chapbook, essays, novella |
| A subject index | `config/index-terms.yaml` | the cookbook and the manual |
| Interior illustration plates | plate files in `assets/woodcuts/` | the Alice example |
| The reading measure and web styling | `assets/web/extra.css` | the chapbook |


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

# Supplement added by the managing editor (2026-11-11): real capture

## S1. `ls dist/` after `press all` on the press's own Alice example (slug `alice-in-wonderland`), captured 2026-11-11

```text
$ ls dist/
alice-in-wonderland-site.zip
alice-in-wonderland-source.zip
alice-in-wonderland.docx
alice-in-wonderland.epub
alice-in-wonderland.html
alice-in-wonderland.md
alice-in-wonderland.pdf
alice-in-wonderland.txt
pages
site
```

For the book's sample (slug `alice`) replace `alice-in-wonderland` with `alice` and keep everything else. The run ended with these lines, verbatim:

```text
commerce release gate: print ordering is not enabled; no commerce release gate

  press. your book is ready → dist/

```

## S2. Ruling: `press all` builds `dist/pages/`

The fact base section 5.3 lists the `press all` sequence: 1 check, 2 every format, 3 the source zip, 4 pages, 5 the verifiers, 6 the commerce gate (advisory). So `press all` does assemble `dist/pages/`; QUICKSTART runs `press pages` afterwards only to show the command. The listing above confirms `pages` is present after `press all`.

## S3. The complete `press all` output on the Alice example, captured 2026-11-11 (29 lines, verbatim; paths elided with ...)

```text
Source checks passed: 4 ordered Markdown files
  note: em-dash.md also drew: - .../known-bad/em-dash.md:4: glyph U+2014 is outside the print-font set
  note: en-dash.md also drew: - .../known-bad/en-dash.md:4: glyph U+2013 is outside the print-font set
Checker self-test passed: 19 known-bad fixtures each tripped their declared rule, known-good fixture accepted, 2 extra diagnostics noted
Editorial checks passed: 4 Markdown files
Jargon check passed: no rewrite-status terms (full audit in build/jargon-report.txt)
  ¶ check      ✓ style, source, jargon
+ pandoc --defaults=~/alice/build/defaults/pdf.yaml book/chapters/01-down-the-rabbit-hole.md book/chapters/02-the-pool-of-tears.md book/chapters/03-a-caucus-race-and-a-long-tale.md book/appendices/z-about-this-edition.md --output dist/alice-in-wonderland.pdf
  pandoc took 26.7s
+ pandoc --defaults=~/alice/build/defaults/epub.yaml --metadata rights=The text and illustrations are in the public domain. Published by The Press (gallery example), Oxford. --epub-metadata=~/alice/build/epub-metadata.xml book/chapters/01-down-the-rabbit-hole.md book/chapters/02-the-pool-of-tears.md book/chapters/03-a-caucus-race-and-a-long-tale.md book/appendices/z-about-this-edition.md --output dist/alice-in-wonderland.epub
+ pandoc --defaults=~/alice/build/defaults/html.yaml book/chapters/01-down-the-rabbit-hole.md book/chapters/02-the-pool-of-tears.md book/chapters/03-a-caucus-race-and-a-long-tale.md book/appendices/z-about-this-edition.md --output dist/alice-in-wonderland.html
+ stitched 4 files -> dist/alice-in-wonderland.md
+ pandoc --defaults=~/alice/build/defaults/portable.yaml --to=plain --columns=80 book/chapters/01-down-the-rabbit-hole.md book/chapters/02-the-pool-of-tears.md book/chapters/03-a-caucus-race-and-a-long-tale.md book/appendices/z-about-this-edition.md --output dist/alice-in-wonderland.txt
+ pandoc --defaults=~/alice/build/defaults/portable.yaml --to=docx book/chapters/01-down-the-rabbit-hole.md book/chapters/02-the-pool-of-tears.md book/chapters/03-a-caucus-race-and-a-long-tale.md book/appendices/z-about-this-edition.md --output dist/alice-in-wonderland.docx
+ pandoc --defaults=~/alice/build/defaults/chunked.yaml --to=chunkedhtml book/chapters/01-down-the-rabbit-hole.md book/chapters/02-the-pool-of-tears.md book/chapters/03-a-caucus-race-and-a-long-tale.md book/appendices/z-about-this-edition.md --output dist/site
~/alice/dist/alice-in-wonderland-source.zip
archived 12 files; excluded dirs ['.git', '__pycache__', 'build', 'dist']
+ assembled pages site -> dist/pages
  ¶ typeset    ✓ PDF · EPUB · web · text · DOCX
Verified dist/pages: every local reference resolves (fragments and stylesheet assets included), 8 downloads present and linked, sentinels on the public reading surface
Verified alice-in-wonderland.pdf: 23 pages, 6 x 9 trim, embedded fonts, 2 sentinel(s) plus the title as witnesses, every rendered page contains ink, no edge clipping, cover on page 1
WARNING: epubcheck not installed; EPUB validated structurally only. The press toolchain runs the full check in CI. (brew install epubcheck)
Verified alice-in-wonderland.html, alice-in-wonderland.epub, alice-in-wonderland.md, alice-in-wonderland.txt, alice-in-wonderland.docx, site/ (2 sentinel(s), the title, and the manuscript line 'and here alice began to get rather sleep...' as witnesses); 7 editions agree on all 4 chapter witnesses
Verified archives: alice-in-wonderland-site.zip, alice-in-wonderland-source.zip
  ¶ verify     ✓ 7 editions match source
commerce release gate: print ordering is not enabled; no commerce release gate

  press. your book is ready → dist/

```

Notes: the `¶` and `✓` glyphs and the `→` arrow are part of the real output and may appear inside a code block (the glyph law exempts code; Source Code Pro carries them). The run was on the press example whose slug is `alice-in-wonderland`; the book's sample uses `alice`. The slow step was the PDF: `pandoc took` lines show the per-step timing if present above.


---

# Supplement S4 added by the managing editor (2026-11-11): sections the chapter needs that its slice lacked

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


### 2.1 The Python package

- `requires-python = ">=3.10"`. Python 3.10 through 3.14 are tested: CI runs all five on Ubuntu, plus 3.12 on macOS 15 (`docs/COMPATIBILITY.md`).
- Runtime dependencies (`pyproject.toml`): `Pillow>=10.0`, `pypdf>=6.21.4`, `ruamel.yaml>=0.18`. ruamel is "the package's one YAML library (see press.yamlio)": it reads YAML 1.2 so bare `no`/`yes`/`on` stay strings, and its round-trip mode preserves comments.
- Extras:
  - `tui`: `textual>=8.2.8,<9`, for the desk.
  - `dev`: ruff, mypy, pre-commit, build, twine, pytest, pytest-asyncio, pytest-cov, pytest-xdist, hypothesis, textual, plus `celebrimbor @ git+https://github.com/clintecker/celebrimbor@v0.12.0 ; python_version >= '3.11'`. celebrimbor is the quality framework; it is dev/CI only, never a book runtime dependency.
- Classifier: "Development Status :: 4 - Beta". Licence `MIT`. Authors: Clint Ecker; maintainers: LGTM Systems, LLC.

**Install paths:**

1. **Pip from git at a tag.** This is the supported channel (`docs/INSTALL.md`):

   ```sh
   pip install "press @ git+https://github.com/clintecker/press@v3"
   ```

   "the press is not published to PyPI, and nothing in its metadata should imply otherwise". `@v3` floats; `@v3.0.0` (any three-part tag) is immutable.
2. **Editable, for development or tracking a clone:** `pip install -e .` from a clone (`README.md`). The scaffolded `requirements.txt` comment recommends `pip install -e ~/path/to/press` for day-to-day book work.
3. **With the desk:** `pip install 'press[tui]'`.
4. **pipx.** Not documented anywhere in the repo. Do not claim it is supported. It would presumably work as a generic Python CLI, but nothing proves it.
5. **The container, with no local toolchain at all** (`docs/INSTALL.md`):

   ```sh
   docker run --rm -v "$PWD":/book ghcr.io/clintecker/press-toolchain:latest \
     bash -c "pip install --break-system-packages 'press @ git+https://github.com/clintecker/press@v3' && cd /book && press all"
   ```

6. **In CI.** The composite action installs press from its own checkout, never pip-from-git (§12).

There are discovery commands that need no book and no toolchain: `press --version`, `press --help`, and `press <command> --help`. All three exit 0 (`SUPPORT.md`).


### 2.2 System toolchain

**macOS** (`docs/INSTALL.md`):

```sh
brew install pandoc poppler
brew install --cask mactex-no-gui   # lualatex, latexmk, TeX Live
brew install epubcheck              # optional: the retail EPUB gate locally
```

"Fonts: TeX Live carries Libertinus for the PDF; nothing else to install."

**Debian/Ubuntu.** The `Dockerfile` is the canonical package list:

```sh
sudo apt-get install --no-install-recommends \
  make git pandoc python3 python3-pip poppler-utils \
  texlive-luatex texlive-latex-extra texlive-fonts-extra \
  fonts-linuxlibertine latexmk epubcheck
```

- `fonts-linuxlibertine` is explicit because Ubuntu has no `fonts-libertinus`, and `--no-install-recommends` would drop the Libertine keyboard face.
- `texlive-fonts-extra` also provides the `yinit` foliate initials used by `chapter-opening.style: ornate`.

**Versions.** No pandoc or TeX version is pinned by number anywhere. "the exact tool versions are whatever Ubuntu 24.04 shipped, frozen by the image digest" (`docs/COMPATIBILITY.md`). Writers should say "Ubuntu 24.04's pandoc and TeX Live", not quote a version.

**Required external tools** (from `src/press/doctor.py:28-39`):

| Tool | Purpose (verbatim doctor text) | Required |
|---|---|---|
| pandoc | every build target | yes |
| lualatex | PDF and print builds | yes |
| latexmk | PDF and print builds (multi-pass convergence) | yes |
| pdftoppm | PDF verification renders | yes |
| pdffonts | font-embedding verification | yes |
| pdfinfo | PDF structure verification | yes |
| pdftotext | PDF text verification | yes |
| git | scaffolding identity and book repositories | yes |
| epubcheck | the retail EPUB gate (softens to a warning locally) | no |
| claude | the operator: press improve, research, aesthetic briefs | no |

doctor also reports:

- `realesrgan`: "plate enhancement upscaling (press art enhance)", optional, found through the enhancer's own resolver;
- `OPENAI_API_KEY` and `GEMINI_API_KEY`: `ok` or `unset`;
- the Python version, against the tested range;
- whether Pillow, pypdf, and ruamel.yaml import.

**Not checked by doctor, but used:**

- `pdfimages` (poppler). Its absence softens two checks to notes.
- `java`, inside the container's epubcheck wrapper.
- `oxipng` or `pngcrush`, optional for `art enhance`.
- Headless Chrome, used only by the press's *own docs site* layout check (`scripts/check_layout.py`). It is not needed for books.

**Toolchain image.** `ghcr.io/clintecker/press-toolchain`:

- built `FROM ubuntu:24.04`;
- multi-arch, amd64 and arm64 (#206);
- public since 2026-07-20 (#161);
- carries a `java -jar` wrapper for epubcheck at `/usr/local/bin/epubcheck`;
- on amd64, carries `realesrgan-ncnn-vulkan` (v0.2.5.0 zip, sha256-verified) plus the remacri and ultrasharp models in `/usr/local/share/realesrgan/models`;
- in the container, `pip install` needs `--break-system-packages`.

**Apple Silicon.** This is the maintainer's primary platform. Local arm64 container builds work since the image went multi-arch. The arm64 image has no upstream Real-ESRGAN binary, so `art enhance` there resamples instead of upscaling (`docs/ILLUSTRATIONS.md`). `scripts/verify.sh --full` "runs natively on Apple Silicon since the toolchain image went multi-arch" (`CONTRIBUTING.md`).

**First-run behavior** (a CLAUDE.md scar):

> First LuaLaTeX run on a fresh machine triggers a several-minute font scan that looks like a hang. It is not a hang.


### 4.1 The dialect

Every pandoc build reads the manuscript as
`markdown+smart+yaml_metadata_block+fenced_divs+footnotes`, with `standalone: true` and `number-sections: true`. The same settings appear in all six `src/press/data/defaults/*.yaml` files.

- **Smart typography.** Because of `+smart`, the author types straight quotes and pandoc curls them in the output. Two hyphens (`--`) become an en dash, three (`---`) an em dash, and three dots an ellipsis. In source, though, the house bans the literal characters U+2014 and U+2013 and the curly quotes. Writing `--` in source is not banned by the checker, but the house law says "rewrite the sentence instead".
- **Headings.** A `#` heading is a chapter (`top-level-division: chapter`). Chapters are numbered automatically. A heading marked `{.unnumbered}` or `{-}` gets no number.
  - Manual numbering in a heading such as `# 3. Title` is refused in book prose with `manual number in heading`.
  - A title-case heading is refused with `title-case heading: <text>`. The test: ignoring the first word, 21 listed small words, and ALL-CAPS words, at least 3 candidate words remain and 80% or more of them are capitalized.
- **Glyph law.** Book prose may contain only tab, LF, CR, U+0020–U+007E, and U+00C0–U+017F (`style_audit.py:29`). That last range is the accented Latin letters, plus × and ÷.
  - Everything in U+00A0–U+00BF fails: ©, °, §, £, «, », ½, NBSP, ¿.
  - Greek, math symbols, and emoji also fail: `glyph U+XXXX is outside the print-font set`.
  - Writers should state this law exactly. It is surprising, because © cannot be typed in a chapter.
- **Paragraph law.** A paragraph must be under 190 words. Over 190 gives an error in book prose and a warning in `audit-dirs`:
  `paragraph N has W words (the law is under 190; split it)`.
  This was enforced from v1.7.0 (CHANGELOG).
- **Trailing whitespace** is forbidden everywhere, including inside code fences.
- **Footnotes** use the standard `[^label]` syntax. The PDF sets them at the foot of the page; the EPUB and the web reader collect them as linked notes. "There is no separate endnote setting" (`docs/BOOK-PARTS.md`).

  ```markdown
  The press was proven on one book first.[^scars]

  [^scars]: Every scar in the pipeline was paid for by that first production.
  ```

- **Tables** are pandoc pipe tables. In the HTML edition and the reader, headed tables get `data-label` attributes on each cell (`webmeta.label_table_cells`). Below 34rem, the reader CSS turns each row into a card.
- **Code** uses pandoc fenced code. In the PDF it is set in Source Code Pro scaled 0.86, with `fvextra` `breaklines,breakanywhere`. Prose rules skip fenced code, except the trailing-whitespace rule.
- **Blockquotes.** In the PDF, `quote` is an `mdframed` box: papergray background, 0.4pt rulegray line, `\small\itshape`. The jargon lint skips blockquotes by default.
- **Definition lists** are standard pandoc. They are the recommended form for a glossary appendix.
- **Line blocks** (`| line`) preserve line breaks. They are the input form for the set pieces below.


### 4.5 Drop caps and chapter openings

These settings live in metadata `chapter-opening` and are merged over the design profile's default, which is `none` in every shipped profile.

- **Styles:** `none`, `drop-cap`, `raised-cap`, `ornate`.
  - `raised-cap` is accepted but renders the same as `drop-cap`. No code treats it differently.
- **`lines`** defaults to 3 and **`small-caps-remainder`** to true.
- **Where it applies.** `chapter-dropcap.lua` finds the first eligible paragraph after each level-1 heading that is not `{.unnumbered}`/`{.unlisted}`. It skips blockquotes (an epigraph), code, lists, tables, rules, and figures along the way.
- **PDF.** The filter emits `\PressDropCap{lead}{I}{rest}`, which wraps `lettrine`:
  `\lettrine[lines=3,depth=0,findent=2pt,nindent=0pt]{#2}{\scshape #3}`, preceded by `\Needspace*{4\baselineskip}`.
- **Dialogue openers** (v3.0.0). The leading quotation mark, the "lead", hangs into the left margin at body size through `ante={\smash{\llap{...}}}` (Bringhurst's rule). On the web, `.drop-cap-lead` takes a margin of −.52em.
- **`ornate`** sets the initial in the yinit foliate font (`yfonts`, from `texlive-fonts-extra`) in print only. The web and EPUB degrade it honestly to a styled display capital: Luminari / Apple Chancery / Zapfino… at 3.6em in the ornament colour.
- **Unicode.** The initial is one grapheme, including combining marks.
- **Formats without drop caps:** txt and docx.
- **Scar** (from the maintainer's notes): sentinels must be mid-chapter phrases, because the drop cap splits and small-caps a chapter's opening word, which breaks exact PDF matching.


### 12.2 The composite action (`action.yml`), verbatim

```yaml
name: press
description: >-
  Install the press from this action's own checkout and run a press target
  against the calling book repository. Because GitHub materializes the action
  repository onto the runner, even a private book can use the press with
  no cross-repo token.
inputs:
  command:
    description: press target to run (default builds and verifies everything)
    default: all
runs:
  using: composite
  steps:
    - name: Install press
      shell: bash
      # Runtime dependencies from the hash-pinned lock first (#194: a pinned
      # release resolves immutable dependency bytes, not whatever PyPI serves
      # today), then press itself with --no-deps so nothing is resolved fresh.
      run: |
        python3 -m pip install --quiet --break-system-packages \
          --require-hashes -r "$GITHUB_ACTION_PATH/requirements-lock.txt"
        python3 -m pip install --quiet --break-system-packages \
          --no-deps "$GITHUB_ACTION_PATH"
    - name: Run press
      shell: bash
      env:
        # The input reaches the script as an environment value, never
        # interpolated into shell text, so metacharacters are data.
        PRESS_COMMAND: ${{ inputs.command }}
      run: |
        if ! [[ "$PRESS_COMMAND" =~ ^[a-z][a-z0-9-]*( [A-Za-z0-9._/=-]+)*$ ]]; then
          echo "press action: refusing command input: $PRESS_COMMAND"
          echo "targets are lowercase words with plain path/flag arguments;"
          echo "shell syntax is not part of the grammar"
          exit 2
        fi
        read -r -a argv <<< "$PRESS_COMMAND"
        python3 -m press "${argv[@]}"
```

**Self-checkout install is law.** From `CLAUDE.md`: "it keeps a private book working with no cross-repo token and pins the installed press to the exact action ref; do not replace it with pip-from-git."

**The lock.** `requirements-lock.txt` pins three packages: `pillow==13.0.0`, `pypdf==6.21.4`, `ruamel-yaml==0.19.1`. It carries 87 sha256 hashes and was compiled with Python 3.12. Regenerate it with `scripts/lock-deps.sh`, which runs pip-compile in the pinned image. "pip-compile keeps existing pins, so a security bump is `scripts/lock-deps.sh --upgrade-package <name>`."


### 12.4 The toolchain image

- **Name and basis.** `ghcr.io/clintecker/press-toolchain`, built from `Dockerfile` (`FROM ubuntu:24.04`, `ENV PRESS_TOOLCHAIN=1`).
- **apt packages:** make, git, gh, pandoc, python3, python3-pip, poppler-utils, epubcheck, texlive-luatex, texlive-latex-extra (for lettrine), texlive-fonts-extra (for yfonts/yinit), fonts-linuxlibertine, latexmk.
- **epubcheck wrapper.** `printf '#!/bin/sh\nexec java -jar /usr/share/java/epubcheck.jar "$@"\n' > /usr/local/bin/epubcheck`.
- **Image processing.** Real-ESRGAN plus the models, amd64 only. `mesa-vulkan-drivers` provides a software Vulkan.
- **Lua tooling.** stylua v2.5.2, and selene 0.31.0 on amd64.
- **Multi-arch.** The image is published for amd64 (`ubuntu-24.04`) and arm64 (`ubuntu-24.04-arm`) by `.github/workflows/toolchain.yml`, and each is smoked before push. The tags are `:latest` and `:sha-<SHA>`.
- **Public since 2026-07-20 (#161).** "a book under any account pulls it with no package grant and no configured secret". In CI the pull is authenticated with the workflow's own `GITHUB_TOKEN`, "which works for a public image, including on fork and Dependabot pull requests". Locally it pulls anonymously.


## S5. Rulings

- `press new <directory>` sets `slug: "<directory>"` in the scaffolded `config/metadata.yaml` (see the scaffold in 3.1 and the field in 3.3), so `press new alice` yields slug `alice` and every artifact is `dist/alice.*`.
- The drop cap is NOT the house default: `chapter-opening` defaults to `none` in every shipped profile (4.5); the Alice example opts in. The chapter must not say chapters open with a drop cap by default.
- Python 3.10 through 3.14, pandoc, LuaLaTeX, latexmk, poppler (`pdftoppm`, `pdffonts`), epubcheck and a Java to run it, and the Libertine faces are the toolchain as 2.2 states it; the image is `ghcr.io/clintecker/press-toolchain` (12.4).
