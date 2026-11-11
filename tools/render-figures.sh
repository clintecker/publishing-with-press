#!/usr/bin/env bash
# Render every figure into assets/figures/ and check the house output format.
# Usage: tools/render-figures.sh        (from anywhere)
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
PY=python3
[ -x "$ROOT/.venv-tools/bin/python3" ] && PY="$ROOT/.venv-tools/bin/python3"
export PYTHONWARNINGS=ignore
mkdir -p assets/figures

shopt -s nullglob
for f in tools/figures/fig-*.py; do
  echo "== $f"
  "$PY" "$f"
done
for t in tools/figures/*.txt; do
  name="$(basename "$t" .txt)"
  title=""
  [ -f "tools/figures/$name.title" ] && title="$(head -n1 "tools/figures/$name.title")"
  echo "== $t"
  "$PY" tools/figures/terminal.py "$t" "assets/figures/$name.png" --title "$title"
done

"$PY" - <<'PYEOF'
import sys
from pathlib import Path
from PIL import Image

rows, bad = [], []
for p in sorted(Path("assets/figures").glob("*.png")):
    im = Image.open(p)
    dpi = im.info.get("dpi", (0, 0))
    dpi = tuple(round(float(d)) for d in dpi)
    rows.append((p.name, im.width, im.height, im.mode, f"{dpi[0]}x{dpi[1]}",
                 p.stat().st_size))
    if im.mode != "L":
        bad.append(f"{p.name}: mode {im.mode}, want L (8-bit grayscale)")
    if im.width not in (1800, 900):
        bad.append(f"{p.name}: width {im.width}, want 1800 or 900")
    if dpi != (300, 300):
        bad.append(f"{p.name}: dpi {dpi}, want (300, 300)")
fmt = "{:<34} {:>6} {:>6} {:>5} {:>8} {:>9}"
print()
print(fmt.format("file", "width", "height", "mode", "dpi", "bytes"))
for r in rows:
    print(fmt.format(*r))
if not rows:
    bad.append("no PNGs in assets/figures/")
if bad:
    print("\nFAIL:", *bad, sep="\n  ", file=sys.stderr)
    sys.exit(1)
print(f"\nok: {len(rows)} figures")
PYEOF
