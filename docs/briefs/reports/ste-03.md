# STE80 editor report: Chapter 3, The shape of a book repository

File: `book/chapters/03-the-shape-of-a-book.md`

Ratchet count: 12 before (baseline 12), 2 after. `press check` passes.
`python3 tools/ste-ratchet.py` (gate) exits 0.

Sentinels: none of the three stands in this file (0 before, 0 after).
Index terms: every match string in `config/index-terms.yaml` occurs in
this file as often as before or more ("press check" 6 to 6; one interim
wording raised it and was reworded).

## Edits

Line numbers are in the edited file.

1. L17, S1/S2 (26 words). Old: "You will spend most of your working hours inside this one directory, so it pays to know what each file does and which program reads it." New: "You will spend most of your working hours inside this one directory. It pays to know what each file does and which program reads it."
2. L32 (Table 3.1 cell), S1/S3. Old: "Without it, press reads `git config user.name`, and if Git has no name either, it writes "The Author"." New: "Without it, press reads `git config user.name`. If Git has no name either, press writes "The Author"."
3. L40 (Tip), S6. Old: "The options in this table, and most options in this book, are accepted but not listed." New: "The press accepts the options in this table, and most options in this book, but does not list them."
4. L43, S1 (three ideas). Old: "The Alice book belongs to the GitHub account `wonderland-press`, and its author is Lewis Carroll, so `alice` gives both on the command line." New: "The Alice book belongs to the GitHub account `wonderland-press`, and its author is Lewis Carroll. The user `alice` therefore gives both on the command line."
5. L68, S8 (-ing rider). Old: "A slug must match the pattern `[a-z0-9][a-z0-9-]*`: lowercase letters, digits, and hyphens, starting with a letter or a digit." New: "A slug must match the pattern `[a-z0-9][a-z0-9-]*`. It holds lowercase letters, digits, and hyphens, and it starts with a letter or a digit."
6. L88 (Table 3.2 cell), S1/S2 (four-clause sentence). Old: "*aesthetic-brief.js* drafts ... brief, *art-direction.js* writes *art/commissions.md*, *authorities-research.js* builds ..., and *editorial-passes.js* runs the iterative editorial machine." New: "*aesthetic-brief.js* drafts ... brief, and *art-direction.js* writes *art/commissions.md*. *authorities-research.js* builds ..., and *editorial-passes.js* runs the iterative editorial machine."
7. L114, S8. Old: "Every press target starts by finding the *book root*." New: "Every press target first finds the *book root*."
8. L114, S1/S3. Old: "That directory must contain *config/metadata.yaml*, and if it does not, press refuses with the message ..." New: "That directory must contain *config/metadata.yaml*. If it does not, press refuses with the message ..."
9. L122, S1. Old: "A book grows other files as its author asks more of the press, and each of them is optional." New: "A book grows other files as its author asks more of the press. Each of them is optional."
10. L128, S2 (27 words). Old: "It holds the book's identity, the facts the press needs to name and publish the artifacts, and the knobs that tell the verifiers how hard to look." New: "It holds the book's identity and the facts the press needs to name and publish the artifacts. It also holds the knobs that tell the verifiers how hard to look."
11. L130, S1. Old: "Every build checks the file against the model, and Chapter 16, *Inside the press*, shows how the model works." New: "Every build checks the file against the model. Chapter 16, *Inside the press*, shows how the model works."
12. L132, S13 (paragraph would reach 7 sentences). Split the paragraph at its turn from the book model to pandoc: the new paragraph starts "Pandoc reads the raw file as well."
13. L132, S2 (25 words). Old: "Every pandoc defaults file names the metadata file as its `metadata-file`, so a standard pandoc key that you add here passes through to every edition." New: "Every pandoc defaults file names the metadata file as its `metadata-file`. As a result, a standard pandoc key that you add here passes through to every edition."
14. L134, S1/S2 (29 words). Old: "After `site-url`, the real file goes on with the verification knobs, which the section "Verification knobs" later in this chapter shows, and with commented lines for print and registrations." New: "After `site-url`, the real file goes on with the verification knobs and with commented lines for print and registrations. The section "Verification knobs" later in this chapter shows the knobs."
15. L193 (Table 3.3 cell), S8. Old: "(a four-digit number beginning 1 or 2)" New: "(a four-digit number that begins with 1 or 2)"
16. L200 (Table 3.3 cell), S1. Old: "It is a rights statement, which press passes through to pandoc, except in the EPUB, where the press sets its own `--metadata rights=` value." New: "It is a rights statement, which press passes through to pandoc. In the EPUB, the press sets its own `--metadata rights=` value instead."
17. L204, S10 (phrasal verb; the counter joins this sentence to the next across the footnote marker, 46 words). Old: "The press therefore pulls the year out of your free-text date and writes it into the EPUB metadata itself." New: "The press therefore extracts the year from your free-text date and writes it into the EPUB metadata itself." ("extracts" is the footnote's own word.)
18. L204, S1/S2 (28 words). Old: "A date such as "First edition, 2026" gives the EPUB the year 2026 and gives the title page its roman numerals, so you never type the year twice." New: "A date such as "First edition, 2026" gives the EPUB the year 2026. The same date gives the title page its roman numerals, so you never type the year twice."
19. L228, S2 (48 words with the quotation). Old: "The template's own advice for choosing them is good: "...", and take them from the middle of a chapter, never its first words (Chapter 6 says why)." New: "The template's own advice for choosing them is good: "...". Take them from the middle of a chapter, never its first words (Chapter 6 says why)." Quotation untouched.
20. L362, S8 (-ing rider). Old: "It prints one line for every config file the press knows, including the optional ones the book does not have yet." New: "It prints one line for every config file the press knows, among them the optional files the book does not have yet." (A two-sentence version pushed the paragraph to 7 sentences.)
21. L376, S6. Old: "No key is checked." New: "The press does not check any key."
22. L384, S2 (29 words). Old: "It merges the chapters first, then the appendixes in the order of their letters, and the generated subject index takes its place among the appendixes by its own letter." New: "It merges the chapters first, then the appendixes in the order of their letters. The generated subject index takes its place among the appendixes by its own letter."
23. L396, S8. Old: "The `press add appendix` target takes the next free letter, counting down from `z`." New: "The `press add appendix` target takes the next free letter and counts down from `z`."
24. L396, S1/S8. Old: "The generated subject index takes the first free letter counting up from `a`, and the press never assigns it `z`." New: "The generated subject index counts up from `a` and takes the first free letter. The press never assigns it `z`."
25. L422, S8 (-ing chain). Old: "Example 3.7 shows `alice` adding the first chapter and two pieces of back matter, then listing the two directories and the new chapter file." New: "In Example 3.7, `alice` adds the first chapter and two pieces of back matter. Then `alice` lists the two directories and the new chapter file."
26. L457, S1. Old: "The real file lists all 16 targets on both of its long lines, and we cut the end of the comment." New: "The real file lists all 16 targets on both of its long lines. We cut the end of the comment."
27. L473, S1/S2 (25 words). Old: "The press has more targets than the Makefile names, such as `print` and `coverwrap` for the print pack, and for those you run `press` itself." New: "The press has more targets than the Makefile names, such as `print` and `coverwrap` for the print pack. For those, you run `press` itself."
28. L539, S1/S2 (28 words). Old: "On a machine without epubcheck, the run also prints a warning that it validated the EPUB structurally only, and the toolchain image runs the full check in CI." New: "On a machine without epubcheck, the run also prints a warning that it validated the EPUB structurally only. The toolchain image runs the full check in CI."
29. L560 to L562, S6 (passive "is archived"), S1/S2 (29 words). Old: "A book outside any repository is archived whole, less *build/*, *dist/*, and caches, but a book that sits untracked inside another repository archives nothing until Git tracks its files." New: "For a book outside any repository, the press archives the whole book, less *build/*, *dist/*, and caches. For a book that sits untracked inside another repository, the press archives nothing until Git tracks its files."
30. L560 to L562, S13 (7 sentences). Split "What Git gives the press" into two paragraphs by topic. The first keeps what the zip holds: the opening three sentences, then the `.gitignore` sentence and "A Source edition therefore cannot contain old artifacts." (moved up two sentences, so "therefore" follows the facts it rests on). The second holds the Source edition before `git init`: "Before `git init`, ..." and the two sentences of edit 29.
31. L591, S1. Old: "The file grants the job four permissions, and it hands all the work to one line: the reusable workflow at `v3`." New: "The file grants the job four permissions. It hands all the work to one line: the reusable workflow at `v3`."
32. L611, S1. Old: "The first eight files are the editions, named as Table 1.2 names them, and the figure's annotations give each name." New: "The first eight files are the editions, named as Table 1.2 names them. The figure's annotations give each name."
33. L625, S10 (phrasal verb). Old: "To look at the PDF page by page, run `press render`, ..." New: "To examine the PDF page by page, run `press render`, ..."
34. L625, S1. Old: "The generated subject index lives under *build/generated/*, with its letter in its name, and the flattened, print-safe copies of your images live under *build/print-assets/*." New: "The generated subject index lives under *build/generated/*, with its letter in its name. The flattened, print-safe copies of your images live under *build/print-assets/*."

## Leads declined

- L70 (Tip), passive "were permanent": a false positive. "as if it were permanent" is a subjunctive with a linking verb, not a passive.
- L489 (sidebar "Why CI does not install press from Git"), 10 sentences in one paragraph: the sidebar is Light mode, and it has no sentence over 30 words, no three-idea sentence, and no semicolon. Its four internal paragraphs hold 2, 2, 4, and 2 sentences. The counter merges them because `prose_only` strips `^>\s?`, and `\s?` takes the newline after each bare `>` line. The whole sidebar is about 150 words, under the 190-word limit for a sidebar counted as one paragraph.

## Sentences over 25 words kept

- L226 "If the PDF, the EPUB, or the Telegraphic edition (the plain text) loses a chapter on the way out, a sentinel from that chapter goes missing." stays: the condition comes first, and the parenthesis counts as one word (about 23).
- L591 "With this file, CI builds the book on a push to any branch, on a tag that starts with `v`, on a pull request, or on demand." (27 by a plain count) stays: the four triggers form one list, and a split would scatter it.
- L387 (Warning) "The press skips any other Markdown file ... so a chapter saved as *chapter-two.md* never reaches the book." (25) stays: two linked facts joined by cause.

## Passives kept

- L102 "the fixtures under *tests/known-bad/* must stay rejected": "rejected" is a predicate adjective after "stay", and the house term for a fixture is "reject".
- Fewer than three passives remain in the body prose. None needed a reason beyond this one.
