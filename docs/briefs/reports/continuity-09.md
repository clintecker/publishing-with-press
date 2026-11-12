# Continuity report: Chapter 9, *The house design*

Desk: continuity editor. Chapter read as it stands after its desks, its
re-review (`rereview-09.md`, APPROVED), and the final small revision (405
lines). Cross-checked against Chapters 1 to 4, 6, 7, 8 (committed), the
drafts of 5, 10, 11, 12 and Appendix B, `docs/vocabulary.md`,
`docs/design.md` section 5, and the press source for the two table cells
the re-review left to this pass (*src/press/data/web/reader.css*,
*src/press/data/tex/book-header.tex*, *tex/book.css*, *data/profiles/*).

Status: **PASS.** No blocks. Three shoulds in Chapter 9 (findings 1 to 3),
one should raised against Chapter 11 (finding 4), three mays (5 to 7).

The re-review's two open items are closed in the text: O1 (l.21, 137, 279
now say "the Alice book"; l.204 "the press's own three-chapter Alice
example"; l.206 and l.208 "the three-chapter example") and O2 (l.306 now
opens "In the light theme").

**Cross-references.** Every chapter title cited matches its file heading
and design.md section 5: Ch. 2 *Installing press* (l.78), Ch. 3 *The shape
of a book repository* (l.144), Ch. 4 *Writing the manuscript* (l.117),
Ch. 5 *Figures, plates, and illustrations* (l.45), Ch. 10 *Front matter,
the index, and the table of authorities* (l.113, 403), Ch. 11 *The art
department* (l.100), Ch. 12 *The print pack* (l.51), Ch. 14 *Continuous
integration and the release contract* (l.377). "The section 'Six profiles'
later in this chapter" (l.21) is later (l.133); "the section 'Type'
earlier in this chapter" (l.383) is earlier (l.61). Every promise out is
kept by its target: the packages (Ch. 2 l.195 to 210), the diff and the
trim refusal message (Ch. 3 l.269, 324), asking for a drop cap (Ch. 4
l.260 to 286), the height cap (Ch. 5 l.285), the generated front matter
(Ch. 10), the other craft laws (Ch. 11 l.102, four, in quotation), the art
direction (Ch. 11 l.61 to 92), the rest of the print interior (Ch. 12
l.151 to 165), why providers refuse a color interior (Ch. 12 l.78), the
spine arithmetic (Ch. 12 l.86 to 97), the release pin (Ch. 14 "Tags:
floating and immutable", l.64).

**Promises made to this chapter.** All kept: the six profiles compared
(Ch. 1 l.32; Figure 9.2, Table 9.4); profiles and chapter openings (Ch. 3
l.269; l.115 to 119, 133 to 144); the aesthetic file (Ch. 3 l.118, 360;
l.258 to 349); the running head and the folio (Ch. 4 l.44; l.121 to 127);
the profiles (Ch. 5 l.216); the profile and aesthetic files and the house
reader stylesheet (Ch. 7 l.202, 252; l.175 to 230, 258 to 320); the
typography and layout (Ch. 8 l.509); the keys that reach the build (Ch. 11
l.86; Table 9.7); the geometry of each profile (Ch. 12 l.55; Table 9.4);
the chapter opening on the page (App. B l.128; l.115 to 119); the aesthetic
keys (App. B l.249, 303 to 327).

**Conflict closed.** Shared fact "Running heads and folio" carried
continuity-04 finding 1 (Figure 4.1 against Chapter 9). Chapter 4 l.44 and
its art brief l.48 now give the opening page a folio and no running head,
and Chapter 9 l.123 ("The folio appears on plain pages too, so a chapter's
opening page carries its number") agrees. Closed.

**Numbering.** Figures 9.1 `09-01-page-geometry`, 9.2
`09-02-profiles-compared`, 9.3 `09-03-reader-site`: design.md order, no
gap, no repeat, slugs match, each `@fig:` cited before its figure (l.23,
146, 204), one blank line before each `art:` comment. Tables 9.1 to 9.7,
no gap, each cited before it appears. Examples 9.1 and 9.2, no gap. Two
uncaptioned fences (l.139, 359), not referred to by number. Every fence
`text`. Footnotes `9-libertine`, `9-hypcap`, `9-migrate`.

**Cast.** `alice` on `hatter` (l.137); "the Alice book" for her novel; the
press's own three-chapter Alice example for the Figure 9.3 capture,
labeled as such; the chapbook example (l.357) is the press's own. No other
sample names.

**Terms.** New to the bible: *folio* (l.123), *runt* (l.86), *craft law*
(l.100), *tokens* (l.179). Defined again consistently: *the house* (l.17),
*design profiles* (l.17), *aesthetic* (l.76), *floating tag* and
*immutable tag* (l.377). Redefined differently: *leaf* (finding 1).

## Findings

### 1. *Leaf* defined for a second thing (should)

Quote, l.152: "the width of its *leaf*, the paper column that holds the
text on the reader site". Also l.135 ("a leaf width for the Web"), Table
9.4's column head and title (l.154, 163), l.165, 183, 186, 191, 198, alt
text l.206, l.234, 357, 368.

Rule: a term already in the bible must not be redefined differently.
Chapter 5 l.150 defines *leaf* in the trade sense ("one sheet of the book,
two pages back to back") and uses it at l.159, 160, 182, 198, 267;
Chapter 10 uses the trade sense at l.31 ("half-title leaf") and l.420
("the title leaf"). This is the conflict continuity-05 finding B flagged
for this pass; it is still open.

Fix: in Chapter 9 call the reader-site element the *paper column* (or
"the column"), defined once at l.152, and write "column width" for "leaf
width" (l.135, 154, 163 "Margins and column widths by profile", 165, 368).
Press's own profile key is `web.measure`, and the vocabulary reserves
*measure* for the width class, so "measure" is not the alternative. The
landing page's "narrower leaf" (l.234) becomes "narrower column". If the
managing editor would rather keep *leaf*, the vocabulary needs a row that
separates the two senses, and Chapter 9 must say at l.152 that this is not
Chapter 5's printed leaf. "Single-leaf edition" is press's label and is
unaffected.

### 2. "Figure cap" and "height cap" for one thing (should)

Quotes: Table 9.1 row "Figure cap" (l.41); alt text l.25 "the 6.3 inch
figure cap"; art l.27 "figure cap 6.3in"; l.135 "a figure cap"; Figure
9.2 column "figure cap" (alt l.148, art l.150); l.165 "the tallest figure
cap"; tip l.172 "The figure cap and the text width". Chapter 9 ties the two
once at l.45 ("The last row is the height cap from Chapter 5").

Rule: one name per thing. Chapter 5 l.287 defines the *height cap*, and
the bible's term row, Chapters 1, 8 and the shared fact use it. Chapter 10
l.263 also writes "figure cap" (noted for its errata).

Fix: write "height cap" in the prose, Table 9.1, the tip, and Figure 9.2's
column head and brief; name the profile key once in constant width at
l.45: "The last row is the height cap from Chapter 5, ..., and each profile
sets its own value with the key `figure-cap`."

### 3. Figure 9.2's blank cells against Chapter 12 (should)

Quote, l.146: "A blank cell means that this book has no stated value for
it." Figure 9.2 (art l.150) leaves "intended use" blank for
`novella-5x8`, `digest-5.5x8.5`, and `mass-market-4.25x6.87`, and "text
width" blank for the four non-house profiles.

Against: Chapter 12 Table 12.2 (l.63 to 65) states those uses: "It suits a
short novel or a novella", "It suits trade-paperback genre fiction", "It
is a rack-sized genre paperback". The text widths follow from Chapter 9's
own Table 9.4 (trim less inner and outer margins): novella 3.75 in, digest
4.14 in, large print 5.35 in, mass market 3.17 in; the profile files'
comments give the last three as "~4.14in", "~5.35in", "~3.17in".

Rule: shared facts. The sentence at l.146 is a statement about the book,
and Chapter 12 makes it false. The coordinator's ruling on dev N3 kept the
blank cells; that ruling predates this check, so it goes back to the
managing editor.

Fix: fill the intended-use cells from Table 12.2 ("novella", "genre trade
paperback", "rack-size paperback") and, if the column stays, the four text
widths; or keep the blanks and reword l.146 to "A blank cell means that
the profile file states no value for it" and drop the text-width column.

### 4. Two different aesthetic files for the Alice book (should, for Chapter 11)

Quotes: Ch. 9 l.277 "Suppose `alice` wants a red cloth ... She writes the
file in Example 9.1", caption l.279 "An aesthetic file for the Alice
book" (`web-palette`, `web-palette-dark`, `book-colors`, `scene-break:
fairy-dust`). Ch. 11 l.71 "Example 11.1 shows a *config/aesthetic.yaml*
for the Alice book. It replaces the `plates:` section", caption l.73 "The
Alice book's config/aesthetic.yaml", holding only `plates:`.

Rule: shared facts (the sample book's state). The chapters follow the
order in which a book is made, so by Chapter 11 the Alice book's file
already holds Example 9.1's sections, and a caption that calls a
plates-only file "The Alice book's config/aesthetic.yaml" says otherwise.

Fix (Chapter 11's pass): "Example 11.1 shows the `plates:` section that
`alice` adds to the file from Chapter 9's Example 9.1", caption "The
plates section of the Alice book's config/aesthetic.yaml". Chapter 9
needs no change.

### 5. Table 9.5's `--hairline` and `--ornament` rows (may; re-review "Not counted")

Quotes: l.187 "`--hairline` | `var(--foil)` | It takes the foil color for
hairlines."; l.190 "`--ornament` | `var(--foil-deep)` | It colors the
ornate drop cap."

Source: *reader.css* l.232, in the dark-mode block, sets `--ornament:
var(--foil); --hairline: var(--foil-deep)`. The two swap in the dark
theme. The re-review's suggested fix ("`var(--foil)`, dark unchanged")
would therefore make the cell wrong; do not apply it.

The `--ornament` meaning is also narrow. The token colors the diamond rule
under every `h1` (l.64 to 70), the scene-break diamond and its two
hairlines (l.49 to 53), the asterism and the fairy dust (l.113 to 123),
the list markers (l.128), and the ornate drop cap (l.107). `--hairline`
draws link underlines (l.38) and the borders of the narrow-screen table
cards (l.275); the scene-break hairlines of Chapter 4 Table 4.4 and
Chapter 9 l.200 are drawn in `--ornament`, not `--hairline`.

Fix: `--hairline` "`var(--foil)`, dark `var(--foil-deep)`" / "It
underlines the links and borders the table cards." `--ornament`
"`var(--foil-deep)`, dark `var(--foil)`" / "It colors the ornaments: the
diamond rules, the scene breaks, the list markers, and the ornate drop
cap." This also makes l.179's convention hold for every row.

### 6. Table 9.3's `accent` row (may; re-review "Not counted")

Quote, l.108: "The header defines it as the house accent.
`book-colors.accent` overrides it."; l.277 "In the PDF it sets the accent
to the cloth red".

Source: *book-header.tex* l.65 defines `accent` and nothing in the house
TeX uses it, so Example 9.1's `accent: 7B2D26` (l.301) changes nothing a
reader sees in the PDF. The same value `#4b3e8a` colors the Single-leaf
edition's links through *book.css* (l.7, 24), which `book-colors` does not
reach, and Chapter 11 l.140 and Appendix B l.312 say the cover prompt
reads a separate `web-palette.accent` (fallback `#7a2325`). Chapter 9's
palette list (l.275) names twelve tokens and not `accent`, which agrees
with the reader sheet but leaves Chapter 11's key unmentioned.

Fix: l.108 "The header defines it but uses it nowhere at the time of this
writing. `book-colors.accent` overrides it."; at l.277 drop "sets the
accent to the cloth red" or say it is kept for consistency; optionally add
to l.275 Appendix B's sentence, "The cover prompts also read `paper` and
`accent` (Chapter 11)."

### 7. Chapter 5 names the profiles by short names (may, for Chapter 5)

Chapter 5 Table 5.5 (l.293 to 299) labels its rows `house`, `novella`,
`digest`, `large-print`, `mass-market`; Chapters 9 and 12 use the ids
(`house-6x9`, `novella-5x8`, ...). "house" as a row label also collides
with *the house*. The values agree with Chapter 9 (6.3, 5.6, 6.0, 7.2,
4.8; `house-6x9-color` 6.3, which Ch. 5 l.291 now correctly leaves out as
equal to the house cap). Fix in Chapter 5: use the profile ids.

## Bible entries

Added 30: 4 terms (*folio*, *runt*, *craft law*, *tokens*); 17 shared
facts (house page geometry, print interior class and margins, house type,
line-breaking rules, house PDF colors and links, the six profiles' values,
profile seals, reader sheet tokens, palette keys, the aesthetic merge, the
Alice book's aesthetic, the reader-site chapter page, reader-site
metadata, the other sheets, the landing page, *extra.css* and
*reader.css*, the design contract); 7 cross-reference rows; 1 numbering
row; 1 Preface entry. Updated: *leaf*, *height cap*, *design profile*,
*the house*, *floating tag*/*immutable tag* terms; shared facts "Running
heads and folio" (conflict closed), "Chapter-opening settings", "Image
height cap", "Number of design profiles", "The editions", "The reader site
build", "Print and opening defaults"; incoming promise rows from Chapters
1, 3, 4, 5, 7, 8.
