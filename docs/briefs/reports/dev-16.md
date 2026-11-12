# Developmental edit: Chapter 16, Inside the press

File: `book/chapters/16-inside-the-press.md` (5,646 words by `press
wordcount`). Read against `docs/design.md` sections 2 and 5 (row 16),
`docs/briefs/brief-16.md`, `docs/style-guide.md` section 2, and the
promises in `docs/continuity.md` that name Chapter 16.

Reader. The desk brief names the book's first reader, the author. Design
section 2 assigns Chapters 14 to 16 to the second reader, "a developer
asked to keep a group's book builds running", and the chapter says the
same thing in line 19. This edit judges the path for that developer: a
person who can read Python, has a book (`~/alice`) and a press clone
(`~/press`) on `hatter`, and wants to change the press without breaking
anyone.

Status: DONE_WITH_CONCERNS. 0 blocks, 17 shoulds, 1 note. Several fixes
need facts the writer does not have; each is marked **needs fact**.

## 1. Coverage

All eleven A-heads are present, in the brief's order, and match the "In
this chapter" box word for word.

| A-head | Verdict |
|---|---|
| A map of the package | Answers it. Table 16.1 and Figure 16.1 cover all sixteen areas. |
| The data flow, end to end | Answers it. See finding 11 on the figure. |
| One statement of each fact | Answers it: the catalog, the registry, *yamlio.py*, the generated docs, and the one planned duplicate (jargon parity). |
| The typed book model | Partly. It says the model is frozen, typed, and collects every problem. It does not show how a field is declared, which is what Ch. 3 l.126 promised ("shows how the model works": kind, required or not, default). Finding 6. |
| The adapters boundary | Answers the "what" and the "why". The "how", adding a helper, is missing. Finding 7. |
| Invariants | Answers it. The four-part entry and Table 16.4 work well. |
| The selftest | Answers what it is. It leaves unclear where to run it. Finding 2. |
| The quality gate and the ratchets | Answers it "in brief", as the design row asks. The Lua-test promise from Ch. 7 l.187 is only half kept. Finding 8. |
| Trust receipts | Answers it. The CLI block does not earn its place. Finding 9. |
| Extensions | Answers it, the extension contract promised by Ch. 1 l.118 included. It is honest that no runtime loader exists. |
| Contributing a scar | Covers "what a scar must earn" well (l.357 to 361). "How to contribute" (design row) appears only as a list of duties. It never shows the contributor how to run a changed press against a book. Finding 1. |

Design row core content: every listed topic is reached. "How to
contribute" is reached in name but not in practice. I rate that a should
under Path (a procedure with a missing step) rather than a block, but it
is the chapter's largest gap.

Continuity promises:

- Ch. 3 l.126 (book model): partly kept. Finding 6.
- Ch. 1 l.118 (extension contract): kept.
- Ch. 7 l.187 and footnote 7-lua (filter tests, "a coverage floor for each filter"): partly kept. Finding 8.
- Ch. 5 footnote 5-tocdepth ("for the Chapter 16 reader"): Ch. 5 explains the scar in the footnote itself, and Ch. 7 and 9 repeat it. Chapter 16 owes nothing here. No action. The managing editor may want to reword the footnote's address, because Chapter 16 never mentions tocdepth.
- Continuity "due 16" rows: defaults templating (l.68, kept briefly), the registry's artifact table (l.90, kept by name), the jargon lint's two copies (l.96, kept). The reading PDF's six preparation steps and the kind classes are not covered. Ch. 7 and Ch. 5 already state both in full, so no action unless the ledger insists.

## 2. Path

1. **No working setup for the contributor (should; needs fact).** Line 19
   puts a clone in *~/press* "beside the book in *~/alice*" and never
   says how the two are wired together. Line 232 says "she runs it from
   her clone". Step 1 at line 365 says "Reproduce the failure in a real
   book". Step 7 at line 371 says "Run *scripts/verify.sh*", but
   celebrimbor is a development dependency (l.240) and the chapter never
   installs it. A developer stalls at step 1: how does `press` in
   *~/alice* run the code in *~/press*? The chapter also never says how a
   change reaches the press: a pull request, a fork, or a push. Line 377
   says only that `main` "takes direct pushes by design", which an
   outside contributor cannot do. Fix: before the numbered list in
   "Contributing a scar", or as a B-head opening it, add one short
   session, Example 16.4. It should clone, install the clone in editable
   mode into the book's environment, run `press all` in *~/alice*, run
   `press selftest` and *scripts/verify.sh* in *~/press*, and say how a
   change is submitted. facts-16 has none of this. The press's
   *CLAUDE.md* section "Verifying changes here" does (`pip install -e`
   the checkout into a consuming book, `press all`, `scripts/verify.sh
   --full` before tagging, `scripts/dev-render.sh` for the
   edit-render-look loop). *CONTRIBUTING.md* should say how outsiders
   submit. The managing editor must add these to facts-16.

