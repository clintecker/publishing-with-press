# Copyedit: Chapter 4, Writing the manuscript

File: `book/chapters/04-writing-the-manuscript.md`

## Status

REVISE. Four blocks (watchlist jargon, one-sighting list), 24 should, 11 may.
`press check` names no finding in this file (the run fails only on
paragraph length in 02). The blocks are on the contract's one-sighting
list, so the checker's silence does not clear them.

Counts by severity: blocks 4, should 24, may 11.

Most frequent rules broken: wrong term (9), hidden actor (7), then era
spelling and synonym rotation (5 each).

## The writer's 36 ste_check defences, judged

- Sentence length over 25 (lines 6, 38, 42, 73, 94, 206, 293, 299, 319,
  336, 407, 431): accepted. Each is the In-this-chapter list, an `art:`
  comment fused with its image line, a fusion across a code block, the
  abbreviation lists, or a sentence at or under the 30-word ceiling. No
  prose sentence exceeds 30 words.
- Semicolons (42, 95, 431): accepted. All three are in `art:` or index
  comments, and the one at 161 is inside a code span. No prose semicolon.
- Passive "is Markdown" (18), progressive "is trailing" (231): accepted,
  false positives.
- `-ing` forms (1, 90, 92, 155, 165, 206, 431): accepted. Headings,
  chapter titles, and the term "trailing whitespace".
- "therefore" (22, 279, 381): accepted; the contract allows it.
  "identical" (336, art comment) and "look at" (416, sidebar): accepted.
- Paragraph length over six (42, 319, 336, 381): **rejected for 381.**
  The defence says "the art comments only", but line 381 is a prose
  paragraph of seven sentences (item 5). The other three are art
  comments and are accepted.

The checker does not catch the problems below. They come from reading
every sentence.

## Findings

1. "The drop cap, if the book has one, skips the blockquote and lands on
   the first real paragraph after it." (187)
   Rule: watchlist jargon ("lands", one-sighting list). Severity: blocks.
   Fix: "The drop cap, if the book has one, skips the blockquote and goes
   on the first real paragraph after it."

2. "### Where the drop cap lands" (277)
   Rule: watchlist jargon ("lands", one-sighting list), in a heading.
   Severity: blocks.
   Fix: "### Where the drop cap goes"

3. "The examples come from the Alice example, the sample book that ships
   with press, which user `alice` keeps on the workstation `hatter`." (18)
   Rule: watchlist jargon ("ship", one-sighting list). Severity: blocks.
   Fix: "The examples come from the Alice example, the sample book that
   comes with press, which user `alice` keeps on the workstation
   `hatter`."

4. "Every profile that ships with press defaults to `none`, so a new book
   opens its chapters with a plain paragraph." (248)
   Rule: watchlist jargon ("ship", one-sighting list). Severity: blocks.
   Fix: "Every profile that comes with press defaults to `none`, so a new
   book opens its chapters with a plain paragraph."

5. "The tail is the most elaborate of the three. ... Example 4.9 shows the
   opening lines of the Mouse's Tale in a tail." (381, seven sentences)
   Rule: paragraph over six sentences (the writer's defence does not
   cover this paragraph). Severity: should.
   Fix: end the first paragraph at "The lines therefore swing out and
   back, and the type tapers as the tail goes down." Start a new
   paragraph at "In the PDF the lines run from `\normalsize` ..."

6. "Each pattern is a case-sensitive regular expression, matched as
   written, with a label that the checker prints as
   `<file>:<line>: <label>`." (157)
   Rule: hidden actor. Severity: should.
   Fix: "Each pattern is a case-sensitive regular expression that the
   checker matches as written, and the checker prints its label as
   `<file>:<line>: <label>`."

7. "The division carries the role of a separator and is hidden from
   screen readers, which have no use for eleven asterisks." (328)
   Rule: hidden actor. Severity: should.
   Fix: "The division carries the role of a separator, and press hides it
   from screen readers, which have no use for eleven asterisks."

