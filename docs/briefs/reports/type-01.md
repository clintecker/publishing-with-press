# Typesetter report: Chapter 1, Introduction

File: `book/chapters/01-introduction.md`. `press check`: source, self-test,
and jargon passes clean for this file; the editorial pass failed only on
`02-installing-press.md` (three paragraphs over 189 words; not this desk).
`press pdf`: passed (chapter occupies PDF pages 12 to 25; all twelve figure
files were present when built, no placeholders were created by this desk).

Counts: blocks 0, should 6 (five numbered findings and the index note).

Checked clean: In this chapter box matches the eight A-heads; tip, warning,
sidebar forms and counts (2 tips, 3 warnings, 1 sidebar of about 165 words);
example captions and fences (no language tags); every code line at most 72
characters, no trailing whitespace, no non-ASCII; table captions and
separators; figure `art:` comments directly before the image line, paths,
`#fig:` ids, `.diagram`, `width=full-measure`, `fig-alt` differing from the
caption, sentence-case captions, each figure referred to by `@fig:` first;
frontispiece plate line untouched; headings sentence case, never two in a
row; footnote labels unique and all used; index comment last. No heading at
a page foot, no blockquote box breaking across a page, no example caption
parted from its fence, no table over the measure, no wrapped code line.

## Findings

1. Quote: `Panel 2, each line exactly ... 72 columns` and `Three boxed terminal
   panels in a row ... 72 columns wide` (art brief for `#fig:ten-minute-tour`).
   Rule: a terminal panel's transcript must fit 72 columns; fig brief rules.
   Severity: should. Three 72-column panels side by side need about 216
   columns across a 4.5 in measure, so the lettering would print at roughly
   a third of the size of the code in Examples 1.1 and 1.2. Fix: change the
   archetype to a vertical filmstrip (three panels stacked, numbered 1 to 3
   at the left), each panel 72 columns wide, about 8 to 9 lines tall at most
   in all so the stack stays under the 1740 px cap.

2. Quote: `Chapter 14 follows that build step by step.` (line 211) and
   `Chapter 10 covers it.` (line 238). Rule: cross-reference form is
   `Chapter N, *Title*`. Severity: should. Fix: `Chapter 14, *Continuous
   integration and the release contract*, follows ...` and `Chapter 10,
   *<title>*, covers it`, using the title the chapter file carries.

3. Quote: `Appendix D covers the toolchain platform by platform, and Appendix E
   is the glossary.` (line 281). Rule: `see Appendix A, *Command reference*`
   form. Severity: should. Fix: add the italic titles, as Appendix A to C
   in the same paragraph have them.

4. Quote: row `| Chapter edition | \`site/\` and \`alice-site.zip\` |` and row
   `\`alice-source.zip\`` in Table 1.2. Rule: tables, "proportioned separator"
   steering widths. Severity: should. In the PDF the Artifact column is too
   narrow, so the filenames break at their hyphen (`alice-` / `site.zip`,
   `alice-` / `source.zip`), which reads as a different filename. Table 1.1
   also wraps `Source checks passed` and `Checker self-test passed` in its
   first column. Fix: lengthen the first-column dashes in Table 1.1 and the
   second-column dashes in Table 1.2 (for example Artifact to about 28
   dashes, Edition to 18, Meaning to 40).

5. Quote: `Another trim, a colour interior, or large print` (line 115).
   Rule: house spelling; the rest of the book and press itself use American
   forms (the press docs say "color interior"). Severity: should.
   Fix: `color interior`.

## Note outside the checker

Index candidates `dist directory` and `build directory` appear in prose only
as part of longer phrases or not at all (`dist directory` occurs only in a
`fig-alt`; `build directory` nowhere). The markup guide requires a term to
appear in prose somewhere in the book; if no later chapter uses them, drop
them from the index comment on line 295 or use the phrase once in prose
(for example "the build directory, *build/*"). Severity: should; cannot be
confirmed from this chapter alone.
