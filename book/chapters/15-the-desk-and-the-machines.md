# The operator's desk and the editorial machines

::: {.in-this-chapter}
> **In this chapter:**
>
> - Two ways to drive the press
> - The desk
> - Evidence states
> - The setup wizard
> - Workflows
> - The editorial passes
> - Research, aesthetics, and art direction
> - Skills
> - Running a workflow headless
> - Why the diseases are hard-coded
:::

You can drive press in two ways: by hand, one target at a time, or by agent, through a workflow that reads and writes the book for you. Every earlier chapter drove it by hand from a shell prompt. The *desk* is a full-screen console that does the same work by hand from a list, with the book's state in view. The workflows are the agent route, and they read *skills*, the packaged authoring guides that come with press, which an agent reads before it writes. The examples use the Alice book, which `alice` keeps on `hatter` in the book repository at *~/alice*.

## Two ways to drive the press

The first way is by hand. Every action press takes on a book starts as a `press` command, and you can type the command at the shell prompt or pick it from a list on the desk. Both routes reach the same code. The desk builds the argument list you would type and runs `press` as a child process. The press's documentation puts it in one sentence: "Every action it runs is a `press <target>` you can type yourself; the RUN view even prints the exact command it launched." The RUN view is the desk's screen for a target while it runs.

The command line suits scripts, CI, and anyone who already knows the target names. The desk suits a working session at the keyboard. It keeps the book's state in view while you work: which artifacts exist, which tools the machine lacks, and what the last run printed. Every action the desk runs is a command you can type yourself. What it adds is the view and the setup wizard.

The second way is by agent. A *workflow* is a packaged agent procedure: a script that dispatches language-model agents, gathers what they return, and runs press targets to check their work. Press comes with four of them.

You run a workflow in one of two ways. The first is from your own session in Claude Code, the agent program whose command is `claude`, through its Workflow tool. The second is to let press start `claude` for you. Press calls the commands that take the second route the *operator*. These commands, such as `press improve`, hand work to an agent.

A target and an operator command differ in one respect. A target runs fixed code: `press verify` builds the Print edition (the PDF), and its verifier decides the result. An operator command asks a model to read and write prose, and two runs can return different edits. Two of the workflows therefore end by running a target, `press check` or `press pdf`, whose exit status decides the result. The other two end in an audit by another agent.

## The desk

The desk lives in the optional `tui` extra, which Chapter 2, *Installing press*, installs. Without the extra, `press desk` prints an install hint and exits with status 2. The hint reads "press desk needs the optional interface: pip install 'press[tui]'". With the extra installed, run the desk from the top of the book repository:

```text
$ cd ~/alice
$ press desk
```

The desk needs a terminal. Without a TTY, it points you to the command line instead.[^15-pipe] A cron job or a CI step should call the targets directly.

The desk opens on its home screen, which the code calls DESK. The home screen draws the desk's *read model*, the facts the desk gathers about the book and the machine. @fig:the-desk shows it on `hatter`. The top of the screen gives the book's identity: its title, its authors, its trim, and its slug. The trim prints in inches, as `6 x 9 in` for the house profile. Under the identity sits the artifact table, with one row for each artifact in the registry whose condition holds for this book. Each row has three columns: the artifact, its state, and its published flag.