8. "You can set them from the command line, which checks each value
   before it writes the file:" (260)
   Rule: hidden actor (the command line checks nothing; `press config
   set` does). Severity: should.
   Fix: "You can set them with `press config set`, which checks each value
   before it writes the file:"

9. "A paragraph of 190 words or more fails `press check`." (161)
   Rule: wrong term ("fail" is for a verifier result; the checker
   refuses). Severity: should.
   Fix: "The checker refuses a paragraph of 190 words or more."

10. "Every one of them fails. Greek letters, mathematical symbols, and
    emoji fail too." (111)
    Rule: wrong term (refuse, not fail, for the checker). Severity: should.
    Fix: "The checker refuses every one of them. It refuses Greek letters,
    mathematical symbols, and emoji too."

11. "If you reword that sentence, the claim no longer matches, and the
    build fails." (206)
    Rule: wrong term (press stops with a message: refuse). Severity:
    should.
    Fix: "If you reword that sentence, the claim no longer matches, and
    press refuses the build."

12. "Press matches the terms in *config/index-terms.yaml* against the text
    by pattern, so you never mark up the manuscript for the index." (206)
    Rule: wrong term ("the text" for the manuscript). Severity: should.
    Fix: "Press matches the terms in *config/index-terms.yaml* against the
    manuscript by pattern, so you never mark up the manuscript for the
    index."

13. "After a title, it ties the title to a following capitalized word,
    for Mr., Mrs., ..." (407)
    Rule: wrong term ("title" means a chapter title everywhere else in
    this chapter). Severity: should.
    Fix: "After an honorific, it ties the honorific to a following
    capitalized word, for Mr., Mrs., Ms., Dr., Prof., St., Mt., Sr., Jr.,
    Rev., Hon., Capt., Sgt., Gen., Col., Lt., and Fr."

14. "A chapter file is plain Markdown, and most of what you type in one is
    Markdown you already know." (18)
    Rule: wrong term (first use of *chapter file* must be italic and
    defined; the chapter defines it only at 49). Severity: should.
    Fix: "A *chapter file*, one Markdown file in *book/chapters/*, is plain
    Markdown, and most of what you type in one is Markdown you already
    know." (Then set "chapter file" roman at 49.)

15. "The set pieces use this extension." (31, Table 4.1; again at 200)
    Rule: wrong term (used twice before its italic definition at 332).
    Severity: should.
    Fix: "The set pieces, described later in this chapter, use this
    extension." (Keep the italic definition at 332.)

16. "An unnumbered chapter also gets no chapter opening, which the section
    "Chapter openings and drop caps" later in this chapter describes."
    (65)
    Rule: wrong term (used before its italic definition at 248).
    Severity: should.
    Fix: "An unnumbered chapter also gets no drop cap or other special
    first letter, as the section "Chapter openings and drop caps" later in
    this chapter describes."

17. "The checker refuses a heading such as `# 3. The pool of tears` with
    the message `manual number in heading`, because pandoc would print the
    number a second time beside its own." (71)
    Rule: wrong term (first use of *the checker*, never italicized or
    defined in this chapter). Severity: should.
    Fix: "The *checker*, `press check`, refuses a heading such as
    `# 3. The pool of tears` with the message `manual number in heading`,
    because pandoc would print the number a second time."

18. "The EPUB and the Web reader collect the notes as linked notes." (173)
    Rule: synonym rotation (the chapter also says "the reader site",
    "the reader", "the Web", and "the HTML edition"). Severity: should.
    Fix: "The EPUB, the HTML edition, and the reader site collect the notes
    as linked notes."

19. "The Web and EPUB editions set a styled display capital instead, at
    3.6em in the ornament colour." (297)
    Rule: synonym rotation ("Web edition" is not an edition name).
    Severity: should. (The spelling is item 22.)
    Fix: "The HTML, reader-site, and EPUB editions set a styled display
    capital instead, at 3.6em in the ornament color."

