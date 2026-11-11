# Report: Chapter 6, Checking the manuscript

File: `book/chapters/06-checking-the-manuscript.md`

## Status

DONE_WITH_CONCERNS (small; listed below).

## Word count

`press wordcount`: 6,167 (target 5,500; inside 15 percent, upper end).
Prose only (tables, code, comments, captions stripped): about 4,000 words
in about 260 sentences, average about 15.5 words by my count, longest 30.
The rest is tables, examples, captions, and three art directives.

## Gates

- `press style`: no finding in this file.
- `press check` in the repository stops in the source checks on plates
  `02-01`, `02-02` (and `02-03`) never referenced by Chapter 2, and the
  style audit fails on Chapter 2 paragraph lengths. Not mine. In a
  throwaway copy with Chapter 2 stubbed, all three of my passes are clean
  (source, self-test 29 fixtures, editorial 23 files); the jargon lint
  then fails only on `authoritative` in Chapter 5. My file draws three
  `inspect` sightings (spine, churn, in a sentence that names inspect
  terms; spine in the sewing-machine example), which do not fail.
- Three art directives are 127 to 131 words; the sidebar is 166 words.

## Figures

- 6.1 `@fig:checker-guards-the-build` (pipeline): chapter and config file
  icons; one large `press check` box holding four rounded pass boxes in
  order; a pass arrow to `press pdf`, `press epub`, `press site`; a fail
  arrow down to a shadowed "stop (nonzero exit)" box.
- 6.2 `@fig:fixture-round-trip` (flowchart): fixture icon with its expect
  comment (described in words, since a literal `-->` would close the art
  comment); audit and lint box; diamond; Yes to "fixture passes"; No to
  the quoted `expected rule ... did not fire (no diagnostics at all)`.
- 6.3 `@fig:check-output` (terminal): the captured passing output, line
  by line, in a window titled `alice@hatter: ~/alice`.

Tables 6.1 to 6.7, Examples 6.1 to 6.15, one sidebar (war story 11),
three tips, three warnings, four footnotes. Each is referenced before it
appears.

## Deviations from the brief, with reasons

- Figure 6.1: the brief says "stop (exit 1)". The fact file gives no
  exit code for a failed `press check` (only 0 on success, in facts-01),
  so the box reads "stop (nonzero exit)" and the prose says nonzero.
- Table 6.3 lists 17 of the 19 packaged fixtures. `testament.md` and
  `vibrant-tapestry.md` trip this book's own `assistant vocabulary`
  pattern even inside inline code, so the prose names their expected
  rules and says why they are left out.
- The three unfinished markers are described, not shown: the source
  check refuses `lorem ipsum` even inside a fenced code block.
- Example 6.8 (Alice house rules) uses `jargon-allow: [seams]` in place
  of the fact file's `leverage`: this book's banned patterns refuse
  `leverage` even inside fenced code.

## Facts observed in this repository, not in the fact file

- Banned patterns and the unfinished-marker check read fenced code too
  (observed while drafting). I state only the marker case in prose.
