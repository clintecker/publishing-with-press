# Re-review: Chapter 15, The operator's desk and the editorial machines

File: `book/chapters/15-the-desk-and-the-machines.md` (404 lines, 5,146 words
by `press wordcount`). Scope: every blocks and should finding in facts-15,
dev-15, copy-15, and type-15, checked against the Revision section of
report-15 and the managing editor's rulings. Line numbers are `cat -n` line
numbers in the revised file.

## Verdict

**APPROVED.** 0 open blocks, 3 open shoulds (listed below), plus four mays
that are not counted.

## Checks run

- `press check`: exit 1. The only failure is "plate never referenced by the
  manuscript: assets/woodcuts/12-01-cover-wrap-anatomy.png", which belongs to
  Chapter 12. No failure names this file.
- `python3 tools/ste_check.py`: 38 findings (385 sentences, average 11.7
  words). All but one are the accepted classes in the writer's defence: the
  In-this-chapter list (6), `art:` comments (47, 210, 242), the fig-alt (208),
  the index comment (404), quotations (22, 127, 218, 220, 252, 253, 299), and
  headings and gerunds (30, 34, 180, 311). The 80 percent rule covers
  "therefore", "whether", "verify", and "identical". The exception is line
  238, a 32-word prose sentence (open should 3).
- Fences: all eight are `text`. No line in any fence is over 64 columns.
- Footnotes: `15-pipe`, `15-popen`, and `15-counsel` are each defined once.
- Art comments: Figure 15.1 (45/47), Figure 15.2 (208/210), and the plate
  (240/242) each have an image, one blank line, and then the comment. The
  plate's image line and comment match `git show HEAD` lines 3 and 4 byte for
  byte.
- Watchlist: none of "ships", "proves", or "drift" remains.

## Vocabulary rulings since

- **The Alice book:** the term never appears in the chapter (open should 2).
  The users `alice` and `hatter` are used correctly at 182 and 297.
- **The logomark:** used correctly at 269. Table 15.5 (290) calls it only
  "the printer's mark" (may).
- **Edition names:** "the Print edition (the PDF)" is glossed once, at 30. No
  other edition is named.
- **Checker self-test:** not used in this chapter, so nothing to check.
- The catalog (79) and the desk (18) are italicized and defined at first
  use, and the operator (28) is defined there too.

## Findings table

