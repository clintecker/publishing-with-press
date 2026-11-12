# STE80 review: Chapter 8, Verifying the artifacts

File: `book/chapters/08-verifying-the-artifacts.md`, diff against HEAD
(26 edits, all read hunk by hunk).

Status: REVISE. Blocks: 1. Should: 1.

1. **L192, attribution lost (blocks, Facts).**
   Old: "The press's own notes record that a missing `pdfimages` softens two checks to notes in this way, and `press doctor` does not check for the tool."
   New: "The press's own notes record that a missing `pdfimages` softens two checks to notes in this way. The `press doctor` command does not check for the tool."
   What went wrong: in the old sentence both facts sat under "record that", so the doctor fact was the press's notes speaking. The split leaves the second sentence with no source, and it now reads as the author's own assertion. The certainty is the same; the warrant moved from the press to the author.
   Corrected: "The press's own notes record that a missing `pdfimages` softens two checks to notes in this way. They also record that `press doctor` does not check for the tool."

2. **L321, "keying on `CI`" became "a test of `CI`" (should, Terms).**
   Old: "The press's source gives the reason: keying on `CI` would fail"
   New: "The press's source gives the reason: a test of `CI` would fail"
   What went wrong: `docs/vocabulary.md` lists "test" as a forbidden name for a verifier, and this sentence sits in the verifier chapter beside the epubcheck strictness check, so "a test of `CI`" reads as a verifier that tests CI, or a test run of CI. The press's source says the decision "keys on" the variable (`verify_formats.py:408`); the new phrase loses "basing the decision on" and keeps only "inspecting". The two sentences before it already use "read", which gives a clean replacement.
   Corrected: "The press's source gives the reason: a decision based on `CI` would fail "because `CI=false` would read as truthy"."

## Passed on the four hard checks

- **L144 (renderer).** "Unless a helper renderer is present, the verifier renders every page to a PNG image at 120 dots per inch with `pdftoppm -png -r 120`." The "Unless" clause opens the sentence and governs the whole main clause, 120 dpi included, so the sentence says nothing about the helper's resolution. This matches the old sentence, where the trailing "unless" governed the same span. (The press's `verify_pdf.py:343` does pass `--dpi 120` to the helper too, so a reader who inferred it would not be misled. The fact file does not state it, and the sentence does not claim it.) Condition-first is correct. No finding.
- **L247 (Table 8.3, Circulating).** "When the book has a registered ISBN, the package must also carry it in the form `urn:isbn:` and the number." The condition is unchanged ("when the book has one" equals "when the book has a registered ISBN"), "must" keeps its strength, and `urn:isbn:` is verbatim. It matches facts-08 (`EPUB metadata is missing the registered ISBN <isbn>`). The cell is still one table row. No finding.
- **L192** and **L321**: findings 1 and 2.

## Other hunks

All other edits (L17, L25-27, L65, L69, L74, L84-86, L132, L139, L146, L154, L173, L185, L210, L266, L276, L298 x2, L341, L420, L487, L493-495, L513) keep every fact at its strength. Notes:

- L17 "user `alice`'s full novel" is the vocabulary entry word for word; "She" agrees with "her first sentinel" at L487.
- L139 is a sidebar (Light mode). The old sentence held three ideas at 28 words, so the split is a permitted fix. The blockquote is still one block.
- L493-495: the four causes now span two paragraphs (5 and 4 sentences). The topic sentence still governs both. "so run" became "Run": the imperative is unchanged in force.
- L513 footnote: "In most" kept.

## Verbatim and markup

- Sentinel "You do not choose the witness" is byte-identical (in "You do not choose the witness: the press finds it") and occurs once (HEAD: once). The other two sentinels do not occur in this file, before or after.
- Every code span, every double-quoted string, and every footnote label is identical between HEAD and the working tree (sorted multiset diff, empty).
- `press check`: exit 0. `tools/ste-ratchet.py --report`: 0 for this file.
- No paragraph over 190 words (largest is the sidebar at 152, unchanged in length class). No blockquote split.

## Outside the editor's diff (not counted)

- L321's quotation "because `CI=false` would read as truthy" is not verbatim from the press's source, which reads "CI=false would read truthy" (`src/press/verify_formats.py:409-410`, no "because", no "as"). This predates the STE pass and is carried in facts-08 line 67. It is a quotation-fidelity defect for the copyeditor or fact desk, not this review.
