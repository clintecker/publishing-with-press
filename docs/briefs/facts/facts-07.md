## 5. Building

### 5.1 Targets and what they run

The CLI lives in `src/press/__main__.py`. The format targets go to `build.build_target`. pandoc must be on PATH, or the build stops with `SystemExit("pandoc is required")`.

| Target | Mechanism | Defaults file | Output |
|---|---|---|---|
| `press pdf` | pandoc → latexmk `-lualatex` | `pdf.yaml` | `dist/<slug>.pdf` |
| `press epub` | pandoc | `epub.yaml` | `dist/<slug>.epub` |
| `press html` | pandoc `self-contained`, then table-cell labels | `html.yaml` | `dist/<slug>.html` |
| `press markdown` | **not pandoc**: header + raw stitched source with heading attribute blocks stripped | none | `dist/<slug>.md` |
| `press site` | pandoc `--to=chunkedhtml`, `split-level: 1`, then reader CSS, assets (JPEGs re-saved q70), reader metadata, zip | `chunked.yaml` | `dist/site/`, `dist/<slug>-site.zip` |
| `press txt` | pandoc `--to=plain --columns=80` | `portable.yaml` | `dist/<slug>.txt` |
| `press docx` | pandoc `--to=docx` | `portable.yaml` | `dist/<slug>.docx` |
| `press source` | `package_source` (git-tracked files only) | none | `dist/<slug>-source.zip` |
| `press pages` | assemble landing + read/ + downloads/ + sitemap, **then verify** | none | `dist/pages/` |
| `press print` | pandoc → latexmk, twoside, print-safe images | `print.yaml` | `dist/<slug>-interior.pdf` |
| `press coverwrap` | build print, then `gen_coverwrap` (latexmk on generated TikZ), then verify | none | `dist/<slug>-coverwrap.pdf` |
| `press render` | build pdf, then `pdftoppm -png -r 160` | none | `build/rendered-book/page-*.png` |
| `press all` | the full gauntlet (below) | none | everything except print/coverwrap |
| `press clean` | delete `build/` and `dist/` | none | none |

**The pandoc command** (`build.py:223-233`):

```text
pandoc --defaults=<root>/build/defaults/<name>.yaml [extra...] <chapters...> <appendices + generated...> --output <output>
```

- It runs from the book root and prints `+ <command>`.
- When pandoc takes 1s or more it prints `  pandoc took N.Ns`.
- When more than one step is timed, the registry prints `press timings: …`.

**Defaults templating** (`build.render_defaults`). Paths in `src/press/data/defaults/*.yaml` use prefixes:

- `@press/…` resolves into the package `data/`;
- `@book/…` resolves into the book;
- a `?optional` suffix drops the entry when the file is absent;
- a missing non-optional file stops the build: `defaults reference a missing file`.

The rendered copies are written to `build/defaults/`.

**Environment injected into builds:**

- `SOURCE_DATE_EPOCH`, default `1784160000` (2026-07-16) unless the caller set it;
- `BOOK_ROOT`;
- `BOOK_PUBLISHER`, which the fallback TeX title reads through `\directlua`.

**Metadata injected:** `chapter-opening-style`, `chapter-opening-lines`, `chapter-opening-smallcaps`, `scene-break-ornament`.

**PDF and print pre-steps:**

1. write `build/profile-dropcap.tex`;
2. set the `lof` variable when `assets/woodcuts/` has files;
3. generate `build/front-matter.tex`;
4. write `build/aesthetic.tex`;
5. write `build/profile-geometry.tex`;
6. for print only, `print_safe.prepare` writes `build/print-assets/`.

**EPUB specifics:**

- `--metadata rights="<copyright> Published by <publisher>, <place>."`;
- `identifier=urn:isbn:<isbn>` when an EPUB ISBN is registered;
- `build/epub-metadata.xml` carries `<dc:date>YEAR</dc:date>`, because epubcheck rejects pandoc's empty dc:date (RSC-005);
- `epub-cover-image` is `assets/cover.jpg` when present.

### 5.2 Lua filters and their order

Pandoc runs filters in list order:

| Defaults | Filter order |
|---|---|
| pdf, epub, html, chunked | typographic-spacing → set-pieces → chapter-dropcap → scene-break → figure-numbering |
| print | typographic-spacing → set-pieces → **print-safe-images** → chapter-dropcap → scene-break → figure-numbering |
| portable (txt, docx) | typographic-spacing → set-pieces → figure-numbering |

What each filter does:

