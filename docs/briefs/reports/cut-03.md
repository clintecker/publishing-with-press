# Cut report: Chapter 3 and Appendix C

Files: book/chapters/03-the-shape-of-a-book.md (7980 -> 7669 words),
book/appendices/c-messages.md (4158 -> 4273 words).

## Chapter 3

1. Part 4 should, Table 3.1 help text. After Table 3.1, added a Tip:
   "`press <command> --help` prints the argument grammar only. The options in
   this table, and most options in this book, are accepted but not listed.
   Appendix A marks each one." (The brief's semicolon became a period, per
   the no-semicolon rule.)
2. Tic, fit the page (03:128). Before: "We wrapped that block's opening
   comment to fit the page and cut the ends of four long lines." After: "We
   cut the ends of four long lines."
3. Retold, drop-cap sentinel (03:222, 03:224-226). Warning box "Never take
   a sentinel from the first words of a chapter ..." cut. Clause appended to
   the template-advice sentence at 03:222: ', and take them from the middle
   of a chapter, never its first words (Chapter 6 says why).' ("take them" is
   the joining word: the bare clause does not parse after the quotation.)
4. Part 4 should, hyphenation (03:222). Added after the advice sentence:
   "Prefer short words: a word LuaLaTeX hyphenates at a line end breaks the
   match."
5. Tic, fit the page (03:230). Before: "We fold its first line to fit the
   page and cut the end of the second." After: "We cut the end of the second
   line."
6. Part 4 should, aesthetic validation (after Example 3.6). Added a
   paragraph: "For the aesthetic file, `ok` means only that it parsed as
   YAML. No key is checked." (Semicolon became a period.)
7. Maxim, cut and fold (03:416). Before: "..., zero-padded to at least two
   digits. The first chapter of a book is `01`." After: "..., zero-padded to
   at least two digits, so the first chapter is `01`."
8. Retold, font scan (03:537). Cut: "The first time LuaLaTeX runs on a new
   machine, it scans the system fonts ... Let it finish."
9. Retold, wordcount (03:541-549). The paragraph, the `press wordcount`
   session, and the HTML-comments paragraph cut to: "Run `press wordcount`
   to see the new files counted (Chapter 7)." Footnote `[^3-wordcount]`
   removed from Chapter 3.
10. Retold, Initialize containers (03:597). Cut: 'If a CI run dies at the
    step "Initialize containers", run it again. The image is public, and the
    step needs no secret.'
11. Retold, edition names (03:613-617). The two paragraphs "The first eight
    files in @fig:dist-after-all are the editions ..." and "The two zip files
    box the rest ..." cut to: "The first eight files are the editions, named
    as Table 1.2 names them, and the figure's annotations give each name."
    The sources-companion sentence ("A book with *config/authorities.yaml*
    also gets *alice-sources.md* ...") is kept and joins that paragraph. (The
    brief's semicolon became ", and".)
12. Retold, print pack (03:625). Cut: "In a book without print ordering,
    `press all` makes none of these." The first sentence, the print-targets
    sentence, and the registration-targets sentence stay.
13. Retold, no-stale (03:627-631). Cut the warning "Do not run a verifier
    over *dist/* ..." and the paragraph "A verifier run over an old *dist/*
    proves only that last week's files were good ...".
14. Tic, plainly (03:645). Before: "The source of `press add` states the
    purpose plainly." After: "The source of `press add` states the purpose."

Maxims marked leave or keep (03:174, 326, 404, 418, 484, 553, 566, 601, 605,
635, 637, 639): untouched. Protected passages: none in this file. Keeper
facts held here (file sorting and `press add`, 03:376-449; `site-url`,
Table 3.4 and 03:216): kept in full.

## Appendix C

15. Part 4 should, pointer table (from the 06 entry). Added after the
    introduction, before "## press check": a sentence ("This appendix holds
    the checker's and the verifiers' messages. Table C.1 points to the
    chapters that quote the messages of the generators, intake,
    `press config`, the retail flag, and the commerce gate.") and Table C.1:
    `gen_index` -> Chapter 10, `gen_authorities` -> Chapter 10,
    `front matter needs` -> Chapter 10, `press art accept` (intake) ->
    Chapter 11, `press config` -> Chapter 3, `registrations.retail` ->
    Chapter 13, the commerce gate -> Chapter 7 and Chapter 12. Each target
    chapter was confirmed by grep for the quoted message.
16. C:303 hyphenation remedy: kept, as the brief says. C:5 convention and
    C:128 "State the claim plainly": kept, as the brief says. C:47 remedy:
    kept.

## Declined or handed off

- `[^3-wordcount]` move to Chapter 7 at 07:509: removed from Chapter 3, but
  not added to Chapter 7, which is outside this group. The Chapter 7 editor
  must add it: "The counter matches words with the pattern `\b[\w'-]+\b`, so
  a hyphenated compound or a contraction counts as one word."

## press check

Passes: source checks (23 files), checker self-test, editorial checks, jargon
check.
