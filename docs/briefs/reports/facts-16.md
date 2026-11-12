# Fact check: Chapter 16, Inside the press

Chapter: `book/chapters/16-inside-the-press.md`. Fact file:
`docs/briefs/facts/facts-16.md` (including Shared context, sections 19
and 20). Per the desk's instruction, `docs/briefs/facts/facts-14.md`
section 12.5 is admissible for the trust-receipt and release-contract
facts, and facts from other chapters' slices of the same fact base are
cited where they decide a claim.

Status: **blocked**. 2 contradicted, 7 unsupported, 12 drifted, 2 missing.

## The writer's three flagged inferences

1. **Sidebar, line 129** ("because the call site then names only `Popen`
   and never mentions `subprocess`"; "The desk launcher, which starts the
   targets you pick on the desk"). **Supported.** The cause follows from
   the file's fix, "The gate now resolves aliases" (facts-16 19.28): a gate
   that had to learn to resolve aliases was missing the aliased name. The
   launcher gloss is supported by the desk facts: the picker "is generated
   from `catalog.COMMANDS`" and "`process_control.py` runs exactly one
   child at a time" (facts-15, RUN view). No change needed.
2. **Warning, line 255** ("A baseline written on one workstation would
   record that machine's numbers as the floor for everyone"). **Unsupported**;
   see Unsupported 4.
3. **Line 108** ("A book with a missing description and a malformed slug
   gets both complaints in one run"). **Unsupported**, and the fact base
   places the description rule elsewhere; see Unsupported 3. The general
   claim "The model collects every problem" is supported ("every problem
   collected", 16.1).

## 1. Unsupported (severity: blocks)

1. Lines 124 and 147. "A gate searches the modules outside *adapters/* for
   direct use of the three modules" and, in the warning, "Do not import
   `subprocess`, read `os.environ`, or call `urllib` ... or the boundary gate
   will refuse the change." Searched facts-16 and all fact files for the
   gate's scope ("gate", "boundary gate", "os.environ", "urllib"). Every
   mention is the subprocess gate: "The subprocess gate's blind spot. The
   adapters boundary gate missed `from subprocess import Popen`" (19.28).
   Nothing says the gate checks `os.environ` or `urllib`. Fix: say the gate
   searches for direct process calls (as the sidebar already does), and
   keep the three-module rule as the package's own words, "the one approved
   home for direct `subprocess`/`os.environ`/`urllib` calls", without
   claiming a gate refuses the other two.
2. Line 132. "The boundary also decides the exit status that you see."
   Searched for where `CalledProcessError` is unwrapped. The file says only
   "that tool's own exit code (`CalledProcessError` unwrapped,
   `INV-cli-exit-code`; selftest proves 43 → 43)" (17.4), with no module
   named. Fix: cut the attribution to the boundary; begin "When an external
   tool fails, the press unwraps ..."
3. Line 108 (writer's inference 3). "A book with a missing description and
   a malformed slug gets both complaints in one run". The file says only
   "frozen typed `Book`, every problem collected" (16.1). facts-03 records
   the description rule as a `press check` rule, not a model rule:
   "`description` ... **`press check` requires it** (`check_source.py:45-51`)".
   So the example puts a check-time complaint into the model. Fix: cut the
   example, or use two model problems the fact base names, or soften to
   "The model collects every problem before it reports, so one run lists
   them all."
4. Line 255 (writer's inference 2). "A baseline written on one workstation
   would record that machine's numbers as the floor for everyone." facts-16
   gives the rule with no reason: "Never pass --update-baselines locally".
   "Do not run `scripts/coverage_ratchet.py --update`" (16.5). The nearest
   fact is facts-07: "Contributors must never `update` that floor from a
   macOS measurement" (Lua floor only). Fix: cut the sentence, or replace it
   with facts-07's wording for the Lua floor.
5. Line 289. "the integration gate writes `receipt-integration`." The file
   says the release contract "downloads the `receipt-quality` and
   `receipt-integration` artifacts" (facts-14 12.5) and that the `quality`
   job ends in a "receipt" (12.7). The `integration.yml` row (12.7) mentions
   no receipt. Fix: "the release contract also downloads a
   `receipt-integration` artifact".
6. Line 287. "A receipt records that a layer of proof ran and passed."
   Searched 16.6 and facts-14 12.5; neither defines what a receipt records.
   Fix: cut, or soften to what the file says: receipts form a chain in which
   "every layer [is] present, contiguous, and linked to its predecessor".
7. Footnote `16-quotes`, line 116. "a field typed as text would then fail
   the model." The file says only "Ambiguous strings ("3", "true", dates)
   are double-quoted" (16.7), with no consequence stated. Fix: cut the
   second clause, or end at "turn the string `3` into a number and the
   string `true` into a boolean".

## 2. Contradicted (severity: blocks)

1. Line 74: "A verify target rebuilds what it reads, so it can never bless
   last week's PDF." Echoed at line 176 ("The command line rebuilds before
   it verifies") and line 361 ("the registry's dependency edges make every
   verify target rebuild first"). The contradiction list says otherwise:
   "**`press verify-formats`** includes an existing, possibly stale,
   `dist/<slug>.pdf` in the cross-edition agreement check without rebuilding
   it" (20.B.11; also facts-07: "It does not rebuild the PDF, but it reads
   an existing `dist/<slug>.pdf` into the cross-edition agreement check").
   Corrected wording: "A verify target rebuilds the artifacts it verifies"
   (or the scar's own wording, "the CLI's dependency edges exist so that
   cannot happen", 19.8), and do not say "never" or "every". The PDF claim
   at line 74 must go: `verify-formats` does read last week's PDF.
2. Line 377: "A change that broke any of them stops the tag there." In the
   release sequence the immutable tag is pushed before the contract runs:
   "2. Immutable tag. Push the three-part tag. 3. Release contract. Wait for
   the `contract` check. On failure the major has **not** moved"
   (facts-14 12.5). The tag already exists when the checks fail. Corrected
   wording: "A change that broke any of them turns the release contract
   red, and the floating major does not move."

## 3. Drifted (severity: should)

1. Table 16.1, row "Registry". The file names the area "Graph" (16.1). If
   the book's vocabulary rule ("the registry", never "the graph") requires
   the rename, keep it; otherwise use "Graph". The writer flagged this.
2. Line 72: "`verify_archives` opens the two zips." facts-08: "`verify_archives`
   covers three files": the reader zip, the source zip, and the sources
   companion "when `config/authorities.yaml` exists". Fix: "opens the two
   zips and the sources companion".
3. Line 94: "`press selftest --write-docs` generates three documents". The
   file lists four outputs: "`docs/REFERENCE.md`, `docs/INVARIANTS.md`,
   `docs/PROVIDER-QUALIFICATION.md`, and the packaged provider record"
   (16.4). Fix: add "and the packaged provider record" (the `docs` check
   still covers the three documents).
4. Line 114, the secret regex. "It matches the words api key ..." The regex
   is `api[_-]?key`: it matches `apikey`, `api_key`, `api-key`, never "api
   key" with a space. "the opening line of an armored private key": the
   pattern is `-----BEGIN`, which matches any PEM armor line, not only a
   private key. Fix: "`api_key` and its spellings without or with a hyphen"
   and "any line beginning `-----BEGIN`".
5. Line 144: "in most shells, `CI=false` counts as set." The fact is about
   how code reads the value, not the shell: "because `CI=false` would read as
   truthy" (facts-08); "`CI=false` is truthy" (19.14). Fix: "a variable set
   to `CI=false` would still read as true."
6. Line 165: "The ledger states its reason for the fourth part". The file
   quotes the sentence under "Entry shape" (16.3) without saying the ledger
   is its source. Fix: "The press states its reason ..." or attribute to
   *docs/INVARIANTS.md* only if another source confirms it.
7. Line 235, tip: "A run from a book's environment skips every check that
   reads repository files." The file: "Repo-file checks are skipped from an
   installed wheel" (16.4). A book environment with an editable install of a
   press checkout is not an installed wheel. Fix: "A run from an installed
   wheel skips ..." (line 232 has the same slide, "the environment for
   *~/alice*"; tie it to the wheel).
8. Line 248: "The same directory holds *surfaces.yaml* and
   *known-bad.expected.yaml*." *surfaces.yaml* is confirmed in
   `.celebrimbor/` (20.A.3). For `known-bad.expected.yaml` the file gives no
   path (16.5), and facts-C/facts-06 name a different file,
   `src/press/data/known-bad/expected.yaml`. Fix: "The gate also holds
   `surfaces.yaml` and `known-bad.expected.yaml`", without placing the
   second.
9. Line 250: "The reason for the producer ledger is in *CONTRIBUTING.md*".
   The file presents the quotation as the gate's "stated philosophy
   (CONTRIBUTING)" (16.5), not as the producer ledger's reason. Fix: "The
   gate's philosophy, in *CONTRIBUTING.md*, ..."
10. Line 258: "Table 16.5 lists the press repository's workflows." The file
    lists ten (12.7); the table has six, omitting `codeql.yml`,
    `dependency-review.yml`, `roadmap.yml`, `repo-metadata.yml`. Fix: "lists
    the main workflows" or add the four rows.
11. Table 16.5, *toolchain.yml*: "for both architectures". The file says
    "the multi-arch image" (12.7). Fix: "a multi-architecture image".
12. Line 124: "and the receipt chain includes a layer named `boundary`."
    Placed after the gate sentence, it implies the `boundary` layer is the
    adapters gate's proof. The file names the layer only (facts-14 12.5).
    Fix: cut, or say only that the twelve receipt layers include one named
    `boundary`.

## 4. Missing (severity: may)

1. Table 16.1, Desk row: "These modules draw the desk" includes `events.py`.
   A developer reading the module map would want 16.6 / 20.B.17: it
   "defines a versioned child-event protocol ... Nothing emits it at
   runtime; the desk parses log text instead." One clause prevents a reader
   from wiring to a dead protocol.
2. With Contradicted 1: the `INV-graph-no-stale` limit should carry the
   `verify-formats` exception (20.B.11) wherever the chapter states the
   no-stale rule, since this chapter is where a developer learns it.

## Code blocks

- Example 16.1 (critical invariants): matches 16.3 name for name and in
  order.
- Example 16.2 (selftest checks): matches 16.4's 29 names and order.
  It is a reformatted list, not presented as captured output.
- Receipts CLI (line 296): matches facts-14 12.5 exactly.
- Example 16.3 (reference manifest): matches 15 key for key and value for
  value, comments removed as the lead-in says.
- Selftest success line (line 230, in prose): matches 16.4 character for
  character.

## Worst finding

Contradicted 1: line 74 says a verify target "can never bless last week's
PDF", and lines 176 and 361 repeat it. Section 20.B.11 records that
`press verify-formats` reads an existing, possibly stale, `dist/<slug>.pdf`
without rebuilding it.
