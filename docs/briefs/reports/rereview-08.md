# Re-review: Chapter 8, Verifying the artifacts

File: `book/chapters/08-verifying-the-artifacts.md` (517 lines, revised).
Against: `facts-08.md`, `dev-08.md`, `copy-08.md`, `type-08.md`, the
Revision section of `report-08.md`, the production ledger's last sixty
lines, and facts-08 S1 to S4. Line numbers are the revised file's.

**Verdict: REVISE.** 0 open blocks, 4 open shoulds (one inherited
convention, three introduced or left by the revision). All four are small
and mechanical; none needs a new ruling.

## Mechanical checks

- `press check`: the only failure is `plate never referenced by the
  manuscript: assets/woodcuts/croquet-ground.png`, not this file.
- `ste_check.py`: residuals are the defended set (passives and
  semicolons in verbatim quotations at 27, 431, 449, 451; the art
  directives and index comment at 55, 437, 487, 517; "whether" and
  "therefore" at the copy desk's own fixes; gerunds in cross-referenced
  chapter titles). No prose sentence over 30 words.
- Fences: 20, every one tagged `text`. No line inside a fence exceeds 64
  columns. No non-ASCII characters in the file.
- `art:` comments: all four (plate 19/21, Figure 8.1 53/55, Figure 8.2
  435/437, Figure 8.3 485/487) follow their image line after exactly one
  blank line. The plate's image line and comment are byte-identical to
  the stub (`7e1b352`), with the blank line between.
- Watchlist: "lands", "ships", "surface" gone from the prose. Remaining
  hits are the verbatim CONTRIBUTING quotation ("shipped", 27) and the
  verifier's own phrase "public reading surface" (376, 395), which the
  copy desk ruled stays.
- Examples 8.1 and 8.2 are the real S1/S2 runs, slug `alice`, timing
  elided with `...`, line breaks announced in the prose (194, 274), and
  labelled "the press's own three-chapter Alice example" / "the
  three-chapter Alice example". Example 8.2 carries
  `Verified archives: alice-site.zip, alice-source.zip`, and the
  archives section quotes it (359).
- Page floor: "The Alice example meets both rules" is gone; 206 states
  the gallery floor of 1 and the full novel's 24, per S4.
- Chapter witness: defined at first use (272) exactly as S3 gives it;
  the S3 long-code-line hazard is the Warning at 233.
- "First words" rule: gone; 459 starts from the command that ran (but
  see open item 3).
- Contradictions: `verify-formats` reading an existing PDF is stated as
  the one exception (433, 439) and drawn as a dotted arrow in Figure
  8.2's directive; `press all` runs four named verifiers and not the
  print pack (442, 445); `pdfimages` is "two checks" in both body (188)
  and Tip (191), and `press doctor` "does not check" it (188, 463).
- The `press all` success line is not quoted; 447 points to Example 1.2,
  which exists in Chapter 1 (line 176). Acceptable either way per the
  ruling.

## Findings table

