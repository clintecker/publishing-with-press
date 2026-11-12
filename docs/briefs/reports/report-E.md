# Report: Appendix E (Glossary) and the Colophon

Writer, 2026-11-11. Nothing committed. Files touched:
`book/appendices/e-glossary.md`, `book/appendices/z-colophon.md`, this report.

## Word counts (`press wordcount`)

- `e-glossary.md`: 2,931 (target about 3,000).
- `z-colophon.md`: 374 (target about 400).

## Glossary

- Heading `# Appendix E: Glossary {.unnumbered}`, one orienting sentence pair,
  then a definition list (bold term, `: ` definition), alphabetical, 145
  entries, each one to three sentences ending with the chapter(s) that treat
  the term. Entry cross-references are italic. No figures, no footnotes.
- All 75 facts-E terms are present, a few under the controlled-vocabulary
  name: "defaults template" as *defaults file*; "check the checkers" as
  *checker self-test*; "`art:` description" as *directive*; "profile seal"
  as *seal* (Ch. 12's word); "provider spec" as *provider*; "floating
  major" as *floating tag*; "edition manifest / edition_id" as one entry;
  "trust receipt / receipt chain" as one entry; "informative figure" is a
  see-reference to *figure*.
- Every term in the bible's "Terms defined" table is present, with the
  gist and chapter the bible records. Added from Ch. 9 and 12 to 16 (not
  in the bible table): art target,
  caliper, spine shape, golden copy, qualification, print ordering, seal,
  quality gate, ratchet, extension manifest, sealed capability, counsel
  mode, evidence state.
- Cut for length after a first draft of 4,400 words: allowance, bleed,
  trim, safety, digest, hash lock, logomark, registration, release receipt,
  folio. Each is defined in its chapter; restore any the editor wants.

## Colophon

- Heading changed to `# Colophon {.unnumbered}` as the brief specifies.
- Plate line and `art:` comment kept verbatim. **One change:** the stub had
  the comment on the line directly after the image, with no blank line.
  `docs/markup.md` says that form turns the plate into inline text with no
  list entry, the controller's dispatch describes the plate as "image line,
  blank line, `art:` comment", and every chapter plate has the blank line.
  I inserted the blank line. Revert if the editor meant "byte for byte".
- Paragraph 1: the brief's natural-history facts only (range, mantle about
  45 cm, eight arms and two feeding tentacles, W pupil, chromatophores,
  ink and the pigment's name, one to two years). No other figure.
- Paragraph 2: production as the brief states it, plus the logomark through
  Gemini (art report). The word "pipeline" is barred as a name by the
  vocabulary, so "the press it describes".
- Paragraph 3: type from the art report (Libertinus Serif condensed to 82
  percent, Libertinus Italic subtitle), sepia band, plus two facts from the
  art report: the series line "A Workbench Handbook" in white small caps in
  the band, and the unlettered cuttlefish facing left with no scenery.

## Contradictions and choices

1. **Manuscript witness.** facts-E 20 says every edition must carry it; the
   bible (Ch. 8 l.218) says every edition but the PDF. Followed the chapter.
2. **Lua filter count.** facts-E 12 says seven plus `press-util`; Ch. 7
   Table 7.3 lists six plus `press-util.lua`. The entry gives no count.
3. **PPI.** facts-E 40 gives PPI as pages per inch of a stock; Ch. 5 (bible)
   defines it as pixels per inch, and Ch. 12 uses `ppi-table` for pages per
   inch. The entry gives pixels per inch and notes the `ppi-table` sense.
4. **Provider names.** vocabulary lists `ingram`; Ch. 12 says `ingramspark`.
   The entry names no values, so neither is asserted.
5. **Evidence state.** Only the three live-desk glyphs (`-`, `o`, `/`, Ch. 15
   Table 15.3) appear, per facts section 20 A.19.
6. **Seller of record.** Stated as press's model with the publisher to
   confirm, per facts section 20 A.12.

## Checker

- `press check`: my two files draw nothing. A first full run passed every
  pass. A later run failed on source checks naming
  `assets/woodcuts/14-02-resolving-v3.png` and `14-03-release-state-machine.png`
  (plates never referenced), another writer's Chapter 14 work in progress.
- `tools/ste_check.py`:
  - Glossary: seven `-ing` forms, all nouns, adjectives, or names
    ("Cataloging in Publication", "floating tag", "ending in `.md`"), and
    "verify" in a quoted command name. No passive, no semicolon.
  - Colophon: line 5 findings are the untouched `art:` comment. Two passives
    ("was written", "were commissioned") are the museum-label register the
    brief dictates almost word for word. One `-ing` ("facing left").

## Revision 1 (after facts-E, copy-e, type-e and the coordinator's rulings)

Word counts now: glossary 3,054, colophon 397. `press check` passes in
full (all four passes). Nothing committed.

Applied in the glossary:
- Fact blocks: *leaf* loses the paper-column sentence (now Chapters 5 and
  10), and a new *paper column* entry (Chapter 9). *stale artifact* names the
  `press verify-formats` exception (Chapters 8 and 16).
- Fact shoulds: *design profile* (indent and leading, the width of the paper
  column, font family to the aesthetic); chapter citations for skill and
  workflow (11, 15), commerce (7, 8, 12), seller of record (3, 12);
  *fairy-dust* attribution to press; *migration* backup and receipt under
  *.press/*; *finisher* "at the time of this writing"; *glyph law* ranges.
- Copy block: "Press ships four" is now "The press carries four".
- Copy shoulds 2 to 20 and 27: line 3 note on italic filenames; actors
  named (compositing, warnings, rendering, `press illustrate`); split
  two-idea sentences; *cleared leaf* no longer italic; "a check" in
  *generator*; "the Print edition (the PDF)" at first use, then "the Print
  edition"; "print shop" in *preflight*; "Web site" in *print ordering*;
  *quality gate* rider removed; *editable install* moved before *edition*;
  craft laws say "flat plates".
- *witness* now follows the vocabulary: a text every edition carries; the
  Print edition carries the title and sentinels but no manuscript witness
  line; the page floor is left to *release witnesses*.
- Copy mays taken: 28, 29, 31, 32, 33, 36. Others left.

Applied in the colophon:
- Plate caption now "Common cuttlefish, *Sepia officinalis*" in the image
  line only; the `art:` comment and filename unchanged.
- Animal: mantle "45 centimeters ... at most, and most adults are smaller";
  sepia pigment made from the ink, pigment and genus sharing the Greek name.
- Production: diagrams by scripts with Pillow and matplotlib (no Graphviz);
  plates commissioned, taken in by intake, finished by `press art enhance`;
  cover engraving from an image model, keyed and composed by a script kept
  with the manuscript; logomark from Gemini; "group" for "squad".
- Cover: "Libertinus Serif Italic" (one face name); band and series line
  split into two sentences.

Not changed:
- `config/front-matter.yaml` (fact items 2.3 and 3.13): already corrected by
  another desk ("Source Code Pro", "the program this book describes"), and
  not my file.
- Typesetter findings 1 and 2 (running head, plate 16.1) are house behavior
  per ruling 8. Finding 3 (colophon over two pages) needs no fix.

Residual `ste_check` findings, defended:
- Colophon paragraph 1 has nine sentences: the brief asks for the opening
  sentence plus four to eight of natural history. Paragraph 2 has seven:
  every one is a production fact the brief or the rulings require.
- Passives "was made" (the pigment) and "were commissioned" (the
  coordinator's wording for the plates) are the museum-label register.
- Glossary `-ing` forms are nouns, adjectives, or proper names; "verify" is
  the verify targets' name.

## Revision 2 (sweep item 11, glossary gaps)

Added 36 entries, each from its defining chapter: Alice book and
three-chapter example (Preface); data kind, List of Figures, List of Plates
(5); folio, tokens (9); logomark, cover style, flat-ground test, author
portrait (11); allowance, trim, bleed, safety, inner offset, module, quiet
zone, disposition (12); registration (13); upload bundle, hash lock, digest,
release receipt (14); read model, prose skills, maxim quota, editorial passes
(one entry for scout, suggest, synthesize, law and the cadence, repetition,
and arc lenses) (15); integration gate, producer, producer ledger (16);
writable field, immutable field, file field (3). *structured field* and
*generatable kind* now cross-refer to the new entries in italic.

Entries: 181. `press wordcount`: 3933 for the glossary, past the brief's
3,000 at the coordinator's direction. `press check` passes in full.
`ste_check`: only the defended `-ing` forms and "verify" remain.
