### 6.4 Editorial law: `press check`

`press check` runs four stages in order, stopping at the first failure:

1. **`check_source`.**
   - Per chapter file:
     - `missing source file`
     - `suspiciously short source` (body under 80 characters)
     - `no level-1 heading`
     - `unfinished marker '<phrase>'`, for `TODO: write`, `TBD: write`, or `lorem ipsum`
   - `metadata missing <key>:` for title, author, description, or slug.
   - Registrations and commerce failures.
   - `sentinel not found in the manuscript: <s>`.
   - Orphan plates.
   - Figure placement errors.
   - Config file shapes: index-terms, authorities, front-matter, house-rules.
   - Print feasibility: trim, binding, and ink against the provider catalog.
   - Passes as `Source checks passed: N ordered Markdown files`.
2. **`check_the_checkers`**, which proves the checkers can fail (§6.5).
3. **`style_audit`.**
   - Applies to every audited file (book/ plus `audit-dirs`):

     | Rule | Diagnostic |
     |---|---|
     | `—` U+2014 | `contains em dash` |
     | `–` U+2013 | `contains en dash` |
     | `\bin conclusion\b` | `generic conclusion` |
     | `it is important to note` / `it is worth noting` | `throat-clearing phrase` |
     | `at its core` / `the real question is` | `fake-revelation phrase` |
     | `let's (dive\|delve\|explore\|break this down)` / `without further ado` | `chatbot signposting` |
     | `stands as a testament` | `inflated significance` |
     | `vibrant tapestry` | `inflated AI phrase` |
     | `not only … but also` (within 120 chars) | `formulaic negative parallelism` |
     | trailing whitespace | `trailing whitespace` |

   - Book prose only: curly quotes, the glyph set, and the book's banned patterns.
   - Headings: manual numbers, title case. Paragraphs: 190 words.
   - Passes as `Editorial checks passed: N Markdown files`; warnings print as `Editorial warnings:`.
4. **Jargon.** Runs `python -m press.jargon_lint --fail-on rewrite [--allow T]... <chapter files>` and writes `build/jargon-report.txt`.
   - Passes as `Jargon check passed: no rewrite-status terms (full audit in build/jargon-report.txt)`.
   - Covers only the manuscript files, not `audit-dirs`.

`press style` runs the style audit alone.

**The jargon lint** (`src/press/jargon_lint.py`).

- Statuses and their levels: `allow` 0, `inspect` 1, `rewrite` 2, `ban` 3. `--fail-on none|inspect|rewrite|ban` defaults to `rewrite`.
- Flags: `--allow TERM`, `--include-quotes`, `--json`, `--max-findings` (default 500).
- It skips fenced code, inline code, URLs, and blockquotes.
- Word boundaries use `(?<![\w-])…(?![\w-])`, so "gate" never matches "gateway".
- Output format:

  ```text
  path:line:col: rewrite: 'seam' [structural metaphor]
    <context line>
    Ask: <question>
  ```

- The tool exits 2 on a malformed watchlist.

**The watchlist** (`src/press/data/skills/overused-jargon/references/watchlist.csv`).

- 53 rules. Columns: `term,match,status,category,question,allowed_when,source,notes`.
- 39 `inspect`, 14 `rewrite`, none `allow`/`ban`. Match types: 45 word, 8 phrase.
- The 14 rewrite terms: load-bearing, blast radius, footgun, yak shaving, belt-and-suspenders, belt and suspenders, smoking gun, seam, seams, substrate, cleanly, decisive, authoritative, genuinely.
- Example inspect terms: spine, gate, gating, scaffold, wiring, drift, parity, surface, clean, healthy, canonical, proves, truth, verified, honest, ship, lands, round-trip, end-to-end, fallback, stale, churn.

Example rows:

```text
load-bearing,phrase,rewrite,stock metaphor,"What depends on it, and what fails without it?",Literal structural use; direct quotation; deliberate house voice,user seed,Prefer the actual dependency and failure.
seam,word,rewrite,structural metaphor,Which two components or responsibilities meet here?,Literal material use; precise domain term; deliberate metaphor,user seed,Name the interface or shared responsibility.
gate,word,inspect,process shorthand,What condition must pass before what action?,Literal gate; logic gate; standard named domain concept,user seed,"May mean test, approval, deadline, flag, or authority."
```

**Two copies, one contract.** The package `src/press/jargon_lint.py` and the portable `src/press/data/skills/overused-jargon/scripts/jargon_lint.py` must be byte-identical function by function, except `parse_args` (selftest `check_jargon_parity`, `INV-editorial-jargon-parity`). A versioned corpus at `tests/corpus/jargon_parity/` drives both copies. The portable copy exists "so the skill is usable without installing the press".


### 6.5 Check the checkers (known-bad fixtures)

"A rule that cannot fail is not a rule." `check_the_checkers.py` runs the style audit and jargon lint over every packaged `src/press/data/known-bad/*.md` plus the book's `tests/known-bad/*.md`.

- A fixture declares the rule it must trip with a comment such as `<!-- expect: em dash -->`. Docs say "anywhere in the file"; the code's regex reads the first matching comment.
- The expected rule must appear, case-insensitively, as a substring of at least one diagnostic. Other diagnostics print as `note: <fixture> also drew: …` and do not fail.
- A fixture with no `expect:` comment needs only some rejection.
- The known-good fixture `src/press/data/known-good/clean.md` must draw zero diagnostics.

Failure messages:

```text
<fixture>: expected rule '<rule>' did not fire (<up to 3 others or "no diagnostics at all">)
<fixture>: no checker rejected a known-bad fixture (and it declares no expected rule)
<fixture>: a checker rejected the known-good fixture: …
```

