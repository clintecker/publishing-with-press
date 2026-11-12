# Report: Chapter 15, The operator's desk and the editorial machines

File: `book/chapters/15-the-desk-and-the-machines.md`. Not committed.

## Word count

`press wordcount`: 4,933 (target 5,000; within 2 percent).

## Checks

- `press check`: exit 0. Source, self-test, editorial, and jargon checks all
  pass; no finding names this file (one inspect finding, "settles", fixed;
  one rewrite finding, "authoritative", inside a quotation, removed).
- No line over 64 columns in any `text` fence; no non-ASCII character; no
  trailing whitespace. Each image line plus its `art:` comment: Figure 15.1,
  159 words; Figure 15.2, 170 words; the plate, 96 words. Sidebar: 131 words.

## Figures

- **Figure 15.1** `@fig:the-desk`, `assets/woodcuts/15-01-the-desk.png`,
  `.photo`, screenshot. A headless capture of `press desk` in the alice book
  on hatter at 100 x 36, title bar `alice@hatter`. It shows the identity block
  (title, authors, trim `6 x 9 in`, slug), the artifact table (artifact, state,
  published) with `-` and `o` rows after a `press pdf` run, the toolchain line,
  the doctor table with glyphs, and then the target picker with its argument
  box (after pressing `p`). Reader sees the state column first, then the
  toolchain line. Note for the illustrator: if the picker replaces the DESK
  screen instead of overlaying it, a two-frame capture (DESK, then picker)
  answers the directive; the fact file does not say which.
- **Figure 15.2** `@fig:editorial-passes-machine`,
  `assets/woodcuts/15-02-editorial-passes-machine.png`, `.diagram`,
  flowchart top to bottom: Scout (manuscript, `press skills`); per-chapter
  passes and the three whole-book lenses (cadence, repetition, arc) feeding
  suggestions; one synthesizer per chapter with a side arrow to
  `build/editorial-rejections.md`; `press check` labelled Law; a diamond for the
  stop rule (zero suggestions or fewer than 5 applied) and a diamond for rounds
  left (default 2) looping back. The loop is what the reader sees first.
