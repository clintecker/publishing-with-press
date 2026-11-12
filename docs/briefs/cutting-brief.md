# Cutting brief

One editor per chapter. Each list below is complete for its chapter, so an
editor need not read any other chapter to act. Quotations are exact from
the files as of 2026-11-11; `NN:LL` is chapter file and line. "Pointer"
means replace the cut with the one clause given. "Cut outright" means
delete and let the surrounding sentences close up. Nothing in this brief
changes a fact; it removes second tellings, three verbal tics, and the
paragraph-closing maxims above the quota of two per chapter.

Rules every editor applies:

- A fact is told in full once, in the chapter whose subject it is (the
  keeper). Every other telling becomes a pointer or goes.
- A quotation is introduced without counting its words.
- "plainly", "says so plainly", "is plain about", "puts it plainly" go.
- A message shown on several lines carries no aside about the page. The
  Preface will say once: "A message shown on more than one line in this
  book is one line in the terminal." (Preface editor: add that sentence to
  the `...` convention at `00:110`.)
- At most two coined closing maxims per chapter. A cut maxim either lets
  the paragraph end one sentence earlier or folds its fact into the
  sentence before it; each entry says which.

## 1. Retold facts

Format: **fact** (keeper). Then, per other chapter: `file:line`, the
sentence or paragraph, the action.

**The `press verify-formats` exception to no-stale** (keeper: Chapter 8,
section "The no-stale law", `08:429-439`; keep `08:433` and `08:439` there,
and cut the earlier mention in the same chapter).

- `06:473` "Press also declares dependency edges between its targets. Each
  verify target rebuilds what it verifies before it inspects it, so a
  verifier does not bless an edition that the current manuscript did not
  produce. The one exception is `press verify-formats`, which includes an
  existing Print edition, *dist/alice.pdf*, in its cross-edition agreement
  check without rebuilding it. Chapter 8 describes the edges target by
  target." Cut to: "Each verify target rebuilds what it verifies before it
  inspects it, with one exception that Chapter 8 explains."
- `07:339` last two sentences, "Every verify target rebuilds the artifacts
  it verifies before it verifies them, and the command line offers no way
  around that. The one exception is `press verify-formats`, which reads an
  existing *dist/alice.pdf* into its cross-edition agreement check without
  rebuilding it." Keep the first; replace the second with "(one exception,
  Chapter 8)".
- `07:341` "The press records this as an *invariant* ... Code that imports a
  verifier module directly skips the rebuild." and the warning at `07:343-345`
  "Do not call a verifier module from your own script to save time." Cut
  the warning outright; keep the invariant sentence.
- `08:210` last sentence, "Its last check confirms that all the editions,
  the Print edition included, agree with the manuscript." Leave (it is the
  chapter's first statement of the agreement check); the exception itself
  first appears at `08:433`, which stays.
- `16:78` "There is one exception. `press verify-formats` reads an existing
  *dist/alice.pdf* into its cross-edition agreement check without rebuilding
  it." Pointer: "with the one exception Chapter 8 names."
