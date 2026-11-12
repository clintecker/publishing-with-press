# Report: Chapter 12, The print pack

File: `book/chapters/12-the-print-pack.md`. Nothing committed.

## Word count

`press wordcount`: 6528 (target 6,000; within 15 percent, ceiling 6,900).
The count includes tables, examples, captions, and art directives.

## Shape

- Eleven A-heads in the brief's order. B-heads under Design profiles
  (digests and seals, colour profile, new profiles), Providers (spine
  shapes, what each provider makes, paper and the Lulu paperback), Cover
  wrap (layout, what the press draws), Barcode (EAN-13 arithmetic, honest
  placeholder), Qualification (researched providers, eleven points,
  edition identity), Ordering (printing at Lulu, print ordering for
  readers).
- Tables 12.1 to 12.10, Examples 12.1 to 12.7, Figures 12.1 to 12.3, each
  referenced before it appears.
- Sidebar: war story 15, the barcode that crowded its quiet zone (150
  words). War story 23 (602 PPI) is body text in "Print-safe images",
  since Chapter 5 already tells it.
- Four tips, three warnings. Five footnotes (house allowance comment,
  Ingram official formulas, canonical ISBN, KDP verified date, Lulu
  adapter reachable only from tests).

## Figures

- **12.1 `cover-wrap-anatomy`** (page anatomy): the house 6x9, 200-page
  cream perfect-bound wrap to proportion (12.75 x 9.25): back, spine,
  front, bleed 0.125, trim, safety, the spine and wrap formulas worked,
  barcode box with its 0.5in offsets, spine-text threshold. Placed in
  "Providers and their numbers" so it numbers 12.1 ahead of 12.2;
  "The cover wrap" refers back to it.
- **12.2 `spine-math`** (matrix): five rows (house, kdp, lulu paperback,
  lulu hardcover, ingramspark) by spine shape, formula or table,
  allowance. Allowance blank for Lulu hardcover and IngramSpark.
- **12.3 `print-pack-graph`** (pipeline): print profile and print-safe
  assets, print interior, verify_pdf print profile, gen_coverwrap,
  verify_coverwrap, press publish, edition manifest, qualification,
  commerce gate (drop-shadowed, last).

## Facts I needed and left out

- No house safety value: the fact table gives "0.125" alone for house.
  Figure 12.1 draws a "safety" line with no number. Provider safety
  values appear only as the ledger's declarations (Table 12.3); I say
  nothing about whether press applies them (contradiction B.4).
- No captured `press print`, `press coverwrap`, or `press publish`
  session. The only session shown is `press verify-print` ending in the
  no-cover line quoted in Chapter 8.
- The exact `check_selection` refusal text is not in the fact file; the
  chapter says only that the checker refuses and where the message comes
  from.
- Profile geometry (margins, caps per profile) is in facts section 7.2,
  which I did not have; deferred to Chapter 9.
