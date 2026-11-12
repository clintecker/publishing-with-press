# STE80 review: Chapter 16, Inside the press

File: `book/chapters/16-inside-the-press.md`, reviewed against
`git diff HEAD`, `docs/briefs/facts/facts-16.md`, and `docs/vocabulary.md`.

Status: APPROVED. Blocks: 0. Should: 1.

Checks run: `press check` exits 0. `tools/ste-ratchet.py --report` gives 0
for the chapter. No prose paragraph exceeds 150 words. The sentinel "the
selftest skips the checks" is byte-identical to HEAD and occurs once (L210).
The other two sentinels are not in this chapter.

Items checked hardest, no finding:

- "The model collects every problem before it reports, so one run lists them
  all." Moved unchanged into the description paragraph. The fact stays at its
  strength. The previous paragraph is at six sentences, so this is the only
  description paragraph that can take it.
- The frozen-`Book` split. The procedure keeps both declarations (model with
  type and default; CLI registry in *config_schema.py*), "Then read it from
  the `Book` everywhere", and "Never read the raw YAML a second time".
- "The conformance gate refuses six faults, ..." Moved unchanged. It now
  introduces "the gate" in the paragraph that uses it. All six faults and
  all five fixtures match facts-16 (Refusals, Hostile fixtures). "Of the
  five" refers correctly to the five fixtures.
- "floating major" to "floating tag". Chapters 1, 2, and 14 define a floating
  tag as the tag that names a major (`v3`). The book has no other kind of
  floating tag, so "the floating tag does not move" says the same thing. The
  index term `floating tag` lists "floating major" as a match and has many
  other hits, so no zero-hit index failure is possible.
- Edition names (L74). "The Manuscript edition (the stitched Markdown)" and
  "the Source edition (the source zip)" are the vocabulary names, glossed
  once, on their first use in the chapter. "source zip" stays verbatim.
- The four new openings: L62 "For the Alice book, @fig:..." (mid-sentence
  references occur in Chapters 7, 8, 10, and 15 too), L226 "The directory",
  L303 "Of the five," and "The fixture", L307 "The files". No path changed.
  No fact added.

## Findings

1. L315, edit 19.
   - Old: "*CLAUDE.md* carries the scar in its list, beginning "Verifying
     `dist/` without rebuilding blesses stale artifacts"."
   - New: "In the scars list of *CLAUDE.md*, its entry begins "Verifying
     `dist/` without rebuilding blesses stale artifacts"."
   - What went wrong: "its" has no clear antecedent. The nearest candidates
     are *CLAUDE.md* in the same clause and "The ledger entry" in the
     sentence before, and neither is the scar. The old sentence said that
     *CLAUDE.md* carries this scar. The new one implies it. Also, the old
     "beginning" modified "list" and was not a §15 rider bolted to a
     fact, so the edit was optional.
   - Severity: should.
   - Corrected: "The scar's entry in the scars list of *CLAUDE.md* begins
     "Verifying `dist/` without rebuilding blesses stale artifacts"."
