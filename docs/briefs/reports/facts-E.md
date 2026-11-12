# Fact check: Appendix E (Glossary) and the Colophon

Fact checker, 2026-11-11. Nothing committed. Only this file touched.

Sources: `docs/briefs/facts/facts-E.md` (all of it, with the shared context and
section 20), `docs/continuity.md` (terms table and shared facts), the defining
chapters where the bible was silent or stale, `docs/vocabulary.md`,
`docs/style-guide.md` 1.7, `docs/briefs/reports/art.md`,
`art/commissions.md`, `config/front-matter.yaml`, `tools/figures/README.md`.
Where facts-E and a chapter disagree, the chapter governs.

Neither file has a code block of captured output, so there is nothing to
match character by character. The `<!-- expect: <rule> -->` form (glossary
l.147) matches facts-E 16.

Status: **blocks** (1 unsupported, 3 contradicted).

## 1. Unsupported (blocks)

1. **Colophon l.9:** "The diagrams were drawn with Graphviz and Pillow from
   scripts kept with the manuscript." At the time of this check, six diagrams
   the chapters cite have no script in *tools/figures/*: `14-01-ci-topology`,
   `14-02-resolving-v3`, `14-03-release-state-machine`, `16-01-module-map`,
   `16-02-end-to-end-data-flow`, `16-03-trust-tiers`. Their PNGs are untracked
   in *assets/woodcuts/*. (`09-03-reader-site` and `15-01-the-desk` are
   `.photo` screenshots, so "diagrams" leaves them out correctly.) The tool list
   is also short. *tools/figures/README.md* says the toolkit "Needs Graphviz
   `dot`, Python 3 with matplotlib and Pillow". Fix: write "Graphviz,
   matplotlib, and Pillow", and recheck at lock that every diagram has its
   `fig-*.py`. Otherwise soften to "most of the diagrams". Other desks are
   still adding scripts (09-01, 09-02, and 15-02 appeared during this check),
   so this item may close by itself.

## 2. Contradicted (blocks)

1. **Glossary l.240, leaf:** "On the reader site, the leaf is the paper column
   (Chapters 5 and 9)." Chapter 9 no longer uses the word that way. Its l.152
   defines "its *paper column*, the framed column that holds the text on the
   reader site", and `docs/vocabulary.md` l.64 bars "the leaf" for that column.
   The bible's open finding (continuity-05 B, continuity-09 finding 1) has been
   resolved in Chapter 9's favour. Fix: cut the sentence, cite the leaf to
   "Chapters 5 and 10" (Chapter 10 uses the trade sense, l.31 and l.420), and
   add a *paper column* entry (see Missing 1).
2. **Glossary l.387, stale artifact:** "The registry's edges make every verify
   target rebuild first, so the command line never verifies one (Chapters 7 and
   16)." The chapter it cites says otherwise. Chapter 16 l.78: "There is one
   exception. `press verify-formats` reads an existing *dist/alice.pdf* into its
   cross-edition agreement check without rebuilding it". Chapter 16 l.178 and
   the bible's "no-stale law" row say the same. That row also records Chapter
   7's exception-free statement as a conflict (continuity-08 finding 3), and
   the entry copies the Chapter 7 version. Fix: "The registry's edges make
   every verify target rebuild what it verifies first. The one exception is
   `press verify-formats`, which reads an existing PDF into its agreement check
   (Chapters 8 and 16)." The defining chapter is 8 ("The no-stale law", l.429).
3. **config/front-matter.yaml l.19, `colophon-note`:** "Set in Libertinus Serif
   and Libertinus Mono". The house sets code in Source Code Pro, not Libertinus
   Mono: Chapter 9 Table 9.2 l.72 ("Monospace | Source Code Pro, scaled 0.86"),
   Chapter 4 l.231, and the bible's "House type" row. The book's own Colophon
   (l.9) says "the code face is Source Code Pro". The copyright page and the
   Colophon would contradict each other in print. Fix: "Set in Libertinus
   Serif and Source Code Pro by pandoc and LuaLaTeX ...".

## 3. Drifted (should)

1. **Glossary l.114, design profile:** "trim, margins, *height cap*,
   typography, and Web measure". Chapter 9 l.135 (bible row) lists "a trim,
   four margins, a height cap, an indent and leading, and a Web column width".
   It adds that "font family and palette belong to the aesthetic". The word
   "typography" claims the face for the profile. Fix: replace "typography" with
   "indent and leading".
2. **Glossary l.372, skill (Chapter 15):** the bible gives Chapter 11 (l.47) as
   the defining chapter, and Chapter 15 l.277 agrees. Fix: "(Chapters 11 and
   15)".
3. **Glossary l.435, workflow (Chapter 15):** Chapter 11 l.49 defines the term
   first ("the `art-direction` *workflow*, a packaged agent procedure"). Fix:
   "(Chapters 11 and 15)". The gist matches Chapter 15 l.26.
4. **Glossary l.87, commerce (Chapters 8 and 12):** the entry defines the gate,
   and the bible's "commerce gate" row gives Chapter 7 as its home (l.424,
   A-head). The bible also notes that the gate builds print and coverwrap and
   is advisory unless `PRESS_RELEASE=1`. Fix: "(Chapters 7, 8, and 12)". The
   gate details are optional.
5. **Glossary l.363, seller of record (Chapter 3):** Chapter 12 l.480 treats
   the term at length ("The press's model is that the provider sells the copy
   ... confirm it before you publish the link"). Fix: "(Chapters 3 and 12)".
6. **Glossary l.156, fairy-dust:** "Tenniel's 1866 array" is stated as fact.
   Chapter 4 l.325 attributes it: "Press describes it as Tenniel's 1866
   array." Fix: "eleven asterisks in rows of four, three, and four, which press
   describes as Tenniel's 1866 array".
7. **Glossary l.261, migration:** "which rewrites the press pins and touches
   nothing else". Chapter 14 l.406 says "The target changes only the pin, and
   only in two places". l.420 says `apply` also writes
   *.press/migration-backup.json* and *.press/migration-receipt.json*, and the
   plan "leaves the manuscript, the config, and the accepted art alone". Fix:
   "which rewrites only the press pins, after an exact backup, and leaves the
   manuscript, config, and art alone".
8. **Glossary l.165, finisher:** "It is not part of press 3.0.2". The bible's
   cast rule pairs the version with "at the time of this writing". Fix: "At
   the time of this writing it is not part of press (3.0.2)". Alternatively,
   keep the immutable version and add the phrase.
9. **Glossary l.186, glyph law:** "ASCII and the accented Latin letters". The
   law admits tab, LF, CR, and U+0020 to U+007E (Chapter 4; bible "Glyph law
   ranges"). That is not all of ASCII: no other control characters, no DEL.
   Chapter 6 l.194 uses the same loose phrase, and the bible accepts it there,
   so this one is low priority. Fix: "printable ASCII with tab and line ends,
   and the accented Latin letters, U+00C0 to U+017F".
10. **Colophon l.9:** "the press's own intake finished each one." The art
    report says otherwise for two of the three kinds of art:
    - The cover engraving was keyed ("ground >= 246 clear") and composed
      outside the press, by *tools/cover.py* in Pillow. Only the finished
      *front.png* went through `press art accept --as cover`.
    - The plates were finished by `press art enhance`, after intake.

    Fix: "and each one came into the book through the press's own intake,
    with `press art enhance` finishing the plates". You could also name the
    cover composer (see Missing 6).
11. **Colophon l.7:** "its mantle grows to about 45 centimeters." Read as a
    typical size, this is wrong. About 45 cm (some references give up to 49
    cm, in warm waters) is the recorded maximum. Most adults are far smaller,
    around 15 to 25 cm in temperate waters. Fix: "its mantle can reach about 45
    centimeters, though most adults are much smaller".
12. **Colophon l.7:** "the brown pigment sepia takes its name from that ink."
    The pigment was made from the ink, but the name belongs to the animal:
    Greek *sēpia*, cuttlefish, which is also the genus *Sepia*. Fix: "and the
    brown pigment sepia, once made from that ink, takes its name from the
    animal".
13. **config/front-matter.yaml l.20, `colophon-note`:** "press 3.0.2, the
    pipeline this book describes". `docs/vocabulary.md` l.10 bars "the pipeline
    (as a name)" for press. The Colophon already says "the press it describes".
    Fix: "press 3.0.2, the press this book describes".

## 4. Missing (may)

1. **paper column** (Chapter 9 l.152; vocabulary l.64). This entry is needed
   once Contradicted 1 is fixed.
2. **logomark** (Chapter 11 l.448: the imprint's mark, *assets/press-logo.png*,
   ink on transparency). The Colophon (l.9) and the *art target* entry both use
   the word, and the writer cut it for length.
3. **Lua filter count.** Chapter 7 l.82 and Table 7.3 give six filters plus
   *press-util.lua*. The entry gives no count. That is safe, but "six" is now
   supportable from the chapter.
4. **Other bible terms with no entry:** tokens (9), cover style (11),
   flat-ground test (11), author portrait (11), binding and cover material
   (12), trim and bleed (12), safety (12), inner offset (12), module and quiet
   zone (12), researched provider and disposition (12), folio (9), allowance
   (12). Trim and bleed appear inside other entries (cover wrap, craft law,
   design profile). The writer's report lists the ones cut for length.
5. **Directive keywords.** Glossary l.120 names only `art:`. The bible's
   "Image, blank line, art comment" row says the keyword may be `art:`,
   `data:`, or `source:`.
6. **Colophon against style guide 1.7.** The animal paragraph has range, size,
   anatomy, color change, ink, and lifespan. It has no diet or habits, and no
   conservation status, which the guide says "often" appears. All are general
   knowledge: it ambushes crustaceans and small fish, and it is listed as Least
   Concern (verify the current IUCN listing before adding). Several structural
   parts are also absent: the series boilerplate opening (item 1), the
   production and index credits (item 3), the cover-layout tool (item 4:
   *tools/cover.py*, Pillow), and the closing credit line (item 7). These are
   for the editor, not errors.

## Verified (no finding)

- **Colophon natural history.** Each of these is right: the eastern Atlantic
  and Mediterranean range; eight arms and two longer feeding tentacles; the
  W-shaped pupil; chromatophores as pigment sacs that muscles open and close;
  the ink cloud under threat; the one-to-two-year lifespan.
- **No link between animal and software.** The animal paragraph (l.7) draws
  none, as the style guide requires.
- **Colophon cover type (l.11)** matches art.md:
  - Libertinus Serif condensed to 82 percent for the title, and Libertinus
    Italic for the subtitle.
  - A sepia band (`#4a2e1a`) carrying "A Workbench Handbook" in white small
    capitals. Art.md says these are built from capitals at 74 percent, which
    is fair to call small capitals.
  - The engraving beneath the title: the cuttlefish alone, facing left, with no
    scenery.
- **Logomark.** "from Gemini" matches art.md, which records the
  `--model gemini` commission and the acceptance of `gemini-2.png`. The
  Acceptance record in *art/commissions.md* l.27 to 34 lists six plates, the
  cover, and the logomark.
- **Faces and version.** Text face Libertinus Serif and code face Source Code
  Pro match Chapter 9 Table 9.2. "press 3.0.2" matches `colophon-note`.
- **Glossary entries.** All other entries agree with the bible's gist and
  name a chapter that treats the term. This includes every number checked: 19
  fixtures, 53 watchlist terms, eight editions, six profiles, four craft laws,
  eleven skills, four workflows, eleven checklist points, twelve layers in
  three tiers, five sealed capabilities, the 190-word law, the 225/45 key,
  the 6.3 in cap, the 24-page release floor, and the three live-desk glyphs
  (Chapter 15 Table 15.3).

## The writer's three facts-E conflicts (report-E)

1. **Manuscript witness ("every edition but the PDF").** The writer is right.
   Chapter 8 l.218 and the bible's "Per-edition witnesses" row agree: "the PDF
   carries title and sentinels, not the manuscript witness". facts-E 20 is
   wrong.
2. **Lua filter count (no count given).** The writer is right. Chapter 7 gives
   six filters plus *press-util.lua*, where the sixth is *print-safe-images*
   in the print chain. facts-E 12's "seven" has no support in the chapter.
   "Six" could now be stated (Missing 3).
3. **PPI (pixels per inch, with the `ppi-table` note).** The writer is right.
   Chapter 5 l.343 governs the abbreviation. Chapter 12 l.96 calls the
   `ppi-table` figure "a pages-per-inch figure" and uses "PPI" itself only for
   pixels (l.265 to 291). The entry's second sentence rests on facts-E 40 and
   the shape's own name, which is acceptable.

The writer's cases 4 to 6 (provider names, evidence glyphs, seller of record)
are also handled correctly.

## Worst finding

Contradicted 3: `config/front-matter.yaml` sets the copyright page's
`colophon-note` to "Libertinus Serif and Libertinus Mono". The house code face
is Source Code Pro (Chapter 9 Table 9.2), and the book's own Colophon says so.
The printed book would name two different code faces.
