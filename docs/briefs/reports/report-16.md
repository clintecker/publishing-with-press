# Report: Chapter 16, Inside the press

File: `book/chapters/16-inside-the-press.md`. Not committed.

## Word count

`press wordcount`: 5,646 (target 5,000; within 15 percent). The count
includes the three `art:` comments and the index comment (about 450
words); prose, tables, and captions alone come to about 5,200.

## Checks

- `press check`: passes (source checks, checker self-test, editorial
  checks, jargon). The jargon report has one `inspect` note for this file,
  "honest" at line 167, inside a verbatim quotation from the ledger.
- Fences: all tagged `text`, no code line over 64 columns, no trailing
  whitespace, ASCII only.
- `art:` comment plus image line: 173, 187, and 164 words (all under 190).
- Sidebar: 129 words. Tips 3, warnings 3. Footnotes 5, all `16-` labels.

## Figures

- 16.1 `@fig:module-map` (stack): bands for entry and CLI; desk, operator
  and instruments; build, generators, editorial law, verifiers; print and
  commerce, registrations, art, scaffolding; registry; book model and
  config; a tall trust column on the right; a heavy ruled frame labelled
  `adapters/` with three arrows out (`subprocess`, `os.environ`,
  `urllib`). Two departures from the brief's list: I added "operator and
  instruments" (it is a module area in the fact file and in Table 16.1),
  and I labelled the "graph" band "registry" per the vocabulary ("the
  registry", never "the graph").
- 16.2 `@fig:end-to-end-data-flow` (data-flow): three inputs, bookmodel /
  booklib.chapter_files / tex fragments, build.book_inputs, gen_index and
  gen_authorities side arrows, render_defaults, pandoc + Lua filters, six
  writers, dist cylinder, three verifiers, pages assembly, verify_pages,
  then a CI band (upload, tag Release, main Pages). The print branch is
  described in prose and left out of the figure.
- 16.3 `@fig:trust-tiers` (stack): twelve receipt layers bottom to top,
  chained; beside them three tier boxes (quality, integration, release)
  feeding `receipt-quality` and `receipt-integration` into
  `press.receipts assemble`, which writes `release-receipt` (wheel digest,
  toolchain digest).

## Facts needed and not found

- Which receipt layers belong to which tier. The fact base names the 12
  layers and the 3 tiers but not the grouping, so the directive tells the
  illustrator to draw the tiers as a separate column "not aligned to
  particular bands", and the prose does not assign layers to tiers.
- facts-16 sends trust receipts to "§12.5", which is not in facts-16. I
  took the receipt layers, tiers, the chain-completeness quote, the
  release receipt's two digests, the CLI, and the release contract's
  receipt steps from facts-14 sections 12.5 (same fact base). Flagging in
  case that is out of bounds.
- What `instruments.py`, `import_guard`, and the adapters' "streaming"
  do. Named only, not explained.
- The exact refusal message of `press config` for a secret, and the key
  path for a dedication. No session shown; the exit status (4) comes from
  the exit-code table.
- The selftest success line is 115 characters, too long for a 64-column
  fence, so it is quoted in prose.
- The ledger's YAML key names. Table 16.3 gives the four parts in the
  fact file's words, not as YAML keys.

## Inferences to review

- Sidebar: "the call site then names only `Popen`" (why the gate missed
  it) and the gloss of the desk launcher as what "starts the targets you
  pick on the desk". The fact file says only that the gate missed the
  form and the launcher used it.
- Warning on baselines: the reason ("would record that machine's numbers
  as the floor for everyone") is my explanation, not a quoted one.
- "The model collects every problem": the Alice example of two
  complaints in one run illustrates "every problem collected".

## Contradictions in the fact file

- facts-16 16.3 says ARCHITECTURE.md names `quality/invariants.yaml`.
  The chapter gives only `.celebrimbor/invariants.yaml` and is silent on
  the old path. Same for `surfaces.yaml`.
- Extension contract major 3 and `config/extensions.yaml`: not
  mentioned; the chapter says the press supports `(2,)` and no runtime
  loads extensions.
- Nothing from section 20.C is stated. `events.py` is listed only as a
  module in the desk area (20.B.17); its protocol is not described.

## Checker residuals (`ste_check.py`, 38 findings) and defence

- sentence-length: the In-this-chapter box, fig-alt lines, filename
  lists (the dots in `*.yaml*` names split badly), and sentences that
  run into footnote text. Prose sentences are all 30 words or fewer,
  except two that carry long verbatim quotations (the CONTRIBUTING
  quote and the integration gate's own words). The mean over prose
  sentences is about 15 words, a little under the 16 to 22 the brief
  asks for. Tables and lists pull it down.
- passive: every remaining hit sits inside a quotation ("is forbidden
  by construction", "Facts are stated once", "edges are unstated ...
  overtrusted", "is only proven by a verifier").
- paragraph-length: the fig-alt and `art:` lines, the selftest
  explanation paragraph (now split), and the sidebar (7 sentences, one
  boxed aside).
- semicolon: only inside the verbatim "does not cover" quotations in
  Table 16.4 and the index comment. No semicolon in my own prose.
- word swaps (verify, therefore), -ing forms (alternating, branching in
  the art comments, "Contributing" in the A-head the brief fixes), the
  phrasal verb "go through" (one use, in "Writes go through the same
  model"): left as period-correct.

## Revision (after facts-16, dev-16, copy-16, type-16)

Word count after revision: 5,679 by `press wordcount` (within 15
percent of 5,000). `press check` passes. Tools run: `tag-fences.py`,
`prefix-footnotes.py`, `space-art-comments.py` (no changes needed).
Art comment plus image line: 173, 186, 164 words. Sidebar: 125 words,
6 sentences. Footnotes: 4 (16-epoch, 16-quotes, 16-macos, 16-main).
Admonitions: 2 tips, 3 warnings.

### Fact check (all blocks and shoulds applied)

- Contradicted 1: the no-stale rule now says a verify target "rebuilds
  the artifacts it verifies" and names the one exception (`press
  verify-formats` reads an existing *dist/alice.pdf*). "Last week's
  PDF" claim gone. The Invariants section and its warning carry the
  exception too (Missing 2 accepted). The scar example no longer says
  "every verify target".
- Contradicted 2: the closing now says the release script pushes the
  immutable tag first, and a red contract leaves the floating major
  where it was.
- Unsupported 1: the adapters gate is described as a process-call gate
  only; the warning keeps the three-module rule as the package's own
  words.
- Unsupported 2: "The boundary also decides the exit status" cut.
- Unsupported 3: the description/slug example is cut; "so one run lists
  them all".
- Unsupported 4: the baseline warning now carries only the S1 rules
  (`coverage_ratchet.py --update` re-measures on your machine; never
  update the Lua floor from macOS; `update --from-report`).
- Unsupported 5, 6, 7: `receipt-integration` is now downloaded by the
  release contract (no producer named); "a receipt records that a layer
  ran" replaced by a definition as the records receipts.py keeps per
  layer; footnote 16-quotes cut to its first clause.
- Drifted: `verify_archives` adds the sources companion; `--write-docs`
  generates four things; secret regex detail cut (the developmental
  edit asked to cut serialization detail, which removes the "api key"
  wording); `CI=false` "would still read as true"; "The press states
  its reason"; selftest skip tied to the installed wheel; *surfaces.yaml*
  placed, *known-bad.expected.yaml* unplaced; "The gate's philosophy";
  Table 16.5 "main workflows"; toolchain "multi-architecture image";
  the `boundary` layer sentence cut. Registry row name kept per the
  vocabulary.
- Missing 1 (events.py): accepted, one clause in Table 16.1.

### Developmental

- 1 (setup): new B-heads "Setting up to work on the press" (Example
  16.3, the `$` session: activate *~/.press-venv*, clone, `pip install
  -e '.[dev]'`, `pre-commit install`, `press doctor`, `press selftest`,
  `press all` in *~/alice*, `scripts/verify.sh`) and "Submitting a
  change" (the pull request template, issue forms, private security
  reports, one maintainer; `main` direct pushes described as the
  maintainer's). verify.sh `--quick`/`--full` and `dev-render.sh` from
  S1 and S4. The clone URL is the repository named in S2's links.
- 2: the skip is described as the fact file does (installed wheel).
- 3: the four laws listed in order at the end of "A map of the
  package", then cited by number.
- 4, 5: integration gate, release witnesses (with `PRESS_RELEASE`),
  producer ledger (with *producer*), trust receipt defined at first use.
- 6: no field-declaration excerpt exists in the fact base. The chapter
  says what the model records (kind, required, default, from Ch. 3),
  where it lives, and that `press config list` prints the declared
  fields. Not shown: an excerpt or collected-problems output (no fact).
- 7 (adapters helper names): declined; the fact base names no helper.
- 8: Lua tests located (S3), how they run, the floor file, and the
  coverage report command. "Lua coverage floor" used throughout.
- 9: the receipts CLI block cut; `assemble` kept in the CI paragraph.
- 10: "The press counts them separately from the selftest's 29."
- 11: Figure 16.2 directive now has the bypass arrow "markdown, source
  (no pandoc)" to the dist cylinder.
- 12: serialization detail cut to the atomic replace and the quoting
  rule; the secret rule cut to its consequence.
- 13: Example 16.1 (critical invariants) removed; the 13 names are in
  one prose sentence. Examples renumbered: 16.1 selftest checks, 16.2
  manifest, 16.3 setup.
- 14, 15: the duplicated docs/contract_mirror explanation replaced by a
  pointer; the Monday sentence cut, the table row kept; the
  security-controls, codeql, dependency-review, roadmap rows dropped
  (table now "main workflows").
- 16: the extend-today list is a grouped prose paragraph.
- 17: one session (Example 16.3) added.

### Copyedit

All three blocks fixed ("lands"; both one-line closers deleted). Shoulds
applied: 4 to 31 except 19 (Tip deleted, as asked) and 22 (producer
defined from the CONTRIBUTING quote rather than as "module plus its
verifier", which the facts do not state). Mays applied: 32, 33, 34, 35,
36, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51 (steps split), 54.
Mays declined:
- 37: the indent numbers left the chapter with the serialization cut.
- 38: the regex wording left with the same cut.
- 39: applied in substance ("decides how strict to be about the
  toolchain from").
- 52: the paragraph now carries the verify-formats exception, so the
  warning adds a step (`press pdf` first) and no longer repeats it.
- 53: the sidebar is held to six sentences by ruling; 125 words meets
  the markup guide's 120 to 180.
- 55: resolved: six faults (the refusal list), five hostile fixtures,
  named one for one; no claim that a sixth fixture is absent.
- 56: resolved as dev 10.

### Typesetter

- 3: Table 16.1's Modules column widened (separator 20/48/36) and the
  Meaning cells shortened.
- 4: Figure 16.2 label `latexmk (pdf, print)`; gen_index,
  render_defaults, and gen_authorities merged into one row; the CI tail
  folded to one box.
- 1: moot (Example 16.1 of the critical invariants is gone).
- 2: the manifest (now Example 16.2) is 14 lines; I left it whole
  because the fields paragraph walks every key. Re-check the page break
  after the figures land.

### Residual ste_check findings

Passives only inside quotations (laws, the ledger quote, CONTRIBUTING);
the paragraph-length hits are the fig-alt and art lines; the semicolon
is the index comment; "whether" stays (period-correct); the remaining
sentence-length hits are the In-this-chapter box, fig-alt text, and two
sentences carrying long verbatim quotations (the first law's second
sentence and the CONTRIBUTING philosophy).
