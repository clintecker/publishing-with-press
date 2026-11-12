# Developmental edit: Chapter 12, The print pack

Desk: developmental editor. File: `book/chapters/12-the-print-pack.md`
(509 lines). I read it as the design's reader would: an author who can use
a shell and does not know TeX. Line numbers refer to the file as read.

Status: DONE_WITH_CONCERNS. 0 block, 24 should.

## 1. Coverage

All eleven A-heads from the brief are present, in order, in sentence case,
with prose between every pair of headings. Every core topic in the design
row is reached: the four choices, profiles and the lifecycle, provider
specs and spine math, `press print` and `verify-print`, the wrap, bleed,
the EAN-13, print-safe images, qualification and the golden copy,
`press publish`, the three shops, and ordering links. All three figures
and the suggested sidebar (war story 15) are present. No block.

| A-head | Line | Does the section deliver? |
|---|---|---|
| Four orthogonal choices | 21 | Yes. Table 12.1 and Example 12.1 make the point, and the refusal paragraph shows the payoff. The example leaves the running book in a state the rest of the chapter ignores (P2). |
| Design profiles | 53 | Yes, for the author, in Table 12.2 and the colour warning. Two of its three B-heads are for contributors and run long (R1). |
| Providers and their numbers | 107 | Mostly. Spine shapes, Example 12.2, and Table 12.3 are the chapter's strongest material. Bleed, safety, and allowance are used and never defined (P1), and `print.paper` is never shown being set (P3). |
| Building the interior | 174 | Yes. The `press all` exception is the most useful paragraph in the chapter. The colour-from-code paragraph gives no remedy (P8). |
| The cover wrap | 194 | Partly. The arithmetic is there, but Example 12.3 rests on two terms it never explains (P5), and the author never learns what the cover art covers (P6). |
| The barcode | 238 | Yes. Placement, size, check digit, placeholder, and sidebar all land. The guard-pattern paragraph runs long (R2). |
| Print-safe images | 276 | Yes. Short, concrete, with the reason. |
| Verifying the print pack | 290 | Mostly. Table 12.5 is complete. Failures are named but not remedied (P12). |
| Qualification and the golden copy | 328 | Partly. The eleven points and edition identity are clear. The reader cannot fill Example 12.6 because the chapter never says where the `edition_id` comes from (P9). |
| Publish checklists | 403 | Mostly. The section describes the checklist file and never shows one (C3). |
| Ordering a copy | 422 | Yes. The Lulu procedure is followable. Example 12.7 contradicts the chapter's own seller warning (P10). |

**C1 (should). KDP and IngramSpark have no route of their own.** The design
row asks for "Lulu, KDP, IngramSpark as the docs and ledger state them".
Lulu gets a six-step procedure (lines 430 to 437). KDP and IngramSpark
appear only as numbers (Table 12.3) and as checklist items (Table 12.8).
The fact file holds a guide for Lulu only, so a matching procedure would be
invention. Fix: in "Publish checklists" or at the head of "Ordering a
copy", say in one or two sentences that for KDP and IngramSpark the
`press publish` checklist is the press's whole route, and that the press
documentation has no step-by-step guide for either shop.

