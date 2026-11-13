# Typesetter report: typography of the Print edition

Scope: `build/docker6/dist/publishing-with-press.pdf` (381 pages, press
3.0.2; PDF page = printed folio + 8 in the main matter). Pages rendered at
72 to 100 dpi; geometry measured from `pdftotext -bbox-layout`; causes
proved by compiling the same LaTeX (regenerated with `build/defaults/pdf.yaml`
from the stitched manuscript) with `\typeout` probes, then with each fix
applied. Those test builds used local TeX Live, not the toolchain image,
so their folios run about two pages off the shipped PDF; the measurements
compare like with like. Nothing under `book/` or `config/` was edited.

## Summary

| # | Finding | Cause | Fix | Where | Kind |
|---|---------|-------|-----|-------|------|
| 1a | No paragraph indent after the Chapter 1 frontispiece; every paragraph in the book from PDF page 19 on starts flush left | `\captionof` emitted outside a group leaks `\parindent=0pt` and `\sloppy` into the rest of the document | wrap the full-page leaf in a group | press `figure-numbering.lua:164` | correction |
| 1b | False hyphens in constant-width text: 64 inserted hyphens, 93 more breaks right after a real hyphen | the monospace font hyphenates | `HyphenChar=None` on the mono font, plus zero-width break points at `/ . _` (#287) | press `book-header.tex:13` + a Lua filter | correction |
| 1c | Sentence spaces are 1.37 times the word space | no `\frenchspacing` | `\frenchspacing` | press `book-header.tex` | design change |
| 1d | Constant-width text is 10.5% wider per letter than the serif | `sourcecodepro` `scaled=0.86` | leave it, or 0.82 | press `book-header.tex:13` | design change |
| 2 | Example captions sit flush against the text above (0 pt) with a 10.4 pt gap below; one caption is stranded at the foot of a page | the caption is an ordinary bold paragraph, and the listing's list `\topsep` sits between it and its fence | an example-caption rule: space above, `\Needspace`, `\nopagebreak`, kern back the `\topsep` | press (new filter rule + header macro); the book's markup already fits | see 2 |
| 3 | Only 1 page holds an unbroken run of 30 lines or more (folio 276); 15 pages hold runs of 20 or more | 1a, then the manuscript at folio 276 | 1a | press, then the book shares the blame at folio 276 | — |

## 1. Folio 276: the wall of text

### 1a. The indent is lost for the whole book, not just this page

Measured. The header sets `\parindent` to 1.1em (`book-header.tex:69`) and
the profile repeats it (`build/profile-geometry.tex:3`). On folio 276
(PDF 284), all 10 paragraphs start at x = 56.2 pt, the left margin. In the
Preface (PDF 11 to 16), paragraphs start at x = 67.1 pt: the margin plus
11.0 pt, which is 1.1em at 10 pt. The Preface reads well because it still
has its indent. Over the whole PDF, indented first lines occur only on
PDF pages 11 to 17. They stop at the frontispiece on PDF page 18 and never
return.

Cause, proved by probe. `\typeout{\the\parindent}` before every
`\chapter` and `\section` reads 11.00pt for the first 9 headings and 0.0pt
for the other 242. The value falls to zero on the single line
`\captionof{figure}{The shop at morning: ...}`, which
`figure-numbering.lua` emits for the `{place=frontispiece}` image at
`book/chapters/01-introduction.md:17`. The full-page leaf writes
`\captionof` at top level, outside any group
(`src/press/data/lua/figure-numbering.lua:164`, inside `full_page` at
lines 145 to 170, added in a0c186a and shipped since v3.0.0). Inside a
float, `\caption` runs `\@parboxrestore` in the float's group. At top
level, `\captionof` runs it globally for the rest of the document. That
sets:

- `\parindent` to 0pt, which removes every paragraph indent from that point on.
- `\sloppy`, which sets `\tolerance` to 9999 for the rest of the book (probe
  at section 16.2: `TOL=9999`; with the fix: `TOL=200`). This explains the
  loose lines on folio 276. Across PDF pages 21 to 340, the widest mean word
  space on a justified serif line is 6.21 pt now and 4.84 pt with the fix,
  and 8 lines exceed 4.5 pt against 2.

The cause is none of the others suspected. No `\noindent` comes from
pandoc or any filter after figures or divs (the only `\noindent` in the
body is in the verse and cascade set pieces). No Div resets the indent
(the generated body contains no `\parindent`). The drop-cap filter is
inactive (`chapter-opening-style: none`). The chapter's markup is plain
paragraphs. The book holds one `\captionof`, so the whole book after
PDF page 18 is affected. Any book with a `place=frontispiece` or
`place=full-bleed` figure has the same fault.

Smallest fix (press, correction). In `full_page`, open a group before
`\begin{center}` and close it after the caption and `lof2` line (or write
`{\captionof{figure}{...}}`). Tested: with the caption in braces, the
probe reads `PI=11.00pt TOL=200` at section 16.2, and folio 276 renders
with all 10 paragraphs indented (see "Proof" below). This restores the
design the header already states. It reflows the book from Chapter 1 on.
The design contract allows that because the current output is broken.
A regression test belongs beside it: build a fixture with a frontispiece
and assert `\parindent` after it.

Is 1.1em too small? No. With the indent restored, folio 276 reads as 10
distinct paragraphs. The test build has 996 paragraph breaks inside
running text on 289 pages. In the shipped PDF, 79 of them follow a
full-measure last line, so neither an indent nor a short line shows the
break. The indent is the only signal at those breaks. 1.1em (11 pt, about
two characters at an 80-character measure) is a normal book indent. It
needs no increase once it is actually present.

### Levers for dense, fact-heavy pages, in order of effect

1. **Restore the indent (1a).** It is by far the largest effect: it
   marks every paragraph break and removes the `\sloppy` loose lines.
   Press, correction.

2. **Stop hyphenating constant-width text (1b).** Press issue **#287**
   covers this. #288 is the colophon numbering issue. Measured across the
   PDF: 166 monospace words end a line with a hyphen. Checking each one
   against the manuscript, 64 of those hyphens are inserted and are false
   (`pdfim-ages`, `FileNotFoundEr-ror`, `OPE-NAI_API_KEY` four times,
   `PRESS_RE-LEASE=1`, `booklib.chap-ter_files`, `gen_author-ities` on
   folio 276, `\line-spread`). The other 93 are breaks right after a real
   hyphen (`verify-` / `min-pages`, `--` / `profile` on folio 276), which a
   reader cannot tell from an inserted one. Fix in `book-header.tex:13`:
   load the mono face with `HyphenChar=None` (fontspec) so code spans never
   take an inserted hyphen. Then let a filter (`typographic-spacing.lua`
   already walks inlines) put zero-width `\allowbreak` after `/`, `.`, `_`
   in `Code` inlines, so long identifiers can still break without a glyph.
   Press, correction: the false hyphens are wrong output. Only paragraphs
   that contain code spans reflow.

3. **Single sentence spacing (1c).** Measured on 1722 justified serif
   lines: the space after a sentence is a median 1.37 times the word space
   (LaTeX's default `\nonfrenchspacing`). The manuscript writes short
   sentences, two or three to a line, so these wider gaps leave visible
   holes on dense pages. American technical books, O'Reilly's among them,
   set single spacing. Fix: `\frenchspacing` in `book-header.tex` near
   line 53. Press, design change (new major): it changes every line of
   every valid book.

4. **Constant-width size (1d).** It is already below the 90 percent
   proposed: `\usepackage[scaled=0.86]{sourcecodepro}`
   (`book-header.tex:13`). Font metrics: Source Code Pro x-height 0.486em,
   Libertinus Serif 0.429em. At 0.86 the code x-height is 0.418em, which is
   97% of the serif's. Going to 0.90 would make code spans larger
   (x-height 102%), not smaller. What makes inline code look loud is width:
   measured on folio 276, `render_defaults` takes 5.14 pt a character
   against 4.2 to 4.4 pt for the serif (font advance 0.516em against
   0.467em, +10.5%). Of the size changes, only a drop to 0.82 helps
   (x-height 93%, width +5%). The package also has a `light` weight
   option, which I did not test. Either is a design change (new major),
   and its effect is small next to levers 1 and 2.

5. **Block paragraphs with space between (O'Reilly style).** Setting
   `\parskip` to about 0.5\baselineskip with `\parindent` 0 (the house
   style of late-1990s O'Reilly books, as the author describes it; I did
   not measure a reference copy here) is a different house style. It also
   breaks the baseline grid that the 12.54 pt leading now keeps. Do not
   combine it with an indent. Press, design change (new major). With 1a
   fixed, it is not needed to make folio 276 readable.

6. Measured and left alone: leading 12.54 pt (10 pt type,
   `\linespread{1.045}`), about 80 characters a full line. That is at the
   long end of comfortable, and a narrower measure would be a design change
   with little gain once 1a is in.

## 2. Example 16.1 and the example captions

Measured on folio 281 (PDF 289). The section's last text line sits at
y = 181.8. The caption "Example 16.1. The selftest checks, in order" sits
at 194.3, one baseline (12.5 pt) below it, so it has **0 pt** of extra
space above. The first listing line sits at 217.2, 22.9 pt below the
caption, so it has **10.4 pt** of extra space below. That is the inverse
of a caption: it binds to the paragraph above and floats away from its
listing.

Cause. The press has no example-caption construct. The caption is the
manuscript's own bold paragraph (`**Example 16.1. ...**`,
`book/chapters/16-inside-the-press.md:186`), so it takes ordinary
paragraph spacing: `\parskip` 0pt (`book-header.tex:70`). The listing
under it is pandoc's `Shaded`/`Highlighting` (`book-header.tex:240`;
pandoc's template defines `Shaded` as an empty environment). fancyvrb's
list then adds `\topsep` 8pt plus `\partopsep` 2pt above it. The caption
package settings (`book-header.tex:137-139`) never apply, because nothing
calls `\caption`. Setting `\topsep` in a group before the listing does not
work: `\@trivlist` resets it from `\@listi` (tested).

Every example shows it. 112 caption lines in the PDF. 105 sit flush
against the text above (the other 7 follow a listing, a list, or a
heading, or sit at the top of a page). The extra space below is 19 to
23 pt across all of them. Because nothing ties the caption to its fence,
one is stranded: **Example 6.11** is the last line of folio 107, and its
listing starts on folio 108.

Table captions do not show the fault. All 116 are real `\caption`s in
`longtable`, set above the table: 20 to 21 pt of extra space above
(`\LTpre` plus the caption skip) and 14.9 pt from caption to rule. Space
above, tight below, which is the right pattern.

Smallest fix (press). In a filter (beside `set-pieces.lua`), match a
paragraph that is a single `Strong` reading `Example N.N. ...` followed
directly by a `CodeBlock`. Emit before the code block:

```latex
\par\addvspace{\medskipamount}\Needspace{6\baselineskip}%
\noindent\textbf{<caption>}\par\nopagebreak
\kern-\dimexpr\topsep+\partopsep-0.25\baselineskip\relax
```

(better as a `\PressExampleCaption` macro in `book-header.tex`).
`\addvspace` ignores a negative glue, so the kern is what cancels the
list's own space. Tested on all 106 caption-plus-fence pairs: 6.0 pt
above, 3.6 pt below, and no caption left within the last five lines of a
page. Example 16.1 then reads as one unit. It needs no change to the
book: its markup (`**Example C.N. Title**` directly above the fence) is
already uniform.

Kind. Any book with this markup changes layout, so under the design
contract the implicit pattern match is a design change (new major).
Alternatives that can ship in a minor: an opt-in (`example-captions:
house` in the aesthetic or metadata), or an explicit attribute on the
fence (`caption=`). The explicit attribute would be a markup change in the
book, not a prose change. The stranded caption on folio 107 is a defect
under either route. The 7 source captions not followed by a `Shaded` listing (untagged fences go through `verbatim`,
press #279) need the same rule checked against their listing environment.

## 3. Pages that are one unbroken block

Method. A page counts if a run of consecutive body lines (10 pt serif, no
heading, list, code, table, box, or figure, and no gap between lines
greater than the 12.54 pt baseline) covers it. Index and glossary pages
are excluded (more than half their lines are short).

- Whole pages that are one unbroken block: **0**.
- Runs of 30 lines or more (about 70% of a 43-line page): **1**, folio
  276 (38 lines, Chapter 16).
- Runs of 25 lines or more: 5. Runs of 20 or more: 15, as follows. Opener
  pages: 3 and 321 (Appendix A opening), 335. Chapter 1: 14, 22. Chapter 2:
  37. Chapter 4: 71. Chapter 5: 92. Chapter 7: 129. Chapter 9: 156.
  Chapter 12: 211, 216. Chapter 16: 276, 277, 286.

Paragraph separation on those pages. All of them come after PDF page 18,
so on every one the paragraphs touch with no indent, and only a ragged
last line shows a break (1a). That is the typography's fault, and fix 1a
cures it. Folio 276 is the one true outlier: 38 lines and 10 paragraphs
with no heading, list, or listing, and dense with code spans. The
manuscript shares the blame there. Chapter 16 holds three of the fifteen
pages, and no other chapter holds more than two. Beyond that, the
problem is typographic, not structural.

## Proof

Renders in the session scratchpad (`.../scratchpad/typo/`):
`p-284.png` (shipped folio 276, flush), `fixed-dataflow-283.png` (same
text, frontispiece caption grouped: indented), `p-289.png` (shipped
Example 16.1), `excap-290.png` (Example 16.1 with the caption rule
applied).
