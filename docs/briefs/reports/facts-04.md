# Fact check: Chapter 4, Writing the manuscript

I checked `book/chapters/04-writing-the-manuscript.md` against `docs/briefs/facts/facts-04.md`: sections 4.1 to 4.9 and 3.2, plus the Shared context (1.4, 19, 20). Line numbers refer to the chapter. The managing editor's ruling also applies: Chapter 6, *Checking the manuscript*, introduces sentinels, and Chapter 8 proves them.

**Captured output.** The chapter has no captured multi-line output. The `$ press check` session (lines 235 to 238) is fully elided. Examples 4.1 and 4.3 to 4.9 are inputs, not captures. Every checker message the chapter quotes matches the file character for character: `manual number in heading`, `title-case heading:` plus the text, `glyph U+XXXX is outside the print-font set`, `paragraph N has W words (the law is under 190; split it)`, and `<file>:<line>: <label>`. I scanned the prose mechanically. Outside fenced code there is no character beyond the glyph law and no trailing whitespace. The forbidden characters appear only inside Example 4.2's fence.

**Cross-references.** The chapter titles cited (5, 6, 8, 9, 10) match the current chapter headings.

## 1. Unsupported

1. **Footnote labels unique "within its chapter file."** Line 181: "A label must be unique within its chapter file." I searched for unique, label, footnote, and duplicate, and found nothing. The file says the chapters are merged into one manuscript ("Merge order is chapters, then appendices, then the generated subject index", 3.2) and calls the Markdown edition "raw stitched source" (20.B.9). On that reading a label must be unique across the whole book, so the sentence is probably wrong as well as unsupported. Fix: cut it. Or, if the editor confirms, write "A label must be unique in the whole book, because press merges the chapter files before pandoc reads them."
2. **Claims about what the Alice example contains.** I searched for Alice. The file says only that "The Alice example uses [cascade] for 'Alice's Right Foot, Esq.'" and that `tail` "exists for the Mouse's Tale in Alice". The file does not support the following:
   - Line 18: "the sample book that ships with press".
   - Line 47: "In the PDF of the Alice example, the first section of the second chapter prints as 2.1, and its first subsection prints as 2.1.1." Nothing says the example has sections or subsections at all.
   - Line 55: "The Alice example holds the first three chapters of Carroll's book."
   - Line 248, and the title of Example 4.5: "The Alice example sets a three-line drop cap with small caps for the rest of the first word."
   - Line 285: "The second chapter of the Alice example opens with speech". This is true of Carroll; the file does not say it of the example.
   - Line 317, and the title of Example 4.6: "The Alice example uses `fairy-dust`". The file says only that fairy dust is "Tenniel's 1866 staggered array".
   - Line 210: "a small table drawn from the first two chapters of the Alice example".

   Fix: either have the editor confirm these against the example's `config/metadata.yaml`, `config/aesthetic.yaml`, and chapter files, or recast them as hypotheticals: "A book that sets a three-line drop cap ...", "A book set in Tenniel's manner might choose `fairy-dust`".
3. **"before any build begins."** Line 99: "The checker refuses such a character before any build begins." I searched for check, build, and dependency. The file never says that builds run the checker first. 20.A.10 says the known-bad fixtures run "in `press check` and `press all`, not in a bare `press pdf`", which suggests a bare build target need not check at all. Fix: "`press check` refuses such a character."
4. **`press config set chapter-opening.style drop-cap`.** Lines 260 to 264: "You can set them from the command line, which checks each value before it writes the file". Searched: config set, and config. Neither the command, nor its dotted-key form, nor its validation appears in facts-04. The writer says it comes from facts-03/B, a file this desk does not have. Fix: confirm it against facts-03 or a captured session. Otherwise cut it, and keep Example 4.5's YAML.
5. **Minor glosses not in the file.** These are low stakes. Soften them, or accept them as general knowledge; the editor decides.
   - Line 71: "because pandoc would print the number a second time beside its own". Line 38 makes the same claim: "a number you type yourself prints twice". The file gives the refusal but no reason for it. Fix: "because pandoc numbers the heading itself".
   - Line 243, the tip: "Keep code lines to 72 characters or fewer." I found no 72-character rule in the file. If it is house style for this book, that is fine. It is not a press rule.
   - Line 223: "with each cell set under its column's name". The file says only "the reader CSS turns each row into a card".
   - Line 381: "where t is the line's position along the tail". The file gives only `3.0em·sin(t·2π)` and does not define t.
   - Line 368, Example 4.8: "the start of the Lobster's song". In Carroll it is a poem Alice recites, "'Tis the voice of the Lobster", and the Lobster does not sing it. Fix: "the start of 'Tis the voice of the Lobster".

## 2. Contradicted

