# Developmental edit: Chapter 10, Front matter, the index, and the table of authorities

Desk: developmental editor. File:
`book/chapters/10-front-matter-index-authorities.md` (429 lines). I read it
as the design's reader would: an author who can use a shell and does not
know TeX. Line numbers refer to the file as read.

Status: DONE_WITH_CONCERNS. 0 block, 13 should.

## 1. Coverage

All eight A-heads from the brief are present, in order, in sentence case,
with prose between every pair of headings. Every core topic in the design
row is reached: `front-matter.yaml` key by key, the stacked OR subtitle,
the `tex/title-page.tex` override, `index-terms.yaml` and the chapter-label
index, the zero-hit rule, `authorities.yaml` and the claim check, the
sources companion, and what is not generated. Both figures and the
suggested sidebar are present. No block.

| A-head | Line | Does the section deliver? |
|---|---|---|
| What press generates and what it does not | 18 | Yes. The first law gives the why, Table 10.1 the not-generated list. One wobble in the "three kinds of book part" count (C1). |
| The front-matter file, key by key | 35 | Yes. Example 10.1 and Table 10.2 are the chapter's best pair. The tip at line 121 contradicts line 126 (P1). |
| The title page and the stacked subtitle | 134 | Yes. Table 10.3 and the Alice subtitle make the splitter concrete. Opens on TeX the reader does not know (P3). |
| The copyright page | 176 | Mostly. Table 10.4 and the Alice walk-through deliver. The B-head at line 202 carries material that belongs to the whole front matter, and repeats Table 10.2 (R1). |
| Overriding the front matter | 210 | Partly. Table 10.5 and the order rule are clear. The override itself is described and never shown, and its warning is opaque to this reader (P3, P4). |
| The subject index | 247 | Yes. Strongest section: shape, matcher, zero-hit, locators, sidebar. One numbered example is unannounced (N1). |
| The table of authorities | 320 | Mostly. Table 10.7 is thorough. Example 10.6 depends on a ledger the reader never saw (P2). |
| The sources companion | 399 | Partly. The section describes the file and never shows one (C2). |

**C1 (should). The companion is counted as a book part, then placed
outside the book.** Line 22: "The press generates three kinds of book
part", the third being the table of authorities, which "publishes it as a
companion document beside the book". Line 401 then says the companion is
published "beside the book and never inside it". The reader who maps the
chapter from line 22 will look for the ledger inside the PDF. Fix: line 22
must say two parts are inside the book and the third is a separate
document, in the same breath as the count.

**C2 (should). The sources companion is never shown.** The A-head promises
the reader the artifact; lines 403 to 409 give its shape in a template
(`- "<claim>": <authority>. <url> <note>`) and then a prose description of
the Alice entry. The reader cannot see what *dist/alice-sources.md* looks
like. Fix: add a short example (heading, italic companion line, the "In the
preface" group, the one Alice entry) and refer to it before it appears.
The writer's report says the spacing for an entry without `url` is not in
the fact file; either give Example 10.5 a `url` so the rendered line needs
no guess, or get the empty-field rule from the fact checker.

## 2. Path

**P1 (should). The tip at line 121 contradicts line 126.** The tip says to
set copyright, publisher, and place "before you set any front-matter key"
because "a missing one stops the next build". Five lines later: "The
scaffold fills all five, so a new book passes." The reader, who scaffolded
with `press new`, cannot tell whether Example 10.2's first command is
required or cosmetic. Fix: the tip must say what case it guards (a book
whose metadata was hand-trimmed, or a book adopted from elsewhere), or go.
Example 10.2's metadata line should be framed as replacing the scaffold's
placeholder values.

**P2 (should). Example 10.6 cites a ledger entry the reader never saw.**
Line 359: "a third entry repeats the claim of the second", and the output
quotes entry 3's duplicate "drawn by John Tenniel". Example 10.5 has one
entry. The reader cannot check the second fault against anything. Fix:
either give Example 10.5 the second and third entries (it is the example
the refusal refers back to), or show the three-entry ledger in Example 10.6
above the session.

**P3 (should). TeX vocabulary the reader does not have.** Line 136 opens
the title-page section on "one redefinition of the LaTeX `\maketitle`
command"; line 230 warns "Do not stack a third `titlepage` environment"
and points at "the same scar as the image height cap", which the chapter
explains only at line 233 and Chapter 5 tells. The reader does not know
what an environment is, why "third", or what the scar was. Fix: line 136
must give the reader's fact (the generated pages always come out in one
fixed order) and drop the command name, or footnote it. The warning must
say in plain terms what the failure looks like (empty pages, a build that
never finishes) and move after line 233 so the cap comes first.

