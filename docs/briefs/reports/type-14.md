# Typesetter report: Chapter 14, Continuous integration and the release contract

Builds: `press check` passed (23 files; no message names this file).
`press pdf` completed (one early run failed on another desk's
*03-03-dist-after-all.png*, which was being rewritten mid-build; the retry
passed). No placeholder PNGs were needed or created; all three Chapter 14
figure files exist. Chapter 14 occupies PDF pages 244 to 260.

Blocks: 0. Should: 4.

## Findings

1. Quote: `**Example 14.4. Building on hatter in the image that CI uses**`
   (line 189). Rule: an example caption must not be separated from its
   fence (desk brief; markup guide "directly above a fence"). Severity:
   should. In the built PDF the caption is the last line of page 250 and
   the fence opens page 251. Fix: none in the source is certain to hold
   across reflow; if it persists after the other desks finish, shorten the
   paragraph before it (lines 185 to 187) by a line so the pair moves
   together, or let the caption keep with its fence at the next build.

2. Quote: line 95 and line 97, `        python3 -m pip install --quiet
   --break-system-packages \` (64 characters each, verbatim from
   *action.yml*); line 178, the 64-hex digest
   `0d784ac08282a94e64b444efd86ee3bf9eb45262a9e6e758fc656a2363b2ca04`.
   Rule: code lines at most 64 columns, no hook ("nothing has to wrap").
   Severity: should. Both are within the 64 limit, but in the PDF the
   effective measure takes fewer than 64 characters: the two pip lines
   wrap with a hook (page 247, a bare ` ↪   \` line each) and the digest
   wraps onto a hook line (page 250). Fix: for the pip lines, the verbatim
   exception allows excerpting, so elide the flags (`python3 -m pip
   install --quiet \` then `...` ) or accept the hook; for the digest,
   split it across two fenced lines at 32 characters with the sentence
   above saying so, or show it as `@sha256:0d784ac0...` and keep the full
   value only in the art brief and the text.

3. Quote: figure filenames `14-03-resolving-v3.png` (line 234) precedes
   `14-02-release-state-machine.png` (line 305). Rule: path
   `assets/woodcuts/CC-NN-slug.png` with NN the sequence. Severity:
   should. Figure order in the chapter is topology (14.1), resolving-v3
   (14.2), release-state-machine (14.3), but the files are numbered
   01, 03, 02. Fix: rename the pair (and the three references: image path
   in each line) so resolving-v3 is `14-02-` and the state machine is
   `14-03-`, with the files renamed to match; coordinate with the art desk.

4. Quote: art comment at line 307 ("A start dot, then seven circles in
   monospace, each with a short italic gloss ... a double circle 'done'
   ... Below, a square box 'stopped' ..."). Rule: figure briefs must fit
   the figure rules. Severity: should. Nine nodes in a single left-to-right
   row (start, seven states, done) with glosses crowd a 1362 px full-measure
   figure; the lettering will shrink as it does in a wrap. Fix: ask for the
   seven states in two rows (four over three, snaking), or drop the glosses
   to the caption and the prose. The other two briefs are within the rules
   (topology about 9 nodes, flowchart 6 boxes; both under 14 rows; no
   terminal panel, so no 72-column limit applies).

## Verified clean

- "In this chapter" box: blockquote in `.in-this-chapter` Div, ten items
  matching the ten A-heads exactly.
- Seven tips/warnings (limit eight), each one to three sentences with bold
  lead; one sidebar, 152 words with the title, bold title line, blank quote
  line, no heading, table, figure, or code in it.
- Five example captions `**Example 14.N. ...**` directly above fences; all
  12 fences tagged `text`; no language tags; no untagged fences; no
  trailing whitespace; prompts are `$ `; no code line over 64.
- Four tables, each with header row, proportioned separator, `Table: Table
  14.N. ...` caption after a blank line, no period; Meaning columns are
  sentences.
- Three figures: `art:` comment after the image line with one blank line
  between; `#fig:slug`, `.diagram`, `width=full-measure`; `fig-alt` differs
  from caption; captions in sentence case, no period; each referenced by
  `@fig:` before it appears; each comment plus image line under 190 words.
- Headings sentence case, no digits, no two in a row, no typed numbers.
- Footnote labels `14-pillow`, `14-main`, `14-macos`, `14-migrate`, all
  unique and prefixed. Index comment is the last line, 24 terms.
- No non-ASCII, no dashes, no "below" references. No heading at a page foot;
  no blockquote box runs over a page; no table wider than the measure.
