## 16. Internals and architecture

### 16.1 Module map (`src/press/`, ~19,750 lines of Python)

| Area | Modules |
|---|---|
| Entry and CLI | `__main__.py` (route table, console, help), `catalog.py` (the one typed command catalog; CLI usage, help, and desk picker all render from it; difflib "did you mean"), `brand.py` |
| Book model | `booklib.py` (root, metadata, chapter discovery, release witnesses), `bookmodel.py` (frozen typed `Book`, every problem collected), `yamlio.py` ("the single YAML door", ruamel at YAML 1.2) |
| Graph | `registry.py` (`ARTIFACTS`, `build_order`, `download_names`) |
| Build | `build.py`, `dropcaps.py`, `figures.py`, `profiles.py`, `provider_specs.py`, `aesthetic.py`, `print_safe.py`, `webmeta.py`, `reader_meta.py`, `package_source.py`, `wordcount.py` |
| Generators | `gen_front_matter.py`, `gen_index.py`, `gen_authorities.py`, `gen_coverwrap.py`, `barcode.py` |
| Editorial law | `check_source.py`, `check_the_checkers.py`, `style_audit.py`, `jargon_lint.py` |
| Verifiers | `verify_pdf.py`, `verify_formats.py`, `verify_pages.py`, `verify_archives.py`, `verify_coverwrap.py` |
| Config | `config_cli.py`, `config_schema.py`, `config_store.py` |
| Print and commerce | `publish.py`, `commerce.py`, `edition.py`, `qualification.py`, `profile_lifecycle.py`, `providers/` (contract, fake, lulu, transport) |
| Registrations | `registrations.py`, `onix.py`, `pcn.py`, `idlookup.py` |
| Art | `cover.py`, `illustrate.py`, `art.py`, `art_commission.py`, `art_enhance.py` |
| Operator and instruments | `operator.py`, `instruments.py` |
| Desk | `desk/`, `desk_model.py`, `artifact_status.py`, `process_control.py`, `events.py` |
| Scaffolding | `scaffold.py`, `add.py`, `migrate.py`, `extensions.py` |
| Trust | `selftest.py`, `selftest_book.py`, `selftest_release.py`, `invariants.py`, `receipts.py`, `scenarios.py`, `mutation.py`, `quality_checks.py`, `results.py`, `doctor.py` |
| Boundary | `adapters/`: "the one approved home for direct `subprocess`/`os.environ`/`urllib` calls"; http with a 30s timeout and byte cap, retry, import_guard, streaming |

### 16.2 Data flow, in prose (for a diagram)

```text
config/*.yaml ─► bookmodel (typed, validated) ─┐
book/chapters + book/appendices ─► booklib.chapter_files ─┼─► build.book_inputs ─► [gen_index → build/generated/] [gen_authorities → dist/<slug>-sources.md]
profiles + aesthetic + front-matter ─► build/*.tex fragments ┘
        │
        ▼
render_defaults(@press/ @book/ ?optional) ─► build/defaults/<fmt>.yaml
        │
        ▼
pandoc (+ Lua filters) ─► latexmk -lualatex (pdf/print) | epub | html | chunkedhtml | plain | docx
        │
        ▼
dist/<slug>.* ─► verify_pdf / verify_formats(+epubcheck) / verify_archives ─► pages assembly ─► verify_pages
        │
        ▼ (CI)
upload artifacts ─► (tag) GitHub Release with CHANGELOG notes ─► (main) GitHub Pages
```

Print branch: `print_safe` → print interior → `verify_pdf --profile print` → `gen_coverwrap` (latexmk TikZ) → `verify_coverwrap` → `publish` checklist → edition manifest and qualification → commerce gate.

### 16.3 Invariants

