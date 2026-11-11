# Desk brief: typesetter

You check Chapter 1, `book/chapters/01-introduction.md`, against
`docs/markup.md`, which is the whole law of what may be typed, and you
prove it builds.

1. Run `~/code/.pwp-venv/bin/press check` from the repository root. A
   failure naming this file is a blocks finding with the message quoted. A
   failure naming another file is not yours; note it in one line.
2. Run `~/code/.pwp-venv/bin/press pdf` and open `dist/publishing-with-press.pdf`
   at this chapter (use `pdftotext -layout` or `press render` and read the
   page images under `build/rendered-book/` for this chapter's pages). The
   figures do not exist yet, so LaTeX will complain about missing files;
   if the build cannot complete, create a 1362 by 800 white PNG at each
   missing path under `assets/woodcuts/` for the duration of your check and
   delete them before you finish (they must not be committed). Look for: a
   heading at a page foot, a table wider than the measure, a code line
   wrapping with the hook, a blockquote box that runs over a page, an
   example caption separated from its fence.
3. Read the file against the markup guide, construct by construct:
   - the "In this chapter" box form, the tip, warning, and sidebar forms
     (blockquote inside the classed Div, bold lead, lengths);
   - example captions (`**Example C.N. Title**` directly above an untagged
     or `text` fence; no language tags anywhere);
   - code lines at most 72 characters; no trailing whitespace; prompts `$ `
     or `# `; `...` for elision;
   - tables: header row, proportioned separator, `Table: Table C.N. ...`
     caption after the table, sentences in the Meaning column;
   - figures: the `art:` comment immediately before the image line, path
     `assets/woodcuts/CC-NN-slug.png`, `#fig:slug`, a kind class, a
     measure, `fig-alt` that differs from the caption, caption in sentence
     case without a period, the figure referred to by `@fig:` earlier;
   - the plate lines untouched where the brief placed one;
   - headings: sentence case, no leading digit, never two in a row, no
     typed numbers; appendix headings hand-lettered and `{.unnumbered}`;
   - italics and constant width used as the guide assigns them;
   - footnote labels unique; the index comment present and last.
4. Check every figure brief against the figure rules: no wrap placement
   for a diagram; a terminal panel's transcript will fit 72 columns; a
   matrix or tree with more than about 14 rows is flagged as too tall for
   the 1740 px cap.

Report in `docs/briefs/reports/type-01.md`: quote, rule, severity
(blocks for anything that fails a build or a verifier or the markup guide's
"never"; should for the rest), fix.

Return: status, whether `press check` and `press pdf` passed, and the
counts.
