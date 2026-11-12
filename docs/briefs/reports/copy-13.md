# Copyedit: Chapter 13, Registrations

File: `book/chapters/13-registrations.md`

## Status

REVISE. Two blocks: one watchlist sighting ("lands", in a heading and its
In-this-chapter entry) and one one-line closer, which ends the sidebar.
`press check` passes the whole book. Its jargon audit names one
inspect term in this file, "honest" (31), which sits inside a verbatim
quotation of the registrations skill and is press's own name for the
placeholder (the Chapter 12 precedent). "lands" is on `jargon-allow`, but
here it is not press's name for anything, and the contract puts the
watchlist on the one-sighting list (the Chapter 8 and 12 precedent).

Counts by severity: blocks 2, should 20, may 22, fact 3 (items 12, 16,
and 35; item 12 also carries a may).

Most frequent rules broken: two ideas (9), wrong term (8, counting the
watchlist block), synonym rotation (6).

Line numbers are `cat -n` line numbers in the file as it stands.

## The ste_check findings, judged

ste_check reports 18 findings (238 sentences, average 11.9 words, max 45).

- "verify" (42): accepted under the 80 percent rule. The word names the
  target.
- Semicolons at 46, 175 (the "No LCCN recorded yet" quotation), and 221:
  accepted. All three are inside verbatim quotations of press's
  documentation and output. 304 is the index comment. No prose semicolon.
- Sentence length at 98 and 177: accepted. The footnote marker merges
  the sentence with the next one. Each sentence is under 30 words.
- Sentence length at 248 (alt text), 304 (index comment), and paragraph
  length at 250 (the `art:` directive): accepted. None is running prose.
- Modal passive and passive at 175 ("must be deposited"): accepted. The
  text is a verbatim quotation of the PCN listing. The same holds for
  "are stated" at 246 (the first law, quoted).
- Passive "is labelled" at 248: the voice is acceptable in alt text, but
  the spelling is British (item 2).
- `-ing` forms at 130 ("Cataloging in Publication", a program name), 213
  (a heading), and 254 (a chapter title): accepted.
- Paragraph length at 141: a real finding (item 22).

Also accepted on reading:

- "scaffold" (150, 177, 300) is a literal name, and it is on
  `jargon-allow`.
- Cross-references of the form "The section ... later in this chapter
  explains" (42, 130) are accepted, as in Chapter 12.
