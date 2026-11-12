# STE80 review: book/chapters/04-writing-the-manuscript.md

Status: APPROVED (0 blocks, 1 should).

Scope: `git diff HEAD -- book/chapters/04-writing-the-manuscript.md`, all
20 edits in `docs/briefs/reports/ste-04.md`, read hunk by hunk against
`docs/briefs/facts/facts-04.md` and, for the tie lists, the filter itself
(`src/press/data/lua/typographic-spacing.lua` in the press checkout).

## Findings

1. Line 101 (the sentence moved out of the figure paragraph).
   - Old: "For a chapter or a section, write the reference in words: "see Chapter 6, *Checking the manuscript*"."
   - New: "Press has no machinery for citing chapters or sections. Write such a reference in words: "see Chapter 6, *Checking the manuscript*"."
   - What went wrong: "such a reference" has no noun to point back to; the
     previous sentence says "citing", not "reference". The old sentence named
     its object. No fact changed (facts-04: "There is no chapter or section
     cross-reference mechanism"), and the move itself is sound: the figure
     paragraph still closes on "Chapter 5 ... covers figure identifiers in
     full", and the new paragraph keeps the limitation and the remedy together.
   - Severity: should (S11, unclear reference).
   - Corrected: "Press has no machinery for citing chapters or sections. Write a reference to a chapter or a section in words: "see Chapter 6, *Checking the manuscript*"."

## Checked hardest, no finding

- Line 420, honorifics. The old text was "for Mr., Mrs., ..., and Fr." with
  no "such as": a closed list. facts-04 §4.7 gives the same 17 titles, and
  the filter's `TITLES` table holds exactly those 17. "The honorifics are"
  is faithful. The reference forms were open-ended ("for forms such as"),
  and facts-04 and the filter's `REFS` add § and ¶; the editor wrote "The
  reference forms include", which keeps the list open. Both lists are
  byte-identical to the old text.
- Line 426. "so press needs no pandoc-crossref" became "Press therefore
  needs no pandoc-crossref." Same causal claim, same strength; facts-04:
  "There is no pandoc-crossref dependency. The number is computed once by
  `figure-numbering.lua`." "therefore" is period-correct under
  `docs/prose-contract.md`. "Press" capitalized at sentence start matches
  the chapter's usage.
- Lines 99-101. No fact lost: figures are numbered and cited by name, the
  unknown-identifier behaviour, the Chapter 5 pointer, and the
  chapter/section limitation with its in-words remedy are all present.
  Only the "but" contrast became a paragraph turn.

The other 17 edits are clean splits or reorders: no qualifier dropped, no
code span, path, key, or message altered, "it" referents intact (line 250
now names "inline code", which is what the old "it" meant).

## Mechanical

- Sentinels, each counted across `book/`: "You do not choose the witness"
  1 (ch. 08), "On a fresh scaffold it succeeds" 1 (ch. 01), "the selftest
  skips the checks" 1 (ch. 16). All byte-identical to
  `config/metadata.yaml`; none lives in chapter 4.
- No `config/authorities.yaml` exists, so no claim fragment can break.
- Longest paragraphs: a table (162 words) and the sidebar blockquote (164),
  both unchanged and under 190. No blockquote split.
- `press check` exits 0 (source, checker self-test, editorial, jargon).
