# Fact check: Chapter 1, Introduction

Checked `book/chapters/01-introduction.md` against `docs/briefs/facts/facts-01.md`, including the Shared context (sections 1.4, 19, 20) and the managing editor's supplement (S1, S2). Line numbers refer to the chapter.

**Captured output.** Three code blocks present captured output.

- The `press check` fragment (lines 149 to 153) matches the file's capture (facts lines 125 to 132): the first line verbatim, the rest elided with `...`.
- The `press wordcount` block (lines 170 to 174) matches the file character for character (facts lines 136 to 139).
- In the Figure 1.3 directive (line 196), panel 2's quoted lines match the capture verbatim, with the two `note:` lines elided as `...`.
- Example 1.2 (lines 186 to 192) and panel 3 of the Figure 1.3 directive do not match the real capture in S1. See Contradicted 1 and 2.

Two claims about this book, not about press, were checked against the book's own config and hold. Line 61: the title page carries "Clint Ecker" and "LGTM" (`config/metadata.yaml` sets author "Clint Ecker" and publisher "LGTM Publishing"). Line 81: *config/house-rules.yaml* exists and has `banned-patterns`.

## 1. Unsupported

1. **The slug `alice` and where it lives.** Line 71: "The slug `alice` appears once, in *config/metadata.yaml*." Example 1.1 (lines 133 to 141) runs `press new alice` and never sets a slug. Every filename in the chapter (*alice.pdf*, Table 1.2, Examples 1.2) depends on the slug being `alice`. I searched for: slug, `press new`, metadata.yaml. The file says only that the slug is one of the book-specific facts that "lives in the book repository" (1.4), that artifacts are "named from the registry" as `<slug>.pdf` and so on (3.5), and, in S1, that the book's sample has "slug `alice`". Nothing says that `press new alice` writes `slug: alice`, or that the slug lives in *config/metadata.yaml*. Fix: have the editor confirm what `press new alice` writes for the slug. If it does not write `alice`, add an explicit set to Example 1.1. Until then, soften line 71 to the file's wording: the slug is a book-specific fact that "lives in the book repository", and the registry names every artifact from it.
2. **The checker's rules.** Line 31: "An em dash, a curly quote, a glyph outside the print fonts, or a paragraph of 190 words or more each stops it." I searched for: curly, quote, 190, paragraph. The file supports the em dash and the glyph rule through the fixture note ("glyph U+2014 is outside the print-font set", facts line 127). It has no curly-quote rule and no 190-word limit. (The writer's report takes the 190 from the checker's behaviour on this book. That is not the fact file.) Fix: "An em dash or any other glyph outside the print-font set stops it." Leave the full list to Chapter 6.
3. **Python floor and poppler.** Line 40: "the fonts, epubcheck, and poppler. press itself needs Python 3.10 or later." The Figure 1.2 directive (line 42) also has the band "Python 3.10 or later". I searched for: 3.10, Python, poppler. The file mentions 3.10 only in the 3.0.2 note: "Pillow 13 needs Python 3.11; ... 3.10 installs resolve 12.x". That implies 3.10 installs work, but the file never states a floor. poppler is never named; the file names its tools `pdftoppm` (war story 9) and `pdfimages` (20.B.14). Fix: name the tools the file names ("`pdftoppm` and `pdfimages`"), and either cut the floor or soften it to "an install on Python 3.10 still works, with Pillow 12.x". Make the directive's band read "Python".
4. **The image name and the watchlist.** Line 45: "`ghcr.io/clintecker/press-toolchain`, a public container image" and "the jargon watchlist". I searched for: ghcr, press-toolchain, watchlist. The file says only "the image is public" (3.4) and calls the jargon pass "no rewrite-status terms". Fix: confirm the image name with the editor, or write "the toolchain image, a public container image". For the house contents, say "the jargon list" or name only what the file shows.
5. **Sentinels.** Line 241: "listed under `verify-sentinels` in *config/metadata.yaml*, that each rendered edition must contain. If a sentinel goes missing from any edition, the build stops". I searched for: verify-sentinels, sentinel. The file has the refusal `sentinel ... not found` (3.4) and says a sentinel on a drop cap "fails exact PDF matching" (war story 29). It gives no key name and no claim that every edition is checked. Fix: "A *sentinel* is a phrase from the manuscript that the verifiers must find in the built book; a missing one stops the build with `sentinel ... not found`." Have the editor confirm the key name before printing `verify-sentinels`.
6. **The drop cap as the house opening.** Line 244: "The house chapter opening sets a drop cap that splits the first word and small-caps the rest of it." I searched for: drop cap, chapter-opening, house. The file's gallery table lists a drop cap as a per-book setting (Alice, the almanac, the novella), and GALLERY's "To change… The initial that opens each chapter | `chapter-opening:`" (facts line 258) presents it as something a book opts into. The file never says the house default is a drop cap. War story 29 reads "The drop cap splits and small-caps a chapter's first word". Fix: "A drop-cap chapter opening splits and small-caps a chapter's first word, so a sentinel placed there fails exact PDF matching."
7. **The 11.5 percent sidebar.** Line 92: "one dropped out of place, and one clipped". Line 96: "checks for the cover on page 1 of every book it inspects, including books that never had a cover problem". The file says only "shipped a dropped and a clipped cover" and "This is also why the PDF verifier checks the cover on page 1" (war story 20). "Dropped" may mean that the cover went missing, so "out of place" is a guess. "Every book" also conflicts with covers being optional (a book may have no `assets/cover.jpg`). Fix: "one dropped and one clipped", and "The PDF verifier now checks the cover on page 1."
8. **"it will tell you so."** Line 121: "If you want to rename *alice.pdf* or skip epubcheck, you ask for something press does not offer, and it will tell you so." I searched for: rename, skip, refusal. Nothing says press refuses or reports such a request. Fix: cut "and it will tell you so". The QUICKSTART ownership line carries the point: "The press owns": build order, verification pipeline, file names, and formats.
9. **Every example from 3.0.2.** Line 249: "and every example in this book comes from it." The file dates only the S1 capture (2026-11-11). It gives no press version for any capture. Fix: cut the clause, or have the managing editor rule on it.
10. **CI install mechanics and the tag convention.** Line 267: "*the composite action*, *action.yml*, installs press from its own checkout." Line 261: "the tags follow the GitHub Actions convention" and "moves to the latest compatible release in its major". I searched for: action.yml, composite, checkout, Actions convention. The file's design rationale says only "Why pip-from-git is not used in CI. A private book needs no cross-repo token, and the installed press is pinned to the exact action ref", and on tags only "`vN` floats; three-part tags are immutable". Fix: "In CI, press is not installed with pip from Git: a private book then needs no cross-repo token, and the installed press is pinned to the exact action ref." For tags: "A floating tag such as `v3` floats; an immutable tag such as `v3.0.2` ...". Have the editor confirm `action.yml` before naming it.
11. **"sealed".** Line 27: "A *profile* is a sealed interior geometry". I searched for: sealed, profile. The file says only that v2 and later "have six profiles" (20.A.1), with per-profile image caps (20.A.5). Fix: "A *profile* is one interior geometry: trim, margins, and image caps".
12. **Minor glosses not in the file.** Low stakes; the editor can soften them or accept them as general knowledge.
    - Line 29: "press calls each command that does one of them a *target*". The file never uses the term.
    - Line 33: "pandoc's own writers produce ... the single HTML file, ... the plain text, and the DOCX". The file ties pandoc only to the EPUB (war story 13) and the chunked site (war story 6).
    - Line 105: "The ROADMAP explains why the laws stack the way they do." The ROADMAP's trust law is about layers of proof, not about the order of the four laws. Fix: "The ROADMAP adds a law about proof."

