# Continuity report: Chapter 6, *Checking the manuscript*

Desk: continuity editor. Chapter read as it stands after its desks, the
re-review (`rereview-06.md`), and Revisions 2 and 3 (503 lines). Cross-checked
against Chapters 1, 3, 4 (committed), 7 and 8 (final revisions, with
`continuity-08.md`), 5, 12, 13 where Chapter 6 points to them, the press
source (`check_source.py`, `verify_pdf.py`, `verify_formats.py`,
`verify_pages.py`), `docs/vocabulary.md`, `docs/design.md` section 5, and
`docs/production-ledger.md`.

Status: **PASS WITH FIXES.** In Chapter 6: no blocks, two should, three may.
Against earlier chapters: one block (Chapters 1 and 3) and two should
(Chapter 1, Chapter 3). Every fence is tagged `text` (15), no code line
exceeds 64 columns, every image is followed by one blank line and its `art:`
comment. Figures 6.1 to 6.3 (`06-01-checker-guards-the-build`,
`06-02-fixture-round-trip`, `06-03-check-output`), Tables 6.1 to 6.5,
Examples 6.1 to 6.14: no gap, no repeat, slugs match, every `@fig:` has its
figure and is cited before it. The cast is clean; "the Alice book" (the
novel) and "the press's own three-chapter Alice example" (the captures,
l.408 to 410) obey the two Alices ruling.

Confirmed from the Chapter 3 pass: Example 6.10 (l.369 to 372) now carries
the sample book's sentinels, "Twinkle, twinkle, little bat" and "she made
some tarts", from the middles of chapters VII and XI, with
`verify-min-pages: 24`; it agrees with Chapter 3 (l.222, 245) and Chapter 8
(l.109 to 111). l.388 now says "the book model" (continuity-03, finding 4,
fixed). Chapter 6 defining *sentinel* (l.361) follows the ledger ruling
"sentinels are introduced in Ch 6"; continuity-04 finding 4 is withdrawn.

