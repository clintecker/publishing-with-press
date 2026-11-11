# Developmental edit: Chapter 8, Verifying the artifacts

Desk: developmental editor. File: `book/chapters/08-verifying-the-artifacts.md`
(495 lines). I read it as the design's reader would: an author who can use a
shell and does not know TeX. Line numbers refer to the file as read.

Status: DONE_WITH_CONCERNS. 0 block, 15 should.

## 1. Coverage

All nine A-heads from the brief are present, in order and in sentence case,
with prose between every pair of headings. The design row's core topics are
all reached: the philosophy, every `verify_pdf` check, every `verify_formats`
check, epubcheck and the binfmt scar, archives, pages, cross-edition
agreement, the manuscript witness, the no-stale law with which command
rebuilds what, and reading a failure. One core topic, chapter witnesses, is
named but never explained (C1).

| A-head | Line | Does the section deliver? |
|---|---|---|
| Artifacts as objects | 22 | Yes. The law, the 11.5 percent incident, and the independent-tools argument together give the chapter its why. Table 8.1 is a good map. |
| What the PDF verifier checks | 53 | Yes, thoroughly. Table 8.2 in run order, then each group's messages. Runs long on the detector self-test (R1). |
| What the formats verifier checks | 203 | Yes. The three witnesses and Table 8.3 cover every edition. |
| epubcheck | 269 | Yes. Table 8.4, the two missing-tool messages, and the binfmt scar told plainly. |
| Archives and the source edition | 304 | Yes. Reader zip, source zip policy, the secret patterns, and the sources companion. Missing a success line (N2). |
| The pages verifier | 338 | Mostly. The reference failures are clear. The commerce checks rely on a term the reader has not been given (P5). |
| Witnesses and cross-edition agreement | 371 | Partly. The window rule is the best explanation in the chapter, but the opening half restates earlier sections (R2) and the chapter witness stays undefined (C1). |
| The no-stale law | 404 | Yes. The `press verify-formats` stale-PDF edge (line 415) is the most useful warning in the chapter. |
| Reading a failure | 435 | Partly. Its first rule of thumb does not hold for the chapter's own messages (P1). |

**C1 (should). Chapter witnesses are used and never defined.** Line 257
("Each chapter's witness must appear on exactly one page") and Table 8.6,
line 380 ("Each chapter has a witness line") both assume the reader knows
what a chapter's witness is. The chapter defines the manuscript witness
with care at line 213 (longest plain line, 40 characters, chosen by press)
and gives the chapter witness nothing. The reader will ask whether it is
the same rule applied per chapter and whether they can steer it. Fix: at
first use (line 257) say in one sentence how press picks a chapter's
witness. If the fact file does not state the rule (I find only its uses at
facts-08 lines 72 and 74), the writer should ask the managing editor for it
rather than guess. Without it, say plainly that press derives one line per
chapter and the author does not choose it.

## 2. Path

**P1 (should). The "first words" rule at line 437 is false for most of the
chapter's own messages.** "Every verifier message names its subject in its
first words. A message that starts with `PDF`, `pdffonts`, ... comes from
`verify_pdf`." But the `verify_pdf` messages quoted earlier begin
`missing text sentinel`, `suspiciously short`, `unexpected trim size`,
`unembedded fonts`, `apparently blank`, `ink touches`, and `rendered N
pages`. Table 8.7's first four rows start with none of the listed prefixes.
A reader who applies the rule to the message in Figure 8.3 gets no answer.
Fix: give the reader a rule that holds. The target that failed names the
verifier (`press verify` runs only `verify_pdf`, and so on, per Figure 8.2),
and under `press all` the verifiers run in a known order (line 423).
Alternatively, the subject (PDF, EPUB, site, an edition label) appears
somewhere in the message, not in its first words. Then the paragraph should
point at Table 8.1.

