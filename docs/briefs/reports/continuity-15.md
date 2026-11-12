# Continuity report: Chapter 15, *The operator's desk and the editorial machines*

Desk: continuity editor. Chapter read as it stands after its desks, its
re-review, and the second revision (405 lines). Cross-checked against
Chapters 1 to 12 (committed), Chapter 16 and Appendixes A, B, D, E where
they share facts with it, `docs/vocabulary.md`, `docs/design.md` section 5,
facts-07 and facts-15, and the press source (`src/press/desk/`,
`desk_model.py`, `catalog.py`, `__main__.py`, `doctor.py`) where two
chapters had to be judged against each other.

Status: **PASS WITH FIXES.** One block, three should, seven may. The block
is a contradicted shared fact (what `press pdf` does, against Chapters 7
and 8 and Appendix A). The three should are a second sense of *target*, a
second name for the art directive, and a second name for a skill.

What holds:

- **Chapter 2's promises are kept.** The doctor panel (Ch. 2 l.262) is the
  doctor table at l.49 and Table 15.1, which names it "the panel that
  Chapter 2 promised". The operator commands (Ch. 2 l.165) are Table 15.6
  and "Running a workflow headless" (l.311 to 368). The `tui` extra and its
  hint (l.34) match Ch. 2 Example 2.3 and App. A l.490 to 495, and the hint
  string matches *desk/__init__.py* l.22 exactly. "At the end of Chapter 2,
  `alice` repaired `claude`" (l.182) matches Ch. 2 l.347 (Example 2.7, after
  the `BROKEN` line of Figure 2.2, l.224).
