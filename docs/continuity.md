# Continuity bible

Maintained by the continuity editor only. Chapters are numbered as in
`docs/design.md` section 5.

Chapter 3's pass is done (report continuity-03): every entry citing it is
confirmed or corrected, and Chapter 3 is the defining chapter for the sample
book's config (sentinels, page floor, metadata values). Chapter 1's pass is done (report continuity-01): its
entries are confirmed, with line numbers to the 315-line text. Chapter 4's pass is done (report continuity-04). Chapter 8's pass is done (report continuity-08).

## Fixed cast

| Thing | Name |
|---|---|
| sample book | *Alice's Adventures in Wonderland*, slug `alice` |
| author at the keyboard | `alice` |
| workstation | `hatter` |
| CI host | `printshop` |
| repository owner | `wonderland-press` |
| press version | 3.0.2, always with "at the time of this writing" |
| scope of the sample book (ruling) | the book's sample `alice`, kept by `alice` on `hatter`, is the whole novel (twelve chapters; filenames such as *10-the-lobster-quadrille.md* belong to it). It is not press's gallery example. Ledger ruling "the two Alices"; Ch. 1 l.124 (confirmed, continuity-01); Ch. 4 l.18 conflates them (continuity-04, finding 2) |
| press's gallery example | `examples/alice-in-wonderland/` in the press repository, called "the press's own Alice example" or "the Alice example": three chapters (01 Down the rabbit-hole, 02 The pool of tears, 03 A caucus-race and a long tale) and one appendix (*z-about-this-edition.md*), 23 pages; `drop-cap` opening, `fairy-dust` scene break, a cascade and a verse block in chapter 2, a tail in chapter 3. Any capture from it is labeled as such. Ch. 1 (labeled at l.170, 208, 277), 2, 4 |

## Terms defined (term, chapter of definition, the definition's gist)

A chapter may define a term again at its first use there (the vocabulary's
per-chapter italic rule), but the gist must agree with the row below.

