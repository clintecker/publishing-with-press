# Screenshots

Three figures are screenshots of real output. Take them from a real build,
convert to 8-bit grayscale, box them with a 0.5 pt rule, and save at 1362
px wide under `assets/woodcuts/` with the figure's slug. Use the figure
toolkit's `look.frame_screenshot(path_in, path_out)` if present; otherwise
Pillow.

- Reader site page (Chapter 9): build with `press site`, open
  `dist/site/<a chapter page>.html` in headless Chrome at 1100 px wide,
  light theme, capture the viewport from the chapter heading down past the
  first figure. The press checkout's `scripts/check_layout.py` shows how it
  drives Chrome.
- Landing page (Chapter 9 or 14, if briefed): `press pages`, open
  `dist/pages/index.html` the same way.
- The desk (Chapter 15): `press desk` needs the `tui` extra; install it in
  the venv (`~/code/.pwp-venv/bin/pip install -e '/Users/clint/code/press[tui]'`)
  and capture through Textual's headless screenshot support as the press's
  own `tests/test_desk_app.py` does (it saves an SVG; render the SVG with
  `rsvg-convert` to PNG). If that cannot be made to work in an hour, draw
  the desk from its description in the chapter's fact file as a
  terminal-panel figure and say so in the report.
