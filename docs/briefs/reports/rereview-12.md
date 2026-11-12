# Re-review: Chapter 12, The print pack

File: `book/chapters/12-the-print-pack.md` (496 lines), against
facts-12, dev-12, copy-12, type-12, the Revision section of report-12,
the production ledger's rulings, and facts-12 S1. Nothing edited, nothing
committed.

**Verdict: REVISE.** Open: 1 blocks, 5 should (the limit is three
shoulds). The writer resolved all 7 of the copyeditor's blocks, all 3 of
the typesetter's blocks, and all 11 of the fact checker's blocks. What is
left is one new factual overstatement in the deltas paragraph, two
partial carry-overs from the developmental edit, one vocabulary ruling
not applied, and two wording faults that the revision introduced. All six
are one-sentence or mechanical fixes.

## Mechanical checks

- `press check`: exit 0 for this file. Source checks pass. The editorial
  failures all name *book/appendices/c-messages.md*, which is not this
  chapter.
- `ste_check.py`: 42 findings. They are accepted as before (tables, code,
  art comments, quotations, -ing A-heads, "therefore", "whether"), except
  for the prose paragraphs at 165 (7 sentences), 191 (10), and 215 (8).
  These are graded may, after the copy desk's sidebar precedent (item 38).
  Line 191 is the deltas paragraph, and the blocks fix below should split
  it as well.
- Every fence is tagged `text`. No code line is over 64 columns (the
  longest line in Example 12.5 is 54 columns).
- Each `art:` comment comes after its image, with one blank line between.
  Image line plus comment: Figure 12.1 183 words, 12.2 167, 12.3 184. All
  are under 190.
- Every footnote label begins with `12-`, and `[^isbn]` is gone. The
  chapter is ASCII only.
- The figure PNGs are still 5 KB placeholders, so Type S4 (the caption of
  Example 12.7 splitting from its fence) stays deferred until the real
  art arrives.

## Findings table

