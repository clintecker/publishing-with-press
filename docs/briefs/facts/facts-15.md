## 13. The operator desk (`press desk`)

**Install and launch.** `pip install 'press[tui]'` (Textual 8.x), then run `press desk` inside a book.
- Without the extra it prints `press desk needs the optional interface: pip install 'press[tui]'` and exits 2.
- With no TTY it points you to the CLI. "It never draws into a pipe."
- The code lives in `src/press/desk/` (`app.py`, `wizard.py`, `__init__.py`), with `src/press/desk_model.py` as the read model.

**The DESK home screen** (the read model, rendered) shows:
- the identity: title, authors, trim (`"{w:g} x {h:g} in"`), slug;
- an artifact table (artifact, state, published), one row per registry artifact whose condition holds;
- a toolchain line, "toolchain ready: this machine can build every artifact" or `not ready: … (press doctor names each cost)`;
- a doctor table with one row per capability.

**Artifact evidence glyphs** (`docs/DESK.md`):

| glyph | state | meaning |
|---|---|---|
| `-` | not built | the artifact's output does not exist |
| `o` | present, unverified | it exists, but no evidence records a verified digest |
| `*` | verified | its current digest matches the digest that was verified |
| `!` | changed since proof | it exists but its bytes differ from the verified digest |
| `/` | incomplete | some of a multi-output artifact's outputs are missing |

State is derived from "content digests and recorded verification, never a timestamp". The live desk passes no evidence, so in practice a present artifact shows `o` (§20).

**Doctor glyphs:** `*` ok, `-` absent, `!` missing or broken, `~` warn, `-` unset.

**Keymap:**

| key | action |
|---|---|
| `p` | open the target picker and run a target |
| `w` | open the setup wizard (guided book configuration) |
| `r` | refresh the model (never caches a fact a rebuild would change) |
| `q` | quit |
| `escape` | leave a run, the picker, or the wizard, back to DESK |
| `c` | (RUN view) cancel the child, signalling its process group, not in DESK.md |

**Picker.**
- It is generated from `catalog.COMMANDS` (minus `desk`) and has an argument box.
- A command that needs arguments refuses to start without them.
- `pdf`, `print`, `verify`, `verify-print`, and `all` are greyed when pandoc, lualatex, or latexmk is failing.

**RUN view.**
- It shows `$ press <target args>`, a stage line, the streamed log, and a verdict: `done`, `failed (exit N)`, or `cancelled (exit N)`, plus "; the exit code is the verdict".
- The stage line reads `✓ check · typeset · verify    N steps`. It is parsed from the log's `¶ <phase>` markers and `+ ` lines, "so it can never claim progress the build did not print".
- `process_control.py` runs exactly one child at a time. A second one raises `SingleChildError`. Arguments are passed as argv, never as a shell string.

**Setup wizard (`w`)** (`src/press/desk/wizard.py`).
- **Fields.** One step covering `title`, `subtitle`, `author`, `description`, each pre-filled with its current value and help.
- **Validation.** It goes through `config_cli.preview_edits`, the same boundary `press config` uses.
- **Review.** `Ctrl+R` reviews the exact diff with the validator's verdict. `Ctrl+A` applies a clean preview. Escape discards.
- **Refusals.** A secret-looking value is refused.
- **Finish.** "identity written; next: press check". The wizard never claims the book is ready.
- **Scope.** CLAUDE.md says "every field" is reachable from the wizard. Only these four are (§20).

**Escape hatch.** "Every action it runs is a `press <target>` you can type yourself; the RUN view even prints the exact command it launched."

---


## 14. Agent workflows and skills

### 14.1 How they ship and run

- **Packaging.** Workflows and skills are package data in `src/press/data/workflows/*.js` and `src/press/data/skills/`, "versioned with the press, listed by the CLI, and resolved from the installed package first".
- **Scaffolding.** `press new` copies each workflow into `<book>/.claude/workflows/<name>.js` with the stamp `// scaffolded by press <version>; source of truth: press data/workflows`. This happens only at `press new`; nothing refreshes the copies later.
- **Running.** Use the Claude Code **Workflow tool** by name from inside a book, for example `Workflow({name: "editorial-passes", args: {root: "/abs/book"}})`.
- **Headless drivers** (`src/press/operator.py`), which run through the `claude` CLI:
  - `press improve [--apply] [--rounds N]` runs editorial-passes.
  - `press research [--max-claims-per-file N]` runs authorities-research.
  - `press aesthetic "<brief>" [--overwrite]` runs aesthetic-brief.

  They invoke:

  ```text
  claude -p "Use the Workflow tool with scriptPath <path> and args <json>. When it completes, report its returned result and nothing else." --allowedTools Workflow <bash grant> --permission-mode acceptEdits --output-format text
  ```

  The timeout is 3600 s and the working directory is the book root. The workflow comes from the **installed package**, not the book's pinned copy. The Bash grant is `Bash(press:*)`, `Bash(python3:*)` unless `--apply` is passed, which grants full `Bash`. `press research` adds WebSearch and WebFetch. There is no CLI driver for art-direction.
