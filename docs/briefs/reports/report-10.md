# Report: Chapter 10, Front matter, the index, and the table of authorities

File: `book/chapters/10-front-matter-index-authorities.md`

## Word count

`press wordcount`: 5,095 (target 4,500; +13 percent, inside 15). Running
prose alone (outside tables, examples, captions, art comments) is about
3,300 words over 203 sentences, average 16.2 words, none over 30.

## Numbered items (each referenced before it appears)

- Tables 10.1 (parts not generated), 10.2 (front-matter keys), 10.3 (title
  page, top to bottom), 10.4 (copyright-page lines in order), 10.5 (when
  front matter generates), 10.6 (authorities keys), 10.7 (ledger faults).
- Examples 10.1 (scaffolded front-matter.yaml, verbatim), 10.2 (`press
  config set` for Alice), 10.3 (Alice index-terms.yaml), 10.4 (zero-hit
  refusal), 10.5 (Alice authorities.yaml), 10.6 (ledger refusal).
- One sidebar ("Why the index has no page numbers", about 150 words), six
  tips and warnings, four footnotes.

## Figures

- **10.1** `@fig:config-to-front-matter`, data-flow, left to right:
  metadata.yaml and front-matter.yaml at the left, seven page outlines in
  order (title page, copyright page, dedication, epigraph,
  acknowledgements, contents, lists), each arrow labelled with the keys it
  carries; a third dashed input from the chapters feeds contents and lists.
- **10.2** `@fig:index-entry-path`, flowchart, top to bottom: a term in
  index-terms.yaml, strip code and image lines, whole-word case-insensitive
  match, "Any hits?" diamond; No goes to "build stops" with the gen_index
  message, Yes to an entry with locators "1, 3, A" in "Appendix A: Index of
  subjects".

## Facts needed and not found (left out)

- The exact form of the stacked-subtitle split (case sensitivity of
  `;? or,`). The template comment says `"OR, ...; OR, ..."`; I used a
  lowercase "; or," example, which matches either way, and made no claim
  about capitals.
- Alice's real publisher, place, copyright line and subtitle are not in the
  fact file. Example 10.2 has user `alice` set "Wonderland Press",
  "Oxford", "Copyright 2026 Wonderland Press", and a demonstration double
  subtitle; the prose presents them as values alice sets, not as the
  shipped example's values.
- Exact spacing of a companion entry with no `url`; I showed only the
  template shape and did not render a sample entry.
- Whether the authorities matcher ignores code or Markdown emphasis; not
  stated.
- The index entry separator in the fact file is U+00B7, outside the glyph
  law; described as "a separator".
- The scaffold's comment on config/front-matter.yaml says the identity
  facts include `date`, but the required-keys list omits it; I said the
  list omits `date` and both pages read it.

## Contradictions in the fact file

- Docs claim a "page-accurate" index; code uses chapter/appendix labels.
  Followed the code (section 20.A.6).
- The CLI example in the fact file sets copyright to a value containing
  U+00A9, which no chapter can hold; I replaced it with an ASCII line.

## Checker residuals and defence

- `press check`: no finding names this file. It exits 1 on
  `09-the-house-design.md` and `11-the-art-department.md` (other writers).
- Example 10.1 reproduces the scaffold verbatim, as asked; 13 of its lines
  exceed 64 columns and will wrap with a hook. markup.md calls this
  tolerable for a real file reproduced exactly.