**P2 (should). Witness vocabulary appears before its definitions.** Table
8.1, line 38: "for the title, the sentinels, and the witness". Table 8.2,
line 59: "Release witnesses". "Page floor" appears at line 59 and is first
glossed at line 102. The manuscript witness is defined at line 213, 175
lines after the reader first meets "the witness". Fix: in Table 8.1 write
"a line press picks from the manuscript" or forward-point to the section
"The three witnesses". In Table 8.2 name the row by what it checks
(sentinel count and page floor) and gloss the floor as
`verify-min-pages` there.

**P3 (should). TeX vocabulary the reader does not have.** The reader does
not know TeX (design section 2). Line 155 hangs the print exception on
"the verso that `\mainmatter` leaves". The sidebar (line 132 onward) uses
"hyperref package", "the anchor of a float", and "the caption package"
without a word of gloss. Fix: line 155 must say what happens in book
terms, that the main text starts on a right-hand page so the page before it
may be empty, and can then name `\mainmatter` in passing or drop it. In the
sidebar, gloss "float" once (a figure LaTeX is free to move) and let
"hyperref" stand as the name of the link package.

**P4 (should). "The authoring sandbox" at line 139 is undefined.** "On the
authoring sandbox, a helper script does the rendering when it is present."
The reader has no sandbox, and the sentence makes them wonder if they
should have one. Fix: say whose sandbox it is (the environment the press
was developed in) or say only that press renders with `pdftoppm` and keep
the history in footnote `[^fallback]`.

**P5 (should). Commerce arrives with no setup.** Line 363: "Three more
checks concern commerce. A call to buy must appear exactly when the book
enables commerce, the generated policy pages must disclose the seller..."
The reader has met `commerce` only as one name in a list of mappings in
Chapter 3 (line 255 there). "Call to buy", "policy pages", and "the seller"
are new. Line 423's commerce gate has the same problem. Fix: one sentence
saying that a book can turn on print ordering in *config/metadata.yaml*,
that the Alice example does not, and that Chapter 12 covers it. Then the
three checks read as conditional and the reader can skip them.

**P6 (should). Line 74 says the reverse of what the table shows.** "Every
check in Table 8.2 except the last applies to it." The next sentence
corrects it ("the print checks belong to the print profile only"), so the
row "Print profile" is also reading-profile-exempt. The reader must
reconcile two sentences against a twelve-row table. Fix: say it once.
Both profiles run every row except the last two, and each of those two
belongs to one profile.

**P7 (should, escalate to the managing editor). The running sample fails
its own page floor.** The chapter configures Alice with `verify-min-pages:
24` (line 110, and Chapter 3, line 245, has the same setting). The
managing editor's capture of the real Alice example (facts-08 supplement
S1, and facts-01 line 498) reports `23 pages`. Under the chapter's own
settings that book fails with `suspiciously short PDF: 23 pages (minimum
24)`. Once N2 is adopted, the chapter will contradict itself on the page.
Fix: the managing editor decides across Chapters 3, 6, and 8. Either show
the real capture with a floor the book meets, or keep 24 and say the
sample book is padded to release length. The writer of Chapter 8 should
not choose alone.

## 3. Proportion

**R1 (should). The detector self-test runs long for what the author can do
with it.** Lines 80 to 89 spend three paragraphs, a code block, and the
detector's thresholds (1.2, 249, 252.5) on a check whose failure, as line
89 says, "says nothing about your book". The author needs two facts: the
check exists, and its messages mean the machine is at fault. Fix: keep
the "a detector that called every page inked" argument and the two
messages. Cut the threshold sentence or move it to a footnote. Spend the
words saved on C1 and P1.

