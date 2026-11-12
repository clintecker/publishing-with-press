# Proof report: Publishing with Press, HEAD cd41d01

Read from build/docker4/dist/publishing-with-press.pdf (382 pages), rendered with
`pdftoppm -r 110` into build/proof-render/. Folio = PDF page minus 9 from Chapter 1 on;
front-matter pages are given as "PDF p.N".

**Findings: 24. Blocks (text lost, wrong number, wrong fact in a cross-reference): 2** (items 3 and 19).

Method. Every page image read (in 2x2 montages, ten pages a run or so, full-size crops for
anything suspect). Mechanically checked across the whole PDF text: every "Figure/Table/Example
N.M" reference resolves to a caption that exists (no gaps, no dangling numbers, 565
references); every "Chapter N, *Title*" and "Appendix X, *Title*" matches the Contents; List of
Figures titles and pages match the captions; no line of set text runs past the 56 to 384 pt
measure; no em or en dash in the set text (the only U+2014 is the literal glyph in
Example 4.2); no doubled words in prose; every footnote marker has its note and every note its
marker; no unmatched asterisk, backtick, or bracket outside code; source prose carries no curly
quotes or dashes. Index: 20 random terms spot-checked against their locators, all 20 hold.
Production-editor items (stranded captions, part-empty pages before floats, short table heads,
appendix running heads) are not repeated here.

Form: `folio | file:line | quoted text | fault | fix`

## Front matter

