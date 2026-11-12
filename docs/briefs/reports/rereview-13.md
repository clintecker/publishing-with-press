# Re-review: Chapter 13, Registrations

File: `book/chapters/13-registrations.md` (323 lines, `press wordcount`
3,268). Line numbers are `cat -n` numbers in the file as it stands; the
desk reports' numbers refer to the earlier draft (their "line 177" is now
192, "line 256" is now 273).

Verdict: **APPROVED**. Open: 0 blocks, 1 should (new, introduced by the
revision), 2 mays.

## Tools

- `press check`: fails only on `assets/woodcuts/14-02-resolving-v3.png`
  and `14-03-release-state-machine.png` ("plate never referenced by the
  manuscript"), Chapter 14's files. Nothing in this file fails.
- `tools/ste_check.py`: 17 findings (237 sentences, average 11.6 words).
  Fourteen are the kinds the writer defended and the copy desk accepted
  (quoted semicolons at 48, 190, 238; the quoted PCN passive at 190; the
  quoted first law at 263; `verify` at 44; the -ing names and headings at
  130, 230, 271; the alt text and `art:` comment at 265 and 267; the index
  comment at 323). Two are new prose findings the revision introduced
  (315, 273), listed below as N1 and N2.

## Checklist

| Check | Result |
|---|---|
| Example 13.5 labelled a fresh scaffold's output | Yes: caption "for a fresh Alice scaffold" (167); lead-in 165 names `press new alice --author "Lewis Carroll"`, says values are the metadata's and labels/layout the press's |
| Gap paragraph describes the scaffold, not the Alice book | Yes (192): "The fresh scaffold shows a different gap ... Chapters 3 and 10 replace them in the Alice book" |
| Retail section states S1 exactly | Yes (136): two real ISBNs, `isbn print missing` / `isbn epub missing`, pending listed as pending, LCCN/ISSN need not be declared, a declared one must not be `pending` |
| Retail section ends with `press check` and `press all` | Yes (155-159), and step 8 (309-313) |
| No Chapter 14 pointer for the retail flag | None in the file |
| Line 256 (now 273) says what the barcode and EPUB each carry | Yes: "The barcode carries only the print ISBN, and the EPUB identifier carries only the EPUB ISBN", then the corrected "cannot show a print ISBN that differs ..." |
| Invented details gone | Yes: "no artifact gets built", "Neither refusal changes the file", the 123X-5678 reason, "in the order the form asks", "each step needs a number", "and none can", "as the place to start", "power of ten", "the model would refuse", "time of the build", "cannot go on sale", the ISBN-10 footnote; no lookup-before-store promise |
| Heading "Where each number goes" | Yes (13, 261) |
| Sidebar closer gone | Yes; sidebar ends on the retail flag sentence (150), two paragraphs |
| "copyright page", one colophon parenthetical | Yes; the only "colophon" is the parenthetical at 269 |
| Chapter 3 by full title | Yes (31) |
| mod-11 check spelled one way | Yes (102, 104, Table 13.2 "Mod-11 check"); "160 mod 11" in Example 13.4 is arithmetic in code |
| "the book model" | The phrase is gone; 92 reads "the validated path of `press config`" (the fact desk's wording); no stray "the model" |
| Every fence `text` | Yes, all 11 |
| Footnote labels `13-` | Yes: `13-earth`, `13-agent` |
| `art:` comment after image, one blank line | Yes (265, 266 blank, 267) |
| "the Alice book" | Used throughout; no "sample" or other name |
| "the logomark" | Not used in this chapter |
| Edition names glossed once | Yes (48: "the Print edition (the PDF) and the Circulating edition (the EPUB)"); later edition sentences use "Circulating edition" (214, 271); later EPUB uses are about the file, key, or ONIX product |

## Findings

### Fact desk (`facts-13.md`)

| Desk | No. | Severity | Status | Note |
|---|---|---|---|---|
| Facts | U1 | blocks | resolved | sentence cut; 136 states S1 |
| Facts | U2 | blocks | resolved | cut (94) |
| Facts | U3 | blocks | resolved | 115 names the invalid cases only |
| Facts | U4 | blocks | resolved | "prints them as a list" (163) |
| Facts | U5 | blocks | resolved | 255 "Once she holds an LCCN, she can run ..."; tip 258 as proposed |
| Facts | U6 | blocks | resolved | 277 "in the order that the registrations skill gives" |
| Facts | U7 | blocks | resolved | each line is right per the sister fact file named; ISBN-10 footnote cut. Carrying the lines into facts-13 is the editor's, not the writer's |
| Facts | C1 | blocks | resolved | fresh scaffold labelled (79, 165, 167, 192); no invented Wonderland Press output |
| Facts | C2 | blocks | resolved | 273, as proposed |
| Facts | D1 | should | resolved | ledger ruling recorded; lead-in 165 says the values come from the metadata |
| Facts | D2 | should | resolved | "broken into three lines" (79) |
| Facts | D3 | should | resolved | 67 |
| Facts | D4 | should | resolved | 92 |
| Facts | D5 | should | resolved | "the main elements" (204, caption 222) |
| Facts | D6 | should | resolved | "a date and time, to the minute" (210) |
| Facts | D7 | should | resolved | Table 13.1 (25) |
| Facts | D8 | should | resolved | 51 |
| Facts | D9 | should | resolved | sidebar 150 |
| Facts | D10 | should | resolved | 226 |

### Developmental desk (`dev-13.md`)

| Desk | No. | Severity | Status | Note |
|---|---|---|---|---|
| Dev | P1 | should | resolved | 136 states S1 |
| Dev | P2 | should | resolved | as C1 |
| Dev | P3 | should | declined-accepted | no `press isbn assign` capture exists; minting from 0 is a section 20.B.20 item and stays unstated |
| Dev | P4 | should | resolved / declined-accepted | step 1 split (279-280); rebuild step 8; ISSN gap stated (315). No `press config set` for the nested block (form unconfirmed) and no lookup step (fact U5): both reasons hold |
| Dev | P5 | should | resolved | 102 |
| Dev | P6 | should | resolved (equivalent) | 255 "Only `found` exits 0 ..." plus tip 258; meanings not in the fact file (ruling 5) |
| Dev | P7 | should | resolved / declined-accepted | `SentDateTime` fixed; `{label}` is undefined in the fact file, and the cell keeps the code's real pattern rather than drop it. The reason holds |
| Dev | P8 | should | resolved | "no artifact gets built" cut; Chapter 14 pointer gone |
| Dev | P9 | should | resolved | KDP rule attributed to the skill (51); ISBN-10 sentence and footnote cut |
| Dev | P10 | should | resolved | 31 |
| Dev | R1 | should | resolved | DOCTYPE in Table 13.4's cell (248) |
| Dev | R2 | should | resolved | 115 is one sentence; prose keeps normalization and the PCN route |
| Dev | R3 | should | resolved (equivalent) | rationale in the sidebar only (44, 273 cut to facts); the retail command sits in the retail section, as ruling 1 requires |
| Dev | N1 | should | resolved | 79 |

### Copy desk (`copy-13.md`)

| Desk | No. | Severity | Status | Note |
|---|---|---|---|---|
| Copy | 1 | blocks | resolved | "Where each number goes" (13, 261) |
| Copy | 2 | should | resolved | "labeled" (265) |
| Copy | 3 | blocks | resolved | closer cut |
| Copy | 4 | should | resolved | 17 |
| Copy | 5 | should | resolved | sentence replaced (44) |
| Copy | 6 | should | resolved | 56 |
| Copy | 7 | should | resolved | 67, "1,000" |
| Copy | 8 | should | resolved | "The checker refuses a malformed block" (71), ruling 4 |
| Copy | 9 | should | resolved | 71 |
| Copy | 13 | should | resolved | superseded by fact D4 wording (92) |
| Copy | 17 | should | resolved | "eight to twelve digits" (Table 13.2) |
| Copy | 19 | should | resolved | 134 |
| Copy | 20 | should | resolved | sentence cut (fact U1) |
| Copy | 22 | should | resolved | sidebar in two paragraphs |
| Copy | 23 | should | resolved | 150 |
| Copy | 24 | should | resolved | 150 ("makes the checker refuse the book") |
| Copy | 26 | should | resolved | 165 |
| Copy | 28 | should | resolved | Table 13.3 Meaning cells are sentences |
| Copy | 30 | should | resolved | Table 13.4 |
| Copy | 31 | should | resolved | paragraph cut to the table cell |
| Copy | 32 | should | resolved | "When the LCCN comes back" (190, 295) |
| Copy | 34 | should | resolved | superseded by fact C2 and ruling 4 (273) |
| Copy | 38 | should | resolved | 315 (but see N1) |

### Typesetter (`type-13.md`)

| Desk | No. | Severity | Status | Note |
|---|---|---|---|---|
| Type | 1 | should | resolved in source | Element column 32 dashes, Value 18 (207); PDF not rebuilt here, recheck at final typesetting |
| Type | 2 | should | resolved in source | both tokens moved mid-sentence (92, 204); recheck in the PDF (see N3) |
| Type | 3 | should | declined-accepted | layout-dependent; recheck after final layout |
| Type | 4 | should | declined-accepted | depends on the real art's height; recheck once Figure 13.1 is in |

### New, introduced by the revision

| Desk | No. | Severity | Status |
|---|---|---|---|
| Re-review | N1 | should | open |
| Re-review | N2 | may | open |
| Re-review | N3 | may | open |

## Open items

**N1 (should). Line 315, 32 words in one sentence (ste_check; the
description maximum is 25, and this is running prose).**
Quote: "The retail flag comes last, because once it is set, the checker
refuses the book while either ISBN is absent or pending, or while a
declared LCCN or ISSN is still pending."
Fix: "The retail flag comes last. Once it is set, the checker refuses the
book while either ISBN is absent or pending, or while a declared LCCN or
ISSN is still pending."

**N2 (may). Line 273, "therefore" (ste_check word list).**
Quote: "Every route starts at the same block. The copyright page therefore
cannot show a print ISBN ..."
Fix: "Every route starts at the same block, so the copyright page cannot
show a print ISBN that differs from the barcode's, or an EPUB ISBN that
differs from the EPUB identifier."

**N3 (may). Line 204, a redundant phrase added to move a line break.**
Quote: "writes an ONIX 3.0 record to *dist/alice.onix.xml* in the book's
dist directory."
The path already names the dist directory, so the reader reads it twice.
Fix: "writes an ONIX 3.0 record, *dist/alice.onix.xml*, for the Alice
book." and let the typesetter's PDF recheck (Type 2) confirm the token
does not hyphenate; if it still does, reword there rather than pad.

## Reading

Read once straight through as the design's reader. The chapter now
answers the question the developmental desk named as the one change: a
retail edition needs two real ISBNs, and an LCCN or ISSN only if declared
and then not `pending`, and the chapter ends with the numbers rebuilt
into the artifacts. The fresh-scaffold device is clear and does not
contradict Chapters 3 and 10 (the omitted `--owner` from Example 3.1
does not affect any PCN field shown). Line 192 runs seven sentences once
the footnote marker is read as a break; it stays inside one topic and
is not counted.
