# Developmental edit: Chapter 14, Continuous integration and the release contract

Desk: developmental editor. File: `book/chapters/14-continuous-integration.md`
(448 lines). I read it as the design's reader would: an author who can use
a shell and does not know TeX, and as the design's second reader for
Chapters 14 to 16, a developer asked to keep a group's book builds running.
Line numbers refer to the file as read.

Status: DONE_WITH_CONCERNS. 0 block, 13 should.

## 1. Coverage

All ten A-heads from the brief are present, in order, in sentence case,
with prose between every pair of headings. Every core topic in the design
row is reached: `book.yml`; the reusable workflow and the composite action;
self-checkout install and the hash lock; the toolchain image pinned by
digest; the Pages deploy; receipts; floating and immutable tags; the
release contract workflow; what `PRESS_RELEASE` enforces; `press migrate`.
Three figures, the suggested sidebar (war story 19), seven tips and
warnings, and four footnotes are present. No block.

| A-head | Line | Does the section deliver? |
|---|---|---|
| What a book's CI is | 20 | Yes. Triggers, permissions, the first-law reason, and the topology figure. |
| The reusable workflow | 40 | Yes. Table 14.1 and the five build steps are the chapter's clearest teaching. |
| The composite action | 74 | Yes, and it keeps Chapter 2's promise. It runs long on the run-step guard (R1) and elides the line the hash-lock subsection rests on (P3). |
| The toolchain image | 153 | Yes. It keeps Chapter 2's digest promise exactly (see Continuity). |
| Receipts | 210 | Yes for what a receipt is. It leans on "the release contract" before that section (P5). |
| Tags: floating and immutable | 226 | Mostly. Table 14.2 reads as a rule for the reader's own tags (P6). |
| The release contract | 274 | Yes. |
| Release builds | 328 | Partly. The procedure has gaps at the step the author actually performs (P1, P2). |
| Pages | 370 | Mostly. The last paragraph asserts a safety it does not show (P7). |
| Moving between majors | 380 | Yes in prose. Example 14.5 documents a behavior the fact file lists as a bug (N1). |

### Continuity: the promises other chapters made

- **Chapter 2 l.315, where the digest is found.** Kept. Lines 159 to 183
  name the `image:` line of the press's *build.yml* at the pinned tag,
  break the value at its punctuation, and Example 14.4 substitutes it for
  `:latest` with the matching three-part tag, as Chapter 2 promised. The
  continuity note's caution is obeyed: line 183 says the release notes do
  not carry the digest and sends the reader to the workflow and the
  receipt, never the CHANGELOG.
