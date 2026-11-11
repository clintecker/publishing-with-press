# Typesetter report: Chapter 2, Installing press

`press check`: FAILED, and the failures naming this file are blocks findings
1 and 2 below. Failures naming Chapter 3 (paragraphs 21, 102, 131, 161 over
190 words) are not mine. `press pdf`: PASSED (exit 0, chapter on PDF pages
25 to 39) only after placeholder PNGs were made for the 12 figure files
missing book-wide; all 12 were deleted afterward.

Counts: 3 blocks, 8 should.

## Blocks

1. Quote: the `art:` comment for `#fig:tools-in-the-build` (line 115,
   "<!-- art: ARCHETYPE data-flow, top to bottom. ..."). Rule:
   `press check` paragraph limit; the style audit counts an `art:` comment as
   a paragraph and it has 264 words (limit 190). Message: "paragraph 40 has
   264 words (the law is under 190; split it)". Severity: blocks. Fix: cut the
   brief to under about 180 words (drop the repeated "monospace on its arrow"
   sentences), or insert a blank line inside the comment, as the doctor-report
   brief does.
2. Quote: the `art:` comment for `#fig:local-versus-container` (line 311,
   "<!-- art: ARCHETYPE topology. Three elements in a row ..."). Rule: same.
   Message: "paragraph 104 has 253 words". Severity: blocks. Fix: shorten under
   about 180 words, or split with a blank line.
3. Quote: the sidebar "The hang that isn't" (lines 347 to 358). Rule: same
   limit; the checker treats the whole blockquote Div as one paragraph (223
   words counted) while the markup guide allows a sidebar of 150 to 250 words.
   Message: "paragraph 118 has 223 words". Severity: blocks. Fix: trim the sidebar
   to about 170 counted words (still above the guide's 150 floor); report the
   guide/checker conflict to the markup owner (a sidebar over 190 cannot pass).

## Should

4. Quote: Tables 2.1 to 2.4, separator rows such as `|------|-----...-----|`
   (lines 24, 93, 123, 231). Rule: "make the separator row long and
   proportioned to steer the widths". Rendered result: the first column is
   far too narrow. Words break mid-word ("pan-doc", "lu-ala-tex", "pip in-stall
   -e ."), and in Table 2.3 `pdftoppm` runs into the next column (PDF p. 30).
   Severity: should (visually the worst defect in the chapter). Fix: give the
   first column about a third of the dashes, for example `|--------------|--------------------------|`
   for 2.1, 2.3, 2.4, and about 40/60 for 2.2 (its first column holds
   `pip install -e ~/src/press` from a book).
5. Quote: "$ press doctor" first output line inside the doctor `art:` comment
   (line 203, "press doctor"). Rule: figure brief "character for character"; the
   transcript repeats the command as the first output line after the prompt
   line. Severity: should. Fix: delete the bare "press doctor" line.
6. Quote: the doctor transcript lines for `epubcheck` (74 columns), `claude`
   (106) and the "not ready:" line (118). Rule: brief step 4, a terminal
   panel's transcript fits 72 columns. Severity: should. Fix: shorten the
   purposes on the page transcript (for example "present but cannot execute"
   with the operator text dropped) and break the "not ready" line at 72 by hand,
   or state the wrap in the brief per line; keep the prose in Table 2.3 as is.
7. Quote: `![The press doctor report on hatter](assets/woodcuts/02-01-doctor-report.png)`
   appears second, while `02-02-tools-in-the-build.png` appears first. Rule:
   path `CC-NN-slug.png` with NN as sequence. Severity: should. Fix: rename the
   tools figure `02-01-tools-in-the-build.png` and the doctor figure
   `02-02-doctor-report.png` (sequence 1, 2, 3 in reading order); the
   illustrator brief is unaffected.
8. Quote: "1. Ask press for its version: `$ press --version`" (lines 331 to 338,
   the numbered list in "The first run"). Rule: a session shows the prompt
   `$ ` inside a fence with a caption when referred to; a list of inline
   prompts is not a guide construct, and the items wrap awkwardly in the PDF.
   Severity: should. Fix: replace with a captioned `**Example 2.6. The first
   run on a new machine**` fence holding the four commands, and a one-line
   prose reference.
9. Quote: `requirements.txt` (line 70), `Dockerfile` (lines 168, 182, 260, 376),
   `/usr/local/bin/epubcheck` (266). Rule: "Italic for a filename". These are
   constant width. Severity: should. Fix: `*requirements.txt*`, `*Dockerfile*`,
   `*/usr/local/bin/epubcheck*` (a path in prose; leave `/book` where it is
   part of the typed command).
10. Quote: "The scan belongs to LuaLaTeX, and press does not hurry it." (line
    350). Rule: the Div must close on its own with a blank line after it; the
    paragraph abuts the closing `:::` (line 349). It renders correctly today but
    is fragile. Severity: should. Fix: add a blank line after `:::`.
11. Quote: `[^yaml]`, `[^dev]`, `[^binfmt]`, `[^macos]` definitions (lines
    372 to 378). Rule: definitions go "at the end of the section". They sit at
    the end of the file. Labels are unique and pandoc resolves them. Severity:
    should. Fix: move each definition after the paragraph that cites it.

## Checked and clean

In this chapter box matches the seven A-heads exactly; headings sentence
case, no digits, never two in a row; no language tags; no code line over 72
characters in any fence; no trailing whitespace; ASCII only; no dashes; the
three figures have the art comment first, `#fig:`, `.diagram`,
`width=full-measure`, `fig-alt` unlike the caption, caption without period, and
an `@fig:` reference before each. Tables each have a header row and a
`Table: Table 2.N.` caption after a blank line. Six tips and warnings (limit 8)
and one sidebar; each tip or warning is one to four sentences. Index comment
last, 25 terms. Cross-reference titles to Chapters 3, 7, 8, 11, 14, 15 match
the chapter files. No plates in this chapter. Figure briefs: no wrap
placement, no tree or matrix over 14 rows. Layout: no heading stranded at a
page foot; Table 2.1 and Table 2.3 split across pages with the header
repeated (acceptable); "Table 2.4 lists the states" ends PDF p. 33 and the
table starts on the next page (acceptable).
