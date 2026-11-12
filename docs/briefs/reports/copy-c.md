# Copyedit: Appendix C, Messages and refusals

File: `book/appendices/c-messages.md`

## Status

REVISE. Two blocks, both watchlist sightings that are not press's own
names ("lands" at 259, "from clean" at 256). `press check` passes the
whole book as it stands (self-test, style audit, and jargon lint all
green), and the jargon audit names no term in this file. The blocks follow
the Chapter 15 precedent: `jargon-allow` lets "lands" and "clean" through,
but neither is press's name for anything here, and the contract puts the
watchlist on the one-sighting list.

Counts by severity: blocks 2, should 24, may 14, fact 0.

Most frequent rules broken: wrong term (18 items, counting the two
watchlist blocks, four edition names without their gloss, and three
"witness" for "witness line" or "the companion" for "the sources
companion"), hidden actor (8), two ideas (4 as the main rule, 7 counting
items where it rides beside another). Procedure mixed into description in
a Remedy paragraph follows with 2.

The definition-list form (message, **Cause.**, **Remedy.**) is the
appendix's design and is not counted as bold labels on list items. Quoted
messages are not touched: "honest" (327), the double hyphens (293, 298),
and the semicolons inside messages (268, 357, 362, 367, 372) are press's
own text.

Line numbers are `cat -n` line numbers in the file as it stands.

## The ste_check findings, judged

ste_check reports 5 findings (328 sentences, average 6.0 words, max 37).

- Semicolon and sentence length at 462: accepted. It is the index
  comment. No prose sentence passes 30 words, and no prose sentence holds
  a semicolon.
- `-ing` form at 11 ("Checking"): accepted. It is the title of Chapter 6.
- "verify" (5) and "therefore" (5): accepted under the 80 percent rule.
  "verify" names the verifier family. Line 5 has a real finding on other
  grounds (item 5).

Also accepted on reading:

- Line 3, "This appendix lists the messages by the command that prints
  them": accepted. An appendix stating its own arrangement in its opening
  paragraph is the era's reference convention, and it is not narration of
  the text in progress.
- "As for the message before it." (211, 261, 301, 355) and "As for the PDF
  sentinel message." (335): accepted as the reference-entry cross-reference
  form, used consistently.
- "Report it to the press." (206, 266, 296, 365, 439): "the press" as the
  institution, per the vocabulary.
- "reader site" (392 to 400) beside "the Chapter edition": accepted. The
  vocabulary glosses the Chapter edition as the reader site and its zip.
- "pandoc output" (315): ordinary English for what pandoc prints, not the
  forbidden "output" for an edition or artifact.
- Second person and present tense hold, no "we", no "I". No admonitions.
  The one footnote (460) carries an aside the body does not need. No dry
  understatement appears, which is fine for a reference appendix. American
  spelling throughout except item 3.

## Findings

1. "A list link lands on a page without the image, often the caption's
   page." (259) Rule: wrong term (watchlist "lands", on the one-sighting
   list). Severity: block. Fix: "A list link points at a page without the
   image, often the caption's page."

2. "Rebuild from clean with `press clean` and `press verify`." (256) Rule:
   wrong term (watchlist "clean"; the target is press's name, the idiom
   "from clean" is not). Severity: block. Fix: "Run `press clean`, then
   rebuild with `press verify`."

3. "Each diagnostic follows the file name and the line number." (73) Rule:
   era spelling. Severity: should. Fix: "Each diagnostic follows the
   filename and the line number."

4. "The third pass reads every audited file, the manuscript and any audit
   directories." (73) Rule: two ideas (the appositive reads as a list of
   three). Severity: should. Fix: "The third pass reads every audited
   file: the manuscript and the files in any audit directory."

5. "A check or verify failure exits with status 1." (5) Rule: hidden actor
   (a failure does not exit; press does), and noun stack. Severity:
   should. Fix: "When a check or a verifier fails, press exits with status
   1."

6. "A failing external tool, such as `pandoc` or `latexmk`, passes its own
   exit status through press." (5) Rule: hidden actor. Severity: may. Fix:
   "When an external tool such as `pandoc` or `latexmk` fails, press exits
   with that tool's status."

7. "The values press fills in will differ from the ones you see on your
   terminal." (7) Rule: wrong term (press fills in both sets; the contrast
   is this appendix against your terminal). Severity: may. Fix: "The
   values on your terminal will differ from the values in this appendix."

