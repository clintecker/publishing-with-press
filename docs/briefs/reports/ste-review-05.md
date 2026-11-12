# STE80 review: Chapter 5, Figures, plates, and illustrations

File: `book/chapters/05-figures-and-plates.md`
Diff: `git diff HEAD -- book/chapters/05-figures-and-plates.md` (19 edits, 6 paragraph splits)

Status: REVISE (one should, no blocks)

Counts: blocks 0, should 1.

Method: every hunk read old against new, word by word (`--word-diff`).
Facts checked against `docs/briefs/facts/facts-05.md` (style precedence
L108, arm64 resample L188, `tex/title-page-print.tex` L76). Terms checked
against `docs/vocabulary.md`. `press check` run on the edited tree: source,
checker self-test, editorial, and jargon passes all passed. Every split adds a
blank line only. No paragraph exceeds 150 words. No code span, path, flag,
identifier, quotation, number, heading, image line, art comment, or fig-alt
changed. No sentinel occurs in this file.

## Findings

1. **L276 to L278 (edits 13 and 14, the three-way split), structure.**
   Old (one paragraph): "... The Circulating, Single-leaf, and Chapter
   editions get an ordinary link to the figure's identifier. A plate gets no
   number anywhere, and in the PDF its entry goes into the List of Plates.
   @fig:where-a-figure-lands traces the image line of Example 5.2 into each
   rendered edition."
   New (third paragraph): "A plate gets no number anywhere. In the PDF its
   entry goes into the List of Plates. @fig:where-a-figure-lands traces the
   image line of Example 5.2 into each rendered edition."
   What went wrong: the split strands the cross-reference to Figure 5.3 at
   the end of a paragraph whose topic is plates. Example 5.2 is the numbered
   `.chart` figure, and Figure 5.3 traces its number, link, and list entry
   through every edition. Read in its new paragraph, the sentence seems to
   say that the plate's path is the one traced. In the old paragraph it
   closed the whole number-and-link discussion. This breaks the
   one-topic-per-paragraph rule that motivated the split.
   Severity: should.
   Corrected: put the cross-reference in its own paragraph directly before
   the image line, and leave the plate paragraph with two sentences:

   > A plate gets no number anywhere. In the PDF its entry goes into the List of Plates.
   >
   > @fig:where-a-figure-lands traces the image line of Example 5.2 into each rendered edition.

## Hardest-checked lines (editor's flags), cleared

- **L18 (edit 1).** "a plate changes sides" became "A plate can also
  change sides". In the old sentence, "or" joined the three costs as
  alternatives, so each was already a possibility. "can" keeps that
  strength and does not weaken a certainty. "also" turns the third
  alternative into an addition, and the meaning does not change. Cleared.
- **L81 (edit 6).** Precedence stays `--style`, then `style=`, then
  `plates.style`, then `wood-engraving`, which matches facts-05 L108.
  "Third comes" matches the existing "Last comes". The italic first use of
  *aesthetic* and its gloss are intact. Cleared.
- **L379 (edit 19).** The condition still comes before the requirement
  ("If it does, ... must come from"). "must" keeps its strength. Both paths
  are verbatim. The parenthetical gloss is kept word for word as an
  appositive. "A book can supply" states what the old "If the book
  supplies" already presupposed, so it adds no fact. Cleared.

## Considered and not raised

- L298 (edit 16): "so" was dropped between "meets the line before it meets
  the cap" and "prints at the full width". The paragraph's topic sentence
  ("the limit that binds first sets the size") still states the cause, and
  the next sentence about the tall image has the same structure. No loss.
- L278: "In the PDF its entry" has no comma, but the sentence before it in
  L276 has "In the PDF, the citation". This is a style difference, not a
  defect.
- L354 (edit 18): "Resampling only ever goes down." is now a short
  sentence between two longer ones. That improves the rhythm, and the facts
  match facts-05 L188.
