# STE80 pass: brief and plan

Date: 2026-11-12. Requested by the author after publication: "an STE80
skill across all the prose", pointing at Dodaios/ste80-humanizer.

## What this is

The prose contract (`docs/prose-contract.md`) already adopted the STE80
method when the book was planned, and the copyeditors used its linter as
leads chapter by chapter. The published manuscript averages 12.5 words a
sentence. What remains is a book-wide conformance pass on the structural
rules (Pass 2, S1 to S15, at 80 percent), measured, reviewed for fidelity,
rebuilt, and held by a ratchet so it cannot drift back.

## Scope and mode

- Every file under `book/chapters/` and `book/appendices/`.
- Humanize mode (Pass 2 at 80 percent) on body prose, admonitions,
  footnotes, captions, prose table cells, glossary entries.
- Light mode on the Preface, sidebars, anecdotes, epigraphs.
- No strict mode. The book has almost no pure procedures, and strict STE
  bans "check" and "test" as verbs, which are press's own verbs.
- The contract's relaxations stand: however, therefore, whether, should,
  we recommend. Ceiling 30 words, target 16 to 22 on average.

## Tooling

- `docs/skills/ste80-humanizer/` vendors the skill (SKILL.md, references,
  MIT licence). `tools/ste_check.py` was already vendored.
- `tools/ste-ratchet.py` wraps the linter with the contract's thresholds
  and drops what is not the book's prose (art comments, image lines,
  quotations, title-case "-ing" words, the relaxed words). It compares
  per-file counts with `tools/ste-baseline.json` and fails when a file's
  count rises. `--update` lowers the baseline after a pass.
- `.github/workflows/book.yml` gained a `prose-ratchet` job that runs it on
  every push beside the press workflow. The book's law says machinery
  belongs in press. A structural prose lint behind a `house-rules.yaml`
  knob is item 3 of the contract's press wish list and is filed there. The
  job is the book-side stand-in until press ships it.

Baseline before the pass: 168 findings in 23 files (51 paragraphs over six
sentences, 42 sentences over 30 words, 32 "-ing" leads, 24 passive leads,
15 phrasal verbs, 3 perfect tenses, 1 progressive).

## The loop

1. One STE80 editor per file (`docs/squad/ste-editor.md`), in waves of
   eight, each editing only its file and writing `reports/ste-NN.md`.
2. `press check` and the ratchet after each wave.
3. One STE80 reviewer per file (`docs/squad/ste-reviewer.md`) on the diff
   against the published commit, for facts, verbatim material, voice,
   terms, markup.
4. The managing editor rules on findings, applies fixes, reruns check and
   ratchet, lowers the baseline, rebuilds in the toolchain image, runs
   verify-print, and proofs the index terms and sentinels.
5. Ledger entry, commit, push, CI green including the ratchet job.

## Hard constraints

Sentinels byte-identical. Every index term still hits (the build fails
otherwise). No code, command, message, quotation, or identifier touched.
Paragraphs under 190 words. No file outside `book/` changed by an editor.
