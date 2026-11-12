"""Capture press desk headless (as tests/test_desk_app.py drives it) to SVG.
Usage: desk_shot.py BOOK OUTPREFIX COLS ROWS THEME"""
import asyncio, os, sys
from pathlib import Path
root, out, cols, rows, theme = Path(sys.argv[1]).resolve(), sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
os.chdir(root); os.environ["BOOK_ROOT"] = str(root)
from press.desk.app import DeskApp
async def main():
    app = DeskApp(root=root)
    async with app.run_test(size=(cols, rows)) as pilot:
        app.theme = theme
        await pilot.pause(); await pilot.pause(0.5)
        Path(out + "-desk.svg").write_text(app.export_screenshot(title="alice@hatter"))
        await pilot.press("p")
        await pilot.pause(); await pilot.pause(0.5)
        Path(out + "-picker.svg").write_text(app.export_screenshot(title="alice@hatter"))
asyncio.run(main())