8. "Avoid the first words of a chapter, because the drop cap splits the
   first word in the PDF." (45) Rule: wrong term (no profile sets a drop
   cap by default, per Chapter 9, so "the" presumes one). Severity:
   should. Fix: "Avoid the first words of a chapter, because a drop cap
   splits the first word in the PDF."

9. "If the label is right, the pattern itself no longer matches the
   fixture." (54) Rule: procedure apart from description (the Remedy ends
   on a diagnosis, not a command). Severity: should. Fix: "If the label is
   right, the pattern no longer matches the fixture. Fix the pattern."

10. "Make the fixture break the rule it was written for, or add the rule a
    book pattern should enforce." (59) Rule: hidden actor ("was written");
    the second clause does not say what to add or where. Severity: should.
    Fix: "Make the fixture break the rule you wrote it for, or add a
    banned pattern for that rule to *config/house-rules.yaml*."

11. "On a fresh scaffold the dash fixtures also draw the glyph law, and the
    pass reports "2 extra diagnostics noted"." (67) Rule: wrong term (a
    fixture draws a diagnostic, not a law). Severity: may. Fix: "On a
    fresh scaffold the dash fixtures also trip the glyph law, and the pass
    reports "2 extra diagnostics noted"."

12. "Two hyphens pass the audit, but pandoc prints them as a dash, so
    rewrite those as well." (78) Rule: two ideas (fact, cause, and command
    in one sentence). Severity: should. Fix: "Two hyphens pass the audit,
    but pandoc prints them as a dash. Rewrite them as well."

13. "Book prose holds a character outside the glyph law: tab, line feed,
    ..." (126) Rule: wrong term (the law is a rule; the list is the set it
    allows). Severity: may. Fix: "Book prose holds a character outside the
    set the glyph law allows: tab, line feed, carriage return, U+0020 to
    U+007E, and U+00C0 to U+017F."

14. "A line that matches one of the book's banned patterns prints the label
    from *config/house-rules.yaml* in place of a packaged diagnostic."
    (145) Rule: hidden actor (press prints, not the line). Severity:
    should. Fix: "When a line matches one of the book's banned patterns,
    press prints the label from *config/house-rules.yaml* in place of a
    packaged diagnostic."

15. "A finding prints in three lines: ..." (150) Rule: hidden actor.
    Severity: may. Fix: "Press prints each finding in three lines: the
    location, status, term, and category, then the line of context, then
    a question."

16. "`press verify` rebuilds the Print edition and runs the PDF verifier
    over it." (191) Rule: wrong term (edition name not glossed with its
    format on first use, as the vocabulary requires once per chapter).
    Severity: should. Fix: "`press verify` rebuilds the Print edition (the
    PDF) and runs the PDF verifier over it."

17. "The Single-leaf edition lacks a sentinel." (333) Rule: wrong term
    (gloss missing). Severity: should. Fix: "The Single-leaf edition (the
    self-contained HTML) lacks a sentinel."

18. "The Office edition lost plates." (383) Rule: wrong term (gloss
    missing). Severity: should. Fix: "The Office edition (DOCX) lost
    plates."

19. "The Chapter edition has no index page." (388) Rule: wrong term (gloss
    missing). Severity: should. Fix: "The Chapter edition (the reader site
    and its zip) has no index page."

20. "The verifier tests its own blank-page detector before it trusts it,
    and the detector called a blank test image inked." (204) Rule: two
    ideas (the general practice and this failure). Severity: should. Fix:
    "The verifier tests its own blank-page detector before it trusts it.
    Here the detector called a blank test image inked."

