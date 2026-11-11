# Continuity report: Chapter 7, *Building the editions*

Desk: continuity editor. Chapter read: `book/chapters/07-building-the-editions.md`
(working tree, 515 lines, after its desks, the re-review, and Revision 2).
Cross-checked against Chapters 1 and 3 (committed or passed), the drafts of
Chapters 6 and 8, the drafts of Chapters 4, 9, 10, 11, 12, 13, and 15 where they
share facts with Chapter 7 or make promises about it, `docs/vocabulary.md`,
`docs/design.md` section 5, `docs/production-ledger.md`, and, for one disputed
fact, the press source (`src/press/build.py`). The chapter was not edited.

Status: **PASS WITH ONE BLOCK.** Every cross-reference names the right chapter
by its right title, "later in this chapter" is later each time, the numbering
is clean (four figures, five tables, five examples, no gap, slugs match
design.md), the three footnote labels carry the `7-` prefix, and the chapter
keeps every promise earlier chapters made about it. The registry table, the
filter order, the `press all` sequence, and the defaults templating agree with
Chapters 1, 6, and 8 with one exception: Chapter 7 states the no-stale rule
without the `press verify-formats` exception that Chapters 6 and 8 both state
(finding 1, blocks; also continuity-08, finding 3). Chapter 7 has three
shoulds and two mays of its own. Two shoulds belong to Chapter 8 and are new
(the Chapter 8 pass did not raise them); two mays belong to Chapters 3 and 1.

The bible (`docs/continuity.md`) now holds 33 new entries: 1 term, 14 shared
facts, 17 cross-references and promises, and 1 numbering row. Another 19
existing entries citing Chapter 7 are confirmed with current line numbers or
annotated with a conflict. The Chapter 8 pass, running at the same time,
had already logged the *invariant* term, the no-stale law, what each verify
target builds, the `press all` verifier order, and the source zip policy
(with `SOURCE_DATE_EPOCH`); those rows are confirmed, not duplicated.

## Findings

### 1. The no-stale rule is stated without its one exception (blocks; fix in Ch. 7)

Quote, l.339: "The press does not allow this through its command line. Every
verify target rebuilds the artifacts it verifies before it verifies them."
Quote, l.349: "`press verify-formats` builds the EPUB, the HTML, the Markdown,
text, and Word editions, the reader site, and the Source edition, and then runs
the format and archive verifiers."

