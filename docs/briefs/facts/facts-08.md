### 6.1 The verify_pdf checks

`src/press/verify_pdf.py` runs these in order for the reading PDF and, with `--profile print`, the interior.

1. **Release witnesses** under `PRESS_RELEASE`: at least 2 sentinels, min-pages at least 24.
2. **Trim from the design profile.** Tolerance ±1.0pt.
3. **File exists:** `PDF not found: <path>`.
4. **Detector self-test.** The verifier tests its own blank-page detector before using it. A synthetic blank 300×450 image must read blank, and one marked "KNOWN INK" must not. Failures read `blank-page detector failed to reject a blank fixture` / `blank-page detector rejected a marked fixture`. The blank rule is stddev < 1.2, or darkest pixel > 249 and mean > 252.5. This is invariant `INV-pdf-detector` (critical).
5. **pdfinfo.**
   - `required verification tool missing: <tool>`
   - `could not parse pdfinfo output`
   - `unexpected trim size: W x H pt (expected 6 x 9 inches)`
   - `suspiciously short PDF: N pages (minimum M)`
6. **Text via pdftotext,** whitespace folded.
   - Sentinels are exact case, with straight and curly quotes equated: `missing text sentinel in PDF: <s>`.
   - The title is case-folded, because title pages set it in caps: `missing title in PDF text: <title>`.
7. **Fonts via pdffonts:** `pdffonts found no fonts`; `unembedded fonts: [...]`.
8. **List links via pypdf.** Every link in "List of plates" and "List of Figures" must resolve to a page that carries an image XObject.
   - `<label> link <dest> resolves to no page`
   - `<label> links point at imageless pages: [n...]`
   - `<label> present but contains no links`
   - If pypdf won't import: `pypdf unavailable; illustration-list destinations not verified`.
9. **Render.** Uses a sandbox helper script if present; otherwise `pdftoppm -png -r 120`. The renderer fallback scar: "Keep that fallback working." Check: `rendered N pages, pdfinfo reports M`.
10. **Ink on every page.**
    - `apparently blank rendered pages: [...]`
    - `ink touches rendered page edge: [...]` (any pixel < 245 in a 2px border)
    - `inconsistent rendered page dimensions: [...]`
    - The print profile forgives exactly one isolated blank even page, the structural `\mainmatter` verso.
11. **Print profile only.**
    - **Mirrored margins.** Skipping the first 20% of pages, the median left ink edge of rectos and versos must differ by at least 18px at 120dpi:
      `print profile: margins do not mirror (recto left edge Xpx, verso Ypx); the gutter is missing`.
    - **Black ink.** A page fails when more than 200 pixels have an RGB channel spread of 48 or more. The check is skipped when the profile is `ink: color`:
      `print profile: colored ink on pages [...] (a colored cover plate in a hand-authored tex/title-page.tex belongs on the wrap; supply tex/title-page-print.tex without it)`.
12. **Reading profile only: cover on page 1.** This applies when `assets/cover.jpg` exists and there is no `tex/title-page.tex`.
    - `assets/cover.jpg exists but page 1 of the reading PDF renders blank -- the cover plate was clipped off the page`
    - `... carries no cover image -- the generated front matter dropped it` (needs `pdfimages`; otherwise `note: pdfimages absent; cover-on-page-1 identity unverified`)

Success line:

```text
Verified <pdf>: N pages, 6 x 9 trim, embedded fonts, K sentinel(s) plus the title as witnesses, every rendered page contains ink, no edge clipping[, mirrored margins, black ink only | , cover on page 1]
```


### 6.2 The verify_formats checks (HTML, EPUB, Markdown, TXT, DOCX, site, agreement)

The checks below come from `src/press/verify_formats.py`.

- **Size floor.** HTML and EPUB must be at least 1000 bytes: `missing or suspicious artifact: <path>`.
- **Witnesses** (`INV-format-witness`, critical). Every format must carry three things:
  - the title: `<label> does not carry the book title: <title>`;
  - every sentinel;
  - the **manuscript witness**: the longest markup-free line of 40 or more characters across the chapters: `<label> lost the manuscript witness line: <first 60 chars>...`.
  If no such line exists, the check fails: `no manuscript witness derivable; ... (write one honest plain sentence)`.
- **HTML.** Checks are `HTML missing sentinel`, `HTML output has no html element`, and figure-label parity: `HTML carries N numbered-figure labels; the source declares M`.
- **EPUB.**
  - `EPUB has invalid mimetype`
  - `EPUB missing container.xml`
  - `EPUB carries an empty dc:date (retail validators reject it); the date field should contain a four-digit year`
  - `EPUB metadata is missing the registered ISBN <isbn>`
  - sentinels, witnesses, and figure-label parity
