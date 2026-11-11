# Production ledger

Managing editor's record. Append only.

- 2026-11-11 foundation committed (0d829e4); squad seated (e455d29).
- Wave 1 writers dispatched: ch 1, 2, 3, 4. Art director dispatched.
- Ch 2 drafted, DONE_WITH_CONCERNS: dev-render left out (not in facts);
  doctor warn state left out; `[tui]` extra spelled as "add [tui] to the
  install form"; promise to Ch 14 (toolchain digest location) logged for
  continuity. Four desks dispatched on ch 2.
- Ruling: proof figures retired from assets/woodcuts (unreferenced plates
  fail press check for every writer); the toolkit README is the API.
- Ch 2 dev edit: dev-render and the install-environment facts were missing from facts-02; supplement S1/S2 appended with a ruling (venv is the book's advice, PEP 668 is Python's, not press's).
- Ch 2 fact check: 3 contradicted, 9 unsupported, 13 drifted. Ruling: Figure 2.3's
  "wrapfig/lettrine" came from my brief (production probe), not the fact file; drop
  them, name only epubcheck and the Java wrapper. Ruling: "press doctor && press all"
  advice is wrong per the doctor's optional-tool behaviour; the chapter states the
  behaviour plainly and recommends reading the report, not chaining on its exit code.
- Ch 4 drafted (5,718 words). Rulings: sentinels are introduced in Ch 6 (the
  checker validates them) and proven in Ch 8 (the verifiers); Ch 4 points to Ch 6.
  An art: comment plus its image line is one paragraph for the 190-word law
  (markup.md updated). Process fault: my `git add -A` swept in-progress drafts;
  from now on only named files are committed while writers are active.
- Ch 1 and Ch 3 drafted. Real captures appended to facts-01 (ls dist/ after press
  all on Alice) and facts-03 (press add output, commerce block, --owner lines).
  Rulings: press all does build pages (fact base 5.3); sidebars are capped at 180
  words because the checker counts a sidebar as one paragraph; figure files are
  numbered in order of appearance. Untracked 12 placeholder PNGs the sweep had
  committed. Desks dispatched on ch 1 and ch 3.
- Art accepted (six plates, logomark, cover) and committed. Correction: the art:
  comment goes AFTER the image line (figures.py); markup.md fixed; chapters 1 to 4
  must move theirs in revision. facts-04 supplemented (examples table; tables, code,
  inline code, footnote-label scope). Press issues to file: logomark path pinned to
  gpt-image-1; illustrate always 1024 square.
- Rulings: `press wordcount` is the length measure (prose at least three quarters of
  it); the arrow and pilcrow glyphs stay verbatim inside code blocks; facts-01 S3 adds
  the full 29-line press all capture for the tour's verification step.
- facts-01 widened (S4: sections 3.1, 3.3, 2.1, 2.2, 4.1, 4.5, 12.2, 12.4; S5 rulings: slug from press new; drop cap not default).
- Ruling: code fences are capped at 64 columns. Untagged fences are plain verbatim in
  the PDF (only pandoc's Highlighting environment carries fvextra's breaklines), so a
  longer line runs off the 4.54 in measure. Long real files are excerpted with a `...`
  line. markup.md, the typesetter brief, and the chapter briefs updated. Press issue filed.
- Ruling (supersedes "untagged"): every fence is tagged `text`. Tested under the CI
  pandoc 3.1.3: a text fence becomes Shaded/Highlighting with NormalTok only (black,
  wraps with breaklines); an untagged fence is verbatim and runs off the page. 64
  columns stays the target. tools/tag-fences.py applies the tag mechanically at commit.
- Ch 6 drafted (6,167). Note from writer: the book's banned patterns read inside code fences too; writers describe banned strings rather than show them.
- Ch 7 (5,798) and Ch 8 (6,765) drafted. facts-07 gains the full press all capture with
  pandoc echoes, the pdf.yaml defaults template and its rendered copy, press wordcount;
  facts-08 gains real press verify and verify-formats runs; facts-02 gains the
  python3-venv note. Ch 2 re-review: REVISE with five mechanical items; sent back.
  Desks dispatched on ch 7 and 8.
- Wave 3 writers 9, 10, 11 dispatched; Ch 12 deferred (20-agent cap), dispatch when a slot frees.
- Correction (tested on pandoc 3.9 and the CI 3.1.3): an image followed on the next
  line by a comment is a Para, not a Figure; one blank line between restores the
  figure. Rule: image, blank line, art comment. tools/space-art-comments.py applied to
  02, 04, 05, 06, 07, 08, 15, colophon; writers of 01, 03, 09, 10, 11 instructed.
  Ch 2 Revision 2 DONE; Ch 4 re-review REVISE (4 items); Ch 5 drafted (5,772).
- Rulings: edition names are press's landing-page names (Print, Circulating, Single-leaf,
  Manuscript, Telegraphic, Office, Chapter, Source edition), glossed once per chapter;
  glyphs like the pilcrow are allowed in code blocks only, not table cells (the checker
  refuses them there). facts-06 S1: bare format targets do not run the checker; press
  all and CI do. Ch 1 revised (5,066) -> re-review.
- Rulings: banned patterns skip fenced code, fire in inline code (tested). The two
  Alices: the book's sample `alice` is the full novel; captures from press's gallery
  example (three chapters, 23 pages) are quoted as such. Chapter witness rule added to
  facts-08. Ch 3 revised (6,731) -> re-review; Ch 4 Revision 2 DONE -> continuity.
