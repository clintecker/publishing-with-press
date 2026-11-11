# Desk brief: production editor

You take the finished manuscript, figures, plates, and cover through the
press's own toolchain image and read what comes out. The native build is
for quick looks; the image is the truth (it has epubcheck and the complete
TeX). Read `docs/design.md` section 10 and the build notes in
`docs/squad/build.md`.

1. Commit state check: `git status` clean except your own `build/` and
   `dist/`. The source edition is packed from the git index, so an
   uncommitted file is absent from it.
2. Build everything in the image: `tools/docker-build.sh . build/docker all
   verify-print coverwrap` (the script streams the book in and `dist/`
   out). Keep the full log. Any verifier failure is a blocks finding with
   the message quoted and the file and line it points at, if any.
3. Render: `~/code/.pwp-venv/bin/press render` natively, then read every
   page image under `build/rendered-book/` (there will be about 320; read
   them in runs of ten). Record, with page numbers: a heading at a page
   foot with no text under it; a widow or orphan line; a figure separated
   from the paragraph that introduces it by more than a page; a table
   broken across pages or wider than the measure; a code block that wraps
   or overflows; a blockquote box split across pages; a caption separated
   from its figure; a plate on a recto when it should face a chapter; an
   empty or nearly empty page; a List of Figures or Plates entry whose
   page number is wrong (spot-check ten); a running head that does not
   match the chapter.
4. Open `dist/site/index.html` and five chapter pages in a headless Chrome
   (`scripts/check_layout.py` in the press checkout shows how) at 1280 and
   390 px wide; record anything that overlaps, overflows, or hides.
5. Open `dist/publishing-with-press.epub` in the toolchain's epubcheck
   (already run by the build) and note its report; read three chapters'
   XHTML for the classed boxes and the figure captions.
6. Check the print pack: `dist/publishing-with-press-interior.pdf` (black
   ink, mirrored margins, the verifier's report) and the cover wrap (spine
   width against the page count, barcode placeholder, the front matching
   `assets/cover.jpg`).
7. Report in `docs/briefs/reports/production.md`: the build log summary,
   the page-by-page fault list with the smallest fix for each (most are a
   sentence added or cut by the writer, a figure moved a paragraph, or a
   `place=plate` added; never a change to press), and the Web and EPUB
   notes.

Do not edit chapters. Do not commit.