| Desk | No. | Sev. | Status | Note |
|---|---|---|---|---|
| facts | U1 | blocks | declined-accepted | The no-cover line is in facts-07 and facts-08. Cross-slice facts are admissible. It is now what the target prints without a cover, not an Alice session (157). |
| facts | U2 | blocks | declined-accepted | The colored-ink message and the plate source are in facts-04 and facts-08. The `text` remedy was added (165). |
| facts | U3 | blocks | resolved | The timing is cut ("before LuaLaTeX sets a single page", 51). |
| facts | U4 | blocks | resolved | "with mirrored margins" only (151). |
| facts | U5 | blocks | resolved | The art comment says "No safety line" (197). |
| facts | U6 | blocks | resolved | `press publish` is a side branch off `verify_coverwrap` (273, 277). The gate builds the interior and wrap itself. |
| facts | U7 | blocks | resolved | The text now says the mediabox is checked within 0.01in (217). |
| facts | U8 | blocks | resolved | No command is named (70). |
| facts | U9 | blocks | resolved | The tip names the filter. The remaining clause is a plain corollary (268). |
| facts | C1 | blocks | resolved | "gives the rule plainly" (88). |
| facts | C2 | blocks | resolved | The hinge is in the width only (206). |
| facts | D1 | should | declined-accepted | "×" is outside the glyph law (markup.md 46), so "6x9" inside the quotation is forced. |
| facts | D2 | should | resolved | "At the time of this writing, press 3.0.2" (57). |
| facts | D3 | should | resolved | The count is dropped. |
| facts | D4 | should | resolved | The provider changes the arithmetic and what the shop makes (36). |
| facts | D5 | should | resolved | Alice has *assets/cover.jpg* throughout (19, 157, 423). |
| facts | D6 | should | resolved | "0.5in up" (221). |
| dev | C1 | should | resolved | `press publish` is the route for both shops (384). |
| dev | C2 | should | resolved | The `press print` paragraph covers when to run it and what it writes (153). |
| dev | C3 | should | resolved | Table 12.8 shows the checklist's shape. |
| dev | P1 | should | resolved | Trim, bleed, and safety are defined in "The layout" (175, 177). Allowance is defined at 92. |
| dev | P2 | should | resolved | Example 12.1 is framed as a sample, and Alice stays house 6 by 9 (36). |
| dev | P3 | should | resolved | `print.paper` values and the command are shown (137 to 141). |
| dev | P4 | should | resolved | The bleed is fixed, and the provider no longer owns it (86, 175, Table 12.1). |
| dev | P5 | should | resolved, with new blocks NB1 | The deltas are explained and the strip is glossed. The dust-jacket claim overreaches S1 (see NB1). |
| dev | P6 | should | **open** | See O1. |
| dev | P7 | should | resolved | Table 12.3 house row. |
| dev | P8 | should | resolved | "Tag the block `text` instead" (165). |
| dev | P9 | should | **open** | See O2. The `product_id` and `inspector` parts are resolved. |
| dev | P10 | should | resolved | Placeholder seller. The prose gives the docs' sample, the ledger's `unsupported`, and "confirm it before you publish the link" (467, 476). |
| dev | P11 | should | resolved | The researched list is separate from `print.provider` (315). |
| dev | P12 | should | declined-accepted, with part resolved | The fact base has no refusal text for a session. The wrap messages now point to Appendix C (296). |
| dev | R1 | should | resolved | Seals and lifecycle take 3 sentences. Forbidden keys, capabilities, and the guard pattern each take one sentence. The ledger projection takes one. |
| dev | R2 | should | resolved | One sentence (239). |
| dev | R3 | should | resolved | The hardcover figures are in Table 12.3. The UNCONFIRMED paragraph says to order a proof (133). |
| dev | R4 | should | resolved | The duplicate tip sentence and the seller caution are cut. Line 415 points back to the tip. |
| dev | R5 | should | resolved | "the roadmap's Icebox, its list of deferred work" (489). |
| dev | O1 | should | resolved | The opening gives the why, with `alice` as the only cast (19). |
| dev | N1 | should | resolved | Figure 12.1 is in "The layout", after Example 12.3 (195). |
| dev | N2 | should | resolved | The column key comes before Example 12.2 (107). |
| dev | N3 | should | resolved | `[^12-kdpdate]` is on Table 12.3's lead-in (122). |
| copy | 12 | blocks | resolved | The "shipped" sentence is cut with the lifecycle list. |
| copy | 33 | blocks | resolved | "the ISBN that the press's selftest checks" (227). The footnote is deleted. |
| copy | 36 | blocks | resolved | "shows only" (242). |
| copy | 48 | blocks | resolved | The meta-narration sentence is gone (328). |
| copy | 52 | blocks | resolved | "when an inspection stops holding" (380). |
| copy | 56 | blocks | resolved | "A press book meets two kinds of order" (411). |
| copy | 62 | blocks | resolved | "You can ignore that note" (441). |
| copy | 1, 22 | should | resolved | "the Print edition" (19, 151), glossed with *dist/alice.pdf*. "printing press" (151). |
| copy | 3, 6, 7, 8, 25, 26, 27, 31, 63 | should | resolved | American spelling in prose. "colour" (76) and "centred" (340) remain only inside verbatim quotations. 8: the warning is cut to two sentences. 31: the TeX expression is dropped. |
| copy | 9, 10 | should | resolved | The lifecycle subcommand passage is cut (R1). |
| copy | 13, 16, 17, 18, 21, 24, 28, 30, 32, 37, 39, 40, 41, 43, 45, 46, 47, 49, 53, 58, 64, 66, 67, 69 | should | resolved | Each is applied as given or by an equivalent (checked line by line). |
| copy | 23 | should | resolved | The closer is gone, and the tip is one sentence (162). |
| copy | 34, 35 | should | resolved | The guard-pattern paragraph is cut to one sentence (R2). |
| copy | 44 | should | resolved | "stage" is gone (273). |
| copy | 59 | should | resolved | The warning comes before the procedure, with "draws" (418). |
| copy | 68 | should | resolved | The Icebox is glossed and the two ideas are split (489). |
| type | B1 | blocks | resolved | The B-head is "The placeholder that says pending". "honest" remains only in the verbatim success line (306). |
| type | B2 | blocks | resolved | "harmless" is cut. |
| type | B3 | blocks | resolved | The labels are `12-` prefixed. |
| type | S1 | should | resolved | Example 12.5 is at most 54 columns. |
| type | S2 | should | resolved | Figure 12.1 totals 183 words. |
| type | S3 | should | resolved | The spine and bleed labels sit outside on leaders. The detail moved to the report. |
| type | S4 | should | declined-accepted (deferred) | The art is still placeholders. Recheck at the first build with real PNGs. |
| type | S5 | should | resolved | Cell wrapping and 20/55/25 widths are in the comment. |
| re-review | NB1 | blocks | **open** | New. See below. |
| re-review | NS1 | should | **open** | New. Vocabulary ruling. See below. |
| re-review | NS2 | should | **open** | New. "allowance" has two meanings. See below. |
| re-review | NS3 | should | **open** | New. The KOMA scar paraphrase is backward. See below. |

## Open items

### NB1 (blocks). Dust-jacket deltas stated as zero for every provider

Quote (191): "The two deltas adjust the panel to the binding. For a paperback
and for a dust jacket, both are zero."

S1 says the deltas are "zero for a paperback or a dust jacket *unless the
provider spec says otherwise*", and that they are read from the
provider's `cover.bindings.<binding>` entry. The source confirms that one
spec does say otherwise. *src/press/data/provider-specs/ingramspark.yaml*
gives the IngramSpark dust jacket `panel-width-delta: 0.4375` and
`panel-height-delta: 0.25`. It also gives the IngramSpark casewrap a
negative width delta (-0.185), which is why Table 12.4's 14.3305 is
narrower than its margins, hinges, trim, and spine alone give. An author
who reads the sentence designs an IngramSpark jacket to the wrong panel.