- **epubcheck**, run by `epubcheck()`:
  - Missing inside the toolchain (`PRESS_TOOLCHAIN` set) is fatal: `epubcheck missing from the press toolchain image; the retail-format gate cannot be skipped where releases are cut`.
  - Missing locally is only a warning: `WARNING: epubcheck not installed; EPUB validated structurally only. The press toolchain runs the full check in CI. (brew install epubcheck)`.
  - Present but unrunnable (the binfmt scar) reads `epubcheck is present but cannot run (<exc>); the toolchain image is broken`.
  - A nonzero exit reads `epubcheck failed on <path> (exit N):` followed by its output. A pass prints `epubcheck passed: <name>`.
  - Strictness keys on `PRESS_TOOLCHAIN`, not `CI`. The source comment reads, verbatim: "CI=false would read truthy" (verify_formats.py, the epubcheck branch).
- **Markdown and TXT** get sentinels and witnesses.
- **DOCX** text is joined across `w:t` runs. The check fails with `docx embeds N images; expected at least M plates`.
- **Reader site.**
  - Structure: `site missing index.html`, `site missing reader.css`, `site has N chapter pages; expected at least M`.
  - Per-chapter identity, where each chapter's witness must appear on exactly one page: `reader site is missing <chapter>: ...` / `reader site duplicates <chapter>: ...`.
  - `site carries N plates; expected M`.
- **Cross-edition agreement.** Every chapter's witness must appear in every edition, the PDF included when `pdftotext` exists. The match is any 8-word window stepped by 4, which tolerates running heads and glued words.
  - Failure: `<label> disagrees with the manuscript: it is missing content from N chapter(s) (...)...`.

Success line:

```text
Verified <files> (K sentinel(s), the title, and the manuscript line '<40 chars>...' as witnesses); E editions agree on all C chapter witnesses
```


### 6.3 The verify_pages and verify_archives checks

**`verify_pages`** crawls `dist/pages`, following every href, src, CSS `url()`, and `.css` file.

- Reference failures: `dead fragment`, `absolute reference`, `broken reference`, `reference escapes the site`.
- Every declared download must exist, and the landing page must link it **exactly once**: `landing page links <name> N times (expected exactly once)`.
- Sentinels must appear on the public reading surface.
- **Commerce.** A CTA is required exactly when the book enables commerce, generated policy pages must disclose the seller, and no secret may leak.
- **Metadata.**
  - JSON-LD present and naming the book.
  - Canonical present exactly when `site-url` is set.
  - Open Graph title and Twitter card on every surface.
  - No foreign edition in JSON-LD.
  - `og:image` must resolve.
  - The head must not match `/Users/|/home/|/dist/|/build/|file://`.
- **Sitemap.** Present exactly when `site-url` is set, with every `<loc>` resolving and every canonical listed.

Success line:

```text
Verified dist/pages: every local reference resolves (fragments and stylesheet assets included), N downloads present and linked, sentinels on the public reading surface
```

**`verify_archives`** covers three files.

- **Reader zip.** It must equal `dist/site/` file by file, compared by sha256 digest (`INV-archive-site-bytes`).
- **Source zip.** It is recomputed from the same `publication_members()` policy, and every member must be DEFLATED (`INV-archive-source-policy`, critical). Members are git-tracked files only, under a `{slug}/` prefix, with fixed timestamp 2026-07-16 12:00, modes 0o755 or 0o644, and deflate level 9. Excluded and rejected material:
  - Excluded directories: `build`, `dist`, `.git`, `__pycache__`.
  - A secret-pattern file **aborts** the archive: `.env`, `.env.*`, `*.pem`, `*.key`, `*.p12`, `*.pfx`, `id_rsa*`, `id_ed25519*`, `.netrc`, `*.keychain`, `credentials*`, `*.secret`.
  - Junk is skipped: `.DS_Store`, `Thumbs.db`, `*.swp`, `*~`.
  - Symlinks are never dereferenced.
- **Sources companion,** when `config/authorities.yaml` exists. It must name the book, be at least 200 characters long, and contain an entry marker: `sources companion looks empty of entries`.


### 6.6 Sentinels and min-pages, summarized

**Sentinels** (`verify-sentinels`) are checked in four places:

- in the manuscript (`check_source`);
- in the PDF text, exact case;
- in every format (`verify_formats`);
- on the public reading surface (`verify_pages`).

**Min pages** (`verify-min-pages`) is the PDF floor:

- the model default is 40, while the scaffold template writes 1;
- a release needs at least 24.

When `PRESS_RELEASE=1`, at least two sentinels are required.


### 6.7 Coverwrap verification

The wrap must be one page, and its size must equal the generator's own computed layout within 0.01in. The other checks:

