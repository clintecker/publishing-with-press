## 7. Design and typography: the house design in numbers

### 7.1 The PDF interior (house-6x9)

The figures below come from `src/press/data/tex/book-header.tex`, `src/press/data/defaults/pdf.yaml`, and `src/press/data/profiles/house-6x9.yaml`.

**Page and fonts.**

- **Class:** KOMA `scrbook`, `oneside, openany, headings=small` for the reading PDF. Print uses `twoside, open=any, headings=small`; the KOMA spelling `open=any` is required, because "openany is silently ignored under twoside", and "open=right would ship genuinely blank versos".
- **Trim:** 6in × 9in.
- **Margins:** inner 0.78in, outer 0.68in, top 0.72in, bottom 0.78in, headsep 0.20in, footskip 0.38in. The text block is about 4.54in × 7.5in.
- **Print interior margins:** `print-header.tex` resets inner 0.88in / outer 0.58in. That is the same 1.46in total, shifted toward the gutter and mirrored by twoside.
- **Body face:** Libertinus (`\usepackage{libertinus}`). The packaged default is used when `typography.pdf-family` is empty. Otherwise `\setmainfont{<family>}[Numbers=OldStyle]` applies.
- **Mono:** Source Code Pro, scaled 0.86.
- **Size and leading:** 10pt, `\linespread{1.045}`.
- **Paragraphs:** `\parindent` 1.1em, `\parskip` 0pt.

**Microtypography and line breaking** (v3.0.0).

- **Microtype:** `protrusion=true,expansion=true,final=true`.
- **`selnolig`:** no ligature across a morpheme seam (`shelf|ful`).
- **Oldstyle figures** for the aesthetic font.
- **Widows and orphans:** `\clubpenalty`, `\widowpenalty`, `\displaywidowpenalty`, `\brokenpenalty`, `\finalhyphendemerits`, `\doublehyphendemerits` are all set to 10000.
- **Runts:** `\parfillskip=0pt plus 0.8\hsize`.
- **Hyphenation:** `\lefthyphenmin=3 \righthyphenmin=3`, `\hyphenpenalty=150`.

**Colours.** The defaults below are overridable by `book-colors`:

| name | hex |
|---|---|
| ink | #171717 |
| muted | #5C5C5C |
| rulegray | #C8C8C8 |
| papergray | #F4F4F1 |
| accent | #4B3E8A |
| linkgreen | #46621F |

Links: `linkcolor: black`, `urlcolor: linkgreen` (black in print), `colorlinks: true`.

**Running heads and footers.**

- `\ihead`: the book title, italic, footnotesize, muted.
- `\ohead`: `\leftmark` (the chapter).
- `\cfoot`: a centred folio, also on plain pages, so chapter openers are numbered.
- `\automark[section]{chapter}`.

**Headings.**

- Chapter, section, and subsection are bold, ink-coloured, and ragged.
- Chapter afterskip is 1.25\baselineskip.
- Section skips are 1.6/0.55\baselineskip; subsection skips are 1.2/0.35.
- `\Needspace` reserves 5 lines before a section and 4 before a subsection.

**Contents and lists.**

- `toc-depth: 1`; "Contents".
- The "List of plates" uses the `lof` file. The tocdepth scar is fixed by `\addtocontents{lof}{\protect\setcounter{tocdepth}{1}}`.
- The "List of Figures" uses a separate `.lof2` file through `\PressListOfFigures`.

**Captions.** The `caption` package is the single caption authority: `font={small,it}, labelformat=empty, justification=centering, hypcap=true`. The separate `hypcap` package was removed (§20). Figures use `[H]`, so they stay where the source puts them.

**Figure cap.** `\PressFigureCap`, 6.3in by default and per profile (§4.2).

**Drop caps.** `lettrine` 3 lines, `findent=2pt`, small-caps remainder (§4.5).

**Blockquotes.** `mdframed`, papergray.

**Fallback title** (no front matter): 25/29pt bold title, `\Large` muted subtitle.

**Fixed design across profiles.** The interior is always single ink, except `house-6x9-color`. That is a craft law, which the aesthetic cannot change.

### 7.2 Profiles change the proportions

