# Appendix D: The toolchain, platform by platform {.unnumbered}

Press is a Python package, and it does little by itself. The work of making a book falls to *the toolchain*, the outside programs press runs: pandoc, LuaLaTeX, latexmk, the fonts, epubcheck with the Java that runs it, and poppler. This appendix gives the toolchain for each platform the press supports, then *the toolchain image* that carries all of it, then what the press does not test. Chapter 2, *Installing press*, walks through the same ground as a first installation.

The press's install guide names its platforms: "Supported platforms are Linux (the container's Ubuntu 24.04 is the reference) and macOS." In this appendix, Linux means Debian and Ubuntu with the package list below, or the toolchain image on either of its two architectures.

## What every platform needs {-}

At the time of this writing, press needs a Python from 3.10 to 3.14 on every platform. The press's CI tests all five of those releases on Ubuntu, and Python 3.12 on macOS 15. Press itself depends on three Python packages: Pillow, pypdf, and ruamel.yaml. Pip installs them with press.

Three commands need no book and no toolchain: `press --version`, `press --help`, and `press <command> --help`. All three exit with status 0, so they make a first test of a new install before the toolchain is complete.

Table D.1 lists the external tools that `press doctor` looks for, with the doctor's own words for what each one does. If a required tool is absent, the doctor reports `MISSING`. If an optional tool is absent, the doctor reports `absent`. If a tool is present but fails both `--version` and `-v` within 15 seconds, the doctor reports `BROKEN`.

| Tool | What it does | Required |
|------------|------------------------------------------------------|----------|
| `pandoc` | every build target | yes |
| `lualatex` | PDF and print builds | yes |
| `latexmk` | PDF and print builds (multi-pass convergence) | yes |
| `pdftoppm` | PDF verification renders | yes |
| `pdffonts` | font-embedding verification | yes |
| `pdfinfo` | PDF structure verification | yes |
| `pdftotext` | PDF text verification | yes |
| `git` | scaffolding identity and book repositories | yes |
| `epubcheck` | the retail EPUB gate (softens to a warning locally) | no |
| `claude` | the operator: press improve, research, aesthetic briefs | no |

Table: Table D.1. The tools press doctor checks

The doctor also reports `realesrgan`, which `press art enhance` uses to upscale plates. It reports if `OPENAI_API_KEY` and `GEMINI_API_KEY` are set. It reports the Python version against the tested range, and it reports if Pillow, pypdf, and ruamel.yaml import.

A few programs escape the doctor. `pdfimages` comes with poppler, and its absence silently softens two checks to notes, so install poppler in full. The toolchain image's epubcheck wrapper needs `java`. When `oxipng` or `pngcrush` is present, `press art enhance` uses it. The press's own documentation Web site drives a headless Chrome for its layout check. No book needs Chrome.

::: {.tip}
> **Tip:** Run `press doctor` after any change to the toolchain. When the machine is ready, it prints `this machine can make books` and exits with status 0. Otherwise it exits with status 1.
:::

At the time of this writing, a broken optional tool also makes the doctor report the machine not ready. The doctor can therefore refuse a machine over a tool that you do not need.

## Debian and Ubuntu {-}

The press builds the toolchain image from Ubuntu 24.04 with its own *Dockerfile*. That file's package list is the canonical list for Debian and Ubuntu. Example D.1 gives the list as the install guide prints it.

**Example D.1. The toolchain on Debian and Ubuntu**

```text
$ sudo apt-get install --no-install-recommends \
    make git pandoc python3 python3-pip poppler-utils \
    texlive-luatex texlive-latex-extra texlive-fonts-extra \
    fonts-linuxlibertine latexmk epubcheck
```

Each package has its own role. `pandoc` reads the manuscript and writes every edition. `texlive-luatex` and `latexmk` set the Print edition (the PDF). The *Dockerfile* names `texlive-latex-extra` for lettrine, and `texlive-fonts-extra` for the yfonts collection, whose yinit initials draw the `ornate` chapter opening. `poppler-utils` supplies the four PDF tools of Table D.1, and `pdfimages` besides. `epubcheck` validates the Circulating edition (the EPUB).

### Two Ubuntu scars {-}

Each of two packages in the list carries a *scar*, the press's word for a production failure turned into a guard. Both concern Ubuntu.

