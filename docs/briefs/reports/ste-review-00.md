# STE80 review: book/chapters/00-preface.md

Status: REVISE. Blocks: 2. Should: 0.

Diff reviewed: `git diff HEAD -- book/chapters/00-preface.md`, nine hunks,
all in Light mode. Sentinels are untouched (none of the three lives in the
Preface). No code span, command, path, URL, or italic term changed.
`press check` passes (checker self-test, editorial, jargon). The ratchet
passes (151 findings against a baseline of 168). No paragraph grew, and no
blockquote was split.

1. **Chapter 12 description (line 59). Fact added: a sequence the chapter
   does not follow.**
   Old: "Builds the print interior and the cover wrap, works through
   providers and spine math, covers the publish checklists, and ends with
   ordering a copy."
   New: "Builds the print interior and the cover wrap, then works through
   providers and spine math. Covers the publish checklists and ends with
   ordering a copy."
   The new "then" says that providers and spine math come after the
   interior and the wrap. In chapter 12 the order is the reverse:
   "Providers and their numbers" and "Four spine shapes" (line 84) come
   before "Building the interior" (line 149) and "The cover wrap" (line
   167). The old sentence was a list and made no claim about order.
   Severity: blocks.
   Corrected: "Builds the print interior and the cover wrap and works
   through providers and spine math. Covers the publish checklists and ends
   with ordering a copy."

2. **Conventions, `[ ]`, `|`, and `...` (line 110). Qualifier lost: "In
   syntax lines" no longer covers the bar and the three periods.**
   Old: "In syntax lines, square brackets enclose an optional item, a
   vertical bar separates alternatives of which you choose one, and three
   periods mark an item you may repeat."
   New: "In syntax lines, square brackets enclose an optional item. A
   vertical bar separates alternatives of which you choose one, and three
   periods mark an item you may repeat."
   The scope phrase now governs only the first sentence. The second
   sentence states the bar and three-period rules with no scope. The next
   sentence then gives `...` a different meaning ("In an example, a line
   that holds only `...` marks output that the example leaves out"). With
   the scope gone, the two rules for `...` read as a contradiction.
   Severity: blocks.
   Corrected: "In syntax lines, square brackets enclose an optional item,
   and a vertical bar separates alternatives of which you choose one. Three
   periods in a syntax line mark an item you may repeat."

## Checked and accepted

- Chapter 1 (line 26). "Then" keeps the old sequence. The chapter runs
  laws (line 67), tour (121), editions (251), so the order is correct, and
  "them" still means the finished editions.
- Chapter 2 (line 29). The added "then" is accurate. "Running the doctor"
  (line 224) follows the package and toolchain installs (lines 41, 140)
  and comes before "The toolchain image" (266).
- Chapters 3, 13, and 16 (lines 32, 62, 71). These are plain splits with
  every item kept.
- How to contact us (line 143). This is a plain split. Both facts and "the
  fact base" stay.
- Pages site (line 153). The italic term stays, it matches
  `docs/vocabulary.md` ("the Pages site"), and both actors and the past
  tense stay.

## Note on the editor's report

The report says the line 153 edit "removes one hidden actor". The old
clause ("which the press built ... and GitHub Pages serves") was already
active and named both actors. The text is correct, but the report's claim
is not. No change to the book is needed.
