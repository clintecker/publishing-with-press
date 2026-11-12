# STE80 review: Chapter 2, Installing press

File: `book/chapters/02-installing-press.md`, diff `git diff HEAD`.
Status: REVISE. Blocks: 0. Should: 4.

All 14 edits checked against the fidelity rules, `docs/vocabulary.md`, and
`docs/briefs/facts/facts-02.md` (item 6, "The composite action installs press
from its own checkout, never pip-from-git"). No code span, command, path,
flag, quotation, or index term changed. The sentinels do not occur in this
file. The sidebar "The first-run font scan" is untouched. `press check`
passes. No paragraph grew, and both paragraph splits (edits 5 and 12) keep
every sentence.

## Findings

1. **Release contract definition (edit 9, line 222).** Severity: should (Terms; also flow).
   - Old: "It runs the same toolchain image, pinned by the same digest, that the press's *release contract*, the workflow that proves each press tag, proved."
   - New: "It runs the same toolchain image, pinned by the same digest, that the press's *release contract* proved. The release contract is the workflow that proves each press tag."
   - What went wrong: `docs/vocabulary.md` line 5 requires the first use to be italic "and defined in the same sentence". The next sentence does not satisfy it. The inserted definition also sits between "trust `printshop`. It runs ..." and "Then run the same build in the toolchain image on `hatter`", so "Then" now follows a definition instead of the advice it continues. No fact changed.
   - Corrected sentence: "It runs the same toolchain image, pinned by the same digest, that passed the press's *release contract*, the workflow that proves each press tag." (24 words; the appositive closes the sentence instead of nesting inside the relative clause, and "Then run ..." follows it directly.)

2. **The epubcheck choices (edit 14, line 383).** Severity: should (Voice; the either/or weakened).
   - Old: "Install it with Homebrew or apt as Examples 2.4 and 2.5 show, or accept the local warning and let the toolchain image run the strict gate."
   - New: "Install it with Homebrew or apt, as Examples 2.4 and 2.5 show. You can also accept the local warning and let the toolchain image run the strict gate."
   - What went wrong: the lead sentence promises "two choices". "You can also" reads as an addition to the first choice, not the alternative to it, and the second choice changes from an instruction to a permission. The old "or" marked them as exclusive.
   - Corrected sentences: "The first is to install it with Homebrew or apt, as Examples 2.4 and 2.5 show. The second is to accept the local warning and let the toolchain image run the strict gate."

3. **EPUB fault cost (edit 8, line 192).** Severity: should (Voice; understatement flattened).
   - Old: "An EPUB fault that you see on your own machine costs you a minute, and the same fault that you first see in CI costs you a round trip."
   - New: "An EPUB fault that you see on your own machine costs you a minute. The same fault costs you a round trip when you first see it in CI."
   - What went wrong: the old sentence was a balanced pair whose weight fell on "a minute" and "a round trip". The split moves the condition after the result (against S3) and ends the paragraph on "in CI" instead of the cost. Facts, including "first", are intact.
   - Corrected sentences: "An EPUB fault that you see on your own machine costs you a minute. When you first see the same fault in CI, it costs you a round trip."

4. **Pronoun across the new paragraph break (edit 12, line 331).** Severity: should (Markup-adjacent readability).
   - Old: (one paragraph) "... An edit to the press's source therefore takes effect on the next run with no reinstall. With no arguments, it builds the PDF of the press's own three-chapter Alice example."
   - New: the split puts "With no arguments, it builds the PDF ..." at the head of a new paragraph.
   - What went wrong: "it" now opens a paragraph, and the last subject before it is "An edit to the press's source". Its antecedent, "The script", is two sentences back and across the break.
   - Corrected sentence: "With no arguments, the script builds the PDF of the press's own three-chapter Alice example."

## Flagged edits judged sound

- **Composite action (edit 4, line 136).** Facts kept: the workflow runs the action to install press; the action is part of the press; it installs from its own checkout, never with pip from Git (matches facts-02 item 6 word for word). The italic first use still carries its definition in the same sentence ("a piece of the press itself", with "To install press" stating its job). "its own checkout" has a clear antecedent. Approved. Note, outside this diff: "reusable workflow" is used here at line 136 but italicized and defined only at line 293; that predates this pass.
- **Edits 1, 2, 3, 5, 6, 7, 10, 11, 13:** no fact, qualifier, or verbatim material changed. Edit 3 drops "also" and turns "You can ... by naming" into "To ..., name"; the preceding sentence already gives the other form, so nothing is lost. Edit 6 adds "Then"; the old series already read as a sequence. Edit 10's "There," scopes the case to the figure, which is what the colon did.

## Worst finding

Finding 1: the release-contract definition no longer meets the vocabulary rule, and it splits "trust `printshop`" from "Then run the same build".
