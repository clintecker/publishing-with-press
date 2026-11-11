# Re-review: Chapter 2, Installing press

Scoped re-review of `book/chapters/02-installing-press.md` (revised, 381
lines) against the blocks and should findings in `facts-02.md`, `dev-02.md`,
`copy-02.md`, and `type-02.md`, the writer's "Revision" section in
`report-02.md`, the rulings in `docs/production-ledger.md`, and supplement
sections S1 and S2 of `docs/briefs/facts/facts-02.md`. Line numbers refer to
the revised chapter.

Severity of the fact desk's lists comes from `desks/fact-checker-02.md`:
Unsupported and Contradicted are blocks, Drifted is should, Missing is may.
Unsupported 10 is marked "low stakes ... editor's call" by the desk and is
treated as may. May items are out of scope and are not tabled.

## Runs

- `press check`: fails only on "plate never referenced by the manuscript"
  for `assets/woodcuts/02-01-doctor-report.png` and
  `02-02-tools-in-the-build.png`, the stale placeholder names after the
  ruling-4 renumbering (known artefact). Nothing against the chapter text.
- `python3 tools/ste_check.py`: 52 findings, 389 sentences, average 12.5
  words, maximum 38. Every residual is a gerund heading, an art directive or
  fig-alt (135, 136, 218, 310), the index comment (381), a semicolon inside a
  verbatim quotation (43, 178, 180), the footnote-marker join (35), a target
  name or flag ("verify", "check out"), a contract-kept word ("therefore",
  "whether"), "harness" inside the dev-render quotation (315), or an
  adjectival "is broken" (351). The 29-word sentence at 180 and the
  25/26-word sentences at 317, 364, 373 are under the 30-word ceiling. No
  prose defect.
- `press figures`: all three Chapter 2 figures report `directive: ""` and
  `description: None` (see open item N1).

## Findings

### Fact checker (facts-02.md)

| Desk | No. | Sev. | Status | Where / note |
|---|---|---|---|---|
| facts | Unsupported 1 | blocks | resolved | 237 pointer reworded; 276 "draws the same line" |
| facts | Unsupported 2 | blocks | resolved | no "first book" or "real time" left; 202 cites the scars list |
| facts | Unsupported 3 | blocks | resolved | ruling 3: 308, 310, 311 name epubcheck and Java only |
| facts | Unsupported 4 | blocks | resolved | 43 |
| facts | Unsupported 5 | blocks | resolved | Example 2.3 uses S2's two forms; 107 explains the path form |
| facts | Unsupported 6 | blocks | resolved | 66 |
| facts | Unsupported 7 | blocks | resolved | 268 |
| facts | Unsupported 8 | blocks | **open** | sidebar fixed, but 367 reintroduces "silent" (see O2) |
| facts | Unsupported 9 | blocks | resolved | 376 has no timing |
| facts | Contradicted 1 | blocks | resolved | ruling 2: 247 |
| facts | Contradicted 2 | blocks | resolved | 290, 371 |
| facts | Contradicted 3 | blocks | resolved | 245 |
| facts | Drifted 1 | should | resolved | Table 2.3 verbatim in code, matches the capture |
| facts | Drifted 2 | should | resolved | 232, 237 |
| facts | Drifted 3 | should | resolved | 329 |
| facts | Drifted 4 | should | resolved | 223 |
| facts | Drifted 5 | should | resolved | 230 |
| facts | Drifted 6 | should | resolved | 250 |
| facts | Drifted 7 | should | resolved | 239 |
| facts | Drifted 8 | should | resolved | 261 |
| facts | Drifted 9 | should | declined-accepted | the aligned line is 76 columns with its prompt, over the fence cap; 165 discloses the narrowing |
| facts | Drifted 10 | should | resolved | 323 |
| facts | Drifted 11 | should | resolved | 371 |
| facts | Drifted 12 | should | resolved | 127 |
| facts | Drifted 13 | should | resolved | 325 |