- `16:178` "So does the cross-edition agreement check in `press
  verify-formats`, which reads whatever PDF already sits in *dist/*." Cut
  outright; the preceding sentence about the imported module is the point
  of the paragraph.
- Warning boxes on the same fact: `03:627-629` "Do not run a verifier over
  *dist/* and trust the result without a fresh build. Run `press all`, which
  rebuilds each artifact before it verifies it." Cut outright with `03:631`
  ("A verifier run over an old *dist/* proves only that last week's files
  were good ..."); the section already says `press clean` deletes both
  directories. `16:180-182` "Do not call a verifier module directly on
  *dist/* to check a book ..." Cut outright; `16:178` keeps the fact.
  `08:453-455` is the keeper's box; keep.

**The first-run font scan** (keeper: Chapter 2, sidebar "The first-run font
scan", `02:367-375`; cut `02:377` "The scan belongs to LuaLaTeX, and press
does not hurry it. If a build on a fresh machine seems to hang for several
minutes, wait: it is almost certainly the scan." outright, the sidebar said
it).

- `01:172-174` warning "Leave the first LuaLaTeX run on a fresh machine
  alone. Its font scan takes several minutes and looks like a hang. It is
  not a hang, although it gives a very convincing imitation of one." Keep
  this one too: the tour is where a new reader first meets it, and the
  sentence is better than the sidebar's. Then cut `01:251` "4. A font scan
  that looks like a hang. The warning earlier in this section covers it."
  from the list of five causes (renumber to four).
- `03:537` "The first time LuaLaTeX runs on a new machine, it scans the
  system fonts, and that scan takes several minutes. It is not a hang,
  although it is a convincing imitation of one. Let it finish." Cut
  outright.
- `07:214-218` "The first LuaLaTeX run on a new machine spends several
  minutes on a font scan, and it looks like a hang. It is not one." and the
  Tip "Run `press pdf` on a new machine well before you need the PDF, and
  leave it alone until it finishes." Cut both outright.
- `A:909` (press pdf) last sentence, "The first run on a fresh machine
  spends several minutes on a font scan, which looks like a hang and is not
  one." Pointer: "(the first run's font scan, Chapter 2)".
- `D:122-124` subsection "The first LuaLaTeX run". Cut outright.

**`press all` does not build the print pack** (keeper: Chapter 7, "What
press all leaves out", `07:442-448`).

- `01:279` "`press all` does not build the print pack, except through the
  commerce gate in a book that enables print ordering. Its own targets do:
  `press print`, `press verify-print`, and `press coverwrap`, which add
  *alice-interior.pdf* and *alice-coverwrap.pdf* to *dist/*." Cut to "Its
  own targets build it (Chapter 12)."
- `03:623-631` subsection "Files `press all` does not make". Keep the
  first sentence "The print pack builds only when you ask for it." and the
  registration-targets sentence; cut "In a book without print ordering,
  `press all` makes none of these."
- `08:447` "A commerce gate follows the verifiers. For a book without print
  ordering ... Under `PRESS_RELEASE`, the press enforces it. Example 1.2 in
  Chapter 1 shows the summary lines of a full run." Cut to "A commerce gate
  follows the verifiers (Chapter 7)."
- `12:159` "`press all` builds neither the print interior nor the cover
  wrap. It builds and verifies every edition a reader downloads, and the
  Pages bundle that serves them. The print pack has its own targets. The one
  exception is the *commerce gate* ..." Cut to "`press all` does not build
  the print pack; its own targets do, and the commerce gate (the last step
  of `press all`) builds it in a book that enables print ordering."
- `A:86` "`press all` builds neither the print interior nor the cover wrap.
  `press print`, `press verify-print`, and `press coverwrap` make them, and
  the commerce gate builds them when print ordering is on." Keep (the
  reference entry should say it once).

**A sentinel from the first words of a chapter fails under a drop cap**
(keeper: Chapter 6, warning at `06:378-380` plus `06:382`).

- `01:285-287` warning "If your book uses the drop-cap chapter opening, do
  not take a sentinel from the first words of a chapter ..." Cut outright.
- `03:224-226` warning "Never take a sentinel from the first words of a
  chapter. A chapter opening can set the first word as one large capital
  followed by small capitals. The PDF then no longer contains the phrase as
  you typed it." Replace with one clause appended to `03:222`: ", and from
  the middle of a chapter, never its first words (Chapter 6 says why)".
- `04:311-313` warning "Never choose a sentinel from the first words of a
  chapter ..." Cut outright; Chapter 4 is about chapter openings, not
  sentinels, and `04:204` already points to Chapter 6.
- `B:83` keeps its one sentence (reference). `C:47` keeps its remedy.

**The retired `macos-14` runner** (keeper: Chapter 14, `[^14-macos]` at
`14:329`).

- `02:335` `[^2-macos]` "The macOS job once ran on `macos-14` ..." Cut the
  footnote and its marker at `02:333`.
- `16:252` `[^16-macos]` "The macOS job once ran on `macos-14` ..." Cut
  the footnote and its marker at `16:250`.
- `D:120` `[^d-runner]` "The press's macOS CI job once ran on `macos-14`
  ..." Cut the footnote and its marker at `D:118`.

**Lulu's preflight: transparency and 602 PPI** (keeper: Chapter 12,
"Print-safe images", `12:269`).

- `05:366` "The pass came from a real preflight. Lulu flagged two problems
  in an early print interior ... triggers **neither** warning"." Cut to
  "The pass came from a real preflight report, which Chapter 12 tells."
  Cut `[^5-lulu]` with it.
- `05:370-372` Tip "In *tex/title-page-print.tex*, point the logomark at
  its copy in *build/print-assets/* ..." Cut outright; the same Tip is at
  `12:271-273`, the keeper.
- `11:316` "The print vendors are the reason. Lulu once flagged a book's
  logomark for its transparency, and for its resolution of over 600 PPI, so
  the pass now flattens each of those images and caps its resolution." Cut
  to "The print vendors are the reason (Chapter 12)."
- `12:19` "as Lulu once did when it flagged a press logomark for
  transparency" Keep; it is the chapter's own opening.

**`CI=false` reads as true** (keeper: Chapter 8, `08:317` and `[^8-ci-false]`).

- `02:277` "The press chose its own variable on purpose, because the
  ambient `CI` variable has a trap: `CI=false` is truthy." Cut to "The press
  chose its own variable instead of the ambient `CI` (Chapter 8 says why)."
- `16:146` "Chapter 8 gives the reason: a variable set to `CI=false` would
  still read as true." Cut the clause after the colon; keep "Chapter 8
  gives the reason."
- `D:147` "Press does not read the ambient `CI` variable for this, because
  `CI=false` would read as truthy." Cut the clause after "for this".

**The cover that passed at 11.5 percent** (keeper: Chapter 1 sidebar,
`01:94-102`).

- `08:27` "The press learned this law from a failure. Its CONTRIBUTING file
  records that "a title-page generator shipped a dropped and a clipped cover
  at 11.5% coverage: the lines ran, the artifact was never inspected." The
  tests ran the code, but nobody inspected the artifact, in which the
  generator dropped one cover and clipped another. The press drew a rule
  from the incident: "A producer is only proven by a verifier that rejects a
  broken artifact." The cover check that you meet later in this chapter
  exists because of that sentence." Cut to "The press learned this law from
  the cover that passed at 11.5 percent coverage (Chapter 1), and drew a
  rule from it: "A producer is only proven by a verifier that rejects a
  broken artifact." The cover check later in this chapter is that rule at
  work."
- `16:226` "The gate's philosophy, in *CONTRIBUTING.md*, reads: "Coverage
  measures that a line *ran*, not that its output was *right*... a
  title-page generator shipped a dropped and a clipped cover at 11.5%
  coverage: the lines ran, the artifact was never inspected." The rule that
  follows is ..." Keep the first quotation up to "*right*"", cut from "...
  a title-page generator" to "inspected."", keep "The rule that follows".

**The jargon lint exists twice** (keeper: Chapter 15 sidebar "The jargon
lint, twice", `15:303-309`).

- `06:299` `[^6-twocopies]` "The jargon lint exists twice ..." Cut to
  "[^6-twocopies]: A second, identical copy of the lint lives in the
  overused-jargon skill (Chapter 15)."
- `16:100` "One fact lives in two places on purpose. The jargon lint exists
  in the press package and again inside the overused-jargon skill, because
  the skill must work without the press installed. The `jargon_parity`
  check requires the two copies to match byte for byte." Cut to "One fact
  lives in two places by design: the jargon lint and its copy in the
  overused-jargon skill (Chapter 15). The `jargon_parity` check requires
  them to match byte for byte."

**`fonts-linuxlibertine`** (keeper: Chapter 2, `02:194-196` warning and
`02:210`).

- `01:311` `[^1-libertine]` "TeX Live carries Libertinus for the PDF.
  Ubuntu has no `fonts-libertinus` package ..." Cut the footnote to "TeX
  Live carries Libertinus for the PDF; Chapter 2 names the one Ubuntu
  package the fonts need."
- `09:78` `[^9-libertine]` "The face has its own scar ..." Cut the footnote
  and its marker at `09:76`.
- `D:59` "The first is the font ..." Keep (Appendix D is the platform
  reference); it may stay as the only appendix telling.

**`toc-depth: 1` empties the List of Plates** (keeper: Chapter 7 sidebar
"The lists that would not converge", `07:206-212`).

- `05:144` from "A second scar sits in the same place." to the end of the
  paragraph, and `[^5-tocdepth]`. Cut to "A second scar in the same lists,
  told in Chapter 7, once emptied the List of Plates."
- `09:92` from "A scar lives here." to "live together." Cut to "(a scar
  Chapter 7 tells kept the List of Plates full at that depth)".

**`hypcap`: list links overshoot** (keeper: Chapter 8 sidebar "Links that
overshoot", `08:130-136`).

- `05:146` "The links in the lists had a fault of their own ... The PDF
  verifier now checks the link destinations with pypdf." and `[^5-hypcap]`.
  Cut to "Each entry links to the top of its illustration, and the PDF
  verifier checks every destination (Chapter 8)."
- `09:94` last sentence "The last option sends a link in the List of Plates
  to the top of the plate instead of to its caption." Keep; cut
  `[^9-hypcap]` and its marker.

**The `Popen` import the gate missed** (keeper: Chapter 16 sidebar "The
import the gate did not see", `16:128-132`).

- `15:400` `[^15-popen]` "The launcher has a history ..." Cut to
  "[^15-popen]: The launcher lives in `press.adapters` for a reason Chapter
  16 tells."

**The `Mr.` tie test that proved nothing** (keeper: Chapter 16, `16:232`).

- `04:439` `[^4-ties]` "Pandoc ties Mr. on its own. For that reason, the
  press's test for the tie once passed with no filter in place at all. The
  Lua coverage work for press 3.0.2 found the empty test. The Lua tests, it
  turned out, also skipped silently in CI until CI set
  `PRESS_REQUIRE_LUA=1`." Cut to "[^4-ties]: Pandoc ties Mr. on its own; the
  filter covers the rest. Chapter 16 tells what that once did to a test."

**`press wordcount` and HTML comments** (keeper: Chapter 7, "Counting the
words", `07:496-509`).

- `01:160-166` "`press wordcount` counts the prose. It strips fenced and
  inline code. It counts HTML comments, so a comment inside a chapter adds
  to the total." and the session. Cut outright; the tour does not need it.
- `03:541-549` "The `press wordcount` target is the one you will run daily
  ..." through "count as words.[^3-wordcount]". Cut to one sentence: "Run
  `press wordcount` to see the new files counted (Chapter 7)." Move
  `[^3-wordcount]` (the `\b[\w'-]+\b` pattern) to Chapter 7 at `07:509`.

**The eight edition names, listed in full** (keepers: Preface `00:125` and
Chapter 1 Table 1.2).

- `03:613-617` paragraph "The first eight files in @fig:dist-after-all are
  the editions, and the registry gives each edition a name ..." Cut to "The
  first eight files are the editions, named as Table 1.2 names them; the
  figure's annotations give each name."
- `07:45` "The press's landing page gives the editions names of their own.
  The reading editions are the Print edition (the PDF) ... and the Source
  edition (the source zip). The rest of this chapter calls the PDF, the
  EPUB, the single-file HTML, and the reader site by their formats, as the
  targets do ..." Keep only the last two sentences (the chapter's naming
  rule).
