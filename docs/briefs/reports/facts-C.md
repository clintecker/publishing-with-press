# Fact check: Appendix C, Messages and refusals

File checked: *book/appendices/c-messages.md* (462 lines) against *docs/briefs/facts/facts-C.md*, with the admitted sources per the ruling: other chapters' fact slices (facts-D for press doctor, facts-06 and facts-07 for the paragraph law, the title-case form, and `pandoc is required`) and the shared-facts tables in *docs/continuity.md*.

Every message in constant width was checked character for character. A script pulled each inline-code span of 12 or more characters from the appendix and searched the admitted sources, treating three periods as U+2026. Every message is found verbatim in an admitted source. Only three non-message spans are missing from the sources, and all three are the book's own examples: `# Writing the manuscript`, `press config set description "One paragraph."`, and `<!-- expect: ... -->`. Two definition terms appear in the sources only as substrings of a longer printed line (see Drifted 1 and 2). The appendix has no code blocks of captured output, so the slug rule does not apply.

Status: **blocks** (2 contradicted, 5 unsupported).

## 1. Unsupported (severity: blocks)

1. **l.62 and l.64, the known-good fixture.** "Every rule must accept it, so a book pattern that matches it is too broad." and "Narrow the banned pattern that the message names." I searched facts-C §6.5 for "known-good", "banned", and "book prose". The file says only that "The known-good fixture `src/press/data/known-good/clean.md` must draw zero diagnostics". The file says book fixtures in *tests/known-bad/* "are judged as book prose under the book's own banned patterns". Nothing says the packaged known-good fixture is judged under the book's patterns, and the message does not name a pattern. Fix: "The packaged known-good fixture drew a diagnostic. It must draw none, so a rule that rejects it is too broad." Remedy: "Read the diagnostics after the colon, and narrow the rule they name."
2. **l.177, the doctor's hints.** "The install hints in the parentheses follow every `not ready:` line." facts-D §2.3 has one captured run. *continuity.md* l.147 gives the form as `not ready: <tools>`. Nothing says the hints are constant or always printed. Fix: "In the captured run, the line ends with install hints in parentheses."
3. **l.269, pypdf.** "This is a note, and press skipped the link checks." facts-C §6.1 step 8 says only "If pypdf won't import: `pypdf unavailable; illustration-list destinations not verified`". It does not say whether this is a note, a warning, or a failure. Fix: "The `pypdf` package does not import, so press did not verify the list links."
4. **l.28, the level-1 heading.** "The chapter file has no line that begins with a single `#`". The mechanism is not in the file. facts-C l.125 gives only the message, and facts-06 l.175 says "A `#` heading is a chapter". Fix: "The chapter file has no level-1 heading, so the chapter has no title." (Low risk, but it describes a mechanism the file does not state.)
5. **l.18, the missing source file.** "The book lists a chapter file that is not on disk." facts-C l.123 gives only the message, under "Per chapter file". No source says how press comes to list a file. Fix: soften to "A chapter file press expects is not on disk." Or cite the chapter-order fact if another slice states one. (Low risk.)

## 2. Contradicted (severity: blocks)

1. **l.460, footnote `c-ellipsis`, the worst finding.** "Press ends this message, and the note after it, with a single ellipsis character." The capture shows the opposite. facts-C l.323 (the `press check` capture on a fresh scaffold) has `note: em-dash.md also drew: - /…/src/press/data/known-bad/em-dash.md:4: glyph U+2014 is outside the print-font set`, and facts-06 l.507 has the same line. Press prints the diagnostic after the colon. The U+2026 in facts-C §6.5 (`note: <fixture> also drew: …`, `a checker rejected the known-good fixture: …`) is the fact file's elision of the diagnostics, not a character press prints. Chapter 6's Example 6.2 already prints it as `...`. The ruling that three periods stand for the ellipsis still holds. Only the footnote's claim about press is wrong. Fix: "Here `...` stands for the diagnostics press prints after the colon." Add `...` to the conventions in l.3 next to `[...]`, or reword the footnote to say this.
2. **l.73, audit directories.** "Faults in an audit directory print under `Editorial warnings:` and do not fail the check." *continuity.md* l.99 (audit directory): "meets the universal battery only (not curly quotes, glyph law, banned patterns); heading and paragraph faults there are warnings under `Editorial warnings:`". facts-06 l.182 says the paragraph law is "an error in book prose and a warning in `audit-dirs`". Only heading and paragraph faults are warnings. An em dash or trailing whitespace in an audit directory is a universal-battery fault and fails the check. Fix: "In an audit directory, heading and paragraph faults print under `Editorial warnings:` and do not fail the check. The universal battery (the dash, phrase, parallelism, and whitespace rules) applies there as everywhere."

## 3. Drifted (severity: should)

1. **l.140, `title-case heading`.** This is presented as the message, and l.3 promises "Each entry quotes the message as press prints it". facts-06 l.177: "A title-case heading is refused with `title-case heading: <text>`." (Chapter 6 Table 6.5 agrees.) Fix: make the term `title-case heading: <text>`.
2. **l.179, `present but cannot execute`.** This is a fragment of the tool's line. facts-D §2.3 prints `[ BROKEN] claude     present but cannot execute; the operator: press improve, research, aesthetic briefs`. Fix: make the term `[ BROKEN] <tool>  present but cannot execute; <purpose>`, or say in the cause that the words appear in the tool's line, after the `BROKEN` state.
3. **l.158, the command line.** "These messages come from press itself before any target runs." The appendix's own cause for `pandoc is required` (l.166) says "A build target found no `pandoc`", and facts-07 l.5 says "The format targets go to `build.build_target`. pandoc must be on PATH, or the build stops with `SystemExit("pandoc is required")`." Fix: "These messages come from press itself, before or at the start of a target, not from a checker."
4. **l.45, setting a sentinel.** "set it with `press config set verify-sentinels`". `verify-sentinels` is a `list[str]` (facts-01 and facts-06 config tables), and a list is set with JSON, as in facts-C §3.4: `press config set author '["Your Name"]' --json`. A reader who copies the bare command has no form that works. Fix: show the list form, for example `press config set verify-sentinels '["<phrase one>", "<phrase two>"]' --json`, or say "set the list with `press config set verify-sentinels ... --json`".
5. **l.86, l.101, l.116, rule wording.** `generic conclusion`: "The line opens a summary with" the phrase. The rule is `\bin conclusion\b` (facts-C §6.4 table) and matches anywhere in a line. Fix: "The line holds the stock two-word phrase...". `formulaic negative parallelism`: "The line opens with 'not only'". The rule is `not only … but also` within 120 characters, anywhere. Fix: "The line holds 'not only' and its usual partner within 120 characters". `chatbot signposting`: the rule also matches "delve" and "break this down" (`let's (dive|delve|explore|break this down)`). Add these, or write "invites the reader to dive in, explore, or the like".
6. **l.17 to l.32, source-check message forms (the sources disagree).** facts-C l.123 to 126 gives `missing source file`, `suspiciously short source`, `no level-1 heading`, `unfinished marker '<phrase>'`. *continuity.md* l.221 (marked "due App. C") gives each with a trailing colon: `missing source file:`, `suspiciously short source:`, `no level-1 heading:`, `unfinished marker '<phrase>':`, matching `metadata missing <key>:`. The appendix follows facts-C, which is defensible. Before the appendix claims to print the message "as press prints it", the continuity desk should rule which form is exact.

Checked and clean. Not findings, listed so the next desk need not redo them:

- Every verify_pdf, verify_formats, verify_pages, and print-profile message, including the two cover messages with their `--` and the leading `...`.
- The release refusal and its two follow-on lines (continuity l.167).
- `paragraph N has W words (the law is under 190; split it)` (facts-06 l.183, continuity l.154).
- The doctor's `not ready:` line, the Python range line, and `this machine can make books` (facts-D §2.3).
- The jargon finding line, every pass line, the 19 fixtures, the exit statuses 1, 2, and 43 → 43.
- The glyph ranges and the "skips fenced code" rule (continuity l.155).
- The trailing-whitespace and unfinished-marker rules read fenced code (continuity l.100, l.221).
- Two hyphens become a dash (facts-06 l.174).
- `print.profile`, `press clean`, `First edition, 2026`, and the edition names Print, Single-leaf, Chapter, Office (continuity l.178, l.187, l.169).
- The highlighted fence turns the ink colored (continuity l.152).
- pypdf as a declared dependency (continuity l.133).
- `pdfimages` is not checked by the doctor (facts-C §20 B14).

On the paragraph law, l.131 "reaches 190 words" follows the message ("under 190"). facts-06 l.182 says "Over 190 gives an error", which reads one word differently. This is the source's own looseness. Leave it.

## 4. Missing (severity: may)

Chapter 6 l.451 promises that Appendix C "holds the full list", and *continuity.md* marks these as owed to Appendix C:

1. **The orphan plate refusal** (a source check; facts-C l.130 "Orphan plates"): `plate never referenced by the manuscript: assets/woodcuts/<name>`. Remedy: delete the file and its image line in the same commit (continuity l.231, "due App. C").
2. **The `fig-alt` refusal** for `decorative=true` (continuity l.228, "due App. C").
3. **`defaults reference a missing file`**, the defaults-templating refusal (continuity l.205, "due App. C").
4. **`no assets/cover.jpg; interior verified, wrap not built`**, printed by `press verify-print` (continuity l.197). It belongs in the print pack section beside the two profile messages.
5. **The curly-quote rule.** The style audit section lists every manuscript rule except curly quotes, although facts-C §6.4 names it ("Book prose only: curly quotes, the glyph set, and the book's banned patterns") and the fixture table has `curly-quotes.md` with the expected text `curly`. No full message is quoted. Give it an entry described in words, as the appendix does for the jargon lint's unquoted messages.
6. **The banned-pattern print form**, `<file>:<line>: <label>` (continuity l.103). l.145 describes it but does not show it.
7. **The command line:** bare `press` with no command prints usage and exits 2 (facts-C §17.4). The jargon lint exits 2 on a malformed watchlist (§17.4, §6.4). The report-CD note on the watchlist is right that no message text exists. The exit status still belongs in a sentence.
8. **The source checks the appendix does not list.** facts-C l.128 to 133 name registrations and commerce failures, figure placement errors, config file shapes, and print feasibility, with no message text. One sentence saying the first pass also refuses these, with pointers to Chapters 5, 12, and 13, keeps the "full list" promise honest.
