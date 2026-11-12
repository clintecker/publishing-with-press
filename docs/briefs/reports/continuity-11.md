# Continuity report: Chapter 11, *The art department*

Desk: continuity editor. Chapter read as it stands after its desks, its
re-review, and the final small revision (527 lines). Cross-checked against
Chapters 1 to 4 and 8 (committed), the drafts of 5, 7, 9, 10, 12, 15, 16 and
Appendixes B and C that Chapter 11 cites or that cite it, `docs/vocabulary.md`,
and `docs/design.md` section 5.

Status: **PASS WITH FIXES.** Two blocks, three should, four may. Both blocks
are cross-chapter: Chapter 11 contradicts Chapter 5 on wrapped plates
(finding 1) and Chapter 9 on the Alice book's aesthetic file (finding 2).
Each is a one-sentence fix in Chapter 11.

What holds:

- The old bible conflict on *target* is closed. The chapter now says *art
  target* every time (defined l.51; Table 11.5 "The art targets"; l.418 to
  425, 484 to 519). No bare "target" names an `--as` value.
- Every cross-reference out is right in number and title: Chapter 5,
  *Figures, plates, and illustrations* (l.220, 316); Chapter 9, *The house
  design* (l.86); Chapter 12, *The print pack* (l.102); Chapter 15, *The
  operator's desk and the editorial machines* (l.55, 375). Each target
  delivers: Ch. 5 Example 5.1 declares `white-rabbit` with an `art:`
  directive and Ch. 5 l.351 to 372 describes the print-safe pass; Ch. 9
  Table 9.7 lists the aesthetic keys that reach the build; Ch. 12 l.62
  describes `house-6x9-color`; Ch. 15 "Workflows" (l.133), "Skills"
  (l.261), "art-direction" (l.251), and "Running a workflow headless"
  (l.297) describe skills, workflows, and how a workflow runs. Ch. 15 l.259
  ("No operator command runs `art-direction`") agrees with step 3 (l.49).
- Internal pointers run the right way: "Table 11.7, in the last section"
  (l.18; the table is at l.482 in the last A-head); "Intake: what acceptance
  enforces later in this chapter" (l.90; at l.250); "The commission record
  later in this chapter" (l.234; at l.371); "One master, every surface later
  in this chapter" (l.282; at l.312); "@fig:one-master-every-surface in the
  previous section" (l.314; the figure is at l.284, in the previous A-head).