2. **Where the selftest skips (should; needs fact).** Line 232 equates
   "the environment for *~/alice*" with "an installed wheel". But an
   editable install from *~/press*, the setup that finding 1 adds, runs
   from the repository and has the repository files. The reader cannot
   tell what the skip actually keys on: the presence of repository files,
   or the environment. Fix: state the condition the skip tests, in one
   sentence. If the fact exists, mark in Example 16.2 which checks skip
   outside a repository. That turns the example from a list into a tool.
   facts-16 says only "Repo-file checks are skipped from an installed
   wheel".

3. **"The third of the press's four laws" before the first (should).**
   Line 74 cites the third law. Line 86 then introduces "The first of the
   four laws in *docs/ARCHITECTURE.md*". Lines 357 and 359 cite the
   fourth and second. The reader meets the laws out of order and never
   sees all four together. Fix: name the four laws once, by number and
   short title, with their source file, early in the chapter. The end of
   "A map of the package" fits, since the "no book in here" rule is
   already there. Then cite them by number.

4. **"Integration gate" used before it is defined (should).** Line 23
   quotes "its integration gate". The gate is explained at lines 263 and
   271. Fix: add a clause at line 23 ("the CI job that builds a
   stranger's book", or similar) or a forward reference.

5. **"Release witnesses" and "release build" undefined (should).** Line
   104: "It holds the release witnesses, the floor of two sentinels and
   24 pages for a release build." Neither term appears earlier in this
   chapter. Fix: name `PRESS_RELEASE` and point to Chapter 14,
   *Continuous integration and the release contract*, in the same
   sentence, or drop the clause.

6. **Where a new config field goes (should; needs fact).** Line 106
   tells the developer to "add it to the model with its type and its
   default". Table 16.1 (l.36) gives *config_schema.py* "the schema that
   every write must pass". Line 104 gives *bookmodel.py* the frozen
   `Book`. In a chapter whose third A-head is "One statement of each
   fact", the developer will ask whether a field is declared in one of
   these files or both. The chapter does not answer. Ch. 3 also promised
   to show kind, required, and default. Fix: say which module declares a
   field and which consumes the declaration. Show a short excerpt of one
   real field declaration, and the collected-problems output from line
   108 as a short session (missing description plus malformed slug).
   facts-16 has neither excerpt nor output.

7. **The adapters warning sends the reader nowhere (should; needs
   fact).** Line 147: "Add a helper to `press.adapters` and call that
   instead." Line 122 says the package "holds a small set of tools" and
   names none. The writer's report confirms that `import_guard` and
   "streaming" were names only. Fix: name the existing helper a module
   calls to run a tool, and the one it calls to read the environment,
   with their module paths. A six-line excerpt of one call site would
   make the warning actionable.

8. **The Lua filter tests (should; needs fact).** Ch. 7 l.187 sends the
   reader here for the filters' tests, and its footnote says CI "holds a
   coverage floor for each filter". Line 246 says "coverage baselines for
   the Lua filters". Line 252 tells the history but not where the tests
   live or how to run them locally with `PRESS_REQUIRE_LUA=1` so they
   cannot skip. Fix: use one phrase for the floor in both chapters (the
   vocabulary says "ratchet" or "floor"). Add one sentence that names the
   test location and the local command.

9. **The receipts CLI is shown and not explained (should).** Lines 293
   to 297 list `emit|assemble|verify|verify-release` without a word on
   what each mode does or when a developer runs one. Fix: give each mode
   a clause and say whether a contributor ever runs it locally. If the
   facts do not support that, cut the block and keep the CI account at
   line 289.

10. **Two lists of 29 checks (should; needs fact).** Line 204: the
    selftest "runs 29 checks". Line 242: *quality_checks.py* "registers
    29 press domain checks with the gate". A developer will assume these
    are the same list and will be wrong or right by luck. Fix: say in
    one sentence whether the gate's 29 are the selftest's 29. If the
    facts cannot settle it, say the two lists are separate registrations
    and leave the count off one of them.

11. **Figure 16.2 drops two editions (should).** Line 70 says the
    Manuscript and Source editions "do not pass through pandoc". The
    `art:` directive (l.62) draws only six writers converging on
    `dist/alice.*`. The reader who follows the arrows, as line 58
    invites, finds no road for the stitched Markdown or the source zip. Fix: add
    to the directive a bypass arrow from `build.book_inputs` straight to
    the `dist/` cylinder, labelled "markdown, source (no pandoc)". The
    alternative is one sentence saying the figure leaves them out, as
    line 78 does for the print branch.

## 3. Proportion

12. **The book model section spends its words on serialization (should).**
    Line 112 (line width 4096, indents 2, 4, 2) and line 114 (the secret
    regex, spelled out) run about 170 words together. The thing the
    developer must learn, how a field is declared and validated, gets one
    sentence (l.106). Fix: cut line 112 to its first sentence plus the
    quoting rule. Shorten line 114 to the rule and its consequence (the
    "secret" dedication, exit 4). Spend the words on finding 6.

13. **Example 16.1 does not earn its number (should).** Lines 182 to 200
    list thirteen bare names. The developer learns nothing per entry, and
    the four meant to teach (Table 16.4) are already shown. Fix: either
    make it a two-column table with each invariant's one-sentence
    statement from the ledger, or cut it. If cut, name the critical ones
    already met in a sentence and point to *docs/INVARIANTS.md*.

14. **The docs check is stated twice (should).** Line 94 explains `press
    selftest --write-docs`, the `docs` check, and `contract_mirror`. Line
    228 restates both checks. Fix: cut line 228. Example 16.2 and line 94
    cover it.

15. **The Monday workflow is stated twice (should).** Line 248 ("Every
    Monday, a workflow opens an issue...") and Table 16.5's
    *ledger-review.yml* row say the same thing. Fix: keep the table row
    and cut the sentence, or keep the sentence and cut the row. The
    *security-controls.yml* row also matters little to a contributor and
    could go.

16. **Bullet sprawl at the end of "Extensions" (should).** Lines 346 to
    353 list six paths with no clause. "A book can still extend the
    press today" is the developer's practical answer, and the list gives
    no hint what each file extends or where it is explained. Fix: make it
    a two-column table (file, what it extends, with the chapter that
    covers it), or a prose sentence that groups them: art styles, visual
    identity, web CSS, TeX front matter, house-rule fixtures.

17. **Short on what matters most (should).** The chapter has no `$`
    session anywhere. For a developer, a run of `press selftest` (the
    success line exists in facts-16), the setup in finding 1, and the
    model's collected errors in finding 6 are the parts they will
    reproduce. Three short sessions would do more than Examples 16.1 and
    16.2 do now. This is the proportion side of findings 1 and 6. It is
    not a separate fix.

## 4. Opening and closing

- The box matches the A-heads exactly.
- The orientation (l.19) is four sentences with no heading above it, and
  it says who the chapter is for and why. Pass.
- The close (l.377 to 379) ends on a technical point, the release
  boundary as the place the checks bite. Pass. Once finding 1 says how a
  contributor submits, check that this paragraph still follows from it.
  "Direct pushes" without that context reads as an invitation an outsider
  cannot accept.

No findings.

## 5. Numbered items

Every figure, table, and example is cited before it appears: Table 16.1
(l.25), Figure 16.1 (l.48), Figure 16.2 (l.58), Table 16.2 (l.132), Table
16.3 (l.154), Table 16.4 (l.165), Example 16.1 (l.182), Example 16.2
(l.204), Table 16.5 (l.258), Figure 16.3 (l.281), Table 16.6 (l.303),
Example 16.3 (l.315). The one unnumbered fence (l.295) is one line and
needs no number.

Earning their place: Example 16.1 does not (finding 13). Example 16.2
earns it only partly (finding 2). Figure 16.2 has a gap (finding 11).
The rest earn their place. Table 16.4 is the best item in the chapter.

## 6. Length

5,646 words against a 5,000 target: plus 12.9 percent, inside the 15
percent band (ceiling 5,750). Findings 1, 6, and 7 add words. Pay for
them with findings 12 to 15 (about 250 words recoverable) so the chapter
stays under 5,750.

## Note (not counted)

- facts-16 section 16.3 records that *docs/ARCHITECTURE.md* still names
  the old ledger path, *quality/invariants.yaml*. Line 86 sends the
  developer to *ARCHITECTURE.md* for the laws, and line 152 gives the
  correct path. A footnote warning that *ARCHITECTURE.md* still shows
  the old path would save one wrong search. Optional.

## The one change

Give the contributor a working loop before the duties (finding 1). One
short session should clone the press, install it in editable mode into
*~/alice*'s environment, run `press all`, `press selftest`, and
*scripts/verify.sh*, and say how a change is submitted. The managing
editor must first add those facts to facts-16, from the press's
*CLAUDE.md* "Verifying changes here" and *CONTRIBUTING.md*.