## 2. Contradicted

1. **Example 1.2 is a reconstruction, not the capture.** Lines 186 to 192 print `ls dist/` as two columns:

   ```text
   alice-site.zip    alice.docx  alice.html  alice.pdf  pages
   alice-source.zip  alice.epub  alice.md    alice.txt  site
   ```

   The real capture (S1, facts lines 448 to 460, with the slug changed to `alice` as S1 directs) is one entry per line. The block presents itself as captured output, so it must match character for character. Fix: replace the block with:

   ```text
   $ press all
   ...
   $ ls dist/
   alice-site.zip
   alice-source.zip
   alice.docx
   alice.epub
   alice.html
   alice.md
   alice.pdf
   alice.txt
   pages
   site
   ```

   The set of entries and their order are the same as the chapter's, so the prose at line 194 and Table 1.2 still hold. Optionally, the `...` after `press all` can end with the run's real closing lines from S1 (see Missing 1).
2. **Figure 1.3, panel 3, carries the same reconstruction.** The directive (line 196) says: "Panel 3: "$ ls dist/", then "alice-site.zip    alice.docx  alice.html  alice.pdf  pages" and "alice-source.zip  alice.epub  alice.md    alice.txt  site"". Fix: "Panel 3, each line exactly: "$ ls dist/"; "alice-site.zip"; "alice-source.zip"; "alice.docx"; "alice.epub"; "alice.html"; "alice.md"; "alice.pdf"; "alice.txt"; "pages"; "site"." The fig-alt ("the third lists the artifacts in the dist directory") still holds. Panel 3 now runs to eleven lines, so the illustrator may need taller panels.

