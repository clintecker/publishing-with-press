# Report: Chapter 2, Installing press

## Word count

`press wordcount`: 5,309 for `book/chapters/02-installing-press.md` (target 5,000; within 15 percent).

## Figures

- Figure 2.1 `@fig:doctor-report` (terminal): a grayscale 72-column terminal titled alice@hatter, reproducing the fact file's `press doctor` output character for character; the reader sees the bracketed state column first, then the absent and BROKEN lines, then the "not ready: claude" line.
- Figure 2.2 `@fig:tools-in-the-build` (data-flow, top to bottom): the manuscript, an arrow labelled "Lua filters" into pandoc, then PDF (latexmk to LuaLaTeX), EPUB and HTML (pandoc writers) branches, converging on a drop-shadowed verify box with `epubcheck`, `pdftoppm`, `pdffonts` in monospace on the arrows.
- Figure 2.3 `@fig:local-versus-container` (topology): hatter (native toolchain, "may lack" epubcheck, wrapfig, lettrine), the `~/alice` repository cylinder in the centre, the toolchain image crate with `ghcr.io/clintecker/press-toolchain@sha256:...`; arrows labelled with what flows (chapters and config, dist/, mounted at /book, docker pull).

## Tables, examples, admonitions, footnotes

Tables 2.1 to 2.4; Examples 2.1 to 2.5; three tips, three warnings (fonts-linuxlibertine, grep before &&, the epubcheck that cannot run); one sidebar ("The hang that isn't", war story 10); four footnotes (YAML 1.1 booleans, celebrimbor dev-only, the Dockerfile's "epubcheck/binfmt scar", the macos-14 retirement).

## Facts needed and not found (left out)

- `scripts/dev-render.sh`: named in design.md's row for this chapter, absent from facts-02. Not mentioned.
- The `warn` doctor state: listed but undefined in the fact file. Left out of Table 2.4.
- `press --version` output format: not given. Example 2.1 elides it with `...`.
- How to combine the `tui` extra with the Git URL: the fact file gives only `pip install 'press[tui]'` (which would hit PyPI, where press is not published). The chapter quotes that spelling and tells the reader to add `[tui]` to whichever requirement form they use; the reviewer may want to confirm `"press[tui] @ git+...@v3"`.
- wrapfig: the brief's Figure 2.3 names it as something a workstation may lack; facts-02 never mentions wrapfig. It appears only in the art directive, never in prose.
- The digest location: the chapter promises Chapter 14 shows where to find the reusable workflow's pinned digest.

## Contradictions and hazards handled

- Docs say a `sha-` tag pins the toolchain; the chapter uses the `@sha256:` digest wording (A.2).
- Doctor's `pdfimages` blind spot and "broken optional tool denies readiness" are listed as bug-like (B.14); the chapter states neither as a rule. It shows the BROKEN claude line and says only that the final line names claude.
- The fact file's capture had BROKEN claude from a sandbox; the chapter attributes it to "that run" on hatter.
- Gemini spend-by-default (B.15) not mentioned. pipx not named; the chapter says pip is the only installer the press documents. Windows: one sentence, "Windows is not tested."
- Version numbers used are only those in facts-02: Python 3.10 to 3.14, 3.12, macOS 15, Ubuntu 24.04, v3/v3.0.2, macos-14/15. No pandoc or TeX version.

## Checker residuals (`tools/ste_check.py`) and defence

- Lines 115, 202, 213, 220, 221, 311: art directives (doctor output, figure briefs) trip sentence length, paragraph length, and semicolons. These are comments, not prose.
- Line 158: semicolon inside a verbatim quotation from the install guide.
- Line 380: the index comment (semicolon separated by the brief).
- Lines 35 and 88: sentence counter joins two sentences across a footnote marker (`[^yaml] Its`, `[^dev] None`); each real sentence is under 25 words.
- Lines 356, 364: 26-word sentences, under the 30 ceiling.
- `-ing` heading words (Installing, Running, Reading, Pulling) are the brief's required A-heads or gerund B-heads in the style guide's idiom. "therefore", "whether" are period-correct per the prose contract. "verify"/"enhance"/"attempt" are press target names or literal flags.

`press check` reports no error naming this file. It currently fails on unreferenced plates belonging to other files (00-proof-*.png, proof-check.png, the-proofreaders-bench.upscaled.png).
