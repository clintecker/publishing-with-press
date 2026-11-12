# Fact check: Appendix B, Configuration reference

File: `book/appendices/b-configuration-reference.md`, checked against
`docs/briefs/facts/facts-B.md` and, as the writer's report declares, the same
fact base's slices facts-06, 09, 10, 11, 12, and 13.

**Status: passes with fixes.** Every key in the `press config list` capture
(facts-B 17.3) appears in the appendix. All 70-odd types match the capture
(`str`, `int`, `float`, `bool`, `list[str]`, `mapping`, IMMUTABLE,
STRUCTURED, FILE), and so does every default the fact base gives
(`house-6x9`, `house`, `perfect-bound`, `paperback`, `cream`,
`standard-color`, 3, true, false, `[]`, 40/1, `penguin-tri-band`,
`wood-engraving`, `rule`, the house palette and `book-colors` values, and the
Iowan stack). Every quoted message I checked matches its source, and so do
the six profile ids, the four providers, the bindings and materials, and the
ten cover and seven illustration style ids. One claim blocks.

Counts: Unsupported 2, Contradicted 1, Drifted 11, Missing 5.

## 1. Unsupported

1. Line 109, `print.provider`: "The `house` numbers belong to no real shop."
   I searched facts-B, facts-12 10.4, and 20.A.13. The file describes `house`
   as "constant; white 0.002252, cream 0.0025 in/page; allowance 0.0 ("v1
   value; real specs use 0.06")" and, in 20.A.13, as "KDP-like calipers, 0
   allowance". Fix: soften to the file's wording, for example "The `house`
   numbers are KDP-like page calipers with no spine allowance, the press's v1
   values; real provider specs add 0.06in."
2. Line 414, *config/illustration-styles.yaml*: "A book's
   *config/illustration-styles.yaml* adds to the house library in the same
   way". After the cover-styles section, "in the same way" means merging over
   the house library and replacing a style by its id. I searched facts-11 8.5
   and found only "A book can add styles in `config/illustration-styles.yaml`
   (`styles: {id: {name, note, source?, prompt}}`)". Nothing says that a book
   style replaces a house style of the same id. Fix: "A book's
   *config/illustration-styles.yaml* can add styles, under one top-level key,
   `styles` ...", and cut "in the same way".

## 2. Contradicted

