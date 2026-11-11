# Developmental edit: Chapter 7, Building the editions

Desk: developmental editor. File: `book/chapters/07-building-the-editions.md`
(419 lines, read as the design's reader: an author who can use a shell and
does not know TeX). Line numbers refer to the file as read. Facts checked
against `docs/briefs/facts/facts-07.md`, including the managing editor's
supplement S1 to S3 (real captures), which the chapter does not yet use.

Status: DONE_WITH_CONCERNS. 0 block, 24 should.

## 1. Coverage

All ten A-heads from the brief are present, in order, in sentence case,
with prose between every pair of headings. Every core topic in the design
row is reached: every target and what runs (Table 7.1), the pandoc command
(Example 7.1), defaults templating, the filter chain in order (Figure 7.2,
Table 7.3), latexmk and why, the EPUB specifics, the chunked reader, the
Markdown and text editions, the registry graph (Figure 7.1, Tables 7.4 and
7.5), `press all` in sequence, timings and logs, and `render`, `wordcount`,
`clean`. Nothing blocks.

| A-head | Line | Does the section deliver? |
|---|---|---|
| Targets | 20 | Yes. Table 7.1 is the right map; one row misleads (P7). |
| What pandoc is told | 54 | Yes for mechanism. The reader never sees a real defaults file or a real echo line (C2, N2). |
| The filter chain | 113 | Yes, but half the section is TeX internals and contributor material (R1, R2, R8). |
| The PDF through latexmk | 149 | Yes. The six pre-steps and the reason for latexmk are clear; the sidebar repeats the body (R3). |
| The EPUB | 178 | Yes. The rights line is not tied to the reader's config (P8). |
| The single-file HTML and the reader site | 198 | Mostly. Two undefined steps (P6) and a scar told in Python (R5). |
| The portable editions | 221 | Yes for Markdown, text, Word, source. The sources companion is misfiled here (R6). |
| The registry and the order of work | 245 | Yes. The strongest section: the no-stale story with `alice` and the rebuild list are what an author needs. |
| What press all does, in order | 321 | Thin. The reader's main command gets a bare list, no output, and an undefined gate (C1, C2, P1, P3). |
| Rendering, counting, and cleaning | 353 | Yes for its three targets, but two of its four B-heads are off its promise (C1). |

**C1 (should). Two B-heads sit under the wrong A-head.** "Rendering,
counting, and cleaning" opens with "Before them comes the log that every
build prints" (355) and then carries "Reading the log" (357 to 363) and
"What the build leaves behind" (365 to 393). Neither is rendering,
counting, or cleaning. Both are what a reader wants right after "What press
all does, in order": what the run printed and what it left in *dist/*. Fix:
move both B-heads to the end of the `press all` section, after the
print-pack warning, so that section ends on the log and Example 7.2, and
"Rendering, counting, and cleaning" holds only its three targets. The
orientation's last sentence (18) then reads true as well.

