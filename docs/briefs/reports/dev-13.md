# Developmental edit: Chapter 13, Registrations

Desk: developmental editor. File: `book/chapters/13-registrations.md`
(304 lines). I read it as the design's reader would: an author who can use
a shell and does not know TeX. Line numbers refer to the file as read.

Status: DONE_WITH_CONCERNS. 0 block, 14 should.

## 1. Coverage

All nine A-heads from the brief are present, in order, in sentence case,
with prose between every pair of headings. Every core topic in the design
row is reached: the governing rule, ISBN blocks and `press isbn`, ISSN and
LCCN, `retail`, `press pcn`, `press onix`, `press lookup`, where each
number lands (colophon, EPUB, barcode), and the order of operations. The
figure, the sidebar (the suggested pending-placeholder rationale), six
tips and warnings, and three footnotes are present. No block.

| A-head | Line | Does the section deliver? |
|---|---|---|
| The governing rule | 19 | Yes. Table 13.1 and Example 13.1 set up the rule and the placeholder cleanly. |
| ISBNs | 44 | Mostly. The block rules and the worked digit count (line 67) are the chapter's best teaching. The reader never sees a successful assignment or the number it produces (P3). |
| ISSN and LCCN | 100 | Partly. The checks are clear, but the reader never learns where an ISSN is stored (P5), and the section spends its weight on arithmetic (R2). |
| The retail flag | 132 | Partly. The switch and its message are there. The reader cannot tell which numbers a retail edition demands (P1). |
| Preassigned control numbers | 146 | Yes. Example 13.5 and the two quoted lines make the form followable. Its state disagrees with the Alice book of Chapter 10 (P2). |
| ONIX | 187 | Mostly. Table 13.3 is complete. Two of its cells leave the reader guessing (P7). |
| Looking numbers up | 213 | Partly. The limits are exhaustive and the outcomes are only named (P6, R1). |
| Where each number lands | 244 | Yes. Short, concrete, and the figure carries it. |
| Order of operations | 258 | Partly. The steps are in the right order and the procedure is missing steps the chapter itself asks for (P4). |

## 2. Path

**P1 (should). The reader cannot tell which numbers a retail edition
needs.** Line 134: "When it is `true`, the press treats the same numbers
as defects". "The same numbers" is every registration? The reader of a
novel with no series and no LCCN plan must know whether `retail: true`
refuses the book for an absent ISSN or an absent LCCN. As written, the
answer looks like yes, which would send every author to the Library of
Congress and to an ISSN agency before sale. Fix: say which keys the retail
check requires (the print ISBN, the EPUB ISBN, an LCCN if declared, and so
on). The fact file (11.4) says only "missing or pending numbers", so the
writer must get the list from the fact desk, or say plainly that a number
the book does not declare is not checked, if that is what the code does.
Do not guess.

**P2 (should). Example 13.5 shows a different book from the one the
reader has built.** Chapter 10 (lines 180 and 182 of that chapter) gives
the Alice book the publisher "Wonderland Press" and the place "Oxford".
Line 207 of this chapter relies on Alice's `site-url`. Example 13.5 and
line 150 then show "a fresh copy of the Alice book" with title `alice`,
publisher Lewis Carroll, and place "Earth", and line 177 tells the reader
to fix those placeholders. A reader who followed Chapter 10 will not see
this listing, and will wonder which Alice is real. Fix: the lead-in must
say why the example is a fresh scaffold (it is the captured output) and
say in one sentence that the Alice book as Chapter 10 left it lists
Wonderland Press and Oxford in those two fields. Rewrite line 177 to
match, and let the "Earth" footnote go if it no longer has a sentence to
hang on. Example 13.3 uses the same device and needs the same clause.

**P3 (should). The reader never sees an ISBN get assigned.** Lines 88 to
92 describe `press isbn assign` and its two refusals, and the reader never
learns what the first number looks like. The fact file (11.2) says minting
starts at publication number 0, which the chapter omits, so an author with
the example block will be surprised to receive `...-00-` as the first
title. Fix: state that minting starts at 0, and work the first number from
Example 13.2 in a sentence or a short example (the prefix, publication
`00`, and the check digit by the Chapter 12 formula). If the fact desk has
the captured output of `assign` and of `status` with a block, show them.
Do not invent their wording.

**P4 (should). The procedure is missing steps the chapter asks for.**
Lines 262 to 292.
- Step 1 has no command. Example 13.2 shows YAML, and the reader is told
  at line 31 that `press config` writes these fields. Show the two
  `press config set registrations.isbn-block...` commands, once the fact
  desk confirms the nested key form, so the procedure leads with the CLI.
- Line 238 and the tip at line 241 tell `alice` to run `press lookup lccn`
  before she stores the number. Step 4 skips it. Add it to step 4.
- Nothing rebuilds the book. The numbers reach the colophon, the barcode,
  and the EPUB only when the artifacts are built again. End with
  `press check` (which the retail flag now governs) and `press all`, in
  one step.
- A book with an ISSN has no step. Say where the ISSN goes in the order,
  or say that the order covers books, not serials.

**P5 (should). The ISSN section never says where the ISSN goes.** The key
`registrations.issn` first appears at line 221, in "Looking numbers up".
The ISSN section explains the check digit and leaves the reader with a
number and no place to put it. Fix: one sentence and one
`press config set registrations.issn ...` command in the ISSN section.
The fact file does not say who issues an ISSN. Either get that from the
fact desk or leave the issuer unnamed; do not supply it from general
knowledge.