- **Counsel mode.** `press improve` without `--apply` writes `build/editorial-report.md` and "touches nothing". It fingerprints `book/` and `config/` with SHA-256 before and after. If anything changed it exits with "counsel mode changed the manuscript or config; that violates its contract... report this as a press bug".

**`press workflows` output** (captured in a fresh book; paths abbreviated):

```text
aesthetic-brief
  args: {root: absolute path to the book repository, brief: the author\'s description of the look}. args: {overwrite?: boolean (default false)}
  pinned: …/demo/.claude/workflows/aesthetic-brief.js (matches installed press 3.0.2)
  invoke: Workflow({name: "aesthetic-brief", args: {root: "…/demo"}})
art-direction
  args: {root: absolute path to the book repository}. Run once the manuscript is stable enough to know its imagery. args: {maxPlates?: number (default 8)}
  pinned: …/demo/.claude/workflows/art-direction.js (matches installed press 3.0.2)
  invoke: Workflow({name: "art-direction", args: {root: "…/demo"}})
authorities-research
  args: {root: absolute path to the book repository}. Run against a book repository whose chapters assert facts (historical, technical, numerical) that deserve attribution. args: {maxClaimsPerFile?: number (default 0 = exhaustive; a positive cap samples and the accounting discloses omissions)}
  pinned: …/demo/.claude/workflows/authorities-research.js (matches installed press 3.0.2)
  invoke: Workflow({name: "authorities-research", args: {root: "…/demo"}})
editorial-passes
  args: {root: absolute path to the book repository}. Run against a book repository after composing or substantially revising chapters. args: {rounds?: number (default 2), maxims?: number (default 2), report?: boolean (suggestions written to build/editorial-report.md, nothing applied)}
  pinned: …/demo/.claude/workflows/editorial-passes.js (matches installed press 3.0.2)
  invoke: Workflow({name: "editorial-passes", args: {root: "…/demo"}})
```

When a pinned copy has drifted, the line reads `DIFFERS from installed press X`.

### 14.2 `editorial-passes`

- **Args:** `root` (required), `rounds` (default 2), `maxims` (default 2), `report` (forces one round, applies nothing).
- **Phases:** Scout → Suggest → Synthesize → Law.
  1. **Scout.** Lists the manuscript and finds the four prose skills via `press skills`. It records sentinels, banned labels, and jargon-allow.
  2. **Suggest** (parallel). One agent per file reads all four prose skills "in full" and returns at most 12 suggestions (current, proposed, reason); "an empty list is an acceptable answer". Three whole-book lenses (**cadence**, **repetition**, **arc**) return at most 15 each. From round 2 on, prompts carry a "PREVIOUSLY REJECTED" ledger. A rejection whose quoted text no longer appears "is stale and no longer binds".
  3. **Synthesize.** One synthesizer per file applies the suggestions with judgment: "Preserve the author's voice; do not add length." Rejections are appended to `build/editorial-rejections.md`.
  4. **Law.** Runs `press check` until it is green, "by rewriting sentences (never by substituting other punctuation)", and restores any lost sentinel.
- **Stop condition.** A round with zero suggestions, or fewer than 5 applied, ends the loop; otherwise it stops after `rounds`.
- **The house law string**, verbatim:

  ```text
  HOUSE LAW (mechanical, build-enforced): no em or en dashes anywhere (rewrite the sentence), straight quotes only, sentence-case headings, no manual heading numbers, ASCII plus accented latin only, paragraphs under 190 words, no trailing whitespace.
  ```

- **The named diseases of agent prose**, verbatim (`editorial-passes.js:39-44`):

  ```text
  1. Epigram compulsion: paragraphs that close on coined maxims. QUOTA: at most ${MAXIMS} coined maxims per chapter; every other one demoted to plain statement or cut. A paragraph is allowed to just end.
  2. Uniform rhetorical rhythm: X-not-Y antithesis, chiasmus, triplets recurring every few sentences; every sentence polished to the same sheen. Plain sentences must do plain work.
  3. Self-annotation: clauses that grade the previous clause ("and that is the point", "which is exactly the lesson"). Cut them; trust the material.
  4. Emblematic abstraction where grit belongs: prefer a real duration, count, or cost to a rounded gesture.
  5. Throat-clearing, inflated significance, chatbot signposting, formulaic negative parallelism.
  ```

  The rationale from CLAUDE.md: "because 'apply the skills' alone produces locally-obedient, globally-patterned prose."
- **Returns:** `{rounds, totalApplied, totalRejected, rejectionsFile}`.

### 14.3 `authorities-research`

- **Args:** `root`, `maxClaimsPerFile` (0 means exhaustive), `press` (the command name).
- **Phases:**
  1. **Extract.** A scout states the subject and 2–4 `sourceKinds` ("nothing about any particular trade may be assumed"). Then one agent per file extracts claims as a 5–15-word verbatim `fragment` plus an `assertion`. The author's opinions are excluded.
  2. **Research.** One web-searching agent per claim returns `supported`, `caveat`, or `unsupported`, with authority, URL, and note. "Do not invent citations; an invented authority is worse than none."
  3. **Verify.** An adversarial auditor rules each claim `holds`, `overstates`, or `fails`.
  4. **Ledger.** Writes `config/authorities.yaml`, shortening fragments until they match, and runs `press pdf` until it passes. Unsourced and unresolved claims are reported, not ledgered.
