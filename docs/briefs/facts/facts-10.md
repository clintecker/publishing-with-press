## 9. Front matter, index, authorities, colophon

### 9.1 Generated front matter (`src/press/gen_front_matter.py` + `src/press/data/tex/front-matter.tex`)

**When it activates** (`gen_front_matter.py:241-256`):

- If `tex/title-page.tex` exists, front matter is never generated. That file is "the whole-cloth override".
- Otherwise it is generated when `config/front-matter.yaml` exists. For the reading PDF only, it is also generated when `assets/cover.jpg` exists, so the cover plate can show.
- The print interior is generated with `include_cover=False`. The cover belongs on the wrap.
- The output goes to `build/front-matter.tex`. Any leftover copy is deleted first.
- A print-only override, `tex/title-page-print.tex`, replaces the title page for the interior so the two never stack.

**Required metadata** once front matter is on: title, author, copyright, publisher, publisher-place. A missing key fails with:

```text
front matter needs these config/metadata.yaml keys: …
```

**Shape check.** `epigraph` must be a mapping with `quote` and `attribution`.

**Page order.** Everything is inside one redefined `\maketitle`, which honors the "never stack a third `titlepage`" scar.

1. **Cover plate.** Shown when the cover is on: `width=\textwidth,height=\textheight,keepaspectratio`.
2. **Title page.**
   - Title at 30/34pt bold, uppercased, with a full stop added unless it already ends in `.`, `!` or `?`.
   - A 0.9in muted ornamental rule.
   - The subtitle as stacked OR clauses. It is split on `;? or,`; each clause after the first gets a small-caps "or," line, and all clauses are set in small caps, lowercased.
   - A second rule, only when there is a subtitle. This was fixed in v3.0.0: before, a subtitle-less book showed two empty rules.
   - "by", then the authors in `\Large\scshape`.
   - The place, lowercased.
   - The year in **lowercase roman numerals**.
3. **Colophon**, in this order:
   - edition line: `edition-note`, else the date before its first comma, lowercased
   - `rights-notice`, then a rule
   - copyright
   - "Published by <publisher>"
   - place
   - `manufacture`
   - registration lines ("ISBN (print) …", "ISBN (ebook) …", "LCCN …")
   - `contact`
   - `colophon-note` (italic)
   - `motto` (italic)
   - the logo `assets/press-logo.png` at 1.7in. Print uses the flattened `build/print-assets/assets/press-logo.png`.
4. **Dedication.** `\vspace*{2.1in}`, a 3.1in italic parbox.
5. **Epigraph.** 1.7in down, `\Large\itshape`, attribution in muted.
6. **Acknowledgements.** 1.2in down, a 3.6in parbox.

**How optional blocks work.** Each one sits between `%<<if name>>` and `%<<end name>>` markers and is kept or dropped. Every value is LaTeX-escaped (`\ & % $ # _ { } ~ ^`).

**The scaffolded `config/front-matter.yaml`**, verbatim:

```yaml
# Front matter facts. The presence of this file asks the press to
# generate the PDF's title page, colophon, and surrounding pages from
# config (delete it, or supply tex/title-page.tex, to opt out). The
# title page stacks the subtitle's OR clauses when the subtitle is
# written as "OR, ...; OR, ...". Everything below is optional and
# absent sections simply do not render; the identity facts (title,
# author, copyright, publisher, place, date) come from metadata.yaml
# and are never restated here.

# dedication: "For the night shift."

# epigraph:
#   quote: "The devil did it."
#   attribution: "Every printer, since printing began"

# acknowledgements: >-
#   The author thanks the machines, who worked without complaint, and
#   the people who taught them what to refuse.

# Colophon knobs. edition-note overrides the line derived from the
# date field; manufacture is the classic origin line; colophon-note is
# the production note naming type and method.
# edition-note: "first edition, second printing"
# manufacture: "Published in the United States of America"
# colophon-note: >-
#   Set in Libertinus Serif by machines under supervision, and proofed
#   by machinery that was itself proofed.

# rights-notice: >-
#   All rights reserved. No part of this book may be reproduced without
#   permission of the publisher.

# contact: "you@example.com"

# motto: "A line of the press, set in italics at the colophon's foot."
```

**Setting it from the CLI** (`docs/BOOK-PARTS.md`):

```sh
press config set copyright "© 2026 Jane Roe" && \
press config set publisher "Old Street Press" && \
press config set publisher-place "London"
press config set dedication "For my mother, who kept every letter."
press config set epigraph.quote "We are what we pretend to be." && \
press config set epigraph.attribution "Kurt Vonnegut"
press config set edition-note "First edition" && press config set motto "Made slowly."
```

Setting any front-matter field creates `config/front-matter.yaml`.

Invariant `INV-front-matter-golden` holds generated front matter byte-for-byte against a golden copy.

**Absent file.** "no generated front matter; the formats build with pandoc's plain title handling." The fallback `\maketitle` in `book-header.tex` sets the title at 25/29pt bold, a `\Large` muted subtitle, the author, the date, and the publisher. The publisher comes from the env var.

### 9.2 Subject index (`src/press/gen_index.py`)

**Config:** `config/index-terms.yaml`, a *list* of entries. With no file there is no index.

