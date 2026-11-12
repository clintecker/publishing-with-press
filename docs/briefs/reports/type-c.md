# Typesetter report: Appendix C (book/appendices/c-messages.md)

Builds: `press check` passed (23 files; the self-test passed). `press pdf`
passed (exit 0; Appendix C is PDF pages 338 to 347). No placeholder PNGs
were needed or created.

Counts: blocks 2, should 2.

Clean on the markup guide: heading text and `{.unnumbered}`, no two
headings in a row, no fences (so no untagged or language-tagged fence), no
tables, figures, tips, warnings, or sidebars, no non-ASCII, no trailing
whitespace, footnote label prefixed `c-`, index comment present and last.

## Blocks

1. Quote: `` `<fixture>: a checker rejected the known-good fixture: ...`[^c-ellipsis] ``
   (line 61; note at line 460)
   Rule: a footnote must typeset. The marker sits inside a definition-list
   term; in the PDF the "6" appears after the term but the note text appears
   nowhere (pdftotext finds no "Press ends this message"), and latexmk
   reports "unreferenced destination with name 'Hfootnote.61'".
   Severity: blocks (text silently lost, link error in the log).
   Fix: move the marker out of the term into the Cause sentence, for example
   the first sentence of the entry's Cause, and keep the note at line 460.

2. Quote: the long terms listed under "Should 1" below.
   Rule: markup guide, lines at most 64 columns; verbatim messages may run
   long but must set legibly. In the PDF the term is a single unbreakable
   constant-width run, so it is clipped at the right margin: the end of the
   message is not in the printed page (for example line 51 ends at
   "(up to 3 others or "no di"). Text is lost, which is worse than the
   "wraps badly" case the brief anticipates.
   Severity: blocks for the clipped ones (lines 51, 56, 174, 293, 357, 362,
   367, 402, 450, 455); the same fix applies to all.
   Fix: shorten the term to its fixed leading words and put the full
   message in a `text` fence under it (each line at most 64 columns,
   breaking at natural spaces), or paraphrase with `<...>` placeholders. A
   term of about 85 characters or fewer sets on one line; those near that
   (lines 51 at 92, 450 at 92) clip by a few characters.

## Should

1. Terms over about 85 characters (term length excluding backticks):
   51 (92), 56 (85, clips "...expected rule)"), 174 (118), 293 (111), 357
   (108), 362 (113), 367 (139), 402 (87), 450 (92), 455 (167). Lines 193,
   298, 327, 372 wrapped acceptably. This is the list the Blocks 2 fix
   applies to; no separate fix.

2. Quote: section headings render as "16.71 press check", "16.74 The PDF
   verifier", and so on, under the running head "16 Inside the press".
   Rule: appendix headings are `{.unnumbered}`; the A-heads inherit chapter
   16's counter (Appendix D shows 16.80.1). This is systemic to all
   appendices, not specific to this file, and not fixable in the markup;
   raise it with the press owner (a unnumbered-chapter counter reset).
   Severity: should (outside this desk).
   Fix: none in this file.

Other desks: nothing in `press check` or `press pdf` named another file.