- Plate (the proofreaders' bench): moved to the end of "The editorial passes",
  the two lines and the blank line between them unchanged.

## Tables and examples

Tables 15.1 (doctor glyphs), 15.2 (keymap), 15.3 (live evidence states),
15.4 (workflows), 15.5 (skills), 15.6 (operator commands). Examples 15.1
(`press workflows` entry), 15.2 (house law), 15.3 (the `claude` command),
15.4 (the named diseases). Each is referenced before it appears. Three short
uncaptioned fences (launching the desk, a Workflow call, the counsel-mode
message) plus one six-line-of-commands session, none referred to again.

## Rulings followed

- Evidence states: the chapter follows the live desk. Table 15.3 lists only
  `-`, `o`, `/`; the prose says the read model can express a verified and a
  changed state but the live desk passes no evidence, so present artifacts
  show `o`. A warning tells the reader not to wait for a verified glyph.
- Keymap includes `c` (cancel, process group) and notes that the desk's own
  documentation omits it.
- Wizard: four fields only (title, subtitle, author, description); other keys
  go through `press config`.
- Named diseases quoted verbatim from the fact file's quotation of the
  workflow source; the reason is CLAUDE.md's sentence, quoted.
- Doctor panel (Chapter 2 promise): described with Table 15.1 and shown in
  Figure 15.1. Operator commands (Chapter 2 promise), skills, the Workflow
  tool, and `claude` (Chapter 11), `authorities-research` and `press research`
  (Chapter 10), workflow stamps (Chapter 3), and the phase and plus-sign lines
  (Chapter 7) are all covered.

## Facts needed and not found (left out)

- Captured desk output: none in the fact file, so no desk session is
  reproduced; the figure directive describes the screen from the read model.
- Exact artifact names in the desk's table: not given; left general.
- Whether the picker overlays DESK or replaces it: not given (see figure note).
- The installed path printed by `press skills`: the fact file abbreviates it,
  so the chapter describes the output instead of reproducing it.
- `press improve` output: none captured; the session shows commands with
  elided output only.
- Chapter 7 says the desk also uses the time lines for progress; facts-15
  names only the pilcrow phase lines and the plus-sign lines, so the chapter
  names those two.

## Contradictions in the fact file

- Doctor glyphs list `-` twice (absent and unset). The chapter reports it as
  one glyph with two meanings.
- The stage line contains a check mark and middle dots, and the phase markers
  a pilcrow, all outside ASCII. The chapter describes them in words.

## Edits to quoted output

- `press workflows` (Example 15.1): `demo` became `alice`, the abbreviated
  path became `/Users/alice/alice` (hatter is a Mac, per Chapter 8), and the
  four lines are broken to fit 64 columns, which the text says.
- House law, diseases, the counsel-mode message, and the `claude` command are
  broken to fit; the `claude` command is written with shell continuations and
  the text says press passes it as an argument list.

## Residual `ste_check.py` findings, with defence

- Semicolons (lines 22, 47, 127, 192, 200, 228, 239, 390): all inside quoted
  press text ("Every action it runs ...", "identity written; next: press
  check", "Preserve the author's voice; do not add length", "Do not invent
  citations; ..."), inside an `art:` comment or the plate's untouched comment,
  or in the index comment. None in my own prose.
- Passive "may be assumed" (238): quotation from the workflow.
- Sentence length over 25: line 6 is the In-this-chapter box read as one
  sentence; 41 counts across a footnote marker; 47, 190, 192, 228, 390 are
  image lines, `art:` comments, and the index comment; 198 is 29 words, under
  the 30 ceiling.
- Paragraph of 7 sentences (294): the sidebar, which the checker counts as one
  paragraph; it is 131 words.
- Word swaps (whether, therefore, verify, identical): period-correct by the
  prose contract's 80% rule, or the name of a phase (*Verify*).

## Revision (after facts-15, dev-15, copy-15, type-15)

Word count after revision: 5,146 (`press wordcount`; target 5,000). `press
check` exits 1 only on `book/chapters/16-inside-the-press.md:232` (assistant
vocabulary), which is another writer's file. Nothing names this file.

### Coordinator rulings applied

1. Facts. Line 30: only `editorial-passes` (`press check`) and
   `authorities-research` (`press pdf`) end on a target. The other two end in
   an audit. "Deterministic" is cut, and so is the Chapter 2 doctor-line
   quotation. The research section's opening now claims only a scout, then
   each workflow's own phases. The house-law sentence now quotes the string's
   own "mechanical, build-enforced". The sidebar now claims only the two
   copies, the portable copy's place beside *references/watchlist.csv*, the
   reason (works without press installed), and the byte-parity contract. The
   "same CSV" and "one watchlist" claims are gone. Example 15.1 keeps the
   capture's shortened paths (with the capture's ellipsis typed as three
   periods) and its line order, breaks only at spaces with a four-space
   continuation indent, and the lead-in says so. The Bash grant paragraph now
   says every run grants `Workflow` and `acceptEdits`, and that the grant
   limits only the shell. Table 15.6 marks `--rounds`,
   `--max-claims-per-file`, and `--overwrite` "not listed by `--help`", as
   Appendix A does.
2. Developmental. Added a seven-step procedure, "Running editorial-passes from
   your own session". It starts from `press doctor` showing `claude` `ok`,
   with one sentence saying that `alice` repaired `claude` at the end of
   Chapter 2 (Example 2.7), and it ends on the four return keys and the
   rejections file. Claude Code is defined in a clause at first use. The
   orientation is five sentences, and its "two ways" (by hand, by agent) now
   match the first A-head. The final paragraph's "long build" contrast is
   cut, and the chapter now ends on the whole-book lenses. RUN view, read
   model, coined maxim, and maxim quota are defined at first use. A paragraph
   after Example 15.1 explains its two `args:` braces. The counsel session is
   now Example 15.4, and the diseases became 15.5. Only one "commit before you
   apply" warning remains, in the procedure. The operator warning is now
   about the full Bash grant. Cut: the `c`-key documentation note,
   `preview_edits`, and the `human-writing` front-matter name. P5 "up to
   three rounds" and P6 (how to read a skill, on `alice`) are both done.
3. Copy blocks: "ships" x5 became "carries" or "comes with", "proves" became
   "checks", and "drift apart" became "come to differ". The -ing rider is now
   "writes ... and shortens". Both closers (24, 85) are rewritten or cut. Term
   changes: "list of diagnostic patterns", "the validation step", sidebar
   title "The jargon lint, twice", "book repository" (two places), "the Print
   edition (the PDF)". American spellings are in ("grays", "afterward" x2,
   "right after"). "honors" went with the cut `c` note.
