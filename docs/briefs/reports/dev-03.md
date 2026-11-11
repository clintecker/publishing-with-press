# Developmental edit: Chapter 3, The shape of a book repository

Desk: developmental editor. File: `book/chapters/03-the-shape-of-a-book.md`
(599 lines). I read it as the design's reader would: an author who can use
a shell and does not know TeX. Line numbers refer to the file as read.

Status: DONE_WITH_CONCERNS. 0 block, 15 should.

## 1. Coverage

All nine A-heads from the brief are present, in order, in sentence case,
with prose between every pair of headings.

| A-head | Line | Does the section deliver? |
|---|---|---|
| Scaffolding a book | 19 | Yes. Synopsis, flags, the six steps, slugs, and no `git init`. |
| The tree, file by file | 68 | Yes. Figure 3.1 and Table 3.2 cover every file. The book root rule is here too. |
| The metadata file | 133 | Mostly. The fields are all here. The design asks for defaults and Table 3.3 omits them (C1). |
| Reading and writing config from the shell | 274 | Partly. `set`, `unset`, `list`, and `validate` are covered. `get` is named and never shown (C2). |
| Chapters, appendixes, and how they sort | 338 | Yes. Discovery, lexical sort, letters, `00-`, and no parts. |
| Adding a chapter | 374 | Yes. |
| The Makefile and local builds | 416 | Makefile yes. "Local builds" stops before the build (P3). |
| What git has to do with it | 492 | Partly. It does not deliver the promise made at line 66 (C3). |
| Where things go: build and dist | 546 | Yes. |

Every core topic in the design row is reached: `press new` and its flags,
the tree, the metadata fields, `press config`, slugs, discovery and
sorting, `press add`, `00-` front parts, the Makefile, `.gitignore`,
`git init` and the source zip, and `build/` and `dist/`. Nothing blocks.

**C1 (should). Table 3.3 has no defaults.** The design row asks for
"`metadata.yaml` field by field with types and defaults". Table 3.4 states
defaults in its Meaning column, and Table 3.5 has a Default column. Table
3.3 (line 194) has neither. Give Table 3.3 a Default column, as Table 3.5
has, and state for each field either the model default or "none, required".
Facts-03 section 3.3 has the values.

**C2 (should). `press config get` never appears.** Line 279 names five
subcommands, and the section shows four. The reader who has just set a
title in Example 3.5 has no way shown to read it back. Add one `get` line to
Example 3.5, or a two-line session after it, that reads back a field
`alice` just set.

**C3 (should). The git section does not keep line 66's promise.** Line 66
says the later section "explains why you want one before your first full
build". Lines 507 to 510 explain that the Source zip holds only tracked
files. They never say what a full build does in a directory with no
repository at all. Facts-03 section 20, item A26, marks the whole claim as
inferred and asks that it be verified before a writer states it. Either
the controller supplies a captured `press all` (or `press source`) run in
an untracked directory, or the writer weakens line 66 to match what lines
507 to 510 actually establish. Do not let the writer guess the behavior.

## 2. Path

**P1 (should, highest priority). Example 3.5 breaks the next two things
the reader runs.** At line 293, `alice` sets two sentinels and
`verify-min-pages 24` on a book whose only manuscript is the preface stub.
The chapter's own Table 3.4 (line 224) says the verifiers must find each
sentinel "in the manuscript and in every artifact". Line 241 says the
template writes 1 "so that a new book with nothing but its preface stub
passes on the first day". After Example 3.5, neither sentinel exists in
the manuscript, and the PDF has nowhere near 24 pages. The `press check`
in Example 3.10 then runs "on a fresh scaffold", but the reader's
directory is no longer fresh: it now holds the knobs from Example 3.5.
Facts-03 section 3.4 lists `sentinel ... not found` among the common
first-run refusals. The reader who follows the chapter line by line meets
a refusal the chapter says will not happen. Remove the sentinel and
page-floor lines from Example 3.5 and keep only identity (title,
subtitle, description, paper). Then make the verification knobs paragraph
(lines 233 to 243) say when `alice` sets them: once the chapters hold the
two phrases and the book is long enough, before the first tag. A short
session there can carry the `--json` sentinel line, so the JSON rule at
line 299 keeps its example.