Ch. 6 l.473: "The one exception is `press verify-formats`, which includes an
existing Print edition, *dist/alice.pdf*, in its cross-edition agreement check
without rebuilding it." Ch. 8 l.433 and l.439 state the same exception, draw it
as a dotted arrow in Figure 8.2, and give the exact scenario l.339 says cannot
happen ("If `alice` edits a chapter and runs only `press verify-formats`, the
agreement check compares the new editions with the PDF from whatever last built
it").

Rule: shared fact (which verify target rebuilds what). Severity: blocks.
The Chapter 8 pass raised the same block from its side (continuity-08,
finding 3, which also checked the source, `verify_formats.py` l.274); this is
the same finding, confirmed from Chapter 7, not a second one.

Fix (Ch. 7): at l.339, "The press does not allow this through its command
line, with one exception that the next section names." At l.349, after the
`verify-formats` sentence: "When `pdftotext` is present, it also reads whatever
*dist/alice.pdf* is there into its agreement check, without rebuilding it.
Chapter 8 describes what that costs."

### 2. Banned edition names (should; fix in Ch. 7)

Quotes: "Every edition except the Markdown edition and the Source edition"
(l.59); "The text and Word editions share `portable.yaml`" (l.80); "the
Markdown edition (the Manuscript edition), the text edition (the Telegraphic
edition), and the Word edition (the Office edition)" (l.275); headings "The
Markdown edition" (l.277) and "The text and Word editions" (l.281); "the
Markdown, text, and Word editions" (l.349); "waits on the Markdown edition"
(l.369); "the Markdown edition, the text edition, the Word edition" (l.414);
"# the Word edition" (l.473).

Rule: `docs/vocabulary.md` lists "the Markdown edition" and "the text edition"
under "never these"; the ledger ruling (Ch. 7 Revision 2 entry) lets a sentence
about the file use the format name, but a sentence about the edition uses
press's name. The gloss at l.45 and the parenthetical gloss at l.275 are right;
the uses after them are not. Severity: should (two names for one thing).

Fix: in sentences about the edition, say the Manuscript, Telegraphic, and
Office editions; in sentences about the file, say *dist/alice.md*, the Markdown
file, the plain text, the DOCX. Headings: "The Manuscript edition", "The
Telegraphic and Office editions". l.275: "the Manuscript edition (the stitched
Markdown), the Telegraphic edition (plain text), and the Office edition
(DOCX)". l.369: "waits on the Manuscript edition". l.414: "the Manuscript
edition, the Telegraphic edition, the Office edition". l.473: "# the Office
edition". l.80 is about the files and may read "The plain-text and Word
editions" only if changed to "The text and Word files".

### 3. The two Alices merged (should; fix in Ch. 7)

Quote, l.59: "The captures in this chapter come from the press's own
three-chapter Alice example, which `alice` keeps in *~/alice* on `hatter`."

Rule: cast, and the ledger ruling "the two Alices": *~/alice* on `hatter` is
the book's sample (the whole novel, made with `press new` in Ch. 3); the gallery
example lives in the press repository at *examples/alice-in-wonderland/*. The
slug-change ruling lets the captures read `alice` and *~/alice*, but the
sentence should not say that `alice` keeps the gallery example in *~/alice*.
Same defect as continuity-04, finding 2. Severity: should.

Fix: "The captures in this chapter come from the press's own three-chapter
Alice example, run on `hatter`; the paths read *~/alice* because its slug is
`alice`."

### 4. "Page bundle" beside "Pages bundle" (should; fix in Ch. 7)

Quotes: "The page bundle needs every other published artifact" (l.51), and the
same at l.271, 308 to 316, 349; but "# the GitHub Pages bundle" (l.477).

Rule: one name per thing. Ch. 1 (l.170, 200, 275) and Ch. 3 call *dist/pages/*
the Pages bundle, and the bible's shared fact is "The Pages bundle". Chapter 7
uses both. Severity: should.

Same as continuity-08, finding 2, which asks for a ruling and a vocabulary
row; this pass concurs.

Fix: "Pages bundle" throughout Ch. 7. l.316's distinction between the bundle
(the directory) and the Pages site (what GitHub Pages serves from it) is good
and should stay.

### 5. Chapter 8 shows the advisory line as every ordinary run's (should; fix in Ch. 8)

Quote, Ch. 8 l.447: "In an ordinary run the gate is advisory and says so,
`(commerce gate is advisory here; a release build (PRESS_RELEASE=1) enforces
it)`."

Ch. 7 l.426 to 433, Ch. 3 Example 3.10 (l.518), and Ch. 12 ("Print ordering
for readers", currently l.487): a book
without print ordering (the Alice example) prints `commerce release gate: print
ordering is not enabled; no commerce release gate`; only a book that enables
ordering gets the advisory line. Rule: shared fact (commerce gate lines).
Severity: should (Ch. 8 omits a condition rather than asserting its opposite).

Fix (Ch. 8): "In a book that enables print ordering, an ordinary run treats the
gate as advisory and says so, ... Without ordering, the gate prints `commerce
release gate: print ordering is not enabled; no commerce release gate`."

### 6. Chapter 8 writes the sources companion unconditionally (should; fix in Ch. 8)

Quote, Ch. 8 l.449: "That function deletes *build/generated/*, regenerates the
subject index, and writes *dist/alice-sources.md* from the authorities ledger."
Ch. 8 l.363 lists "the sources companion" among the nine artifacts `press
pages` builds, with no condition.

Ch. 7 l.365: "If the book has *config/authorities.yaml*, it writes
*dist/alice-sources.md* from that ledger" (the fact desk's correction, facts-07
item 8); Table 7.4 marks the `sources` row "yes (when authorities configured)";
Ch. 8 l.359 itself says the Alice example has no ledger. Rule: shared fact
(generated inputs). Severity: should.

Fix (Ch. 8): l.449 "and, when the book has *config/authorities.yaml*, writes
...". l.363 "and the sources companion when the book has a table of
authorities".

### 7. The registry defined as "a table" (may; Ch. 7)

Quote, l.295: "*the registry*, a table in *src/press/registry.py*". Figure 7.1's
caption: "The artifact graph the registry declares".

Rule: vocabulary, "the registry: the artifact graph in `registry.py`; never the
graph, the DAG, the table". Ch. 1 l.74 defines the registry as the artifact
graph. The definition reads as a second name, and the caption makes the graph
something other than the registry. Severity: may.

Fix: "*the registry*, the artifact graph that *src/press/registry.py* holds as
a table, with one entry per artifact." Caption: "The registry's artifacts and
their prerequisites".

### 8. The EPUB rights line overrides the `rights` field (may; fix in Ch. 3 or Ch. 7)

Ch. 7 l.234: the press builds the EPUB rights line as `<copyright> Published by
<publisher>, <place>.` and passes it with `--metadata rights=`. Ch. 3 l.194
(Table 3.3): "`rights` ... is a rights statement, which press passes through
to pandoc."

Checked in the press: `build.py` l.601 to 609 builds the value from
`copyright`, `publisher`, and `publisher_place` (the "Published by" clause drops
out when there is no publisher) and passes it with `--metadata`, which in
pandoc overrides the same key from the metadata file. So for the EPUB a book's
own `rights` value never reaches the file. Rule: shared fact. Severity: may (the
two statements describe different paths and neither is false for the other
editions).

Fix: in Ch. 3 Table 3.3, "... which press passes through to pandoc, except in
the EPUB, where the press writes its own rights line (Chapter 7)."

### 9. Chapter 1 says `press all` never builds the print pack (may; whole-book sweep)

Ch. 1 l.279: "`press all` does not build the print pack." Ch. 7 l.444 and Ch. 12
("Building the interior" and "Print ordering for readers", currently l.159
and 487; Ch. 12 is being revised, so cite by section): the commerce gate in a book that enables print ordering does build
`print` and `coverwrap`. Ch. 1 is committed, and its l.170 already ties the gate
to print ordering. Severity: may.

Fix (Ch. 1, in the whole-book sweep): "An ordinary `press all` does not build
the print pack, unless the book enables print ordering."

### 10. "Defaults file" used before it is defined (may; no fix needed)

Ch. 3 l.635 says "read the defaults file it used under *build/defaults/*"; Ch. 7
l.80 defines *defaults file*. The Ch. 3 use is plain enough in context. Logged
so the glossary (App. E) defines it once, from Ch. 7.

## Shared facts checked and agreeing

- The registry table (Table 7.4, Figure 7.1): `pages` waits on nine artifacts,
  `sources` on `markdown`, `coverwrap` on `print`. Agrees with Ch. 8 l.363
  ("nine prerequisites"), l.433 (`registry.ARTIFACTS`), Figure 8.2, Ch. 1 l.74,
  and Ch. 10 l.408.
- The filter order (Table 7.3, Figure 7.2): five filters in the shared chain,
  `print-safe-images` after `set-pieces` in print only, portable dropping
  `chapter-dropcap` and `scene-break`. Agrees with the Ch. 4 bible row.
- The `press all` sequence (Example 7.4, l.411 to 444): check (four passes,
  stops at the first refusal), formats (PDF, EPUB, HTML, Markdown, text, Word,
  site), source, pages, verify (pages, PDF, formats, archives), commerce gate.
  Agrees with Ch. 1 l.170 and Example 1.2, Ch. 3 l.533, Ch. 6 l.471, and Ch. 8
  l.442 to 447 (verifier order identical). Phase lines and `7 editions match
  source` agree with Ch. 1 Table 1.1 and Ch. 8 l.294.
- The defaults templating (l.90 to 143): `@press/`, `@book/`, `?optional`,
  `defaults reference a missing file`, rendered copies in *build/defaults/*.
  Ch. 3 l.635 agrees. No other chapter states it.
- `press render` at 160 dpi into *build/rendered-book/* (Ch. 3 l.637);
  `press wordcount` keeps HTML comments (Ch. 1 l.160, Ch. 3 l.549); 19
  known-bad fixtures, run by `press check` and `press all` but not a bare
  `press pdf` (Ch. 3 l.535, Ch. 6 l.141); `pandoc is required` (Ch. 1 l.248,
  Ch. 3 l.539); the empty `dc:date` and RSC-005 (Ch. 3 footnote, Ch. 8 l.260);
  `no assets/cover.jpg; interior verified, wrap not built` (Ch. 8 l.177);
  `INV-graph-no-stale`, critical, CLI path only (Ch. 8 l.431, 451);
  `press verify-pages` as another name for `press pages` (Ch. 8 l.363).
- Promises into Chapter 7, all kept: Ch. 2 l.381 (what `press all` builds; the
  print pack separate, l.371 to 448), Ch. 6 l.501 (builds each edition), Ch. 10
  l.408 (the companion in the registry, Table 7.4), Ch. 15 l.81 (the pilcrow
  phase lines and plus-sign lines, l.452 to 456).

## Not findings

- The gallery publisher "The Press (gallery example), Oxford" (l.234) is the
  press's own example's metadata, quoted as such.
- PNGs for Figures 7.1 to 7.4 are not yet drawn; the directives and alt text
  are in place.
- Ch. 8's heading "Archives and the source edition" (lowercase) belongs to the
  Chapter 8 pass.
