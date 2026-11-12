# STE80 review: Chapter 7, Building the editions

File: `book/chapters/07-building-the-editions.md`
Diff: `git diff HEAD -- book/chapters/07-building-the-editions.md` (17 edits, as the editor's report lists them).

Status: APPROVED. Blocks 0, should 2.

Mechanical checks run:

- Verbatim material: every inline code span, italic path, `@` reference, and number in the removed lines reappears unchanged in the added lines (multiset comparison over the diff).
- Index terms: every string in `config/index-terms.yaml` occurs the same number of times in HEAD and in the working file.
- Sentinels: none of the three stands in this chapter, before or after.
- Markup: `press check` passes (checker self-test, editorial checks over 23 files, jargon check). No prose paragraph exceeds 190 words. No blockquote was touched. The sidebar "The lists that would not converge" (Light mode) is unchanged.
- Facts: checked against `docs/briefs/facts/facts-07.md` (pandoc command shape, generated appendices, registry tables, `book_inputs()` steps) and the managing editor's correction in `docs/briefs/facts/facts-03.md` (archive outside a repository versus untracked inside one). No fact is added, lost, weakened, or strengthened.

The two edits the editor flagged:

- Edit 2 (line 74, "carries none"): the fact survives, but the pronoun admits a false reading. See finding 1.
- Edit 12 (line 312, "the bundle" for "it"): correct. In the old sentence, "it" had the subject "The Pages bundle" as its referent, and the reason clause ("so it is never a download itself") is about the bundle, which the registry marks "no". "The Pages site holds the downloads" keeps the old relative clause at full strength. "The bundle" is a short form of the vocabulary term "the Pages bundle" (`docs/vocabulary.md` line 31), not a banned variant, and the paragraph names "the Pages bundle" in full twice before it. No finding.

## Findings

1. Line 74. Severity: should (ambiguity; the fact survives in the intended reading).
   - Old: "The input files follow in book order: the chapter files, then the appendix files sorted by letter, with any generated appendix, such as the subject index, sorted among them. The Alice command carries no generated file."
   - New: "The input files follow in book order: the chapter files, then the appendix files sorted by letter. The press sorts any generated appendix, such as the subject index, among them, and the Alice command carries none."
   - What went wrong: "none" has two candidate antecedents, "any generated appendix" and "them" (the appendix files). The second reading says that the Alice command carries no appendix files, and Example 7.1 directly above shows `book/appendices/z-about-this-edition.md`. The old text named the thing explicitly ("no generated file"). The editor joined the sentences to keep the paragraph at six sentences, so the fix keeps the join and restores the noun.
   - Corrected: "The press sorts any generated appendix, such as the subject index, among them, and the Alice command carries no generated file."

2. Line 206. Severity: should (voice; repetition introduced).
   - Old: "Pandoc then writes the LaTeX and hands it to latexmk(1), the PDF engine that Example 7.2 names. latexmk runs LuaLaTeX with the `-lualatex` option, as many times as the document needs."
   - New: "Pandoc then writes the LaTeX and hands it to latexmk(1), the PDF engine that Example 7.2 names. Then latexmk runs LuaLaTeX with the `-lualatex` option, as many times as the document needs."
   - What went wrong: the added "Then" fixes the hidden sentence boundary for the counter, but it echoes the "then" one sentence earlier, so two consecutive sentences open their sequence with the same word. No fact changes. A subject that starts with a capital letter fixes the boundary without the echo.
   - Corrected: "Pandoc then writes the LaTeX and hands it to latexmk(1), the PDF engine that Example 7.2 names. The latexmk program runs LuaLaTeX with the `-lualatex` option, as many times as the document needs."

## Edits approved without finding

Edits 1, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, and 17. Notes on the ones that were close:

- Edit 10 (line 283): "is archived whole" became "the press archives all of it". This is the same strength as the original and matches facts-03's correction. The excluded directories (`.git`, `__pycache__`, `build`, `dist`) are reported in the next sentences, so "all of it" does not contradict them any more than "whole" did.
- Edit 15 (line 357): "published beside the book" became "The press publishes it beside the book." Naming the actor adds no fact. Table 7.4 marks `sources` as published, and Table 7.5 gives its destinations.
- Edit 17 (line 482): "look over" became "examine". The sense is the same, and Chapter 3 line 625 already uses "examine" for the same `press render` use.
- Edit 7 (Table 7.3): the cell now holds two sentences. "It" can refer only to "This filter". The table row stays one line, so the pipe table is intact.