1. Line 156, `registrations.retail`: "When it is `true`, a missing or pending
   number makes `press check` fail with `retail edition declared while
   registrations are absent or pending: ...`." This entry sits among the
   `lccn` and `issn` entries, so "a missing or pending number" covers all
   four. facts-13 S1 (confirmed from `registrations.py:340-362`): "It requires
   an ISBN for both editions, `print` and `epub` ... The LCCN and ISSN are not
   part of the retail check; they are validated separately when present ... So
   a retail edition needs two real ISBNs and nothing else from this file."
   Fix: "When it is `true`, `press check` fails unless both
   `registrations.isbn.print` and `registrations.isbn.epub` hold real numbers,
   with `retail edition declared while registrations are absent or pending:
   ...`. The LCCN and ISSN are not part of this check." (The `press config
   list` description, "true makes missing/pending registrations fail check", is
   looser than the code; follow the code, as the appendix's opening paragraph
   promises.)

## 3. Drifted

1. Lines 91-99, Example B.1: the message text is folded from three lines to
   five. The brief allows only the slug change and `...` elision. facts-B 3.3
   (and facts-06 3.3) give exactly:
   ```text
   this is a release build (PRESS_RELEASE=1) and its witnesses are vacuous:
   verify-sentinels has N entries; a release needs at least 2 distinctive prose fragments
   verify-min-pages is N; a release needs at least 24
   ```
   Fix: print the three lines unfolded and cut the folding note on line 99. If
   the measure cannot hold them, elide with `...` instead of folding.
2. Line 54, `description`: "The cover commission uses it as the subject when
   neither `--subject` nor `cover.subject` names one." The press has a command
   called `press art commission`, and this precedence belongs to `press cover`
   (facts-11 8.4, "Subject precedence ... `--subject`, then `cover.subject`,
   then metadata `description`"). Fix: "`press cover` uses it as the subject
   ...".
3. Line 265, `cover.subject`: "The cover prompt takes the subject from
   `--subject`, then this key, then the metadata `description`, then
   `cover.emblem`." The chain is incomplete. facts-11 8.4: "... then
   `cover.emblem`, then the literal "the book's subject"." Fix: add the final
   fallback.
4. Line 79, `verify-sentinels`: "A chapter opening splits a chapter's first
   word, which breaks an exact match in the PDF." Every shipped profile sets
   the chapter opening to `none` (facts-09 4.5), and the scar names the drop
   cap: "the drop cap splits and small-caps a chapter's opening word"
   (facts-B 3.3, war story 29). Fix: "A drop cap (any `chapter-opening.style`
   other than `none`) splits and small-caps a chapter's first word ...".
5. Line 162, `registrations.isbn-block.size`: "10, 100, or 1000" with no
   qualifier. The appendix's opening says it follows the code where docs and
   code disagree. facts-13 11.2: "`size` may be 10, 100, or 1000 in the docs.
   The code accepts 10 through 1,000,000." Fix: "`press config list` names 10,
   100, or 1000, the sizes the agency sells; the code accepts sizes from 10
   through 1,000,000." Alternatively, drop the promise on line 3 for this
   entry.
6. Line 239, `banned-patterns`: "Double each backslash in the YAML." The fact
   base shows only the double-quoted example `"\\bvery unique\\b"` (facts-06
   4.9) and gives no general rule. A backslash needs doubling only inside a
   double-quoted YAML string. Fix: "Inside a double-quoted YAML string, double
   each backslash, as in `"\\bvery unique\\b"`."
7. Line 399, `styles.<id>.era`: "such as 1935 for `penguin-tri-band`." facts-11
   8.4 gives "penguin-tri-band (1935–, Edward Young & Jan Tschichold)" and does
   not quote the field value itself. Fix: "such as 1935 onward for
   `penguin-tri-band`", or cut the example.
8. Line 377, cover styles: the book's file "merges over it, style by style".
   facts-11 8.4: "A book's `config/cover-styles.yaml` merges over it, key by
   key." Fix: use the file's "key by key", or keep "a book can add a style or
   replace one by its id", which is the substance.
9. Line 441, `assets`: "Each one is optional, and each consumer works without
   it." facts-12 10.5 lists the requirement "`assets/cover.jpg` ("coverwrap
   needs assets/cover.jpg")", and the LULU troubleshooting row reads "No cover
   was built | No `assets/cover.jpg`". Fix: "Each one is optional, and every
   consumer degrades gracefully without it, except `press coverwrap`, which
   needs *assets/cover.jpg*."
10. Line 9: "An *immutable* field, such as `trim`". "Such as" suggests that
    others exist. The capture has exactly one IMMUTABLE field. Fix: "The one
    *immutable* field, `trim`, refuses writes ...".
11. Line 150, `registrations.lccn`: "through the Preassigned Control Number
    program." facts-13 calls it "**PCN** (PrePub Book Link), not CIP". The
    expansion appears only in facts-E (glossary item 73), which is outside this
    appendix's declared sources. Fix: "through the Library of Congress's PCN
    program (PrePub Book Link)". Alternatively, the editor can accept facts-E.

## 4. Missing

1. `print.page-thickness` (line 121): the entry says the press "uses it in
   place of the paper's thickness", without exception. 20.B.5: "`print.page-thickness`
   is ignored for Lulu hardcovers. The IngramSpark dust-jacket spine uses the
   paperback PPI formula." This is listed as a bug, so do not document it as a
   feature. A reference still needs a hedge, such as "(Lulu's hardcover spine
   table does not read it)".
2. `chapter-opening.style` (line 131): `raised-cap` is listed as a distinct
   choice. 20.B.7 / facts-09 4.5: "`raised-cap` is accepted but renders the same
   as `drop-cap`. No code treats it differently." A reader picking it would
   want to know.
3. Line 7, `press config` options: the appendix names only `--json`. 20.A.23
   records `config --json/--dry-run/--file`, which exist in code but not in
   `--help`. The appendix notes the same gap for `aesthetic --overwrite` on
   line 329, so `--dry-run` (which prints the diff, then `(dry run: nothing
   written)`; facts-03 S4) deserves the same line.
4. `styles.<id>.prompt` for illustrations (line 426): the quirk in facts-11 8.5,
   "the house `book-colors.ink` is `171717` with no `#`, so prompts read "in
   171717 ink"".
5. Line 251: "The build itself reads only `scene-break`, the `typography`
   keys, the two palettes, and `book-colors`." This is true of the build, but
   `press art enhance` also reads `plates.medium` to choose its upscaler model
   and colour count (facts-11 8.7). The `plates.medium` entry gives the intake
   rule only.

## Note for the editor: claims resting on slices outside the declared set

These claims are correct, but they rest on facts-03 or facts-E, not on the
slices that the writer's report and this brief name: the `--author` / git
user / "The Author" chain, the `--publisher` and `--place` defaults, the
`--owner` behaviour of `repository` and `site-url`, the slug as the directory
name (facts-03 3.1); the scaffolded house rules `banned-patterns: {}`,
`jargon-allow: []`, and `audit-dirs: []` (facts-03 3.1 tree); "`press config
validate` ... reports an absent file as `ok`" (facts-03 S4); and the PCN
expansion (facts-E 73). Either rule that facts-03 and facts-E are admissible
or soften these claims.

## Captured output and verbatim strings checked

The following match their sources: `metadata missing <key>:`; `sentinel not
found in the manuscript: <s>`; `unknown print profile '<id>'; available: ...`;
`retail edition declared while registrations are absent or pending: ...`;
`front matter needs these config/metadata.yaml keys: ...`; the banned-pattern
regex refusal; `gen_index: curated terms match nothing in the text: <terms>`;
`gen_authorities: the ledger does not hold:`; `the <style> style needs source
material: --from <image>` (the source has `{style_id}`); the quoted
`trim is not set directly; choose it with print.profile`; Example B.2 (matches
facts-10 9.2); and Example B.3 (a documentation example, not a capture; it
elides with `...` and rightly drops the `composited` comment). Example B.1
fails; see Drifted 1.
