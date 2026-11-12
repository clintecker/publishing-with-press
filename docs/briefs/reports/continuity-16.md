# Continuity report: Chapter 16, *Inside the press*

Desk: continuity editor. Chapter read as it stands after fact, developmental,
copy, and typesetting review and its re-review (APPROVED): 382 lines,
6,177 words. Cross-checked against Chapters 1, 2, 3, 5, 7, 8, 11, 13, 14, 15,
Appendixes A, C, D, E, the Preface, `docs/vocabulary.md`, `docs/design.md`
section 5, the production-ledger rulings, and the bible.

Status: **PASS WITH FIXES.** No block. One should (a second name for one
thing across Chapters 15 and 16), three may. Bible entries added: 8 terms,
8 shared facts, 15 cross-reference rows, 1 numbering row (32), plus 5
term rows and 4 cross-reference rows confirmed or updated. No conflict with an earlier chapter's
facts; one earlier-chapter promise is not kept (finding 3).

## Findings

1. **Cast and cross-references: clean.**
   Cast: `alice`, `hatter`, `printshop` only; `acme-quarto` (Example 16.2) is
   the press's own reference manifest, a real file. Every "Chapter N, *Title*"
   matches the file's H1 and design.md section 5 (13, 7, 3, 14). Every "later"
   and "earlier" in the chapter points the right way. The three figures, six
   tables, and three examples run without gap or repeat; slugs are
   `16-01-module-map`, `16-02-end-to-end-data-flow`, `16-03-trust-tiers`, and
   the PNGs exist. Footnote labels carry the `16-` prefix. The In-this-chapter
   box matches the eleven A-heads in order.

2. **Quote:** the sidebar (l.131) and warning (l.150ff) say "the adapters
   gate" and "the gate"; Chapter 15, footnote 15-popen (l.400): "a boundary
   gate around `press.adapters`".
   **Rule:** a thing called by two names across chapters.
   **Severity:** should.
   **Fix:** Chapter 15's footnote says "the adapters gate", the name
   Chapter 16 uses (Chapter 16 also names the area "Boundary" in Table 16.1,
   which is the module area, not the gate). Chapter 16 itself is consistent
   once the sidebar names it; optionally change the Warning's "The gate
   refuses" (l.150) to "The adapters gate refuses", since five different
   gates appear in the book (integration, adapters, quality, conformance,
   commerce).

3. **Quote:** Chapter 5, footnote 5-tocdepth (l.378): "For the Chapter 16
   reader: the pandoc setting `toc-depth: 1` sets the LaTeX counter
   `tocdepth` to 0...".
   **Rule:** promise made by an earlier chapter about this one; Chapter 16
   never mentions `toc-depth` or the List of Plates.
   **Severity:** may (the footnote only addresses an audience, and Chapters 7
   and 9 explain the scar).
   **Fix:** reword Chapter 5's footnote ("For the reader of the press's own
   source: ...") or leave it; no change to Chapter 16.

4. **Quote:** Preface l.70: "Maps the package, follows the data from
   manuscript to edition, and covers invariants, the selftest, and what a
   contributed scar must earn."
   **Rule:** the Preface's Organization must match the chapter in substance.
   **Severity:** may. It does match in substance; it omits the adapters
   boundary, the quality gate, receipts, and extensions.
   **Fix:** optionally append "the adapters boundary, receipts, and
   extensions" at the whole-book sweep.

5. **Quote (l.80):** "A push to `main` deploys the Pages bundle to GitHub
   Pages."
   **Rule:** vocabulary, "the Pages bundle" is `dist/pages/`, "the Pages
   site" is what GitHub Pages serves; Chapter 14 (l.353) says the run
   "deploys the Pages site".
   **Severity:** may (the bundle is what is deployed, so the sentence is
   defensible).
   **Fix:** "deploys the Pages site", to match Chapter 14.

## Vocabulary and rulings checked

- **Edition names:** glossed once, in "The data flow" (l.74), all eight in
  one paragraph with their formats; later sentences about a file name the
  format (`alice.pdf`), none uses a banned form (the PDF edition, the text
  edition). Kept.
- **"The Alice book" and the three-chapter example:** l.62 uses "the Alice
  book" for the full-novel sample; the chapter never cites the press's own
  Alice example, so the other form never arises. Kept.
- **"Press" capitalised only at a sentence start:** one capital, l.272,
  inside a quotation that opens a sentence ("Press extends by declaration,
  not by code."). Kept.
- **Other vocabulary rows:** no use of project, folder, execute, output,
  pipeline (as a name), "the graph", or validator for a thing the vocabulary
  names. "Job" and "stage" are used only for CI jobs and the extension
  contract's own stages, not for press targets. "Contract" appears only as
  the extension contract and the release contract. Kept.
- **Terms defined (italic at first use):** *integration gate*, *invariant*,
  *quality gate*, *ratchet*, *producer*, *producer ledger*, *Trust receipts*,
  *scar*, *book model* and *release witnesses* (both restating their
  Chapter 3 gloss; the gists agree), *loads* (emphasis, not a term). All
  in the bible. *Trust receipt* and *release receipt* are Chapter 14's
  terms; Chapter 16's gloss agrees.

## Promises

Kept: Ch. 1 l.118 (extension contract), Ch. 3 l.126 (how the book model
works), Ch. 7 l.187 (the Lua filters' tests), App. A l.1044 and App. E
(catalog, extension declaration, invariant, quality gate, ratchet, sealed
capability). Not kept: Ch. 5 footnote (finding 3). Chapter 16 makes no
forward promise beyond the chapter.

## Shared facts checked and added

Agreed with other chapters: 29 selftest checks and the closing line (App. A
l.1026 to 1040); the eight-edition glosses; the epoch `1784160000` (Ch. 7,
App. A); `PRESS_TOOLCHAIN` over `CI` (Ch. 2, 8, App. D); the macOS 15
runner story (Ch. 2, 14, App. D); Python 3.10 to 3.14 and macOS 15 with 3.12
(Ch. 2, App. D); exit statuses 0, 1, 2, and the `press config` set (Ch. 3,
15, App. A, C); the integration-gate quotation (Ch. 14 l.287, word for word);
the receipt layers, tiers, and artifact names (Ch. 14); the `CONTRIBUTING.md`
producer quotation (Ch. 1, 8); `press doctor`'s last line (Ch. 2, App. A);
`--write-docs` regenerating four things (App. A). Added to the bible:
Selftest, Invariant ledger, Exit statuses, The press repository's workflows,
Quality gate tooling, Adapters gate history, Package size and epoch,
Extension contract. Open for the Appendix D pass: stylua v2.5.2 versus
Chapter 16's silence on the image's Lua tooling (no conflict).

## Bible changes

Terms added: adapters boundary, the catalog, integration gate, quality gate,
ratchet, producer / producer ledger, extension contract / extension
manifest, sealed capability. Terms confirmed: book model, invariant,
release witnesses, scar, edition manifest (stale line cited, corrected).
Cross-reference rows closed: Ch. 1 l.118, Ch. 3 l.126, Ch. 7 l.187; Ch. 5
footnote marked not kept. Chapter 16 outbound references, figure, and table
numbering recorded. A pass note was added to the bible's opening.