- Ruling: the slug change to `alice` covers the S1 to S3 captures when the prose labels them as the press's own three-chapter Alice example.
- Tested: a comment between a wrap and its paragraph breaks the fusion. Rulings in
  facts-05 S1 to S3; press issue #280 filed (next-line comment kills the figure; docs
  show that form; wrap + directive). Ch 2 continuity: 1 block (composite action
  wording vs Ch 3) sent to the writer as Revision 3.
- Ch 2 COMMITTED. Ch 1 re-review: five mechanical items back to the writer. Ch 10 drafted (5,095); desks dispatched.
- Footnote labels must be unique across the whole book (pandoc merges files): hypcap and libertine collide between ch 5 and ch 9. Convention from now: prefix every footnote label with the chapter number (e.g. [^5-hypcap]). Continuity editor to enforce; markup.md updated.
- Captures: press config session (set/unset print a diff; --dry-run says nothing written);
  press all succeeds with no git repository (source zip archives nothing). facts-03 S4/S5.
  Ruling: `spine` added to jargon-allow (the book means the bound edge). Ch 1 Revision 2
  DONE -> continuity. Ch 3 re-review REVISE (9) and Ch 5 desks complete -> writers.
- Ch 12 drafted (6,528); desks dispatched. Ch 4 continuity: 1 block (Figure 4.1 running head on an opening page) -> writer Revision 3.
- Ch 11 drafted (5,009); blank lines inserted before its art comments; desks dispatched.
- Ch 9 drafted (5,708); desks dispatched.
- Ch 4 COMMITTED.
- Ch 3 Revision 2 DONE -> continuity. Ch 8 revised (6,662) -> re-review. Ch 10 blank lines applied.
- Ch 5 revised (6,237) -> re-review; stale croquet-ground placeholder removed. Ch 7 revised (6,199) -> re-review. Ch 10 desks complete -> writer.
- Ruling: 'the table of authorities' is the ledger (config/authorities.yaml); 'the sources companion' is dist/<slug>-sources.md. Ch 1 continuity: 1 should -> writer, then commit. Footnote prefixes applied to ch 2 and 4 mechanically.
- Ruling: edition names apply book-wide; chapters reviewed before the ruling get it in their open revision or in the whole-book continuity sweep. Writers 14, 15, 16 dispatched.
- Ch 7 re-review APPROVED (2 shoulds: footnote prefix applied by me; edition gloss to writer, then continuity). Ch 11 desks complete -> writer. Vocabulary: art target.
- Ch 1 COMMITTED. Ch 6 re-review APPROVED (3 shoulds) -> writer, then continuity.
- Ch 8 Revision 2 DONE -> continuity. Ch 10 revised (5,148) -> re-review. Illustrator batches dispatched for ch 1, 2, 4.
- Ch 7 Revision 2 DONE -> continuity. Ch 9 and 12 desks complete -> writers. Ruling: after the once-per-chapter gloss, a sentence about the file may use the format name; a sentence about the edition uses press's name.
- Ch 3 continuity PASS; cross-chapter rulings: description "A girl falls into Wonderland."
  book-wide; Ch 1 scaffold gains --owner; Ch 6 adopts the sample's sentinels (Twinkle /
  tarts); "the book model" is the term. Writers 1, 3, 6 sent the items. Ch 6 Revision 2
  DONE; ch 7 -> continuity.
- Ch 1 final fix committed. Ch 13 drafted (3,299); desks dispatched.
- Ch 3 COMMITTED. Figures 4.1-4.3 committed. Ch 6 Revision 3 DONE -> continuity.
- Figures 1.1-3.3 committed. Ch 10 Revision 2 DONE -> continuity. Ch 11 revised (5,315) -> re-review. Appendixes A, B, C+D writers dispatched.
- Rulings (ch 8 continuity): 'the Alice book' for the full-novel sample; 'the press's own three-chapter Alice example' for the gallery; 'the Pages bundle' (dist/pages) vs 'the Pages site' (deployed); 'witness' widened. Applied in open revisions (7, 8) and the whole-book sweep for 1-6.
- Ch 9 revised (5,694) -> re-review. Ch 15 drafted (4,933); desks dispatched.
- Ruling (ch 13): in a captured block presented as what alice's run prints, metadata-derived values (author, publisher) may be the sample's own, stated as coming from the book's metadata; press's own text stays verbatim. A fresh-scaffold capture is labelled as such, never as the Alice book.
- Ch 12 revised (6,574) -> re-review; facts-12 S1 confirms the deltas from source. Ch 13 fact + copy in; typesetter pending.
- Ch 8 COMMITTED.
- Ruling: 'the three-chapter example' is the short form after first mention. Ch 7 Revision 3 DONE; awaiting its continuity pass.
- Ch 7 continuity PASS (naming items -> writer Revision 4). Ch 8: two facts from the ch 7 pass -> writer Revision 4, recommit. Whole-book sweep items: Ch 1 l.279 (press all and the commerce gate's print build); Ch 3 l.194 (rights passes through except the EPUB override).
- Ch 11 Revision 2 DONE -> continuity. Ch 16 drafted (5,646). Ch 6 continuity PASS with fixes; the 'sentinel ... not found' wording in ch 1 and 3 is wrong (checker: 'sentinel not found in the manuscript:'; verifiers: 'missing text sentinel in PDF:' / '<label> missing sentinel:'); writers 1, 3, 6 sent. Vocabulary: fail, checker self-test.
- Ch 8 fix committed. Ch 14 drafted (5,716); desks dispatching as slots free.
- Ch 1, 3 fixes committed; Ch 6 and Ch 7 COMMITTED (with figures 6.1-6.3). Ch 5 continuity: 1 block -> writer. Ruling: ornament = scene-break glyph; decoration = decorative image.
