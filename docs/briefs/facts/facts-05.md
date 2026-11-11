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


### 10.7 Print-safe images (`src/press/print_safe.py`)

The print build flattens every image onto white and caps its resolution, so a vendor preflight sees no transparency and no over-resolution.

- **Caps:** logo long edge 1000px; figures 1900px (about 300 PPI at 6.3in).
- **Conversion:** grayscale is kept; JPEG is written at q88, PNG otherwise.
- **Output:** `build/print-assets/`.
- **Image paths:** `print-safe-images.lua` points interior images there.

History (`docs/LULU.md`): Lulu once flagged *transparency* (the logomark is ink on transparency) and *images over 600 PPI*, because a 1024px logo at 1.7in is about 602 PPI. "a current `press verify-print` interior triggers **neither** warning". A custom `tex/title-page-print.tex` should point its logo at `build/print-assets/`.


### 8.5 `press illustrate <name> [--style <id>] [--subject <text>] [--from <image>] [--print] | --list`

The grammar is at `illustrate.py:144-177`. The spec is `("gpt-image-2", "1024x1024", "high", False)`, so the result is always square.

```text
  botanical-plate        A precise natural-history engraving of a specimen.
  engraved-map           An antique cartographic engraving; give it a real map to redraw.
  figure-from-photo      Redraws a photograph you supply into a wood engraving. (needs --from)
  line-diagram           A spare technical diagram; clear over pretty.
  ornament               A small engraved vignette, rule, or device.
  technical-cutaway      An engraving-style cutaway showing internal structure.
  wood-engraving         The house interior plate: bold engraved linework, one ink.
```

**Subject.** Without `--subject`, the press finds the manuscript figure whose image file stem equals `<name>` and uses the `<!-- art: ... -->` comment that follows it. It refuses in three cases:

- the figure is not declared;
- the figure is a data kind, `.chart` or `.diagram` (`figures.DATA_KINDS`, `figures.py:45`);
- the figure has no `art:` description. The message is "A caption is a label, not art direction (#225)".

Example from `docs/ILLUSTRATIONS.md`:

```markdown
![A compositor at the case](assets/fig/compositor.jpg){.plate style=wood-engraving}
<!-- art: a compositor's left hand holding a brass composing stick, thumb setting
     the measure; type in the case behind; 19th-c workshop, high contrast line,
     no lettering -->
```

**Style.** `--style`, then the figure's `style=` attribute, then `aesthetic.plates.style`, then `wood-engraving`.

**`--from <image>`.** Sent through OpenAI `images/edits`. The `figure-from-photo` style is `source: required`; without `--from` it fails with "the {style_id} style needs source material: --from <image>".

**Template fields.** `{ink}` is `book-colors.ink`, then `web-palette.ink`, then `#1b1b1b`. `{paper}` is `web-palette.paper`, then `#f4f1e6`. Quirk: the house `book-colors.ink` is `171717` with no `#`, so prompts read "in 171717 ink".

**Guardrail**, always appended:

```text
Single ink only, no colour wash. No text, no words, no lettering, no caption, no page border, no watermark, no signature.
```

**Output.** `build/illustrations/<name>.png`, then the hint `press art accept build/illustrations/<name>.png --as plate:<name>`.

A book can add styles in `config/illustration-styles.yaml` (`styles: {id: {name, note, source?, prompt}}`). Templates may use `{subject}`, `{ink}`, and `{paper}`.


### 8.6 `press art accept <file> --as cover|plate:<name>|logomark|portrait`

The source is `art.py:196-285`. Every input is first EXIF-transposed.

| Target | Destination | Treatment |
|---|---|---|
| `cover` | `assets/cover.jpg` | Aspect check against the trim; alpha flattened onto white (never black); JPEG quality 88, optimized |
| `plate:<name>` | `assets/woodcuts/<name>.png` | Alpha PNG master (below); `<name>` must match `[a-z0-9][a-z0-9-]*` |
| `logomark` | `assets/press-logo.png` | Ink on transparency |
| `portrait` | `assets/author.jpg` | Flattened onto white, JPEG q88 |

**Geometry.** The only intake geometry check is the cover's aspect ratio. Height/width must be within `COVER_ASPECT_TOLERANCE = 0.03` (3%) of the trim ratio, or intake fails with "crop the source, do not stretch it". The trim is read from `metadata.trim`, default 6x9 (`art.py:190-193`).

There is no minimum pixel or DPI check at intake. The docstring says the height cap "is enforced at typeset time by the TeX header, not here".

**Plate master** (`_plate_master`, `art.py:136-167`). The plate is "single ink" unless the design profile ink is `color`. In addition, `plates.medium` in the aesthetic must contain both the substrings "single" and "ink" (`art.py:42-50`).

For a single-ink plate:

- A transparent delivery keeps its mask and is greyed. A delivery counts as opaque if its minimum alpha is 250 or more.
- An opaque delivery first passes the flat-ground test (`_require_flat_ground`):
  - The border band is `max(3, min(w,h)//25)` px wide.
  - At least 82% of border pixels must have luminance of 200 or more.
  - The mean drift top/bottom and left/right must be 45 or less.
  - A gradient or textured ground fails with "the luminance key would leave a ghost on the page". The fix offered is a plain near-white ground, or a colour interior that keeps the plate's exact pixels (v3.0.0).
- Then a luminance key is applied, with `_KEY_WHITE = 225` and `_KEY_BLACK = 45`:
  - luminance 225 or more becomes alpha 0;
  - luminance 45 or less becomes alpha 255;
  - values between ramp linearly as `round(255*(225-v)/180)`.
