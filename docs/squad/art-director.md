# Desk brief: art director

You own the plates and the cover. Read the press design skills first, in
full: `/Users/clint/code/press/src/press/data/skills/plates-and-woodcuts.md`,
`cover-design.md`, `press-logomark.md`, and `book-aesthetics.md`; then
`config/aesthetic.yaml`, `docs/design.md` sections 3 and 8, and
`docs/style-guide.md` section 6.

Plates: six are commissioned under `build/illustrations/` (the shop at
morning, the compositor at the frame, the witness that could say no, the
engraver's bench, the proofreaders' bench, the cuttlefish at its inkwell).
For each: judge it against the skill (one idea, correct perspective, level
floor, no humanoid robots, no torn-paper mat, no lettering, earnest
register); if it fails, recommission with `~/code/.pwp-venv/bin/press
illustrate <name> --style wood-engraving` after sharpening the `art:`
directive in the chapter (that is the one chapter edit you may make, and
you report it); then `press art accept build/illustrations/<name>.png --as
plate:<name>` and `press art enhance assets/woodcuts/<name>.png` (always
with the explicit path, never bare). Check the result composites on white
and on the dark Web palette.

Cover: the engraving is in `build/cover/cover.png` (a cuttlefish on white,
no lettering). Write `tools/cover.py` (Pillow) that composes an 1800 by
2700 cover: white ground; a deep sepia band (`#4a2e1a`) across the top
eighth carrying the series line "A Workbench Handbook" reversed out in
small caps at the right; the title "Publishing with Press" large, flush
left, under the band, in a condensed old-style serif (find one on this
machine or in the press's packaged fonts: Libertinus Serif condensed by
horizontal scaling to 82 percent is acceptable; record what you used); the
subtitle "Building Books from Plain Text" in italic beneath; the engraving
centre-to-lower-right at about 45 percent of the height, facing into the
title, keyed to transparency so no box shows; "Clint Ecker" bottom right;
"LGTM Publishing" small at bottom left. Nothing else. Then `press art
accept <png> --as cover`, and confirm the result on the PDF's first page
with `press pdf` and `press render`. Record the brief as the
`engraved-animal` style's note in `config/cover-styles.yaml` (already
present) and append the acceptance to `art/commissions.md` as `press art
accept` does.

Logomark: brief and commission a small printer's mark per the skill (a
cuttlefish in a roundel with the letters LGTM, single ink), accept it as
`--as logomark`, and check it at 0.5 in in one ink.

Report in `docs/briefs/reports/art.md`: each plate's verdict and what you
did, the cover's fonts and geometry, the logomark, every command you ran,
and anything the skills forbid that you could not avoid. Do not commit.

Return: status, the paths under `assets/`, and any recommission you made.
