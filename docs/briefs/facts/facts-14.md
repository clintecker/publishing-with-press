## 12. CI, the toolchain, the release contract, migration

### 12.1 A book's CI

The scaffolded `.github/workflows/book.yml` is the entire file, verbatim in §3.1. Its job is `uses: clintecker/press/.github/workflows/build.yml@v3`. The book's `CLAUDE.md` says it "is the whole file and should stay that way".

It triggers on:
- a push to any branch;
- `v*` tags;
- pull requests;
- `workflow_dispatch`.

It holds these permissions: `contents: write, packages: read, pages: write, id-token: write`.

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

### 12.3 The reusable workflow (`.github/workflows/build.yml`)

The trigger is `on: workflow_call: {}`. It declares **no inputs and no secrets**, so a book always runs `press all`. Privilege is granted per job: "building a book executes book content, so the build job holds read permissions only; the release job alone can write, and only on tags."

**Job `build`**
- `ubuntu-24.04`, with `contents: read, packages: read`.
- The container image is pinned by digest:

  ```yaml
  image: ghcr.io/clintecker/press-toolchain:sha-0a3a99d676a11a7279085d818805c2473307a026@sha256:0d784ac08282a94e64b444efd86ee3bf9eb45262a9e6e758fc656a2363b2ca04
  credentials:
    username: ${{ github.actor }}
    password: ${{ secrets.github_token }}
  ```

- Steps:
  1. checkout, pinned by full SHA;
  2. `uses: clintecker/press@v3.0.2`, with `PRESS_RELEASE: ${{ startsWith(github.ref, 'refs/tags/v') && '1' || '' }}`;
  3. "Read book identity", which runs a heredoc `from press import booklib`. The comment explains: "The slug law and normalization live in the press; this step asks the installed press instead of keeping a second copy". This yields the outputs `slug`, `title`, `site_url`;
  4. upload `dist/*` except `dist/site` and `dist/pages` (`if-no-files-found: error`);
  5. upload the Pages artifact, only on a push to the default branch.

**Job `release`** (tags only, `contents: write`)
1. Refuses a commit that is not on the default branch.
2. Extracts the `## [version]` section from the **book's** CHANGELOG. If it is missing: `no CHANGELOG section for $version; roll [Unreleased] before tagging`.
3. Appends "## Public downloads" with direct links to `${SITE_URL}/downloads/<name>`.
4. Runs `gh release create` with every file in `dist/`, titled `"$TITLE $GITHUB_REF_NAME"`.

**Job `deploy-pages`** runs only on a default-branch push and needs the `github-pages` environment.

**Action pinning.** Every action is pinned to a 40-hex commit SHA. `tests/test_ci_posture.py::test_every_action_is_pinned_by_full_commit_sha` enforces this, because GitHub has no ruleset for it.

### 12.4 The toolchain image

