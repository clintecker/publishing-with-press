# Copyedit: Chapter 15, The operator's desk and the editorial machines

File: `book/chapters/15-the-desk-and-the-machines.md`

## Status

REVISE. Ten blocks: seven watchlist sightings ("ships" five times,
"proves", "drift"), one `-ing` rider, and two one-line closers.
`press check` passes the whole book, and its jargon audit names no term in
this file. The watchlist blocks follow the Chapter 4, 6, 8, and 12
precedent: `jargon-allow` lets "ship", "drift", and "verified" through, but
"ships", "proves", and "drift" are not press's own name for anything here,
and the contract puts the watchlist on the one-sighting list.

Counts by severity: blocks 10, should 26, may 20, fact 0.

Most frequent rules broken: wrong term (22 items, counting the seven
watchlist blocks), two ideas (11), rhythm (9). Era spelling follows with
5 ("honours", "greys", "afterwards" twice, "straight after").

Line numbers are `cat -n` line numbers in the file as it stands.

## The ste_check findings, judged

ste_check reports 36 findings (365 sentences, average 11.8 words, max 86).

- Sentence and paragraph length at 6 (the In-this-chapter list), 47, 192,
  and 228 (`art:` directives), 190 (alt text), and 390 (the index
  comment): accepted. None of them is prose. 41 is two sentences that the
  footnote marker merges. 198 (29 words) is under the ceiling. 294 (seven
  sentences) is a real finding (item 33).
- Semicolons: accepted. The hits at 22, 127, 200, and 239 are inside
  verbatim quotations. 47, 192, 228, and 390 are directives and the index
  comment. 146, 335, and the Example 15.4 lines are inside code. No prose
  semicolon.
- Passive and modal passive at 238 ("may be assumed"): accepted. It is a
  verbatim quotation.
- `-ing` forms at 28 (the chapter title *Installing press*), 30 ("by
  running", a gerund), 202 (quotation), 285 (quotation), and 297 (a
  heading): accepted. At 241 the `-ing` form is a rider (item 8).
- "therefore" (30, 263), "verify" (83, 240), "whether" (109, 127, 352),
  "attempt" (249), and "identical" (294): accepted under the 80 percent
  rule. "verify" names a phase and a target. 249 has a real finding on
  other grounds (item 28).
- "landscape" (228): accepted. It names the orientation in an art
  directive, as in Chapters 8 and 12.

Also accepted on reading:

- "scaffolding" (277), "scaffolded" (146), "boundary gate" (386), and
  "verified" (102, 107, 112) are press's own names: the profile lifecycle
  step, the scaffold stamp, the import guard in `press.adapters`, and the
  desk's `verified` evidence state. "surface" (272) and "stale" (218) are
  inside verbatim quotations. "source of truth" (146) is inside the stamp.
- "absent", "missing", "broken", "unset" are the doctor's own state words
  (`desk_model.py`), so Table 15.1 keeps all four (item 38 asks only that
  the words appear).
- "fingerprint" (332) is the operator's own word (`_manuscript_fingerprint`);
  it is not the witness sense the vocabulary forbids (item 52 is a may).
- "house law" (202, 214) is press's name for the string in Example 15.2.
  "parity" (294) is press's "parity contract" (item 50).
- "5 to 15 words" (238) and "at most 12 suggestions" (198): accepted. A
  range that runs past ten keeps numerals.
- The `<path>` "..., not the book's copy" (322) is a factual contrast, not
  the staged "not X but Y".
- Cross-references of the form "as the section ... later in this chapter
  explains" (168) are accepted.