- **`press-util.lua`** holds shared helpers: the measure tables, guard sizes, cascade step 2.4em, and tail amplitude 3.0em with its size ramp.
- **`typographic-spacing.lua`**: non-breaking spaces after titles, reference forms, and initials (§4.7).
- **`set-pieces.lua`**: cascade, verse, tail (§4.3).
- **`chapter-dropcap.lua`**: splits the first paragraph into lead, initial, rest of word, and rest of text; emits `\PressDropCap` or the `.chapter-opening` spans (§4.5).
- **`scene-break.lua`**: thematic break → rule, asterism, or fairy-dust (§4.4).
- **`print-safe-images.lua`**: in print only, rewrites `assets/…` image paths to `build/print-assets/assets/…`, the flattened white-ground copies.
- **`figure-numbering.lua`**:
  - numbers informative figures C.N;
  - emits `\caption*{\mbox{\textbf{Figure~C.N.}}\enspace …}` plus `\addcontentsline{lof2}…`;
  - inserts `\PressListOfFigures`;
  - lays wraps, leaves, and frontispieces;
  - resolves `@id` cross-references;
  - tidies image attributes so `place`/`outset`/`fig-alt`/`decorative` never leak as `data-*`.

  The label is boxed in `\mbox` so a narrow column can never hyphenate it into "Fig-ure".

Since v3.0.2, CI requires the Lua tests to run (`PRESS_REQUIRE_LUA=1`) and holds a per-filter line-coverage floor in `.celebrimbor/baselines/lua-coverage.yaml` through `scripts/lua_coverage_ratchet.py`. Contributors must never `update` that floor from a macOS measurement.

### 5.3 The dependency graph (the "no stale artifact" law)

`registry.ARTIFACTS` (`src/press/registry.py:28-72`) is the one table. This is the generated `docs/REFERENCE.md` table, verbatim:

```text
| artifact | outputs | prerequisites | published |
|---|---|---|---|
| pdf | {slug}.pdf | - | yes |
| epub | {slug}.epub | - | yes |
| html | {slug}.html | - | yes |
| markdown | {slug}.md | - | yes |
| txt | {slug}.txt | - | yes |
| docx | {slug}.docx | - | yes |
| site | site, {slug}-site.zip | - | yes |
| source | {slug}-source.zip | - | yes |
| sources | {slug}-sources.md | markdown | yes (when authorities configured) |
| pages | pages | pdf, epub, html, markdown, txt, docx, site, source, sources | no |
| print | {slug}-interior.pdf | - | no |
| coverwrap | {slug}-coverwrap.pdf | print | no |
```

Builders, verifiers, and destinations (also from `docs/REFERENCE.md`):

```text
| artifact | builder | verifier | publication destination |
|---|---|---|---|
| pdf | build (pandoc + latexmk) | verify_pdf | Pages downloads + GitHub Release |
| epub | build | verify_formats + epubcheck | Pages downloads + GitHub Release |
| html | build | verify_formats | Pages downloads + GitHub Release |
| markdown | build | verify_formats | Pages downloads + GitHub Release |
| txt | build | verify_formats | Pages downloads + GitHub Release |
| docx | build | verify_formats | Pages downloads + GitHub Release |
| site | build | verify_formats + verify_archives | Pages downloads + GitHub Release |
| source | package_source | verify_archives | Pages downloads + GitHub Release |
| sources | gen_authorities | verify_archives | Pages downloads + GitHub Release (when authorities configured) |
| pages | build | verify_pages | deployed as the Pages site |
| print | build (print profile) | verify_pdf (print profile) | GitHub Release when built (print pack) |
| coverwrap | gen_coverwrap | verify_coverwrap | GitHub Release when built (print pack) |
```

**Which verify command rebuilds what:**

- **`press verify`** builds the PDF, then runs `verify_pdf`.
- **`press verify-formats`** builds epub, html, markdown, site, txt, docx, and the source zip, then runs `verify_formats` and `verify_archives`. It does not rebuild the PDF, but it reads an existing `dist/<slug>.pdf` into the cross-edition agreement check when `pdftotext` exists.
- **`press pages` / `verify-pages`** run `registry.build("pages")` over all nine prerequisites, then `verify_pages`.
- **`press verify-print`** builds print, runs `verify_pdf --profile print`, and then, if `assets/cover.jpg` exists, builds the coverwrap (which builds print again) and runs `verify_coverwrap`. Without a cover it prints `no assets/cover.jpg; interior verified, wrap not built`.
- **`press coverwrap`** builds print, then the wrap, then `verify_coverwrap`.

**The press all sequence** (`__main__.py:455-491`):

1. `check`: check_source, then check_the_checkers, then style_audit, then jargon, stopping at the first failure;
2. every FORMAT;
3. the source zip;
4. pages;
5. `verify_pages`, `verify_pdf`, `verify_formats`, `verify_archives`;
6. the commerce gate: advisory with `(commerce gate is advisory here; a release build (PRESS_RELEASE=1) enforces it)`, enforcing under `PRESS_RELEASE`.

**`press all` does not build `print` or `coverwrap`.**

