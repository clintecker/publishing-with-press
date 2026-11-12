# STE80 review: Appendix A, Command reference

File: `book/appendices/a-command-reference.md`, reviewed against
`git diff HEAD` and the editor's report `docs/briefs/reports/ste-a.md`.

Status: **APPROVED**. Blocks 0, should 0.

The diff holds exactly the ten hunks the report lists, and nothing else.
No code span, path, flag, message, or identifier changed. The three
sentinels are not in this file (they live in chapters 01, 08, and 16) and
are untouched. `press check` exits 0, and `tools/ste-ratchet.py` holds the
file at 4, its baseline.

## Findings

None.

## The three hard cases, checked

1. **Line 118, Table A.3, `--as cover`.** Old: "...within 3 percent of the
   ratio of the legacy `trim` field (6 by 9 unless set), not the
   profile's." New: "...within 3 percent of the ratio of the legacy `trim`
   field, not the profile's. That field is 6 by 9 unless set." The fact
   file (facts-A, discrepancy 17) says intake reads `metadata.trim`,
   default 6x9, not the profile. Both halves survive at full strength. "At
   the time of this writing" still governs the check against the legacy
   field, which is the behavior the qualifier exists for; the default is
   not the time-bound part. "That field" has one antecedent: "the
   profile's" elides "ratio", and a profile has no field. No finding.
2. **Line 396, `press config validate`.** Old: "...reports each file on
   its own line, the absent optional files included, as `ok` or with its
   problems." New: "It reports each file on its own line, as `ok` or with
   its problems. The absent optional files get a line too." Checked
   against press `src/press/config_cli.py` `_validate`: the loop runs over
   every file in `schema.FILE_VALIDATORS` whether or not it exists and
   prints `<file>: ok` or the problem count and list. "too" keeps the
   inclusion, and the format clause still covers every line. No finding.
3. **Line 1012, Table A.17, `--max-claims-per-file N`.** Old: "A positive
   cap takes a sample of the claims, and the workflow's accounting reports
   the claims it left out." New: "With a positive cap, the workflow
   samples the claims, and its accounting reports the claims it left out."
   Checked against press: `operator.py` passes the cap to the
   `authorities-research` workflow as `maxClaimsPerFile`, and the workflow
   applies it (`authorities-research.js` line 31 returns at most CAP claims
   and `totalFound`; line 40 logs the omitted count). The workflow's own
   `whenToUse` says "a positive cap samples and the accounting discloses
   omissions". Naming the workflow as the actor is correct, and "its"
   refers to the workflow as "the workflow's" did. No finding.

## The other seven, checked

- Line 3: the gloss "the book's sample, slug `alice`" moved to its own
  sentence, verbatim. Paragraph now six sentences.
- Line 15: split at "and"; the condition was already first in its clause.
  Paragraph six sentences.
- Line 25: split; "at least two digits" and `z-` kept.
- Line 54: "naming" to "that names"; same meaning.
- Line 112: "During intake" restates the colon's relation. The italic
  definition of *intake* and the path *art/commissions.md* are intact.
- Line 509: split; the state list `ok` ... `unset` is verbatim.
- Line 1329: condition first; index term "exit status" kept.

Voice: the appendix is reference prose with no Light-mode passage. The
splits leave lengths varied in each paragraph. No term in
`docs/vocabulary.md` changed.
