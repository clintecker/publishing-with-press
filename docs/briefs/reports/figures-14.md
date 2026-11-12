# Figures, chapter 14

## 14-01 CI topology
- Path: assets/woodcuts/14-01-ci-topology.png (script tools/figures/fig-14-01-ci-topology.py)
- Archetype: client/CI topology (Canvas)
- Labels shortened: none. The monitor is drawn as a plain box with a stand (no monitor icon in the toolkit); "alice" sits beneath "hatter" in monospace. The registry crate is a plain box.
- Brief elements not drawn: none. Arrow labels are italic sans; "uses build.yml@v3" and "pull image by digest" and "publish release (tags)" are broken over two lines for space.

## 14-02 Resolving @v3
- Path: assets/woodcuts/14-02-resolving-v3.png (script tools/figures/fig-14-02-resolving-v3.py)
- Archetype: flowchart, top to bottom (Canvas)
- Labels shortened: none. "build.yml at v3.0.2" is set in monospace inside the heavy-ruled box (1.6 pt rule, the only non-house stroke weight, per the brief).
- Brief elements not drawn: none.

## 14-03 Release state machine
- Path: assets/woodcuts/14-03-release-state-machine.png (script tools/figures/fig-14-03-release-state-machine.py)
- Archetype: state machine, two snaking rows (Canvas)
- Order follows the brief and report-14 (pushed, tagged, built, verified). "floating tag moved" carries a 10 percent gray fill to hold the eye (grays are within the house set). The gloss for "floating tag moved" is "v3"; "release published" and "done" carry none, as the brief gives none.
- The fail arcs from "verified" and "contract proved" share one bus down the right edge into "stopped" (one arrowhead); the one from "release published" joins the same bus. The three fail labels sit on the built arc, the right bus, and the release-published drop. The dashed rerun arc runs up the left edge and enters "tagged" from below, so no arcs cross.
- Brief elements not drawn: none.

All three pass render-figures.sh (mode L, 1362 px wide, 300 dpi). Judged at 50 percent zoom: labels legible, nothing near the frame.
