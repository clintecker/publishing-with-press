# Fact check 00: Preface

Status: DONE_WITH_CONCERNS. Unsupported 2, Contradicted 2, Drifted 7,
Missing 2. Four further claims hold only once production finishes; they
are listed separately under "Conditional" and are not counted as blockers
today.

Sources checked: *docs/briefs/facts/facts-01.md* sections 1.1 to 1.4 and
the shared context (sections 19 and 20, S5); *docs/design.md* section 5;
the A-heads of every file in *book/chapters/* and *book/appendices/*;
*docs/markup.md*, *docs/vocabulary.md*, *docs/prose-contract.md*,
*docs/style-guide.md* (the "Using Code Examples" skeleton);
*config/metadata.yaml* and *config/front-matter.yaml*.

Note on the report path: the desk brief names
*docs/briefs/reports/facts-01.md*, which already holds the Chapter 1 fact
check. This report is written to *facts-00.md*, as the assignment says, and
*facts-01.md* is untouched.

The Preface has no code blocks, so there is no captured output to compare.

## 1. Unsupported (blocks)

1. **"The press keeps its own documentation on the Web. It covers the
   current release, so it is the place to look when a command behaves
   differently from the way this book describes it."** (How to contact us)
   Searched facts-01 1.3 ("Docs site: <https://clintecker.github.io/press/>")
   and facts-14 12.7 (`docs-site.yml` "Builds the example PDFs ... then
   deploys <https://clintecker.github.io/press/>"). Nothing says which
   version the site documents; the site is built by a workflow in the press
   repository, not from a release. Fix: cut "It covers the current release"
   and soften to what the file says, for example "The press keeps its own
   documentation on the Web, built from the press repository by its own
   CI:".

2. **"Selling or redistributing a collection of the examples does."**
   (Using code examples) The binding text is the `rights-notice` in
   *config/front-matter.yaml*: "The text of this book may be quoted and its
   examples reused in your own books and build scripts without permission.
   Reproducing a substantial part of it requires the publisher's consent."
   The notice names no restriction on selling or redistributing a
   collection; the sentence comes from the style guide's O'Reilly skeleton,
   not from the book's rights. Fix: cut it, or have the author add the
   restriction to `rights-notice` so the copyright page and the Preface
   agree.

## 2. Contradicted (blocks)

1. **Chapter 12 blurb: "Builds the print interior and the cover wrap,
   works through providers and spine math, and ends with the publish
   checklists."** The chapter's last A-head is "Ordering a copy" (Lulu
   printing and reader print ordering), after "Publish checklists"
   (*book/chapters/12-the-print-pack.md* lines 386 and 413; the "In this
   chapter" box lists both). Corrected wording: "... works through
   providers and spine math, and ends with the publish checklists and
   ordering a copy." (or "... covers the publish checklists, and ends with
   ordering a copy.")

2. **"In general, you may use the commands and configuration in this book
   in your own book repositories and documentation. You do not need to
   contact us for permission unless you reproduce a significant portion of
   the book."** The `rights-notice` grants something different: "The text
   of this book may be quoted and its examples reused in your own books and
   build scripts without permission. Reproducing a substantial part of it
   requires the publisher's consent." The Preface extends the grant to
   "documentation", which the notice does not name, and narrows it to
   "commands and configuration", where the notice says "examples" and also
   permits quoting the text. Corrected wording, from the notice: "In
   general, you may quote the text of this book and reuse its examples in
   your own books and build scripts without permission. Reproducing a
   substantial part of the book requires the publisher's consent." (The
   writer's concern 5 raised the same question; the notice answers it.)

## 3. Drifted (should)

1. **Chapter 1 blurb: "then builds a book in ten minutes".** The fact file
   documents no build timing (20.C: "Build timings. Only the first-run font
   scan is described."), and the first LuaLaTeX run spends "several
   minutes on a font scan" (19.10). "A ten-minute tour" is the chapter's
   A-head, a title, not a measured time. Fix: "then takes a ten-minute tour
   from `press new` to the finished editions, and lists them."

2. **Chapter 13 blurb: "and shows where each number appears in the
   book."** The A-head is "Where each number goes", and its routes run to
   the copyright page, the EPUB metadata, the wrap barcode, the ONIX file,
   and the PCN listing (ch. 13, figure 13.1). Three of the five are not "in
   the book". Fix: "and shows where each number goes."

3. **Conventions, "Figure 2.1": "Figures, tables, and examples carry numbers
   by chapter."** The appendixes number by letter (Table B.1 in Appendix
   B, Table D.1 in Appendix D). Fix: "carry numbers by chapter, or by letter
   in an appendix (Table B.1)."

4. **"We wrote the examples against press 3.0.2."** (Using code examples)
   Two paragraphs earlier the Preface promises that "A version number in
   the text comes with the phrase 'at the time of this writing'". Either
   add the phrase ("against press 3.0.2, the current release at the time
   of this writing") or narrow the convention to versions stated as
   current. (The paragraph 3 sentence on 3.0.2 already carries it; the
   historical 2.0.0 and 3.0.0 dates do not need it.)

5. **"significant portion" and "contact us for permission"** (Using code
   examples). The notice says "a substantial part" and "the publisher's
   consent". Use the notice's words so the two pages read as one rule;
   folded into the fix for Contradicted 2.

6. **"We checked the information in this book against the press's source
   and its documentation"** (How to contact us) versus the Acknowledgments,
   "A squad of editorial agents then checked every chapter against that
   fact base", and the colophon, which says the same. The checks ran
   against the fact base extracted from the source and documentation, not
   against the source. Fix: "We checked the information in this book
   against a fact base drawn from the press's source and its
   documentation". Paragraph 3's "Every statement about the press comes
   from its source and its documentation at that release" is acceptable,
   since the fact base was extracted from them.

7. **Appendix F blurb: "Lists the subjects of the book with the chapters
   and appendixes where they appear."** Chapter 10 ("What the index
   prints"): "A hit in the preface reads 'Preface'". Minor: "with the
   chapters, appendixes, and Preface where they appear", or "with the
   places where they appear".

## 4. Missing (may)

1. The `rights-notice` permits quoting the text without permission. The
   Preface never says so; a reader who wants to quote a paragraph in a
   review or a blog post would need it. Covered by the fix for
   Contradicted 2.

2. Structure, for the editor rather than facts: *docs/design.md* section 5
   asks for "two untitled opening paragraphs"; the Preface has four. The
   writer's report states this choice. Not a fact error.

## 5. Conditional (true only at the end of production; re-check before ship)

1. **"The press built every edition of it from the Markdown in its own
   repository. It verified each edition with the checks the chapters
   describe."** Today *config/metadata.yaml* has `verify-sentinels: []` and
   `verify-min-pages: 1`, which the metadata template comment calls "DRAFT
   settings; a release build (CI on a tag) refuses them". With no
   sentinels, the sentinel check the chapters describe proves nothing.
   *docs/design.md* plans three sentinels and `verify-min-pages: 240`.
   The sentence holds only after production step 6 and a passing release
   build. (Writer's concern 3.)

2. **Appendix F: "The press generates it from *config/index-terms.yaml* on
   every build."** *config/index-terms.yaml* does not exist yet, and
   Chapter 10 says "With no such file, the book has no index." Until step
   6 assembles the file, there is no Appendix F. The letter F is right
   once it exists: appendixes a to e are taken, and the index takes the
   first free letter from `a` to `y` (ch. 10; 20.A.7), so it sorts before
   *z-colophon.md*.

3. **"The book's own Web site ... carries every edition of the book:
   *https://clintecker.github.io/publishing-with-press*"**. The URL matches
   `site-url` exactly, but the claim holds only once the Pages site is
   deployed. (Writer's concern 2.)

4. **"the press refused the book each time it broke a rule"**
   (Acknowledgments). A production claim; true by construction of the
   build, but confirm at the final build.

## Verified

- Docstring quotation "the next book starts with the scars already paid
  for" is verbatim (1.1). *Mostly Done.* and *Make Ready* (1.2; registered
  ISBNs among Make Ready's facilities), neither in the press repository
  (1.2, 1.4 "There is no book in here").
- Scar defined as a production failure turned into a guard (vocabulary;
  law 4 "Every production failure earns a mechanical guard"). The
  empty-pages failure (19.1).
- Dates: first commit 2026-07-17; 2.0.0 2026-07-21 (four days later);
  3.0.0 2026-11-10, a design major; 3.0.2 2026-11-11, the last tag (1.2).
  "Where the documentation and the code disagree, we follow the code"
  agrees with 20.A's heading.
- No cross-references to chapters or sections (20.C); "the weakest kind of
  guard" reads law 2 fairly.
- Maintainer Clint Ecker (1.3); MIT, "code and bundled content alike" and
  "A book you make with the press is yours entirely" both from the README
  (1.3); repository `clintecker/press` (1.3); docs site URL (1.3).
- Issue tracker URL equals the `contact` value in
  *config/front-matter.yaml* and `repository` plus */issues*. No postal
  address or phone, as design.md requires.
