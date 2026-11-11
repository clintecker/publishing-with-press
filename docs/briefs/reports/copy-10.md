# Copyedit: Chapter 10, Front matter, the index, and the table of authorities

File: `book/chapters/10-front-matter-index-authorities.md`

## Status

REVISE. Five blocks, 27 should, 10 may, and two sentences referred to
the fact checker. `press check` names no finding in this file. Its
findings are all in other chapters. Two of the blocks are watchlist
terms that the house `jargon-allow` list lets through ("fallback",
"proves"), used here in their generic sense and not as press's own
name for a thing. This follows the Chapter 4 and Chapter 8 precedent.
One block is a one-line closer. Two are -ing riders, which the
contract puts on the one-sighting list although the house regex
catches only the named verbs.

Counts by severity: blocks 5, should 27, may 10.

Most frequent rules broken: wrong term (9), era spelling (7), then two
ideas (6).

Line numbers are `grep -n` line numbers in the file as it stands.

## The ste_check findings, judged

- Passive at 20 ("Facts are stated once"): accepted. It is the press's
  first law, quoted verbatim.
- Semicolons at 241, 312, and 395: accepted. All three sit inside
  verbatim quotations of the press. The semicolon at 429 is in the
  index comment. No prose semicolon.
- Sentence and paragraph length at 6 (the In-this-chapter list), 138
  and 278 (figure line and art directive), and 429 (index comment):
  accepted. None is prose.
- Sentence length at 97 (30 words), 157 (28), and 198 (29): accepted,
  at or under the 30-word ceiling. At 178 the counter runs the footnote
  marker and the table caption together. No prose sentence there
  exceeds 30 words.
- Paragraph length at 317 (the sidebar, nine sentences): upheld,
  item 21.
- "therefore" at 37, 223, 281, 283, and 411: accepted under the 80
  percent rule.
- `-ing` forms at 210 and 357 (headings), and 417 (the title of
  Chapter 8): accepted. The form at 272 is upheld, item 4.
- "appendices" at 312: accepted. It is inside a verbatim quotation of
  the press's code.
- "proves" at 417: accepted. The vocabulary itself uses "proves" for
  what the release contract does to a tag, so a verifier that proves
  an artifact is the house sense. The use at 349 is not (item 2).
- "scaffold" at 37 and 126: accepted. It is press's own name and is on
  `jargon-allow`.

The checker does not catch most of the items below. They come from
reading every sentence.

## Findings

1. "The index records what the prose says, and it ignores what the
   code and the captions show." (281)
   Rule: one-line closer (it restates the two sentences before it as a
   balanced maxim). Severity: blocks.
   Fix: delete the sentence. The paragraph ends on "A term that appears
   only inside an example, a constant-width span, or a figure line
   therefore has no hits."

