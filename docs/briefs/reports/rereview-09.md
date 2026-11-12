# Re-review: Chapter 9, The house design

File: `book/chapters/09-the-house-design.md` (405 lines, `press wordcount`
5,694). Checked against `facts-09.md`, `dev-09.md`, `copy-09.md`,
`type-09.md`, the "Revision" section of `report-09.md`, the managing
editor's rulings in `docs/production-ledger.md`, and `docs/vocabulary.md`.
Line numbers refer to the revised chapter.

## Verdict

**APPROVED.** No open blocks. Two open shoulds, both mechanical: one comes
from a vocabulary ruling the writer did not apply, and one is a new
accuracy point. Both are listed under "Open items".

## Gates

- `~/code/.pwp-venv/bin/press check`: exit 0. Source checks, checker
  self-test (29 fixtures), editorial checks (23 files), and jargon lint all
  pass. Nothing in Chapter 9 is named.
- `tools/ste_check.py`: 36 findings, 373 sentences, average 13.0 words. All
  the residuals are accepted forms: the In-this-chapter box (6), figure
  lines with their art comments (148, 150, 208), the sidebar (27), the
  index comment (405), quoted passives (58 "is silently ignored", 220 "is
  emitted"), the semicolon inside the PRINT-FORMATS quotation (135),
  "therefore" (period-correct), chapter titles in -ing (Installing,
  Writing, Running), and "choosing" inside a quotation. The longer
  sentences at 152 (31), 171 (30), and 383 (30) are the copy desk's own
  fix wording or are within one word of the limit. No finding needs action.
- Fences: four, all tagged `text` (139, 281, 324, 359). No code line goes
  past 64 columns.
- `art:` comments: all three (27, 150, 208) come after their image line,
  with exactly one blank line between.
- Footnotes: `9-libertine`, `9-hypcap`, `9-migrate`, all prefixed.
- Tables 9.5 and 9.6 have a Meaning column.
- No non-ASCII characters and no trailing whitespace.

## Vocabulary rulings since the desks

- "List of Plates": capitalized at 92 and 94. Resolved.
- Edition names glossed once: Print (21), Chapter (177), Single-leaf (228),
  Circulating (230). Table 9.6 gives the rest as press's labels. Resolved.
- "the Pages bundle" / "the Pages site": neither term is needed. Line 234
  names *dist/pages/index.html* as the landing page, which is correct.
  Nothing to fix.
- "the Alice book" / "the press's own three-chapter Alice example":
  **open** (item O1). The chapter still writes "the Alice example", a term
  that the vocabulary puts in the "never" column for both Alices.
- Sources: the label "Table of authorities" for `-sources.md` is press's
  own label, and the Meaning cell "It is the sources companion" follows
  the ruling. Resolved.

## Findings table

### Fact desk (facts-09)

| # | Finding | Status |
|---|---|---|
| U1 | Example 9.1 presented as Alice's real file | resolved: recast as what `alice` writes (277), with values from facts-11 8.8 (ruling 1) |
| U2 | Example 9.2 `extra.css` panel, "needs" | resolved: cut (ruling 1); the chapbook rule now comes from the fact file (357-361) |
| U3 | Alice running-head strings | resolved: the strings are cut and only the mechanism is given (123-127) |
| U4 | Contents page "through the A-heads" | resolved: "it lists the chapters" (92) |
| U5 | Figure-cap purpose clause | resolved: the clause is cut (45) |
| U6 | `web-palette` `#` syntax | resolved: supported by the facts-11 8.8 capture (308) |
| U7 | Tip on fields falling back | resolved: tip reworded to "replaces the section as a whole" (317) |
| U8 | Replacement-sheet warning "no longer" | resolved (368) |
| U9 | Where a book names its profile | resolved: `print.profile` in *config/metadata.yaml* (135), per facts-03 |
| U10 | Logomark and portrait art direction | resolved: supported by facts-11 8.8 prose keys (260) |
| U11 | Low-stakes glosses | resolved: "binding takes up paper", "a printer bills", and "many designs leave it off" are cut; the footskip and indent rows are reworded; Table 9.3 rows are tied to their uses |
| C1 | Contents depth | resolved (92) |
| C2 | "Every token of the light palette" | resolved: "nine tokens of the light palette" (314); Example 9.1 has nine |
| C3 | "The same red" | resolved: two reds, named separately (277) |
| D1 | `book-colors` overrides four, not six | resolved (100) |
| D2 | "Either list" for hypcap | resolved: List of Plates only (94) |
| D3 | "Issue 262" | resolved: "number 262" (389) |
| D4 | Above/below/one-per-row placements | resolved: cut (200, 204) |
| D5 | Drawer "opens with" | resolved: "starts closed" (204); alt text and directive agree |
| M1 | Drop caps off by default | resolved (117) |
| M2 | Large print's 1.4rem Web type | resolved (165) |
| M3 | Landing page `Book` / `workExample` | resolved (216) |
| M4 | `scene-break` default | resolved: `rule` (the default) in Table 9.7. The txt/docx plain rule is not stated, which is acceptable because the chapter leaves txt/docx alone throughout (20.B.10) |

### Developmental desk (dev-09)

| # | Finding | Status |
|---|---|---|
| P1 | No key that chooses a profile | resolved: `print.profile`, a `$ press config set` session for alice on hatter, and the trim refusal pointed to Chapter 3 (135-144) |
| P2 | No way to see a design change | resolved: `press aesthetic` and Example 9.2 (320-349); `press site` and *dist/site/index.html* (177). `press pages` is left out, which ruling 3 allows |
| P3 | First A-head opens on TeX | resolved: the section opens on the page; class options moved to "The print interior" with one-sided and two-sided glossed (49); file suffixes and the macro line are gone |
| P4 | Craft law undefined | resolved: glossed at 100 with a pointer to Chapter 11 |
| P5 | Running heads by macro; sides unclear | resolved: left/right on the one-sided PDF (125); `\automark` is cut |
| P6 | Drawer open versus closed | resolved (204, 206, 208 agree) |
| P7 | Example 9.1 seems to break the rule | resolved: five dark tokens explained (306); `typography` is no longer in the example, so the font-stack point is moot |
| P8 | Example 9.2 contradicts Chapter 5 | resolved: the example is cut (ruling 1) |
| R1 | Reader site's CSS measures | resolved: clamp, outline, drop-cap measures, rel links, and card rows are cut; "Metadata in the head" is kept as R1 asked |
| R2 | Misfiled material in "The page in numbers" | resolved: "Headings and captions" now sits under Type (88); the fallback title is reduced to a pointer to Chapter 10 (113) |
| R3 | 3.0.0 re-lists the rules | resolved: a back-reference to "Type" (383); the pin paragraph keeps only what is new (397) |
| R4 | Warning repeats the paragraph | resolved: 363 no longer restates it; the warning drops "no longer" (368) |
| N1 | Table 9.5 has no meaning | resolved: Meaning column added, with the three derived tokens |
| N2 | `rulegray` and `accent` rows | resolved per ruling 3: `rulegray` says plainly that nothing touches it. The `accent` row is still thin, but the fact file gives no use (see "Not counted") |
| N3 | Figure 9.2 mostly blank | declined, accepted: body-size column dropped; blank cells stay by the coordinator's ruling |

### Copy desk (copy-09), blocks and shoulds

| # | Finding | Status |
|---|---|---|
| 1 | Heading-restating opener: print interior | resolved (49) |
| 2 | Heading-restating opener: reader site | resolved (177) |
| 3 | Heading-restating opener: landing page | resolved (234) |
| 4 | Heading-restating opener: aesthetic file | resolved (260) |
| 5 | Heading-restating opener: 3.0.0 | resolved (383) |
| 6 | Heading-restating opener: machinery | resolved (393) |
| 7 | *design profiles* defined at first use | resolved (17; roman at 135) |
| 8 | Print edition gloss | resolved (21) |
| 9 | "foot margin" versus "bottom margin" | resolved (29) |
| 10 | Folio before its definition | resolved (Table 9.1 says "page number") |
| 11 | "List of Plates" | resolved |
| 12 | "centred" (65) | resolved |
| 13 | "picture", "land" | resolved: the clause is rewritten (94) |
| 14 | "figures" for numerals (84) | resolved (76) |
| 15 | *aesthetic* defined late | resolved (76; roman at 260) |
| 16 | "measure" in parfillskip | resolved (86) |
| 17 | `lettrine` in constant width | resolved (117) |
| 18 | "initial" | resolved: "drop cap" throughout (117-119) |
| 19 | "centre" (123) | resolved |
| 20 | "centre" (125) | resolved: the sentence is cut |
| 21 | "measure" for the Web width; *leaf* | resolved: "leaf width" throughout; *leaf* defined (152) |
| 22 | "pictures"; two ideas | resolved (167) |
| 23 | "centred"; two ideas (h1) | resolved (200) |
| 24 | "horizontal rule", scene break | resolved (200) |
| 25 | Alt text: "centred", "engraving", length | resolved (206) |
| 26 | Index-page sentence length | resolved (212) |
| 27 | Single-leaf edition | resolved (228) |
| 28 | Circulating edition; length | resolved (230) |
| 29 | Chapbook sentence | resolved (357) |
| 30 | "figures", "font" in 3.0.0 list | resolved: the list is cut by R3 |
| 31 | "lesson" | resolved: "left one more scar" (387) |
| 32 | "pipeline" | resolved: "press code" (397) |
| fact referrals | four values, four colors, indent and leading, five words, two reds, token count | all resolved (86, 100, 165, 230, 277, 314) |

The mays (33 to 43) were applied as well. Copy 40 is moot because its
sentence was cut.

### Typesetter (type-09)

| # | Finding | Status |
|---|---|---|
| 1 | `[^hypcap]` label | resolved: `9-hypcap` |
| 2 | `[^libertine]` label | resolved: `9-libertine` |
| 3 | `[^migrate]` label | resolved: `9-migrate` |
| 4 | Table 9.5 splits across folios | declined, accepted: the table and the text around it changed, so the managing editor checks it on the next `press pdf`. It is not fixable by markup in any case |
| 5 | Example 9.1 caption at a page foot | declined, accepted: same reason. The managing editor checks it on the next `press pdf` |
| 6 | Figure 9.1 portrait at full measure | resolved: `width=half-measure`, and the directive says to draw it narrow (25, 27) |
| 7 | Chapters 10 and 12 without titles | resolved (51, 113, 403) |
| 8 | Tables 9.5 and 9.6 without a Meaning column | resolved |

## Open items

**O1 (should, vocabulary ruling). "the Alice example".** The vocabulary
lists "the Alice example" under "Never these" for both Alices. It appears
six times:

- 21: "Open the reading PDF of the Alice example, the Print edition"
- 137: "To move the Alice example to the novella page"
- 204: "shows a chapter page from the Alice example"
- 206: caption "A chapter page of the Alice example on the reader site"
- 208: art directive "a real reader-site build of the Alice example"
- 279: "**Example 9.1. An aesthetic file for the Alice example**"

Fix: at 21, 137, and 279, write "the Alice book". These are what user
`alice` does to her own novel ("Open the reading PDF of the Alice book",
"To move the Alice book to the novella page", "Example 9.1. An aesthetic
file for the Alice book"). Figure 9.3 is a real capture. By the rule that
captures from the gallery are labelled as such, write at 204 "a chapter
page from the press's own three-chapter Alice example"; in the caption at
206, "the three-chapter example" (the short form per the latest ruling,
after the first mention at 204); and in the directive at 208 "the press's
own three-chapter Alice example". If the illustrator instead captures the
Alice book itself, use "the Alice book" in all three.

**O2 (should, new accuracy point). Dark-theme links.** Line 306: "The
links on the reader site follow the new deep cloth, because the sheet's
`--link` takes its value from `--cloth-deep`." That holds only in the light
theme. Table 9.5 (185) and facts-09 7.3 give the dark `--link` as
`var(--foil-bright)`, which Example 9.1 does not change. Fix: "In the light
theme, the links on the reader site follow the new deep cloth, because the
sheet's `--link` takes its value from `--cloth-deep`."

## Not counted (for the continuity pass, may)

- Table 9.3, `accent` (108): "The header defines it as the house accent"
  still says little more than the name, and Example 9.1 turns it red. The
  fact file gives no use, so this is acceptable under ruling 3. "The fact
  file names no element that uses it" would be the plainest version.
- Table 9.5: `--hairline` and `--ornament` (187, 190) give no dark value
  and no "dark unchanged" mark, unlike the other rows that keep their
  value. "`var(--foil)`, dark unchanged" would make the convention at 179
  hold for every row.

## Reading as a reader

The chapter now opens on the page the reader sees and keeps TeX in the
places where it explains a choice. It also gives the two actions the
reader came for: choosing a profile (137-144) and checking the merge
(320-349). Example 9.1 and Example 9.2 now read as a pair, the book's file
against the house values it restates, and the token count, the red cloth,
and the five dark tokens all agree with the code. The cuts to the reader
site removed the measures a reader cannot act on, and nothing the later
sections rely on was lost. The closing pointer to Chapter 10 follows the
last tip as before.
