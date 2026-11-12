# Fact check: Chapter 15, The operator's desk and the editorial machines

Chapter: `book/chapters/15-the-desk-and-the-machines.md`.
Fact file: `docs/briefs/facts/facts-15.md` (sections 13, 14, and the shared
context, sections 1.4, 19, 20). Line numbers are the chapter's.

The chapter is accurate on almost every mechanical fact. The verbatim
quotations, the keymap, the wizard keys, the stop rule, the Bash grant, the
counsel fingerprint, and the order of `press skills` all match the file. Most
findings are glosses that go a little past the file. Two claims go well past
it. Both describe a mechanism that the file's own phase lists do not show.

## 1. Unsupported (blocks)

1. **Line 30:** "Press therefore surrounds each workflow with mechanical
   checks, and every workflow ends by running a target whose exit status
   decides the result."
   Searched sections 14.2 to 14.5 for a closing target. Only editorial-passes
   (`press check`, Law phase) and authorities-research (`press pdf`, Ledger
   phase) run one. aesthetic-brief ends at **Audit**: "Checks for valid YAML,
   concrete craft language, coherence, and no attempt to repeal craft law. It
   then writes the file". art-direction ends at **Write**: "Produces
   `art/commissions.md`". Neither runs a target. Fix: limit the claim to the
   two workflows the file supports, for example "Two of the workflows end by
   running a target, `press check` or `press pdf`, whose exit status decides
   the result; the other two end in an audit by another agent."
2. **Line 232:** "The other three workflows follow the same plan: a scout,
   parallel agents, an audit, and a write that a target then checks."
   This has the same problem as item 1, and it adds another. aesthetic-brief's
   phases are "Scout", "Draft", "Audit". The file names no parallel agents for
   it and no target after the write. art-direction has parallel agents
   ("Commission (parallel)") and a curate audit, but no target check. Fix:
   "The other three workflows also open with a scout and close with an audit
   or a check," or describe each one's phases as the file lists them.
3. **Line 30:** "A target is deterministic. Given the same manuscript and
   the same toolchain, `press pdf` builds the same PDF."
   Searched for "deterministic" and "same bytes". The file has only
   ROADMAP's "Trust accumulates from deterministic functions ..." (1.4), which
   does not say a build is reproducible. Fix: soften to the contrast the file
   supports. A target runs fixed code and its verifier decides, while an
   operator command asks a model to write, and two runs can differ.
4. **Line 28:** "Chapter 2 ... showed the doctor's line for `claude`, which
   names this use: 'the operator: press improve, research, aesthetic
   briefs'".
   The quoted doctor line is not in facts-15. Searched for "aesthetic briefs"
   and "the operator:". Fix: check it against Chapter 2 and its fact file
   (facts-02). If it is not there word for word, cut the quotation.