| Term | Ch. | Gist |
|---|---|---|
| the toolchain | 1 (confirmed); 2 agrees | the outside programs press runs: pandoc, LuaLaTeX, latexmk, the fonts, epubcheck (with Java), poppler. Git and Python are not in it. |
| the toolchain image | 1 (confirmed); 2 agrees | `ghcr.io/clintecker/press-toolchain`, a public container image the press builds from its own *Dockerfile*; every CI build runs inside it |
| target | 1 (confirmed); 2 agrees | a `press` command that builds, checks, or verifies. Not the operator commands (Ch. 2). Ch. 11 l.255 calls the `--as` value of `press art accept` a *target*: conflict, continuity-01 |
| scar | 1 (confirmed); 2 agrees | the press's word for a production failure turned into a guard |
| floating tag | 1 (confirmed); 2 agrees | a tag such as `v3` that names a major and moves to the newest compatible release within it |
| immutable tag | 1 (confirmed); 2 agrees | a three-part tag such as `v3.0.2` that names exactly one release forever |
| the release contract | 1 (confirmed); 2 agrees | the workflow that proves each press tag |
| the desk | 1 (confirmed); 2 agrees | `press desk`, press's full-screen console in the terminal |
| editable install | 2 | an install that points Python at the files in a clone, so a `git pull` changes the installed press with no reinstall |
| extras | 2 | pip's optional dependency groups; press has `tui` (Textual, for the desk) and `dev` (press development only) |
| the composite action | 2 | `action.yml`; installs press in CI from the action's own checkout, never pip from Git. See the Chapter 2 conflict under shared facts: it is reached through the reusable workflow, not named by a book's CI. |
| the operator | 2 | the commands such as `press improve` (also `research`, `aesthetic`) that hand work to an agent through `claude` |
| the reusable workflow | 2 | `build.yml`, the workflow file a book's CI calls; pins the composite action and the toolchain image |
| the checker | 1 (confirmed, l.36); 4 agrees; 6 | `press check`: reads every chapter file before anything builds and refuses a manuscript that breaks a rule. Four passes (vocabulary) |
| chapter file | 3 (confirmed, l.378); 4 agrees | a file in *book/chapters/* whose name matches `[0-9]*.md` (starts with a digit, ends in `.md`) |
| appendix file | 3 (confirmed, l.378); 4 agrees | a file in *book/appendices/* whose name matches `[a-z]-*.md` (one lowercase letter, a hyphen, the rest) |
| sentinel | 1 (confirmed, l.283; says "in the source", read the manuscript: continuity-01, finding 2); 3 (confirmed, l.220), 4, 6, 8 agree | a phrase listed under `verify-sentinels` in *config/metadata.yaml* that must appear in the manuscript and in every edition; Ch. 4 l.204 says "in each finished edition" (narrower, not contradictory) |
| glyph law | 4 | the checker's list of characters allowed in book prose: tab, LF, CR; U+0020 to U+007E; U+00C0 to U+017F. Nothing else, including U+00A0 to U+00BF |
| jargon lint | 4 (Ch. 1 l.156 uses it, glossed with the watchlist) | the pass of the checker that looks for overused words from the watchlist; skips quotations and inline code |
| chapter opening | 4 | the treatment of the first letter of each chapter, set by `chapter-opening` in *config/metadata.yaml*. Usage: *drop cap* = the `drop-cap` style; *initial* = the large letter itself (continuity-04, finding 8) |
| lead | 4 | the quotation mark that opens a dialogue paragraph; press drops the letter after it and hangs the lead into the margin (reader site class `.drop-cap-lead`) |
| scene break | 4 | a pause inside a chapter, typed as `* * *`; drawn per `scene-break` in *config/aesthetic.yaml* by *scene-break.lua* |
| set piece | 4 | `cascade`, `verse`, `tail`: a fenced div around a line block that *set-pieces.lua* lays out; the words stay live text |
| tie | 4 | a non-breaking space that *typographic-spacing.lua* puts between a word and the word it must not leave at a line end (`~` in the PDF, U+00A0 elsewhere) |
| edition | 1; 7 agrees | one published form of the book (print-ready PDF, EPUB, Web site, and the rest); press names eight (see shared facts) |
| book repository | 1; 3 agrees (confirmed, l.17) | a directory that holds *config/metadata.yaml* and the manuscript under *book/* |
| the manuscript | 1; 3, 4 agree | the chapter files and appendix files under *book/* |
| design profile | 1; 9, 12 agree | one of six trims, each with its own interior geometry; 9 and 12 add "sealed" |
| Lua filter | 1; 4, 7 use it | a small script in Lua that pandoc runs over the document between reading and writing it |
| verifier | 1; 8 agrees | the check that opens a finished artifact and inspects it as an object (8: a `verify_*` module and the check it runs) |
| artifact | 1; 3, 7 agree | a file or directory in *dist/* that the press names and tracks (the registry names it) |
| the house | 1; 9 agrees | press's default design and law: the TeX header, the reader stylesheet, the checker's rules; a book changes it through its own config, never by editing press. Ch. 9 gives the design half |
| the registry | 1; 7 agrees | the artifact graph: the part of press that names every artifact and records what each depends on (7: the table in *registry.py*) |
| generator | 1 | machinery that makes the right thing; ranked above a checker and a convention by the second law |
| the watchlist | 1; 6 | the press's list of overused words, read by the jargon lint |
| known-bad fixture | 1; 6 agrees | a file that every check must reject; press carries 19 |
| plate | 1; 5 agrees | an unnumbered illustration in the List of Plates |
| the print pack | 1; 12 agrees | the set of artifacts a printer needs: print-profile interior, cover wrap, retail channel checklists |
| cover wrap | 1; 12 agrees | the whole cover, back to front, as one PDF, with computed spine and EAN-13 |
| finisher | 1 | planned supplied-interior source mode (`interior: path/to/interior.pdf`); on the Book breadth milestone; not in 3.0.2 |
| slug | 3 | the directory name given to `press new`, the basename of every artifact; must match `[a-z0-9][a-z0-9-]*` |
| book root | 3 | the directory a target works in: `BOOK_ROOT` if set, else the current directory; must hold *config/metadata.yaml* ("is not a book" otherwise); no upward search. Ch. 7 l.150 (press sets `BOOK_ROOT` for its subprocesses) is compatible |
| book model | 3; due 16 | the press's typed set of rules for every config field: kind, required or not, default; every build and every `press config set` checks against it. Ch. 6 l.388 and Ch. 10 l.101 say "the typed model": continuity-03, finding 4 |
| page floor | 6, 8 (Ch. 3 l.228 uses it undefined: continuity-03, finding 6) | `verify-min-pages`, the fewest pages the PDF verifier accepts |
| release witnesses | 3; 6 agrees | what a release build demands under `PRESS_RELEASE=1`: at least two sentinels and a page floor of at least 24. Ch. 6 l.392 gives the name to the two settings themselves (compatible) |
| vacuous witnesses | 3; 6, 8 (l.82 cites Ch. 3) | press's phrase, in its release refusal, for draft knobs too weak to prove anything (empty sentinel list, one-page floor) |
| writable / immutable / structured / file field | 3 | the four kinds of config field in `press config`: takes set and unset / refuses writes and says what to change (`trim`) / too rich for one command line (index terms, authorities, qualification records) / a whole file (*tex/title-page.tex*, assets). "immutable" here is not the immutable tag |
| invariant | 7 (l.341); 8 (l.91) agrees | a named `INV-` entry in the press's ledger of properties it enforces. Ch. 8 names `INV-pdf-detector`, `INV-format-witness`, `INV-archive-source-policy`, `INV-graph-no-stale` (all critical) and `INV-archive-site-bytes` |
| witness (the class) | 8 (l.400, Table 8.6) | any evidence a verifier requires: sentinels, title, manuscript witness, chapter witnesses, page floor; press's own line says "2 sentinel(s) plus the title as witnesses". `docs/vocabulary.md` is narrower (the lines only): continuity-08, finding 5 |
| manuscript witness | 8 (l.218) | the longest markup-free line of 40 or more characters in the whole manuscript (free of fifteen characters: asterisk, underscore, backtick, square brackets, parentheses, angle brackets, both quotes, ampersand, hash, bang, vertical bar; Ch. 8 l.221); press chooses it; every edition but the PDF must carry it |
| chapter witness | 8 (l.272) | the same rule applied to one chapter file; must appear on exactly one reader-site page and in every edition (the agreement check) |
| float | 8 (sidebar l.133) | LaTeX's word for a block it may move to a better spot on the page (not a placement; vocabulary's "float" ban is for placement) |
| commerce | 8 (l.382) | the optional ordering of printed copies from the book's site; Ch. 3, 7, 12 call the feature "print ordering" and keep "commerce" for the gate: continuity-08, finding 7 |

## Shared facts (a fact two chapters both state)

| Fact | Value | Stated in |
|---|---|---|
| Python floor and tested range | `requires-python = ">=3.10"`; tested 3.10 through 3.14 (Ubuntu), plus 3.12 on macOS 15 | 1 (floor only, l.48), 2 |
| Runtime dependencies | three: Pillow, pypdf, ruamel.yaml (ruamel.yaml is the one YAML library, YAML 1.2) | 2; due 14 (the hash lock pins the same three) |
| Install channel | pip from Git at a tag, `"press @ git+https://github.com/clintecker/press@v3"`; press is not on PyPI | 2, 3 |
| Editable install of a clone | `pip install -e <path>`; the scaffold's *requirements.txt* comment recommends it for day-to-day work | 1 (`pip install -e .` in a clone), 2, 3 |
| Toolchain members | pandoc, LuaLaTeX, latexmk, fonts, epubcheck (Java), poppler | 1, 2 |
| House PDF typeface | Libertinus, carried by TeX Live; Ubuntu has no `fonts-libertinus`, so the Dockerfile names `fonts-linuxlibertine` (the Libertine keyboard face) | 1 (footnote), 2. Ch. 1 body (l.48) still says "the Libertine fonts" after its own pass: continuity-02 finding 6, continuity-01 finding 3 (may) |
| Toolchain image identity | `ghcr.io/clintecker/press-toolchain`, public, `FROM ubuntu:24.04`, amd64 and arm64; anonymous pull locally, `GITHUB_TOKEN` in CI | 1, 2, 3 |
| Toolchain versions | none pinned by number; Ubuntu 24.04's pandoc and TeX Live, frozen by the image digest | 1, 2 |
| Image pin | the reusable workflow pins the image by `@sha256:` digest; `:latest` and `:sha-` tags are mutable; the release contract refuses a three-part tag whose workflow names only a `sha-` tag | 1, 2, 3; due 14 |
| epubcheck scar | Ubuntu's launcher needs binfmt_misc, which containers do not register: present, found by `which`, dies with "Exec format error"; the image ships a `java -jar` wrapper; the verifier reports a toolchain fault, not an EPUB fault | 1, 2; due 8 |
| Missing local epubcheck | softens the retail EPUB gate to a warning locally; CI (the image) always runs it | 1, 2, 3 |
| First-run font scan | the first LuaLaTeX run on a fresh machine scans fonts for several minutes; it looks like a hang and is not one | 1, 2, 3 (l.537) |
| How CI installs press | the composite action installs press from its own checkout at the action ref, never pip from Git; *requirements.txt* is for local builds only | 2, 3 |
| Who a book's CI calls | the scaffolded *book.yml* calls the reusable workflow at `v3`; the reusable workflow pins the composite action and the image, "so the book never names either one" (Ch. 3) | 3; Ch. 1 l.236 agrees in substance but names it "the press's own build workflow" (continuity-01, finding 1, should); Ch. 2 line 134 conflicts: see report continuity-02, finding 1 |
| `press all` and the print pack | `press all` does not build the print interior or cover wrap; `press print`, `verify-print`, `coverwrap` do | 1, 2, 3 |
| Doctor's ready line and status | `this machine can make books`, exit 0; otherwise `not ready: <tools>`, exit 1; a broken optional tool still makes the machine not ready | 2; due 15 (desk panel), App. C |
| Doctor's `BROKEN` test | present but fails both `--version` and `-v` within 15 s | 2; due App. A or C |
| `pdfimages` | not checked by the doctor; its absence softens two checks to notes | 2; due 8 |
| Release and tags in examples | current release 3.0.2 (with "at the time of this writing"); `v3` floating, `v3.0.2` immutable as the example pair | 1, 2, 3 |
| Code line width | at most 64 columns in every fenced block (the measure in the code face); excerpt long files with `...`, break long commands with `\`; terminal panel figures are drawn at 72 columns | ledger ruling; markup.md; 4 states it (l.255 tip) and obeys it. Ch. 1 now obeys (confirmed, continuity-01); Ch. 3 obeys (confirmed, continuity-03) |
| Fence tag | every fence is tagged `text`: black, and a long line wraps with a hook. An untagged fence is plain verbatim and runs off the page; a language tag highlights in color and `press verify-print` refuses the interior with `print profile: colored ink on pages [N]` | ledger ruling (supersedes "untagged"); markup.md; 4 states it (l.231 to 238) and obeys it. design.md 5c still says "untagged": stale. Ch. 1 now tagged throughout (confirmed, continuity-01); Ch. 3 now tagged throughout, 17 fences (confirmed, continuity-03) |
| Image, blank line, art comment | the `art:` comment follows the image line after exactly one blank line; a comment on the very next line makes pandoc set a paragraph, not a figure (no caption, no list entry); a comment above the image belongs to nothing | ledger correction; markup.md; 4 obeys (l.46, 99, 331, 351). Ch. 1 now obeys in all four places (confirmed, continuity-01); Ch. 3 now obeys in all three places (l.76 to 78, 394 to 396, 609 to 611; confirmed, continuity-03); Ch. 5 l.59 says the next line is allowed: continuity-04 |
| Paragraph law | a paragraph must be under 190 words; message `paragraph N has W words (the law is under 190; split it)`; a warning in an audit directory; enforced since press 1.7.0 | 1, 3, 4; due 6 |
| Glyph law ranges | tab, LF, CR; U+0020 to U+007E; U+00C0 to U+017F; message `glyph U+XXXX is outside the print-font set`; fenced code skipped | 1 ("print-font set"), 3 ("ASCII plus accented Latin letters"), 4; due 6 |
| Dash and quote law | no em dash, en dash, or curly quotes in prose; type straight quotes and let `+smart` curl them; `--` passes the checker but prints as a dash, so rewrite | 1, 3, 4 |
| Sentinel placement | never from the first words of a chapter: the drop cap splits the first word and small-caps the rest, so the PDF match fails | 1 (l.286), 3 (l.225, confirmed), 4 (l.312), 8 (l.466) |
| Chapter-opening settings | `style` none, drop-cap, raised-cap (renders as drop-cap), ornate; `lines` 3; `small-caps-remainder` true; every shipped profile defaults to `none`; unnumbered chapters get none | 1 (house default no drop cap), 3, 4; due 9 |
| Ornate initial font | yinit, from `yfonts` in TeX Live's fonts-extra collection (`texlive-fonts-extra`); print only | 2 (l.208), 4 (l.309) |
| Discovery and sorting | lexical sort by filename; chapters, then appendixes, then the generated index; `press add` pads to at least two digits; appendixes count down from `z-`; the index takes the first free letter up from `a` | 3, 4 |
| `press add chapter` | lowercases the name and turns each run of non-letters-or-digits into one hyphen; keeps a title word for word as the heading; a slug-form name gets a sentence-case heading; refuses to overwrite, exit 1; `--front` makes *00-preface.md* with `# Preface {.unnumbered}` | 3, 4 |
| Pandoc dialect | `markdown+smart+yaml_metadata_block+fenced_divs+footnotes`, `standalone: true`, `number-sections: true`, in all six defaults files (pdf, epub, html, chunked, portable, print); `top-level-division: chapter` only in pdf, epub, print | 4, 7. Ch. 4 l.50 overstates the division: continuity-04, finding 5 |
| Lua filters (author's side) | typographic-spacing, set-pieces, chapter-dropcap, scene-break, figure-numbering; *portable.yaml* (plain text and DOCX) drops chapter-dropcap and scene-break, so those editions have no drop cap and a plain rule | 4, 7 |
| Running heads and folio | book title at the inner head, chapter title at the outer head; folio centred in the foot (`\cfoot`) on every page; a chapter's opening page (plain.scrheadings) has the folio and no running head | 9; Ch. 4 Figure 4.1 (l.44, 48) conflicts: continuity-04, finding 1 |
| Shell prompt | `$` on `hatter` and on `printshop`; `#` only for root | markup.md; 1 to 4 |
| Sample book's sentinels | `"Twinkle, twinkle, little bat"` and `"she made some tarts"`: two lines of verse from the middles of Carroll's chapters VII and XI, set with `press config set verify-sentinels '[...]' --json` once both are in the manuscript | 3 (l.222, 243), 8 (l.109 to 111, Figure 8.3). **Ch. 6 Example 6.10 (l.365 to 372) conflicts** ("We're all mad here.", "Why is a raven like a writing-desk?"): continuity-03, finding 1 |
| Release witnesses and refusal | CI sets `PRESS_RELEASE=1` on a tag whose name starts with `v`; then at least 2 sentinels and a floor of at least 24, else `this is a release build (PRESS_RELEASE=1) and its witnesses are vacuous:` / `verify-sentinels has N entries; a release needs at least 2 distinctive prose fragments` / `verify-min-pages is N; a release needs at least 24` | 1, 3 (Example 3.3), 6 (Example 6.11, l.404), 8 (l.63, 82); due 14 |
| Sentinel matching | exact case; curly and straight quotes equal; the PDF text has whitespace folded; the title is matched case-folded | 3 (l.220), 6 (l.365), 8 (l.106, 114) |
| Scaffold metadata values | `press new alice --author "Lewis Carroll" --owner wonderland-press`: `title: "alice"`, `subtitle: "A subtitle"`, `author: ["Lewis Carroll"]` (else `git config user.name`, else "The Author"), `date: "First edition, 2026"`, `lang: en-US`, `copyright: "Copyright 2026."`, `publisher` = the author, `publisher-place: "Earth"`, placeholder description, `keywords: [writing]`; `repository`/`site-url` live only with `--owner` (else commented, `OWNER`); `verify-sentinels: []`, `verify-min-pages: 1`; *config/front-matter.yaml* written, all keys commented, so front matter is on | 3 (Table 3.1, Example 3.2); 10 (l.126, scaffold fills the five front-matter keys) agrees |
| Sample book's identity after setup | `title: "Alice's Adventures in Wonderland"`; `author: ["Lewis Carroll"]`; `description: "A girl follows a rabbit underground and argues with all."`; `keywords: ["fantasy", "children"]`; `print.paper: white`; `repository: https://github.com/wonderland-press/alice`; `site-url: https://wonderland-press.github.io/alice`. Later, Ch. 10: `copyright: "Copyright 2026 Wonderland Press"`, `publisher: "Wonderland Press"`, `publisher-place: "Oxford"`, subtitle `"A Tale for Children; or, Alice's Adventures Under Ground"` (Ch. 3 sets a subtitle and unsets it, Example 3.4) | 3 (Examples 3.1, 3.4, 3.5), 10 (Example 10.2, l.166). **Ch. 1 Example 1.1 l.137 conflicts** (description "A girl falls into Wonderland."): continuity-03, finding 3. Ch. 12 l.111, 218 ("Alice example", 200 pages, cream): finding 10 |
| Required metadata keys | the model needs `title`, `author`, `slug`; with *config/front-matter.yaml* also `copyright`, `publisher`, `publisher-place`; the checker also refuses a book without `description` (`metadata missing <key>:`) | 3 (Table 3.3, l.200), 6 (l.56), 10 (l.126) |
| Year from the date | the press takes the first four-digit year (beginning 1 or 2) from the free-text `date` for the EPUB date (written to *build/epub-metadata.xml*, because pandoc's empty `dc:date` fails epubcheck RSC-005) and for the title page's roman numerals (2026 = mmxxvi) | 3 (l.187, 198, footnote), 7 (l.236), 8 (l.260), 10 (l.156) |
| Print and opening defaults | `print.profile` `house-6x9`, `print.provider` `house`, `print.binding` `perfect-bound`, `print.material` `paperback`, `print.paper` model default `cream` (template choices `white`, `cream`), `page-thickness` overrides paper; `trim` derived from the profile and refused as a direct write; house `chapter-opening.style` `none`, `lines` 3 | 3 (Table 3.5, l.268), 8 (l.82, 6 by 9), 9, 12 |
| `press new` behaviour | refuses an existing path; checks the slug before copying; copies the template, renames `dot-` files, stamps the four workflows into *.claude/workflows/* (`// scaffolded by press 3.0.2; ...`), substitutes slug, author, publisher, place, repository, site-url; does not run `git init` | 1 (l.142), 3 (l.53 to 70, 100) |
| GitHub Pages and the first CI run | set Pages Source to GitHub Actions once per book repository; a run that dies at "Initialize containers" is rerun; the image is public and needs no secret | 1 (l.244, 252), 3 (l.597, 601) |
| Scaffolded *book.yml* | triggers: push to any branch, tags `v*`, pull requests, `workflow_dispatch`; permissions `contents: write`, `packages: read`, `pages: write`, `id-token: write`; one job, `uses: clintecker/press/.github/workflows/build.yml@v3` | 3 (Example 3.12); due 14 |
| Scaffolded Makefile | `PRESS ?= python3 -m press`; 16 `.PHONY` targets (`all check pdf epub html markdown site txt docx pages source verify verify-formats render wordcount clean`), each `$(PRESS) $@` | 3 (Example 3.8, l.467) |
| The editions | eight: Print (`alice.pdf`), Circulating (`alice.epub`), Single-leaf (`alice.html`), Chapter (`site/` and `alice-site.zip`), Manuscript (`alice.md`, stitched, no pandoc), Telegraphic (`alice.txt`, 80 columns), Office (`alice.docx`), Source (`alice-source.zip`, files Git tracks) | 1 (Table 1.2), 3 (l.615), 7. Ch. 10 l.317 "seven editions at once" conflicts: continuity-01 |
| The agreement count | `7 editions match source` (`press all`), `7 editions agree on all 4 chapter witnesses` (verify): the six editions the `Verified` line names plus the PDF when `pdftotext` is present; not the number of editions | 1 (Table 1.1), 7 (l.403), 8 (l.294, 427) |
| Name of *alice-sources.md* | "the table of authorities" in 1 (l.277), 3 (l.617), 9 (l.246); "the sources companion" in 8 (l.327), 10 (l.401), where the table of authorities is the ledger. Ruling needed: continuity-01, finding 7 recommends ledger = table of authorities, file = sources companion | 1, 3, 8, 9, 10 |
| Image height cap | the TeX header caps every included image; per profile; 6.3 inches on the house 6 by 9 | 1 (l.84), 5, 8, 9, 10 |
| Number of design profiles | six | 1 (l.32), 9, 12 |
| Universal known-bad fixtures | 19 in the press; the count rises by one per file in *tests/known-bad/* | 1 (l.158), 3 (l.508, 535; confirmed: runs in `press check` and `press all`, not a bare `press pdf`), 6 (l.118), 7 (l.383) |
| `verify-min-pages` and release witnesses | model default 40; the scaffold writes 1; a release build (`PRESS_RELEASE=1`) needs at least 2 sentinels and a floor of at least 24 | 1 (l.283), 3 (Table 3.4, l.228 to 246, Example 3.3; confirmed), 6 (l.373 to 404), 8 (l.63, 82, 206): agree. The sample book sets 24 once its chapters exist (3, 6, 8) |
| `description` required | the checker refuses a book without a description | 1 (l.142), 3 (l.192, confirmed), 6 (l.56) |
| `press wordcount` | strips fenced and inline code; counts HTML comments; fresh scaffold: 42 words in *00-preface.md* | 1 (l.160 to 165), 3 (l.541 to 549, confirmed; pattern `\b[\w'-]+\b`), 7 (l.496) |
| *build/* and `press clean` | *build/* holds rendered defaults, the generated index, front matter as TeX, the jargon report, `press render` page images at 160 dpi; `press clean` deletes *build/* and *dist/* | 1 (l.281), 3 (l.605, 635 to 637, confirmed), 7 (l.492) |
| The Pages bundle | *dist/pages/*: landing page, *read/* copy of the reader, *downloads/* linking every download exactly once; *sitemap.xml* and *robots.txt* only with `site-url`; `press pages` rebuilds it alone | 1 (l.228, 275), 3 (l.621, confirmed), 7, 8 |
| Print pack artifacts | `press print`, `press verify-print`, `press coverwrap` add *alice-interior.pdf* and *alice-coverwrap.pdf* | 1 (l.279), 3 (l.625, confirmed), 12 |
| `press all` sequence | checker, every edition, source archive, Pages bundle, verifiers, then the commerce gate (advisory unless `PRESS_RELEASE` and only when print ordering is on) | 1 (l.170), 7, 8 |
| Checker passes, in order | source checks, checker self-test, style audit (`Editorial checks`), jargon lint | 1 (l.146 to 158), 6, 7 |
| Cross-references | press numbers and cites figures only; chapter, section, table, and example references are typed by hand (a convention) | 1 (l.116, 305), 5 (l.118); due Preface |
| Press history dates | first commit 2026-07-17; repository public since 2026-07-19 (per ROADMAP); 2.0.0 2026-07-21 ("composable press"); 3.0.0 2026-11-10 (design major); 3.0.2 2026-11-11 | 1 (l.60 to 66, 291); due Preface ("where press came from") |
| Earlier books | *Mostly Done.* (extracted from); *Make Ready* (taken end to end: clothbound cover, fourteen plates, index, ISBNs, authorities); neither in the press repository | 1 (l.60, 64); due Preface |
| Example conventions | `$` then what you type; a line of only `...` is elided output; the cast as fixed above | 1 (l.305), markup.md; due Preface |
| The no-stale law | `INV-graph-no-stale`, critical; every verify target builds what it verifies before verifying it; CLI path only (importing a verifier module skips the rebuild); one exception: `press verify-formats` reads whatever *dist/alice.pdf* exists into the agreement check without rebuilding it, when `pdftotext` is present (source: `verify_formats.py` l.274); `book_inputs()` deletes *build/generated/* before every pandoc build | 6 (l.473), 8 (l.431 to 451, Figure 8.2): agree. **7 (l.339) states it with no exception: conflict, continuity-08, finding 3** |
| What each verify target builds | `press verify`: pdf, then `verify_pdf`. `press verify-formats`: epub, html, markdown, txt, docx, site, source, then `verify_formats`, `verify_archives`. `press pages` (alias `press verify-pages`): the nine prerequisites pdf, epub, html, markdown, txt, docx, site, source, sources, then pages and `verify_pages`. `press verify-print`: print, `verify_pdf --profile print`, then coverwrap and `verify_coverwrap` only with *assets/cover.jpg*, else `no assets/cover.jpg; interior verified, wrap not built`. `press coverwrap`: print, coverwrap, `verify_coverwrap` | 6 (l.36, `press verify` without the checker), 7 (l.349 to 357), 8 (l.59, 160, 177, 210, 363, Figure 8.2), 12 (l.178): agree |
| `press all` verifier order | `verify_pages`, `verify_pdf`, `verify_formats`, `verify_archives` | 7 (l.377 art, l.418), 8 (l.445) |
| Per-edition witnesses | every edition carries the title, every sentinel, and the manuscript witness (`INV-format-witness`, critical); the PDF carries title and sentinels, not the manuscript witness; the `Verified` line prints the witness lowercased, cut at 40 characters | 8 (l.216 to 230, 287 to 294, Table 8.6); due App. C |
| Sentinel matching and places | exact case; straight and curly quotes equal; the title is case-folded in the PDF; a sentinel is checked in the manuscript (checker), the PDF, every edition, and the public reading site | 6 (l.361, 365), 8 (l.106, 114, 376, Table 8.6): agree |
| Agreement windows | the chapter witness cut into windows of eight consecutive words, a new window every four words; any one window present passes | 8 (l.418, footnote); due App. C |
| Source zip policy | Git-tracked files only; `alice/` prefix; fixed member timestamp 2026-07-16 12:00 (not `SOURCE_DATE_EPOCH`, which is 1784160000 = 2026-07-16 00:00 UTC, Ch. 7 l.151); modes 0o755 or 0o644; DEFLATE level 9; excludes `build`, `dist`, `.git`, `__pycache__`; skips junk; never follows a symlink; a secret-pattern filename aborts the archive; the gallery example reports `archived 12 files` | 3 (Git and the source zip), 7 (l.287, 398), 8 (l.335 to 349) |
| epubcheck outcomes | five: missing under `PRESS_TOOLCHAIN` fails; missing without it warns; present but cannot run fails as a toolchain fault; nonzero exit fails; pass. The image sets `PRESS_TOOLCHAIN`; press does not key on `CI` | 1, 2 (soft locally), 8 (Table 8.4, l.317); due 14 |
| Doctor states | `absent` (optional missing), `MISSING` (required missing), `BROKEN`; a broken optional tool still keeps the machine from ready; the report opens with its own header line `press doctor` | 2 (Table, l.239 to 256), 8 (l.470, 483): agree |

## Cross-references and promises (from, to, what is promised)

Status: kept (target delivers it), open (target not yet written), or
conflict.

| From | To | Promise |
|---|---|---|
| 1 (l.54) | 2 | covers both routes: the toolchain installed by hand and the toolchain image. Kept. |
| 1 (l.124, 307) | 2 | assumes press and the toolchain installed as Ch. 2 describes; puts the toolchain on `hatter`. Kept. |
| 3 (l.484) | 2 | covers installation in full, including the editable install of a clone. Kept (Example 2.2). |
| 3 (l.500) | 2 | supplies the toolchain a full build needs. Kept. |
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
| 3 (l.641); 7 (l.109, 131); 8 (l.466); 9 (l.114) | 4 | the chapter files; chapter openings, scene breaks, set pieces from the author's side; the drop cap splitting the first word; how a book chooses its chapter opening. All kept. |
| 4 (l.44, 329, 349) | Figures 4.1 `@fig:page-anatomy`, 4.2 `@fig:scene-break-ornaments`, 4.3 `@fig:set-pieces` | page anatomy; the three ornaments in PDF and reader site; the three set pieces. All present (l.46, 331, 351). |
| 1 (l.32) | 9, *The house design* | compares the six design profiles. Kept in draft (Ch. 9 l.135, Figure 9.2). |
| 1 (l.34) | later chapters | `press check`, `press pdf`, `press all`, and the other targets one at a time. Kept (6, 7). |
| 1 (l.36) | 6, *Checking the manuscript* | lists every rule and its message. Kept in draft (Ch. 6 message table, l.457). |
| 1 (l.60) | 1, later | several scars appear later in the chapter. Kept (l.84, l.108, footnote libertine). |
| 1 (l.62) | 1, "Versions and the pinned contract" | explains why design needs a major. Kept (l.291). |
| 1 (l.118) | 16, *Inside the press* | describes the extension contract. Open (stub; design.md row 16 names it). |
| 1 (l.142) | 3, *The shape of a book repository* | walks the scaffold file by file. Kept (Ch. 3, Figure 3.1). |
| 1 (l.208) | 1, the sidebar earlier | the cover-on-page-1 check. Kept (l.94). |
| 1 (l.228, 250) | 1, "The editions" | names the editions; explains sentinels. Kept (l.260, 283). |
| 1 (l.251) | 1, the warning earlier in this section | the first-run font scan. Kept (l.173, same A-head). |
| 1 (l.244) | 14, *Continuous integration and the release contract* | follows the CI build on `printshop` step by step. Open (stub). |
| 1 (l.294) | 14 | takes the pin mechanism apart (floating versus three-part pin, digest). Open (stub). |
| 1 (l.277) | 10, *Front matter, the index, and the table of authorities* | covers *alice-sources.md*. Kept in draft (Ch. 10 l.399, "The sources companion"); see the name ruling under shared facts. |
| 1 (l.279) | 12, *The print pack* | covers the print pack in full. Kept in draft. |
| 1 (l.303) | Appendixes A to E | A *Command reference*: every target (read: command) in manual-page form; B *Configuration reference*: every key of every config file; C *Messages and refusals*: look up a message before reading code; D *The toolchain, platform by platform*: each operating system; E *Glossary*: defines the terms. Titles match the files. Open (stubs). |
| 1 (l.305) | Preface | lists the typographic conventions. Open (Preface written last; see "For the Preface" below). |
| 1 (l.42, 124, 228; l.48) | Figures 1.1 `@fig:pipeline-overview`, 1.2 `@fig:the-stack`, 1.3 `@fig:ten-minute-tour` | manuscript to *dist/*; the layered stack; the tour filmstrip. All present (l.44, 50, 230). |
| 8 (l.25) | 1 | describes the four laws. Kept (l.68 to 108). |
| 8 (l.447) | 1, Example 1.2 | the summary lines of a full run. Kept (l.176 to 192). |
| 10 (l.233) | 5 | names it *Figures and plates*; the title is *Figures, plates, and illustrations*. Conflict (continuity-01, for Ch. 10's pass). |
| 3 (l.70, 106, 128) | 3, "What git has to do with it", "Chapters, appendixes, and how they sort", "Verification knobs" | each "later in this chapter"; all three are later (l.551, 376, 218). Kept. |
| 3 (l.100) | 15, *The operator's desk and the editorial machines* | what the four stamped workflows do. Open (Ch. 15 is a stub). |
| 3 (l.118, 120) | 10, 9, 11, 6 | 10 and 9 cover *index-terms.yaml*, *authorities.yaml*, *aesthetic.yaml* and *tex/title-page.tex*; 11 covers *art/* commissions and candidates; 6 covers *tests/known-bad/*. Kept in draft. |
| 3 (l.126) | 16, *Inside the press* | shows how the book model works. Open (Ch. 16 is a stub). |
| 3 (l.174) | 12, *The print pack* | covers direct print ordering (`commerce.print-ordering`, *config/qualification.yaml*). Kept in draft (Ch. 12 l.499). |
| 3 (l.268) | 9; 12; 13, *Registrations* | 9 the profiles and chapter openings; 12 the print fields; 13 the registration numbers. 9 and 12 kept in draft; 13 open (stub). |
| 3 (l.360) | 9, 10 | add the aesthetic, the index terms, the table of authorities. Kept in draft. |
| 3 (l.484, 500) | 2 | see the existing rows above (installation in full; the toolchain). Kept. |
| 3 (l.535) | 6; 8, *Verifying the artifacts* | 6 takes the four passes apart; 8 covers the verifiers. Kept in draft. |
| 3 (l.599; art l.611) | 14, *Continuous integration and the release contract* | the rest of CI on a tag (`PRESS_RELEASE`, release notes from *CHANGELOG.md*); the Pages bundle. Open (stub). |
| 3 (l.625) | 12 | the publish checklists (`press publish`). Kept in draft (Ch. 12 l.411). |
| 3 (l.74, 390, 607, 615) | Figures 3.1 `@fig:scaffold-tree`, 3.2 `@fig:how-files-sort`, 3.3 `@fig:dist-after-all` | the scaffold tree; how files sort; *dist/* after `press all`. All present (l.76, 394, 609). |
| 7 (l.232) | 3 | lists the `copyright` and `publisher` fields. Kept (Table 3.3). |
| 8 (l.82) | 3 | calls draft knobs vacuous witnesses and shows the refusal. Kept (l.230, Example 3.3; the example cuts "vacuous": continuity-03, finding 7). |
| 8 (l.106) | 3 | set the two sentinels with `press config set`. Kept (l.243). |
| 9 (l.135) | 3 | a book names its design profile in its metadata. Kept (Table 3.5, `print.profile`). |
| 10 (l.171) | 3 | the landing page stacks the subtitle's clauses. Kept (Table 3.3), but **cited as *The shape of a book***: conflict, continuity-03, finding 2. |
| 8 (l.25, 447; l.465; l.491; l.412) | 1; 2; 4; 6 | the four laws and Example 1.2; `press doctor`; the drop cap splitting the first word; the checker looks for sentinels in the manuscript. All kept (Ch. 1 l.68 to 108, 176 to 192; Ch. 2 l.224 to 262; Ch. 4; Ch. 6 l.361). |
| 8 (l.31, 177, 382) | 12, *The print pack* | covers `verify_coverwrap`; the wrap built by `press verify-print`; print ordering. Kept in draft (Ch. 12 l.290 to 298, Table 12.5; "Ordering a copy"). |
| 8 (l.357) | 10, *Front matter, the index, and the table of authorities* | describes the ledger that feeds the sources companion. Kept in draft (Ch. 10 l.399 to 410). |
| 8 (l.509) | 9, *The house design* | next chapter: the typography and layout the verifiers inspect. Kept in draft. |
| 8 (l.27, 210, 274, 412, 459) | 8 | the cover check later (l.179); "Archives and the source edition" later (l.325); "Witnesses and cross-edition agreement" later (l.398); "What the PDF verifier checks" earlier (l.57); the order in the previous section (l.445). All kept. |
| 2 (l.381); 3 (l.535); 4 (l.204); 6 (l.357, 473); 7 (l.357, 422, 513); 10 (l.410); 12 (l.178, 298); 13 (l.254) | 8, *Verifying the artifacts* | reading a failure; the verifiers; sentinels proved in the editions; both settings proved; the edges target by target; what each verifier inspects; what a missing epubcheck costs; opening the artifacts; the archive verifier; the print verifier in full; the EPUB identifier check. All kept (13 in substance: Table 8.3, l.257, no `urn:isbn:` form). Bible items due 8 (epubcheck scar, `pdfimages`) kept (l.323; l.188, 191). |
| 8 (l.51, 433, 485) | Figures 8.1 `@fig:what-each-verifier-inspects`, 8.2 `@fig:rebuild-edges`, 8.3 `@fig:verify-run` | the check-by-run matrix; the rebuild edges and the verify-formats exception; a failed `press verify` on `hatter`. All present (l.53, 435, 487). |

## Numbering check (per chapter: figures, tables, examples)

| Ch. | Figures | Tables | Examples |
|---|---|---|---|
| 2 | 2.1 `02-01-tools-in-the-build`, 2.2 `02-02-doctor-report`, 2.3 `02-03-local-versus-container`: no gap, no repeat, slugs match `CC-NN-slug`, every `@fig:` has its figure. Order follows dev ruling 4 (reading order) and reverses design.md section 5 and brief-02, which still list the doctor report as 2.1. PNGs 02-01 and 02-02 not yet drawn. | 2.1 to 2.4, no gap | 2.1 to 2.7, no gap (the `python3-venv` command at l.69 is an unnumbered display) |
| 3 | 3.1 `03-01-scaffold-tree`, 3.2 `03-02-how-files-sort`, 3.3 `03-03-dist-after-all`: no gap, no repeat, slugs match, every `@fig:` has its figure, each cited before or at its place, order matches design.md section 5 | 3.1 to 3.6, no gap | 3.1 to 3.12, no gap; five uncaptioned fences (l.23, 242, 274, 412, 543), none referred to by number |
| 4 | 4.1 `04-01-page-anatomy`, 4.2 `04-02-scene-break-ornaments`, 4.3 `04-03-set-pieces`: no gap, no repeat, slugs match, every `@fig:` has its figure, each cited before it appears. Reading order swaps design.md's 4.2 and 4.3 (update design.md). One plate, *the-compositor-at-the-frame.png*, unnumbered. PNGs 04-01 to 04-03 not yet drawn | 4.1 to 4.4, no gap | 4.1 to 4.9, no gap; six short uncaptioned fences (l.60, 175, 189, 247, 274, 299), none referred to again |
| 1 | 1.1 `01-01-pipeline-overview`, 1.2 `01-02-the-stack`, 1.3 `01-03-ten-minute-tour`: design.md order, no gap, no repeat, slugs match, every `@fig:` has its figure and is cited at or before it. PNGs are placeholders. Frontispiece plate *the-shop-at-morning.png* unnumbered, present | 1.1, 1.2, no gap | 1.1 to 1.3, no gap; three short uncaptioned fences (l.148, 162, 238), none referred to again |
| 8 | 8.1 `08-01-what-each-verifier-inspects`, 8.2 `08-02-rebuild-edges`, 8.3 `08-03-verify-run`: design.md order, no gap, no repeat, slugs match, every `@fig:` has its figure, each cited before it appears. Plate *the-witness-that-could-say-no.png* unnumbered | 8.1 to 8.7, no gap | 8.1 to 8.3, no gap; every fence `text`, none over 64 columns; many short uncaptioned message fences, none referred to by number |

## For the Preface (from Chapter 1)

Chapter 1's "How to read this book" (l.297 to 307) is the book's own
account of its plan. The Preface, written last, must agree with it, and
its Organization section must match every chapter's final title and A-heads.

- Order: the chapters follow the order in which you make a book.
- Chapters 2 to 8 take a book from installation to verified artifacts:
  installation, the shape of a book repository, the manuscript, figures
  and plates, checking, building, verifying. Read them in order the first
  time.
- Chapters 9 to 13 cover the work after a sound manuscript: the house
  design, the front matter and index (Ch. 10's title also names the table
  of authorities), the art department, the print pack, registrations. Read
  them as the book needs them.
- Chapters 14 to 16 are for the person who runs the press: CI and the
  release contract, the desk and the editorial workflows, the internals.
- Appendixes are for reference: A *Command reference*, B *Configuration
  reference*, C *Messages and refusals* (look a message up here before
  reading the code), D *The toolchain, platform by platform*, E
  *Glossary*. Chapter 1 does not mention the generated subject index or
  the Colophon.
- Promised to the Preface: the typographic conventions. Chapter 1 already
  states two (the `$` prompt; a line of only `...` is elided output) and
  the cast (`alice` on `hatter`, `printshop`, `wonderland-press`). It also
  says chapter references are typed by hand because press cross-references
  figures only, and so are a convention, "the weakest kind of guard". The
  Preface must not contradict any of these.
- History the Preface's opening paragraphs will restate: see shared facts
  "Press history dates" and "Earlier books".
