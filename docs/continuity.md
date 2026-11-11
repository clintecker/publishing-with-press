# Continuity bible

Maintained by the continuity editor only. Chapters are numbered as in
`docs/design.md` section 5.

Chapters 1, 3, and 4 have not had their own continuity pass. Entries that
cite them were cross-checked from Chapter 2's pass against their current
drafts and stay provisional until each chapter's own pass confirms them.

## Fixed cast

| Thing | Name |
|---|---|
| sample book | *Alice's Adventures in Wonderland*, slug `alice` |
| author at the keyboard | `alice` |
| workstation | `hatter` |
| CI host | `printshop` |
| repository owner | `wonderland-press` |
| press version | 3.0.2, always with "at the time of this writing" |

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

## Numbering check (per chapter: figures, tables, examples)

| Ch. | Figures | Tables | Examples |
|---|---|---|---|
| 2 | 2.1 `02-01-tools-in-the-build`, 2.2 `02-02-doctor-report`, 2.3 `02-03-local-versus-container`: no gap, no repeat, slugs match `CC-NN-slug`, every `@fig:` has its figure. Order follows dev ruling 4 (reading order) and reverses design.md section 5 and brief-02, which still list the doctor report as 2.1. PNGs 02-01 and 02-02 not yet drawn. | 2.1 to 2.4, no gap | 2.1 to 2.7, no gap (the `python3-venv` command at l.69 is an unnumbered display) |
