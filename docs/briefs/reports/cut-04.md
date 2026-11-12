# Cut report: 04-writing-the-manuscript.md

Words: 6996 before, 6602 after (`wc -w`).

## Retold facts (part 1)

1. `04:52` file sorting. Before: "Press finds chapters by their filenames. A chapter file's name starts with a digit and ends in `.md`. An *appendix file* is ... Press pads the numbers it hands out to at least two digits for that reason." After: "A chapter file's name starts with a digit, and Chapter 3 gives the sorting rules." (The brief's wording has a semicolon; the comma-and form keeps the no-semicolon rule.)
2. `04:54-56` warning "Start every chapter file's name with a digit ..." Cut (Chapter 3 holds the same box).
3. `04:58-66` "The simplest way to start a chapter is to let press create the file ..." through "covers the index." Cut to the session (`$ press add chapter "The rabbit sends in a little Bill"`, verbatim) followed by "`press add chapter` names the file and writes the heading word for word (Chapter 3)."
4. `04:97` hand-typed chapter references. Kept, as the brief says (author-facing instruction).
5. `04:311-313` warning "Never choose a sentinel from the first words of a chapter ..." Cut outright (Chapter 6 keeps it; `04:204` points there).
6. `04:439` `[^4-ties]`. Before: "Pandoc ties Mr. on its own. For that reason, the press's test for the tie once passed with no filter in place at all. The Lua coverage work for press 3.0.2 found the empty test. The Lua tests, it turned out, also skipped silently in CI until CI set `PRESS_REQUIRE_LUA=1`." After: "Pandoc ties Mr. on its own, and the filter covers the rest. Chapter 16 tells what that once did to a test." (Brief's semicolon replaced with ", and".)

## Tics (part 2)

7. `04:142` "The house law is plain about what to do instead: rewrite the sentence." -> "The house law says what to do instead: rewrite the sentence."
8. `04:291` "so a preface opens plainly." -> "so a preface opens with a plain paragraph."
9. `04:419` "The press states the principle plainly." Cut; the paragraph opens on "The manuscript stays plain prose, ..."

No word-counted quotations or fit-the-page asides in this file.

## Closing maxims (part 3)

10. `04:132` "You never need the sign in a chapter." Cut, ends earlier on "... which Chapter 10 describes."
Kept: `04:89` "The house would still write it in sentence case." and `04:252` "A session that you typed from memory ... catches out." All "leave" entries untouched.

## Shoulds (part 4)

None name this file.

## Protected

`04:138-151` (dash law through Example 4.3) and `04:413-419` (fine work) untouched except the two tic fixes the brief names inside them (items 7 and 9).

## press check

`~/code/.pwp-venv/bin/press check` passed: source, checker self-test (29 fixtures), editorial, and jargon checks.
