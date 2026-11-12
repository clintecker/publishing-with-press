# STE80 review: Chapter 9, The house design

File: `book/chapters/09-the-house-design.md`. Diff: `git diff HEAD`, 12 hunks,
23 edits, matching the editor's report one for one.

Status: **REVISE** (0 blocks, 2 should).

Checks run: `press check` exits 0 (self-test, editorial, jargon). `python3
tools/ste-ratchet.py` passes (77 findings against a baseline of 139). The three
sentinels occur in neither the old nor the new file, as the editor says. No
code span, path, key, identifier, number, quotation, heading, figure line, art
comment, footnote, or sidebar changed. No paragraph grows; every edited
paragraph stays at six sentences or fewer.

Edits checked hardest, approved:

- Edit 3 ("That option makes the chosen face set its numerals in the old
  style"). The old "so" already tied the effect to the command the header
  writes, and the only thing in that command that sets figures is
  `Numbers=OldStyle`. `docs/briefs/facts/facts-09.md` (lines 13 and 22) backs
  it: `\setmainfont{<family>}[Numbers=OldStyle]` and "Oldstyle figures for the
  aesthetic font". Naming the option as the cause is accurate, not added.
  Certainty is unchanged ("sets" became "makes ... set"). The Libertinus case
  is untouched.
- Edits 1, 2, 4, 6 to 18, 20 to 23: facts, qualifiers ("may" in edit 12,
  "only" in edit 18, "also" carries "and" in edit 21), and order hold. Edit 7
  is a correct passive-to-active swap with the header as actor. Edit 8 changes
  no words.

## Findings

1. **Edit 5, L90, List of Plates.**
   Old: "The plates and the figures have separate lists, the List of Plates
   and the List of Figures (a scar Chapter 7 tells kept the List of Plates full
   at that depth)."
   New: "The plates and the figures have separate lists, the List of Plates
   and the List of Figures. A scar that Chapter 7 tells kept the List of Plates
   full at that depth."
   What went wrong: no fact changed, but the new sentence is a garden path.
   It opens on a bare noun phrase, and the reader parses "A scar that Chapter
   7 tells" as a fragment, then meets "tells kept" and must back up to find
   the verb. As a parenthetical the aside could stay loose; as its own
   sentence it reads as a fragment. Severity: should (voice).
   Corrected: "Chapter 7 tells the scar that kept the List of Plates full at
   that depth."

2. **Edit 19, L312, Example 9.1 and the merge rule.**
   Old: "It writes nine tokens of the light palette and all four book colors,
   including the values it keeps."
   New: "It writes nine tokens of the light palette and all four book colors,
   the values it keeps among them."
   What went wrong: the meaning holds, but the fix swaps a preposition the
   ratchet misread as an -ing form for a verbless absolute phrase, which is
   harder to parse than the original and reads as a tag clipped off a
   sentence. "Keeps" also now floats at the end of a dangling phrase, where
   it is easy to read as "holds" rather than "leaves at the house value", and
   that point (unchanged values must be restated) is the whole lesson of the
   paragraph. Severity: should (voice, clarity of the one fact the paragraph
   teaches).
   Corrected (one sentence, so the paragraph stays at six): "It writes nine
   tokens of the light palette and all four book colors, and the values it
   keeps are among them."

## Not findings

- Edit 22 ("an author moving" to "an author who moved"): the message reached
  authors at the time of the move either way; no fact shifts.
- Edit 1 moves "then" from the third clause to the second. The order of the
  chapter's parts is still stated correctly.