- **Accounting:** `harvested = ledgered + unsourced + unresolved`.

### 14.4 `aesthetic-brief`

- **Args:** `root`, `brief`, `overwrite` (default false).
- **Phases:**
  1. **Scout.** Reads the manuscript gist, the book-aesthetics skill, and the current `press aesthetic`. It refuses to overwrite an existing file.
  2. **Draft.** Writes every section, palettes and fonts included. "a pulp paperback brief with the Victorian house palette left in place is a failed draft".
  3. **Audit.** Checks for valid YAML, concrete craft language, coherence, and no attempt to repeal craft law. It then writes the file with a two-line header naming the brief.

### 14.5 `art-direction`

- **Args:** `root`, `maxPlates` (default 8).
- **Phases:**
  1. **Scout.** Summarizes the chapters with each one's "strongest concrete image". Reads metadata, the three design skills, `press aesthetic` verbatim, and `press figures` JSON ("the authoritative reading... do NOT re-parse the markdown by eye").
  2. **Commission** (parallel):
     - **Cover:** six aesthetic fields; every line of text verbatim.
     - **Logomark:** "suited to appear at 2.2in on a colophon".
     - **Portrait:** "No text in the image".
     - **Plates:** one per declared generatable figure with an `art:` description, else one candidate per chapter.
  3. **Curate.** Keeps at most `maxPlates`. Audits for verbatim text, concrete medium (never "detailed illustration"), a flat cover (no mockup), and one idea per plate.
  4. **Write.** Produces `art/commissions.md` with `## Cover`, `## Plates` (each with its `press art accept … --as plate:<name>` line), `## Logomark`, and `## Author portrait`. Prior "Accepted" lines are kept under `## Acceptance record`.

### 14.6 The skills (`press skills`, captured)

```text
book-aesthetics	…/src/press/data/skills/book-aesthetics.md
cover-design	…/src/press/data/skills/cover-design.md
elems_of_style	…/src/press/data/skills/elems_of_style.md
hemingway	…/src/press/data/skills/hemingway.md
humanizer	…/src/press/data/skills/humanizer.md
onwritingwell	…/src/press/data/skills/onwritingwell.md
plates-and-woodcuts	…/src/press/data/skills/plates-and-woodcuts.md
press-logomark	…/src/press/data/skills/press-logomark.md
profile-lifecycle	…/src/press/data/skills/profile-lifecycle.md
registrations	…/src/press/data/skills/registrations.md
overused-jargon	…/src/press/data/skills/overused-jargon/SKILL.md
```

| Skill (frontmatter name) | Purpose |
|---|---|
| `humanizer` (`human-writing`, v2.0.0, CC-BY-SA-4.0) | Draft, revise, and audit prose "so it sounds like a specific writer making deliberate choices rather than a generic assistant"; a large diagnostic pattern catalog and a scoring rubric. |
| `onwritingwell` (`writing-well`) | An operational synthesis of Zinsser's *On Writing Well* for nonfiction, with an "LLM-specific failure modes" section. |
| `elems_of_style` (`elements-of-style`, CC0) | Clarity, concision, and correctness after Strunk & White. |
| `hemingway` (`hemingway-prose`) | Concrete detail, compression, omission, restraint, "without becoming a surface imitation". |
| `overused-jargon` (CC0) | The watchlist skill. Modes: Draft, Revise, Audit, Discover, Maintain. "A watchlist match starts a review. It does not decide the edit." Ships `references/watchlist.csv`, `scripts/jargon_lint.py` (the portable copy), and `scripts/discover_jargon.py`. |
| `book-aesthetics` | Elicits and writes `config/aesthetic.yaml`, with the full schema and a six-question interview ("Point me at three covers you wish this book sat beside"). |
| `cover-design` | House Victorian bookcloth idiom. Describe the object, not a style label; name every line of text verbatim; front board only, no mockup; "never 'detailed illustration'". |
| `plates-and-woodcuts` | Brief the plate like a period engraver: one idea per plate; "The joke belongs in the subject; the style stays dead serious"; deliberate landscape or portrait; machines as "compact brass apparatus... Never humanoid skeletal robots". |
| `press-logomark` | The printer's mark: on the colophon at about 2.2in and in the landing footer, "Nowhere else"; must survive at 0.5in in one ink; `assets/press-logo.png` with transparency. |
| `profile-lifecycle` | For maintainers: scaffold, prove, and seal a print profile. |
| `registrations` | ISBN, LCCN, ISSN, and ONIX paperwork end to end; "The press never issues a number over the network." |

The four "prose skills" that editorial-passes requires are humanizer, onwritingwell, elems_of_style, and hemingway. "Read the relevant ones before composing prose or art direction for any book" (CLAUDE.md).

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