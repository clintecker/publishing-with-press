# STE80 review: book/chapters/01-introduction.md

Status: REVISE. Blocks: 0. Should: 2.

Diff reviewed: `git diff HEAD -- book/chapters/01-introduction.md`, 14
hunks covering the editor's 25 listed edits. The sentinel "On a fresh
scaffold it succeeds" is byte-identical: line 148 now (146 at HEAD), with
the 80 characters before and 40 after identical in both versions. The other
two sentinels do not occur in this file. No code span, command, path, URL,
flag, YAML key, number, version, quotation, footnote label, art comment, or
italic term changed. `press check` exits 0. `tools/ste-ratchet.py --report`
counts 9 findings for this file (the editor's report says 11). Either way
the count is under the baseline of 14. No paragraph grew past 190 words, no
blockquote was split, and no Light-mode passage was touched (the sidebar at
line 92 and the *Make Ready* anecdote are unchanged).

Edits judged sound, including the three the editor flagged:

- Edit 4 (line 45): "The press runs epubcheck, the validator that retail
  channels run, over the EPUB." The actor matches Table 1.2 ("The press runs
  epubcheck over it.") and the epubcheck scar in facts-01. The old sentence was just as
  unconditional, so the strength did not change. The local exception
  ("structurally only", line 202) is still stated where it was. Edit 3
  ("leaves out" to "omits") on the same line is sound.
- Edit 16 (Warning move): the Warning is unchanged and now comes before
  "run `press all`", which is the tour's first LuaLaTeX run (`press check`
  does not run LuaLaTeX). This satisfies S14. Line 240 ("the font scan in
  the warning earlier in this section") sits under "Publishing the book",
  so "this section" means "A ten-minute tour". It was true before the move
  and is still true. The understatement ("a very convincing imitation of
  one") is intact.
- Edit 8, "`press check`, which refuses an em dash, is a checker": the
  example now names the target rather than the act. The second law's
  ranking still reads the same, and `press check` is a checker.

Findings:

1. **Line 43, edit 2. Unclear referent for a definition.**
   Old: "Then latexmk, a program that reruns LaTeX until the page references
   and the lists stop changing, drives it through as many passes as the book
   needs."
   New: "Then latexmk drives LuaLaTeX through as many passes as the book
   needs. That program reruns LaTeX until the page references and the lists
   stop changing."
   Replacing "it" with "LuaLaTeX" is correct (facts-01 scar 4). However, the
   nearest program before "That program" is now LuaLaTeX, so a reader can
   take the rerun behaviour to belong to LuaLaTeX instead of latexmk. That
   would misattribute the convergence fact.
   Severity: should.
   Corrected: "Then latexmk drives LuaLaTeX through as many passes as the
   book needs. Latexmk is a program that reruns LaTeX until the page
   references and the lists stop changing."

2. **Line 285 (Tip), edit 25. Split turns a manner clause into a bare
   command.**
   Old: "When a book must rebuild from the same press and toolchain years
   from now, pin a three-part tag such as `v3.0.2` and move that pin on
   purpose."
   New: "When a book must rebuild from the same press and toolchain years
   from now, pin a three-part tag such as `v3.0.2`. Move that pin on
   purpose."
   In the old sentence, "and move that pin on purpose" was governed by the
   condition and read as "move it only deliberately". This contrasts with
   `v3`, which moves by itself. As its own sentence, "Move that pin on
   purpose." reads as an instruction to move the pin, which is the opposite
   of the advice. The old sentence was 27 words with the condition first and
   two linked actions joined by "and". The contract permits that, so the
   split was not needed.
   Severity: should.
   Corrected: restore the old sentence: "When a book must rebuild from the
   same press and toolchain years from now, pin a three-part tag such as
   `v3.0.2` and move that pin on purpose."
