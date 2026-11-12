# Cut report: Chapter 2 and Appendix B

Files: book/chapters/02-installing-press.md, book/appendices/b-configuration-reference.md.

Words: 02 5738 -> 5654. B 5401 -> 5408.

## book/chapters/02-installing-press.md

1. Retold (CI=false, keeper Ch 8), `02:277`.
   Before: "The press chose its own variable on purpose, because the ambient `CI` variable has a trap: `CI=false` is truthy."
   After: "The press chose its own variable instead of the ambient `CI` (Chapter 8 says why)."
2. Retold (BROKEN probes, keeper Table 2.4), `02:246`.
   Before: "A tool that fails both `--version` and `-v` within 15 s counts as broken, whatever `which` says about it."
   After: "A tool that fails both probes counts as broken, whatever `which` says about it."
3. Retold (scar defined, keeper Ch 1), `02:210`.
   Before: "The package `fonts-linuxlibertine` is a *scar*, the press's word for a production failure turned into a guard."
   After: "The package `fonts-linuxlibertine` is a scar."
4. Retold (macos-14 runner, keeper Ch 14), `02:333-335`: footnote `[^2-macos]` and its marker. Cut.
5. Retold (font scan, keeper is this chapter's sidebar), `02:377`: "The scan belongs to LuaLaTeX, and press does not hurry it. If a build on a fresh machine seems to hang for several minutes, wait: it is almost certainly the scan." Cut.
6. Tic (plainly), `02:43`.
   Before: "Its install guide says so plainly:"
   After: "Its install guide says:"
7. Tic (word count), `02:341`.
   Before: "The install guide states the supported platforms in one sentence:"
   After: "The install guide states the supported platforms:"
8. Tic (word count, not listed in the brief, covered by the cutter brief's general rule), `02:372` sidebar.
   Before: "The press's scars list records the behavior in two flat sentences:"
   After: "The press's scars list records the behavior:"
9. Maxim cut, ends earlier, `02:192`: "One package in it needs a warning first." Cut.
10. Maxim cut, ends earlier, `02:337`: "Contributors to the press need no emulation either." Cut.
11. Should, `02:55-71`: the `python3-venv` paragraph and its `sudo apt-get install python3-venv` block moved, verbatim, from after Example 2.1 to directly above it.
12. Should, after Table 2.2: added "To take a new release on your workstation, run `pip install --upgrade "press @ git+https://github.com/clintecker/press@v3"`. The floating tag moves on GitHub, not in your environment." (The brief's semicolon became a period, per the no-semicolon rule.)

Protected/kept: the font-scan sidebar (keeper), the `fonts-linuxlibertine` warning at `02:194-196` and the rest of `02:210` (keeper), the tag definitions at `02:75-81`, the maxims marked keep (`02:266`, `02:341`).

## book/appendices/b-configuration-reference.md

1. Should, `B:335`.
   Before: "The press sends you to the file or to the index workflow instead of the shell."
   After: "The press's help text names an "index workflow", but at the time of this writing none ships, so edit the file by hand." (The brief's semicolon became ", but", per the no-semicolon rule.)

`B:83` keeps its sentinel sentence, as the brief says. No other entry names Appendix B.

## press check

`~/code/.pwp-venv/bin/press check` passed: source checks, checker self-test, editorial checks, jargon check.