The first is the font. The house PDF face is Libertinus, which TeX Live carries. Ubuntu has no `fonts-libertinus` package. Also, `--no-install-recommends` drops the Libertine keyboard face. The *Dockerfile* therefore names `fonts-linuxlibertine` explicitly. If you copy the flag, keep that package in your own list.

The second is epubcheck: Ubuntu's launcher runs the jar through binfmt_misc, which containers do not register, so it dies with "Exec format error" only when it runs (Chapter 2).

The press repairs this in two parts: the image's wrapper (Example D.4) replaces the launcher, and the verifier reports a present-but-unrunnable epubcheck as a fault in the toolchain, not in your EPUB.

::: {.warning}
> **Warning:** If you build your own container from Ubuntu, replace the packaged `epubcheck` launcher with a wrapper that runs `java -jar /usr/share/java/epubcheck.jar` with the original arguments.
:::

The verifier's message for the broken launcher reads `epubcheck is present but cannot run (<exc>); the toolchain image is broken`. Appendix C, *Messages and refusals*, lists the other epubcheck messages.

### Installing press on Debian and Ubuntu {-}

Ubuntu 24.04's own Python refuses a bare `pip install` under PEP 668, and the press's container recipe answers with `--break-system-packages` (Chapter 2).

We recommend that you give press a virtual environment of its own. On Debian and Ubuntu the `venv` module comes in a separate package, `python3-venv`, which the press's list does not include. Example D.2 adds that package to the press's list, as our own addition. It then installs press from Git at the *floating tag* `v3`, the tag that moves to each compatible v3 release.

**Example D.2. Press in a virtual environment on Ubuntu**

```text
$ sudo apt-get install python3-venv
$ python3 -m venv ~/.press-venv
$ . ~/.press-venv/bin/activate
$ pip install \
    "press @ git+https://github.com/clintecker/press@v3"
$ press doctor
```

Pip from Git at a tag is the supported channel. Press is not on PyPI, so you install it from Git. For *the desk* (`press desk`, described in Chapter 15), install the `tui` extra with `"press[tui] @ git+https://github.com/clintecker/press@v3"`. To track a clone of the press, install it editable with `pip install -e .` from the clone, or `pip install -e '/path/to/press[tui]'` with the desk.

### Versions on Debian and Ubuntu {-}

The press pins no pandoc or TeX Live release by number. Its compatibility notes say that "the exact tool versions are whatever Ubuntu 24.04 shipped, frozen by the image digest". Another Debian or Ubuntu release brings its own pandoc and TeX Live, and the press does not test them.

## macOS {-}

On macOS, Homebrew supplies the whole toolchain, TeX distribution included. Example D.3 gives the three commands from the install guide, with the guide's own comments.

**Example D.3. The toolchain on macOS**

```text
$ brew install pandoc poppler
$ brew install --cask mactex-no-gui   # lualatex, latexmk,
                                      # TeX Live
$ brew install epubcheck              # optional: the retail
                                      # EPUB gate locally
```

The MacTeX cask brings LuaLaTeX, latexmk, and TeX Live in one install. About fonts, the guide says: "TeX Live carries Libertinus for the PDF; nothing else to install." The Ubuntu font scar therefore does not arise on the Mac.

The epubcheck formula is optional. Without it, press validates the EPUB structurally and prints a warning that names the remedy, `brew install epubcheck`. The retail EPUB gate runs in CI whatever your workstation lacks. If you want to see epubcheck's faults before you push, install the formula locally.

When the doctor reports the machine not ready, its last line carries a short install hint for each platform. In the press's captured run, the hint followed a broken optional tool. The macOS hint reads `brew install pandoc mactex-no-gui poppler`. It names the required packages of Example D.3 in one line, and it leaves out epubcheck.

A Homebrew Python refuses a bare `pip install` into its own site-packages directory, as Ubuntu's does. We recommend the same virtual environment as Example D.2, without the `apt-get` line.

### Apple Silicon {-}

Apple Silicon is the maintainer's primary platform. Local container builds on Apple Silicon work, because the press publishes the toolchain image for arm64. The press's full verification script, `scripts/verify.sh --full`, also runs natively on Apple Silicon.

## The toolchain image {-}

The toolchain image is `ghcr.io/clintecker/press-toolchain`, a container image the press builds from its own *Dockerfile*. The *reusable workflow*, the press's *build.yml* that a book's CI calls, runs book builds inside it, pinned by digest. On a workstation it is the one route that needs no toolchain installed at all, only Docker.

### What the image holds {-}