- **The ledger.** `.celebrimbor/invariants.yaml`, rendered to `docs/INVARIANTS.md` by `press selftest --write-docs`. ARCHITECTURE.md still names the old path `quality/invariants.yaml`, which no longer exists.
- **Counts.** 85 invariants, 13 of them critical.
- **The critical 13:** INV-archive-source-policy, INV-config-slug, INV-edition-manifest, INV-editorial-checkers, INV-extension-conformance, INV-extension-seal, INV-format-witness, INV-graph-no-stale, INV-migration-safe, INV-pdf-detector, INV-provider-contract, INV-release-receipt-chain, INV-release-tag-grammar.
- **Entry shape:** a statement, "enforced by `module:function`", "proven by" a test or fixture, and an honest "does not cover".

  "An honest limitation column is the point: a guarantee whose edges are unstated is a guarantee waiting to be overtrusted."

  Examples:
  - `INV-editorial-battery`, which does not cover: "The glyph law flags legitimate Greek or math; short title-case headings slip."
  - `INV-graph-no-stale`, which does not cover: "CLI-path only; importing a verifier module directly skips the rebuild."
  - `INV-pdf-detector`, which does not cover: "Two synthetic extremes; a faint hairline can still read as blank."
  - `INV-archive-source-policy`, which does not cover: "a novel secret filename is not caught."
  - `INV-art-key-never-stored`: "The image-model key is read from the environment on demand and its absence is refused, never stored."

### 16.4 `press selftest`

"The press checking itself." It runs 29 ordered checks, and pytest parametrizes over the same list. The success line:

```text
Selftest passed: 29 checks, arithmetic agrees with the canonical examples, usage and README name every target
```

The checks, in order:

1. arithmetic (ISBN, EAN-13, ISSN)
2. slug_invariant
3. jargon_parity
4. source_policy
5. pages_verifier
6. scaffold_neutrality
7. book_model
8. registry
9. format_witnesses
10. editions_agree
11. editorial_checkers
12. site_identity
13. authorities_ledger
14. honest_refusals
15. release_grammar
16. receipt_chain
17. edition_manifest
18. provider_qualification
19. profile_seals
20. commerce_config
21. commerce_release_gate
22. provider_contract
23. coverwrap_detectors
24. aesthetic_schema
25. contract_mirror (`AGENTS.md` equals `CLAUDE.md` below the heading)
26. migration
27. extension_conformance
28. command_catalog
29. docs (REFERENCE, INVARIANTS, and PROVIDER-QUALIFICATION must match their sources)

`press selftest --write-docs` regenerates `docs/REFERENCE.md`, `docs/INVARIANTS.md`, `docs/PROVIDER-QUALIFICATION.md`, and the packaged provider record. Repo-file checks are skipped from an installed wheel.

### 16.5 The celebrimbor gate (briefly)

- **What it is.** celebrimbor is a separate quality framework (`clintecker/celebrimbor@v0.12.0`). It is a dev and CI dependency only, needs Python 3.11 or later, and is never a book runtime dependency.
- **What it holds.** `src/press/quality_checks.py` registers 29 press domain checks with it. It also holds:
  - the per-module branch-coverage floor ratchet;
  - the mutation-score ratchet over pure modules (`barcode`, `artifact_status`, `dropcaps`, `figures`; `src/press/mutation.py`);
  - the producer ledger (`.celebrimbor/producers.yaml`, whose pending entries carry `review_by` dates);
  - `surfaces.yaml`;
  - `known-bad.expected.yaml`;
  - the Lua coverage baselines.
- **Where it runs.** `scripts/verify.sh` runs `celebrimbor gate`.
- **The ratchet law.** "Never pass --update-baselines locally". "Do not run `scripts/coverage_ratchet.py --update`" (CONTRIBUTING).
- **Its stated philosophy** (CONTRIBUTING): "Coverage measures that a line *ran*, not that its output was *right*... a title-page generator shipped a dropped and a clipped cover at 11.5% coverage: the lines ran, the artifact was never inspected." Hence "A producer is only proven by a verifier that rejects a broken artifact."

### 16.6 Events and receipts

- **`events.py`** defines a versioned child-event protocol: `PROTOCOL_VERSION = 1`, sentinel `"\x1e\x1epress-event\x1e"`, and the types stage_start, stage_end, diagnostic, artifact, complete. Nothing emits it at runtime; the desk parses log text instead.
- **`receipts.py`** handles trust receipts (§12.5). It also yields the edition manifest's receipt digests and the release receipt.
- **`artifact_status.py`** computes the digest-based desk states.

### 16.7 Other internal facts worth a sidebar

