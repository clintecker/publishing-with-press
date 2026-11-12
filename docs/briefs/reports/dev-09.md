# Developmental edit: Chapter 9, The house design

Desk: developmental editor. File: `book/chapters/09-the-house-design.md`
(379 lines). I read it as the design's reader would: an author who can use a
shell and does not know TeX. Line numbers refer to the file as read.

Status: DONE_WITH_CONCERNS. 0 block, 15 should.

## 1. Coverage

All nine A-heads from the brief are present, in order and in sentence case,
with prose between every pair of headings. Every core topic in the design
row is reached: the 6 by 9 in numbers (fonts, sizes, leading, margins, drop
cap, running heads, figure cap), the six profiles, the reader site and
landing page, `aesthetic.yaml` palettes, typography and book colours,
`extra.css` and `reader.css`, and design as part of the contract. No block.

| A-head | Line | Does the section deliver? |
|---|---|---|
| The page in numbers | 19 | Mostly. Table 9.1 and Figure 9.1 deliver the numbers. It opens on TeX class options (P3) and then drifts into headings, lists, and captions, which are not "the page in numbers" (R2). |
| Type | 69 | Yes. Table 9.2 and the line-breaking rules are clear and explained by effect. The colour subsection has one weak table (N2) and a misfiled fallback-title paragraph (R2). |
| Running heads and folios | 121 | Yes, briefly. The reading PDF's sides are unclear (P5). |
| Six profiles | 133 | Partly. Table 9.4 is good, but the section never says how a book picks a profile (P1) and Figure 9.2 is thin (N3). |
| The reader site | 166 | Yes, and at length. Longest section in the chapter, much of it CSS measures the reader cannot act on (R1). |
| The landing page | 228 | Yes. Table 9.6 and the four parts. "How This Book Was Built" is named and never described in a clause; add one if the fact file allows, otherwise leave it. |
| The aesthetic file | 254 | Mostly. Table 9.7 and Example 9.1 work. The example appears to break the rule the section states (P7), and the reader is not told how to see the merge (P2). |
| Extra CSS and the reader sheet | 320 | Yes. The addition-versus-replacement advice at 339 is the most useful paragraph in the chapter. Example 9.2 conflicts with Chapter 5 (P8); the warning repeats the prose (R4). |
| Why a design change is a new major | 345 | Yes. The spine argument at 353 and the "a widow is legal TeX" point at 359 make the case well. Some restatement (R3). |

## 2. Path

**P1 (should). The chapter never names the key that chooses a profile.**
Line 135: "A book names one in its metadata, as Chapter 3, *The shape of a
book repository*, describes." Chapter 3, line 268, says the reverse: "Chapter
9 covers the profiles and chapter openings." Each chapter hands the reader to
the other, and the reader finishes "Six profiles" knowing the six names and
not how to choose one. Fix: in "Six profiles", name `print.profile`, show the
one command (`press config set print.profile novella-5x8`, as a `$` session
on the Alice example), and say in a sentence that the trim follows the
profile and is not set directly (Chapter 3 line 268 already states the
refusal message; point to it rather than repeat it). The tip at 163 then has
something to act on.

**P2 (should). The reader is never told how to see a design change.** The
chapter describes four things an author changes (profile, `aesthetic.yaml`,
`extra.css`, `reader.css`) and names no command that rebuilds the result or
shows it. Two specific gaps: (a) after the merge warning at 314, the obvious
next step is `press aesthetic` with no arguments, which prints the effective
merge (Chapter 11, line 63) and is the only check the author gets, since
*config/aesthetic.yaml* has no validator (Chapter 3, line 278; Chapter 11,
line 96); (b) line 168 says the reader site is built into *dist/site* and
line 234 links the Chapter edition to *read/index.html*, with no word that
`press pages` copies one into the other (Chapter 7, line 269). Fix: one
sentence at the end of "The aesthetic file" pointing to `press aesthetic`,
and one sentence in "The reader site" naming `press site` and `press pages`
and where to open the result. Cross-reference Chapters 7 and 11; do not
re-teach them.

