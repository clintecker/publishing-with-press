# Production report 2

Production editor, 2026-11-11, second production build, against commit
`7d487ef` (tree clean apart from `build/` and `dist/`). Press checkout
`~/code/press` at v3.0.2; toolchain image from its `build.yml` pin.

**Verdict: RED.** Every press target and verifier exits 0 in the image, and
epubcheck passes. The page read found three blocks: one more case of text
silently lost (the B5 class) and two table cells printed over their
neighbours. It also found eight should findings. All of them are writer's
fixes. Declined items S1 (appendix running heads, press #282), S4 (Appendix C
"Press prints:" lead-ins at a page foot) and S7 (phone-width tables, press
#283) are not re-reported.

## 1. Build log summary

Logs:
- `build/docker2/build-all.log`: `tools/docker-build.sh . build/docker2 all verify-print coverwrap`
- `build/docker2/verify-formats.log`: `tools/docker-build.sh . build/docker2/vf verify-formats`

Artifacts are in `build/docker2/dist/`. The script did not halt, so no
per-target rerun was needed.

| Target | Exit | Last verifier line (verbatim) |
|---|---|---|
| `press all` | 0 | `Verified archives: publishing-with-press-site.zip, publishing-with-press-source.zip` |
| (inside `all`) check | 0 | `Source checks passed: 23 ordered Markdown files` / `Checker self-test passed: 29 known-bad fixtures ...` / `Editorial checks passed: 23 Markdown files` / `Jargon check passed: no rewrite-status terms` |
| (inside `all`) pages | 0 | `Verified dist/pages: every local reference resolves (fragments and stylesheet assets included), 8 downloads present and linked, sentinels on the public reading surface` |
| (inside `all`) PDF | 0 | `Verified publishing-with-press.pdf: 385 pages, 6 x 9 trim, embedded fonts, 3 sentinel(s) plus the title as witnesses, every rendered page contains ink, no edge clipping, cover on page 1` |
| (inside `all`) formats | 0 | `epubcheck passed: publishing-with-press.epub` / `Verified publishing-with-press.html, ...epub, ...md, ...txt, ...docx, site/ (3 sentinel(s), the title, and the manuscript line 'the first commit to the press carries th...' as witnesses); 7 editions agree on all 22 chapter witnesses` |
| `press verify-print` | 0 | `Verified publishing-with-press-interior.pdf: 384 pages, 6 x 9 trim, embedded fonts, 3 sentinel(s) plus the title as witnesses, every rendered page contains ink, no edge clipping, mirrored margins, black ink only` and `Verified publishing-with-press-coverwrap.pdf: one page, 13.210 x 9.250 in (384-page spine), embedded fonts, no transparency, images under 600 PPI, front art present, title survives, barcode: honest placeholder present` |
| `press coverwrap` | 0 | `coverwrap: 384 pages -> 0.960in spine, 13.210 x 9.250in with bleed` and the same coverwrap `Verified` line |
| `press verify-formats` | 0 | `epubcheck passed: publishing-with-press.epub` / `... 6 editions agree on all 22 chapter witnesses` / `Verified archives: ...` |

Wall time: all targets about 10 min 23 s; verify-formats alone 1 min 15 s.

- **Sentinels:** all three ("You do not choose the witness", "On a fresh
  scaffold it succeeds", "the selftest skips the checks") pass in the PDF,
  the interior, every format edition, and the Pages bundle. Each verifier
  says so in its line: "3 sentinel(s) plus the title as witnesses" and
  "sentinels on the public reading surface".
- **Page floor:** the reading PDF has 385 pages and the interior has 384,
  against `verify-min-pages: 300`. The PDF verifier passed, so there was no
  "suspiciously short PDF" refusal.
- **Folios:** in the reading PDF, PDF page = folio + 9. Below, "f." is the
  folio.
- **Native vs image:** the native `press render` PDF (`dist/`) has **384**
  pages, against 385 in the image. About 180 folios break differently. The
  page read covered all 385 native page images (`build/rendered-book/`, in
  runs of six). It then covered every image page that differs from native
  (`build/rendered-docker2/`, pdftoppm at 160 dpi). Every finding below is
  stated against the **image** PDF.
- **Press note (not counted):** `build/rendered-book/page-385.png` dates from
  an earlier render (18:48). `press render` does not clear stale page images
  when the page count falls, so the directory shows 385 images for a 384-page
  PDF.

## 2. Blocks findings

**B1. `__main__.py` loses its underscores in every edition** (the B5 class:
text silently lost). f. 277: "Every command enters through ***main**.py*."
In the HTML it is `<em><strong>main</strong>.py</em>`. Source:
`book/chapters/16-inside-the-press.md:58`, `*__main__.py*`. Pandoc reads the
double underscores as strong emphasis.
*Fix:* write it as a code span, `` `__main__.py` ``. (The other `__pycache__`
mentions are already inside code.)

**B2. Table 13.3 prints one cell over another**, f. 235. The Value cell
`{base}/{slug}-{label}` (row `RecordReference`) cannot break. Its
"{slug}-" runs into the Meaning column and prints over "The base is". Source:
`book/chapters/13-registrations.md:211`.
*Fix:* lengthen the Value column's run of hyphens in the separator row so
that pandoc gives that column room for 21 monospace characters. Or break the
pattern into two code spans at the slash (`` `{base}/` `` `` `{slug}-{label}` ``).

**B3. Table A.20 prints one cell over another**, f. 323.
`PRESS_REQUIRE_BROWSER_CHECK` is hyphenated "PRESS_RE-/QUIRE_BROWSER_CHECK".
Its second half runs into the Effect column and prints over "the headless
Chrome". Source: `book/appendices/a-command-reference.md:1346`.
*Fix:* widen the Variable column in the separator row, the same fix as B2.

## 3. Should findings (page read, image PDF)

**S1. Chapter 1 opener is a heading alone on a page.** f. 9 holds only
"1 Introduction". The frontispiece takes f. 10, and the chapter's text starts
on f. 11, so the plate faces the continuation and not the chapter opening.
Source: `01-introduction.md:3`, where the `{place=frontispiece}` image comes
*after* the `#` heading.
*Fix:* move the frontispiece image line so that it comes before the chapter
it faces, at the end of `00-preface.md`. A frontispiece "faces the chapter
that follows". Then confirm the plate's number with `press figures`.

**S2. Example caption stranded at a page foot, code on the next page.** This
is the first report's S2 class. 10.2, 10.4 and A.4 are now fixed. New
instances:
- f. 78: "Example 4.8. A verse block" (`04-writing-the-manuscript.md`)
- f. 104: "Example 6.4. The command the fourth pass runs" (above the footnotes) (`06-checking-the-manuscript.md`)
- f. 109: "Example 6.11. The release refusal" (`06-checking-the-manuscript.md`)
- f. 152: "Example 8.3. Part of a press doctor report" (`08-verifying-the-artifacts.md`)
- f. 289: "Example 16.3. A working setup on hatter" (`16-inside-the-press.md`)
- f. 305: "Example A.6. press figures" (`a-command-reference.md`)

*Fix:* the same move the fixer made for 10.2 and 10.4. Fold the sentence
after each example into its lead-in, or cut one line above it on that page,
so the caption moves over with its code.

**S3. Code lines wrap with the continuation hook.** The book's code measure
holds 63 characters. Every fenced line of exactly 64 characters wraps, and
every line of 63 fits. The nine wrapped lines are:
- f. 18 `01-introduction.md:135` (`... "Alice's Adventures in Wonderland" && \`; the `\` wraps alone)
- f. 71 `04-writing-the-manuscript.md:168`
- f. 72 `04-writing-the-manuscript.md:206` (the separator row of Example 4.4; its wrapped part also runs about 0.15 in past the measure)
- f. 85 `05-figures-and-plates.md:135`
- f. 103 `06-checking-the-manuscript.md:165`
- f. 302 `a-command-reference.md:427` (press cover synopsis)
- f. 313 `a-command-reference.md:919`
- f. 316 `a-command-reference.md:1048`

*Fix:* shorten each line by one character, or break it by hand. Also correct
the tip at `04-writing-the-manuscript.md:247`, "Keep code lines to 64
characters or fewer", which this book's own pages contradict. It should say
63, or "fewer than 64".

**S4. Appendix C definition terms run past the measure** (B4 class; not at
the page edge, so verify-print passes), f. 347:
- `c-messages.md:425`: `` `no manuscript witness derivable; ... (write one honest plain sentence)` `` runs about 0.4 in past the measure.
- `c-messages.md:396`: `` `... carries no cover image -- the generated front matter dropped it` `` runs about 0.2 in past it.

*Fix:* as for B4: shorten each term to its head and quote the full message
in a `text` block under "Press prints:".

**S5. Nearly empty pages:**
- f. 24, the last page of Chapter 1, holds only "1.8 How to read this book"
  and its one sentence.
- f. 171, the last page of Chapter 9, holds two lines ("Chapter 10, *Front
  matter, ...*, turns from the design ...").

*Fix:* cut three lines from the pages before each (`01-introduction.md`
around §1.7, the end of `09-the-house-design.md`), or fold the closing
sentence into the paragraph before it.

**S6. Pages left about half empty ahead of a float.** f. 183 is a recurrence
of first-report S3: the "Why the index has no page numbers" sidebar no longer
splits, but it moves whole to f. 184 and leaves f. 183 about 35 percent
blank.
- f. 12: about 46 percent blank before Figure 1.1
- f. 33: about 47 percent blank before Figure 2.2
- f. 134: the Chapter 8 opener is about 50 percent blank, because plate 8.1 moves to f. 135
- f. 181: about 40 percent blank before Figure 10.2
- f. 183: about 35 percent blank before the index sidebar
- f. 185: about 45 percent blank before Table 10.7
- f. 196: about 45 percent blank before plate 11.1

*Fix:* move each figure or plate one paragraph earlier, after the sentence
that cites it, or trim the box by two lines.

**S7. Table head stranded at a page foot** (header plus one row, rest
overleaf; first-report S5 class):
- Table 2.3, f. 30 (`02-installing-press.md`)
- Table 3.3, f. 47 (`03-the-shape-of-a-book.md`)
- Table 3.5, f. 50 (`03-the-shape-of-a-book.md`)
- Table 4.1, f. 64 (`04-writing-the-manuscript.md`)
- Table 6.5, f. 111 (`06-checking-the-manuscript.md`)
- Table 7.4, f. 125 (`07-building-the-editions.md`)
- Table 12.11, f. 226 (`12-the-print-pack.md`)

Long tables split with repeated heads (7.1, 13.3, 16.1, A.20) are acceptable.
*Fix:* cut or add one or two lines above each table so that it moves whole,
or so that at least three rows stay with the head.

**S8. Phone-width overflow from prose, not tables** (390 px; outside #283):
- Chapter 4: the inline code `markdown+smart+yaml_metadata_block+fenced_divs+footnotes` (`04-writing-the-manuscript.md:22`) runs to 603 px.
- Chapter 13: the URL *https://portal.issn.org/resource/ISSN/{issn}* (`13-registrations.md:238`) runs to 428 px, and the footnote code `press-registrations-lookup (+https://github.com/clintecker/press)` (`:321`) runs to 440 px.
- Chapter 16: *src/press/data/extensions/reference.yaml* (`16-inside-the-press.md:270`) runs to 402 px.

*Fix:* move the dialect string into a `text` block. Break the footnote's
string into its two parts, the agent name and the URL. The italic path and
URL are a press CSS matter (`overflow-wrap`). A writer's fallback is to
rephrase so they are not set in running text.

Clean on the read:
- No blockquote or sidebar box is split in the image PDF. The native build
  split three; the image moves them whole.
- No figure is separated from its caption.
- No ink is at the page edge.
- No blank pages.

Fixer's touched spots:
- Example 10.2 (f. 175) and Example 10.4 (f. 183): caption and code together. **Fixed.**
- Table B.1 (f. 324): whole. **Fixed.**
- Figure 13.1: top of f. 238, facing its reference on f. 237, which is about 20 percent blank. **Fixed.**
- Appendix C, f. 340–352: B4 terms fixed. S4 lead-ins (declined) remain at f. 343, 346 and 350. The new overruns are in S4 above.
- B-heads in Chapters 1, 7 and 12 ("Checking the new book", "Footnote markup", and the others): render correctly, with no stranding.

Running heads: chapter pages match their chapters. Appendix pages carry
"16 Inside the press" (declined S1).

Spot checks:
- **List of Figures:** 25 entries (1.1, 2.1, 2.2, 3.1, 3.3, 4.3, 5.1, 5.2, 6.1, 6.3, 7.1, 7.2, 7.4, 8.2, 8.3, 9.1, 9.3, 11.1, 11.2, 11.3, 12.3, 14.1, 14.3, 15.2, 16.2) matched against the folio of each caption. All correct.
- **List of Plates:** all six (10, 68, 135, 197, 267, 375). All correct.
- **Index locators:** 12 terms (binfmt_misc, celebrimbor, fonts-linuxlibertine, golden copy, hash lock, IngramSpark, quiet zone, runaround, stacked subtitle, zero-hit rule, Dependabot, KOMA-Script) recomputed from the prose of each chapter, with code excluded. All match the index exactly.

## 4. Web notes

Headless Chrome (press `scripts/check_layout.py` driver), 1280 and 390 px,
on index, Chapters 1, 3, 4, 13 and 16, and Appendix A
(`build/docker2/dist/site`).
- **1280 px:** no horizontal overflow on any page, no broken or oversized
  image, no overlap.
- **390 px:** index and Chapter 1 are clean (390 px wide).
- **390 px, tables:** pages wide only because of tables, all known #283
  (`td[data-label]` count is 0 in the image build):
  - Chapter 3 (643 px: Tables 3.2, 3.3, 3.5, 3.6)
  - Chapter 13 (766 px: Table 13.3)
  - Chapter 16 (513 px: 16.1, 16.6)
  - Appendix A (451 px: A.3, A.20)
- **390 px, prose:** the overflows in S8 are not tables and are findings.
- Code blocks scroll inside their own boxes. The skip link and the mobile nav
  sit off-canvas by design. Plates render on their paper card in dark mode.

## 5. EPUB notes

- epubcheck passes in the image, both in `press all` and in
  `press verify-formats`.
- XHTML read for ch003 (Chapter 2), ch009 (Chapter 8) and ch014
  (Chapter 13):
  - Each has one `in-this-chapter` and one `sidebar`, and 2–4 each of `tip`
    and `warning`.
  - Every `<figure>` has a `<figcaption>` (3, 4 and 1 figures).
  - No `<img>` lacks `alt`.
  - Footnote references match their notes (3/3, 4/4, 2/2), with one
    `id="footnotes"` per file.
- Grep of every EPUB XHTML file, `dist/*.html`, `dist/site/*.html`, and the
  Pages HTML:
  - no literal `<image>`, `<name>`, `<slug>` or `<sub>`
  - no HTML comment that contains `--`
- **Note:** the `<!-- art: ... -->` directives ship inside the EPUB and HTML
  as comments. This is harmless and invisible, but it is author's notes in a
  published file.

## 6. Print pack

- **Interior** (`publishing-with-press-interior.pdf`): 384 pages,
  432 x 648 pt (6 x 9). The verifier reports mirrored margins, black ink
  only, no edge clipping, embedded fonts, and the sentinels.
- **Cover wrap:** one page, 951.12 x 666 pt = 13.21 x 9.25 in.
  - **Spine:** 0.960 in = 384 pages x 0.0025 in (cream). The wrap width is
    2 x 0.125 + 2 x 6 + 0.96 = 13.21 in. This matches the page count.
  - **Barcode:** the honest placeholder, a white box that reads
    "[ISBN pending]". The verifier reports "barcode: honest placeholder
    present". Press 3.0.2's placeholder text is "[ISBN pending]", as f. 219
    of this book says. It does not read "not declared for retail".
  - **Front panel:** matches `assets/cover.jpg` side by side (band, title,
    subtitle, cuttlefish, imprint, and author).
  - **Back panel:** the blurb, the LGTM logomark, and the imprint line.
  - **Spine:** title and author.

## 7. Pages bundle

`dist/pages/` exists, with `index.html`, `read/` (the reader site), and
`downloads/`, which holds 8 files, each linked exactly once. At 1280 px the
landing page shows:
- the title, subtitle and cover
- a "Read the Book" button
- a Table of Editions with nine rows: Chapter, Print, Circulating,
  Single-leaf, Manuscript, Telegraphic, Office, Chapter boxed, and Source
- "How This Book Was Built" and the imprint footer

Nothing overlaps or overflows.

## 8. Order of work for the writer

1. B1 (`__main__.py` code span)
2. B2 and B3 (table column widths)
3. S3 (nine 64-character lines and the tip)
4. S4 (two Appendix C terms)
5. S1 (frontispiece position)
6. S2, S5, S6 and S7, page by page, then re-render. They interact: every line
   moved shifts the pages after it.
7. S8 (phone-width prose)

Commit and rerun the image build with all four targets.

## Fixes applied (report 2)

Fixer, 2026-11-11, against the working tree on `7d487ef` (uncommitted, with
the managing editor's hand edits to `01-introduction.md` kept: the expanded
11.5 percent sidebar and the removed "How to read this book" stub heading).
Proof: `press check` passes natively. Each sentinel greps to 1 across `book/`.
`tools/ste_check.py` on every edited file shows nothing new in prose. The new
findings are the frontispiece `art:` comment (now in the Preface), the
editor's sidebar quoting press's "was clipped" message, and the counter
merging an `@fig:` sentence into the one before it. Final native
`press render`: 380 pages. Page numbers below are native PDF pages from that
render. The image PDF breaks differently, so S2, S5, S6 and S7 need the next
image build to confirm.

| Finding | File:line | What I did |
|---|---|---|
| B1 | `16-inside-the-press.md:58` | `*__main__.py*` became the code span `` `__main__.py` ``. It renders as `__main__.py` (p. 282). |
| B2 | `13-registrations.md:207,211` | Separator row is now 18/21/20 hyphens (Element/Value/Meaning), at 64 columns. Widening the column alone still broke the pattern at its hyphen, so I used the allowed fallback: `` `{base}/` `{slug}-{label}` ``. The cell now reads `{base}/` over `{slug}-{label}`, nothing overprints, and `ProductComposition` no longer hyphenates (p. 239). |
| B3 | `a-command-reference.md:1336` | Separator row is now 31/29 hyphens (Variable/Effect), at 63 columns. `PRESS_REQUIRE_BROWSER_CHECK` and `OPENAI_API_KEY, GEMINI_API_KEY` each sit on one line (pp. 327-328). |
| S3 | `01-introduction.md:131` | The title moved to its own continuation line (`press config set title \` then `"Alice's Adventures in Wonderland" && \`). The command still runs. |
| S3 | `04-writing-the-manuscript.md:174` | Broke the Carroll line before `herself.[^2-well]`. The Markdown it shows still parses. |
| S3 | `04-writing-the-manuscript.md:213` | Took one hyphen off the Example 4.4 separator row (63 columns). |
| S3 | `04-writing-the-manuscript.md:254` | The tip now reads "63 characters or fewer". |
| S3 | `05-figures-and-plates.md:135` | Hand-broke the message after the colon, with `assets/woodcuts/<name>` on a two-space continuation line. |
| S3 | `06-checking-the-manuscript.md:158-183` | The Example 6.3 detail lines now indent 2 spaces instead of 4, so the columns stay aligned and the longest line is 62. |
| S3 | `a-command-reference.md:427-428` | The `press cover` synopsis is two lines: `press cover [--style <id>] [--subject <text>] [--print]` and `press cover --list`. Same alternatives. |
| S3 | `a-command-reference.md:920` | Removed the 2-space indent so the line matches the real message and Chapter 10's copy (62 characters). |
| S3 | `a-command-reference.md:1048-1049` | Moved the selftest line's break one word earlier. |
| S3 sweep | `book/` | A fenced-line scan found no other line of 64 or more characters. That includes indented fences. |
| S4 | `c-messages.md:396` | Term shortened to `` `... carries no cover image` ``. The full message from `verify_pdf.py` follows under "Press prints:" in a `text` block (p. 351). |
| S4 | `c-messages.md:434` | Term shortened to `` `no manuscript witness derivable` ``. The full message from `verify_formats.py`, with its `<label>:` prefix, follows under "Press prints:" (p. 352). |
| S1 | `00-preface.md:169` (from `01-introduction.md:3`) | Moved the image line (`{place=frontispiece}`, caption unchanged) and its `art:` comment to the end of the Preface, after a blank line. `press figures` lists it from `00-preface.md`, `numbered: false`. The plate is on p. 18, facing the Chapter 1 opener on p. 19. |
| S8 | `04-writing-the-manuscript.md:22-27` | The dialect string is now a `text` block: "...reads the manuscript in the dialect that follows, with `standalone: true` and `number-sections: true`." |
| S8 | `13-registrations.md:238-243` | Both lookup URLs went into a `text` block ("goes to the first of the two URLs that follow" / "the second"). |
| S8 | `13-registrations.md:326` | The footnote splits the agent string into two code spans, URL first: "The string ends with `(+https://...press)`, after `press-registrations-lookup` and a space." Name first, the URL hyphenated in the PDF (`clin-tecker`). |
| S8 | `16-inside-the-press.md:270` | Now "which press keeps as *reference.yaml* in *src/press/data/extensions/*", so the path can break between the two italics. |
| S5 (Ch 1) | `01-introduction.md:265,278` | The sources-companion sentence is shorter, and the tip says "Chapter 14 takes the mechanism apart" (Chapter 14's title was already given in the section). With the editor's heading cut, the closing sentence sits on p. 31 under the tip. |
| S5 (Ch 9) | `09-the-house-design.md:385,389,391` | Three one-line cuts: "first patch" for "first patch release" in the footnote, "a profile no longer matches its seal", "fails the press's own tests". The closing sentence is back on the last text page (p. 176). |
| S6 (Fig 1.1) | `01-introduction.md:30` | The `@fig:pipeline-overview` sentence moved to the end of the docstring paragraph, with the figure after that paragraph. The figure fills p. 20 under two lines of text. Figure 1.2 shares p. 21 with its text. |
| S6 (Fig 2.2) | `02-installing-press.md:212,224` | Shortened the fonts-libertinus sentence ("the obvious name"). Folded the `@fig:doctor-report` paragraph into the paragraph before it, and merged "Most lines read `ok`" with the `epubcheck` sentence to keep six sentences. The figure now follows its text on p. 40. |
| S6 (plate 8.1) | `08-verifying-the-artifacts.md:27` | The plate was already at its earliest spot, so earlier was impossible. I moved it after the third paragraph of 8.1. The opener page fills (p. 140) and the plate sits mid-p. 141 between text. |
| S6 (Fig 10.2) | `10-front-matter-index-authorities.md:269` | Moving it earlier would put it before its `@fig:` sentence, so I moved it to the end of 10.6.1, after the warning. p. 186 is now about 13 percent blank, down from 45. The index sidebar no longer leaves a gap. |
| S6 (Table 10.7, index sidebar) | none | Native read: Table 10.7 is whole, and the sidebar sits whole on p. 188 with no gap above it. |
| S6 (plate 11.1) | `11-the-art-department.md:236` | Moved two paragraphs earlier, after the guard block. The plate fills p. 200 between text. |
| S2 (Ex 4.8) | `04-writing-the-manuscript.md:367,380` | Moved the layout sentences (3em indent, 0.7em space, hanging quote, `.verse` margin) from the lead-in to just after the example. The lead-in, caption and all seven code lines share p. 84. |
| S2 (Ex 6.4) | `06-checking-the-manuscript.md:194,212` | Two one-line cuts above it: "in place of XXXX. Chapter 4 gives...", and "A clean audit prints ...". Caption and code are together on p. 110. |
| S2 (Ex 6.11) | `06-checking-the-manuscript.md:392` | Moved "The reusable workflow sets `PRESS_RELEASE=1`..." from after the example into its lead-in. Caption and code open p. 116. |
| S2 (Ex 8.3, 16.3, A.6) | none | Native read: caption and code are together (pp. 158, 295, 310). No change. |
| S7 (Table 2.3) | `02-installing-press.md:150` | "Press requires the first eight tools and builds books without the last two." Four rows now stay with the head (p. 37). |
| S7 (Table 3.3) | `03-the-shape-of-a-book.md:178,180,184,187` | Shortened the gloss and the "Notice" sentence. "Its meaning. The model requires the title, the author, and the slug." Narrowed the Field column. Three rows now stay with the head (p. 53). |
| S7 (Table 4.1) | `04-writing-the-manuscript.md:28,42` | The "same settings" paragraph moved to after the table, which offsets the S8 block. Two rows are now with the head (p. 70). |
| S7 (Table 6.5) | `06-checking-the-manuscript.md:449` | "Fix every diagnostic before you run the check again, because the next pass may have more to say." Two rows are now with the head (p. 117). |
| S7 (Table 7.4) | `07-building-the-editions.md:273` | Cut the closing "The result is the manuscript as you wrote it, in one file." It only repeated "changes nothing else". Three rows now stay with the head (p. 131). |
| S7 (Table 12.11) | `12-the-print-pack.md:419-428,448` | "gives the Lulu paperback procedure", "For a hardcover, set", "then **Paperback, Perfect Bound**". The Meaning column is wider. Two rows are now with the head (p. 230). |
| S7 (Table 3.5) | `03-the-shape-of-a-book.md:255` | Rebalanced the columns (Meaning wider). Still two rows with the head (p. 56). |

Declined or left short:
- **S7, Tables 3.5, 4.1, 6.5 and 12.11.** Each now has two rows with its head
  on the native page, not three. The third row needs three or four more cut
  lines on a page that has no closer or restatement left to cut, and adding
  prose was ruled out. Rows that span two lines make each fix cost twice. A
  cure in press (`\needspace` before a longtable head, or a three-row
  minimum) would close the whole class.
- **S8 italic paths.** None left. Both took a short rephrase or a block.
- **Image PDF.** Every page-fit change above was proved on the native render
  only. They fold sentences and move floats rather than pad pages, so a
  one-line shift should not undo them. Ex 4.8 and Table 3.3 have the least
  slack.
- **Out of scope, seen in passing.** `07-building-the-editions.md` 7.7.3 has a
  prose semicolon ("and only those; a book outside..."). Left for the
  writer.