![The desk on hatter, with the target picker open](assets/woodcuts/15-01-the-desk.png){#fig:the-desk .photo width=full-measure fig-alt="A terminal screen showing the book's title, authors, trim, and slug at the top, a table of artifacts with a one-character state for each, a line about the toolchain, and a table of the machine's tools, with a list of press targets beside them."}

<!-- art: ARCHETYPE screenshot. Capture press desk headless in the Alice book on hatter, grayscale, thin 0.5 pt box, title bar "alice@hatter". In reading order: the identity block (title, authors, trim "6 x 9 in", slug "alice"); the artifact table, columns artifact, state, published, with some rows "-" and some "o" after a press pdf run; the toolchain line, which reads "toolchain ready: this machine can build every artifact"; the doctor table, one row per capability with its glyph. Then press p: the target picker with its argument box sits at the right of the tables, never over the state column or the toolchain line. If the picker replaces DESK, set two captures side by side. The reader should see first the state column, then the toolchain line. -->

Below the artifact table, the desk prints the toolchain line. On a ready machine it reads "toolchain ready: this machine can build every artifact". On any other machine it begins `not ready:` and ends "(press doctor names each cost)". The doctor table comes last, with one row for each capability the doctor checks. It is the panel that Chapter 2 promised. The desk reads the doctor's findings and draws each one with a glyph, as Table 15.1 shows.

| Glyph | Meaning |
|-------|----------------------------------------------------------------|
| `*` | The capability is present and works. |
| `-` | The doctor reports the tool `absent`, or the setting (such as an API key) `unset`. |
| `!` | The tool is `missing` or `broken`. The doctor's own report prints these two states in capitals, as `MISSING` and `BROKEN`. A broken tool is present but cannot run. |
| `~` | The doctor raises a warning about the capability. |

Table: Table 15.1. Glyphs in the desk's doctor table

The `-` glyph does double duty. It marks both an absent tool and an unset setting. Read the row's name to tell which.

### Keys

The desk runs on single keys. Table 15.2 lists every binding.

| Key | Meaning |
|--------|-----------------------------------------------------------------|
| `p` | Open the target picker and run a target. |
| `w` | Open the setup wizard, the guided form for the book's identity. |
| `r` | Refresh the desk's read model. The desk never caches a fact that a rebuild would change. |
| `q` | Quit the desk. |
| `escape` | Leave a run, the picker, or the wizard, and return to DESK. |
| `c` | In the RUN view, cancel the running target. The desk signals the child's whole process group. |

Table: Table 15.2. The desk's keymap

### The picker

The `p` key opens the target picker. The desk builds the list from the *catalog* (the typed command table) and leaves out `desk` itself. The picker has an argument box under the list. A target that needs arguments, such as `press art accept`, refuses to start until you supply them. The desk grays out `pdf`, `print`, `verify`, `verify-print`, and `all` when the doctor finds pandoc, LuaLaTeX, or latexmk at fault.

### The RUN view

When you start a target, the desk switches to the RUN view. The first line shows the exact command, such as `$ press pdf`. Under it the desk prints a stage line, then the log as the child writes it. The stage line shows a check mark, the phases the log names so far (check, typeset, verify), and a count that the desk prints as `N steps`. Chapter 7, *Building the editions*, describes the three markers that the desk parses from the log. They are the phase lines that start with a pilcrow, the plus-sign lines that report each command, and time lines such as `pandoc took 26.7s`. The desk builds the stage line from those markers only, "so it can never claim progress the build did not print".

The run ends with one of three result lines: `done`, `failed (exit N)`, or `cancelled (exit N)`. Each line adds that the child's exit code decides the result.

The desk runs exactly one child at a time. A second launch while one runs raises an error. The desk passes the arguments to the child as a list, never as a shell string, so nothing you type in the argument box reaches a shell.[^15-popen]

::: {.tip}
> **Tip:** Read the first line of the RUN view before you report a problem. It is the exact command the desk launched, and you can paste it at a shell prompt to reproduce the run without the desk.
:::

## Evidence states

The state column in the artifact table holds a one-character glyph. The desk derives each state from "content digests and recorded verification, never a timestamp". A file's modification time says only when something touched it, and a checkout or a copy changes that time without changing a byte. A digest changes when the bytes change and at no other time.

Table 15.3 lists the states that the live desk shows at the time of this writing.

| Glyph | State | Meaning |
|-------|----------------------|------------------------------------------------|
| `-` | not built | The artifact's output does not exist. |
| `o` | present, unverified | The output exists, and no recorded evidence names a verified digest for it. |
| `/` | incomplete | The artifact has several outputs, and some of them are missing. |

Table: Table 15.3. Evidence states in the live desk

The read model can express two more states. One marks an artifact whose current digest matches a verified digest, and the other marks an artifact whose bytes changed after verification. Both depend on recorded verification evidence, and the live desk passes none to the model. In practice every present artifact on the desk shows `o`, even right after a green `press all`.

That is less of a gap than it looks. A verifier checks the artifact at the moment it runs, and the exit status of `press all` reports the result.

::: {.warning}
> **Warning:** Do not wait for a "verified" glyph on the desk before you publish. The live desk never shows one. Run `press all`, or the target's own verifier, and read its exit status.
:::

## The setup wizard

The `w` key opens the setup wizard. The wizard edits the book's identity in *config/metadata.yaml*. At the time of this writing it covers four fields: `title`, `subtitle`, `author`, and `description`. All four sit on a single form, each filled with its current value and a line of help. Every other configuration key goes through `press config` or through the file itself.

The wizard writes nothing while you type. It sends your edits through the same validation step that `press config` uses. The desk and the command line accept and refuse the same values. Three keys finish the form:

1. Type `Ctrl+R` to review. The wizard shows the exact change it would make to the file, with the finding of the validation step beside it.
2. Type `Ctrl+A` to apply the change. The wizard applies only a preview that passed the validation step.
3. Type `escape` to discard the edits and return to DESK.

The wizard refuses any value that looks like a secret. An API key pasted into the description field by mistake never reaches the file.

When the write succeeds, the wizard prints "identity written; next: press check". It does not tell you that the book is ready, because a change to the title says nothing about the rest of the book. The checker reads the new metadata with everything else, and only its exit status says whether the book still passes.

::: {.tip}
> **Tip:** After the wizard writes, press `p` and run `check` from the picker. It is the next thing the wizard tells you to do.
:::

## Workflows

Press carries its workflows and skills as package data, inside the installed package. In the words of the press's documentation, they are "versioned with the press, listed by the CLI, and resolved from the installed package first". The four workflows sit in *src/press/data/workflows/*, one JavaScript file each. Table 15.4 names them and what each one leaves behind. The *prose skills* it mentions are four of the skills, described in the section "Skills" later in this chapter.

| Workflow | Meaning |
|------------------------|-------------------------------------------------------|
| `editorial-passes` | It reads every chapter through the prose skills, applies the suggestions it accepts, and runs `press check` until it passes. |
| `authorities-research` | It extracts claims of fact, researches each one on the Web, audits the research, and writes *config/authorities.yaml*. |
| `aesthetic-brief` | It drafts *config/aesthetic.yaml* from a one-line description of the look you want. |
| `art-direction` | It reads the manuscript and the design skills and writes *art/commissions.md*. |

Table: Table 15.4. The four workflows

`press new` lays a copy of each workflow into the book repository at *.claude/workflows/*. Chapter 3, *The shape of a book repository*, showed the stamp in each copy: `// scaffolded by press 3.0.2; source of truth: press data/workflows`. The copy happens only at `press new`. No later command refreshes it, so a book scaffolded under an older press keeps the older workflows until you replace them.

The `press workflows` command reports each workflow's arguments, compares the book's copy with the installed package, and prints the line you would paste to run it. Example 15.1 shows the last entry on `hatter`. The capture shortens each path to three periods and the last part of the path. This page breaks its long lines to fit and indents each continuation four more spaces.

**Example 15.1. One entry of press workflows**

```text
$ press workflows
...
editorial-passes
  args: {root: absolute path to the book repository}. Run
      against a book repository after composing or
      substantially revising chapters. args: {rounds?:
      number (default 2), maxims?: number (default 2),
      report?: boolean (suggestions written to
      build/editorial-report.md, nothing applied)}
  pinned: .../alice/.claude/workflows/editorial-passes.js
      (matches installed press 3.0.2)
  invoke: Workflow({name: "editorial-passes",
      args: {root: ".../alice"}})
```

The `args:` line holds three parts. The first braces hold the required argument, `root`. The sentence after them is the workflow's advice on when to run it. The second braces hold the optional arguments with their defaults, and the `?` after a name marks it optional.

The `pinned:` line is the one to watch after an upgrade. When the book's copy differs from the installed package, the line reads `DIFFERS from installed press` and names the installed version. The difference matters for the operator, which always runs the installed package's copy, as the section "Running a workflow headless" later in this chapter explains.

The `invoke:` line is what you paste into a Claude Code session. Start Claude Code in the book repository. Its Workflow tool takes the workflow's name and an arguments object. Every workflow requires the `root` argument, and its value must be an absolute path. A run that allows up to three rounds looks like this:

```text
Workflow({name: "editorial-passes",
          args: {root: "/Users/alice/alice",
                 rounds: 3}})
```

### Running editorial-passes from your own session

At the end of Chapter 2, `alice` repaired `claude` on `hatter`, and the doctor's `claude` line now reads `ok`. To run the editorial passes on the book from a Claude Code session:

1. Run `press doctor` and confirm that the `claude` line reads `ok`.
2. Change to the book repository with `cd ~/alice`, and commit any work in progress.
3. Run `press workflows` and copy the `invoke:` line for `editorial-passes`.
4. Start Claude Code with `claude`, in the same directory.
5. Paste the `invoke:` line into the session, with the book's absolute path as `root`.
6. Wait for the workflow's result. It returns four keys: `rounds`, `totalApplied`, `totalRejected`, and `rejectionsFile`.
7. Read *build/editorial-rejections.md*, then read `git diff` to see each edit the synthesizers made.

::: {.warning}
> **Warning:** Commit the manuscript before you run a workflow that applies edits. The synthesizers rewrite chapter files in place, and `git diff` is the quickest way to read what they changed.
:::

::: {.tip}
> **Tip:** Run `press workflows` after every upgrade of press. A `DIFFERS` line tells you that the book's copies are older or newer than the press you run.
:::

## The editorial passes

The `editorial-passes` workflow is the editorial machine. It reads the book through the four prose skills (`humanizer`, `onwritingwell`, `elems_of_style`, and `hemingway`), collects suggestions, applies the ones that survive judgment, and holds the result to the checker. It takes four arguments.

The workflow requires the `root` argument. The `rounds` argument sets the largest number of rounds it runs, two by default. The `maxims` argument sets the *maxim quota*, the number of coined maxims a chapter may keep, also two by default. A coined maxim is a short invented saying that closes a paragraph, and the section "Why the diseases are hard-coded" later in this chapter explains why the workflow rations them. The `report` argument forces one round and applies nothing.

Each round runs four phases, which @fig:editorial-passes-machine traces.

![The editorial-passes machine, round by round](assets/woodcuts/15-02-editorial-passes-machine.png){#fig:editorial-passes-machine .diagram width=full-measure fig-alt="A flowchart in which one agent per chapter and three whole-book readers send suggestions to one synthesizer per chapter, whose edits pass to press check. A loop arrow returns to the start of the round until suggestions run dry or the second round ends."}

<!-- art: ARCHETYPE flowchart, left to right, wider than tall. Column 1: rounded box "Scout", fed by dog-eared file "book/chapters/*.md" and box "press skills". Column 2, stacked: three rounded boxes "chapter pass", an ellipsis, labelled "one pass per chapter file", and beside them three rounded boxes "cadence", "repetition", "arc" labelled "whole book"; all arrows meet dog-eared file "suggestions". Column 3: three rounded boxes "synthesizer", an ellipsis, labelled "one per chapter file", with a side arrow to dog-eared file "build/editorial-rejections.md". Column 4: rounded, drop-shadowed box "press check" labelled "Law", then diamond "zero suggestions, or fewer than 5 applied?" ("Yes" to "stop"); "No" to diamond "rounds left? (default 2)" ("No" to "stop"). "Yes" loops back along the bottom to column 2. The reader should see the loop first. -->

### Scout, suggest, synthesize, law

The *scout* phase lists the manuscript and finds the four prose skills through `press skills`. It records the book's sentinels, the labels of its banned patterns, and its `jargon-allow` list, so that later agents know what they must not disturb.

The *suggest* phase runs in parallel. One agent for each chapter file reads all four prose skills "in full" and returns at most 12 suggestions, each with the current text, the proposed text, and a reason. The prompt adds that "an empty list is an acceptable answer". Three more agents read the whole book through one lens each: *cadence*, *repetition*, and *arc*. Each of the three returns at most 15 suggestions. These lenses look for the patterns that no single chapter shows, such as the same paragraph shape in every chapter.

The *synthesize* phase runs one synthesizer for each file. The synthesizer applies the suggestions with judgment and follows one instruction above the rest: "Preserve the author's voice; do not add length." It rejects what it will not apply and appends each rejection to *build/editorial-rejections.md*.

The *law* phase runs `press check` until it passes. The workflow repairs a failure "by rewriting sentences (never by substituting other punctuation)", and it restores any sentinel an edit removed. The agents work under the house law, a fixed string the workflow puts in front of them, shown here in Example 15.2.

**Example 15.2. The house law, broken here to fit the page**

```text
HOUSE LAW (mechanical, build-enforced): no em or en dashes
anywhere (rewrite the sentence), straight quotes only,
sentence-case headings, no manual heading numbers, ASCII
plus accented latin only, paragraphs under 190 words, no
trailing whitespace.
```

The string calls itself "mechanical, build-enforced", and the law phase holds the result to `press check`. The agents learn the law in advance, and the checker still enforces it afterward.

### Rounds and the rejection ledger

From the second round on, every prompt carries a "PREVIOUSLY REJECTED" ledger. Without it, a fresh agent would propose the same edit that a synthesizer turned down the round before. A rejection binds only while its quoted text survives. If an edit elsewhere removed that text, the rejection "is stale and no longer binds".

The workflow stops early when a round returns no suggestions, or when the synthesizers apply fewer than five. Otherwise the workflow stops after the number of rounds you asked for. When it finishes, it returns four keys: the number of rounds, the totals applied and rejected, and the path of the rejections file. Step 6 of the procedure in the section "Workflows" names them.

![The proofreaders' bench, three readers and one page](assets/woodcuts/the-proofreaders-bench.png)

<!-- art: three proofreaders at one long table in a reading room, each with the same printed page before them, the first reading aloud with a finger on the line, the second following with a pencil, the third comparing against a manuscript, a compact brass reading apparatus on the table between them with a lens and a small bell, galley proofs hung on a line behind, a wall clock; landscape composition; wood engraving with dense hatching and crosshatching, single black ink, no gray washes, no lettering anywhere -->

## Research, aesthetics, and art direction

The other three workflows also open with a scout. Each one then has phases of its own, which the sections below list as the workflow names them.

### authorities-research

The `authorities-research` workflow populates the table of authorities, the ledger in *config/authorities.yaml* that Chapter 10, *Front matter, the index, and the table of authorities*, describes. It takes `root`, `maxClaimsPerFile`, and `press`, the name of the press command. The default of 0 for `maxClaimsPerFile` means every claim in every file. The workflow runs four phases:

1. Extract. A scout states the book's subject and two to four kinds of source that suit it, because "nothing about any particular trade may be assumed". Then one agent for each file extracts claims of fact. Each claim is a verbatim fragment of 5 to 15 words with an assertion. The author's opinions stay out.
2. Research. One agent for each claim searches the Web and returns `supported`, `caveat`, or `unsupported`, with an authority, a URL, and a note. Its instructions say, "Do not invent citations; an invented authority is worse than none."
3. Verify. An adversarial auditor rules on each claim: `holds`, `overstates`, or `fails`.
4. Ledger. The workflow writes *config/authorities.yaml* and shortens any fragment that does not match the text until it does. It then runs `press pdf` until the build passes.

Claims without a source, and claims left unresolved, appear in the report and stay out of the ledger. The accounting must balance: the claims harvested equal the claims ledgered, plus the claims unsourced, plus the claims unresolved. A positive `maxClaimsPerFile` samples the claims instead, and the accounting says what it left out.

### aesthetic-brief

The `aesthetic-brief` workflow drafts *config/aesthetic.yaml*, the book's aesthetic, from one line of description. It takes `root`, `brief`, and `overwrite`, which defaults to false. Its scout reads the gist of the manuscript, the book-aesthetics skill, and the current output of `press aesthetic`. The scout refuses to replace an existing file without `overwrite`.

The drafting agent must write every section, palettes and fonts included. The prompt says why: "a pulp paperback brief with the Victorian house palette left in place is a failed draft". An audit then checks the YAML for validity, concrete craft language, and coherence. It also confirms that the draft does not try to repeal the craft laws. The written file opens with a two-line header that names the brief.

### art-direction

Chapter 11, *The art department*, follows the `art-direction` workflow's product, *art/commissions.md*, through the commission and intake targets. The workflow takes `root` and `maxPlates`, which defaults to eight. Its scout notes each chapter's "strongest concrete image" and reads the metadata, the three design skills, and the output of `press aesthetic`. It also reads the JSON output of `press figures`, with the instruction "do NOT re-parse the markdown by eye".

The commission phase drafts four kinds of commission in parallel: the cover, the logomark, the author portrait, and the plates. A plate commission comes from each declared illustration of a generatable kind that carries an `art:` directive. A book with none gets one candidate per chapter.

A curator keeps at most `maxPlates` plate commissions and audits every prompt. Each prompt must give every line of text verbatim and name a concrete medium, never "detailed illustration". The cover must be flat, with no mockup, and each plate must carry one idea. The write phase keeps any earlier "Accepted" lines under the heading `## Acceptance record`.

No operator command runs `art-direction`. You run it with the Workflow tool, by name, from a Claude Code session in the book repository.

## Skills

Each skill is a Markdown file, or a directory with a *SKILL.md* in it. The workflows read skills, and so can you. Press carries eleven of them as package data in *src/press/data/skills/*. The `press skills` command prints one skill to a line, its name and then its installed path. The workflows find their skills through that command first and fall back to a checkout of the press only when it fails. The skill a workflow reads therefore comes from the same package as the press that builds the book.

Table 15.5 lists the eleven skills in the order `press skills` prints them.

| Skill | Meaning |
|------------------------|-------------------------------------------------------|
| `book-aesthetics` | It interviews the author and writes *config/aesthetic.yaml*. It carries the full schema and a six-question interview. |
| `cover-design` | It briefs a cover in the house bookcloth idiom. It describes the object, names every line of text verbatim, and draws the front board only. |
| `elems_of_style` | It applies clarity, concision, and correctness after Strunk and White. |
| `hemingway` | It asks for concrete detail, compression, omission, and restraint, "without becoming a surface imitation". |
| `humanizer` | It drafts, revises, and audits prose so that it reads as one writer's deliberate choices, with a list of diagnostic patterns and a scoring rubric. |
| `onwritingwell` | It applies Zinsser's *On Writing Well* to nonfiction, with a section on the failures peculiar to language models. |
| `plates-and-woodcuts` | It briefs a plate as a period engraver would: one idea per plate, the joke in the subject, and the style "dead serious". |
| `press-logomark` | It designs the logomark, the printer's mark, which must survive at half an inch in one ink. |
| `profile-lifecycle` | It guides a maintainer through scaffolding, proving, and sealing a print profile. |
| `registrations` | It covers ISBN, LCCN, ISSN, and ONIX paperwork end to end. "The press never issues a number over the network." |
| `overused-jargon` | It is the watchlist skill, with modes to draft, revise, audit, discover, and maintain. |

Table: Table 15.5. The skills that come with press

To read a skill yourself, open the path that `press skills` prints for it, or tell your Claude Code session to read that file before it writes. Before `alice` drafts a cover brief for Chapter 11's commissions, for example, `alice` opens the `cover-design` skill.

The editorial passes require all four prose skills. Three skills are design skills: `cover-design`, `plates-and-woodcuts`, and `press-logomark`. The `art-direction` workflow reads those three. The press's instructions to its own maintainers give the same advice to any agent that writes for a book: "Read the relevant ones before composing prose or art direction for any book."

Some skills carry more than one file. The `overused-jargon` skill is a directory. It holds *references/watchlist.csv* and two scripts: *scripts/jargon_lint.py* and *scripts/discover_jargon.py*.

::: {.sidebar}
> **The jargon lint, twice**
>
> The checker's jargon lint runs inside press. The `overused-jargon` skill carries a second copy of the lint, *scripts/jargon_lint.py*, which the press calls the portable copy. It sits in the skill beside *references/watchlist.csv*. The second copy exists because the skill must work without the press installed. An agent can read the skill and run its script with no press on the machine at all.
>
> Two copies of one program usually come to differ, and a writer then gets one finding from the skill and another from the build. The press keeps that from happening with a byte-parity contract, which keeps the two copies identical. The skill adds its own rule for any match it reports: "A watchlist match starts a review. It does not decide the edit." It offers five modes for the work: draft, revise, audit, discover, and maintain.
:::

## Running a workflow headless

Three operator commands run a workflow without a Claude Code session of your own. Each one starts the `claude` command non-interactively in the book repository and asks it to run one workflow. Table 15.6 lists them. Three of the flags in the table exist in the code but do not appear in the grammar that `--help` prints, and the table says so.

| Command | Workflow | Meaning |
|------------------|------------------------|--------------------------------------|
| `press improve` | `editorial-passes` | It takes `--apply` to edit the manuscript, and `--rounds N` to set the round limit. The `--rounds` flag is not listed by `--help`. |
| `press research` | `authorities-research` | It takes `--max-claims-per-file N` to sample claims instead of reading every one. The flag is not listed by `--help`. |
| `press aesthetic "<brief>"` | `aesthetic-brief` | It takes `--overwrite` to replace an existing *config/aesthetic.yaml*. The flag is not listed by `--help`. |

Table: Table 15.6. The operator commands

Example 15.3 shows the shape of the command that press runs, written here as a shell command with continuation lines. Press passes it as an argument list, so no shell sees it.

**Example 15.3. The claude command an operator runs**

```text
claude -p "Use the Workflow tool with scriptPath <path> \
and args <json>. When it completes, report its returned \
result and nothing else." \
  --allowedTools Workflow <bash grant> \
  --permission-mode acceptEdits \
  --output-format text
```

The command runs at the top of the book repository, with a timeout of 3600 s. The `<path>` is the workflow file inside the installed package, not the book's copy in *.claude/workflows/*. A session with the Workflow tool runs the workflow by name, which is the book's pinned copy. A `DIFFERS` line from `press workflows` means the two routes run different workflows.

Every operator run grants the Workflow tool and runs with `--permission-mode acceptEdits`, so the agents can edit files in any mode. The Bash grant limits only their shell. By default it is `Bash(press:*)` and `Bash(python3:*)`, which limits their shell to press targets and Python. With `--apply`, the grant becomes the whole Bash tool. `press research` also grants WebSearch and WebFetch, which the research phase needs.

::: {.warning}
> **Warning:** Give `--apply` only to a run that you would let use any shell command in the book repository. The flag grants the agents the full Bash tool.
:::

### Counsel mode

Without `--apply`, `press improve` runs in *counsel mode*. It uses the workflow's report form, which runs one round, writes its suggestions to *build/editorial-report.md*, and applies nothing. The press's documentation says the mode "touches nothing", and press checks that claim mechanically. Before the run it computes a SHA-256 fingerprint of *book/* and *config/*, and after the run it computes the fingerprint again. If the two differ, `press improve` stops with this message, broken here to fit the page:

```text
counsel mode changed the manuscript or config; that
violates its contract... report this as a press bug
```

Example 15.4 shows a typical session on `hatter`. It takes counsel first and applies afterward.

**Example 15.4. Counsel first, then apply**

```text
$ press improve
...
$ less build/editorial-report.md
$ git commit -am "Before the editorial passes"
...
$ press improve --apply --rounds 3
...
$ git diff --stat
```

Counsel mode runs one round, so it is the cheaper way to learn what the passes think of a chapter. You read the report, decide whether the suggestions are worth a round, and keep every decision yourself.[^15-counsel]

## Why the diseases are hard-coded

The `editorial-passes` workflow does not trust the prose skills alone. It names five faults, the named diseases of agent prose, and hard-codes them in its source. Example 15.5 quotes them from the workflow's source. The `${MAXIMS}` in the first item is the `maxims` argument.

**Example 15.5. The named diseases, broken here to fit the page**

```text
1. Epigram compulsion: paragraphs that close on coined
   maxims. QUOTA: at most ${MAXIMS} coined maxims per
   chapter; every other one demoted to plain statement or
   cut. A paragraph is allowed to just end.
2. Uniform rhetorical rhythm: X-not-Y antithesis, chiasmus,
   triplets recurring every few sentences; every sentence
   polished to the same sheen. Plain sentences must do
   plain work.
3. Self-annotation: clauses that grade the previous clause
   ("and that is the point", "which is exactly the
   lesson"). Cut them; trust the material.
4. Emblematic abstraction where grit belongs: prefer a real
   duration, count, or cost to a rounded gesture.
5. Throat-clearing, inflated significance, chatbot
   signposting, formulaic negative parallelism.
```

The press's maintainers give the reason in one sentence. The workflow hard-codes the diseases "because 'apply the skills' alone produces locally-obedient, globally-patterned prose." A chapter agent that closes each paragraph on a maxim breaks no rule in any skill it read. Twelve chapter agents that all do the same give the book a pattern. None of them can see it, because each one reads only its own file.

The diseases name that pattern, so every agent in the round looks for the same faults. The maxim quota turns the first one into a number. A chapter may keep two coined maxims by default, and the workflow demotes the rest to plain statement or cuts them. The `maxims` argument changes the quota, and no argument removes the list. The whole-book lenses for cadence and repetition read across chapters for the same reason. Each of them sees every chapter, so it sees a rhythm that a chapter agent, alone with one file, cannot.

[^15-pipe]: The desk's documentation puts it more briefly: "It never draws into a pipe."

[^15-popen]: The launcher has a history. The press keeps subprocess calls behind the adapters gate around `press.adapters`. That gate once missed `from subprocess import Popen`, and the desk's launcher used exactly that form. The gate now resolves aliases, and the launcher moved into `press.adapters`.

[^15-counsel]: The word is the press's own. A counsel gives advice and does not sign the papers.

<!-- index: press desk; desk; read model; evidence state; doctor table; target picker; RUN view; setup wizard; workflow; Workflow tool; Claude Code; press workflows; editorial-passes; named diseases; maxim quota; rejection ledger; authorities-research; aesthetic-brief; art-direction; skill; press skills; prose skills; overused-jargon; operator; press improve; counsel mode -->
