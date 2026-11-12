# Cut report: 06-checking-the-manuscript.md

Words: 6352 before, 6233 after. `press check` passes (exit 0). Not committed.

## Part 1, retold facts

1. `06:473` (verify-formats exception, keeper Chapter 8).
   Before: "Press also declares dependency edges between its targets. Each verify target rebuilds what it verifies before it inspects it, so a verifier does not bless an edition that the current manuscript did not produce. The one exception is `press verify-formats`, which includes an existing Print edition, *dist/alice.pdf*, in its cross-edition agreement check without rebuilding it. Chapter 8 describes the edges target by target."
   After: "Each verify target rebuilds what it verifies before it inspects it, with one exception that Chapter 8 explains."
2. `06:299` `[^6-twocopies]` (jargon lint twice, keeper Chapter 15).
   Before: "[^6-twocopies]: The jargon lint exists twice. One copy lives in the press package, and a portable copy lives inside the overused-jargon skill, so that the skill works without press installed. A check in `press selftest` requires the two copies to match byte for byte, function by function, except for the function that parses the command line."
   After: "[^6-twocopies]: A second, identical copy of the lint lives in the overused-jargon skill (Chapter 15)."
3. `06:378-382` (drop-cap sentinel warning): this file is the keeper. Kept in full, unchanged.

## Part 2, tics

4. `06:75` Before: "and the press puts the reason plainly:" After: "and the press gives the reason:"
5. `06:104` Before: "and Example 6.2 gives the message for each, folded to fit the page." After: "and Example 6.2 gives the message for each."
6. `06:258` Before: "Example 6.6 shows three rows of the watchlist, folded to fit the page. In the file, each row is one line." After: "Example 6.6 shows three rows of the watchlist. In the file, each row is one line." (The brief's fix joins the two with a semicolon; the cutter rules forbid semicolons in prose, so a period joins them.)
7. `06:332` Before: "Example 6.9 shows the message, folded to fit the page." After: "Example 6.9 shows the message."
8. `06:392` Before: "... with the message in Example 6.11, folded to fit the page." After: "... with the message in Example 6.11."
9. `06:408` Before: "The example folds long lines to fit the page and shortens the paths in the notes." After: "The example shortens the paths in the notes."
10. `06:437` Before: "Example 6.13 shows the end of a failed check on the Alice book, folded to fit the page." After: "... on the Alice book."

Line breaks inside every example block are untouched.

## Part 3, closing maxims

11. `06:34` "The two passes that read prose come last." Cut, the paragraph ends one sentence earlier.
12. `06:498` "The cure is a habit." Cut, the sidebar's next sentence stands alone.
13. Kept: `06:382` "It then fails in the Print edition." and `06:469` "The printed lines are for you, and the exit status is for every program that runs the checker on your behalf." Left as written: `06:75`, `06:186`, `06:227`.

## Part 4, shoulds

14. `06:451` Before: "Appendix C, *Messages and refusals*, holds the full list." After: "Appendix C holds the checker's and the verifiers' messages."
15. Hyphenation should (shared with 03 and 08). The brief names this file but gives a fix line only for 03 and 08. Applied at the analogous spot, the end of the paragraph quoting the scaffold's rule for choosing sentinels (`06:376`): appended "Prefer short words: a word LuaLaTeX hyphenates at a line end breaks the match." (the sentence the brief gives for `03:222`).

## Part 5, protected

The sidebar "The red check that went out green" (`06:491-499`) is unchanged except for the one cut in item 12. Headings and the "In this chapter" box are unchanged.
