# Art desk report

Art director, 2026-11-11. Nothing committed. No file under `book/` touched.

## Plates

All six were judged against `plates-and-woodcuts` (one idea, perspective,
level floor, no humanoid robot, no torn-paper mat, no lettering, earnest
register), accepted with `press art accept ... --as plate:<name>`, and
finished with `press art enhance assets/woodcuts/<name>.png` (2400x2400,
10-12 grays, alpha kept).

| Plate | Verdict | Action |
|---|---|---|
| the-shop-at-morning | Pass. One-point perspective, level boards, compact iron hand press, thin plain rule. | Accepted, enhanced. |
| the-compositor-at-the-frame | Pass. Correct stick-and-case posture, gas bracket, no lettering. | Accepted, enhanced. |
| the-witness-that-could-say-no | Pass, marginal. The brass lens apparatus is the "second inspector" as briefed; the front tray table is seen from a little higher than the reader's desk, but no floor shows and nothing reads as skewed. | Accepted, enhanced. |
| the-engravers-bench | **Fail, recommissioned.** The proof pinned to the wall showed the cuttlefish facing the same way as the block. A proof is the mirror of its block, and readers of a printing book will catch that. The graver was also held like a pen. | Recommissioned twice (see below). Accepted v3, enhanced. |
| the-proofreaders-bench | Pass. Three readers, a bell-and-lens apparatus, galleys on the line, a level table; the clock has numerals but no words. | Accepted, enhanced. |
| the-cuttlefish-at-its-inkwell | Pass. Correct anatomy (eight arms, two club tentacles, W pupil, full-length fin), ink cloud, inkwell and quill. | Accepted, enhanced. |

### The engraver's bench recommission