20. "...and the filter keeps each pair on one line in the PDF, the EPUB,
    and the reader alike." (409)
    Rule: synonym rotation ("the reader" for the reader site). Severity:
    should.
    Fix: "...and the filter keeps each pair on one line in the PDF, the
    EPUB, and the reader site alike."

21. "The PDF sets a plain horizontal rule, and the reader sets a small
    diamond between two hairlines that fade at their ends." (311, Table
    4.4)
    Rule: synonym rotation ("the reader"). Severity: should.
    Fix: "The PDF has a plain horizontal rule, and the reader site has a
    small diamond between two hairlines that fade at their ends."

22. "...at 3.6em in the ornament colour." (297)
    Rule: era spelling (American spelling). Severity: should.
    Fix: "...at 3.6em in the ornament color."

23. "Press sets three asterisks, centred and spaced a quad apart in the
    PDF, ..." (312, Table 4.4)
    Rule: era spelling (American spelling). Severity: should.
    Fix: "Press sets three asterisks, centered and spaced a quad apart in
    the PDF, and as a paragraph of class `asterism` on the reader site."

24. "A very long paragraph turns a page into one grey block and gives the
    eye nowhere to rest." (163)
    Rule: era spelling (American spelling). Severity: should.
    Fix: "A very long paragraph turns a page into one gray block and gives
    the eye nowhere to rest."

25. "...a framed box with a light paper-grey ground, a 0.4-point rule in
    grey, and small italic type." (185)
    Rule: era spelling (American spelling). Severity: should.
    Fix: "In the PDF, the house sets each one in a framed box with a light
    paper-gray ground, a 0.4-point rule in gray, and small italic type."

26. "...and the filter leaves ordinary sentences exactly as you typed
    them, every full stop included." (409)
    Rule: era spelling ("full stop" is British; American is "period").
    Severity: should.
    Fix: "...and the filter leaves ordinary sentences exactly as you typed
    them, every period included."