2. "That exactness is the purpose of the ledger: a claim that matches
   proves the cited sentence still says what the source supports."
   (349)
   Rule: watchlist jargon ("proves", one-sighting list; generic sense,
   not press's term). Severity: blocks.
   Fix: "That exactness is the purpose of the ledger: a claim that
   matches shows that the cited sentence still says what the source
   supports."

3. "An empty file still gives you the generated title page and
   copyright page, and deleting it gives you the plainer fallback."
   (244, Tip)
   Rule: watchlist jargon ("fallback", one-sighting list). Severity:
   blocks.
   Fix: "An empty file still gives you the generated title page and
   copyright page. If you delete it, you get the plainer title that the
   house TeX header sets."

4. "The other two name the entry by its position in the list, counting
   from one." (272)
   Rule: -ing rider. Severity: blocks.
   Fix: "The other two name the entry by its position in the list, and
   the count starts at one."

5. "The press then reads no key from *config/front-matter.yaml*, and
   the file can stay in the repository doing nothing." (227)
   Rule: -ing rider ("doing nothing"); also wrong term ("repository";
   the vocabulary's word is *book repository*). Severity: blocks.
   Fix: "The press then reads no key from *config/front-matter.yaml*,
   so the file can stay in the book repository and has no effect."

6. "The first is the *front matter*, the run of pages from the cover
   plate through the acknowledgements." (22)
   Rule: era spelling (American "acknowledgments"; the YAML key
   `acknowledgements` stays as code). Severity: should.
   Fix: "The first is the *front matter*, the run of pages from the
   cover plate through the acknowledgments."

7. "The quote is set large and in italic, and the attribution follows
   it in a muted colour." (86, Table 10.2)
   Rule: era spelling (American "color"). Severity: should.
   Fix: "The press sets the quote large and in italic, and the
   attribution follows it in a muted color."
   (The rewrite also names the actor of "is set".)

8. "A short ornamental rule, 0.9 inch long, in a muted colour." (146,
   Table 10.3)
   Rule: era spelling. Severity: should.
   Fix: "A short ornamental rule, 0.9 inch long, in a muted color."
   (See item 29 for the fragment.)

9. "The epigraph starts 1.7 inches down, with the quote large and
   italic and the attribution in a muted colour. The acknowledgements
   start 1.2 inches down, in a column 3.6 inches wide." (204)
   Rule: era spelling, twice. Severity: should.
   Fix: "The epigraph starts 1.7 inches down, with the quote large and
   italic and the attribution in a muted color. The acknowledgments
   start 1.2 inches down, in a column 3.6 inches wide."

10. "Two file icons at the left, metadata.yaml above front-matter.yaml,
    send labelled arrows to seven page outlines ..." (138, fig-alt)
    Rule: era spelling (American "labeled"). Severity: should. (The
    art directive at 279, "Arrow labelled", is the illustrator's text;
    the art desk may want "labeled" for consistency.)
    Fix: "Two file icons at the left, metadata.yaml above
    front-matter.yaml, send labeled arrows to seven page outlines ..."

11. "The press adds a full stop unless the title already ends in a
    period, an exclamation mark, or a question mark." (145, Table 10.3)
    Rule: synonym rotation ("full stop" and "period" for one mark in one
    sentence) and era spelling (American "period", "exclamation
    point"). Severity: should.
    Fix: "The press adds a period unless the title already ends in a
    period, an exclamation point, or a question mark."

12. "For the Alice book, the title becomes ALICE'S ADVENTURES IN
    WONDERLAND with a full stop after it." (155)
    Rule: synonym rotation (same mark as item 11). Severity: should.
    Fix: "For the Alice book, the title becomes ALICE'S ADVENTURES IN
    WONDERLAND with a period after it."

13. "Between them, the two files give the press everything it needs to
    set the opening pages of the PDF." (20)
    Rule: wrong term (the vocabulary names the editions, glossed once
    per chapter; this chapter never glosses one). Severity: should.
    Fix: "Between them, the two files give the press everything it needs
    to set the opening pages of the Print edition (PDF)."

14. "The first command writes to *config/metadata.yaml*, and the rest
    write to *config/front-matter.yaml*. The `config` target knows which
    file owns each key, so you name the key and never the file." (118)
    Rule: wrong term (first use of *target* in the chapter, not italic
    or defined); also, the first `$` line chains three commands, so
    "the first command" reads as one of them. Severity: should.
    Fix: "The three commands on the first line write to
    *config/metadata.yaml*, and the rest write to
    *config/front-matter.yaml*. The `config` *target*, a `press` command
    like `build` or `check`, knows which file owns each key, so you name
    the key and never the file."

15. "An invariant, `INV-front-matter-golden`, holds the generated file
    byte for byte against a golden copy." (208)
    Rule: wrong term (first use of *invariant*, not italic or defined).
    Severity: should.
    Fix: "An *invariant*, a named entry in the press's ledger of
    enforced properties, holds the generated file byte for byte against
    a golden copy. Its name is `INV-front-matter-golden`."

16. "The ledger produces one artifact, the *sources companion*, a
    standalone Markdown file that the press publishes beside the book
    and never inside it." (401)
    Rule: wrong term (first use of *artifact*, not italic or defined).
    Severity: should.
    Fix: "The ledger produces one *artifact*, a file in *dist/* that the
    registry names. That artifact is the *sources companion*, a
    standalone Markdown file that the press publishes beside the book
    and never inside it."

17. "A verifier proves the companion like any other artifact." (417)
    Rule: wrong term (first use of *verifier*, not italic or defined).
    Severity: should.
    Fix: "A *verifier*, one of the press's `verify_*` checks, proves the
    companion like any other artifact."

18. "Three pages follow the copyright page, each only when its key is
    set." (204)
    Rule: hidden actor ("is set"). Severity: should.
    Fix: "Three pages follow the copyright page, each only when you set
    its key."

19. "A print provider once flagged a logo's transparency, and the
    print-safe pass described in Chapter 12, *The print pack*, now
    flattens every image for the interior." (200)
    Rule: hidden actor ("described in"), two ideas (the history and the
    mechanism), and wrong term ("provider" is reserved for a print
    vendor spec; "printer" is the word for the shop). Severity: should.
    Fix: "A printer once flagged a logo's transparency. The print-safe
    pass now flattens every image for the interior, as Chapter 12,
    *The print pack*, describes."

20. "If a book needs a different title page in print, it can supply
    *tex/title-page-print.tex*." (237)
    Rule: second person throughout (the book, not you, acts).
    Severity: should.
    Fix: "If you need a different title page in print, supply
    *tex/title-page-print.tex*."

21. "A press book appears in seven editions at once. The PDF has pages.
    The EPUB has none that stay put, ... The single-leaf HTML edition is
    one long page, and the plain-text edition has no pages at all. ...
    They are the same in the PDF, the EPUB, the reader site, and the
    text file, so one index serves every edition." (317, sidebar)
    Rule: wrong term ("single-leaf HTML edition", "plain-text edition",
    "the reader site", "the text file"; the vocabulary names the
    Single-leaf, Telegraphic, and Chapter editions), and paragraph over
    six sentences (nine). Severity: should.
    Fact: "seven editions": the vocabulary lists eight; see fact
    checker.
    Fix: "A press book appears in every edition at once. The Print
    edition (PDF) has pages. The Circulating edition (EPUB) has none
    that stay put, because each reader's device reflows the text to its
    own screen and type size. The Single-leaf edition (the
    self-contained HTML) is one long page, and the Telegraphic edition
    (plain text) has no pages at all.
    >
    > A page number is a fact about one edition, and an index that
    printed one would be right in the PDF and wrong everywhere else.
    Chapter numbers and appendix letters belong to the manuscript. They
    are the same in the Print, Circulating, Chapter, and Telegraphic
    editions, so one index serves every edition. The cost is precision,
    since a reader who looks up the Cheshire Cat learns the chapter and
    must find the page. For a book of a dozen chapters that is a short
    search."
    (The number of editions stays for the fact checker to settle.)

22. "You can edit the file by hand, but `press config` is the shorter
    path, and the typed model checks each value before it writes a
    byte." (101)
    Rule: two ideas (three clauses; "it" can be the model or the
    target). Severity: should.
    Fix: "You can edit the file by hand, but `press config` is the
    shorter path. The typed model checks each value before `press
    config` writes a byte."

23. "The Alice book declares no rights notice, manufacture line,
    contact, or colophon note, so none of those lines appears, and
    "Made slowly." closes the text above the logo." (196)
    Rule: sentence over 30 words (34) and two ideas. Severity: should.
    Fix: "The Alice book declares no rights notice, manufacture line,
    contact, or colophon note, so none of those lines appears. "Made
    slowly." closes the text above the logo."

24. "A reworded sentence may no longer say what its source supports,
    and only you can judge that, so the press stops and makes you
    look." (355)
    Rule: two ideas (three clauses). Severity: should.
    Fix: "A reworded sentence may no longer say what its source
    supports. Only you can judge that, so the press stops and makes you
    look."

25. "A short claim such as "in 1865" is likely to recur, so declare the
    file for every entry and give the claim enough words to stand
    alone." (387)
    Rule: two ideas (description fused with two commands; procedure
    apart from description), and the Tip at 390 repeats the first
    command (style guide 8.1, an admonition that repeats the paragraph
    above it). Severity: should.
    Fix: "A short claim such as "in 1865" is likely to recur, so give
    each claim enough words to stand alone." (The Tip keeps "Put a
    `file` on every entry.")

26. "A number you have not yet received can stand as `pending`, and
    the press prints it as "[pending]" on the page." (198)
    Rule: perfect tense. Severity: should.
    Fix: "A number you do not hold yet can stand as `pending`, and the
    press prints it as "[pending]" on the page."

27. "Either the pattern is wrong, and you correct the `match` list, or
    the subject has left the book, and you remove the entry." (304)
    Rule: perfect tense. Severity: should.
    Fix: "Either the pattern is wrong, and you correct the `match` list,
    or the subject is gone from the book, and you remove the entry."

28. "A term that matches nothing anywhere in the manuscript is a fault,
    and the press refuses the build. The message names every such term
    at once:" (291)
    Rule: unreferenced example (style guide 3.7: every numbered item is
    referenced in the text before it appears; Example 10.4 is never
    named). Severity: should.
    Fix: "The message names every such term at once, as Example 10.4
    shows."

29. Table 10.3 (145 to 151): "A short ornamental rule, 0.9 inch long,
    in a muted colour." "The word "by", then each author in large small
    capitals." "The `publisher-place`, lowercased."
    Rule: table fragments (style guide 3.7: cells in the Meaning column
    hold sentences). Severity: should.
    Fix: "A short ornamental rule, 0.9 inch long, in a muted color, sits
    below the title." "The word "by" comes first, then each author in
    large small capitals." "The press sets the `publisher-place` in
    lowercase." The Title, Subtitle, and Year rows take the same
    treatment ("The press sets the first four-digit year in `date` in
    lowercase roman numerals.").

30. Table 10.2 (85 to 93): "A short line, set in italic on a page of
    its own, low on the page." "The first line of the copyright page."
    "An address for the publisher, set on the copyright page."
    Rule: table fragments (style guide 3.7). Severity: should.
    Fix: "A short line that the press sets in italic, low on a page of
    its own." "It fills the first line of the copyright page." "It is an
    address for the publisher, and the press sets it on the copyright
    page." The `acknowledgements`, `manufacture`, `colophon-note`,
    `rights-notice`, and `motto` rows take the same treatment.

31. Tables 10.4 (182 to 192) and 10.6 (339 to 343): "The `rights-notice`,
    followed by a rule." "The press logo from *assets/press-logo.png*,
    1.7 inches wide." "Required. The source that warrants the claim."
    Rule: table fragments (style guide 3.7). Severity: should.
    Fix: "The `rights-notice` appears here, followed by a rule." "The
    press sets its logo from *assets/press-logo.png*, 1.7 inches wide."
    "Required. It names the source that warrants the claim." The
    remaining rows of both tables take the same treatment.

32. "The generated front matter has three switches, and they take
    effect in a fixed order." (212; 223 calls them "the conditions",
    and the table heads its column "Condition")
    Rule: synonym rotation ("switches" and "conditions"; "switch" also
    names the `retail` key at 198). Severity: should.
    Fix: "The generated front matter depends on three conditions, and
    the press tests them in a fixed order."

33. "Without that note, the date "First edition, 2026" would give "first
    edition" in lower case." (196)
    Rule: era spelling ("lowercase", as the chapter writes it at 150
    and 182). Severity: may.
    Fix: "Without that note, the date "First edition, 2026" would give
    "first edition" in lowercase."

34. "The press collapses runs of whitespace before it compares, and it
    compares with case." (339, Table 10.6)
    Rule: rhythm (the repeated "compares" and "with case" read as a
    slip). Severity: may.
    Fix: "The press collapses runs of whitespace before it compares, and
    the comparison is case-sensitive."

35. "An override also takes on the image height cap." (233)
    Rule: rhythm (the phrasal verb "takes on" is ambiguous; the next
    sentences say the override must cap its own image). Severity: may.
    Fix: "An override must also enforce the image height cap itself."

36. "The contents and the lists follow, and the manuscript supplies
    them, not either configuration file." (204)
    Rule: rhythm (a trailing "not X" that echoes the staging pattern;
    the figure already makes the point). Severity: may.
    Fix: "The contents and the lists follow, and the manuscript supplies
    them."

37. "A dropped block leaves no trace on the page, which is why an absent
    key never produces a blank leaf." (206)
    Rule: rhythm (restates 79, "a key you leave out produces nothing").
    Severity: may.
    Fix: "A dropped block leaves no trace on the page."

38. "Every key is optional, and a key you leave out produces nothing: no
    empty page, no blank line, no label with nothing after it." (79)
    Rule: rhythm (a forced triad; the three are one fact). Severity:
    may.
    Fix: "Every key is optional, and a key you leave out produces
    nothing, not even a blank line."

39. "You can also run `press research` to drive it." (397)
    Rule: wrong term (the vocabulary keeps "driver" out for an
    *operator*). Severity: may.
    Fix: "You can also run `press research`, which runs the workflow for
    you."

40. "The generator sets a cover plate and a title page, but it has no
    separate half-title leaf." (31, Table 10.1; also "the generator" at
    206 and "The splitter" at 173)
    Rule: synonym rotation (the chapter otherwise calls the actor "the
    press"). Severity: may.
    Fix: "The press sets a cover plate and a title page, but it has no
    separate half-title leaf."

41. "The press can then report a moved claim by name, instead of a
    missing one, and a common phrase in another chapter cannot make the
    entry ambiguous." (390, Tip)
    Rule: two ideas. Severity: may.
    Fix: "The press can then report a moved claim by name, instead of a
    missing one. A common phrase in another chapter also cannot make
    the entry ambiguous."

42. "Each entry is the term in bold, a separator, and its locators,
    separated by commas." (310)
    Rule: rhythm ("separator ... separated"). Severity: may.
    Fix: "Each entry is the term in bold, a separator, and its locators,
    with commas between them."

## For the fact checker

- 283: "The string `mock turtle` also misses "mock-turtle", because the
  hyphen counts as part of a word." The pattern holds a space and the
  text holds a hyphen, so the miss may come from the space, not from
  the boundary rule. Fact: see fact checker.
- 317: "A press book appears in seven editions at once." The vocabulary
  names eight editions. Fact: see fact checker.

## Checked and clean

- Second person and present tense hold, except item 20. "We" never
  appears. "I" never appears.
- The dry understatement appears in the footnotes at 421 and 423, at
  302 ("learns only that the index is wrong"), and at the end of the
  sidebar. That is about once every few pages, and no heading carries
  one.
- Every admonition is imperative and runs three sentences or fewer.
- The four footnotes carry asides and history. The body needs none of
  them.
- Numbers under ten are spelled out in prose. The digits that remain
  are versions, measurements, chapter labels, or code.
- Headings and captions are in sentence case.
- No em or en dash, no semicolon in prose, no assistant vocabulary, no
  hedge stack, no meta-narration.
