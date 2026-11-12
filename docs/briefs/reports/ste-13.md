# STE80 desk report: Chapter 13, Registrations

File: `book/chapters/13-registrations.md`

## Ratchet count

- Before: 4 (baseline in `tools/ste-baseline.json`: 4)
- After: 0

`press check` passes (exit 0) after the edits.

## Edits

Line numbers are in the edited file.

1. Line 17/19, S13 (paragraph split at the turn of topic; my edit 2 had raised the opening paragraph to seven sentences). The paragraph now breaks after "and a serial carries an ISSN." The first paragraph names the numbers. The second says what the press does with them.
2. Line 19, S1. Old: "It checks the numbers you give it, writes them into every artifact that needs them, and assembles the fields that each agency's form asks for." New: "It checks the numbers you give it and writes them into every artifact that needs them. It also assembles the fields that each agency's form asks for."
3. Line 94/96, S13 (ratchet lead, 7 sentences). Split the `press isbn assign` paragraph before "The press knows only the two ISBNs in this repository." The several-titles register is a separate topic. Sentences unchanged.
4. Line 106, S1. Old: "The press tests an ISSN with a mod-11 check, and Example 13.4 works the number that the press's selftest uses as its valid case, 0378-5955." New: "The press tests an ISSN with a mod-11 check. Example 13.4 works the number that the press's selftest uses as its valid case, 0378-5955."
5. Line 169, S7 (ratchet lead, perfect tense). Old: "The scaffold predates the changes of Chapters 3 and 10, and you have set no registration yet." New: "The scaffold predates the changes of Chapters 3 and 10, and it holds no registration yet."
6. Line 196/198, S13 (seven sentences that the ratchet missed because of the footnote marker). Split before "The fresh scaffold shows a different gap." The paragraph about the `(needed on the form)` gap is now separate from the paragraph about the scaffold placeholders. Sentences unchanged.
7. Line 284/286, S13 (ratchet lead, 7 sentences). Split before "The barcode carries only the print ISBN". The copyright-page lines are now separate from the one-block consistency guarantee. Sentences unchanged.
8. Line 328, S2 + S6 (26 words, passive). Old: "Once it is set, the checker refuses the book while either ISBN is absent or pending, or while a declared LCCN or ISSN is still pending." New: "Once you set it, the checker refuses the book while either ISBN is absent or pending. The checker also refuses the book while a declared LCCN or ISSN is still pending."

## Leads declined

- Sidebar "Why pending is a word" (ratchet lead, 11 sentences in one blockquote). The sidebar is in Light mode. No sentence in it is over 30 words, has three ideas, or uses a semicolon. It is already two Markdown paragraphs inside the blockquote, and it runs under 190 words. To cut the sentence count, I would have to merge short sentences, which costs the sidebar its voice. `tools/ste-ratchet.py` changed at 09:59 during this desk's run, and it now unwraps blockquotes. It counts the sidebar as its two inner paragraphs (five and six sentences), so the final run does not flag this lead. I did not edit the sidebar.
- `ste_check.py` semicolon, passive, and modal-passive hits on the lines that start "An ISBN identifies", "The two omitted lines matter", and "The documentation describes it as". Each hit is inside a double-quoted quotation from press or its documentation. Quotations are never edited.
- `-ing` hits on "Cataloging in Publication" (a program name) and on the headings "Looking numbers up" and *Verifying the artifacts* (a heading and a chapter title). Not edited.
- The passive "are stated" in "Facts are stated once." It is a quotation of press's first law. Not edited.
- The 45-word fig-alt sentence and its passive "is labeled". This is the alt-text attribute on an image line, which the ratchet excludes. It lists the five destinations, and it sits next to a figure identifier. Not edited.
- "looks up" (phrasal verb, lookup section). The term is the section's subject and the target's own word ("lookup"). Changing it to "queries" would break the one term per thing rule.

## Passives kept

None in body prose. "made with" (line 169) and "is not open to" (CIP) are a participle and a predicate adjective, not passive verbs.

## Fidelity notes

- Sentinels: none of the three sentinel phrases occur in this file.
- Index terms: no edit removed or respelled a word. Every edit only splits or re-voices an existing sentence.
- Edit 5 changes the actor from "you" to the scaffold ("it holds no registration yet"). The fact (the scaffold has no registration set) is the same.
- Edit 8 changes "Once it is set" to "Once you set it". The actor was implicit, and the reader sets the flag in step 8.