| Desk | No. | Status |
|---|---|---|
| copy | 1 "lands" (blocks) | resolved ("arrives", 128) |
| copy | 2 "ships" (blocks) | resolved ("carries", 323) |
| copy | 3 "every surface" (blocks) | resolved ("Every published page", 378) |
| copy | 4 Warning sentence over 30 | resolved (153, three sentences) |
| copy | 5 "guarantees" | resolved (91) |
| copy | 6 "lesson" | resolved ("scar", 135) |
| copy | 7 "measure" | resolved (sentence cut) |
| copy | 8 "colour" in Table 8.2 | resolved (73) |
| copy | 9 "colour" in prose and directive | resolved (169, 487 "No color") |
| copy | 10 "2 sentinels" | resolved (63) |
| copy | 11 "8 ... 4 words" | resolved (418) |
| copy | 12 title case-fold, two ideas | resolved (114) |
| copy | 13 reader-site messages, two ideas | resolved (272) |
| copy | 14 min-pages and sentinel list | resolved (sentence cut) |
| copy | 15 search / culprit | resolved (489) |
| copy | 16 "as described" | resolved (274) |
| copy | 17 "are cut" | resolved (310) |
| copy | 18 "is set" | resolved (380) |
| copy | 19 ambiguous "it" | resolved (439) |
| copy | 20 "it enforces" | resolved (447) |
| copy | 21 "the source" | declined-accepted ("the press's source", 317; the possessive keeps it off the manuscript, which is what the vocabulary row bars) |
| copy | 22 "step" | resolved (95, 308, 459) |
| copy | referral: `pdfimages` two checks | resolved (188, 191 agree; doctor caveat added) |
| copy | referral: `press all` Tip | resolved (442) |
| dev | C1 chapter witness undefined | resolved (272, from S3) |
| dev | P1 "first words" rule | resolved in substance; replacement sentence has a false figure reference (open 3) |
| dev | P2 witness vocabulary early | resolved (41, 63) |
| dev | P3 TeX vocabulary | resolved (156; sidebar 133, 135) |
| dev | P4 "authoring sandbox" | resolved ("unless a helper renderer is present", 140; history in footnote) |
| dev | P5 commerce unset | resolved (382) |
| dev | P6 profile split | resolved (78) |
| dev | P7 page floor | resolved per S4 (194, 206) |
| dev | R1 detector thresholds | resolved (footnote) |
| dev | R2 witnesses section restates | resolved (412) |
| dev | R3 signpost | resolved (210) |
| dev | R4 pages checks as list | resolved (376 to 382, grouped by condition) |
| dev | N1 Figure 8.1 columns | resolved (29, 31, 53) |
| dev | N2 real runs | resolved (Examples 8.1, 8.2; 359) |
| dev | N3 doctor repeats Ch 2 | resolved (463) |
| type | 1 to 3 `art:` comment order | resolved (55, 437, 487) |
| type | 4 doctor line 74 columns | resolved (477 elided, caption says so) |
| type | 5 to 13 fence lines over 64 | resolved (none over 64) |
| facts | U1 Alice sentinels and title | resolved (sentinels assigned to the full novel, 106; capitals title gone, 114) |
| facts | U2 who sets `PRESS_RELEASE`; Ch 3 refusal | resolved (82; Ch 3 line 230 confirms "vacuous witnesses" and Example 3.3) |
| facts | U3 11.5 percent embellishment | resolved (27) |
| facts | U4 "always the machine" | resolved (91, 461) |
| facts | U5 "first sign" | resolved (153) |
| facts | U6 printers' tools | resolved (33) |
| facts | U7 `PRESS_TOOLCHAIN` | resolved (317) |
| facts | U8 sentinel list empty | resolved (cut) |
| facts | U9 Pages deploy | resolved (331) |
| facts | U10 "names the chapter outright" | resolved (489, 492) |
| facts | U11 "one line ... Verified" | resolved (31, the desk's own wording) |
| facts | U12 low-stakes glosses | resolved (dropped; "pandoc curls" and Table 8.5 kept with reason) |
| facts | C1 floor vs 23 pages | resolved (206) |
| facts | C2 no-stale without exception | resolved (433) |
| facts | C3 `press all` Tip | resolved (442) |
| facts | C4 "first words" | resolved (459) |
| facts | C5 doctor and `pdfimages` | resolved (463) |
| facts | D1 Example 8.1 template | resolved |
| facts | D2 Example 8.2 template | resolved |
| facts | D3 unannounced breaks | resolved (181, 252, 390, 420) |
| facts | D4 added prompt | resolved (468) |
| facts | D5 "List of plates" label | resolved (120) |
| facts | D6 alt text "five verifiers" | resolved (53) |
| facts | D7 "every build" | resolved (135) |
| facts | D8 "last press verify" | resolved (439) |
| facts | D9 "most common cause" | resolved (169) |
| facts | M1 archives success line | resolved (291, 359) |
| facts | M2 source zip report | resolved (282, 344) |
| facts | M3 Figure 8.2 dotted edge | resolved (437) |
| facts | M4 `BROKEN` optional tool | resolved (481) |
| facts | M5 what `E` counts | resolved (294, 427), but see open 2 |
| facts | M6 `press all` success | resolved (447, Example 1.2) |
| ruling | footnote labels prefixed `8-` | **open** (item 1) |

Mays (copy 23 to 35) are out of scope; the writer accepted 23 to 34 and
passed 35 to the art desk.

## Open items

1. **Footnote labels are not prefixed.** (should; ledger convention,
   markup.md "Footnote")
   Quote: `[^detector]` (84, 509), `[^fallback]` (140, 511),
   `[^ci-false]` (317, 513), `[^window]` (418, 515).
   No collision exists today, but the convention exists because pandoc
   merges every chapter into one document.
   Fix: rename to `[^8-detector]`, `[^8-fallback]`, `[^8-ci-false]`,
   `[^8-window]` at each reference and definition.

2. **"Three-chapter" example with four chapter witnesses, unexplained.**
   (should; introduced by the M5 fix)
   Quote (427): "The three-chapter Alice example stitches four files, so
   it has four chapter witnesses."
   A reader told twice that the example has three chapters meets four
   chapter witnesses with no reason given. The fourth file is the
   appendix (press's `examples/alice-in-wonderland/book/appendices/`;
   Chapter 1, line 170: "three chapters and an appendix").
   Fix: "The three-chapter Alice example stitches four files, its three
   chapters and an appendix, so it has four chapter witnesses."

3. **Figure 8.2 does not show verifiers.** (should; introduced by the
   P1/C4 fix)
   Quote (459): "Each verify target runs a known set of verifiers, which
   @fig:rebuild-edges shows."
   The Figure 8.2 directive (437) draws only commands and the artifacts
   they build; no verifier appears in it, and the caption says
   "rebuilds". The reader is sent to a figure that does not hold the
   answer.
   Fix: "Each verify target runs a known set of verifiers. A failure
   under `press verify` comes from `verify_pdf`, under `press
   verify-formats` from `verify_formats` or `verify_archives`, under
   `press pages` from `verify_pages`, and under `press verify-print` from
   the print profile of `verify_pdf` or from `verify_coverwrap`." (Then
   drop the next sentence's two examples, which it repeats.) Do not add
   verifiers to the directive: it is at 173 words against a 190 ceiling.

4. **Two names for the sample book, and the opener misattributes the
   examples.** (should; one term per thing, and the two-Alices ruling)
   Quote (17): "The examples come from the Alice example, which user
   `alice` builds on the workstation `hatter`". Quote (106): "The sample
   book of this manual, the full novel in user `alice`'s repository";
   (206): "The sample book of this manual, the full novel".
   The full novel is "the Alice example" at 17, 35, 49, and 82 and "the
   sample book of this manual" at 106 and 206; the gallery excerpt is a
   third name. Line 17 also says the examples come from the full novel,
   while Examples 8.1 and 8.2 come from the gallery excerpt.
   Fix: keep "the Alice example" for the full novel throughout and
   "the press's own three-chapter Alice example" for the gallery. At 17
   add: "The real runs in Examples 8.1 and 8.2 come from the press's own
   three-chapter Alice example." At 106 write "The Alice example, the
   full novel in user `alice`'s repository, declares ..."; at 206 write
   "The Alice example itself, the full novel, sets its floor at 24 ...".

## Notes for the managing editor (not counted)

- Edition names: the ledger rules that press's landing-page names
  (Print, Circulating, Single-leaf, ...) are glossed once per chapter.
  This chapter uses none (29, Table 8.3), as Chapters 2, 6, and 7 do not.
  The ruling postdates this chapter's desks; decide whether it applies to
  chapters already through review before sending it back.
- 31: "Each verifier ends with a line that begins with `Verified`" sits
  directly after the `verify_coverwrap` sentence, so it reads as covering
  that verifier, whose success line the fact file does not give. The
  wording is the fact desk's own fix; harmless if Chapter 12 shows a
  `Verified` line for the wrap.
- 188: the body names one check that softens without `pdfimages` and
  says the press's notes record two. Consistent with 20.B.14; a reader
  may ask what the second is.
- 294: "`pdftotext` is present on `hatter`" attaches the gallery capture
  to the reader's persona workstation. Fine as framing.
