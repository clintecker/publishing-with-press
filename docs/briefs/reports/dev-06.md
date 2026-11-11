# Developmental edit: Chapter 6, Checking the manuscript

Desk: developmental editor. File: `book/chapters/06-checking-the-manuscript.md`
(534 lines, read as the design's reader: an author who can use a shell and
does not know TeX). Line numbers refer to the file as read.

Status: DONE_WITH_CONCERNS. 0 block, 17 should.

## 1. Coverage

All nine A-heads from the brief are present, in order, in sentence case,
with prose between every pair of headings. Every core topic in the design
row is reached: the four passes in order, each rule and its message,
`house-rules.yaml` and its three keys, the watchlist and its statuses,
known-bad and known-good fixtures, sentinels and the page floor, exit
status, and the red-check scar (as the sidebar). No block.

| A-head | Line | Does the section deliver? |
|---|---|---|
| The four passes | 19 | Yes. Table 6.1 and the order rationale (34) are good. The guard claim at 36 overreaches (P1). |
| Source checks | 47 | Yes. Table 6.2 leans on terms from later chapters (P7). |
| Checking the checkers | 70 | Yes on the mechanism. Weak on the one thing an author does here, write a fixture (P4). Table 6.3 is weight the reader does not need (R3). |
| The style audit | 160 | Yes, but much of "Rules for book prose" and "Headings and paragraphs" re-teaches Chapter 4 (R1). |
| The jargon lint and the watchlist | 239 | Yes. Long on watchlist internals, short on what to do with the report (R5). |
| House rules | 326 | Yes. The strongest section for an author: a real file, a table of keys, the case-sensitivity trap, the YAML backslash. The `appendices` example misleads (P6). |
| Sentinels and the page floor | 380 | Yes. The release refusal (417) is a useful catch. |
| Reading the output | 431 | Yes. Table 6.7 claims more than it holds (N2). The passing output contradicts the Alice state (P2). |
| Exit status and what depends on it | 492 | Partly. The status is "nonzero" with no number (C1), and the mechanism of the scar is told three times (R4). |

**C1 (should). The design row asks for exit codes; the chapter gives only
"0" and "nonzero".** Line 494: "When any pass fails, it stops there and
exits with a nonzero status." The only number the chapter gives is the
jargon lint's 2 on a malformed watchlist (318), in another section. The
writer's report says facts-06 has no failing exit code. Fix: the controller
adds the exit code (or codes) of a failed `press check` to facts-06, and the
writer states it at 494 and in the Figure 6.1 directive, where the box now
reads "stop (nonzero exit)". If the code is 1 for every pass, one sentence
says so. If it differs by pass, a two-column table belongs here.

## 2. Path

**P1 (should). The chapter's thesis contradicts its own line 154.** The
orientation says "Every book that press builds passes through one command
first" (17). Line 36 says the editions do not exist "until all four passes
succeed", and the Figure 6.1 directive (38) tells the illustrator "the only
road to the build targets runs through all four boxes". Then line 154 says
"a bare `press pdf` does not run" the fixtures, and line 496 says only that
`press all` runs the checker first. Facts-06, section 20, item 10, flags
"on every build" as a contradiction to avoid. A reader who runs `press pdf`
will believe the manuscript was checked. Fix: the controller confirms what
a bare format target runs (the writer lists this as a missing fact). Then
17, 36, the directive, and the caption say that `press all` and CI route
every build through the check, and line 154 (or a short paragraph beside
it) says what a bare `press pdf` skips. If the design's figure title "the
checker guards every build" is wrong, the managing editor retitles it.

**P2 (should). The Alice example is in two states at once.** Example 6.12
prints "Source checks passed: 1 ordered Markdown files" and "19 known-bad
fixtures", which line 68 identifies as a fresh scaffold with only the
preface. But the chapter has already given Alice a fixture of its own
(Example 6.1, "A known-bad fixture for the Alice example"), house rules
with a banned pattern and an audit directory (Example 6.8), and a chapter
file, *01-down-the-rabbit-hole.md* (Example 6.13). With those, the counts
would be at least 2 files and 20 fixtures. Example 6.13 contradicts itself:
its own source line says "1 ordered Markdown files" over a failure in
chapter 01. Fix: one sentence at 433 must say that Example 6.12 and Figure
6.3 show the Alice repository on the day it was scaffolded, before any of
the files this chapter added. Example 6.13 is constructed, so its count
must match the files it names.

