# Copyedit report: Preface

Desk: copyeditor. File: `book/chapters/00-preface.md`. Read against
`docs/prose-contract.md`, `docs/style-guide.md` sections 3, 4, 7, and 8,
and `docs/vocabulary.md`. Line numbers refer to the file as it stands.

## Checker leads

`python3 tools/ste_check.py book/chapters/00-preface.md` reports 19
findings (152 sentences, average 15.5 words, max 35). Most are noise:

- The `-ing` flags at 28, 34, 40, 46, 131 are chapter titles and the
  section heading "Using code examples"; 133 is a gerund subject; 169 is
  "Circulating", an edition name.
- The semicolons and the 31-word sentence at 169 sit inside the
  `<!-- index: -->` comment, not prose.
- The lengths at 9, 13, 49, 52, 67, 124, 139 come from the splitter
  merging a definition-list term or a blurb heading with its first
  sentence. The real long sentence the checker misses is the eight-edition
  list at line 125 (item 10).
- Line 5 is real: 30 words, at the ceiling, and two ideas (item 3).
- The passive at 83, "is untested", is real (item 6).

The banned-pattern battery in `config/house-rules.yaml` finds nothing.
Every watchlist hit (spine, scaffolds, proves, verified) is in
`jargon-allow`. No prose semicolon, em or en dash, perfect tense, stacked
hedge, assistant word, staged run-up, or meta-narration appears. There is
no "I". "We" carries the authors' judgment and history only. Second person
and present tense hold, with past tense for history. There are no
admonitions and no footnotes. Spellings are American and period: Unix,
Web, Web site, filename, appendixes, Acknowledgments; "toward" and
"e-mail" do not occur. Numbers under ten are spelled out in prose. The
blurb titles match the chapter and appendix headings.

## Findings

1. "The press built every edition of it from the Markdown in its own
   repository." (line 9)
   Rule: wrong term (first use of *edition* in the Preface is roman; the
   term is not defined until line 125). Severity: should. Fix: "The press
   built every *edition* of it, one for each published form, from the
   Markdown in this book's repository."

2. "from the Markdown in its own repository" (line 9)
   Rule: wrong term ("its" can mean the press or the book; the term is
   *book repository*). Severity: should. Fix: same sentence as item 1,
   "from the Markdown in this book's repository."

3. "A figure taller than the text block once sent LuaLaTeX into an endless
   run of empty pages, and each failure of that kind became a rule the press
   now enforces." (line 5)
   Rule: two ideas (one instance and the general rule, 30 words). Severity:
   should. Fix: "A figure taller than the text block once sent LuaLaTeX into an
   endless run of empty pages. That failure, and each one like it, became a
   rule that the press now enforces."

4. "and what to do when it stops your build." (line 19)
   Rule: wrong term (*refuse* is what the press does when it stops with a
   message). Severity: should. Fix: "It explains one program, the reasons
   behind its rules, and what to do when it refuses your build."

5. "Shows what each target runs, what pandoc is told, how the filter chain
   works, and what `press all` does in order." (line 44, Chapter 7 blurb)
   Rule: hidden actor. Severity: should. Fix: "Shows what each target runs,
   what the press tells pandoc, how the filter chain works, and what
   `press all` does in order."

6. "and inside the toolchain image, and what is untested." (line 83,
   Appendix D blurb)
   Rule: hidden actor. Severity: should. Fix: "Describes what the toolchain
   needs on Debian and Ubuntu, on macOS, and inside the toolchain image, and
   which platforms the press does not test." (fact: see fact checker for
   who does or does not test.)

7. "and explains why a design change needs a new major." (line 50,
   Chapter 9 blurb)
   Rule: wrong term (clipped "major" is release jargon the reader has not
   met). Severity: should. Fix: "Gives the house page in numbers, the six
   design profiles, and the reader site, and explains why a design change
   needs a new major version."