- Why 225: gpt-image lays its ground near `#f1f2f3` (about 241), so a naive `255 - L` would leave a "five-percent box".
- The master's RGB is (0,0,0) everywhere; all tone lives in alpha.

A colour plate keeps any delivered alpha. An opaque colour plate is flattened onto white with its colours unchanged. The docstring names a matting model (BiRefNet/rembg) as future work.

**Logomark** (`art.py:170-187`). An opaque delivery is hard-thresholded: luminance below 96 becomes ink, painted `(23,23,23)` on transparency. It prints "logomark arrived opaque; ink extracted to transparency".

**Acceptance record.** `art/commissions.md` gets a `## Acceptance record` section with one line per target, replacing any earlier line for that target:

```text
- Accepted {date}: `{target}` <- {source.name}, {w}x{h}px, placed at {dest}
```

**One master, every surface** (`docs/ILLUSTRATIONS.md`). The print interior flattens the master onto white at build time (the `print_safe` pass). A cloth cover would flatten it onto the field colour, which is how the imprint logo already works. The reader edition serves the transparent PNG, so a plate reads on light or dark pages. CLAUDE.md scar: "Do not reintroduce a baked-white JPEG master."


### 8.7 `press art enhance [file] [--colors N] [--max-edge PX]`

The source is `art.py:304-374` and `art_enhance.py`. Without a file argument, it finishes every `assets/woodcuts/*.jpg|*.png`. Output always goes to `<stem>.png`.

1. **Upscale** with Real-ESRGAN. The press searches for `realesrgan-ncnn-vulkan` or `upscayl-bin` on PATH, then `/usr/local/bin/realesrgan-ncnn-vulkan`, then `/Applications/Upscayl.app/Contents/Resources/bin/upscayl-bin`.
   - Models are searched in `/usr/local/share/realesrgan/models`, then the Upscayl models directory, then `../models` next to the binary.
   - The invocation is `<bin> -i src -o dst -n model -m models_dir -s 4`, with a 600 s timeout.
   - The model is chosen from the medium in `plates.medium`, by substring:
     - `engrav`, `woodcut`, `wood engraving`, `line`: remacri-4x, 16 colours
     - `pen`, `etch`: remacri-4x, 24 colours
     - `wash`, `watercolour`, `watercolor`: ultrasharp-4x, 64 colours
     - default: remacri-4x, 16 colours
   - Model fallback order: remacri-4x, ultrasharp-4x, realesrgan-x4plus, upscayl-standard-4x.
   - With no upscaler it prints "no Real-ESRGAN upscaler found ... quantizing and compressing without an AI upscale" and continues.
2. **Resample**, downward only, with Lanczos, to a 2400 px long edge by default. Code comment: "covers a full-page plate on a 6x9 interior at 300 DPI".
3. **Quantize** with median-cut to N colours (greyscale `L` unless the profile is colour). Alpha is preserved and reattached.
4. **Compress** with PIL `optimize=True`, then `oxipng -o 4` or `pngcrush -ow`, whichever is found first.

The toolchain image bakes `realesrgan-ncnn-vulkan` and the remacri and ultrasharp models into `/usr/local/bin` and `/usr/local/share/realesrgan/models`. The download is pinned by sha256 in the `Dockerfile`. This works on amd64 only, using CPU inference against a software Vulkan device. The arm64 image has no upstream binary and resamples instead.

CLAUDE.md scar: "Truecolor PNG barely compresses engraving grain, which is why plates were once baked JPEGs; `press art enhance` quantizes the grain to a few grays so a plate ships as a small lossless PNG."


### 9.5 What is not generated

- **Glossary.** Authored as a definition-list appendix. It is neither generated nor checked: "a feature to ask for".
- **"Also by" / further reading.** Authored. The cross-book catalogue is planned for Later — Catalog.
- **About the author.** Authored, `press add appendix about-the-author` → `z-about-the-author.md`.
- **Half-title.** BOOK-PARTS lists a "Half-title & title page". The generator code has a cover plate and a title page but no distinct half-title page, so writers should not promise a separate half-title leaf.

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

# Supplement added by the managing editor (2026-11-11): tested rulings

## S1. Where the `art:` comment goes

Tested on pandoc 3.9.0.2 and the toolchain's 3.1.3: an image followed on the very next line by a comment is a `Para`, not a `Figure` (no caption, no number, no list entry, no cross-reference target); with ONE BLANK LINE between them the figure is intact. `figures.py` accepts both forms and `press figures` reports the directive either way, so nothing warns the author. The book states the rule as: image line, blank line, comment. The fact base's own compositor example (4.2, 8.5) shows the broken form; the book does not reproduce it. Press issue #280.

## S2. A wrap and its directive

Tested with the press PDF defaults: a comment between a `wrap-inner`/`wrap-outer` figure and the paragraph after it defeats the filter's fusion of the wrap onto that paragraph (`\end{wrapfigure}%` followed by text becomes a paragraph break), so the text no longer runs around the figure as designed. Therefore a wrapped figure carries no `art:` comment; the chapter says so and says `press illustrate <name> --subject "..."` is the way to commission one. Press issue #280.

## S3. Print-safe and figure directories

The print pass copies only `assets/*.jpg`, `assets/woodcuts/*`, and the logo (confirmed by a build: a figure under `assets/figures/` failed `press print` with "file not found"; press issue #272). The chapter states this as what the pass copies today and advises keeping every interior image under `assets/woodcuts/`.
