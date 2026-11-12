# Whole-book continuity sweep

Continuity editor, 2026-11-11. Scope: book/chapters/00 to 16, book/appendices/a to e and z-colophon, against docs/vocabulary.md, docs/continuity.md, and the late rulings in docs/production-ledger.md. Nothing is committed.

## Result

- 87 edits in 19 files, each one sentence or less and settled by a ruling, the vocabulary, or the bible (two edits refine an earlier edit on the same line: Ch. 4 l.18 and Ch. 8 l.363). The full list is in "Edits" below.
- `press check` passes after the edits (source checks, checker self-test, editorial checks, jargon). The first run failed at Ch. 8 l.363 ("avoiding is/has" on "serves as"); the sentence was reworded (edit 87) and the second run passed.
- docs/continuity.md updated: a sweep note above the Fixed cast; rows for the gallery example's names, logomark, the editions, the Source zip policy, sentinel places, discovery and sorting, and the Ch. 8 reference ledger.

## Checks and what they found

| Check | Result |
|---|---|
| "Chapter N, *Title*" | 225 references, every title final and matching its number (script over every file, fences excluded). "The next chapter, *Title*" in Ch. 2, 4, 5, 8 names N+1. |
| "later/earlier in this chapter", "next/previous section", "in the section ..." | Every one checked (about 75): every named section exists (A-head or B-head, such as Ch. 3 "Verification knobs" l.218 and Ch. 12 "The layout" l.173) and lies in the claimed direction. |
| Alice naming | Ch. 1, 2, 3, 4, 6, 7, 8 brought to "the press's own three-chapter Alice example" at first mention and "the three-chapter example" after; Ch. 4 l.18 "the sample book" became "the Alice book"; Ch. 2 l.389 "the `alice` book" became "the Alice book"; Ch. 13 l.79 fresh-scaffold capture no longer labelled as the Alice book (ruling, ch 13). |
| Pages bundle / Pages site | Ch. 1 "GitHub Pages bundle" (2), Ch. 3 l.621, Ch. 6 l.361, Ch. 8 l.363 and 404 fixed. |
| the logomark, height cap | "logo" / "press logo" fixed in Ch. 3, 7, 10; "image cap" (Ch. 10 l.214) and "figure height cap" (Ch. 11 l.272) now "height cap". |
| table of authorities | "authorities ledger" fixed in Ch. 8 (3). |
| Edition glosses | Parenthesised gloss added or converted from a comma appositive in Ch. 5 l.267, 9 l.21, 228, 230, 10 l.20, 301, 16 l.74, App. A l.751, 1106; Ch. 8 heading "Archives and the source edition" capitalised in all three places; Ch. 7 l.275 second italic definition of *Source edition* made roman. |
| "Press" capitalised | Only at sentence starts and in the book's title. No fix needed. |
| Provider id | `ingramspark` throughout; `ingram` appears only as the `press publish` channel and *publish-ingram.md*, press's own names, kept verbatim. |
| Retail rule | Ch. 3 l.265, Ch. 13 l.136 and 315, App. B l.158 already correct. Ch. 6 l.62 lacked the LCCN/ISSN half: fixed. Ch. 10 l.182 aligned. Ch. 1 does not state the rule at all (no fix; see ruling 10). |
| `press all` and the print pack | Ch. 1 l.279 now carries the commerce-gate exception (ledger sweep item); Ch. 7 l.444 and App. A l.84 already agree; Ch. 12 l.159 now names the Pages bundle. |
| Source archive | Ch. 3 l.566 and App. A l.1106 already state the ruling. Ch. 7 l.35, 287 and Ch. 8 l.337 said "only those": ruling added. |
| Sentinel messages | Ch. 1 l.250 `sentinel ... not found` replaced by `sentinel not found in the manuscript:` (ledger, ch 6 continuity). Ch. 3, 6, 8 and App. C already verbatim. |
| Footnotes | 61 notes, every label prefixed by chapter number or appendix letter, unique, each referenced once. `[^2-well]` in Ch. 4 l.175 and 181 sits in a fence and in inline code (the reverted example), so it is not a note. |
| Figures | 45 figures: per chapter in sequence, slugs `CC-NN-slug` in appearance order, every `@fig:` resolved and cited before its figure. The two unresolved ids in Ch. 5 (`alice-heights` in a fence, `alice-hieghts` as the deliberate typo) are examples. |
| Tables, examples | Every caption in sequence with no gap, and each referenced before it appears. |
| Preface Organization | Matches every final title. Ch. 10 blurb lacked the table of authorities (an A-head and the title): fixed. Other blurbs agree in substance; omissions noted under ruling 12. |
| Glossary | Headword **commerce** renamed **commerce gate** (Ch. 12 l.159 defines it); **Pages site** added (Preface l.153 defines it; vocabulary settles the wording); chapter pointers widened for composite action, reusable workflow, toolchain image, build/; Pages bundle and print ordering entries aligned with the Pages bundle/site split. About 35 italic-defined terms still have no entry: ruling 11. |
| ASCII | No dashes or curly quotes added. The only non-ASCII bytes are press's own glyph table in Ch. 4 and the desk capture in Ch. 7, both in fences and intended. |
| Index | All 249 terms still hit prose after the edits (approximate script check; `press all` makes the authoritative check). |