5. **Line 214:** "Every clause in the string matches a rule that `press
   check` enforces."
   The file quotes the string and gives no clause-by-clause mapping to
   checker rules. Fix: say what the file supports: "The string calls itself
   'mechanical, build-enforced', and the Law phase holds the result to
   `press check`."
6. **Line 294 (sidebar):** "Both copies read the same *watchlist.csv*, so a
   term added to the watchlist reaches the build and the skill on the same
   day." Also line 287: "the one watchlist that the jargon lint reads".
   The file says only that the skill "Ships `references/watchlist.csv`,
   `scripts/jargon_lint.py` (the portable copy)" (14.6) and that "a
   byte-parity contract keeps the two copies identical" (19, rationales). It
   does not say the press's lint reads the skill's CSV. Fix: cut the "same
   day" sentence and the "one watchlist" clause, or quote the file: "a
   byte-parity contract keeps the two copies identical".
7. **Line 220:** "Below that threshold the passes have little left to say,
   and the workflow stops instead of paying for another round."
   The file gives the stop rule (14.2) and no reason for it. Fix: cut the
   rationale, or mark it as the author's reading.
8. **Line 274:** "William Zinsser's *On Writing Well*". The file says
   "Zinsser's *On Writing Well*". The first name is true, but it is not in the
   file. Fix: "Zinsser's".
9. **Line 263:** "one skill to a line, with a tab between them."
   The capture (14.6) shows the name and path separated by whitespace of
   varying width. Nothing in the file says the separator is a tab. Fix: "one
   skill to a line, its name and then its installed path."
10. **Line 125:** "An API key pasted into the description field by mistake
    never reaches a file that Git tracks."
    The file says only "A secret-looking value is refused" (13). Fix:
    "... never reaches the file." Or cut the sentence.

## 2. Contradicted (blocks)

None. The chapter avoids every section 20 item it touches. It covers the
live desk's evidence states (A19: present artifacts show `o`, and Table
15.3 omits `*` and `!`), the `c` key missing from DESK.md (A19), the four
wizard fields against CLAUDE.md's "every field" (A19), and the count of
eleven skills, including `book-aesthetics` and `profile-lifecycle` (A20).

## 3. Drifted (should)

1. **Example 15.1 (lines 152-166), captured output.** The words match the
   capture after `demo` became `alice`. But the "…/demo" abbreviation was
   expanded to `/Users/alice/alice` (the writer's report says so), and the
   three long lines are rewrapped. The `pinned:` path breaks in the middle,
   `/Users/alice/alice/.claude/workflows/` then `editorial-passes.js`, so a
   reader who copies it gets a broken path. The text does say "broken here to
   fit the page". Fix: break only at spaces and keep each path on one line,
   or keep the `pinned:` and `invoke:` lines whole and wrap only the `args:`
   line. Have the copy desk decide whether expanding "…" to
   `/Users/alice/alice` counts as more than the permitted slug change.
2. **Lines 334-337, the counsel-mode message.** The chapter presents it as
   the message `press improve` "stops with" and breaks it across two lines
   with no notice. The other three wrapped blocks carry "broken here to fit
   the page". The file's wording is one line: "counsel mode changed the
   manuscript or config; that violates its contract... report this as a press
   bug". Fix: add the same notice, or cut the block to the part before the
   semicolon. The file's "..." is the file's own elision, so it should stay.
3. **Line 324:** "By default it is `Bash(press:*)` and `Bash(python3:*)`,
   which lets the agents run press targets and Python and nothing else."
   The file's command line also grants `Workflow` and runs with
   `--permission-mode acceptEdits` (14.1), so even without `--apply` the
   agents run under accepted edits. Only their Bash use is limited. Fix:
   "which limits their shell to press targets and Python".
4. **Line 41:** "When its standard output is not a TTY, it refuses to
   start". The file says "With no TTY it points you to the CLI" (13). It does
   not say which stream is tested, and it does not say "refuses". Fix:
   "Without a TTY, it points you to the command line instead."
5. **Line 49:** "it begins `not ready:`, lists the tools at fault, and ends
   '(press doctor names each cost)'". The file gives `not ready: … (press
   doctor names each cost)` and does not say what the ellipsis holds. Also,
   "The desk reads the doctor's typed findings": "typed" is not in the file.
   Fix: "it begins `not ready:` and ends '(press doctor names each cost)'",
   and drop "typed".
6. **Line 236:** "It takes `root` and `maxClaimsPerFile`". The file lists a
   third argument: "`press` (the command name)" (14.3). Fix: add it, or say
   "It takes `root` and, among others, `maxClaimsPerFile`."
7. **Line 243:** "claims the auditor would not let stand" is given as the
   meaning of "unresolved". The file says only "Unsourced and unresolved
   claims are reported, not ledgered" and does not define "unresolved". Fix:
   "Claims without a source, and claims left unresolved, appear in the
   report".
8. **Line 241:** "shortening each fragment until it matches". The file says
   "shortening fragments until they match", which does not mean every
   fragment is shortened. Fix: "shortening any fragment that does not match
   until it does."
9. **Line 238:** "a verbatim fragment of 5 to 15 words with a one-line
   assertion". The file says "a 5–15-word verbatim `fragment` plus an
   `assertion`". "One-line" is added. Fix: drop "one-line".
10. **Line 255:** "each declared figure that carries an `art:` description".
    The file says "one per declared *generatable* figure with an `art:`
    description". Fix: restore "generatable".
11. **Line 356:** "It names five faults, which its source calls the named
    diseases of agent prose, and writes them into every prompt." The file
    labels them "The named diseases of agent prose" and cites
    `editorial-passes.js:39-44`. It does not say the source uses that
    phrase, and it does not say the list goes into every prompt. Fix: "It
    names five faults, the named diseases of agent prose, in its source."
    Change "writes them into every prompt" to "hard-codes them".
12. **Line 380:** "the synthesizer demotes or cuts the rest". The quota
    text says only "every other one demoted to plain statement or cut". It
    does not say which agent does it. Fix: "the rest are demoted to plain
    statement or cut."
13. **Line 322:** "while a session with the Workflow tool runs the book's
    [copy]". The file says the operator runs the installed package's copy,
    not the pinned one (14.1), and that the Workflow tool runs by name from
    inside a book. It never says that a run by name resolves to
    `.claude/workflows/`. The claim is likely true, but it is inferred. Fix:
    hedge it: "a session with the Workflow tool runs the workflow by name,
    which is the book's pinned copy."
14. **Line 146:** "the stamp on each copy's first line". The file gives the
    stamp text and does not say where it sits. Fix: "the stamp in each copy".
15. **Line 289:** "The workflows use the name that `press skills` prints."
    This is inferred from the four prose skills being named by filename. Fix:
    "The editorial passes name their skills by the names `press skills`
    prints." Or cut the sentence.
16. **Line 85:** "Each line adds that the exit code decides the result." The
    file has the exact words, "; the exit code is the verdict". This is not
    wrong. Quoting the file's words would be exact.
17. **Footnote 15-popen:** "The press keeps every subprocess call inside one
    package, `press.adapters`". The file says "The adapters boundary gate"
    (19, item 28). The "every subprocess call" reading is reasonable but
    broader than the file's wording. Fix: "The press keeps subprocess calls
    behind a boundary gate around `press.adapters`".
18. **Line 24:** "The desk holds no machinery of its own ... It adds a view
    and a setup wizard, and nothing else." This is stronger than the escape
    hatch the file quotes, "Every action it runs is a `press <target>` you
    can type yourself". Fix: "Every action the desk runs is a target you can
    type yourself; what it adds is the view and the setup wizard."

## 4. Missing (may)

1. **The operator flags are not in `--help`** (20, A23): `improve
   --rounds`, `research --max-claims-per-file`, and `aesthetic --overwrite`
   "exist in code but not in `--help`". Table 15.6 lists all three. A reader
   who checks `press improve --help` will not find them and may decide the
   book is wrong. Add one sentence.
2. **Textual 8.x** (13): the `tui` extra installs Textual 8.x. Chapter 2
   may already cover this. If it does not, it belongs here.
3. **art-direction commission details** (14.5): the logomark is "suited to
   appear at 2.2in on a colophon", the portrait has "No text in the image",
   the cover uses six aesthetic fields, and *art/commissions.md* has the
   headings `## Cover`, `## Plates` (each with its `press art accept …
   --as plate:<name>` line), `## Logomark`, `## Author portrait`. These can
   be left to Chapter 11 if Chapter 11 has them.
