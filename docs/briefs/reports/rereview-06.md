# Re-review: Chapter 6, Checking the manuscript

File: `book/chapters/06-checking-the-manuscript.md` (503 lines, revised).
Measured against facts-06, dev-06, copy-06, type-06, the Revision section of
report-06, the ledger's last fifty lines, and facts-06 S1 to S7.

## Verdict: APPROVED (0 open blocks, 3 open shoulds)

## Gates run

- `press check` (repository): source checks pass (23 files); checker
  self-test passes (29 fixtures, 6 notes); editorial checks pass (23 files);
  the jargon lint fails only on `authoritative` in Chapter 5 (not this
  file). This file draws one `inspect` sighting (`churn`, line 256, in the
  sentence that lists inspect terms), which does not fail.
- `tools/ste_check.py`: 35 findings, all residuals already defended. The
  three paragraph-length hits (40, 102, 433) are art comments. The
  sentence-length hits are the In-this-chapter list, the art comment, the
  index comment, a footnote fusion (218), and prose at 29 to 30 words
  (204, 341, 382). The two semicolons are the verbatim scars quote and the
  index comment. The passives are the quoted "to be determined" and the
  adjectival "is malformed".
- Mechanical: all 15 fences tagged `text`; no code line over 64 columns;
  each of the three `art:` comments follows its image after exactly one
  blank line; no non-ASCII; no trailing whitespace; no prose paragraph over
  six sentences.
- `press pdf` in a scratch copy (exit 0): Figures 6.1, 6.2, and 6.3 render
  as captioned figures. Example captions checked for stranding (see open
  item 2).

## Specific checks requested

