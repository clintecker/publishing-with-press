# STE80 editor report: Appendix C (book/appendices/c-messages.md)

Status: done. `press check` exits 0. `tools/ste-ratchet.py` exits 0.

## Ratchet count

- Baseline (`tools/ste-baseline.json`): 2
- Before: 2
- After: 2

Both leads are false positives (see "Leads declined"), so the count stays
at the baseline. The file was already close to the contract: no sentence
over 30 words, no prose semicolons, no dashes. Every entry's Cause and
Remedy already ran in short, active, present-tense sentences.

## Edits (line numbers are in the edited file)

1. Line 3 to 5, S13 (one topic per paragraph, six sentences at most). The
   opening paragraph held six sentences on two topics: what the appendix
   holds, then the notation for values in a message. Split at the turn,
   before "Words in angle brackets". No sentence changed.
2. Line 172, S2 (26 words; split over 25).
   Old: "Book prose holds a character outside the set the glyph law allows:
   tab, line feed, carriage return, U+0020 to U+007E, and U+00C0 to
   U+017F."
   New: "Book prose holds a character outside the set that the glyph law
   allows. The set is tab, line feed, carriage return, U+0020 to U+007E,
   and U+00C0 to U+017F." (S4 also: "that" restored.) Index term "glyph
   law" kept.
3. Line 193, S2 (26 words; split over 25).
   Old: "When a line matches one of the book's banned patterns, press prints
   the label from *config/house-rules.yaml* in place of a packaged
   diagnostic, in the form `<file>:<line>: <label>`."
   New: "When a line matches one of the book's banned patterns, press prints
   the label from *config/house-rules.yaml* in place of a packaged
   diagnostic. The form is `<file>:<line>: <label>`." Index term "banned
   patterns" kept.

## Leads declined

- Line 119, ing-form, "heading": a noun ("heading and paragraph faults"),
  not a verb form.
- Line 204, passive, "is malformed": "malformed" is a predicate adjective
  that states the watchlist's condition. No actor made it malformed in a
  way the reader needs, and press's own wording is "malformed".

## Passives kept (more than two, so listed)

- Line 7, "broken at a space to fit the page": the actor is this appendix's
  typesetting, which does not matter to the reader.
- Line 51, "placeholder abbreviations followed by the verb": a
  participle that describes word order, with no actor.
- Line 221, "not marked optional": the defaults file marks it; the
  sentence already names the defaults, and the actor does not matter.
- Line 498, "`PRESS_TOOLCHAIN` is set": whoever sets the variable (the
  toolchain image, CI, or you) does not matter to the cause.
- Line 204, "is malformed": see above.

## Other notes

- Phrasal verbs "look one up", "look for lost chapters", and "look for a
  hand-authored page" kept: "search" or "examine" reads like a form letter
  in a Remedy line.
- No sentinel phrase occurs in this file. No fence, code span, quoted
  message, heading, or footnote label was touched.