4. **The two evidence glyphs the read model can express** (`*` verified,
   `!` changed since proof). The chapter describes them but does not name the
   glyphs. A reader comparing the chapter with `docs/DESK.md` would find
   them useful. Mark them as not shown by the live desk.
5. **The editorial-passes return keys** `{rounds, totalApplied,
   totalRejected, rejectionsFile}` (14.2). Line 220 paraphrases them. The
   key names would help a reader who reads the Workflow tool's result.

## Captured blocks checked

- Example 15.1: the words match; see Drifted 1 for the wrapping and the path
  expansion.
- Example 15.2 (house law): matches word for word once the lines are joined.
  The wrapping is disclosed.
- Example 15.3 (`claude` command): the prompt and flags match. The text says
  the continuation-line form is the chapter's own.
- Example 15.4 (diseases): all five items match word for word once the lines
  are joined, `${MAXIMS}` included. The wrapping is disclosed.
- Counsel-mode message: the words match; the wrapping is not disclosed (see
  Drifted 2).
- The order of Table 15.5 matches the `press skills` capture exactly.
- These match: the install hint, exit status 2, the toolchain-ready line, the
  wizard finish line, the house-law quotes, the synthesizer instruction, the
  research instruction, the aesthetic-brief failed-draft line, the
  art-direction scout instruction, and the registrations and jargon-skill
  quotes.

## Counts

Unsupported 10, Contradicted 0, Drifted 18, Missing 5.