- Dry understatement appears at 17 ("and it does not try"), 209 ("an
  accurate account of the book"), and footnote 300, never in a heading.
- There is no "I". The two "we" sentences are items 12 and 27.
- Admonitions (48, 71, 94, 179, 183, 240) are all imperative and run two
  sentences each. Six is within the three-to-eight range.
- Three footnotes, each an aside. The ISBN-10 footnote repeats a fact
  that Table 13.2 already gives the body, which is acceptable.
- Spelling is American except item 2. The chapter uses none of the era
  words (Unix, e-mail, Web site, filename, manpage, appendixes, toward),
  so none is misspelled.
- Example 13.4's arithmetic and the table checks are left to the fact
  checker by brief.

## Findings

1. "Where each number lands" (13 and 244)
   Rule: wrong term (watchlist: "lands"). Severity: blocks.
   Fix: "Where each number goes" (in the heading and in the
   In-this-chapter list). It also matches the figure caption at 248.

2. "...five destinations on the right: ... Each arrow is labelled with the
   field it carries." (248, `fig-alt`)
   Rule: era spelling (American). Severity: should.
   Fix: "Each arrow is labeled with the field it carries."

3. "The book can wait for its numbers, and it cannot go on sale before they
   arrive." (141, last sentence of the sidebar)
   Rule: one-line closer (it restates the two sentences before it).
   Severity: blocks.
   Fix: delete the sentence. The sidebar ends on "Once you declare a
   retail edition, a placeholder anywhere in the registrations makes the
   checker refuse the book." (see item 24).

4. "Each edition needs an ISBN, many books carry an LCCN from the Library of
   Congress, and a serial has an ISSN." (17)
   Rule: two ideas (three, in one sentence). Severity: should.
   Fix: "Each edition needs an ISBN. Many books also carry an LCCN from
   the Library of Congress, and a serial carries an ISSN."

5. "You can build, check, and verify the Alice book with Example 13.1 in
   place, and every page that will carry a number shows where it goes."
   (42)
   Rule: two ideas. Severity: should.
   Fix: "You can build, check, and verify the Alice book with Example 13.1
   in place. Every page that will carry a number shows where it goes."

6. "It is not a block that the Alice book owns, so `alice` would type the
   numbers from her own agency's receipt in its place." (54)
   Rule: simple tenses ("would"). Severity: should.
   Fix: "It is not a block that the Alice book owns, so `alice` types the
   numbers from her own agency's receipt in its place."

7. "The size is a power of ten, and the documentation lists 10, 100, and
   1000, although the code accepts any power from 10 through 1,000,000."
   (65)
   Rule: two ideas (and "1000" beside "1,000,000"). Severity: should.
   Fix: "The size is a power of ten. The documentation lists 10, 100, and
   1,000, although the code accepts any power from 10 through 1,000,000."

8. "A malformed block fails `press check`." (69)
   Rule: wrong term ("fail" is for a verifier result; the press refuses).
   Severity: should.
   Fix: "`press check` refuses a malformed block."

9. "An incomplete block, with the prefix or the size missing, is not
   validated at all." (69)
   Rule: hidden actor. Severity: should.
   Fix: "The press does not validate an incomplete block, one with the
   prefix or the size missing."

10. "The press cannot judge a prefix without knowing the size that goes with
    it." (69)
    Rule: -ing chain (the action in the verb). Severity: may.
    Fix: "The press cannot judge a prefix until it knows the size that goes
    with it."

11. "A block with only one of the two passes the checker without
    inspection, so the checker says nothing about a wrong prefix." (72,
    Tip)
    Rule: two ideas. Severity: may.
    Fix: "A block with only one of the two passes the checker without
    inspection. The checker says nothing about a wrong prefix."

12. "We broke the output line in two to fit the page." (77)
    Rule: "we" outside the authors' judgment. Severity: may.
    Fix: "Example 13.3 breaks the output line to fit the page."
    Also fact: see fact checker. Example 13.3 shows the message on three
    lines (83 to 85), not two.

13. "A number that the model would refuse never reaches the file." (90)
    Rule: wrong term ("the model" is never defined in the book's
    vocabulary). Severity: should.
    Fix: "A number that `press config` would refuse never reaches the
    file."

14. "a check modulo 11" (98), "a mod-11 sum" (102), "Mod 11" (Table 13.2,
    124 and 125)
    Rule: synonym rotation. Severity: may.
    Fix: use "a mod-11 check" in prose at 98 and 102, and "Mod 11" in the
    table: "The press also does the ISBN-10 arithmetic, a mod-11 check,
    for the older ten-digit form." "The press checks an ISSN with a mod-11
    check."

15. "The number 123X-5678 carries its `X` in the body of the number, where
    only a digit may stand." (115)
    Rule: honest modals. Severity: may.
    Fix: "The number 123X-5678 carries its `X` in the body of the number,
    where only a digit can stand."

16. "The checker refuses both." (115)
    Fact: see fact checker. The vocabulary reserves "the checker" for
    `press check`. Confirm that `press check` (and not the config model
    or the selftest) is what refuses these numbers, and name that actor.

17. "...which is up to three lowercase letters followed by 8 to 12 digits,
    or `[a-z]{0,3}\d{8,12}` as a pattern." (117)
    Rule: numbers under ten spelled out in prose. Severity: should.
    Fix: "The press can check only its shape, which is up to three
    lowercase letters followed by eight to twelve digits, or
    `[a-z]{0,3}\d{8,12}` as a pattern."

18. "A self-publisher gets an LCCN through the Preassigned Control Number
    program, PCN." (130)
    Rule: synonym rotation (the next sentence but one glosses CIP in
    parentheses). Severity: may.
    Fix: "A self-publisher gets an LCCN through the Preassigned Control
    Number (PCN) program."

19. "The key `registrations.retail` tells the press which of the two you
    are building." (134)
    Rule: simple tenses (progressive). Severity: should.
    Fix: "The key `registrations.retail` tells the press which of the two
    you build."

