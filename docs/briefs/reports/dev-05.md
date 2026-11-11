# Developmental edit: Chapter 5, Figures, plates, and illustrations

Desk: developmental editor. File: `book/chapters/05-figures-and-plates.md`
(353 lines, read as the design's reader: an author who can use a shell and
does not know TeX). Line numbers refer to the file as read. Sources read:
`docs/design.md` sections 2 and 5 (row 5), `docs/briefs/brief-05.md`,
`docs/style-guide.md` section 2, and, to test claims, `docs/briefs/facts/facts-05.md`
and the writer's `docs/briefs/reports/report-05.md`.

Status: DONE_WITH_CONCERNS. 0 block, 20 should.

The chapter is sound in structure and complete against the design row. Its
main weakness is altitude: about a tenth of the prose explains LaTeX
mechanism (macro names, packages, counters) to a reader the design says does
not know TeX, while several things that reader must do (type an ornament,
commission a wrapped plate, get enough pixels on Apple Silicon) are left
unshown.

## 1. Coverage

All ten A-heads from the brief are present, in order, in sentence case, with
prose between every pair of headings. Every core topic in the design row is
reached: image syntax, plates versus figures, kinds, numbering and `@id`
cross-references, both lists, every placement with its measure rules and its
fate in each edition, `outset`, `fig-alt` and `decorative`, the `art:`
directive, the height cap per profile, print-safe flattening, and formats
and resolution. No block.

| A-head | Line | Does the section deliver? |
|---|---|---|
| Two kinds of picture | 20 | Yes. Table 5.1 is clear apart from its first row (P1). The ornament is named but never shown (C2). |
| The image line and its four fields | 42 | Partly. Three of the four fields are usable; the credit line is named and then dropped (C1). The comment-position rule may teach a broken form (P2). |
| Numbered figures and cross-references | 81 | Yes. The raw-citation fault and the tip at 109 are exactly what a reviser needs. TeX detail at 100 (R1). |
| The two lists | 112 | Partly. The List of Plates condition is given; the List of Figures has none (C3). Two of four paragraphs are TeX history (R1). |
| Placement | 132 | Yes, with two reader traps: `margin` against `wrap-outer` (P7) and the placement `plate` against the kind `.plate` (P6). |
| Measures and the runaround | 182 | Yes. The choosing paragraph at 234 is the best in the chapter. Wrap plus directive is unresolved (P3). |
| What each edition does with a placement | 238 | Yes. The prose and Figure 5.3 disagree about text and DOCX (N2). |
| The height cap | 256 | Yes. Table 5.5 and the sidebar do the job; the sidebar strays at its end (R3). |
| Files, formats, and resolution | 290 | Mostly. The PPI arithmetic is good; it fails the arm64 reader (P5) and leans on Chapter 11 state (P4). |
| Print-safe images | 322 | Yes, once the reader knows what a print interior is and how to build one (P8). |

**C1 (should). The fourth field has no form.** Line 57: "A credit line, if
the picture needs one, is separate again." The heading promises four fields,
and the reader learns how to type three. A reader with a licensed photograph
now has nowhere to put the credit. Fix: the controller adds to facts-05 how
a credit line is typed (in the caption, an attribute, or nowhere press
knows); the writer then gives it one sentence. If press has no credit field,
the sentence must say that the author writes the credit into the caption or
the acknowledgements, and the heading's "four" must still hold.

**C2 (should). The ornament is described but never typed.** Line 40 says "a
figure that carries `decorative=true` is an *ornament*" before the reader has
seen an attribute block (the first is Example 5.2, line 91). No example
anywhere shows `decorative=true`. Fix: after Example 5.2, or in the
`fig-alt` paragraph at 73, show one short image line for a tailpiece with
`decorative=true`, and move the definition at 40 to point forward to it.
The controller should also confirm what an ornament does to the lists
(report-05 says the fact file is silent).

**C3 (should). The List of Figures has no rule of appearance.** Line 114
says the List of Plates "appears only when *assets/woodcuts/* holds files".
Line 292 then says this book keeps its numbered figures in that directory.
A reader with only numbered figures there cannot tell whether the book
prints an empty List of Plates, or when the List of Figures appears at all.
Fix: controller adds the List of Figures condition to facts-05 (and whether
the List of Plates counts files or plates); the writer states both in the
first paragraph of "The two lists".

Note, not counted: the design row says "what each edition does", and the
chapter leaves the Markdown edition out because facts-05 contradicts itself
(section 4.2 against bug B9). That is the right call until the controller
settles it.

## 2. Path