**P6 (should). The lookup outcomes are named and not explained.** Line
238 lists `found`, `not-found`, `ambiguous`, `mismatch`, `invalid`, and
`unavailable`. The reader who gets `mismatch` does not know whether the
number is wrong, the catalog is wrong, or the record belongs to another
book, and does not know whether to store the number. Fix: a three-column
table (outcome, meaning, what to do), if the fact desk can supply the
meanings. If it cannot, say in one sentence that only `found` confirms the
number and that anything else means do not store it yet, and note the gap
in the writer's report.

**P7 (should). Two cells in Table 13.3 leave the reader guessing.**
`RecordReference` is `{base}/{slug}-{label}`, and the chapter never says
what `{label}` is. Line 207 then gives the start of the reference without
its end, so the reader cannot reconstruct one. `SentDateTime` is "The time
of the build", while the record is written when `press onix` runs, which
is not the same act in this book's vocabulary. Fix: define the label (fact
desk) or drop the pattern from the Value cell and keep the prose about the
base. Say "the time `press onix` runs".

**P8 (should). Two statements about the retail flag go beyond the fact
file.** Line 136: "no artifact gets built until you fill them". The fact
file says only that `press check` fails. Line 144 sends the reader to
Chapter 14 for "the release build that a retail flag protects", and
Chapter 14 never mentions the retail flag. A reader will look for a
connection between `registrations.retail` and the release contract that
does not exist. Fix: say `press check` refuses the book, and that any
build that runs the checker stops with it (if the fact desk confirms the
dependency edge). Drop the Chapter 14 pointer, or replace it with one
that names what Chapter 14 does cover.

**P9 (should). Two sentences raise a question and leave it.** The warning
at line 49 forbids KDP's free ISBN and gives no reason, and the reader
will want one before spending money. Line 98 says the press does the
ISBN-10 arithmetic and "You will rarely need it", which implies a command
the reader can run. None is named. Fix: give the skill's reason for the
KDP rule in a clause if the fact desk has it; otherwise attribute the rule
to the skill and leave it. Move line 98 into the footnote, and say no
target prints an ISBN-10, unless the fact desk names one.

**P10 (should). Chapter 3 is cited by the wrong title.** Line 31:
"Chapter 3, *The shape of a book*". The design gives *The shape of a book
repository*. Fix the title.

## 3. Proportion

**R1 (should). "Looking numbers up" spends its words on safeguards.**
Table 13.4 (six rows), the `<!DOCTYPE` paragraph at line 236, and the
User-Agent footnote run to about 250 words on behaviour the author never
sees and cannot change. The outcomes, which the author must act on, get
one sentence (P6). Fix: keep Table 13.4, cut line 236 to its first
sentence or into the table's Meaning cell, and spend the words on P6.

**R2 (should). The ISSN and LCCN section says the same thing twice.**
Lines 102 to 119 explain each check in prose, then Table 13.2 restates
them, and its ISBN-10 row repeats the footnote. Example 13.4 and the
invalid-cases paragraph (line 115) give a serial's check digit more room
than the ISBN's, which most readers need and which goes to Chapter 12.
Fix: keep Table 13.2 as the summary, cut line 115 to one sentence, and
let the prose carry only what the table cannot (the normalization steps,
the PCN route). The words saved pay for P5.

**R3 (should). The retail flag is short on what matters and the pending
point is made four times.** The placeholder's purpose is stated at lines
31 and 42, again at line 134, again in the sidebar, and again at line 256.
"Set the flag for the release" appears at line 144, in step 6, and at
line 294. Meanwhile the retail section never says which numbers it demands
(P1) or shows the command that sets it. Fix: let the sidebar carry the
rationale, cut the rationale sentences at line 42 and line 256 to the
facts (`[pending]` prints, the wrap shows its box), keep "for the release"
in the procedure only, and put the `press config set registrations.retail
true` command and the P1 answer in the retail section.

## 4. Opening and closing

The "In this chapter" box matches the nine A-heads exactly. The
orientation (line 17) is five sentences, says what the subject is and why
the press handles it, and has no heading above it. The close (line 296)
is the CIP paragraph, a last technical point, which the anatomy allows.
No finding.

## 5. Numbered items

Every table (13.1 to 13.4), every example (13.1 to 13.5), and Figure 13.1
is referred to in prose before it appears. Each earns its place, with
Table 13.2 subject to R2. The art directive names the archetype, lists
every box and arrow in reading order, and says what to see first. Its
colophon arrow carries all four numbers, which the fact file (9.4)
supports.

**N1 (should). Example 13.3's lead-in miscounts its own lines.** Line 77:
"We broke the output line in two to fit the page." The example shows the
message on three lines (83 to 85). Fix: "We broke the output line to fit
the page."

## 6. Length

`press wordcount`: 3,299 words against a 3,500 target, 5.7 percent under,
within the 15 percent allowance. There are about 200 words of room before
the target, and R1 to R3 free perhaps 200 more, enough for P1, P3, P5, and
P6.

## The one change

Answer, in the retail section, which numbers a retail edition requires,
and close the procedure with `press check` and `press all` so the reader
sees those numbers land. At present an author cannot tell whether going on
sale needs an ISBN only or an ISBN, an LCCN, and an ISSN, and the chapter
ends before the numbers reach a single artifact.
