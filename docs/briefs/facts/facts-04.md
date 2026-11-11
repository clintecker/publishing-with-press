## 4. Writing the manuscript

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

### 4.2 Figures and plates

The canonical syntax is an image with attributes, optionally followed by an `art:` comment:

```markdown
![A compositor at the case](assets/fig/compositor.jpg){.plate style=wood-engraving}
<!-- art: a compositor's left hand holding a brass composing stick, thumb setting
     the measure; type in the case behind; 19th-c workshop, high contrast line,
     no lettering -->
```

- **The four fields.** A figure carries four separate fields. The *caption* is a reader-facing label. The `art:` comment is art direction. `fig-alt` is accessibility text. A credit line is separate again.
  - The press never uses the caption as art direction: "A caption is a label, not art direction (#225)".
  - The comment may be `art:`, `data:`, or `source:`. It may sit on the next line or after one blank line (`figures.py:93-99`).
- **Kinds** are set by the first class on the image:
  - Generatable: `.plate`, `.figure`, `.map`, `.photo`.
  - Data kinds, routed away from the image model: `.chart`, `.diagram`.
  - With no class at all the kind is `figure` for `press figures` purposes. For numbering, though, a bare image is an unnumbered plate.
- **Plates vs numbered figures** (v3.0.0).
  - A *plate*, which is any bare `![…](…)` or `.plate`, is the "literary woodcut idiom". It is unnumbered and listed in the **List of Plates**. That list appears only when `assets/woodcuts/` holds files.
  - An explicit `.figure`, `.chart`, `.map`, `.photo`, or `.diagram` that is not `decorative=true` is an *informative figure*. It is numbered by chapter as "Figure C.N", listed in a separate **List of Figures**, and becomes a cross-reference target.
  - "Plates are **never** numbered."
- **Cross-references.** Give the figure an `#id` and cite it with `@id`. The common convention is `@fig:press`.

  ```markdown
  As @fig:press shows, the platen does the pressing.

  ![The hand press at work](assets/fig/press.jpg){#fig:press .figure
      width=half-measure fig-alt="A hand press, the platen raised over a sheet"}
  ```

  - In LaTeX this becomes `\hyperref[id]{Figure~C.N}`; elsewhere, a link `Figure C.N` → `#id`.
  - There is no pandoc-crossref dependency. The number is computed once by `figure-numbering.lua`.
  - An unknown `@id` is left as a raw citation.
  - There is no chapter or section cross-reference mechanism.
- **Placement vocabulary** (`docs/ILLUSTRATIONS.md`; validated in `src/press/figures.py`):

  | attribute | values | meaning |
  |---|---|---|
  | `width` | `full-measure`, `half-measure`, `third-measure` | width against the line (in-flow figures only) |
  | `place` | `inline`, `wrap-inner`, `wrap-outer`, `plate`, `frontispiece`, `full-bleed`, `margin` | where it sits; wrap runs text around the **parity-aware** side (never left/right) |
  | `outset` | a length in em (default `1em`) | the runaround gap — the book-trade term, not "standoff" |
  | `fig-alt` | text | the **accessible alt text** — a fourth field, distinct from the visible caption, the `art:` prompt, and any credit line |
  | `decorative` | `true` | an ornament: empty alt, never numbered |

  **What `press check` refuses** (`figures.validate`, `figures.py:236-303`):
  - the sides `left`, `right`, `inner`, `outer`, `wrap-left`, `wrap-right` ("not parity-aware");
  - an unknown `place`;
  - an unknown `*-measure`;
  - a measure on a place that is not in-flow (in-flow places are `inline`, `wrap-inner`, `wrap-outer`, `margin`);
  - an absolute length (pt, px, in, cm, mm, %) on an in-flow place;
  - a non-em outset;
  - `decorative` together with `fig-alt`.

  **What each placement does in the PDF** (`figure-numbering.lua`):
  - **`wrap-inner` / `wrap-outer`** become `\Needspace*{guard\baselineskip}` plus `\begin{wrapfigure}{i|o}{measure}`. The default measure is `0.4\linewidth`. The guard in lines is full 20, half 13, third 9 (default 11). The wrap is fused onto the head of the next paragraph so text really runs around it.
  - **`margin`** is an outer-side wrap inside the text column, not in the true margin.
  - **`full-bleed` / `frontispiece`** take a cleared leaf of their own, using `\captionof` with no float. A frontispiece clears to an even page with `\cleardoubleevenpage` so it faces the next chapter. "full-bleed" does not actually ink the trim.
  - **`inline` / `plate`** are ordinary `[H]` figures.
  - **Reflowable formats.** Placement is print-only. In the EPUB, HTML, reader, markdown, txt, and docx editions a placed figure becomes a clean in-flow figure.