## Needs a ruling

1. **Index order: Ch. 4 against Ch. 3 and the bible.** Ch. 4 l.52: "merges the chapters first, then the appendixes, then the generated subject index." Ch. 3 l.380, the defining text, says "the generated subject index takes its place among the appendixes by its own letter", and Ch. 4's own l.66 says the index "usually sorts before the appendixes you write yourself". The bible's Discovery and sorting row agreed with Ch. 4; the sweep corrected the bible to Ch. 3. Recommended: "merges the chapters first, then the appendixes in letter order, with the generated subject index among them by its own letter."
2. **`press all` and the print pack in Ch. 16.** Ch. 16 l.82: "The `publish` checklist, the edition manifest, qualification, and the commerce gate follow." In the print-pack branch, this reads as though `press all` builds the print pack. Recommended: "The `publish` checklist, the edition manifest, and qualification follow; the commerce gate at the end of `press all` builds this branch only for a book that enables print ordering."
3. **Wrap placeholder against the retail rule.** Ch. 12 l.251: "A book with no ISBN yet still gets a wrap." Under `retail: true` a missing ISBN fails `press check`; whether `press coverwrap` itself refuses is not in the fact base. Recommended (after a fact check): "A book with no ISBN yet, and not declared for retail, still gets a wrap."
4. **Timeouts.** Ch. 16 l.124 gives the adapters HTTP client "a 30-second timeout"; Ch. 13 Table 13.4 gives `press lookup` "10 seconds". Both may be true (a default and a per-call limit). Recommended: the fact checker confirms against facts-13/facts-16 and Ch. 16 adds "by default".
5. **"fact base" in Ch. 9.** Ch. 9 l.146: "the profile descriptions in the press's fact base". The fact base is this book's research, not part of press (Preface l.143 calls it "the fact base"). Recommended: "the press's own profile descriptions", if facts-12 takes them from the profiles; otherwise "the profile descriptions in our fact base".
6. **"validator" in Ch. 3.** Ch. 3 l.279: "*config/aesthetic.yaml*, which has no validator", while Ch. 3 l.360 shows `press config validate` printing `config/aesthetic.yaml: ok`. A fact question as well as a word. Recommended: the fact checker states what `config set` checks for the aesthetic, then the sentence says that without "validator".
7. **"every book lives in a Git repository".** Ch. 2 l.19 and l.28 overstate against the Source-archive ruling (a book outside Git builds and archives whole). Recommended: "because a book normally lives in a Git repository". Severity may.
8. **"output" for an artifact's files.** Ch. 15 Table 15.3 (l.101 to 103): "The artifact's output does not exist", "The output exists", "several outputs". If the desk prints these words, keep them; if they are the writer's, recommended "The artifact's files do not exist" and so on. Severity may.
9. **Edition gloss by appositive.** Ch. 9 l.177 "the Chapter edition, the reader site:" stays an appositive because a parenthesis there reads badly ("(the reader site and its zip)" beside a sentence about the site). The vocabulary's "in parentheses" wording would need either a rewrite of the sentence or an allowance for appositive glosses. Recommended: allow an appositive gloss where it names the format. Ch. 7 l.275 and Ch. 13 l.214 gloss an edition a second time; harmless, left.
10. **Ch. 1 and the retail rule.** The brief lists Ch. 1 among the chapters that state the retail rule, but Ch. 1 never states it (its only registration mention is "registered ISBNs", l.64). Recommended: leave Ch. 1 as it is; the rule lives in Ch. 3, 6, 10, 13 and App. B.
11. **Glossary gaps.** These italic-defined terms have no Appendix E entry. Each entry is new copy, so none was added: Alice book and the three-chapter example (Preface l.129); data kind (Ch. 5 l.26); List of Figures, List of Plates (Ch. 5 l.130); folio (Ch. 9 l.123); tokens (Ch. 9 l.179); logomark (Ch. 11 l.18); cover style (Ch. 11 l.113); flat-ground test (Ch. 11 l.290); author portrait (Ch. 11 l.454); allowance (Ch. 12 l.92); trim, bleed (l.175); safety (l.177); inner offset (l.191); module (l.227); quiet zone (l.256); disposition (l.319); registration (Ch. 13 l.21); upload bundle (Ch. 14 l.54); hash lock (l.120); digest (l.160); release receipt (l.217); read model (Ch. 15 l.43); prose skills (l.135); maxim quota (l.204); scout, suggest, synthesize, law and the lenses cadence, repetition, arc (l.214 to 220; perhaps one "editorial passes" entry); integration gate (Ch. 16 l.25); producer, producer ledger (l.228); writable, immutable, file (field kinds, Ch. 3 l.354, beside the existing "structured field"). Recommended: the glossary writer adds them from the bible's term table, with the logomark, registration, upload bundle, trim, bleed, and safety first.
12. **Preface blurbs, omissions in substance (may).** Ch. 1 omits "What press is not" and versions; Ch. 3 omits `press config`, the Makefile, Git, and build/dist; Ch. 9 omits the landing page, the aesthetic file, and extra CSS; Ch. 12 omits profiles, the barcode, verification, and qualification; Ch. 16 omits the adapters boundary, the quality gate, receipts, and extensions. Acceptable for a summary; Recommended: no change unless the managing editor wants every A-head named.
13. **Index comments in appendixes.** `<!-- index: ... -->` comments remain at the end of App. A, B, C, D; the ledger records stripping them from chapters 00 to 16 only. Recommended: strip them for consistency.
14. **`figure-cap` named once in Ch. 5.** The vocabulary asks for the key name once; Ch. 5 l.287 defines *height cap* without naming `figure-cap`. Recommended: "a maximum height that each design profile sets in its `figure-cap` key", after checking l.287's "set in the house TeX header" against the bible row.
15. **Minor wording (may).** Ch. 1 l.271 Table 1.2 "An archive of the files Git tracks" (true for a Git book; leave or add the outside-Git case); Ch. 3 heading "What git has to do with it" lowercases Git (l.70 quotes it); Ch. 15 l.290 "the logomark, the printer's mark" (vocabulary says press's own mark is the pilcrow; consider "the imprint device"); Ch. 15 l.346 "fingerprint" for a digest; Ch. 14 l.363 *vacuous witnesses* sits beside the quoted refusal, which the vocabulary allows; art comments at Ch. 10 l.263 ("figure cap") and Ch. 11 l.43 ("folder") do not print.

## Edits

| # | File | Line | Before | After |
|---|---|---|---|---|
| 1 | chapters/00-preface.md | 53 | Covers the front-matter file key by key, the title and copyright pages, the subject index, and the sources companion. | Covers the front-matter file key by key, the title and copyright pages, the subject index, the table of authorities, and the sources companion. |
| 2 | chapters/01-introduction.md | 170 | from a run on the press's own Alice example, which has three chapters and an appendix, and elides | from a run on the press's own three-chapter Alice example, which also has an appendix, and elides |
| 3 | chapters/01-introduction.md | 208 | For the Alice example, the PDF line reports | For the three-chapter example, the PDF line reports |
| 4 | chapters/01-introduction.md | 277 | The Alice example has no authorities file, so its | The three-chapter example has no authorities file, so its |
| 5 | chapters/01-introduction.md | 200 | The press built the GitHub Pages bundle in | The press built the Pages bundle in |
| 6 | chapters/01-introduction.md | 275 | The GitHub Pages bundle, *dist/pages/*, gathers | The Pages bundle, *dist/pages/*, gathers |
| 7 | chapters/01-introduction.md | 250 | 3. `sentinel ... not found`. The checker | 3. `sentinel not found in the manuscript:`. The checker |
| 8 | chapters/01-introduction.md | 279 | `press all` does not build the print pack. Its own targets do | `press all` does not build the print pack, except through the commerce gate in a book that enables print ordering. Its own targets do |
| 9 | chapters/02-installing-press.md | 327 | it builds the PDF of the press's own Alice example. | it builds the PDF of the press's own three-chapter Alice example. |
| 10 | chapters/02-installing-press.md | 389 | creates the `alice` book with `press new` | creates the Alice book with `press new` |
| 11 | chapters/03-the-shape-of-a-book.md | 502 | **Example 3.10. press all on the press's own Alice example, in part** | **Example 3.10. press all on the three-chapter example, in part** |
| 12 | chapters/03-the-shape-of-a-book.md | 120 | takes the cover, the press logo, the plates | takes the cover, the logomark, the plates |
| 13 | chapters/03-the-shape-of-a-book.md | 621 | The bundle also includes the cover, the logo, and the plates | The bundle also includes the cover, the logomark, and the plates |
| 14 | chapters/03-the-shape-of-a-book.md | 621 | The directory *pages/* is the bundle that GitHub Pages serves. | The directory *pages/* is the Pages bundle, which GitHub Pages serves. |
| 15 | chapters/04-writing-the-manuscript.md | 18 | The examples come from the press's own Alice example, the gallery book that holds the first three chapters of Carroll's novel. The sample book `alice` keeps on the workstation `hatter` is the whole novel, and it sets these constructs the same way. | The examples come from the press's own three-chapter Alice example, the gallery book that holds the first three chapters of Carroll's novel. The Alice book, which `alice` keeps on the workstation `hatter`, is the whole novel, and it sets these constructs the same way. |
| 16 | chapters/04-writing-the-manuscript.md | 44 | opening page of the first chapter of the Alice example. | opening page of the first chapter of the three-chapter example. |
| 17 | chapters/04-writing-the-manuscript.md | 46 | ![The parts of a printed page in the Alice example] | ![The parts of a printed page in the three-chapter example] |
| 18 | chapters/04-writing-the-manuscript.md | 58 | The Alice example holds the first three chapters of Carroll's book. If its | The three-chapter example ends with Carroll's third chapter. If its |
| 19 | chapters/04-writing-the-manuscript.md | 208 | from the first two chapters of the Alice example. | from the first two chapters of the three-chapter example. |
| 20 | chapters/04-writing-the-manuscript.md | 260 | The Alice example sets a three-line drop cap | The three-chapter example sets a three-line drop cap |
| 21 | chapters/04-writing-the-manuscript.md | 280 | **Example 4.5. The Alice example's chapter opening** | **Example 4.5. The three-chapter example's chapter opening** |
| 22 | chapters/04-writing-the-manuscript.md | 297 | The second chapter of the Alice example opens with speech: | The second chapter of the three-chapter example opens with speech: |
| 23 | chapters/04-writing-the-manuscript.md | 329 | The Alice example uses `fairy-dust` | The three-chapter example uses `fairy-dust` |
| 24 | chapters/04-writing-the-manuscript.md | 335 | **Example 4.6. The Alice example's scene break** | **Example 4.6. The three-chapter example's scene break** |
| 25 | chapters/04-writing-the-manuscript.md | 357 | The Alice example uses a cascade for the address | The three-chapter example uses a cascade for the address |
| 26 | chapters/04-writing-the-manuscript.md | 359 | **Example 4.7. A cascade in the Alice example** | **Example 4.7. A cascade in the three-chapter example** |
| 27 | chapters/04-writing-the-manuscript.md | 18 | the gallery book that holds the first three chapters of Carroll's novel. The Alice book | the gallery book that holds the opening of Carroll's novel. The Alice book |
| 28 | chapters/05-figures-and-plates.md | 267 | the Chapter edition (the reader site) | the Chapter edition (the reader site and its zip) |
| 29 | chapters/06-checking-the-manuscript.md | 62 | and it refuses a retail book whose ISBNs are missing or pending. | and it refuses a retail book whose ISBN is missing or pending, or whose declared LCCN or ISSN is still pending. |
| 30 | chapters/06-checking-the-manuscript.md | 361 | in each edition, and on the public reading site. | in each edition, and in the Pages bundle. |
| 31 | chapters/07-building-the-editions.md | 22 | the build order, the verification pipeline, the filenames | the build order, the verifiers, the filenames |
| 32 | chapters/07-building-the-editions.md | 161 | [^7-epoch]: The value falls on July 16, 2026. | [^7-epoch]: The value falls on 2026-07-16. |
| 33 | chapters/07-building-the-editions.md | 35 | \| Press packs the files that Git tracks, and nothing else, into a zip. Pandoc takes no part. \| | \| Press packs the files that Git tracks into a zip, or the whole book when it sits outside any Git repository. Pandoc takes no part. \| |
| 34 | chapters/07-building-the-editions.md | 287 | The zip holds the files that Git tracks in the book repository, and only those. | The zip holds the files that Git tracks in the book repository, and only those; a book outside any Git repository is archived whole, and one untracked inside a parent repository archives nothing. |
| 35 | chapters/07-building-the-editions.md | 454 | The Alice run timed only the PDF, so it printed no summary. | The run on the three-chapter example timed only the PDF, so it printed no summary. |
| 36 | chapters/07-building-the-editions.md | 484 | takes the cover, the press logo, and the plates | takes the cover, the logomark, and the plates |
| 37 | chapters/08-verifying-the-artifacts.md | 10 | > - Archives and the source edition | > - Archives and the Source edition |
| 38 | chapters/08-verifying-the-artifacts.md | 210 | the section "Archives and the source edition" later | the section "Archives and the Source edition" later |
| 39 | chapters/08-verifying-the-artifacts.md | 325 | ## Archives and the source edition | ## Archives and the Source edition |
| 40 | chapters/08-verifying-the-artifacts.md | 337 | - Members are files that Git tracks, and only those. A file that you never committed to Git is not a member. | - Members are files that Git tracks, and only those; a book outside any Git repository is archived whole, and one untracked inside a parent repository archives nothing. A file that you never added to Git is not a member. |
| 41 | chapters/08-verifying-the-artifacts.md | 44 | when the book has an authorities ledger. \| | when the book has a table of authorities. \| |
| 42 | chapters/08-verifying-the-artifacts.md | 359 | for the three-chapter Alice example, which has no authorities ledger: | for the three-chapter example, which has no table of authorities: |
| 43 | chapters/08-verifying-the-artifacts.md | 363 | builds the Pages bundle, the public Web site of the book, in *dist/pages*. | builds the Pages bundle in *dist/pages*, the directory that GitHub Pages serves as the Pages site. |
| 44 | chapters/08-verifying-the-artifacts.md | 404 | \| The manuscript, the PDF, every edition, and the public site \| | \| The manuscript, the PDF, every edition, and the Pages bundle \| |
| 45 | chapters/08-verifying-the-artifacts.md | 449 | writes *dist/alice-sources.md* from the authorities ledger. | writes *dist/alice-sources.md* from the table of authorities. |
| 46 | chapters/08-verifying-the-artifacts.md | 128 | so the reader arrives on the wrong leaf. | so the reader arrives on the wrong page. |
| 47 | chapters/06-checking-the-manuscript.md | 410 | **Example 6.12. A passing check on the press's own three-chapter Alice example** | **Example 6.12. A passing check on the three-chapter example** |
| 48 | chapters/06-checking-the-manuscript.md | 431 | ![A passing check on the press's own three-chapter Alice example] | ![A passing check on the three-chapter example] |
| 49 | chapters/07-building-the-editions.md | 498 | On the press's own three-chapter Alice example, it prints | On the three-chapter example, it prints |
| 50 | chapters/08-verifying-the-artifacts.md | 194 | Example 8.1 shows a real run from the press's own three-chapter Alice example, which | Example 8.1 shows a real run from the three-chapter example, which |
| 51 | chapters/08-verifying-the-artifacts.md | 196 | **Example 8.1. A press verify run on the three-chapter Alice example** | **Example 8.1. A press verify run on the three-chapter example** |
| 52 | chapters/08-verifying-the-artifacts.md | 274 | Example 8.2 shows a real run on the three-chapter Alice example, | Example 8.2 shows a real run on the three-chapter example, |
| 53 | chapters/08-verifying-the-artifacts.md | 276 | **Example 8.2. A press verify-formats run on the three-chapter Alice example** | **Example 8.2. A press verify-formats run on the three-chapter example** |
| 54 | chapters/08-verifying-the-artifacts.md | 427 | The three-chapter Alice example stitches four files | The three-chapter example stitches four files |
| 55 | chapters/08-verifying-the-artifacts.md | 447 | such as the three-chapter Alice example, the run prints | such as the three-chapter example, the run prints |
| 56 | chapters/07-building-the-editions.md | 275 | It also packs the book repository itself into the *Source edition*, a zip | It also packs the book repository itself into the Source edition, a zip |
| 57 | chapters/09-the-house-design.md | 21 | Open the reading PDF of the Alice book, the Print edition, and you see | Open the Print edition (PDF) of the Alice book, and you see |
| 58 | chapters/09-the-house-design.md | 228 | The Single-leaf edition, the self-contained HTML, uses *book.css*. | The Single-leaf edition (the self-contained HTML) uses *book.css*. |
| 59 | chapters/09-the-house-design.md | 230 | The Circulating edition, the EPUB, uses *epub.css*. | The Circulating edition (EPUB) uses *epub.css*. |
| 60 | chapters/10-front-matter-index-authorities.md | 20 | set the opening pages of the Print edition, the PDF. | set the opening pages of the Print edition (PDF). |
| 61 | chapters/10-front-matter-index-authorities.md | 301 | The Circulating edition, the EPUB, reflows its text | The Circulating edition (EPUB) reflows its text |
| 62 | chapters/10-front-matter-index-authorities.md | 301 | and the Telegraphic edition, the plain text, has no pages at all. | and the Telegraphic edition (plain text) has no pages at all. |
| 63 | chapters/10-front-matter-index-authorities.md | 176 | \| Logo \| The press sets its logo from *assets/press-logo.png*, at 1.7 inches. \| | \| Logomark \| The press sets the logomark from *assets/press-logo.png*, at 1.7 inches. \| |
| 64 | chapters/10-front-matter-index-authorities.md | 180 | It has no logo file either, | It has no logomark either, |
| 65 | chapters/10-front-matter-index-authorities.md | 182 | and the `retail` switch that refuses a pending number in a book for sale. | and the `retail` switch, under which a missing or pending ISBN, or a declared LCCN or ISSN still pending, fails the build. |
| 66 | chapters/10-front-matter-index-authorities.md | 184 | every image, the logo included, | every image, the logomark included, |
| 67 | chapters/10-front-matter-index-authorities.md | 214 | the same scar as the image cap, | the same scar as the height cap, |
| 68 | chapters/11-the-art-department.md | 272 | enforces the figure height cap when | enforces the height cap when |
| 69 | chapters/12-the-print-pack.md | 159 | It builds and verifies every edition a reader downloads. The print pack | It builds and verifies every edition a reader downloads, and the Pages bundle that serves them. The print pack |
| 70 | chapters/13-registrations.md | 79 | In a fresh scaffold of the Alice book, with no block yet, it says so | In a fresh scaffold, with no block yet, it says so |
| 71 | chapters/16-inside-the-press.md | 266 | downloads the `receipt-quality` and `receipt-integration` artifacts. | downloads the `receipt-quality` and `receipt-integration` upload bundles. |
| 72 | chapters/16-inside-the-press.md | 74 | The EPUB writer makes the Circulating edition, and the HTML writer makes the Single-leaf edition. The chunked HTML writer makes the Chapter edition. | The EPUB writer makes the Circulating edition (EPUB), and the HTML writer makes the Single-leaf edition (the self-contained HTML). The chunked HTML writer makes the Chapter edition (the reader site and its zip). |
| 73 | chapters/16-inside-the-press.md | 74 | The plain and DOCX writers make the Telegraphic and Office editions. | The plain and DOCX writers make the Telegraphic edition (plain text) and the Office edition (DOCX). |
| 74 | appendices/e-glossary.md | 86 | **commerce** / : The gate | **commerce gate** / : The gate |
| 75 | appendices/e-glossary.md | 93 | never with pip from Git (Chapter 2). | never with pip from Git (Chapters 2 and 14). |
| 76 | appendices/e-glossary.md | 345 | It pins the *composite action* and the *toolchain image* (Chapter 2). | It pins the *composite action* and the *toolchain image* (Chapters 2 and 14). |
| 77 | appendices/e-glossary.md | 417 | Every CI build runs in it (Chapters 1 and 2). | Every CI build runs in it (Chapters 1, 2, and 14). |
| 78 | appendices/e-glossary.md | 48 | : The directory of intermediate files, none of them published (Chapter 1). | : The directory of intermediate files, none of them published (Chapters 1, 3, and 7). |
| 79 | appendices/e-glossary.md | 279 | : The directory *dist/pages/*, which GitHub Pages serves (Chapters 1 and 7). | : The directory *dist/pages/*, which `press pages` assembles and from which GitHub Pages serves the *Pages site* (Chapters 1 and 7). /  / **Pages site** / : What GitHub Pages serves from the *Pages bundle*: the book's public Web site (Preface, Chapters 7 and 14). |
| 80 | appendices/e-glossary.md | 315 | : The optional ordering of printed copies from the book's Web site (Chapters 8 and 12). | : The optional ordering of printed copies from the book's *Pages site* (Chapters 8 and 12). |
| 81 | appendices/a-command-reference.md | 751 | Stitches the Manuscript edition, *dist/alice.md*, | Stitches the Manuscript edition (the stitched Markdown), *dist/alice.md*, |
| 82 | appendices/a-command-reference.md | 1106 | Packages the Source edition, *dist/alice-source.zip*. | Packages the Source edition (the source zip), *dist/alice-source.zip*. |
| 83 | appendices/b-configuration-reference.md | 367 | such as *book/chapters/03-price.md*. | such as *book/chapters/00-preface.md*. |
| 84 | appendices/b-configuration-reference.md | 83 | A drop cap (any `chapter-opening.style` other than `none`) splits | A chapter opening (any `chapter-opening.style` other than `none`) splits |
| 85 | appendices/c-messages.md | 303 | where a drop cap splits it. | where a chapter opening splits it. |
| 86 | appendices/c-messages.md | 47 | because a drop cap splits the first word in the PDF. | because a chapter opening splits the first word in the PDF. |
| 87 | chapters/08-verifying-the-artifacts.md | 363 | the directory that GitHub Pages serves as the Pages site. | the directory from which GitHub Pages serves the Pages site. |
