# STE80 editor report: Chapter 16, Inside the press

File: `book/chapters/16-inside-the-press.md`

## Ratchet count

- Before: 9 (baseline in `tools/ste-baseline.json`: 9)
- After: 0
- `press check`: passes (exit 0). Sentinel "the selftest skips the checks"
  intact. Index terms touched: "source zip" kept verbatim; "floating major"
  became "floating tag", the head term of the same index entry.

## Edits (line numbers are in the edited file)

1. L62, S2 (counter merge after a sentence opening with `@fig:`). Old: "@fig:end-to-end-data-flow draws the whole path for the Alice book." New: "For the Alice book, @fig:end-to-end-data-flow draws the whole path."
2. L74, S1. Old: "Pandoc reads each rendered file, runs its Lua filters over the manuscript, and hands the result to a writer." New: "Pandoc reads each rendered file and runs its Lua filters over the manuscript. Then it hands the result to a writer."
3. L74, S11 (vocabulary: edition names). Old: "The stitched Markdown and the source zip go to *dist/* without pandoc." New: "The Manuscript edition (the stitched Markdown) and the Source edition (the source zip) go to *dist/* without pandoc."
4. L76, S1. Old: "`verify_pdf` inspects the PDF, and `verify_formats` inspects the other editions and runs epubcheck on the EPUB." New: "`verify_pdf` inspects the PDF. `verify_formats` inspects the other editions and runs epubcheck on the EPUB."
5. L78, S1/S2 (29 words, three ideas). Old: "The command line enforces it through the dependency edges in the registry, so a verify target rebuilds the artifacts it verifies, with the one exception Chapter 8 names." New: "The command line enforces it through the dependency edges in the registry. A verify target rebuilds the artifacts it verifies, with the one exception that Chapter 8 names."
6. L82, S1. Old: "`print_safe` prepares the images, the build writes the print interior, and `verify_pdf --profile print` inspects it. Then `gen_coverwrap` draws ..." New: "`print_safe` prepares the images, and the build writes the print interior. `verify_pdf --profile print` inspects the interior. Next, `gen_coverwrap` draws ..."
7. L110-112, S13/S14 (procedure apart from description) and S1. The paragraph on the frozen `Book` mixed description and a procedure. Description now ends with the moved sentence "The model collects every problem before it reports, so one run lists them all." The procedure is its own paragraph. Old: "If you add a config field to the press, declare it in the model, with its type and its default, and in the CLI registry in *config_schema.py*." New: "If you add a config field to the press, declare it in the model with its type and its default. Declare it also in the CLI registry in *config_schema.py*."
8. L114, S10 (phrasal verb). Old: "Writes go through the same model." New: "Writes pass through the same model."
9. L114, S1 (three ideas; also the 45-word counter merge after a sentence opening with a path). Old: "*config_store.py* then writes a temporary file beside the original and moves it into place with `os.replace`, so a crash leaves either the old file or the new one." New: "Then *config_store.py* writes a temporary file beside the original. It moves the file into place with `os.replace`, so a crash leaves either the old file or the new one."
10. L226, S2 (31-word counter merge after a path opening). Old: "*tests/lua/* holds ..." New: "The directory *tests/lua/* holds ..."
11. L228-230, S14 (procedure apart from description). Split the paragraph after "because pandoc writes that tie itself." so the two-step coverage procedure ("To see the filters' coverage on `hatter`, ...") stands alone. No words changed.
12. L243 (Table 16.5, *docs-site.yml* cell), S1. Old: "It builds the example PDFs in the pinned image, builds the press's Web site with the headless Chrome layout check required, and deploys it." New: "It builds the example PDFs in the pinned image and builds the press's Web site with the headless Chrome layout check required. Then it deploys the site."
13. L295-297, S1 and S13 (the split would have made seven sentences). The manifest-key paragraph now splits into identity keys (`name`, `kind`, `provides`, `requires`) and obligation keys. Old: "`invariants` lists the invariants it takes on, `proofs` names a proof for each, and `capabilities` lists what it asserts." New: "`invariants` lists the invariants it takes on, and `proofs` names a proof for each. `capabilities` lists what it asserts."
14. L301-303, S13 (one topic per paragraph). Moved "The conformance gate refuses six faults, ..." from the end of the five-stages paragraph to open the hostile-fixtures paragraph, which is about the same gate. No words changed.
15. L303, S2 (45-word counter merge after path openings). Old: "*hostile/collision.yaml* claims `pdf`, ..." New: "Of the five, *hostile/collision.yaml* claims `pdf`, ..."
16. L303, S2 (same merge). Old: "*unproven.yaml* has `proofs: []`, ..." New: "The fixture *unproven.yaml* has `proofs: []`, ..."
17. L305, S1. Old: "The gate exists and the selftest runs it, but nothing yet reads a third party's manifest during a build." New: "The gate exists, and the selftest runs it. But nothing yet reads a third party's manifest during a build."
18. L307, S2 (36-word counter merge after a path opening). Old: "*config/cover-styles.yaml* and ..." New: "The files *config/cover-styles.yaml* and ..."
19. L315, S8 ("-ing" rider). Old: "*CLAUDE.md* carries the scar in its list, beginning "Verifying `dist/` without rebuilding blesses stale artifacts"." New: "In the scars list of *CLAUDE.md*, its entry begins "Verifying `dist/` without rebuilding blesses stale artifacts"."
20. L319, S1 (three actions in about 30 words). Old: "She clones the press, installs the clone in editable mode with its `dev` extra into the environment that her book already uses, and installs the pre-commit hooks. She then runs `press doctor` and `press selftest`, builds the whole book, and runs the local proof." New: "She clones the press and installs the clone in editable mode, with its `dev` extra, into the environment that her book already uses. Then she installs the pre-commit hooks. Next she runs `press doctor` and `press selftest`. Last, she builds the whole book and runs the local proof."
21. L346, S10 (phrasal verb). Old: "To look at rendered output while you tune ..." New: "To examine rendered output while you tune ..."
22. L366-368, S10 and S13. Split the template paragraph after "CI runs the selftest and the integration gate on every pull request." so the reporting channels stand apart. Old: "Defects and proposals go through the repository's issue forms." New: "Defects and proposals use the repository's issue forms."
23. L370, S11 (vocabulary: floating tag, never "major tag"). Old: "... and the floating major does not move." New: "... and the floating tag does not move."

## Leads declined

- L131, sidebar sentence "The desk launcher, which starts the targets you pick on the desk, used exactly that form, so it started processes from outside the boundary while the gate reported nothing." (29 words.) Light mode. I tried a split, but it took the sidebar to seven sentences, over the paragraph cap. The sentence is under the 30-word ceiling, so it stays.
- L303, "The conformance gate refuses six faults, each with a located reason: ..." (29 words). It is one idea with a list of six. Under the ceiling.
- L100 (Tip, 25 words), L346 ("To examine rendered output ...", 28 words), L354 (procedure step 3, 25 words). Each is under the ceiling, and a split would separate a condition or a purpose from its command.
- "-ing" leads on the headings "Contributing a scar" and "Submitting a change" and on *CONTRIBUTING.md*: a heading and a filename are never edited.
- L315 "The ledger entry names the enforcement, names its proof, and states its limit": a parallel list of the entry's parts, kept.
- L301 "It parses each with `load_manifest`, checks its conformance, and registers it.": these are stages of the five-stage list the sentence describes. A split would chop the sequence.

## Passives kept

- Table 16.1 / list item "driven by *src/press/mutation.py*": a participle with its actor named.
- No other agentless passives found in edited or unedited prose worth acting on.