20. "The rest of the message names the numbers at fault, and no artifact
    gets built until you fill them." (136)
    Rule: hidden actor. Severity: should.
    Fix: "The rest of the message names the numbers at fault. The press
    builds no artifact until you fill them."

21. "Pending, not a guess" (139, sidebar title)
    Rule: not X but Y (the contrast shape in a heading). Severity: may.
    Fix: "Why pending is a word"

22. The sidebar paragraph (141) runs eleven sentences.
    Rule: one topic per paragraph, six sentences at most. Severity:
    should.
    Fix: break after "The press gives the second a name and a rule." The
    first paragraph keeps the waiting and the two choices. The second
    begins "A guessed number looks like a real one..." and carries the
    reasoning and the retail flag.

23. "A guessed number looks like a real one on every page it reaches, and
    nothing in the artifact tells a reader or a distributor that it is
    wrong." (141)
    Rule: two ideas. Severity: should.
    Fix: "A guessed number looks like a real one on every page that it
    reaches. Nothing in the artifact tells a reader or a distributor that
    it is wrong."

24. "Once you declare a retail edition, a placeholder anywhere in the
    registrations stops the checker." (141)
    Rule: wrong term (the checker stops the book; the press refuses).
    Severity: should.
    Fix: "Once you declare a retail edition, a placeholder anywhere in the
    registrations makes the checker refuse the book."

25. "Set the flag for the release, not while you write." (144)
    Rule: not X but Y (the contrast shape). Severity: may.
    Fix: "Set the flag when you prepare the release."

26. "Example 13.5 shows the target in a fresh copy of the Alice book,
    before any registration is set." (150)
    Rule: hidden actor. Severity: should.
    Fix: "Example 13.5 shows the target in a fresh copy of the Alice book,
    before you set any registration."

27. "We broke two long lines to fit the page and cut the closing advice,
    which the next paragraph quotes." (150)
    Rule: "we" outside the authors' judgment. Severity: may.
    Fix: "Example 13.5 breaks two long lines to fit the page and omits the
    closing advice, which the next paragraph quotes."

28. Table 13.3, Meaning column: "The time of the build, to the minute."
    (195), "The product's ISBN-13." (197), "The author, in the ONIX role
    code for an author." (199), "The ISO 639-2/B code mapped from the
    book's `lang`." (200), "The publisher, with `CityOfPublication` beside
    it." (201), "The year of publication only." (203)
    Rule: Meaning cells hold sentences, not fragments (style guide 3.7).
    Severity: should.
    Fix: "The element holds the time of the build, to the minute." "The
    element holds the product's ISBN-13." "The element names the author,
    with the ONIX role code for an author." "The element holds the ISO
    639-2/B code that the press maps from the book's `lang`." (keep the
    second sentence) "The element names the publisher, with
    `CityOfPublication` beside it." "The element holds the year of
    publication only."

29. "The base is the book's `site-url`, then its `repository`, then `press:`
    and the slug." (196)
    Rule: two ideas (the order of preference is implied, not stated).
    Severity: may.
    Fix: "The base is the book's `site-url`. Without one, the press uses
    the `repository`, and without that, `press:` and the slug."

30. "A request that takes longer is abandoned." (227, Table 13.4)
    Rule: hidden actor. Severity: should.
    Fix: "The press abandons a request that takes longer."

31. "A catalog record has no need for either, and an XML parser that honors
    an entity declaration can expand or fetch text that nobody asked for."
    (236)
    Rule: two ideas. Severity: should.
    Fix: "A catalog record has no need for either. An XML parser that
    honors an entity declaration can expand or fetch text that nobody
    asked for."

32. "When the PCN comes back, she will run `press lookup lccn` with the new
    number before she stores it." (238)
    Rule: wrong term (the PCN is the program; the LCCN comes back, as at
    276). Severity: should.
    Fix: "When the LCCN comes back, she will run `press lookup lccn` with
    the new number before she stores it."

33. "The EPUB ISBN becomes the identifier of the Circulating edition,
    written as `urn:isbn:` and the number." (254)
    Rule: hidden actor (a participle rider). Severity: may.
    Fix: "The EPUB ISBN becomes the identifier of the Circulating edition.
    The press writes it as `urn:isbn:` and the number."

