# Re-review: Chapter 5, Figures, plates, and illustrations

File: `book/chapters/05-figures-and-plates.md` (384 lines, working tree,
6,237 words by `press wordcount`).
Against: `facts-05.md`, `dev-05.md`, `copy-05.md`, `type-05.md`, the
Revision section of `report-05.md`, the last seventy lines of
`docs/production-ledger.md`, supplements S1 to S4 of
`docs/briefs/facts/facts-05.md`, and `docs/vocabulary.md`.

## Verdict

**APPROVED.** 0 open blocks, 3 open should (3 open items in all). Every
desk finding is resolved or properly declined. The three open items are
small and mechanical: one is a regression the revision introduced (code
lines over 64 columns), and two are new vocabulary points that no desk
raised (edition names, and one figure caption). The writer should apply
O1 to O3 before continuity, but they do not need another re-review.

## Specific checks

| Check | Result |
|---|---|
| Image line, one blank line, `art:` comment | Yes. Rule stated at 59 ("image line, one blank line, then the comment"), with the next-line failure (no caption, number, list entry, cross-reference target) and the silent `press figures` report; warning at 61 to 63; tip at 90 says the report cannot catch it. Examples 5.1 (49/51), 5.2 (103/108), 5.3 (187/189) all leave the blank line. |
| Wrapped figure: no `art:`, commissioned with `--subject` | Yes (248 to 257). Example 5.4 has no comment and says why in S2's terms; Example 5.5 shows `press illustrate cheshire-cat --subject "..."`. |
| Print pass copies only woodcuts, top-level `*.jpg`, logo | Yes (362): "the logomark, the JPEG files at the top of *assets/*, and everything in *assets/woodcuts/*", the "file not found" failure, and the advice to keep images under *assets/woodcuts/*. 317 tells the reader the same thing earlier. Note: 339 still says the pass takes "each interior image", and the qualification follows three paragraphs later. Accepted, because S3 asks for exactly that statement and the section makes it. |
| "every rendered edition", Manuscript named as the exception | Yes in prose: 267, 277, 280 say "every rendered edition"; 273 names the Manuscript edition as "the one exception" and warns that it publishes every directive verbatim. The Figure 5.3 caption still says "each edition" (O3). |
| S4 credit line | Yes (57): no field, write it into the caption. |
| S4 list conditions | Yes (128): both follow the Contents; List of Figures when a kind class without `decorative=true` appears; List of Plates when *assets/woodcuts/* holds any image file. |
| S4 `margin` as `wrap-outer` | Yes: Table 5.2 row and 178 ("in the PDF it looks the same as `wrap-outer`"); Figure 5.1 draws page 4 "as page 3". |
| S4 text and DOCX editions | Yes in content (265, 267): placement dropped, "Figure 5.1" label kept. The names do not follow the vocabulary (O2). |
| S4 ornament markup | Yes (81 to 85): `![](assets/woodcuts/rule.png){decorative=true}` verbatim; empty alt, never numbered, never listed, `fig-alt` refused. |
| Banned words (authoritative, settle, wins, shipped, clean, surface, vendor, print build, we) | None. `grep -iw` finds none. |
| "spine" | Literal use only; allowed by the jargon-allow ruling. |
| TeX passages cut | Yes. The only backslash in the file is a shell line continuation (330). `tocdepth` survives in the footnote for the Chapter 16 reader, and the `hypcap=true` option in its footnote; both are accepted under R1. |
| Footnote labels | All five carry `5-`: `5-silly-plates`, `5-tocdepth`, `5-hypcap`, `5-square`, `5-lulu`; each is used once and defined once. |
| Every fence tagged `text` | Yes: nine fences, nine `text` tags. |
| Code lines at most 64 columns | **No**: 49 (67), 72 (121), 103 (67). See O1. |
| `art:` comment plus image line under 190 words | Yes: Figure 5.1 182 (56 + 126), Figure 5.2 165 (51 + 114), Figure 5.3 180 (73 + 107). |
| The chapter's own figures obey its rules | Yes. All three: under *assets/woodcuts/*, numbered `05-01` to `05-03` in order, `.diagram`, `width=full-measure` with no `place` (not wrapped, so the comment is legal), blank line before the comment, `fig-alt` distinct from the caption, each cited by `@fig:` before it appears, no diagram wrapped (261). |
| figure / plate / illustration vocabulary | Held in the prose. The copy desk's corrections (11 to 15, 35) are in. Minor residuals noted under "Notes". |
| `press check` | Passes: source checks (23 files), checker self-test (29 fixtures), editorial checks, jargon check. The croquet-ground placeholder is gone, so no unreferenced-plate failure appears. |
| `ste_check.py` | 30 findings, all in accepted classes: the In-this-chapter list (6), fig-alt and art comments (164, 166, 220, 222, 271), the index comment (384), table cells (144 is prose, 30 words, see below), "therefore" (9, allowed), "whether" (allowed), "however" meaning "no matter how" (308), "is print-only" (adjective), "enhance" (command name), `-ing` in chapter and example titles. Prose sentences at 30 words: 75 (the style precedence), 144 (hypcap story), 267 (the edition list). None carries two ideas; accepted. |
| Index comment | Present, last, 25 terms (at the ceiling, as type 9 allowed). |

## Findings table

R = resolved, D = declined-accepted, O = open.

### Fact desk (facts-05)

| No. | Finding | Status |
|---|---|---|
| U1 | Alice example claims | R. Each example now "how you might type" (44, 95, 182, 235); 292's directory claim reduced to "the plates are PNG files under *assets/woodcuts/*". |
| U2 | Sidebar's origin claim | R. "A book built with press once had a figure taller than its text block" (306). |
| U3 | Default placement | R. Sentence cut. |
| U4 | Source form of a wrap | R. Now backed by S2 (235, 248). |
| U5 | Section numbers | R. "no `@` form reaches a chapter or a section" (120). |
| U6 | Print interior follows placement | R. Cut. |
| U7 | Square plate meets the line | R. "On most pages" (287). |
| U8 | Logo filename | R. "its copy in *build/print-assets/*" (365, 369). |
| U9 | Minor glosses | R. `.photo` says "photograph"; title-page sentence cut; wider-wrap reason cut. "ends at the first `-->`" kept as general knowledge; accepted. |
| C1 | Next-line comment | R. 59 to 63 and 90, per S1. |
| C2 | "every edition" | R in prose (267, 277, 280); see O3 for the caption. |
| C3 | "every image" in the print pass | R by S3 (362). |
| D1 | Guardrail reflowed and over-applied | R in content: one line, verbatim, "`press illustrate` adds a guardrail" (69). But the one line is 121 columns; see O1. |
| D2 | Figure 5.3 inconsistent | R. "six editions in four groups"; text/DOCX box carries "Figure 5.1". |
| D3 | pypdf "fails the PDF" | R. "now checks the link destinations with pypdf" (144). |
| D4 | "Nothing came out" | R. "Nothing reported a failure. The run never finished, so there was no PDF to inspect." (306). |
| D5 | "1.7 inches wide" | R. "printed at 1.7 inches" (364). |
| D6 | Cap and enlargement | R. Bridge cut; "never scales one up" sits with the resolution paragraph (339). |
| D7 | "The press documentation calls" | R. "Press treats this report as the one reading" (87). |
| M1 | Manuscript edition ships raw | R (273). |
| M2 | Wrapped plate has no directive | R (248 to 257). |
| M3 | 7.1 in in the skills | R (289). Sixth profile: Table 5.5 names "the profiles that the header names"; accepted. |
| M4 | `press art enhance` with no file | R (337): every JPEG and PNG under *assets/woodcuts/*, output to `<stem>.png`. |

### Developmental desk (dev-05)

| No. | Finding | Status |
|---|---|---|
| C1 | Credit line has no form | R (57, per S4). |
| C2 | Ornament never typed | R (79 to 85). |
| C3 | List of Figures condition | R (128, per S4). |
| P1 | Table 5.1 first row | R. Row says only "A bare image with no class is a plate"; the report quirk moved to 87. |
| P2 | Next-line comment | R (59 to 63, per S1). |
| P3 | Wrapped plate commission | R (248 to 257, per S2). |
| P4 | Example depends on Chapter 11 | R (323): needs the service's account and key, writes to *build/illustrations/*. |
| P5 | Apple Silicon resolution | R (341 to 346): 1024 px stays 1024, about 162 PPI; host upscaler search order; tip true on arm64. |
| P6 | "plate" kind against placement | R (168). |
| P7 | `margin` against `wrap-outer` | R (178, per S4). |
| P8 | Print interior unannounced | R (351): defined, `press print`, Chapter 12. |
| P9 | Terms used before defined | R. aesthetic (75), leaf and cleared leaf (148), profile (214), "Press's Lua filter" (235); "the tie" cut. |
| P10 | List of Plates in every edition | R. "in the PDF its entry goes into the List of Plates" (267). |
| R1 | TeX mechanism | R. No macro in the prose; tocdepth in a footnote. |
| R2 | Docs-against-code aside | R. Cut; 200 states the rule. |
| R3 | Sidebar strays | R. `titlepage` sentence cut. |
| R4 | Bridge sentences | R. Both cut. |
| O1 | Orientation says why | R (18): the refused line, the raw `@fig:`, the plate that changes sides. |
| N1 | Figure 5.2 bracket | R. fig-alt "a bracket spans one figure and the lines beside it". |
| N2 | Figure 5.3 text and DOCX | R, per S4. |

### Copy desk (copy-05), blocks and shoulds

| No. | Finding | Status |
|---|---|---|
| 1 | "shipped" (sidebar) | R. "emitted". |
| 2 | "shipped" (JPEG masters) | R. "the house once kept plates". |
| 3 | "settle" | R. "converge. Press therefore builds". |
| 4 | "wins" | R. "the limit that binds first sets the size" (287). |
| 5 | "authoritative" | R (87). |
| 6 | "clean" | R. "ordinary figure" (265). |
| 7 | "surface" | R. "onto its own page" (275). |
| 8 | Meta-narration | R. "and the sidebar tells the story" cut (301). |
| 9 | "spine" | D. Ledger ruling adds `spine` to jargon-allow; `press check` passes. |
| 10 | inline/plate "not X but Y" | R (168). |
| 11 | "a figure that carries decorative" | R (40). |
| 12 | figure for plate in illustrate lookup | R (67). |
| 13 | "figure's own style" | R (75). |
| 14 | "fig-alt for every figure" | R (77). |
| 15 | "where a figure sits" | R (148). |
| 16 | Two ideas, caption into alt | R (77). |
| 17 | Two ideas, tip | R. Tip rewritten (90). |
| 18 | Two ideas, Figure 8.1 | R. Now Figure 5.1 (112). |
| 19 | Two ideas, plate citation | R (118). |
| 20 | Two ideas, trim for profile | R (214). |
| 21 | Two ideas, height cap | R (285). |
| 22 | Two ideas, intake | R (339). |
| 23 | "fails press check" | R (130). |
| 24 | "fail" for refusal | R (172). |
| 25 | "print build" | R (351). |
| 26 | "vendor" | R (351). |
| 27 | "the press needs" | R. "than print needs" (351). |
| 28 | "figure" for a number | R (289 and footnote 5-lulu). |
| 29 | "the source" | R (235). |
| 30 | Hidden actor, "The filter" | R (235). |
| 31 | Hidden actor, `\pandocbounded` | R. Sentence recast without the macro (285). |
| 32 | Hidden actor, sidebar | R (308). |
| 33 | Perfect tense | R (69). |
| 34 | "we elide" | R (323). |
| 35 | "picture" for plate and image | R (22, 339, 341). |
| 36 | Nested double quotes | R (120). |

The copy desk's mays (37 to 49) are not graded here. The writer accepted
all but 43; the reason given for keeping that warning holds.

### Typesetter desk (type-05)

| No. | Finding | Status |
|---|---|---|
| 1 | Untagged fences | R. All nine fences tagged `text`. But the revision pushed three lines past 64 columns; see O1. |
| 2 | Figure 8.1 in a Chapter 5 example | R. The Alice chart is in that book's fifth chapter: Figure 5.1. |
| 3 | Figure 5.3 lettering | R. Every label says Figure 5.1. |
| 4 | Figure briefs near 190 | R. 182, 165, 180. |
| 5 | Example 5.4 has no `art:` | D. S2 forbids the comment on a wrap; the chapter says why and shows `--subject`. |
| 6 | Attribute lines broken | R. 95 says the break is only for the page width. |
| 7 | `.map` and the book's classes | R (40). |
| 8 | Table 5.5 Cap column | D. Meaning column states the value; accepted. |
| 9 | Index at 25 terms | D. Kept at 25; accepted. |

## Open items

### O1 (should). Three code lines run past 64 columns

Rule: the ledger's fence ruling (64 columns), which this chapter teaches.
The revision introduced all three; the typesetter's pass found none.

- 49, 67 columns: `![Alice follows the White Rabbit](assets/woodcuts/white-rabbit.png)`
  Fix: `![Alice and the White Rabbit](assets/woodcuts/white-rabbit.png)` (63).
- 103, 67 columns: `![Alice's height through the chapter](assets/woodcuts/heights.png){`
  Fix: `![Alice's height](assets/woodcuts/heights.png){` (47). No other
  line quotes either caption.
- 72, 121 columns: the guardrail, set as one line to satisfy fact D1.
  Fact D1 offered two remedies, and only the second fits the 64-column law.
  Fix: break it into three lines,

  ```text
  Single ink only, no colour wash. No text, no words, no
  lettering, no caption, no page border, no watermark, no
  signature.
  ```

  and end the lead-in sentence at 69 with: "The prompt receives it as one
  line; the break here is only for the width of the page." (Use two
  sentences if the writer prefers no semicolon in prose.)

### O2 (should, new). Edition names do not follow the vocabulary

Rule: `docs/vocabulary.md` line 17 and the ledger ruling: use press's
landing-page names for the editions, glossed once per chapter with the
format in parentheses. The vocabulary bars "the text edition" by name.
Chapter 4, already committed, does this (its line 40). Chapter 5 already
says "the Manuscript edition" (273) but uses plain format names elsewhere.

- 265: "Press therefore ignores the placement in the EPUB, the HTML
  edition, the reader site, the text edition, and the DOCX edition."
- 267: "in the PDF, the EPUB, the HTML edition, the reader site, the text
  edition, and the DOCX edition" and "The EPUB, the HTML edition, and the
  reader site get an ordinary link".
- 269, fig-alt: "The text and DOCX editions get an in-flow figure".

Fix: gloss once at 265: "Press therefore ignores the placement in the
Circulating edition (EPUB), the Single-leaf edition (the self-contained
HTML), the Chapter edition (the reader site), the Telegraphic edition
(plain text), and the Office edition (DOCX)." At 267 use "the Circulating,
Single-leaf, Chapter, Telegraphic, and Office editions" and "The
Circulating, Single-leaf, and Chapter editions get an ordinary link". At
first use of "the Manuscript edition" (273), add "(the stitched
Markdown)". The fig-alt may say "The plain-text and DOCX editions"; the
drawn box labels ("text / DOCX", "EPUB / HTML") may stay as they are,
since they label formats. Short references such as "the PDF" and "the
EPUB" elsewhere match Chapter 4 and can stay.

### O3 (should, new). Figure 5.3's caption overclaims

Rule: ledger ruling 2 ("every rendered edition" replaces "every edition
throughout"). The caption is also the figure's List of Figures entry,
where the Manuscript exception at 273 is not beside it.

- 269: `![Where an image line goes in each edition](...)`, and the
  sentence before it: "traces one image line into each edition" (267).

Fix: caption "Where an image line goes in each rendered edition"; at 267,
"traces one image line into each rendered edition". The fig-alt already
says "six editions", which is correct.

## Notes (not counted)

- 248: "A wrapped figure cannot carry an `art:` comment". Example 5.4 is a
  plate, and S2 covers every wrap. "A wrapped illustration" would match
  the vocabulary.
- 339: "passes each interior image through a *print-safe* pass" reads
  as universal until 362 qualifies it. "each interior image under the
  directories it copies (below)" would close the gap, but S3 is
  satisfied as written.
- Figure 5.3 draws "Figure 5.1", the Alice chart's number, in a chapter
  whose own Figure 5.1 is the placement matrix. The report's figure notes
  record that this is deliberate, and the top box names
  `#fig:alice-heights`. A reader would have more help if 267 said "traces
  the image line of Example 5.2 into each rendered edition".
- 306 and 312 say "a figure taller than the text block" for what could be
  any image. This is the scar's own wording, so it is accepted.

## Read as a reader

The chapter now teaches in the right order: the kinds, then the line and
its fields, then numbering, lists, placement, measures, editions, the cap,
files, and print. Every term is defined before use. The two traps that
the desks found (the next-line comment and the wrapped plate's directive)
each get a rule, a reason, and a remedy that the reader can type. The
Apple Silicon paragraph and tip are true on the primary platform. No
claim goes past facts-05 and its supplements. Nothing in the prose
contradicts the chapter's own three figures.