- embedded fonts;
- no soft-mask transparency;
- images no more than 600 PPI;
- the title survives as text;
- not blank;
- a front panel stddev of at least 8;
- a barcode card;
- with an ISBN: at least 25 transitions on the scanline (EAN-13 has 59) and clean quiet zones.

Details are in §10.6.

---


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


### 2.3 `press doctor`

Real output shape, captured on a macOS authoring machine:

```text
press doctor
  [     ok] pandoc     every build target
  [     ok] lualatex   PDF and print builds
  [     ok] latexmk    PDF and print builds (multi-pass convergence)
  [     ok] pdftoppm   PDF verification renders
  [     ok] pdffonts   font-embedding verification
  [     ok] pdfinfo    PDF structure verification
  [     ok] pdftotext  PDF text verification
  [     ok] git        scaffolding identity and book repositories
  [ absent] epubcheck  the retail EPUB gate (softens to a warning locally)
  [ BROKEN] claude     present but cannot execute; the operator: press improve, research, aesthetic briefs
  [     ok] realesrgan plate enhancement upscaling (press art enhance)
  [     ok] OPENAI_API_KEY   press art commission --model openai
  [     ok] GEMINI_API_KEY   press art commission --model gemini
  [     ok] python     3.12 is within the tested range 3.10 to 3.14
  [     ok] python     Pillow, pypdf, ruamel.yaml importable

not ready: claude (macOS: brew install pandoc mactex-no-gui poppler; Debian/Ubuntu: see the Dockerfile's package list)
```

That run exited 1. The `BROKEN claude` line is an artifact of the sandboxed capture environment and does not reflect a normal machine. Writers can use it as an example of the broken state.

- **States:** ok, absent (an optional tool missing), MISSING (a required tool missing), BROKEN (present but fails both `--version` and `-v` within 15 s), warn, unset. They print in a 7-character gutter.
- **Ready line:** `this machine can make books`.
- **Exit:** 0 when ready, 1 otherwise.
- **Surprise:** a *broken optional* tool also denies readiness (`doctor.py:46-50`).
- **Python out of range:** `X.Y is outside the tested range 3.10 to 3.14 (see docs/COMPATIBILITY.md)`.

doctor's findings are typed. The desk renders them as a panel (§13).

---


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

## S1. `press verify` on the Alice example (exit 0), verbatim apart from path elision

```text
$ press verify
  pandoc took 23.7s
Verified alice-in-wonderland.pdf: 23 pages, 6 x 9 trim, embedded fonts, 2 sentinel(s) plus the title as witnesses, every rendered page contains ink, no edge clipping, cover on page 1
```

## S2. `press verify-formats` on the same book (exit 0), verbatim apart from path elision

```text
$ press verify-formats
+ stitched 4 files -> dist/alice-in-wonderland.md
~/alice/dist/alice-in-wonderland-source.zip
archived 12 files; excluded dirs ['.git', '__pycache__', 'build', 'dist']
WARNING: epubcheck not installed; EPUB validated structurally only. The press toolchain runs the full check in CI. (brew install epubcheck)
Verified alice-in-wonderland.html, alice-in-wonderland.epub, alice-in-wonderland.md, alice-in-wonderland.txt, alice-in-wonderland.docx, site/ (2 sentinel(s), the title, and the manuscript line 'and here alice began to get rather sleep...' as witnesses); 7 editions agree on all 4 chapter witnesses
Verified archives: alice-in-wonderland-site.zip, alice-in-wonderland-source.zip
```

The slug is `alice-in-wonderland`; the book's sample uses `alice`. The WARNING line is what a machine without epubcheck prints; in the toolchain image epubcheck runs. The `press all` run that preceded these ended with `  ¶ verify     ✓ 7 editions match source` (full capture in facts-01 S3).

## S3. The witnesses (from `verify_formats.py`, as the fact base glossary and the production probe state them)

- The *manuscript witness* is the longest markup-free line of 40 or more characters in the whole manuscript: a line containing none of the characters `* _ ` [ ] ( ) < > " ' & # ! |`. Every edition must carry it.
- A *chapter witness* is the same rule applied per chapter file: its longest such line. The formats verifier requires all seven editions to agree on every chapter's witness ("7 editions agree on all 4 chapter witnesses" in the S2 capture), and the reader site uses the chapter witnesses for page identity.
- A raw line of 40 or more plain characters that is not prose (a long code line without any of those characters) can therefore become a witness and fail the HTML and EPUB verifiers when it does not survive rendering.

## S4. Ruling on the page floor

Press's own gallery Alice renders 23 pages with `verify-min-pages: 1`; the book's sample `alice` is the full novel and sets 24 only once its twelve chapters exist. Any capture from the gallery example is quoted as "the press's own three-chapter Alice example". See facts-06 S5.
