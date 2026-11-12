# Developmental edit: Chapter 15, The operator's desk and the editorial machines

Desk: developmental editor. File: `book/chapters/15-the-desk-and-the-machines.md`
(390 lines). I read it as the design's reader: an author who can use a shell
and does not know TeX, and, since the design gives Chapters 14 to 16 to them as
well, the developer who keeps a group's builds running. Line numbers refer to
the file as read.

Status: DONE_WITH_CONCERNS. 0 block, 14 should.

## 1. Coverage

All ten A-heads from the brief are present, in order, in sentence case, with
prose between every pair of headings. Every core topic in the design row is
reached: `press desk` (screens, keys, evidence glyphs, the wizard), the four
workflows and their phases, the skills, `press skills` and `press workflows`,
`press improve` with counsel mode and `--apply`, `press research`, `press
aesthetic`, and the named diseases. Both figures, the plate (moved to the end of
"The editorial passes", lines unchanged), one sidebar (131 words), six tips and
warnings, and three footnotes are present. No block.

| A-head | Line | Does the section deliver? |
|---|---|---|
| Two ways to drive the press | 20 | Partly. It answers its heading in two paragraphs, then introduces two more routes (Workflow tool, operator) under the same "two" (O1). |
| The desk | 32 | Yes. Launch, refusal, home screen, doctor panel, keys, picker, RUN view. |
| Evidence states | 93 | Yes, honestly: it follows the code and warns the reader off a glyph that never appears. Some padding (R1). |
| The setup wizard | 115 | Yes. Four fields, the review and apply keys, the secret refusal, the next step. |
| Workflows | 133 | Mostly. Table 15.4 and the stamp are clear. Example 15.1 needs one more sentence of reading (P4). |
| The editorial passes | 182 | Yes. The chapter's best section: phases, ledger, stop rule, all traced by Figure 15.2. |
| Research, aesthetics, and art direction | 230 | Yes. Each workflow gets its arguments and phases. |
| Skills | 261 | Mostly. Table 15.5 is complete. "and so can you" (line 263) is never followed by how (P6). |
| Running a workflow headless | 297 | Yes, with a precondition missing on the sample machine (P1). |
| Why the diseases are hard-coded | 354 | Yes. The reason is quoted and argued (lines 378 to 380). The close is weak (O2). |

### Continuity: the promises other chapters made

- Chapter 2, line 262, "The desk reads the same findings and draws them as a
  panel, as Chapter 15 shows": **kept** (lines 49 to 60, Table 15.1, Figure
  15.1).
- Chapter 2, line 165, the operator commands "Chapter 15 ... describes them":
  **kept** (Table 15.6, Example 15.3, counsel mode). But see P1: Chapter 2 left
  `claude` BROKEN on `hatter`, and this chapter runs the operator on `hatter`
  without repairing it.
- Chapter 11, line 55, "Skills and workflows run in Claude Code, an agent
  program whose command is `claude`. Chapter 15 ... describes them", and line
  375, "Chapter 15 ... describes how a workflow runs": **kept in part**. Skills
  and the operator's use of `claude` are described in full. How a workflow runs
  from your own session is two sentences and one three-line fence (lines 170 to
  176). The reader never sees the session start or what the workflow hands back
  (P2).
- Chapter 3, line 100 (what the four stamped workflows do): **kept** (Table
  15.4, line 146).
- Chapter 10, line 382 (`authorities-research` and `press research`): **kept**
  (lines 234 to 243, Table 15.6).
- Chapter 7, line 456, says the desk uses "the phase lines, the plus-sign lines,
  and the time lines". This chapter (line 83) says the stage line comes from the
  first two "only", which is what facts-15 supports. **Conflict, in Chapter 7**
  (P7).

## 2. Path