**P4 (should). The whole-cloth override is never shown.** Lines 227 and
237 tell the reader to write *tex/title-page.tex* (or
*tex/title-page-print.tex*) "in LaTeX yourself" and give no skeleton, no
statement of what the file must contain, and no pointer to where one is.
This reader cannot act on it. Fix: either a minimal example (a title, an
author, a page break) with a sentence on what the press expects of it, or
a sentence that says plainly the override is for a reader who writes
LaTeX, and points to the house template or appendix that shows one.

**P5 (should). The Alice `date` is used and never set.** Line 155 and line
196 quote the date "First edition, 2026" to derive "mmxxvi" and "first
edition". Example 10.2 sets six keys and not `date`, and no earlier example
in the chapter shows it. Fix: show the value where it is first used ("the
scaffold's `date` for Alice reads ..."), or add it to Example 10.2. Line
132 also says both pages read `date` without saying what they print when
it is absent; one clause fixes that.

**P6 (should). Two cross-reference titles do not match the design.** Line
170 cites "Chapter 3, *The shape of a book*"; the design's title is *The
shape of a book repository*. Line 233 cites "Chapter 5, *Figures and
plates*"; the title is *Figures, plates, and illustrations*. Fix both.

## 3. Proportion

**R1 (should). The front-matter pages are described twice.** Table 10.2
already gives each page's look (dedication "in italic on a page of its
own, low on the page"; epigraph "set large and in italic ... in a muted
colour"; acknowledgements "in a narrow column"). Line 204 restates all
three with dimensions, under a B-head inside "The copyright page" that is
not about the copyright page. Fix: keep the look in one place. Either move
the dimensions into Table 10.2 and cut line 204's restatement, or keep line
204 and shorten the table's Meaning cells to what the key holds. Lines 206
and 208 (template markers, the golden file) are about all generated pages
and sit better at the end of "The front-matter file" or the top of
"Overriding".

**R2 (should). Maintainer detail where the author needs little.** Line 208
(`INV-front-matter-golden`, byte-for-byte golden copy), line 206 (the
`%<<if name>>` markers), line 241 (`BOOK_PUBLISHER`), and line 200
(*build/print-assets/...*) are facts for Chapter 16's reader, not this
one. Line 157, the pre-3.0.0 history of the second rule, is a footnote's
worth of material spending a paragraph. Fix: reduce each to the one
consequence the author sees (an absent key leaves no blank page; the print
logo is flattened for you) and move the mechanism to a footnote or to
Chapter 16. Drop `INV-front-matter-golden` from the index comment if the
term leaves the chapter. The words saved should go to C2 and P4, which
are short on what matters most.

**R3 (should). Table 10.4 and Table 10.2 overlap on the copyright page.**
Six of Table 10.2's nine rows (`edition-note` through `motto`) are
copyright-page lines that Table 10.4 lists again in order. This is
tolerable because one is by key and one by position, but the Meaning cells
repeat ("The production note that names the type and the method, set in
italic" against "The `colophon-note`, in italic"). Fix: let Table 10.2's
rows for those six keys say only "copyright page; see Table 10.4" plus
what the value holds, so the reader reads each fact once.

No bullet sprawl: the chapter argues in prose and uses tables where the
material is a list. Admonitions (four tips, three warnings) are in range.

## 4. Opening and closing

The "In this chapter" box matches the eight A-heads exactly. The
orientation paragraph (line 16) is four sentences, says what and why, and
has no heading above it.

**O1 (should). The orientation overclaims.** Line 16 says press builds the
pages "before its first chapter and pages after its last" and then lists
the index and the ledger. The ledger's output is not a page after the last
chapter (see C1). Fix: name what is built after the last chapter (the
index) and that the ledger is checked and published separately.

The close (line 419) is a one-sentence forward pointer after the last
technical point, as the style guide asks. It passes.

## 5. Numbered items

Figures 10.1 (line 136) and 10.2 (line 276), Tables 10.1 to 10.7, and
Examples 10.1, 10.2, 10.3, 10.5, and 10.6 are each referred to in prose
before they appear, and each earns its place.

**N1 (should). Example 10.4 is never referred to by number.** Line 291
ends "The message names every such term at once:" and the example caption
follows. Fix: name Example 10.4 in that sentence.

## 6. Length

`press wordcount`: 5,095 against a target of 4,500, +13 percent, inside the
15 percent band. The design counts the target on prose only, with tables,
examples, and captions extra. Stripping code blocks (about 470 words),
table rows (about 920), captions, and art comments leaves about 3,900
words of prose including admonitions, sidebar, and footnotes, about 13
percent under the prose target. Both readings fall inside the band, at
opposite edges. The fixes for C2 and P4 add words where the chapter is
thin, and R1 and R2 remove about as many where it is long, so the net
change should be small.

## The one change

Show the reader the two things the chapter only describes: a minimal
*tex/title-page.tex* (P4) and the rendered *dist/alice-sources.md* (C2),
paying for them with the maintainer detail in R2.
