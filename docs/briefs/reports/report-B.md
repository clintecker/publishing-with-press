# Report B: Appendix B, Configuration reference

File: `book/appendices/b-configuration-reference.md`.

## Word count

4,491 by `press wordcount` (target about 4,000; within 15 percent, upper side).
It includes Table B.1, three examples, and the index comment.

## Structure

Heading `# Appendix B: Configuration reference {.unnumbered}`. Four opening
paragraphs (how to read an entry, `press config` usage, the four field kinds)
and Table B.1 (file to chapter). Then one `##` per file in the brief's order:
metadata, front-matter, house-rules, aesthetic, index-terms, authorities,
cover-styles, illustration-styles. Metadata and aesthetic have `###` groups
(identity, press facts, verification knobs, print, chapter-opening,
registrations, commerce; direction for the art, values the build reads).
Every key in `press config list` is a definition-list term in bold constant
width, with type, default, meaning, and chapter.

One deviation: a closing `## Fields kept outside these files` for the three
`press config list` entries that live in no listed file (`qualification`,
`tex/title-page.tex`, `assets`). Without it "every key" would miss them. The
editor may cut it or move it.

Figures: none (appendix). Examples B.1 (release refusal, folded), B.2
(index terms), B.3 (a cover style). Footnotes: none.

## Facts used beyond facts-B

facts-B did not carry the house-rules scaffold, the front-matter details,
the index and authorities schemas, the cover/illustration style schemas, the
print profile and provider lists, or registrations detail. I took them from
the same fact base in facts-06 (4.9), facts-10 (9.1 to 9.3), facts-11 (8.4,
8.5), facts-12 (10.1, 10.2, 10.8), facts-13 (11.2 to 11.4), facts-09 (4.4,
4.5), and Chapter 3 Table 3.1 for the scaffolded house rules
(`banned-patterns: {}` and so on).

## Contradictions and how they were handled

- `verify-min-pages`: model and CONFIGURATION.md default 40, scaffold writes
  1. Both stated.
- `trim`: stated as immutable, from the profile, with the legacy mapping
  only cross-checked. The bug that some surfaces still read `metadata.trim`
  (20.B.3, 20.A.17) is not mentioned.
- `cover-styles` `text: composited`: stated that the docs describe it but no
  code composites, and any non-`baked` value only drops the guardrail (code).
- `web-palette.accent`: stated that the cover prompt reads it and the house
  palette lacks it, so `#7a2325` applies (20.A.15, code).
- Plate greying: stated the code condition ("single" and "ink" in
  `plates.medium`, non-colour profile) (20.A.18).
- `seller-of-record`: said the press's model is provider-as-seller and the
  publisher must confirm; Lulu not named as seller (20.A.12).
- `isbn-block.size`: gave 10, 100, 1000 as `press config list` does; silent
  on the code accepting up to 1,000,000.
- Left out as 20.B items: `raised-cap` rendering like `drop-cap`,
  `page-thickness` ignored for Lulu hardcovers, txt/docx lacking drop caps and
  ornaments, landing-page `lang` fixed.
- `press aesthetic --overwrite`: stated only that the option exists and is
  not in `--help`; its behaviour is not in the fact base.

## Facts I could not find (left out)

- The scaffolded `config/house-rules.yaml` verbatim (Chapter 3's summary used).
- Defaults for `commerce.print-ordering.*` other than `enabled` (written
  "default none").
- Whether `press config validate` reads the style libraries (said only that
  its captured output does not list them).

## Checker residuals

`press check` passes (all four passes, 23 files). Jargon lint: no rewrite
terms. Inspect hits are "scaffold" (the press's own word for `press new`'s
output) and one "canonical" (the HTML canonical link, literal).

`tools/ste_check.py`: about 60 findings. Defence:
- Definition entries are many short fragments, so several entries read as
  paragraphs of 7 or 8 sentences. Each is one key, one topic.
- Long "sentences" at the index comment (line 443) and the `trim` quotation
  (line 85, semicolon inside the verbatim `press config list` text).
- Passives that remain are in "is merged", "is set in small caps", "is
  folded", and the like, where the actor is the press and naming it each time
  would lengthen the entry. I converted the refusals ("is refused") to active
  where it read better.
- `-ing` forms are gerund subjects ("Matching ignores case"), not riders.

## Revision (after fact, copy, and type desks)

Word count: about 4,590 by `press wordcount` (within 15 percent of 4,000).
`press check`: no error names this file. The remaining failure is in
another writer's file (*16-inside-the-press.md*). Jargon lint: no rewrite
terms. Tools run: `unnumber-appendix-heads.py` (18 heads marked `{-}`),
`tag-fences.py` (0 changed), `prefix-footnotes.py` (unchanged).

Applied, per the coordinator's rulings:
- `registrations.retail`: requires two real ISBNs, print and epub. Any
  declared LCCN or ISSN must also be real, and a declared `pending` one
  joins the refusal's list. A missing LCCN or ISSN is not a retail fault.
  (This follows the coordinator's corrected ruling.)
- Cut "belong to no real shop". Replaced with the fact base's words:
  KDP-like calipers, no spine allowance, the v1 values. The illustration-styles
  merge claim is now "can add styles".
- Example B.1: the original lines, with `...` elision only, plus a
  sentence that gives the elided endings verbatim.
- `isbn-block.size`: the list's 10, 100, 1000 and what the code accepts,
  10 through 1,000,000. `print.page-thickness`: notes the Lulu hardcover
  exception.
- "shipped" changed to "house profiles". Actors named for require, accept,
  refuse, and ignore. American spellings (period, acknowledgments, grays).
  Print and Circulating edition names glossed once. "chapter opening" or
  "capital" in place of "initial". The backslash rule is limited to
  double-quoted YAML strings. Line 103 no longer says `press check` renders.
- Fact desk drifted 1 to 11 and missing 1, 3, 4, 5 are applied (`press
  cover` subject chain with its last step, the drop-cap wording, era
  "1935 onward", "key by key", the coverwrap needs *assets/cover.jpg*,
  "the one immutable field", PCN expanded per facts-E, `--dry-run` noted,
  the `171717 ink` quirk, `press art enhance` reading `plates.medium`).
- Copy desk blocks 1 and 2 and every should (3 to 36) are applied. Mays
  applied: 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49.

Declined:
- Fact missing 2 (`raised-cap` renders like `drop-cap`): the fact base
  lists it under 20.B, behaviour that looks like a bug and that writers
  must not document.
- Copy may 42 ("returns"): `press config list` itself calls it the
  "returns page", so the appendix keeps that word.
- Type desk 2 to 4 (inline definition terms, an entry split across a page,
  sections absent from the contents): these come from the house template
  and toc-depth, and the file cannot fix them. Type 1 (Chapter 16's
  counter) is fixed with `{-}` on every head.

To fit the band I cut redundant `--json` reminders, two "listed under"
pointers, and the scaffold's `page-thickness` example.