Fix: "The two deltas adjust a panel from the trim to the board or jacket
size, and the provider's spec sets them. For a paperback, both are zero.
For a hardcover, they depend on the provider. The Lulu casewrap in Table
12.4 comes out 0.25in taller and 0.25in wider than its margins, hinges,
trim, and spine alone give, and that difference is the two deltas. A
delta can also be negative, which is why the IngramSpark casewrap is
narrower than the same sum." Split the paragraph at "The two deltas" (it
has 10 sentences now).

### O1 (should, dev P6). The reader still cannot size the cover art

Quote (215): "The cover art belongs on the front panel. ... The press sets
the title as type, and the verifier reads it back as text."

The front panel is now named, which resolves the larger half. Two things
are still missing for the reader who has to prepare a cover that fits:

- **What the press sets.** The press's own type (title, description, logo,
  publisher) goes in the back-cover text block. The fact base supports
  this: facts-12 B.3, "the coverwrap back-text width ... their back-cover
  text box". The front is the art alone. The cover-design skill says to
  "name every line of text verbatim; front board only" (facts-15). As
  written, the sentence lets the reader think the press sets the title
  over the front art, so the reader leaves it out of the art.
- **What size the art fills.** In source (`gen_coverwrap.py:146-148,
  379-381`), the art is placed at `front_x` and scaled to the front panel
  plus the outer bleed, for the full wrap height: 6.125 by 9.25in for the
  house example. A hinged or flapped cover keeps it to the panel. This is
  not yet in the fact base, so it needs an S2 from the managing editor
  before the chapter can state it.

Fix: "The cover art fills the front panel, and the wrap verifier looks
for it there and fails a wrap whose front panel is nearly flat. The press
sets its own type, the title, the description, the logo, and the
publisher, on the back panel. Any lettering on the front belongs in the
art itself, as Chapter 11 describes." After S2, add: "On a paperback the
art runs out through the bleed on the outer edge and at the top and
bottom, so for the house example *assets/cover.jpg* should be drawn to
6.125 by 9.25 inches."

### O2 (should, dev P9). Where the `edition_id` comes from

Quote (378): "You do not choose the id. The press computes it, and the
commerce gate computes it each time it builds the edition manifest."

The reader still cannot fill `edition_id` in Example 12.6. The writer's
reason, that the fact base names no command, holds. But the dev fix
allowed for this case ("if the fact file is silent, say so honestly"),
and the chapter says nothing. In source, the gate's summary prints only
the first 12 characters (`commerce.py:361`), so this is a gap in press
itself and worth a press issue.

Fix: add after the quoted sentences: "At the time of this writing, the
press documentation names no command that prints the full id for you to
copy into the record." The managing editor may want to file the press
issue.

### NS1 (should). The ruling "the Alice book" is not applied

The ledger rules that "the Alice book" means the full-novel sample, and
that open revisions apply it. The chapter's sample is that book
(*dist/alice.pdf*), but six places say "the Alice example": lines 19, 36,
157, 350, 421, 457.

Fix: replace each with "the Alice book" (19: "The Alice book here is a 6
by 9 paperback ..."). No "Pages bundle" or "Pages site" occurs, so that
ruling has nothing to apply.

### NS2 (should). "allowance" has two meanings

Line 92 defines an *allowance* as "a fixed amount added on top of the
thickness of the pages", meaning a spine figure. Two later places use the
word for something else:

- Table 12.1 (32): "the spine arithmetic, the hardcover allowances".
- Line 191: "The *inner* band is the sum of the binding's own allowances:
  `inner = hinge + flap + strip`."

The reader working the wrap meets one defined term with two meanings.

Fix: in Table 12.1, write "the spine arithmetic, the hardcover margins
and hinges". At 191, write "The *inner* band is the sum of the binding's
own extra widths: `inner = hinge + flap + strip`."

### NS3 (should). The KOMA scar paraphrase is backward

Quote (155): "and `open=right` would put a blank verso before every chapter
that ends on a recto."

The fact base gives "would ship genuinely blank versos" (facts-04,
facts-14). The blank verso comes after a chapter that ends on a recto,
before the next chapter. The sentence as written puts it before the
chapter that ends on the recto.

Fix: "and `open=right` would leave a blank verso after every chapter
that ends on a recto."

## Mays noted, not counted

- Prose paragraphs 165 (7 sentences) and 215 (8): split if convenient.
- 88: "The copy inside the installed press is generated from it" has a
  hidden actor. A possible fix: "The press generates its installed copy
  from it."
- Table 12.4 "board margin" (206) beside "the turn-in" (191) and
  "margin" (Table 12.3). The dev edit asked for one word for the board
  fold. "margin" glossed once as the turn-in is enough, so drop "board".
- 72: "prove it at its trim". "prove" is not the watchlisted "proves", and
  it paraphrases the lifecycle doc. Accepted.

## Reading as the cover maker

With NB1 and O1 fixed, the chapter gets the reader from the four keys to
the spine figure, to the wrap's seven bands with their sizes, to where
the art and the barcode sit and what the press sets itself, and to the
safety margin they must keep by hand. The layout section is now the
strongest part of the chapter. Figure 12.1 sits where its numbers are
worked, and Table 12.4 can be reproduced from Example 12.3 for every row
once the reader knows that deltas exist and can be negative.
