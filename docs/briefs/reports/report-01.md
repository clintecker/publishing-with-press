# Report: Chapter 1, Introduction

Status: DONE_WITH_CONCERNS

## Word count

`press wordcount`: 5,353 for `book/chapters/01-introduction.md` (target
5,000, within 15 percent). The count includes the three `art:` directives,
the frontispiece directive, and the tables, because wordcount does not strip
HTML comments. Prose alone is roughly 4,500 words.

## Figures

- Figure 1.1 `@fig:pipeline-overview` (pipeline): two manuscript file icons,
  press check, pandoc + Lua filters, fork into latexmk/LuaLaTeX to
  alice.pdf and pandoc writers to five edition icons, a "stitch" arrow
  straight to alice.md, all converging on a drop-shadowed "verifiers" box,
  then dist/.
- Figure 1.2 `@fig:the-stack` (stack): six bands bottom to top, OS, Python
  3.10 or later, pandoc, TeX Live and LuaLaTeX, press, your book (shadowed),
  with a bracket marking pandoc and TeX as "the toolchain".
- Figure 1.3 `@fig:ten-minute-tour` (filmstrip): three boxed 72-column
  terminal panels: press new alice / cd alice; the captured press check
  output (note lines elided as "..."); ls dist/ with the two-line listing.

Plate: frontispiece lines untouched.

## Facts I needed and could not find (left out or flagged)

- No captured output for `press new` or for `ls dist/`. The `ls dist/`
  listing in Example 1.2 and Figure 1.3 is constructed from the registry
  layout in facts section 3.5 (slug alice, without the authorities
  companion). The managing editor should replace it with a real capture.
- Whether `press all` itself writes `dist/pages/`: README says it does, but
  QUICKSTART runs `press pages` after `ls dist/`. I listed `pages` in the
  listing and kept the QUICKSTART's `press pages` step.
