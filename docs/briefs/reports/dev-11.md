# Developmental edit: Chapter 11, The art department

Desk: developmental editor. File: `book/chapters/11-the-art-department.md`
(525 lines). I read it as the design's reader would: an author who can use
a shell and does not know TeX. Line numbers refer to the file as read.

Status: DONE_WITH_CONCERNS. 0 block, 15 should.

## 1. Coverage

All ten A-heads from the brief are present, in order, in sentence case,
with prose between every pair of headings. Every core topic in the design
row is reached: the aesthetic and its merge, cover styles and `press
cover`, `press illustrate` and the `art:` directive, `press art accept`
for all four targets, the luminance key and alpha masters, `press art
enhance`, *art/commissions.md*, the art-direction workflow, models and
keys and what spends money, the logomark and the portrait. All three
figures, the plate, and the suggested sidebar (the five-percent box) are
present. No block.

| A-head | Line | Does the section deliver? |
|---|---|---|
| What the art department is | 20 | Yes. The one-time-commission rule and Table 11.1 frame the chapter well. Step 7's justification is a non sequitur (P3). |
| The aesthetic | 57 | Yes. The shallow-merge rule and Example 11.1 are the right pair. Leans on a skill and `claude` it never defines (P1). |
| Covers | 100 | Yes. Subject precedence and the lettering guardrail are the useful core. Long on the Penguin grid (R2). |
| Interior plates | 190 | Yes. The five-step procedure depends on a figure shown only in Chapter 5 (P2). |
| Intake: what acceptance enforces | 246 | Yes. The strongest section: Table 11.5, the aspect check, the flat-ground test, the key, the sidebar. Formulas in Python (P4). |
| One master, every surface | 304 | Partly. Half the section is the JPEG scar; the three surfaces get one sentence between them (R4). |
| Finishing a plate | 318 | Yes. Table 11.6 and the four steps are clear. |
| The commission record | 361 | Mostly. Example 11.4 and 11.5 deliver. The workflow that writes the file gets one sentence (C1), and the shape-from-prompt rule that governs these prompts is held back to the last section (P6). |
| Logomark and portrait | 435 | Yes. |
| Keys, models, and what spends money | 459 | Yes. Table 11.7 and the warning answer the heading. Long on endpoints (R1). |

**C1 (should). The art-direction workflow is a core topic reached in one
sentence.** Line 363: "The workflow reads the manuscript, applies the
design skills, and writes one paste-ready prompt for each picture the
book needs." With step 3 at line 49 ("Run the `art-direction` workflow by
name with the Workflow tool"), that is all the reader gets about the
thing that writes the file every later command reads. Fix: the paragraph
at line 363 must tell the reader what they do to run it and what they get
back, from whatever the fact file holds, and give a forward pointer to
Chapter 15, *The operator's desk and the editorial machines*, for the
machinery. If the fact file holds nothing more, the pointer carries it.

## 2. Path

