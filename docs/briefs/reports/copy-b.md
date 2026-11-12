# Copyedit: Appendix B, Configuration reference

File: `book/appendices/b-configuration-reference.md`

## Status

REVISE. Two blocks, both watchlist sightings of "shipped" ("the six
shipped profiles", "every shipped profile"). This follows the Chapter 12
precedent: `jargon-allow` lets "shipped" through, but here it is not
press's name for anything. `press check` passes the whole book, and its
jargon audit names no term in this file. The other allow-listed watchlist
words in the file are accepted: "scaffold" (press's name for what
`press new` writes), "spine" (the bound edge), "canonical link" (the HTML
name), and "release gate" at 169 (the commerce gate, which is the
vocabulary's reserved use).

Counts by severity: blocks 2, should 34, may 13, fact 2.

Most frequent rules broken: hidden actor (16 items, counting the passive
inside block 2), two ideas (15, most of them as the second rule on an
item), wrong term (7, counting both blocks). Synonym rotation (4), era
spelling (4), and sentence over 30 words (4) follow.

The entries are definition lists. Per the desk instruction, the list form
itself is not counted: entry fragments ("Type `str`, default none."),
entries over six sentences, and the reference's terse rhythm are
accepted. The prose inside each entry is judged by the contract.

Line numbers are `cat -n` line numbers in the file as it stands.

## The ste_check findings, judged

ste_check reports 45 findings (654 sentences, average 7.4 words, max 50).

- Paragraph length at 41, 47, 73, 78, 81, 108, 238, 244, 311, 349, 404,
  425, and 434: accepted. Each is one definition-list entry, and the
  counter reads the term line and its body as one paragraph. Line 7 is a
  real prose paragraph of seven sentences (item 5). Line 38's count is
  the `author` entry, accepted.
- Sentence length at 7 (24 words) is under the ceiling. 41 is the `date`
  entry (item 9). 251, 373, and 377 are real (items 26, 33, 34). 443 (50
  words) is the index comment, accepted.
- Semicolons: accepted. The hit at 85 is inside the verbatim
  `press config list` message, and 443 is the index comment. Example B.1
  and the profile refusal at 106 carry semicolons inside press's own
  messages. No prose semicolon.
- Passive at 3, 45, 48, 99, 115, 128, 350, 365, 423, and 438: real
  (hidden actor; items 3, 11, 12, 15, 16, 2, 31, 32, 35, 36). At 39 the
  hit is real (item 8). At 153 ("is written `X`") and 292 ("is
  composed") the passive states a convention or a property and has no
  actor to name: accepted.
- Perfect tense at 373 ("has moved"): real (item 33).
- `-ing` forms at 103 ("binding", a noun), 128 and 236 (chapter titles),
  350 ("Matching", "matching", gerunds), and 359 ("Rewording", a gerund
  subject): accepted. 224 ("naming") is a participle phrase (item 44).
- 'whether' at 137: accepted. The contract keeps "whether" for this
  voice.
- 'landscape' at 292: accepted. It is the plate's orientation, not the
  assistant word.

## Findings

1. "The six shipped profiles are `house-6x9`, `house-6x9-color`,
   `novella-5x8`, `digest-5.5x8.5`, `mass-market-4.25x6.87`, and
   `large-print-7x10`." (106)
   Rule: wrong term (watchlist "shipped", one-sighting list). Severity:
   blocks.
   Fix: "The six profiles the press carries are `house-6x9`,
   `house-6x9-color`, `novella-5x8`, `digest-5.5x8.5`,
   `mass-market-4.25x6.87`, and `large-print-7x10`."

2. "The book's chapter opening is merged over the design profile's
   setting, and every shipped profile sets `none`." (128)
   Rule: wrong term (watchlist "shipped"), with a hidden actor and two
   ideas. Severity: blocks.
   Fix: "The press merges the book's chapter opening over the design
   profile's setting. Every profile the press carries sets `none`."

3. "The files live in *config/*, and only *config/metadata.yaml* is
   required." (3)
   Rule: hidden actor. Severity: should.
   Fix: "The files live in *config/*, and the press requires only
   *config/metadata.yaml*."

4. "*config/aesthetic.yaml* has no validator." (7)
   Rule: wrong term ("validator" is on the never list; the thing missing
   is the typed model the previous sentence names). Severity: should.
   Fix: "No typed model checks *config/aesthetic.yaml*."

5. The paragraph at line 7 (seven sentences, two topics: the
   `press config` commands, then validation).
   Rule: six sentences at most, one topic per paragraph. Severity: should.
   Fix: start a new paragraph at "Before `press config set` writes a
   byte, it checks the new value with the typed model that a build uses."

6. "The generated title page sets it in capitals and adds a full stop
   unless the title already ends in a period, an exclamation mark, or a
   question mark." (33)
   Rule: era spelling ("full stop" is British), and synonym rotation
   ("full stop", then "period", for one mark). Severity: should.
   Fix: "The generated title page sets it in capitals and adds a period
   unless the title already ends in a period, an exclamation mark, or a
   question mark."

7. "Written as clauses joined by "or," (for example `"OR, ...; OR,
   ..."`), it stacks on the title page, one clause to a line, and on the
   landing page." (36)
   Rule: hidden actor (who writes it), condition not first as a clause.
   Severity: should.
   Fix: "If you write it as clauses joined by "or," (for example
   `"OR, ...; OR, ..."`), it stacks on the title page, one clause to a
   line, and on the landing page."

8. "A single string is accepted and becomes a list of one." (39)
   Rule: hidden actor. Severity: should.
   Fix: "The press also accepts a single string and makes it a list of
   one."

9. "The press takes the first four-digit year in it that begins with 1 or
   2 and uses that year for the EPUB date and for the lowercase roman
   numerals on the title page." (42)
   Rule: sentence over 30 words, two ideas. Severity: should.
   Fix: "The press takes the first four-digit year in it that begins with
   1 or 2. It uses that year for the EPUB date and for the lowercase
   roman numerals on the title page."

10. "The colophon's edition line comes from the text before the first
    comma, lowercased, unless `edition-note` is set." (42)
    Rule: hidden actor, and the condition comes last. Severity: should.
    Fix: "Unless you set `edition-note`, the colophon's edition line comes
    from the text before the first comma, lowercased."

11. "It is required once *config/front-matter.yaml* exists." (45)
    Rule: hidden actor. Severity: should.
    Fix: "The press requires it once *config/front-matter.yaml* exists."

12. "The press also exports it to TeX as the environment variable
    `BOOK_PUBLISHER`, which the plain title page reads when no front
    matter is generated." (48)
    Rule: hidden actor. Severity: should.
    Fix: "The press also exports it to TeX as the environment variable
    `BOOK_PUBLISHER`, which the plain title page reads when the press
    generates no front matter."

13. "The cover commission uses it as the subject when neither `--subject`
    nor `cover.subject` names one." (54)
    Rule: synonym rotation. Lines 33, 48, and 265 call the same thing
    "the cover prompt", and "commission" is the vocabulary's word for an
    entry in *art/commissions.md*, which `press cover` does not write.
    Severity: should.
    Fix: "The cover prompt uses it as the subject when neither `--subject`
    nor `cover.subject` names one."

14. "The `ornate` style sets a foliate initial in the PDF and a styled
    display capital on the Web and in the EPUB." (131)
    Rule: wrong term. The appendix never uses press's edition names; it
    says "the PDF" and "the EPUB" throughout (42, 68, 79, 82, 131, 200,
    318). For a file path (`dist/<slug>.pdf`) or a verifier ("the PDF
    verifier") the format word is right. Where the sentence means the
    edition, gloss the name once, here, and use it at 79 as well.
    Severity: should.
    Fix: "The `ornate` style sets a foliate initial in the Print edition
    (PDF) and a styled display capital on the Web and in the Circulating
    edition (EPUB)." At 79: "..., which breaks an exact match in the
    Print edition."

15. "The three lines are folded here to fit the page." (99)
    Rule: hidden actor. Severity: should.
    Fix: "We folded the three lines to fit the page."

16. "The first two are printed." (115)
    Rule: hidden actor. Severity: should.
    Fix: "`paperback` and `casewrap` are printed covers."

17. "With `linen`, the press prints only the jacket and suppresses the
    printed field, and it never prints a simulated cloth texture." (115)
    Rule: two ideas. Severity: should.
    Fix: "With `linen`, the press prints only the jacket and suppresses
    the printed field. It never prints a simulated cloth texture."

18. "Only the `house-6x9-color` profile reads it, and that profile needs a
    provider with a documented color caliper, which today means `kdp`."
    (124)
    Rule: era spelling (house era touch: "at the time of this writing"
    before a claim that will date), and two ideas. Severity: should.
    Fix: "Only the `house-6x9-color` profile reads it. That profile needs
    a provider with a documented color caliper, which at the time of
    this writing means `kdp`."

19. "The chapter-opening initial: `none`, `drop-cap`, `raised-cap`, or
    `ornate`." (131) and "The number of text lines the initial spans."
    (134)
    Rule: wrong term ("initial" is on the never list for the chapter
    opening; give the trade word once at most). Severity: should.
    Fix: "The chapter-opening style: `none`, `drop-cap`, `raised-cap`, or
    `ornate`." and "The number of text lines the chapter opening spans."
    Keep "a foliate initial" in item 14 as the one trade-name use.

20. "The gate only advises unless `PRESS_RELEASE=1` is set." (169)
    Rule: hidden actor, and the condition comes last. Severity: should.
    Fix: "Unless CI or you set `PRESS_RELEASE=1`, the gate only advises."

21. "The press's model has the provider as the seller, and the publisher
    must confirm who the legal seller is." (178)
    Rule: two ideas, and third person where the house voice says "you".
    Severity: should.
    Fix: "The press's model has the provider as the seller. You must
    confirm who the legal seller is."

22. "...and the dedication, epigraph, and acknowledgements pages." (200)
    and "The text of the acknowledgements page." (215)
    Rule: era spelling (American is "acknowledgments"; the style guide
    spells it so). The key `acknowledgements` stays as it is in code.
    Severity: should.
    Fix: "...and the dedication, epigraph, and acknowledgments pages."
    and "The text of the acknowledgments page."

23. "The epigraph page prints only when this key is set." (209)
    Rule: hidden actor. Severity: should.
    Fix: "The epigraph page prints only when you set this key."

24. "Watchlist terms this book may use." (242), "It may use the fields
    `{title}`, ..." (408), and "It may use `{subject}`, `{ink}`, and
    `{paper}`." (426)
    Rule: honest modals (Pass 2: "may" only for real uncertainty or
    advice; this is capability). Severity: should.
    Fix: "Watchlist terms this book can use.", "It can use the fields
    `{title}`, ...", and "It can use `{subject}`, `{ink}`, and
    `{paper}`."

25. "`press aesthetic` with no argument prints the merged result, and the
    defaults below are the house values." (249)
    Rule: two ideas. Severity: should.
    Fix: "`press aesthetic` with no argument prints the merged result. The
    defaults below are the house values."

26. "Certain craft laws hold whatever the aesthetic says: the exact title
    and author appear verbatim on the art, cover plates are flat, print
    interiors are single ink (the `house-6x9-color` profile is the one
    exception), and the trim is the trim." (251)
    Rule: sentence over 30 words. Severity: should. Keep "the trim is
    the trim": it is the appendix's best understatement.
    Fix: "Certain craft laws hold whatever the aesthetic says. The exact
    title and author appear verbatim on the art, cover plates are flat,
    and the trim is the trim. Print interiors are single ink, except
    under the `house-6x9-color` profile."

27. "Intake greys a plate to the single interior ink when this text
    contains both the words "single" and "ink" and the design profile is
    not a color profile." (289)
    Rule: era spelling ("greys"), and the condition comes last.
    Severity: should.
    Fix: "When this text contains both the words "single" and "ink" and
    the design profile is not a color profile, intake grays a plate to
    the single interior ink."

28. "A named family is set with oldstyle numerals." (309)
    Rule: hidden actor. Severity: should.
    Fix: "The press sets a named family with oldstyle numerals."

29. "Each entry maps a token to a `#hex` color, and press writes it into
    the reader sheet's light theme." (312)
    Rule: two ideas. Severity: should. ("reader sheet" here and "the
    sheet" at 315 are a third name for the reader stylesheet; may.)
    Fix: "Each entry maps a token to a `#hex` color. Press writes the
    palette into the light theme of the reader stylesheet."

30. "Press writes each book color as a `\definecolor` line in
    *build/aesthetic.tex*, and it removes that file when the book sets no
    override." (318)
    Rule: two ideas. Severity: should.
    Fix: "Press writes each book color as a `\definecolor` line in
    *build/aesthetic.tex*. When the book sets no override, press removes
    that file."

31. "Fenced code, inline code, and image lines are removed before
    matching." (350)
    Rule: hidden actor. Severity: should.
    Fix: "The press removes fenced code, inline code, and image lines
    before it matches."

32. "With a declared file, the claim must appear exactly once in that
    file, and copies elsewhere are allowed." (365)
    Rule: hidden actor, two ideas. Severity: should.
    Fix: "With a declared file, the claim must appear exactly once in that
    file. The press allows copies elsewhere."

33. "It refuses a malformed entry, a duplicate claim, a claim that matches
    nothing, a claim that matches more than once, an unknown declared
    file, and a claim that has moved to another file." (373)
    Rule: sentence over 30 words, perfect tense. Severity: should.
    Fix: "It refuses a malformed entry, a duplicate claim, and an unknown
    declared file. It also refuses a claim that matches nothing, a claim
    that matches more than once, and a claim that moved to another file."

34. "The house library lives inside the press, and a book's
    *config/cover-styles.yaml* merges over it, style by style, so a book
    can add a style or replace one by its id." (377)
    Rule: sentence over 30 words, two ideas. Severity: should.
    Fix: "The house library lives inside the press. A book's
    *config/cover-styles.yaml* merges over it, style by style, so a book
    can add a style or replace one by its id."

35. "Without `--from`, such a style is refused with `the <style> style
    needs source material: --from <image>`." (423)
    Rule: hidden actor. Severity: should.
    Fix: "Without `--from`, the press refuses such a style with `the
    <style> style needs source material: --from <image>`."

36. "When it exists, the press never generates front matter, and
    *config/front-matter.yaml* is ignored." (438)
    Rule: hidden actor. Severity: should.
    Fix: "When it exists, the press never generates front matter and
    ignores *config/front-matter.yaml*."

37. "What `press config list` prints is the authority for each key's type
    and purpose." (3)
    Rule: wrong term ("authority" is a key and a concept in the table of
    authorities, which this appendix documents at 361). Severity: may.
    Fix: "What `press config list` prints decides each key's type and
    purpose."

38. "The two style libraries at the end of this appendix are not in
    `press config list`, and you edit them by hand." (9)
    Rule: two ideas (and a second topic in a paragraph about the four
    kinds). Severity: may.
    Fix: move it to its own line after the paragraph: "The two style
    libraries at the end of this appendix are not in `press config list`.
    You edit them by hand."

39. "Type `str`, default none, optional." (71, 74, 181, 184, 187)
    Rule: synonym rotation in the entry form. Every other key with no
    default says only "default none", so "optional" here reads as a
    different status. Severity: may.
    Fix: "Type `str`, default none." in all five, or add "optional" to
    every optional key.

40. "Type `int`. ... The model's default is 40, and the press
    documentation gives 40." (82)
    Rule: two ideas, and the entry breaks the form the opening sets
    (default in the first line; documentation named only where it
    disagrees with the code). Severity: may.
    Fix: "Type `int`, default `40`. The page floor: the smallest page
    count the PDF verifier accepts."

41. "Set this key to the shop that will print the book before you design
    the cover." (109)
    Rule: condition first (a warning before the step it protects).
    Severity: may.
    Fix: "Before you design the cover, set this key to the shop that will
    print the book."

42. "A returns page, which must be an HTTPS URL." (187) and "appended to
    the generated returns page" (196)
    Rule: synonym rotation (the key is `refund-url`, the file is
    *refunds.html*, the prose says "returns"). Press's own page title is
    "Returns & refunds", so "returns" is defensible. Severity: may.
    Fix: "A returns page, which must be an HTTPS URL. If you omit it, the
    press generates *refunds.html*, titled "Returns & refunds"." (Or
    "refund page" in both entries.)

43. "The scaffold writes the file with every key commented out, and
    `press config set` creates it if it is missing." (200)
    Rule: two ideas. Severity: may.
    Fix: "The scaffold writes the file with every key commented out. If
    the file is missing, `press config set` creates it."

44. "The colophon's production note, naming the type and the method, set
    in italic." (224)
    Rule: -ing rider (a participle phrase, not the comma-ensuring kind).
    Severity: may.
    Fix: "The colophon's production note, which names the type and the
    method, set in italic."

45. "In `press config list` it is the structured field `index-terms`, and
    the press sends you to the file or to the index workflow instead of
    the shell." (333)
    Rule: two ideas. Severity: may.
    Fix: "In `press config list` it is the structured field
    `index-terms`. The press sends you to the file or to the index
    workflow instead of the shell."

46. "The ledger checks claims. It does not format citations, so use
    footnotes for citations in the text." (373)
    Rule: "not X but Y" (weak form: a positive sentence staged against a
    negative one). Severity: may.
    Fix: "The ledger does not format citations, so use footnotes for
    citations in the text."

47. "With `baked`, the image model letters the title, and press appends a
    guardrail that names the exact title, author, and imprint and forbids
    other words." (405)
    Rule: two ideas. Severity: may.
    Fix: "With `baked`, the image model letters the title. Press appends a
    guardrail that names the exact title, author, and imprint and forbids
    other words."

48. "A hand-authored front matter." (438)
    Rule: rhythm (front matter takes no article). Severity: may.
    Fix: "Hand-authored front matter."

49. "A heading fault or a long paragraph there is a warning, not an
    error." (245)
    Rule: wrong term ("error" is on the vocabulary's never list for a
    red result). If "warning" and "error" are the words press prints,
    keep them in code type; otherwise reword. Severity: may.
    Fix: "A heading fault or a long paragraph there draws a warning and
    does not fail the check."

## Sent to the fact checker

F1. "Double each backslash in the YAML." (239) fact: see fact checker. Only a
    double-quoted YAML string needs the doubling. A single-quoted pattern
    takes one backslash, and this book's own *config/house-rules.yaml*
    writes its patterns single-quoted with single backslashes.

F2. "`press check` refuses a trim, binding, or ink that the provider does
    not offer, before it renders anything." (103) fact: see fact checker.
    `press check` does not render, so "before it renders anything" may
    belong to the build that reads the print group, not to the checker.

## Other checks

- Second person and present tense hold throughout, except item 21. No
  "I". "We" does not appear. Item 15 introduces it for an authorial act.
- Dry understatement: "The `house` numbers belong to no real shop" (109),
  "and the trim is the trim" (251), and "TeX knows it by the house name
  `linkgreen`, whatever its color" (327). That is three in about fifteen
  pages, none in a heading. It is the right rate.
- Admonitions: none. Footnotes: none. Both are fine for a reference
  appendix.
- Headings and captions are in sentence case. No title case.
- Era spellings: "Web" (131, 441) is correct. No "website", "email",
  "file name", "man page", "appendices", "UNIX", "folder", or "towards".
  The British forms are items 6, 22, and 27.
- Numbers: under ten are spelled out in prose ("four groups", "two to
  four", "three lines", "six profiles", "eleven points"). Digits appear
  only for values (`1`, "1 or 2", "at least 24", "10, 100, or 1000"),
  which the rule exempts.
- Vocabulary note (not an appendix fault): `docs/vocabulary.md` lists
  the provider as `ingram`. The press's provider id is `ingramspark`
  (`src/press/data/provider-specs/ingramspark.yaml`), and the appendix
  follows the code at 109 and 118. The vocabulary row should change.