**P3 (should). "Self-test" is used before it is defined, and it collides
with `press selftest`.** Line 34 says "The self-test comes second" when the
reader has only the pass name "Checking the checkers" from Table 6.1. The
term is never italicized and defined. Footnote `twocopies` (324) then uses
"the press's own self-test" for a different thing, the `press selftest`
command of Chapter 16. Chapter 1 (153) spells the pass "selftest". Fix: at
72, define the term once ("the second pass, the *checker self-test*"), use
it consistently, and make the footnote name `press selftest` in constant
width so the reader can tell the two apart. The controller should add the
term to `docs/vocabulary.md` so Chapters 1 and 3 can follow.

**P4 (should). Writing a fixture has no procedure.** The section the author
will act on (144) says fixtures go in *tests/known-bad/*, but Example 6.1
never names its file, and the only filename the chapter gives,
*tests/known-bad/very-unique.md*, is inside the Figure 6.2 art directive,
which the reader never sees. Nor does the reader see the success line rise
from 19 to 20, the one signal that press found the fixture. Fix: name the
file in Example 6.1's caption or the sentence before it, and give the steps
in order (create the directory, write the file with one expect comment, add
the pattern, run `press check`, look for the count). The success output for
a book with its own fixtures is "quoted in section 3.4" of the fact base
and absent from facts-06; the controller supplies it.

**P5 (should). Package paths that the reader cannot find.** Lines 74, 91,
142, and 254 give *src/press/data/known-bad/*, *src/press/data/known-good/
clean.md*, *src/press/data/known-bad/expected.yaml*, and the watchlist's
*src/press/data/skills/...* path. A reader in `~/alice` on `hatter` finds
none of them. The warning at 321 tells the reader not to edit the
watchlist, but never says where to read it. Fix: say once, at 74, that
these paths are inside the installed press package. For the watchlist, say
how to locate it (if the fact base supports `press skills` printing
installed paths, use that; otherwise the controller adds the fact).

**P6 (should). The `audit-dirs` example names a directory the reader
already knows as part of the manuscript.** Example 6.8 sets `audit-dirs:
[appendices]`, and line 378 calls the audited files "notes and drafts that
never print in the book". Chapter 3 (347) taught that appendixes live in
*book/appendices/* and print, and line 68 counts them among the "ordered
Markdown files". The reader cannot tell whether `appendices` means
*book/appendices/* (which would then meet the lighter battery and skip the
jargon lint) or a top-level *appendices/* directory. Fix: say what an
`audit-dirs` entry is relative to, and choose a name that cannot collide,
such as `notes`. The writer already substituted `seams` for the fact
file's `leverage`, so a substitution has precedent. If the controller
prefers the fact file's value, add one sentence that removes the doubt.

**P7 (should). Table 6.2 leans on terms from later chapters without
pointers.** "a retail book that still holds a placeholder" (59), "a plate
image" (61), and "the provider's catalog" (64) are Chapter 13, Chapter 5,
and Chapter 12 terms. Fix: one cross-reference per row in the Meaning cell,
in the house form (Chapter 13, *Registrations*).

**P8 (should). "Worth knowing exactly", then not exact.** Line 221 promises
the exact title-case test and withholds the 21 small words, so the reader
still cannot predict a borderline heading. Chapter 4 (77) already states the
same test. Fix: either the controller supplies the list (an example or a
table), or the paragraph drops the promise and points to Chapter 4 (see R1).

## 3. Proportion

**R1 (should). The style audit re-teaches Chapter 4.** The glyph law
(209 to 213), the title-case test (221), the paragraph law (223), and the
drop-cap sentinel warning (403 to 407) repeat Chapter 4 lines 77, 103 to
113, 157, and 310, in places nearly word for word. Chapter 4 (153, 202)
hands the reader to this chapter for `audit-dirs`, banned patterns, and
sentinels, not for these. Fix: for each, keep the diagnostic and what is
new about the checker (the block-as-one-paragraph rule at 229 is new and
valuable; keep it whole), and replace the rest with a cross-reference to
Chapter 4, *Writing the manuscript*. Line 407 restates the warning above
it and goes entirely.

**R2 (should). The audit-directory rule is told six times.** Lines 162,
209, 233, 250, 366, and 378 each restate which rules the audit directories
meet. Fix: line 233 is the home. The House rules B-head "Audit directories"
(376 to 378) becomes one sentence that points back to it, and 250 and 366
drop their restatements.

**R3 (should). Three overlapping lists of the same rules.** Table 6.3
(17 packaged fixtures, each Meaning cell "The fixture expects..."), Table
6.4 (the universal battery, described in riddles), and Example 6.3 (the
same patterns in plain text) cover one set of rules. Line 166 says the
table describes the phrases "instead of quoting them, because this chapter
is itself audited", and twelve lines later Example 6.3 quotes them. The
reader then wonders why. Line 118 spends three sentences on why two
fixtures are missing because of "this book's own house rules", which is
the book talking about itself. The author never edits the packaged
fixtures. Fix: let Example 6.3 carry the patterns, with a third column
for the fixture filename where the code block allows it. Reduce Table 6.4
to what each family is for, or cut it. Drop Table 6.3 and line 118. One
sentence keeps the fact that each battery rule has a packaged fixture.

**R4 (should). The red-check mechanism is told three times in thirty
lines.** Line 514 explains it, the sidebar's second paragraph (521)
explains it again, and the warning (527) restates the rule the sidebar
quotes. Fix: line 514 keeps one sentence on what grep's status does at the
`&&`. The sidebar carries the story and the quoted scar. The warning keeps
its second sentence, the remedy, which is the part not said elsewhere.

**R5 (should). The jargon section spends its weight on internals.** The
counts by match type (254, "45 match as words and 8 as phrases"), the
column list, and "Running the lint by hand" (316 to 318: `--json`,
`--max-findings`) serve a tool author, not a book author. What the author
does with the report gets one sentence (314): "Read the report after a
long revision anyway." Fix: cut the match-type counts and fold the
hand-run options into one sentence or a cross-reference to Appendix A.
Spend the words on reading *build/jargon-report.txt*: what an inspect
sighting asks, and the choice between rewriting and `jargon-allow`.

## 4. Opening and closing

The "In this chapter" box (3 to 15) lists the nine A-heads exactly. The
orientation (17) is five sentences under no heading and says what and
why; its first sentence carries the overclaim in P1.

**O1 (should). The chapter closes on two pointers.** Line 530 points to
Chapter 14, and 532 points to Chapter 7. Fix: move the CI sentence (530)
up into the section's body, after the shell paragraph (498), as the third
reader of the exit status. Then close on 532 alone.

## 5. Numbered items

Tables 6.1 to 6.7, Examples 6.1 to 6.15, and Figures 6.1 to 6.3 are each
referred to in prose before they appear. The unnumbered paragraph message
at 225 is under six lines and is not referred to again; it is fine.

**N1 (should). Figure 6.3 duplicates Example 6.12 line for line.** Line
433 introduces both together, and the art directive (454) copies the
example's text. The design row lists only Figures 6.1 and 6.2; the brief
added 6.3. The reader gains nothing from the second copy. Fix: the
managing editor drops Figure 6.3 and keeps the example, which the reader
can copy and which the P2 framing sentence can annotate. If the figure
stays, the example goes, and the prose at 452 refers to the figure.

**N2 (should). Table 6.7 says it "collects the diagnostic forms in this
chapter" (476), and leaves out about half.** Missing: `missing source
file`, `suspiciously short source`, `no level-1 heading`, `contains em
dash`, `contains en dash`, the curly-quote diagnostic, the phrase-battery
labels, the three self-test failures, the malformed-pattern refusal, and
the release refusal. A reader matching a line of output to its rule will
not find these. Fix: either complete the table or reword 476 to "the forms
you are most likely to meet", and add a cross-reference to Appendix C,
*Messages and refusals*, which carries the full list.

## 6. Length

`press wordcount`: 6,167 against a target of 5,500, 12.1 percent over,
inside the 15 percent band (4,675 to 6,325). Counted as prose alone (code,
tables, captions, art directives, and the index comment removed; sidebar,
tips, and footnotes kept), the chapter is about 4,600 words, 16 percent
under. That is the same split as in Chapters 3 and 4: the brief's gate
counts tables, while the design and brief say the target is for prose. The
controller should settle which measure governs. The cuts in R1 to R5
remove a few hundred words of repetition, and C1, P1, P4, and R5 ask for
a smaller amount of new prose. On `press wordcount` the chapter stays
inside the band either way.

## The one change that would most improve the chapter

Fix P1. The chapter's central picture, Figure 6.1 and its caption, tells
the author that every edition passes through the checker. Line 154 says a
bare `press pdf` skips the self-test, and the fact file forbids "on every
build". An author who believes the picture will build with `press pdf`
and think the manuscript is checked. Get the fact of what each format
target runs, then make the orientation, line 36, the figure, and the exit
status section say the same thing.
