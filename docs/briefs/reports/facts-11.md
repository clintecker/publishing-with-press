# Fact check: Chapter 11, The art department

Chapter: `book/chapters/11-the-art-department.md`. Fact file:
`docs/briefs/facts/facts-11.md` (sections 8.1 to 8.9, 7.4, and the shared
context, including sections 19 and 20). Two facts come from the managing
editor and are not in the fact file: the logomark path of
`press art commission` requests `gpt-image-1`, which the OpenAI API now
rejects (press issue #277), and `press illustrate` always requests
1024 by 1024 whatever the composition words say (press issue #278).

Overall: the chapter is accurate. Every number, threshold, path, message,
model name, size, and precedence chain I checked matches the fact file.
The findings below are mostly about hedging and a few small overstatements.

## 1. Unsupported (blocks)

1. Line 55: "The aesthetic comes first, because every commission reads it."
   I searched 8.3, 8.8, and 8.9. The file says the prose keys are "prompt
   material only" (8.8). `press cover` reads `cover.style` and `press
   illustrate` reads `plates.style`. `press art commission` reads only
   `art/commissions.md` (8.3), and the aesthetic reaches it only through
   the art-direction workflow. Nothing says every commission reads the
   aesthetic. Fix: soften to "The aesthetic comes first, because the
   commission prompts draw on it."
2. Line 96: "The `--overwrite` option lets it replace an existing file."
   The file gives only the grammar, `press aesthetic "<brief>" [--overwrite]`
   (8.8), and section 20 A23 says the flag is missing from `--help`. It
   never says what the flag does, or that the command refuses an existing
   file without it. Fix: cut the sentence, or soften it to "The command
   also takes an `--overwrite` option."
3. Line 363: "The workflow reads the manuscript, applies the design
   skills, and writes one paste-ready prompt for each picture the book
   needs." The file (8.9 step 3) says only: "Run the `art-direction`
   workflow (Workflow tool, by name). It writes `art/commissions.md`."
   Nothing in it supports "reads the manuscript", "applies the design
   skills", or "paste-ready". Fix: cut to "The `art-direction` workflow
   writes it."

Note, not counted: in Example 11.5 the `ls` output (`openai-1.png
openai-2.png`) is not a capture. It is built from the 8.3 naming rule
("`<model>-<n>.png`. They number upward and never overwrite"). It follows
from that rule, and the writer says so in report-11. Keep it if the house
allows constructed sessions.

## 2. Contradicted (blocks)

1. Line 479: "`press art accept` and `press art enhance` work on files on
   your own machine and call no image model." The file (8.7 step 1) says
   enhance's first step is "**Upscale** with Real-ESRGAN", the AI upscale
   model. The chapter's own line 344 calls it "an AI upscale". The intended
   point, that neither command calls a paid service, is right. The literal
   claim is wrong. Fix: "...work on files on your own machine and send
   nothing to a paid image service. The Real-ESRGAN upscale in `press art
   enhance` runs locally."

## 3. Drifted (should)

1. **Logomark on `gpt-image-1` (press #277).** The chapter presents the
   OpenAI logomark path as working, in four places:
   - Line 441: "`press art commission` requests the logomark from
     `gpt-image-1` at 1024 by 1024 pixels with a transparent background."
   - Table 11.8, `logomark` row.
   - Line 498: "`gpt-image-1` for transparency".
   - The procedure at lines 487 to 494, whose step 3 runs `press art
     commission --model openai` with no targets. That includes the
     logomark, so the run sends a request that the API rejects.

   The file's constants (8.2) are right as code facts. The API has moved
   on. Fix: keep the code facts and add a hedge after line 441: "At the
   time of this writing, OpenAI rejects requests for `gpt-image-1` (press
   issue #277), so the OpenAI logomark request fails. Commission the mark
   with `--model gemini`. Intake extracts the ink of an opaque logomark
   onto transparency." The last sentence is 8.6, and Gemini's logomark
   shape is 8.2. In the procedure, change step 3 to name targets without
   `logomark`, or add the same note.
2. **`press illustrate` is always square (press #278).** Line 230:
   "`press illustrate` sends one request to `gpt-image-2` at 1024 by 1024
   pixels, so its plate is always square." This matches 8.5 and does not
   promise anything wrong. But this is a filed issue, so the claim will
   date. Fix: "At the time of this writing, `press illustrate` sends one
   request ... so its plate is square whatever the prompt says about
   composition (press issue #278)."
3. **Shape keywords (section 20 B16).** Lines 517 and 520 present the
   "landscape composition" / "portrait composition" rule as plain behaviour.
   Section 20 lists it under "Code behaviors that look like bugs. Do not
   document them as features." The tip is useful and fits the file. Add
   "at the time of this writing" to line 517, so that a later fix does not
   make the sentence false.
4. **The `press aesthetic` comment line (line 63).** "It prints a comment
   line, `# effective aesthetic (` *`path`* `)`". The file (8.8) gives
   `# effective aesthetic (<source path>)`. The split markup renders with
   spaces inside the parentheses, "( path )", and that is not the output.
   Fix: one code span, `# effective aesthetic (<source path>)`.
5. **The acceptance-record line (lines 428 to 431).** The block breaks the
   template over two lines, with `placed at {dest}` on an indented second
   line. The file (8.6) gives one line:
   `` - Accepted {date}: `{target}` <- {source.name}, {w}x{h}px, placed at {dest} ``.
   A reader who greps the record, or writes one by hand, will copy the
   wrong shape. Fix: keep the line whole. If it cannot fit the measure,
   say in the text that the record is one line per target. The guardrail
   and likeness-preamble blocks (lines 146, 224, 447) are also re-wrapped.
   Those are prose prompts, where line breaks matter less. Note them for
   consistency.
6. **"A misspelled key simply does nothing" (line 96).** The file says
   only that `config/aesthetic.yaml` "has no config validator" (8.8). What
   a misspelled key does is not stated. A misspelled prose key may still
   reach a prompt, and a misspelled top-level section does not replace the
   house section. Fix: "...so nothing catches a misspelled key."

## 4. Missing (may)

1. **The house accent.** Section 20 A15: the code reads
   `web-palette.accent`, "which the house palette does not define, so the
   hard-coded `#7a2325` is used." Table 11.3 gives the fallback but does
   not say that every book on the house palette gets it. A reader who
   wonders why their cover is not in their cloth colour needs this.
2. **What `text:` other than `baked` does.** Example 11.3 shows the `text`
   setting, and line 168 lists it as a style key, but the chapter gives
   only the `baked` case. File 8.4 and A15: a non-`baked` value "only
   skips the guardrail"; nothing composites type. One sentence would stop
   readers from trusting `composited`.
3. **The cover aspect check reads `trim`, not the profile.** Line 266
   states the rule correctly, but section 20 A17 adds the consequence: "A
   5×8 book's cover is checked against 1.5, not 1.6." An author on a
   non-6x9 profile needs to know to set `trim`.
4. **A missing `GEMINI_API_KEY` stops the run late (section 20 B15).**
   "Without `GEMINI_API_KEY` it exits after already paying for the OpenAI
   images." The warning at line 484 already tells readers to name
   `--model`. A hedged sentence ("at the time of this writing, a missing
   `GEMINI_API_KEY` stops the run only after the OpenAI images are paid
   for") would explain why, without documenting the behaviour as a
   feature. This is the writer's call; report-11 left it out deliberately.

## Captured output

- Example 11.2: `# no OPENAI_API_KEY set; emitting the prompt to run
  elsewhere.` matches 8.4 character for character.
- The `press aesthetic "<brief>"` session: `review it: press aesthetic`
  matches 8.8.
- The messages quoted in prose ("no commissions.md; run the art-direction
  workflow first", "crop the source, do not stretch it", "the luminance key
  would leave a ghost on the page", "logomark arrived opaque; ink extracted
  to transparency", "{var} is not set; the press does not store keys", "the
  figure-from-photo style needs source material: --from <image>", "A
  caption is a label, not art direction (#225)") all match the file.
- Example 11.5 `ls`: constructed, not captured (see the note under 1).

## Counts

Unsupported 3, Contradicted 1, Drifted 6, Missing 4.

Worst finding: Drifted 1. The chapter presents the `gpt-image-1` logomark
path as working, and the whole-set procedure (step 3, `press art
commission --model openai`) sends the logomark request that the OpenAI API
now rejects (press #277). It needs a dated hedge and a Gemini route.
