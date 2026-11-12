# STE80 editor report: Chapter 5, Figures, plates, and illustrations

File: `book/chapters/05-figures-and-plates.md`

## Counts

- Ratchet count before: 3 (baseline in `tools/ste-baseline.json`: 3)
- Ratchet count after: 2
- `press check`: passed (source, checker self-test, editorial, jargon)
- Edits: 19 numbered edits (17 sentence rewrites; edits 2 and 11 are
  paragraph splits with no words changed; 3 more splits ride on edits 5, 13, 18)

No sentinel phrase occurs in this file. No index term was reworded away:
every touched sentence keeps its terms (aesthetic, *config/aesthetic.yaml*,
leaf, cleared leaf, recto, measure, design profile, List of Plates, List
of Figures, Manuscript edition, arm64, Apple Silicon, logomark). No fence,
code span, quotation, heading, image line, art comment, or fig-alt was
touched. All edits are ASCII, no dashes, no semicolons.

## Edits

Line numbers are in the edited file.

1. L18, S1/S2 (three ideas, 28 words).
   Old: "The checker refuses an image line, a citation prints as a raw `@fig:` in the proof, or a plate changes sides when a chapter grows by a page."
   New: "The checker refuses an image line, or a citation prints as a raw `@fig:` in the proof. A plate can also change sides when a chapter grows by a page."
2. L18 to L20, S13 (paragraph grew to nine sentences; split at the turn
   from the cost of a slip to the chapter overview). No words changed.
3. L20, S1/S2 (four-part list, 28 words).
   Old: "This chapter shows how to type an illustration, how press numbers and lists it, where it sits on the printed page, and what each edition does with it."
   New: "This chapter shows how to type an illustration and how press numbers and lists it. It then shows where an illustration sits on the printed page and what each edition does with it."
4. L20, S2 (29 words).
   Old: "The examples use the Alice book, the full novel that user `alice` keeps on the workstation `hatter`, and none of them comes from the press's own three-chapter Alice example."
   New: "The examples use the Alice book, the full novel that user `alice` keeps on the workstation `hatter`. None of them comes from the press's own three-chapter Alice example."
5. L63, S1 (three clauses, 26 words), with S13 split (paragraph would
   reach seven sentences; split at the turn from the rule to the failure).
   Old: "Press reads a comment on the very next line too, but that comment joins the image's paragraph, and pandoc then makes no figure of the image."
   New: "Press reads a comment on the very next line too. But that comment joins the image's paragraph, and pandoc then makes no figure of the image."
6. L81, S2 (30 words, ratchet-independent ste_check lead).
   Old: "Press takes the style from the `--style` option first, then from the illustration's own `style=` attribute, then from `plates.style` in the *aesthetic*, the book's visual identity in *config/aesthetic.yaml*."
   New: "Press takes the style from the `--style` option first, then from the illustration's own `style=` attribute. Third comes `plates.style` in the *aesthetic*, the book's visual identity in *config/aesthetic.yaml*."
7. L118, S1 (three clauses).
   Old: "It is the first figure in that chapter, so press numbers it Figure 5.1, and the citation prints as "Figure 5.1" with a link to the figure."
   New: "It is the first figure in that chapter, so press numbers it Figure 5.1. The citation prints as "Figure 5.1" with a link to the figure."
8. L153, S1/S2 (two definitions, 27 words).
   Old: "A *leaf* is one sheet of the book, two pages back to back, and a *cleared leaf* is a fresh page that holds nothing but the illustration."
   New: "A *leaf* is one sheet of the book, two pages back to back. A *cleared leaf* is a fresh page that holds nothing but the illustration."
9. L175, S1/S2 (26 words).
   Old: "A printed book has two kinds of page: a *recto* is a right-hand page with an odd number, and its spine edge is on the left."
   New: "A printed book has two kinds of page. A *recto* is a right-hand page with an odd number, and its spine edge is on the left."
10. L205, S1/S2 (29 words, two facts plus a definition).
    Old: "Press knows three, `full-measure`, `half-measure`, and `third-measure`, and a measure applies only to an in-flow placement, one that sits among the lines of text: `inline`, `wrap-inner`, `wrap-outer`, and `margin`."
    New: "Press knows three: `full-measure`, `half-measure`, and `third-measure`. A measure applies only to an in-flow placement, one that sits among the lines of text: `inline`, `wrap-inner`, `wrap-outer`, and `margin`."
11. L205 to L207, S13 (the ratchet then counted eight sentences; split at
    the turn from what a measure is to what the checker refuses). No words
    changed.
12. L221, S1/S2 (26 words).
    Old: "Each *design profile* is a sealed page geometry, a trim with its own margins and line, and the line is a different length in each profile."
    New: "Each *design profile* is a sealed page geometry, a trim with its own margins and line. The line is a different length in each profile."