| Desk | No. | Status | Note |
|---|---|---|---|
| facts | B1 | resolved | 30: "Two of the workflows therefore end by running a target ... The other two end in an audit by another agent." |
| facts | B2 | resolved | 246: "also open with a scout. Each one then has phases of its own" |
| facts | B3 | resolved | "deterministic" cut; 30 now contrasts fixed code with model edits |
| facts | B4 | resolved | doctor-line quotation cut |
| facts | B5 | resolved | 232 quotes "mechanical, build-enforced" |
| facts | B6 | resolved | the sidebar claims only the two copies, the place beside the CSV, the reason, and the byte-parity contract |
| facts | B7 | resolved | stop-rule rationale cut (238) |
| facts | B8 | resolved | "Zinsser's" (288) |
| facts | B9 | resolved | "its name and then its installed path" (277) |
| facts | B10 | resolved | "never reaches the file" (125) |
| facts | D1 | resolved | Example 15.1 keeps the shortened paths, breaks at spaces with a four-space indent, and keeps the `pinned:` path whole; 148 discloses this |
| facts | D2 | resolved | "broken here to fit the page" (346) |
| facts | D3 | resolved | 338: Workflow and acceptEdits in every mode; "limits their shell" |
| facts | D4 | resolved | 41: "Without a TTY, it points you to the command line instead." |
| facts | D5 | resolved | 49: no claim about the middle of the line, and "typed" is dropped |
| facts | D6 | resolved | 250: `press` added |
| facts | D7 | resolved | 257: "claims left unresolved", with no definition |
| facts | D8 | resolved | 255: "any fragment that does not match" |
| facts | D9 | resolved | "one-line" dropped (252) |
| facts | D10 | resolved | "generatable" restored (269) |
| facts | D11 | resolved | 372: "hard-codes them in its source" |
| facts | D12 | resolved | 396: "the workflow demotes the rest" (equivalent: no particular agent is named) |
| facts | D13 | resolved | 336: hedged as "runs the workflow by name, which is the book's pinned copy" |
| facts | D14 | resolved | "the stamp in each copy" (146) |
| facts | D15 | resolved | sentence cut. 277's "find their skills through that command first" is CLAUDE.md's fact, a different claim |
| facts | D16 | declined-accepted | 85 paraphrases the line; the finding said it was not wrong |
| facts | D17 | resolved | footnote `15-popen`: "behind a boundary gate around `press.adapters`" |
| facts | D18 | resolved | 24: "Every action the desk runs is a target you can type yourself. What it adds is the view and the setup wizard." |
| facts (coordinator) | 5.4 markers | **open** | open should 1 |
| dev | P1 | resolved | 182 and step 1; the Figure 15.1 directive names the ready line |
| dev | P2 | resolved | Claude Code defined at 28; seven-step procedure at 180 to 190 |
| dev | P3 | resolved | RUN view (22), read model (43, 70), coined maxim (204) |
| dev | P4 | resolved | 168 |
| dev | P5 | resolved | "allows up to three rounds" (172) |
| dev | P6 | resolved | 297 |
| dev | P7 | **open** | superseded by fact base 5.4: Chapter 7 is right and line 83 is wrong (open should 1) |
| dev | R1 | resolved | `/` sentences and the antithesis cut (109) |
| dev | R2 | resolved | one commit warning (193) |
| dev | R3 | resolved | `c` note, `preview_edits`, and `human-writing` cut |
| dev | O1 | resolved | 18: five sentences; "by hand / by agent" matches 22 and 26 |
| dev | O2 | resolved | the chapter ends on the whole-book lenses (396) |
| dev | N1 | resolved | Example 15.4 with caption, referenced at 353 |
| dev | N2 | resolved | two-capture fallback and ready line in the 47 directive |
| copy | 1 to 5 | resolved | "come with" / "carries" (18, 26, 135, 277, 295) |
| copy | 6 | resolved | "checks ... reports the result" (109) |
| copy | 7 | resolved | "come to differ" (308) |
| copy | 8 | resolved | "writes ... and shortens" (255) |
| copy | 9 | resolved | 24 rewritten per facts D18 |
| copy | 10 | resolved | closer cut (85) |
| copy | 11, 12, 13 | resolved | 18, 28, 30 |
| copy | 14 | resolved | Print edition glossed (30) |
| copy | 15 | resolved | moot: the sentence was cut |
| copy | 16, 17 | resolved | 79 |
| copy | 18 | resolved | "a count that the desk prints as `N steps`" (equivalent: it names the desk's own output) |
| copy | 19, 20, 21 | resolved | 87, 109, 117 |
| copy | 22, 23 | resolved | "validation step" (119, 121, 122) |
| copy | 24 | resolved | defined in italics at 202 (but see the may on Table 15.4) |
| copy | 25, 26 | resolved | 232, 238 |
| copy | 27 | resolved | rationale cut per facts B7 |
| copy | 28 | resolved | 263 |
| copy | 29 | resolved | 193: "a workflow that applies edits" |
| copy | 30, 31, 32, 33 | resolved | 287, 304, 336, sidebar now two paragraphs |
| copy | 34, 35, 36 | resolved | 353, 394, 60 |
| type | 1 | resolved | *maxim quota* in prose (204, 396) |
| type | 2 | resolved | Example 15.4 |
| type | 3 | resolved | plain step labels (252 to 255) |
| type | 4 | resolved | left to right, wider than tall, ellipsis boxes (210) |
| type | 5 | resolved | picker at the right, two-capture fallback; fig-alt says "beside them" |
| type | 6 | declined-accepted | depends on final pagination |
| re-review | new | **open** | open should 2 (the Alice book) |
| re-review | new | **open** | open should 3 (the 32-word sentence at 238) |

## Open items

### Open should 1: the desk parses three markers (fact base 5.4; dev P7)

Quote (83): "Chapter 7, *Building the editions*, describes the phase lines that start
with a pilcrow and the plus-sign lines that report each command. The desk
parses the stage line from those two kinds of line only, "so it can never
claim progress the build did not print"."

facts-07 (line 169) says: "The desk parses three markers from this stream:
`+ ` lines ..., `¶ <phase>` ..., and `<tool> took Ns`." Chapter 7, line 456,
already says this ("the phase lines, the plus-sign lines, and the time
lines"), so no continuity routing is needed. Chapter 7 is correct.

Fix: "Chapter 7, *Building the editions*, describes the phase lines that
start with a pilcrow, the plus-sign lines that report each command, and the
time lines. The desk parses its progress from those three kinds of line
only, "so it can never claim progress the build did not print"." Chapter 7
calls them "time lines", so this chapter uses that term too.

### Open should 2: the Alice book is not named (vocabulary ruling)

Quote (18): "The examples follow `alice` on `hatter`, in the book repository
at *~/alice*."

The ruling uses "the Alice book" for the full-novel sample. Here `alice`
could be read as the user or as the slug. Chapter 11, line 18, sets the form.

Fix: "The examples use the Alice book, which the user `alice` keeps at
*~/alice* on the workstation `hatter`." The Figure 15.1 directive (47) says
"in the alice book". Capitalize it to "the Alice book" in the same pass.

### Open should 3: a 32-word sentence (ste_check, line 238)

Quote (238): "When it finishes, it returns the four keys that the procedure in the
section "Workflows" names: the number of rounds, the totals applied and
rejected, and the path of the rejections file."

This sentence came in with the revision. It is 32 words, over the 30-word
ceiling. Its pointer is also loose: the keys are named in step 6 of the
subsection "Running editorial-passes from your own session", not in the
"Workflows" section's own prose.

Fix: "When it finishes, it returns four keys: the number of rounds, the totals
applied and rejected, and the path of the rejections file. Step 6 of the
procedure earlier in this chapter names them."

## Mays (not counted)

- 290, Table 15.5: "It designs the printer's mark". Use the vocabulary term
  with Chapter 11's gloss: "It designs the logomark, the printer's mark of
  the imprint, which must survive at half an inch in one ink."
- 139, Table 15.4: "through the prose skills" comes before the italic
  definition at 202. Either name the four skills here or point forward.
- 127: "a title change cannot prove that". This is a "prove" sighting next
  to the "proves" block. Consider "cannot show that".
- 30, 119, 277, 336: four uses of "therefore". Each one is accepted, but
  dropping one or two would loosen the rhythm.

## Reading as a reader

The chapter reads cleanly from the two routes, to the desk, to the
workflows, to the procedure, and to the headless operator. The procedure
gives the agent half of the chapter a real path. One spot may trip a
reader: step 5 asks for the absolute path while Example 15.1's `invoke:`
line shows `.../alice`. The text at 148 and the step's own wording both
cover this, so no change is required. Nothing else stops a reader.