Shared facts that agree across 1, 3, 4, 6, 7, 8: the four passes and their
order; the four summary lines; 19 packaged fixtures, plus one per file in
*tests/known-bad/*; fixtures run in `press check` and `press all`, not a bare
`press pdf`; the paragraph law and its message; the glyph law message;
dashes and `--`; required metadata keys; `verify-min-pages` 40 / 1 / 24;
release witnesses and the refusal text; sentinel matching (exact case,
quotes equal); the four places a sentinel is checked (6 l.361, 8 l.404);
the drop-cap warning; `press verify` builds the PDF without the checker;
the `press verify-formats` stale-PDF exception (6 l.473, 8 l.433 to 439);
*build/jargon-report.txt*.

## Findings

### 1. `sentinel ... not found` is the checker's message, not a verifier's (blocks, against Chapters 1 and 3)

Quotes: Ch. 1 l.250 "3. `sentinel ... not found`. A verifier could not find
a sentinel phrase". Ch. 3 l.539 "The message `sentinel ... not found` means
a sentinel is not in the manuscript, or not in one of the artifacts."

Rule: shared fact (sentinel messages). Only the source checks print a
"not found" form: `sentinel not found in the manuscript: <s>`
(`check_source.py` l.61; Ch. 6 l.361, Table 6.5). The verifiers say
"missing": `missing text sentinel in PDF: <s>` (`verify_pdf.py` l.324; Ch. 8
l.114, 501), `<label> missing sentinel: <s>` (`verify_formats.py`),
`public reading surface missing sentinel: <s>` (`verify_pages.py`). A reader
who meets the verifier's message in Chapter 8 will not find it under the
form Chapter 1 taught.

Fix: Ch. 1 l.250: "3. `sentinel not found in the manuscript` or `missing
text sentinel in PDF`. The checker or a verifier could not find a sentinel
phrase, which the section "The editions" explains." Ch. 3 l.539: "The
message `sentinel not found in the manuscript` means a sentinel is not in
the manuscript; `missing text sentinel in PDF` means the PDF lost one."
Both chapters are committed; this goes to the whole-book sweep or a fix
commit. Chapter 6 needs no change.

### 2. The second pass has two names in Chapter 6 (should)

Quotes: Table 6.1 l.28 "Checking the checkers"; A-head l.73 and
in-this-chapter list l.8 "Checking the checkers"; Figure 6.1 art brief l.40
"checking the checkers". l.75 "The second pass, `check_the_checkers`, is the
*checker self-test*"; l.98 to 141 and Example 6.12 use "checker self-test".

Rule: one thing, one name. The press's own line says `Checker self-test
passed`; Chapters 3 (l.508, 535) and 7 (l.413) say "the self-test".

Fix: Table 6.1 row "Checker self-test"; Figure 6.1 label "checker
self-test" (the PNG is a placeholder, so this costs nothing). The A-head may
stay as a title, or become "The checker self-test" (with l.8); writer's call.

### 3. "the house rules" for the house's law in general (should)

Quote, l.21: "refuses a book that breaks the house rules". l.303 then
defines *House rules* as the file *config/house-rules.yaml*, which is
optional and holds only the book's own additions.

Rule: one name, one thing (vocabulary: house rules = *config/house-rules.yaml*;
the house = press's default design and law). A book with no house-rules
file is still refused for an em dash.

Fix, l.21: "refuses a book that breaks one of its rules" (Chapter 1 l.36's
wording).

### 4. "selftest" in Chapter 1 (should, against Chapter 1)

Quotes: Ch. 1 l.156 "One is a selftest of the checker's own rules."; l.158
"The selftest is the unusual pass ... the selftest fails".

Rule: one thing, one name. Chapters 3, 6, 7 write "self-test" (press's own
line: `Checker self-test passed`), and Chapter 6 footnote l.299 names a
different thing, the `press selftest` target. Chapter 1's spelling makes
the pass and the target one word.

Fix (Ch. 1, committed; sweep): "checker self-test" at l.156, "The checker
self-test is the unusual pass" and "the checker self-test fails" at l.158.

### 5. "the editorial checks" and "the jargon check" in Chapter 3 (should, against Chapter 3)

Quote, Ch. 3 l.533: "the source checks, the self-test, the editorial checks,
and the jargon check."

Rule: one thing, one name. Chapters 1 (l.156), 4, 6, and 7 (l.413) say "the
style audit" and "the jargon lint"; the printed lines say `Editorial checks`
and `Jargon check`, which Chapter 6 quotes as messages only.

Fix (Ch. 3, committed; sweep): "the source checks, the checker self-test,
the style audit, and the jargon lint."

### 6. design.md lists two figures for Chapter 6; it has three (may)

`docs/design.md` section 5 row 6 lists 6.1 and 6.2. The chapter adds 6.3
`06-03-check-output` (a terminal capture, l.431). Fix: add 6.3 to design.md.

### 7. Figure 6.3's title bar (may)

Quote: art brief l.433 "a plain title bar reading
"alice@hatter: ~/alice-in-wonderland""; fig-alt l.431 "A terminal window
titled alice at hatter". Chapter 8's Figure 8.3 title bar is "alice@hatter".
No other chapter puts the gallery example in *~/alice-in-wonderland* on
`hatter`.

Fix: title bar "alice@hatter", matching the fig-alt and Figure 8.3.

### 8. Chapter 1's promise "lists every rule and its message" (may)

Ch. 1 l.36 promises Chapter 6 "lists every rule and its message". Chapter 6
describes every rule and gives most messages, then calls Table 6.5 the ones
"you are most likely to meet" and sends the reader to Appendix C for the
full list (l.451). Kept in substance; the full list is now owed by
Appendix C, *Messages and refusals* (stub). Recorded in the ledger; no
change to either chapter.

### 9. "fails" for a checker pass (may; vocabulary)

Quotes: l.21 "the first pass that fails", l.75 "the check fails", l.131,
l.239, l.449. The vocabulary reserves "fail" for a verifier result and
"refuse" for press stopping with a message. Press's own header is
`Editorial checks failed:`, and the passes do fail in that sense. No
change to the chapter; recommend the vocabulary allow "fail" for a pass of
the checker, with "refuse" for what the checker does to the book.

## Promises kept (incoming)

1 (l.36) every rule and its message (finding 8); 3 (l.120) *tests/known-bad/*
(l.120 to 141); 3 (l.535) the four passes taken apart; 4 (l.155)
`audit-dirs` and `banned-patterns` (l.301 to 353); 4 (l.185) the jargon lint
and its watchlist (l.216 to 299); 4 (l.204) sentinels introduced (l.361);
5 (l.122) cited as an example only; 7 (l.22) the targets that read the
manuscript (`press check`, `press style`); 8 (l.412) the checker's sentinel
check (l.361).

## Cross-references out (all correct)

13 *Registrations* (l.62); 5 *Figures, plates, and illustrations* (l.64, 65);
12 *The print pack* (l.67); 4 *Writing the manuscript* (l.194, 202); 8
*Verifying the artifacts* (l.357, 473); Appendix C *Messages and refusals*
(l.451); 14 *Continuous integration and the release contract* (l.475); 7
*Building the editions* (l.501, next chapter). "Later in this chapter":
l.63 to l.355, l.132 and l.196 to l.301, l.291 to l.301, all later.
"Earlier": l.353 to l.145, l.471 to l.19.
