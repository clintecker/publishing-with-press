# Re-review: Chapter 11, The art department

File: `book/chapters/11-the-art-department.md` (uncommitted revision, 5,315
words by `press wordcount`, target 5,500, inside the band). Reports read:
facts-11, dev-11, copy-11, type-11, and the Revision section of report-11.

## Checks run

- `press check`: passes in full (source, self-test, editorial, jargon). Nothing
  names this file.
- `tools/ste_check.py`: 43 findings. Every one is of a kind the writer's
  report defends and copy-11 accepted: `art:` comments, figure lines, the
  In-this-chapter box, quoted press text, the command name `enhance`,
  "landscape" as an orientation, "therefore", "Finishing"/"Commissioning" in a
  heading and a caption, a table row (341), and footnote markers joining two
  sentences (130, 290, 523). No prose semicolon. Accepted.
- Fences: 19 fences, every opener is `text`; Example 11.3's inner fences are
  file content inside a four-backtick `text` fence.
- `art:` comments: all four (11.1, the plate, 11.2, 11.3) follow their image
  after exactly one blank line.
- Footnotes: `11-penguin`, `11-ink`, `11-band`, `11-upscayl`, `11-imagen`;
  each defined once and referenced once.
- The plate: the image line and the `art:` line are character-identical to the
  stub (commit 7e1b352). The only change is the blank line between them, which
  the ruling requires.
- Prose grep: no "ship", "lands", or "surface" outside the exempt A-head, its
  In-this-chapter entry, the quoted section title at 282, and the figure id.
  No British spelling outside the quoted guardrail ("no colour wash") and the
  `watercolour` match string.

## Findings

| Desk | No. | Severity | Status | Note |
|---|---|---|---|---|
| facts | U1 | blocks | resolved | "the commission prompts draw on it" (61) |
| facts | U2 | blocks | resolved | "The command also takes an `--overwrite` option." (100) |
| facts | U3 | blocks | resolved | The unsupported clause is cut; the new workflow paragraph (375) claims only order, output, and what `press art commission` sends (8.3, 8.9) |
| facts | C1 | blocks | resolved | "send nothing to a paid image service. The Real-ESRGAN upscale ... runs locally." |
| facts | D1 | should | resolved | #277 hedge "At the time of this writing", with `--model gemini` and ink extraction at intake; the procedure's step 3 leaves out `logomark` and step 4 sends it to Gemini |
| facts | D2 | should | resolved | #278 hedged "At the time of this writing" |
| facts | D3 | should | resolved | Shape-keyword rule hedged, moved after Example 11.3 |
| facts | D4 | should | resolved | One code span, `# effective aesthetic (<source path>)` |
| facts | D5 | should | resolved | One-line inline code span, verbatim, plus "Each art target has one line" |
| facts | D6 | should | resolved | "nothing catches a misspelled key" |
| dev | C1 | should | resolved, one new item | The paragraph covers how to run it, what feeds it, what comes back, and the Chapter 15 pointer. See open item 1 |
| dev | P1 | should | resolved | skill (47), workflow and Workflow tool (49), Claude Code and `claude` (55), with a pointer to Chapter 15 by full title |
| dev | P2 | should | resolved | Example 5.1 named (220, step 1) |
| dev | P3 | should | resolved | Step 7's reason is the CI rule; the orphan rule goes with step 2 |
| dev | P4 | should | resolved | Band and ramp in words; expressions in `[^11-band]` |
| dev | P5 | should | resolved | `press aesthetic` with a brief and the workflow "run an agent through `claude`", with no claim about cost |
| dev | P6 | should | resolved | Rule and tip moved to "The commission record" |
| dev | R1 | should | resolved | Endpoints in `[^11-imagen]` |
| dev | R2 | should | resolved | Penguin grid in two sentences |
| dev | R3 | should | resolved | Narration folded into the introduction to Example 11.4; one-commit restatement cut |
| dev | R4 | should | resolved | One sentence for each ground; scar shortened |
| dev | O1 | should | resolved | Five sentences; names Table 11.7 |
| dev | N1 | should | resolved | Demoted to an unnumbered session; examples renumbered |
| dev | N2 | should | resolved | Directive draws the cloth cover; prose keeps the documentation's conditional (ruling allows) |
| dev | N3 | should | resolved | Art target, Meaning; `gemini-3.1-flash-image` named in full |
| copy | 1-6 | blocks | resolved | "ships" and "lands" gone from prose |
| copy | 7 | blocks | declined-accepted | A-head "One master, every surface" exempt by ruling; prose and alt text say "ground" |
| copy | 8 | blocks | resolved | "do not lay ... at pure white" gone |
| copy | 9 | should | resolved | "on your own machine" |
| copy | 10 | should | resolved | |
| copy | 11 | should | resolved | "refuses" |
| copy | 12 | should | resolved | "the Alice example" |
| copy | 13 | should | resolved | Split; cites the kept A-head |
| copy | 14 | should | resolved | "config validation does not cover" |
| copy | 15 | should | declined-accepted | The brief fixes the A-heads (ruling 4) |
| copy | 16 | should | resolved | "art target" defined in step 5 and used throughout; synopsis keeps `[targets]` |
| copy | 17 | should | resolved | |
| copy | 18 | should | resolved | |
| copy | 19 | should | resolved | "The Chapter edition (the reader site)"; figure label matches |
| copy | 20 | should | resolved | Description, not imperatives |
| copy | 21 | should | resolved | |
| copy | 22 | should | resolved | |
| copy | 23 | should | resolved | |
| copy | 24 | should | resolved | |
| copy | 25 | should | resolved | "some photographs" |
| copy | 26 | should | resolved | |
| copy | 27 | should | resolved | "OpenAI or Google" |
| copy | 28 | should | resolved | The tip now adds an action (search for "composition") and does not repeat the paragraph |
| copy | 29-41 | should | resolved | American spelling throughout the prose, tables, and art comments |
| type | 1-4 | blocks | resolved | Labels prefixed `11-` |
| type | 5 | should | declined-accepted | Pagination; no markup fix; recheck with real art |
| type | 6 | should | declined-accepted | `...` marks the repeatable `--model` (fact 8.3) |
| type | 7 | should | resolved | Figure 11.1 brief in two rows |

Copy mays (42 to 51) and fact Missing 1 to 4 are not required. All four
Missing items were added, each with a hedge where it was needed, and most of
the copy mays were applied.

## Open items

1. Should (new, from the reader read). Line 375: "What comes back is
   *art/commissions.md*, in the fixed headings that the next paragraph
   describes." The next paragraph is the one-line "`press art commission`
   reads the file back..." paragraph. The headings come two paragraphs later,
   with Example 11.3.
   Fix: "...in the fixed headings that Example 11.3 shows."

Not counted, for continuity: Table 11.8's `logomark` row reads "`gpt-image-1`
draws it at 1024x1024" with no hedge. The #277 hedge two sections earlier
covers it, and the fact checker's fix did not ask for a hedge in the table.
If the editor wants each place hedged, add "(press issue #277)" to that cell.

## Reader read

The chapter reads in order without stalls. The first procedure is now
runnable: every agent term is defined before or next to the step that needs
it. "Claude Code" appears in step 3 and gets its definition in the paragraph
directly after the list, which is close enough. The money section answers its
heading completely, and the whole-set procedure no longer sends a request
that fails.

## Verdict

APPROVED. 0 open blocks, 1 open should (open item 1, a one-phrase fix).
