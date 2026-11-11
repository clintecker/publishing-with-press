# Continuity bible

Maintained by the continuity editor only. Chapters are numbered as in
`docs/design.md` section 5.

Chapters 1 and 3 have not had their own continuity pass. Entries that
cite them were cross-checked from Chapter 2's and Chapter 4's passes against
their current drafts and stay provisional until each chapter's own pass
confirms them. Chapter 4's pass is done (report continuity-04).

## Fixed cast

| Thing | Name |
|---|---|
| sample book | *Alice's Adventures in Wonderland*, slug `alice` |
| author at the keyboard | `alice` |
| workstation | `hatter` |
| CI host | `printshop` |
| repository owner | `wonderland-press` |
| press version | 3.0.2, always with "at the time of this writing" |
| scope of the sample book (ruling) | the book's sample `alice`, kept by `alice` on `hatter`, is the whole novel (twelve chapters; filenames such as *10-the-lobster-quadrille.md* belong to it). It is not press's gallery example. Ledger ruling "the two Alices"; Ch. 1 l.121; Ch. 4 l.18 conflates them (continuity-04, finding 2) |
| press's gallery example | `examples/alice-in-wonderland/` in the press repository, called "the press's own Alice example" or "the Alice example": three chapters (01 Down the rabbit-hole, 02 The pool of tears, 03 A caucus-race and a long tale) and one appendix (*z-about-this-edition.md*), 23 pages; `drop-cap` opening, `fairy-dust` scene break, a cascade and a verse block in chapter 2, a tail in chapter 3. Any capture from it is labeled as such. Ch. 1, 2, 4 |

## Terms defined (term, chapter of definition, the definition's gist)

A chapter may define a term again at its first use there (the vocabulary's
per-chapter italic rule), but the gist must agree with the row below.

