# Typesetter report: Chapter 3, The shape of a book repository

Status: `press check` passed for this file (it reported only
`02-installing-press.md`: paragraphs 40, 104, 118 over 190 words; not mine).
`press pdf` completed (rc 0) with white 1362x800 placeholders for the 12
missing figure files; chapter 3 is PDF pages 41-61. Placeholders I created
were deleted afterward.

Counts: 7 blocks, 7 should.

## Measure finding that governs the code lines

In the PDF a code line holds about 64 characters before it passes the text
block (the grey tip boxes end there). The page is 432 pt wide and a
monospace character is about 5.1 pt, so a line of 65 to 72 characters hangs
into the right margin, and a line of 73 or more runs off the page edge and
is cut. Long lines that contain a hyphen or a space wrap, but the wrap
point is the first break after the overrun, and the first segment is still
cut. No wrap hook is drawn. "At most 72 characters" in the markup guide is
therefore too generous; every code line over 64 is a risk, and over 72 is a
certain loss. The fixes below get every line to 64 or under where I could.

## Blocks

1. Quote: Example 3.4 line `verify-sentinels has 0 entries; a release needs at least 2 distinctive prose fragments` (86 cols).
   Rule: 72-column code limit; PDF shows `...at least 2 distinctive pro` and loses the rest (page 40).
   Severity: blocks. Fix: re-set the refusal as the tool prints it but excerpt:
   `verify-sentinels has 0 entries; a release needs at least 2 ...` and
   `verify-min-pages is 1; a release needs at least 24`; shorten the first
   line (`this is a release build (PRESS_RELEASE=1) and its witnesses are vacuous:` is 72) to `this is a release build (PRESS_RELEASE=1); its witnesses are vacuous:` or elide with `...`. Add "we cut the long lines" to the sentence above.

2. Quote: Example 3.8 `.PHONY: all check pdf epub html markdown site txt docx pages source verify verify-formats render wordcount clean` (112) and the matching `all check ... clean:` rule line (105).
   Rule: 72 columns. PDF: the first wrapped segment runs off the page (`...source verif`), the hyphen of `verify-formats` is the break, so the reader sees `verify verify`. Not acceptable (page 56).
   Severity: blocks. Fix: a shorter verbatim excerpt:
   ```
   PRESS ?= python3 -m press

   .PHONY: all check pdf epub html ...
   all check pdf epub html ...:
   	$(PRESS) $@
   ```
   with a prose sentence "The real file lists all sixteen targets on both lines." Also the first comment line is 72; use `# Muscle-memory wrapper; the pipeline lives in the press package.` (64).

3. Quote: Example 3.9 `# Local builds. CI does not read this file; the press action installs itself` (76) and `# from its own checkout. For day-to-day work prefer an editable install of` (74).
   Rule: 72 columns; PDF cuts both (`installs its`, `install o`; page 56/57).
   Severity: blocks. Fix: show shorter lines, saying the comment is abridged:
   ```
   # Local builds. CI does not read this file.
   # For day-to-day work prefer an editable install of
   # your press clone: pip install -e ~/path/to/press
   press @ git+https://github.com/clintecker/press@v3
   ```
   (longest is 51). Prose "the comment above it" stays true.

4. Quote: Example 3.3, `# Press facts: artifact basename, canonical repo, and the public Pages URL` (74) and the other comment lines of 66 to 72 columns (the "Verification knobs", "print pack", and "Registrations" blocks).
   Rule: 72 columns; the 74-column line is cut (`Pages UR`), several others hang into the margin (page 37).
   Severity: blocks. Fix: shorter excerpt. End the example after `site-url: "https://wonderland-press.github.io/alice"` and then a line `...`; change the sentence above to "The real file continues with the verification knobs, the print comments, and the registrations block, which Chapter 12, *The print pack*, and Chapter 13, *Registrations*, cover." Then `verify-sentinels` and `verify-min-pages` are shown in Example 3.5 anyway. This also removes the page split in item S1.

5. Quote: Example 3.2 body, lines `this sentence and the one before it; keep the heading. This paragraph only` (74) and two 72-column neighbours.
   Rule: 72 columns; PDF cuts `only` to `onl` (page 35).
   Severity: blocks. Fix: you may not rewrap an "exact" reproduction without saying so. Cut it down: show `# Preface {.unnumbered}`, a blank line, then `Why this book exists, in your own voice, with no throat-clearing. Delete` (70, still hangs) is no better; use `...` after the heading and say "followed by one paragraph telling you to replace it", or rewrap at 64 and change the sentence to "reproduces it, wrapped for the page".

6. Quote: Example 3.10 `Checker self-test passed: 19 known-bad fixtures each tripped their declared rule, known-good fixture accepted, 2 extra diagnostics noted` (136) and `Jargon check passed: no rewrite-status terms (full audit in build/jargon-report.txt)` (84).
   Rule: 72 columns; PDF cuts the first (`declar`) and wraps the second after `jargon-` (page 48).
   Severity: blocks. Fix: end each line early with ` ...`: `Checker self-test passed: 19 known-bad fixtures ...` and `Jargon check passed: no rewrite-status terms ...`, and add to the lead-in "the last two lines are longer than a page, and we cut them".

