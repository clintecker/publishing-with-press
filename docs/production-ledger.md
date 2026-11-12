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
- Ch 10 COMMITTED. Ch 3 errata (sources companion) applied to prose and Figure 3.3. Figures 5.1-5.3 drawn, awaiting ch 5's final commit.
- Ch 5 COMMITTED with figures.
- Figures 8.1-8.3 committed. Appendix B and C+D drafted; desks dispatching (fact-b, fact-c running).
- Ch 12 Revision 2 DONE -> continuity. facts-14 S1/S2 added for the ch 14 revision.
- Figures 7.1-7.4 and 10.1-10.2 committed. Appendix E + colophon writer dispatched; remaining appendix desks dispatched.
- Ch 16 desks complete -> writer. Appendix B fact-check in (1 contradiction: retail entry), Appendix D fact-check in; facts-D S1 rulings added.
- Ch 11 COMMITTED. Ch 15 desks complete -> writer. Appendix C fact-check in.
- Rulings: appendix ## and ### headings carry {-} (press numbers them 16.71...; tool added); long message terms go into text fences; provider id is ingramspark. Appendix B and C desks complete -> writers.
- Appendix A drafted (5,551). Ruling: a writer's own capture from press 3.0.2 on a scratch book is admissible as fact (the fact base is the same kind of capture); the fact checker verifies it by rerunning where cheap. Desks dispatched for A.
- Rulings (ch 9 continuity): 'leaf' keeps the trade sense; the reader site's column is 'the paper column'; 'height cap' is the term, 'figure-cap' the key; Figure 9.2's blank cells may be filled from facts the fact base states elsewhere (facts-12 profile uses; widths derived from Table 9.4's trims and margins) and left blank otherwise. Ch 14 and Appendix D desks complete -> writers.
- Ch 9 COMMITTED. Ch 13 Revision 2 DONE -> re-review. Ch 12 continuity: 1 block (Ch 5 title), logomark naming, figure order -> writer.
- Figures 11.1-11.3 committed (alt text aligned). Appendix B COMMITTED. Ch 15 revised (5,146) -> re-review.
- Figure 13.1 committed. Ch 16 revised (5,679) -> re-review.
- Ch 12 COMMITTED (figure files renamed by the writer: 12-01 spine math, 12-02 wrap, 12-03 graph; the illustrator's output will be renamed to match). Preface (2,401) and Appendix E (2,931) + colophon (374) drafted; desks dispatched.
- Appendixes C and D COMMITTED.
- Ch 14 revised (5,633) -> re-review. Ch 15 re-review APPROVED (3 shoulds -> writer). Appendix A typesetter in.
- Ruling: 'Press' capitalised only at a sentence start (ordinary English); otherwise lowercase; the command always constant width. Appendix A copy in; fact pending.
- Ch 16 re-review APPROVED (2 shoulds -> writer). Ch 14 re-review REVISE (1 block: CHANGELOG section must follow the v1.0.1 retag; 1 should -> writer). Preface fact and copy in; typesetter pending. Figures 9.1-9.2 in (09-03 is the screenshot desk's).
- Rulings (preface): the "Using code examples" section restates the rights notice in config/front-matter.yaml and grants nothing beyond it; commas stay outside closing quotes book-wide (literal strings must survive quoting; Chapter 1 set the pattern); dates stay ISO (2026-07-17) book-wide.
- Ch 13 continuity: 1 block (ISSN does not print on the copyright page; line 273, art brief, and Figure 13.1 corrected by the managing editor); retail rule overstated in Ch 3 l.265 and Ch 6 l.62 (fixed). Ruling: facts-03 S5 was wrong; a book outside any Git repository is archived whole, one untracked inside a parent repository archives nothing (retested by the managing editor); Ch 3 l.566, facts-03, and Appendix A corrected. A tool rewrite of Chapter 4's fenced footnote example reverted. Five stray placeholder plates named by Chapter 5's fenced examples removed.
- Figures 14.1-14.3, 15.2, 16.1-16.3 committed. Colophon note now names Source Code Pro. Preface desks in (0 blocks; {-} on its ## heads). Appendix E and colophon desks in (fact blocks: leaf/paper column, stale artifact exception, sepia etymology, 45 cm is a maximum). Appendix A desks in -> writer. Ch 14 and 16 -> continuity.
- Ch 14 continuity PASS (0 blocks). Rulings: "the Pages site, the Web site that GitHub Pages serves" is a gloss, not a name, and stands in Ch 7 and 14; Ch 2 says Ubuntu manages the image's Python; Ch 16 uses "upload bundle"; design.md rows 12 and 14 now list figures in appearance order. Screenshots 9.3 (two crops of the three-chapter example's chapter 1, torn-edge gap) and 15.1 (slug alice, inset picker) accepted. Ch 14 COMMITTED.
- Ch 16 continuity PASS (0 blocks; Ch 5 footnote reworded, Ch 16 "deploys the Pages site", Ch 15 footnote to say "the adapters gate" -> writer). Ch 15 continuity: 1 block (press pdf does not verify) -> writer. Appendix A revised (5,728) -> fact re-review. Preface revised (2,440) + blurb fixes for 14 and 15 -> writer. Ch 16 COMMITTED.
- Ch 15 revised (5,203; adapters gate footnote fixed by the managing editor) COMMITTED. Preface revised (2,463) COMMITTED; the whole-book sweep rechecks its Organization section against the final titles.
- Appendix A re-review APPROVED (unzip warning replaced by press's own line) COMMITTED. Appendix E (3,054) and colophon (397) revised -> fact re-review. Indexer dispatched.
- Appendix E re-review: witness entry widened to include the page floor (Chapter 8 governs; vocabulary updated). Appendix E and the colophon COMMITTED. Sentinels set ("You do not choose the witness", "On a fresh scaffold it succeeds", "the selftest skips the checks"); verify-min-pages 300 (last native build: 375 pages).
- Index: 249 flat terms in config/index-terms.yaml, zero zero-hit, index comments stripped from chapters 00-16. Ruling: long-locator core terms (14-17 locators) stand; the index regenerates each build. COMMITTED. Whole-book continuity sweep dispatched.
- Sweep COMMITTED (87 edits). Rulings on its 15 open items: index among the appendixes by its own letter (Ch 3 governs; Ch 4 fixed); Ch 16 names the commerce-gate exception; wrap placeholder "not declared for retail"; adapters timeout 30 s by default, lookup 10 s (both facts); "the press's own profile descriptions"; aesthetic.yaml "has no typed model of its own"; "a book normally lives in a Git repository"; desk Table 15.3 keeps the desk's words; an appositive edition gloss is allowed (vocabulary); Ch 1 states no retail rule (fine); glossary gaps -> glossary writer; Preface blurbs stand; appendix index comments stripped; Ch 5 names the figure-cap key; "What Git has to do with it"; "the imprint device". Prose audit (56 shoulds, 0 blocks) -> fixer, sentinels verbatim.
- Prose audit applied (44 fixes; first-law quotation and CLAUDE.md quotes left verbatim; sentinels intact) COMMITTED. Glossary 181 entries COMMITTED. Production editor dispatched: toolchain-image build of all, verify-print, coverwrap; page read.
- Final reader review: 1 block (Example 11.3 inner fences), 17 shoulds, and the structural fault: 29 facts retold across chapters, 18 counted quotations, 17 "plainly", 30 "fit the page" asides, closers above two per chapter. Ruling: a cutting pass per docs/briefs/cutting-brief.md (keeper chapter keeps the telling; others point or cut); code rulings: commissions run when asked, Table 10.4 follows Chapter 13, a bare image is kind figure, the accent token exists. Fifteen cutters dispatched; rebuild and proofread follow.
- Cutting pass COMMITTED: 21 files, every brief entry applied (cutters replaced the brief's semicolons with periods or ", and"); sentinels intact. Production report (red): B1 tilde subscript, B2 witness line with @fig:, B3/B5 raw angle brackets and -- in art comments break EPUB and drop print text, B4 Appendix C long terms at page edge, S2-S8 -> fixer; press defects filed as #281 (witness picker) and #282 (running heads on unnumbered chapters).
- Production fixes COMMITTED: B1-B5, S2, S3, S5, S6, S8, Ch 11 repeat; angle-bracket paths and `--` art comments now code spans, tildes escaped, two B-heads renamed (no heading attributes allowed), Figure 13.1 moved after its reference. Declined: S4 (Appendix C lead-ins at page foot; needs keep-with-next in press), S7 (phone-width tables; press webmeta matches only bare `<tr>`, filed), S1 (#282). Image: verify, verify-print, verify-formats and epubcheck exit 0; 385/384 pages. Second full image build and proofread next.
- Production report 2 (red on the page read, every verifier green: 385/384 pages, sentinels and floor pass, spine 0.960 in, epubcheck pass). Blocks: `*__main__.py*` read as bold, two table cells overprinting (13.3, A.20). Shoulds: 64-column code lines wrap (63 fits; Ch 4 tip to say 63), two Appendix C terms past the measure, Chapter 1 heading alone before its frontispiece, six stranded example captions, two near-empty pages, seven half-empty pages before floats, seven stranded table heads, four phone-width prose overflows. Rulings: frontispiece moves to the end of the Preface (plates are unnumbered); "[ISBN pending]" is press's own wording and stands; art comments shipping in EPUB/HTML is accepted. Press defects filed: #283 (table-cell labeller matches only bare `<tr>`), #284 (frontispiece at a chapter head strands the heading), #285 (render keeps stale page images). Fixer dispatched; third image build and proofread follow.
- Author's notes on the second build (2026-11-12): the 11.5 percent sidebar expanded from CHANGELOG 2.1.0 and verify_pdf (the front-matter trigger, the fixed 5.6x7.1 in plate, the page-1 check and its two refusals; facts-01 S20 extended with sources); the sidebar must stay under 190 words because the checker counts a blockquote as one paragraph. Section 1.8 "How to read this book" was a stub left by the cutting pass (the brief cut the body as a retelling of the Preface's Organization section but the cutter kept the heading): heading removed, the forward pointer closes the chapter. Fixer resumed after a reboot.
- Report 2 fixes COMMITTED (0f69a5b, f10d4d6): B1-B3, S1, S3 (no fenced line over 63 columns; Ch 4 tip says 63), S4, S8, page fitting for S2/S5/S6/S7 on the native render (Tables 3.5, 4.1, 6.5, 12.11 keep two rows with their head: accepted); `{base}/` `{slug}-{label}` split at the slash; the S8 footnote names the URL first so LuaLaTeX cannot hyphenate it. Native render 380 pages. The two remaining prose semicolons (Ch 7, Ch 8, the Source archive sentence) made into two sentences. Press #286 filed: keep a table head with its rows and a definition term with its definition. Third image build dispatched (report production-3.md); proofreader follows on green.
- Third image build: all editions green (381 pages, sentinels, floor, epubcheck, spine) except verify-print: "apparently blank rendered pages: [17]". A frontispiece clears to an even page, and the cover shifts the reading PDF one page against the interior, so a frontispiece placed at the end of the Preface puts a blank page in whichever edition lands on the wrong parity. Ruling: the plate sits after Chapter 1's orientation paragraph. The opening recto holds the heading, the box, and the paragraph, the plate takes the facing verso in both editions, and the text resumes on the next recto. Native verify-print passes (380 pages). The stale "How to read this book" bullet left the chapter box. Added to press #284.
