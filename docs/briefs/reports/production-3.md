# Production report 3

Production editor, 2026-11-11, third production build. The brief named HEAD
`0f69a5b`. `git status --short` was clean at the start. Two commits landed as
the build began: `f10d4d6` (Chapter 8, a prose semicolon) and `3f0a69d`
(ledger). The image packs the working tree, and the source zip it produced
matches **`3f0a69d`** exactly in `00-preface.md`, `01-introduction.md`,
`08-verifying-the-artifacts.md` and the ledger, so this report is against
`3f0a69d`, which is `0f69a5b` plus those two commits. A fourth commit,
`cd41d01` ("the shop plate faces the chapter opening without a blank page in
either edition"), landed at 22:40, after this build packed its tree. **It is
not proven here.** Press checkout `~/code/press` at v3.0.2. The toolchain
image comes from its `build.yml` pin.

**Verdict: RED.** `press verify-print` fails with a blank recto in the print
interior (B1). Every other target and verifier exits 0, and epubcheck passes.
The page read found no lost or overprinted text and no ink off the page. It
found six should findings (17 instances). Declined items are not re-reported:
appendix running heads (press #282), Appendix C "Press prints:" lead-ins at a
page foot, phone-width tables (press #283), art comments shipping as HTML
comments, and the "[ISBN pending]" wording. Tables 3.5, 4.1 and 12.11 keep two
rows with their head, the accepted partial.

## 1. Build log summary

Logs:
- `build/docker3/build-all-halted.log`: `tools/docker-build.sh . build/docker3 all verify-print coverwrap`. It halted at verify-print. Under `set -e` the script then streamed no `dist/` out at all.
- `build/docker3/build-all.log`: the same three targets, rerun through a scratch copy of the script that records each target's exit status and goes on past a failure. The copy is otherwise identical: same image, same tar stream. Artifacts are in `build/docker3/dist/`.
- `build/docker3/verify-formats.log`: `tools/docker-build.sh . build/docker3/vf verify-formats`

(The first attempt failed before the build, because colima was not running.
I started it and reran.)

| Target | Exit | Last verifier line (verbatim) |
|---|---|---|
| `press all` | 0 | `Verified archives: publishing-with-press-site.zip, publishing-with-press-source.zip` |
| (inside `all`) check | 0 | `Source checks passed: 23 ordered Markdown files` / `Checker self-test passed: 29 known-bad fixtures each tripped their declared rule, known-good fixture accepted, 6 extra diagnostics noted` / `Editorial checks passed: 23 Markdown files` / `Jargon check passed: no rewrite-status terms (full audit in build/jargon-report.txt)` |
| (inside `all`) pages | 0 | `Verified dist/pages: every local reference resolves (fragments and stylesheet assets included), 8 downloads present and linked, sentinels on the public reading surface` |
| (inside `all`) PDF | 0 | `Verified publishing-with-press.pdf: 381 pages, 6 x 9 trim, embedded fonts, 3 sentinel(s) plus the title as witnesses, every rendered page contains ink, no edge clipping, cover on page 1` |
| (inside `all`) formats | 0 | `epubcheck passed: publishing-with-press.epub` / `Verified publishing-with-press.html, publishing-with-press.epub, publishing-with-press.md, publishing-with-press.txt, publishing-with-press.docx, site/ (3 sentinel(s), the title, and the manuscript line 'the first commit to the press carries th...' as witnesses); 7 editions agree on all 22 chapter witnesses` |
| `press verify-print` | **1** | `apparently blank rendered pages: [17]` |
| `press coverwrap` | 0 | `coverwrap: 381 pages -> 0.953in spine, 13.203 x 9.250in with bleed -> dist/publishing-with-press-coverwrap.pdf` / `Verified publishing-with-press-coverwrap.pdf: one page, 13.203 x 9.250 in (381-page spine), embedded fonts, no transparency, images under 600 PPI, front art present, title survives, barcode: honest placeholder present` |
| `press verify-formats` | 0 | `epubcheck passed: publishing-with-press.epub` / `Verified ... site/ (3 sentinel(s), the title, and the manuscript line 'the first commit to the press carries th...' as witnesses); 6 editions agree on all 22 chapter witnesses` / `Verified archives: publishing-with-press-site.zip, publishing-with-press-source.zip` |

Wall time: all three targets took 7 min 18 s (pandoc PDF 122.8 s, print
61.7 s). verify-formats alone took 48 s.

- **Sentinels:** all three ("You do not choose the witness", "On a fresh
  scaffold it succeeds", "the selftest skips the checks") pass in the reading
  PDF, every format edition, and the Pages bundle. The verifier lines say "3
  sentinel(s) plus the title as witnesses", "(3 sentinel(s), the title, and
  the manuscript line ...)" and "sentinels on the public reading surface".
  The interior's sentinel check runs before the blank-page check in
  `verify_pdf.main`, so it also passed there before the refusal.
- **Page floor:** the reading PDF has 381 pages against
  `verify-min-pages: 300`. It passed, with no "suspiciously short PDF". The
  interior also has 381 pages: it drops the cover but adds the blank recto
  of B1.
- **Rest of the print checks:** I ran press's own `verify_mirrored_margins`,
  `verify_black_ink` and `edge_has_ink` by hand over the image interior at
  120 dpi, which is what verify-print would have done after the blank-page
  check. Margins mirror, the ink is black only, and no edge is clipped. Only
  page 17 is blank.
- **Folios:** in the reading PDF, PDF page = folio + 9. Below, "f." is the
  folio. The interior page = the reading PDF page - 1 up to the blank.

## 2. Blocks findings

**B1. `press verify-print` refuses the interior: `apparently blank rendered
pages: [17]`.** Interior page 17 is an empty recto between the end of the
Preface (interior p. 16, the acknowledgements, a verso) and the frontispiece
(p. 18, verso), which faces Chapter 1 (p. 19).
- Cause: the frontispiece now sits at the end of `00-preface.md`.
  `figure-numbering.lua` emits `\cleardoubleevenpage` before a frontispiece.
  The reading PDF is one-sided, so there the clear is a plain `\clearpage`:
  no blank, and the plate (PDF p. 18) faces Chapter 1 (p. 19), as intended.
  The interior is `twoside`, and the Preface ends on an even page, so KOMA
  inserts a blank recto to reach the next even page.
- Why the verifier refuses it: `drop_structural_blank` forgives one isolated
  blank *verso* only. A blank recto is always the empty-pages failure.
- Fix (writer): the plate needs the text before it to end on an odd interior
  page. Either cut or add a page of Preface so that it ends on a recto, or
  move the plate. Commit `cd41d01` moves the image into Chapter 1 after its
  first paragraph. That should remove the blank, but it also takes the plate
  off the opening it was meant to face. Check it on the next image build:
  interior page count, no blank, and which page the plate faces.
- Fix (press, for the record): this case catches any book that ends a
  section on a verso before a frontispiece. The filter and the verifier
  disagree about what a twoside frontispiece may cost. It is worth an issue
  against press: a frontispiece clear that cannot produce a blank recto, or
  a verifier rule that pairs the blank recto with the plate verso that
  follows it.

No text is lost or overprinted, and no ink is off the page. The B1–B3
witnesses of report 2 are cured:
- `__main__.py` (f. 273) renders whole in the PDF, and in the EPUB as code (`ch017.xhtml`, 4 hits).
- Table 13.3 (f. 231–232): `{base}/` over `{slug}-{label}`, with nothing overprinted.
- Table A.20 (f. 318–319): `PRESS_REQUIRE_BROWSER_CHECK` on one line.

## 3. Should findings (page read, image PDF)

All 381 pages were read in runs of ten from `build/rendered-docker3/`
(pdftoppm, 160 dpi). A text scan of every page also looked for a caption or
heading on the last line, and a pixel scan measured the white space below the
text on every page.

**S1. Example caption stranded at a page foot, with the code overleaf**
(report 2 S2 class):
- f. 104: "Example 6.9. The refusal of a malformed pattern" (`06-checking-the-manuscript.md`, §6.6). New.
- f. 301: "Example A.6. press figures" (`a-command-reference.md`). **Recurring** from report 2. The fixer saw it whole on the native render, but in the image it is stranded again.

*Fix:* cut one line above each caption on that page, or fold the sentence
after the example into its lead-in.

**S2. Short examples split across a page, caption kept** (the least-slack
spots the fixer named):
- Example 4.8 (verse block), f. 75–76: caption and four of seven lines on f. 75, three lines overleaf. The fixer reported all seven on one native page.
- Example 6.11 (release refusal), f. 106–107: caption and two lines on f. 106, two overleaf.

Example 6.4 (f. 101) and Example 8.3 (f. 149) are whole. *Fix:* pull three
lines (4.8) or two lines (6.11) off the page above, or let the example lead
the next page by one more line of lead-in.

**S3. Table head stranded with fewer than three rows** (report 2 S7 class;
3.5, 4.1 and 12.11 accepted at two rows):
- Table 1.2, f. 20 (`01-introduction.md`, §1.6): head plus one row (Print edition). New.
- Table 3.3, f. 44 (`03-the-shape-of-a-book.md`): head plus two rows (`title`, `subtitle`). The fixer reported three.
- Table 6.5, f. 108 (`06-checking-the-manuscript.md`): head plus **one** row (`metadata missing <key>:`). Worse than the accepted two.
- Table 7.4, f. 122 (`07-building-the-editions.md`): head plus two rows (`pdf`, `epub`). The fixer reported three.

Table 2.3 (f. 28) now keeps three rows: **fixed**. Long split tables with
repeated heads (A.20 and others) are acceptable as before.

**S4. Pages left a quarter to a third empty ahead of a float.** The
percentage is the white space below the text block.
- f. 133: 30 percent before Figure 8.1
- f. 152, the Chapter 9 opener: 30 percent before Figure 9.1
- f. 160: 26 percent before Figure 9.3
- f. 194: 25 percent before Figure 11.2
- f. 208: 24 percent before Figure 12.1
- f. 247: 32 percent before Figure 14.3
- f. 282: 27 percent before Figure 16.3

*Fix:* move each figure one paragraph earlier (after the sentence that cites
it), or add the next paragraph's first lines above it by moving the figure
one paragraph later.

**S5. Nearly empty last pages of a chapter** (report 2 S5 class; the
Chapter 1 and Chapter 9 instances are fixed):
- f. 151, end of Chapter 8: the last three rows of the message table and a two-line closing sentence. 74 percent blank.
- f. 183, end of Chapter 10: five lines ("the book, to run to at least 200 characters ... the art department that commissions them."). 89 percent blank.

*Fix:* cut three to five lines from the pages before each, or fold the
closing sentence into the paragraph before it.

**S6. Phone-width overflow from prose** (390 px; report 2 S8, recurring):
- Chapter 13 footnote: the code span `(+https://github.com/clintecker/press)` runs to 445 px (`13-registrations.md`, footnote on the User-Agent string). The fixer's split separated the agent name from the URL, but the URL span alone is still wider than the phone.

*Fix:* set the URL as a plain link or in a `text` block, or rephrase so the
URL is not one unbreakable code span.

### Clean on the read

- No figure is separated from its caption.
- No blockquote or sidebar box is split.
- No ink is at the page edge.
- No code line wraps. A fenced-line scan of `book/` finds no line of 64 or
  more characters, and none of the page images shows a continuation hook.

### Checked at the spots named in the brief

| Spot | Folio | Result |
|---|---|---|
| Frontispiece | f. 9 (PDF p. 18), verso | Faces "1 Introduction" (f. 10). **Fixed** in the reading PDF; see B1 for the interior. |
| End of Chapter 1 | f. 22 | No stub section. §1.7 and its tip, then the closing line, on a half page. **Fixed.** |
| "The cover that passed at 11.5 percent" sidebar | f. 15 | Whole, mid-page. |
| Example 4.8 | f. 75–76 | Caption with code, block split 4/3 (S2). |
| Table 3.3 | f. 44 | Two rows with the head (S3). |
| Examples 6.4, 6.11, 8.3, 16.3, A.6 | f. 101, 106, 149, 286, 301 | 6.4, 8.3 and 16.3 whole. 6.11 split (S2). A.6 stranded (S1). |
| Tables 2.3, 7.4 | f. 28, 122 | 2.3 fixed. 7.4 two rows (S3). |
| Plate 8.1 | f. 132 | Mid-page between text. The Chapter 8 opener (f. 131) is full. **Fixed.** |
| Figure 10.2 | f. 178 | With its text. The page before (f. 177) is full. **Fixed.** |
| Index sidebar, Chapter 10 | f. 179 | Whole, with no gap above it. **Fixed.** |
| Table 10.7 | f. 181 | Whole. **Fixed.** |
| Plate 11.1 | f. 192 | Top of the page, with text below it. **Fixed.** |

Running heads: chapter pages match their chapters. Appendix pages carry "16
Inside the press" (declined, press #282).

### Spot checks

- **List of Figures:** all 41 entries were matched against the folio of
  their "Figure N.M." caption (1.1 through 16.3, including 10.2 at 178 and
  12.2 at 213). All correct.
- **List of Plates:** all six were matched against their caption pages:
  frontispiece 9, 4.1 at 65, 8.1 at 132, 11.1 at 192, 15.1 at 263, 16.1 at
  371. All correct.
- **Index locators:** twelve terms were recomputed from the reader-site HTML
  of each chapter, with code, comments and captions stripped: binfmt_misc,
  celebrimbor, Dependabot, hash lock, IngramSpark, quiet zone, runaround,
  zero-hit rule, KOMA-Script, golden copy, Tenniel, and fairy-dust. Eleven
  match the index exactly. For fairy-dust the index adds Chapter 4. Press's
  matcher reads the Markdown, where "fairy-dust" occurs in an `art:` comment,
  and Chapter 4's prose does say "fairy dust" (§4 scene breaks). The
  locator is fair, so this is not a finding.

## 4. Web notes

Headless Chrome (press `scripts/check_layout.py` driver), 1280 and 390 px,
on index, Chapters 1, 3, 4, 13 and 16, and Appendix A
(`build/docker3/dist/site`).
- **1280 px:** no horizontal overflow on any page, no broken or oversized image.
- **390 px:** index and Chapter 1 are clean (390 px wide).
- **390 px, tables:** pages wide only because of tables, all known #283
  (`td[data-label]` count is 0 in the image build):
  - Chapter 3 (643 px: Tables 3.2, 3.3, 3.5, 3.6)
  - Chapter 4 (448 px: Table 4.1)
  - Chapter 13 (766 px: Table 13.3)
  - Chapter 16 (513 px: 16.1, 16.6)
  - Appendix A (451 px: A.3, A.20)
- **390 px, prose:** only the Chapter 13 footnote (S6). The Chapter 4 dialect
  string, the Chapter 13 lookup URLs and the Chapter 16 path are now
  contained. **Fixed.**

## 5. EPUB notes

- epubcheck passes in the image, both in `press all` and in
  `press verify-formats`.
- I read the XHTML for ch002, ch008 and ch014:
  - Each has one `in-this-chapter` and one `sidebar`, and 1–3 each of `tip`
    and `warning`.
  - Every `<figure>` has a `<figcaption>` (3, 4 and 1 figures).
- I grepped 80 files: every EPUB XHTML, `dist/*.html`, `dist/site/*.html`,
  and `dist/pages/**/*.html`. They hold:
  - no literal `<image>`, `<name>`, `<slug>` or `<sub>`
  - no `<em><strong>main`
  - no HTML comment that contains `--`

## 6. Print pack

- **Interior** (`publishing-with-press-interior.pdf`): 381 pages,
  6 x 9. The verifier stops at B1. By hand, the remaining checks pass:
  margins mirror, black ink only, no edge clipping.
- **Cover wrap:** one page, 950.58 x 666 pt = 13.203 x 9.25 in.
  - **Spine:** 0.953 in = 381 x 0.0025 in (cream). The width is
    2 x 0.125 + 2 x 6 + 0.953 = 13.203 in, which matches the interior page
    count. That count includes B1's blank page. With B1 fixed, the next
    build's spine follows the new count.
  - **Barcode:** the honest placeholder, a white card that reads
    "[ISBN pending]". The verifier reports "barcode: honest placeholder
    present".
  - **Front panel:** matches `assets/cover.jpg` side by side (band, title,
    subtitle, cuttlefish, imprint, author).
  - **Back panel:** the blurb, the LGTM logomark, and the imprint line.
  - **Spine:** title and author.

## 7. Pages bundle

`dist/pages/` holds:
- `index.html`
- `read/`
- `downloads/`, with 8 files, each linked exactly once
- `sitemap.xml` and `robots.txt`
- the cover, the logo, and `woodcuts/`

At 1280 px the landing page shows:
- the title, subtitle and cover
- a "Read the Book" button
- a Table of Editions with nine rows
- "How This Book Was Built"
- the logomark and the imprint footer

Nothing overlaps or overflows (scroll width 1280). `read/index.html` is
clean too.

## 8. Order of work for the writer

1. B1. Prove whatever placement `cd41d01` settles on in the image, with
   verify-print green and the interior page count recorded.
2. S1 (Examples 6.9 and A.6) and S3 (Tables 1.2, 3.3, 6.5, 7.4).
3. S2 (Examples 4.8 and 6.11), S4 and S5, page by page. They interact, and
   B1's fix shifts every page after Chapter 1.
4. S6 (Chapter 13 footnote URL).

Commit, then rerun the image build with all four targets. The script halts
at the first failing target and then streams out no artifacts. If a target
fails again, rerun the targets one at a time.

## Fixes applied (report 3)

Production fixer, 2026-11-11, against HEAD `cd41d01` (image PDF
`build/docker4`, 382 pages). Checked after the edits in a fresh image
build of the `pdf` target (`build/fit-render/docker2`, 380 pages; that
build also packed other writers' uncommitted edits to chapters 5, 12, 14
and 15). `press check` passes. Each sentinel occurs once in `book/`.

| Finding | File:line | Change | Result in the image PDF |
|---|---|---|---|
| S1, Example A.6 caption stranded | `book/appendices/a-command-reference.md:584` | Added one sentence to the lead-in that names the eleven keys the `...` line stands for (from `figures.as_dict`). The lead-in grows by two lines, so it now splits 3/2 and the caption leads the next page with its code. | Caption and code together on f. 301. Any shift of one line either way still keeps them together. |
| S1, Example 6.9 caption stranded | `book/chapters/06-checking-the-manuscript.md:330` | Moved the "Press refuses a pattern that does not compile" paragraph and Example 6.9 above the "A match prints as" paragraph. No words changed. The example now sits about four lines higher on the page. | Caption and code together at f. 105, with about two lines to spare. |
| S2, Example 4.8 split 4/3 | `book/chapters/04-writing-the-manuscript.md:344, 352, 367, 380` | Cut about three lines above the example. The Figure 4.3 lead-in drops "when she grows too tall to reach it". The cascade paragraph drops the 2.4em/4.8em walk-through, because the rule before it states the same thing. The verse lead-in is shorter. The stanza-gap sentence moves after the example. | All seven lines on f. 76, in the image and the native PDF. |
| S5, end of Chapter 8 | `book/chapters/08-verifying-the-artifacts.md:465, 467-479, 489, 491` | Folded the tip's advice ("run `press verify-formats` too") into the sentinel-causes paragraph and removed the tip. Cut three `ok` rows (`pdffonts`, `pdfinfo`, `pdftotext`) from the Example 8.3 excerpt, which is already marked as partial. "macOS workstation" becomes "Mac". Folded the closing sentence into the Table 8.7 lead-in. | Chapter 8 ends on f. 151 after Table 8.7, with no stub page. Sentinel unchanged. |
| S5, end of Chapter 10 | `book/chapters/10-front-matter-index-authorities.md:380, 382, 386, 388, 404, 410` | Cut about four lines in 10.7.3 and 10.8: shorter workflow and footnote sentences, the artifact sentence, the companion description, and the substitutions rationale folded into its lead sentence. Shortened the verifier definition and folded the closing sentence into the paragraph before it. | Chapter 10 ends on f. 182 with about two lines to spare. |
| S6, Chapter 13 footnote overflow | `book/chapters/13-registrations.md:326` | Split the user-agent string into code spans of at most 26 characters: `press-registrations-lookup`, `(+https://github.com/`, `clintecker/press)`. The prose says they run together. | Footnote sets cleanly on f. 232. The phone width was not re-measured, but no span is longer than 26 characters. |

Declined: none of the five. As ruled, stranded table heads (S3) and
part-empty pages before floats (S4) were not touched. Example 6.11 (S2)
was not in the brief. In the native PDF, Examples 6.9 and A.6 still break
badly because the native build runs about five to seven lines off the
image on those pages. The image PDF is the authority.