### Developmental editor (dev-02.md)

| Desk | No. | Sev. | Status | Where / note |
|---|---|---|---|---|
| dev | B1 | blocks | resolved | 313 to 319, "The developer's render loop", after "Building a book inside the image"; faithful to S1 (see below) |
| dev | P1 | should | resolved | 45 to 66 and Example 2.1, per the S2 ruling (but see new item O4) |
| dev | P2 | should | resolved | procedure ends at the doctor (Example 2.7); 290 says Chapter 3 creates the repository; Example 2.2 has no `cd` |
| dev | P3 | should | resolved | ruling 2: 247 |
| dev | P4 | should | resolved | Example 2.3 |
| dev | P5 | should | **open** (part) | target 131, scar 202, composite action 127, reusable workflow 282 are fine; "release contract" is used at 210 and defined only at 286 (see O3) |
| dev | P6 | should | resolved | 210 |
| dev | S1 | should | resolved | 355, sidebar, 367 |
| dev | S2 | should | resolved | 237 keeps mechanism and pointer only |
| dev | S3 | should | resolved | licence and Chrome cut; 33 keeps the CI detail |
| dev | S4 | should | resolved | 70 points forward; 286 closes the argument |
| dev | S5 | should | resolved (equivalent) | Example 2.7 shows the ready line and `echo $?` printing `0`; nothing invented |
| dev | S6 | should | resolved | 331, 333; no claim about a Windows host |
| dev | S7 | should | resolved | blank line after the sidebar at 366 |
| dev | S8 | should | resolved | ruling 4: files 02-01 tools, 02-02 doctor, 02-03 topology, in reading order |
| dev | S9 | should | resolved | Table 2.3 header "What the doctor prints", cells verbatim |

### Copyeditor (copy-02.md)

| Desk | No. | Sev. | Status | Where / note |
|---|---|---|---|---|
| copy | 4 | should | resolved | 33 |
| copy | 5 | should | resolved | 33 |
| copy | 9 | should | resolved | 95 |
| copy | 12 | blocks | resolved | 333 |
| copy | 14 | should | resolved | 131 (definition restated with the term as object) |
| copy | 15 | should | resolved | 157, "e-book", no "validator" |
| copy | 19 | should | resolved | Tip deleted; sentence ends the 180 paragraph |
| copy | 22 | should | resolved | Warning at 186 precedes Example 2.5 |
| copy | 25 | blocks | resolved | ruling 7: "shipped" survives only inside the quoted scar (250) |
| copy | 27 | should | resolved | 270, "the Ubuntu launcher it replaces hides a failure" |
| copy | 28 | should | resolved | 273 |
| copy | 29 | should | resolved | 276 |
| copy | 31 | should | declined-accepted | `docs/markup.md` line 49 sets a directory in italic; the typesetter agrees |
| copy | 33 | should | resolved | 327 |
| copy | 35 | should | resolved | 333 |
| copy | 37 | blocks | resolved | 355 |
| copy | 39 | should | declined-accepted | superseded by ruling 1; the body now sets up the sidebar in one sentence and the sidebar does not repeat it |
| copy | 40 | should | resolved | 358, "The first-run font scan" |
| copy | 42 | blocks | resolved | sentence gone |
| copy | 44 | should | resolved | 371 |
| copy | 45 | should | resolved | 371 |
| copy | 46 | should | resolved | 373 ends at "the strict gate"; Tip kept |
| copy | 47 | should | resolved | 278 |
| copy | 48 | should | resolved | 325, with Drifted 13 |

### Typesetter (type-02.md)