27. "**Warning:** Press silently ignores any other `.md` file in
    *book/chapters/* or *book/appendices/*. A file named `notes.md` or
    `chapter-four.md` never reaches the book, and no target tells you so."
    (52)
    Rule: admonition not imperative (brief: admonitions are imperative).
    Severity: should.
    Fix: "**Warning:** Start every chapter file's name with a digit. Press
    silently ignores any other `.md` file in *book/chapters/* or
    *book/appendices/*, so a file named `notes.md` or `chapter-four.md`
    never reaches the book, and no target tells you so."

28. "The same principle runs through this whole chapter. You type straight
    quotes and three periods, and pandoc sets curly quotes and an
    ellipsis. You type `* * *`, and the aesthetic chooses the ornament. You
    type a bare heading, and pandoc numbers it." (411)
    Rule: meta-narration (a recap of the chapter; it re-explains what the
    reader has just read). Severity: should.
    Fix: delete the recap and keep the one new fact: "The
    `figure-numbering.lua` filter numbers each figure once, by chapter,
    and turns every `@fig:` citation into "Figure 4.1" with a link, so
    press needs no pandoc-crossref."

29. "**Tip:** Set your editor to strip trailing whitespace when it saves a
    file. The checker refuses trailing whitespace even inside code blocks,
    where it reads nothing else." (168)
    Rule: admonition repeats the paragraph above (style guide 8.1). The
    fact also appears at 165 and 231, three times in all. Severity: may.
    Fix: "**Tip:** Set your editor to strip trailing whitespace when it
    saves a file."

30. "A verse block sets its lines to the house stanza measure, which the
    PDF calls `\PressVerse`." (366)
    Rule: hidden actor (a PDF calls nothing). Severity: may.
    Fix: "A verse block sets its lines to the house stanza measure. In the
    PDF, that measure is the macro `\PressVerse`."

31. "The PDF will break a longer line for you, but it breaks it at the
    measure, which is rarely where a reader expects the break." (243)
    Rule: hidden actor (`fvextra` breaks the line, as line 229 says).
    Severity: may.
    Fix: "The `fvextra` package breaks a longer line for you, but at the
    measure, which is rarely where a reader expects the break."

32. "Because pandoc curls quotes for you, you type the straight ones and
    let the machine choose the direction." (38)
    Rule: synonym rotation ("the machine" for pandoc). Severity: may.
    Fix: "Because pandoc curls quotes for you, you type the straight ones
    and let pandoc choose the direction."

33. "A book can name extra directories for the checker to read in
    `audit-dirs` in *config/house-rules.yaml*." (155)
    Rule: rhythm (two "in" phrases in a row make the sentence hard to
    read). Severity: may.
    Fix: "A book can list extra directories for the checker under
    `audit-dirs` in *config/house-rules.yaml*."

34. "A book adds its own refusals in the same file, under
    `banned-patterns`." (157)
    Rule: rhythm (one topic per paragraph; this paragraph is about
    banned patterns, under the heading "What the audit directories
    get"). Severity: may.
    Fix: give it its own subsection: "### The book's own patterns",
    followed by "A book adds its own refusals in
    *config/house-rules.yaml*, under `banned-patterns`."

35. "Press keeps a title you type verbatim as the heading." (61)
    Rule: rhythm (reads at first as "type verbatim"). Severity: may.
    Fix: "Press keeps the title you type, word for word, as the heading."

36. "You type the other six, and the rest of this chapter takes them in
    turn." (40)
    Rule: meta-narration (the opener allowance covers line 18, not this
    later paragraph). Severity: may.
    Fix: "You type the other six."

37. "A chapter epigraph is an ordinary blockquote placed right after the
    chapter heading." (187)
    Rule: hidden actor. Severity: may.
    Fix: "A chapter epigraph is an ordinary blockquote that you place right
    after the chapter heading."

38. "You build a dialect from a base format and a list of extensions,
    each one switched on with a plus sign." (22)
    Rule: hidden actor. Severity: may.
    Fix: "You build a dialect from a base format and a list of extensions,
    and you switch each extension on with a plus sign."

39. "A book that uses no set pieces renders byte for byte as it did before
    press added them." (401)
    Rule: rhythm. The comparison is to press's own history, not the
    reader's book, so it reads as release-note talk. Severity: may.
    Fix: "A book that uses no set pieces renders exactly as it would if
    press had no set pieces."

## Fact: see fact checker (not counted)

- "It follows Tenniel's 1866 Alice." (313): Tenniel drew the
  illustrations. Whether the asterisk arrangement was his, and whether
  1866 is the right edition, needs a source.
- "the float package's starred command `\caption*`" (416): `\caption*`
  usually comes from the caption package, not float.
- "| 'Tis the voice of the Lobster;" (372): with `+smart`, a leading
  straight apostrophe curls as an opening single quote, not an
  apostrophe. If the Alice example ships this line, its output is wrong.
- "The Lua coverage work for press 3.0.2 found the empty test." (429):
  confirm the release that carried the Lua coverage work.
- "You type "Dr. Dodgson"" (409): Dodgson held no doctorate. The example
  is hypothetical, but "Rev. Dodgson" would be both true and on the
  honorific list.

## Other checks

- Second person and present tense hold throughout. "We" appears only
  for the authors' judgment (202) and practice (240). No "I".
- Dry understatement appears at 84, 151, 328, and 416, about once every
  few pages, and never in a heading.
- Admonitions: three warnings and three tips, each under four sentences.
  Only 52 is not imperative (item 27).
- Footnotes (three) carry history and asides. The body does not need
  them.
- Spelling: filename, appendixes, Web page are correct. No "Unix",
  "e-mail", "Web site", "manpage", or "toward" occasion arises. The
  British spellings are items 22 to 26.
- Numbers: under ten spelled out in prose. Numerals appear only in
  versions, measurements, section numbers, and code.
- No semicolons, dashes, perfect tenses, hedge stacks, assistant
  vocabulary, or noun stacks over three in prose.
