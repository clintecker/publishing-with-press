# Figures, the two screenshots (9.3 and 15.1)

Both figures are real captures, recaptured under the coordinator's rulings. Each is converted to 8-bit grayscale, framed with a 2 px (0.5 pt) black rule, 1362 px wide, mode L, at 300 dpi. I ran the format check from `tools/render-figures.sh` on its own and it passes for all 45 figures (`ok: 45 figures`, exit 0). I judged both PNGs at 50 percent zoom.

The capture scripts stay in the toolkit, as ruled, at `tools/figures/screens/`:

- `site_shot.py` drives headless Chrome over CDP, using the `Chrome` class from the press's `scripts/check_layout.py`.
- `desk_shot.py` drives `DeskApp` under Textual's `run_test`.
- `frame.py` has three modes: `site`, `desk` (with the inset picker) and `stack` (two crops of one page joined by a torn-edge gap band).

Their names do not start with `fig-`, so `render-figures.sh` does not run them.

The source is one scratch copy of `/Users/clint/code/press/examples/alice-in-wonderland`, with `slug` set to `alice` through `press config set slug alice`. The example already sets the drop-cap opening (`chapter-opening: style: drop-cap, lines: 3, small-caps-remainder: true`). No placeholders were created, because every referenced figure file already existed. No chapter file was edited.

## 09-03 A chapter page of the reader site

- Path: `assets/woodcuts/09-03-reader-site.png` (1362 x 1519)
- Archetype: screenshot, two crops of one page stacked
- Source: `dist/site/1-down-the-rabbit-hole.html` from the Alice example's `press site`. It was captured full-page in headless Chrome at 1100 CSS px wide, with `prefers-color-scheme: light` emulated, at device scale 2.
- Top crop (CSS y 0 to 985): the cloth at both sides, the paper column, the masthead "Alice's Adventures in Wonderland", the closed "Contents" drawer with the arrow pager, the small-caps "Chapter 1" line, the centered heading "Down the rabbit-hole", and the diamond rule. Then come the drop-cap paragraph (a three-line "A" with a small-caps first line) and the next two paragraphs.
- Gap band: 40 px of white with torn (zigzag) edges on both crops.
- Bottom crop (CSS y 7525 to 7735): the previous card ("Previous ← Alice's Adventures in Wonderland") and the next card ("Next The pool of tears →"), with the line "use ← and → to turn pages".
- Not drawn: the plate. The White Rabbit plate starts at CSS y 1010 and is 1,062 px tall. It does not fit beside the head and foot under the 1740 px cap, and the ruling allowed for that ("the plate if it fits"). The `fig-alt` mentions "a framed plate", so the editor may want to drop that phrase or accept the omission. Everything else in the `fig-alt` is shown.

## 15-01 The desk on hatter, with the target picker open

- Path: `assets/woodcuts/15-01-the-desk.png` (1362 x 1523)
- Archetype: screenshot, a composite of two real captures (the inset picker was accepted)
- Source: the same scratch copy. I deleted `dist/` and `build/`, ran `press pdf` (output `dist/alice.pdf`), and then took the capture. The site build for 09-03 came after the desk capture, so the site row still reads `- not built`.
- Capture: `DeskApp(root=...)` under `app.run_test(size=...)`, as `tests/test_desk_app.py` drives it, with the theme `textual-light`. It was exported with `app.export_screenshot(title="alice@hatter")` and rendered by `rsvg-convert -z 1.5`. The desk is 88 x 48 cells. After pressing `p`, the picker was captured at 40 x 18 cells and inset at the same cell scale, right of the artifact table. That position is clear of the state and published columns and above the toolchain line; the script asserts this.
- Grayscale uses the darkest of the RGB channels, so the green toolchain line and the blue cursor keep their contrast.
- What shows:
  - the window title "alice@hatter" and the real "DeskApp" header;
  - the identity line "Alice's Adventures in Wonderland / Lewis Carroll  6 x 9 in  alice";
  - the artifact table, with pdf at `o present, unverified` and the other ten rows at `- not built`;
  - the line "toolchain ready: this machine can build every artifact";
  - the doctor table, with 15 rows of glyphs: `* ok` everywhere except `- absent` for epubcheck. The API-key rows show presence only, as ruled.
  - the inset picker, showing "run a target", the target list, and the "arguments (optional)" box.
- Remaining note: the eye lands first on the black `pdf` cursor and its `o` state. The toolchain line reads clearly but is not the second thing the eye meets.

## Commands run

```sh
S=<session scratchpad>
B=/Users/clint/code/publishing-with-press
cp -R /Users/clint/code/press/examples/alice-in-wonderland $S/alice
~/code/.pwp-venv/bin/pip install -e '/Users/clint/code/press[tui]'
cd $S/alice && ~/code/.pwp-venv/bin/press doctor
~/code/.pwp-venv/bin/press config set slug alice
rm -rf dist build && ~/code/.pwp-venv/bin/press pdf

# 15-01
~/code/.pwp-venv/bin/python -I $B/tools/figures/screens/desk_shot.py $S/alice $S/D2 88 48 textual-light
~/code/.pwp-venv/bin/python -I $B/tools/figures/screens/desk_shot.py $S/alice $S/P2 40 18 textual-light
rsvg-convert -z 1.5 $S/D2-desk.svg -o $S/D2-desk.png
rsvg-convert -z 1.5 $S/P2-picker.svg -o $S/P2-picker.png
cd $B && python3 -I tools/figures/screens/frame.py desk $S/D2-desk.png $S/P2-picker.png assets/woodcuts/15-01-the-desk.png

# 09-03
cd $S/alice && ~/code/.pwp-venv/bin/press site
python3 -I $B/tools/figures/screens/site_shot.py $S/alice/dist/site/1-down-the-rabbit-hole.html $S/alice-full2x.png 1100 1000 2
cd $B && python3 -I tools/figures/screens/frame.py stack $S/alice-full2x.png assets/woodcuts/09-03-reader-site.png 1100 0 985 7525 7735

# format check (the PYEOF block of tools/render-figures.sh, run alone)
sed -n "/<<'PYEOF'/,/^PYEOF/p" tools/render-figures.sh | sed '1d;$d' > $S/check.py && python3 -I $S/check.py
```

Superseded first pass, for the record: the first 09-03 was captured from this book's own site (`press site` in `$B`, Chapter 1), and the first 15-01 had the slug `alice-in-wonderland`. Both were replaced under the rulings. Nothing was committed.