## 3. Drifted

1. **The README quote's ending** (line 25). The quote ends "gated GitHub releases." The source continues "gated GitHub releases; the print pack adds ...". A period has replaced the semicolon inside quotation marks. Fix: end with an elision ("... and gated GitHub releases ...") or close the quotation before the full stop in running text.
2. **"lives only in the tags"** (line 51). The file: "Earlier history lives in the tags". The same sentence then quotes the CHANGELOG's summary of that history, so "only" contradicts itself. Fix: drop "only".
3. **"Inside the toolchain image"** (line 103). The file places the failure in "containers", which "do not register" binfmt_misc. The toolchain image now ships the wrapper, so the failure no longer happens inside it. Fix: "In a container, 'the command exists ...'".
4. **The trust ladder drops a rung** (line 105). The chapter has "from deterministic functions through real tools, complete workflows, consumer repositories, and release identity". The file: "from deterministic functions through compositions, real tools, complete workflows, consumer repositories, and release identity". Fix: restore "compositions".
5. **`press pages` after `press all`** (line 194): "To look at the landing page as a reader will see it, run `press pages` and open *dist/pages/index.html*". Ruling S2: "`press all` does assemble `dist/pages/`; QUICKSTART runs `press pages` afterwards only to show the command." Fix: "`press all` has already built the landing page; open *dist/pages/index.html* in a Web browser. `press pages` rebuilds the bundle alone."
6. **"no change in its typography"** (line 263). The rule protects "typography or layout of a valid book", and "fixes may correct broken output". Fix: "and no change in the typography of a valid book".
7. **Who pins the image** (line 45): "A book's CI pins the image itself by digest". By the chapter's own line 261 and file 20.A.2, the press's reusable workflow (*build.yml*) at a tag pins the image by `@sha256:` digest. The book does not pin it. Fix: "The press's reusable workflow pins the image by digest".
8. **The public date** (line 59): "The repository `clintecker/press` became public on 2026-07-19." The file attributes this to a source: "The roadmap describes the GitHub repo `clintecker/press` as public since 2026-07-19." Fix: "According to the ROADMAP, the repository has been public since 2026-07-19."
9. **The vacuous-test footnote** (`[^vacuous]`, line 291). "the variable `PRESS_REQUIRE_LUA=1`" names the setting as the variable; the variable is `PRESS_REQUIRE_LUA`. "The backfill that followed" adds an order the file does not give: both changes landed in 3.0.2. Fix: "until `PRESS_REQUIRE_LUA=1` forbade the skip. The same release backfilled 31 Lua tests, and they found a title-tie test that passed with no filter at all, because pandoc ties `Mr.` itself."
10. **Dependency edges stated as absolute** (line 87): "The commands in press carry dependency edges for that reason". File 20.B.11: "`press verify-formats` includes an existing, possibly stale, `dist/<slug>.pdf` in the cross-edition agreement check without rebuilding it." Fix: use the file's statement of intent, "the CLI's dependency edges exist so that cannot happen", and do not claim that every command has them.
11. **"a 42-word preface stub"** (line 143). The 42 comes from `press wordcount`, which the chapter says five paragraphs later also counts HTML comments. The stub's prose may therefore be shorter. Fix: "a preface stub that `press wordcount` counts at 42 words".

## 4. Missing

1. **How `press all` ends.** S1 gives the run's closing lines verbatim:

   ```text
   commerce release gate: print ordering is not enabled; no commerce release gate

     press. your book is ready → dist/
   ```

   Example 1.2's `...` could end with them, so the reader recognises success. Caution: the capture uses `→` (U+2192). Confirm that it passes the book's print-font glyph check before setting it in a code block.
2. **The full `press all` sequence** (line 182 says check, build, verify). S2 gives six steps: check, every format, the source zip, pages, the verifiers, and the commerce gate (advisory). Adding "the source archive, the Pages bundle" and "an advisory commerce gate" would explain both `pages` in the listing and the closing line above.
3. **`press all` does not build the print pack** (20.B.13). Line 237 implies this with "has its own targets". One explicit clause would stop the reader from looking for *alice-interior.pdf* after `press all`.
4. **The `verify-min-pages` default** (20.A.9). The scaffold writes 1, but the model default is 40. A reader who deletes the line from *config/metadata.yaml* gets 40, and a short book then fails. One clause at line 241 would prevent that.
