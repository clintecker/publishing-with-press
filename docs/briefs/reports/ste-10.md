# STE80 editor report: Chapter 10

File: `book/chapters/10-front-matter-index-authorities.md`

Ratchet count: 3 before (baseline 3), 1 after. `press check` passes.

## Edits

Line numbers are those of the edited file.

1. Line 39, S1 (two ideas) and S3 (condition first), 34 words.
   Old: It says that the file's presence asks the press "to generate the PDF's title page, colophon, and surrounding pages from config", and that you opt out if you delete the file or supply *tex/title-page.tex*.
   New: It says that the file's presence asks the press "to generate the PDF's title page, colophon, and surrounding pages from config". If you delete the file or supply *tex/title-page.tex*, you opt out.
2. Line 39, S1 (two ideas), 31 words.
   Old: It adds that "absent sections simply do not render", and that the identity facts "come from metadata.yaml and are never restated here."
   New: It adds that "absent sections simply do not render". It also says that the identity facts "come from metadata.yaml and are never restated here."
3. Line 39 (now split into two paragraphs), S13 (paragraph of seven sentences after edits 1 and 2). Split the paragraph at its turn of topic, from what the opening comment says to what Example 10.1 shows. No words changed.
4. Line 87, S8 (-ing chain).
   Old: Example 10.2 shows user `alice` replacing the scaffold's placeholder identity facts and filling in the Alice front matter in one sitting.
   New: In Example 10.2, user `alice` replaces the scaffold's placeholder identity facts and fills in the Alice front matter in one sitting.
5. Line 164, ratchet lead (37 words). The footnote marker after "page." glued two sentences together for the counter. Moved `[^10-colophon]` to follow the word it glosses. Label and footnote text unchanged.
   Old: The press calls the page after the title page the *colophon*, although most readers know it as the copyright page.[^10-colophon] It holds ...
   New: The press calls the page after the title page the *colophon*,[^10-colophon] although most readers know it as the copyright page. It holds ...
6. Line 184, S1 and S2 (29 words, a "which" clause carrying a second idea).
   Old: Chapter 13, *Registrations*, covers the numbers themselves and the `retail` switch, under which a missing or pending ISBN, or a declared LCCN or ISSN still pending, fails the build.
   New: Chapter 13, *Registrations*, covers the numbers themselves and the `retail` switch. Under that switch, a missing or pending ISBN fails the build, and so does a declared LCCN or ISSN still pending.
7. Line 192, S1 (28 words, two facts).
   Old: The List of Plates and the List of Figures come next, and the house TeX header sets each one only when the book has plates or numbered figures.
   New: The List of Plates and the List of Figures come next. The house TeX header sets each one only when the book has plates or numbered figures.
8. Line 196, S8 (action in a noun).
   Old: Table 10.5 gives the decision the press makes on each build of the reading PDF.
   New: Table 10.5 shows what the press decides on each build of the reading PDF.
9. Line 277, ratchet lead, S1 and S2 (30 words, two ideas).
   Old: A revision that cuts the last mention of a term leaves it in this state, and the zero-hit rule turns the cut into a refusal you see at your desk.[^10-silence]
   New: A revision that cuts the last mention of a term leaves it in this state. The zero-hit rule turns the cut into a refusal you see at your desk.[^10-silence]
10. Line 296, S3 (condition first) and S2 (27 words).
    Old: An entry for the Mock Turtle in the Alice book reads its two chapter numbers, 9 and 10, if the creature appears in only those two chapters.
    New: If the Mock Turtle appears in only two chapters of the Alice book, 9 and 10, its entry reads those two chapter numbers.

## Leads declined

- Line 303, perfect-tense "has fixed": a false positive. "fixed" is an adjective ("has fixed pages"), not a perfect tense. The sentence is in a sidebar (light mode) and is 18 words.
- Line 83 (30 words): a list of nine characters the press escapes. A split would break the list.
- Line 225 (30 words with quote): most of its length is a verbatim message in double quotes.
- Lines 20, 298, 310, 382: counted long only because a quotation sits inside them. Quotations are never touched.
- Line 303 sidebar, "The cost is precision: ..." (30 words): at the ceiling, not over it, and a sidebar is light mode.
- Lines 211, 265, 290, 296 (25 words each): at the description target, one idea each or a parallel either/or, and a split would break the meaning.

## Passives kept

None added or kept beyond participial modifiers ("an appendix built from", "grouped by where each claim sits"), which are not finite passives. Every edited sentence names its actor.
