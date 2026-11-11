# Developmental edit: Chapter 4, Writing the manuscript

Desk: developmental editor. File: `book/chapters/04-writing-the-manuscript.md`
(431 lines, read as the design's reader: an author who can use a shell and
does not know TeX). Line numbers refer to the file as read.

Status: DONE_WITH_CONCERNS. 0 block, 19 should.

## 1. Coverage

All ten A-heads from the brief are present, in order, in sentence case, with
prose between every pair of headings. Every core topic in the design row is
reached: dialect and smart punctuation, headings and numbering, the glyph
law, footnotes, tables and captions, code blocks, epigraphs, scene breaks
and ornaments, chapter openings and drop caps, the set pieces, typographic
spacing, the 190-word paragraph, and the Alice example throughout.

| A-head | Line | Does the section deliver? |
|---|---|---|
| The dialect | 20 | Yes. Table 4.1 and the paragraph after it tie `+smart` and `number-sections` to the rules that follow. Figure 4.1 is misplaced here (N2). |
| Headings and chapters | 45 | Yes. The strongest section: discovery, `press add chapter`, unnumbered chapters, no parts, the title-case test with a worked example. |
| Characters you may and may not type | 97 | Yes for characters. The B-head "What the audit directories get" drifts off the heading's promise (R2). |
| Paragraphs, footnotes, and quotations | 159 | Yes. "Sentences that other files name" (204) is a good catch for a reviser. |
| Tables | 208 | Partly. The table caption is shown, but the reader cannot tell whether press numbers a table (C2). |
| Code | 227 | Partly. Fencing and the PDF face are here. Nothing on language tags, highlighting, or inline code (C3). |
| Chapter openings and drop caps | 246 | Yes, with a reader trap on `lines` (P4). |
| Scene breaks | 303 | Yes. |
| The set pieces | 330 | Yes, at more length than it earns (R1). |
| The fine work press does for you | 403 | Yes for the ties. The third paragraph is a recap (R4). |

**C1 (should). Figure 4.1 misdraws the Alice example's page and drops two
design callouts.** The design row asks the page-anatomy figure for "running
head, folio, drop cap, scene break, footnote". The brief's list replaced drop
cap and scene break with blockquote and figure, and the directive (line 42)
then draws the opening page of "Down the rabbit-hole" as "grey text lines"
under the title. The Alice example sets a three-line drop cap (line 248) and
fairy-dust scene breaks (line 317), so a true page of it shows both. Fix:
the directive's first paragraph must start with a three-line drop cap, and
the managing editor should decide whether the drop cap and a scene break
join the callouts (nine or ten) or the brief's eight stand. Either way the
drawing must not show the Alice opening without its drop cap.

**C2 (should). Table numbering is left unanswered.** Every table in the
chapter carries a hand-typed number in its caption line (`Table: Table 4.1.
The pandoc dialect press reads`, line 36), while Example 4.4 (line 220)
teaches `Table: What Alice swallows` with no number. A reader copying either
one cannot tell which is right, or whether press numbers tables the way it
numbers figures. Fix: one or two sentences after Example 4.4 that state
what press does with a `Table:` caption and, if it does not number tables,
that a book that wants numbers types them into the caption. If facts-04 is
silent (it is: section 4.1 says only "pipe tables"), the controller must
add the fact first.

