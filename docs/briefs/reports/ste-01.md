# STE80 editor report: book/chapters/01-introduction.md

Ratchet count: 14 before (baseline 14), 11 after. `press check` passes
(exit 0). Line numbers below are in the edited file.

## Edits

1. L31, S1. Old: "It belongs to one of six *design profiles*, each a trim with its own interior geometry, and Chapter 9, *The house design*, compares them." New: "It belongs to one of six *design profiles*, each a trim with its own interior geometry. Chapter 9, *The house design*, compares them."
2. L43, S1/S2. Old: "Then latexmk, a program that reruns LaTeX until the page references and the lists stop changing, drives it through as many passes as the book needs." New: "Then latexmk drives LuaLaTeX through as many passes as the book needs. That program reruns LaTeX until the page references and the lists stop changing."
3. L45, S10. Old: "Verifying is the part a homemade build script usually leaves out." New: "Verifying is the part a homemade build script usually omits."
4. L45, S6. Old: "The EPUB goes through epubcheck, the validator that retail channels run." New: "The press runs epubcheck, the validator that retail channels run, over the EPUB." (Actor taken from Table 1.2: "The press runs epubcheck over it.")
5. L65, S1. Old: "The ROADMAP records the repository `clintecker/press` as public since 2026-07-19, and the documentation site is at *https://clintecker.github.io/press/*." New: two sentences, "...since 2026-07-19. The documentation site is at *https://clintecker.github.io/press/*."
6. L69, S8 (-ing rider, ratchet lead). Old: "They account for most of the decisions you will meet in later chapters, including several that look strange the first time a refusal stops your build." New: "They account for most of the decisions you will meet in later chapters. Several of those decisions look strange the first time a refusal stops your build."
7. L77, S1. Old: "A book repository therefore holds book facts only, and a capability that one book needs goes into the press, where every other book can use it." New: "A book repository therefore holds book facts only. A capability that one book needs goes into the press, where every other book can use it."
8. L85, S8. Old: "`press check` refusing an em dash is a checker." New: "`press check`, which refuses an em dash, is a checker."
9. L113, S2. Old: "For books with designed interiors, the plan is the *finisher*, a supplied-interior source mode in which the book names a finished PDF with `interior: path/to/interior.pdf`." New: "For books with designed interiors, the plan is the *finisher*, a supplied-interior source mode. In that mode the book names a finished PDF with `interior: path/to/interior.pdf`."
10. L117, S10 (phrasal verb, ratchet lead). Old: "Extensions go through a declared extension contract, which Chapter 16, *Inside the press*, describes." New: "Extensions use a declared extension contract, which Chapter 16, *Inside the press*, describes."
11. L127, S10. Old: "...so the scaffold also fills in the `repository` and `site-url` lines of the metadata." New: "...so the scaffold also writes the `repository` and `site-url` lines of the metadata."
12. L142, S10. Old: "Chapter 3, *The shape of a book repository*, walks through it file by file." New: "Chapter 3, *The shape of a book repository*, examines it file by file."
13. L142/144, S13. The seven-sentence paragraph split at its turn of topic: what the directory holds (L142, 2 sentences) and what the tour's commands did (L144, 5 sentences).
14. L144, S1. Old: "Each `press config set` writes one field, and the `--json` option reads the value as JSON, which is how a list of authors goes in." New: "Each `press config set` writes one field. The `--json` option reads the value as JSON, which is how a list of authors goes in."
15. L144, S1/S2. Old: "`press new` does not run `git init`, so the tour commits the scaffold first, which is the habit the Source edition rewards once the book lives in a repository.[^1-make]" New: "`press new` does not run `git init`, so the tour commits the scaffold first. The Source edition rewards that habit once the book lives in a repository.[^1-make]"
16. L165-168, S14 (warning before the step). The LuaLaTeX font-scan Warning moved, unchanged, from after the "run `press all`" paragraph to directly under the "Building everything" heading, so it precedes the step it protects. L240 ("the font scan in the warning earlier in this section") stays true.
17. L168, S2. Old: "Example 1.2 shows the summary lines from a run on the press's own three-chapter Alice example, which also has an appendix, and elides the rest." New: "Example 1.2 shows the summary lines from a run on the press's own three-chapter Alice example and elides the rest. That example also has an appendix."
18. L202, S10. Old: "...and goes on to "every rendered page contains ink, ..."" New: "...and continues with "every rendered page contains ink, ...""
19. L202, S1. Old: "On a machine without epubcheck, the run warns that it validated the EPUB "structurally only", and it notes that the toolchain image runs the full check in CI." New: "On a machine without epubcheck, the run warns that it validated the EPUB "structurally only". It also notes that the toolchain image runs the full check in CI."
20. L230, S1. Old: "The scaffold already carries *.github/workflows/book.yml*, a short workflow that calls the press's reusable workflow, *build.yml*, so a push is all that CI needs." New: "...the press's reusable workflow, *build.yml*. As a result, a push is all that CI needs."
21. L272, S2. Old: "It holds a print-profile interior, a *cover wrap* (the whole cover, back to front, as one PDF) with a computed spine and an EAN-13 barcode, and the retail channel checklists." New: "It holds a print-profile interior, a *cover wrap*, and the retail channel checklists. The cover wrap is the whole cover, back to front, as one PDF, with a computed spine and an EAN-13 barcode."
22. L274, S2. Old: "That directory holds the rendered pandoc defaults, the generated subject index, the front matter as TeX, the jargon report, and the page images that `press render` draws at 160 dpi." New: "That directory holds the rendered pandoc defaults, the generated subject index, the front matter as TeX, and the jargon report. It also holds the page images that `press render` draws at 160 dpi."
23. L276/278, S13 (ratchet lead, 7 sentences). The sentinel paragraph split at its turn of topic: sentinels (3 sentences) and the page floor plus the release floor (4 sentences). No words changed.
24. L282, S1/S10. Old: "A *floating tag* such as `v3` moves forward within its major as new releases come out, and an *immutable tag* such as `v3.0.2` names one release forever." New: "A *floating tag* such as `v3` moves forward within its major as new releases appear. An *immutable tag* such as `v3.0.2` names one release forever."
25. L285 (Tip), S2. Old: "When a book must rebuild from the same press and toolchain years from now, pin a three-part tag such as `v3.0.2` and move that pin on purpose." New: "When a book must rebuild from the same press and toolchain years from now, pin a three-part tag such as `v3.0.2`. Move that pin on purpose."

