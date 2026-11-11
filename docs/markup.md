# Markup: exactly what to type

Every construct below was proven in press 3.0.2's own toolchain. Type it
exactly; the reviewer and `press check` hold the line. Nothing else is
available: no raw LaTeX, no HTML, no attributes beyond those shown.

## The chapter file

```markdown
# Checking the manuscript

::: {.in-this-chapter}
> **In this chapter:**
>
> - The four passes of press check
> - The style audit
> - House rules
> - Known-bad fixtures
> - Sentinels and the page floor
:::

Before press builds anything, it reads every chapter and compares it
against the house rules. ...
```

- The first line is the chapter title, sentence case, no number (press
  numbers chapters). The Preface is `# Preface {.unnumbered}`.
- The "In this chapter" box is a blockquote inside a classed Div. It
  renders as the house grey box in the PDF and a ruled box on the Web. List
  the A-heads exactly as they appear.
- Then the orientation paragraph, with no heading above it.

## Headings

- A-head: `## Running the checker`. B-head: `### The style audit`. Sentence
  case. Press numbers them (1.1, 1.1.1); do not type numbers.
- Never a heading that starts with a digit. Never two headings in a row.
- Appendixes: `# Appendix A: Command reference {.unnumbered}`. The letter is
  typed by hand and matches the filename letter.

## Prose

- Straight quotes only; pandoc curls them. No em or en dash; no `--` or
  `---` either (they become dashes). Use a comma, a colon, a period, or
  parentheses.
- Only ASCII plus accented Latin letters. No `©`, `§`, `°`, `×`, `...`
  (type three periods), arrows, or non-breaking spaces.
- A paragraph has fewer than 190 words.
- Italic for a filename, a directory, a URL, and a new term at its
  definition: `*config/metadata.yaml*`, `*dist/*`, `*target*`.
- Constant width for a command, an option, a config key, an environment
  variable, a value, and anything the reader could type: `` `press check` ``,
  `` `--strict` ``, `` `verify-min-pages` ``, `` `PRESS_RELEASE` ``.
- Program names as proper nouns are roman: pandoc, LuaLaTeX, latexmk,
  epubcheck, Graphviz, Git. The command is constant width: `` `pandoc` ``.
- Footnote: `text.[^note]` and, at the end of the section,
  `[^note]: The note.` Labels are unique within the file.

## Tips, warnings, and sidebars

```markdown
::: {.tip}
> **Tip:** Run `press check` before you commit. The CI build runs the same
> command, and it is faster to learn at your desk than from an e-mail an
> hour later.
:::

::: {.warning}
> **Warning:** Do not raise the figure height cap. A figure taller than the
> text block makes LuaLaTeX emit empty pages forever, silently, at full CPU.
:::

::: {.sidebar}
> **The red check that shipped green**
>
> A commit chain once piped `press check` into `grep` before the `&&`. The
> pipeline's exit status was grep's, and a failing check shipped as a
> passing one. ...
:::
```

- All three are a blockquote inside a Div with the class named. The PDF
  shows the house box (grey, hairline, small italic); the Web shows the
  classed box; the EPUB shows a ruled quote.
- A tip or warning is one to four sentences and begins with the bold lead
  word and a colon. A sidebar begins with a bold title line, then a blank
  quote line, then its paragraphs, 120 to 180 words in all (the checker counts the whole sidebar as one paragraph and refuses 190). Do not put a heading,
  a table, a figure, or a code block inside one.
- At most eight tips and warnings and one sidebar per chapter.

## Examples (code)

```markdown
Example 3.1 shows the smallest metadata file press accepts.

**Example 3.1. A minimal metadata.yaml**

```
title: "Alice's Adventures in Wonderland"
author:
  - "Lewis Carroll"
slug: "alice"
```
```

- The caption is a bold paragraph directly above the fence: `Example C.N.`
  then a title in sentence case, no period at the end.
- Fences are untagged (three backticks and nothing after them) or tagged
  `text`. Never a language tag: a highlighted fence puts colour in the
  print interior and the print verifier refuses it.
- Sessions show the prompt as `$ ` (or `# ` for root), then the command,
  then the output. No bold, no colour. Elide with a line holding `...`.
- Lines are at most 72 characters (a terminal panel is drawn at 72
  columns, and the page wraps longer code lines with a hook). No trailing
  whitespace, even in code.
