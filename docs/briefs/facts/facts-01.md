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
