# Desk brief: indexer

You build `config/index-terms.yaml` from the index candidates each chapter
left in its last line (`<!-- index: ... -->`) and from your own reading.
Read `docs/briefs/facts/facts-10.md` section 9.2 for how the index works:
flat terms, literal whole-word matches, case-insensitive, code spans and
blocks and image lines stripped, a zero-hit term fails the build, locators
are chapter numbers.

1. Collect every candidate. Merge duplicates and near-duplicates (singular
   and plural become one term with two `match` entries). Decide the
   reader's lookup form: lowercase except proper nouns; commands and
   filenames as they are typed (`press check`, `metadata.yaml`); concepts
   as nouns ("sentinel", "drop cap", "house rules").
2. For a concept with sub-aspects, make flat compound terms the way a
   period index would: "figures, numbering of"; "figures, placement of".
3. Add "see" entries as terms whose `term` reads "runaround (see wrap)"
   and whose `match` is the alias, so the reader who looks up the alias
   finds the pointer.
4. Aim for 180 to 260 terms. Every term must match prose somewhere, so for
   each term grep the chapters outside code and image lines before you
   keep it; press will fail the build on a miss.
5. Write the file, then run `~/code/.pwp-venv/bin/press check` and
   `~/code/.pwp-venv/bin/press pdf`, and read the generated index appendix
   in the PDF: look for terms that landed in a chapter they should not
   have (a common word matching the wrong sense) and tighten their
   `match`.
6. Remove the `<!-- index: ... -->` comments from the chapters once the
   file is complete.

Report in `docs/briefs/reports/index.md`: the count, the terms you cut and
why, any term whose matching is loose. Do not commit.