**R2 (should). "Witnesses and cross-edition agreement" opens by restating.**
Table 8.6 collects witnesses the reader met a page earlier. Line 385 lists
the four places sentinels are checked, which Figure 8.1 (line 48) and the
section "What the PDF verifier checks" already gave. Line 387 restates the
release floor from line 78 and Chapter 3. Fix: keep Table 8.6, since a
table that gathers is fair at this point, but cut line 385 down to its
last sentence, the useful inference ("passes the checker and fails
`verify_pdf` ... the PDF is wrong"), and cut line 387 to a cross-reference.
The agreement B-head then carries the section, as it should.

**R3 (should). Signpost sentence at line 205.** "This section covers the
first verifier, and the section "Archives and the source edition" later in
this chapter covers the second." That is writing about the document. The
reader already has the A-head. Fix: delete it, or fold the forward
reference into the previous sentence as a clause about `verify_archives`.

**R4 (should). The pages verifier's second half is a list in prose.** Lines
353 to 363 run a series of short "must" declaratives (downloads, sentinels,
JSON-LD, Open Graph, Twitter card, `og:image`, canonical, sitemap, head
leaks, three commerce checks). None of it argues. The reader cannot tell
which matter for a book like Alice (no `site-url`, no commerce) and which
do not apply. Fix: either make it a table in the style of Table 8.5
(check, when it applies, failure), or regroup the prose by condition:
always, when `site-url` is set, when commerce is on. The head-leak
paragraph earns its prose and should stay.

## 4. Opening and closing

No findings. The "In this chapter" box matches the nine A-heads exactly.
The orientation (line 17) is five sentences with no heading above it, and it
says what (programs that open and compare artifacts) and why (exit status
proves nothing about the pages). The plate sits between the orientation and
the first A-head, which satisfies the brief. The close (line 485) is a
single forward pointer to Chapter 9 with no recap.

## 5. Numbered items

All seven tables, four examples, and three figures are referred to in the
prose before they appear. Every table has a Meaning-style column in
sentences. Tables 8.1, 8.2, 8.5, and 8.7 earn their place clearly.

**N1 (should). Figure 8.1's columns do not match the five verifiers the
chapter just named.** Line 28 names five verifiers, `verify_coverwrap`
among them, and Table 8.1 gives it a row. The matrix (line 50) has a
column for "verify_pdf print profile" instead and no column for
`verify_coverwrap`. The brief prescribed those columns, so the directive
is right to follow it. The reader still sees five verifiers in the prose
and a different five in the figure. Fix: one clause in the prose at line
48 saying the figure treats the print profile as its own column and
leaves `verify_coverwrap` to Chapter 12.

**N2 (should). The chapter shows forms where real runs now exist.**
Examples 8.1 and 8.2 give the success lines as templates with `<pdf>`,
`N`, `K`, `E`, and `C`. The `verify_archives` success line is never shown.
The managing editor's supplement to facts-08 (S1 and S2) now carries
verbatim captures of `press verify` and `press verify-formats` on the
Alice example, including `Verified archives: ...` and the real
epubcheck warning. The brief asks Figure 8.3 to use a captured run "if
present". A reader learns what success looks like faster from the real
line than from its grammar. Fix: show S1 and S2 (slug changed to
`alice`) as numbered examples next to, or instead of, Examples 8.1 and
8.2, and add the archives line to the section "Archives and the source
edition". Figure 8.3 may keep the failure framing, since "Reading a
failure" needs one, but the managing editor should confirm that this
choice stands against the brief's wording. P7 must be settled first.

**N3 (should). Example 8.4 repeats Chapter 2 without saying so.** Chapter 2
covers `press doctor` and its report (its Figure 2.1 and Table 2.3). Line
439 introduces the example as if new. Fix: add "as Chapter 2, *Installing
press*, describes" and cut the example to the lines this chapter needs,
the four poppler tools and epubcheck, which it nearly does already.
Otherwise it earns its place: it gives the reader the next command after
a machine fault.

## 6. Length

`press wordcount` reports 6,765 words against a target of 6,000, which is
12.8 percent over and inside the 15 percent band. Carrying out R1 to R4
would cut roughly 300 to 400 words, and C1, P1, P3, P5, and N2 would add
back about as many. The chapter should land near where it is now.

## The one change

Replace the template success lines with the real Alice captures (N2), once
the managing editor settles the 23-page floor conflict (P7). That gives
the reader the concrete picture of a passing run that the whole chapter
argues for, and it brings the chapter's evidence up to its own law.
