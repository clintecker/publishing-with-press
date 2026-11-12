# Fact check: Chapter 13, Registrations

Chapter: `book/chapters/13-registrations.md`. Fact file:
`docs/briefs/facts/facts-13.md` (sections 11.1 to 11.8, 9.4, shared context,
19, 20). Nothing committed; no other file edited.

Status: **blocks** (2 contradicted, 7 unsupported). Most of the chapter checks
clean: the governing-rule quotation, the block rules and the `12 - log10(size)`
arithmetic (ten-digit prefix, two-digit publication number), both refusal
strings of `press isbn assign`, the `press isbn status` template, the ISSN
arithmetic (sum 160, remainder 6, check 5, which yields the selftest's valid
number), the LCCN pattern and its three normalizations, every row of Table
13.3 against 11.6, every row of Table 13.4 against 11.7, the lookup quotation,
both endpoints, the six outcomes, the User-Agent string, the no-price
quotation, the products rule, the order of operations (11.8), and the CIP
placement.

## Captured output

- **Example 13.3** (`press isbn status`, no block). The words match the
  capture character for character. The chapter adds a `$ press isbn status`
  prompt line, which the capture does not have, and breaks the line in three,
  which the prose discloses ("We broke the output line in two to fit the
  page"). See Drifted 2: the line is broken in *three*.
- **Example 13.5** (`press pcn`). Against the capture: the prompt line is
  added; line 2 and the Print ISBN line are broken (the two spaces before
  each parenthesis become a newline and a four-space indent), which the prose
  discloses; `demo` becomes `alice` twice (Title, `dist/alice-pcn.txt`), as
  ruled; the two closing lines are elided with `...`, and line 175 quotes them
  verbatim (the second quotation starts after `Obligations: `, which is a
  legitimate partial quote). The two `Clint Ecker` lines become
  `Lewis Carroll`. That is outside the ruling; my judgement is in Drifted 1.
  Every other character matches.

## 1. Unsupported (severity: blocks)

1. Line 136: "The rest of the message names the numbers at fault, and no
   artifact gets built until you fill them." The capture (11.4) ends at
   `pending: ...`; nothing says what follows. 11.4 says only that the numbers
   become "`press check` failures". Whether `press pdf` or other targets also
   stop is not in the file. Searched: "retail", "absent or pending",
   "artifact". Fix: "The rest of the message is not reproduced here, and
   `press check` fails until you fill the numbers."
2. Line 92: "Neither refusal changes the file." The file gives the two
   refusal strings (11.2) and nothing about the file's state. Fix: cut.
3. Line 115: "The number 123X-5678 carries its `X` in the body of the
   number, where only a digit may stand." The file says only that
   "`0378-5954` and `123X-5678` are not" valid (11.3); it gives no reason.
   (The reason for 0378-5954 is derivable from Example 13.4 and can stay.)
   Fix: "The number 123X-5678 is also invalid, and the checker refuses
   both."
4. Line 148: "prints them in the order the form asks for them". 11.5 says
   only that the target "assembles the fields for the Library of Congress
   PrePub Book Link form". Fix: "and prints them as a list".
5. Lines 238 and 241: "When the PCN comes back, she will run `press lookup
   lccn` with the new number before she stores it" and the tip "Give the
   number on the command line the first time. A lookup that finds the record
   confirms the number before `press config set` writes it into the book."
   The skill's order of operations (11.8) has no lookup step, and the file
   does not say that a newly assigned PCN number is in the catalog at
   `lccn.loc.gov` yet. A reader who follows the tip and gets `not-found` has
   been told to expect confirmation. Fix: line 238, "Once she holds one, she
   can run `press lookup lccn <number>`." Tip: "You can give a number on the
   command line before you store it. If the catalog holds a record for it,
   the lookup ends `found`."
6. Line 260: "The registrations skill gives the steps in a fixed order,
   because each step needs a number that the step before it produced." The
   file gives the order as "registrations skill, paraphrased" with no
   rationale, and the claim does not hold for every step: `press onix`
   (step 5) uses the ISBNs, not the LCCN from step 4. Line 294 already gives
   the two real dependencies. Fix: "The registrations skill gives the steps
   in this order."
7. Supported in sister fact files, absent from facts-13. The writer had only
   facts-13, so these are unsupported as briefed; each is right according to
   the file named, and the fix is to carry the line into facts-13, not to
   cut.
   - Line 134, "When it is `false`, the default": facts-03 field table,
     "`registrations.retail` | bool | false".
   - Line 141, "a box that reads `[ISBN pending]`", and line 256, "the cover
     wrap shows its placeholder box": facts-12, "With no ISBN: a 2in x 1.2in
     white box reading `[ISBN pending]`".
   - Line 150, "the scaffold uses the author as the publisher by default":
     facts-03 3.1, "`--publisher`: defaults to the author" (also Chapter 3,
     Table 3.1).
   - Line 207, "Its default binding is perfect-bound": facts-03, "`print.binding`
     | str | `perfect-bound`".
   - Line 256, "The colophon carries one line for each registration that the
     book declares": facts-13 9.4 says only "Registration numbers flow into
     the colophon"; Chapter 10, Table 10.4 (line 172), gives the line-per-number
     rule.
   - Footnote 13-isbn10, second sentence, "A ten-digit ISBN drops the leading
     978, and it has no way to write 979": true of ISBNs generally but not in
     any fact file; 11.2 says only that `isbn13_to_isbn10` "returns None for
     979". Keep only with the editor's sign-off, or cut to the first sentence.

## 2. Contradicted (severity: blocks)

1. **The Alice book's identity at Chapter 13.** Line 177: "The Alice book
   shows a different gap. Its subtitle still reads 'A subtitle', and its
   place of publication is still 'Earth', the scaffold's default." Also the
   caption of Example 13.5, "The PCN field values for the Alice book", and
   line 150, "The author and the publisher are both Lewis Carroll". By this
   chapter the Alice book has changed every one of these: Chapter 3 line 331
   (and Chapter 1 line 135) sets the title to "Alice's Adventures in
   Wonderland"; Chapter 10 Example 10.2 sets `publisher "Wonderland Press"`
   and `publisher-place "Oxford"`; Chapter 10 line 150 sets the subtitle "A
   Tale for Children; or, Alice's Adventures Under Ground". facts-10 S2
   fixes the sample's identity the same way ("publisher and place as the
   Chapter 10 writer set them (Wonderland Press, Oxford)"). facts-13 does
   not carry S2, but the brief names Chapter 3 as the authority on the
   sample, and the chapter contradicts the book. Example 13.5 is consistent
   only with a *fresh scaffold* (title = slug `alice`, subtitle "A subtitle",
   place "Earth", publisher = author), which line 150 half-says ("in a fresh
   copy of the Alice book"). Fix: make the fresh scaffold explicit and stop
   calling its placeholders the Alice book's. Caption: "Example 13.5. The PCN
   field values for a fresh Alice scaffold". Line 150: "Example 13.5 shows
   the target in a fresh scaffold made with `press new alice --author "Lewis
   Carroll"`, before the changes of Chapters 3 and 10. Its author and
   publisher are both Lewis Carroll, because the scaffold uses the author as
   the publisher by default." Line 177: "The fresh scaffold shows a different
   gap. Its title is the slug, its subtitle reads 'A subtitle', and its place
   of publication is 'Earth', the scaffold's default. All three are
   placeholders, and the Alice book replaced them in Chapters 3 and 10." (Keep
   the footnote.) Do not rewrite the block to show Wonderland Press and
   Oxford: that would be invented output.
