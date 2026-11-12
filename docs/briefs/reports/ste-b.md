# STE80 editor report: Appendix B, Configuration reference

File: `book/appendices/b-configuration-reference.md`

## Ratchet

- Before: 23 (baseline in `tools/ste-baseline.json`: 23)
- After: 21
- `press check`: passed (source, checker self-test, editorial, jargon).

## Edits

Line numbers are in the edited file.

1. L37, S2 (27 words, two actions). Old: "The generated title page sets it in capitals and adds a period unless the title already ends in a period, an exclamation mark, or a question mark." New: "The generated title page sets it in capitals. It adds a period unless the title already ends in a period, an exclamation mark, or a question mark."
2. L46, S4/S13 (label fragment folded into the sentence it qualifies, `date` entry from 7 prose sentences to 6). Old: "Free text. The press takes the first four-digit year in it that begins with 1 or 2." New: "The press reads this free text for the first four-digit year that begins with 1 or 2."
3. L111, S13 (two sentences of one instruction merged, `print.provider` entry from 7 to 6). Old: "Before you design the cover, set this key to the shop that will print the book. For a Lulu paperback, set it to `lulu`." New: "Before you design the cover, set this key to the shop that will print the book, such as `lulu` for a Lulu paperback."
4. L123, S1/S2 (28 words, a rule and its exception). Old: "When you set it, the press uses it in place of the paper's thickness, except for a Lulu hardcover, whose spine comes from Lulu's table of page-count bands." New: "When you set it, the press uses it in place of the paper's thickness. The exception is a Lulu hardcover, whose spine comes from Lulu's table of page-count bands."
5. L180, S6 (hidden actor). Old: "The party the reader buys from, named on the landing page before the reader leaves it." New: "The party the reader buys from, which the press names on the landing page before the reader leaves it."
6. L202 to L204, S8 and S13 (a noun doing the verb's work, and an 8-sentence paragraph with two topics: what the file generates, then how the file comes to exist and what overrides it). Old first sentence: "The presence of this file asks the press to generate the PDF's front matter: the title page, the copyright page, and the dedication, epigraph, and acknowledgments pages." New: "When this file exists, the press generates the PDF's front matter: the title page, the copyright page, and the dedication, epigraph, and acknowledgments pages." The paragraph splits before "The scaffold writes the file with every key commented out." No other sentence changed.
7. L253 to L255, S3 and S13 (7-sentence paragraph, and a command before its condition). Old: "Restate a whole section when you touch it." New: "When you touch a section, restate the whole section." The paragraph splits after that sentence: the merge rule, then how to print the merge and where the chapters explain the keys.
8. L257 to L259, S1 and S13 (three ideas in one sentence, and a paragraph that turned from which keys the build reads to the craft laws). Old: "Certain craft laws hold whatever the aesthetic says. The exact title and author appear verbatim on the art, cover plates are flat, and the trim is the trim." New: "Certain craft laws hold whatever the aesthetic says: the exact title and author appear verbatim on the art, cover plates are flat, and the trim is the trim." It opens a new paragraph with "Print interiors are single ink, except under the `house-6x9-color` profile."
9. L323, S4/S6 (fragment with a hidden actor). Old: "Token to `#hex` for the dark theme, written into the reader stylesheet after its dark-mode media query." New: "Each entry maps a token to a `#hex` color for the dark theme. Press writes the palette into the reader stylesheet after its dark-mode media query." The wording mirrors the `web-palette` entry, which already says "Each entry maps a token to a `#hex` color" and "Press writes the palette into the light theme".
10. L341, S1 (three ideas: the help text, the missing workflow, the instruction). Old: "The press's help text names an "index workflow", but at the time of this writing none ships, so edit the file by hand." New: "The press's help text names an "index workflow", but at the time of this writing none ships. Edit the file by hand."
11. L367, S3/S8 (gerund subject, no named actor). Old: "Rewording the sentence in the chapter fails the build until you update the claim." New: "If you reword the sentence in the chapter, the build fails until you update the claim."
12. L431, S6 (hidden actor). Old: "With `required`, the style needs an image to redraw, given with `--from`." New: "With `required`, the style needs an image to redraw, which you give with `--from`."

## Leads declined

- Paragraph-length leads on definition entries: L39 `subtitle`, L45 `date`, L51 `publisher`, L77 `site-url`, L82 `verify-sentinels`, L85 `verify-min-pages`, L110 `print.provider`, L116 `print.material`, L157 `registrations.retail`, L242 `banned-patterns`, L248 `audit-dirs`, L319 `web-palette`, L357 `match`, L372 `file`, L412 `styles.<id>.text`, L433 `styles.<id>.prompt`, L442 `qualification`. Two reasons.
  - The counter reads each entry's bold key line as a sentence of its own (it splits "CODE :" at the colon), so every entry counts one high. Each entry also holds two label fragments, the "Type `x`, default y." line and the "See Chapter N." pointer, which S4 treats as table text. Without those three, every entry holds six prose sentences or fewer. `verify-sentinels` holds the most, at six.
  - The fix the counter wants is a second paragraph inside the entry. The appendix uses compact definition lists (no blank line between term and definition). I tested this with pandoc. A 4-space continuation paragraph in a compact entry comes out as a second `Plain` block. The HTML and EPUB writers run it into the first paragraph with no break. A loose entry gives real paragraphs but different spacing from its neighbours. Either is a typography change, not a sentence change. The ratchet also drops 4-space-indented lines as code, so that split would hide the prose from the gate rather than fix it.
  - Where two sentences merged cleanly, I merged them anyway (edits 2 and 3). The count for `date` and `print.provider` still shows 7 because of the key-line artifact.
- L82, the 30-word sentence in `verify-sentinels` ("A chapter opening (...) splits a chapter's first word and sets it in small caps, which breaks an exact match in the Print edition (the PDF)."): the counter scores it 25, because a parenthesis counts as one word. That is not over 25. A split would make the entry's longest paragraph longer still, so I kept it.
- L105 `-ing` lead, "binding": a noun ("the binding"), not a verb form.
- L360, "A term that matches nothing fails the build with `...`, followed by the advice to fix the patterns or remove the terms.": it is 21 words by the counter's rules (a code span is one word) and holds one idea, the message and what it says. Kept.
- Over-25 raw-word sentences that are one idea with a list (L7 config subcommands, L114 binding shapes, L133 ornate style, L168 commerce refusals, L171 release gate, L297 plates.medium condition, L360 index shape refusals, L416 prompt fields, L449 assets): each is a single statement over a list of identifiers, or two linked facts joined by "and". Each is at or under 25 by the counter's rules. Not split.

## Passives kept

- L117 "`paperback` and `casewrap` are printed covers": "printed" is an adjective here, not a passive verb.
- L155 "a check value of 10 is written `X`": a notation convention. Who writes it does not matter.
- L300 "How a plate is composed.": a label for prompt text that goes to an image model. The actor (the model) does not matter to the reader.
- L139 "Whether the rest of the first word is set in small caps.", and the participles in the colophon entries ("set in italic", "printed after the edition line"): label fragments that describe the page. LuaLaTeX acts in every case, and the reader does not need it named.

## Fidelity notes

- Edit 6 changes "asks the press to generate" to "the press generates". The override sentence that follows ("A file at *tex/title-page.tex* overrides all of it.") still states the exception, now at the start of the next paragraph. If the reviewer wants the softer verb, "When this file exists, it asks the press to generate the PDF's front matter: ..." also works at 26 words.
- Edit 3 makes the Lulu instruction an example of the general rule ("such as"). The original stated it as a separate instruction. The fact (set `lulu` for a Lulu paperback) is unchanged.
- No sentinel phrase, index term, number, identifier, quotation, code span, or heading changed. No semicolons or dashes were added.
