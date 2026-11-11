# Continuity report: Chapter 5, *Figures, plates, and illustrations*

Desk: continuity editor. Chapter read as it stands after its desks, the
re-review (`rereview-05.md`), and the final small revision (386 lines).
Cross-checked against Chapters 1 to 4 (committed), the drafts that share
figure facts with it or point into it (6, 7, 8, 9, 10, 11, 12),
`docs/vocabulary.md`, `docs/design.md` sections 5 and 8, the production
ledger, and the press source for the height cap
(`src/press/data/tex/book-header.tex`, `src/press/data/profiles/*.yaml`).

Status: **PASS WITH FIXES.** One blocks in the chapter (the two Alices, in
two examples), four should in the chapter, five may. Outside the chapter:
one blocks (Ch. 12's citation of the title) and three should for the
Chapter 9, 11, and 12 passes. The chapter obeys the shared markup rules:
every fence `text`, no code line over 64 columns, image line then one blank
line then the `art:` comment in all three figures, footnote labels
prefixed `5-` and unique across the book. Its l.59 now states the
blank-line rule correctly (the conflict continuity-04 logged is closed).
Numbering is clean: Figures 5.1 to 5.3, Tables 5.1 to 5.6, Examples 5.1 to
5.6, no gap, no repeat, slugs `05-01` to `05-03`, every `@fig:` has its
figure and is cited at or before it. Every promise Chapters 4, 6, 7, 9,
10, and 11 make about Chapter 5 is kept.

## Findings in the chapter

### 1. The gallery example given chapters it does not have (blocks)

Quotes: l.184 "Example 5.3 shows how the Alice example might give Chapter
7, 'A Mad Tea-Party', a frontispiece." l.237 "Example 5.4 shows how the
Alice example might put the Cheshire Cat on the fore-edge of a page in
Chapter 6, 'Pig and Pepper'."

Rule: cast and shared fact. The bible's "press's gallery example" row:
`examples/alice-in-wonderland/` has three chapters (01 Down the
rabbit-hole, 02 The pool of tears, 03 A caucus-race and a long tale). It
has no Chapter 6 or 7. The book's sample `alice` is the whole novel
(ledger ruling "the two Alices").

Fix: l.184 "Example 5.3 shows how the sample book `alice` might give
Chapter 7, ..."; l.237 "Example 5.4 shows how the sample book might put
the Cheshire Cat ...". l.44 ("the first chapter of the Alice example") is
true of either book; change it to "the sample book" for consistency.

### 2. The two Alices merged, and a third name (should)

Quotes: l.18 "The examples use the Alice example, which user `alice`
keeps on the workstation `hatter`." l.40 "The `.chart` in Example 5.2
belongs to the Alice book." l.97 "a numbered chart that the Alice book
might put in its own fifth chapter".

Rule: cast (same as continuity-04, finding 2) and one name per thing.
The gallery example is not what `alice` keeps on `hatter`, and "the Alice
book" is a third name. No example in this chapter is a capture from the
gallery example, so all of them belong to the sample book.

Fix: l.18 "The examples use the sample book, *Alice's Adventures in
Wonderland*, which user `alice` keeps on the workstation `hatter`." l.40
"belongs to the sample book." l.97 "that the sample book might put in its
own fifth chapter".

### 3. *ornament* defined for a second thing (should)

Quote, l.81: "An *ornament* is an illustration that holds no information,
such as a tailpiece, a rule, or a small vignette". Also l.87, Table 5.3
l.212 "alt text on an ornament", index l.386.

Rule: one term per thing. `docs/vocabulary.md` reserves "ornament" for
the scene-break glyph (scene break row: "ornament (use for the glyph)"),
and Chapter 4 uses it so (Figure 4.2 "The three scene-break ornaments").
Chapter 5 makes it the name of a `decorative=true` image.

Fix: call the `decorative=true` image a *decoration* (l.81 "A
*decoration* is an illustration that holds no information ..."; l.87,
l.212, index), or have the vocabulary owner rule that "ornament" covers
both and add it to the vocabulary. The first is cheaper.

### 4. "runaround" used past its one trade-name mention (should)

Quotes: A-head l.11 and l.200 "Measures and the runaround"; l.218 (the
trade-name gloss, correct); l.250 "cannot carry an `art:` comment without
losing its runaround".

Rule: vocabulary, wrap row: "runaround (give once as the trade name)".
l.250 uses it as a second name for the wrap.

Fix: l.250 "without losing its wrap". The A-head may stay (it is the
section that gives the trade name), but "Measures and wraps" would be
cleaner; if it changes, change the In-this-chapter box and tell the
Preface.

### 5. The closing promise to Chapter 6 is only half kept (should)

Quote, l.374: "The next chapter, *Checking the manuscript*, describes the
checker that holds every image line to the rules in Table 5.3."

Rule: promises. Chapter 6 as drafted gives image lines two rows in Table
6.2 ("Orphan plates", "Figure placement"). It states no measure, outset,
absolute-length, or `decorative` plus `fig-alt` rule, and its message
table has no `plate never referenced by the manuscript:` entry.

Fix: either the Chapter 6 writer adds the Table 5.3 rules and the
orphan-plate message (preferred; logged for Ch. 6's pass), or l.374
promises less: "The next chapter, *Checking the manuscript*, describes the
checker, which applies the rules in Table 5.3 on every build."

### 6. *wrap* used without its definition (may)

The chapter defines placement, measure, outset, guard, and runaround in
italics but never italicizes *wrap*, the vocabulary's term for text
flowing beside a figure. Fix: l.155 or l.172, "A *wrap* is an
illustration with text running around it: `wrap-inner`, `wrap-outer`, and
`margin`."

### 7. Table 5.5 lists five of six profiles (may)

Quote, l.291: "Table 5.5 lists the cap in the profiles that the header
names." The caps live in the profile files (`figure-cap:` in
*src/press/data/profiles/*.yaml*, written to *build/profile-geometry.tex*);
the header holds only the 6.3in default. Chapter 9 (Figure 9.2 brief)
lists six profiles, including `house-6x9-color` at 6.3 in. Fix: "Table 5.5
lists the cap in each profile", add a `house-6x9-color` row (6.3 inches),
and consider the profile ids (`house-6x9`, `novella-5x8`, ...) Chapter 9
uses.

### 8. Two Figure 5.1s (may)

l.114: the Alice chart "is the first figure in that chapter, so press
numbers it Figure 5.1". This book's own Figure 5.1 is the placement
vocabulary (l.164). l.114 says "in that chapter", so it is correct, but a
reader skimming for "Figure 5.1" meets two. Fix (optional): add "in the
Alice book's fifth chapter" to the second sentence of l.114, with the
name corrected per finding 2.

### 9. "picture" as a second word for the general class (may)

A-head l.6/l.20 "Two kinds of picture"; l.22 "an *illustration* is any
picture". The vocabulary gives "illustration" for the general class and
lists "picture" under plate's forbidden words. Here "picture" is used
loosely, not for a plate; leave it or rename the A-head "Two kinds of
illustration".

### 10. Housekeeping for other files (may)

- `docs/vocabulary.md`, placement row, lists six placements and omits
  `margin`; the chapter (and the code) has seven.
- `docs/design.md` section 5 gives Figure 5.3 as "the two lists and where
  a figure appears in each"; the drawn figure is "where an image line goes
  in each rendered edition". Update design.md.
- The three PNGs (`05-01` to `05-03`) are 5 KB placeholders, untracked.

## Findings for other chapters' passes

### A. Chapter 12 cites Chapter 5 by the wrong title (blocks)

Quote (Ch. 12, print-safe section): "Chapter 5, *Figures and plates*,
describes the pass for the interior". The title is *Figures, plates, and
illustrations*. (Ch. 10's old citation of the same short title is gone:
Ch. 10 now cites the full title at l.211.)

### B. Chapter 9 defines *leaf* for a different thing (should)

Ch. 5 l.150: "A *leaf* is one sheet of the book, two pages back to back".
Ch. 9 (reader-site section): "*leaf*, the paper column that holds the text
on the reader site". One term, two definitions. Chapter 5 has the trade
sense and uses it (l.159, 160, 267). Fix in Ch. 9: "the paper column" or
"the reader's page", or gloss it as the reader site's own word for its
column, distinct from a printed leaf.

### C. Chapter 11 calls Example 5.1's plate "the figure" (should)

Ch. 11 l.220 "It looks for the figure whose image file stem equals the
name ... when no chapter declares the figure, when the figure is a data
kind"; l.238 "Confirm that the figure from Example 5.1 has an `art:`
directive". Example 5.1 has no class, so by Ch. 5 l.44 it is a plate, and
a figure is numbered. Fix: "the illustration" (l.220), "the plate from
Example 5.1" (l.238); l.48 "Declare each illustration".

### D. "every image" for the print-safe pass (may)

Ch. 11 l.316 ("does this for every image in the print interior") and Ch.
12 ("passes every image through a print-safe pass") are looser than Ch. 5
l.364: the pass copies only the logomark, the JPEG files at the top of
*assets/*, and *assets/woodcuts/*; an image elsewhere stops `press print`
with "file not found". Not a contradiction while every interior image
lives in *assets/woodcuts/*, but Ch. 12 should carry the limit.

## Cross-references and promises out of Chapter 5 (all checked)

| Line | Target | Status |
|---|---|---|
| 22 | "The two lists" later in this chapter | later (l.128); kept |
| 40 | "as the next section shows" (`decorative=true`) | l.81; kept |
| 67 | Ch. 11, *The art department*: the commission from directive to finished plate | title right; kept (Ch. 11 `press illustrate` section) |
| 216 | Ch. 9, *The house design*: the profiles | title right; kept (Ch. 9 Figure 9.2) |
| 220 | "Placement" earlier in this chapter | earlier (l.148); kept |
| 277, 319 | "Print-safe images" later in this chapter | later (l.351); kept |
| 321 | Ch. 11: the luminance key and intake's refusals | kept (flat-ground test, key) |
| 325 | Ch. 11: the image-model account and key | kept (`OPENAI_API_KEY`, `GEMINI_API_KEY` section) |
| 353 | Ch. 12, *The print pack*: the print interior in full | title right; kept in draft |
| 353 | "listed later in this section" | l.364; kept |
| 374 | Ch. 6, *Checking the manuscript*: the checker holds every image line to Table 5.3 | partly kept (finding 5) |
| 378 | footnote "For the Chapter 16 reader" (tocdepth) | Ch. 16 is a stub; Ch. 7 sidebar and Ch. 9 already explain it; open |
| 164, 220, 269 | Figures 5.1 to 5.3 | all present (l.166, 222, 271) |

l.122's "see Chapter 6, *Checking the manuscript*" and "the section
'Placement' later in this chapter" are examples of how to write a
reference, quoted, and both happen to be true.

## Promises into Chapter 5 (all checked)

Ch. 4 l.44 (covers the figure), l.97 (identifiers in full), l.433
(plates, numbered figures, placements): kept. Ch. 6 Table 6.2 (orphan
plates; placements): kept. Ch. 7 l.167 (placements and cross-references):
kept. Ch. 9 l.45 (the height cap): kept. Ch. 10 l.211 (the empty-pages
scar): kept. Ch. 11 l.220 (how to write the directive; Example 5.1
declares `white-rabbit`): kept. Ch. 11 l.316 (the print-safe pass): kept.
Ch. 12 (the pass for the interior): kept, title wrong (A).

## Shared facts checked against Chapters 4 and 11

Agree: the blank-line rule (Ch. 4 obeys it four times; Ch. 11 restates
only "the `art:` directive that follows the image line"); `place=plate`
with no measure (Ch. 4 Figure 4.1); `.diagram`/`.photo` for this book's
figures (Ch. 9 Figure 9.3 is `.photo`); `press illustrate` name = file
stem, style order (`--style`, `style=`, `plates.style`,
`wood-engraving`), three refusals, the #225 reason, the guardrail text
word for word, the 1024 square delivery to *build/illustrations/*; intake
`--as plate:<name>`, name pattern, single-ink alpha master with black
colour channels, no resolution check; `press art enhance` four steps,
scale 4, 2400-pixel edge, 16 grays for an engraving, oxipng or pngcrush,
upscaler search order, amd64-only upscale in the image; the portrait at
*assets/author.jpg*; the print-safe caps (1000 and 1900 pixels, JPEG
quality 88, *build/print-assets/*, *print-safe-images.lua*) with Ch. 12;
the Lulu 600 PPI story with Ch. 11; the height cap (6.3 in on the house
page) with Chs. 1, 8, 9, 10, and the per-profile values with Ch. 9's
Figure 9.2 brief; the two lists, latexmk, the tocdepth scar, and the
hypcap anchor with Chs. 7, 8, 9, 10.
