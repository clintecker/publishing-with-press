# Production report

Production editor, 2026-11-11, against commit `7cbe8fe` (tree clean apart
from `build/` and `dist/`). Press checkout `~/code/press` at v3.0.2, toolchain
image from its `build.yml` pin.

**Verdict: red.** Three press targets fail in the toolchain image. Five blocks
findings and eight should findings, all fixable in the manuscript.

## 1. Build log summary

The docker build ran. The first run, `tools/docker-build.sh . build/docker all
verify-print coverwrap`, exited 1 inside `press all` and streamed no `dist/`
out, because the script's `set -e` stops at the first failing target. Log:
`build/docker-build.log`. The verifier's message is printed *above* the check
output there because stdout and stderr were buffered differently.

To get every target's result and the artifacts anyway, I ran the same image,
mounts, and lockfile install through a copy of the script that records each
target's exit code and keeps going
(`/private/tmp/.../scratchpad/dbuild.sh`, not committed). Log:
`build/docker-build-pertarget.log`. Artifacts: `build/docker/dist/`.

| Target | Result | Message (verbatim) |
|---|---|---|
| `press all` | **exit 1** | `ink touches rendered page edge: [36]` |
| `press verify-formats` | **exit 1** | `HTML lost the manuscript witness line: the first eight files in @fig:dist-after-all are the edition...` |
| (epubcheck, run by hand in the image because verify-formats stopped before it) | **would fail** | `Messages: 6 fatals / 19 errors / 0 warnings / 0 infos` |
| `press verify-print` | **exit 1** | `ink touches rendered page edge: [35, 353, 357]` |
| `press coverwrap` | exit 0 | `Verified publishing-with-press-coverwrap.pdf: one page, 13.210 x 9.250 in (384-page spine), embedded fonts, no transparency, images under 600 PPI, front art present, title survives, barcode: honest placeholder present` |

Inside `press all`, everything before the PDF verifier passed. The check
passed: source, self-test (29 fixtures), editorial, and jargon. Every edition
typeset, and the source zip archived 499 files. `verify_pages` passed with
"sentinels on the public reading surface".

- **Sentinels:** all three were found. The PDF verifier checks text sentinels
  before it renders pages, and it reached the render stage, so there was no
  sentinel miss. The pages verifier also found them.
- **Page floor:** the reading PDF has 385 pages and the interior has 384,
  against `verify-min-pages: 300`. No floor miss.
- **Page numbering:** in the reading PDF, PDF page = folio + 9. Below,
  "f." is the printed folio and "p." is the PDF page.
- **Native vs image:** the native `press render` (385 pages) differs from the
  image PDF on most pages (fonts and TeX versions differ). The page read below
  was done on the **image** PDF, rendered with `pdftoppm -r 160` to
  `build/rendered-docker/`. The native render in `build/rendered-book/` was used
  only for a first look at pp. 1–40. Only one native page touches the edge
  (p. 358 = f. 349); that is the same fault as B4b.

## 2. Blocks findings

**B1. Accidental subscript runs off the page: p. 36 (f. 27), interior p. 35.**
`book/chapters/02-installing-press.md:73` has two unescaped tildes on one line:
`*~/.press-venv*` … `*~/.press-venv/bin/press*`. Pandoc reads the text between
them as subscript (`<sub>/.press-venv` in the HTML). The run cannot break, so
it overruns the measure to the paper edge. Both the reading and print
verifiers die on it.
*Fix:* write the paths as code spans (`` `~/.press-venv` ``) or escape the
tildes (`\~`).

