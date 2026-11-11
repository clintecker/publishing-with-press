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

## Revision (after the four desks)

Word count: `press wordcount` gives 6,731, inside the 5,100 to 6,900 window.
Prose alone is about 5,230 words (78 percent). The rest is tables 820, art
directives 410, image lines 170, and captions 95. Every code line is now at
most 64 columns, and every directive plus its image line is under 190
words. The sidebar is 164 words.

Checks:
- `press check`: the source, self-test, and editorial passes are green. The
  jargon pass fails on `05-figures-and-plates.md` ("authoritative"), which is
  another writer's file. Its only note on this file is an inspect-level
  "spine" in Table 3.5, the literal book spine.
- `ste_check`: the residuals are the same kinds as before. They are lists,
  the in-this-chapter box, art comments, the index comment, quoted messages,
  "therefore"/"however", a subjunctive, and the quoted "Facts are stated
  once". There is no prose sentence over 30 words and no prose semicolon.

Rulings:
1. Applied. Example 3.6 is the S1 capture. Its `cat` line is cut with
   `...`, and the full placeholder text appears in prose. Example 3.2 ends
   with the commerce block. The prose glosses "press qualify" (no such
   command, so the qualification is recorded by hand) and gives
   seller-of-record as press's provider-as-seller model, which the
   publisher must confirm.
2. Applied, with every code line at 64 columns or fewer.
   - The Makefile, requirements.txt, refusal message, `press new` output,
     and the commerce lines are cut with ` ...`, and the prose says what
     was cut.
   - The commerce block's opening comment is rewrapped at 64 columns, and
     the prose says so.
   - The preface stub moved into a prose quotation, which also removed an
     example.
   - The `--json`, `wonderland-press`, and `git remote` lines are broken
     with a trailing backslash.
   - The typesetter offered a reworded Makefile comment and a merged
     requirements comment. I declined both because they were not verbatim
     and truncated the original lines instead.
3. Applied.
   - `cd alice` closes Example 3.1, and Example 3.10 drops its own `cd`.
   - The sentinels and `verify-min-pages 24` are now shown as what `alice`
     sets later, with the reason.
   - "A first local build" shows `press all` (from facts-01 S3, with the
     slug `alice`) and `ls dist/` (from S1). The capture's four files match
     the Alice state at that point.
   - The font-scan paragraph sits beside the run.
4. Applied.
   - "Book model" is defined, with a pointer to Chapter 16.
   - `press config get` has a shown session. Its outputs (the raw string,
     JSON for a list, and `subtitle: not set`) come from reading
     `config_cli.py` and are not a capture. The claim that each `set`
     prints the change and that `--dry-run` writes nothing has the same
     source.
   - Tables 3.3 and 3.4 gained a Default column. I folded the Type column
     into Meaning to keep three columns.
5. Applied. All three directives now follow their image lines. Figure 3.1
   has 13 rows, with `.claude/workflows/ (four files)` collapsed to one.
   Figure 3.3 has 12 rows, with `pages/ (see Chapter 14)` collapsed to one.
   Figure 3.2 uses the prose filenames and the real index filename, and
   draws S1's y-glossary/z-about-the-author.
6. Applied: manuscript (not "source"), artifact (not "output"/"build"),
   "run" (not "call"), "the reusable workflow", "includes"/"comes with" in
   place of "ships", "release witnesses", and "acknowledgments" in prose.
7. Applied. The skip-file Warning now opens with an instruction, and I cut
   the git Tip. That leaves 3 tips and 4 warnings.
8. Applied (176, 183, and 178 words with image lines; the sidebar is 164).
9. Applied (see the word count above).

Facts desk:
- Unsupported 1 to 7 applied. Unsupported 8 applied: Example 3.4 is now
  introduced as commands, and the prose says each `set` prints a change,
  which the example leaves out.
- Contradicted 1 to 3 applied.
- Drifted 1 to 9 applied. Drifted 2 follows the S3 wording.
- Missing 1 to 5 applied:
  - the common first-run refusals and the CI "Initialize containers" retry;
  - the publish checklists, with "in a book without print ordering" as the
    hedge;
  - the CLAUDE.md house laws.

Developmental desk:
- C1, C2, and P1 to P7 applied. C3 is resolved by weakening the forward
  pointer to "what the Source edition needs from git", with no claim about
  building without a repository. P5 adds a line telling the reader to
  create the empty GitHub repository first. I did not add a branch step.
- R1 applied: the build directory is now prose that pairs each failure
  with the file to read.
- R2, R3 (the Python block is cut, and the globs appear inline), and R4
  (the INV paragraph is cut, the printf footnote is kept, and
  `INV-graph-no-stale` is dropped) applied.
- N1 applied.
- The two closing turns are revised. "readers will see them" replaces the
  joke, and the font scan ends "Let it finish."

Copy desk: items 1 to 28 applied.
- Item 5 follows the fact desk's "each of them is optional" instead of the
  copyeditor's wording, which claimed that the files degrade gracefully.
- Item 25: "The first eight files ... are the editions".
- Item 28: `press art commission`.

