# Cut report: 01-introduction.md

Words: 5412 before, 4899 after (`wc -w`). `press check`: pass.

## Cuts

1. `01:24` (tic) Before: "The press README describes the program in one plain sentence:" After: "The press README describes the program:"
2. `01:66` (plainly) Before: "The README is plain about ownership:" After: "The README says of ownership:"
3. `01:70` (tic, maxim cut, ends earlier) Before: "Each law fits in a line." After: cut.
4. `01:78` (plainly) Before: "Its *CLAUDE.md* says so plainly:" After: "Its *CLAUDE.md* says:"
5. `01:92` (tic) Before: "...the two halves of the work in one sentence:" After: "...the two halves of the work:"
6. `01:97` (tic, inside the protected sidebar; the brief names it) Before: "*CONTRIBUTING.md* records the cause in one clause:" After: "*CONTRIBUTING.md* records the cause:"
7. `01:118` (tic) Before: "*ARCHITECTURE.md* gives the reason in one line:" After: "*ARCHITECTURE.md* gives the reason:"
8. `01:142` (should) Before: "`press new` does not run `git init`, and the source archive holds only the files Git tracks, so the tour commits the scaffold before the first build.[^1-make]" After: "`press new` does not run `git init`, so the tour commits the scaffold first, which is the habit the Source edition rewards once the book lives in a repository.[^1-make]"
9. `01:160-166` (retold, wordcount) Before: "`press wordcount` counts the prose. It strips fenced and inline code. It counts HTML comments, ..." and its session. After: cut.
10. `01:172-174` font-scan warning: kept, as the brief says.
11. `01:246` (joining clause for the font-scan cut) Before: "When the tour goes wrong, the QUICKSTART lists five usual causes:" After: "When the tour goes wrong, the QUICKSTART lists five usual causes. One is the font scan in the warning earlier in this section, and the other four follow:" (keeps the QUICKSTART's count of five true).
12. `01:251` (retold) Before: "4. A font scan that looks like a hang. The warning earlier in this section covers it." After: cut; item 5 renumbered to 4.
13. `01:279` (retold, print pack) Before: "`press all` does not build the print pack, except through the commerce gate in a book that enables print ordering. Its own targets do: `press print`, `press verify-print`, and `press coverwrap`, which add *alice-interior.pdf* and *alice-coverwrap.pdf* to *dist/*." After: "Its own targets build it." The brief's "(Chapter 12)" is dropped because the next sentence, "Chapter 12, *The print pack*, covers it in full." (marked leave), already points there.
14. `01:285-287` (retold, drop-cap sentinel warning) Before: "Warning: If your book uses the drop-cap chapter opening, ..." After: cut.
15. `01:291` (retold, tags) Before: "*The release contract* is the workflow that proves a tag. ... which is why v3.0.0 is one." After: "Chapter 14 explains the release contract that proves each tag, and Chapter 9 explains why a design change needs a new major."
16. `01:62` (joining fix for cut 15) Before: "It was a design major, and the section "Versions and the pinned contract" later in this chapter explains why design needs one." After: "It was a design major, and Chapter 9 explains why design needs one." (that section no longer explains it).
17. `01:299-305` (retold, How to read this book) Before: four paragraphs, "The chapters follow the order in which you make a book." through "...the matching degree of trust." (includes the `01:305` hand-typed references sentence and the `01:299` closer). After: cut; the heading and the last line "Chapter 2, *Installing press*, puts the toolchain on `hatter`." stay.
18. `01:311` (retold, footnote) Before: "[^1-libertine]: TeX Live carries Libertinus for the PDF. Ubuntu has no `fonts-libertinus` package, and `--no-install-recommends` drops the Libertine keyboard face, so the toolchain image names `fonts-linuxlibertine` explicitly." After: "[^1-libertine]: TeX Live carries Libertinus for the PDF. Chapter 2 names the one Ubuntu package the fonts need." (period in place of the brief's semicolon, per the no-semicolon rule.)

## Not applied

- `01:60` "The first commit carries the date 2026-07-17." Marked leave, optional cut. Kept.
- `01:307` "Chapter 2, *Installing press*, puts the toolchain on `hatter`." The brief says it "may go too". Kept, because the heading must stay and the "In this chapter" box still lists the section, so the section needs a line.

## Protected and untouched

`01:80-86` (second law) and `01:94-102` (sidebar) unchanged apart from the brief-named tic at `01:97`. Keepers `01:60`, `01:110-120`, `01:252` unchanged. Sentinel "On a fresh scaffold it succeeds" intact. No "fit the page" asides were present.