- **Chapter 2 l.134, the composite action in detail.** Kept. Lines 74 to
  149 cover the self-checkout install, the action-ref pin, the hash lock,
  and the run step. Line 76 ("The reusable workflow runs it in its second
  step, so a book never names it") agrees with Chapter 2 l.134's "the piece
  of the press that the reusable workflow runs", and with Chapter 3's "the
  book never names either one".
- **Chapter 1 l.244** (the CI build step by step), **Chapter 1 l.294** (the
  pin mechanism), **Chapter 3 l.599** (PRESS_RELEASE, release notes from
  *CHANGELOG.md*, the Pages bundle), **Chapter 6 l.475** (the reusable
  workflow runs `press all`), **Chapter 7 l.316 and l.440** (the GitHub
  Release, the Pages site, the release build). All kept.
- Line 376 cites Chapter 1 for the Pages Source setting. Chapter 3 l.601
  gives the same instruction in the book-repository chapter, which is the
  better home for the citation. May; for the continuity desk.

## 2. Path

**P1 (should), line 342.** "Watch the run on `printshop`." The reader has
not been told where a run is watched (the repository's Actions tab), and
step 2 pushes `main` and a tag in one command, which starts two runs, one
that deploys Pages and one that releases. "The build job runs first, and
the release job runs after it" describes only the tag run. Fix: name where
the run appears, and say that the push starts two runs and what each one
does.

**P2 (should), lines 330 to 346.** The section that the author will use on
release day never shows what failure on the first tag looks like. The tip
at 345 warns that a fresh book's draft settings "fail on the first tag",
and the refusal text exists (continuity bible, "Release witnesses and
refusal", due 14). Fix: show the refusal as it appears in the run, two or
three lines, and say what to change before re-tagging (including that the
tag must be deleted or a new one cut, if the fact file says which).

**P3 (should), line 113.** "Its elided line passes `--require-hashes -r`
with the file ..." The subsection about the hash lock rests on the one
line Example 14.1 cut. The reader is asked to trust a line they cannot
see. Fix: restore that line in Example 14.1 (folded if it is wide) and
elide something else, so the example shows what the subsection explains.

**P4 (should), lines 59 and 64.** `PRESS_RELEASE` is introduced in the
build job, with its expression explained, but what it changes waits
until "Release builds" with no pointer. A reader at line 64 knows how the
value is computed and not why it matters. Fix: one clause pointing to the
section "Release builds" later in this chapter.

**P5 (should), line 216.** "The release contract assembles this receipt.
It builds the wheel, downloads the artifacts ..." The release contract's
steps are described here before its own section (line 274) and then again
in its step 4 (line 281). Fix: say here only that the release contract
assembles the receipt, as described in the section "The release contract"
later in this chapter, and keep the mechanics in one place.

**P6 (should), lines 250 to 262.** Table 14.2 gives "the press's release
tag grammar" under an A-head the author reads as being about their own
tags, in the chapter that later tells them to `git tag v1.0.0`. Nothing
says whether a book's tags must obey it. The book's CI triggers on any tag
starting with `v`, so a reader may wrongly think `v1.0.0-rc1` is refused
for their book. Fix: one sentence stating that the grammar governs the
press's own release tags and that a book's CI treats any tag beginning
with `v` as a release.

**P7 (should), line 378.** "so every tagged release points at downloads
that a push to `main` deploys." The paragraph asserts the links work, but
the Pages site always shows the newest `main` (line 374), so the links in
an old release's notes serve whatever `main` now holds, while the files
attached to the release stay fixed. The reader cannot tell which copy is
the release. Fix: say which copy the "Public downloads" links serve once
`main` moves on, and that the files attached to the GitHub Release are the
fixed ones, if the fact file supports it. If it does not, cut the
conclusion and keep the two facts.

**P8 (should), line 68.** "The reader site already travels in *dist/* as
*alice-site.zip*, the Chapter edition (the reader site and its zip), and
the Pages bundle ..." The parenthetical gloss inside an appositive makes
the reader parse three names for two things. Fix: name the Chapter
edition once, then say which directory is left out and why.

**P9 (may), lines 197 to 200.** Example 14.4 installs press with `pip
install 'press @ git+...'`, ninety lines after a warning (line 108) never
to install press from a Git URL. The warning is scoped to the install step
of the action, and Chapter 2's Table 2.2 sanctions the Git form locally,
but the reader meets the two side by side. Fix: one clause in the prose
after the example saying that a local build installs from Git and only CI
uses the self-checkout.

## 3. Proportion

**R1 (should), lines 121 to 149.** "The run step" spends about 330 words,
an example, and a refusal on an input guard that, by line 149's own
admission, a book cannot reach ("A book cannot set the input at all").
For this chapter's readers it is the least useful mechanism in the
composite action. Fix: keep the environment-variable reason and the
refusal message, cut the regex walk-through and the `read -r -a`
paragraph to a sentence, and give the words to Release builds (P1, P2).

**R2 (should), lines 105 and 108.** The paragraph at 105 quotes the
self-checkout law and then explains its two halves; the warning at 108
restates both halves again in nearly the same words. Fix: the paragraph
should carry the reason and the warning only the instruction, or the
other way round, but not both.

**R3 (should), sections 6 to 7 against 8.** The press-maintainer material
(tag grammar, platform rulesets, the release contract's five steps, Table
14.3, the state machine, recovery, the sidebar) runs to roughly 1,700
words. "Release builds", the procedure every author performs, runs to
about 550 and delegates its substance to Chapters 6 and 7. The design row
asks for all of it, so nothing should go, but the balance tilts toward the
press's release and away from the book's. Fix: the words saved by R1 and
R2 go to Release builds, specifically P1 and P2.

## 4. Opening and closing

The "In this chapter" box lists all ten A-heads in order and matches them
exactly. The orientation paragraph (line 18) has no heading above it, is
five sentences, and says what and why: the book's CI delegates, the press
does the work, and the chapter follows the Alice cast through it. The
close (line 444) is the last technical point, that `alice`'s book stays on
`v3` and its digest until she runs `apply`; only a footnote and the index
comment follow. No finding.

## 5. Numbered items

Every table, example, and figure is referred to before it appears: Table
14.1 (l.44/46), Example 14.1 (l.76/78), Example 14.2 (l.123/125), Example
14.3 (l.161/163), Example 14.4 (l.187/189), Table 14.2 (l.252/254), Table
14.3 (l.290/292), Table 14.4 (l.382/384), Example 14.5 (l.417/419),
`@fig:ci-topology` (l.32/34), `@fig:resolving-v3` (l.232/234),
`@fig:release-state-machine` (l.303/305). The seven unnumbered fences are
each six lines or fewer and not referred to again.

**N1 (should), lines 417 to 444, Example 14.5.** The example is the
fact file's capture of `press migrate` on a v3 book proposing v4, and the
fact file's section 20.B.21 lists exactly that ("`migrate plan` on a v3
book proposes v4, which does not exist") among behaviors that look like
bugs: "Do not document them as features." The prose at 417 explains the
output as designed ("because it always proposes the current major plus
one"), and the example sends the reader to *docs/MIGRATION.md* "for what
v4 changes", which does not exist. "Do not apply this plan" is an honest
patch, but the brief forbids stating the behavior at all. Fix: cut Example
14.5 and its explanatory paragraph at 444; describe what the plan reports
in prose from fact-file 12.6 (the pins found, each rewrite, the override
files to recheck, the dry-run rule), which the section already half does
at 395 to 397. The close then moves to the end of "What each step up
changes", or to the warning at 414; the writer should make sure the
chapter still ends on a technical point.

**N2 (should), figure numbers.** The brief and the design row number the
release state machine 14.2 and the resolution flowchart 14.3, and the
files are named *14-02-release-state-machine.png* and
*14-03-resolving-v3.png*. The A-head order puts `@fig:resolving-v3`
(line 234, under "Tags") before `@fig:release-state-machine` (line 305,
under "The release contract"). The press's figure filter numbers by the
LaTeX figure counter, in order of appearance, so the book will print the
flowchart as Figure 14.2 and the state machine as Figure 14.3, against
their file names and the design. The writer's report lists them the
design's way, so the mismatch is not yet noticed. Fix: the A-head order
is fixed, so rename the two asset files (and the design row) to the
printed order; this is a managing-editor change, not a prose one.

All the numbered items earn their place. Table 14.2 earns it only once P6
is fixed.

## 6. Length

`press wordcount`: 5,716 against a target of 5,500, 3.9 percent over,
within the 15 percent band. The cuts in R1, R2, and N1 roughly pay for
P1 and P2.

## For the copy desk (not counted)

- Line 216 and line 286 each say "in the press's words" or quote the press
  for a sentence that would stand as plain statement; check the quotation
  rate across the chapter.
- Line 280, "60 times 30 seconds", then line 284 restates it as "half an
  hour at most"; one form is enough.
- Line 276, "proves five things in order": step 5 (upload) is not a proof.

## The one change

Rebuild "Release builds" around the author's release day: say where the
run is watched and that one push starts two runs (P1), and show the
release-witness refusal a fresh book meets on its first tag with what to
do about it (P2). Pay for it with the run-step guard (R1) and Example
14.5, which must go anyway (N1).