| Desk | No. | Sev. | Status | Where / note |
|---|---|---|---|---|
| type | 1 | blocks | resolved | ruling 5; `press check` passes the paragraph law |
| type | 2 | blocks | resolved | as 1 |
| type | 3 | blocks | resolved | sidebar 142 words, under the 180 cap |
| type | 4 | should | resolved | 2.1 30/50, 2.2 44/48, 2.3 24/56; 2.4 is 16/56 (about 22 percent), adequate for seven-character states (not re-rendered) |
| type | 5 | should | resolved | ruling 8; report-02 capture drops the bare line |
| type | 6 | should | declined-accepted | superseded by ruling 8 (captures stay verbatim and wrap) |
| type | 7 | should | resolved | ruling 4 |
| type | 8 | should | resolved | Example 2.7, captioned, referred to at 337 |
| type | 9 | should | resolved | italic file and directory names throughout |
| type | 10 | should | resolved | 366 |
| type | 11 | should | resolved | each definition follows its paragraph |

### New items found on re-review

| Source | No. | Sev. | Status |
|---|---|---|---|
| ledger ruling / markup.md (4bcfc2f) | N1 | blocks | **open** |
| reader's pass | N2 | should | **open** |
| markup.md (074b172, after the revision) | N3 | should | **open** |

## Supplement use (S1, S2)