- Contradiction A26 (source zip and git): I moved `git init` and a commit
  before `press all` (as README's quick start does) instead of claiming the
  source zip needs it. The prose says only that the Source edition holds
  files Git tracks.
- `press new` output and what CI does on push were not in the fact file, so
  the tour defers CI to Chapter 14.

## Places the fact file contradicted itself or needed adapting

- The captured `press check` output contains a non-ASCII ellipsis
  (`/…/src/press/...`) and lines over 72 columns. The chapter shows only the
  first line in a session fragment and explains all four lines in Table 1.1;
  the full text (ellipsis as three periods) is in the Figure 1.3 directive.
- The README sentence with "6 x 9" is stale per A1; I quoted it and noted
  six profiles since v2. The 6.3in cap is given as per-profile (A5).
- The design-contract and four-laws quotes contain semicolons and em dashes;
  I quoted only the dash- and semicolon-free parts and paraphrased the rest.
- design.md row asks for the pinned contract "in one paragraph"; the brief
  gives it an A-head. I followed the brief at five paragraphs plus a table.

## Checker residuals and defence

`press check` reports no error naming this file (it fails on paragraph
length in chapters 02 and 03, other writers' files). Note: press counts an
`art:` comment plus its image line, and a whole sidebar, as one paragraph;
I trimmed the directives and the sidebar (170 words) to stay under 190.

`ste_check.py` residuals, all defensible:

- Lines 3-4 (sentence length, semicolon, "landscape"): the frontispiece
  directive, which the brief says to leave exactly as it is.
- Lines 37, 42, 196 (paragraph length, semicolons, long sentences): the
  three `art:` directives; they are illustrator briefs, not prose.
- Lines 25, 83-85, 96, 263 (passives, long sentences): verbatim quotations
  of the README, the third law, CONTRIBUTING.md, and the press repository.
- Lines 67, 69, 71: B-heads that quote the law names verbatim.
- Remaining sentence-length flags of 24-31: the checker merges a sentence
  with the following footnote or quote, or counts list items inside a
  sentence; no prose sentence is over 30 words by my count. Prose average is
  about 16 words per sentence.
- ing-form flags are heading gerunds and words such as "including".
- "verify", "whether", "therefore", "attempt": period-correct per the prose
  contract's 80 percent rule.

## Revision (after the four desks)

Word count after revision: 5,066 (`press wordcount`). `press check`: no
error names this file (the run fails on a rewrite-status term in
`05-figures-and-plates.md`); the only diagnostic for this file is an
`inspect` note on "spine", used literally for the cover wrap.

### Coordinator rulings

1. Fact file S1 to S5 used: real `ls dist/` (Example 1.3, one entry per
   line), `press all` builds pages (the `press pages` step is gone; the
   target is mentioned only as the one that rebuilds the bundle alone),
   S3's summary lines as Example 1.2 with Table 1.1 explaining them, S4 for
   the slug, toolchain, image name, `verify-sentinels`, and checker rules,
   S5 for the drop cap. Applied.
   Concern: the ruling says the glyph law exempts code. It does: `press check`
   passed the code block with the pilcrow, check mark, middle dot, and arrow.
   It refused them in Table 1.1's first column, so the table names each line
   by its words (`check`, `typeset`, `verify`) and leaves the glyphs out.
   Example 1.2 is framed as a run on the press's gallery Alice example
   (three chapters and an appendix), because S3 shows that run and not the
   one-preface scaffold.
2. O1 and O2: the orientation now gives the payoff (a directory of chapters
   in, every edition out, no TeX, every file opened and checked); "What press
   is" opens with the README's first sentence, then its second (elided at
   the semicolon); the lowercase name and the pilcrow moved to a footnote;
   design profiles reduced to two sentences and a pointer to Chapter 9.
   Applied.
3. pandoc, Lua filter (italic term), LuaLaTeX, latexmk, poppler and
   `pdftoppm` each get a one-clause gloss at first mention. Applied.
4. Cut `INV-graph-no-stale`, the trust-tier paragraph and its footnote, and
   the grep warning. "Versions" is one paragraph plus the tip; Table 1.3,
   the migrate paragraph, the CI install paragraph, and the Pillow footnote
   are gone. "Where it came from" lost the commit hash, commit count, tag
   footnote, CHANGELOG quote, and the scaffold-neutrality paragraph. Applied.
5. All three `art:` comments now follow their image lines. Figure 1.3 is a
   vertical stack. Applied. Panel 3 is eleven lines (the real `ls`), above
   the typesetter's eight to nine; the directive says each panel is only as
   tall as its lines.
6. One name per thing: Manuscript edition (the copyeditor's choice and the
   registry's name; defined in italic at first use), design profile, the
   desk (defined), selftest; American spellings (color, e-books, labeled,
   centered, homemade); "ships" became "carries"; edition, artifact,
   manuscript, scar, registry, Lua filter, watchlist, known-bad fixture,
   plate, cover wrap, design profile all defined in italic before use.
   Applied.
7. No sentence opens with bare lowercase "press"; each is recast as "The
   press ...". Sentences that open with a command in code (`press check`,
   `press all`) are left as they are, since they name the command.
8. Chapter 10, Chapter 14, Appendix D, and Appendix E carry their titles.
   Applied.
9. Table 1.2 separators lengthened (Artifact column 32 dashes); Table 1.1 now
   explains only lines Example 1.2 shows. Applied.
10. Art plus image: 186, 139, 161 words. Sidebar: 155 words with title. Every
    paragraph is six sentences or fewer. Applied.
11. "the dist directory" and "the build directory" now appear in prose.
    Applied.

### Fact desk

Unsupported 1 to 6, 11: now supported by S4/S5 and applied as worded there
(the drop cap is opt-in, house default none). 7: applied. 8: cut. 9: cut.
10: CI install paragraph cut; tags reworded without the GitHub Actions
convention. 12: `target` kept (the book's controlled vocabulary); pandoc
writers kept (S3 shows each pandoc call); the ROADMAP sentence is gone.
Contradicted 1, 2: applied. Drifted 1, 3, 5 to 8, 10, 11: applied; 2, 4, 9:
moot after cuts. Missing 1 to 4: applied (Example 1.2, the `press all`
sequence, print pack not built by `press all`, the default of 40).

### Developmental desk

O1, O2, O3, P1 to P9, R1 to R3, N1: applied. P4 resolved by moving the
table to the `press all` lines the session shows; the `press check`
fragment shows two lines and the prose names the two it elides.

### Copy desk

Items 1 to 43 applied or moot after cuts (10, 14, 18, 19, 22, 37, 38 went
with cut text). Mays: 44 resolved by ruling 7; 45 applied (footnote moved
to the name); 46 applied (selftest); 47 to 57 applied; 58 applied (two
understatements cut); 59 moot. Fact queries 60 to 65 moot or resolved by
the fact desk.

### Type desk

1 to 5 and the index note: applied.

### Residual ste_check findings

Unchanged in kind from the first report: the frontispiece directive, the
three `art:` directives, quoted passives in the four laws and the sidebar,
and splitter merges at footnote markers. None is a prose semicolon or a
passive in my own sentences.

## Revision 2 (scoped re-review)

- B1: `tools/space-art-comments.py` inserted 4 blank lines, one between each
  image line and its `art:` comment, frontispiece included. The plate's two
  lines are unchanged. Applied.
- S1: `tools/tag-fences.py` tagged 6 fences `text`. Applied.
- S2: the description value is now "A girl falls into Wonderland.", and
  `git remote add` breaks with a trailing backslash. No line in a code
  block is over 64 columns. Applied.
- S3: Table 1.1's `typeset` row now names "the Single-leaf and Chapter
  editions". Applied.
- S4: line 19 glosses TeX as "the typesetting language behind the print
  PDF". Applied.

`press check`: no error in this file (the only note is an `inspect` on
"spine", used literally). The run still fails on the rewrite term
"authoritative" in `05-figures-and-plates.md`. `press figures` shows an
`art` description for the frontispiece plate and all three numbered
figures. `press wordcount`: 5,075.

## Revision 3 (continuity)

Applied all of it: the reusable workflow, *build.yml*, named at the push step; "the manuscript" in the sentinel sentence; the Libertinus fonts (the footnote now says TeX Live carries Libertinus); Figure 1.2 bracket labels the whole toolchain; Table 1.1 glosses the Single-leaf and Chapter editions in its cell; Appendix A gives "every command"; *alice-sources.md* is the sources companion, and the table of authorities is the ledger in *config/authorities.yaml*; footnote labels prefixed `1-`. `press check`: nothing names this file. Word count 5,099.

## Revision 4

Example 1.1 and the Figure 1.3 brief now run `press new alice --owner wonderland-press`, and the scaffolding paragraph says `--owner` fills in the `repository` and `site-url` lines (no prose had said they stay commented). The description stays "A girl falls into Wonderland." `press check` passes. Word count 5119.