- The file holding the `commerce` block is not named in the facts. I
  wrote *config/metadata.yaml*, inferred from contradiction A.25 (the
  metadata template's comment about enabling it). Please confirm.
- Cover art cap "590 x wrap_h px" is read as 590 pixels per inch of wrap
  height; the logo cap (649 px at 1.1in = 590 PPI) supports that reading.

## Contradictions handled

- A.12: Lulu is not called the seller of record. The chapter states the
  press's model (provider sells, the field names it), the ledger's
  `unsupported` for Lulu, Peecho as the only `supported`, and tells the
  publisher to confirm. Example 12.7 keeps the docs' `"Lulu"` value.
- A.13: the chapter says Lulu's paperback spine ignores paper, the default
  provider is `house`, and a Lulu book should set `print.provider lulu`.
  The LULU.md troubleshooting row about paper is given with that caveat.
- Colour refused at Lulu and IngramSpark, stated as the press's refusal
  with "the press will not guess a thickness".
- B.13: `press all` builds neither print nor coverwrap; the commerce gate
  (ordering-enabled books only) does, and the chapter says both.
- A.18: colour profile "keeps plates in colour instead of greying them",
  with no claim that every other profile greys.
- A.25: no `press qualify`; qualification is recorded by hand.
- Not mentioned: back-text width from legacy trim, unused spine-text
  minimums, page-thickness on Lulu hardcover, double interior build,
  page bounds only in coverwrap, the pdfimages note softening.

## Checker residuals

- `press check`: passes, no error naming this file. Its "inspect: spine"
  notes are the literal book spine; "honest" is the press's own term for
  the placeholder; "harmless" paraphrases LULU.md.
- `ste_check.py`: remaining findings are in tables, code, art comments,
  quotations ("is researched", "was added", "v1 value; real specs use
  0.06", the YAML privacy line, the "does not process or store" quote),
  headings with -ing words (the brief's own A-heads), "therefore" and
  "whether" (relaxed by the prose contract), and "has" as possession
  flagged as perfect tense. Semicolon findings are all inside code or
  quotations. No prose semicolon or passive remains that I can find.

## Revision

Applied facts-12, dev-12, copy-12, and type-12 under the coordinator's
rulings. `press check` passes (only literal "spine" inspect notes for this
file). `press wordcount`: 6577 (target 6,000; within 15 percent).

### Facts
- Lulu casewrap row: board margin adds to width and height, hinge to width.
- "four words" replaced ("gives the rule plainly").
- Figure 12.1: no safety line; spine and bleed labels outside the
  rectangle on leaders; moved to "The layout" after Example 12.3.
- Figure 12.3: `press publish` is a side branch off `verify_coverwrap`;
  the main chain runs to edition manifest, qualification, commerce gate,
  and the prose says the gate builds interior and wrap and computes the
  manifest itself.
- Timing ("few seconds") cut. "wrong size never reaches dist/" cut.
  "costs you one run of the checker" cut. Gutter gloss cut ("mirrored
  margins" only). Tip reason restated from 10.7.
- `verify-print` no-cover line and `colored ink` message kept (rulings).
- "press 3.0.2" now carries "at the time of this writing".
- Alice has cover art throughout; the no-cover line appears as what the
  target prints without a cover, not as an Alice session.
- "Three targets build the interior" dropped. Provider now changes the
  arithmetic and what the shop makes. "0.5in up" without "bottom edge".
- Declined (may): pdfimages softening (B.14), legacy trim (B.3), page
  bounds only in coverwrap (B.6): all are on the bug list, and the brief
  forbids documenting them.

### Developmental
- Wrap written from the author's side: trim, bleed, safety defined in
  "The layout" (safety: ledger figures, press does not draw or check it);
  allowance defined with the spine shapes; inner, flap, strip glossed;
  deltas explained (zero for paperback and dust jacket; the Lulu
  casewrap's 0.25in extra in each direction derived from Table 12.4).
- "What goes on the wrap": art on the front panel (from the front-art
  check), title as text, field, logo, barcode, spine text; Chapter 11
  for art. TeX color expression dropped from prose.
- Bleed owner: fixed 0.125in everywhere, Table 12.1 and the provider
  definition no longer give the provider the bleed.
- House provider: lists three bindings and keeps no trim or page list,
  so refuses none (Table 12.3); "refuses nothing" removed.
- `press print` paragraph (pandoc, latexmk, `print.yaml`, two-sided,
  print-safe filter, from facts-07), plus the KOMA `open=any` scar.
- KDP and IngramSpark: `press publish` named as the route; checklist
  shape as Table 12.8 (three sections, contents from 10.10).
- `edition_id`: the press computes it; the commerce gate computes it with
  the manifest. No standalone command or manifest path is in the fact
  base, so none is named.
- Example 12.7: `seller-of-record` is a placeholder; the prose says the
  docs' sample writes "Lulu", the ledger says `unsupported`, confirm.
  `storefront-url` and `policies` glossed (facts-03).
- `print.paper` shown with its values (facts-03 / Chapter 3).
- Researched list separated from `print.provider` values.
- Contributor material cut to a sentence each: seals and lifecycle,
  forbidden keys (two examples), capabilities (count plus two), EAN guard
  pattern (one sentence). Ledger projection to one sentence.
- Hardcover figures moved into Table 12.3; the UNCONFIRMED paragraph now
  says what to do (proof). Duplicate tip sentence and seller caution cut.
- Opening says why the reader is here. Icebox glossed as the roadmap's
  list of deferred work. Footnote `12-kdpdate` moved to Table 12.3's
  lead-in. Example 12.2 key moved before it. Color-code paragraph gives
  the remedy (tag `text`). Wrap messages point to Appendix C.
- Declined: showing the `check_selection` refusal as a session (no text
  in the fact base).

### Copy and type
- Watchlist blocks fixed: "shipped", "canonical", "proves", "goes
  stale", "harmless"; B-head now "The placeholder that says pending" and
  the "honest placeholder" quotation dropped from prose (it remains only
  inside the verbatim success line).
- Meta-narration ("this book does not repeat it", "two kinds of order in
  this chapter") rewritten. "reading PDF" is now the Print edition.
  Golden copy defined at first use. American spelling in prose ("colour"
  and "centred" remain only inside quotations). Two-idea sentences split
  where flagged; Lulu warning moved before the procedure; step 6 split.
  `inspector: "alice"`. Table 12.6 dispositions in code. Caption names in
  code. Numerals for 10 and over except "eleven points" and "twelve
  digits" (accepted may).
- Footnotes prefixed with `tools/prefix-footnotes.py`; `[^isbn]` deleted.
- Figure 12.1 image plus comment 183 words, 12.2 167, 12.3 184.
- Figure 12.2 cells shortened, widths 20/55/25, wrap inside cells.
- Example 12.5 re-broken to 60 columns or less; Example 12.6 longest
  line shortened.
- Example 12.7 caption-fence page split: recheck after real PNGs land.

### Figure notes (detail moved out of the directives)
- 12.1: drawn at about 107 px per inch at full measure; spine 53 px,
  bleed band 13 px, so all spine and bleed labels go outside on leaders;
  minimum label height about 24 px; the barcode box (about 1.235 by
  0.9in of bars on a white card) may carry its own label inside. The
  spine-text rule (drawn only at 0.25in or wider) can sit below the page
  as a note if room allows.
- 12.2: the Lulu hardcover cell abbreviates the 26 bands to the first
  and last; the full table is 24-84 pages 0.25in, 85-140 0.5in, then
  +0.0625in per band to 779-800 pages 2.0625in.

## Revision 2

Applied the six open items of rereview-12 with facts-12 S1 to S3.
`press check` passes; `press wordcount` 6746 (within 15 percent of 6,000).

- NB1 (blocks): the deltas paragraph now says the provider's spec sets
  the deltas, zero for the house and KDP soft covers, provider-dependent
  for hardcovers; gives the Lulu casewrap 0.25in derivation and
  IngramSpark's own deltas (jacket 0.4375 and 0.25, casewrap -0.185), and
  why the IngramSpark casewrap is narrower. The ten-sentence paragraph is
  split at "The two deltas".
- O1: what the art fills (front panel, full wrap height bleed to bleed,
  plus the outer bleed on a soft cover: 6.125 by 9.25in on the house
  wrap; panel width alone with a hinge or flap) and what the press sets
  (its own type and the 1.1in logo on the back, barcode lower right; any
  front lettering belongs in *assets/cover.jpg*). Paragraph split in two.
- O2: the press shows only the first twelve characters of `edition_id`
  (gate line and `press.edition verify`); the full value lives in the
  manifest the gate writes, and the reader copies it from there.
- NS1: "the Alice example" is now "the Alice book" at all six places.
- NS2: "allowance" kept for the spine figure only. Table 12.1 reads "the
  hardcover margins and hinges"; the hinge, flap, and strip are "the
  inner offset" in the layout text and the seven-band list.
- NS3: `open=right` leaves a blank verso after a chapter that ends on a
  recto.
- Mays taken: hidden actor at the ledger-projection sentence fixed ("The
  press generates its installed copy"); "board margin" in Table 12.4
  is now "margin".

## Revision 3

Continuity-12 applied: Chapter 5 cited as *Figures, plates, and
illustrations*; "logomark" throughout; the pass caps "each figure and
plate"; "a JPEG source"; Appendix C pointer replaced ("`verify_coverwrap`
reports each fault by name"); *edition manifest*, *qualification*, and
*commerce gate* italic at first use; seals named as *profile-seals.yaml*
and `check_profile_seals`; "Web"; Print edition glossed "(the reading
PDF)"; `house-6x9` paperback; "The layout" promise narrowed; linen prints
"only the dust jacket"; "each interior image, from the directories
Chapter 5 names". Figure files renamed to match print order:
*12-01-spine-math.png* (Figure 12.1), *12-02-cover-wrap-anatomy.png*
(Figure 12.2), *12-03-print-pack-graph.png*; image lines updated. The
figure notes above for "12.1" (wrap) now apply to Figure 12.2, and
design.md row 12 still lists the wrap as 12.1 (not my file; for the
managing editor). `press check` fails only on two unreferenced Chapter 14
plates (not this file). Word count 6792.
