# Re-review: Appendix E (Glossary) and the Colophon

Fact checker, 2026-11-11. Nothing edited except this file; nothing committed.
Scope: the blocked and Drifted items of `facts-E.md`, plus the coordinator's
witness reconciliation.

Verdict: **REVISE**, one open item (W1 below). Every other item is resolved.

## Blocked items

- **U1, diagram tools.** Resolved. Colophon l.9 now reads "Scripts kept with
  the manuscript drew the diagrams with Pillow and matplotlib." Every numbered
  figure the chapters cite has a `tools/figures/fig-*.py` script or a captured
  `.txt`. The two exceptions, `09-03-reader-site` and `15-01-the-desk`, are
  `.photo` screenshots, so they are not diagrams. No `fig-*.py` calls
  `render_dot`, so leaving out Graphviz is correct.
- **C1, leaf.** Resolved. The leaf entry (l.239-240) cites Chapters 5 and 10
  and no longer mentions the reader site. A *paper column* entry (l.281-282,
  Chapter 9) has been added, and the design profile entry uses it.
- **C2, stale artifact.** Resolved. The entry (l.389-390) names the
  `press verify-formats` exception and cites Chapters 8 and 16.
- **C3, front-matter code face.** Resolved. `colophon-note` now reads "Set in
  Libertinus Serif and Source Code Pro". "the pipeline this book describes"
  is now "the program this book describes", which also clears D13.

## Drifted items

| # | Item | Status |
|---|---|---|
| D1 | design profile: "typography" | Resolved: "indent and leading", and "The font family belongs to the *aesthetic*" |
| D2 | skill citation | Resolved: Chapters 11 and 15 |
| D3 | workflow citation | Resolved: Chapters 11 and 15 |
| D4 | commerce citation | Resolved: Chapters 7, 8, and 12 |
| D5 | seller of record citation | Resolved: Chapters 3 and 12 |
| D6 | fairy-dust attribution | Resolved: "which press describes as Tenniel's 1866 array" |
| D7 | migration "touches nothing else" | Resolved: "rewrites only the press pins", with the backup, the receipt under *.press/*, and the manuscript, config, and art left alone |
| D8 | finisher version | Resolved: "At the time of this writing, it is not part of press 3.0.2" |
| D9 | glyph law "ASCII" | Resolved: "printable ASCII with tab and line ends" |
| D10 | colophon intake | Resolved: plates go through intake and `press art enhance`; a script kept with the manuscript keyed the engraving and composed the cover |
| D11 | mantle size | Resolved: "It reaches 45 centimeters in mantle length at most, and most adults are smaller." |
| D12 | sepia etymology | Resolved: "The pigment sepia was made from that ink, and the pigment and the genus share the Greek name for the cuttlefish." |
| D13 | "pipeline" in front-matter | Resolved (see C3) |

The animal paragraph still draws no link to the software. The new
natural-history wording is correct.

## Open item

**W1, witness (glossary l.434-435).** The entry now reads: "A text the
verifiers require every edition to carry: a *sentinel*, the title, the
*manuscript witness* line, or a *chapter witness* line."

This narrows the class that Chapter 8 defines. Chapter 8 l.400 says "The
press calls them all witnesses", and its Table 8.6 (l.402-409) has a fifth
row, "Page floor | The PDF | The count `verify-min-pages` sets proves that the
PDF is not a fragment of the book." The page floor is not a text, and only the
PDF carries it, so "a text ... every edition [must] carry" leaves it out.
Chapter witnesses are also checked in "The reader site and the agreement
check" (Table 8.6), which is not the same as every edition carrying them.

Fix, in Chapter 8's terms: "Any evidence a verifier requires: the
*sentinels*, the title, the *manuscript witness*, the *chapter witnesses*, and
the *page floor* (Table 8.6). The Print edition carries the title and the
sentinels but no manuscript witness. See also *release witnesses* (Chapter
8)."

The manuscript witness entry (l.254-255, "Every edition but the Print
edition") and the chapter witness entry (l.68-69) are now consistent with
Chapter 8.