- **Chapter 11's promises are kept.** Skills and workflows "run in Claude
  Code, an agent program whose command is `claude`" (Ch. 11 l.55) is l.28;
  how a workflow runs (Ch. 11 l.375) is l.172 to 191 and l.311 to 338. The
  definitions agree: *skill* (Ch. 11 l.47, "a packaged authoring guide that
  an agent reads"; Ch. 15 l.277 adds the file shape and the count, eleven),
  *workflow* (Ch. 11 l.49; Ch. 15 l.26), the Workflow tool (Ch. 11 l.49;
  Ch. 15 l.28, 172). The `art-direction` facts agree with the shared fact
  "The commission record": `maxPlates` 8 (l.267), *art/commissions.md*,
  "Accepted" lines under `## Acceptance record` (l.271), Workflow tool only
  (l.273; Ch. 11 l.375, 490). `press aesthetic "<brief>"` runs
  `aesthetic-brief` through `claude` with `--overwrite` (Table 15.6; Ch. 11
  l.100; App. A l.51 to 60; App. B l.331).
- **Chapters 3, 7, and 10 are kept.** The stamp `// scaffolded by press
  3.0.2; source of truth: press data/workflows` (l.146) is Ch. 3 l.100 word
  for word; what the four workflows do (Ch. 3 l.100) is Table 15.4. The
  three desk markers (Ch. 7 l.456) are at l.83, and the back reference
  ("Chapter 7, *Building the editions*, describes the three markers") is
  kept by Ch. 7 l.454 to 456: phase lines with a pilcrow, plus-sign lines,
  time lines such as `pandoc took 26.7s` (two-space indent, one second or
  more). facts-07 item 169 names the same three; facts-15 l.46 names only
  two for the stage line, which the press code bears out (finding 8), and
  the chapter's "builds the stage line from those markers only" is true of
  both. The table of authorities and `press research` (Ch. 10 l.382) are
  l.248 to 257 and Table 15.6; the ledger is *config/authorities.yaml*, per
  the vocabulary ruling (l.250).
- **`press check` closing each round agrees with Chapters 6 and 7.** The
  law phase "runs `press check` until it passes" (l.139, 220; Figure 15.2's
  brief) and the wizard's "next: press check" (l.127) rest on the shared
  facts "What runs the checker" and "Exit status": `press check` runs the
  four passes and only its exit status decides (Ch. 6 l.469 to 498; Ch. 7
  l.420). The house law of Example 15.2 states the paragraph law as "under
  190 words" (shared fact "Paragraph law") and the dash and quote law
  (shared fact "Dash and quote law"); it is the workflow's own string, and
  l.232 keeps the checker as the enforcer. The authorities workflow ends in
  `press pdf` (l.255), which is consistent with Ch. 10's check of the ledger
  on every build and does not claim the checker runs.
- **Defaults and flags agree with Appendix A.** `rounds` 2, `--rounds N`
  not in `--help` (Table 15.6; App. A l.663 to 673); `maxClaimsPerFile` 0
  (l.250; App. A l.1004); `--apply` grants the full Bash tool instead of
  `press` and `python3` (l.338; App. A l.672); counsel mode fingerprints
  *book/* and *config/* (l.346; App. A l.666; App. E l.96). Eleven skills,
  `book-aesthetics` first, `overused-jargon` last (Table 15.5; App. A l.1075,
  1083). Desk keys `p`, `w`, `r`, `q` (Table 15.2; App. A l.486). The live
  states `-`, `o`, `/` (Table 15.3; App. E l.144).
- **The watchlist skill agrees with Chapters 4 and 6**: *references/
  watchlist.csv*, two copies of the lint kept identical (l.301 to 308;
  shared fact "Jargon lint and watchlist", which says `press selftest`; the
  chapter's "byte-parity contract" is the same guard, unnamed).
- **Cast.** `alice` on `hatter`, *~/alice*, and `/Users/alice/alice` (l.176;
  Ch. 8 l.390, App. A l.1293 to 1296 agree). No other sample name.
- **Cross-references out** are right in number and title: Chapter 2,
  *Installing press* (l.34; bare at l.49, 182); Chapter 7, *Building the
  editions* (l.83); Chapter 3, *The shape of a book repository* (l.146);
  Chapter 10, *Front matter, the index, and the table of authorities*
  (l.250); Chapter 11, *The art department* (l.267; bare at l.297). The
  three "later in this chapter" sections are later: "Skills" (l.135 to
  l.275), "Running a workflow headless" (l.170 to l.311), "Why the diseases
  are hard-coded" (l.204 to l.370). "Step 6 of the procedure in the section
  'Workflows'" (l.238) points back to l.189, inside that A-head.
- **Numbering.** Figures 15.1 `15-01-the-desk` and 15.2
  `15-02-editorial-passes-machine`, design.md order, each cited before it
  appears (l.43, 206), both PNGs present; plate *the-proofreaders-bench.png*
  unnumbered, present, as design.md names it. Tables 15.1 to 15.6, Examples
  15.1 to 15.5, no gap, no repeat. Three uncaptioned fences (l.36, 174,
  348), none referred to by number. Footnotes `15-pipe`, `15-popen`,
  `15-counsel`, prefixed and unique. The In-this-chapter box matches the ten
  A-heads.

## Findings

### 1. `press pdf` does not run a verifier (blocks)

> "A target runs fixed code: `press pdf` builds the Print edition (the PDF),
> and its verifier decides the result." (l.30)

Rule: shared facts agree (rule 7). Chapter 7 Table 7.1 (l.28) has `press
pdf` build the reading PDF and nothing more; Chapter 8 l.59 gives the
verifier to `press verify` ("builds *dist/alice.pdf* and then runs
`verify_pdf`"); App. A l.211 and the shared fact "What runs the checker"
agree. In the code `pdf` is a build target and `verify` a separate one
(*catalog.py* l.35, 48; *__main__.py* `verify_built`). Fix: "`press pdf`
builds the Print edition (the PDF), and its exit status decides the result",
or name `press verify`: "`press verify` builds the Print edition (the PDF)
and its verifier decides the result." The rest of the paragraph ("end by
running a target, `press check` or `press pdf`, whose exit status decides")
already says it right.

### 2. *Target* in two senses (should)

> "Every action press takes on a book starts as a target, and you can type
> the target at the shell prompt or pick it from a list on the desk." (l.22)
> "Every action the desk runs is a target you can type yourself." (l.24)

Rule: a term must not be redefined differently (rule 2). Chapter 1 and
Chapter 2 (term table: *target*, "Not the operator commands") and this
chapter's own l.28 to 30 ("A target and an operator command differ") keep
the operator out of *target*. The picker is built from the whole catalog
(l.79), which holds `improve`, `research`, and `aesthetic` (*catalog.py*
l.124 to 126) as well as `doctor`, `config`, `new`, and the rest. So the
desk can run an operator command, which l.22 and l.24 call a target. Fix:
"command" in l.22 and l.24 ("Every action ... starts as a `press` command";
"Every action the desk runs is a command you can type yourself"), keeping
"target picker" as the desk's name for its list. The press quotation at
l.22 ("a `press <target>` you can type yourself") is the press's own and
stays.

### 3. "`art:` description" for the art directive (should)

> "A plate commission comes from each declared generatable figure that
> carries an `art:` description." (l.269)

Rule: one name per thing (rule 2; vocabulary). Chapter 5 defines the
*directive* (l.57; Example 5.1 "A plate and its art directive") and Chapter
11 says "an `art:` directive" (l.375, Figure 11.1 brief). *Figure* here also
stands for the general class; the vocabulary keeps *figure* for the numbered
kind and *illustration* for the class, and Chapter 5's term is *generatable
kind* (l.26). Fix: "A plate commission comes from each declared illustration
of a generatable kind that carries an `art:` directive."

### 4. "Authoring guides" before *skill* (should)

> "The workflows are the agent route, and they read the authoring guides
> that come with press." (l.18)
> "The *prose skills* it mentions are four of the authoring guides that come
> with press, described in the section 'Skills' later in this chapter."
> (l.135)

Rule: one name per thing (rule 2); the vocabulary bars "guide" for a skill;
first use italic and defined. The thing is called "the authoring guides" at
l.18 and l.135, and "skill" first appears roman at l.135 ("its workflows and
skills as package data"), 142 lines before its definition (l.277). The
genus "a packaged authoring guide" inside the definition is Chapter 11's
and is fine. Fix: at l.18, "they read the skills, the authoring guides that
come with press"; at l.135, "four of the skills, described in the section
'Skills' later in this chapter", with *skill* italicized at its first use or
the gloss moved up.

### 5. The workflow definition and two of the four (may)

> "A *workflow* is a packaged agent procedure: a script that dispatches
> language-model agents, gathers what they return, and runs press targets to
> check their work." (l.26)
> "The other two end in an audit by another agent." (l.30)

Rule: internal agreement. `aesthetic-brief` and `art-direction` run no
target (l.263, 271). App. E l.435 repeats the l.26 gist. The bible's gist
(Ch. 11) is only "a packaged agent procedure". Fix: "... gathers what they
return, and checks their work, two of them by running a press target."

### 6. `missing` and `broken` against Chapter 2's `MISSING` and `BROKEN` (may)

> "| `!` | The doctor reports the tool `missing` or `broken`. ..." (Table 15.1)

Rule: shared fact "Doctor states" (Ch. 2 Table 2.4 l.236 to 242, Figure
2.2). The doctor prints the failing states in capitals; the typed findings
and the desk's word beside the glyph are lowercase (*doctor.py* l.56 to 59;
*desk_model.py* l.35 to 42), so the table is right about the desk and reads
as two state names against Chapter 2. Fix: "The doctor reports the tool
`MISSING` or `BROKEN`; the desk prints the word in lowercase." `absent`,
`unset`, and `warn` are the same in both.

### 7. "Headless" for the operator route (may)

> "## Running a workflow headless" (l.311; also l.14, 170)

Rule: vocabulary, *operator*: never "headless mode". The chapter uses the
adjective for the route, not as a name for the commands, and Chapter 11
l.100 says "headlessly"; the operator is named at l.28 and in Table 15.6.
No change needed; recorded so that no later chapter calls the operator
"headless mode".

### 8. The time lines reach the desk but not the stage line (may)

> "The desk builds the stage line from those markers only" (l.83)

Rule: shared fact "Log forms". In *desk_model.py* `progress_event` parses
all three markers (l.104 to 120), and `RunProgress.observe` ignores a timing
(l.133 to 145): the stage line counts plus-sign lines as steps and ticks the
phases. Chapter 15 is correct. Chapter 7 l.456 ("uses the phase lines, the
plus-sign lines, and the time lines to show its progress") claims a little
more than the code does. No change to Chapter 15; errata note for Chapter 7
if the copy desk wants it exact.

### 9. The Preface's line for Chapter 15 (may, for the Preface pass)

> "Shows the desk, the four workflows and their skills, and why the
> editorial passes name the faults of machine prose outright." (Preface
> l.68)

Rule 8. In substance it covers seven of the ten A-heads; it leaves out the
operator ("Running a workflow headless": `press improve`, counsel mode,
`--apply`), which design.md section 5 names. Fix: "... the four workflows
and their skills, the operator commands that run them for you, and why ..."

### 10. Appendix A breaks the desk hint without saying so (may, for App. A)

App. A l.494 to 495 prints the hint on two lines; press prints it on one
(*desk/__init__.py* l.22), as Chapter 15 l.34 quotes it. Fix in App. A: one
line, or "broken here to fit the page", the chapter's own convention.

### 11. Noted for other desks (no continuity rule)

- l.95 "holds a one-character glyph": the desk prints the glyph and its
  word (`o present, unverified`; *desk/app.py* l.36 to 42, 105), as the
  State column of Table 15.3 implies. The Figure 15.1 brief (l.47) asks for
  "-" and "o" rows only. For the fact desk and the art capture.

## Bible changes

Added to `docs/continuity.md`: nine term rows (read model, catalog, prose
skills, maxim quota and coined maxim, the four editorial-passes phases, the
three whole-book lenses, counsel mode, the named diseases, the house law),
eleven shared-fact rows (desk install and launch; desk home screen; desk
keys and picker; RUN view; evidence states; setup wizard; the four
workflows' arguments and defaults; editorial-passes rounds; `press
workflows` entries; the skills; operator runs and counsel mode), eight
reference rows from Chapter 15, and the Chapter 15 numbering row; 29 in
all. Updated in place: the term rows for the desk, the operator, skill,
workflow, the Workflow tool (line numbers to the 405-line text); the shared
facts "Doctor's ready line and status", "Doctor states", "Log forms",
"Jargon lint and watchlist", "What spends money", "Table of authorities
rules", "The aesthetic file", "The commission record", "Name of
*alice-sources.md*"; the reference rows 2 (l.165), 2 (l.262), 3 (l.100), 7
(l.456), 15 (l.81), 10 (l.382), 11 (l.55, 375), and the Ch. 10 and Ch. 11
collected rows; and the Preface section (Chapter 15's final A-heads).