**B2. Manuscript witness missing from every edition but Markdown.**
The message is quoted above. The chosen witness is the longest markup-free
line, `book/chapters/03-the-shape-of-a-book.md:615`, and it contains the
cross-reference `@fig:dist-after-all`. In the HTML, EPUB, text, DOCX, and site
editions that reference renders as "Figure 3.3", so the line appears nowhere.
The site check fails the same way: `reader site is missing
03-the-shape-of-a-book.md: its witness line ... appears on no page`.
*Fix (book):* change "in @fig:dist-after-all" on line 615 to "in the figure",
or add any inline markup to the line (for example *dist/*) so it stops being
the witness. Line 607 already cites the figure.
*Note for the controller:* this is a press defect. `_manuscript_witness` and
`chapter_witnesses` do not reject lines with `@fig:` cross-references. Per the
brief, I made no change to press.

**B3. EPUB fails epubcheck: 6 fatals, 19 errors.** It is masked today by B2,
and it is the next red. Report from the image's epubcheck:
- *`--` inside HTML comments* (fatal RSC-016) in ch002, ch004, and ch013.
  These are `<!-- art: ... -->` directives that contain command flags such as
  `--owner` and `--front`:
  - `01-introduction.md`, comment opening at line 232
  - `03-the-shape-of-a-book.md`, comment opening at line 396
  - `12-the-print-pack.md`, comment opening at line 281

  *Fix:* in those three comments, spell each flag without the doubled hyphen
  (for example "the owner flag").
- *Raw angle brackets parsed as tags* (fatal):
  - ch012: `11-the-art-department.md:224`, `"...source material: --from <image>"`
  - ch018: `a-command-reference.md:31`, `*book/chapters/00-<name>.md*`
  - ch022: `e-glossary.md:474`, `*dist/<slug>-sources.md*`

  *Fix:* make each one a code span.
- *Duplicate ID `footnotes`* (ch005). The heading `### Footnotes` at
  `04-writing-the-manuscript.md:171` gets the same id as pandoc's endnotes
  section. *Fix:* add `{#footnote-markup}` to the heading.
- *8× RSC-012 "Fragment identifier is not defined"* (footnote refs in ch002,
  ch004, ch012, ch013). These are fallout from the fatal parse errors in the
  same files and should clear with them. Re-run epubcheck to confirm.

**B4. Print interior: ink at the page edge on interior pp. 353 and 357** (plus
p. 35, which is B1). Both come from long code-span definition terms in
`book/appendices/c-messages.md`:
- (a) Line 240: `` `X.Y is outside the tested range 3.10 to 3.14 (see docs/COMPATIBILITY.md)` ``
  runs past the measure (f. 345 in the reading PDF).
- (b) Line 474: `` `epubcheck is present but cannot run (<exc>); the toolchain image is broken` ``
  runs off the page. In the reading PDF it is visibly clipped as
  "…the toolchain image is broke" (f. 349).

*Fix:* shorten each term to the message's head (for example
`epubcheck is present but cannot run`) and quote the full line in the Cause
text, or break it as the other long messages in that appendix are broken.

**B5. Text silently lost in print and Web** (same source as the B3 angle
brackets). The PDF reads:
- f. 197: "the figure-from-photo style needs source material: –from ."
  The flag became an en dash and `<image>` vanished.
- f. 294: "this makes *book/chapters/00-.md*"
- f. 367: "The file *dist/-sources.md*"

*Fix:* the same three code spans as in B3.

## 3. Should findings (page read)

I read all 385 pages of the image PDF in runs of ten. Page numbers are given
as folio / PDF page.

1. **Wrong running head on every appendix page:** f. 293–376 / p. 302–385 read
   "16 Inside the press" through Appendixes A–F and the Colophon. The appendix
   and preface headings are `{.unnumbered}`, so no chapter mark is set. There
   is no clean book-side fix. This is a **press** defect for the controller
   (unnumbered chapters should set the mark); the brief forbids changing press
   here.
2. **Example caption separated from its code:**
   - f. 175 / p. 184: "Example 10.2. Setting the Alice front matter" is the
     last line on the page, and its code is on f. 176.
   - f. 183 / p. 192: "Example 10.4. A term that matches nothing" is the last
     line on the page, and its code is on f. 184.

   *Fix:* cut one sentence earlier on each page (`10-front-matter-index-authorities.md`)
   so the caption moves to the next page with its code.
3. **Nearly half-empty pages:**
   - f. 184 / p. 193: about 45% blank. The "Why the index has no page numbers"
     sidebar did not fit and moved to f. 185. *Fix:* move the sidebar one
     paragraph earlier, or trim it by two lines.
   - f. 238 / p. 247: half blank ahead of Figure 13.1. *Fix:* move the figure
     a paragraph earlier in `13-registrations.md`.
   - f. 226 / p. 235: the bottom third is blank before §12.11. *Fix:* add a
     sentence, or accept.
4. **Lead-in at the page foot:** f. 344 / p. 353, Appendix C. "`[ BROKEN]`
   Press prints:" ends the page, and its message block is on f. 345. *Fix:*
   cut a line above it on that page.
5. **Tables broken across pages:**
   - Table 16.1 (f. 276–277)
   - Table A.20 (f. 323–324)
   - Table B.1 (f. 325–326): a single row, `config/illustration-styles.yaml`,
     is stranded on f. 326. *Fix for B.1:* cut one sentence from the Appendix B
     intro to pull the row back. The other two are long tables and can stay
     split with their repeated heads.
6. **Duplicate heading id on the reader site:** `### Checking the manuscript`
   at `01-introduction.md:144` takes the id of Chapter 6's title. Chapter 6's
   page is therefore published as `6-checking-the-manuscript-1.html`.
   *Fix:* add `{#intro-checking}` to the Chapter 1 heading.
7. **Phone-width overflow on the reader site** (headless Chrome, 390 px):
   - Chapter 3's page is 643 px wide, so the whole page scrolls sideways.
     Table 3.5 (print and registration fields) and Table 3.2 overflow, with
     Tables 3.3 and 3.6 by a few pixels.
   - Appendix A's page is 451 px wide because of Table A.20.

   *Fix:* break the long unbreakable code tokens in those cells, or add
   `table{display:block;overflow-x:auto}` to `assets/web/extra.css`.
8. **Fragile tilde pairs**, not misrendering today but one edit away from B1:
   `07-building-the-editions.md:59`, `16-inside-the-press.md:19` and `:354`
   (two `*~/...*` paths on one line). *Fix:* make them code spans or escape
   the tildes.

Note for the type desk (not counted): several body paragraphs set flush left
with no indent and no space above, so they run on from the paragraph before
(for example f. 136 "The press learned this law", f. 152 "The mechanism is
the registry"). I did not trace the cause.

Clean on the read:
- No heading is stranded at a page foot without text.
- No code block wraps or overflows other than the B4 terms.
- No blockquote box is split.
- No figure is separated from its caption.
- The plates (frontispiece, the engraver's bench, the proofreaders' bench, the
  witness plate at Chapter 8, the colophon cuttlefish) sit with their chapters.
- No blank pages.
- List of Figures spot-check: 11 entries compared against caption pages
  (1.1 through 14.2). All correct.

## 4. Web notes

Headless Chrome (press `scripts/check_layout.py` driver) at 1280 and 390 px
on index, Chapters 1, 3, 5, and 12, and Appendix A:
- At 1280 there is no horizontal overflow, no broken image, and no image wider
  than the viewport.
- At 390, only the two pages in S7 overflow. Code blocks scroll inside their
  own boxes, as designed.
- The skip link and the mobile nav sit off-canvas by design.

Screenshots are in the scratchpad `shots/` folder.

## 5. EPUB notes

epubcheck results are in B3. Three chapters' XHTML were read: 2, 8, and 15.
- Every classed box is present: one `in-this-chapter`, one `sidebar`, and 2–4
  each of `tip` and `warning` per chapter.
- Each figure has a `<figcaption>`, and no `<img>` lacks `alt`.

## 6. Print pack

- **Interior** (`dist/publishing-with-press-interior.pdf`, 384 pp., 6×9): the
  verifier stopped at the edge-ink stage (B1, B4). The mirrored-margin and
  black-ink checks were therefore **not reached**. Re-run `press verify-print`
  after the fixes.
- **Cover wrap:** verified. The spine is 0.960 in for 384 pages on cream
  (384 × 0.0025 in), which matches the page count. The barcode is the honest
  `[ISBN pending]` placeholder. The front panel matches `assets/cover.jpg`
  (compared side by side at low resolution).

## 7. Order of work for the writer

1. B1 and S8 (tildes)
2. B2 (line 615)
3. B3 and B5 (code spans, comment flags, footnote heading id)
4. B4 (Appendix C terms)

Then commit and re-run the image build with all four targets. Expect the page
count to stay at 385/384. Re-read pp. 175–193 and 323–353 after the edits move
lines.

## Fixes applied

Typesetter, 2026-11-11, on top of `2277c76` (the cutting pass), uncommitted.
Manuscript only. The three sentinel phrases are untouched. Proof:
`press check` passes natively. In the toolchain image, `press verify`,
`press verify-print`, and `press verify-formats` all exit 0 (epubcheck passed,
witnesses found, no edge clipping, mirrored margins checked). The reading PDF
is still 385 pages and the interior 384. The native `dist/*.html` and the
unzipped EPUB XHTML hold no literal `<image>`, `<name>`, `<slug>`, `<model>`,
`<stem>`, or `<n>`, no comment containing `--`, no `<sub>`, and one
`id="footnotes"` per file.

| Finding | File | Before | After |
|---|---|---|---|
| B1 | `02-installing-press.md` | `*~/.press-venv*` and `*~/.press-venv/bin/press*` | `*\~/.press-venv*` and `*\~/.press-venv/bin/press*` |
| S8 | `07-building-the-editions.md` | `*~/alice*` (twice on one line) | `*\~/alice*` |
| S8 | `16-inside-the-press.md` | `*~/press*`, `*~/alice*` (two lines) | `*\~/press*`, `*\~/alice*` |
| B2 | `03-the-shape-of-a-book.md` | (already reworded by the cutting pass: the line now says "the figure's annotations" and holds no `@fig:`) | no change needed |
| B2 (same defect, new witnesses after the cut) | `07-building-the-editions.md` | Chapter 7's witness held `@fig:filter-chain`: "The print defaults add a sixth filter in the middle of that chain" | "The print defaults add a sixth filter, `print-safe-images`, in the middle of that chain" (the code span stops the line being the witness) |
| B2 (same) | `12-the-print-pack.md` | Chapter 12's witness opened `@fig:cover-wrap-anatomy`: "200 pages on cream stock." | "200 pages on cream stock (`paper: cream`)." |
| B3 comment | `01-introduction.md` art comment | `"$ press new alice --owner wonderland-press";` | `"$ press new alice", then the owner flag (two hyphens, then "owner"), then " wonderland-press", all on one line;` |
| B3 comment | `03-the-shape-of-a-book.md` art comment | `(d) italic label "press add appendix --front":` | `(d) italic label "press add appendix" followed by the front flag (two hyphens, then "front"):` |
| B3 comment | `12-the-print-pack.md` art comment | `rounded box "verify_pdf --profile print".` | `rounded box "verify_pdf", then the profile flag (two hyphens, then "profile"), then " print", all on one line.` |
| B3/B5 | `11-the-art-department.md` | `"the figure-from-photo style needs source material: --from <image>"` | `` `the figure-from-photo style needs source material: --from <image>` `` |
| B3/B5 | `a-command-reference.md` | `*book/chapters/00-<name>.md*` | `` `book/chapters/00-<name>.md` `` |
| B3/B5 | `e-glossary.md` | `*dist/<slug>-sources.md*` | `` `dist/<slug>-sources.md` `` |
| B3/B5 (same class, found by a sweep) | `a-command-reference.md` | `*assets/woodcuts/<name>.png*`, `*<model>-<n>.png*`, `*<stem>.png*`, `*build/illustrations/<name>.png*` | each as a code span |
| B3/B5 (same class) | `11-the-art-department.md` | `*assets/woodcuts/<name>.png*` (Table 11 row) | `` `assets/woodcuts/<name>.png` `` |
| B5 (same class: `--` became an en dash) | `16-inside-the-press.md` | `*scripts/verify.sh --full*` | `` `scripts/verify.sh --full` `` |
| B3 duplicate id | `04-writing-the-manuscript.md` | `### Footnotes` | `### Footnote markup` (renamed rather than given an attribute, since markup.md allows no heading attributes) |
| B4a | `c-messages.md` | term `` `X.Y is outside the tested range 3.10 to 3.14 (see docs/COMPATIBILITY.md)` `` | term `` `X.Y is outside the tested range` ``, then "Press prints:" and a `text` fence with the message broken at a space |
| B4b | `c-messages.md` | term `` `epubcheck is present but cannot run (<exc>); the toolchain image is broken` `` | term `` `epubcheck is present but cannot run` ``, then "Press prints:" and a `text` fence broken at a space |
| S2 (Example 10.2) | `10-front-matter-index-authorities.md` | "The `date` command repeats the value the scaffold wrote." sat after the example | moved into the lead-in as "The `date` command in it repeats the value that the scaffold wrote." Caption and code now share f. 175 |
| S2 (Example 10.4) | `10-front-matter-index-authorities.md` | "A revision that cuts the last mention of a term would leave such an entry. The zero-hit rule turns the cut into a refusal you see at your desk.[^10-silence]" sat after the example | moved into the lead-in: "A revision that cuts the last mention of a term leaves it in this state, and the zero-hit rule turns the cut into a refusal you see at your desk.[^10-silence]" Caption and code now share f. 183 |
| S3 (Figure 13.1) | `13-registrations.md` | image and `art:` comment directly after the "Facts are stated once" paragraph | moved two paragraphs later, after "The EPUB ISBN becomes the identifier..." (still after its `@fig:` reference). Moving it *earlier*, as the report says, would put it before its reference; moving it later fills f. 237 |
| S3 (index sidebar, f. 226) | none | | already clear after the cutting pass: the sidebar sits on f. 183 and f. 226 is full |
| S5 (Table B.1) | `b-configuration-reference.md` | "The default is the value the press uses when the key is absent." | "The default applies when the key is absent." The stranded row is back on f. 324 |
| S6 | `01-introduction.md` | `### Checking the manuscript` | `### Checking the new book` (renamed for the same reason as B3). The reader page is `6-checking-the-manuscript.html` again |
| Ch. 11 repeat | `11-the-art-department.md` | "...the file of Chapter 9's Example 9.1, and restates every key in it." | "...the file of Chapter 9's Example 9.1, and spells out each of the section's keys." |

Declined:
- **S4.** The reported instance (`[ BROKEN]` Press prints:) now sits with its
  block on f. 344. After the B4 entries grew, three other lead-ins in
  Appendix C end their pages: `not ready:` (f. 343),
  `assets/cover.jpg exists but page 1` (f. 346), and
  `print profile: margins do not mirror` (f. 350). A cut above a lead-in cannot
  pull a multi-line verbatim block up, and padding each page is whack-a-mole
  that any later edit undoes. The cure belongs in press: keep a definition
  lead-in with the fenced block that follows it (`\needspace` or similar).
- **S7.** The overflow is a press defect, not a manuscript one.
  `webmeta.label_table_cells` stamps `data-label` only on `<tr>`, but the
  image's pandoc emits `<tr class="odd">`, so in the image the phone stacking
  never applies. A native build with the newer pandoc stacks every table, and
  Chapter 3 and Appendix A measure 390 px wide at 390 px. Fix the regex to
  `<tr\b[^>]*>` in press. The fallback, `table{display:block;overflow-x:auto}`
  in `assets/web/extra.css`, is outside the manuscript-only scope.
- **S1** (running heads on the appendixes) is a press defect, as reported.