- Second person and present tense hold throughout. There is no "I" and no
  "we". Dry understatement appears at 60 ("does double duty"), 109 ("less
  of a gap than it looks"), and footnote 388, never in a heading.
  Admonitions (90, 112, 130, 179, 223, 327) are all imperative and under
  four sentences. The three footnotes carry a quotation, a history, and the
  joke, not facts the body needs. Headings are sentence case.

## Findings

### Blocks

1. "Both rest on the same targets, and the workflows read the skills that
   press ships beside them." (18)
   Rule: wrong term (watchlist jargon, "ship", one-sighting list), and two
   ideas. Severity: blocks.
   Fix: "Both rest on the same targets. The workflows read the skills that
   come with press."

2. "Press ships four of them." (26)
   Rule: wrong term (watchlist jargon, "ship"). Severity: blocks.
   Fix: "Press comes with four of them."

3. "Press ships its workflows and skills as package data, inside the
   installed package." (135)
   Rule: wrong term (watchlist jargon, "ship"). Severity: blocks.
   Fix: "Press carries its workflows and skills as package data, inside the
   installed package."

4. "Press ships eleven of them as package data in
   *src/press/data/skills/*." (263)
   Rule: wrong term (watchlist jargon, "ship"). Severity: blocks.
   Fix: "Press carries eleven of them as package data in
   *src/press/data/skills/*."

5. "Table: Table 15.5. The skills press ships" (281)
   Rule: wrong term (watchlist jargon, "ship", in a caption). Severity:
   blocks.
   Fix: "Table: Table 15.5. The skills that come with press"

6. "A verifier proves the artifact at the moment it runs, and the exit
   status of `press all` is the proof." (109)
   Rule: wrong term (watchlist jargon, "proves", a certainty claim).
   Severity: blocks.
   Fix: "A verifier checks the artifact at the moment it runs, and the exit
   status of `press all` reports the result."

7. "Two copies of one program usually drift apart, and a writer then gets
   one finding from the skill and another from the build." (294, sidebar)
   Rule: wrong term (watchlist jargon, "drift"; not press's name for a
   thing here). Severity: blocks.
   Fix: "Two copies of one program usually come to differ, and a writer then
   gets one finding from the skill and another from the build."

8. "The workflow writes *config/authorities.yaml*, shortening each fragment
   until it matches the text exactly." (241)
   Rule: -ing rider. Severity: blocks.
   Fix: "The workflow writes *config/authorities.yaml* and shortens each
   fragment until it matches the text exactly."

9. "It adds a view and a setup wizard, and nothing else." (24)
   Rule: one-line closer ("and nothing else" repeats "holds no machinery
   of its own"). Severity: blocks.
   Fix: merge the two sentences: "The desk holds no machinery of its own.
   It adds a view and a setup wizard, so it can do nothing that the
   command line cannot."

10. "The desk adds no judgment of its own on top of the child's exit
    status." (85)
    Rule: one-line closer (it repeats "the exit code decides the result").
    Severity: blocks.
    Fix: cut the sentence, and make the one before it carry the point:
    "Each line adds that the child's exit code decides the result."

### Should

11. "The desk is a full-screen console that shows the state of the book and
    runs targets for you." (18)
    Rule: wrong term (first use of a vocabulary term must be italic and
    defined). Severity: should.
    Fix: "The *desk* is a full-screen console that shows the state of the
    book and runs targets for you."

12. "Press calls the second route the *operator*, the commands such as
    `press improve` that hand work to an agent." (28)
    Rule: two ideas (the apposition makes "operator" name both a route and
    a set of commands). Severity: should.
    Fix: "Press calls the commands that take the second route the
    *operator*. These commands, such as `press improve`, hand work to an
    agent."

13. "Press therefore surrounds each workflow with mechanical checks, and
    every workflow ends by running a target whose exit status decides the
    result." (30)
    Rule: two ideas. Severity: should.
    Fix: "Press therefore surrounds each workflow with mechanical checks.
    Every workflow ends with a target whose exit status decides the
    result."

14. "Given the same manuscript and the same toolchain, `press pdf` builds
    the same PDF." (30)
    Rule: wrong term (the edition has a name, glossed once per chapter).
    Severity: should.
    Fix: "Given the same manuscript and the same toolchain, `press pdf`
    builds the same Print edition (PDF)."

15. "...but the live desk honours it in the RUN view." (64)
    Rule: era spelling (American). Severity: should.
    Fix: "The `c` key does not appear in the press's own desk documentation,
    but the live desk honors it in the RUN view."

16. "The desk generates the list from the catalog, the typed command table,
    and leaves out `desk` itself." (79)
    Rule: wrong term (first use of "the catalog" must be italic and
    defined; the apposition reads as a three-item list). Severity: should.
    Fix: "The desk builds the list from the *catalog* (the typed command
    table) and leaves out `desk` itself."

17. "The desk greys out `pdf`, `print`, `verify`, `verify-print`, and `all`
    when the doctor finds pandoc, LuaLaTeX, or latexmk at fault." (79)
    Rule: era spelling (American). Severity: should.
    Fix: "The desk grays out `pdf`, `print`, `verify`, `verify-print`, and
    `all` when the doctor finds pandoc, LuaLaTeX, or latexmk at fault."

18. "...the phases the log names so far (check, typeset, verify), and a
    count of steps." (83)
    Rule: wrong term ("step" is a never-word for a target, and the count is
    of the plus-sign command lines). Severity: should.
    Fix: "The stage line shows a check mark, the phases the log names so far
    (check, typeset, verify), and a count of the commands the log
    reports."

19. "The desk runs exactly one child at a time, and a second launch while
    one runs raises an error in the code." (87)
    Rule: two ideas. Severity: should.
    Fix: "The desk runs exactly one child at a time. A second launch while
    one runs raises an error."

20. "The `/` state carries the most news of the three. It tells you that an
    artifact with several outputs is missing some of them." (109)
    Rule: two ideas (one topic per paragraph: the paragraph argues about
    verifiers, then turns to the `/` state, which Table 15.3 already
    defines). Severity: should.
    Fix: move the pair to its own paragraph after Table 15.3, or cut the
    second sentence: "Of the three, the `/` state carries the most news."

21. "The wizard edits the book's identity in *config/metadata.yaml*, and at
    the time of this writing it covers four fields: `title`, `subtitle`,
    `author`, and `description`." (117)
    Rule: two ideas. Severity: should.
    Fix: "The wizard edits the book's identity in *config/metadata.yaml*.
    At the time of this writing it covers four fields: `title`,
    `subtitle`, `author`, and `description`."

22. "It sends your edits through the same validation boundary that
    `press config` uses, the function `preview_edits`, so the desk and the
    command line accept and refuse the same values." (119)
    Rule: two ideas. Severity: should.
    Fix: "It sends your edits through `preview_edits`, the same validation
    boundary that `press config` uses. The desk and the command line
    therefore accept and refuse the same values."

23. "...with the validator's finding beside it." (121) and "The wizard
    applies only a preview that the validator passed." (122)
    Rule: wrong term ("validator" is a never-word; the thing is the
    validation boundary of 119). Severity: should.
    Fix: "The wizard shows the exact change it would make to the file, with
    the validation finding beside it." and "The wizard applies only a
    preview that passed validation."

24. "It reads the book through the four prose skills, collects suggestions,
    applies the ones that survive judgment, and holds the result to the
    checker." (184)
    Rule: wrong term (the term *prose skills* is used here and at 196 and
    198 but defined only at 283). Severity: should.
    Fix: "It reads the book through the four *prose skills* (`humanizer`,
    `onwritingwell`, `elems_of_style`, and `hemingway`), collects
    suggestions, applies the ones that survive judgment, and holds the
    result to the checker." Then at 283: "The editorial passes require
    all four prose skills."

25. "The agents learn the law in advance, and the checker still enforces it
    afterwards." (214)
    Rule: era spelling (American "afterward"). Severity: should.
    Fix: "The agents learn the law in advance, and the checker still
    enforces it afterward."

26. "The workflow stops early when a round returns no suggestions, or when
    the synthesizers apply fewer than 5." (220)
    Rule: wrong term (a number under ten in prose is spelled out).
    Severity: should.
    Fix: "The workflow stops early when a round returns no suggestions, or
    when the synthesizers apply fewer than five."

27. "Otherwise it stops after the number of rounds you asked for. Below
    that threshold the passes have little left to say, and the workflow
    stops instead of paying for another round." (220)
    Rule: two ideas ("that threshold" points back past an intervening
    sentence). Severity: should.
    Fix: put the reason right after the threshold: "The workflow stops
    early when a round returns no suggestions, or when the synthesizers
    apply fewer than five. Below that threshold the passes have little
    left to say, and another round costs more than it returns. Otherwise
    the workflow stops after the number of rounds you asked for."

28. "It also confirms the draft makes no attempt to repeal the craft laws."
    (249)
    Rule: noun stack (the action in a noun: "makes no attempt"; and keep
    "that"). Severity: should.
    Fix: "It also confirms that the draft does not try to repeal the craft
    laws."

29. "Commit the manuscript before you run the editorial passes in applying
    mode." (223, Warning)
    Rule: synonym rotation ("applying mode" is defined nowhere; the chapter
    names the forms `report` and `--apply`). Severity: should.
    Fix: "Commit the manuscript before you run the editorial passes without
    the `report` argument."

30. "...with a catalog of diagnostic patterns and a scoring rubric." (273,
    Table 15.5)
    Rule: wrong term ("the catalog" is the typed command table, as at 79).
    Severity: should.
    Fix: "It drafts, revises, and audits prose so that it reads as one
    writer's deliberate choices, with a list of diagnostic patterns and a
    scoring rubric."

31. "**Why the jargon checker exists twice**" (292, sidebar title)
    Rule: wrong term ("the checker" is reserved for `press check`; the body
    calls the program the jargon lint). Severity: should.
    Fix: "**Why the jargon lint exists twice**"

32. "The working directory is the book root, and the run has a timeout of
    3600 s." (322)
    Rule: wrong term ("book root" for the book repository), and two ideas.
    Severity: should.
    Fix: "The command runs at the top of the book repository, with a
    timeout of 3600 s."

33. The sidebar paragraph (294) runs seven sentences.
    Rule: two ideas (one topic per paragraph, six sentences at most: why
    the copy exists, then how press keeps the copies alike). Severity:
    should.
    Fix: break after "An agent can read the skill and run its script in any
    directory, with no press installed at all." Start the second paragraph
    at "Two copies of one program usually come to differ...".

34. "A typical session on `hatter` takes counsel first and applies
    afterwards:" (339)
    Rule: era spelling (American "afterward"). Severity: should.
    Fix: "A typical session on `hatter` takes counsel first and applies
    afterward:"

35. "Twelve chapter agents that all do the same give the book a pattern,
    and none of them can see it, because each one reads only its own
    file." (378)
    Rule: two ideas. Severity: should.
    Fix: "Twelve chapter agents that all do the same give the book a
    pattern. None of them can see it, because each one reads only its own
    file."

36. "The `-` glyph does double duty. It marks both an absent tool and an
    unset setting, so read the row's name to tell which." (60)
    Rule: two ideas (the second sentence carries a fact and a command).
    Severity: should.
    Fix: "The `-` glyph does double duty. It marks both an absent tool and
    an unset setting. Read the row's name to tell which."

### May

37. "The workflows are agent procedures that read the manuscript, suggest
    and apply edits, research claims of fact, and direct the art." (18)
    Rule: wrong term (the italic definition of *workflow* comes at 26,
    after this first use). Severity: may.
    Fix: leave 18 roman and keep the definition at 26, or move the italic
    here: "The *workflows* are agent procedures that ..."

38. "| `-` | The tool is absent, or the setting (such as an API key) is
    unset. |" and "| `!` | The tool is missing or broken. ... |" (54, 55,
    Table 15.1)
    Rule: synonym rotation (to a reader, "absent" and "missing" are the
    same word; they are the doctor's two states). Severity: may.
    Fix: name the doctor's words: "| `-` | The doctor reports the tool
    `absent`, or the setting (such as an API key) `unset`. |" and "| `!` |
    The doctor reports the tool `missing` or `broken`. A broken tool is
    present but cannot run. |"

39. "| `r` | Refresh the model. ..." (70, Table 15.2)
    Rule: wrong term ("the model" reads as the language model in a chapter
    about agents; 107 calls it the read model). Severity: may.
    Fix: "| `r` | Refresh the desk's read model. The desk never caches a fact
    that a rebuild would change. |"

40. "In practice every present artifact on the desk shows `o`, even
    straight after a green `press all`." (107)
    Rule: era spelling (British idiom "straight after"). Severity: may.
    Fix: "In practice every present artifact on the desk shows `o`, even
    right after a green `press all`."

41. "The desk tells you what exists. The verifiers tell you whether it is
    right." (109)
    Rule: rhythm (an antithetical pair of matched sentences, the uniform
    rhythm the named diseases list). Severity: may.
    Fix: "The desk tells you which artifacts exist, and the verifiers tell
    you whether each one is right."

42. "Press `Ctrl+R` to review." (121)
    Rule: wrong term (a capitalized "Press" at a sentence start reads as
    the program). Severity: may.
    Fix: "Type `Ctrl+R` to review." (and "Type `Ctrl+A`", "Type `escape`"
    in steps 2 and 3).

43. "`press new` lays a copy of each workflow into the book at
    *.claude/workflows/*." (146)
    Rule: wrong term ("the book" for the book repository). Severity: may.
    Fix: "`press new` lays a copy of each workflow into the book repository
    at *.claude/workflows/*."

44. "Inside Claude Code, started in the book repository, the Workflow tool
    takes the workflow's name and an arguments object." (170)
    Rule: two ideas (the participle "started" attaches to the tool, not to
    Claude Code). Severity: may.
    Fix: "Start Claude Code in the book repository. Its Workflow tool takes
    the workflow's name and an arguments object."

45. "The `rounds` argument sets the most rounds it runs, by default 2." and
    "...also 2 by default." (186); "...which defaults to 8." (253)
    Rule: rhythm ("the most rounds") and number style (a default in prose,
    not in code). Severity: may.
    Fix: "The `rounds` argument sets the largest number of rounds it runs,
    two by default." "...also two by default." "...which defaults to
    eight." (Or set the defaults as code: `2`, `8`.)

46. "...an audit, and a write that a target then checks." (232)
    Rule: noun stack (a verb used as a noun, "a write"). Severity: may.
    Fix: "The other three workflows follow the same plan: a scout, parallel
    agents, an audit, and a written file that a target then checks."

47. "...where the default of 0 means exhaustive." (236)
    Rule: rhythm (an adjective standing for a behavior). Severity: may.
    Fix: "It takes `root` and `maxClaimsPerFile`, where the default of 0
    means every claim in every file."

48. "A curator keeps at most `maxPlates` and audits every prompt." (257)
    Rule: rhythm (the object of "keeps" is missing). Severity: may.
    Fix: "A curator keeps at most `maxPlates` plate commissions and audits
    every prompt."

49. "The art-direction workflow reads those three." (283)
    Rule: synonym rotation (everywhere else the workflow name is code,
    `art-direction`). Severity: may.
    Fix: "The `art-direction` workflow reads those three."

50. "The press closes that door with a byte-parity contract: ..." (294)
    Rule: wrong term (press's own name is the parity contract, in
    *docs/WORKFLOWS.md* and *tests/test_jargon_parity.py*; "contract" is
    otherwise reserved). Severity: may.
    Fix: "The press closes that door with its parity contract: the portable
    copy must stay byte for byte identical to the copy that press runs."

51. "If `press workflows` reports `DIFFERS`, the operator runs the installed
    press's copy, while a session with the Workflow tool runs the book's."
    (322)
    Rule: rhythm (it repeats 168 almost word for word). Severity: may.
    Fix: "A session with the Workflow tool runs the book's copy instead, so
    a `DIFFERS` line means the two routes run different workflows."

52. "Before the run it computes a SHA-256 fingerprint of *book/* and
    *config/*, and after the run it computes the fingerprint again." (332)
    Rule: synonym rotation (95 calls the same kind of hash a "digest").
    Severity: may.
    Fix: "Before the run it computes a SHA-256 digest of *book/* and
    *config/*, and after the run it computes the digest again."

53. "A sentence about "a long build" tells the reader nothing. A sentence
    about a build that ran several minutes ... tells the reader what to
    expect." (382)
    Rule: rhythm (second person elsewhere; the matched pair ends the
    chapter on an antithesis). Severity: may.
    Fix: "A sentence about "a long build" tells you nothing. Say instead
    that the first build ran several minutes because LuaLaTeX scanned its
    fonts, and the reader knows what to expect."

54. "A target and an operator command differ in one respect that matters."
    (30)
    Rule: rhythm (a staged lead-in; "that matters" inflates). Severity:
    may.
    Fix: "A target and an operator command differ in one respect."

55. "It runs the workflow in its report form, which runs one round, writes
    its suggestions to *build/editorial-report.md*, and applies nothing."
    (332)
    Rule: rhythm ("runs" twice in one sentence, three times with the one
    before). Severity: may.
    Fix: "It uses the workflow's report form, which runs one round, writes
    its suggestions to *build/editorial-report.md*, and applies nothing."

56. "The skill's front matter sometimes gives a name different from the
    filename." (289)
    Rule: rhythm (the definite article points at no skill in particular).
    Severity: may.
    Fix: "A skill's front matter sometimes gives a name different from its
    filename."