- `ste_check.py` residuals: four semicolons, all inside verbatim quotations
  of press (the no-front-matter message, the index rationale, the
  "not a citation engine" line) or the index comment. One passive ("are
  stated") is the quoted first law. Sentence-length hits on lines 6, 138,
  278 and 317 are the In-this-chapter box, the figure image/art lines, and
  run-on counting across list and sidebar lines; perfect tense "has
  generated" etc. are mis-parses (adjective "generated"). "therefore" is
  period-correct per the prose contract. `-ing` hits are the brief's own
  A-heads and "counting".

## Revision (after facts, dev, copy, and type desks)

Word count after revision: 5,148 (`press wordcount`; +14 percent, inside
15). `press check`: no finding names this file. `press figures` lists
both figures with their `art:` descriptions (one blank line between
image line and comment, as inserted).

### Rulings applied

1. S1: line 204 rewritten. The generated pages end at the
   acknowledgments; the Contents comes from pandoc's table of contents and
   the two lists from the house TeX header, each only with plates or
   numbered figures. Figure 10.1 redrawn: five generated pages fed by the
   two config files, plus a gray "from elsewhere" group (Contents, List
   of Plates, List of Figures) with dashed arrows from "pandoc toc" and
   "TeX header". S2: Alice has no registrations and no logo; the
   copyright-page walk-through now says so; the ledger is something alice
   writes ("has no ledger yet").
2. Reasoning: `turtle` now carries the boundary-rule example; `mock
   turtle` misses "mock-turtle" because of space versus hyphen. The `file`
   tip now says the press "notices when a claim leaves its chapter";
   Table 10.7 says `moved` applies only when the entry declares a `file`.
3. Developmental: override described in prose (replaces every generated
   page; must hold every opening page you want), no invented skeleton.
   Example 10.7 shows the companion's shape with angle-bracket fields only.
   Example 10.5 now has two entries, and Example 10.6's two faults
   (missing, ambiguous) both refer to them. The tip now guards hand-trimmed
   or adopted metadata, agreeing that the scaffold fills the five keys.
   `\maketitle` cut; `titlepage` glossed as "the LaTeX block that sets a
   page of its own", warning moved after the cap paragraph and states the
   failure. Example 10.2 sets `date`. Cross-references: Chapter 3, *The
   shape of a book repository*; Chapter 5, *Figures, plates, and
   illustrations*. Dedication/epigraph/acknowledgments looks given once
   (prose); Table 10.2 cells say only what each key holds. Cut:
   `INV-front-matter-golden`, `BOOK_PUBLISHER`, the `%<<if>>` markers, the
   print-assets path; the second-rule history moved to a footnote.
   Example 10.4 named in prose before it appears. Orientation and the
   "three kinds" count now put the ledger beside the book (C1, O1).
4. Copy blocks: closer at 281 deleted; "proves" -> "shows"; "fallback"
   tip rewritten; both -ing riders removed ("counting from one" cut as
   unsupported; "doing nothing" -> "has no effect"). Editions: Print,
   Circulating, Single-leaf, Telegraphic, each glossed; "eight editions"
   by the vocabulary's and Chapter 3's count (Print, Circulating,
   Single-leaf, Manuscript, Telegraphic, Office, Chapter, Source).
   American spellings (acknowledgments, color, labeled, period,
   exclamation point); YAML key `acknowledgements` kept. *artifact* and
   *verifier* italic and defined; "target" and "invariant" no longer
   appear. Table cells are sentences. Sidebar six sentences, about 130 words.
   Tip at 390 no longer repeats the paragraph. Items 18 to 32 applied.
5. Markup: every fence `text`; Example 10.1 excerpted to the key lines,
   all under 64 columns, with `...` lines and a prose note naming what
   was cut (opening comment, paraphrased and quoted in prose; colophon
   comment; folded sample text; the 70-column `motto` line). Footnote
   labels now `10-`.

### Fact-desk items

Applied: 1 (contents), 2 (BOOK_PUBLISHER cut), 3 (year: "the year", with
a pointer to Chapter 3 for how it is found), 4 (landing page cut), 5
(companion: "published as a download", build timing cut), 6 (editions,
per ruling), 7 (override), 8 (workflow), 9 (typed model cut), 10, 11
(counting cut; the examples still number entries from 1, which I did not
confirm), 12 (S2), 13 (roman footnote softened; glossary quote now "the
press calls"; golden-copy and "book's own order" cut; companion
"therefore passes" cut). Drifted 2 (shape-error tail restored, broken
with disclosure), 3, 4, 5, 6, 7 applied. Drifted 1: breaks kept with
disclosure, per the type desk. Missing 1 applied (`{-}`, no section
number).

### Declined mays (one line each)

- Fact Missing 2 (ambiguous/moved verbatim): Example 10.6 now shows the
  real `ambiguous ... appears 2 times in <file>` form; the `matches T
  times (<file> xN, ...)` form would exceed 64 columns for little gain.
- Copy 35, 36, 37, 41: the sentences they touch were rewritten or cut.
- Type should 3 (figure height): added "no taller than the house figure
  cap" to the Figure 10.2 directive; no `place=plate`.

### Residual uncertainty

- The `<file>` rendering inside the `ambiguous` message in Example 10.6
  is assumed to be the declared path.
- `ste_check.py` residuals are as before: semicolons only inside quoted
  press text or the index comment; "are stated" is the quoted first law;
  long-sentence hits are the In-this-chapter box, the figure lines, the
  footnote-marker join at the colophon paragraph, and quotes; "-ing"
  hits are the brief's A-heads and Chapter 8's title.

## Revision 2

Applied the re-review's two items: "hands out letters from `z-` downward", and the sidebar's repeat gloss of the Print edition cut. Example 10.6 unchanged (supported by fact file S3). `press check`: no finding names this file.
