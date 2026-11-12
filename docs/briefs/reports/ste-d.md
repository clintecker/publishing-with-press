# STE80 editor report: Appendix D, The toolchain

File: `book/appendices/d-the-toolchain.md`. Mode: Humanize for body prose,
table cells, admonitions, and the footnote. No sidebar or anecdote in this
appendix needed Light mode. No fence, code span, quotation, message,
heading, or footnote label was touched.

## Ratchet

- Before: 4 (baseline in `tools/ste-baseline.json`: 4)
- After: 1 (the heading "What is untested", which the brief puts out of reach)
- `press check`: passes (exit 0).

## Edits (line numbers are in the edited file)

1. Line 3, S1/S2 (27 words, three parts) and S10 (phrasal verb).
   Old: "This appendix gives the toolchain for each platform the press supports, then *the toolchain image* that carries all of it, then what the press does not test. Chapter 2, *Installing press*, walks through the same ground as a first installation."
   New: "This appendix gives the toolchain for each platform the press supports. It then describes *the toolchain image* that carries all of it, and what the press does not test. Chapter 2, *Installing press*, covers the same ground as a first installation."
2. Line 30, S10 (one meaning per word; "if" read as a condition). The fact file's own word is "whether".
   Old: "It reports if `OPENAI_API_KEY` and `GEMINI_API_KEY` are set. ... and it reports if Pillow, pypdf, and ruamel.yaml import."
   New: "It reports whether `OPENAI_API_KEY` and `GEMINI_API_KEY` are set. ... and it reports whether Pillow, pypdf, and ruamel.yaml import."
3. Line 32, S1 (three ideas) and S3 (condition first).
   Old: "`pdfimages` comes with poppler, and its absence silently softens two checks to notes, so install poppler in full."
   New: "`pdfimages` comes with poppler. If `pdfimages` is absent, two checks silently soften to notes, so install poppler in full."
4. Line 32, S13 (the split above made seven sentences; two linked facts joined).
   Old: "The press's own documentation Web site drives a headless Chrome for its layout check. No book needs Chrome."
   New: "The press's own documentation Web site drives a headless Chrome for its layout check, but no book needs Chrome."
5. Line 61, S1/S2 (29 words, three ideas).
   Old: "The second is epubcheck: Ubuntu's launcher runs the jar through binfmt_misc, which containers do not register, so it dies with "Exec format error" only when it runs (Chapter 2)."
   New: "The second is epubcheck. Ubuntu's launcher runs the jar through binfmt_misc, which containers do not register. The launcher therefore dies with "Exec format error" only when it runs (Chapter 2)."
6. Line 63, S2 (ratchet lead, 31 words) and S1.
   Old: "The press repairs this in two parts: the image's wrapper (Example D.4) replaces the launcher, and the verifier reports a present-but-unrunnable epubcheck as a fault in the toolchain, not in your EPUB."
   New: "The press repairs this in two parts. First, the image's wrapper (Example D.4) replaces the launcher. Second, the verifier reports a present-but-unrunnable epubcheck as a fault in the toolchain, not in your EPUB."
7. Line 167, S1 (three ideas in one sentence).
   Old: "Inside the image, `pip install` needs `--break-system-packages`, `--rm` removes the container afterward, and the artifacts stay in the mounted *dist/* (Chapter 2)."
   New: "Inside the image, `pip install` needs `--break-system-packages`. The `--rm` flag removes the container afterward, and the artifacts stay in the mounted *dist/* (Chapter 2)."
8. Line 169, S2 (ratchet lead, 31 words) and S1.
   Old: "For a build that matches CI, replace `:latest` with the digest on the `image:` line of the press's *build.yml* at your book's tag, and install press at that tag (Chapters 2 and 14)."
   New: "For a build that matches CI, replace `:latest` with the digest on the `image:` line of the press's *build.yml* at your book's tag. Install press at that tag as well (Chapters 2 and 14)."
9. Line 173, S2 (ratchet lead, 33 words) and S1. The footnote stays on the Colima sentence, which it explains.
   Old: "People who work on the press itself have *scripts/dev-render.sh*, which runs the checkout inside the pinned toolchain image (Chapter 2) and on macOS with Colima can mount a book only under `$HOME`.[^d-colima]"
   New: "People who work on the press itself have *scripts/dev-render.sh*. It runs the checkout inside the pinned toolchain image (Chapter 2). On macOS with Colima, the script can mount a book only under `$HOME`.[^d-colima]"

## Leads declined

- Line 177, passive "is untested": it is a heading. The brief forbids
  touching headings.
- Line 53, "The *Dockerfile* names `texlive-latex-extra` for lettrine, and
  `texlive-fonts-extra` for the yfonts collection, whose yinit initials draw
  the `ornate` chapter opening." (24 words; not a ratchet lead). It holds
  two parallel package-to-purpose pairs. A split would push the paragraph to
  seven sentences, and the existing sentences each carry a fact.

## Passives kept

- Line 122, "runs book builds inside it, pinned by digest": a participle.
  The actor (the reusable workflow) is the subject of the sentence.
- Line 88, "(`press desk`, described in Chapter 15)": a cross-reference
  participle. The actor (this book) does not matter.

## Fidelity checks

- All index terms that the file held before still occur (binfmt_misc,
  dev-render.sh, poppler, OPENAI_API_KEY, GEMINI_API_KEY, Pillow, pypdf,
  build.yml, digest, and the others). The three sentinels are not in this
  file and are untouched elsewhere.
- No semicolon in prose. The two semicolons in the file are inside a
  press message and a quotation.
- Edit 3 keeps "silently" and the actor stays unnamed, as in the fact file
  ("its absence silently softens two checks to notes").
