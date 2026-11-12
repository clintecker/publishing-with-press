# STE80 review: Chapter 12, The print pack

File: `book/chapters/12-the-print-pack.md`, diff `git diff HEAD`.
Status: REVISE. Blocks: 0. Should: 2.

All 24 edits in `docs/briefs/reports/ste-12.md` read hunk by hunk against
the fidelity rules, `docs/prose-contract.md`, `docs/vocabulary.md`, and
`docs/briefs/facts/facts-12.md`. No code span, command, path, flag, key,
message, quotation, or identifier changed (every code span on a `-` line
reappears on a `+` line). None of the three sentinels occurs in this file.
The sidebar "The barcode that crowded its quiet zone" is untouched.
`press check` exits 0. `python3 tools/ste-ratchet.py` exits 0. Every
paragraph split keeps every sentence, and no paragraph grew.

Points the desk was asked to check hardest, all cleared:

- **L88, "The file".** "The file *docs/PROVIDER-DATA.md* gives the rule"
  adds a noun that names what the path already is. No fact added.
- **L159, "also".** facts-12.md (Release gate) says the gate builds
  `print` and `coverwrap` at the end of `press all`. "Also" restates the
  old "and"; the gate does build the pack in addition to its own targets.
  No fact added. "Step" was in the old text and is outside this desk.
- **L388, "there".** "You copy it from there for the record" carries the
  old "that is where you copy it from". facts-12.md S3 permits "the full
  value lives in the manifest file the gate writes". No change of mood or
  strength.
- **L225, Chapter 11 pointer.** "covers the making of" to "tells how to
  make" keeps the scope. Chapter 11 does tell how: its "Covers" section and
  the commission, accept, and finish commands. Verb for noun, S8. Clear.
- **L252, Warning.** Split into "...well formed." and "Nobody can
  correct...". Both claims keep their strength ("only", "Nobody"). The
  Warning still opens with the instruction, stays one blockquote inside one
  `{.warning}` div, and is three sentences.
- **Footnotes, L504-510.** Only blank lines were added. The four labels
  (`12-allowance`, `12-ingram`, `12-kdpdate`, `12-adapter`) are
  byte-identical to HEAD, in the same order, and each is defined once and
  referenced once. Blank-line-separated definitions are standard pandoc
  footnote syntax, as in Chapter 7. `press check` has no footnote rule of
  its own; the pairing was checked by script.

## Findings

1. **"therefore" added three times in one chapter (edits 1, 4, 13).
   Severity should (voice).**
   The chapter held 3 "therefore"s at HEAD and holds 6 now. Two of the new
   ones land a few lines from an old one: L72 (new) beside L78 (old), and
   L137 (new) beside L143 (old). The connective becomes a tic. The
   prose contract lets "therefore" stay where it stood; it does not ask
   for more. Keep edit 1's. Drop the other two; the cause stays clear from
   the sentence before.
   - Edit 4, old: "...both read `print.paper`, so a white book and a cream
     book get different spines at KDP, at IngramSpark, and on the house
     provider."
     New: "...both read `print.paper`. A white book and a cream book
     therefore get different spines at KDP, at IngramSpark, and on the
     house provider."
     Corrected: "The `constant` shape and the `ppi-table` shape both read
     `print.paper`. So a white book and a cream book get different spines
     at KDP, at IngramSpark, and on the house provider."
   - Edit 13, old: "...on the outer edge, so for the house example
     *assets/cover.jpg* fills 6.125 by 9.25 inches."
     New: "For the house example, *assets/cover.jpg* therefore fills 6.125
     by 9.25 inches."
     Corrected: "For the house example, *assets/cover.jpg* fills 6.125 by
     9.25 inches."

2. **L105, edit 3: the new sentence's "It" now reads as the house provider.
   Severity should (clarity of reference).**
   Old: "That makes it a sound default for a book with no shop chosen yet,
   and it also means the house spine is no real provider's spine."
   New: "That makes it a sound default for a book with no shop chosen yet.
   It also means that the house spine is no real provider's spine."
   What went wrong: in the old sentence "it" continued "That" (the fact
   that the house provider is KDP with zero allowance). Standing at the
   head of its own sentence, "It" takes the nearest noun, the house
   provider ("it" in "makes it"), and a provider does not "mean". No fact
   changed.
   Corrected: "That makes it a sound default for a book with no shop chosen
   yet. That also means that the house spine is no real provider's spine."

## Outside this pass: Table 12.9, the `kdp` row (L406)

The defect predates this pass. HEAD (`git show
HEAD:book/chapters/12-the-print-pack.md`, line 406) has the identical row,
and `git log -S` puts it in the chapter's first commit, e615e38 "Chapter
12: The print pack". The diff does not touch the table.

The row drops the opening quote on the second, third, and fourth items. The
source is `CHANNELS["kdp"]["manual"]` in press's `src/press/publish.py`
(lines 24-27), four separate strings. The `ingram` row below it already has
the right form. The correct row is:

    | `kdp` | "KDP account with tax interview completed", "Category selections (2 allowed; note 10 keyword slots)", "Pricing per marketplace and royalty option (60% print)", "Order a physical proof before approving publication". |

The semicolon is inside a verbatim quotation of the press's own string, so
it stays. Not fixed here (a quotation, and outside the desk); it belongs to
a copyedit pass.