2. **Line 256:** "Because every route starts at the same block, the copyright
   page cannot show an ISBN that the barcode or the EPUB does not carry." As
   worded it is false by the file's own routes (11.2): the barcode carries
   only the print ISBN and the EPUB identifier only the EPUB ISBN, so the
   copyright page, which shows both, always shows an ISBN that one of them
   does not carry. (Chapter 10 line 182 has the safe form: "an ISBN that the
   EPUB does not carry".) Fix: "Because every route starts at the same block,
   the copyright page cannot show a print ISBN that differs from the
   barcode's, or an EPUB ISBN that differs from the EPUB's identifier."

## 3. Drifted (severity: should)

1. **Example 13.5, `Clint Ecker` to `Lewis Carroll`.** Outside the ruling
   (slug only). My judgement: the substitution is acceptable in substance and
   should stand, provided Contradicted 1 is fixed. The chapter does not
   present the block as the press's verbatim capture; it presents it as what
   alice's run prints ("shows the target in a fresh copy of the Alice
   book", with her prompt line). The Author(s) and Publisher name values are
   not press text but echoes of the book's metadata, and a scaffold made the
   way Chapter 3 makes it (`--author "Lewis Carroll"`, publisher defaulting
   to the author) would print Lewis Carroll in both. Keeping `Clint Ecker`
   would assert that Alice's author is the maintainer, contradicting Chapter
   3 and the scaffold-neutrality rule (shared context 1.4: a scaffolded book
   contains no "Clint Ecker"). The press text, the field labels, the column
   alignment, and every other value are unchanged. Two conditions: the editor
   should record the substitution as a ruling, as was done for the slug; and
   the lead-in should say that the field values are the book's own, e.g. add
   to line 150, "The values come from the book's metadata; the labels and the
   layout are the press's." If the editor rules the other way, the only
   correct alternative is to cut the two lines with `...`, not to restore the
   maintainer's name.
2. **Line 77:** "We broke the output line in two to fit the page." Example
   13.3 breaks it into three lines. Fix: "We broke the output line to fit the
   page." Also, both Example 13.3 and Example 13.5 add a `$` prompt line that
   the capture lacks (the Chapter 8 check flagged the same thing). Acceptable
   as session framing, but the lead-ins should not imply a raw capture.
3. **Line 65:** "The size is a power of ten ... although the code accepts any
   power from 10 through 1,000,000." 11.2: "The code accepts 10 through
   1,000,000." The file does not say "power". The digit rule implies it, but
   the chapter states it as fact. Fix: "The documentation lists 10, 100, and
   1000, and the code accepts sizes from 10 through 1,000,000."
4. **Line 90:** "A number that the model would refuse never reaches the
   file." 11.2 says only that the target "writes `registrations.isbn.<edition>`
   through the validated `press config` path". Fix: "The target writes the
   number ... through the validated path of `press config`, the same check
   that any `press config set` passes."
5. **Line 189 and Table 13.3:** "Table 13.3 lists the elements that the press
   writes". It omits `ProductComposition 00` and the title (`TitleType 01`)
   from 11.6 (and, correctly, `NotificationType 03`, per 20.B.20). Fix:
   "lists the main elements". See Missing 1.
6. **Table 13.3, `SentDateTime`:** "The time of the build, to the minute."
   The file gives only the format, `YYYYMMDDTHHMM`; `press onix` is not a
   build. Fix: "A date and time, to the minute."
7. **Table 13.1, Issuance:** "No press target does this, and none can." The
   file says "The press never issues a number over the network" and, for
   ISBNs only, "there is no API that issues ISBNs". Fix: "No press target
   does this."
8. **Line 49:** "it names the Bowker 10-pack as the place to start". 11.2:
   "The skill says to buy the Bowker 10-pack". Fix: "and it names the Bowker
   10-pack".
9. **Sidebar, line 141:** "it cannot go on sale before they arrive". The flag
   makes `press check` fail; the press cannot stop a sale. Fix: "and it cannot
   pass the checker as a retail edition before they arrive."
10. **Line 209:** "A distributor that receives the Alice book's record today
   sees a print product and no EPUB product." True for a book with no
   registrations (line 17), but Example 13.1 shows the book with `epub:
   pending`, and the file does not say whether `pending` counts as "an EPUB
   ISBN exists" (11.6). Fix: "...receives the record of a book with no EPUB
   ISBN sees a print product and no EPUB product."

## 4. Missing (severity: may)

1. **The rest of the ONIX product (11.6).** `ProductComposition 00` and the
   title, `TitleType 01`, are written for every product and absent from Table
   13.3. A reader checking a record against the table will find a title the
   table never mentions. Two rows would do. Leave `NotificationType 03` out
   (20.B.20).

## Notes on the writer's decisions

- ISSN "check = 11 - 6": the file gives only "mod 11, weights 8 to 2, 10
  written X". The arithmetic is correct and reproduces the selftest's valid
  number, so it stands; I do not count it.
- ISBN minting from publication number 0 (20.B.20) is correctly avoided
  ("lowest unused").
- The writer's "not found, left out" list is accurate; none of those gaps is
  papered over in the chapter except the ones listed above.