| profile id | trim | margins in/out/top/bot | figure cap | indent / leading | web measure / size / line height |
|---|---|---|---|---|---|
| house-6x9 (default) | 6×9 | .78/.68/.72/.78 | 6.3in | 1.1em / 1.045 | 48rem / 1.25rem / 1.62 |
| house-6x9-color (`ink: color`) | 6×9 | same | 6.3 | same | same |
| novella-5x8 | 5×8 | .70/.55/.62/.68 | 5.6 | 1.0em / 1.08 | 40rem / 1.2rem / 1.66 |
| digest-5.5x8.5 | 5.5×8.5 | .74/.62/.66/.72 | 6.0 | 1.05em / 1.06 | 44rem / 1.2rem / 1.64 |
| large-print-7x10 | 7×10 | .90/.75/.85/.95 | 7.2 | 1.1em / 1.2 | 54rem / 1.4rem / 1.8 |
| mass-market-4.25x6.87 | 4.25×6.87 | .62/.46/.56/.62 | 4.8 | 0.9em / 1.02 | 34rem / 1.15rem / 1.6 |

"choosing a profile changes the design's proportions; choosing an aesthetic changes its voice" (`docs/PRINT-FORMATS.md`).

The font family and palette stay with the aesthetic. Large print "sets a larger base face and markedly more open leading". Every profile's font size stays 10pt; only the leading changes.

### 7.3 The web reader (`dist/site`, from `src/press/data/web/`)

**`reader.css`.**

- **Palette tokens:** `--cloth:#5a7d2a --cloth-deep:#46621f --foil:#b8963f --foil-bright:#c9a961 --foil-deep:#8f7226 --paper:#f4efe3 --paper-warm:#ece5d3 --ink:#23201a --ink-soft:#4d463a`, plus `--link:var(--cloth-deep) --ornament:var(--foil-deep) --hairline:var(--foil)` and `color-scheme: light dark`.
- **Page frame:** the green cloth background holds a paper "leaf". It is max-width 48rem, with the font stack `"Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif`, 1.25rem / 1.62 line height, a foil border, an inset 4px paper outline, and a shadow. The frame drops below 56rem.
- **Headings:**
  - `h1` is centred at `clamp(1.9rem,5.5vw,2.5rem)`, with a small-caps "Chapter N" line and a diamond rule.
  - `h2` is small caps; `h3` is italic.
  - The first line after an h1 is set in small caps.
- **Rules and ornaments:** `hr` becomes a ◆ between gradient hairlines.
- **Drop cap:** floated at 3.1em, line-height .82.
- **Figures:** natural aspect ratio on a paper-warm mat with a foil border.
- **Dark mode:** `@media (prefers-color-scheme: dark)` with `--cloth:#141a0e --paper:#1d1b15 --paper-warm:#26231b --ink:#e8e0cc --ink-soft:#b5ab93 --link:var(--foil-bright)`. Images are dimmed with `brightness(.87)`.
- **Other:** print and reduced-motion rules; tables become cards below 34rem.

**Reader template** (`chunked-template.html`).

- `lang="$lang$"`, `rel=next|prev|prefetch`, and a "Skip to chapter" link.
- **Chapter pages:** a masthead (title, accesskey u), a `<details>` contents drawer with the current chapter expanded, and ←/→ links (accesskeys p/n).
- **Index page:** title block, optional cover, the lede "This is the reading edition…", and a "Start reading →" button (accesskey s).
- **Footer:** pager cards, the hint "use ← and → to turn pages", and a colophon linking `../index.html`.
- **Inline JS:** the arrow keys turn pages (ignored with modifiers or in form fields), and `aria-current` marks the current page in the drawer.

**Landing page** (`index-template.html`, `dist/pages/index.html`).

- The same tokens, but **no dark mode**, and `lang="en"` is fixed.
- `.leaf` max 44rem.
- **Sections:**
  - a "Read the Book" CTA with "one chapter to a page, as is proper";
  - a "Table of Editions";
  - "How This Book Was Built";
  - a footer reading "Printed on paper, electrons, or both."