| Term | Ch. | Gist |
|---|---|---|
| the toolchain | 1 (draft); 2 agrees | the outside programs press runs: pandoc, LuaLaTeX, latexmk, the fonts, epubcheck (with Java), poppler. Git and Python are not in it. |
| the toolchain image | 1 (draft); 2 agrees | `ghcr.io/clintecker/press-toolchain`, a public container image the press builds from its own *Dockerfile*; every CI build runs inside it |
| target | 1 (draft); 2 agrees | a `press` command that builds, checks, or verifies |
| scar | 1 (draft); 2 agrees | the press's word for a production failure turned into a guard |
| floating tag | 1 (draft); 2 agrees | a tag such as `v3` that names a major and moves to the newest compatible release within it |
| immutable tag | 1 (draft); 2 agrees | a three-part tag such as `v3.0.2` that names exactly one release forever |
| the release contract | 1 (draft); 2 agrees | the workflow that proves each press tag |
| the desk | 1 (draft); 2 agrees | `press desk`, press's full-screen console in the terminal |
| editable install | 2 | an install that points Python at the files in a clone, so a `git pull` changes the installed press with no reinstall |
| extras | 2 | pip's optional dependency groups; press has `tui` (Textual, for the desk) and `dev` (press development only) |
| the composite action | 2 | `action.yml`; installs press in CI from the action's own checkout, never pip from Git. See the Chapter 2 conflict under shared facts: it is reached through the reusable workflow, not named by a book's CI. |
| the operator | 2 | the commands such as `press improve` (also `research`, `aesthetic`) that hand work to an agent through `claude` |
| the reusable workflow | 2 | `build.yml`, the workflow file a book's CI calls; pins the composite action and the toolchain image |
| the checker | 1 (draft); 4 agrees; 6 | `press check`: reads every chapter file before anything builds and refuses a manuscript that breaks a rule. Four passes (vocabulary) |
| chapter file | 3; 4 agrees | a file in *book/chapters/* whose name matches `[0-9]*.md` (starts with a digit, ends in `.md`) |
| appendix file | 3; 4 agrees | a file in *book/appendices/* whose name matches `[a-z]-*.md` (one lowercase letter, a hyphen, the rest) |
| sentinel | 1 (draft); 3, 4, 6 agree | a phrase listed under `verify-sentinels` in *config/metadata.yaml* that must appear in the manuscript and in every edition; Ch. 4 l.204 says "in each finished edition" (narrower, not contradictory) |
| glyph law | 4 | the checker's list of characters allowed in book prose: tab, LF, CR; U+0020 to U+007E; U+00C0 to U+017F. Nothing else, including U+00A0 to U+00BF |
| jargon lint | 4 (Ch. 1 l.153 uses it, glossed with the watchlist) | the pass of the checker that looks for overused words from the watchlist; skips quotations and inline code |
| chapter opening | 4 | the treatment of the first letter of each chapter, set by `chapter-opening` in *config/metadata.yaml*. Usage: *drop cap* = the `drop-cap` style; *initial* = the large letter itself (continuity-04, finding 8) |
| lead | 4 | the quotation mark that opens a dialogue paragraph; press drops the letter after it and hangs the lead into the margin (reader site class `.drop-cap-lead`) |
| scene break | 4 | a pause inside a chapter, typed as `* * *`; drawn per `scene-break` in *config/aesthetic.yaml* by *scene-break.lua* |
| set piece | 4 | `cascade`, `verse`, `tail`: a fenced div around a line block that *set-pieces.lua* lays out; the words stay live text |
| tie | 4 | a non-breaking space that *typographic-spacing.lua* puts between a word and the word it must not leave at a line end (`~` in the PDF, U+00A0 elsewhere) |

## Shared facts (a fact two chapters both state)

| Fact | Value | Stated in |
|---|---|---|
| Python floor and tested range | `requires-python = ">=3.10"`; tested 3.10 through 3.14 (Ubuntu), plus 3.12 on macOS 15 | 1, 2 |
| Runtime dependencies | three: Pillow, pypdf, ruamel.yaml (ruamel.yaml is the one YAML library, YAML 1.2) | 2; due 14 (the hash lock pins the same three) |
| Install channel | pip from Git at a tag, `"press @ git+https://github.com/clintecker/press@v3"`; press is not on PyPI | 2, 3 |
| Editable install of a clone | `pip install -e <path>`; the scaffold's *requirements.txt* comment recommends it for day-to-day work | 1 (`pip install -e .` in a clone), 2, 3 |
| Toolchain members | pandoc, LuaLaTeX, latexmk, fonts, epubcheck (Java), poppler | 1, 2 |
| House PDF typeface | Libertinus, carried by TeX Live; Ubuntu has no `fonts-libertinus`, so the Dockerfile names `fonts-linuxlibertine` (the Libertine keyboard face) | 1 (footnote), 2. Ch. 1 body says "the Libertine fonts": see report continuity-02, finding 6 |
| Toolchain image identity | `ghcr.io/clintecker/press-toolchain`, public, `FROM ubuntu:24.04`, amd64 and arm64; anonymous pull locally, `GITHUB_TOKEN` in CI | 1, 2, 3 |
| Toolchain versions | none pinned by number; Ubuntu 24.04's pandoc and TeX Live, frozen by the image digest | 1, 2 |
| Image pin | the reusable workflow pins the image by `@sha256:` digest; `:latest` and `:sha-` tags are mutable; the release contract refuses a three-part tag whose workflow names only a `sha-` tag | 1, 2, 3; due 14 |
| epubcheck scar | Ubuntu's launcher needs binfmt_misc, which containers do not register: present, found by `which`, dies with "Exec format error"; the image ships a `java -jar` wrapper; the verifier reports a toolchain fault, not an EPUB fault | 1, 2; due 8 |
| Missing local epubcheck | softens the retail EPUB gate to a warning locally; CI (the image) always runs it | 1, 2, 3 |
| First-run font scan | the first LuaLaTeX run on a fresh machine scans fonts for several minutes; it looks like a hang and is not one | 1, 2 |
| How CI installs press | the composite action installs press from its own checkout at the action ref, never pip from Git; *requirements.txt* is for local builds only | 2, 3 |
| Who a book's CI calls | the scaffolded *book.yml* calls the reusable workflow at `v3`; the reusable workflow pins the composite action and the image, "so the book never names either one" (Ch. 3) | 3; Ch. 2 line 134 conflicts: see report continuity-02, finding 1 |
| `press all` and the print pack | `press all` does not build the print interior or cover wrap; `press print`, `verify-print`, `coverwrap` do | 1, 2, 3 |
| Doctor's ready line and status | `this machine can make books`, exit 0; otherwise `not ready: <tools>`, exit 1; a broken optional tool still makes the machine not ready | 2; due 15 (desk panel), App. C |
| Doctor's `BROKEN` test | present but fails both `--version` and `-v` within 15 s | 2; due App. A or C |
| `pdfimages` | not checked by the doctor; its absence softens two checks to notes | 2; due 8 |
| Release and tags in examples | current release 3.0.2 (with "at the time of this writing"); `v3` floating, `v3.0.2` immutable as the example pair | 1, 2, 3 |
| Code line width | at most 64 columns in every fenced block (the measure in the code face); excerpt long files with `...`, break long commands with `\`; terminal panel figures are drawn at 72 columns | ledger ruling; markup.md; 4 states it (l.255 tip) and obeys it. Ch. 1 l.134 and l.235 are 65: continuity-04 |
| Fence tag | every fence is tagged `text`: black, and a long line wraps with a hook. An untagged fence is plain verbatim and runs off the page; a language tag highlights in color and `press verify-print` refuses the interior with `print profile: colored ink on pages [N]` | ledger ruling (supersedes "untagged"); markup.md; 4 states it (l.231 to 238) and obeys it. design.md 5c still says "untagged": stale. Ch. 1 and 3 drafts untagged until `tools/tag-fences.py` runs at commit |
| Image, blank line, art comment | the `art:` comment follows the image line after exactly one blank line; a comment on the very next line makes pandoc set a paragraph, not a figure (no caption, no list entry); a comment above the image belongs to nothing | ledger correction; markup.md; 4 obeys (l.46, 99, 331, 351). Ch. 1 (4 places) and Ch. 3 (3 places) violate; Ch. 5 l.59 says the next line is allowed: continuity-04 |
| Paragraph law | a paragraph must be under 190 words; message `paragraph N has W words (the law is under 190; split it)`; a warning in an audit directory; enforced since press 1.7.0 | 1, 3, 4; due 6 |
| Glyph law ranges | tab, LF, CR; U+0020 to U+007E; U+00C0 to U+017F; message `glyph U+XXXX is outside the print-font set`; fenced code skipped | 1 ("print-font set"), 3 ("ASCII plus accented Latin letters"), 4; due 6 |
| Dash and quote law | no em dash, en dash, or curly quotes in prose; type straight quotes and let `+smart` curl them; `--` passes the checker but prints as a dash, so rewrite | 1, 3, 4 |
| Sentinel placement | never from the first words of a chapter: the drop cap splits the first word and small-caps the rest, so the PDF match fails | 1 (l.281), 3 (l.224), 4 (l.312), 8 (l.466) |
| Chapter-opening settings | `style` none, drop-cap, raised-cap (renders as drop-cap), ornate; `lines` 3; `small-caps-remainder` true; every shipped profile defaults to `none`; unnumbered chapters get none | 1 (house default no drop cap), 3, 4; due 9 |
| Ornate initial font | yinit, from `yfonts` in TeX Live's fonts-extra collection (`texlive-fonts-extra`); print only | 2 (l.208), 4 (l.309) |
| Discovery and sorting | lexical sort by filename; chapters, then appendixes, then the generated index; `press add` pads to at least two digits; appendixes count down from `z-`; the index takes the first free letter up from `a` | 3, 4 |
| `press add chapter` | lowercases the name and turns each run of non-letters-or-digits into one hyphen; keeps a title word for word as the heading; a slug-form name gets a sentence-case heading; refuses to overwrite, exit 1; `--front` makes *00-preface.md* with `# Preface {.unnumbered}` | 3, 4 |
| Pandoc dialect | `markdown+smart+yaml_metadata_block+fenced_divs+footnotes`, `standalone: true`, `number-sections: true`, in all six defaults files (pdf, epub, html, chunked, portable, print); `top-level-division: chapter` only in pdf, epub, print | 4, 7. Ch. 4 l.50 overstates the division: continuity-04, finding 5 |
| Lua filters (author's side) | typographic-spacing, set-pieces, chapter-dropcap, scene-break, figure-numbering; *portable.yaml* (plain text and DOCX) drops chapter-dropcap and scene-break, so those editions have no drop cap and a plain rule | 4, 7 |
| Running heads and folio | book title at the inner head, chapter title at the outer head; folio centred in the foot (`\cfoot`) on every page; a chapter's opening page (plain.scrheadings) has the folio and no running head | 9; Ch. 4 Figure 4.1 (l.44, 48) conflicts: continuity-04, finding 1 |
| Shell prompt | `$` on `hatter` and on `printshop`; `#` only for root | markup.md; 1 to 4 |

## Cross-references and promises (from, to, what is promised)

Status: kept (target delivers it), open (target not yet written), or
conflict.

| From | To | Promise |
|---|---|---|
| 1 (l.51) | 2 | covers both routes: the toolchain installed by hand and the toolchain image. Kept. |
| 1 (l.302) | 2 | puts the toolchain on `hatter`. Kept. |
| 3 (l.449) | 2 | covers installation in full, including the editable install of a clone. Kept (Example 2.2). |
| 3 (l.465) | 2 | supplies the toolchain a full build needs. Kept. |
| 2 (l.19) | 2, "The toolchain image" | describes the toolchain image "later". Kept (l.264). |
| 2 (l.77) | 2, "The toolchain image" | shows the immutability idea "one level down". Kept (digest, l.295). |
| 2 (l.134) | 14, *Continuous integration and the release contract* | covers the composite action in detail: self-checkout install, the action ref pin. Open (Ch. 14 is a stub; brief-14 A-head 3 "The composite action"). |
| 2 (l.165) | 15, *The operator's desk and the editorial machines* | describes the operator targets (`press improve`, research, aesthetic briefs). Open (brief-15 A-heads 7 and 9). |
| 2 (l.212) | 2, "The toolchain image" | explains Ubuntu's container-only epubcheck trap. Kept (l.282). |
| 2 (l.246) | 2, "The toolchain image" | tells the story of a program that exists and cannot run. Kept (l.282). |
| 2 (l.248) | 11, *The art department* | generating art, where the `OPENAI_API_KEY` and `GEMINI_API_KEY` keys matter (`press art commission`). Open (brief-11 A-head 10). |
| 2 (l.262) | 15 | the desk reads the doctor's typed findings and draws them as a panel. Open (facts-15 supports a doctor table; brief-15 does not name it: the Ch. 15 writer must show it). |
| 2 (l.299) | 3 | creates the book repository at *~/alice*. Kept. |
| 2 (l.315) | 14 | **shows where to find the toolchain image digest**: the `image:` line of the press's *build.yml* (the reusable workflow) at the pinned tag, the value to put in place of `:latest` in Example 2.6 for a CI-exact local build, together with the matching three-part press tag. Open (Ch. 14 is a stub). Note for Ch. 14: facts-14 item 341 says the digest is not in the release notes but in the build.yml pin and the release receipt; do not send the reader to the CHANGELOG. |
| 2 (l.361) | 3, *The shape of a book repository* | makes a book. Kept. |
| 2 (l.381) | 8, *Verifying the artifacts* | explains how to read a failure. Kept in draft (design A-topic "reading a failure"). |
| 2 (l.381) | 7, *Building the editions* | explains what `press all` builds; print interior and cover wrap are separate targets. Kept in draft. |
| 2 (l.389) | 3 | creates the `alice` book with `press new` and describes every file it makes. Kept. |
| 2 (l.140) | Figure 2.1 `@fig:tools-in-the-build` | where each tool sits in the build. Figure present (l.142). |
| 2 (l.224, 256) | Figure 2.2 `@fig:doctor-report` | the doctor report on `hatter`, with `epubcheck` absent and `claude` BROKEN. Figure present (l.226). |
| 2 (l.317) | Figure 2.3 `@fig:local-versus-container` | workstation versus toolchain image. Figure present (l.319). |
| 4 (l.30) | 3 | *config/metadata.yaml* holds the book's metadata. Kept. |
| 4 (l.31, 198) | 4, "The set pieces" | the set pieces use fenced divs and take a line block. Kept (l.345). |
| 4 (l.44) | 9, *The house design* | describes the running head and the folio. Kept in draft (Ch. 9 l.120 to 126). |
| 4 (l.44) | 5 | covers the figure. Kept in draft. |
| 4 (l.66) | 10, *Front matter, the index, and the table of authorities* | covers the generated subject index. Open (Ch. 10 draft). |
| 4 (l.70) | 4, "Chapter openings and drop caps" | unnumbered chapters get no drop cap. Kept (l.291). |
| 4 (l.97) | 5, *Figures, plates, and illustrations* | covers figure identifiers in full. Kept in draft. |
| 4 (l.132, 187) | 10 | the copyright line belongs to the generated front matter; the book's epigraph from `epigraph.quote` and `epigraph.attribution`. Open (Ch. 10 draft). |
| 4 (l.155) | 6, *Checking the manuscript* | covers `audit-dirs` and `banned-patterns`. Kept in draft. |
| 4 (l.163) | 4, "Tables" | covers tables. Kept (l.206). |
| 4 (l.185) | 6 | describes the jargon lint and its watchlist. Kept in draft. |
| 4 (l.204) | 10; 6; 8, *Verifying the artifacts* | 10 covers the index and authorities; 6 "introduces" sentinels (wrong verb: Ch. 1 and 3 introduce them; continuity-04, finding 4); 8 proves them in the finished editions. Kept in draft. |
| 4 (l.235) | 12, *The print pack* | describes the print pack build and `verify-print`. Open (Ch. 12 is a stub). |
| 4 (l.433) | 5 | takes up plates, numbered figures, and placements. Kept in draft. |
| 3 (l.605); 7 (l.109, 131); 8 (l.466); 9 (l.114) | 4 | the chapter files; chapter openings, scene breaks, set pieces from the author's side; the drop cap splitting the first word; how a book chooses its chapter opening. All kept. |
| 4 (l.44, 329, 349) | Figures 4.1 `@fig:page-anatomy`, 4.2 `@fig:scene-break-ornaments`, 4.3 `@fig:set-pieces` | page anatomy; the three ornaments in PDF and reader site; the three set pieces. All present (l.46, 331, 351). |

## Numbering check (per chapter: figures, tables, examples)

| Ch. | Figures | Tables | Examples |
|---|---|---|---|
| 2 | 2.1 `02-01-tools-in-the-build`, 2.2 `02-02-doctor-report`, 2.3 `02-03-local-versus-container`: no gap, no repeat, slugs match `CC-NN-slug`, every `@fig:` has its figure. Order follows dev ruling 4 (reading order) and reverses design.md section 5 and brief-02, which still list the doctor report as 2.1. PNGs 02-01 and 02-02 not yet drawn. | 2.1 to 2.4, no gap | 2.1 to 2.7, no gap (the `python3-venv` command at l.69 is an unnumbered display) |
| 4 | 4.1 `04-01-page-anatomy`, 4.2 `04-02-scene-break-ornaments`, 4.3 `04-03-set-pieces`: no gap, no repeat, slugs match, every `@fig:` has its figure, each cited before it appears. Reading order swaps design.md's 4.2 and 4.3 (update design.md). One plate, *the-compositor-at-the-frame.png*, unnumbered. PNGs 04-01 to 04-03 not yet drawn | 4.1 to 4.4, no gap | 4.1 to 4.9, no gap; six short uncaptioned fences (l.60, 175, 189, 247, 274, 299), none referred to again |