1. PDF p.10-11 (printed "1", "2") | (press template, no manuscript line) | List of Figures folios "1" and "2" | front-matter pages switch to arabic folios before the Preface; List of plates is "ix" on the page before, and the Preface then starts at "3", so the LoF takes arabic 1-2 and pushes every chapter folio up by two | keep the LoF on roman folios (x, xi) and start arabic 1 at the Preface, or report to press if the template sets \pagenumbering there
2. PDF p.9 / PDF p.10 | (press template) | "List of plates" / "List of Figures" | heading case differs between the two lists on facing pages | one case for both ("List of Plates", matching the Contents' own usage in Chapter 10 prose)
3. PDF p.9 | appendices/z-colophon.md (plate) | "16.1 Common cuttlefish, Sepia officinalis . . . 372" | BLOCK, wrong number: the colophon plate is numbered as a Chapter 16 plate, but it sits in the Colophon after Appendix F | number it as unnumbered/colophon (no chapter number), or keep it out of the List of Plates
4. PDF p.6 vs folio 7 | config/front-matter.yaml:11 (generated heading) vs book/chapters/00-preface.md:159 | "acknowledgements" (generated page heading) vs "Acknowledgments" (Preface section) | the same word spelled two ways in the book, and the index entry reads "acknowledgments" | pick one spelling; the generated heading comes from press, so either change the Preface heading to match or report the press template spelling
5. folios 4-8 | book/chapters/00-preface.md | running head reads only "Publishing with Press"; the Preface pages carry no section head where every chapter's pages carry "N Title" | running head does not name its part | set the recto head to "Preface"

## Chapter 4

6. 73 | book/chapters/04-writing-the-manuscript.md:294 | "4.7.2 Dialogue openers / The second chapter of the three-chapter example opens with speech:" | orphan: heading plus one lead-in line alone at the foot of 73, the example it introduces starts on 74 | pull the heading and line to 74, or let 73 run one line short

## Chapter 5

7. 90 | book/chapters/05-figures-and-plates.md:276 | "The reader site serves the transparent PNG itself" | vocabulary: "transparent PNG" is on the never-list for alpha master | "serves the alpha master itself"

## Chapter 11

8. 196 (footnote 3) | book/chapters/11-the-art-department.md:312 | "the ramp is round(255*(225-" / "v)/180)" | code span broken at its own minus sign at a line end; it reads as a hyphenated break, and text extraction drops the minus (round(255*(225v)/180)) | keep `round(255*(225-v)/180)` on one line (tie or rewrap)

## Chapter 12

9. 222 (Table 12.9, kdp row) | book/chapters/12-the-print-pack.md:406 | "“KDP account with tax interview completed”; “Category selections (2 allowed; note 10 keyword slots)”; “Pricing per marketplace ...”" | semicolons separating items in running prose (the semicolons inside the quotes are KDP's; the three between the quotes are ours); the ingram row has the same form | separate the quoted items with commas, or set them one per line

## Chapter 14

10. 237 | book/chapters/14-continuous-integration.md:22 | ".github/work- / flows/book.yml" | path hyphenated at a line end, inserting a hyphen that is not in the filename | forbid hyphenation in paths (or rewrap)
11. 250 | book/chapters/14-continuous-integration.md:333 | "PRESS_RE- / LEASE=1" | inline code hyphenated at a line end; the variable gains a false hyphen | no hyphenation in code spans
12. 252 | book/chapters/14-continuous-integration.md:407 | "(clintecker/press(?:/[\w./- / ]*?)?@v)(\d+)(\.\d+\.\d+)?" | the regex breaks exactly after its literal "-", so the reader cannot tell a real character from a break hyphen | keep the pattern on one line (set it as a display line)

## Chapter 15

13. 255 | book/chapters/15-the-desk-and-the-machines.md:34 | "pip install ‘press[tui]’ ”" | a copyable command printed with curly single quotes (pandoc smartened the quoted message), and a stray space before the closing quote | set the message in constant width (`press desk needs the optional interface: pip install 'press[tui]'`) so the quotes stay straight; Appendix A (folio 301) already shows it correctly
14. 260 | book/chapters/15-the-desk-and-the-machines.md:146 | ".claude/work- / flows/" | path hyphenated at a line end | as item 10

## Chapter 16 and the code-span hyphenation generally

15. 275, 276, 277, 278, 281, 283, 286 | book/chapters/16-inside-the-press.md | "booklib.chap- / ter_files", "gen_author- / ities", "contract_mir- / ror", "os.re- / place", "scaf- / fold_neutrality", "re- / ceipt_chain", "load_man- / ifest", "SUP- / PORTED_CONTRACT_MAJORS" | identifiers in constant width hyphenated at line ends; each break adds a hyphen the identifier does not have | one fix for the whole book: no hyphenation in code spans (and in italic paths), break only at "/", "_", or ".", or rewrap. Same fault elsewhere: 30 "realesr-gan", "pdfim-ages"; 53 "FileNotFoundEr-ror"; 121 "identi-fier=urn:isbn:"; 156 "\widow-penalty", "\parfill-skip"; 190 "OPE-NAI_API_KEY"; 228 "reg-istrations.isbn.print"; 240 "test_ev-ery_action_is_pinned..."; 247 "press.re-ceipts"; 250 "python_ver-sion"; 253 "check_mi-gration"; 359 "edi-tion_id"; 363 "\parfill-skip"; italic paths 39, 175, 305 "config/meta-data.yaml", 126, 198, 286, 302 "as-sets/...", 192 "assets/wood-cuts/...", 194 "build/illustra-tions/", 306 "dist/al-ice.md", 358 "print.pro-file"

## Appendix A

16. 313 | book/appendices/a-command-reference.md:1055 | "press site / Synopsis. / press site" at the foot of 313, Description on 314 | orphan: entry head and synopsis alone at a page foot | pull to 314
17. 317 | book/appendices/a-command-reference.md:1261 | "press wordcount / Synopsis. / press wordcount" at the foot of 317 | orphan, as item 16 | pull to 318

## Appendix C

18. 340 | book/appendices/c-messages.md:227 | "not ready: Press prints:" last line of 340, the printed message on 341 | orphan: entry head separated from the message it introduces | pull to 341

## Appendix F (index)

19. 366-371 | config/index-terms.yaml (generated) | "GEMINI_API_KEY · 11, A, Z", "intake · ... E, Z", "colophon · ... E, Z", "Libertinus · ... D, Z", "logomark · ... E, Z", "Pillow · 2, 14, D, Z" | BLOCK, wrong cross-reference: locator "Z" names no appendix: the head note says "letters are appendices", the Contents has A to F, and the Colophon is unlettered | print the colophon locator as "Colophon" (as the Preface prints as "Preface"), or drop it
20. 366 | config/index-terms.yaml:35 | "appendices · 1, 3, 7, 16, A, E" | the vocabulary spelling is "appendixes"; the prose uses "appendixes" | term: appendixes (keep "appendices" as a match string)
21. 366-370 | config/index-terms.yaml | "chapter edition", "manuscript edition", "print edition" vs "Circulating edition", "Office edition", "Single-leaf edition", "Source edition", "Telegraphic edition" | edition names capitalized two ways in one index; the vocabulary capitalizes all eight | "Chapter edition", "Manuscript edition", "Print edition"
22. 366 | config/index-terms.yaml:3 | "acknowledgments · Preface, 3, 10, B, E" | the entry is spelled "acknowledgments" while the front-matter page it describes prints "acknowledgements" (item 4) | resolve with item 4 so the entry, the page heading, and the Preface section share one spelling
23. 366 | (index head) | "Numbers are chapters and letters are appendices; both stay put across editions" | this is press's own message, so the "appendices" spelling is quoted, but it is set as the book's own head note in roman, not as a quotation | either mark it as press's wording or render the house spelling "appendixes"

## Chapter 3 (minor)

24. 53 | book/chapters/03-the-shape-of-a-book.md (sort example) | "then b- / glossary.md" | filename broken at its own hyphen at a line end; reads as "bglossary.md" with a break hyphen | keep "b-glossary.md" on one line