```yaml
- term: Margins
  match: [margin, margins]
- term: Spine width
  match: [spine width, spine arithmetic]
```

**Matching.**

- Fenced code, inline code, and `![` image lines are stripped first.
- Matching is case-insensitive, with the boundary `(?<![\w-])…(?![\w-])`.
- Locations are **chapter and appendix labels, not page numbers**: `Preface` for `00-*`, the chapter integer, or the appendix letter.
- From the code: "Numbers are chapters and letters are appendices; both stay put across editions, which page numbers do not."
- The docs ("A page-accurate subject index", "Press will not print a wrong page number") overstate this; see §20.

**Output.**

- File: `build/generated/<letter>-index-of-subjects.md`. The letter is the first free one from `a` to `y`.
- Heading: `# Appendix X: Index of subjects {-}`.
- Then a fixed explanatory paragraph.
- Then entries sorted alphabetically: `**term** · 1, 3, A`.

**A zero-hit term fails the build:**

```text
gen_index: curated terms match nothing in the text: <terms> (fix the patterns or remove the terms; silence is not allowed)
```

**Shape errors**, raised by `press check`, `press config validate`, and every build:

- `must be a list of {term, match} entries, not … (see docs/CONFIGURATION.md)`
- `entry N: term is missing or empty`
- `entry N: match must be a non-empty list of strings`

A `terms:` wrapper is refused.

### 9.3 Table of authorities (`src/press/gen_authorities.py`)

**Config:** `config/authorities.yaml`, a list.

```yaml
- claim: "the Model T sold for $260 in 1925"
  authority: "Ford Motor Company annual report, 1925"
  url: https://example.org/ford-1925
  file: book/chapters/03-price.md
  note: "list price, not average transaction price"
```

| Key | Status | Meaning |
|---|---|---|
| `claim` | required | Exact fragment, matched as a whitespace-normalized, case-sensitive substring |
| `authority` | required | The source |
| `file` | preferred | Pins the claim to one chapter |
| `url` | optional | |
| `note` | optional | "a dry aside" |

**The ledger must hold on every build.** All problems are collected under `gen_authorities: the ledger does not hold:`.

```text
entry N: malformed (not a mapping) / (claim missing or empty) / (authority missing or empty)
entry N: duplicate claim "…" (first stated at entry M)
entry N: missing, "…" matches nothing in the book (the text moved out from under its citation)
entry N: ambiguous, "…" matches T times (<file> xN, …); lengthen the fragment or declare file:
entry N: declares unknown file "…"
entry N: ambiguous, "…" appears K times in <file>; lengthen the fragment
entry N: moved, "…" is no longer in <file> but appears in <where>; update file:
```

With a declared `file:`, only that file's count must be exactly 1. Occurrences elsewhere are allowed.

**Output: a standalone companion** `dist/<slug>-sources.md`. It is **not** an appendix inside the book, a change made explicit in CLAUDE.md.

- Heading `# <Title>: sources and authorities`.
- `*Companion to <Title> by <authors>[, publisher][, date].*`
- Entries are grouped under `## In the preface`, `## In chapter N`, `## In appendix X`.
- Each entry reads `- "<claim>": <authority>. <url> <note>`.
- Every field passes through `print_safe`:
  - dashes become `", "`
  - quotes are straightened
  - the ellipsis becomes `...`
  - NBSP becomes a space
  - a backslash becomes a space
- The companion is published as a download, labelled "Table of authorities".
- It is verified by `verify_archives`: it must name the book, run to at least 200 chars, and contain an entry marker.

**It is not a citation engine.** "It verifies a sources ledger; it is not a BibTeX or CSL citation engine." Use footnotes for in-text citations.

**Populating it.** The `authorities-research` workflow (§14), or `press research`.

### 9.4 Colophon and identity lines

The colophon is generated (§9.1). Registration numbers flow into the colophon, into the EPUB identifier (`urn:isbn:`), into the OPF (verified), and into the wrap barcode. `pending` renders as `[pending]`.

The book CHANGELOG feeds the GitHub Release notes (§12).

### 9.5 What is not generated

- **Glossary.** Authored as a definition-list appendix. It is neither generated nor checked: "a feature to ask for".
- **"Also by" / further reading.** Authored. The cross-book catalogue is planned for Later — Catalog.
- **About the author.** Authored, `press add appendix about-the-author` → `z-about-the-author.md`.
- **Half-title.** BOOK-PARTS lists a "Half-title & title page". The generator code has a cover plate and a title page but no distinct half-title page, so writers should not promise a separate half-title leaf.

---


### 4.8 Index terms, authorities, sentinels, front matter

These are covered elsewhere: front matter, index, and authorities in §9; sentinels in §3.3 and §6.

How each one shows up while writing:

- **Index terms.** You never mark up the manuscript. Terms are matched by pattern from `config/index-terms.yaml`.
- **Authorities.** The `claim` must be an exact fragment of your prose. Rewording that sentence fails the build.
- **Sentinels.** These must survive every revision verbatim.


### 11.4 `registrations.retail`

`retail: true` turns missing or pending numbers into `press check` failures:

```text
retail edition declared while registrations are absent or pending: ...
```

When it is false they stay advisory.


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