- v2 asked for the image to fill its rectangle to the edge. The model got
  the mirror right, but `press art accept` refused it ("only 29% of the
  border is light"): a full-bleed plate cannot be luminance-keyed. Kept at
  `build/illustrations/rejected/the-engravers-bench.v2-fullbleed.png`.
- v3 (accepted) puts the scene inside a thin rule on a white margin. The
  block faces right, the proof faces left, the graver is palm-held, and no
  landscape shows through the window. v1 is kept at
  `build/illustrations/rejected/the-engravers-bench.v1.png`.

**For the managing editor:** a suggested `art:` line for
`book/chapters/11-the-art-department.md` (line 4), matching the accepted
plate:

```
<!-- art: an engraver's bench by a north window, seen from slightly above and in front at a gently raised vantage with one consistent vanishing point and a level bench top: a boxwood block resting on a round leather sandbag, the engraver's right hand pushing a graver held in the palm with the handle against the heel of the hand, the left hand steadying the block; the block is half cut and shows a cuttlefish facing RIGHT; pinned to the wall behind is a proof pulled from that block, which shows the same cuttlefish mirror-reversed, facing LEFT, as a printed proof must be the mirror image of its block; a rack of burins and scorpers, a magnifying glass on a stand, a small brass proofing press at the bench's end, boxwood shavings on the bench; plain wall, no landscape through the window; the scene sits inside one plain thin black rule with a clean white margin all round it on a plain white sheet; landscape composition; wood engraving with dense hatching and crosshatching, single black ink, no gray washes, no lettering anywhere -->
```

### Compositing

- **On white:** all six key cleanly, with no ghost of the ground.
- **On the dark Web palette:** the reader's dark theme panels a plate on
  `--paper-warm`, which this book sets to `#242120`. Black ink on that
  nearly vanishes. I added `assets/web/extra.css`, which in dark mode only
  sets `figure img { background: #ece6dc; }`. Each plate then reads as a
  print laid on the dark page. The light theme is untouched. Drop the file
  if the design desk prefers another answer. The press's house rule
  (`figure img` on `--paper-warm`) has the same weakness for any book with
  a dark `paper-warm`, and is worth a press issue.

## Cover

- **Engraving** (`build/cover/cover.png`): an unlettered cuttlefish, no
  scenery, facing left. Its ground measures 252-255 (model noise on white,
  not cream) and the key takes it out completely, so it was not
  recommissioned.
- **Composer:** `tools/cover.py` (Pillow 11.1, system `python3`; no venv
  needed). It writes `build/cover/front.png`, accepted as `assets/cover.jpg`
  (1800x2700).
- **Fonts:** Libertinus Serif Regular and Italic (OFL, from
  `~/Library/texmf/fonts/opentype/public/libertinus-fonts`, found by
  kpsewhich). No Garamond is installed. Libertinus Serif condensed by
  horizontal scaling to 82 percent is the brief's sanctioned alternative.
  Pillow here lacks raqm, so OpenType `smcp` is unavailable and small caps
  are built from capitals at 74 percent, letterspaced.
- **Geometry (px):**
  - Sepia `#4a2e1a` band 0-338 (the top eighth). "A Workbench Handbook" in
    small caps (58/43 px), white, flush right at a 120 px margin.
  - Title "Publishing with Press" on one line at 214 px, condensed to 82
    percent, flush left at x=114, top at y=448.
  - Subtitle in Libertinus Italic at 104 px directly beneath.
  - Engraving keyed (luminance key, ground >= 246 clear) and scaled to
    1560x779, right edge at x=1720, top at y=1301.
  - "Clint Ecker" at 92 px, flush right, baseline y=2550. "LGTM
    Publishing" in small caps (44/33 px), flush left on the same
    baseline. Nothing else.
- **Departure:** the animal is landscape, so at the full width of the
  measure it stands 29 percent of the cover's height, not 45. The field it
  sits in (subtitle to foot) is about 45 percent. Making it taller would
  mean cropping it or running it off the trim.
- **Record:** the brief is in the `engraved-animal` style's `note` in
  `config/cover-styles.yaml` (shown by `press cover --list`). The
  acceptance is in `art/commissions.md`.

## Logomark

- **Brief:** written into `art/commissions.md` under `## Logomark`. A
  cuttlefish facing left in a double-ruled roundel, with LGTM in a roman
  serif inside a ruled band. Single ink, on transparency.
- **Press defect:** `press art commission logomark --model openai` fails.
  The logomark shape is pinned to `gpt-image-1`, which the API now rejects
  ("The model 'gpt-image-1' does not exist"). This is in
  `press/src/press/art_commission.py`, `OPENAI_TRANSPARENT`, and should be
  filed against the press.
- **Commission:** ran `--model gemini --count 2`. Gemini painted a fake
  transparency checkerboard into an opaque RGB image. `press art accept`
  extracted the ink and the corners came out fully clear (alpha 0).
- **Accepted:** `art/candidates/logomark/gemini-2.png` (the bolder line),
  as `assets/press-logo.png`. LGTM is spelled correctly.
- **At 0.5 in, one ink, thresholded:** the roundel and LGTM read. The
  cuttlefish fills in toward a silhouette but holds its shape.
- **On dark:** the landing page has no dark theme, so the mark always sits
  on paper there. Raw black-on-dark is illegible, which matters only if a
  dark landing footer is ever added.
- It renders on the colophon page (PDF page 3).

## Proof

- `press check`: exit 1, only on the editorial paragraph-length law in
  `book/chapters/02-installing-press.md` (paragraphs 40, 104, 118). That is
  a writer's file, not art.
- `press pdf` in the repo: exit 43. LaTeX cannot find the numbered figure
  `assets/woodcuts/01-01-pipeline-overview.png` (the expected missing
  figures). The `dist/` PDF there is from an earlier run by someone else.
- I proved the art in a scratch copy of the repo, with blank stand-ins for
  the 12 missing numbered figures: `press pdf` exit 0, 97 pages.
  - Page 1: the composed cover (1800x2700).
  - Page 3: the colophon with the logomark.
  - Plates at pages 12 (the shop at morning, at the head of chapter 1),
    67, 83, 86, 90 and 97. All render, single ink on white.
  - The shop plate carries `{place=frontispiece}` but lands at the head of
    chapter 1, not facing the title page. Worth the managing editor's
    attention; it is not an art fault.

## Commands run (from the repository root)

```
press illustrate the-engravers-bench --style wood-engraving --subject "<v2 brief>"   # refused at intake: full bleed
press illustrate the-engravers-bench --style wood-engraving --subject "<v3 brief>"   # accepted
press art accept build/illustrations/<name>.png --as plate:<name>                    # x6
press art enhance assets/woodcuts/<name>.png                                         # x6
python3 tools/cover.py
press art accept build/cover/front.png --as cover
press cover --list
press art commission logomark --model openai --count 2                               # failed: gpt-image-1 retired
press art commission logomark --model gemini --count 2
press art accept art/candidates/logomark/gemini-2.png --as logomark
press check
press pdf
```

(`press` is `~/code/.pwp-venv/bin/press`.)

## What the skills forbid that could not be avoided

- **Square plates.** The skill asks for a deliberate landscape or portrait
  plate. `press illustrate` hard-codes 1024x1024 (`_SPEC` in
  `illustrate.py`), so every plate is square despite "landscape
  composition" in each brief. The plates use the square well, but on the
  6x9 trim they waste some width. A press fix would honour the brief's
  stated orientation, as `press art commission` already does.
- **Square plates in a near-white margin.** Every plate except the
  compositor, the witness and the cuttlefish has a thin plain rule, which
  the skill permits.
- **The logomark through Gemini.** Gemini is not the transparency-capable
  model the press intends for marks; the intake's ink extraction made up
  for it.
- **The cover type is not Garamond.** It is Libertinus condensed, the
  brief's sanctioned fallback.

## Note for the desk

At the start of this run `assets/woodcuts/` held four untracked files
(`00-proof-pipeline.png`, `00-proof-stack.png`, `00-proof-tree.png`,
`proof-check.png`). They disappeared while this desk worked. No press
command I ran deletes files (I checked `art.py` and `art_enhance.py`).
Another desk probably cleaned up its proofs.