- A failing style audit prints `Editorial checks failed:` and lines of
  the form `  - <file>:<line>: <label>` and `  - <file>: paragraph N has
  W words (...)` (observed in this book's own check). Example 6.13 is
  built on that form.
- The book's banned patterns also apply to the packaged fixtures (this
  book's check notes `testament.md also drew: ... assistant
  vocabulary`). The chapter says so in "Fixtures for your own rules".

## Facts needed and left out

- The exit code of a failing `press check` (see above).
- Whether `press pdf` and the other format targets run `press check` at
  all; the chapter says only that `press all` runs it first and that a
  bare `press pdf` does not run the fixtures.
- The 21 small words of the title-case test.
- The success output when a book has its own fixtures ("quoted in §3.4"
  of the fact base, not in facts-06).
- The exact em dash, en dash, and curly-quote diagnostics as printed with
  a filename prefix.

## Contradictions noticed

- The prose contract says the watchlist has 54 terms; facts-06 says 53
  rules. I used 53.
- Docs say the expect comment may sit anywhere; the code reads the first.
  Footnoted, with the advice to use one.
- The style guide's calibration sample shows `--strict`, `--only`,
  `--rules`, `--quiet` for `press check`; none is in the fact file. Not
  used.

## ste_check residuals (defended)

- Semicolons: one inside the verbatim scars-list quotation in the
  sidebar, and the index comment's required separator.
- "be determined" is the quoted phrase "to be determined"; "is malformed"
  is adjectival.
- Remaining sentence-length and paragraph-length hits are tables,
  examples, art directives, and the index comment.
- `-ing` hits are headings and adjectives (trailing whitespace,
  "Checking the checkers").

## Revision (after facts-06, dev-06, copy-06, type-06 and the coordinator's rulings)

`press wordcount`: 5,696 (target 5,500). Prose about 4,550 of it (80
percent). `press check`: source checks, checker self-test (29 fixtures),
and editorial pass all pass; the jargon lint fails only on
`authoritative` in Chapter 5 (not mine). No diagnostic names this file.
ste_check residuals: "be determined" (quoted phrase), "is malformed"
(adjective), two semicolons (verbatim scars quote, index comment), long
"sentences" that are art comments, the In-this-chapter list, or footnote
fusions.

### Coordinator rulings

1. S1: opening, Figure 6.1 (now "The checker as press all runs it",
   directive draws `press all` and its builds), the four-passes section
   (bare format targets and `press verify` skip the checker), the fixtures
   line, and the exit section all agree. S2: "nonzero" throughout, 0 on
   success. S3: the style audit now says the universal battery skips fenced
   code except trailing whitespace, the book's patterns skip fenced code,
   and both read inline code (reconfirmed in a scratch copy; my earlier
   report's claim about fenced code was wrong for banned patterns, right
   for the unfinished markers, which the source checks do read in fences).
   S4/S5: Example 6.12 and Figure 6.3 are S4's capture, labelled "the
   press's own three-chapter Alice example". The sample `alice` is one
   state throughout: its description set on day one (Chapter 1), its own
   fixture *tests/known-bad/very-unique.md*, house rules with
   `audit-dirs: [notes]`, sentinels from Carroll's chapters 6 and 7, floor
   24 once its chapters exist. Example 6.13 now shows only the failing
   block (no counts). S6: exactness claim dropped; title-case test points
   to Chapter 4. S7: "checker self-test" defined at the second pass;
   footnote names `press selftest`.
2. "ship/ships/shipped" gone except inside the verbatim scars quotation
   (copy-06 item 10 keeps it); sidebar retitled "The red check that went
   out green". "Source" for files replaced by "the manuscript" or "chapter
   file". "refuse" reserved for press; the lint's boundary "allows no
   match".
3. Self-reference cut (the markers sentence, the two missing fixtures, the
   table-describes-instead sentence, the code-block sentence, "this book,
   for example", "this chapter introduces them", the opening's examples
   sentence).
4. Line 496 rewritten: each verify target rebuilds what it verifies, with
   `press verify-formats` and the existing PDF as the one exception. Line
   209: "every rendered edition except the Manuscript edition (the
   stitched Markdown)".
5. Fixture procedure added ("Writing a fixture", five steps, including
   the deliberate first failure and the count rising to 20). Audit
   directories defined once in "The style audit"; the House rules B-head
   points back; example `notes`. Tables 6.3/6.4 and Example 6.3 merged
   into one example (pattern, diagnostic, fixture, all in fenced code,
   where the testament and tapestry filenames are safe); the six
   book-prose fixtures are no longer listed. Glyph, title-case, paragraph
   detail now points to Chapter 4. The scar is told in the sidebar; prose
   keeps one sentence on pipeline status and Example 6.15 is gone. One
   forward pointer at the close (CI moved into the section body). Table
   6.5 (was 6.7) retitled "Diagnostics you are most likely to meet" with
   a pointer to Appendix C. Package paths removed; the watchlist is located
   through `press skills`.
6. Art comments after their image lines with one blank line; all fences
   `text`; no code line over 64 columns; no prose paragraph over six
   sentences; sidebar 160 words.

### facts-06 (fact check)

- Unsupported 1: resolved by S4. 2: kept, now tied to Chapter 1's
  `press config set` of the description. 3: kept, reconfirmed by test
  (markers are read in fences). 4: applied (Table 6.2 placement row). 5:
  applied ("number of manuscript files it read, in order"; scaffold 1 kept
  per S5). 6: kept (observed: this repository's check notes
  `testament.md also drew: ... assistant vocabulary`); follow-on corrected
  to "matches text in one of the packaged fixtures". 7: kept for tips,
  warnings, sidebars (markup.md states it); the art-comment sentence is
  cut, since the comment is now its own paragraph. 8: applied (cut). 9:
  kept the header and hyphen form, which are a real capture from this
  repository's own check; the session prompt and counts are removed. 10:
  applied. 11: applied (`expected.yaml` and its footnote cut with the
  package paths). 12: applied (`[Vv]` example; "refuses a pattern that
  does not compile"). 13: applied by ruling (it is now the Alice book's
  own file, `leverage` restored since banned patterns skip fences). 14:
  applied (general mechanism; only historical claim is the quote). 15:
  0 kept (facts-01 capture), nonzero per S2. 16: applied per S1. 17:
  softened (order rationale reduced; "several are also the literal names
  of things in press" kept as framing).
- Contradicted 1-3: applied. Drifted 1: applied (conditional warning,
  house sets none). 2-3: moot (detail moved to Chapter 4; fixture table
  gone). 4: applied ("folded to fit the page" on every folded example).
  5: applied. 6: applied. 7: applied ("on every check"). 8: applied. 9:
  applied. 10: applied. Missing 1: applied (two hyphens).
- Editor note on Chapter 4: Chapter 4 line 243 says the banned patterns
  skip inline code, which S3 contradicts. Not my file.

### dev-06

C1 applied (S2). P1 applied. P2 applied (S4/S5, one Alice state). P3
applied (S7). P4 applied (procedure). P5 applied. P6 applied (`notes`).
P7 applied (cross-references in Table 6.2). P8 applied (pointer to
Chapter 4). R1 applied. R2 applied. R3 applied. R4 applied. R5 applied
(match counts and column list cut, hand-run options in one sentence,
"Reading the jargon report" added). O1 applied. N1 declined: the brief
and the ruling keep Figure 6.3; the prose now introduces it as the
terminal view of Example 6.12. N2 applied (retitled, Appendix C pointer).

### copy-06

Blocks 1-10 applied (10 retitled; the quote stays verbatim). Should:
11-14 applied; 15 applied; 16 n/a (sentence cut); 17 applied as the new
"matches text in a packaged fixture"; 18-23 applied; 24 applied; 25
applied; 26 applied (scars defined in the sidebar, the prose sentence
cut); 27-28 applied (28 now moot, paragraph cut to Chapter 4 pointer);
29-33 applied; 34-43 applied (39 per wording; 43 deleted). May: 44
applied; 45 applied; 46 n/a (cut); 47 n/a (counts cut); 48 applied; 49
applied; 50 applied (instruction moved to the body; footnote keeps the
doc discrepancy); 51 applied; 52 applied (warning placed after the
shell paragraph, before the sidebar, and phrased as the remedy); 53 n/a
(cut); 54 applied; 55 applied ("terms" for watchlist entries, "rows" for
CSV lines).

### type-06

Blocks 1-3 applied: by the coordinator's ruling 6 the `art:` comment now
follows its image line with one blank line (`tools/space-art-comments.py`
reports nothing left to insert). Should: fences tagged; eight long lines
rewrapped under 64 columns; stranded example captions depend on final
pagination and the chapter is about 470 words shorter, so they need a
re-render to judge (not checked here).

## Revision 2 (after rereview-06)

`press wordcount`: 5,669. `press check` from the repository root passes
all four passes (23 files, 29 fixtures, jargon clean). ste_check residuals
unchanged and defended (quoted "to be determined", adjectival "is
malformed", the scars quote and index comment semicolons).

1. Footnote labels: confirmed, all three read `[^6-...]`
   (`6-first-expect`, `6-law-date`, `6-twocopies`), reference and
   definition.
2. Example 6.8: `jargon-allow` now lists `seams`, a rewrite term on the
   watchlist, which matches the sewing-machine sentence in "Jargon
   allowances".
3. Nits applied: "The checker self-test line now counts 20 fixtures";
   the repeated "reads the manuscript and its configuration" cut from the
   opening's second sentence and from the four-passes paragraph; the
   audit-directory restatements cut from "Banned patterns" and "Audit
   directories" (the definition in "The style audit" is the only one).
4. Edition names: the Print edition glossed once as "(PDF)" at
   `press verify` in "The four passes", then "the Print edition" for the
   sentinel places, the drop-cap warning, the page floor, and the
   `verify-formats` exception (*dist/alice.pdf* kept as the filename).
   The Manuscript edition was already glossed "(the stitched Markdown)".
   Figure 6.1's directive now draws "Print edition", "Circulating
   edition", "Chapter edition". "PDF verifier" stays, as the verifier's
   name.
5. Open item 2 (Example 6.11's caption stranded at a page foot): not
   applied; it depends on final pagination, as the re-review says.
- Revision 3: Example 6.10's sentinels now match Chapters 3 and 8 ("Twinkle, twinkle, little bat", "she made some tarts"; lead-in says Carroll's seventh and eleventh chapters); "the typed model" is now "the book model". press check passes.
- Revision 4: second pass named "the checker self-test" in Table 6.1, Figure 6.1 directive, and the first sentence of "Checking the checkers" (A-head words kept); line 21 now "the house's law" (house rules stays the file); Figure 6.3 title bar "alice@hatter", matching Figure 8.3 and the continuity fix (not "~/alice", since the run is on the press's own Alice example, not the Alice book directory). press check passes.
