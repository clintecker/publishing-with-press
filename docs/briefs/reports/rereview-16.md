# Re-review: Chapter 16, Inside the press

File: `book/chapters/16-inside-the-press.md` (revised, 5,679 words by the
writer's count). Read against the four desk reports, the Revision section
of `report-16.md`, the production ledger's rulings, and facts-16 S1 to S4.
Line numbers are `cat -n` numbers in the file as it stands.

## Verdict

**APPROVED.** No open blocks. Two open shoulds (copy 20, dev 6), both
one-sentence fixes, listed below for the writer or the continuity pass.

## Checks run

- `press check`: fails only on source checks naming Chapter 12's plates
  (`12-01-cover-wrap-anatomy.png`, `12-02-spine-math.png` never
  referenced). Not this chapter's. Nothing names chapter 16.
- `tools/ste_check.py`: 44 findings (414 sentences, mean 11.8 words). All
  judged residual: passives inside quotations (27, 78, 167, 226);
  sentence and paragraph lengths in the box, fig-alt lines, `art:`
  comments, the index comment, and sentences the counter merges at
  filename dots (114, 230, 313, 317); `-ing` forms in headings, art
  comments, and the file name *CONTRIBUTING.md*; "verify" as the target
  and script name; "go through" and "look at" (plain); the semicolon in
  the index comment. The 25-word Tip at 102 was accepted at copyedit.
- Fences: three, all `text`; no code line over 64 columns. ASCII only.
- Footnotes: four, all `16-` labels (16-epoch, 16-quotes, 16-macos,
  16-main).
- Figures: each `art:` comment follows its image line after one blank
  line (54/56, 64/66, 260/262). Art plus image line: 173, 186, 164 words.
- Sidebar: six sentences, one paragraph, about 125 words.
- American spelling: "labeled", "canceled", "centered"; no "labelled",
  "centred", "cancelled", "colour", "behaviour".
- Vocabulary: "lands" absent; "artifact graph" absent as a name (only
  the sealed capability id `artifact-graph`, which is code); "the
  graph" absent; "three-part tag" absent ("immutable tag" at 266, 378,
  380); "guarantee" only inside the ledger quotation (167); "the Alice
  book" at 62; edition names are press's and glossed by writer at 74;
  no logomark mention, so that ruling does not bite.

## The Chapter 12 continuity note (edition manifest and receipt digests)

