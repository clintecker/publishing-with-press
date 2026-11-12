# STE80 review: Chapter 13, Registrations

File: `book/chapters/13-registrations.md` (`git diff HEAD`, 8 hunks)

Status: **APPROVED**. Blocks: 0. Should: 0. Notes: 1 (no change required).

`press check` exits 0. None of the three sentinels occurs in this chapter. No code span, command, path, key, quotation, footnote marker, or index-term word changed in any hunk. Every paragraph got shorter.

## Findings

None that blocks or should be changed. Each edit was checked as follows.

1. Lines 17/19 and 19 (edits 1 and 2): paragraph split after "a serial carries an ISSN."; "It checks ... and writes them ... It also assembles ...". All three tasks survive. "also" keeps the press as the actor. Clean.
2. Lines 94/96 (edit 3): split before "The press knows only the two ISBNs". Sentences unchanged. Clean.
3. Line 106 (edit 4): ISSN mod-11 sentence split. 0378-5955 exact (facts 11.3). Clean.
4. Line 169 (edit 5, flagged by the editor). Old: "and you have set no registration yet." New: "and it holds no registration yet." The scaffold template's `registrations:` block in `config/metadata.yaml` is entirely commented out (press `src/press/data/template/config/metadata.yaml` lines 38-43), so the scaffold holds no registration. That is the same fact, and it is not stronger. "it" can only mean the scaffold. Clean.
5. Lines 196/198 (edit 6): split before "The fresh scaffold shows a different gap." Sentences and the `[^13-earth]` marker unchanged. Clean.
6. Lines 284/286 (edit 7): split before "The barcode carries only the print ISBN". Sentences unchanged. Clean.
7. Line 328 (edit 8, flagged by the editor). Old: "Once it is set, the checker refuses the book while either ISBN is absent or pending, or while a declared LCCN or ISSN is still pending." New: "Once you set it, the checker refuses the book while either ISBN is absent or pending. The checker also refuses the book while a declared LCCN or ISSN is still pending."
   - Actor: step 8 directly above says "Declare the retail edition" in the reader's voice (`press config set registrations.retail true`). "you" is accurate. Clean.
   - Condition (note): the retail condition now reaches the second sentence only through "also". Facts 11.4 say a pending number is advisory when `retail` is false, so the sentence on its own would overstate. Line 140 already uses the same "also" construction for the same LCCN/ISSN rule, and line 138 says plainly that `false` produces only advice. In this context "also" carries the condition, so no change is required. If the editor wants it explicit, the corrected sentence is: "With the flag set, the checker also refuses the book while a declared LCCN or ISSN is still pending."

## Voice and terms

No Light-mode passage was edited. The sidebar "Why pending is a word" is untouched, and declining it was correct. The splits do not make a run of same-length sentences. The two-sentence paragraph at line 196 ("A field with no value ... before the Library sees it on the form.") keeps its point. No term changed against `docs/vocabulary.md`.