- **Fixed timestamps.** `SOURCE_DATE_EPOCH` defaults to 1784160000 (2026-07-16), and the source zip uses a fixed timestamp of 2026-07-16 12:00. Both aim at reproducible artifacts.
- **Config writes are atomic and comment-preserving.** A temp file `.<name>.press-tmp` is fsynced, then `os.replace`d. The ruamel round-trip uses width 4096 and indents mapping=2, sequence=4, offset=2. Ambiguous strings ("3", "true", dates) are double-quoted.
- **One secret regex.** `press config` refuses any value matching `(?i)(api[_-]?key|secret|token|password|bearer|-----BEGIN|sk-[a-z0-9]{16,}|gh[pousr]_[a-z0-9]{16,})`. A dedication containing "secret" is therefore refused.
- **Docs drift is impossible by construction** for REFERENCE, INVARIANTS, and PROVIDER-QUALIFICATION: the selftest fails on any drift. The docs-law note says docs land in the same commit as surface changes.
- **AGENTS.md mirrors CLAUDE.md** (selftest `contract_mirror`).

---


## 15. Extensions (`docs/EXTENSION-CONTRACT.md`, `src/press/extensions.py`)

**"Press extends by declaration, not by code."** "The press has **no plugin loader, no entry-point group, and no import-time discovery**, and that absence is the contract, not a missing feature." Behaviour "cannot come from the accident of which package imported first".

**Five extensible surfaces**, each a named data registry selected by id:

| Surface | Registry | Selected by |
| --- | --- | --- |
| `design-profile` | `data/profiles/<id>.yaml` | `print.profile` |
| `provider-spec` | `data/provider-specs/<id>.yaml` | `print.provider` |
| `artifact` | `registry.ARTIFACTS` | build target / download policy |
| `skill` | `data/skills/<id>/` | `press skills`, workflows |
| `workflow` | `data/workflows/<id>.js` | `press workflows`, the Workflow tool |

**Sealed capabilities.** An extension may depend on these but never claim them: `core-verification`, `path-containment`, `artifact-graph`, `config-validation`, `release-gate`.

**The manifest** (`src/press/data/extensions/reference.yaml`):

```yaml
name: acme-quarto           # the extension's own id (must not collide)
kind: design-profile        # which sealed-list surface it registers into
contract-major: 2           # the extension contract it was written against
provides:                   # the exact names it claims in that registry
  - acme-quarto
requires:                   # names it depends on: core or self-provided
  - pdf
invariants:                 # the guarantees it takes on
  - INV-acme-quarto-geometry
proofs:                     # how each is proven (may not be empty if any)
  - fixture:acme-quarto.md
capabilities:               # what it asserts — never a sealed capability
  - interior-geometry
publication: internal       # published | internal, for artifacts it adds
```

**Lifecycle:** discover (sorted, never import order) → parse (`load_manifest`) → check conformance → register → build and verify under the same laws.

**Refusals,** each a located reason: Collision, Unsupported contract, Unknown dependency, Sealed claim, Unproven obligation, Malformed.

**Hostile fixtures** that selftest refuses (`check_extension_conformance`):
- `hostile/collision.yaml` claims `pdf`;
- `version.yaml` targets major 99;
- `sealed.yaml` claims `core-verification`;
- `unproven.yaml` has `proofs: []`;
- `malformed.yaml` has `contract-major: "two"`.

**Invariants:** `INV-extension-conformance` and `INV-extension-seal`, both critical.