7. Quote: Example 3.5 `    '["Twinkle, twinkle, little bat", "she made some tarts"]' --json` (68) and Example 3.1 `$ press new alice --author "Lewis Carroll" --owner wonderland-press` (67).
   Rule: 72 columns holds on paper, but the page measure is 64, so `--json` breaks as `--` / `json` (page 42) and `wonderland-press` breaks as `wonderland-` / `press` (page 32).
   Severity: blocks (the reader sees a broken option). Fix: put the option on its own continued line:
   `$ press new alice --author "Lewis Carroll" \` / `    --owner wonderland-press` and
   `    '["Twinkle, twinkle, little bat", "she made some tarts"]' \` / `    --json` (the first of those is 62).

## Should

S1. Quote: Example 3.3 (pages 37-38 in the book, PDF 46-47) and Example 3.12 (PDF 58-59) split across a page.
   Rule: a verbatim block should stay whole where it can.
   Severity: should. Fix: 3.3 is solved by item 4. For 3.12 nothing to do unless the layout changes after the figures arrive; recheck then.

S2. Quote: the sidebar "Why CI does not install press from git" starts at the foot of PDF page 56 with only its title line inside the box, and the body is on page 57.
   Rule: a blockquote box should not run over a page, and a title should not be stranded.
   Severity: should. Fix: nothing in the file stops it; if it survives the figure insertion, move the sidebar after the next paragraph or shorten the text above it by one paragraph. Recheck at the final build.

S3. Quote: `| --publisher | The imprint. ...` in Table 3.1 and `registrations.isbn.print` in Table 3.5 (the separator `|--------------|` and `|-----------------------------------|`).
   Rule: proportion the separator to steer widths.
   Severity: should. Fix: the first column breaks as `--` / `publisher` and `registra-` / `tions.isbn.print`; widen the first column's dashes (about 20 for Table 3.1; Table 3.5 needs 24 and a narrower Meaning).

S4. Quote: `| *.github/workflows/book.yml* |` and `| *.claude/workflows/* |` in Table 3.2.
   Rule: the same.
   Severity: should. Fix: break as `.github/work-` / `flows/book.yml` and `book/chapters/00-` / `preface.md`; widen the Path column separator by about a third.

S5. Quote: Example 3.11 `    git remote add origin https://github.com/wonderland-press/alice && \` (72) and Example 3.12's `uses:` line, and lines 65 to 72 in Examples 3.1 and 3.7.
   Rule: the 64-column page measure above.
   Severity: should. Fix: Example 3.11 move `&& \` to the start of the next continued line is not possible in shell; instead split `git remote add origin \` / `    https://github.com/wonderland-press/alice && \`.

S6. Quote: lines 343 and 344, `appendices = sorted((root() / "book" / "appendices").glob("[a-z]-*.md"))` (72) and its neighbour.
   Rule: the same; the wrap falls inside the character class (`[0-` / `9]*.md`, page 44).
   Severity: should. Fix: set them in two lines each with a hanging indent, `chapters = sorted(` / `    (root() / "book" / "chapters").glob("[0-9]*.md"))` and say "set for the page".

S7. Quote: Figures 3.1 and 3.3 briefs, tree archetypes. Figure 3.1 lists about 19 rows (alice/, 4 workflows plus parent, book.yml and its two parent directories, the book files, config and 3 children, and 3 files); Figure 3.3 lists about 16.
   Rule: a tree of more than about 14 rows is flagged as too tall for the 1740 px cap.
   Severity: should. Fix: drop the two path-parent rows in 3.1 (show `.github/workflows/book.yml` on one stub as written, which the brief half does) and the `.claude/workflows/` children (name them in prose, as Table 3.2 does) to land near 12 rows; for 3.3, fold `index.html`, `read/`, `downloads/`, `sitemap.xml` into one annotation or accept the tall panel with `place=plate` (the guide allows `place=plate` for a taller figure).

## Checked and clean

In this chapter box lists the nine A-heads exactly in order; tips and warnings are four and four (eight, the maximum) with one sidebar (177 words); every example is captioned `Example 3.N.` directly above an untagged fence, no language tags, no trailing whitespace, no non-ASCII; tables 3.1 to 3.6 have headers, proportioned separators, and `Table: Table 3.N.` captions after; figures: `art:` comment immediately before the image, paths `03-NN-slug`, `#fig:` ids, `.diagram`, `width=full-measure`, no placement, `fig-alt` differs from the caption, captions sentence case without a period, and each `@fig:` reference comes before its figure (art plus image lines 148, 165, 157 words); no plate lines in this chapter; footnote labels `epubdate`, `printf`, `wordcount` unique; index comment is last. Prose nit (not filed): "git" is lower case in the narrative ("what git gives the press"); the guide lists Git as a proper noun.