**C2 (should). `press print` gets one clause.** Line 178: "`press print`
builds it from the design profile". The design row names `press print`
as core. The reader never sees it run, and never learns why to choose it
over `press verify-print`. Fix: the paragraph must say when an author runs
`press print` alone (for example, to look at the interior before any
verifier runs) and what it leaves in *dist/*.

**C3 (should). The checklist is described and never shown.** Line 411
names the three sections and the four file lines in a run of quotations,
and Table 12.8 gives the last section. The reader never sees
*dist/publish-kdp.md*. Fix: if the fact desk can supply the file's real
layout, add a short numbered example of the Alice checklist and refer to
it before it appears. If not, turn line 411 into a three-row table (section
and what it holds) so the shape is visible.

## 2. Path

**P1 (should). Bleed, trim, safety, and allowance are never defined.** The
reader does not know print. "Bleed" first appears at line 32 ("the
numbers for the spine, the bleed, and the wrap"), "allowance" at line 123,
"safety" in Table 12.3 and Figure 12.1, and none of the four gets a
definition. Bleed is core content in the design row. Fix: where these
terms first matter (with Figure 12.1, see N1), define each in a sentence:
what the bleed is for, where the trim line falls, what the safety line
protects, and what an allowance adds to a spine. Separately, for the fact
desk: the fact file (section 20.B.4) says provider `safety` values are
declared but unused. Table 12.3 and the art directive's dashed "safety"
line present them as numbers the press works to. The chapter must say the
press does not enforce a safety margin, or drop the figures.

**P2 (should). Example 12.1 leaves the Alice book as a Lulu 5 by 8
hardcover, and nothing after it agrees.** Figure 12.1, Table 12.4, and
the Lulu procedure all assume a house or Lulu 6 by 9 paperback. A reader
who ran Example 12.1 has a different book from the one the chapter then
works. Fix: frame Example 12.1 as a sample of the four keys that the
reader does not need to run, or follow it with the commands that put Alice
back on `house-6x9` paperback before the next section.

**P3 (should). `print.paper` is the fifth setting, and the chapter never
shows how to set it.** Table 12.1 lists four choices. Figure 12.1 (line
111) already says "cream stock", and line 166 says the spine reads
`print.paper`. The reader never sees `press config set print.paper ...`,
never learns the allowed values, and Figure 12.2 offers IngramSpark stocks
(`white-70`, `groundwood`) without saying whether the key takes them.
Fix: one sentence and one command at line 166, giving the values the fact
desk confirms.

**P4 (should). Who owns the bleed?** Table 12.1 (line 32) and line 109
say the provider decides "how far the bleed runs". Line 214 says the press
fixes it at `BLEED_IN = 0.125`, "universal across print vendors", and
Table 12.3 repeats 0.125in for every shop. The reader cannot tell whether
changing the provider can change the bleed. Fix: line 109 and Table 12.1
must agree with line 214: the provider supplies the spine and the
hardcover margins, and the bleed is the same everywhere.

**P5 (should). Example 12.3 rests on `width_delta` and `height_delta`,
and the chapter never says what they are.** Without them the reader cannot
reproduce Table 12.4: a Lulu casewrap works to 14.75in wide from the
figures given, not 15.0. The same paragraph introduces "strip" (line 214)
without a definition, and calls the board allowance a "margin" where line
47 called it a "turn-in". Fix: say what each delta is and when it is
non-zero (from the fact desk, if the fact file is silent), define the
strip beside the flap, and use one word for the board fold throughout.

**P6 (should). The author never learns what the cover art covers.** Line
198 says the wrap needs *assets/cover.jpg* and the metadata. Line 234
says the press lays down a "cloth-coloured field". The reader preparing
art needs to know whether the image fills the front panel or the whole
wrap, what shape it should be, and where the title, author, and publisher
are set on the back and spine. Fix: say what the press places on each
panel. The fact file is silent on image placement, so the writer must get
it from the fact desk or say plainly what the chapter cannot tell the
reader, and point to Chapter 11 for the art itself. Drop the TeX colour
expression `black!85!red!25!white` from prose, since this reader does not
read TeX; the RGB triple is enough.

**P7 (should). The house provider "refuses nothing", and also takes three
bindings.** Line 134: "it refuses nothing, because it has no catalog of
trims or bindings". Table 12.3: "The house provider takes `perfect-bound`,
`saddle-stitch`, and `coil`". The reader cannot tell whether a house
casewrap builds. Fix: make the two statements agree.

**P8 (should). The colour-from-code paragraph gives no remedy.** Line
192 explains that a fence with a language tag prints in colour and fails
the interior, then cites Chapter 4. The reader at the failure needs the
fix in place: what to type instead. Fix: add the remedy in one sentence,
in the terms Chapter 4 uses.

**P9 (should). The reader cannot fill Example 12.6.** Its `edition_id`
line is a placeholder, and the section that explains the id (lines 397 to
401) never says how to obtain it: which command prints it, or where the
manifest file lives. Line 401 then gives
`python3 -m press.edition verify <manifest.json>` for a file the reader has
never seen. The same example gives `product_id: "PB-BW-6x9"` with no word
on where it comes from, and `inspector: "Your Name"` where the running
sample is user `alice`. Fix: say where the id and the manifest come from
(fact desk; if the fact file is silent, say so honestly), explain
`product_id` in a clause, and make the inspector `alice`.

**P10 (should). Example 12.7 names Lulu as the seller after the chapter
warns twice against it.** Lines 347 and 490 say the ledger records Lulu
as `unsupported` for `seller_of_record` and tell the reader to confirm who
sells. Example 12.7 then sets `seller-of-record: "Lulu"`. The reader will
copy the example. Fix: either say in the lead-in that the value is the
documentation's sample and the reader must confirm it, or change the prose
so the example and the warning agree. Also say in a clause where the
`storefront-url` comes from (the shop's page for a published title).

**P11 (should). "Provider" means two lists.** Line 109 defines a provider
as one of `house`, `kdp`, `lulu`, `ingramspark`. Table 12.6 lists nine
other names (bookvault, peecho, mixam...), with KDP and IngramSpark absent.
The reader will try `press config set print.provider peecho`. Fix: one
sentence at line 334 saying the researched list is a ledger of ordering
candidates, separate from the four values of `print.provider`.

**P12 (should). Refusals are named but not remedied.** The design's
purpose is that the reader can "read a press refusal and know what to do".
Line 51 describes the `check_selection` refusal without showing it.
Line 315 quotes the transparency and front-art messages and the quiet-zone
check without a fix for any of them. Fix: show the provider refusal as a
two-line session (from the fact file, if it holds the message), and give
each wrap failure its remedy in a clause, or point to Appendix C,
*Messages and refusals*.

## 3. Proportion

**R1 (should). Contributor internals run long while the author's needs
run short.** The fact file labels the lifecycle "contributors, not
authors". The chapter spends about 350 words on seals and the lifecycle
(lines 72 to 105), plus the ledger projection and selftest at line 117,
`ProviderSpec.check_selection` (51), pypdf (196), the latexmk command line
(236), the sixteen forbidden manifest keys (401), and the eleven
capability names (334). Meanwhile P1, P5, P6, and P9 are gaps. Fix: keep
"Digests and seals" to two sentences (what a seal is, why the reader can
trust a profile not to drift), keep "New profiles" to its four-step list
under one sentence saying it is for contributors, cut line 117 to one
sentence, and drop the capability and forbidden-key lists to their counts
with one example each. Spend the words on P1, P5, P6, and P9.

**R2 (should). The guard-pattern paragraph (line 258) matters little.**
The reader never builds an EAN-13 by hand. Example 12.4 earns its place
because a check digit is what refuses a mistyped ISBN. The `"101"` and
L/G parity paragraph does not. Fix: one sentence (the bars come from a
fixed 95-module pattern), or cut.

**R3 (should). Line 162 is a table set as prose.** Seven figures for three
shops' hardcover margins, hinges, flaps, and strips in one paragraph.
Fix: move them into Table 12.3 (it already has a row per shop) and keep
the paragraph to what an UNCONFIRMED figure means for the author: proof
before trusting it.

**R4 (should). Three points are made more than once.** The tip at line
189 restates the paragraph at line 186. The seller-of-record caution
appears at line 347 and again at line 490. "Set `print.provider` to
`lulu`" appears at lines 168, 171, 428, and 465. Fix: keep the tip and
cut the last sentence of line 186, keep the seller caution at line 490
only (line 347 can end at the ledger fact), and let lines 428 and 465
point back to the tip in a clause.

**R5 (should). The closing paragraph carries roadmap jargon.** Line 501:
"sits in the Icebox". The reader does not know the press's backlog
vocabulary, and the direct-ordering plan and the adapter footnote are
for contributors. Fix: say the press has no checkout and will not take
payment, drop "Icebox", and keep the adapter footnote only if it answers a
question the author would ask.

## 4. Opening and closing

The "In this chapter" box matches the eleven A-heads exactly. The close
(line 501) ends on a one-sentence forward pointer to Chapter 13, which
the anatomy allows.

**O1 (should). The orientation spends half its sentences on the cast.**
Line 19: four sentences, which is in range, but the last two name
`hatter`, `printshop`, and `wonderland-press`, and the last two never
appear again in the chapter. Nothing says why the author is here: that a
shop rejects files built to the wrong numbers and that the press checks
both files before money is spent. Fix: replace the cast sentence with
that why. One clause naming user `alice` is enough.

## 5. Numbered items

Every table (12.1 to 12.10), every example (12.1 to 12.7), and every
figure is referred to in prose before it appears. Each earns its place.

**N1 (should). Figure 12.1 sits a section early.** It appears at line
113, in "Providers and their numbers", and its formulas (`panel_w`,
`wrap_w`) are not explained until Example 12.3 and line 216, a hundred
lines later. Fix: move the figure and its art directive into "The
layout", after Example 12.3, where line 216 already works its numbers.
Leave a forward reference at line 111 if the providers section needs it.

**N2 (should). Example 12.2's column key comes after it.** The headings
`Ing-c`, `Lulu-HC`, `KDP-w` are decoded at line 147. Fix: move the key
sentence into the lead-in at line 136, or spell the headings out.

**N3 (should). The KDP-date footnote is attached to the wrong sentence.**
`[^kdpdate]` hangs on the `--report-only` sentence (line 420), but it
dates the provider numbers. Fix: attach it to Table 12.3's lead-in or
to the KDP row discussion.

Note for the copy desk, not counted: Table 12.7's Meaning cells are
fragments, against the brief's "sentences in its Meaning column". The
caption says "verbatim" and the fact file gives them verbatim, so I
accept them.

## 6. Length

`press wordcount`: 6,528 words of prose against a 6,000 target, 8.8
percent over, within the 15 percent allowance. The cuts in R1 to R5 free
roughly 500 words, which should pay for P1, P5, P6, and P9 without moving
the count.

## The one change

Write the wrap from the author's side. Move Figure 12.1 to "The layout",
define bleed, trim, safety, and allowance there, explain the two deltas,
and say what *assets/cover.jpg* fills on the wrap. Pay for it with the
contributor internals in R1. At present the reader can compute a spine to
four decimal places and still cannot prepare a cover that fits it.