4. Typesetting: "maxim quota" is now in prose (italic, defined) and stays in
   the index. Every example over six lines is numbered. The step labels in
   the research list are plain text. Figure 15.2's directive now runs left to
   right and wider than tall, with "one pass per chapter file" (three boxes
   and an ellipsis), and so do the synthesizers. Figure 15.1's directive puts
   the picker to the right of the tables, clear of the state column and the
   toolchain line, and names the toolchain line it shows (the ready line,
   after the repair). Its fig-alt now says "beside them". Ran
   `tools/prefix-footnotes.py`: unchanged, labels already `15-`. Every fence
   is `text`.

### Other shoulds resolved

- facts-15 drifted 2 to 18: the counsel message is marked "broken here to
  fit the page". Other changes: "Without a TTY, it points you to the
  command line". The `not ready:` line no longer claims what sits between
  its ends, and "typed" is dropped. `press` is added as the third
  `authorities-research` argument, "unresolved" is no longer defined, "any
  fragment that does not match", "one-line" is dropped, "generatable" is
  restored, "hard-codes them in its source", and "the workflow demotes the
  rest". The Workflow-tool route is hedged as "runs the workflow by name,
  which is the book's pinned copy". Also: "the stamp in each copy", the
  "workflows use the name" sentence cut, the result line on the child's exit
  code, "behind a boundary gate around `press.adapters`", the desk's
  escape-hatch wording, "Zinsser's", "one skill to a line, its name and then
  its installed path", "never reaches the file", and the stop-rule rationale
  cut.
- copy-15 should 11 to 36: all applied. Item 14 is folded into ruling 1. For
  item 27, the rationale is cut per facts. For item 29, the warning moved to
  the procedure and says "a workflow that applies edits".
- dev P7 (Chapter 7's "time lines"): no change here. Route to continuity:
  Chapter 7 l.456 should drop "and the time lines", or facts must confirm
  them. N2 is folded into the Figure 15.1 directive. R1: the `/` sentences
  and the desk/verifier antithesis are cut.

### Mays

- facts M1 (`--help` omissions): applied. M5 (return keys): applied in the
  procedure.
- facts M2 (Textual 8.x): declined. Chapter 2 owns the extra.
- facts M3 (commission headings and details): declined. Chapter 11 covers
  them.
- facts M4 (naming `*` and `!`): declined. Per the coordinator, the chapter
  follows the live desk, where those glyphs cannot appear.
- copy 37: declined. *workflow* keeps its italic definition at its first
  defining sentence.
- copy 38 to 49, 51, 54, 55: applied. 53 is moot (paragraph cut) and 56 is
  moot (sentence cut).
- copy 50 ("parity contract"): declined. The fact file's wording is
  "byte-parity contract".
- copy 52 ("digest" for fingerprint): declined. "Fingerprint" is the
  operator's own word.
- type 6 (Table 15.5 page break): no change. The break depends on final
  pagination.
- dev, for the copy desk (re-italicizing workflow, skill, operator): kept
  italic, per vocabulary.md (first use in each chapter). The sidebar stays
  the brief's suggested design rationale.

### Residual ste_check findings

- Paragraph length at 47 and 210: the two `art:` comments.
- Semicolons and long "sentences" are all in quotations, `art:` comments, the
  In-this-chapter list, the fig-alt, or the index comment. The modal passive
  at 252 is a quotation from the workflow. Word-swap and -ing hits (headings,
  quotations, gerunds, "therefore", "whether", the phase name *Verify*) are
  accepted under the 80 percent rule, as before.

## Revision 2 (after rereview-15)

Changes in this pass:

- Line 83: the desk parses three markers, the phase lines, the plus-sign lines, and the time lines (`pandoc took 26.7s`), per facts-07.
- Line 18 and the Figure 15.1 directive now say "the Alice book".
- Line 238 is split, with a pointer to step 6 of the procedure.

Mays applied:

- Table 15.5 now says "the logomark, the printer's mark".
- "Prose skills" is glossed before Table 15.4, with a pointer to "Skills".
- Line 127 is reworded.
- Three of the "therefore" uses are cut.

Results:

- 5,197 words.
- `press check` fails only on Chapter 12's unreferenced plates; nothing names this file.

## Revision 3 (after continuity-15)

l.30 now names `press verify`; "command" replaces "target" at l.22 and l.24; l.269 says "illustration of a generatable kind" and "`art:` directive"; *skill* is italic and defined at l.18, and l.135 and l.277 now use the term; Table 15.1 keeps the lowercase desk states and notes the doctor prints `MISSING` and `BROKEN`. The `press check` failures name other files only.
