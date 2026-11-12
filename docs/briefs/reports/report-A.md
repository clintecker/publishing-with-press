# Report: Appendix A, Command reference

File: `book/appendices/a-command-reference.md`. Not committed.

## Word count

5,551 by `press wordcount` (target 6,000; 7.5 percent under, inside the
15 percent band). The count strips fenced and inline code, and this
appendix is dense with both, so the printed length is well above 5,551.

## Shape

- Heading `# Appendix A: Command reference {.unnumbered}`, two
  orientation paragraphs (synopsis conventions, `--help`/`-h`,
  `--version`, the bare-press and unknown-command exit 2, the "not
  listed by `--help`" convention, session conventions), then 48 `##`
  entries in alphabetical order, then `## Exit codes` and
  `## Environment variables`, then the index line.
- Entry granularity: `art` and `config` are split into their
  subcommands (`art accept`, `art commission`, `art enhance`;
  `config get`, `list`, `set`, `unset`, `validate`), because each
  subcommand has its own flags. `isbn`, `migrate`, and `lookup` are one
  entry each, with their verbs in the synopsis, because their verbs take
  no flags. `verify-pages` has its own short entry (alias, not in
  `--help`).
- Each entry: **Synopsis.** (text fence), **Description.** (one to three
  sentences), **Options.** (table or "None."), **Example.** (a lead-in
  sentence or two, then a session), **See also.** (chapter by number and
  italic title, then sibling commands).
- Tables A.1 to A.20 (18 option tables, exit codes, environment
  variables), each cited in prose before it appears. Examples A.1 to
  A.9 are captioned (sessions of six lines or more), each cited before
  it appears; shorter sessions are uncaptioned. One warning box
  (`press art commission`, name the model). No figures, no footnotes,
  no `art:` comments.
- Every flag in facts-A 17.2 appears. Flags marked absent from the help
  grammar (20.A.23) say "Not listed by `--help`": `art enhance` (whole
  subcommand), `cover --print`, `illustrate --subject/--print`,
  `improve --rounds`, `research --max-claims-per-file`,
  `aesthetic --overwrite`, `new --author/--publisher/--place/--owner`,
  `config --json/--dry-run/--file`, `selftest --write-docs`, and the
  alias `verify-pages`.

## Sources for the sessions

Sessions reuse captures already in the chapters (Ch. 3, 5, 6, 7, 8, 10,
11, 13, 15) or the fact files. Where neither had output, I ran the
installed press 3.0.2 (`~/code/.pwp-venv/bin/press`) on a throwaway
scaffold in my scratch directory (`press new alice --author "Lewis
Carroll"`) and quoted the real output: `config get registrations.lccn`
(`not set`, exit 5), `config set trim 5x8` (exit 3), `config list
--file config/house-rules.yaml`, `config unset subtitle --dry-run`,
`isbn status` with the docs' example block, `onix` (`ISBNs: none yet`),
`migrate status`, `desk` without the extra (exit 2), `figures` on one
plate, `add appendix <name> --front` (makes `a-<name>.md`), the
`art accept` success line format, the aesthetic source comment.
Nothing in the repository was touched by those runs.

- The `press verify` capture (23 pages) is the press's own Alice
  example; the entry labels it so, per the cast ruling.
- The `art accept` line shows `(1024x1024)`, the size `press
  illustrate` requests per facts-11 8.5; the line format is real.
- Long output lines are wrapped with a four-space continuation, as
  Chapter 6 does; two absolute paths are shortened with `...`.

## Facts needed and not found (left out)

- Output of `press render`, `press print`, `press verify-print`,
  `press publish`, `press research`, `press lookup`, `press coverwrap`
  (beyond its refusal), and `press isbn assign`: shown as the command
  with `...`.
- `press render`'s page-image filenames: not stated, so the session
  lists the directory with `...`.

## Deliberately avoided (fact file section 20)

- `isbn assign` output and the `onix` ISBN line: both would show the
  publication number starting at 0 (20.B.20); not shown.
- `migrate plan` on a v3 book proposing v4 (20.B.21): the example uses
  `migrate status` only.
- The Markdown edition shipping figure attributes and `art:` comments
  as written (20.B.9), txt/docx having no drop cap (20.B.10),
  `verify-formats` and a stale PDF (20.B.11), `verify-print` building
  twice (20.B.12), the doctor and `pdfimages` (20.B.14): not mentioned.
- "vacuous witnesses" is not used outside a quoted message; the
  `PRESS_RELEASE` row says "release witnesses".
- The Gemini default (20.B.15) is stated only as the default plus a
  warning, matching Chapter 11 l.484 to 495.
- `press add --front` is described as a `00-` chapter or an `a-`
  appendix, not a "front-matter part" (20.A.22).
- The desk's wizard is not claimed to cover every field (20.A.19).

## Contradictions noticed

- `press --help` omits `verify-pages`, but the usage block that a bare
  `press` (or an unknown command) prints does list it under
  "checking". The entry says "not listed by `--help`", which is true of
  `--help`.
- facts-A 17.2 writes `config list [--file F]`; the code compares F with
  the file path as `config/house-rules.yaml` (a bare `house-rules`
  matches nothing). The entry uses the path form.

## Checker residuals

- `press check`: passes, no finding naming this file.
- `tools/ste_check.py`: 26 findings, all defended.
  - 12 `ing-form`: chapter titles in See also lines (*Installing
    press*, *Verifying the artifacts*, *Checking the manuscript*).
  - 8 `sentence-length`: the counter splits paths and inline code
    (*build/cover/cover.png*, `[a-z0-9][a-z0-9-]*`) into several words
    and joins sentences at dots inside filenames; by the STE rule
    (identifier = one word) none exceeds 30. One is the index comment.
  - No `passive` findings remain; the one ("is required") was
    rewritten, and the counter does not flag the brief's required
    phrase "not listed by `--help`".
  - 4 `word`: `enhance` (the subcommand's name), `verify` (a command
    name), `whether` (period-correct per the prose contract).
  - 1 `perfect-tense` ("press has eleven"): a possessive "has", not a
    perfect.
  - 1 `semicolon`: the index comment, whose format requires them.

## Revision 1 (after facts-A, copy-a, type-a and the managing editor's rulings)

Word count now 5,733 by `press wordcount`. `press check` passes.

- Rulings applied: `press source` states the two cases from the editor's
  rerun (outside any Git repository the whole directory, 14 files on a
  fresh scaffold; untracked inside another repository, an empty archive
  until Git tracks the files); `--front chapter` makes `00-<name>.md`;
  the print-safe copy advice (`press print`) and the broken-optional-tool
  sentence (`press doctor`) are cut; `press lookup` reaches the network
  as `cover`, `illustrate`, `art commission`, and `research` do;
  `press selftest` prints progress and ends with the success line (`...`
  in the session); the uncaptured `ls` in `art commission` and the
  colored-code-block claim in `verify-print` are cut; the three
  `art commission` flags say "Not listed by `--help`".
- Every wrapped output line is rebroken at a word boundary, at most 64
  columns, with the continuation indented two spaces past the line's own
  indent; the intro states the convention. Lines reproduced unbroken
  from the reruns where they fit.
- Fact fixes: unknown command (usage first, then the suggestion when
  there is one); `--front appendix` counts up from `a-`; a chapter takes
  the number after the highest in use; cover aspect read from the legacy
  `trim` field at the time of this writing; the ghost refusal is for
  single-ink plates; `press all` and the commerce gate with print
  ordering; `config list --json` fields; full coverwrap and verify-print
  messages; workflows paths as `.../alice`; skills tab noted; isbn
  no-block message, exit 1, and the two `config set` calls; render
  `page-*.png`; migrate hedge (press 3 is the newest major).
- Copy fixes: both blocks ("EPUB gate", "fallback title"); sentence-start
  "Press" capitalized; "the Alice book" for the sample book; edition
  names; American "color"; "table of authorities" for "ledger"; the two-
  idea splits, hidden actors, and the may items.
- Type fixes: `tools/unnumber-appendix-heads.py` marked all 50 headings
  ` {-}`; `tag-fences.py` and `space-art-comments.py` made no changes;
  the first column of every option table widened to 24 dashes. The
  appendix running head (type item 2) is a template matter outside this
  file.