- `16:74` "The EPUB writer makes the Circulating edition (EPUB), and the
  HTML writer makes the Single-leaf edition (the self-contained HTML). The
  chunked HTML writer makes the Chapter edition (the reader site and its
  zip). The plain and DOCX writers make the Telegraphic edition (plain text)
  and the Office edition (DOCX). The Manuscript edition (the stitched
  Markdown) and the Source edition (the source zip) go to *dist/* without
  pandoc." Cut to "The EPUB, HTML, chunked HTML, plain, and DOCX writers
  make the other five rendered editions; the stitched Markdown and the
  source zip go to *dist/* without pandoc."

**How to read this book** (keeper: Preface, "Organization of this book",
`00:21-91`).

- `01:297-305` section "How to read this book", four paragraphs beginning
  "The chapters follow the order in which you make a book." Cut the
  section to its last line: "Chapter 2, *Installing press*, puts the
  toolchain on `hatter`." (Then that line falls under the chapter-end rule
  in section 3 and may go too.)

**Hand-typed chapter references are a convention** (keeper: Preface
`00:127`).

- `01:305` "The author typed the chapter references in this book by hand,
  because the press cross-references figures and nothing else. By the terms
  of the second law they are a convention, the weakest kind of guard, and
  you should treat them with the matching degree of trust." Cut outright
  (goes with the section above).
- `04:97` last two sentences, "For a chapter or a section, write the
  reference in words: "see Chapter 6, *Checking the manuscript*". Chapter
  5, *Figures, plates, and illustrations*, covers figure identifiers in
  full." Keep (this is the author-facing instruction).
- `05:122` "Press has no cross-reference mechanism for chapters or sections
  either, and no `@` form reaches a chapter or a section. Write those
  references in words ... Tables and examples in this book carry hand-typed
  numbers for the same reason." Cut to "Chapters, sections, tables, and
  examples have no `@` form; write those references in words (Chapter 4)."

**Trust receipts and the twelve layers** (keeper: Chapter 14, "Receipts",
`14:211-225`).

- `16:256-268` section "Trust receipts": "One of the product laws in
  *ROADMAP.md* describes how the press builds trust ..." through "read its
  release receipt." Cut the section to two sentences: "Chapter 14 describes
  the trust receipts, the twelve layers, and the release receipt that names
  the wheel and toolchain digests. The ledger names the complete-chain rule
  `INV-release-receipt-chain`, and the selftest's `receipt_chain` check
  exercises it." Keep @fig:trust-tiers only if Chapter 14 does not take it;
  otherwise move the figure to Chapter 14.

**File sorting and `press add`** (keeper: Chapter 3, `03:376-449`).

- `04:52` "Press finds chapters by their filenames ... Press pads the
  numbers it hands out to at least two digits for that reason." Cut to "A
  chapter file's name starts with a digit; Chapter 3 gives the sorting
  rules."
- `04:54-56` warning "Start every chapter file's name with a digit ..." Cut
  outright (same box at `03:382-384`).
- `04:58-66` "The simplest way to start a chapter is to let press create
  the file ..." through "covers the index." Cut to the session alone
  (`04:60-62`) and one sentence: "`press add chapter` names the file and
  writes the heading word for word (Chapter 3)."

**`SOURCE_DATE_EPOCH` and the fixed timestamp** (keeper: Chapter 7, Table
7.2 and `[^7-epoch]`; Chapter 8, `08:339` for the zip).

- `16:84-86` "Two fixed dates keep the artifacts reproducible ..." and
  `[^16-epoch]`. Cut to "Two fixed dates keep the artifacts reproducible:
  `SOURCE_DATE_EPOCH` (Chapter 7) and the source zip's member timestamp
  (Chapter 8)."

**`book_inputs()` cleans *build/generated/* first** (keeper: Chapter 7,
"Generated inputs", `07:359-369`).

- `08:449` "The law reaches the generated inputs too. Every pandoc build
  calls `book_inputs()` first ... "the generated appendices are cleaned
  first so stale copies cannot survive"." Cut to "The law reaches the
  generated inputs too: every pandoc build regenerates them first
  (Chapter 7)."

**`site-url` governs every absolute URL** (keeper: Chapter 3, Table 3.4 and
`03:216`).

- `09:220` "All of this depends on the field `site-url`. The rule is short:
  "when there is no public base URL, nothing URL-shaped is emitted." A book
  without it gets no canonical link, no `og:url` or `og:image`, and no
  sitemap." Keep the quotation (it is new); cut the third sentence.
- `09:222-224` Tip "Set `site-url` ... before you publish the reader site."
  Keep.

**Floating and immutable tags** (keeper: Chapter 14, "Tags: floating and
immutable", `14:227-249`; Chapter 2 `02:75-81` keeps its first definition
because the install command needs it).

- `01:291` "A *floating tag* such as `v3` moves forward within its major as
  new releases come out, and an *immutable tag* such as `v3.0.2` names one
  release forever." Keep as the first mention; cut the rest of the
  paragraph from "*The release contract* is the workflow" to "which is why
  v3.0.0 is one." to "Chapter 14 explains the release contract that proves
  each tag, and Chapter 9 explains why a design change needs a new major."
- `09:377` "A *floating tag* such as `v3` moves to each new compatible
  release, and an *immutable tag* such as `v3.0.2` never moves." Cut
  outright; the sentence after it ("An author on the floating tag ...")
  carries the point.
- `09:397` "On `v3.0.2`, it keeps the same press code, the same composite
  action, and the same toolchain bytes forever." Cut to "On `v3.0.2`,
  nothing moves."

**NON-GOALS: "Press is a prose engine"** (keeper: Chapter 1, "What press is
not", `01:110-120`).

- `09:169` "The list has a limit, which *NON-GOALS.md* states: "Press is a
  prose engine." Another trim, a color interior, or large print is a new
  profile and core press work. A fixed-layout picture book or a magazine is
  a new engine, and press does not take it on." Cut to "Another trim, a
  color interior, or large print is a new profile; a new engine is outside
  the press (Chapter 1)."

**"Restate a whole section when you touch it"** (keeper: Chapter 9,
`09:314-318`).

- `11:67-69` "The merge is shallow at the top level. The press copies the
  house file and lays each top-level section of the book's file over it,
  whole." and "Suppose the Alice book writes a `cover:` section with only a
  `style:` key in it ... "restate a whole section when you touch it"." Cut
  to "The merge is shallow: a section the book names replaces the whole
  house section (Chapter 9), so Example 11.1 restates every key."

**The KOMA `open=any` spelling** (keeper: Chapter 9 sidebar "The KOMA
spelling trap", `09:53-59`).

- `12:155` "The `print.yaml` defaults carry one scar of their own. A
  two-sided KOMA document must spell "open chapters on any page" as
  `open=any` ... The defaults use the KOMA spelling." Cut to "The
  `print.yaml` defaults spell the open-chapter option the KOMA way, for the
  reason Chapter 9 tells."

**`no assets/cover.jpg; interior verified, wrap not built`** (keeper:
Chapter 12, `12:157`).

- `07:351-355` "If *assets/cover.jpg* exists, it then builds the cover wrap
  ... Without a cover, it stops after the interior and says so:" and the
  message block. Cut the block; end at "stops after the interior and says
  so."
- `08:177` "Without a cover, the target prints `no assets/cover.jpg;
  interior verified, wrap not built` and stops there." Cut to "Without a
  cover, the target stops after the interior."

**"Initialize containers": run it again** (keeper: Chapter 1, `01:252`).

- `03:597` "If a CI run dies at the step "Initialize containers", run it
  again. The image is public, and the step needs no secret." Cut outright.

**BROKEN: fails `--version` and `-v` within 15 s** (keeper: Chapter 2,
Table 2.4 `02:241`).

- `02:246` "A tool that fails both `--version` and `-v` within 15 s counts
  as broken, whatever `which` says about it." Cut to "A tool that fails both
  probes counts as broken, whatever `which` says about it."

**The scar, defined** (keeper: Chapter 1, `01:60`).

- `00:5` "A *scar*, in the press's vocabulary, is a production failure
  turned into a guard." Keep (the Preface may define it).
- `02:210` "The package `fonts-linuxlibertine` is a *scar*, the press's word
  for a production failure turned into a guard." Cut to "The package
  `fonts-linuxlibertine` is a scar."
- `16:321` "A *scar* is the press's word for a production failure turned
  into a guard." Cut outright; begin the section at "The fourth law states
  the policy".

**Appendix D against Chapter 2.** Appendix D restates Chapter 2's binfmt
story (`D:61-69`), `--break-system-packages` (`D:73`), the Docker command
(`D:157-175`), and dev-render (`D:177-181`). The appendix editor keeps the
package lists, the wrapper (Example D.4), the architecture note, and Table
D.2, and cuts each restated paragraph to one sentence with "(Chapter 2)".

## 2. The three tics, per chapter

### Word-counted quotations (drop the counting phrase, keep the quotation)

- `01:24` "The press README describes the program in one plain sentence:"
  Fix: "The press README describes the program:"
- `01:70` "Each law fits in a line." Cut outright.
- `01:92` "*ARCHITECTURE.md* draws the line between the two halves of the
  work in one sentence:" Fix: "*ARCHITECTURE.md* draws the line between the
  two halves of the work:"
- `01:97` "*CONTRIBUTING.md* records the cause in one clause:" Fix:
  "*CONTRIBUTING.md* records the cause:"
- `01:118` "*ARCHITECTURE.md* gives the reason in one line:" Fix:
  "*ARCHITECTURE.md* gives the reason:"
- `02:341` "The install guide states the supported platforms in one
  sentence:" Fix: "The install guide states the supported platforms:"
- `08:25` "The press ROADMAP puts the same idea in fewer words." Fix: "The
  press ROADMAP says the same:"
- `09:135` "The documentation divides the labor in one sentence:" Fix: "The
  documentation divides the labor:"
- `09:230` "and the press gives the reason in five words: "the reader owns
  the theme."" Fix: "and the press gives the reason: "the reader owns the
  theme.""
- `09:314` "The house documentation gives the rule in eight words: "restate
  a whole section when you touch it."" Fix: "The house documentation's rule
  is "restate a whole section when you touch it.""
- `11:63` "Its register gives the idea in three sentences:" Fix: "Its
  register:"
- `13:21` "states the rule for all of them in one sentence:" Fix: "states
  the rule for all of them:"
- `14:30` "puts the rule in one clause:" Fix: "puts the rule:"
- `14:108` "The description states the design in one sentence:" Fix: "The
  description states the design:"
- `15:22` "The press's documentation puts it in one sentence:" Fix: "The
  press's documentation puts it:"
- `15:394` "The press's maintainers give the reason in one sentence." Cut
  outright; the next sentence quotes the reason.
- `16:23` "The press's *CLAUDE.md* states the rule in one sentence:" Fix:
  "The press's *CLAUDE.md* states the rule:"
- `D:5` "The press's install guide names its platforms in one sentence:"
  Fix: "The press's install guide names its platforms:"

(`16:160`, "It states the property in one sentence.", describes a ledger
field and stays.)

### "plainly" (drop the word or the attribution clause)

- `00:137` "Its README is plain about the result:" Fix: "Its README says:"
- `01:66` "The README is plain about ownership:" Fix: "The README says of
  ownership:"
- `01:78` "Its *CLAUDE.md* says so plainly:" Fix: "Its *CLAUDE.md* says:"
- `02:43` "Its install guide says so plainly:" Fix: "Its install guide
  says:"
- `03:645` "The source of `press add` states the purpose plainly." Fix:
  "The source of `press add` states the purpose."
- `04:142` "The house law is plain about what to do instead: rewrite the
  sentence." Fix: "The house law says what to do instead: rewrite the
  sentence."
- `04:291` "so a preface opens plainly" Fix: "so a preface opens with a
  plain paragraph" (this one is descriptive, not attributive; change only
  for consistency).
- `04:419` "The press states the principle plainly." Cut outright; the next
  sentence is the principle.
- `05:323` "The scars list says it plainly:" Fix: "The scars list says:"
- `06:75` "and the press puts the reason plainly:" Fix: "and the press gives
  the reason:"
- `10:380` "The press says plainly what the ledger does not do:" Fix: "The
  press says what the ledger does not do:"
- `11:320` "The scars list puts it plainly:" Fix: "The scars list says:"
- `12:49` "The documentation states the reason plainly:" Fix: "The
  documentation states the reason:"
- `12:88` "and *docs/PROVIDER-DATA.md* gives the rule plainly:" Fix: "and
  *docs/PROVIDER-DATA.md* gives the rule:"
- `14:394` "The press's migration guide puts it plainly:" Fix: "The press's
  migration guide says:"
- `16:354` "*CONTRIBUTING.md* puts the point of `press all` plainly:" Fix:
  "*CONTRIBUTING.md* puts the point of `press all`:"
- `C:128` "**Remedy.** State the claim plainly." Keep; it is advice, not
  attribution.

### "to fit the page" (drop the aside, keep the break)

- `03:128` "We wrapped that block's opening comment to fit the page and cut
  the ends of four long lines." Fix: "We cut the ends of four long lines."
- `03:230` "We fold its first line to fit the page and cut the end of the
  second." Fix: "We cut the end of the second line."
- `05:97` "Pandoc lets the attributes run over several lines, and the
  example breaks them only to fit the width of this page." Fix: "Pandoc lets
  the attributes run over several lines." (`05:341`, "scale an image down to
  fit the page", is about the page and stays.)
- `06:104` "and Example 6.2 gives the message for each, folded to fit the
  page." Fix: "and Example 6.2 gives the message for each."
- `06:258` "Example 6.6 shows three rows of the watchlist, folded to fit the
  page. In the file, each row is one line." Fix: "Example 6.6 shows three
  rows of the watchlist; in the file, each row is one line."
- `06:332` "Example 6.9 shows the message, folded to fit the page." Fix:
  "Example 6.9 shows the message."
- `06:392` "It refuses vacuous witnesses with the message in Example 6.11,
  folded to fit the page." Fix: "... in Example 6.11."
- `06:408` "The example folds long lines to fit the page and shortens the
  paths in the notes." Fix: "The example shortens the paths in the notes."
- `06:437` "Example 6.13 shows the end of a failed check on the Alice book,
  folded to fit the page." Fix: "... on the Alice book."
- `07:59` "Example 7.1 shows the line for the single-file HTML, broken
  across lines to fit the page." Fix: "Example 7.1 shows the line for the
  single-file HTML."
- `07:433` "The press prints that message on one line, broken here to fit
  the page." Cut outright.
- `08:162` "If they do not, the verifier prints this message, here broken
  across two lines to fit the page:" Fix: "If they do not, the verifier
  prints:"
- `08:169` "The message names a likely cause. It appears here on three lines
  to fit the page:" Fix: "The message names a likely cause:"
- `08:181` "If the page renders blank, it prints this message, broken here
  to fit the page:" Fix: "If the page renders blank, it prints:"
- `08:252` "Two more messages concern the metadata, the first broken here to
  fit the page:" Fix: "Two more messages concern the metadata:"
- `08:274` "with the slug changed to `alice` and the long lines broken to
  fit the page." Fix: "with the slug changed to `alice`."
- `08:310` "Inside the image, the verifier prints this message instead,
  broken here to fit the page:" Fix: "Inside the image, the verifier prints
  instead:"
- `08:390` "When everything passes, the verifier prints its line, broken
  here to fit the page:" Fix: "When everything passes, the verifier prints:"
- `08:420` "It prints as one line, broken here to fit the page:" Cut
  outright.
- `10:255` "The first message is one line in the press's output, broken
  here to fit the page. The other two name the entry by its position in the
  list." Fix: "The last two name the entry by its position in the list."
- `10:286` "The press prints the message as one line. It appears here on two
  to fit the page." Cut both sentences.
- `10:359` "Each message is one line in the press's output, broken here to
  fit the page." Cut outright.
- `12:302` "Example 12.5 gives its form, broken here across lines to fit
  the page." Fix: "Example 12.5 gives its form."
- `13:79` "Example 13.3 shows that run, with the output broken into three
  lines to fit the page." Fix: "Example 13.3 shows that run."
- `13:136` "The refusal reads as follows, broken here to fit the page:"
  Fix: "The refusal reads:"
- `13:165` "Example 13.5 breaks two long lines to fit the page and omits the
  closing advice, which the next paragraph quotes." Fix: "Example 13.5
  omits the closing advice, which the next paragraph quotes."
- `15:222` "**Example 15.2. The house law, broken here to fit the page**"
  Fix: "**Example 15.2. The house law**"
- `15:346` "`press improve` stops with this message, broken here to fit the
  page:" Fix: "`press improve` stops with:"
- `15:374` "**Example 15.5. The named diseases, broken here to fit the
  page**" Fix: "**Example 15.5. The named diseases**"
- `C:5` "The message itself follows in a block, broken at a space to fit the
  page. Press prints it as one line, and an indented line in the block
  continues the line above it." Keep; this is Appendix C's own convention
  statement and does the work for the whole appendix.
- `D:96` "with the guide's own comments wrapped to fit the page." Fix: "with
  the guide's own comments."

## 3. Closing maxims, per chapter

Every paragraph of three or more sentences that closes on a sentence of
nine words or fewer, with a verdict. **keep** = one of the chapter's two.
**cut, ends earlier** = delete the sentence; the paragraph closes on the
one before. **cut, fold** = delete the sentence and move its fact into the
sentence before it, as given. **leave** = a pointer or a plain statement,
not a maxim; no action.

### Preface

- `00:7` "Where neither says anything, neither do we." **keep**
- `00:23` "The appendixes are for reference." leave
- `00:115` "A warning always comes before the step it protects." **keep**
- `00:135` "Copyright 2026 Clint Ecker."" leave

### Chapter 1

- `01:54` "Chapter 2, *Installing press*, covers both routes." leave
- `01:60` "The first commit carries the date 2026-07-17." leave (it repeats
  `00:7`; cut if the editor wants one fewer date)
- `01:70` "Each law fits in a line." cut, ends earlier (also a word count)
- `01:82` "A convention asks people to avoid it and hopes." **keep**
- `01:112` "It does not build interactive or rich-media e-books either."
  leave
- `01:116` "Nobody tests the press on Windows." **keep**
- `01:228` "@fig:ten-minute-tour gathers the tour so far into three frames."
  leave
- `01:279` "Chapter 12, *The print pack*, covers it in full." leave
- `01:281` "`press clean` deletes both *build/* and *dist/*." leave
- `01:299` "Read them in order the first time." goes with the section cut
  in part 1

### Chapter 2

- `02:192` "One package in it needs a warning first." cut, ends earlier
  (the Warning box follows at once)
- `02:222` "It prints one line for each check." leave
- `02:266` "Every CI build of every book runs inside it." **keep**
- `02:315` "Chapter 14 shows where to find the digest." leave
- `02:337` "Contributors to the press need no emulation either." cut, ends
  earlier
- `02:341` "Ubuntu therefore has the strongest record of any platform."
  **keep**
- `02:347` "The last command prints the doctor's exit status." leave

### Chapter 3

- `03:174` "Chapter 12, *The print pack*, covers direct print ordering."
  leave
- `03:326` "We leave out the diff that each command prints." leave
- `03:404` "The scaffold's preface heading uses the long form." leave
- `03:416` "The first chapter of a book is `01`." cut, fold: "zero-padded to
  at least two digits, so the first chapter is `01`."
- `03:418` "We cut the end of the last line." leave
- `03:484` "Chapter 2, *Installing press*, covers installation in full."
  leave
- `03:537` "Let it finish." goes with the font-scan cut in part 1
- `03:553` "Example 3.11 shows the rest for the Alice book." leave
- `03:566` "A Source edition therefore cannot contain old artifacts." **keep**
- `03:601` "You do this once per book repository." leave
- `03:605` "Git ignores both, and `press clean` deletes both." leave
- `03:635` and `03:637` leave (file lists)
- `03:639` "Neither is an artifact." **keep**

### Chapter 4

- `04:50` "Pandoc numbers all three." leave
- `04:89` "The house would still write it in sentence case." **keep**
- `04:132` "You never need the sign in a chapter." cut, ends earlier
- `04:142` "Example 4.3 shows one such rewrite." leave
- `04:155`, `04:185` chapter pointers, leave
- `04:233` "If you write `text`, the code prints in black." leave
- `04:293` "The Telegraphic and Office editions carry no drop cap." leave
- `04:415` ""C. L. Dodgson".[^4-ties]" leave (end of a list)
- Not caught by the count but a maxim: `04:252` "A session that you typed
  from memory, rather than copied from a terminal, is the first thing a
  careful reader catches out." **keep**

### Chapter 5

- `05:44` "It has no class, so it is a plate." leave
- `05:180` "Prefer `wrap-outer`, which names what the PDF does." **keep**
- `05:216` "Chapter 9, *The house design*, describes the profiles." leave
- `05:218` "The checker refuses any other unit." leave
- `05:353` "Table 5.6 gives the caps." leave
- `05:364` "Keep every interior image under *assets/woodcuts/*." **keep**
- Not caught by the count: `05:118` "The fault is easy to see in a proof
  and easy to miss in a hurry." cut, ends earlier. `05:275` "Write each
  directive as though a reader will see it." cut, fold: "so that edition
  publishes every directive verbatim, for any reader to see."

### Chapter 6

- `06:34` "The two passes that read prose come last." cut, ends earlier
- `06:75` "If any of them gets through, the check fails." leave
- `06:186` "The house law says to rewrite the sentence instead." leave
- `06:227` "The `--include-quotes` option makes it read blockquotes as
  well." leave
- `06:382` "It then fails in the Print edition." **keep**
- `06:473` goes with the exception cut in part 1
- Not caught by the count: `06:469` "The printed lines are for you, and the
  exit status is for every program that runs the checker on your behalf."
  **keep**. `06:498` "The cure is a habit." cut, ends earlier (the
  sidebar's next sentence stands alone).

### Chapter 7

- `07:47`, `07:422`, `07:440` chapter pointers, leave
- `07:72` "The last part names the file that pandoc writes." leave
- `07:80` "The Telegraphic and Office editions share `portable.yaml`." leave
- `07:295` "Table 7.4 reproduces that table exactly, cell for cell." leave
- `07:444` "`press all` also does not run `press render`." leave
- `07:456` "The run's last line begins `press. your book is ready`." leave
- Not caught by the count: `07:367` "The deletion comes first on purpose."
  cut, ends earlier (it opens, not closes; the quotation after it carries
  the point). `07:420` "The check step matters more than it looks." cut,
  ends earlier. `07:143` "If you suspect that pandoc read the wrong header,
  open the matching file in *build/defaults/* before you look anywhere
  else." **keep**. `07:339` "The fix never reached the file, and a green
  result now covers a stale book." **keep**.

### Chapter 8

- `08:91` "The verifier failed its own test." **keep**
- `08:216` "The third is the manuscript witness." leave
- `08:250` "The EPUB message reports the same comparison." leave
- `08:298`, `08:400` table pointers, leave
- `08:317` "An ordinary workstation does not." cut, fold: "The toolchain
  image sets `PRESS_TOOLCHAIN`; an ordinary workstation does not."
- Not caught by the count: `08:128` "It does not fail the build for a
  missing library, and it does not pretend it checked the links either."
  **keep**. `08:230` "The press chooses the witness, so it tests a line that
  you never thought to protect." leave (mid-paragraph). `08:135` "The
  verifier now does it on every verify run, so nobody has to remember." cut,
  ends earlier. `08:17` "It tells you nothing about the pages inside the
  PDF." cut with its preceding sentence; begin the chapter at "Press
  therefore opens every artifact it makes" (drop "therefore").

### Chapter 9

- `09:86` "The value `\hyphenpenalty=150` raises the cost of every hyphen."
  leave
- `09:228` "It has no dark theme." leave
- `09:260` "Table 9.7 lists the keys that touch the design." leave
- `09:277` "It also asks for the fairy-dust scene break." leave
- `09:320` "Those are the house values that Example 9.1 restates." leave
- `09:379` "An author proofs those exact pages." **keep**
- `09:387` "Release 3.0.1 corrected the message." leave
- Not caught by the count: `09:58` "The first mistake is silent, and the
  second costs paper." **keep**. `09:308` "In Example 9.1 the URLs in the
  reading PDF therefore print in the deep red, under the name of a green."
  leave (it is the paragraph's point, not a flourish). `09:314` "and that
  surprises authors once." (opening clause) leave.

### Chapter 10

- `10:141` "It waits for the copyright page.[^10-rules]" **keep**
- `10:190` "Neither configuration file feeds those three pages." leave
- `10:233` "Example 10.3 shows three entries for the Alice book." leave
- Not caught by the count: `10:286` "The zero-hit rule turns the cut into a
  refusal you see at your desk." **keep**. `10:336` "That exactness is the
  purpose of the ledger: a claim that matches shows that the cited sentence
  still says what the source supports." leave (explanatory). `10:380` "The
  ledger then records, out of the reader's sight, that the footnote's
  sentence still says what its source supports." cut, ends earlier (it
  repeats `10:336`).

### Chapter 11

- `11:61` "It lives in *config/aesthetic.yaml*, which is optional." leave
- `11:63` end of a quotation, leave
- `11:86` "Chapter 9, *The house design*, describes those keys." leave
- `11:113` "Table 11.2 describes the ten styles." leave
- `11:259` "Table 11.5 gives the four art targets." leave
- `11:354` "The `--max-edge` option changes it." leave
- `11:387` inside an example, leave
- `11:425` "A second run adds *openai-2.png* beside the first." leave (and
  see part 4; it is the true statement)
- Not caught by the count: `11:24` "The build reads the committed file and
  never asks the model again." **keep**. `11:57` "Step 7 matters more than
  it looks." cut, ends earlier (begin the paragraph at "The CI build on
  `printshop` reads only committed files"). `11:444` "A year later, the
  record still tells the maintainer which candidate became each plate and
  at what size." **keep**. `11:157` "Check the lettering on every candidate
  yourself, as the press's cover documentation advises." leave (advice).

### Chapter 12

- `12:76` "The key `print.color-grade` takes ..." leave
- `12:143` "The guide does not say so." **keep**
- `12:155` goes with the KOMA cut in part 1
- `12:227` "The bars are 0.9in tall." leave
- `12:265` "Your masters in *assets/* never change." leave
- `12:277` "The gate then looks for a qualification." leave
- `12:319` "Table 12.6 gives the dispositions." leave
- `12:411` "Run the full target before an upload." leave (instruction)
- `12:457` "Check the provider setting before you check the paper." **keep**
- `12:493` "Chapter 13, *Registrations*, covers that paperwork." leave
- Not caught by the count: `12:105` "and it also means the house spine is no
  real provider's spine." leave (mid-sentence). `12:243` "It does not catch
  a valid number that belongs to some other book." leave (fact the Warning
  needs). `12:258` "The verifier was right about the pixels." leave: it is
  mid-sidebar and earns its place. `12:315` "The press keeps that second
  question apart from the first." cut, ends earlier (the quotation that
  follows says it).

### Chapter 13

- `13:238` leave (URL)
- `13:263` "@fig:where-numbers-land shows the routes." leave
- `13:315` "The skill's order names no step for an ISSN." leave
- Not caught by the count: `13:74` "The checker then says nothing about a
  wrong prefix." cut, fold: "A block with only one of the two passes the
  checker without inspection, so a wrong prefix goes unremarked." `13:150`
  "Once you declare a retail edition, a pending number makes the checker
  refuse the book." **keep**. `13:226` "A book with no EPUB ISBN sends a
  distributor a print product only, which is an accurate account of the
  book." **keep**.

### Chapter 14

- `14:28` "Everything else belongs to the press." **keep**
- `14:32` "After a tag, it publishes a GitHub Release." leave
- `14:44` "Table 14.1 lists the three jobs." leave
- `14:80` "Every other line is verbatim." leave
- `14:120` "pip-compile produced it under Python 3.12." leave
- `14:124` "Release 3.0.2 was one such upgrade.[^14-pillow]" leave
- `14:267` "The floating tag moves only through *scripts/release.sh*." leave
- `14:386` "The site therefore always shows `main`." **keep**
- `14:394` "Table 14.4 lists its subcommands." leave
- Not caught by the count: `14:70` "A run that produced no artifacts cannot
  pass with nothing to show." cut, ends earlier. `14:185` "Do not look for
  the digest in the release notes." leave (instruction). `14:208` Tip "No
  release contract ever proved the image of one tag with the press of
  another." leave (the Tip's reason).

### Chapter 15

- `15:26` "Press comes with four of them." leave
- `15:60` "Read the row's name to tell which." leave
- `15:202` "It takes four arguments." leave
- `15:204` "The `report` argument forces one round and applies nothing."
  leave
- `15:269` "A book with none gets one candidate per chapter." leave
- `15:301` leave (file list)
- Not caught by the count: `15:109` "That is less of a gap than it looks."
  cut, fold: begin the paragraph "The gap is small in practice: a verifier
  checks the artifact at the moment it runs ..." `15:127` "and only its exit
  status says whether the book still passes." leave. `15:232` "The agents
  learn the law in advance, and the checker still enforces it afterward."
  **keep**. `15:396` "Each of them sees every chapter, so it sees a rhythm
  that a chapter agent, alone with one file, cannot." **keep**.

### Chapter 16

- `16:27` "The fourth is "Scars become law."" leave
- `16:62` "@fig:end-to-end-data-flow draws the whole path for the Alice
  book." leave
- `16:76` "Then `verify_pages` crawls the assembled *dist/pages/*." leave
- `16:110` "*bookmodel.py* reads the config into a frozen, typed `Book`."
  leave
- `16:116` "`alice` must find another word for hers." **keep**
- `16:122` "Environment reads and network requests belong there too." leave
- `16:134` "Table 16.2 lists the general exit statuses." leave
- `16:218` "No book installs it." leave
- `16:232` leave (instruction)
- `16:307`, `16:313` leave (facts)
- Not caught by the count: `16:90` "Before you add a list of anything to the
  press, look for the list that already exists." **keep**. `16:112` "Never
  read the raw YAML a second time." leave (instruction). `16:167` "An
  invariant without its limits invites you to lean on it where it does not
  hold." cut, ends earlier (the quotation before it says it). `16:230` last
  sentence "Before it did, the tests skipped in CI without a word." leave.

## 4. The block and the shoulds, by file

**`00-preface.md` and `01-introduction.md`** (should). `01:142` "`press
new` does not run `git init`, and the source archive holds only the files
Git tracks, so the tour commits the scaffold before the first build." The
reason is false for a fresh directory (Chapter 3, `03:566`: "A book
outside any repository is archived whole"). Fix: "so the tour commits the
scaffold first, which is the habit the Source edition rewards once the book
lives in a repository."

**`02-installing-press.md`** (should). `02:55-71`: Example 2.1 runs
`python3 -m venv ~/.press-venv` before the paragraph "On Debian and Ubuntu,
the `venv` module comes in a separate package, `python3-venv` ..." and its
`sudo apt-get install python3-venv`. Fix: move that paragraph and command
above Example 2.1.

**`02-installing-press.md`** (should). `02:75` "A *floating tag* such as
`v3` names a major version and moves forward to the newest compatible
release within it." and `02:124` "Use it for most books. You receive fixes
within the major version." Nothing says how a workstation receives them.
Fix: after Table 2.2 add "To take a new release on your workstation, run
`pip install --upgrade "press @ git+https://github.com/clintecker/press@v3"`;
the floating tag moves on GitHub, not in your environment."

**`03-the-shape-of-a-book.md`** (should). `03:21-37`, Table 3.1 lists
`--author`, `--publisher`, `--place`, `--owner`; none appears in `press new
--help` (Appendix A, `A:803-806`). Fix: a Tip after Table 3.1: "`press
<command> --help` prints the argument grammar only. The options in this
table, and most options in this book, are accepted but not listed; Appendix
A marks each one." Chapter 11's editor adds the same sentence after the
first synopsis at `11:106-111`.

**`03-the-shape-of-a-book.md`, `06-checking-the-manuscript.md`,
`08-verifying-the-artifacts.md`** (should). Hyphenation breaks a sentinel;
only `C:303` says so ("Then check that no word in it breaks with a hyphen at
the end of a line."). Fix: `03:222`, after "each distinctive enough to appear
exactly once ...": add "Prefer short words: a word LuaLaTeX hyphenates at a
line end breaks the match." `08:492`, "A missing sentinel has three usual
causes." becomes four, adding "The fourth is a word in the phrase that
LuaLaTeX hyphenated at a line end; choose shorter words or another phrase."

**`03-the-shape-of-a-book.md`** (should). `03:279` "The one exception is
*config/aesthetic.yaml*, which has no typed model of its own." against
Example 3.6 (`03:369`) "config/aesthetic.yaml: ok" and `11:100` "The press's
config validation does not cover *config/aesthetic.yaml*, so nothing
catches a misspelled key." Fix: after Example 3.6 add "For the aesthetic
file, `ok` means only that it parsed as YAML; no key is checked."

**`05-figures-and-plates.md`** (should). `05:368` "If the book supplies its
own *tex/title-page-print.tex*, the logomark in it must come from
*build/print-assets/*" is the file's first appearance; Chapter 10 defines
it at `10:219`. Fix: "its own *tex/title-page-print.tex* (a hand-written
title page for the print interior only; Chapter 10)".

**`06-checking-the-manuscript.md`** (should). `06:451` "Appendix C,
*Messages and refusals*, holds the full list." It holds the checker's and
verifiers' messages and not the generators', intake's, config's, or
commerce's (Appendix C says so for intake only, `C:558`). Fix: "Appendix C
holds the checker's and the verifiers' messages." (Appendix C's editor: add
a one-line pointer table at the head of the appendix for `gen_index`,
`gen_authorities`, `front matter needs`, intake, `press config`, retail, and
the commerce gate, each with the chapter that quotes it.)

**`09-the-house-design.md`** (should). `09:275` "The tokens a palette can
name are `paper`, `paper-warm`, `ink`, `ink-soft`, `cloth`, `cloth-deep`,
`foil`, `foil-bright`, `foil-deep`, `hairline`, `link`, and `ornament`."
Ruling: the accent token exists; `cover.py` reads `palette.get("accent")`,
and `11:140` and `B:314` say so. Fix: append ", and `accent`, which only
the cover prompt reads."

**`10-front-matter-index-authorities.md`** (should). `10:172`, Table 10.4:
"The press sets one line for each registration number the book declares,
such as "ISBN (print)", "ISBN (ebook)", and "LCCN"." Ruling: Table 10.4
follows Chapter 13 (`13:273` "The ISSN does not print there."); the code
prints the two ISBNs and the LCCN only. Fix: "The press sets one line for
each ISBN the book declares, "ISBN (print)" and "ISBN (ebook)", and one
for the LCCN. The ISSN does not print."

**`11-the-art-department.md`** (blocks). `11:383-410`, Example 11.3: the
inner closing fences at lines 388, 397, 403 and 409 read ` ```text `. A
closing fence takes no info string, so none of the four blocks closes. Fix:
make each of the four a bare ` ``` `.

**`11-the-art-department.md`** (should). `11:22` "a prompt for an image
model that the book keeps in *art/commissions.md*, and press runs each
commission once." against `11:425` "Candidates number upward and never
overwrite. A second run adds *openai-2.png* beside the first." Ruling:
press runs a commission as many times as you ask and never on its own; the
build never does. Fix at `11:22`: "and press runs a commission only when
you ask it to; the build never does."

**`13-registrations.md`** (should). `13:92` "It mints the lowest unused
publication number". Unused within this book repository only. Fix: add
"The press knows only the two ISBNs in this repository. A press with several
titles on one block keeps its own register and sets `registrations.isbn.print`
by hand from it in every book but the first."

**`13-registrations.md`** (should). `13:238` quotes "the one command that
reaches the network; ordinary builds never do." against `A:729` "It reaches
the network, as `press cover`, `press illustrate`, `press art commission`,
and `press research` do." Fix: after the quotation add "(the one command
among the registration targets; the art and operator commands reach their
own services)".

**`14-continuous-integration.md`** (should). `14:200` installs
`'press @ git+https://github.com/clintecker/press@v3'` while `14:205` says
"`v3.0.2` here in place of `v3`". Fix: change line 200 to `@v3.0.2`.

**`a-command-reference.md`** (should). `A:594` Example A.6 shows `"kind":
"plate"` for the White Rabbit, which Example 5.1 declares with no class.
Ruling: a bare image's kind is `figure` (`figures.py`, `DEFAULT_KIND =
"figure"`; `05:89`). Fix: change the captured value to `"figure"` and add
before the example "The White Rabbit has no class, so the report calls it a
`figure`; the numbering treats it as a plate (Chapter 5)."

**`b-configuration-reference.md`** (should). `B:335` "The press sends you
to the file or to the index workflow instead of the shell." No index
workflow ships (Chapter 15's four are editorial-passes,
authorities-research, aesthetic-brief, art-direction). Fix: "The press's
help text names an "index workflow"; at the time of this writing none
ships, so edit the file by hand."

**`c-messages.md`** (should, shared with 03/06/08 above): the hyphenation
remedy at `C:303` stays; it is now also in the chapters.

## 5. Passages to protect

Do not cut, tighten, or re-gloss these.

1. `01-introduction.md:80-86`, "The second law ranks three kinds of guard".
2. `01-introduction.md:94-102`, sidebar "The cover that passed at 11.5
   percent".
3. `04-writing-the-manuscript.md:138-151`, "The house sets no em dash and no
   en dash in prose." through Example 4.3.
4. `04-writing-the-manuscript.md:413-419`, "Some typesetting is too fine to
   ask of an author."
5. `05-figures-and-plates.md:172-174`, "The two wraps name a side of the
   page by its relation to the spine", and `05:250`, "Example 5.4 carries
   no `art:` directive, and that is deliberate." (cut only "and that is
   deliberate").
6. `06-checking-the-manuscript.md:491-499`, sidebar "The red check that went
   out green" (less its last two-line coda, per part 3).
7. `08-verifying-the-artifacts.md:216-230`, "Every edition must carry three
   pieces of evidence that it holds the book."
8. `09-the-house-design.md:371-397`, "Press makes a promise about design".
9. `12-the-print-pack.md:84-147`, "A *provider* is a print shop's
   specification as the press records it" through the Tip, and `12:457`,
   "The guide also lists an off-center spine".
10. `15-the-desk-and-the-machines.md:370-396`, "The `editorial-passes`
    workflow does not trust the prose skills alone."

## Counts per chapter

Retold = cuts or pointers from part 1 that land in that file. Tics = word
counts + plainly + fit-the-page. Maxims = closers marked cut. Shoulds =
entries in part 4 touching the file (the block counted under 11).

| File | Retold | Tics | Maxims cut | Shoulds |
|---|---|---|---|---|
| 00 | 0 | 1 | 0 | 0 (adds one convention sentence) |
| 01 | 9 | 6 | 1 | 1 |
| 02 | 5 | 2 | 2 | 2 |
| 03 | 7 | 2 | 1 | 3 |
| 04 | 6 | 3 | 2 | 0 |
| 05 | 6 | 2 | 2 | 1 |
| 06 | 3 | 7 | 2 | 2 |
| 07 | 8 | 2 | 2 | 0 |
| 08 | 7 | 9 | 3 | 1 |
| 09 | 8 | 3 | 0 | 1 |
| 10 | 0 | 4 | 1 | 1 |
| 11 | 4 | 3 | 1 | 2 (one block) |
| 12 | 4 | 3 | 1 | 0 |
| 13 | 0 | 4 | 1 | 2 |
| 14 | 1 | 3 | 1 | 1 |
| 15 | 1 | 4 | 1 | 0 |
| 16 | 11 | 2 | 1 | 0 |
| A | 2 | 0 | 0 | 1 |
| B | 0 | 0 | 0 | 1 |
| C | 0 | 0 | 0 | 1 |
| D | 7 | 2 | 0 | 0 |