**P3 (should). The first A-head opens on TeX for a reader who does not know
TeX.** Line 21: "a KOMA-Script book ... the class `scrbook` with the options
`oneside`, `openany`, and `headings=small`". The reader meets four unknown
terms before the first number. The same section continues with
`\PressFigureCap` and `[H]` (45), the `lof` and `.lof2` files (61), and the
raw `\addtocontents{lof}{...}` line (63). Fix: open the section on the page
itself (the trim, the block, Figure 9.1, Table 9.1). Move the class options
to "The print interior", where the sidebar needs them, and gloss one-sided
and two-sided there in plain words. At 61 and 63, keep what the reader sees
(two lists, and a shallow contents page that no longer empties the List of
plates) and drop the file suffixes and the macro line, or move them to a
footnote.

**P4 (should). "Craft law" is used before the book defines it.** Lines 98
and 158 lean on "a craft law" as though the reader knows the set. Chapter
11, line 98, is where the four laws are named. Fix: at 98, gloss in one
clause (a rule of the house that no configuration can change) and point
forward to Chapter 11.

**P5 (should). The running heads are explained by macro, and the reading
PDF's sides are left unclear.** Line 125 explains `\automark[section]{chapter}`
and "the left mark", which the reader does not need. Line 123 puts the title
in "the inner head", but the reading PDF is one-sided (line 21), and the
reader cannot tell which side "inner" is on a page with no binding. Fix: say
where the title and chapter title sit on a page of the reading PDF in
left/right terms, then say how the print interior differs (127 already does
this well). Cut the `\automark` sentence or reduce it to "the header takes
the chapter title from the chapter heading".