## Leads declined

- Ratchet L28 (31 words, "One `press all` produces..."): a verbatim blockquote of the press README. Never mode (quotation).
- Ratchet L30 (37 words, L31 "The program is a Python package..."): splitter artifact. The counter does not split after "name.[^1-name]" because a footnote label follows the period. The real sentences are 15 and 19 words.
- Ratchet L32 (37 words, L33 "You will meet..."): splitter artifact. The counter does not split before a sentence that opens with "@fig:". Real sentences: 17 and 20 words.
- Ratchet L46 (31 words, L47 "The press itself needs Python 3.10 or later. @fig:the-stack..."): same "@fig:" artifact. Real sentences: 8 and 23 words.
- Ratchet L119 (31 words, L123 "It assumes that you already installed..."): same "@fig:" artifact. Real sentences: 18 and 13 words.
- Ratchet L54 "editing" (L55 "never by editing the press"): a gerund after "by", a noun use, not a verb form or a chain. A rewrite ("never by an edit to the press") reads worse and says nothing more clearly.
- Ratchet L70 and L86 ("Facts are stated once", "Artifacts are verified as objects"): headings, and the names of laws quoted from *ARCHITECTURE.md*. Never mode.
- Ratchet L74 ("facts are stated once and projected mechanically", L75): the ROADMAP's own wording of the law (ROADMAP.md line 149, verbatim). Kept.
- Ratchet L92, both findings (sidebar "The cover that passed at 11.5 percent"): Light mode. The 34-word "sentence" is the bold title run into the first sentence (the title has no period); the real first sentence is 27 words, one idea, no semicolon. The 11-sentence paragraph is the sidebar counted as one paragraph; S13 is not a Light-mode fix, and `press check` passes it under the 190-word limit.

## Passives kept

- L75 "facts are stated once and projected mechanically": quoted law wording (above).
- L63 "*Make Ready* was "taken end to end through the built-in facilities"": inside a quotation.
- L89, L91: passives inside double-quoted quotations from the press documents.
No other passive kept in the book's own prose.

## Fidelity notes

- Sentinels: "On a fresh scaffold it succeeds" (L148) untouched. The other two sentinels do not occur in this file.
- Edit 2 replaces the pronoun "it" with its referent, LuaLaTeX, which the previous sentence named.
- Edit 4 names the press as the actor that runs epubcheck, on the authority of Table 1.2 in this chapter.
- Edit 25 drops the joining "and". "Move that pin on purpose" keeps the original's sense (move it deliberately) without implying a sequence.
- No fence, heading, image line, art comment, footnote label, or code span changed.