**Generated inputs are rebuilt every time.** Every pandoc build calls `book_inputs()`, which:

1. deletes `build/generated/`;
2. regenerates the index;
3. writes `dist/<slug>-sources.md` from the authorities ledger.

So "the generated appendices are cleaned first so stale copies cannot survive" (`docs/ARCHITECTURE.md`).

The scar (CLAUDE.md): "Verifying `dist/` without rebuilding blesses stale artifacts; the CLI's dependency edges exist so that cannot happen. Keep them." It is invariant `INV-graph-no-stale` (critical), with this stated limitation: "CLI-path only; importing a verifier module directly skips the rebuild."

### 5.4 Timing and logs

- **Live output.** pandoc command lines are echoed with `+ `. A pandoc run that takes 1s or more reports `pandoc took N.Ns`, and the registry prints `press timings:`.
- **Desk progress.** The desk parses three markers from this stream: `+ ` lines (tool invocations), `¶ <phase>` (check/typeset/verify), and `<tool> took Ns`.
- **First run.** The first LuaLaTeX run takes several minutes for the font scan.
- **Report files.** Jargon writes `build/jargon-report.txt`. The PDF verifier writes `build/verify-text.txt`.
- **Docs-site build times.** The pytest suite is about 4.5 minutes in parallel (`pyproject.toml` comment). No other timing is documented, so writers should not invent build times.

### 5.5 Flags

The build targets take no flags beyond `--help`/`-h`. There is no `--` passthrough to pandoc; extra pandoc args are internal only. Every flag that exists is listed in §17.

---


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

## S1. The complete `press all` output on the Alice example, with the pandoc echo lines (verbatim; paths elided)

```text
$ press all
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

## S2. A defaults template and its rendered copy (verbatim)

The package template `src/press/data/defaults/pdf.yaml`:

```text
from: markdown+smart+yaml_metadata_block+fenced_divs+footnotes
standalone: true
toc: true
toc-depth: 1
number-sections: true
top-level-division: chapter
pdf-engine: latexmk
pdf-engine-opts:
  - -lualatex
metadata-file: "@book/config/metadata.yaml"
filters:
  - "@press/lua/typographic-spacing.lua"
  - "@press/lua/set-pieces.lua"
  - "@press/lua/chapter-dropcap.lua"
  - "@press/lua/scene-break.lua"
  - "@press/lua/figure-numbering.lua"
include-in-header:
  - "@press/tex/book-header.tex"
  - "@book/build/profile-geometry.tex?optional"
  - "@book/build/profile-dropcap.tex?optional"
  - "@book/build/aesthetic.tex?optional"
  - "@book/build/front-matter.tex?optional"
  - "@book/tex/title-page.tex?optional"
variables:
  documentclass: scrbook
  classoption:
    - oneside
    - openany
    - headings=small
  fontsize: 10pt
  colorlinks: true
  linkcolor: black
  urlcolor: linkgreen
  citecolor: black
  toc-title: Contents
  lot: false
  thanks: ""
```

The rendered copy `build/defaults/pdf.yaml` in the Alice book after `press pdf` (paths elided to `.../press` and `~/alice`):

```text
from: markdown+smart+yaml_metadata_block+fenced_divs+footnotes
standalone: true
toc: true
toc-depth: 1
number-sections: true
top-level-division: chapter
pdf-engine: latexmk
pdf-engine-opts:
- -lualatex
metadata-file: ~/alice/config/metadata.yaml
filters:
- .../press/data/lua/typographic-spacing.lua
- .../press/data/lua/set-pieces.lua
- .../press/data/lua/chapter-dropcap.lua
- .../press/data/lua/scene-break.lua
- .../press/data/lua/figure-numbering.lua
include-in-header:
- .../press/data/tex/book-header.tex
- ~/alice/build/profile-geometry.tex
- ~/alice/build/profile-dropcap.tex
- ~/alice/build/aesthetic.tex
- ~/alice/build/front-matter.tex
variables:
  documentclass: scrbook
  classoption:
  - oneside
  - openany
  - headings=small
  fontsize: 10pt
  colorlinks: true
  linkcolor: black
  urlcolor: linkgreen
  citecolor: black
  toc-title: Contents
  lot: false
  thanks: ''
  lof: true
metadata:
  chapter-opening-style: drop-cap
  chapter-opening-lines: 3
  chapter-opening-smallcaps: 'true'
  scene-break-ornament: fairy-dust
```

## S3. `press wordcount` on the Alice example (verbatim)

```text
$ press wordcount
  2160  book/chapters/01-down-the-rabbit-hole.md
  2136  book/chapters/02-the-pool-of-tears.md
  1721  book/chapters/03-a-caucus-race-and-a-long-tale.md
   228  book/appendices/z-about-this-edition.md
  6245  TOTAL
```
