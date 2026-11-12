# Typesetter report: Appendix A

File: book/appendices/a-command-reference.md (1341 lines). Status: builds; 1 blocks-class markup rule broken (50 headings), 3 should.

## press check / press pdf

- `press check`: source checks passed (23 files); checker self-test passed. Editorial checks failed on `book/appendices/e-glossary.md:300: avoiding is/has`, not this file. Nothing was reported against Appendix A.
- `press pdf`: first run failed on 23 missing PNGs (17 figures plus 5 plates and rule/heights). I created 1362x800 white placeholders for exactly the 23 missing at build time, built (357 pages, exit 0), and deleted those 23. Appendix A is PDF pages 294-324 (printed 285-315).

## Findings

1. blocks. Quote: `## press add` (and every `##`: 50 of 50; `###`: none). Rule: markup.md "Every `##` and `###` in an appendix ends with ` {-}`". Effect in the PDF: entries are numbered with the last chapter's counter ("16.12 press add", "16.13 press aesthetic", ... "16.56 press verify-pages"). Fix: `tools/unnumber-appendix-heads.py` (not run; desk may not edit).
2. should. Running head on every Appendix A page after the first reads "Publishing with Press / 16 Inside the press" (the last chapter's head). Same on Appendices B and C. Not fixable from the markdown; a press/template issue (appendix running head). The contents page lists "Appendix A: Command reference ... 285" correctly and lists no `##` entries, as intended.
3. should. Table A.2 and Table A.5 first column is too narrow for the option names: `--overwrite` breaks as "--" / "overwrite", `--max-edge PX` breaks as "--max-edge" / "PX". Quote: `|--------------|----...` (separator at 14 dashes for column 1 in all 20 tables). Fix: lengthen the first-column dashes (about 24) in those tables, or all 20 for consistency.
4. should. No page breaks between entries; the 48 entries run on continuously (about 1.5 per page). Synopsis behaves: each `## ` heading is followed by its Synopsis label and fence on the same page (headings at p296, p311, p317, p320 foot keep heading+Synopsis label+synopsis together; the Description follows on the next page). This is acceptable; report only if page breaks per entry are required (they cannot be typed in the markdown).
5. should (minor). `Options. Table A.1 lists the one option.` is at the foot of p294 with its table at the head of p295; table captions sit above their tables (house style).

## Construct checks (all clean)

- H1 exact: `# Appendix A: Command reference {.unnumbered}`.
- 48 entries each with Synopsis/Description/Options (50 `##` = 48 commands plus "Environment variables" and one other section).
- Fences: all tagged `text`; no untagged or language fences. Longest code line within 64; no line wrapped with a hook (no hook glyph in the appendix pages). No trailing whitespace.
- Footnotes: none in the file. No non-ASCII characters, no em/en dashes or `--` in prose (the `--- a/metadata.yaml` at line 377 is diff output inside a fence).
- Example captions: 9, `**Example A.N. Title**`, no trailing period, sequential A.1 to A.9. Tables: 20, each with header row, proportioned separator, `Table: Table A.N.` caption after (A.1 to A.20, none ending in a period). The `**Example.**` bold lead-ins are prose, not captions.
- No figures, tips, warnings, sidebars, or "In this chapter" box (appendix; none required). No paragraph of 190 words (the 245-word hit is the environment-variable table).
- Index comment present and last line (line 1341).
