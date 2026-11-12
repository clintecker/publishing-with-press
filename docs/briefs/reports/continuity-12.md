# Continuity report: Chapter 12, *The print pack*

Desk: continuity editor. Chapter read as it stands after its desks, its
re-review, and the second revision (500 lines). Cross-checked against
Chapters 1 to 8 and 10 (committed), the drafts of 9, 11, 13, 16 and
Appendixes B and C that Chapter 12 cites or that cite it,
`docs/vocabulary.md`, and `docs/design.md` section 5.

Status: **PASS WITH FIXES.** One block, three should, ten may. The block is
the Chapter 5 title, which the Chapter 5 pass (continuity-05, finding A)
and the copy desk (copy-12, #41, which carried the wrong title into its fix)
both left standing. Two should are conflicts with Chapters 5 and 11; the third is a promise that Appendix C hands back (finding 14).

What holds:

- **Profile facts agree with Chapter 9.** Six profiles (l.57; Ch. 9 l.135);
  the six ids and trims of Table 12.2 match Figure 9.2's brief (l.150),
  including `mass-market-4.25x6.87`; the interior is single ink in every
  profile except `house-6x9-color` (l.70; Ch. 9 l.100, 167); the color
  profile is the house geometry unchanged (l.76; Ch. 9 Table 9.4 l.157);
  "sealed" in both definitions (l.55; Ch. 9 l.17); the print header's
  `twoside`, `open=any` (l.155; Ch. 9 l.49). Ch. 9 l.167's promise ("Chapter
  12 explains why some providers refuse a color interior") is kept at l.78.
- **Figure-cap facts agree with Chapter 5.** 1900 pixels "about 300 PPI at
  6.3 inches" (l.265) is the house cap of Table 5.5 and the cap of Table 5.6;
  the logomark cap of 1000 pixels, JPEG q88, *build/print-assets/*,
  *print-safe-images.lua*, masters untouched, the Lulu origin (1024 px over
  1.7in = about 602 PPI), and the *tex/title-page-print.tex* tip all match
  Ch. 5 l.351 to 372 (see findings 3, 5, 6 for the wording).
- **`press all` and the gate agree with Chapters 7 and 8.** `press all`
  builds neither the interior nor the wrap except through the commerce gate
  in a book with print ordering on (l.159, 491; Ch. 7 l.444; Ch. 1 l.170);
  the gate is advisory unless `PRESS_RELEASE=1` (l.491; Ch. 7 l.436 to 440;
  Ch. 8 l.447); `press verify-print` and `press coverwrap` build what the
  shared fact says, with the same no-cover line (l.157, 169; Ch. 8 l.160,
  177); `print profile: colored ink on pages [N]` (l.165; Ch. 4 l.235;
  Ch. 8 l.172).
- **Chapter 3 agrees.** Defaults of Table 12.1 and `print.paper` default
  `cream` match Table 3.5; no `press qualify` command, qualification by hand
  in *config/qualification.yaml* (l.354; Ch. 3 l.174); the template's
  `seller-of-record: "Lulu"` and the provider-as-seller model (l.480; Ch. 3
  l.174).
- **Every earlier promise to Chapter 12 is kept**: the print pack in full
  (Ch. 1 l.279; Ch. 5 l.353; Ch. 7 l.220); direct print ordering (Ch. 3
  l.174; Ch. 7 l.426; Ch. 8 l.382); the print fields (Ch. 3 l.269); the
  publish checklists (Ch. 3 l.625); the print pack build and `verify-print`
  (Ch. 4 l.235); the providers (Ch. 6 l.67); `verify_coverwrap` (Ch. 8 l.31,
  177; App. C l.448); the rest of the print interior and the spine
  arithmetic (Ch. 9 l.51, 379); the flattened copy of every image (Ch. 10
  l.184); `house-6x9-color` (Ch. 11 l.102); the check digit by hand (Ch. 13
  l.90, 123); `press all` not taking the branch (Ch. 16 l.78). Ch. 16 l.291
  ("the receipt digests that the edition manifest of Chapter 12 records") is
  only half kept: l.382 names the toolchain digest among the hashed facts and
  says the receipts stay out of the hash, but never says the manifest records
  receipt digests. For Ch. 16's pass.
- **Cross-references out** are right in number and title except finding 1:
  Chapter 9, *The house design* (l.55); Chapter 8, *Verifying the artifacts*
  (l.157; l.283 bare number); Chapter 4, *Writing the manuscript* (l.165);
  Chapter 11, *The art department* (l.219); Chapter 13, *Registrations*
  (l.225, 493); Appendix C, *Messages and refusals* (l.300; number and title
  right, content not delivered: finding 14). Internal: "The layout" later (l.86 to l.173); "Print-safe images"
  later (l.151 to l.261); "Ordering a copy" later (l.159 to l.413, the gate
  at l.491); "the last section of this chapter" (l.332 to l.480); the tip in
  "Paper and the Lulu paperback" (l.419 to l.146), earlier and named as such.
- **Cast** is clean: `alice` only (Example 12.6 `inspector`); no host is
  named; `example.test` for the support URL; the ISBN 978-0-306-40615-7 is
  the press's own selftest number; the shops are real.
- **The old Alice conflict is closed.** The bible's note on Ch. 12 ("Alice
  example", 200 pages, cream, old l.111, 218) no longer applies: the 200-page
  cream book is now "the house example" (l.195, 217), and l.140 sets the
  Alice book's `print.paper white`, as Ch. 3 does.
- **Numbering**: Tables 12.1 to 12.11 and Examples 12.1 to 12.7 run with no
  gap and no repeat, each cited at or before its place; every fence is
  tagged `text` and none is over 64 columns; each image line is followed by
  one blank line and its `art:` comment; footnotes `12-allowance`,
  `12-ingram`, `12-kdpdate`, `12-adapter` are prefixed and unique. Figures:
  finding 4.
- The arithmetic was rechecked: Example 12.2 (every cell), Table 12.4 (all
  seven wraps, including the Lulu casewrap's 0.125in per-panel width delta
  and IngramSpark's -0.185in), the house wrap 12.75 by 9.25, and Example
  12.4's sum of 93 and check digit 7.

## Findings

### 1. Chapter 5 cited by a short title (blocks)

Quote (l.263): "Chapter 5, *Figures and plates*, describes the pass for the
interior."

Rule: cross-reference title (brief item 4). The file's heading and
design.md row 5 read *Figures, plates, and illustrations*; Ch. 4 l.97, Ch. 7
l.167, Ch. 9 l.45, Ch. 10 l.211, and Ch. 11 l.220 cite it so. Already raised
as continuity-05, finding A; copy-12 #41 reproduced the short title in its
fix.

Fix: "Chapter 5, *Figures, plates, and illustrations*, describes the pass
for the interior."

### 2. The logomark under three other names (should)

Quote: "a press logo" (l.19); "the imprint logo" (l.219); "the logo"
(l.265, 267 twice, 269 twice, 272).

Rule: one name per thing. Chapter 11 defines *logomark* (l.18, "the
printer's mark of the imprint"); Chapter 5 says "logomark" throughout the
same print-safe material (Table 5.6, l.364, 368, 371); the vocabulary's art
target row names it `logomark`. copy-12 #43 settled the chapter on "logo"
for internal consistency, which went the other way from Chapters 5 and 11.
("Imprint logo" is the source's comment wording, not a name to adopt.)
The same split is open across Chapters 3, 10, and 11 (continuity-11,
finding 5, which asks for a vocabulary ruling); this finding asks for
*logomark*.

Fix: "logomark" at each place: "flagged a press logomark for transparency"
(l.19), "the logomark there at 1.1in wide" (l.219), "caps the logomark at
1000 pixels" (l.265), "and the logomark at 649 pixels. The logomark prints
1.1in wide" (l.267), "since the logomark is ink on transparency ... a
1024-pixel logomark" (l.269), "point its logomark at" (l.272).

### 3. "Each figure" for figures and plates (should)

Quote (l.265): "the pass caps the logo at 1000 pixels on its long edge and
each figure at 1900 pixels".

Rule: vocabulary (*figure* is a numbered illustration only) and shared fact
"Print-safe pass" (Ch. 5 Table 5.6: "each interior figure and plate"). As
written, the plates, the bulk of what the pass caps, are left out.

Fix: "and each figure and plate at 1900 pixels".

### 4. Figure order against the file slugs (may)

The figures are cited and placed in the order spine math (l.99, 101), cover
wrap (l.195, 197), print pack graph (l.277, 279). *figure-numbering.lua*
numbers by sequence, so the spine-math figure prints as Figure 12.1 from
*12-02-spine-math.png*, and the cover wrap as Figure 12.2 from
*12-01-cover-wrap-anatomy.png*. design.md row 12 lists the cover wrap as
12.1.

Rule: brief item 6 (slug `CC-NN-slug` matches the number). Ch. 2 and Ch. 4
set the precedent: reading order wins and design.md is updated (dev ruling
4).

Fix: rename the two untracked PNGs to *12-01-spine-math.png* and
*12-02-cover-wrap-anatomy.png*, update the two image lines, and swap 12.1
and 12.2 in design.md row 12. No `@fig:` id changes.

### 5. "Every image" through the print-safe pass (may)

Quote (l.263): "The press therefore passes every image through a
*print-safe* pass before the image goes onto paper."

Rule: shared fact "Print-safe pass": the pass copies only the logomark,
the top-level *assets/* JPEGs, and *assets/woodcuts/*; elsewhere `press
print` stops with "file not found" (Ch. 5 l.364). Carried from
continuity-05, finding D; Ch. 10 l.184 and Ch. 11 l.316 share the loose
wording.

Fix: "passes each interior image, from the directories Chapter 5 names,
through a *print-safe* pass".

### 6. "Writes a JPEG at quality 88" (may)

Quote (l.265): "It writes a JPEG at quality 88, and every other image as a
PNG."

Rule: shared fact (Ch. 5 l.362: "It writes a JPEG source as a JPEG at
quality 88"); copy-12 #42 raised the ambiguity and the line kept it.

Fix: "It writes a JPEG source as a JPEG at quality 88, and every other
image as a PNG."

### 7. Three of the chapter's terms used before or without a definition (may)

- *edition manifest*: first at l.277 ("computes the edition manifest"),
  again at l.382, 384, 491, never defined. Fix at l.382: "the *edition
  manifest*, the JSON file the gate writes with the production facts and
  their hash".
- *qualification*: defined in roman at l.336 ("Qualification means one
  physical copy ..."). Fix: italicize it there.
- *commerce gate*: first at l.159, defined in Ch. 7 (l.424) but not here
  (the per-chapter italic rule). Fix at l.159: "the *commerce gate*, the
  last step of `press all`, which guards print ordering".

### 8. The seal file under a second name (may)

Quote (l.72): "a short hash of its geometry, recorded in the press's own
seal ledger. A selftest recomputes every hash".

Rule: Ch. 9 l.393 names the file *profile-seals.yaml*, the digest "of its
contents", and the check `check_profile_seals`. "Ledger" is also this
chapter's word for *quality/providers.yaml* (l.88 onward) and the
vocabulary's for the table of authorities.

Fix: "a short digest of its contents, recorded in *profile-seals.yaml* in
the press's package data. The check `check_profile_seals` recomputes every
digest".

### 9. "A house 6 by 9 paperback" (may)

Quote (l.36): "the Alice book stays a house 6 by 9 paperback."

Rule: one meaning per word. "House" here could be read as the provider,
but from l.425 the Alice book is printed at Lulu with `print.provider` set
to `lulu` (Examples 12.6, 12.7).

Fix: "the Alice book stays a `house-6x9` paperback."

### 10. "Draws all of these numbers on one page" (may)

Quote (l.86): "The section "The layout" later in this chapter draws all of
these numbers on one page."

Rule: promise kept in part. "The layout" (l.173) and Figure 12.1 draw the
house wrap's spine, bleed, and panels; hinges and margins appear only in
Example 12.3 and Table 12.4, and the trims, bindings, and page bounds a
shop accepts appear in Table 12.3, not in that section.

Fix: "The section "The layout" later in this chapter shows how these
numbers place the bands of the cover wrap."

### 11. The vocabulary's provider ids (may, for `docs/vocabulary.md`)

The vocabulary row *provider* lists `house`, `lulu`, `kdp`, `ingram`. The
press's provider id is `ingramspark` (*data/provider-specs/ingramspark.yaml*;
the chapter at l.86, Table 12.3), and `ingram` is only the `press publish`
channel (*publish.py* l.31; the chapter at l.391). The chapter is right.

Fix: in vocabulary.md, `ingramspark` in the provider row.

### 12. Spellings and the edition gloss (may)

- l.55 "the web settings": the vocabulary's spelling is "Web". Fix: "the
  Web settings".
- l.19 names "the Print edition" without its format; the gloss arrives at
  l.151 as a path. Fix at l.19: "the Print edition (the reading PDF)".

### 13. "Prints only the jacket" for linen (may)

Quote (l.49): "A `linen` cover is cloth, so the press suppresses the
printed field and prints only the jacket."

Rule: "jacket" is barred for the cover wrap and is also the `dust-jacket`
binding. The press's own plan pairs linen with the dust jacket (*PRINT-PROFILES-PLAN.md* l.30, 156: "yes (linen case)"; *gen_coverwrap.py* l.358: "linen case: the material is the finish; no printed field"), so the fact is right and the word is the problem: a reader may take "the jacket" for the cover wrap.

Fix: "A `linen` cover is cloth, so the press suppresses the printed field on the case and prints only the dust jacket that goes over it."

### 14. Appendix C and Chapter 12 each send the reader to the other (should)

Quote (l.300): "Appendix C, *Messages and refusals*, collects these
messages." (the `verify_coverwrap` transparency and front-art messages, and
by placement the chapter's others).

Rule: promise kept (brief item 5). The draft of App. C (l.448) says only
"Chapter 12, *The print pack*, lists the cover wrap checks", and holds none
of the chapter's messages: not `coverwrap needs assets/cover.jpg`, the
soft-mask line, "the cover art did not survive", `unknown print profile`,
the commerce gate's "order and inspect a copy ..." line, or the
check-digit refusal. The reader is sent in a circle.

Fix: in App. C, add a `press coverwrap` / `verify_coverwrap` group and a
commerce group quoting those messages (the appendix's own convention).
If App. C is to stay a pointer, change l.300 to "Table 12.5 gives the
checks; the messages above are the ones you will meet."

## Bible

Updated `docs/continuity.md`: Chapter 12's terms, shared facts, the
promises in and out, and its numbering row; the open rows that waited on
Chapter 12 are marked kept.
