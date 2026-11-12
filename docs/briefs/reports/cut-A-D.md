# Cutting pass: Appendix A and Appendix D

Files: book/appendices/a-command-reference.md, book/appendices/d-the-toolchain.md.
Words: A 7690 -> 7703 (+13, the should adds a sentence), D 2527 -> 2265 (-262).
`press check`: passed (exit 0).

## Appendix A

1. `A:909` (press pdf), font scan, pointer.
   Before: "The first run on a fresh machine spends several minutes on a font scan, which looks like a hang and is not one."
   After: "A fresh machine's first run is slow (the first run's font scan, Chapter 2)."
2. `A:86` (press all), print pack. Kept as the brief directs (the reference entry says it once).
3. `A:594` should, Example A.6.
   Captured value: `"kind": "plate",` -> `"kind": "figure",`.
   Added after "Example A.6 shows the start of the entry for one plate.":
   "The White Rabbit has no class, so the report calls it a `figure`. The numbering treats it as a plate (Chapter 5)."
   The brief's text joins these with a semicolon. The house bans semicolons in prose, so the two clauses became two sentences. Verified in press: `figures.py` `DEFAULT_KIND = "figure"`.

## Appendix D

4. `D:5` word count.
   Before: "The press's install guide names its platforms in one sentence:"
   After: "The press's install guide names its platforms:"
5. `D:61` binfmt story, cut to one sentence (Chapter 2 keeps it).
   Before: "The second is epubcheck. Ubuntu's `epubcheck` launcher runs the jar through binfmt_misc, which containers do not register. The command exists and `which` finds it. It dies with "Exec format error" only when it runs."
   After: "The second is epubcheck: Ubuntu's launcher runs the jar through binfmt_misc, which containers do not register, so it dies with "Exec format error" only when it runs (Chapter 2)."
6. `D:63` binfmt repair, cut to one sentence.
   Before: "The press repairs this in two parts. The toolchain image replaces the launcher with a plain wrapper, shown in Example D.4. The verifier reports a present-but-unrunnable epubcheck as a fault in the toolchain, not in your EPUB."
   After: "The press repairs this in two parts: the image's wrapper (Example D.4) replaces the launcher, and the verifier reports a present-but-unrunnable epubcheck as a fault in the toolchain, not in your EPUB."
7. `D:65-67` warning, cut to one sentence (the jar path kept).
   Before: "If you build your own container from Ubuntu, do not trust the packaged `epubcheck` launcher. Install a wrapper that runs `java -jar /usr/share/java/epubcheck.jar` with the original arguments, as the toolchain image does."
   After: "If you build your own container from Ubuntu, replace the packaged `epubcheck` launcher with a wrapper that runs `java -jar /usr/share/java/epubcheck.jar` with the original arguments."
   `D:69` (the verifier's quoted message and the Appendix C pointer) kept verbatim: it is not told in Chapter 2.
8. `D:73` `--break-system-packages`, cut to one sentence.
   Before: "Ubuntu 24.04 manages its own Python. That Python refuses a bare `pip install` into its site-packages directory. The rule comes from Python's packaging standards (PEP 668), not from press. The press's install guide never mentions a virtual environment, and its container recipe uses `--break-system-packages` instead."
   After: "Ubuntu 24.04's own Python refuses a bare `pip install` under PEP 668, and the press's container recipe answers with `--break-system-packages` (Chapter 2)."
9. `D:96` fit-the-page aside.
   Before: "with the guide's own comments wrapped to fit the page."
   After: "with the guide's own comments." (The line breaks in Example D.3 kept.)
10. `D:118-120` `[^d-runner]` (`macos-14`). Footnote and its marker cut.
11. `D:122-124` subsection "The first LuaLaTeX run". Cut outright (heading and paragraph). Table D.2's "first-run font scan" row stays.
12. `D:147` `CI=false`.
    Before: "Press does not read the ambient `CI` variable for this, because `CI=false` would read as truthy."
    After: "Press does not read the ambient `CI` variable for this."
13. `D:159` Docker command intro, cut to one sentence.
    Before: "Example D.5 runs `press all` in the image from the top of the `alice` book repository on `hatter`. The command mounts the book repository at */book*, installs press inside the container, and runs the target there."
    After: "Example D.5 runs `press all` in the image from the top of the `alice` book repository on `hatter`, mounted at */book* (Chapter 2)."
    Example D.5 itself kept verbatim.
14. `D:173` flags paragraph, cut to one sentence.
    Before: "Inside the image, `pip install` needs `--break-system-packages`, because the image's Python belongs to the operating system and refuses a bare install. The `--rm` flag removes the container when the build ends. The artifacts remain in the book repository's *dist/* directory, which lives on the mounted volume."
    After: "Inside the image, `pip install` needs `--break-system-packages`, `--rm` removes the container afterward, and the artifacts stay in the mounted *dist/* (Chapter 2)."
15. `D:175` matching CI, cut to one sentence.
    Before: "The tag `:latest` suits an experiment. For a build that matches CI exactly, replace `:latest` with the digest from the `image:` line of the press's *build.yml* at the tag your book pins. Then install press at that same immutable tag. CI itself installs press from the composite action's own checkout of that tag, never with pip from Git. Chapter 14, *Continuous integration and the release contract*, shows where the pin lives."
    After: "For a build that matches CI, replace `:latest` with the digest on the `image:` line of the press's *build.yml* at your book's tag, and install press at that tag (Chapters 2 and 14)."
    The self-checkout fact is told in Chapter 14 ("Self-checkout install", `14:110-112`, and `14:205`).
16. `D:179` dev-render, cut to one sentence; the Colima limit and `[^d-colima]` kept, because Chapter 2 does not tell them.
    Before: "People who work on the press itself have *scripts/dev-render.sh* in the press checkout. It runs `python -m press` from the checkout's *src/* directory inside the pinned toolchain image, so a source edit takes effect on the next run with no reinstall. It reads the image from *build.yml*, so it runs the image that the reusable workflow pins. The press's notes call it "the edit-render-look loop, not the proof". On macOS with Colima, it can mount a book only under `$HOME`.[^d-colima] A book author never needs it."
    After: "People who work on the press itself have *scripts/dev-render.sh*, which runs the checkout inside the pinned toolchain image (Chapter 2) and on macOS with Colima can mount a book only under `$HOME`.[^d-colima]"

Kept, per the brief: `D:59` font scar (the only appendix telling), the package lists (Examples D.1 to D.3), the wrapper (Example D.4), the architecture note ("Architectures, tags, and the digest", "Apple Silicon"), Table D.2.

## Declined or adjusted

- `A:594`: the brief's semicolon replaced with a period (house rule).
- Nothing else declined. No closing maxims were listed for A or D.

## Noticed, not changed (outside the brief)

- Example A.6 captures `"caption": "The White Rabbit"`, while Example 5.1 (`05:49`) declares the caption "Alice and the White Rabbit". Captured output, so left for the facts editor.
