# STE80 desk report: Appendix A, Command reference

File: `book/appendices/a-command-reference.md`. Mode: Humanize (Pass 2 at
80 percent) for descriptions, table cells, and the closing sections. The
appendix has no sidebar, anecdote, or epigraph.

## Ratchet count

- Before: 4 (baseline in `tools/ste-baseline.json`: 4)
- After: 4

All four leads were false or declined (below), so the count does not
fall. No sentence in the file exceeded 30 words before or after the pass.
`press check` passes (exit status 0).

## Edits

1. Line 3, S1/S2 (29 words, gloss in a parenthesis). Old: "It gives a
   synopsis, a description, the options, a short session on the Alice book
   (the book's sample, slug `alice`), and the chapter that explains the
   command in full." New: "It gives a synopsis, a description, the
   options, a short session on the Alice book, and the chapter that
   explains the command in full. The Alice book is the book's sample, slug
   `alice`."
2. Line 15, S1/S3 (26 words, two ideas, condition buried). Old: "We shorten
   the long ones, and where a line of output is wider than the page we
   break it and indent the rest by two spaces." New: "We shorten the long
   ones. Where a line of output is wider than the page, we break it and
   indent the rest by two spaces."
3. Line 25, S1 (two facts about two different things). Old: "A chapter
   takes the number after the highest one in use, padded to at least two
   digits, and an appendix counts down from `z-`." New: "A chapter takes
   the number after the highest one in use, padded to at least two digits.
   An appendix counts down from `z-`."
4. Line 54, S8 (-ing participle). Old: "a comment naming its source" New:
   "a comment that names its source"
5. Line 112, S1/S2 (28 words, definition plus a three-step sequence). Old:
   "Takes a finished image into the book through *intake*: press converts
   the file to the house form, puts it in place, and records the
   acceptance in *art/commissions.md*." New: "Takes a finished image into
   the book through *intake*. During intake, press converts the file to the
   house form, puts it in place, and records the acceptance in
   *art/commissions.md*." (Index term "intake" kept, twice.)
6. Line 118 (Table A.3 cell), S2 (30 words, at the ceiling). Old: "At the
   time of this writing, its aspect ratio must be within 3 percent of the
   ratio of the legacy `trim` field (6 by 9 unless set), not the
   profile's." New: "At the time of this writing, its aspect ratio must
   be within 3 percent of the ratio of the legacy `trim` field, not the
   profile's. That field is 6 by 9 unless set."
7. Line 396, S1/S2 (28 words, three ideas). Old: "Checks every config file
   against the book model and reports each file on its own line, the
   absent optional files included, as `ok` or with its problems." New:
   "Checks every config file against the book model. It reports each file
   on its own line, as `ok` or with its problems. The absent optional files
   get a line too."
8. Line 509, S1/S2 (26 words, two actions). Old: "Checks every program and
   key the press can use, and prints one line per capability with its
   state: ..." New: "Checks every program and key the press can use. It
   prints one line per capability with its state: ..."
9. Line 1012 (Table A.17 cell), S6/S8 (actor hidden behind "the cap",
   action in a noun). Old: "A positive cap takes a sample of the claims,
   and the workflow's accounting reports the claims it left out." New:
   "With a positive cap, the workflow samples the claims, and its
   accounting reports the claims it left out."
10. Line 1329, S3 (condition first). Old: "Test the exit status, not the
    output, in a script." New: "In a script, test the exit status, not the
    output." (Index term "exit status" kept.)

## Leads declined

- Line 90, phrasal verb "turn on" (print ordering). The swap list rejects
  "enable", and "turn on" matches the rest of the file ("when print
  ordering is on", "This turns on release mode", "turn color ... off or
  on"). Changing one instance would break one term per thing.
- Line 1084, "perfect tense: 'has eleven'". False positive: "press has
  eleven" is the possessive present, not a perfect.
- Line 1130, "-ing form: 'heading'". False positive: "heading" is a noun
  ("heading and paragraph problems").
- Line 1172, "-ing form: 'clipping'". False positive: "clipping at the
  edges" is a noun, the thing the verifier looks for.

Sentences of 25 to 29 words left whole, because each is one idea carrying
an enumerated list that a split would break: lines 185 (`--colors`
defaults), 209 (the four passes), 297 (`--json` fields), 485 (the desk's
contents), 955 (the four retail files), 965 (the checklist's three parts),
1291 (`press workflows` contents), and the Table A.19 `press config` cell.

## Passives kept

- Line 179 ("The subcommand is not listed by `--help`.") and the many
  "Not listed by `--help`." cells: the introduction promises that entries
  say "not listed by `--help`", so the formula stays as written.
- "whether it is required" (Table A.7) is a property of a field, not an
  action with a hidden actor.
