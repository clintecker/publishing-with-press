# STE80 desk report: Chapter 6, Checking the manuscript

File: `book/chapters/06-checking-the-manuscript.md`

Ratchet count: 6 before (baseline 6), 3 after.
`press check`: passed (exit 0) after the edits.

Mode: Humanize for body prose, tips, warnings, table cells, and the
footnotes. Light for the sidebar "The red check that went out green"
(no edit needed). No fence, code span, quotation, heading, figure line,
or art comment was touched. All three sentinels are outside this file and
untouched. Index terms in edited sentences (audit directories,
`audit-dirs`, sentinel, watchlist, jargon lint, banned patterns) keep
their exact spelling.

## Edits (18)

1. L54, S2 (31 words, split). Old: Two of the markers are placeholders: the common abbreviations for "to do" and "to be determined", each in capitals and followed by a colon, a space, and the verb "write". New: Two of the markers are placeholders: the common abbreviations for "to do" and "to be determined". Each is in capitals and followed by a colon, a space, and the verb "write".
2. L62 (Table 6.2 cell), S1/S2 (31 words, two ideas). Old: Press validates any ISBN, LCCN, or ISSN the book declares, and it refuses a retail book whose ISBN is missing or pending, or whose declared LCCN or ISSN is still pending. New: Press validates any ISBN, LCCN, or ISSN the book declares. It refuses a retail book whose ISBN is missing or pending, or whose declared LCCN or ISSN is still pending.
3. L75, S1. Old: It proves on every check that each rule can refuse something, and the press gives the reason: "A rule that cannot fail is not a rule." New: It proves on every check that each rule can refuse something. The press gives the reason: "A rule that cannot fail is not a rule."
4. L98, S1 (three-verb sequence). Old: The checker reads the fixture, collects every diagnostic it draws, and looks for the declared rule among them. New: The checker reads the fixture and collects every diagnostic it draws. Then it looks for the declared rule among them.
5. L118, S8 (ratchet lead, "-ing" rider "beginning"). Old: When every fixture behaves, press prints one line that counts them, beginning `Checker self-test passed: 19 known-bad fixtures`. New: When every fixture behaves, press prints one line that counts them. The line begins `Checker self-test passed: 19 known-bad fixtures`.
6. L131 (procedure step 3), S6. Old: That failure shows that the fixture is read. New: That failure shows that press reads the fixture.
7. L149, S1/S2 (27 words, definition plus a second clause). Old: The *audit directories* are the directories a book names under `audit-dirs` in *config/house-rules.yaml*, outside the manuscript, that the style audit reads with a lighter battery. New: The *audit directories* are the directories outside the manuscript that a book names under `audit-dirs` in *config/house-rules.yaml*. The style audit reads them with a lighter battery.
8. L192, S1/S2 (26 words). Old: Pandoc's smart typography curls your straight quotes in every rendered edition except the Manuscript edition (the stitched Markdown), which keeps your characters as you typed them. New: ...except the Manuscript edition (the stitched Markdown). That edition keeps your characters as you typed them.
9. L218, S2 (ratchet lead, 41 words). The counter merged two sentences because the footnote marker sat after the period with no space. The footnote is about the lint (its second copy), so the marker moved to the term it annotates. Old: The fourth pass runs the *jargon lint*, a separate program that reads the chapter files against a list of overused engineering terms.[^6-twocopies] Press runs it... New: The fourth pass runs the *jargon lint*,[^6-twocopies] a separate program that reads the chapter files against a list of overused engineering terms. Press runs it... (Wording unchanged. Flag for the copyeditor if the house wants footnote markers only at sentence ends.)
10. L227, S11 (ambiguous pronoun: "It" followed "The style audit" but meant the jargon lint). Old: The style audit reads the audit directories. It skips fenced code, inline code, URLs, and blockquotes, ... New: The style audit reads the audit directories. The lint skips fenced code, inline code, URLs, and blockquotes, ...
11. L231, S1. Old: It lives in the overused-jargon skill, as *references/watchlist.csv* in the skill's directory, and `press skills` prints each installed skill with its path. New: It lives in the overused-jargon skill, as *references/watchlist.csv* in the skill's directory. The `press skills` target prints each installed skill with its path.
12. L244, S1 (three ideas). Old: The default is `rewrite`, and `press check` uses it, so an inspect term appears in the report and does not fail the check. New: The default is `rewrite`, and `press check` uses it. An inspect term therefore appears in the report and does not fail the check.
13. L258, S1 (three ideas). Old: The `question` column is the useful one, because it asks what the term stands for, and the answer is usually the sentence to write instead. New: The `question` column is the useful one, because it asks what the term stands for. The answer is usually the sentence to write instead.
14. L293, S1 (three options in one sentence). Old: The `--json` option prints the findings for another program, `--max-findings` caps them at a number (500 by default), and `--allow` takes one term and can repeat. New: The `--json` option prints the findings for another program. The `--max-findings` option caps them at a number (500 by default), and `--allow` takes one term and can repeat.
15. L365, S6/S8 (ratchet lead, "including"; gerund subject with no actor). Old: Matching is exact, including case. New: Press matches each sentinel exactly, and case counts.
16. L386, S1/S2 (27 words). Old: A Print edition shorter than the floor fails verification, so the floor catches a build that ran to the end and set only part of the book. New: A Print edition shorter than the floor fails verification. The floor thus catches a build that ran to the end and set only part of the book.
17. L388, S1 (three ideas). Old: The book model's default is 40, while the scaffold's template writes 1, so a new book builds and verifies before it has a second page. New: The book model's default is 40, while the scaffold's template writes 1. A new book therefore builds and verifies before it has a second page.
18. L475, S6. Old: ...so a failed check fails the CI job before any edition is built. New: ...so a failed check fails the CI job before press builds any edition.

## Leads declined

- L256, ing-form 'wiring': "wiring" is one item in a list of watchlist terms named as words. It is a mention, not a verb.
- L293, passive 'is malformed': "malformed" is a predicate adjective ("If the watchlist itself is malformed"), not a passive. No actor is hidden.
- L491 to L499, paragraph-length 8 sentences: the sidebar is Light mode. Its three on-page paragraphs hold 2, 5, and 1 sentences. No sentence is over 30 words, and the only semicolon is inside the quoted scar entry. Merging sentences to meet the counter would cost voice for no reader benefit. The grep sentence ("Grep reads that text, finds a line it matches, ... and exits 0, as grep does.") is one narrated sequence, so I kept it.

## Other sentences considered and kept

- L122: "A fixture is the only way to show, on every check, that a pattern you added to *config/house-rules.yaml* still catches what you wrote it to catch." (26 words). A split would separate the claim from its condition "on every check".
- L341: the three-part list of what banned patterns enforce is a claim with three parts, kept whole.

## Passives kept

- L54 (edited): "Each is in capitals and followed by a colon..." describes the marker's form. No actor exists.
- L328: "press applies it exactly as written" is a participle of description. The actor (you) does not matter.
No more than two passives kept.

## Fidelity notes

No fact, number, identifier, or modal changed. "therefore" and "thus" were added only as the joint the removed "so" carried. The one change to position (the footnote marker in edit 9) is noted above.