8. "The press repository carries a smaller example of its own, a
   three-chapter edition of the same novel, and every real capture in this
   book comes from it." (line 129)
   Rule: wrong term (*edition* is reserved for a published form; the
   vocabulary's first-mention name is "the press's own three-chapter Alice
   example"). Severity: should. Fix: "The press repository carries its own
   *three-chapter Alice example*, the opening chapters of the same novel,
   and every real capture in this book comes from it."

9. "We call it the Alice book." (line 129)
   Rule: wrong term (first use of a controlled term is italic). Severity:
   should. Fix: "We call it the *Alice book*."

10. "They are the Print edition (PDF), the Circulating edition (EPUB), the
    Single-leaf edition (one self-contained HTML file), the Chapter edition
    (the reader site and its zip), the Manuscript edition (the stitched
    Markdown), the Telegraphic edition (plain text), the Office edition
    (DOCX), and the Source edition (the source zip)." (line 125)
    Rule: sentence over 30 words (about 50). Severity: should. Fix: "Four
    of them are the Print edition (PDF), the Circulating edition (EPUB), the
    Single-leaf edition (one self-contained HTML file), and the Chapter
    edition (the reader site and its zip). The other four are the
    Manuscript edition (the stitched Markdown), the Telegraphic edition
    (plain text), the Office edition (DOCX), and the Source edition (the
    source zip)."

11. "The press itself has a license of its own, MIT, "code and bundled
    content alike", and its README is plain about the result: "A book you
    make with the press is yours entirely."" (line 137)
    Rule: two ideas (the license, then the README's reading of it).
    Severity: should. Fix: "The press itself has a license of its own,
    MIT, for "code and bundled content alike". Its README is plain about
    the result: "A book you make with the press is yours entirely.""

12. "Language models drafted the text from a fact base extracted from the
    press source and its documentation." (line 163)
    Rule: hidden actor (who extracted the fact base). Severity: should.
    Fix: "Language models drafted the text from a fact base, and the fact
    base came from the press source and its documentation." (If the
    extractor is known, name it; fact: see fact checker.)

13. "The book's own Web site, built from this manuscript by the press,
    carries every edition of the book:" (line 153)
    Rule: wrong term (the vocabulary names what GitHub Pages serves "the
    Pages site" and lists "the Web site" under never). Severity: should,
    though the editor may grant the contact block a period exception.
    Fix: "The book's *Pages site*, which the press built from this
    manuscript and GitHub Pages serves, carries every edition of the
    book:"

14. "covers invariants, the selftest, and what a contributed scar must
    earn." (line 71, Chapter 16 blurb)
    Rule: wrong term (the vocabulary reserves "selftest" for
    `press selftest` and wants the command named). Severity: should. Fix:
    "Maps the package, follows the data from manuscript to edition, and
    covers invariants, `press selftest`, and what a contributed scar must
    earn."

15. "A second reader is the developer asked to keep a group's book builds
    running." (line 17)
    Rule: hidden actor (reduced passive; the actor is obvious). Severity:
    may. Fix: "A second reader is the developer whom a group asks to keep its
    book builds running."

16. "Chapters 14 through 16 are for the person who runs the press." (line 23)
    Rule: synonym rotation (line 17 names the same reader "the developer
    asked to keep a group's book builds running"). Severity: may. Fix:
    "Chapters 14 through 16 are for the developer who keeps the builds
    running."

17. "Gives the messages the press prints when it stops, each with its cause
    and remedy. Look a message up here before you read the code." (line 80,
    Appendix C blurb)
    Rule: two ideas (style guide section 7: a blurb is one sentence;
    "stops" is also the wrong term for *refuse*). Severity: may. Fix:
    "Gives each message the press prints when it refuses a build, with its
    cause and remedy, so that you can look a message up before you read
    the code."

18. "Lists the subjects of the book with the chapters and appendixes where
    they appear. The press generates it from *config/index-terms.yaml* on
    every build." (line 89, Appendix F blurb)
    Rule: two ideas (one-sentence blurb form). Severity: may. Fix: "Lists
    the subjects of the book and the chapters and appendixes where they
    appear, as the press generates them from *config/index-terms.yaml* on
    every build."

19. "By the press's own second law such references are a convention, the
    weakest kind of guard, and you should trust them accordingly." (line
    127)
    Rule: rhythm (the introductory phrase wants its comma). Severity: may.
    Fix: "By the press's own second law, such references are a convention,
    the weakest kind of guard, and you should trust them accordingly."

20. "the phrase "at the time of this writing", because" (line 127); also
    ""code and bundled content alike", and" (line 137)
    Rule: era spelling (American punctuation sets the comma inside the
    closing quote; the book sets it outside). Severity: may; decide once
    for the whole book, since the other chapters follow the same logical
    style. Fix, if American style wins: "A version number in the text comes
    with the phrase "at the time of this writing," because the press will
    move on after the book goes to print."

21. "His book is long out of copyright, and until now few people asked it to
    pass epubcheck. We thank him for a manuscript that never once missed a
    deadline." (line 165)
    Rule: rhythm (the dry understatement appears at lines 7, 127, 163, 165
    twice, and 167; the Acknowledgments alone carry four in four paragraphs,
    and the style guide permits one joke there). Severity: may. Fix: "His
    book is long out of copyright. We thank him for a manuscript that never
    once missed a deadline."

22. "Small-press operators who publish several books under one imprint will
    find the same machinery serves every title they keep." (line 13)
    Rule: rhythm (Pass 2 keeps "that"). Severity: may. Fix: "Small-press
    operators who publish several books under one imprint will find that
    the same machinery serves every title they keep."

23. "and then inspects each finished file as an object." (line 3)
    Rule: wrong term ("as an object" is vague; the book's word for the act
    is *verify*, and Chapter 1 says "opens each file it built"). Severity:
    may. Fix: "This book is about press, a program that builds all of them
    from one directory of Markdown and then opens each finished file to
    verify it."

24. "The first commit to the press carries the date 2026-07-17." (line 7;
    also "2026-11-10" and "2026-11-11")
    Rule: era spelling (a period book writes dates in words; ISO form reads
    as log output). Severity: may; Chapter 1 line 60 uses the ISO form too,
    so decide book-wide. Fix: "The first commit to the press carries the
    date July 17, 2026."

25. "*https://clintecker.github.io/press/*" (line 151) and
    "*https://clintecker.github.io/publishing-with-press*" (line 155)
    Rule: fact: see fact checker (one URL ends in a slash and the other does
    not; confirm the canonical form of each). Severity: may.

26. "A short passage set apart in a box and headed **Tip:** gives a
    suggestion or a shortcut." (line 113; also the Warning entry, line 116)
    Rule: fact: see fact checker (style guide sections 3.4 and 8.1 call for
    a margin icon and name a bold "Note:" label as an illusion breaker;
    confirm what the press actually renders before the entry describes it).
    Severity: may.

## Counts

- blocks: 0
- should: 14
- may: 12

Most frequent rules: wrong term (9), hidden actor (4), two ideas (4).