The image starts `FROM ubuntu:24.04` and sets `PRESS_TOOLCHAIN=1`. Its apt packages are those of Example D.1 plus `gh`, the GitHub command-line tool. On top of the packages it adds three things:

- a wrapper for epubcheck at */usr/local/bin/epubcheck*
- Real-ESRGAN with the remacri and ultrasharp models in */usr/local/share/realesrgan/models*, on amd64 only, with `mesa-vulkan-drivers` for a software Vulkan
- the image's Lua tooling: at the time of this writing, stylua v2.5.2, and selene 0.31.0 on amd64

Example D.4 shows the wrapper, as the *Dockerfile* writes it. It is the image's half of the repair for the binfmt scar. The verifier's report of a toolchain fault is the other half.

**Example D.4. The epubcheck wrapper in the toolchain image**

```text
#!/bin/sh
exec java -jar /usr/share/java/epubcheck.jar "$@"
```

The variable `PRESS_TOOLCHAIN` tells press that it runs in the reference environment. Press sets its strictness from that variable. Inside the image, a missing epubcheck is fatal, where on a workstation it is a warning. Press does not read the ambient `CI` variable for this.

### Architectures, tags, and the digest {-}

The press publishes the image for amd64 and arm64 and tests each build before it pushes it. The arm64 image has no upstream Real-ESRGAN binary, so on arm64 `press art enhance` resamples a plate instead of upscaling it.

Two tags point at the image: `:latest` and `:sha-` followed by a commit hash. Neither is immutable. The reusable workflow therefore pins the image by its `@sha256:` digest, a hash of the image's exact bytes. The release contract refuses an *immutable tag*, a three-part press tag such as `v3.0.2`, whose reusable workflow names only a `sha-` tag. The digest is how a book pinned to `v3.0.2` builds with the same pandoc and TeX Live on every run.

The image is public. A book under any account pulls it with no package grant and no configured secret. In CI, the reusable workflow authenticates the pull with its own `GITHUB_TOKEN`. That token works for a public image on fork and Dependabot pull requests too. On a workstation, Docker pulls the image anonymously.

### Running a build in the image {-}

Example D.5 runs `press all` in the image from the top of the `alice` book repository on `hatter`, mounted at */book* (Chapter 2).

**Example D.5. Building the editions inside the toolchain image**

```text
$ cd ~/alice
$ docker run --rm -v "$PWD":/book \
    ghcr.io/clintecker/press-toolchain:latest \
    bash -c "pip install --break-system-packages \
    'press @ git+https://github.com/clintecker/press@v3' \
    && cd /book && press all"
...
```

Inside the image, `pip install` needs `--break-system-packages`, `--rm` removes the container afterward, and the artifacts stay in the mounted *dist/* (Chapter 2).

For a build that matches CI, replace `:latest` with the digest on the `image:` line of the press's *build.yml* at your book's tag, and install press at that tag (Chapters 2 and 14).

### The developer's render loop {-}

People who work on the press itself have *scripts/dev-render.sh*, which runs the checkout inside the pinned toolchain image (Chapter 2) and on macOS with Colima can mount a book only under `$HOME`.[^d-colima]

[^d-colima]: This limit is press issue #276. The script's default `--out` directory also lies inside the press checkout.

## What is untested {-}

The press states what it tests, and the earlier sections of this appendix cover that ground. Outside it, the press makes no claim, and neither does this book. Table D.2 lists the areas.

| Area | What the press says |
|----------------------|------------------------------------------------------|
| Windows | The press does not test Windows. |
| Other Linux distributions | The reference is Ubuntu 24.04. The press names no other distribution and tests none. |
| Other tool versions | The press tests the pandoc and TeX Live that came with Ubuntu 24.04, as the image freezes them. Homebrew moves forward on its own schedule, so a Mac may carry different releases from the image. |
| Python outside 3.10 to 3.14 | The doctor reports such a Python with `X.Y is outside the tested range 3.10 to 3.14 (see docs/COMPATIBILITY.md)`. |
| Installers other than pip | The install guide documents pip alone. Other installers, such as pipx, may work, because press is an ordinary command-line package. The press does not document or test them. |
| Build timings | The press documents only the first-run font scan. It states no number for how long a build takes. |

Table: Table D.2. What the press does not test

When a build on your workstation disagrees with a build in CI, trust CI. Then run the same target in the toolchain image, pinned by the same digest, to see the reference result on your own machine.