**Status.** `SUPPORTED_CONTRACT_MAJORS = (2,)`; no runtime loader exists yet. "A future runtime that *loads* extensions will reuse exactly this gate." The docs describe a `contract-major: 3` with book-declared `config/extensions.yaml` (`docs/THIRD-PARTY-EXTENSIONS-PLAN.md`, #173, in the Icebox). That is **not implemented**.

What a book can extend today without the manifest machinery:
- `config/cover-styles.yaml`
- `config/illustration-styles.yaml`
- `config/aesthetic.yaml`
- `assets/web/*.css`
- `tex/title-page*.tex`
- `tests/known-bad/`

---


### 12.7 The press's own CI (for the internals chapter)

| Workflow | Name | What it does |
|---|---|---|
| `selftest.yml` | "Press selftest" | Job `quality`: lint, celebrimbor gate, Lua coverage, site build, receipt. Job `selftest`: Ubuntu × Python 3.10–3.14 plus macos-15/3.12, running `press selftest`, pytest, and `press new matrix-proof` then `press check`. Job `desk`: a bare wheel must refuse the desk; the tui wheel runs it headless. |
| `integration.yml` | "Press integration gate" | Job `consumer`: `scripts/gauntlet-steps.sh` in the pinned container. "build the wheel, scaffold a stranger's book, run the whole `press all`, and prove tampering turns the verifier red". |
| `toolchain.yml` | | Builds and publishes the multi-arch image. |
| `docs-site.yml` | | Builds the example PDFs in the pinned image, then `scripts/build_site.py` with `PRESS_REQUIRE_BROWSER_CHECK=1` (headless Chrome layout check), then deploys <https://clintecker.github.io/press/>. |
| `codeql.yml` | | Static analysis. |
| `dependency-review.yml` | | Dependency review on PRs. |
| `ledger-review.yml` | | Monday job: opens an issue for pending-producer entries within 30 days of `review_by`. |
| `roadmap.yml` | | Projects `roadmap/milestones.json` into ROADMAP.md and GitHub milestones. |
| `security-controls.yml` | | Weekly drift check of the platform toggles, using `SECURITY_AUDIT_TOKEN`. |
| `repo-metadata.yml` | | |

---


### 17.4 Exit codes

| Situation | Exit |
|---|---|
| Success | 0 |
| A check or verify failure (`SystemExit("msg")`) | 1 |
| Bare `press` with no command (prints usage) | 2 |
| Unknown target (prints `unknown target: X` plus a suggestion) | 2 |
| A failing external tool | that tool's own exit code (`CalledProcessError` unwrapped, `INV-cli-exit-code`; selftest proves 43 → 43) |
| `press config` | 0 ok, 2 usage, 3 unknown or non-writable field, 4 refused or validation failure, 5 key missing on read |
| `press add` | 1 refuses to overwrite, 2 usage |
| `press doctor` | 0 ready, 1 not ready |
| `press desk` without `[tui]` or a TTY | 2 |
| The action's command-grammar refusal | 2 |
| `press lookup` | only `found` exits 0 |
| `press publish` | 1 if anything is unverified (unless `--report-only`) |
| `jargon_lint` | 1 on findings at or above `--fail-on`; 2 on a malformed watchlist |


### 17.5 Environment variables

| Variable | Effect |
|---|---|
| `BOOK_ROOT` | The book root (default: the current directory). Also set for builds. |
| `PRESS_RELEASE` | Release mode: refuses vacuous witnesses (at least 2 sentinels, at least 24 pages); makes the commerce gate fail closed. CI sets it on `refs/tags/v*`. |
| `PRESS_TOOLCHAIN` | Set in the toolchain image; makes a missing epubcheck fatal. |
| `OPENAI_API_KEY` / `GEMINI_API_KEY` | Image-model keys for art; read on demand, never stored. |
| `SOURCE_DATE_EPOCH` | Default 1784160000 for reproducible builds. |
| `BOOK_PUBLISHER` | Set by press for TeX's fallback title. |
| `NO_COLOR` / `FORCE_COLOR` | Terminal colour. |
| `GITHUB_SHA` | Used by receipts in CI. |
| `PRESS_REQUIRE_LUA` | (dev/CI) Forbids skipping the Lua filter tests. |
| `PRESS_LUA_COV_DIR` | (dev) Lua coverage measurement directory. |
| `PRESS_REQUIRE_BROWSER_CHECK` | (docs-site CI) Requires the headless-Chrome layout check. |
| `SECURITY_AUDIT_TOKEN` | (press repo CI secret) The security-controls drift check. |


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

# Supplement added by the managing editor (2026-11-11): contributing, from the press checkout

## S1. `CONTRIBUTING.md`, opening and the verify ladder (verbatim)

```text
# Contributing

The press accepts contributions that follow its laws (see
[the architecture guide](https://github.com/clintecker/press/blob/main/docs/ARCHITECTURE.md):
facts once, generators over checkers over conventions, artifacts verified
as objects, scars become law).

- Run `press doctor`, then `press selftest`, before and after your
  change; both must be green.
- Install the local gates once: `pip install -e '.[dev]'` then
  `pre-commit install`. Every commit then lints every checked-in
  format: ruff (with a cyclomatic-complexity ceiling of 15 for new
  code), mypy, shellcheck, yamllint, pymarkdown, TOML/JSON validity,
  and the selftest. CI runs the identical battery via
  `pre-commit run --all-files`, so the hook only saves you the round
  trip. The complexity ceiling is enforced with no current exceptions;
  do not introduce a `# noqa: C901`, decompose instead.
- Prove changes against a real book: scaffold one (`press new`) or use
  your own, and run `press all`. A green `pip install` is not a
  working pipeline.
- New CLI targets, artifacts, or config keys must land with their
  documentation in the same commit; the selftest enforces the parts it
  can reach mechanically.
- Design changes to rendered output of valid books are breaking
  changes and wait for a new major; say so in your PR.
- CI runs the selftest and the integration gate (wheel build, clean
  scaffold, full gauntlet, tamper test) on every PR. Toolchain PRs
  additionally build and smoke the image without publishing.

## One command to verify

From a clean checkout with `pip install -e '.[dev]'`, run the whole local
proof, fast layers first:

```sh
scripts/verify.sh          # lint + type + selftest + pytest, then the
                           # coverage and mutation ratchets and the site build
scripts/verify.sh --quick  # stop after the fast lint/type/test layer
scripts/verify.sh --full   # also run CI's container gauntlet locally (Docker)
```

CI calls these same tools. `--full` additionally runs the integration gauntlet
in the pinned toolchain image (`scripts/gauntlet.sh`) — build the wheel,
scaffold a stranger's book, run the whole `press all`, and prove tampering
turns the verifier red — so the container tier where rendered-artifact bugs
surface is proven before you push, not on the CI round-trip. It runs natively
on Apple Silicon since the toolchain image went multi-arch (needs Docker).
Only the live second-party proofs (a fork-PR from another account, a private
book in another org) stay CI/human-only. Do not run
`scripts/coverage_ratchet.py --update`: it re-measures on your machine and
can push the committed baselines above the floor CI enforces.

The Lua filters have their own floor, `.celebrimbor/baselines/lua-coverage.yaml`.
`scripts/verify.sh` checks it when pandoc is installed (a new filter with no
floor fails the check until `update` gives it one); to see the numbers and
the uncovered lines, run the Lua tests with `PRESS_LUA_COV_DIR` set to an empty
directory, then `python3 scripts/lua_coverage_ratchet.py report --cov-dir` that
directory. Never `update` it from a macOS measurement either; feed it CI's report
with `update --from-report`.

```

## S2. `CONTRIBUTING.md`, "Filing and proposing" (verbatim)

```text
## Filing and proposing

Open issues through the [issue forms](https://github.com/clintecker/press/issues/new/choose)
(defect, proposal, documentation); a defect asks for `press doctor`,
`press selftest`, the version, and a minimal reproduction. Report security
vulnerabilities privately per
[the security policy](https://github.com/clintecker/press/blob/main/SECURITY.md),
never as a public issue. Pull requests follow the template: a test that
fails before and passes after, regenerated projections, and the
compatibility impact.

This project has one maintainer; how decisions, releases, and conduct are
handled is in
[the governance doc](https://github.com/clintecker/press/blob/main/GOVERNANCE.md),
and participation is under the
```

## S3. Where the Lua tests live

Under `tests/` in the press checkout: `tests/lua/` holds `test_press_util.lua` and `coverage-hook.lua`; `tests/lua_coverage.py` is the harness; `tests/test_lua_compiles.py`, `tests/test_lua_coverage_harness.py`, `tests/test_lua_coverage_ratchet.py`, and `tests/test_press_util_lua.py` are the pytest entry points. They run inside `python3 -m pytest`; `PRESS_REQUIRE_LUA=1` makes a missing pandoc a failure instead of a skip (CI sets it); `PRESS_LUA_COV_DIR` collects line coverage for `scripts/lua_coverage_ratchet.py report --cov-dir <dir>`.

## S4. `CLAUDE.md`, "Verifying changes here" (verbatim)

```text
## Verifying changes here

The press has no book of its own, so prove changes against a real one:
clone a consuming book, `pip install -e` this checkout into it, run
`press all`, and confirm every verifier passes before tagging. A green
`pip install` is not a working pipeline.

To look at output while tuning a template, filter, or aesthetic,
`scripts/dev-render.sh` builds one book in the pinned toolchain image and
drops the artifacts (and, with `--preview`, JPEG page previews) on the host:
it mounts this checkout read-only and runs `python -m press` from `src/`, so
edits take effect with no reinstall, and it reads the toolchain image from
`build.yml` so it cannot drift from CI. Defaults to the Alice example; pass
`--book DIR` for another. It is the edit–render–look loop, not the proof —
`scripts/verify.sh --full` is still the gate before tagging.
```

Ruling: an outside contributor submits a pull request through the template S2 names (a test that fails before and passes after, regenerated projections, the compatibility impact); "main takes direct pushes" describes the maintainer, and the chapter says both.