The claim is no longer in the chapter. Line 291 is now the reference
extension manifest (`name: acme-quarto`), and "edition manifest" appears
only as a Table 16.1 cell and in `INV-edition-manifest`. No action. For
the record: facts-14 section 12.5 does not say it, but the facts-14
module notes do ("`receipts.py` ... also yields the edition manifest's
receipt digests", facts-14 line 218), so the claim was supported by the
fact base if anyone restores it.

## Findings

| Desk | No. | Sev. | Status | Note |
|---|---|---|---|---|
| facts | Unsupported 1 | blocks | resolved | 126 and sidebar: a gate for direct process calls; warning 149 keeps the three-module rule as the package's own words and claims refusal only for process calls. |
| facts | Unsupported 2 | blocks | resolved | 134 begins "When an external tool fails, the press unwraps..." |
| facts | Unsupported 3 | blocks | resolved | 112 ends "so one run lists them all"; description/slug example cut. |
| facts | Unsupported 4 | blocks | resolved | Warning 235 carries only the S1 rules. |
| facts | Unsupported 5 | blocks | resolved | 266: the release contract downloads both receipts; no producer named. |
| facts | Unsupported 6 | blocks | resolved | 256 defines receipts as the records receipts.py keeps for each layer; 264 quotes the chain wording. |
| facts | Unsupported 7 | blocks | resolved | Footnote 16-quotes ends at the boolean. |
| facts | Contradicted 1 | blocks | resolved | 78 "rebuilds the artifacts it verifies" plus the verify-formats exception; 178 and Warning 181 carry it; 325 no longer says "every". See note 1. |
| facts | Contradicted 2 | blocks | resolved | 378: the script pushes the immutable tag, then the contract waits for `quality`, `consumer`, `desk`; a red contract leaves the floating major unmoved (facts-14 12.5 steps 2 to 4). |
| facts | Drifted 1 | should | declined-accepted | "Registry" kept by the vocabulary ruling. |
| facts | Drifted 2 | should | resolved | 76. |
| facts | Drifted 3 | should | resolved | 98, four outputs, `docs` check on three documents. |
| facts | Drifted 4 | should | resolved | Regex detail cut; 116 states the rule broadly and its consequence. |
| facts | Drifted 5 | should | resolved | 146. |
| facts | Drifted 6 | should | resolved | 167 "The press states its reason". |
| facts | Drifted 7 | should | resolved | Tip deleted; 214 ties the skip to an installed wheel. |
| facts | Drifted 8 | should | resolved | 228 places *surfaces.yaml* in *.celebrimbor/*, leaves *known-bad.expected.yaml* unplaced. |
| facts | Drifted 9 | should | resolved | 226 "The gate's philosophy". |
| facts | Drifted 10 | should | resolved | 238 and caption "main workflows". |
| facts | Drifted 11 | should | resolved | Table 16.5 toolchain row. |
| facts | Drifted 12 | should | resolved | `boundary` sentence cut. |
| dev | 1 | should | resolved | Example 16.3 (activate, clone, `pip install -e '.[dev]'`, `pre-commit install`, `press doctor`, `press selftest`, `press all` in *~/alice*, `scripts/verify.sh`), verify ladder and dev-render (S1, S4), and "Submitting a change": pull request template, issue forms, private security reports; direct pushes described as the maintainer's (S2 ruling). |
| dev | 2 | should | resolved | 214. |
| dev | 3 | should | resolved | 27 lists the four laws in order; cited by number at 78, 90, 321, 323. |
| dev | 4 | should | resolved | Integration gate defined at 25. |
| dev | 5 | should | resolved | Release witnesses and `PRESS_RELEASE` at 110, pointing to Ch. 14. |
| dev | 6 | should | **open** | See open item 2. The fact base does say where a field is declared (facts-03 3.3: two sources). |
| dev | 7 | should | declined-accepted | The fact base names no adapters helper; nothing to name. |
| dev | 8 | should | resolved | 224, 230, 232 (S3); "Lua coverage floor" throughout. |
| dev | 9 | should | resolved | CLI block cut; `assemble` kept at 266. |
| dev | 10 | should | resolved | 220 "counts them separately", the "separate registrations" equivalent. |
| dev | 11 | should | resolved | Bypass arrow in the 16.2 directive. |
| dev | 12 | should | resolved | 114, 116. |
| dev | 13 | should | resolved | Example cut; the 13 names in prose at 184. |
| dev | 14 | should | resolved | 210 points back. |
| dev | 15 | should | resolved | Table row kept, sentence cut, minor rows dropped. |
| dev | 16 | should | resolved | 317, grouped prose with chapters. |
| dev | 17 | should | resolved | Example 16.3. |
| copy | 1 | blocks | resolved | 76 "The press writes every edition". |
| copy | 2 | blocks | resolved | Closer gone; 309 ends on "must never claim one". |
| copy | 3 | blocks | resolved | Closer gone; 321 ends on the ROADMAP quotation. |
| copy | 4 | should | resolved | Sentence gone. |
| copy | 5 to 15 | should | resolved | 23, 52, 54, 58, 72, 84, 96, 78, footnote 118, 124, boundary sentence cut. |
| copy | 16 | should | resolved | By ruling: sidebar held to six sentences (125 words). |
| copy | 17, 18 | should | resolved | 134, 188. |
| copy | 19 | should | resolved | Tip deleted. |
| copy | 20 | should | **open** | First sentence split; second still joined. See open item 1. |
| copy | 21 to 31 | should | resolved | 220, 228, 252, 256, 264, 266/378/380, 307, 311, 315, 323 and step 2, 378. |
| copy | 55 (fact) | - | resolved | 311 six refusals; 313 five fixtures named one for one, no sixth claimed (facts-16 15 lists five). |
| copy | 56 (fact) | - | resolved | As dev 10. |
| type | 1 | should | resolved | Moot; the example is gone. |
| type | 2 | should | declined-accepted | Manifest kept whole (the fields paragraph walks every key); the typesetter's fix was conditional on the page break after figures land. Re-check on the next PDF build (the current *dist/* PDF predates the revision, so I did not judge the break). |
| type | 3 | should | resolved | Separator 20/48/36; Meaning cells shortened. |
| type | 4 | should | resolved | `latexmk (pdf, print)`; side branches in one row; CI tail one box; directive plus image 186 words. |

Note 1, the no-stale exception. The exception is named at 78 and at
178/181. At 325 the chapter no longer states the rule as universal (it
says the guard lives in the dependency edges and quotes the ledger's
limit), so nothing contradicts the fact base. If the editor wants the
exception literally in the third place, add "and `press verify-formats`
is the one target that reads an existing PDF" after "the command-line
path only". Optional; not counted.

## Open items

1. Copy 20 (should). Line 218: "It needs Python 3.11 or later, and no
   book installs it."
   Fix: "It needs Python 3.11 or later. No book installs it."

2. Dev 6 (should). Line 108: "`press config list` prints every field
   with its type and a one-line description, which is the quickest way
   to see what the model declares." and line 112: "If you add a config
   field to the press, add it to the model with its type and its
   default, and read it from the `Book` everywhere."
   facts-03 section 3.3: "There are two sources. The typed model lives
   in `src/press/bookmodel.py` and `booklib.py`. The CLI registry lives
   in `src/press/config_schema.py`; `press config list` output is
   verbatim in §17." So `press config list` prints the CLI registry,
   not the model, and a developer adding a field who follows line 112
   will miss *config_schema.py*. In a chapter about stating each fact
   once, the reader needs to know there are two declarations.
   Fix at 108: "`press config list` prints every field that the CLI
   registry in *config_schema.py* declares, with its type and a
   one-line description." Fix at 112: "If you add a config field to the
   press, declare it in the model with its type and its default and in
   the CLI registry in *config_schema.py*, and read it from the `Book`
   everywhere." (Do not claim a check keeps the two in step; the fact
   base does not say one does.)

## Read as the developer

The path now holds: map, flow, the four laws by number, the model, the
boundary, the ledger, the selftest, the gate, receipts, extensions, then
a working setup and a submission route. Example 16.3 runs as written
from the environment Chapter 2 builds (*~/.press-venv*, facts-02), and
the `press doctor` ready line matches facts-02/08. The close follows from
"Submitting a change": an outsider opens a pull request, the maintainer
pushes `main`, and the tag is where the checks stop a release. The only
place I stalled was open item 2.
