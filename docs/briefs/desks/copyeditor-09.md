# Desk brief: copyeditor

You copyedit Chapter 9, `book/chapters/09-the-house-design.md`, against
`docs/prose-contract.md` (the whole file; the prompt block is the law),
`docs/style-guide.md` sections 3, 4, and 8 (voice, code typography,
anti-patterns and era touches), and `docs/vocabulary.md`.

Run `python3 tools/ste_check.py book/chapters/09-the-house-design.md` first and
treat its findings as leads, not verdicts: quoted output and tables trip
the sentence counter and are fine; a semicolon, a passive with a hidden
actor, a "could potentially", or a 35-word sentence in prose is not.

Then read every sentence. Report, in `docs/briefs/reports/copy-09.md`,
one numbered list, each item: the quote, the rule (by the contract's name
for it: "not X but Y", "one-line closer", "-ing rider", "assistant
vocabulary", "sentence over 30 words", "two ideas", "hidden actor",
"perfect tense", "noun stack", "synonym rotation", "hedge stack",
"semicolon", "meta-narration", "title case", "era spelling", "wrong
term"), the severity, and the fix as the corrected sentence.

Severity: blocks for anything on the one-sighting list and anything
`press check` would refuse; should for the sentence rules and vocabulary;
may for rhythm.

Also check: second person and present tense throughout; "we" only for the
authors' judgment; no "I"; the dry understatement appears once every few
pages and never in a heading; admonitions are imperative and under four
sentences; footnotes carry asides, not facts the body needs; American
spelling; "Unix", "e-mail", "Web site", "filename", "manpage",
"appendixes", "toward"; numbers under ten spelled out in prose except
versions, measurements, and anything in code.

Do not touch facts. If a sentence is wrong in fact, note "fact: see fact
checker" and move on.

Return: status, the counts by severity, and the three most frequent rules
broken.
