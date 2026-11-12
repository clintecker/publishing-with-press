# Typesetter report: Chapter 13, Registrations

Status: builds clean; 0 blocks, 4 should. `press check` passed (exit 0,
"Source checks passed: 23 ordered Markdown files"; the known-bad notes
name only fixtures). `press pdf` passed (exit 0) once placeholder PNGs
stood in for missing figures; they were deleted afterward (see Notes).

## Blocks

None. Construct by construct: the "In this chapter" box lists the nine
A-heads exactly; six tips and warnings (three of each, under the
cap of eight) and one sidebar (163 words) use the Div
form with bold lead; examples 13.1 to 13.5 each have a bold caption
directly above a `text` fence; the no-caption fence at line 217 is one
line; no code line exceeds 64 columns; no trailing whitespace; no
non-ASCII; tables 13.1 to 13.4 have header, long separator, and caption
after; footnotes `13-isbn10`, `13-earth`, `13-agent` are unique and
prefixed; the figure has the `art:` comment after the image with one
blank line, path `13-01-where-numbers-land.png`, `#fig:where-numbers-land`,
`.diagram`, `width=full-measure`, `fig-alt` unlike the caption, caption
in sentence case without a period, `@fig:` cited just before it; the
index comment is last. The figure is a data-flow with one source and
five destinations (about 6 elements per side), within the 1740 px cap;
placement is the default inline, which is correct for a diagram.

## Should

1. Quote: the Element column of Table 13.3 (`| Element | Value | Meaning |`
   with separator `|----------------------|------------------------|...`).
   Rule: PDF layout; constant-width identifiers must not hyphenate.
   In the PDF they break mid-word: "Sender/Sender-Name", "RecordRefer-ence",
   "ProductIdenti-fier", "PublishingSta-tus". Severity: should.
   Fix: widen the Element column and narrow Value in the separator row
   (for example `|--------------------------------|----------------|-----------------------------|`).
2. Quote: "*dist/alice.onix.xml*" (line 189) and
   "`registrations.isbn.epub`" (line 90).
   Rule: PDF layout; a filename or key that hyphenates mid-token misleads
   a reader who copies it. The PDF shows "dist/al-ice.onix.xml",
   "registra-tions.isbn.epub", and "hy-phenates". Severity: should.
   Fix: reword so each token falls mid-line, for example move "to
   *dist/alice.onix.xml*" earlier in the sentence, and name the two keys
   in separate sentences so neither lands at a line end. Recheck the PDF.
3. Quote: Table 13.2 (line 121 to 128).
   Rule: PDF layout; a table should not strand one row. The LCCN row
   alone sits at the head of the next page (PDF pp. 226 to 227). Tables
   13.3 and 13.4 also split across pages, with a repeated header, which
   is acceptable. Severity: should.
   Fix: tighten the text before Table 13.2 or shorten the Meaning cells
   (the ISBN-13 cell is four lines) so the table fits; the break moves
   with every earlier edit, so recheck after the copy desk's changes.
4. Quote: "shows the routes." (line 246), the figure paragraph.
   Rule: PDF layout; Figure 13.1 floats to the next page and leaves
   roughly a third of PDF p. 231 blank under heading 13.8. The figure is
   a placeholder here, so the real height decides. Severity: should.
   Fix: none now; recheck once the illustrator's art is in. If the gap
   persists, move the first paragraph of 13.8 so the figure follows a
   longer run of text.

## Notes

- Not seen as faults: no heading at a page foot, no table wider than
  the measure, no code line wrapping with a hook, no box running over a
  page, every example caption sits with its fence.
- Advisory only (outside the markup law): `tools/ste_check.py` flags the
  sidebar (11 sentences, max 6), the semicolon in the quoted PCN message
  (line 175, line 221), and a few passives. These are the copy desk's.
- A first `press pdf` attempt failed on missing figure files; other desks
  were building in the same tree at the same time, and one build logged
  "libpng error: Read Error" while still exiting 0. I created 1362 by 800
  white PNGs for every referenced figure missing at build time and
  deleted the 23 that were still my placeholders afterward (the rest had
  been replaced by real art or other desks' files, and I left them).
- Other files: no `press check` failure named another file.