**P1 (should). Table 5.1 opens on a term the chapter has not met.** Line 30,
the first row of the first table: "The `press figures` report gives its kind
as `figure`, but the numbering treats it as an unnumbered plate." The report
is introduced at line 75. Fix: the row says only that a bare image is a
plate; the `press figures` quirk moves to the paragraph at 75.

**P2 (should). The chapter may teach a form that drops the figure.** Line
59: the comment "may sit on the next line or after one blank line". The
writer's report (concern 1) says the next-line form parses as one paragraph,
so pandoc makes no figure of it: no caption, no number, no List of Plates
entry. If that holds, a reader who follows line 59 loses the picture
silently. Fix: the controller confirms with a build (Chapter 4's plates use
the next-line form, so a build of this repository is the test). If
confirmed, line 59 teaches the blank-line form only and a warning names the
failure; if not, the line stands.

**P3 (should). A wrapped plate cannot be commissioned, and the chapter does
not say so.** Line 221: "type the image line, one blank line, and then the
paragraph that wraps, with nothing between them." Line 59 put the directive
in exactly that place. Example 5.4 is a plate with no directive, so `press
illustrate cheshire-cat` would refuse it (line 61, third case). The reader
is left with two rules that collide. Fix: one paragraph after Example 5.4
that says where the directive goes for a wrap, or, if it cannot go anywhere,
that a wrapped plate is commissioned with `--subject`. This rests on filter
behaviour the fact file does not state (report-05, concern 2); the
controller must confirm before the writer asserts it.