- Promises kept. Ch. 2 l.248 (generating art, where `OPENAI_API_KEY` and
  `GEMINI_API_KEY` matter): kept by "Keys, models, and what spends money"
  (l.470 to 525, Table 11.7). Ch. 5 l.67 (the commission from directive to
  finished plate): kept (l.236 to 242, Example 11.4). Ch. 5 l.321 (the
  luminance key and intake's refusals): kept (l.288 to 310). Ch. 5 l.325
  (the image-model key "which Chapter 11 sets up"): kept for the key
  (l.472 to 478); see finding 9 for the account. The shape keywords:
  Ch. 5 footnote `5-square` and l.343 (every `press illustrate` delivery is
  a 1024 square) agree with l.234 (press #278), and l.412 states the
  "landscape composition" / "portrait composition" rule for `press art
  commission` with "at the time of this writing", per facts-11 finding 3.
  Inbound promises also kept: Ch. 3 l.120 (*art/* commissions and
  candidates: l.373, 425); Ch. 7 l.246 (how a book gets its cover: "Covers"
  and Table 11.5); Ch. 9 l.100 (Chapter 11 names the other craft laws:
  l.102 names all four); Ch. 9 l.260 (art direction for cover, plates,
  logomark, portrait); Ch. 10 l.412 (next chapter turns to pictures);
  Ch. 12 l.215 (the making of the cover art); Ch. 15 l.253; Ch. 16 l.39;
  App. B (cover and illustration style keys, `plates.medium` and the
  "single"/"ink" rule, `cover.style` default `penguin-tri-band`, the subject
  chain, the merge rule, no validator); App. C l.448 (intake refusals
  belong to Chapter 11: l.270, 292, 377, 224 quote them).
- Terms that the bible already held agree: *the aesthetic* (l.61: visual
  identity in *config/aesthetic.yaml*, merged with the house), *intake*
  (l.252), *alpha master* (l.280: colour channels (0,0,0), tone in alpha).
  *skill* (l.47) and *workflow* (l.49) agree with Ch. 15's definitions
  (l.263, l.26) and the vocabulary. The Workflow tool (l.49) agrees with
  Ch. 15 l.28.
- Shared facts agree: `press illustrate` (1024 by 1024, `gpt-image-2`,
  *build/illustrations/<name>.png*, the style chain, the three refusals,
  the guardrail word for word); asset paths (Table 11.5 against Ch. 5
  l.319); plate intake (name pattern, the "single"/"ink" test, the cover
  aspect as the only shape check, against Ch. 5 l.321, 341); `press art
  enhance` (four steps, 2400 px, 16 grays, oxipng/pngcrush, the upscaler
  search, amd64 only, against Ch. 5 l.339 to 349 and Ch. 2 l.167); the
  height cap left to the TeX header (l.272); the Lulu story (l.316, against
  Ch. 5 l.366 and Ch. 12 l.265); the baked-JPEG scar quoted the same way as
  Ch. 5 l.323; `house-6x9-color` keeping plates in colour (l.280, against
  Ch. 9 l.76); the aesthetic's top-level merge and "restate a whole section
  when you touch it" (l.67 to 69, against Ch. 9 l.314 and App. B l.249);
  `--overwrite` on `press aesthetic` (l.100, against Ch. 15 l.305).
- Cast clean: the Alice book, `alice`, `hatter`, `printshop`. Other names
  are real (Tenniel, Lustig, Rand, Edward Young, Jan Tschichold, Lulu,
  Upscayl, Real-ESRGAN, OpenAI, Google) or the Alice book's own style id
  `nursery-gilt`. No "Alice example".
- Numbering clean: Figures 11.1 `11-01-art-direction-loop`, 11.2
  `11-02-one-master-every-surface`, 11.3 `11-03-intake-before-after`,
  design.md order, each cited before it appears (l.39, 282, 294), each
  followed by one blank line and its `art:` comment; files present (5 KB
  placeholders). Tables 11.1 to 11.8 and Examples 11.1 to 11.4, no gap, no
  repeat. Plate *the-engravers-bench.png* unnumbered, present (4.2 MB), as
  design.md names it. Footnotes `11-penguin`, `11-ink`, `11-band`,
  `11-upscayl`, `11-imagen`, prefixed and unique. Every fence tagged
  `text`, none over 64 columns (Example 11.3's inner fences sit inside a
  four-backtick `text` fence). The "In this chapter" box lists the ten
  A-heads exactly.

## Findings

### 1. "An `art:` directive on every figure" contradicts Chapter 5's wrap rule (blocks)

Quotes: l.48 "Declare each figure in the manuscript with an `art:`
directive." l.375 "an `art:` directive on every figure that `press figures`
reports."

Against: Ch. 5 l.250 "A wrapped illustration cannot carry an `art:` comment
without losing its runaround ... Commission a wrapped plate with `press
illustrate <name> --subject "..."` instead", and Example 5.5; bible shared
fact "Measures and the wrap" (press issue #280). Chapter 11 never mentions a
wrap, so the reader who follows its loop gives a wrapped plate a directive
and silently loses the wrap. The promise to carry the `--subject` route into
the art department is not kept: l.220 mentions `--subject` only as the way
around the manuscript lookup.

Rule: shared fact contradicted (blocks).

Fix: after step 2 (l.48), add: "A wrapped plate is the exception. It carries
no directive, because the comment would break the wrap (Chapter 5, *Figures,
plates, and illustrations*); commission it with `press illustrate <name>
--subject "..."`." At l.375, "on every figure ... except a wrapped plate".

### 2. Example 11.1 is captioned as the whole Alice aesthetic file, and Chapter 9 gives a different one (blocks)

Quotes: l.71 "Example 11.1 shows a *config/aesthetic.yaml* for the Alice
book." Caption l.73 "The Alice book's config/aesthetic.yaml". The example
holds only `plates:`.

Against: Ch. 9 Example 9.1 ("An aesthetic file for the Alice book", l.279 to
302), which `alice` writes with `web-palette`, `web-palette-dark`,
`book-colors`, and `scene-break: fairy-dust`, and no `plates:`. Read as the
file, Example 11.1 throws away the whole of Chapter 9's palette, and the
chapter's own merge rule (l.67) says that a section absent from the file is
the house's.

Rule: shared fact contradicted, the contents of one file (blocks). New
shared-fact row "The Alice book's aesthetic file".

Fix: caption "The plates section of the Alice book's config/aesthetic.yaml";
l.71 "Example 11.1 adds a `plates:` section to the Alice book's
*config/aesthetic.yaml*, the file of Chapter 9's Example 9.1, and restates
every key in it."

### 3. The plate is still "the figure" (should)

Quotes: l.48 "Declare each figure"; l.218 "the figure's own `style=`
attribute"; l.220 "It looks for the figure whose image file stem equals the
name ... that figure's image line ... when no chapter declares the figure,
when the figure is a data kind ... when the figure has no `art:` directive";
l.238 "Confirm that the figure from Example 5.1 has an `art:` directive";
l.375 "every figure that `press figures` reports".

Against: vocabulary (figure = a numbered informative illustration;
illustration = the general class); Ch. 5 l.22 and l.67 ("finds the
illustration whose image file stem matches the name"). Example 5.1 is a
plate (no class). This is continuity-05 finding C, still open; the same
sentences also say "chapter" where Ch. 5 says "the manuscript" (an appendix
image line counts too; l.57 "no chapter references" has the same narrowing,
against shared fact "Orphan plate refusal").

Rule: one thing, two names (should).

Fix: "illustration" for the general class at each place above; "the plate
from Example 5.1" at l.238; "no image line in the manuscript" at l.57 and
l.220.

### 4. A-head "Intake: what acceptance enforces" (should)

Quote: l.10 and l.250, the A-head; l.90 cites it by name.

Against: vocabulary, intake: "never ... acceptance (use for the record)".
The chapter keeps "acceptance" for the record everywhere else (l.34, 252,
444).

Rule: second name for one thing (should). The Preface's Organization
section will copy the A-head.

Fix: "Intake: what `press art accept` enforces", or "What intake enforces";
change the box (l.10) and l.90 to match.

### 5. "the transparent PNG" for the alpha master; "imprint logo" and "a book's logo" for the logomark (should)

Quotes: l.318 "The Chapter edition (the reader site) serves the transparent
PNG as it is" (also Figure 11.2's art label, l.286, "Chapter edition,
transparent PNG"); l.318 "which is how the imprint logo already works";
l.316 "Lulu once flagged a book's logo".

Against: vocabulary, alpha master: "never transparent PNG, master file".
The chapter defines *logomark* (l.448) and uses it elsewhere; Ch. 5 says
logomark throughout. (Across chapters the same file is "the press logo" in
Ch. 3 l.120, "logo" in Ch. 10 l.176, 184 and Ch. 12 l.215, 261, 265; the
vocabulary has no row for it. Recommend a ledger ruling: *logomark*, with
"logo" allowed only in the Lulu story.)

Rule: second name for one thing (should).

Fix: l.318 "serves the alpha master as it is" and "which is how the
logomark already works"; l.316 "flagged a book's logomark". The figure label
may keep "transparent PNG" as a file description if the art desk wants it.

### 6. "A 5 by 8 book that does not set `trim`" (may)

Quote: l.272 "Intake reads the trim from `trim` in *config/metadata.yaml*
and takes it as 6 by 9 when the key is absent ... A 5 by 8 book that does not
set `trim` therefore has its cover checked against 6 by 9."

Against: Ch. 3 l.269 and l.354: the press derives `trim` from the profile
and refuses a direct write ("trim is not set directly; choose it with
print.profile"); only an older book's `trim` mapping survives, and it must
agree with the profile. Not a contradiction, but the sentence reads as if
setting `trim` were the normal remedy, and `press config set trim` refuses.

Rule: shared fact stated loosely (may).

Fix: "A book made by a current press has no `trim` key, since the press
refuses a direct write (Chapter 3), so a 5 by 8 book has its cover checked
against 6 by 9. A hand-written `trim` mapping that agrees with the profile
corrects the check."

### 7. "commission" is used and never defined (may)

Quotes: l.22 "Press treats the art as a one-time commission" (the act);
l.373 "holds the book's commissions" (the prompts); l.442 "A plate
commission also carries style" (the request); l.454 "the portrait
commission".

Against: vocabulary, commission: "a prompt for an image model, in
`art/commissions.md`", first use italic and defined. The chapter defines
every other art term it names.

Rule: may.

Fix: at l.373, "The file *art/commissions.md* holds the book's *commissions*,
the prompts for the image models, and the record of what the book
accepted."

### 8. The print-safe pass "flattens every image" (may; continuity-05 finding D still open)

Quote: l.316 "does this for every image in the print interior ... the pass
now flattens every image and caps its resolution."

Against: Ch. 5 l.364 ("The pass does not copy every image"; only the
logomark, top-level *assets/* JPEGs, and *assets/woodcuts/*).

Rule: may (as logged for Ch. 5).

Fix: "for every plate, figure, and logomark in the print interior".

### 9. Chapter 5's "account and key, which Chapter 11 sets up" is half kept (may, for Chapter 5)

Quote (Ch. 5 l.325): "it needs that service's account and key, which
Chapter 11 sets up." Chapter 11 sets up the key (l.472 to 478) and says
nothing of opening an account. Fix in Ch. 5: "needs that service's API key,
which Chapter 11 sets up."

## Bible

Updated `docs/continuity.md`: the status note; terms *target* (conflict
closed), *plate* (finding C still open, new lines), *the aesthetic*, *alpha
master*, *intake* (line numbers); shared facts "Measures and the wrap"
(finding 1), "Print-safe pass" (finding 8); promise rows Ch. 2 l.248 and
Ch. 5 l.67, l.321/325 (kept). Added 12 terms, 11 shared facts, 7
cross-reference rows, and the Chapter 11 numbering row (31 entries).
