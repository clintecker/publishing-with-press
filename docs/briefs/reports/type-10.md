# Typesetter report: Chapter 10, Front matter, the index, and the table of authorities

Status: 2 blocks, 3 should. `press check` exit 1 (no finding names this file; see note). `press pdf` exit 0 (with temporary placeholder PNGs, since removed).

## Blocks

1. Quote (line 138-139, Figure 10.1): the image line `![How the two configuration files become the front matter](assets/woodcuts/10-01-config-to-front-matter.png){#fig:config-to-front-matter ...}` is followed on the very next line by `<!-- art: ARCHETYPE data-flow, ...`.
   Rule: markup.md, Figures: the `art:` comment goes AFTER the image line with ONE BLANK LINE between; no blank line means no figure.
   Severity: blocks. Proven in the PDF: no "Figure 10.1" caption appears, and the prose reference renders as the literal text "@fig:config-to-front-matter" (page 174 of the build).
   Fix: insert one blank line between the image line and the `<!-- art:` line.

2. Quote (line 278-279, Figure 10.2): same defect for `10-02-index-entry-path.png` / `{#fig:index-entry-path ...}`. The PDF shows the literal "@fig:index-entry-path follows one term..." (page 179) and no figure.
   Rule and severity: as above, blocks.
   Fix: insert one blank line between the image line and the `<!-- art: ... -->` line.

## Should

1. Quote (lines 42-76, Example 10.1, "# Front matter facts. The presence of this file asks the press to"): the verbatim scaffold file has 14 lines of 65 to 71 characters, so the PDF wraps them with the hook, leaving fragments such as "to", "The", "is", "and" alone on a line. Also the fence breaks across pages 171 and 172 between "# epigraph:" and its "quote:" line.
   Rule: markup.md, Examples: lines at most 64; a verbatim real file may wrap, tolerable only if the wrapped lines read. These do not read well.
   Severity: should.
   Fix: excerpt the file (keep the opening comment's first lines trimmed to a few lines and the keys, ending with a `...` line) so every line is 64 or fewer, and say in the prose that the comment is abridged; or accept the wrap and keep the fence from splitting across the page.

2. Quote (line 302): "The press prints the message as one line. It appears here on two to fit the page." Example 10.4's lines are 62 columns and do not wrap, so this is accurate only as to the source message; harmless. Likewise line 372 note for Example 10.6. No change required beyond confirming the sentence is still true after any edit.
   Severity: should (informational).
   Fix: none needed.

3. Figure 10.2 brief (flowchart, top to bottom): seven stacked nodes with a side branch. Within the 14-row limit, but a tall flowchart at full measure on a 1362 by 800 canvas may exceed the 1740 px cap if drawn vertically; ask the illustrator to keep it at or under the cap, or mark `place=plate` if it must be taller. Figure 10.1 (seven page outlines) is within limits.
   Severity: should.
   Fix: none in the file unless the artwork comes back too tall.

## Checked and clean

- In-this-chapter box lists the eight A-heads exactly as they appear.
- Six tips and warnings plus one sidebar (150 words); the sidebar is within 120 to 180 and under 190; all in the blockquote-in-Div form with bold leads.
- Examples 10.1 to 10.6: bold caption directly above a fence tagged `text`; all numbered in sequence; each referred to in prose before or at use; no trailing whitespace; prompts `$ `; `...` elision. Only Example 10.1 exceeds 64 columns.
- Tables 10.1 to 10.7: header row, proportioned separators, `Table: Table C.N.` caption after the table with a blank line, each referred to before it appears, sentences in the Meaning column.
- Both figure briefs: path `assets/woodcuts/10-NN-slug.png`, `#fig:` id, `.diagram`, `width=full-measure`, `fig-alt` differs from caption, captions in sentence case with no period, referred to by `@fig:` before the figure, each art comment under 190 words together with the image line (122 and 128 words), no wrap placement.
- Headings sentence case, no digits, no two in a row, no typed numbers; unique footnote labels (devil, roman, colophon, silence); index comment present and last. No heading at a page foot, no table wider than the measure, no blockquote box running over a page, no example caption separated from its fence in the PDF.

## Notes

- `press check` exits 1 for editorial "inspect" and "rewrite" findings in other files (chapters 1, 3, 5, 12 and others); none names `10-front-matter-index-authorities.md`. Source checks and the checker self-test passed.
- `press pdf` completed once placeholder PNGs existed for every missing figure file in the book (28 in all, two of them mine). All were created by this desk and deleted afterward; none remain.