**P1 (should). "Workflow tool", "skill", and `claude` are used and never
defined.** Line 47 ("the book-aesthetics skill"), line 49 ("with the
Workflow tool"), line 96 ("headlessly through `claude`"), line 363 ("the
design skills"). This reader has never met Claude Code and stalls at step
3 of the chapter's first procedure. Fix: at first use (line 47 or 49),
one or two sentences saying that skills and workflows are agent
instructions that run in Claude Code, that `claude` is its command, and
that Chapter 15 covers them. The other three uses then stand.

**P2 (should). The Alice plate procedure depends on a figure the chapter
never shows.** Lines 232 to 238 commission `white-rabbit` from its `art:`
directive; line 216 points at Chapter 5 only in general. The reader does
not know the Alice book already declares this figure. Fix: name Example
5.1 at line 216 or at step 1 (line 234), as the figure the procedure
draws from.

**P3 (should). Line 55 justifies "commit the assets" with the orphan
rule.** "Step 7 matters more than it looks. A plate that sits on disk and
that no chapter references is an orphan, and `press check` fails the book
over it." An orphan is about referencing, not committing; committing does
nothing for an orphan. Fix: step 7's reason is the one line 22 already
gives (CI on `printshop` builds only committed files). Put the orphan rule
where it belongs, with step 2 or step 5, as the failure that follows
accepting a plate no chapter declares.

**P4 (should). Two rules arrive as Python.** Line 284,
`max(3, min(w,h)//25)`, and line 288, `round(255*(225-v)/180)`. This
reader cannot read floor division. Fix: state each in words (a band one
twenty-fifth of the shorter side, never under 3 pixels; alpha falls in a
straight line from 255 at 45 to 0 at 225). Figure 11.3 already draws the
second. A footnote may keep the expressions.

**P5 (should). The money section is silent on the agent runs.** Line 469
limits Table 11.7 to "a paid image service", and line 479 clears `press
aesthetic` "with no arguments", which leaves the reader to wonder about
`press aesthetic "<brief>"` and the art-direction workflow, both of which
run through `claude`. The writer's report says the fact file does not
state their cost. Fix: ask the fact checker; failing a fact, line 479
must say these two run an agent through `claude` under the author's own
setup, and claim nothing about cost.

**P6 (should). A procedure step depends on a rule given later.** Step 2
at line 490 says "confirm that every plate prompt names its composition";
the reason (the exact phrases "landscape composition" and "portrait
composition" pick the size, and anything else gets a square) arrives at
line 517, after the procedure. Example 11.4 already shows "landscape
composition" at line 382 with no comment. Fix: move the paragraph at line
517 and its tip to "The commission record", after Example 11.4, and let
Table 11.8's plate rows refer back to it. The section then closes on the
request shapes or the Gemini refusal note.

## 3. Proportion

**R1 (should). Line 513 runs long on what this reader never touches.**
Two endpoint URLs, a third with `{model}` in it, the multipart form, and
the `x-goog-api-key` header. The reader's fact is the first sentence: each
request goes from the author's machine straight to the provider. Fix: keep
that sentence and the transparency note if the writer wants it; move the
rest to a footnote or cut it.

**R2 (should). The Penguin grid paragraph (line 126) gives percentages the
reader cannot use.** Three band proportions describe a prompt template
the reader never edits. Fix: one sentence on what the default looks like,
then the footnote. The words go to C1 or R4.

**R3 (should). Two paragraphs restate what precedes them.** Line 422
narrates Example 11.5 line by line; only its last clause (the destination
path) is new. Line 496 ("One commit then holds the acceptance record and
the assets it describes") restates step 6. Fix: fold the destination into
the sentence that introduces Example 11.5 and cut line 422; cut line 496
or give it the reason the two belong in one commit.

**R4 (should). "One master, every surface" is short on its promise.** 262
words, and lines 310 to 312 spend half of them on the baked-JPEG history.
The three surfaces share lines 306 and 308, and the reader edition gets
one clause. Fix: give each surface its own sentence saying which edition
uses it and what happens to the master there (print: flattened onto white
by the print-safe pass; reader: the transparent PNG as is; cloth: in the
conditional the fact file uses). Keep the scar after that, shorter.

## 4. Opening and closing

The "In this chapter" box lists the ten A-heads exactly. No heading
precedes the orientation. The close ends on a technical point and a tip,
not a summary; that passes, and P6 changes which point it ends on.

**O1 (should). The orientation runs seven sentences and points at an
unnamed list.** Line 18. "This chapter follows one picture from the
manuscript to the page" talks about the document, and "It also names the
commands that send work to a paid service. Read that list before you run
any of them" sends the reader to a list they cannot find. Fix: five
sentences at most, what and why, and name Table 11.7 if the warning stays.
The Alice sentence can move to the first example.

## 5. Numbered items

Every table (11.1 to 11.8), example (11.1 to 11.5), and figure (11.1 to
11.3) is referred to in prose before it appears. Figure 11.2 is placed in
the intake section ahead of its own A-head so that it numbers before
11.3; line 306 refers back to it correctly. That is acceptable.

**N1 (should). Example 11.2 does not earn its number.** Lines 157 to 162:
a command, one comment line, and `...`. The prose already quotes the
behaviour at line 153. Fix: if the fact file holds the opening lines of
the printed prompt, show them so the reader sees what `--print` gives
them; if not, demote it to an unnumbered three-line session.

**N2 (should). Figure 11.2 draws as fact what the prose states as a
condition.** Line 308: "a cloth cover would flatten the master onto the
field colour". The directive at line 280 draws a "cloth field" surface as
one of three equals, and the fig-alt says the rabbit appears "on a dark
cloth field". The writer's report flags the same tension in the fact file.
Fix: the prose, caption, alt text, and directive must agree. Either the
middle surface becomes the imprint logo on cloth (the case line 308 says
already works), or the label carries the condition.

**N3 (should). Table 11.8 breaks the house table rule.** Line 502: three
columns, none of them a Meaning column with sentences, and the Gemini
column says "flash" where the prose names `gemini-3.1-flash-image`. Fix:
recast as Target and Meaning (two columns, a sentence per target giving
both providers), or keep the grid and say why in the writer's report;
either way name the flash model once in full.

## 6. Length

`press wordcount`: 5,009 words against a target of 5,500, 9 percent
under, inside the 15 percent band. The cuts in R1, R2, and R3 free about
200 words; C1, P1, and R4 want about the same, so the chapter should
stay in band.

## The one change

Fix P1 with C1: define skills, workflows, and `claude` at first use and
point to Chapter 15, so that the reader can run step 3 of the chapter's
first procedure, the step that writes the file every later command reads.