The packaged 19 fixtures:

| Fixture | Expect |
|---|---|
| at-its-core.md | fake-revelation phrase |
| curly-quotes.md | curly |
| em-dash.md | em dash |
| emoji.md (🚀) | outside the print-font set |
| en-dash.md | en dash |
| in-conclusion.md | generic conclusion |
| jargon.md ("The seam is load-bearing and the blast radius is clean.") | jargon |
| lets-dive.md | chatbot signposting |
| long-paragraph.md (208 words) | words |
| negative-parallelism.md | formulaic negative parallelism |
| numbered-heading.md (`# 3. A numbered heading`) | manual number in heading |
| real-question.md | fake-revelation phrase |
| testament.md | inflated significance |
| throat-clearing-important.md | throat-clearing phrase |
| throat-clearing-worth.md | throat-clearing phrase |
| title-case.md (`# A Heading That Is Fully Title Cased Everywhere`) | title-case heading |
| trailing-whitespace.md | trailing whitespace |
| vibrant-tapestry.md | inflated AI phrase |
| without-further-ado.md | chatbot signposting |

`src/press/data/known-bad/expected.yaml` maps each fixture to its checker and diagnostic. It is "Generated from quality/fixtures.yaml".

**A book's own fixture** (`docs/CONFIGURATION.md`):

```markdown
This sentence is very unique. <!-- expect: very unique -->
```

Book fixtures are judged as book prose under the book's own banned patterns, so a book can prove its own house rules. The success output is quoted in §3.4. Invariant: `INV-editorial-checkers` (critical).


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


### 4.9 House rules a book adds

These go in `config/house-rules.yaml`:

```yaml
banned-patterns:
  "\\bvery unique\\b": "very unique (unique does not grade)"
jargon-allow:
  - leverage
audit-dirs:
  - appendices
```

- **Banned patterns** are case-sensitive regexes, as written. The diagnostic is `<file>:<line>: <label>`. A malformed regex is refused:
  `config/house-rules.yaml: banned pattern '<p>' is not a valid regex (<exc>)`.
- **`audit-dirs`** files get the dash and phrase battery but not the curly-quote, glyph, or banned-pattern rules. Heading and paragraph problems there are warnings, not errors.
- **`jargon-allow`** is case-folded.

---


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

# Supplement added by the managing editor (2026-11-11)

## S1. Which commands run the checker (from `src/press/__main__.py`, confirmed)

A bare format target (`press pdf`, `press epub`, `press html`, `press site`, `press txt`, `press docx`, `press markdown`) calls `build.build_target(<name>)` directly and does not run `press check` first. `press verify` builds the PDF the same way, then runs the PDF verifier. `press all` runs the checker's four passes first (source checks, check-the-checkers, style audit, jargon lint) and stops at the first failure before any format is built. So the known-bad fixtures run "in `press check` and `press all`, not in a bare `press pdf`" (fact base 20.A.10). The sentence "every build passes through press check" is true of `press all` and of CI (whose reusable workflow runs `press all`), and false of a bare format target; the chapter says which.

## S2. Exit status

The fact base records only "nonzero" for a failed `press check` (its exit is 1 in the captured refusals, see `press add` and `press check` captures where given); a usage error exits 2 (fact base 3.2 for `press add`). Say "exits with status 1" only where a capture shows it; otherwise "nonzero".

## S3. What the book's banned patterns read (tested 2026-11-11)

A banned pattern in `config/house-rules.yaml` does NOT fire inside a fenced code block, but it DOES fire inside inline code (a backticked span in a prose line) and in any other prose line. Test: a fence containing "leverages a robust" drew nothing; an inline `delve` on a prose line drew `assistant vocabulary`. The universal battery behaves the same way ("Prose rules skip fenced code, except the trailing-whitespace rule").

## S4. A real `press check` on press's own Alice gallery example (four manuscript files, no book fixtures), verbatim apart from path elision

```text
$ press check
Source checks passed: 4 ordered Markdown files
  note: em-dash.md also drew: - .../known-bad/em-dash.md:4: glyph U+2014 is outside the print-font set
  note: en-dash.md also drew: - .../known-bad/en-dash.md:4: glyph U+2013 is outside the print-font set
Checker self-test passed: 19 known-bad fixtures each tripped their declared rule, known-good fixture accepted, 2 extra diagnostics noted
Editorial checks passed: 4 Markdown files
Jargon check passed: no rewrite-status terms (full audit in build/jargon-report.txt)
```

## S5. Ruling on the two Alices

The book's running sample `alice` is the full novel (twelve chapters) that user alice is producing; press's gallery example `alice-in-wonderland` holds chapters 1 to 3 of the novel plus one appendix and renders 23 pages. A capture taken from the gallery example (this one, the `press all` in facts-01 S3, the verify runs in facts-08) is quoted as such: "on the press's own three-chapter Alice example". The fresh-scaffold capture in 3.4 (one file, 19 fixtures) is labelled as a fresh scaffold's output, never as the Alice book's. The sample book sets `verify-min-pages: 24` only once its chapters exist.

## S6. The title-case test's small words (from `style_audit.py`, verbatim list)

a, an, and, as, at, but, by, for, from, in, into, nor, of, on, or, over, the, to, up, with, without (21 words). The test ignores the heading's first word, these words, and ALL-CAPS words; if at least three candidate words remain and 80 percent or more of them are capitalised, the heading is refused as title case.

## S7. Two names

The fixture pass prints `Checker self-test passed: ...`; call it the *checker self-test*, press's own name. Press's own test suite (pytest, `press selftest`) is a different thing: call it *press's test suite* or `press selftest` by name, never "the self-test".