13. L276, S2 (ratchet lead, 30 words), with S13 split of the old
    six-sentence paragraph into three: number labels, link forms, plates.
    Old: "The link changes form from one edition to the next: in the PDF, the citation links to the figure, and the figure has an entry in the List of Figures."
    New: "The link changes form from one edition to the next. In the PDF, the citation links to the figure, and the figure has an entry in the List of Figures."
14. L278, S2 (ratchet lead, 31 words as counted: the counter joins the
    sentence to the following `@fig:` sentence).
    Old: "A plate gets no number anywhere, and in the PDF its entry goes into the List of Plates."
    New: "A plate gets no number anywhere. In the PDF its entry goes into the List of Plates."
15. L284, S1/S2 (27 words).
    Old: "Its image lines appear as you typed them, with their attributes and their `art:` comments, so that edition publishes every directive verbatim, for any reader to see."
    New: "Its image lines appear as you typed them, with their attributes and their `art:` comments. That edition therefore publishes every directive verbatim, for any reader to see."
16. L298, S2 (27 words).
    Old: "A wide, shallow image meets the line before it meets the cap, so it prints at the full width of the line and well under the cap."
    New: "A wide, shallow image meets the line before it meets the cap. It prints at the full width of the line and well under the cap."
17. L328, S2 (28 words).
    Old: "This book keeps its numbered figures in *assets/woodcuts/* as well, and you should do the same with every interior image, for a reason the section "Print-safe images" gives."
    New: "This book keeps its numbered figures in *assets/woodcuts/* as well. You should do the same with every interior image, for a reason the section "Print-safe images" gives."
18. L354, S1 (three clauses), with S13 split (paragraph would reach seven
    sentences; split at "Outside the image", the turn from the toolchain
    image to the host).
    Old: "The arm64 image has no upstream binary, so it resamples and quantizes without the upscale, and resampling only ever goes down."
    New: "The arm64 image has no upstream binary, so it resamples and quantizes without the upscale. Resampling only ever goes down."
19. L379, S2/S3 (31 words, a parenthesis inside the condition).
    Old: "If the book supplies its own *tex/title-page-print.tex* (a hand-written title page for the print interior only, which Chapter 10 describes), the logomark in it must come from *build/print-assets/*, not from *assets/*."
    New: "A book can supply its own *tex/title-page-print.tex*, a hand-written title page for the print interior only, which Chapter 10 describes. If it does, the logomark in that file must come from *build/print-assets/*, not from *assets/*."

## Leads declined

- L272 (ratchet line 264), passive "is print": "Placement is print-only" is a predicate
  adjective, not a passive. The heuristic is wrong.
- L315 (ratchet line 306), paragraph length (10 sentences): the sidebar "The infinite empty
  pages". Light mode: it is a war story, every sentence is under 30 words
  with one idea, it holds no semicolon, and it runs about 135 words, under
  the 190 ceiling. Merging or cutting sentences would cost the voice.
- ste_check leads not in the ratchet, declined:
  - Lines 6, 167, 223, 272 (and the 34-word and -ing findings near
    them): the in-this-chapter box, art comments, and fig-alt text, which
    the brief puts out of reach.
  - "therefore", "whether", "however": the contract relaxes them.
  - "-ing" at the Example 5.5 caption ("Commissioning") and the next
    chapter's title ("Checking the manuscript"): a caption label and a
    title, not -ing riders.
- L272 (Circulating edition list, about 31 raw words): one idea, a list
  of edition names with their formats. Splitting it would break the list.
- L266 ("A map that the reader must study wants the full measure and an
  `inline` placement, so nothing competes with it for the width of the
  page."): 25 words by STE counting, and the "so" clause is the reason.
- L71 refusal list ("Press refuses in three cases: ..."): three
  conditions, but at about 25 words and in running reasoning; S5 says not
  to chop reasoning into bullets.
- Footnote [^5-square] (27 raw words): 22 by STE counting (1024 by 1024
  pixels is one number with its unit). Left alone.

## Passives kept

None found in prose by the ratchet or by a scan for be-plus-participle.
Participial modifiers ("called the *guard*", "set with `wrap-inner`") are
not finite passives and stay.

## Fidelity notes

- Edit 1: the original listed three possible costs joined by "or". The
  new second sentence says a plate "can also change sides", which keeps
  the possibility at its strength rather than asserting it always happens.
- Edit 6: "then from" became "Third comes", matching the existing "Last
  comes" so the precedence order (option, attribute, aesthetic, house) is
  unchanged.
- Edit 19: "If the book supplies" became "A book can supply ... If it
  does"; the condition still comes before the requirement, and the
  parenthetical gloss is kept word for word as an appositive.