**C2 (should). The chapter does not use the real captures it now has.**
The writer's report says "No captured `press all` or `+ pandoc` output
exists", and the chapter works around it: a session that shows `<root>` in
terminal output (69 to 73), a schematic defaults file in Figure 7.3, a
`press wordcount` run on a fresh `press new` book rather than Alice
(407 to 411), and a `press all` section with no output at all. The
supplement in facts-07 gives all three verbatim: S1 (the complete `press
all` run on Alice, echo lines included), S2 (`pdf.yaml` and its rendered
copy), S3 (`press wordcount` on Alice). Fix: (a) replace the session at 69
to 73 with the first `+ pandoc` line and the `pandoc took 26.7s` line from
S1; (b) add a numbered example of the S1 run, trimmed with `...`, in "What
press all does, in order", and walk the six steps against it (the `¶
check`, `¶ typeset`, `¶ verify` lines mark the phases); (c) add a short
numbered excerpt of the S2 rendered copy under "Templating the defaults";
(d) replace the wordcount session with S3. Settle the slug first (see the
note at the end).

## 2. Path

**P1 (should). The commerce gate is never defined, and Alice does not
print the line the chapter promises.** "The press runs the commerce gate"
(335) is the first and only description. A reader cannot tell what it
checks, whether their book has one, or why a release build cares. The
chapter then says the advisory run "says so in a line of its own" and
quotes the advisory line (339 to 343). On Alice, S1 shows a different
line: `commerce release gate: print ordering is not enabled; no commerce
release gate`. Fix: one or two sentences saying the gate concerns print
ordering and has nothing to check on a book without ordering enabled (as
Alice), with a pointer to the chapter that covers ordering; then show both
lines, the one Alice prints and the advisory one an ordering-enabled book
prints. If the controller has no fact for what the gate checks, say only
what S1 and facts 5.3 state.

**P2 (should). "Copy the command from the log and run it yourself" fails
for the EPUB.** Line 75 promises that the echoed command can be pasted.
S1 shows the EPUB echo with the rights value unquoted (`--metadata
rights=The text and illustrations are in the public domain. Published
by ...`). Pasted into a shell, that splits into many arguments. Fix: keep
the advice, and add that the echo does not quote values with spaces, so a
pasted EPUB command needs quotes around the rights value.

**P3 (should). Step 2 of `press all` does not say what it builds.**
"**Every edition.** The press builds each edition target in turn" (331).
The reader has just read about seven targets and cannot tell which of them
`press all` runs or in what order. S1 shows the order: pdf, epub, html,
markdown, txt, docx, site. Fix: name them in that order.

**P4 (should). Paths into the press repository are given as if the reader
had it.** *src/press/data/defaults/* (79), *src/press/registry.py* and
*docs/REFERENCE.md* (247), and *.celebrimbor/baselines/lua-coverage.yaml*
(146) are paths in the press source tree. The design's reader installed
press with pip and has none of them. Fix: say once that these live in the
press repository (and that the reference tables are on the press
documentation site), or name the installed package's data directory for
the defaults.

**P5 (should). "GitHub Release" and "the Pages site" arrive undefined.**
Table 7.5's destination column and line 268 use both as known terms. The
reader meets them properly in Chapter 14. Fix: one clause at 268 saying
what each is, and a pointer to Chapter 14.

**P6 (should). Two steps are named and never explained.** "A second pass
then labels the table cells" (30, 204) and "It adds the reader metadata"
(32, 212). The reader cannot tell what either does or whether it touches
their files. Fix: the controller supplies a one-line fact for each
(the writer's report says facts-07 has none); otherwise cut them to a
clause that does not promise more than it says.

**P7 (should). Table 7.1's `press all` row is wrong by position.**
"everything above except print and coverwrap" (40) includes `press
render`, which sits above it and which `press all` does not run. Fix:
"every published edition and the page bundle, then every verifier".

**P8 (should). The EPUB rights line is not tied to the reader's config.**
`<copyright>`, `<publisher>`, and `<place>` (183) are placeholders with no
source named. Fix: say which fields of *config/metadata.yaml* fill them
(cross-reference Chapter 3, *The shape of a book repository*) and show the
real value from S1.

**P9 (should). "cascade", "verse", and "tail" are used before the
pointer that explains them.** Table 7.3's `set-pieces.lua` row (122) uses
all three; the pointer to Chapter 4 comes after the table (131). Fix: put
the Chapter 4 pointer in the sentence that introduces the table (117).

**P10 (should). The rule for plus-sign lines is too broad.** Line 359
says a line that starts with a plus sign "is a command that the press is
about to run". S1 also shows `+ stitched 4 files -> dist/...md` and `+
assembled pages site -> dist/pages`, which are not commands. Line 361
then implies the pilcrow phase lines are something the desk reads, when
S1 shows them in the reader's own terminal. Fix: say that plus-sign lines
mark each step (a tool invocation or a press step), and that the `¶`
lines appear in every run, with the desk reading the same stream.

## 3. Proportion

The chapter runs long on TeX and press internals and short on the reader's
main command. "The filter chain" (113 to 147) is about 520 words of prose
and table, of which perhaps half is for a contributor; "What press all
does, in order" (321 to 351) is about 400, with no output.

**R1 (should). "What figure numbering emits" is written for a TeX user.**
`\caption*`, `\addcontentsline{lof2}`, `\PressListOfFigures`, `\mbox`
(135 to 137) and the float-package footnote (139) mean nothing to the
design's reader. Fix: say what the reader sees in each edition (the
number, the bold label, the List of Figures entry, no stray attributes in
the HTML) and keep the "Fig-ure" story in one sentence. Drop the footnote.

**R2 (should). "Tests for the filters" and its warning are contributor
material.** Lines 141 to 147 address someone who works on the press
itself, which is Chapter 16's reader. The warning is an order to that
reader. Fix: reduce to one sentence that the filters have their own tests
in CI, with the pointer to Chapter 16, and drop the warning.

**R3 (should). The sidebar repeats the paragraph before it.** Line 162
explains that latexmk reruns LuaLaTeX until the lists converge; the
sidebar (165 to 167) opens by telling the same thing as history. Fix: let
162 carry the mechanism in two sentences and the sidebar carry what is
new (the simple build that failed, and the `toc-depth` trap), or the
reverse. Not both.

**R4 (should). Two tips restate their paragraphs.** The font-scan tip
(172 to 174) repeats 170 and ends on a quip ("a very convincing imitation
of one"); the source-zip tip (237 to 239) repeats 235. Fix: each tip
should carry only the action (run `press pdf` once on a new machine
ahead of need; commit before you build the source zip) and nothing the
paragraph already said.

**R5 (should). The chunked-writer scar is told in Python.** Line 217 ends
on `dirs_exist_ok=True`. An author gains nothing from the argument name.
Fix: one or two sentences: pandoc copies referenced media itself, and the
press now writes into directories that already exist.

**R6 (should). The sources companion is described twice, once in the
wrong place.** "The sources companion" B-head (241 to 243) sits under
"The portable editions", which it is not, and "Generated inputs" (313 to
319) explains it again. Fix: cut the B-head and let "Generated inputs"
carry it, with the Chapter 10 pointer moved there.

**R7 (should). Line 266 reads Table 7.4 aloud.** The graph is drawn
(Figure 7.1), tabled (Table 7.4), and then counted in prose ("Eight
artifacts need nothing first..."). Fix: keep one sentence that names what
to notice (pages waits on nine artifacts, the print branch stands apart)
and cut the rest.

**R8 (should). Table 7.3's `press-util.lua` row carries internal numbers.**
"the measure tables, the guard sizes, the cascade step of 2.4em, and the
tail amplitude of 3.0em with its size ramp" (127) is not something the
reader can use or see. Fix: "shared helpers the other filters use".

**R9 (should). Two sentences are about the press's documentation rather
than the reader's build.** "The press documents no other timing, and the
first LuaLaTeX run ... is the one slow step that its documentation
describes" (359) and the footnote quoting the scar list (401). Fix: cut
the first; cut the footnote or turn it into a plain fact the reader can
act on.

**R10 (should). The environment table does not say why the reader cares.**
Table 7.2 tells the reader that `BOOK_PUBLISHER` is read "through
`\directlua`" (105), which is TeX, and never says what the reader can do
with any of the three variables. Fix: drop `\directlua`, and add one
sentence after the table on the one variable the reader may set
(`SOURCE_DATE_EPOCH`) and why. If the S2 excerpt (C2) goes in, point at
its `metadata:` block for the four values in 109.

## 4. Opening and closing

The "In this chapter" box (3 to 16) matches the ten A-heads exactly. The
orientation paragraph (18) has no heading above it, runs four sentences,
and says what the chapter covers and why the reader is here ("still only a
directory of Markdown files"). Once C1 moves the log and dist tree, its
last sentence remains accurate. The close (417) ends on the last technical
point about `press clean` and one forward pointer to Chapter 8. No
findings.

## 5. Numbered items

Every figure, table, and example is referred to in prose before it
appears: Table 7.1 (24), Example 7.1 (56), Figure 7.1 (49), Figure 7.2
(81), Table 7.3 (81, 117), Figure 7.3 (90), Table 7.2 (99), Table 7.4
(247), Table 7.5 (268, 270), Figure 7.4 (323), Example 7.2 (367). Each
earns its place, with the overlap noted in R7.

**N1 (should). Figure 7.4 and the list it illustrates use different
names.** The directive's states are "check", "formats", "source", "pages",
"verify", "commerce gate" (325); the list's steps are "check", "Every
edition", "The source zip", "The pages", "Every verifier", "The commerce
gate" (330 to 335). A reader matching the figure to the list has to
translate. Fix: one set of names in both. The figure's short labels are
better; the list items can open with them.

**N2 (should). Figure 7.3 draws a defaults file that does not exist.**
The directive (92) is schematic by the writer's own account, and its
optional line, `@book/assets/web/extra.css?optional`, is not in
`pdf.yaml`. S2 now gives the real template and rendered copy. Fix: redraw
from S2: (a) three or four real lines, including
`@book/tex/title-page.tex?optional`, which is the entry dropped in the
Alice render; (b) the same lines resolved, the title-page line gone, and
the added `lof: true` and `metadata:` block marked as added. That one
figure then shows the templating, step 2 of the PDF pre-steps (154), and
the injected metadata (109) together.

## 6. Length

`press wordcount`: 5,798 against a target of 6,000, 3.4 percent under,
inside the 15 percent band. That count includes table cells, captions, and
the four `art:` directives. Counted as prose alone (code, tables, table
captions, and comments removed), the chapter is about 4,640 words, 23
percent under. The design (section 5) says the target is for the prose;
the brief's "Done means" uses `press wordcount`. As on Chapters 3 and 4,
the controller should settle which measure governs. R1 to R10 take back
about 450 words; C2, P1, P3, P5, P6, P8, and the S1 walk-through add about
350 words of prose plus two examples. The chapter will land near its
present `press wordcount` with the space moved from internals to the
reader's own run.

## The one change that would most improve the chapter

Build "What press all does, in order" around the real S1 capture: a
numbered example of the Alice run, the six steps walked against its
phase lines, the commerce gate defined and its actual Alice line shown,
and the log and *dist/* B-heads moved in from the last section (C1, C2,
P1, P3). The reader's daily command is now the thinnest section; this
makes it the one they can check their own terminal against.

## Notes for other desks (not findings)

- Controller: S1 names the Alice outputs `alice-in-wonderland.pdf` and so
  on, while the design and this chapter use slug `alice`. The brief's
  rule ("change the slug to `alice`") applies to the `demo` captures; say
  whether it applies to S1 to S3 too, before C2 is done. A reader who
  builds the real example will see `alice-in-wonderland`.
- Fact desk: S1 shows the EPUB echo passing `--epub-metadata=` for
  *build/epub-metadata.xml*; line 186 could name the option if wanted.
- Fact desk: line 301 lists `press verify-formats` rebuilds correctly and
  stays silent on B.11 (it reads an existing PDF); keep it silent.