- **Edition labels:**

  | file | label |
  |---|---|
  | .pdf | Print edition |
  | .epub | Circulating edition |
  | .html | Single-leaf edition |
  | .md | Manuscript edition |
  | .txt | Telegraphic edition |
  | .docx | Office edition |
  | -site.zip | Chapter edition, boxed |
  | -source.zip | Source edition |
  | -sources.md | Table of authorities |

  The first row is always "Chapter edition" → `read/index.html`.
- **The PDF row** reads "{trim}, typeset by LuaLaTeX, suitable for paper".
- **Subtitle stack:** `or,` clauses get their own lines.

**Head metadata** (`webmeta.py`, `reader_meta.py`).

- **Fields:** canonical, Open Graph, Twitter `summary_large_image`, and JSON-LD.
  - The landing page is a `Book` with `workExample` entries for the shipped editions.
  - A chapter page is an `Article` with `isPartOf` and a `BreadcrumbList`.
- **Chapter description:** the first `<p>` of at least 20 characters, cut to 157 characters plus "...".
- **Without `site-url`:** "when there is no public base URL, nothing URL-shaped is emitted". That means no canonical, no og:url/og:image, and no sitemap.
- **Social image:** the cover's real pixel dimensions are read from the file.

**`book.css`** (the single-file HTML edition).

- **Tokens:** `--ink:#171717 --muted:#5c5c5c --paper:#fbfbf8 --panel:#f1f1ed --rule:#c8c8c8 --accent:#4b3e8a`.
- **Type and layout:** Charter / Bitstream Charter / Georgia at 19px / 1.58, max 42rem. No dark mode.

**`epub.css`.** Minimal: serif at 1.45, drop cap at 3em, `figure img{max-width:100%}`. No colours: "the reader owns the theme".

**Overrides.**

- `assets/web/reader.css` **replaces** the house reader sheet entirely. The profile web measure is not appended.
- `assets/web/extra.css` is **appended** after a `/* assets/web/extra.css */` comment, so it wins the cascade. It is also injected as a `<style>` on the landing page.
- A book supplying neither "renders byte-identically to before".
- The aesthetic palette applies to either sheet.
- The chapbook example's `extra.css` uses `.reader main {max-width: 30rem}` and line-height 1.85 for verse.

### 7.4 `config/aesthetic.yaml` knobs

The full treatment is in §8.8. The knobs that matter for design:

- `web-palette` and `web-palette-dark`. Tokens are substituted before and after the dark-mode seam.
  - The book-aesthetics skill lists these tokens: paper, paper-warm, ink, ink-soft, cloth, cloth-deep, foil, foil-bright, foil-deep, hairline, link, ornament.
- `typography.web-family`
- `typography.pdf-family`
- `book-colors.{ink,muted,accent,link}`, given as hex without `#`. These become `\definecolor` in `build/aesthetic.tex`, with link → `linkgreen`.
- `scene-break`
- `cover.style`
- `plates.style`

The merge is a **top-level replace**: "restate a whole section when you touch it".

### 7.5 Design is part of the contract

From `docs/ARCHITECTURE.md`:

> Within a major version, a fix may correct broken output ... but must not change the typography or layout of a book that was already valid. A book that rebuilt cleanly yesterday must produce the same design today.

The machinery that holds this in place:

- Profiles carry a `design-major` and are sealed by digest in `src/press/data/profile-seals.yaml`.
- `check_profile_seals` turns red on drift.
- Visual regression baselines are re-recorded only "with a reason" in a new major.


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


### 4.4 Scene breaks

In the manuscript a scene break is a Markdown thematic break, `* * *`. The aesthetic key `scene-break` chooses how it renders (`scene-break.lua`):

- **`rule`** (the default) is the plain horizontal rule. In the reader it is a diamond ◆ between gradient hairlines.
- **`asterism`** is a centred `*\quad*\quad*` in the PDF and `<p class="asterism">* * *</p>` on the web.
- **`fairy-dust`** is Tenniel's 1866 staggered array of asterisks in three rows of 4, 3, 4. The PDF uses `\PressFairyDust` (step 1.9em); the web uses `<div class="fairy-dust" role="separator" aria-hidden="true">`.

The txt and docx editions keep a plain rule.


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