- **The height cap.** Every image is scaled down to fit both `\PressFigureCap` (height) and `\linewidth` (width), and never up. The redefined `\pandocbounded` in `book-header.tex:148-186` does this. The cap is set per profile: house 6.3in, novella 5.6, digest 6.0, large-print 7.2, mass-market 4.8.
- **Orphaned plates.** Any plate on disk under `assets/woodcuts/` that the manuscript never references fails `press check`:
  `plate never referenced by the manuscript: assets/woodcuts/<name>`.
- **`press figures`** prints every declared figure as JSON. The fields are file, src, caption, kind, style, directive, description, generatable, identifier, width, place, outset, alt, decorative, and numbered. This is "the authoritative reading" that `press illustrate` and the art-direction workflow use.

### 4.3 Set pieces (v3.0.0): `::: cascade`, `::: verse`, `::: tail`

These are fenced divs, normally wrapping a line block. `set-pieces.lua` lays out the form. If there is no line block inside, each paragraph counts as one line.

```markdown
::: verse
| 'Tis the voice of the Lobster;
| I heard him declare,
:::
```

- **`cascade`** steps each line one more indent: 2.4em times (line − 1). It suits an address or an inscription. The Alice example uses it for "Alice's Right Foot, Esq."
- **`verse`** sets the house stanza measure, `\PressVerse`: `\leftskip=3em`, no indent, 0.7em above and below. A blank line gives a stanza gap. Opening quotes hang by protrusion. In the reader it is `.verse` with a left margin of 2.4em.
- **`tail`** builds a serpentine calligram from the lines. The offset is `3.0em·sin(t·2π)` and the type size tapers `\normalsize → \small → \footnotesize → \scriptsize → \tiny`; on the web, 1em → .68em. It exists for the Mouse's Tale in Alice.
- **Output by format.** The text stays live, searchable, and accessible. Plain text and docx get a native line block. **The Markdown edition gets the raw `:::` source**, because no Lua filter runs on it (§5).
- A book that uses none of these renders byte-for-byte as before.

### 4.4 Scene breaks

In the manuscript a scene break is a Markdown thematic break, `* * *`. The aesthetic key `scene-break` chooses how it renders (`scene-break.lua`):

- **`rule`** (the default) is the plain horizontal rule. In the reader it is a diamond ◆ between gradient hairlines.
- **`asterism`** is a centred `*\quad*\quad*` in the PDF and `<p class="asterism">* * *</p>` on the web.
- **`fairy-dust`** is Tenniel's 1866 staggered array of asterisks in three rows of 4, 3, 4. The PDF uses `\PressFairyDust` (step 1.9em); the web uses `<div class="fairy-dust" role="separator" aria-hidden="true">`.

The txt and docx editions keep a plain rule.

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

### 4.6 Epigraphs

There are two kinds.

- **The book epigraph** is generated from `config/front-matter.yaml` (`epigraph.quote`, `epigraph.attribution`) onto its own front-matter page (§9).
- **A chapter epigraph** is just a Markdown blockquote placed right after the chapter heading. The drop cap skips blockquotes and lands on the first real paragraph.

No dedicated chapter-epigraph syntax exists.

### 4.7 Typographic spacing (v3.0.0)

`typographic-spacing.lua` adds a non-breaking space (U+00A0, `~` in LaTeX) in three situations, in every edition:

- after a title before a capitalized word: Mr., Mrs., Ms., Dr., Prof., St., Mt., Sr., Jr., Rev., Hon., Capt., Sgt., Gen., Col., Lt., Fr.;
- after a reference form before a digit: p., pp., No., Nos., Fig., Figs., Ch., Vol., Pt., Eq., §, ¶;
- between chained initials, as in "C. L. Dodgson".

"The manuscript stays plain prose; the house does the fine work, and ordinary sentences (every full stop included) are left exactly as typed."

### 4.8 Index terms, authorities, sentinels, front matter

These are covered elsewhere: front matter, index, and authorities in §9; sentinels in §3.3 and §6.

How each one shows up while writing:

- **Index terms.** You never mark up the manuscript. Terms are matched by pattern from `config/index-terms.yaml`.
- **Authorities.** The `claim` must be an exact fragment of your prose. Rewording that sentence fails the build.
- **Sentinels.** These must survive every revision verbatim.

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