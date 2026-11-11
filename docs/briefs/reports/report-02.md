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

## Figure notes

- Figure 2.1 `@fig:tools-in-the-build`, file `assets/woodcuts/02-01-tools-in-the-build.png` (data-flow). The directive is complete. Square corners for file icons, rounded corners for pandoc, LuaLaTeX, and verify. The PDF and EPUB file icons are labeled with the slug `alice`.
- Figure 2.2 `@fig:doctor-report`, file `assets/woodcuts/02-02-doctor-report.png` (terminal). The panel shows the prompt line `$ press doctor` and then this capture, verbatim. Per ruling 8, the capture's duplicated bare `press doctor` first line is dropped. Lines over 72 columns stay as captured, and the panel wraps them as a terminal would. Keep the blank line before `not ready:`.

```text
  [     ok] pandoc     every build target
  [     ok] lualatex   PDF and print builds
  [     ok] latexmk    PDF and print builds (multi-pass convergence)
  [     ok] pdftoppm   PDF verification renders
  [     ok] pdffonts   font-embedding verification
  [     ok] pdfinfo    PDF structure verification
  [     ok] pdftotext  PDF text verification
  [     ok] git        scaffolding identity and book repositories
  [ absent] epubcheck  the retail EPUB gate (softens to a warning locally)
  [ BROKEN] claude     present but cannot execute; the operator: press improve, research, aesthetic briefs
  [     ok] realesrgan plate enhancement upscaling (press art enhance)
  [     ok] OPENAI_API_KEY   press art commission --model openai
  [     ok] GEMINI_API_KEY   press art commission --model gemini
  [     ok] python     3.12 is within the tested range 3.10 to 3.14
  [     ok] python     Pillow, pypdf, ruamel.yaml importable

not ready: claude (macOS: brew install pandoc mactex-no-gui poppler; Debian/Ubuntu: see the Dockerfile's package list)
```

- Figure 2.3 `@fig:local-versus-container`, file `assets/woodcuts/02-03-local-versus-container.png` (topology). Per ruling 3, the "may lack" list is `epubcheck` and `java` (the Java that runs the epubcheck jar). wrapfig and lettrine are gone. Use rounded corners for the two machines and square corners for the cylinder's label.

## Revision (after four desks)

Word count after revision: 5,199 (`press wordcount`). Every `art:` block is under 190 words with its image line (177, 132, 161). The sidebar is 142 words.

Coordinator rulings: 1 to 9 applied. On ruling 4, the chapter now references `02-01-tools-in-the-build.png`, `02-02-doctor-report.png`, `02-03-local-versus-container.png`. The untracked placeholder PNGs on disk still carry the old names, so `press check` now reports "plate never referenced" for `02-01-doctor-report.png` and `02-02-tools-in-the-build.png`. Those are not my files, so I left them. The controller should swap the two placeholder names (or regenerate them).

### Fact checker (facts-02.md)

