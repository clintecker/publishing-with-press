# Developmental edit: Chapter 1, Introduction

Desk: developmental editor. File: `book/chapters/01-introduction.md`
(295 lines, read as the design's reader: an author who can use a shell,
knows git at clone-commit-push, and does not know TeX or pandoc). Line
numbers refer to the file as read.

Status: DONE_WITH_CONCERNS. 0 block, 16 should.

The chapter is accurate, covers every A-head and every core topic, and the
close is right. Its weakness is the first two pages. A reader who has never
heard of press learns *what* it does by line 35, but the *why should I
care* is never said in the reader's terms, and the opening section spends
its early sentences on typography of the name, a profile detour, and a
footnote about the pilcrow. Fix O1 and O2 first.

## 1. Coverage

All eight A-heads from the brief are present, in order, sentence case, with
prose between every pair of headings. The "In this chapter" box matches them.

| A-head | Line | Does the section deliver? |
|---|---|---|
| What press is | 21 | Yes on what (lines 25, 31 to 35). Weak on why for this reader (O1, O2) and leaves the toolchain names undefined (P1). |
| Where it came from | 47 | Yes. Runs to repository trivia (R2). |
| The four laws | 63 | Yes, and well argued with a scar per law. Runs long on internals (R1). |
| What press is not | 111 | Yes. Clean and proportionate. |
| A ten-minute tour | 123 | Mostly. Every step from `press new` to `ls dist/` is here, but the tour never shows the verification the chapter has just argued for (P5), and Table 1.1 reads output the reader cannot see (P4). |
| The editions | 216 | Yes. One internal contradiction about `site/` (P7). |
| Versions and the pinned contract | 247 | Over-delivered. The design row asks for one paragraph; the section is 445 words with a table, five paragraphs, a footnote, and a tip (R3). |
| How to read this book | 273 | Yes. |

No core topic from the design row is missing. No block.

## 2. Path

**P1 (should). pandoc, LuaLaTeX, latexmk, Lua filters, and poppler are
used without saying what they are.** Line 33: "Building is the work of
pandoc. It reads the Markdown and passes the document through a chain of
Lua filters". Line 40 adds poppler. The design's reader "does not know TeX
or pandoc". Each name needs a clause the first time it appears: what the
program is and what it does for the book (pandoc converts Markdown to other
formats; LuaLaTeX is the TeX engine that typesets the PDF; latexmk reruns
it until the cross-references settle; a Lua filter is a small script pandoc
runs over the document; poppler is the PDF toolkit the verifiers read
pages with). One clause each, no more. This is also where the chapter
should say that the author never writes TeX (see O1).

**P2 (should). Line 45 uses three terms before the chapter defines them
and carries three topics.** "the jargon watchlist" (never defined),
"a set of fixtures that every check must reject" (defined at line 166 as
*known-bad fixture*), and "pins the image itself by digest" (explained at
line 261). The paragraph covers the toolchain image, CI pinning, and the
house. Split it: one paragraph on where the toolchain comes from (install
it or use the image), one on the house. Drop the CI-pinning sentence here
(line 261 already does it), and either define the watchlist in a clause or
leave it out of the list.

**P3 (should). *scar* is used before it is defined.** It appears in the
docstring quote at line 49 ("with the scars already paid for") and as a
noun at line 79 ("The tallest scar in press"), but the definition comes at
line 101. Define it at line 49, where the reader first meets the word, and
let line 101 refer back.

**P4 (should). Table 1.1 reads four lines the reader sees one of.** Lines
149 to 153 show only `Source checks passed: 1 ordered Markdown files` and
`...`. Line 155 then says "The full output has four summary lines ... and
Table 1.1 reads them". The full output exists only inside Figure 1.3's
art directive, 40 lines later. Show the full captured output (six lines,
from facts-01 section 3.4, slug changed) as a numbered example, refer to it
before it appears, and let Table 1.1 read it. Row 2's last sentence (the
em-dash and en-dash second complaints) then has something to point at;
otherwise cut it, since it is Chapter 6 detail.