- **Name and basis.** `ghcr.io/clintecker/press-toolchain`, built from `Dockerfile` (`FROM ubuntu:24.04`, `ENV PRESS_TOOLCHAIN=1`).
- **apt packages:** make, git, gh, pandoc, python3, python3-pip, poppler-utils, epubcheck, texlive-luatex, texlive-latex-extra (for lettrine), texlive-fonts-extra (for yfonts/yinit), fonts-linuxlibertine, latexmk.
- **epubcheck wrapper.** `printf '#!/bin/sh\nexec java -jar /usr/share/java/epubcheck.jar "$@"\n' > /usr/local/bin/epubcheck`.
- **Image processing.** Real-ESRGAN plus the models, amd64 only. `mesa-vulkan-drivers` provides a software Vulkan.
- **Lua tooling.** stylua v2.5.2, and selene 0.31.0 on amd64.
- **Multi-arch.** The image is published for amd64 (`ubuntu-24.04`) and arm64 (`ubuntu-24.04-arm`) by `.github/workflows/toolchain.yml`, and each is smoked before push. The tags are `:latest` and `:sha-<SHA>`.
- **Public since 2026-07-20 (#161).** "a book under any account pulls it with no package grant and no configured secret". In CI the pull is authenticated with the workflow's own `GITHUB_TOKEN`, "which works for a public image, including on fork and Dependabot pull requests". Locally it pulls anonymously.

### 12.5 Tags, `vN` semantics, the release contract

From `CLAUDE.md`, "The contract":

> Books pin a tag (`@v1`). Tags follow the GitHub Actions convention: `vN` is a floating major that moves to the latest compatible `vN.x.y`; the three-part tags are immutable, and immutability is enforced, not promised: a three-part tag's build.yml must pin the press action to that exact tag and the toolchain image to an immutable `@sha256:` digest that resolves (the release-contract workflow turns red otherwise; a `sha-` tag alone is mutable and is refused), so a pinned book resolves the same pipeline, action, and toolchain bytes forever, while `vN` floats normally.

**`.github/workflows/release-contract.yml`** runs on tags matching `v[0-9]+.[0-9]+.[0-9]+`. It works in five steps:

1. **Pin check.** build.yml must contain `uses: clintecker/press@${tag}`, and its image must match `press-toolchain:sha-…@sha256:<64 hex>`.
2. **Image resolves.** `docker manifest inspect` must succeed on that image.
3. **Check runs pass.** It waits up to 60 × 30 seconds for the `quality`, `consumer`, and `desk` check runs on that SHA to succeed. The newest run of each name decides.
4. **Receipt chain.** It builds the wheel, downloads the `receipt-quality` and `receipt-integration` artifacts, and runs `python3 -m press.receipts assemble`.
5. **Upload.** It uploads `release-receipt`.

**Platform rulesets** (`SECURITY.md`):
- `main` cannot be force-pushed or deleted.
- Three-part tags `v*.*.*` cannot be moved or deleted.
- The floating major moves only through `scripts/release.sh`.
- `main` takes direct pushes by design (#153). The checks are enforced at the release boundary.

**Tag grammar.** It is proven by selftest. Good: `v1.0.0`, `v0.0.1`, `v10.20.30`. Bad: `v1.0`, `v1.0.0.0`, `v1.0.0-rc1`, `v01.0.0`, `1.0.0`, `"v1.0.0 "`.

**Releasing (`scripts/release.sh vN.x.y`).** The script is "the one release path and a resumable state machine": "rerunning after any failure is the recovery procedure". Before running it, roll the CHANGELOG's `[Unreleased]` section into a version section.

| Step | What it does |
|---|---|
| Preflight | Clean tree. A CHANGELOG section exists. A remote tag that already exists is resumed only if its build.yml pins itself. |
| 1. Release commit | Waits for the `consumer` (integration) check on HEAD. Rewrites `uses: clintecker/press@vX` in build.yml and `version = "..."` in pyproject. The rewrite is anchored with `count=1`, because an earlier version once rewrote mypy's `python_version`. Runs the selftest, commits "Release vX", pushes main. |
| 2. Immutable tag | Push the three-part tag. |
| 3. Release contract | Wait for the `contract` check. On failure the major has **not** moved. |
| 4. Float the major | `git push -f origin vN`. |
| 5. GitHub Release | Notes come from the CHANGELOG; the title is `press vX`. |

`--check-tag vN.x.y` validates the tag without touching the network. The script does not repin the toolchain digest; that is a separate change to build.yml. For a new major, also move the requirements pin in the template.

**Trust receipts** (`src/press/receipts.py`). There are 12 layers: collection, unit, property, component, damage, graph, scenario, integration, distribution, container, boundary, release. They are grouped into the release tiers quality, integration, and release.

Verification requires a complete chain: "every layer present, contiguous, and linked to its predecessor — so a partial chain standing in for the missing layers cannot pass". The terminal release receipt names the built wheel's digest and the pinned toolchain digest. The CLI is `python3 -m press.receipts emit|assemble|verify|verify-release`.

### 12.6 Migration between majors (`press migrate`)

Source: `src/press/migrate.py`, `docs/MIGRATION.md`.

```bash
press migrate            # or: press migrate plan — dry run, writes nothing
press migrate apply      # repin, after writing an exact backup
press migrate status     # what you're pinned to, and any recorded migration
press migrate rollback   # restore the exact prior pin
```

**What it rewrites.** Only the pin, and only in two places: `requirements.txt` and `.github/workflows/*.yml|*.yaml`. The pin regex is `(clintecker/press(?:/[\w./-]*?)?@v)(\d+)(\.\d+\.\d+)?`.

**What it refuses.**
- A pin found anywhere else is refused, not rewritten.
- A book split across two majors is refused ("reconcile them before migrating").

**Pin handling.**
- An immutable pin (`@v1.20.0`) is floated to the new major (`@v2`).
- The target is always the current major + 1.

**What it reports.** The plan names any overrides the profile does not govern (`tex/title-page.tex`, `assets/web/reader.css`, `assets/web/extra.css`, `config/aesthetic.yaml`) so you can re-check them.

**Apply and rollback.**
- `apply` first writes `.press/migration-backup.json` (the full bytes), then rewrites the pins, then writes `.press/migration-receipt.json` (`from_major`, `to_major`, `press_version`, `sites`).
- `rollback` restores the exact bytes and removes both files. With nothing to undo it says: `no migration to roll back (no .press/migration-backup.json)`.

**What each step up changes.**
- **v1 → v2.** "byte-for-byte as it did under v1" if the book keeps the house profile.
- **v2 → v3.** A design major: "a re-proof of your PDF, not a quiet repin". The craft pass moves glyphs and line breaks, and page counts may move.

**Captured on a v3 book.** The plan offers v3 → v4 even though v4 does not exist:

```text
pinned to v3:
  requirements.txt: clintecker/press@v3
  .github/workflows/book.yml: clintecker/press/.github/workflows/build.yml@v3
migrate v3 -> v4

changes:
  requirements.txt: clintecker/press@v3  ->  clintecker/press@v4
  .github/workflows/book.yml: clintecker/press/.github/workflows/build.yml@v3  ->  clintecker/press/.github/workflows/build.yml@v4

before you apply:
  - design: see docs/MIGRATION.md for what v4 changes relative to v3; nothing here is rewritten but the pin.
  - the manuscript, config, and accepted art are not touched.

nothing is written until you run `press migrate apply`.
```

**Invariants.** `INV-migration-safe` (critical) and `INV-migration-preview`. Both are proven by selftest `check_migration` with a real plan → apply → rollback round-trip on a scaffolded book.

"Old pins keep working": a book that never repins stays on its major forever.

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


### 16.6 Events and receipts

- **`events.py`** defines a versioned child-event protocol: `PROTOCOL_VERSION = 1`, sentinel `"\x1e\x1epress-event\x1e"`, and the types stage_start, stage_end, diagnostic, artifact, complete. Nothing emits it at runtime; the desk parses log text instead.
- **`receipts.py`** handles trust receipts (§12.5). It also yields the edition manifest's receipt digests and the release receipt.
- **`artifact_status.py`** computes the digest-based desk states.


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