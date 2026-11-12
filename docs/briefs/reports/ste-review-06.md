# STE80 review: Chapter 6, Checking the manuscript

File: `book/chapters/06-checking-the-manuscript.md` (diff against HEAD, 18 edits).
Status: REVISE. Blocks 0, should 3. Accepted on judgment: 2 (items 4 and 5).
`press check` exits 0 on the edited tree. Ratchet: 3, under the baseline of 6.
No sentinel is in this file. No code span, command, path, flag, key, message,
quotation, or index term changed. Facts checked against `docs/briefs/facts/facts-06.md`.
Edit 10 ("It" to "The lint") is correct: facts 6.4 says the jargon lint skips
fenced code, inline code, URLs, and blockquotes, and `--include-quotes` is a lint flag.

1. **L231, term (should).**
   Old: "..., and `press skills` prints each installed skill with its path."
   New: "The `press skills` target prints each installed skill with its path."
   What went wrong: the editor added the word "target". `docs/vocabulary.md` defines
   a target as "a `press` command that builds, checks, or verifies". `press skills`
   does none of those. Chapter 15 (L277) calls it "the `press skills` command".
   Corrected: "The `press skills` command prints each installed skill with its path."

2. **L386, added "thus" (should, voice).**
   Old: "A Print edition shorter than the floor fails verification, so the floor catches a build that ran to the end and set only part of the book."
   New: "A Print edition shorter than the floor fails verification. The floor thus catches a build that ran to the end and set only part of the book."
   What went wrong: this is the only "thus" in the whole book. The contract keeps
   "however", "therefore", and "whether" for the period voice. It does not list
   "thus". Two sentences later the editor also added "therefore" (L388), so the two
   paragraphs of "The page floor" end on back-to-back connective sentences. The
   old sentence was 27 words, under the 30-word ceiling. It joined two linked facts
   with "so", and the contract allows that.
   Corrected (revert): "A Print edition shorter than the floor fails verification, so the floor catches a build that ran to the end and set only part of the book."

3. **L244, added "therefore" (should, voice).**
   Old: "The default is `rewrite`, and `press check` uses it, so an inspect term appears in the report and does not fail the check."
   New: "The default is `rewrite`, and `press check` uses it. An inspect term therefore appears in the report and does not fail the check."
   What went wrong: the chapter already had five "X therefore Y" sentences. These
   edits make seven, and this one sits 12 lines before the existing "The watchlist
   therefore asks a question" (L256). That is a uniform rhetorical pattern made
   by the edit. The facts are the same.
   Corrected (one link, two ideas): "`press check` uses the default, `rewrite`, so an inspect term appears in the report and does not fail the check."

4. **L388, added "therefore" (accepted, no change).**
   New: "The book model's default is 40, while the scaffold's template writes 1. A new book therefore builds and verifies before it has a second page."
   Judgment: "therefore" is a permitted connective and does the job the removed
   "so" did. Both numbers are kept. With item 2 reverted, it no longer stacks.

5. **L218, footnote marker moved mid-sentence (accepted, no change. Tool defect noted).**
   Old: "...against a list of overused engineering terms.[^6-twocopies]"
   New: "The fourth pass runs the *jargon lint*,[^6-twocopies] a separate program ..."
   Judgment: no words changed. The note reads "A second, identical copy of the lint
   lives in the overused-jargon skill". Facts 6.4 ("Two copies, one contract")
   confirms that the note is about the program. In the old position the note
   followed "a list of overused engineering terms", which is the watchlist. The
   watchlist also lives in the overused-jargon skill (L231). A reader could take
   the note to mean a second copy of the list, so the new position is more
   accurate. There is precedent for the placement: Chapter 1, L47,
   "the Libertinus fonts,[^1-libertine]".
   The editor's reason for the move is a counter defect, and the fix for it belongs
   in the tool, not in the text. `tools/ste_check.py` `sentences()` splits on
   `(?<=[.!?:])\s+`. A period followed directly by `[^label]` is not followed by
   whitespace, so the counter joins every sentence that ends in a footnote to the
   sentence after it. This happens across the whole book. Strip `[^...]` markers
   before the split. Do not move markers to satisfy the counter.

The other 13 edits (L54, L62, L75, L98, L118, L131, L149, L192, L227, L258,
L293, L365, L475) keep every fact, qualifier, and identifier at full strength.
No changes are needed.