21. "The fault lies in the press or its image library, not in the book."
    (206) Rule: rhythm (a contrastive tail; not the one-sighting "not X but
    Y" form, but the same cadence). Severity: may. Fix: "The book is not at
    fault. The fault lies in the press or its image library."

22. "The match is exact in case, with straight and curly quotes equal."
    (234) Rule: rhythm (compressed to the point of strain). Severity: may.
    Fix: "The match is case-sensitive, and straight and curly quotes count
    as equal."

23. "Check that the phrase does not open a chapter, where the drop cap
    splits it, and that a line break has not hyphenated a word in it."
    (236) Rule: perfect tense, two ideas, and the article of item 8.
    Severity: should. Fix: "Check that the phrase does not open a chapter,
    where a drop cap splits it. Then check that no word in it breaks with
    a hyphen at the end of a line."

24. "The `pypdf` package does not import. This is a note, and press skipped
    the link checks." (269) Rule: hidden actor (who imports), and a tense
    shift to the past. Severity: should. Fix: "Python cannot import the
    `pypdf` package. Press prints this note and skips the link checks."

25. "Report it to the press with the PDF. The press's own generated front
    matter places the cover, so the fault is the press's." (296) Rule:
    rhythm ("the press's" twice in one sentence, three times in two).
    Severity: may. Fix: "Report it to the press with the PDF. The press
    generates the front matter that places the cover, so the fault is in
    the press."

26. "`pdfimages`, part of poppler, is not installed, so the check softened
    to a note." (304) Rule: hidden actor, and a tense shift to the past.
    Severity: should. Fix: "`pdfimages`, part of poppler, is not
    installed, so press reports a note in place of a failure."

27. "Each edition must carry the title, every sentinel, and the manuscript
    witness." (310) Rule: wrong term (the vocabulary's witness is "the
    manuscript witness line", which the message at 322 also uses).
    Severity: should. Fix: "Each edition must carry the title, every
    sentinel, and the manuscript witness line."

28. "Find where the edition breaks that line, often a filter or a
    stylesheet." (325) Rule: wrong term ("where" answered by a "what").
    Severity: should. Fix: "Find what breaks that line in the edition,
    often a filter or a stylesheet."

29. "The edition numbered a different count of figures than the manuscript
    declares." (343) Rule: noun stack ("a different count of figures") and
    a tense shift. Severity: may. Fix: "The edition numbers more or fewer
    figures than the manuscript declares."

30. "`PRESS_TOOLCHAIN` is set, and no epubcheck is found." (363) Rule:
    hidden actor. Severity: should. Fix: "`PRESS_TOOLCHAIN` is set, and
    press finds no epubcheck."

31. "The command exists and fails to start, the binfmt scar Appendix D
    describes." (373) Rule: two ideas (a dangling appositive carries the
    second). Severity: should. Fix: "The command exists but fails to
    start. This is the binfmt scar that Appendix D describes."

32. "No page of the reader site carries the chapter's witness." (393) Rule:
    wrong term (the vocabulary's "chapter witness line"). Severity: should.
    Fix: "No page of the reader site carries the chapter witness line."

33. "A chapter that lost its witness line causes the first message, and
    two pages that share one cause the second." (395) Rule: procedure apart
    from description (cause matter in the Remedy), and two ideas.
    Severity: should. Fix: move it to the Cause paragraph as "The first
    message means the chapter lost its witness line. The second means two
    pages share one." and leave the Remedy as "Open the reader site at the
    chapter's page."

34. "An edition lacks every 8-word window of a chapter's witness." (403)
    Rule: numbers under ten spelled out in prose, and wrong term as in
    item 32. Severity: should. Fix: "An edition lacks every eight-word
    window of a chapter witness line."

35. "*config/authorities.yaml* exists, and the companion has no entries."
    (442) Rule: wrong term (the vocabulary's "the sources companion",
    first use in the appendix). Severity: should. Fix:
    "*config/authorities.yaml* exists, and the sources companion has no
    entries."

36. "Populate the table of authorities (Chapter 10)." (444) Rule: wrong
    term (cross-reference form; elsewhere the appendix gives a chapter's
    title in italics on first mention, as at 11, 345, 410, 448). Severity:
    may. Fix: "Populate the table of authorities (Chapter 10, *title*)",
    with the chapter's real title.

37. "A highlighted code fence does it too." (456) Rule: wrong term ("does
    it" has no clear antecedent). Severity: may. Fix: "A code fence with
    syntax highlighting also puts color on a page."

38. "Fix every message in a failure before you run the check again." (11)
    Rule: wrong term (you fix the fault, not the message). Severity: may.
    Fix: "Fix the fault behind every message before you run the check
    again."

39. "The HTML file is not a document." (338) Rule: wrong term (vague
    "document"). Severity: may. Fix: "The HTML file has no `<html>`
    element, so it is not an HTML document."

40. "A fixture without an expect comment drew no diagnostic at all." (57),
    "The packaged known-good fixture drew a diagnostic." (62), "A fixture
    drew a diagnostic beside the one it declares." (67), "The list printed
    without its links." (264) Rule: present tense (Cause paragraphs
    elsewhere describe the fault in the present: "holds", "lacks").
    Severity: may. Fix: "A fixture without an expect comment draws no
    diagnostic at all." "The packaged known-good fixture draws a
    diagnostic." "A fixture draws a diagnostic beside the one it declares."
    "The list prints without its links."