- A syntax line uses `[ ]` for optional, `|` for alternatives, `...` for
  repetition: `press add chapter|appendix <name> [--front]`.
- Fragments under six lines that are not referred to again need no caption.

## Tables

```markdown
Table 6.1 lists the options the checker takes.

| Option | Meaning |
|--------|-------------------------------------------------------------|
| `--strict` | Treat warnings as errors. The CI build uses this. |
| `--only` *`chapter`* | Check one chapter instead of the whole book. |

Table: Table 6.1. press check options
```

- The caption line begins `Table: Table C.N.` and ends without a period.
  It goes after the table with a blank line between.
- Two or three columns; the header row is required; make the separator row
  long and proportioned to steer the widths; sentences in the Meaning
  column.

## Figures (numbered diagrams, terminal panels, screenshots)

```markdown
Figure 7.1 shows the graph the registry declares.

![The build graph the registry declares](assets/woodcuts/07-01-build-graph.png){#fig:build-graph .diagram width=full-measure fig-alt="A left-to-right diagram: chapter and config files flow into press check, then pandoc with its filters, then into seven editions, which converge on the verifiers."}
<!-- art: ARCHETYPE pipeline, left to right. Left: two file icons, "book/chapters/*.md" and "config/*.yaml". Centre: a rounded process box "press check", then a rounded box "pandoc" listing in small monospace the five filters in order (typographic-spacing, set-pieces, chapter-dropcap, scene-break, figure-numbering). Right: ... The reader should see first that every edition starts from the same two inputs. -->
```

- Refer to the figure in prose before it appears, by `@fig:slug`, which
  renders as "Figure 7.1". Never "the figure below".
- The `art:` comment is the illustrator's brief and comes on the line
  immediately AFTER the image line (press attaches a comment to the image
  it follows; a comment before the image belongs to nothing). The checker counts the comment and the image line
  as one paragraph, so the two together stay under 190 words; put detail
  the illustrator needs beyond that in the report file. Name the archetype (pipeline, data-flow, tree,
  stack, topology, before/after, page anatomy, state machine, filmstrip,
  flowchart, timeline, matrix) and list every element in reading order.
- The image path is `assets/woodcuts/CC-NN-slug.png` (chapter, sequence,
  slug). The file does not exist when you write; the illustrator makes it
  from your brief.
- The kind class is `.diagram` for drawn figures and terminal panels, and
  `.photo` for a screenshot. Width is `full-measure` unless the brief says
  `half-measure`. Placement is `inline` (the default; type nothing) unless
  a figure is taller than wide and long, then `place=plate`. Do not use
  wraps for diagrams; their lettering shrinks.
- Caption in sentence case, no period. `fig-alt` describes the picture for
  a reader who cannot see it, one or two sentences, and is never the same
  text as the caption.

## Plates (unnumbered engravings)

Plates are already placed in the chapters that have them. Leave the image
line and its `art:` comment exactly as they are. A plate has no kind class
and is never referred to by number.

## Cross-references

- Chapter: `see Chapter 7, *Building the editions*`.
- Section: `as described in the section "Reading a failure" later in this
  chapter` or `in the section "The release contract" in Chapter 14`.
- Appendix: `see Appendix A, *Command reference*`.
- Figure: `@fig:slug`. Table and example: by number in prose, `Table 6.1`.
- Manpage: `latexmk(1)`, `crontab(5)`.
- External: `the pandoc Web site at *https://pandoc.org/*`.

## Set pieces and scene breaks

Not used in this book, except a `::: cascade` line block for a sequence of
commands if a chapter has a natural use. A scene break (`* * *`) is not
used.

## Index candidates

The last line of the file:

```markdown
<!-- index: press check; style audit; house rules; known-bad fixture; sentinel; verify-min-pages; jargon lint; watchlist; banned patterns; exit status -->
```

Flat terms only, as a reader would look them up, 10 to 25 per chapter. A
term must appear in prose (not only in code) somewhere in the book.

## What press check refuses

Title-case headings, manual heading numbers, em and en dashes, curly
quotes, glyphs outside ASCII plus accented Latin, paragraphs of 190 words or
more, trailing whitespace, the universal AI phrases, the book's banned
patterns (`config/house-rules.yaml`), the watchlist's rewrite terms, a plate
file nobody references, an unknown figure placement, an absolute figure
width, `left`/`right` placements, and `TODO: write` or `lorem ipsum`.
