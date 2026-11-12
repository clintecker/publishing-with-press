# Inside the press

::: {.in-this-chapter}
> **In this chapter:**
>
> - A map of the package
> - The data flow, end to end
> - One statement of each fact
> - The typed book model
> - The adapters boundary
> - Invariants
> - The selftest
> - The quality gate and the ratchets
> - Trust receipts
> - Extensions
> - Contributing a scar
:::

The earlier chapters treated press as a machine that takes a manuscript in and hands editions back. This chapter opens the case for the developer who keeps the builds running or wants to change the press itself. It names modules and files freely. In the examples, `alice` keeps a clone of the press repository in *\~/press* on `hatter`, beside the book in *\~/alice*.

## A map of the package

The press is one Python package, *src/press/*, of about 19,750 lines at the time of this writing. Every book repository runs the same code, and the package holds no book of its own. The title, the slug, the sentinels, the banned patterns, the front matter, and the art all live in the book repository. The press's *CLAUDE.md* states the rule: "There is no book in here." It also states the other half of the rule: "if a book needs machinery, the machinery belongs here".

The press enforces the first half in CI. Its *integration gate* is the CI job that builds the wheel, scaffolds a stranger's book, and runs `press all`. The gate requires that "no original-book identity may appear in a clean scaffold's public artifacts".

The design rests on four laws, which *docs/ARCHITECTURE.md* states in this order and this chapter cites by number. The first is "Facts are stated once." The second ranks generators over checkers over conventions. The third says that the press verifies artifacts as objects. The fourth is "Scars become law."

The modules fall into sixteen areas. Table 16.1 lists each area with its modules and what they do.

| Area | Modules | Meaning |
|--------------------|------------------------------------------------|------------------------------------|
| Entry and CLI | `__main__.py`, `catalog.py`, `brand.py` | `__main__.py` holds the route table, the console, and help. `catalog.py` holds the catalog of commands. |
| Book model | `booklib.py`, `bookmodel.py`, `yamlio.py` | These modules find the book, read its config into a typed book, and do all YAML reading and writing. |
| Registry | `registry.py` | It names every artifact, the build order, and the download names. |
| Build | `build.py`, `dropcaps.py`, `figures.py`, `profiles.py`, `provider_specs.py`, `aesthetic.py`, `print_safe.py`, `webmeta.py`, `reader_meta.py`, `package_source.py`, `wordcount.py` | These modules prepare the inputs, run pandoc and latexmk, and assemble each edition. |
| Generators | `gen_front_matter.py`, `gen_index.py`, `gen_authorities.py`, `gen_coverwrap.py`, `barcode.py` | Each one writes a part of the book from config. |
| Editorial law | `check_source.py`, `check_the_checkers.py`, `style_audit.py`, `jargon_lint.py` | These modules are the four passes of the checker. |
| Verifiers | `verify_pdf.py`, `verify_formats.py`, `verify_pages.py`, `verify_archives.py`, `verify_coverwrap.py` | Each one inspects finished artifacts as objects. |
| Config | `config_cli.py`, `config_schema.py`, `config_store.py` | These modules run `press config` and hold its schema. |
| Print and commerce | `publish.py`, `commerce.py`, `edition.py`, `qualification.py`, `profile_lifecycle.py`, `providers/` | These modules hold the print checklists, the edition manifest, qualification, and the provider contract. |
| Registrations | `registrations.py`, `onix.py`, `pcn.py`, `idlookup.py` | These modules handle the numbers of Chapter 13, *Registrations*. |
| Art | `cover.py`, `illustrate.py`, `art.py`, `art_commission.py`, `art_enhance.py` | These modules run the art department of Chapter 11. |
| Operator and instruments | `operator.py`, `instruments.py` | These modules run the operator targets, such as `press improve`. |
| Desk | `desk/`, `desk_model.py`, `artifact_status.py`, `process_control.py`, `events.py` | These modules draw the desk. `events.py` defines a child-event protocol that nothing emits at run time. |
| Scaffolding | `scaffold.py`, `add.py`, `migrate.py`, `extensions.py` | These modules make a book, add chapters, migrate between majors, and check extension manifests. |
| Trust | `selftest.py`, `selftest_book.py`, `selftest_release.py`, `invariants.py`, `receipts.py`, `scenarios.py`, `mutation.py`, `quality_checks.py`, `results.py`, `doctor.py` | These modules check the press itself. |
| Boundary | `adapters/` | It is the one approved home for process, environment, and URL calls. |

Table: Table 16.1. The module areas of src/press

@fig:module-map draws the same areas as a stack. The ruled frame around the outside is the adapters boundary. The section "The adapters boundary" later in this chapter explains what passes through it.

![The module areas of the press package](assets/woodcuts/16-01-module-map.png){#fig:module-map .diagram width=full-measure fig-alt="A stack of labeled bands for the press's module areas, from the command line at the top to the book model at the bottom, with a trust column down the right side. A heavy ruled frame encloses everything, and three arrows leave through it to the operating system."}

<!-- art: ARCHETYPE stack, alternating 10 and 20 percent gray bands, labels centered in small sans, module names in small monospace beneath each. Top band, full width: "entry and CLI" (__main__.py, catalog.py). Band 2: "desk", "operator and instruments". Band 3: "build", "generators", "editorial law", "verifiers". Band 4: "print and commerce", "registrations", "art", "scaffolding". Band 5, full width: "registry" (registry.py). Bottom band: "book model" (bookmodel.py, booklib.py), "config". Right side, one tall box spanning bands 1 to 6: "trust" (selftest, invariants, receipts). Around everything, a heavy ruled frame labeled at its top edge "adapters/" in monospace. Three short arrows cross the frame outward on the right, labeled "subprocess", "os.environ", "urllib". The reader should see the frame first. -->

Every command enters through *__main__.py*. Both `press pdf` and `python -m press pdf` arrive there. The route table then finds the target in the catalog. For an unknown target, the press prints `unknown target: X` with a suggestion and exits with status 2. The suggestion comes from difflib, which compares what you typed against the catalog.

## The data flow, end to end

A full build moves through the package in one direction. It starts with the files in the book repository and ends with verified artifacts in *dist/* and, in CI, a published release. @fig:end-to-end-data-flow draws the whole path for the Alice book.

![The data flow from book repository to release](assets/woodcuts/16-02-end-to-end-data-flow.png){#fig:end-to-end-data-flow .diagram width=full-measure fig-alt="A top-to-bottom flow. Config files, chapter files, and design fragments merge into one input box, pass through rendered defaults and pandoc with its filters, fan out to six writers, collect in dist with two editions that bypass pandoc, and pass through three verifiers, page assembly, and CI."}

<!-- art: ARCHETYPE data-flow, top to bottom. Row 1, three dog-eared file boxes: "config/*.yaml", "book/chapters + book/appendices", "profiles + aesthetic + front matter". Row 2, rounded boxes beneath: "bookmodel", "booklib.chapter_files", "build/*.tex". All converge on a rounded box, 2 pt shadow: "build.book_inputs". Row 3, three boxes side by side: "gen_index -> build/generated/", "render_defaults -> build/defaults/", "gen_authorities -> dist/alice-sources.md". Down: "pandoc + Lua filters", fanning out to "latexmk (pdf, print)", "epub", "html", "chunkedhtml", "plain", "docx". All converge on a cylinder "dist/alice.*". A bypass arrow runs from "build.book_inputs" down the left edge to the cylinder, labeled "markdown, source (no pandoc)". Down: "verify_pdf", "verify_formats", "verify_archives". Down: "pages, verify_pages". Below a dashed rule labeled "CI": "upload, tag: Release, main: Pages". The reader should see first one path from three inputs to one dist. -->

Three kinds of input enter at the top. The config files under *config/* go to `bookmodel`, which turns them into a typed, validated book. The chapter files and appendix files under *book/chapters/* and *book/appendices/* go to `booklib.chapter_files`, which finds them and sorts them. The build turns the design profile, the aesthetic, and the front matter into TeX fragments under *build/*. All three kinds of input meet in `build.book_inputs`, which hands one assembled set of inputs to everything after it.

Two generators run at this point. `gen_index` writes the subject index into *build/generated/*. The build treats the index as one more appendix. `gen_authorities` writes the sources companion straight to *dist/alice-sources.md*, because the press publishes it beside the book, never inside it.

Next, `render_defaults` turns each defaults template in the package into a concrete file, such as *build/defaults/pdf.yaml*. The templates name their paths with the prefixes `@press/` and `@book/` and the suffix `?optional`, as Chapter 7, *Building the editions*, describes. `render_defaults` resolves each prefix against the installed press or the book repository. It drops an optional file that the book does not have.

Pandoc reads each rendered file, runs its Lua filters over the manuscript, and hands the result to a writer. For the Print edition (the PDF) and the print interior, pandoc writes LaTeX and latexmk runs LuaLaTeX with `-lualatex`. The EPUB, HTML, chunked HTML, plain, and DOCX writers make the other five rendered editions. The stitched Markdown and the source zip go to *dist/* without pandoc.

The press writes every edition into *dist/* under the slug, as *alice.pdf*, *alice.epub*, and the rest. Three verifiers then open them. `verify_pdf` inspects the PDF, and `verify_formats` inspects the other editions and runs epubcheck on the EPUB. `verify_archives` opens the two zips and, when *config/authorities.yaml* exists, the sources companion. Then `verify_pages` crawls the assembled *dist/pages/*.

The third law governs the bottom of the figure: "Verifying without rebuilding is forbidden by construction." The command line enforces it through the dependency edges in the registry, so a verify target rebuilds the artifacts it verifies, with the one exception Chapter 8 names. The invariant ledger, which the section "Invariants" describes, records the rule as `INV-graph-no-stale`.

On `printshop`, CI keeps the artifacts as the upload bundle when the build finishes. A push of a tag also creates a GitHub Release, with notes taken from the CHANGELOG. A push to `main` deploys the Pages site from the Pages bundle. Chapter 14, *Continuous integration and the release contract*, covers that half of the path.

The print pack takes a side branch that the figure leaves out. `print_safe` prepares the images, the build writes the print interior, and `verify_pdf --profile print` inspects it. Then `gen_coverwrap` draws the cover wrap in TikZ through latexmk, and `verify_coverwrap` inspects the wrap. The `publish` checklist, the edition manifest, and qualification follow. The commerce gate at the end of `press all` builds this branch only for a book that enables print ordering.

Two fixed dates keep the artifacts reproducible: `SOURCE_DATE_EPOCH` (Chapter 7) and the source zip's member timestamp (Chapter 8).

## One statement of each fact

The first law continues past its first sentence: "If you find the same fact in two places, one of them is a bug already filed or a bug you should file." The press applies the law to books, and it applies the same law to its own code. Before you add a list of anything to the press, look for the list that already exists.

The catalog is the press's single statement of its commands. *catalog.py* holds one typed table. The usage text, `press --help`, and the picker on the desk all render from it. A new target goes into the catalog once and appears in all three places. A selftest check named `command_catalog` reads the table. The selftest's success line ends with the promise that "usage and README name every target".

The registry is the single statement of the artifacts. `ARTIFACTS` in *registry.py* names every artifact and what it depends on. `build_order` derives the order of the build from those edges, and `download_names` gives the filenames that the Pages bundle offers for download. The build and the downloads page read the same table, so they cannot disagree about what the book publishes.

YAML has one door. *yamlio.py* calls itself "the single YAML door". Every read or write of a YAML file in the press passes through it, with ruamel.yaml at YAML 1.2. A second YAML library, or a second set of settings, would let two parts of the press read the same file two ways.

`press selftest --write-docs` generates four things from their sources: *docs/REFERENCE.md*, *docs/INVARIANTS.md*, *docs/PROVIDER-QUALIFICATION.md*, and the packaged provider record. The selftest's `docs` check fails on any difference in the three documents, so they cannot fall behind the code. The `contract_mirror` check keeps *AGENTS.md* equal to *CLAUDE.md* below the heading in the same way.

One fact lives in two places by design: the jargon lint and its copy in the overused-jargon skill (Chapter 15). The `jargon_parity` check requires them to match byte for byte.

::: {.tip}
> **Tip:** After you change a command, an invariant, or a provider record, run `press selftest --write-docs` and commit the regenerated documents in the same commit as the change.
:::

## The typed book model

Chapter 3, *The shape of a book repository*, introduced the *book model*, the typed set of rules the press holds for every config field. For each field, the model records its kind of value, whether the book must supply it, and its default. `press config list` prints every field that the CLI registry in *config_schema.py* declares, with its type and a one-line description.

Two modules hold the model. *booklib.py* finds the book root, which is `BOOK_ROOT` or the current directory, and reads the metadata. It also finds the chapter files. It holds the *release witnesses*, the floor of two sentinels and 24 pages that a release build requires. A release build is one with `PRESS_RELEASE` set, which CI does for a tag, as Chapter 14 describes. *bookmodel.py* reads the config into a frozen, typed `Book`.

Frozen means that no code can change the `Book` after the model builds it. Every later module reads the same values, and no module can quietly adjust a field for the modules after it. If you add a config field to the press, declare it in the model, with its type and its default, and in the CLI registry in *config_schema.py*. Then read it from the `Book` everywhere. Never read the raw YAML a second time. The model collects every problem before it reports, so one run lists them all.

Writes go through the same model. `press config set` runs the new value through the typed model before it touches a byte on disk. *config_store.py* then writes a temporary file beside the original and moves it into place with `os.replace`, so a crash leaves either the old file or the new one. The round trip keeps your comments. A value that YAML could read as another type, such as `"3"` or `"true"`, goes back to the file in double quotes.[^16-quotes]

`press config` also refuses any value that looks like a secret, from words such as "secret", "token", and "password" to the prefixes of real keys. The rule is broad. The press refuses a dedication that contains the word "secret", with exit status 4. `alice` must find another word for hers.

[^16-quotes]: Without the quotes, a later read would turn the string `3` into a number and the string `true` into a boolean.

## The adapters boundary

*src/press/adapters/* is, in its own words, "the one approved home for direct `subprocess`/`os.environ`/`urllib` calls". Every external program that the press runs starts there: pandoc, latexmk, epubcheck, and the poppler tools. Environment reads and network requests belong there too.

The package holds a small set of tools. Its HTTP client gives every request a 30-second timeout by default and a cap on the bytes it will read. The client also retries failed requests. The package also holds an import guard and support for streaming. Because every outside effect belongs in one package, a reviewer who wants to know what the press does to the machine reads one directory.

The press checks the process side of the boundary mechanically. A gate searches the modules outside *adapters/* for direct process calls. The gate once had a blind spot, which the sidebar describes.

::: {.sidebar}
> **The import the gate did not see**
>
> The adapters gate searches the rest of the package for direct process calls, so that every process start stays in one package where a reviewer can find it. A line that read `from subprocess import Popen` slipped past it, because the call site then names only `Popen` and never mentions `subprocess`. The desk launcher, which starts the targets you pick on the desk, used exactly that form, so it started processes from outside the boundary while the gate reported nothing. The fix, in version 2.3.1, had two parts. The gate now resolves aliases, so a name imported from `subprocess` counts as `subprocess` wherever it appears. The launcher itself moved into `press.adapters`, where every other process start already lived.
:::

When an external tool fails, the press unwraps Python's `CalledProcessError` and exits with the tool's own status. The ledger names this `INV-cli-exit-code`. The selftest shows it with a tool that exits 43, and the press exits 43 as well. Table 16.2 lists the general exit statuses.

| Situation | Meaning |
|------------------------------|------------------------------------------------------|
| Success | The press exits 0. |
| A check or verify failure | The press exits 1, with the message that names the failure. |
| Bare `press`, or an unknown target | The press prints the usage or a suggestion and exits 2. |
| A failing external tool | The press exits with the tool's own status. |
| `press config` | The command exits 0 on success, 2 on a usage error, 3 for an unknown or non-writable field, 4 for a refused or invalid value, and 5 when a read finds no key. |

Table: Table 16.2. Exit statuses of press targets

The press reads the image-model keys, `OPENAI_API_KEY` and `GEMINI_API_KEY`, on demand and never stores them, under `INV-art-key-never-stored`. The press also decides how strict to be about the toolchain from `PRESS_TOOLCHAIN`, which the toolchain image sets, and never from the ambient `CI` variable. Chapter 8 gives the reason.

::: {.warning}
> **Warning:** Keep every `subprocess`, `os.environ`, and `urllib` call inside *adapters/*, their one approved home. The gate refuses a direct process call anywhere else in the package.
:::

## Invariants

An *invariant* is a named entry in the press's ledger of properties that the press enforces. The ledger is one file in the press repository, *.celebrimbor/invariants.yaml*. `press selftest --write-docs` renders it as *docs/INVARIANTS.md*, and the `docs` check keeps the two equal. At the time of this writing, the ledger holds 85 invariants, and it marks 13 of them critical.

Each entry has four parts, which Table 16.3 describes.

| Part | Meaning |
|-----------------|------------------------------------------------------------|
| Statement | It states the property in one sentence. For `INV-art-key-never-stored`, it reads "The image-model key is read from the environment on demand and its absence is refused, never stored." |
| Enforced by | It names the function that makes the property hold, in the form `module:function`. |
| Proven by | It names the test or fixture that shows the enforcement works. |
| Does not cover | It states the known edges of the property, in plain words. |

Table: Table 16.3. The four parts of a ledger entry

The press states its reason for the fourth part: "An honest limitation column is the point: a guarantee whose edges are unstated is a guarantee waiting to be overtrusted." Table 16.4 shows four of the limits as the ledger records them.

| Invariant | Does not cover |
|----------------------------|----------------------------------------------------------|
| `INV-editorial-battery` | "The glyph law flags legitimate Greek or math; short title-case headings slip." |
| `INV-graph-no-stale` | "CLI-path only; importing a verifier module directly skips the rebuild." |
| `INV-pdf-detector` | "Two synthetic extremes; a faint hairline can still read as blank." |
| `INV-archive-source-policy` | "a novel secret filename is not caught." |

Table: Table 16.4. Limits that the ledger states

Read the limits before you write code that depends on an invariant. `INV-graph-no-stale` is the usual trap for a developer. A script that imports `verify_pdf` and calls it on *dist/alice.pdf* skips the rebuild.

The 13 critical invariants include several that earlier chapters met at work, among them `INV-pdf-detector` and `INV-format-witness` in Chapter 8. The others are `INV-archive-source-policy`, `INV-config-slug`, `INV-edition-manifest`, `INV-editorial-checkers`, `INV-extension-conformance`, `INV-extension-seal`, `INV-graph-no-stale`, `INV-migration-safe`, `INV-provider-contract`, `INV-release-receipt-chain`, and `INV-release-tag-grammar`.

## The selftest

`press selftest` is, in its own description, "the press checking itself." It runs 29 checks in a fixed order. The test suite parametrizes pytest over the same list, so the command and the test suite cannot disagree about which checks exist. Example 16.1 lists the checks in the order the selftest runs them.

**Example 16.1. The selftest checks, in order**

```text
 1 arithmetic             16 receipt_chain
 2 slug_invariant         17 edition_manifest
 3 jargon_parity          18 provider_qualification
 4 source_policy          19 profile_seals
 5 pages_verifier         20 commerce_config
 6 scaffold_neutrality    21 commerce_release_gate
 7 book_model             22 provider_contract
 8 registry               23 coverwrap_detectors
 9 format_witnesses       24 aesthetic_schema
10 editions_agree         25 contract_mirror
11 editorial_checkers     26 migration
12 site_identity          27 extension_conformance
13 authorities_ledger     28 command_catalog
14 honest_refusals        29 docs
15 release_grammar
```

Most names say what the check guards, and a few need a sentence. `arithmetic` checks the ISBN, EAN-13, and ISSN arithmetic against canonical examples. `scaffold_neutrality` scaffolds a new book and searches it for the original book's identity. `release_grammar` feeds the tag parser good tags such as `v1.0.0` and bad ones such as `v1.0`, `v1.0.0-rc1`, and `v01.0.0`. The parser must accept the first and refuse the rest. `contract_mirror` and `docs` are the two checks of the section "One statement of each fact" earlier in this chapter.

A passing run ends with one line: "Selftest passed: 29 checks, arithmetic agrees with the canonical examples, usage and README name every target".

From an installed wheel, the selftest skips the checks that read repository files. To run all 29, run it from a clone of the press with the editable install that the section "Contributing a scar" sets up.

## The quality gate and the ratchets

The press's development checks run on a separate framework called celebrimbor, at the time of this writing at version 0.12.0. The *quality gate* is celebrimbor's gate as the press configures it. *scripts/verify.sh* runs it with `celebrimbor gate`. Celebrimbor is a development and CI dependency only. It needs Python 3.11 or later. No book installs it.

*src/press/quality_checks.py* registers 29 press domain checks with the gate. The press counts them separately from the selftest's 29. The gate also holds the press's ratchets. A *ratchet* is a floor recorded in a baseline file. The gate fails when a measurement falls below its floor. The press keeps three kinds:

- a branch-coverage floor for each module
- a mutation-score floor over the pure modules `barcode`, `artifact_status`, `dropcaps`, and `figures`, driven by *src/press/mutation.py*
- the Lua coverage floor, *.celebrimbor/baselines/lua-coverage.yaml*

The gate's philosophy, in *CONTRIBUTING.md*, reads: "Coverage measures that a line *ran*, not that its output was *right*." The rule that follows is "A producer is only proven by a verifier that rejects a broken artifact." The PDF verifier's cover check on page 1 exists because of the cover that passed at 11.5 percent (Chapter 1).

A *producer* in that rule is code that writes an artifact, such as the title-page generator. The *producer ledger*, *.celebrimbor/producers.yaml*, records the producers, and its pending entries carry `review_by` dates. The gate also holds *surfaces.yaml*, beside the ledger in *.celebrimbor/*, and a file named *known-bad.expected.yaml*.

The Lua filters of Chapter 7 have tests of their own under *tests/* in the press clone. *tests/lua/* holds *test_press_util.lua* and *coverage-hook.lua*, and *tests/lua_coverage.py* drives them. Four pytest files, such as *tests/test_lua_compiles.py*, are the entry points, so the Lua tests run inside `python3 -m pytest`. Without pandoc they skip. `PRESS_REQUIRE_LUA=1` turns a missing pandoc into a failure, and CI sets it. Before it did, the tests skipped in CI without a word.

The 3.0.2 coverage backfill for the filters found a test that proved nothing. A test of the tie after `Mr.` passed with no filter at all, because pandoc writes that tie itself. To see the filters' coverage on `hatter`, set `PRESS_LUA_COV_DIR` to an empty directory and run the Lua tests. Then run *scripts/lua_coverage_ratchet.py* `report --cov-dir` with that directory.

::: {.warning}
> **Warning:** Never pass `--update-baselines` locally, and do not run `scripts/coverage_ratchet.py --update`, which re-measures on your machine. Never update the Lua floor from a macOS measurement. Feed it CI's report with `update --from-report`.
:::

The gate is one part of the press's own CI. Table 16.5 lists the main workflows of the press repository.

| Workflow | Meaning |
|----------------------------|------------------------------------------------------------|
| *selftest.yml* | Job `quality` runs lint, the quality gate, Lua coverage, the site build, and a receipt. Job `selftest` runs `press selftest`, pytest, and a scaffolded book's `press check` on Ubuntu with Python 3.10 to 3.14 and on macOS 15 with Python 3.12. Job `desk` requires a bare wheel to refuse the desk and runs the desk headless from the `tui` wheel. |
| *integration.yml* | Job `consumer` runs *scripts/gauntlet-steps.sh* in the pinned toolchain image. |
| *toolchain.yml* | It builds and publishes the toolchain image as a multi-architecture image. |
| *docs-site.yml* | It builds the example PDFs in the pinned image, builds the press's Web site with the headless Chrome layout check required, and deploys it. |
| *ledger-review.yml* | It opens an issue every Monday for pending producer entries within 30 days of their `review_by` date. |

Table: Table 16.5. The main workflows of the press repository

The integration gate runs the press as a stranger would. In its own words, it must "build the wheel, scaffold a stranger's book, run the whole `press all`, and prove tampering turns the verifier red".

## Trust receipts

Chapter 14 describes the trust receipts, the twelve layers (@fig:trust-tiers), and the release receipt that names the wheel and toolchain digests. The ledger names the complete-chain rule `INV-release-receipt-chain`, and the selftest's `receipt_chain` check exercises it.

![The trust receipt chain](assets/woodcuts/16-03-trust-tiers.png){#fig:trust-tiers .diagram width=full-measure fig-alt="Twelve stacked bands of proof, from collection at the bottom to release at the top, each linked to the band below. Beside them, three tier boxes feed two CI receipts into an assemble step that writes one release receipt."}

<!-- art: ARCHETYPE stack. Left, twelve thin bands, alternating 10 and 20 percent gray, bottom to top: "collection", "unit", "property", "component", "damage", "graph", "scenario", "integration", "distribution", "container", "boundary", "release". A small chain-link glyph joins each band to the one below. Right, a separate column of three boxes, bottom to top, not aligned to particular bands: "quality tier", "integration tier", "release tier". From the first two, arrows labeled in monospace "receipt-quality" and "receipt-integration" run into a rounded box "press.receipts assemble". It writes a dog-eared file "release-receipt" with two lines inside: "wheel digest", "toolchain digest". Small italic note under the left stack: "a gap anywhere breaks the chain". The reader should see first the unbroken links of the left stack. -->

## Extensions

The extension contract, in *docs/EXTENSION-CONTRACT.md*, opens with one line: "Press extends by declaration, not by code." It goes on: "The press has no plugin loader, no entry-point group, and no import-time discovery, and that absence is the contract, not a missing feature." Behavior in the press "cannot come from the accident of which package imported first".

An extension adds an entry to one of five data tables, and the press selects the entry by its id. Table 16.6 lists the five extensible surfaces.

| Surface | Where it lives | Meaning |
|-------------------|-----------------------------------|-------------------------------------------------|
| `design-profile` | *data/profiles/\<id\>.yaml* | A book selects a profile with `print.profile`. |
| `provider-spec` | *data/provider-specs/\<id\>.yaml* | A book selects a provider with `print.provider`. |
| `artifact` | `registry.ARTIFACTS` | A build target or the download policy selects it. |
| `skill` | *data/skills/\<id\>/* | `press skills` and the workflows select it. |
| `workflow` | *data/workflows/\<id\>.js* | `press workflows` and the Workflow tool select it. |

Table: Table 16.6. The extensible surfaces

An extension declares itself in a manifest. Example 16.2 shows the reference manifest, *src/press/data/extensions/reference.yaml*, with its comments removed.

**Example 16.2. The reference extension manifest**

```text
name: acme-quarto
kind: design-profile
contract-major: 2
provides:
  - acme-quarto
requires:
  - pdf
invariants:
  - INV-acme-quarto-geometry
proofs:
  - fixture:acme-quarto.md
capabilities:
  - interior-geometry
publication: internal
```

`name` is the extension's own id, and it must not collide with an existing name. `kind` names the surface it registers into, and `contract-major` the contract its author targeted. `provides` lists the exact names it claims on that surface. `requires` lists the names it depends on, from the core or from itself. `invariants` lists the invariants it takes on, `proofs` names a proof for each, and `capabilities` lists what it asserts. `publication` is `published` or `internal`, for artifacts it adds.

The press seals five capabilities: `core-verification`, `path-containment`, `artifact-graph`, `config-validation`, and `release-gate`. An extension can depend on a sealed capability but must never claim one.

The contract defines five stages in the life of an extension. The press discovers manifests in sorted order, never in import order. It parses each with `load_manifest`, checks its conformance, and registers it. The extension then builds and verifies under the same laws as the core. The conformance gate refuses six faults, each with a located reason: a collision, an unsupported contract, an unknown dependency, a sealed claim, an unproven obligation, and a malformed manifest.

The selftest's `extension_conformance` check feeds the gate five hostile fixtures, and the gate must refuse each one. *hostile/collision.yaml* claims `pdf`, *version.yaml* targets major 99, and *sealed.yaml* claims `core-verification`. *unproven.yaml* has `proofs: []`, and *malformed.yaml* gives `contract-major` as the string `"two"`. Two critical invariants, `INV-extension-conformance` and `INV-extension-seal`, cover the gate.

At the time of this writing, the press supports one contract major, `SUPPORTED_CONTRACT_MAJORS = (2,)`. No runtime loads extensions. The gate exists and the selftest runs it, but nothing yet reads a third party's manifest during a build. The contract says: "A future runtime that *loads* extensions will reuse exactly this gate."

A book can still extend the press today through files that need no manifest. *config/cover-styles.yaml* and *config/illustration-styles.yaml* add art styles, and *config/aesthetic.yaml* sets the visual identity, all in Chapter 11. Stylesheets in *assets/web/* change the reader site. A *tex/title-page.tex* replaces the generated front matter, and *tests/known-bad/* adds fixtures for the book's own house rules, as Chapter 6 describes.

## Contributing a scar

The fourth law states the policy: "Every production failure earns a mechanical guard and an entry in CLAUDE.md's scars list. Do not relearn them." The product laws in *ROADMAP.md* say what form the guard takes: "A scar becomes an executable invariant, a named proof, or an explicit public contract".

The second law ranks the guards. It reads: "Prefer machinery that produces the right thing to machinery that detects the wrong thing, and either to a sentence in a document asking people to behave." If a generator can make the failure impossible, write the generator. If it cannot, write a check for the checker or a verifier that refuses the broken result.

`INV-graph-no-stale`, met earlier in this chapter, shows a finished scar. The guard is structural, in the registry's dependency edges. The ledger entry names the enforcement, names its proof, and states its limit, the command-line path only. *CLAUDE.md* carries the scar in its list, beginning "Verifying `dist/` without rebuilding blesses stale artifacts".

### Setting up to work on the press

*CONTRIBUTING.md* asks for one setup and one rule: "Prove changes against a real book." Example 16.3 shows the whole loop for `alice`. She clones the press, installs the clone in editable mode with its `dev` extra into the environment that her book already uses, and installs the pre-commit hooks. She then runs `press doctor` and `press selftest`, builds the whole book, and runs the local proof.

**Example 16.3. A working setup on hatter**

```text
$ . ~/.press-venv/bin/activate
$ git clone https://github.com/clintecker/press ~/press
$ cd ~/press
$ pip install -e '.[dev]'
...
$ pre-commit install
...
$ press doctor
...
this machine can make books
$ press selftest
...
$ cd ~/alice
$ press all
...
$ cd ~/press
$ scripts/verify.sh
...
```

The editable install points `press` in *\~/alice* at the files in *\~/press*, so an edit takes effect at the next run. After `pre-commit install`, every commit runs ruff, mypy, shellcheck, yamllint, pymarkdown, the TOML and JSON checks, and the selftest. CI runs the same battery with `pre-commit run --all-files`. *CONTRIBUTING.md* puts the point of `press all`: "A green `pip install` is not a working pipeline."

*scripts/verify.sh* runs lint, types, the selftest, and pytest first, and then the coverage and mutation ratchets and the site build. With `--quick`, it stops after the fast layer. With `--full`, it also runs CI's container gauntlet in the pinned toolchain image, which needs Docker. Run `--full` before you push. To look at rendered output while you tune a template or a filter, *scripts/dev-render.sh* builds one book in the pinned image from the checkout, with no reinstall.

### Submitting a change

To contribute a scar of your own:

1. Reproduce the failure in a real book, such as *~/alice*, and keep the broken artifact or input.
2. Write the guard, as a generator if you can and as a check or a verifier if you cannot.
3. Add a test that fails before the guard and passes after it, such as a known-bad fixture or a verifier test fed the broken artifact.
4. Add an entry to *.celebrimbor/invariants.yaml* with all four parts.
5. Add the scar to the scars list in *CLAUDE.md*.
6. Copy the same change into *AGENTS.md*, below the heading.
7. Run `press selftest --write-docs`, and put the regenerated documents in the same commit as the code.
8. Run `scripts/verify.sh --full` from your clone.
9. Open a pull request that follows the template.

::: {.tip}
> **Tip:** Draft the ledger entry's "does not cover" line before you write the guard, and revise it once the proof runs.
:::

The template asks for three things: "a test that fails before and passes after, regenerated projections, and the compatibility impact." A change to the rendered output of a valid book is a breaking change. It waits for a new major, and the pull request says so. CI runs the selftest and the integration gate on every pull request. Defects and proposals go through the repository's issue forms. A security report goes privately, as *SECURITY.md* describes, never as a public issue.

The press has one maintainer, and the maintainer pushes to `main` directly by design.[^16-main] The checks stop a change at the release boundary instead. The release script pushes the immutable tag, and then the release contract waits for the `quality`, `consumer`, and `desk` checks on that commit. A change that broke any of them fails the release contract, and the floating major does not move.

[^16-main]: The press's *SECURITY.md* records the decision under issue 153. The press enforces trust at the tag, so `main` stays open and every immutable tag stays fixed.
