# Figure gap: folio 274 and fourteen other pages

Typesetter desk report. Source PDF: `build/docker6/dist/publishing-with-press.pdf`
(381 pages, 6 x 9 in, 432 x 648 pt). The PDF index is the printed folio plus 8
(cover and roman front matter), so folio 274 is PDF page 282. The PDF was
built against the v3 press (`press @ ...@v3`, the v3.0.2 release).

## Correction to the reported defect

There is no gap under the caption of Figure 16.1. Measured with
`pdftotext -bbox-layout` on PDF page 282:

| Element | y (pt from top) |
|---|---|
| Figure 16.1 image | about 40 to 290 |
| Caption "Figure 16.1. The module areas..." | 294 to 304 |
| "Every command enters through `__main__.py`..." | starts at 321 (17 pt below the caption, the normal caption skip) |
| Last text line "...For the Alice book, Figure 16.2 draws the whole path." | ends at 461 |
| Bottom of the text block (the most common last-line bottom) | 594 |
| Folio "274" | 609 |

The empty band is at the foot of the page: **133 to 139 pt (about 1.9 in, a
quarter of the 554 pt text block) between the last line and the folio**. The
next thing in the source is Figure 16.2. It does not fit in the remaining
133 pt, so the whole figure moves to folio 275 and nothing fills the space it
leaves.

No figure in the book has a large gap under its caption. Across all 45
numbered-figure captions, the space from caption to the next line is 15 to 37
pt (17 pt before body text, about 32 to 37 pt before a section heading).

## Every page with the same fault

A page is listed when its last line ends 50 pt or more above the text-block
bottom and the next page opens with an unplaced numbered figure. Chapter ends,
front matter, and table breaks are left out.

| Folio | PDF index | Band at foot | Figure pushed to the next page |
|---|---|---|---|
| 59 | 67 | 72 pt | Figure 3.3, the dist directory after press all |
| 87 | 95 | 64 pt | Figure 5.2, a wrap against running text on a verso |
| 108 | 116 | 77 pt | Figure 6.3, a passing check on the three-chapter example |
| 113 | 121 | 54 pt | Figure 7.1, the artifact graph the registry declares |
| 126 | 134 | 127 pt | Figure 7.4, the press all sequence |
| 134 | 142 | 176 pt | Figure 8.1, what each verifier inspects |
| 153 | 161 | 175 pt | Figure 9.1, the house 6 by 9 page drawn to scale |
| 161 | 169 | 153 pt | Figure 9.3, a chapter page of the three-chapter example |
| 178 | 186 | 81 pt | Figure 10.2, the path of an index term |
| 184 | 192 | 51 pt | Figure 11.1, the art-direction loop |
| 208 | 216 | 140 pt | Figure 12.1, spine math by provider |
| 216 | 224 | 70 pt | Figure 12.3, the print pack |
| 248 | 256 | 185 pt | Figure 14.3, the states of one press release |
| **274** | **282** | **139 pt** | **Figure 16.2, the data flow from book repository to release** |
| 283 | 291 | 160 pt | Figure 16.3, the trust receipt chain |

The worst seven (126 to 185 pt) leave a band between a quarter and a third of
the text block. Pages at 160 pt or more come close to the "third of the page"
in the original report.

Some pages also end short before a table, for example folio 41 (120 pt,
before Table 3.2) and folio 72 (106 pt, before Table 4.3). That is probably a
related but separate mechanism (tables that are not allowed to break) and was
not looked into here.

## Ruled out

- **Fixed-height box sized to the 6.3 in cap.** There isn't one. The cap in
  `src/press/data/tex/book-header.tex:154` (`\PressFigureCap`, 6.3 in, re-set
  per profile by `src/press/profiles.py:134`, which is 6.3 for house-6x9)
  works through `\pandocbounded` (book-header.tex:164-183). That macro scales
  the image's own box with `\scalebox` and never pads it to a fixed height.
  The figures:
  - Figure 16.1 (`16-01-module-map.png`, 1362 x 967 px, 300 dpi, aspect
    0.71) at full measure (`\linewidth`, `press-util.lua:12`; 326.9 pt =
    4.54 in measured) is 3.22 in (232 pt) tall. That matches the 40 to 290 pt
    span on the page, and the cap does not bind.
  - Figure 16.2 (`16-02-end-to-end-data-flow.png`, 1362 x 1726 px, aspect
    1.27) is 5.75 in (414 pt) tall, plus the caption. The cap does not bind
    here either, but the figure is about 440 pt including the caption,
    against the 133 pt left on folio 274.