- Unsupported 1: applied. The BROKEN causal claim is cut. The verifier "draws the same line", and the forward pointer is reworded.
- Unsupported 2: applied. All "first book" provenance and "cost real time" text is cut. The sources are now the scars list and law 4.
- Unsupported 3: applied (ruling 3).
- Unsupported 4: applied ("does not install this press").
- Unsupported 5: applied, using supplement S2's two forms (Example 2.3). The clone form puts the brackets after the path, in `"$HOME/src/press[tui]"`, because a quoted `~` would not expand.
- Unsupported 6: applied ("contains spaces").
- Unsupported 7: applied. Only "`CI=false` is truthy" is kept.
- Unsupported 8: applied. The sidebar and the surrounding prose state only the file's facts. The restart claim is cut.
- Unsupported 9: applied. The tip's timing is cut.
- Unsupported 10 (may): applied in part. The MacTeX size gloss, the support-request line, "many libraries still read", the "gates every press change" claim, and the amd64 advice are cut. The operator-console wording became "full-screen console in the terminal". Declined: "Pillow handles images", which is general knowledge about a named dependency.
- Contradicted 1: applied (ruling 2). The behavior is stated plainly, and the reader is told to read the report and not chain a build on the exit status.
- Contradicted 2: applied. "Every verifier" and "every edition" are gone. The print interior and cover wrap are named as separate targets.
- Contradicted 3: applied. The not-ready line wording is now the fact checker's.
- Drifted 1: applied. Table 2.3 prints the doctor's text verbatim in code, and the required/optional status is in the Tool column.
- Drifted 2: applied (the file's wording, "fails both ... within 15 s").
- Drifted 3: applied ("In the arm64 image").
- Drifted 4: applied ("For a broken tool").
- Drifted 5: applied (clause cut).
- Drifted 6: applied. "In a commit chain" is restored, and the scar is quoted verbatim.
- Drifted 7: applied ("until you generate art").
- Drifted 8: applied ("Among other things").
- Drifted 9: declined. The aligned third line runs 79 columns, and the markup law caps fences at 72. I kept the comment text verbatim and added one sentence saying the spacing was narrowed.
- Drifted 10 to 13: applied.
- Missing 1: applied. The `pdfimages` behavior is stated as fact, not as a feature.
- Missing 2: applied (ruling 2).
- Missing 3 (may): declined. `warn` is still undefined in the facts. Table 2.4 says "most often".
- Missing 4 (may): applied ("install the same three-part press tag").

### Developmental editor (dev-02.md)

- B1: applied. The new B-head "The developer's render loop" (about 220 words) comes from supplement S1, with the audience stated as press developers. The Colima limit (#276) is left out, because this chapter names no platform beyond the facts' and a book author never runs the script.
- P1: applied. The new B-head "Choosing where the package goes" gives the virtual environment as the book's own advice and names PEP 668 as Python's rule. Example 2.1 creates and activates *~/.press-venv*.
- P2: applied. The procedure stops at the doctor (Example 2.7). `press new` and `git init` are handed to Chapter 3. Example 2.2 no longer uses `cd ~/alice`. Example 2.6 says the repository is the one Chapter 3 creates.
- P3: applied (ruling 2).
- P4: applied (Example 2.3).
- P5: applied. *target* is now the object of its definition. The doctor is called a command. *scar*, *composite action*, *reusable workflow*, and *release contract* are each defined at first use.
- P6: applied.
- S1: applied. The font scan is set up in one sentence, told in the sidebar, and followed by one short paragraph.
- S2: applied.
- S3: applied. The licence paragraph, the Python restatement, and the Chrome sentence are cut.
- S4: applied. The tag paragraph points forward to the image digest.
- S5: applied. Example 2.7 shows the ready line and `echo $?` printing `0`. No `press all` output is invented.
- S6: applied. A gathered "not tested" paragraph ends the platforms A-head, with INSTALL.md's supported-platforms sentence before it.
- S7: applied.
- S8: applied (ruling 4; see the placeholder note above).
- S9: applied (Drifted 1).
- Table 2.2 suggestion (may): applied. The image row is moved out of the table, which now ends with the `press[tui]` row.

### Copyeditor (copy-02.md)

- Applied: 1, 2, 3, 4, 5, 6 (moot, paragraph cut), 7, 8, 9, 12 (block), 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25 (block, by ruling 7: "ship" appears only inside the quoted scar), 26, 27 (moot, sentence rewritten without provenance), 28, 29, 30, 32, 33, 34, 35, 36 (moot, procedure replaced), 37 (block), 38, 40, 42 (block), 43, 44, 45, 46, 47, 48, 49.
- 10: applied by citing INSTALL.md's own sentence.
- 11: applied (see fact Unsupported 5).
- 31 (should): declined. `docs/markup.md` sets a directory in italic (`*dist/*`), and the typesetter's item 9 agrees.
- 39 (should): superseded by ruling 1. The fact checker found the sidebar's description of the scan's behavior unsupported, so the sidebar now states only the file's facts and does not repeat the body.
- 41 (may): declined. "The remedy is patience" is cut along with its paragraph. The sidebar ends on the tea sentence.

### Typesetter (type-02.md)

- 1, 2, 3: applied (ruling 5).
- 4: applied. The separator rows give the first column about a third of the width (40/60 for Table 2.2).
- 5: applied (ruling 8).
- 6: superseded by ruling 8. Captured lines stay verbatim and wrap in the panel.
- 7: applied (ruling 4).
- 8: applied (Example 2.7).
- 9: applied. *requirements.txt*, *Dockerfile*, */usr/local/bin/epubcheck*, *scripts/dev-render.sh*, and *build.yml* are now italic.
- 10: applied.
- 11: applied. Each footnote definition follows the paragraph that cites it.

### Checker residuals after revision

`press check` reports nothing against the chapter text. The only failures are the placeholder-name issue above, plus other files. `ste_check` residuals: the three art directives and the fig-alt lines (length and semicolons, not prose). Line 35 is the footnote-marker join. Line 43 is a semicolon inside INSTALL.md's verbatim sentence. "harness" appears inside the dev-render header's verbatim quotation. "check out" is the Git verb. The index comment and the gerund headings are as before.

## Revision 2 (scoped re-review)

Word count: 5,257 (`press wordcount`).

1. N1: applied. Each of the three `art:` comments now sits on the line right after its image line, with its text unchanged. `press figures` now shows a description for all three.
2. O2: applied. The sentence now reads "seems to hang for several minutes".
3. O3: applied. *release contract* is now defined at its first use, in the "Which versions" paragraph. The later sentence uses the plain term.
4. N2: applied. A new paragraph after Example 2.1 says that Debian and Ubuntu ship `venv` in `python3-venv`. It says the package is missing from the press's list and that `python3 -m venv` fails without it. It then gives the book's own addition as a short `text` fence: `sudo apt-get install python3-venv`.
5. N3: applied.
   - Example 2.1's pip line is broken with a trailing backslash.
   - Example 2.4 lost its two `#` comments. The sentence before it now gives their content in prose, quoting "optional: the retail EPUB gate locally". The earlier note about narrowing the comment spacing is gone.
   - `tools/tag-fences.py` tagged all 8 fences `text`.
   - No fence line is longer than 64 columns.

Two other edits came out of the checks:

- `press check` newly flagged two lines in the dev-render paragraph:
  - "harness", inside the quoted header phrase, as assistant vocabulary. I paraphrased the phrase without quotation marks.
  - "quick look, and", which matches the `Look,` run-up pattern. It now reads "JPEG previews".
- The jargon lint listed two advisory findings, "settle" and "readiness". I reworded both.

`press check` now reports nothing for this chapter. Its exit status is 1 only because of the jargon findings in Chapters 1, 3, and 5. `ste_check` residuals are as in the previous revision: the art directives and the image lines, the footnote-marker join at line 35, verbatim quotations, and the index comment.

## Revision 3 (continuity)

Applied every item. (1) The composite action is now "the piece of the press that the reusable workflow runs to install it", and the reusable workflow's gloss is unchanged. (2) "The project" became "the press" in five places. (3) The three mays: "could not run", "inside the pinned toolchain image", and the operator's commands are now "commands", not targets. The italic definition of *toolchain image* moved to its first use in "What you need". `tools/space-art-comments.py` inserted 0 lines, because each `art:` comment already had one blank line after its image line. `press check` names nothing in this chapter. Its only failures are in `09-the-house-design.md`. Word count: 5,271.
