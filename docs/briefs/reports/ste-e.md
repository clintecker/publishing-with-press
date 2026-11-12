# STE80 report: Appendix E, Glossary

File: `book/appendices/e-glossary.md`. Mode: Humanize (glossary entries).

## Ratchet count

- Before: 4 (baseline in `tools/ste-baseline.json`: 4)
- After: 1
- `press check`: passed (exit 0).

## Edits (14)

| Line | Rule | Old | New |
|---|---|---|---|
| 12 | S6 | ...with slug `alice`, kept by the user `alice` on the workstation `hatter`. | ...with slug `alice`, which the user `alice` keeps on the workstation `hatter`. |
| 21 | S8 (-ing) | A file in *book/appendices/* whose name is one lowercase letter, a hyphen, and the rest, ending in `.md` | A file in *book/appendices/* whose name starts with one lowercase letter and a hyphen and ends in `.md` |
| 153 | S6 | The barcode symbology for an ISBN-13, drawn by press on the *cover wrap* | The barcode symbology for an ISBN-13, which press draws on the *cover wrap* |
| 168 | S1, S2 | Suggest sends one agent to each chapter file and three through the whole book, one per lens (cadence, repetition, and arc), and law runs `press check` until it passes. | Suggest sends one agent to each chapter file and three through the whole book, one per lens (cadence, repetition, and arc). Law runs `press check` until it passes. |
| 171 | S6 | The desk's glyph for an artifact, derived from content digests and never from a timestamp. | The desk's glyph for an artifact. The desk derives it from content digests and never from a timestamp. |
| 210 | S6 | ...through the acknowledgments, generated from *config/metadata.yaml* and *config/front-matter.yaml* | ...through the acknowledgments, which press generates from *config/metadata.yaml* and *config/front-matter.yaml* |
| 213 | S8 (-ing) | ...on an even page, facing the chapter that follows | ...on an even page, opposite the chapter that follows |
| 237 | S8 (-ing) | A book changes it through its own config, never by editing press | A book changes it through its own config, never through an edit to press |
| 321 | S1 | It first writes an exact backup and afterward a receipt under *.press/*, and it leaves the manuscript, the config, and the art alone | It first writes an exact backup and afterward a receipt under *.press/*. It leaves the manuscript, the config, and the art alone |
| 327 | S6 | ...for product records, written by `press onix` | ...for product records, which `press onix` writes |
| 375 | S6 | The PDF that goes inside the covers, built by `press print` | The PDF that goes inside the covers, which `press print` builds |
| 438 | S6 | A paragraph's last line of one short word, prevented by a finite `\parfillskip` | A paragraph's last line of one short word, which a finite `\parfillskip` prevents |
| 474 | S6 | The file `dist/<slug>-sources.md`, written from the *table of authorities* and published beside the book | The file `dist/<slug>-sources.md`, which press writes from the *table of authorities* and publishes beside the book |
| 480 | S8 (-ing) | ...reads an existing PDF into its agreement check without rebuilding it | ...reads an existing PDF into its agreement check and does not rebuild it |

## Leads declined

- Line 203, "floating": the bold term `floating tag` is the entry's head word, fixed by `docs/vocabulary.md`. It is a label, not a verb.

## Passives kept

- Line 45, "a regular expression mapped to a label": describes the data shape. No actor acts.
- Line 399, "recorded by hand in *config/qualification.yaml*": the fact base does not name who records it. Naming "you" or "the publisher" would add a fact.
- Line 513, "built on Ubuntu 24.04 and pinned by digest": the actor does not matter to the definition.
- Lines 189, 363 ("listed in the List of Figures/Plates") and 141 ("written for the illustrator"): participial descriptions in which the actor does not matter.

## Fidelity notes

- Line 21: "one lowercase letter, a hyphen, and the rest" became "starts with one lowercase letter and a hyphen". "The rest" is now implicit in "starts with". Same rule, parallel to the chapter-file entry.
- Line 213: "facing" became "opposite". Same relation on a spread.
- Lines 210 and 474 name press as the actor. Both follow CLAUDE.md and the vocabulary ("the generated front matter", "the generated sources companion").
- No sentinel occurs in this file. Every bold head term and every index-term spelling is unchanged. No code span, path, or quotation changed.