**P5 (should, second priority). The tour never shows verification
passing.** The chapter's argument (lines 35, 85 to 87, the sidebar) is that
press proves each artifact by opening it. Example 1.2 then elides
everything `press all` prints and climaxes on `ls dist/`. The reader who
has just been told why verification matters never sees it happen. The fact
file's supplement S1 has the verbatim closing lines of a real `press all`
run. Show the run's last lines in Example 1.2 and add one sentence tying
them to the third law. Two controller decisions first: (a) the captured
line contains a non-ASCII arrow (`→`), so rule on whether it stays verbatim
in a code block or is elided; (b) if the writer is to show a verifier's own
pass line, capture it, because facts-01 has none. Do not let the writer
invent verifier output.

**P6 (should). "Publishing the book" assumes a workflow file the chapter
never showed.** Line 208 says the CI runner "builds the book inside the
toolchain image", but nothing tells the reader that the scaffold already
contains *.github/workflows/book.yml* (facts-03, line 35). Add one sentence
before the push saying the scaffold carries the workflow, so pushing is all
it takes. Also line 210: "the cure for that one is to run it again, because
the toolchain image is public" reads as a non sequitur. The reader cannot
see why public means retry works. Either give the reason the fact base
supports, or state the remedy without the "because".

**P7 (should). `site/` is an edition and then not.** Table 1.2 lists
`site/` as the Chapter edition. Line 233 then says "Two further artifacts
gather the editions for readers. *dist/site/* is the reader site itself".
The reader cannot tell whether `site/` is an edition or a container of
editions. Make line 233 about *dist/pages/* only, and say in Table 1.2's
Meaning cell what `site/` holds.

**P8 (should). Two smaller forward references in the tour.** Line 143
names "The Source edition" before Table 1.2 defines editions. Line 168
says an `art:` directive adds to the word count, but the reader has not
been told what an `art:` directive is (the term is Chapter 5's). Gloss the
first in a clause ("the source archive"), and cut the second sentence or
gloss it.

**P9 (should). `press pages` after `press all` looks like a missing step
reversed.** Line 194 tells the reader to run `press pages` to see the
landing page, but Example 1.2 already lists `pages` in *dist/*. By the
managing editor's ruling S2, `press all` builds it. Tell the reader to open
*dist/pages/index.html*, and mention `press pages` only as the command that
rebuilds it alone, or drop it.

## 3. Proportion

Section prose word counts (prose only, approximate): What press is 596,
Where it came from 382, The four laws 1,045, What press is not 318, A
ten-minute tour 722, The editions 401, Versions 445, How to read 400.

**R1 (should). The four laws is the longest section by a third and carries
internals the newcomer cannot use.** The laws themselves, each with its
scar, are the right material. Cut these: the `INV-graph-no-stale` invariant
name (line 87; "invariant" is undefined and the name means nothing yet);
the trust-tier paragraph and its footnote about the Lua title-tie test
(line 105 and footnote `vacuous`, line 291), which is Chapter 16's
material; and the grep-before-`&&` warning (line 107), which concerns a
commit chain the reader does not yet have and is listed for Chapter 6 in
the design row. About 220 words come back.

**R2 (should). "Where it came from" spends a third of its length on
repository trivia.** The commit hash and its footnote (line 49, footnote
`first-commit`), the commit count, the thirteen-tags footnote (line 289),
and the whole scaffold-neutrality paragraph (line 61) tell this reader
nothing they need. The paragraph on *Make Ready* (line 57) and the
ownership sentence (line 59) are the ones that matter, because they say a
real book went through this and the book is the author's. Keep those, cut
the rest, and land the section near 250 words.

**R3 (should). "Versions and the pinned contract" restates history and
borrows Chapter 14.** The design row asks for this topic "in one
paragraph". Table 1.3 repeats what lines 51 to 55 already said about v2.0.0
and v3.0.0. The `press migrate` paragraph (line 265) and the composite
action and hash-lock paragraph (line 267, footnote `pillow`) are Chapter
14's core content. Keep the floating and immutable tags and "Design is part
of the contract" (lines 261 and 263, tightened), keep the tip, and move or
cut the rest. Decide whether Table 1.3 earns its place once the history
section has given the dates; if it stays, cut the overlapping sentences at
line 55.

## 4. Opening and closing

**O1 (should, highest priority). The orientation says what but not why,
in the reader's terms.** Line 19 has five sentences, the permitted
maximum, and the fifth ("The sample book throughout is ...") is
housekeeping that How to read this book (line 281) repeats. The first four
build a print-shop analogy and land on "press is a program that does that
work for a book written in plain Markdown". What the reader never hears is
why that should matter to someone who has a manuscript and does not know
TeX: one directory of plain-text chapters goes in, every edition comes out
(print PDF, EPUB, Web, the rest), the author never writes TeX or a pandoc
command, and press refuses to call a file finished until it has opened it
and checked it. Replace the fifth sentence with that payoff, stated as the
reader's gain, in one sentence. Move the Alice note to the first sentence
of the tour or leave it to line 281.

**O2 (should). The first page of "What press is" opens on trivia and
detours before it delivers.** Line 23 opens on the lowercase name. Line 25
calls the README quote "the whole claim in its first paragraph" but quotes
only its second sentence; the README's first sentence, "A complete small
press: everything required to turn a directory of Markdown chapters into a
publishable book" (facts-01), is the plainest statement of what press is
that this reader will ever get, and it is cut. Line 27 then turns to six
design profiles and "a sealed interior geometry", a term the reader cannot
parse on page 2. The footnote `mark` (line 285, the pilcrow) is an aside on
the reader's second page. The section must reach "what it does" and "how
it works" before it reaches profiles: lead with the README's full claim,
move the lowercase note to a clause, reduce line 27 to a forward pointer
to Chapter 9 without the definition, and cut the pilcrow footnote or move
it to the colophon.

**O3 (should). A warning sits directly under a B-head.** Line 178 puts the
font-scan warning between "### Building everything" and its first
paragraph. Put a sentence of prose first, then the warning after the
`press all` paragraph, where the scan actually happens.

The close (line 283) is a one-sentence forward pointer to Chapter 2. That
is correct; do not change it.

## 5. Numbered items

Every numbered item is referred to before it appears: Figure 1.1 (line 35,
placed 38), Figure 1.2 (40, placed 43), Figure 1.3 (125, placed 197),
Example 1.1 (129), Table 1.1 (155), Example 1.2 (182), Table 1.2 (218),
Table 1.3 (249). Unnumbered sessions are all six lines or fewer and are not
referred to again.

**N1 (should). Figure 1.3 lands 70 lines after its reference, behind the
examples it duplicates.** By the time the filmstrip appears, the reader has
seen all three of its panels as Example 1.1, the check session, and
Example 1.2. Refer to it again at the point it appears (line 194) as the
summary of the tour so far, or place it at the end of "Checking the
manuscript". Table 1.3's place is covered under R3.

## 6. Length

`press wordcount` reports 5,353 for the file against a target of 5,000
(+7 percent, within 15). That count includes the three figure `art:`
directives and the frontispiece directive, roughly 400 words, so the prose
alone sits near 4,950. R1 to R3 return about 550 words; O1, P1, P4, P5,
and P6 cost about 200. The chapter will land near 4,600 words of prose,
still inside the band, with the space moved from history and internals to
the reader's first build.

## Notes for other desks (not findings)

- Fact desk: line 105 paraphrases the ROADMAP's trust sentence but drops
  "compositions" from its list (facts-01, line 72). Moot if R1 cuts it.
- Fact desk: `git tag` dates in the press repository show v1.0.0 to v1.0.3
  on 2026-07-17, the same day as the first commit, against the chapter's
  "all carry the date 2026-07-18, the day after the first commit" (line 51)
  and Table 1.3's start date. These may be lightweight-tag commit dates;
  settle which date the book states.

## The one change

Rewrite the orientation's last sentence and the opening of "What press is"
so the reader learns, in their own terms and before anything else, that a
directory of Markdown becomes every edition with no TeX to learn, and that
press opens each file to prove it (O1 with O2).