**P4 (should). Example 5.5 depends on Chapter 11's state.** Line 303 runs
`press illustrate white-rabbit` as if it works out of the box, and line 294
introduces `build/illustrations/white-rabbit.png` without saying that
`press illustrate` writes there. A reader who types Example 5.5 now stalls
on the image model's credentials. Fix: one sentence before the example
saying what `press illustrate` needs (pointer to Chapter 11, *The art
department*) and that it writes its delivery to *build/illustrations/*.

**P5 (should). The resolution advice fails the primary platform.** Line 312
says the arm64 toolchain image has no upscaler. Line 316 says a delivery is
a 1024-pixel square, and resampling is downward only. So on Apple Silicon a
delivery stays at 1024 pixels, about 162 PPI at the 6.3-inch cap. The tip
at 319 ("Run `press art enhance` on any plate that falls short") then does
not fix the shortfall it names. Fix: the paragraph at 316 says what a reader
without an upscaler gets, and that press also finds an upscaler installed on
the host (facts-05 section 8.7 lists the Upscayl path under
*/Applications/*); the tip must be true on arm64.

**P6 (should). "Plate" names both a kind and a placement.** Table 5.1 has
the class `.plate`; Table 5.2 has `place=plate`; line 148 says the placement
differs from `inline` only in refusing a measure. A reader will ask whether
a `.plate` needs `place=plate`, and why anyone would choose it. Fix: one or
two sentences at 148 that name the collision, say the kind does not need the
placement, and say when the placement is worth typing (or that `inline` with
no width does the same).

**P7 (should). `margin` and `wrap-outer` read as the same thing.** Table 5.2
says `margin` is "an outer-side wrap inside the text column"; line 162 says
the figure "simply sits at the outer edge of the column"; Figure 5.1 draws
pages 3 and 4 alike. The reader cannot choose between them. Fix: the
paragraph at 162 says what differs (default measure, guard, outset) or that
they set alike in the current house. Facts-05 does not say; the controller
supplies it.

**P8 (should). The print interior arrives unannounced.** Line 240 ("the
print interior follows the same rules") and line 324 ("The print interior
has one more reader than the PDF") use the term without saying what it is
or which command builds it; `press verify-print` appears only inside a
quotation at 335. Fix: at first use, one clause that says the print
interior is the PDF built for a print vendor, with a pointer to Chapter 12,
*The print pack*.

**P9 (should). Five terms are used before they are defined.** The *aesthetic*
and `plates.style` (71); "the tie" (100); the "cleared leaf" (143, Table 5.2);
the *profile* (200, defined only by the pointer to Chapter 9); "The filter"
(221, which filter?). Fix: a clause or a pointer at first use of each; cut
"the tie" with the TeX it explains (R1).

**P10 (should). The List of Plates is placed in every edition.** Line 242,
in a paragraph about the reflowable editions: "A plate gets no number
anywhere, and its entry goes into the List of Plates." The reader will look
for a List of Plates in the EPUB. Facts-05 places the lists in the PDF
only. Fix: say "in the PDF, its entry goes into the List of Plates", or
state what the other editions do if the controller has the fact.

## 3. Proportion

**R1 (should). TeX mechanism runs long for a reader who does not know TeX.**
The design reader cannot act on `\hyperref[fig:croquet-ground]{Figure~8.1}`
(100), `tocdepth` and the lof file (128), the caption package option (130),
`\captionof` (164), `\cleardoubleevenpage` (166), `\Needspace*` and
`\begin{wrapfigure}{i}` (204), `0.4\linewidth` (210), or `\pandocbounded`
(258). Together they are roughly 500 words of the chapter's 5,772. The
scars matter; their mechanism does not. Fix: each passage keeps what the
reader sees and can do (the lists converge because press runs enough passes;
a shallow contents setting does not empty the List of Plates; a list entry
lands on the top of the plate; a wrap moves to the next page when too few
lines remain; a wrap with no width takes four tenths of the line) and drops
the macro names, or moves them to a footnote for the Chapter 16 reader.
Chapter 16, *Inside the press*, is the home for the rest.

**R2 (should). A docs-against-code aside the reader does not need.** Line
186: "Some of the press documentation says that `full-bleed` and
`frontispiece` ignore a width. The checker in fact refuses..." The brief
says to follow the code or stay silent where they disagree. Fix: state the
rule (the checker refuses a measure on any placement that is not in-flow)
and drop the first sentence.

**R3 (should). The sidebar strays at its close.** Line 281: "The same history
produced a second rule for the hand-written title page: never stack a third
`titlepage` environment." It is off the chapter's subject and in TeX the
reader does not know. Fix: cut the sentence; the sidebar stays inside 120
to 180 words without it (about 120).

**R4 (should). Two bridge sentences do no work.** Line 274 ("the sidebar
tells the story") talks about the document. Line 288 ("The cap also explains
why the house cannot enlarge a small image") misattributes: the cap limits
height, and the refusal to scale up is the separate rule at 258. Fix: cut
274; make 288 state the rule that does explain it, or cut it and let the
next section open on its own.

The bullet balance is right: the chapter argues in prose throughout, and
its tables are the only lists.

## 4. Opening and closing

The "In this chapter" box (lines 3 to 16) matches the ten A-heads exactly.
The orientation paragraph (18) has no heading above it and runs four
sentences. The close (343) is a one-sentence forward pointer to Chapter 6
with its correct title. Both pass on form.

**O1 (should). The orientation says what, and barely why.** Line 18 opens
"press holds each kind to its own law" and then lists the chapter's route.
Nothing tells the reader what goes wrong without this chapter. Fix: replace
one route sentence with the why, from the chapter's own matter (a picture
press refuses at check time, a citation that prints as raw `@fig:`, or a
plate that lands on the wrong side when a chapter grows by one page).

## 5. Numbered items

Every table (5.1 to 5.6), example (5.1 to 5.5), and figure (5.1 to 5.3) is
cited in prose before it appears, in order: Table 5.1 at 26, Example 5.1 at
44, Example 5.2 at 83, Table 5.2 at 134, Figure 5.1 at 148, Example 5.3 at
166, Table 5.3 at 186, Figure 5.2 at 204, Table 5.4 at 210, Example 5.4 at
221, Figure 5.3 at 242, Table 5.5 at 262, Example 5.5 at 298, Table 5.6 at
324. The two unnumbered blocks (65, 118) are under six lines and not cited
again. Each item earns its place; Table 5.3 is the hinge Chapter 6 points
back to.

**N1 (should). Figure 5.2's alt text puts the guard in the wrong place.**
Line 206: "a bracket over the lines that must remain free above each
figure." The guard demands free lines from the top of the wrap down (line
210: "more free lines below its top"), and the art directive at 208 says
the bracket "spans the block and the lines beside it". Fix: the `fig-alt`
must say the bracket spans the figure and the lines beside it, matching the
directive.

**N2 (should). Figure 5.3 and the prose disagree on text and DOCX.** Line
242: "The number and the citation survive in every edition." The directive
at 246 gives the "text / DOCX" box only "in-flow figure", and the alt text
at 244 matches it. The reader will not know whether a DOCX shows "Figure
8.1". Fix: the controller confirms what the text and DOCX editions receive;
then either the prose limits its claim or the directive and alt text add
"Figure 8.1" to that box.

## 6. Length

`press wordcount`: 5,772 against a target of 6,000, 3.8 percent under, well
inside 15 percent. R1 to R4 cut about 600 words; C1, C2, P3 to P10 and O1
add about 450. The chapter should land near 5,600, still inside the band.

## The one change

Recast the TeX mechanism (R1) as what the reader sees and does, and spend
the words on the three things the reader cannot yet do: type an ornament
(C2), commission a wrapped plate (P3), and get a print-worthy plate on
Apple Silicon (P5).
