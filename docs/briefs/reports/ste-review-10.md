# STE80 review: Chapter 10

File: `book/chapters/10-front-matter-index-authorities.md`
Diff: `git diff HEAD` (10 edits, all hunks read). `press check` passes on the
edited tree. No sentinel, code span, path, key, quotation, or index term
changed. No paragraph passes 190 words (the split paragraph at line 39 is now
two short ones).

Status: REVISE. Blocks: 1. Should: 1.

## Findings

1. **Line 39, edit 1. Attribution dropped; the claim now contradicts Table 10.5.** Severity: blocks (facts).
   - Old: It says that the file's presence asks the press "to generate the PDF's title page, colophon, and surrounding pages from config", and that you opt out if you delete the file or supply *tex/title-page.tex*.
   - New: It says that the file's presence asks the press "to generate the PDF's title page, colophon, and surrounding pages from config". If you delete the file or supply *tex/title-page.tex*, you opt out.
   - What went wrong: in the old sentence, the opt-out was reported speech. It was what the scaffold's comment says (facts-10, the verbatim comment: "delete it, or supply tex/title-page.tex, to opt out"). The split makes the narrator state it as fact, with no condition. The chapter itself says otherwise. Table 10.5 and the sentence after it say that *assets/cover.jpg* still makes the press generate the front matter for the reading PDF when *config/front-matter.yaml* is deleted. So the fact is now stronger than the source, and it conflicts with line 198 onward. Edit 2 kept its attribution ("It also says that..."), and edit 1 must do the same.
   - Corrected: It says that the file's presence asks the press "to generate the PDF's title page, colophon, and surrounding pages from config". It also says that you opt out if you delete the file or supply *tex/title-page.tex*.
     (Edit 2 then needs a new opening so that two sentences do not both start with "It also says". Use "It adds that "absent sections simply do not render", and that the identity facts ..." as the old text had it, or "The comment adds that ...". Either keeps the attribution.)

2. **Line 296, edit 10 (Mock Turtle). The reorder keeps the facts but puts the appositive in the wrong place.** Severity: should (voice/clarity).
   - Old: An entry for the Mock Turtle in the Alice book reads its two chapter numbers, 9 and 10, if the creature appears in only those two chapters.
   - New: If the Mock Turtle appears in only two chapters of the Alice book, 9 and 10, its entry reads those two chapter numbers.
   - Fidelity check: the condition survives, and so does its hedge ("only"). The numbers 9 and 10 survive. The outcome is the same: the entry reads 9 and 10. Nothing is added or lost, and "Mock Turtle" still gets its index hit.
   - What went wrong: "9 and 10" now comes right after "the Alice book", so on a first read it can attach to the book and not to "two chapters". The example also no longer names the locators in its result clause, and the result clause is the point of the paragraph (what a locator reads). The fix is a small reorder, with no change of content.
   - Corrected: If the Mock Turtle appears only in chapters 9 and 10 of the Alice book, its entry reads those two chapter numbers.

## Passed (no finding)

- Edit 2, line 39: the attribution is kept ("It also says"). Quotes are verbatim.
- Edit 3, line 39: the paragraph split is at a real turn of topic, from the comment to Example 10.1. No words changed.
- Edit 4, line 87: the same facts ("in one sitting" is kept).
- Edit 5, line 164 (footnote marker): approved. `[^10-colophon]` glosses the *word* "colophon", meaning its origin as a printer's note at the end of a book and the press keeping the old name. The marker now sits on that word, not on the end of a sentence about the copyright page, so the attachment is better than before. The marker follows the comma, which is correct note placement. The label and the note text at line 420 are unchanged, and `press check` accepts it.
- Edit 6, line 184: the retail failure set is the same (a missing or pending ISBN, and a declared LCCN or ISSN still pending), and "Under that switch" keeps the scope of "under which".
- Edit 7, line 192: a clean split, and "only when" is kept.
- Edit 8, line 196: "shows what the press decides" carries the same meaning.
- Edit 9, line 277: a clean split, and the `[^10-silence]` marker still ends the sentence about the refusal it glosses.
