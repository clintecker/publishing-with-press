# Report: Chapter 11, The art department

File: `book/chapters/11-the-art-department.md`. Not committed.

## Word count

`press wordcount`: 5009 (target 5,500, 9 percent under, inside the 15
percent band). `press check` passes with no error naming this file.

## Figures

- 11.1 `@fig:art-direction-loop` (flowchart): manuscript with art:
  directives, press figures, art-direction workflow, art/commissions.md,
  the three image commands (arrow labelled "your API keys"),
  build/ and art/candidates/, "you choose one" into press art accept,
  assets/, press art enhance, return arrow to the build.
- 11.2 `@fig:one-master-every-surface` (before/after): one alpha master on
  a checkerboard at left; the same ink on a white print page, a dark cloth
  field, and a cream Web panel at right. Placed in the subsection "The
  plate master" (section 5) so that it numbers 11.2 ahead of the intake
  figure; section 6 refers back to it.
- 11.3 `@fig:intake-before-after` (before/after): (a) rabbit on a near-white
  ground with a faint box edge, callout "ground near #f1f2f3"; (b) ink on
  transparency; under both a luminance scale with ticks at 45 and 225 and
  the linear ramp between.

The plate (the engraver's bench) moved, unchanged, to the end of
"Interior plates". Note for the art desk: an `art:` directive must not quote
`<!-- art: ... -->` inside itself, because the inner `-->` closes the
comment early. My first draft of 11.1 did this; the final one does not.

## Facts left out, or handled with care

- Fact file section 20 B15 (art commission exits without GEMINI_API_KEY
  after paying OpenAI) is marked a bug: not stated. The chapter states only
  the 8.3 facts (default both models, no confirmation, plan line) and
  warns the reader to name `--model`.
- B16 (plate shape keywords): stated as the 8.2 rule (`shape_for`), with a
  tip to include the words. Flag if the controller reads B16 as forbidding
  even that.
- A15: `text: composited` and press-set cover type are not mentioned. The
  cloth-cover case in "One master, every surface" is quoted in the
  conditional the docs use ("a cloth cover would flatten...").
- A16/A17: sizes and the aspect check follow the code (1024x1536 vs
  2304x3456; trim read from `metadata.yaml` `trim`, default 6x9).
- A18: greying stated with both conditions.
- `press illustrate` with no OPENAI_API_KEY: the fact file gives the
  no-key behaviour only for `press cover`, so the chapter claims only
  `--print` for illustrate.
- Whether `press aesthetic "<brief>"` costs money (it runs `claude`) is not
  in the fact file; the chapter says nothing about its cost.
- No captured output exists for art commission, accept, or enhance, so
  sessions show commands with `...` and only the messages the fact file
  quotes. The `ls` output in Example 11.5 follows from the stated naming
  rule on a first run with `--count 2`.

## Contradictions in the fact file

- 8.6 says a cloth cover "would" flatten the master; 8.1/brief Figure 11.2
  presents the cloth cover as a surface. The prose keeps the conditional;
  the figure labels the panel "cloth field" only.
- Chapter 5 (another writer) puts the `art:` comment after one blank line;
  `docs/markup.md` says the very next line. This chapter follows markup.md.

## Markup note

Example 11.4 (the shape of art/commissions.md) contains inner fences, so
its outer fence is four backticks tagged `text`. pandoc parses it as one
code block (checked with `pandoc -t native`).

## ste_check residuals and defence

- Lines 6, 41, 241, 276, 287: the In-this-chapter box, figure lines, and
  the untouched plate line count as long sentences. Markup, not prose.
- Semicolons (lines 42, 58, 159, 359, 435, 460 and others): inside art
  comments, the quoted house register, YAML, or quoted press messages.
  None in my prose.
- 'landscape', 'enhance', 'identical': command names, quoted aesthetic
  text, or alt text.
- 'is gilt', 'are prompt', 'is closed', 'is glaring': false positives or
  verbatim quotations.
- '-ing' forms: the brief's heading "Finishing a plate", an example
  caption, and "substring" in a table row.
- 'therefore' (two): period-correct per the prose contract.
- Paragraph-length 58: three of its sentences are the quoted register.
- Line 329 (55 words) and 340: a table row and a numbered fallback list.

## Revision

Word count after revision: 5315 (`press wordcount`; target 5,500, within
band). `press check` names nothing in this file. Footnotes prefixed with
`tools/prefix-footnotes.py` (`11-penguin`, `11-ink`, `11-band`,
`11-upscayl`, `11-imagen`).

Rulings applied:

1. #277: logomark hedge after the `gpt-image-1` sentence, with the
   `--model gemini` route and ink extraction at intake; the whole-set
   procedure now names art targets without `logomark` and adds a Gemini
   step for it. #278: `press illustrate` square output hedged "at the time
   of this writing". The shape-keyword rule is hedged the same way.
2. "Call no image model" now reads "send nothing to a paid image service",
   and the text says the Real-ESRGAN upscale runs locally. Unsupported
   claims cut or reduced: "every commission reads it" (now "the commission
   prompts draw on it"), `--overwrite` (now "also takes"), and the
   workflow's "reads the manuscript, applies the design skills,
   paste-ready" (cut). `# effective aesthetic (<source path>)` is one code
   span. The acceptance-record template is one inline code span, verbatim,
   because at 75 columns it cannot fit a 64-column fence. Missing items,
   one sentence each: the house accent `#7a2325`, non-`baked` `text` only
   skips the guardrail, the aspect check reads `trim` and not the profile
   (5 by 8 example), and the late stop on a missing `GEMINI_API_KEY`
   (hedged).
3. Skill, workflow, Workflow tool, and `claude` defined in clauses at
   first use, with a pointer to Chapter 15. The orientation is five
   sentences and names Table 11.7. Example 11.2 (press cover without a
   key) lost its number, and Examples 11.3 to 11.5 are now 11.2 to 11.4.
   Figure 11.2's directive and alt text draw a cloth cover; the prose
   keeps the documentation's conditional. Table 11.8 is now Art target |
   Meaning, and it names `gemini-3.1-flash-image` once in full. The
   art-direction workflow has a paragraph: how it is run, what feeds it,
   what comes back, and what `press art commission` sends.
4. "ships" (five) and "lands" replaced. The A-head "One master, every
   surface" kept per ruling, and the prose and alt text no longer use
   "surface". The sidebar's "do not lay ... at pure white" staging is gone.
   American spelling throughout the prose and art comments (quoted press
   text such as "no colour wash" and the `watercolour` substring stay).
   "refuses" for press stopping (orphan, aspect, missing commissions.md,
   missing key). "Art target" defined in step 5 and used throughout; the
   synopsis keeps `[targets]`. The reader site is "the Chapter edition
   (the reader site)". The enhance steps are now description ("It
   upscales..."). The composition tip no longer repeats its paragraph.
5. Footnote prefixes applied. Figure 11.1's brief is in two rows. Every
   fence is `text` (the inner fences of Example 11.3 are file content
   inside a four-backtick `text` fence). Every `art:` comment follows its
   image after one blank line (confirmed for all four).

Developmental shoulds also resolved: P3 (step 7's reason is the CI rule,
and the orphan rule moved to step 2), P4 (band and ramp in words,
expressions in a footnote), P6 (the shape rule and tip moved to "The
commission record"), R1 (endpoints moved to a footnote), R2 (Penguin grid
in two sentences), R3 (the Example 11.5 narration and the one-commit
restatement cut), R4 (one sentence per ground, and the scar shortened).

Declined:

- Copy 7 and 15 (rename the A-heads): the brief fixes the A-heads, per
  ruling 4.
- Copy 51 (lengthen the sidebar): it is 136 words, inside markup.md's
  120 to 180 range.
- Type 5 (Example 11.1 caption parted from its fence): pagination, which
  no markup can fix. The example is eight lines. Recheck when the real art
  is in.
- Type 6 (drop `...` after the `--model` group): it marks a repeatable
  option, which is a fact in 8.3.
- Fact Drifted 5, note on re-wrapped guardrail and likeness blocks: these
  are prose prompts quoted to fit 64 columns, and the wrap changes no
  word.

Residual ste_check findings are of the kinds defended above (markup lines,
quotations, command names, table rows, the brief's "Finishing" heading).

## Revision 2

Re-review items applied: line 375 now points at Example 11.3, and the `logomark` row of Table 11.8 cites press issue #277. Per the new vocabulary ruling, "the Alice example" is now "the Alice book" in all 11 places, including the caption and YAML of Example 11.2. The chapter never mentions the three-chapter gallery example or `dist/pages`. `press check` names nothing in this file.

## Revision 3

Continuity fixes applied:
- Blocks: the wrapped-plate exception (no directive; `press illustrate <name> --subject "..."`) now appears at step 2 and in the workflow paragraph. Example 11.1 and its lead-in now present the `plates:` section that alice adds to the file of Chapter 9's Example 9.1.
- Shoulds: "illustration" or "the plate" replaces "figure" for the unnumbered plate. The A-head is kept, and "acceptance" appears only for the record. "Logomark" is used throughout (defined at first use in the orientation), and "the alpha master" replaces "the transparent PNG" in the prose.
- Mays: `trim` is described as a key the press refuses to write (Chapter 3), with the hand-written mapping as the correction. *Commission* is defined at first use. The print-safe pass covers plates, figures, and the logomark rather than every image. The keys section now says a key is all the setup the press needs from each service.

`press check` names nothing in this file. Wordcount is 5428.