**P1 (should). The sample machine cannot run the operator.** Chapter 2
(Figure 2.2 and line 256) leaves `claude` BROKEN on `hatter`
and the doctor at `not ready: claude`. Line 339 here runs `press improve` "on
`hatter`" as if nothing were wrong, and line 49 and the Figure 15.1 directive
(line 47) never say what the toolchain line reads on that machine. Fix: before
Table 15.6, one or two sentences that send the reader to repair `claude` (or
say it is now repaired) and rerun `press doctor` until the `claude` line reads
`ok`. Then make the Figure 15.1 directive name the toolchain line it shows:
either `not ready: claude ...` (the machine as Chapter 2 left it, which also
illustrates the doctor table's `!` row) or the ready line after repair. Pick
one and make the session agree.

**P2 (should). The reader never runs a workflow from a session of their own.**
Line 28 says "from inside an agent session with the Claude Code Workflow tool"
without saying what Claude Code is in this chapter (the developer reader may
start at Chapter 14 and has not seen Chapter 11, line 55). Line 170 says
"Inside Claude Code, started in the book repository" and stops at the paste.
Fix: define Claude Code in a clause at its first use (line 28), and give the
section "Workflows" a short numbered procedure: `cd ~/alice`, start `claude`,
paste the `invoke:` line from `press workflows`, and read what comes back. Line
220 already has the return value (rounds, totals applied and rejected, the
rejections file path); move a pointer to it into the procedure so the reader
knows the run ended. Stay inside the fact file: it gives no Claude Code install
step, so say where press expects the command (on `PATH`, checked by the doctor)
and leave installation alone.

**P3 (should). Three terms are used before they are defined.**
- Line 22 quotes "the RUN view even prints the exact command it launched". The
  RUN view is defined at line 81. Add a clause ("the screen that shows a run")
  or move the quotation to the RUN view section.
- Line 70, Table 15.2: "Refresh the model." The read model first appears at
  line 107, and the reader of line 70 will take "model" to mean a language
  model, since the chapter has just introduced agents. Say "refresh the screen's
  facts" or define the read model at line 43, where the home screen is
  introduced.
- Line 186: "the quota for coined maxims per chapter" before the reader knows
  what a coined maxim is or why it is rationed. Add a forward pointer to the
  section "Why the diseases are hard-coded", or a four-word gloss.

**P4 (should). Example 15.1 shows two `args:` fields and the prose explains
neither.** Line 156 reads `args: {root: ...}`, then a sentence of advice, then
a second `args: {rounds?: ...}`. A reader will think the output is garbled.
Line 148 says only that "Each entry prints as a name and three long lines".
Fix: one sentence after the example saying the first `args:` holds the
required arguments, the sentence is the workflow's advice on when to run it,
and the second `args:` holds the optional ones with their defaults (the `?`
marks optional).

**P5 (should). "A run with a third round" (line 170).** `rounds: 3` sets the
most rounds, and line 220 says the workflow can stop earlier. "A third round"
reads as a promise of exactly three, or of one extra round. Say "a run that
allows up to three rounds".

**P6 (should). "The workflows read skills, and so can you" (line 263) is never
cashed.** Lines 285 to 289 quote the maintainers' advice to read the relevant
skills but never say what the reader does: open the path that `press skills`
prints in an editor, or tell an agent session to read that file before it
writes. Fix: one sentence after Table 15.5 that does this, hung on `alice`
(for example, the `cover-design` skill before a cover brief, which ties to
Chapter 11).

**P7 (should; the fix belongs in Chapter 7).** Chapter 7, line 456, says the
desk reads "the time lines" for progress. facts-15 and this chapter (line 83)
say the stage line is parsed from the pilcrow lines and the plus-sign lines
only. Keep line 83 as written. Route to the continuity desk: Chapter 7 must
drop "and the time lines", or the fact desk must confirm them.

## 3. Proportion

**R1 (should). Line 109 restates the table and closes on a pair.** "The `/`
state carries the most news of the three. It tells you that an artifact with
several outputs is missing some of them" repeats Table 15.3's `/` row. "The
desk tells you what exists. The verifiers tell you whether it is right" is a
balanced two-sentence antithesis, the second disease the chapter itself names
at line 365. The paragraph must do one thing: tell the reader which command
gives the proof the desk does not. The warning at line 111 already does that,
so the paragraph can shrink to its first two or three sentences.

**R2 (should). The same warning appears twice.** Line 223 ("Commit the
manuscript before you run the editorial passes in applying mode") and line 327
("Run `press improve --apply` only after you commit your work") give the same
instruction, and the session at line 345 shows the commit a third time. Keep
the one at line 327, where the reason is new (the full Bash grant). Cut line
223's warning or turn it into a different instruction (for example, reading
*build/editorial-rejections.md* after a run).

**R3 (should). Maintainer trivia sits in the reader's path.** Three places:
- Line 64: "The `c` key does not appear in the press's own desk documentation,
  but the live desk honours it". The brief says where docs and code disagree,
  follow the code or stay silent. The table row is enough. Cut the sentence.
- Line 119: "the function `preview_edits`". The reader needs to know the desk
  and `press config` share one validator, not the function's name. Cut the
  name, or move it to Chapter 16.
- Line 289: the `humanizer` file "calls itself `human-writing`". It matters
  only to someone who opens the file and wonders. If it stays, make it one
  clause inside the Table 15.5 discussion, not its own paragraph.

## 4. Opening and closing

The "In this chapter" box (lines 3 to 16) matches the ten A-heads exactly. No
heading sits above the orientation paragraph.

**O1 (should). The orientation runs six sentences, and its "two" disagrees with
the first A-head.** Line 18 has six sentences (the limit is five) and says
"Press offers two more ways to work on a book", meaning the desk and the
workflows. The A-head at line 20 is "Two ways to drive the press" and means the
shell and the desk, then adds the Workflow tool and the operator as "a separate
matter" (line 26). The reader cannot tell what the two ways are. Fix: decide
what the two are (by hand, through a target, either typed or picked; and by
agent, through a workflow, either in a session or by the operator would be one
reading) and make line 18, line 22, and line 26 say the same. Cutting the last
sentence of line 18 (the `alice` path, which line 37 shows anyway) brings it to
five.

**O2 (should). The close is a staged contrast.** Line 382 ends the chapter on
"A sentence about 'a long build' tells the reader nothing. A sentence about a
build that ran several minutes ... tells the reader what to expect." That is
an X-then-Y antithesis closing on a lesson, in the section that names that
pattern as a disease. Fix: end on the last technical point of the section,
for example what the synthesizer does with a fault it finds, or that the
`maxims` argument is the only knob on the list (line 380 already says this
and could close the chapter if line 382 goes). Do not add a summary or a
forward pointer in its place unless it is one sentence to Chapter 16.

## 5. Numbered items

Every figure, table, and example is referred to before it appears: Figure 15.1
(line 43), Table 15.1 (49), Table 15.2 (64), Table 15.3 (97), Table 15.4 (135),
Example 15.1 (148), Figure 15.2 (188), Example 15.2 (202), Table 15.5 (265),
Table 15.6 (299), Example 15.3 (309), Example 15.4 (356). Each earns its place.

**N1 (should). The session at lines 341 to 350 is nine lines and unnumbered.**
The brief numbers every example over six lines. Give it a number (it becomes
Example 15.4 and the diseases become 15.5, or number it in sequence wherever it
lands after P2's procedure), a caption, and a reference in the lead-in at line
339. The writer's report calls it six lines of commands; the fence is nine.

**N2 (should). The Figure 15.1 directive leaves the illustrator to guess two
things.** It does not say what the toolchain line reads (see P1), and the
writer's report admits the fact file does not say whether the picker overlays
DESK or replaces it. The illustrator captures headless and will see the answer
to the second; the directive should say so ("if the picker replaces DESK,
capture two frames"), as the report does, rather than leave it in the report
only. The first must be decided by the chapter.

## 6. Length

`press wordcount`: 4,933 words against a target of 5,000 (1.3 percent under,
within 15 percent). P2's procedure and N1's caption add perhaps 150 words; R1,
R2, and R3 cut about the same.

## For the copy desk (not counted)

- *workflow* (line 26), *skill* (263), and *operator* (28) are italicized as
  new terms. Chapter 11 (lines 47 to 49) and Chapter 2 (line 165) already
  defined all three. Style guide 2.5: italic once, at first use in the book.
- The sidebar (line 291) is the design rationale the brief suggests, not one
  of the thirty war stories the brief's next sentence asks for. The war story
  that belongs here (the subprocess gate and `Popen`, shared context 28) is in
  footnote `15-popen`. Either is defensible; the managing editor should rule.

## The one change

Add a short worked procedure that runs `editorial-passes` on `alice` from the
reader's own Claude Code session (P2), starting from a `claude` the doctor
reports `ok` (P1): it keeps Chapter 11's promise, fixes the sample machine's
continuity, and gives the chapter's agent half the hands-on path its desk half
already has.