**S1, dev-render.** Correct. The B-head quotes the header verbatim ("the
developer harness for the exact bytes CI builds on"), gives the read-only
mount, `python -m press` from *src/*, no reinstall, the image read from
*build.yml* so it matches the release contract's pin, the defaults (PDF,
the Alice example, *build/dev-render*), `--book`, `--out`, `--preview`,
`--shell`, and the target list exactly as S1 gives them. The CLAUDE.md
quotation ("the edit-render-look loop, not the proof", verify.sh as the gate)
is accurate. The audience is stated (press developers, "a book author never
needs it"). Leaving out the Colima limit (#276) is a sound call for that
audience.

**S2, install environment.** Correct. The venv is "we recommend" and "this
advice is ours" (47), PEP 668 is attributed to Python, not press, and the
chapter says the install guide does not mention virtual environments. The
INSTALL.md quotations at 43, 178, 180, and 331 are verbatim. Example 2.1
activates the venv in place of S2's `~/.press-venv/bin/pip` form, which is
equivalent. Example 2.3's two extras forms match S2, with `$HOME` in place
of the placeholder path. One consequence of the venv advice is not covered
(N2).

## Open items

**N1 (blocks). The three `art:` comments sit before their image lines.**
Lines 135/136, 218/219, 310/311, for example:

> `<!-- art: ARCHETYPE data-flow, top to bottom. ...-->`
> `![Where each tool in the toolchain sits in the build](assets/woodcuts/02-01-tools-in-the-build.png){#fig:tools-in-the-build ...}`

The ledger's correction ("the art: comment goes AFTER the image line
(figures.py) ... chapters 1 to 4 must move theirs in revision") and
`docs/markup.md` ("a comment before the image belongs to nothing") were
both committed (4bcfc2f) before this revision. `press figures` confirms it:
all three Chapter 2 figures report `description: None`, so the illustrator's
brief is attached to nothing. Chapter 4 has already moved its comments.
Fix: move each `art:` comment to the line directly after its image line
(at most one blank line between them), text unchanged. Re-run
`press check` to confirm each pair stays under 190 words, and
`press figures` to confirm each description is attached.

**O2 (blocks, fact Unsupported 8, partial). Line 367 reintroduces the
cut claim about output.**

> "If a build on a fresh machine stays silent for several minutes, wait: it
> is almost certainly the scan."

The fact checker found "the build prints little or nothing" unsupported.
The file says only that the scan "looks like a hang". Fix: "If a build on a
fresh machine seems to hang for several minutes, wait: it is almost
certainly the scan." (The sidebar's "Nothing about it looks like progress"
at 360 restates "looks like a hang" and can stand.)

**O3 (should, dev P5, partial). "release contract" is used before its
definition.** Line 210:

> "It runs the same toolchain image, pinned by the same digest, that the
> press's release contract proved."

The defining clause appears only at 286 ("The *release contract*, the
workflow that proves each press tag"). Fix: move the definition to 210:
"that the press's *release contract*, the workflow that proves each press
tag, proved." At 286, drop the italic and the clause: "The release
contract refuses a three-part tag whose workflow names only a `sha-` tag."

**N2 (should). Example 2.1 fails on a fresh Ubuntu 24.04 with the
chapter's own package list.** Line 58: `$ python3 -m venv ~/.press-venv`.
On Debian and Ubuntu, the `venv` module needs the `python3-venv` package
(`ensurepip` is otherwise missing, and `python3 -m venv` stops with an
error that names the package). Example 2.5's list installs `python3` and
`python3-pip` but not `python3-venv`. The reader on the reference platform
therefore meets an error at the first command, the same failure class as
P1. The fact is general Debian packaging, like PEP 668, and is not in
facts-02. Fix: the controller adds it to S2 (with the same "Python's rule,
not press's" framing). Then the writer adds one sentence after Example 2.1,
for example: "On Debian and Ubuntu, the `venv` module comes in a separate
package. If `python3 -m venv` reports that it is missing, run
`sudo apt-get install python3-venv` and try again." Do not change Example
2.5, which reproduces the *Dockerfile*'s list.

**N3 (should, law changed after the revision). Three fence lines exceed the
new 64-column cap.** `docs/markup.md` (074b172, committed two minutes after
the chapter was saved) now caps code lines at 64, because an untagged fence
does not wrap in the PDF. Three lines are 66 columns:

- 60: `$ pip install "press @ git+https://github.com/clintecker/press@v3"`
- 172: `$ brew install --cask mactex-no-gui  # lualatex, latexmk, TeX Live`
- 174: `$ brew install epubcheck  # optional: the retail EPUB gate locally`

Fix: break line 60 with a trailing backslash, as Example 2.3 already does
(`$ pip install \` then `    "press @ git+https://github.com/clintecker/press@v3"`).
For 172 and 174, show the bare commands and move the two comments into the
prose, which already explains both (178 for MacTeX, 180 for epubcheck).
Then change the sentence at 165, which says the commands appear "with
their comments" and that the spacing was narrowed, to match.

## Notes (not counted)

- 157: "The epubcheck program is the program that ..." is the copyeditor's
  own fix, but the repetition reads awkwardly. "Epubcheck is the program
  that ..." would do. May.
- 373: "If the only complaint concerns epubcheck" does not say whose
  complaint. After the procedure moved to the doctor, a missing epubcheck
  no longer makes the doctor complain (`absent` keeps a machine ready).
  "If the only fault concerns epubcheck" or "If epubcheck is the only thing
  missing" would be clearer. May.
- 127 and 282 both define a thing "that a book's CI calls" (the composite
  action and the reusable workflow). Both are true; Chapter 14 can sort the
  layering. May.
- 351 infers "no required tool is missing and no tool is broken" from the
  ready rule; the undefined `warn` state could also bear on readiness. Low
  risk. May.

## Reader's pass

Read once straight through as the design's reader. The path now works: the
venv is chosen before the first command (subject to N2), the extras are
shown in a form that runs, the doctor's surprise is explained where the
figure shows it, the image and dev-render sections hand off cleanly, and
the first run stops at a result the reader can actually reach in this
chapter before Chapter 3 makes the book. The font scan is told once. No
new fact appears that is outside facts-02 apart from the general packaging
points already ruled on.

## Verdict

**REVISE.** Open: 2 blocks (N1, O2) and 3 shoulds (O3, N2, N3). All five
are small and mechanical: move three comments, change one word, move one
defining clause, add one sentence once the controller supplies the
`python3-venv` fact, and rebreak three code lines. A writer pass on those
five items alone, followed by `press check` and `press figures`, should
reach APPROVED without another full desk round.