34. "Because every route starts at the same block, the copyright page cannot
    show an ISBN that the barcode or the EPUB does not carry." (256)
    Rule: synonym rotation ("copyright page" for the colophon, which the
    same paragraph names) and wrong term ("the EPUB" for the edition).
    Severity: should.
    Fix: "Because every route starts at the same block, the colophon
    cannot show an ISBN that the barcode or the Circulating edition does
    not carry."

35. "The registrations skill gives the steps in a fixed order, because each
    step needs a number that the step before it produced." (260)
    Fact: see fact checker. Steps 5 and 6 do not need the LCCN from step
    4, and 294 gives a different reason for the last step.

36. "For the Alice book, `alice` works through them as follows:" (260)
    Rule: procedure introduced by an infinitive phrase and a colon (style
    guide 3.6). Severity: may.
    Fix: "To register the Alice book, `alice` works through the steps in
    this order:"

37. "Buy an ISBN block from your agency, and record its prefix and size
    under `registrations.isbn-block`." (262) and "Assemble the PCN fields,
    and submit them through PrePub Book Link:" (270)
    Rule: two ideas (each step a single imperative, style guide 3.6).
    Severity: may.
    Fix: split each into two numbered steps: "Buy an ISBN block from your
    agency." / "Record its prefix and size under
    `registrations.isbn-block`." and "Assemble the PCN fields:" / "Submit
    the fields through PrePub Book Link."

38. "The retail flag comes last, because it refuses every number that the
    earlier steps did not fill." (294)
    Rule: wrong term (the checker refuses the book; the flag refuses
    nothing). Severity: should.
    Fix: "The retail flag comes last, because once it is set, the checker
    refuses the book while any number is still absent or pending."

39. "A publisher with CIP data from the Library prints it as a block on the
    copyright page." (296)
    Rule: synonym rotation (see item 34). Severity: may.
    Fix: "A publisher with CIP data from the Library prints it as a block
    on the colophon page." If the book means the trade's copyright page as
    distinct from the colophon, define the term once at first use.

40. "The skill calls it "the one honest placeholder", and the press renders
    it as `[pending]`." (31)
    Rule: two ideas. Severity: may.
    Fix: "The skill calls it "the one honest placeholder". The press
    renders it as `[pending]`."

41. "You copy the values into the form yourself, which keeps the submission
    in your hands." (148)
    Rule: -ing rider (the trailing "which" clause does the same work).
    Severity: may.
    Fix: "You copy the values into the form yourself, so the submission
    stays in your hands."

42. "the press's own examples" (17), "the press's own example block" (54),
    "the press's own PCN listing" (130)
    Rule: rhythm (the phrase repeats). Severity: may.
    Fix: keep "own" at 17 and drop it at 54 and 130: "Example 13.2 shows
    the press's example block." "...as the press's PCN listing reminds
    you."

43. "PCN text" (248, `fig-alt`, and the art directive at 250) against "the
    PCN listing" (175, 177, 252)
    Rule: synonym rotation. Severity: may.
    Fix: "...the ONIX file, and the PCN listing." (alt text), and "PCN
    listing" for the box label in the art directive.

44. `press lookup lccn|issn [<number>]` (218) and
    `press config set registrations.lccn <number>` (279)
    Rule: code typography (replaceable text is constant width italic, not
    angle brackets; style guide 4). Severity: may.
    Fix: set *`number`* in constant width italic through the house filter,
    or keep the angle brackets only if they are press's verbatim synopsis
    and say so.

45. "A person buys a number from an agency." (25, Table 13.1)
    Rule: synonym rotation (the Who acts column says "You"). Severity:
    may.
    Fix: "You buy a number from an agency."

46. "`EA` is the EPUB." (198, Table 13.3)
    Rule: wrong term (the edition has a name). Severity: may.
    Fix: "`EA` is the Circulating edition (EPUB)."

47. "The press documentation states plainly where the numbers come from:"
    (46)
    Rule: hedge stack (an intensifier that adds nothing). Severity: may.
    Fix: "The press documentation states where the numbers come from:"

48. "Its synopsis is:" (215)
    Rule: rhythm (a three-word lead-in). Severity: may.
    Fix: "Its synopsis takes the catalog and an optional number:"