Copy desk, the "may" items (29 to 50): all applied except two.
- Item 49 is half applied. The B-head "Files `press all` does not make"
  now uses code type. I declined to change the A-head "Where things go:
  build and dist", because the brief fixes its wording and the
  In-this-chapter box must match it.
- Item 33 is applied as written.
- Item 50 is applied to Tables 3.1 to 3.5: every cell in the Meaning
  column is now a sentence.
- The typesetter's Git nit is applied. "Git" is capitalized in prose as
  the program name (markup.md). It stays lowercase in commands and in the
  mandated A-head "What git has to do with it"

Typesetter:
- Blocks 1 to 7 applied, as described under ruling 2.
- S3 and S4 applied by widening the separators.
- S5 applied by splitting the remote URL onto its own line.
- S6 applied, because the Python block is gone.
- S7 applied, as described under ruling 5.
- S1 and S2 (page splits and the stranded sidebar title) cannot be fixed
  from the source. Recheck them in the final build, once the figures
  exist.

## Revision 2 (scoped re-review)

`press wordcount` is 6,774. `press check` passes the source, self-test,
and editorial checks. The jargon check fails only on
`05-figures-and-plates.md` ("authoritative"), and the one note on this file
is the inspect-level "spine". `ste_check` leaves the same residual kinds as
before. No prose sentence is over 30 words, and there is no prose
semicolon. Every code line is 64 columns or fewer, and no line has
trailing whitespace.

- B-1, applied. `tools/space-art-comments.py` inserted a blank line
  between each image line and its `art:` comment (3 lines).
- B-2, applied.
  - Example 3.10 is captioned "press all on the gallery Alice, in part",
    and the prose names it as the press's own gallery example (a
    three-chapter Alice with one appendix), with the slug changed to
    `alice`.
  - The four-files sentence now reads "its three chapters and its
    appendix".
  - From S5, the prose says the build needs no Git and can run before
    `git init`. The Git section says that before `git init` the Source
    zip still builds and verifies but archives no files until Git tracks
    them.
- B-3, applied.
  - The invented `get` session is gone. Example 3.4 is now S4's capture:
    `get author`, `get subtitle`, `set subtitle` with its diff, `get`,
    `--dry-run` with its diff and "(dry run: nothing written)", and
    `unset` with its diff.
  - To stay at 64 columns, it cuts the end of one context line and the
    last three lines of the dry-run diff. The cut includes a whitespace-only
    context line that would trip the trailing-whitespace law. The prose
    discloses both cuts.
  - The prose quotes S4's wording on `get`, the diffs, and the dry run.
  - The identity commands moved to Example 3.5, which is now commands only,
    with its diffs left out and the subtitle line dropped. Examples 3.5 to
    3.11 became 3.6 to 3.12. Each one is still referenced before it appears.
- S-1, applied. `tools/tag-fences.py` tagged all 17 fences `text`.
- S-2 and S-3, applied through S4 (see B-3).
- S-4, applied. Each edition is glossed at first use:
  - "the Source edition (the source zip)";
  - "the Telegraphic edition (the plain text)";
  - "the Manuscript edition (the raw Markdown)".

  The later sentences in the dist section now lead with the edition name.
- S-5, applied. The box reads "What git has to do with it", matching the
  A-head. The B-head became "What Git gives the press".
- S-6, applied. The publish checklists now point to Chapter 12.
- The editor's points, not counted:
  - The validate prose now follows S4 (absent files report `ok`).
  - The wordcount block notes that the reader's own list now names the
    new files too.
  - The order of `press all` and `git init` is settled by S5.
  - `main` is left as it is.
- To stay inside the 15 percent window (the edit took the count to 6,900),
  I cut about 125 words of prose that carried no fact.
- Not mine: Copy 12 asks for a "vacuous witness" entry in
  `docs/vocabulary.md`. That entry is for the editor, because I touch only
  this chapter.

## Revision 3 (continuity)

Applied continuity items 5 to 9 and the description ruling.
- The press's own Alice example now has one name, "the press's own
  three-chapter Alice example", in both the prose and the caption of
  Example 3.10.
- *page floor* is defined at first use.
- The first line of Example 3.3 is folded, not cut, so it keeps "are
  vacuous:". The lead-in sentence was updated to match.
- `top-level-division` is limited to the PDF and the EPUB.
- "cross-repository token" replaces "cross-repo token".
- Example 3.5's description is now "A girl falls into Wonderland.", on one
  line.

Footnotes are prefixed `3-`, and every fence was already tagged. `press
check` is fully green, all four passes. `press wordcount` is 6,795.

## Revision 4 (Chapter 6 and 7 continuity)

- The sentinel refusals now quote the checker's `sentinel not found in the
  manuscript:` and the verifiers' `missing text sentinel in PDF:` and
  `<label> missing sentinel:`.
- The checker's passes now carry Chapter 6's names: the source checks, the
  checker self-test, the style audit, and the jargon lint.
- Table 3.3's `rights` row now has a clause for the EPUB exception, where
  the press sets its own `--metadata rights=` value.

`press check` is green on all four passes.
