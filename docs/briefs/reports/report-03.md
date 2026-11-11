# Report: Chapter 3, The shape of a book repository

File: `book/chapters/03-the-shape-of-a-book.md`. Not committed.

## Word count

`press wordcount`: 6,056 (target 6,000; window 5,100 to 6,900). The count
includes tables, captions, and the three `art:` directives.

## Checks

- `press check` from the repository root: no error names this file. The
  run fails only on `book/chapters/02-installing-press.md` (three paragraphs
  over 190 words, another writer's file). I re-ran it on a scratch copy with
  those paragraphs split: all four passes went green, including the jargon pass.
- `ste_check.py`: residual findings, with my defence of each:
  - Line 6 and the tables: list and table rows join into long "sentences".
  - Lines 72, 361, 552 (sentence and paragraph length, semicolons): the
    `art:` directives. They are illustrator briefs, not prose.
  - Line 210 (46 words): two sentences around the `[^epubdate]` marker that
    the counter reads as one. They are 20 and 26 words.
  - Line 63 "were permanent" (subjunctive) and line 229 "are stated" (inside
    the quoted law "Facts are stated once."): neither is a passive in prose.
  - Lines 272 and 406 (semicolons): inside a verbatim refusal message and
    the verbatim `press add` stub text.
  - Line 599: the index comment, which needs semicolons.
  - Sentences of 24 to 29 words: all under the ceiling of 30.
  - "therefore" and "however": the prose contract allows both.
- Code lines over 72 columns: in the verbatim Makefile (`.PHONY` and the
  rule line), *metadata.yaml* comments (74), *requirements.txt* (76/74),
  the release refusal (86), and the captured `press check` line (136). I
  kept them verbatim as instructed, so the page will wrap them with a hook.
- Paragraphs: all under 190 by press's counter. Each figure's art comment,
  together with its image line, is under 190.

## Figures

- 3.1 `@fig:scaffold-tree` (tree): the exact `press new alice` tree, with
  italic leader annotations on *book.yml* (calls build.yml at v3),
  *metadata.yaml* (identity, press facts, verification knobs), and
  *book/chapters/* (your chapters go here). *metadata.yaml* has a 20% gray
  box so the reader sees it first.
- 3.2 `@fig:how-files-sort` (before/after): (a) 1-, 10-, 2- giving 1, 10,
  2; (b) 01-, 02-, 10-. In the second row, (c) `press add appendix` x-, y-,
  z- with the generated index at a-, and (d) `--front` a-, b- with the index
  at c-. The reader should see first that frame (a) puts 10 before 2.
- 3.3 `@fig:dist-after-all` (tree): *dist/* after `press all`. Each file
  carries its edition name, the optional files have dashed outlines, the
  eight editions sit on a gray band, and *pages/* has a gray box.

## Tables, examples, sidebar, admonitions, footnotes

Tables 3.1 to 3.6. Examples 3.1 to 3.12. The text refers to each one before
it appears.
Verbatim scaffold files: Makefile (Ex 3.8, tab kept), requirements.txt
(Ex 3.9), book.yml (Ex 3.12), the preface stub (Ex 3.2), and metadata.yaml
(Ex 3.3, slug alice).
Sidebar (184 words): why CI does not install press from git. There are
four tips and four warnings, and three footnotes.

## Facts I needed and could not find (left out)

- The verbatim commented commerce block at the end of *metadata.yaml*. The
  fact file elides it, so Example 3.3 ends in `...` and the prose names it.
  This also keeps the "press qualify" comment out of the chapter.
- What `press add` prints, so Example 3.7 shows the commands and then an
  `ls -1` of the two directories (derived from the documented naming rules).
- The output format of `press config get`, and what `--dry-run` and
  `--file` do. I left all three out.
- The exact line layout of `.gitignore`. The chapter names its four entries
  only in prose.
- A captured `press new` run with `--author`/`--owner`. Example 3.3's
  author, publisher, repository, and site-url lines come from the
  documented substitution rules and not from a capture.
- The captured output used "…". I replaced it with "..." (glyph law), and
  the `press new` path appears as `/.../alice`.

## Places the fact file contradicts itself

- Index position. 3.2 gives the merge order as "chapters, then appendices,
  then the generated subject index", yet 3.2 and section 20 A.7 say the
  index "usually sorts *before* authored back matter". The chapter states
  the merge order, the letters (index takes the first free letter from a,
  never z, and `press add` counts down from z), and that *a-* sorts ahead
  by filename. It never claims where the index lands in the reading order.
- Git and the Source edition: A.26 calls the need for `git init` an
  inference. The chapter says only that the Source edition holds the files
  git tracks, so an untracked file is missing from it. It never says that
  `press all` fails without git.
- Stale verification: scar 8 says the dependency edges make it impossible,
  while B.11 says `verify-formats` can include a stale PDF. The warning tells
  the reader to run `press all` and makes no absolute claim.

## Other notes

- The Alice sentinels ("Twinkle, twinkle, little bat", "she made some
  tarts") are quotations from the novel's chapters 7 and 11. They do not
  come from the fact file.
- `raised-cap` is listed as an accepted value only. The chapter does not
  describe how it looks (B.7).
