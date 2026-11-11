# Re-review: Chapter 7, Building the editions

File: `book/chapters/07-building-the-editions.md` (513 lines, as revised).
Checked against facts-07, dev-07, copy-07, type-07, the Revision section of
report-07, the last sixty lines of the production ledger, and facts-07 S1 to
S3. The facts-C source for `press wordcount` (U10) and the facts-12 source for
print ordering (P1) are admissible under the shared-fact-base ruling.

## Gates

- `~/code/.pwp-venv/bin/press check`: exit 0. Source checks, self-test (29
  fixtures), editorial checks (23 files), and jargon lint all pass. Nothing
  names chapter 7.
- `python3 tools/ste_check.py`: 46 findings, 435 sentences, average 12.8
  words. Every paragraph-length finding (53, 84, 118, 375) is an `art:`
  comment. Every prose paragraph runs six sentences or fewer. The
  sentence-length findings at 202 and 242 are splitter fusions across `(1),`
  and a footnote marker. The rest are under 30 words, or are list items (412,
  415), the In-this-chapter box, or the index comment. The `-ing` forms are
  headings and titles. "however", "therefore", "whether", and "verify" (a
  target name) are allowed. "are cleaned" sits in a quotation, and the
  semicolon is in the index comment.
- Mechanical: no "ship/shipped", `<root>`, `N.Ns`, or invented defaults paths.
  All eleven fences are tagged `text`. No code line is over 64 columns. No
  list item has a bold label. Each of the four images is followed by one blank
  line and then its `art:` comment. Table separators set column 1 to 24
  (7.1), 30 (7.2), 32 (7.3), and 16 (7.4, 7.5) dashes. No non-ASCII outside
  fences.

## The S1 section

"What press all does, in order" is built on Example 7.4, the S1 capture. The
slug is `alice`, and line 57 labels the captures as "the press's own
three-chapter Alice example". The capture is elided with `...` to 64 columns
and keeps the three `¶` phase lines, the `stitched` and `assembled` reports,
`pandoc took 26.7s`, the source zip's path and its `archived` line, and the
closing line. The six steps are walked against it (409 to 416). Step 2 names
the S1 order. The commerce-gate section shows Alice's real line (427 to 428),
then the advisory line for an ordering-enabled book. Figure 7.3's directive
(118) uses S2's real template and rendered lines, and the title-page entry is
the one dropped.

## Findings

