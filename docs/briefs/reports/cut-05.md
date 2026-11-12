# Cut report: 05-figures-and-plates.md

Words: 6832 before, 6532 after.

## Retold facts

1. `05:122` (hand-typed references, keeper Preface). Before: "Press has no cross-reference mechanism for chapters or sections either, and no `@` form reaches a chapter or a section. Write those references in words: ... Tables and examples in this book carry hand-typed numbers for the same reason." After: "Chapters, sections, tables, and examples have no `@` form, so write those references in words (Chapter 4)." (Brief's semicolon replaced by ", so" to obey the no-semicolon rule.)
2. `05:144` (toc-depth, keeper Chapter 7). Before: "A second scar sits in the same place. A shallow table of contents once emptied the List of Plates without a message. The house TeX header now prevents that, so a book with a one-level Contents still gets a full List of Plates.[^5-tocdepth]" After: "A second scar in the same lists, told in Chapter 7, once emptied the List of Plates." Footnote `[^5-tocdepth]`: cut.
3. `05:146` (hypcap, keeper Chapter 8). Before: the paragraph "The links in the lists had a fault of their own. ... The PDF verifier now checks the link destinations with pypdf." with `[^5-hypcap]`. After: "Each entry links to the top of its illustration, and the PDF verifier checks every destination (Chapter 8)." Joined to the end of the preceding paragraph (both are about the lists). Footnote `[^5-hypcap]`: cut.
4. `05:366` (Lulu preflight, keeper Chapter 12). Before: "The pass came from a real preflight. Lulu flagged two problems ... triggers **neither** warning"." After: "The pass came from a real preflight report, which Chapter 12 tells." Footnote `[^5-lulu]`: cut.
5. `05:370-372` Tip "In *tex/title-page-print.tex*, point the logomark at its copy in *build/print-assets/* ...": cut.

## Tics

6. `05:97` Before: "Pandoc lets the attributes run over several lines, and the example breaks them only to fit the width of this page." After: "Pandoc lets the attributes run over several lines."
7. `05:323` Before: "The scars list says it plainly:" After: "The scars list says:"
8. `05:69` (same family as the page asides, not named by the brief) Before: "The prompt receives it as one line, and the breaks here are only for the width of the page." After: "The prompt receives it as one line."

## Closing maxims

9. `05:118` "The fault is easy to see in a proof and easy to miss in a hurry.": cut, paragraph ends earlier.
10. `05:275` Before: "... so that edition publishes every directive verbatim. Write each directive as though a reader will see it." After: "... so that edition publishes every directive verbatim, for any reader to see."
Kept: `05:180`, `05:364`. Left: `05:44`, `05:216`, `05:218`, `05:353`.

## Shoulds

11. `05:368` Before: "If the book supplies its own *tex/title-page-print.tex*, the logomark ..." After: "If the book supplies its own *tex/title-page-print.tex* (a hand-written title page for the print interior only, which Chapter 10 describes), the logomark ..." (Brief's "; Chapter 10" rewritten without a semicolon.)

## Protected passages

12. `05:250` Before: "Example 5.4 carries no `art:` directive, and that is deliberate." After: "Example 5.4 carries no `art:` directive." (the one cut the brief allows). `05:172-174` untouched.

## press check

Passed (source, checker self-test, editorial, jargon).