**P2 (should). The reader is never told to enter the book directory.**
Example 3.1 scaffolds `alice` from its parent directory. Line 114 then
says press refuses outside the book root. Example 3.5 runs `press config
set` with no `cd`, which fails from the parent directory as line 114 says
it must. The `cd alice` only arrives in Example 3.11, eight sections
later, when the reader has been inside the directory all along. Add the
`cd alice` to Example 3.1 or as one line just after it. Then remove it
from Example 3.11.

**P3 (should). The chapter never runs `press all`.** "The Makefile and
local builds" runs `press check` and `press wordcount` and stops. Figure
3.3 and the whole last section describe "dist/ after press all", and the
warning at line 570 tells the reader to run it. The chapter never shows
the run, never says it needs the toolchain from Chapter 2, and never
shows the `ls dist/` that the press quick start (facts-03 section 3.4)
ends on. The font-scan paragraph (line 490) shows the gap. It warns about
the first LuaLaTeX run, but no step in the section starts LuaLaTeX. Add
the full build to "A first local build" after Example 3.10, with
`press all` and an elided run. Point to Chapter 2 for the toolchain, keep
the font-scan paragraph next to that run, and point forward to Figure 3.3
for what lands in *dist/*. If the controller has no capture of `press all`
output, a session of `$ press all`, `...`, and `$ ls dist/` is enough.

**P4 (should). "The model" is used a dozen times and never defined for
this reader.** Line 135 says "The press reads it through a typed model".
After that the reader meets "the model insists on" (192), "The model needs
it" (196, 198, 201 to 203, 221), "the model refuses the metadata" (213),
"The model defaults to 40" (225), and "the same typed model" (282). An
author who does not program will not know what a typed model is, or why
it differs from the YAML file. Define it in one sentence at line 135: the
set of rules press holds for every field, with its kind of value, whether
the field is required, and its default, checked on every build. After that
the word can stay.

**P5 (should). Example 3.11 assumes a GitHub repository that the reader
never created.** `git remote add origin ...` and `git push -u origin main`
both need an empty `wonderland-press/alice` repository on GitHub, and the
push needs the local branch to be called `main`. The chapter states
neither. Add one sentence before the example: create the empty repository
on GitHub first. If the
controller can supply the fact, add a clause about the branch name too. If
it cannot, leave the branch name alone and do not invent a `git branch -M`
step.

**P6 (should). Example 3.7 hides the output the reader will see.** The
managing editor's capture (facts-03 S1) shows that `press add` prints
`created book/chapters/01-down-the-rabbit-hole.md` and so on, one line per
file. Example 3.7 prints nothing after each `press add`. The capture also
lists `book/chapters:` before `book/appendices:`, and the example reverses
them. A reader comparing their terminal with the page will think
something differs. Put a `created ...` line after each command, and order
the listing as the capture does. Example 3.7 adds three appendixes and
the capture has two, so the writer must build the third `created` line
from the pattern of the other two.

**P7 (should). Example 3.6 shows a state from Chapters 9 to 11.** Line
322 introduces it "for a book that has all six". At this point Alice has
three config files. The other three (aesthetic, index terms, authorities)
are files the reader has not met, apart from one bullet at line 124. A
reader who runs the command sees three lines and wonders what is
missing. The fix is either to say before the example that Alice shows
the first three lines today and the rest appear as Chapters 9 to 11 add
those files, or to cut the example to the three lines Alice prints.
Facts-03 only has the six-line capture, so the first fix is safer. One
more point for the fact desk: facts-03 section 17.3 says
*aesthetic.yaml* has no validator. Line 322's "checks every config file
the book has against its model" overstates this.

## 3. Proportion

The weight falls in the right places. The metadata section is the longest,
as it should be, and its tables carry the detail. Four places spend words
where the reader gains little.

**R1 (should). The build directory list (lines 579 to 587) is an
inventory.** It has nine bullets, and two of them only say that a file
"sits beside it" (*cover-fragment.html*, *verify-text.txt*). Line 577
promises that "when a build goes wrong, the evidence is here", and then
no bullet tells the reader which file to open for which failure. Turn the
list into a short paragraph or two that pairs each kind of failure with
its evidence: the defaults files when pandoc misbehaves, the generated TeX
when the front matter looks wrong, the jargon report after a jargon
failure, and the rendered pages for looking at the PDF. Drop the files
nobody will open in this chapter. The full list belongs in Appendix B or
Chapter 7.

**R2 (should). "Files you add later" (lines 124 to 129) is bullet
sprawl.** It has six bullets of filenames, several of them (*qualification.yaml*,
*title-page-print.tex*, *cover-styles.yaml*) for features this reader is
months away from. Line 131 then sends the reader to three chapters
anyway. Name the file groups once in prose (config extras, TeX overrides,
assets, art, known-bad fixtures), each tied to the chapter that covers
it, and let Figure 3.1 stay the picture of what exists today.

**R3 (should). The source code at lines 342 to 345 and its restatement
at line 347 say the same thing twice.** The reader does not read Python.
Line 347 restates both globs completely in English, which is what the
reader needs. Keep the prose. If the writer wants the patterns on the
page, show only the two glob strings (`[0-9]*.md`, `[a-z]-*.md`) inline in
line 347 and cut the Python block.

**R4 (should). The invariant paragraph (line 414) and its footnote repeat
each other.** The sentence "The target exists so that no author has to
build a chapter file by hand with shell redirection" and footnote
`[^printf]` ("It exists so that authors never `printf > file`") make the
same point. The ledger name `INV-add-no-clobber` is Chapter 16 material
that this reader cannot use yet. The warning at line 411 already tells
the reader everything they need. Cut the paragraph down to one sentence,
or cut it and keep the footnote. The same applies, more mildly, to
`INV-graph-no-stale` at line 573.

Not counted, for the prose desk: two paragraphs close on a turn of phrase
and not on their point. Line 188 ends "will notice them before you do",
and line 490 ends "although it is a convincing imitation".

## 4. Opening and closing

- The "In this chapter" box (lines 3 to 15) matches the nine A-heads
  exactly, in order and wording. Pass.
- The orientation paragraph (line 17) has four sentences and no heading
  above it, and says what the directory is and why the reader needs to
  know it. Pass.
- The close (line 591) is one forward pointer to Chapter 4, with no
  summary. Pass.

No findings.

## 5. Numbered items

Tables 3.1 to 3.6, Examples 3.1 to 3.12, and Figures 3.1 to 3.3 are each
referred to in the prose before they appear. The unnumbered code blocks
(lines 23, 278, 378, 482) are synopses or sessions under six lines, which
the brief allows. Example 3.6 earns its place only with the P7 fix. The
others earn theirs.

**N1 (should). Figure 3.2 does not match the prose it illustrates.** Line
357 names *10-the-lobster-quadrille.md* and *2-the-pool-of-tears.md*. The
`art:` directive at line 361 draws *1-down.md*, *10-lobster.md*, and
*2-pool.md*. The directive also draws the generated index as *a-index.md*,
and line 580 gives its real name, *a-index-of-subjects.md*. The reader
will look from the page to the figure and see different files. Make the
directive use the same filenames as the prose (shortening both is fine,
if they match), and the real index filename in frames (c) and (d).

## 6. Length

`press wordcount` gives 6,056 against a 6,000 target, inside the 5,100 to
6,900 window. That count includes table cells, captions, and the three
`art:` directives. Counted as prose alone (code, tables, captions, and
comments removed), the chapter is about 4,700 words, which is 21 percent
under. The design (section 5) and the brief both say the target is for
prose, with tables extra. The brief's "Done means" uses `press wordcount`,
which counts tables. The controller should settle which measure governs.
The P1, P3, and C3 fixes will add roughly 250 to 400 words of the kind
the chapter is short on, and R1 to R4 will take back about the same
amount.