**C3 (should). Code is missing the questions a technical author asks
first.** The section never says whether a fence may carry a language name
(` ```python `), whether any edition highlights it, or how inline code in
backticks behaves under the prose rules. The writer's report already flags
the inline-code gap. Fix: controller adds a fact block on info strings,
highlighting, and inline spans to facts-04; the writer then adds a short
paragraph and, if highlighting exists, a numbered example.

## 2. Path

**P1 (should). Line 22 points the reader at a directory they do not have.**
"The same settings appear in all six defaults files under
*src/press/data/defaults/*." That path is inside the press package. A reader
in the `alice` repository on `hatter` looks for it and finds nothing. Fix:
either say the files live inside the installed press package (and that
Chapter 7 covers them), or cut the sentence; the point that matters is the
next one, that every edition reads the same dialect.

**P2 (should). `+yaml_metadata_block` raises a question it does not
answer.** Table 4.1 says only "Pandoc accepts a block of YAML metadata."
The reader learned in Chapter 3 that the book's metadata lives in
*config/metadata.yaml*, and now wonders whether a chapter file should open
with a YAML block of its own. Fix: the Meaning cell (or one sentence after
the table) must say what that block is for in a press book, or that a
chapter needs none, from the fact base.

**P3 (should). `{.unlisted}` appears once and is never defined.** Line 279:
"It skips any heading marked `{.unnumbered}` or `{.unlisted}`". The reader
met `{.unnumbered}` at line 65 and has no idea what `{.unlisted}` does. Fix:
define it beside `{.unnumbered}` in "Unnumbered chapters", or drop it from
line 279.

**P4 (should). Table 4.3 offers a `lines` setting that line 281 contradicts.**
Table 4.3 says `lines` is "the number of text lines the initial spans", so a
reader sets `lines: 4`. Line 281 then says the PDF passes
`lines=3,depth=0,findent=2pt,nindent=0pt`, which facts-04 section 4.5
confirms is the fixed macro. A reader who changes `lines` and sees no change
in the PDF has been misled by one of the two. Fix: the writer and controller
establish whether `lines` reaches the PDF; the chapter must then either
qualify the table row or stop presenting `lines` as a working knob. Cut the
lettrine parameters in any case (see R5).

**P5 (should). "Jargon lint" and "watchlist" arrive undefined.** Line 185:
"The jargon lint skips blockquotes by default, so a quoted passage that uses
a word on the watchlist does not trip it." Neither term has appeared yet;
both belong to Chapter 6. Fix: a clause that says what the jargon lint is,
with a pointer to Chapter 6, or cut the sentence.

**P6 (should). The chapter epigraph has no attribution.** The example at
line 189 shows the quotation and nothing else. An author placing an
epigraph will want a source line under it and is not told how, while the
book epigraph two sentences earlier has `epigraph.attribution`. Fix: show
how a chapter epigraph carries its source (a last line inside the
blockquote, if the facts support it), or say plainly that press gives it
no attribution field.

**P7 (should). Line 40 promises coverage the chapter does not give.** "You
type the other six, and the rest of this chapter takes them in turn." The
sixth, callout 8 (a numbered figure with its caption), is Chapter 5's
subject. This chapter only cites a figure. Fix: say this chapter takes five
of them and Chapter 5 the figure.

**P8 (should). Example 4.2 prints in the PDF the very characters the
chapter says the PDF cannot set.** Line 99 says a character outside the
law "is outside the print-font set". Lines 118 to 129 then put the pound
sign, section sign, dashes, and curly quotes into the print interior inside
a code block. Either the code face has them, and the reader wonders why the
law exists, or the PDF shows missing glyphs. The brief also forbids any
character outside ASCII and accented Latin in the file. Fix: drop the glyph
column. The code point and the name carry the example.

**P9 (should). The cross-reference paragraph asks for an identifier
without showing one.** Line 92: "Give a figure an identifier and cite it as
`@fig:page-anatomy`". The reader sees only the rendered "Figure 4.1" and
never the `{#fig:page-anatomy}` attribute that makes it. Fix: one inline
code span showing the attribute on an image line, then the pointer to
Chapter 5 that is already there.

## 3. Proportion

Raw word counts per A-head (prose, tables, examples, and directives):
headings 991, set pieces 857, characters 783, paragraphs 713, fine work
648, dialect 608, chapter openings 596, scene breaks 456, tables 237, code
211.

**R1 (should). The set pieces outweigh tables and code together.** A
reader of a technical manual writes tables and code in every chapter and
the Mouse's Tale perhaps once. Fix: grow Tables and Code (C2, C3) and trim
the set pieces. Table 4.5 (line 339) restates the paragraph at 332 and the
three B-heads that follow it, so cut the table or fold its "suits" clause
into each B-head's first sentence. The tail's size ladder (line 381) can go
with R5.

**R2 (should). "What the audit directories get" (lines 153 to 157) is
Chapter 6 material.** It sits under a heading about characters, and its
second paragraph, on `banned-patterns`, is not about characters at all.
Fix: reduce both paragraphs to one sentence saying audit directories get a
lighter battery and Chapter 6 covers them and the book's own banned
patterns.

**R3 (should). Trailing whitespace in code is said three times.** Line
165, the tip at line 168 ("The checker refuses trailing whitespace even
inside code blocks"), and line 231. Fix: keep the rule at 165 and the
exception at 231. The tip gives the editor setting only.

**R4 (should). Line 411 is a recap.** "The same principle runs through this
whole chapter" then relists straight quotes, three periods, `* * *`, bare
headings, and figure numbering, all covered earlier. The brief forbids a
summary at the close, and this is one placed two paragraphs early. Line 409
also restates line 407 before it reaches its example. Fix: cut 411 (the
`figure-numbering.lua` fact belongs in Chapter 5) and let 409 end on "Dr.
Dodgson" and "p. 42".

**R5 (should). TeX internals the reader cannot use.** The design names a
reader who does not know TeX. Line 229 (`fvextra`, `breaklines`,
`breakanywhere`), line 281 (`\Needspace*{4\baselineskip}`, the lettrine
options, `\scshape`), line 328 (`\PressFairyDust`, 1.9em), line 366
(`\PressVerse`), and line 381 (`\normalsize` through `\tiny`) give macro
names where the reader needs the effect. Fix: keep each effect in plain
words (a drop cap never starts at the foot of a page; long code lines break
at the measure; the tail's type shrinks to a fraction of body size) and cut
the macro names unless a later chapter needs them.

**R6 (should). Line 401, last sentence, is history the reader never had.**
"A book that uses no set pieces renders byte for byte as it did before press
added them." Fix: cut it.

## 4. Opening and closing

The "In this chapter" box (lines 3 to 16) matches the ten A-heads exactly.
The orientation (line 18) is four sentences with no heading above it and
says what and why. The close is one forward-pointer sentence (line 423)
after the sidebar, which works as a bridge to Chapter 5. No finding here
beyond R4, the recap just before the sidebar.

## 5. Numbered items

Tables 4.1 to 4.5 and Examples 4.1 to 4.9 are each referred to in prose
before they appear. Unnumbered examples are all six lines or fewer and not
referred to again.

**N1 (should). The figures will print as 4.2 and 4.3 in the opposite order
from the brief, the design, the filenames, and the writer's report.**
`@fig:scene-break-ornaments` (line 320) appears before `@fig:set-pieces`
(line 337), because "Scene breaks" precedes "The set pieces" in the brief's
fixed A-head order. Numbering by chapter in order of appearance makes the
ornaments Figure 4.2 and the set pieces Figure 4.3, while the files are
*04-02-set-pieces.png* and *04-03-scene-break-ornaments.png*. The prose
cites by identifier, so nothing in the text breaks, but the illustrator's
file list and the List of Figures will disagree. Fix: the managing editor
renames the two files (and the design row) to match the chapter's order, or
confirms with `press figures` how the filter actually numbers them.

**N2 (should). Figure 4.1 sits in the wrong section.** The page-anatomy
figure (lines 40 to 43) is placed in "The dialect", which it has nothing to
do with. Its first callouts are the chapter title and a section heading.
Fix: move the paragraph at line 40 and the figure to the head of "Headings
and chapters", where the reader is about to learn those parts.

Table 4.5 is also weak on earning its place; see R1.

## 6. Length

`press wordcount`: 5,718 against a target of 6,000, 4.7 percent under,
inside the 15 percent band. The writer estimates about 4,450 words of
prose alone. If the design's "targets are for the prose" is read strictly,
that is 26 percent under. The words C2 and C3 ask for, net of the cuts in
R2 to R6, are where the difference should come from.

## The one change that would most improve the chapter

Rebalance toward the reader's daily work: make Tables and Code answer what
an author asks (whether tables are numbered, language tags and
highlighting, inline code), paid for by cutting the TeX macro names, the
set-piece duplication, and the recap at line 411.
