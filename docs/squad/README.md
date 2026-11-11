# The squad: who holds what

Every desk below is a role a subagent is dispatched into with the brief in
this directory. The controller (the session running production) is the
managing editor: it sequences work, rules on conflicts, and commits. No
desk commits; no desk dispatches other agents. Each desk writes its report
to `docs/briefs/reports/` and returns a short status.

| Desk | Holds | Gate it owns | Brief |
|---|---|---|---|
| **Managing editor** (controller) | the schedule, the ledger, every ruling, every commit | nothing ships without its sign-off | this file |
| **Writer** | one chapter's prose, examples, tables, and figure briefs | the chapter exists and passes `press check` | `docs/briefs/brief-NN.md` |
| **Fact checker** | every technical claim against the fact file; nothing invented, nothing from the contradiction list | no claim without a source | `fact-checker.md` |
| **Developmental editor** | structure, coverage of the A-heads, the reader's path, what is missing and what is padding | the chapter does the job its design row names | `developmental-editor.md` |
| **Copyeditor** | the prose contract sentence by sentence, the period voice, the tells, grammar, spelling, the era touches | no defect on the one-sighting list | `copyeditor.md` |
| **Continuity editor** | one term per thing, the fixed cast, cross-references that point where they claim, numbering, promises one chapter makes that another must keep, the continuity bible | the book reads as one book | `continuity-editor.md` |
| **Typesetter** | the markup guide, figure and table conventions, code width, caption form, what will break a build or a verifier | `press check`, `press pdf`, and the figure rules pass | `typesetter.md` |
| **Illustrator** | drawing every numbered figure from its `art:` brief in the house look | every figure matches its brief and the look rules | `illustrator.md` |
| **Art director** | plates and the cover: commissions, intake, enhancement, the aesthetic | the art obeys the design skills | `art-director.md` |
| **Indexer** | `config/index-terms.yaml` from the chapters' candidates, flat terms that hit | the index builds and every term lands | `indexer.md` |
| **Production editor** | the full build in the toolchain image, the rendered pages, layout faults, the print pack, the Pages site | `press all`, `verify-print`, and the coverwrap pass; the pages look right | `production-editor.md` |
| **Proofreader** | the final rendered PDF, page by page, against the manuscript | no typo, no widow, no dangling reference reaches the release | `proofreader.md` |

## The loop for a chapter

1. The writer drafts from the brief and reports.
2. Four desks review in parallel from the same commit: fact checker,
   developmental editor, copyeditor, typesetter. Each writes a numbered
   findings file. Findings are quotes with a fix, never a rewrite.
3. The managing editor merges the findings, rules on conflicts between
   desks (a fact beats a style note; the markup guide beats taste), and
   resumes the writer with the merged list.
4. The writer applies the list and reports. One scoped re-review by the
   desk that raised each surviving finding.
5. The continuity editor reads the finished chapter against the continuity
   bible, updates the bible (terms introduced, cast used, promises made,
   cross-references out), and raises any conflict with earlier chapters.
6. The managing editor commits the chapter.

## The loop for the book

After the last chapter:

1. The continuity editor reads the whole manuscript in order against the
   bible: every "see Chapter N" lands, every term is one term, every
   "later in this chapter" is later, every number is in sequence, the
   Preface's Organization section matches the chapters.
2. The illustrator draws every figure; the art director finishes plates
   and cover; the indexer builds the index; the production editor builds.
3. The proofreader reads the rendered PDF.
4. A final whole-book review on the most capable model, as a reader who
   has not seen the plan.

## Rules of the house for every desk

- Quote, number, fix. A finding is the exact current text, what is wrong,
  which rule says so, and the smallest change that repairs it. "Consider
  tightening" is not a finding.
- Severity in three words: **blocks** (a wrong fact, a build breaker, a
  one-sighting tell), **should** (a rule of the contract or guide), **may**
  (taste). The writer must resolve every blocks and should, and may decline
  a may with a reason.
- Never invent a fact to fix a fact. If the fact file is silent, the fix is
  to cut the claim.
- Keep code, paths, flags, numbers, and versions verbatim.
- Report to the file; return a five-line status.