| Check | Result |
|---|---|
| Not every build passes through the checker | Resolved. Line 17 (`press all` and CI run it; a bare `press pdf` does not); 36 (bare format targets and `press verify` skip it); 141; 471; Figure 6.1 retitled "The checker as press all runs it", with a directive that draws `press all`. Matches S1. |
| Example 6.12 / Figure 6.3 = S4, labelled | Resolved. Unfolded, Example 6.12 is identical to S4 (diffed). Labelled "the press's own three-chapter Alice example" in the lead-in (408), caption (410), figure caption (431); the terminal title is `~/alice-in-wonderland`. Chapter count and appendix match S5. |
| Sample `alice` in one state | Resolved. Description set on day one (56, matches Chapter 1 line 137); own fixture *very-unique.md* (83, 128) so its count is 20 (133), consistent with "19 for a book with no fixtures" (118); `audit-dirs: [notes]`; sentinels from Carroll's chapters 6 and 7 (full novel per S5); floor 24 once chapters exist (388); `dist/alice.pdf` (473). Example 6.13 carries no counts. |
| No ship/ships/shipped | Resolved. The only sighting is inside the verbatim scars quotation (494), which copy-06 item 10 keeps. |
| No sentence about this book | Resolved. The remaining "this chapter" uses are cross-references; 153 and 244 explain an example's fence by the rule's mechanism (copy-06's own wording for items 31 and 32). |
| "Checker self-test" vs press's test suite | Resolved. Defined at 75; footnote names `press selftest` (299). One bare "self-test line" at 133 (nit below). |
| `audit-dirs: [notes]` | Resolved (313, 322, 353). |
| Rules listed once | Resolved. Example 6.3 is the only list of the universal battery; Tables 6.3/6.4 of the draft are gone. |
| Inline code not skipped by banned patterns; fenced is | Resolved. 188 (universal battery skips fences except trailing whitespace, reads inline code) and 198 (banned patterns skip fences, read inline code). Matches S3. |
| Art comment after image, one blank line | Resolved (38/40, 100/102, 431/433). |
| Every fence `text` | Resolved (15 of 15). |
| Code lines at most 64 columns | Resolved (none over 64). |
| Footnote labels prefixed `6-` | OPEN (item 1). |
| Prose paragraphs at most six sentences | Resolved. |
| Example 6.13 plausibility | Accepted per the managing editor. Slug `alice`, the chapter file *book/chapters/01-down-the-rabbit-hole.md*, the Alice book's own banned-pattern label, and a paragraph diagnostic in the message form of line 207. No reference to this book's files. |

## Findings table

### facts-06

| # | Finding | Status |
|---|---|---|
| U1 | Example 6.12 not Alice's capture | Resolved (S4/S5 capture, labelled; curly-quote note question moot, the capture shows two notes) |
| U2 | Alice description | Declined-accepted (tied to Chapter 1's `press config set`, which exists) |
| U3 | Markers read in fences | Declined-accepted (writer's test; stated as fact at 54) |
| U4 | Figure placement list | Resolved (65) |
| U5 | Source-check count | Resolved (71; scaffold "1" kept per S5) |
| U6 | Book patterns apply to packaged fixtures | Declined-accepted (confirmed: this repository's `press check` notes `testament.md also drew: ... assistant vocabulary` from the packaged fixture; follow-on corrected at 135) |
| U7 | Block counted as one paragraph | Declined-accepted (markup.md states it for sidebars; art-comment sentence cut) |
| U8 | Editorial count covers audit dirs | Resolved (cut) |
| U9 | Failure output form | Declined-accepted (managing editor: genuine captured output) |
| U10 | `allow`/`ban` meaning | Resolved (Table 6.3) |
| U11 | Generated fixture map | Resolved (cut) |
| U12 | Regex details | Resolved (`[Vv]` example; "refuses a pattern that does not compile") |
| U13 | Alice house rules | Resolved by ruling, but see open item 3 (`leverage`) |
| U14 | Sidebar narration | Resolved (general mechanism; the quote is the only history) |
| U15 | Exit codes | Resolved (0 from facts-01; nonzero per S2) |
| U16 | `press all` order | Resolved (S1) |
| U17 | Glosses | Declined-accepted (softened; framing) |
| C1 | Every build passes through check | Resolved |
| C2 | Edges and a stale edition | Resolved (473 names the `verify-formats` exception) |
| C3 | Curled quotes in every edition | Resolved (192) |
| D1 | Drop-cap warning unconditional | Resolved (379, 382) |
| D2, D3 | "In capitals", "fully capitalized" | Resolved (moot: detail moved to Chapter 4; table gone) |
| D4 | Folded messages unmarked | Resolved |
| D5 | "190 words or more" | Resolved (204, 461) |
| D6 | "One fault" / "most declare" | Resolved (77) |
| D7 | "On every run" | Resolved (75, 122) |
| D8 | Retail refusal | Resolved (62) |
| D9 | Maxim attribution | Resolved (75) |
| D10 | Trailing whitespace row | Resolved (182) |
| M1 | Two hyphens | Resolved (186) |

### dev-06 (0 block, 17 should)

| # | Status |
|---|---|
| C1 exit codes | Resolved (S2: nonzero) |
| P1 thesis vs line 154 | Resolved |
| P2 Alice in two states | Resolved |
| P3 self-test term | Resolved |
| P4 fixture procedure | Resolved (120 to 133) |
| P5 package paths | Resolved (paths cut; `press skills` at 231) |
| P6 `appendices` | Resolved (`notes`; "outside the manuscript" at 149) |
| P7 Table 6.2 pointers | Resolved |
| P8 "worth knowing exactly" | Resolved (pointer to Chapter 4) |
| R1 re-teaching Chapter 4 | Resolved (382 keeps only what is new: the house sets no drop cap) |
| R2 audit-dir rule six times | Resolved (home at 149; small residue at 341 and 353, nit below) |
| R3 three lists | Resolved |
| R4 red-check told three times | Resolved |
| R5 jargon internals | Resolved ("Reading the jargon report") |
| O1 two closing pointers | Resolved (501) |
| N1 Figure 6.3 duplicates Example 6.12 | Declined-accepted (the managing editor keeps Figure 6.3; the prose introduces it as the terminal view) |
| N2 Table 6.7 incomplete | Resolved (retitled; Appendix C pointer) |

### copy-06 (10 blocks, 33 shoulds)

| # | Status |
|---|---|
| 1 to 9 | Resolved |
| 10 | Resolved (sidebar retitled; the quote stays verbatim, as the item said) |
| 11 to 15, 17 to 25, 27, 29, 30, 32 to 43 | Resolved |
| 16, 26, 28, 31 | Resolved (sentence cut or rewritten to the item's intent; 31 at 153) |

### type-06 (3 blocks, 27 shoulds)

| # | Status |
|---|---|
| Blocks 1 to 3 (art comment before image) | Resolved (image, blank line, comment, per the later ruling) |
| 16 untagged fences | Resolved |
| 8 lines over 64 columns | Resolved |
| Stranded captions (6.6, 6.9, 6.14) | Resolved for those three in the current build; a new one at Example 6.11 is OPEN (item 2) |

## Open items

1. **Footnote labels not prefixed `6-`** (should; ledger convention).
   Quote: `[^first-expect]` (81, 143), `[^law-date]` (204, 214),
   `[^twocopies]` (218, 299). Fix: rename to `[^6-first-expect]`,
   `[^6-law-date]`, `[^6-twocopies]` at both the reference and the
   definition. (No collision today; the build's only duplicate note is
   `libertine` in Chapter 9.)

2. **Example 6.11's caption stranded at a page foot** (should; type-06).
   In a scratch `press pdf` of the current tree, "Example 6.11. The
   release refusal" is the last line of printed page 102, and its fence
   opens the next page. Fix: recheck at final pagination, since other
   chapters are still moving. If it is still stranded, end the paragraph
   at 392 before "It refuses vacuous witnesses ..." so the reference
   sentence and caption fall together, or trim a sentence above in
   "The page floor".

3. **Example 6.8 allows a term that is not on the watchlist** (should;
   follows from facts-06 U13). Quote: "jargon-allow:\n  - leverage" (311),
   against 349, "The `jargon-allow` list tells the jargon lint which
   watchlist terms this book may use." `leverage` is not in the packaged
   *watchlist.csv* (checked: no row matches), so the Alice book's entry
   allows nothing, and a reader learns to allow a word the lint never
   reports. Fix: replace `leverage` with a watchlist term, for example
   `seams` (the draft's choice, a rewrite term), or keep `leverage` and
   say in one sentence that an entry for a term the watchlist does not
   hold has no effect.

## Nits (not counted)

- 133: "The self-test line now counts 20 fixtures." Use "The checker
  self-test line", per S7.
- 17 and 21: "reads the manuscript and its configuration" appears in
  three of five consecutive sentences. Cut the second sentence of 21
  ("It reads only the manuscript and its configuration.").
- 341 ("the audit directories do not meet them") and 353 ("the jargon
  lint does not read it at all") still restate 149 and 227 in passing.