- **A deferred `[t]` float.** Numbered figures do not float at all (see
  below).
- **`\needspace` before a heading.** The next item in the source is a
  figure, not a heading.
- **Vertical space from a placement.** Figure 16.1 has no `place=` or
  `outset=`, so `placed()` returns nil and no `\vfill` or `\clearpage` is
  emitted. Those appear only in `full_page`, for full-bleed and
  frontispiece.

## Cause

Two press decisions combine to cause the band.

1. **Unplaced numbered figures are pinned with `[H]`.**
   `src/press/data/lua/figure-numbering.lua:239-243` emits
   `\begin{figure}[H]\centering ... \end{figure}` for any numbered figure
   (`.diagram`, `.figure`, `.chart`, `.map`, `.photo`) with no `place=`.
   `src/press/data/tex/book-header.tex:126` loads `float`, and line 147 sets
   `\floatplacement{figure}{H}`. The comment at lines 123-124 states the
   intent: "pinned where the source places them rather than floated." An
   `[H]` figure is a solid box in the text. When it does not fit in the space
   left on the page, LaTeX ends the page there, and the text after the figure
   in the source cannot move forward to fill the gap.
2. **The reading PDF is bottom-ragged.** `src/press/data/defaults/pdf.yaml:25-27`
   uses `scrbook` with `oneside`, which defaults to `\raggedbottom`. So the
   unused space is not spread between paragraphs and stays as one band at the
   foot. The print edition (`print.yaml:42-44`, `twoside`, flushbottom by
   default) would instead stretch the paragraph glue on those pages, giving
   underfull pages with loose spacing.

How big the band is depends only on where in the text the next tall figure
falls. Figures 16.2 (5.75 in), 8.1, 9.1, 14.3 and the other tall diagrams
cause the large bands.

## Press defect or book choice?

It is a press defect. The book does nothing unusual: `.diagram
width=full-measure` with no placement is the documented default, and the
manuscript cannot control where page breaks fall. The `[H]` policy is a
deliberate house design, carried over from the woodcut-plate idiom where a
plate belongs at its place in the text. For tall numbered technical figures it
gives a predictable fault: on about a third of figure pages (15 of 45) the
text stops short above the figure. Under the press contract, changing how a
valid book's figures are placed is a layout change. The house fix belongs in
the next major (the v4 edition-parity work). A v3 fix has to be opt-in.

## Smallest fix on each side

**Press (v3, additive, no change to existing output):** add a placement value
such as `place=float` (or `place=top`) to `placed()` in
`figure-numbering.lua:179-189`. It would emit
`\begin{figure}[tbp]\centering <fig_inner> \end{figure}` in place of `[H]`,
and `figures.py` would need to accept the new value in its placement
vocabulary. The text after the figure then fills the page, and the figure
goes to the top of the next one. Its `@fig:` reference already says "Figure
16.2", so the reader can still find it. Add a known-good fixture whose page
ends short today.

**Press (v4, house default):** change line 242 to
`\begin{figure}[tbp]` and remove `\floatplacement{figure}{H}`
(book-header.tex:147) for numbered figures, keeping `[H]` only for
unnumbered literary plates. Verify the List of Figures and `hypcap`
destinations with pypdf, as the scars require.

**Book (now, no press change):** in `book/chapters/16-inside-the-press.md`,
move the Figure 16.2 image line (and its art comment) to after the next
paragraph, "Three kinds of input enter at the top...". About five lines of
text then fill the 133 pt on folio 274, and the figure follows. This only
fixes the page as it is broken today: any reflow earlier in the book moves the
break, and it would have to be done separately for each of the 15 pages. The
book should do it only for a final freeze, not instead of the press fix.
Shrinking 16.2 does not help unless it drops below about 100 pt.
