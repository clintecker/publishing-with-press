# Typesetter report: Appendix D

Status: clean against the markup guide. No blocks findings. 3 should findings.
`press check` passed (23 files). `press pdf` passed (no placeholder PNGs
needed; none created, none deleted). Appendix D is PDF pages 348-353.

Machine checks on `book/appendices/d-the-toolchain.md`: every fence tagged
`text` (5 of 5); longest code line 64 or less (none over); no trailing
whitespace; ASCII only; no paragraph near 190 words; footnote labels
`d-runner`, `d-colima`; heading hand-lettered with `{.unnumbered}`; no
consecutive headings; index comment last. The file has no figures, so the
figure rules have nothing to test. One table (D.1) with header, caption
after, and proportioned separator. One tip, one warning, no sidebar.

## Findings

1. Quote: "16.78 What every platform needs" (and 16.79 through 16.82, with
   16.79.1 and so on beneath them; PDF pages 348-353).
   Rule: appendix headings should not carry chapter-style numbers; press
   numbers A-heads only inside numbered chapters.
   Severity: should. This is not a typed number; press continues the
   Chapter 16 counter into the unnumbered appendix, so every appendix likely
   shows it. Not fixable in this file.
   Fix: the lead or a press-side fix; raise once for all appendices.

2. Quote: "Example D.3. The toolchain on macOS" (caption and the first line
   `$ brew install pandoc poppler` at the foot of page 341; the rest of the
   fence on page 342).
   Rule: an example caption must not be separated from its fence.
   Severity: should. The fence breaks across the page and strands one line.
   Fix: layout is page-dependent and moves with other desks' edits; re-check
   after the final build. If it persists, shorten the preceding prose.

3. Quote: "Example D.5. Building the editions inside the toolchain image"
   (caption and `$ cd ~/alice` at the foot of page 343; the `docker run`
   command on page 344).
   Rule: same as finding 2.
   Severity: should.
   Fix: same as finding 2; re-check after the final build.

Other pages: no heading at a page foot, no table wider than the measure,
no hooked code lines, and the tip and warning boxes sit whole on one page.
Page 349 shows a stretched line ("Pip from Git at a tag is the supported
channel.       Press is not pub-") from hyphenation justification; cosmetic,
not a rule violation.