1. **Sentinels sent to the wrong chapter.** Line 206: "Chapter 10 covers the index and the authorities, and Chapter 8, *Verifying the artifacts*, covers sentinels." The managing editor's ruling is that Chapter 6, *Checking the manuscript*, introduces sentinels and Chapter 8 proves them. The fact file also places sentinels in "§3.3 and §6" (4.8), not only with verification. The chapter sends the reader only to Chapter 8 and skips the chapter that introduces them. Fix: "Chapter 6, *Checking the manuscript*, introduces sentinels, and Chapter 8, *Verifying the artifacts*, proves them in the finished PDF."
2. **"every edition" includes the Markdown edition, which gets no filters and no smart typography.** The fact file says in 4.3, in bold: "**The Markdown edition gets the raw `:::` source**, because no Lua filter runs on it". 20.B.9 says: "The Markdown edition is raw stitched source." Three claims in the chapter run into this:
   - Line 405: `typographic-spacing.lua` "runs in every edition". This repeats 4.7 ("in every edition"), but 4.3 and B.9 contradict it, because no Lua filter runs on the Markdown edition.
   - Line 140: "You type straight quotes and apostrophes, and pandoc curls them in every edition." Raw source keeps its straight quotes.
   - Line 22: "A chapter that renders one way in the PDF therefore reads the same way in the EPUB and on the Web." This overstates the case. Placement is "print-only" (4.2), `ornate` degrades on the web (4.5), and the txt and docx editions have no drop cap or ornament (4.4, 4.5).

   Fix: line 405, "which runs in every edition built through pandoc (the Markdown edition is the raw manuscript, and no filter touches it)". Line 140, "pandoc curls them in the typeset editions". Line 22, "Pandoc parses a chapter the same way for every edition."

## 3. Drifted

1. **The reference forms are listed incompletely, but as if complete.** Line 407 gives "p., pp., No., Nos., Fig., Figs., Ch., Vol., Pt., and Eq." The file's list, 4.7, ends "Pt., Eq., §, ¶". The writer left out the two signs deliberately, because the glyph law forbids them in prose (report-04). That is sound, but the sentence reads as exhaustive. Fix: add "and two signs the glyph law keeps out of your prose anyway, § and ¶". Or write "for reference forms such as".
2. **Exactly 190 words.** Line 161: "A paragraph of 190 words or more fails `press check`." The file says both "must be under 190 words" and "Over 190 gives an error". Exactly 190 is ambiguous in the file. Fix: keep the file's law, "must be under 190 words", and drop "190 words or more". Alternatively, have the editor confirm the boundary.
3. **The reason a short heading passes.** Line 84: "`# Down the Rabbit-Hole` has too few candidates left". The file does not list the 21 small words, and it does not say how a hyphenated word is counted. The heading passes either way: with fewer than three candidates it is exempt, and with three candidates two of three is 67 percent, under the line. The stated reason, though, is a guess. Fix: "has too few candidates, or too few capitals among them, so it passes."
4. **Two digits.** Line 49: "Press pads the numbers it hands out to two digits". The file says "zero-padded to at least two digits". Fix: "to at least two digits".
5. **The source of "Bringhurst's rule."** Footnote `[^hung-quote]`: "The press's notes call this Bringhurst's rule." The file gives "(Bringhurst's rule)" in 4.5 and attributes no notes. "The maintainer's notes" are the source only for the sentinel scar. Fix: "Press calls this Bringhurst's rule."
6. **The Lua test footnote.** Footnote `[^ties]`: "It also found that the Lua tests skipped silently in CI". War story 21 says the backfill found the vacuous test, "and the Lua tests had been silently skipping in CI until `PRESS_REQUIRE_LUA=1`". It does not say that the backfill found the skipping. Fix: "The Lua tests, it turned out, had also been skipping silently in CI until CI set `PRESS_REQUIRE_LUA=1`."
7. **The no-break space in Example 4.2.** Line 118 labels its row "(invisible)", but the row holds plain spaces and no U+00A0. Keeping the character out is the right call. The label implies the character is there, though. Fix: "(not shown)".

## 4. Missing

1. **The Markdown edition's set pieces** (4.3, in bold): "The Markdown edition gets the raw `:::` source". Line 401 says what the plain-text and DOCX editions do but is silent on Markdown. A reader who opens that edition will find `::: verse` lying in the text. This also supports Contradicted 2. State it as a fact, not as a feature (20.B.9).
2. **What txt and docx do with drop caps and scene breaks** (4.4: "The txt and docx editions keep a plain rule"; 4.5: "Formats without drop caps: txt and docx"). The writer left these out by citing B.10. B.10 forbids presenting them as features, not stating them. One sentence in each section would do.
3. **`raised-cap`** (4.5): "accepted but renders the same as `drop-cap`". Table 4.3 lists three styles. A reader who meets `raised-cap` in another book's config, or in validation output, has no explanation for it. If it is mentioned, state it flatly as an accepted value with no effect of its own (20.B.7).
4. **Appendix letters and the index's position** (3.2; 20.A.7). Line 49 explains appendix filenames and the merge order. It does not say that `press add appendix` counts down from `z-`, or that the generated index takes the first free letter from `a` and so "usually sorts *before* authored back matter". A reader who follows line 49 might expect the index last. This may belong to Chapter 10. If so, point the reader there.

## Notes for the editor (not counted)

- **Where the `art:` comments sit.** File 4.2: the comment "may sit on the next line or after one blank line" after the image (`figures.py:93-99`). For all three diagrams (lines 42, 319, and 336) the comment comes *before* the image line, following `docs/markup.md` (report-04, Contradictions). By the file's rule, `press figures` would not attach those comments to their figures. The plate at line 94 is placed correctly. This is not a prose claim, but the art department reads `press figures`, so the editor should resolve the conflict between markup.md and `figures.py`.
- **report-04 numbers the figures wrongly.** It gives 4.2 as set-pieces and 4.3 as scene-break ornaments. In the file, the scene-break figure (line 320) comes before set-pieces (line 337), so scene breaks are Figure 4.2 and set pieces Figure 4.3. The chapter's prose cites both by `@fig:` and states no number, so the chapter itself is correct.