**P6 (should). The contents drawer is open in the prose and closed in the
figure.** Line 198: the drawer "opens with the current chapter expanded"
(facts 7.3: "a `<details>` contents drawer with the current chapter
expanded"). The fig-alt at 200 and the art directive at 202 both specify
"the contents drawer, closed". A reader comparing prose and screenshot will
not know which is the default. Fix: say plainly in the prose whether the
drawer starts closed and, once opened, shows the current chapter expanded;
then make the directive and the alt text agree with it.

**P7 (should). Example 9.1 seems to break the rule the section states.**
Line 314: a section "replaces the house section of the same name. Nothing
from the house section survives inside it", and Example 9.1 "writes out
every token of the light palette". But the example's `web-palette-dark`
lists five tokens, and its `typography.web-family` drops "Palatino Linotype"
from the house stack given at 188. The reader who has just learned the rule
will read both as mistakes. Fix: one sentence after the example saying why
five dark tokens are enough (they are the five the dark theme changes,
Table 9.5), and either restore the house font stack or say the Alice author
shortened it on purpose.

**P8 (should). Example 9.2 contradicts Chapter 5 without saying so.** The
writer's report notes that Chapter 5 says an alpha-master plate "reads on a
light page or a dark one". Line 328 then says the Alice plates, black ink on
transparency, sit on the dark `--paper-warm` mat, which implies they do not
read. Fix: one sentence that reconciles the two: what the reader actually
sees in the dark theme (dark ink on `#26231b`, dimmed to 87 percent, per
line 188) and why this author wants a light panel anyway. Check the
Chapter 5 sentence with the managing editor if the two cannot both stand.

## 3. Proportion

Approximate prose words per section, tables and code excluded: page in
numbers 660, type 650, running heads 250, six profiles 380, reader site 880,
landing page 240, aesthetic 430, extra CSS 340, new major 700.

**R1 (should). The reader site runs longest on what the reader can act on
least.** Lines 186 to 194 and 204 to 214 give the frame's 4-pixel outline,
the h1 `clamp` range, the 3.1 em drop cap on a 0.82 line, the fading
hairlines, the card layout below 34 rem, the access keys, the `rel`
links, and the JSON-LD types. An author who wants to restyle the site needs
instead to know what each token paints (N1), which is scattered across 186,
194 and 188. Fix: cut the decorative measures to what Example 9.2 and the
override sections rely on (the mat, the dark dimming, the leaf width), and
let the saved words go to P1 and to the token roles in Table 9.5. Keep
"Metadata in the head" and the `site-url` tip; those are actionable.

**R2 (should). "The page in numbers" and "Color and links" carry material
that belongs elsewhere.** "Headings and lists" (57 to 67) covers heading
spacing, the contents depth, the toc-depth scar, and captions: type and
furniture, not the page. The fallback title page (113) sits under "Color and
links" and is about front matter. Fix: move heading spacing and captions
under "Type" (or a "Headings and captions" B-head there), and either cut 113
or replace it with a one-line pointer to Chapter 10.

**R3 (should). The v3.0.0 example re-lists the line-breaking rules.** Line
357 enumerates microtype, `selnolig`, old-style figures, the six settings,
the runt rule, and the hyphenation minimums, which 90 to 94 gave in full
three sections earlier. Line 371 restates the floating and immutable tag
behaviour already given at 351. Fix: at 357 refer back to "the line-breaking
rules in the section 'Type'" in one clause and name only the item not given
there (the hung dialogue mark is given at 119, so nothing needs repeating).
At 371 keep only what is new: what the reader should expect from their own
pin, without redefining the tags.

**R4 (should). The warning at 342 repeats the paragraph at 326.** Both say
press does not append the Web measure to a replacement sheet and the book
must set the leaf width. The warning adds only the consequence (lines run
across the screen). "No longer" also implies a history the chapter never
gives. Fix: keep the consequence in the warning and cut the restatement from
326, or the reverse. Drop "no longer".

## 4. Opening and closing

The "In this chapter" box lists the nine A-heads exactly. The orientation
paragraph (17) is four sentences, says what the house is and why the reader
is here, and has no heading above it. The close (377) is a one-sentence
forward pointer to Chapter 10, after the last technical tip. No finding.

The sidebar (51 to 55) is war story 12 from the fact file and runs about
135 words, inside the 120 to 180 range. It is the most TeX-dense passage in
the chapter; P3's gloss of one-sided and two-sided pages, placed just
before it, is what makes it readable.

## 5. Numbered items

Every figure, table, and example is referred to in the prose before it
appears: Figure 9.1 (23), Tables 9.1 (23, 29), 9.2 (71), 9.3 (98), Figure
9.2 (137), Table 9.4 (143), Table 9.5 (170), Figure 9.3 (198), Table 9.6
(234), Table 9.7 (256), Examples 9.1 (273) and 9.2 (328).

**N1 (should). Table 9.5 gives values and no meaning.** Its columns are
Token, Light, Dark, and four of nine Dark cells read "(unchanged)". The
brief asks for sentences in a Meaning column, and this is the table an
author consults when writing a `web-palette`, where the question is what
each token paints. Fix: make the columns Token, Light and dark values, and
What it paints, with a sentence per row drawn from 186 to 194 (cloth: the
page background; paper: the leaf; paper-warm: the figure mat; foil: the
leaf border and hairlines; and so on). Include the three borrowed tokens
(`--link`, `--ornament`, `--hairline`) as rows, since a palette may name
them (271). Table 9.6 also lacks sentences, but as a label lookup it earns
its place as is.

**N2 (should). Two rows of Table 9.3 say nothing the name does not.**
`rulegray` "is the light gray that the house names for rules" and `accent`
"is the single accent color of the house". Example 9.1 changes `accent`, and
the reader cannot tell what in the PDF will turn red. Fix: say where each
appears on the page. If the fact file does not say, the row should state
that plainly (for example, that the house defines it for rules and the
reader will rarely see it) rather than restate the name.

**N3 (should). Figure 9.2 is mostly blank and repeats Table 9.4.** Of its 30
cells, seven are blank and one whole column (body size, 10pt in every row)
carries no comparison; trim and figure cap are already in Table 9.4 and the
prose. As briefed, it does not yet earn a figure. Fix (for the managing
editor, since the brief fixed the columns and the blank rule): either fill
text width by stated arithmetic (trim width minus inner and outer margins,
labelled as computed, as Table 9.1 already does with "about 4.54in"; the
writer's report gives 3.75, 4.14, 5.35, 3.17), or replace the body-size
column with leading, which is the value the prose at 156 says varies.

## 6. Length

`press wordcount`: 5,708 against a target of 5,000, 14.2 percent over and
inside the 15 percent band, near its upper edge. My own count of prose
alone, excluding tables, code, and directives, is about 4,540, also inside
the band. The fixes above should net to zero: R1, R3, and R4 free roughly
200 to 250 words, which P1, P2, P7, P8, and N1 need.

## The one change

Fix P1 and P2 together: in "Six profiles", show `print.profile` and the
`press config set` command on the Alice example, and close "The aesthetic
file" with `press aesthetic`. The chapter describes the house design
thoroughly but never shows the reader how to choose or check a design, and
the reader came to this chapter to do that.