- Attribution example: title, author, and the `copyright` value
  ("Copyright 2026 Clint Ecker.", with "All rights reserved." dropped,
  which is acceptable).
- Every chapter and appendix title in "Organization of this book" matches
  the file's `#` line and design.md section 5; Appendix F's title "Index of
  subjects" matches design.md and ch. 10. Blurbs for Chapters 2 to 11, 14
  to 16, and Appendixes A to E match their A-heads and opening paragraphs
  (Chapter 15 has four workflows, Table 15.4; Chapter 9 has "Six
  profiles"; Appendix A covers exit codes and environment variables;
  Appendix B gives type, default, and chapter; Appendix C gives cause and
  remedy; Appendix E cites chapters). The colophon describes the
  cuttlefish and how the book was made.
- Conventions agree with markup.md: italic, constant width, angle brackets
  in syntax lines, `[ ]`, `|`, `...`, the `...` elision line, `$` and `#`
  prompts; constant width italic is used (ch. 11, Appendix B); root
  commands run through `sudo` at `$` (ch. 2, lines 70 and 201); Tip,
  Warning (warning before the step, prose-contract.md), Sidebar; tables and
  examples numbered by hand, figures by the press, plates unnumbered.
- The eight edition names match vocabulary.md. The cast (`alice`,
  `hatter`, `printshop`, `wonderland-press`, the Alice book, the
  three-chapter example as the source of every real capture) matches
  design.md's fixed cast and vocabulary.md.

## Single worst finding

Contradicted 2: "Using code examples" grants different permissions from
the book's own `rights-notice` (it adds "documentation", drops quoting, and
with Unsupported 2 adds a restriction the notice does not state). The
Preface and the copyright page would give a reader two different licenses.