| Desk | No. | Sev. | Status | Where / note |
|---|---|---|---|---|
| facts | U1 `sh -x` | should | resolved | cut |
| facts | U2 latexmk aux files | should | resolved | 202, sidebar 207 |
| facts | U3 font scan | should | resolved | 212, the fix text |
| facts | U4 "first book" | should | resolved | sidebar opens on the fact |
| facts | U5 epoch rationale | should | resolved | footnote keeps the date only |
| facts | U6 no own copy | should | resolved | 78 "come with the press" |
| facts | U7 reader stylesheet | should | resolved | 250 |
| facts | U8 build/ rewritten | should | resolved | 484 |
| facts | U9 stops at first failure | should | resolved | 371, 411; arc "fail, under PRESS_RELEASE" |
| facts | U10 wordcount | should | resolved | S3 verbatim; strip line kept (facts-C admissible) |
| facts | U11 no cover | should | resolved | 244 (see may 1) |
| facts | U12 "Fig-ure" happened | should | resolved | 185 "can never" |
| facts | C1 plus-sign lines | blocks | resolved | 277, 450 |
| facts | C2 commerce gate on Alice | blocks | resolved | 424 to 438; figure caption text |
| facts | C3 "Mr." | blocks | resolved | Table 7.3 |
| facts | C4 input order | blocks | resolved | 70 |
| facts | C5 `press all` row | blocks | resolved | 40 |
| facts | C6 only non-pandoc target | blocks | resolved | 277 |
| facts | C7 add and commit / .gitignore | blocks | resolved | 285, Tip 288; S1 excluded-dirs line |
| facts | C8 never builds print | blocks | resolved | 442, with the B.13 exception |
| facts | D1 EPUB echo | should | resolved | 224 to 230, real line |
| facts | D2 time line, "prints" | should | resolved | 74, 452 |
| facts | D3 Figure 7.3 lines | should | resolved | 118 |
| facts | D4 Lua coverage warning | should | resolved | cut (dev R2) |
| facts | D5 who owns what | should | resolved | 22 (verification pipeline added; "editions" for formats is the book's term) |
| facts | D6 "press documentation" | should | resolved | 24 |
| facts | D7 eight artifacts | should | resolved | sentence cut (dev R7) |
| facts | D8 sources conditional | should | resolved | 363, 367 |
| facts | D9 "small TeX files" | should | resolved | 191 |
| facts | D10 verify rebuilds | should | resolved | 337 |
| facts | M1 S1 capture | should | resolved | Example 7.4 |
| facts | M2 step-2 order | should | resolved | 412 |
| facts | M3 phase and closing lines | should | resolved | 454 |
| facts | M4 rendered additions | should | resolved | Example 7.3, 120, 157 |
| facts | M5 `--epub-metadata` | should | resolved | 227, 236 |
| facts | M6 source report | should | resolved | 285 |
| facts | M7 policy pages | may | declined-accepted | optional; Alice has no ordering |
| facts | M8 one timing | should | resolved | 74 |
| dev | C1 misplaced B-heads | should | resolved | moved under 369 |
| dev | C2 real captures | should | resolved | Examples 7.1, 7.2 to 7.4, S3 |
| dev | P1 gate undefined | should | resolved | 424 (facts-12) |
| dev | P2 paste fails | should | resolved | 72, 232 |
| dev | P3 step 2 contents | should | resolved | 412 |
| dev | P4 press-repo paths | should | resolved | 78, 293 |
| dev | P5 Release, Pages | should | resolved | 314 |
| dev | P6 table cells, reader metadata | should | declined-accepted | no fact; bare clauses promise nothing more, as dev allowed |
| dev | P7 Table 7.1 row | should | resolved | 40 |
| dev | P8 rights fields | should | resolved | 232 (`copyright`, `publisher` per facts-03) |
| dev | P9 pointer placement | should | resolved | 165 |
| dev | P10 plus-sign rule | should | resolved | 450, 454 |
| dev | R1 TeX internals | should | resolved | 183 to 185 |
| dev | R2 tests, warning | should | resolved | 185, footnote |
| dev | R3 sidebar repeats | should | resolved | 202 / 204 to 210 |
| dev | R4 tips repeat | should | resolved | 215, 288 |
| dev | R5 Python scar | should | resolved | 267 |
| dev | R6 sources twice | should | resolved | 367 only |
| dev | R7 table read aloud | should | resolved | 312 |
| dev | R8 press-util numbers | should | resolved | Table 7.3 |
| dev | R9 documentation sentences | should | resolved | both cut |
| dev | R10 environment table | should | resolved | 149 to 155 |
| dev | N1 figure/list names | should | resolved | 375, 411 to 416 |
| dev | N2 Figure 7.3 schematic | should | resolved | 118 |
| copy | 1 "ships" | blocks | resolved | 78 |
| copy | 2 "shipped" | blocks | resolved | 88 |
| copy | 3 one-line closer | blocks | resolved | 277 ends on "in one file" |
| copy | 4 bold labels | blocks | resolved | 411 to 416 |
| copy | 5 to 8 | should | resolved | 22, 22, 45, 112 |
| copy | 9 seven-sentence paragraph | should | resolved | 112 / 114 |
| copy | 10 artifact, not edition | should | resolved | 49 |
| copy | 11 edition, artifact defined | should | resolved | 18, 49 |
| copy | 12 to 14, 16 two ideas | should | resolved | 22, 70, 80, 163 |
| copy | 15 sidebar length | should | resolved | two paragraphs of four |
| copy | 17 book repository | should | resolved | 273 |
| copy | 18 Tip repeats | should | resolved | 288 |
| copy | 19 invariant | should | resolved | 339 |
| copy | 20 synonym rotation | should | resolved | 347 |
| copy | 21 cover wrap | should | resolved | 38, 349, 355 |
| copy | 22 hidden actor | should | resolved | 359 (see may 2) |
| copy | 23 to 25 refuses | should | resolved | 411, 418, 438 |
| copy | 26 timing sentence | should | resolved | cut |
| copy | 27 condition first | should | resolved | 456 |
| copy | 28 `art:` comment | should | resolved | 507 |
| copy | 29 Source edition | should | resolved | 273 onward |
| copy | 30 date order | should | resolved | 159 |
| copy | 31 hidden actor | should | resolved | 314 |
| copy | 32 American spelling | should | resolved | art comments |
| type | 1 art comment placement (x4) | blocks | resolved | image, blank line, comment (ledger correction) |
| type | 2 untagged fences | should | resolved | 11 of 11 tagged |
| type | 3 rights line 66 columns | should | resolved | moved to prose |
| type | 4 advisory line clipped | should | resolved | 434 to 435, with a note |
| type | 5 to 8 separators | should | resolved | 24 / 30 / 32 / 16 dashes |
| type | 9 lead line at page foot | should | declined-accepted | that lead and session are gone; recheck page flow after PNGs land |
| type | 10 Example 7.5 split | should | declined-accepted | fence shortened; recheck after PNGs |
| type | 11 Table 7.1 split | should | declined-accepted | desk said no markup fix; recheck after PNGs |
| ledger | footnote labels `7-` | should | **open** | see O1 |
| ledger | landing-page edition names | should | **open** | see O2 |

## Open items

**O1 (should, ledger convention).** Footnote labels are not prefixed with the
chapter number: `[^epoch]` (149, 159), `[^lua]` (185, 187), `[^rsc]` (242,
246). No label collides yet, but the convention is book-wide and markup.md
states it. Fix: rename them `[^7-epoch]`, `[^7-lua]`, `[^7-rsc]`, both at the
reference and at the note.

**O2 (should, ledger ruling).** The ledger rules that edition names are the
press's landing-page names, glossed once per chapter. The chapter uses "the
Source edition" correctly, but names the others only by format: "the Markdown
edition" (273, 275), "the text edition", "the Word edition" (273, 279). It
never gives Print, Circulating, Single-leaf, Manuscript, Telegraphic, Office,
or Chapter. Chapters 1 and 3 give them. Fix: gloss them once, best after
Table 7.1 or at 273. For example, after line 24: "The landing page names these
editions the Print, Circulating, Single-leaf, Manuscript, Telegraphic, Office,
and Chapter editions, and the Source edition." Then add the landing-page name
in parentheses at the first mention of each portable edition in 273, such as
"the Markdown edition (the Manuscript edition)". The format names can stay
after that.

## Mays (not counted)

1. 244: "If the book supplies *assets/cover.jpg*, the press names it as the
   `epub-cover-image`. The press names the cover only when that file is
   present." The second sentence repeats the first. Cut it.
2. 359: "The press generates them again for every pandoc build. Before every
   pandoc build, the press calls the same function, ..." The phrase "every
   pandoc build" appears twice in a row. Join them: "The press generates them
   again before every pandoc build, through one function that does three
   things in order:"
3. 415: the verify-step list item runs 31 words with two ideas. Split it after
   "in that order".

## Read as a reader

The chapter now follows the reader's own run. Real echo lines, real defaults,
and a real `press all` sit at the points where the reader needs them, and the
log and the *dist/* tree follow the command that produces them. The commerce
gate is defined before Alice's line appears. The scars are told as mechanism,
not as code. Nothing reads as invented.

## Verdict

APPROVED. No open blocks. Two open shoulds (O1, O2), both mechanical, which
the continuity pass or the writer can apply without another re-review.
