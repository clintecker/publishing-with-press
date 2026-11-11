# Installing press

::: {.in-this-chapter}
> **In this chapter:**
>
> - What you need
> - Installing the Python package
> - The system toolchain
> - Running the doctor
> - The toolchain image
> - Apple Silicon and other platforms
> - The first run
:::

Press comes in two halves, and you install them separately. The first half is a Python package that gives you the `press` command. The second half is a set of programs that press calls to do the real typesetting and checking, and press does not install those for you. This chapter installs both halves on `hatter`, the workstation where `alice` writes her book. It then shows how to confirm that the machine can make books before you ask it to make one.

## What you need

A working press installation needs four things. You need a Python interpreter and the press package itself. You also need the *toolchain*, the outside programs that press runs on your behalf: pandoc, LuaLaTeX, latexmk, the fonts, epubcheck, and the poppler utilities. Finally, you need Git, because press uses it to give a new book its identity and because every book lives in a Git repository. You can skip the toolchain entirely if you would rather not install it. In its place, a container runtime pulls the press's own toolchain image, which this chapter describes later.

Table 2.1 lists the parts and what each one does for you. The rest of the chapter takes them in the order you install them.

| Part | Meaning |
|------|------------------------------------------------------------------|
| Python 3.10 or later | The package declares `requires-python = ">=3.10"`. The project tests 3.10 through 3.14. |
| The press package | It gives you the `press` command, and pip installs its three Python dependencies with it. |
| The toolchain | Pandoc, LuaLaTeX, latexmk, fonts, epubcheck, and poppler do the conversion, typesetting, and inspection. |
| Git | Press reads your identity from it when it creates a book, and your book lives in a Git repository. |
| A container runtime (optional) | It lets you run the toolchain image instead of installing the toolchain on your own machine. |

Table: Table 2.1. What a press installation needs

The Python requirement is a floor, and the tested range is a fact about the project's own testing. At the time of this writing, the continuous integration runs all five Python releases from 3.10 to 3.14 on Ubuntu, plus Python 3.12 on macOS 15. A newer Python may work, but no test proves it yet, and `press doctor` will say so when you run it.

The package has three runtime dependencies, and pip installs them for you. Pillow handles images, and pypdf reads the finished PDF so the verifiers can inspect it. The third, ruamel.yaml, reads every configuration file. Press uses ruamel.yaml as its one YAML library for two reasons. It reads YAML 1.2, so a bare `no`, `yes`, or `on` in your metadata stays a string.[^yaml] Its round-trip mode also keeps your comments when press writes a value back into one of your files.

Press is MIT-licensed. Its package metadata classifies it as "Development Status :: 4 - Beta", which is an honest label for a tool that still changes from one major version to the next.

You do not need any of this to look around. Three commands work with no book and no toolchain at all: `press --version`, `press --help`, and `press` followed by any command name and `--help`. All three exit with status 0. They are the right commands to run first on a new machine, and the right ones to paste into a support request.

## Installing the Python package

The press is not on PyPI. Its own install guide says so plainly: "the press is not published to PyPI, and nothing in its metadata should imply otherwise". A plain `pip install press` therefore finds nothing useful. Instead, you install press straight from its Git repository at a tag, and pip builds the package from that tag.

### From Git at a tag

The supported channel is pip with a Git URL. Example 2.1 shows `alice` installing the current major version on `hatter` and then asking the new command who it is.

**Example 2.1. Installing press from Git at the floating tag**

```
$ pip install "press @ git+https://github.com/clintecker/press@v3"
...
$ press --version
...
```

The quotation marks matter. The requirement contains a space and an `@`, and the shell would otherwise split it into pieces that pip cannot read.

The part after the last `@` is a tag, and press uses two kinds. A *floating tag* such as `v3` names a major version and moves forward to the newest compatible release within it. An *immutable tag* has three parts, such as `v3.0.2`, and names exactly one release forever. The press enforces that immutability at release time, so a three-part tag cannot quietly change under you. Within a major version, fixes may correct broken output, but they must not change the typography or layout of a valid book. A floating tag therefore gives you bug fixes without a redesign.

::: {.tip}
> **Tip:** Pin an immutable tag such as `v3.0.2` once a book goes to print. A reprint then builds with exactly the press that built the first printing, and a later fix cannot move a single line.
:::

### An editable install from a clone

Sometimes you want to read the press's source, follow its main branch, or test a fix before it reaches a tag. For that, clone the repository and install it in editable mode. An *editable install* points Python at the files in your clone, so a `git pull` changes the installed press with no reinstall. From the top of the clone, the command is `pip install -e .`, as the README gives it.

A book repository can also point at a clone that lives somewhere else. The `requirements.txt` file that press writes into every new book carries a comment that recommends this form for day-to-day book work. Example 2.2 shows the form, with `alice` keeping her clone of press under her home directory on `hatter`.

**Example 2.2. An editable install of a press clone**

```
$ git clone https://github.com/clintecker/press ~/src/press
...
$ cd ~/alice
$ pip install -e ~/src/press
...
```

An editable install trades stability for reach. You see every change on the branch you check out, the good ones and the bad ones alike. For a book that must build the same way next spring, prefer a tag.

### The extras

The package defines two optional groups of dependencies, which pip calls *extras*. The `tui` extra adds Textual, the library behind the desk, press's full-screen operator console. The install documentation spells the command `pip install 'press[tui]'`. Put the `[tui]` after the name `press` in whichever form of the requirement you use, the Git URL or a clone.

The `dev` extra exists for people who work on the press itself. It adds the linters, the type checker, and the test runner with its plugins. It also adds celebrimbor, the quality framework that gates every press change.[^dev] None of it belongs in a book's environment, and a book never needs it to build.

Table 2.2 collects the forms of installation and when each one fits.

| Form | When to use it |
|------|------------------------------------------------------------------|
| `pip install "press @ git+...@v3"` | Use it for most books. You receive fixes within the major version. |
| `pip install "press @ git+...@v3.0.2"` | Use it for a book in print. The press underneath it never changes. |
| `pip install -e .` in a clone | Use it to work on the press, or to try a fix before a release. |
| `pip install -e ~/src/press` from a book | Use it to track a clone while you write, as the scaffold's comment suggests. |
| The `tui` extra | Add it when you want the desk. |
| The toolchain image | Use it when you would rather not install the toolchain. The section "The toolchain image" later in this chapter gives the command. |

Table: Table 2.2. Ways to install press

Pip is the only installer the press documents. Other Python installers may well work, since press is an ordinary command-line package, but the project does not test them and this book does not describe them.

### Installing in continuous integration

A book's continuous integration does not use any of these commands. The composite action that a book's workflow calls installs press from the action's own checkout, never with pip from Git. That choice keeps a private book working without a token for a second repository, and it pins the installed press to the exact ref of the action. Chapter 14, *Continuous integration and the release contract*, covers the action in detail. For now, remember that the press on `printshop` and the press on `hatter` arrive by different roads, and that both roads start at the same tag.

## The system toolchain

The Python package is the smaller half of an installation. Press does not set type itself, and it does not validate an EPUB itself. It prepares the manuscript, decides what to build and in what order, and hands the work to older and specialized programs. Press calls each command that builds, checks, or verifies a *target*, and most targets call at least one of these programs.

@fig:tools-in-the-build shows where each tool sits. Pandoc reads every chapter file and runs the press's Lua filters over it. On the PDF branch, latexmk drives LuaLaTeX until the cross-references and lists settle. On the other branches, pandoc's own writers produce the EPUB and the HTML. The verifiers then use epubcheck and the poppler utilities to inspect the finished artifacts.

<!-- art: ARCHETYPE data-flow, top to bottom. Top: one dog-eared file icon labelled "the manuscript" with "book/chapters/*.md" in small monospace beneath it. A single arrow runs down to a rounded process box labelled "pandoc"; the arrow carries the label "Lua filters" in small sans. From the pandoc box three branches fan out downward. Left branch, labelled PDF: an arrow labelled `latexmk` in monospace to a rounded box "LuaLaTeX", then an arrow down to a dog-eared file icon "alice.pdf". Centre branch, labelled EPUB: an arrow labelled `pandoc` (EPUB writer) to a file icon "alice.epub". Right branch, labelled HTML: an arrow labelled `pandoc` (HTML writer) to a file icon labelled "reader site". Below the three file icons, the three branches converge on one rounded box drawn with a flat 2 pt drop shadow, labelled "verify". The arrows into it carry tool names in monospace: from the PDF file, `pdftoppm` and `pdffonts`; from the EPUB file, `epubcheck`. Every tool name appears in monospace on its arrow, never inside a box except pandoc and LuaLaTeX. The reader should see first that one manuscript enters at the top and every tool in the toolchain sits on a single arrow between it and the verify box. -->
![Where each tool in the toolchain sits in the build](assets/woodcuts/02-02-tools-in-the-build.png){#fig:tools-in-the-build .diagram width=full-measure fig-alt="A top-to-bottom flow: the manuscript passes through pandoc and its Lua filters, then splits into PDF, EPUB, and HTML branches. The PDF branch runs latexmk and LuaLaTeX, and all branches converge on a verify box reached by epubcheck, pdftoppm, and pdffonts."}

### The tools press requires

Press keeps an exact list of the programs it expects, with a purpose for each. Table 2.3 gives that list with each purpose in the words `press doctor` prints. Press requires eight of the tools. The other two are optional, and press builds books without them.

| Tool | Purpose, as the doctor prints it |
|------|------------------------------------------------------------------|
| `pandoc` | Every build target. Nothing builds without it. |
| `lualatex` | PDF and print builds. It is the TeX engine that sets the pages. |
| `latexmk` | PDF and print builds (multi-pass convergence). It reruns LuaLaTeX until the lists settle. |
| `pdftoppm` | PDF verification renders. It draws pages as images for inspection. |
| `pdffonts` | Font-embedding verification. It lists the fonts inside the PDF. |
| `pdfinfo` | PDF structure verification. It reads the document's structure for the verifier. |
| `pdftotext` | PDF text verification. It extracts the words so press can find them. |
| `git` | Scaffolding identity and book repositories. |
| `epubcheck` | The retail EPUB gate (softens to a warning locally). This tool is optional. |
| `claude` | The operator: press improve, research, aesthetic briefs. This tool is optional. |

Table: Table 2.3. External tools press checks for

Two of the entries need a word of explanation. The epubcheck program is the validator that retail ebook channels run on an EPUB before they accept it. Press runs the same program so you learn about a rejection before a retailer tells you. On your own machine, a missing epubcheck softens that gate to a warning. The `claude` command drives the *operator*, the targets such as `press improve` that hand work to an agent. You need it only for those targets, and Chapter 15, *The operator's desk and the editorial machines*, describes them.

The doctor also looks for a few things outside the table. It looks for `realesrgan`, the upscaler behind `press art enhance`, which is optional. It reports whether the `OPENAI_API_KEY` and `GEMINI_API_KEY` environment variables are set. It checks the Python version against the tested range, and it confirms that Pillow, pypdf, and ruamel.yaml import.

A few more programs help press without appearing in the doctor's report. Inside the toolchain image, `java` runs epubcheck. The `art enhance` target can use `oxipng` or `pngcrush` to shrink a PNG further, if either one is present. The press's own documentation Web site uses headless Chrome to check its layout, but a book never needs Chrome.

### Installing on macOS

On macOS, Homebrew supplies the whole toolchain. Example 2.3 shows the three commands from the press's install guide, with their comments.

**Example 2.3. Installing the toolchain on macOS**

```
$ brew install pandoc poppler
...
$ brew install --cask mactex-no-gui   # lualatex, latexmk, TeX Live
...
$ brew install epubcheck  # optional: the retail EPUB gate locally
...
```

The MacTeX cask is large, because it carries a full TeX Live distribution. That size has a benefit: TeX Live includes Libertinus, the typeface the house design uses for the PDF. In the install guide's words, "Fonts: TeX Live carries Libertinus for the PDF; nothing else to install."

The last command is optional, and we recommend it anyway. Without a local epubcheck, the retail gate softens to a warning on your machine. The gate still runs strictly in the toolchain image, so you will learn about an EPUB fault eventually, but you will learn about it later and somewhere else.

::: {.tip}
> **Tip:** Install epubcheck on your own machine. An EPUB fault that you see at your desk costs you a minute, and the same fault that you first see in CI costs you a round trip.
:::

### Installing on Debian and Ubuntu

On Debian and Ubuntu, the canonical package list is the press's own `Dockerfile`, because that file builds the toolchain image that every CI build uses. Example 2.4 shows the list as a single `apt-get` command.

**Example 2.4. Installing the toolchain on Debian or Ubuntu**

```
$ sudo apt-get install --no-install-recommends \
    make git pandoc python3 python3-pip poppler-utils \
    texlive-luatex texlive-latex-extra texlive-fonts-extra \
    fonts-linuxlibertine latexmk epubcheck
...
```

Most of these names explain themselves. The package `poppler-utils` holds the four poppler programs from Table 2.3. The package `texlive-latex-extra` holds lettrine, the LaTeX package behind the chapter opening's large initial. The package `texlive-fonts-extra` holds the `yinit` foliate initials that the `ornate` chapter-opening style uses.

The package `fonts-linuxlibertine` earned its place in the list the hard way. Ubuntu has no `fonts-libertinus` package, so the obvious name does not exist. The `--no-install-recommends` flag also drops the Libertine keyboard face, a font that a full install would pull in as a recommendation. The press found both facts during its first book, and the `Dockerfile` now names `fonts-linuxlibertine` explicitly.

::: {.warning}
> **Warning:** Do not drop `fonts-linuxlibertine` from the command because the TeX packages look like enough. With `--no-install-recommends`, nothing else in the list installs the Libertine keyboard face.
:::

Ubuntu's `epubcheck` package has one more trap, which appears only inside a container. The section "The toolchain image" later in this chapter explains it.

### Which versions

Press pins no version of pandoc or TeX Live by number. The press's compatibility guide states the rule: "the exact tool versions are whatever Ubuntu 24.04 shipped, frozen by the image digest". The toolchain image builds from Ubuntu 24.04, and its digest fixes the exact bytes. Ubuntu 24.04's pandoc and TeX Live are therefore the reference toolchain, and a book built in CI always uses them.

Your own machine may carry newer or older releases. Homebrew in particular moves forward on its own schedule. If a build on `hatter` disagrees with a build on `printshop`, trust `printshop`, because it ran the toolchain that proved the release. Then run the same build in the toolchain image on `hatter` to see the reference result at your own desk.

## Running the doctor

Once both halves are in place, ask press whether the machine is ready. The `press doctor` target checks every tool in Table 2.3, the extra items listed after it, and the Python environment. It prints one line for each check.

@fig:doctor-report shows the report from `hatter`. Most lines read `ok`. The `epubcheck` line reads `absent`, because `alice` did not install it. The `claude` line reads `BROKEN`, because on that run the command was present but could not execute. The final line names what stands between this machine and readiness.

<!-- art: ARCHETYPE terminal. A plain terminal window, grayscale, with a thin 0.5 pt box around it and no colour; a title bar reading "alice@hatter" in small sans; black monospace text on white, set at 72 columns, with long lines wrapping exactly as a terminal wraps them. The window holds a prompt line "$ press doctor" followed by this output, character for character:
press doctor
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
Then a fresh "$" prompt. No highlight, no bold, no colour anywhere; the state words in the bracketed gutter are the only emphasis the text carries. The reader should see first the column of bracketed states down the left, then the two lines that break it ("absent" and "BROKEN"), then the "not ready" line at the foot. -->
![The press doctor report on hatter](assets/woodcuts/02-01-doctor-report.png){#fig:doctor-report .diagram width=full-measure fig-alt="A terminal window on hatter showing press doctor output: fifteen lines with a bracketed state at the left, mostly ok, with epubcheck absent and claude broken, and a final line that reads not ready: claude."}

### Reading the report

Each line has three parts. A bracketed state comes first, set in a gutter seven characters wide so the states line up. The name of the tool or check comes next, and its purpose follows. For a tool that failed, the purpose begins with the reason, as the `claude` line shows.

Table 2.4 lists the states you will meet most often.

| State | Meaning |
|-------|------------------------------------------------------------------|
| `ok` | The tool is present and answers, or the check passed. |
| `absent` | An optional tool is missing. Press builds books without it, with the reduced behavior noted on its line. |
| `MISSING` | A required tool is missing. Press cannot build at least one target until you install it. |
| `BROKEN` | The tool is present but fails both `--version` and `-v` within 15 seconds. |
| `unset` | An environment variable such as `OPENAI_API_KEY` is not set. |

Table: Table 2.4. States in the doctor's report

The `BROKEN` state exists because a program can be present and still useless. The doctor does not stop at finding a file on your `PATH`. It runs the program with `--version`, then with `-v` if the first attempt fails, and it allows each attempt 15 seconds. The doctor calls a program that answers neither one broken, whatever `which` says about it. The section "The toolchain image" later in this chapter tells the story of the program that taught the press this distinction.

The two API key lines report only whether each variable is set. They name the command that reads each key, `press art commission`, with the model it selects. Neither key matters until you commission art, the subject of Chapter 11, *The art department*.

The two `python` lines close the report. The first compares your interpreter with the tested range. On a Python outside it, the line reads `X.Y is outside the tested range 3.10 to 3.14 (see docs/COMPATIBILITY.md)`, with your version in place of `X.Y`. The second line confirms that the three runtime dependencies import.

### The last line and the exit status

The report ends with a line of its own. On a ready machine, that line reads `this machine can make books`. Otherwise, it begins `not ready:`, names the tools at fault, and repeats the install commands for macOS and for Debian and Ubuntu. The doctor exits with status 0 when the machine is ready and 1 otherwise.

The exit status makes the doctor useful in scripts. A shell line such as `press doctor && press all` refuses to start a build on a machine that cannot finish it. Keep the doctor's own status in charge of that `&&`.

::: {.warning}
> **Warning:** Never pipe `press doctor` or any other check into `grep` before an `&&`. The pipeline then reports grep's exit status, not the check's, and a red check passes as green. The press shipped exactly that failure once, and the rule against it is now a scar.
:::

The doctor reports typed findings as well as printed lines. The desk reads the same findings and draws them as a panel, as Chapter 15 shows.

## The toolchain image

Installing the toolchain by hand works. The press also offers a second road, a ready-made Linux environment with every tool already in place. The *toolchain image* is `ghcr.io/clintecker/press-toolchain`, a container image built from the press's own `Dockerfile`. Every CI build of every book runs inside it.

### What the image holds

The image starts `FROM ubuntu:24.04` and sets one environment variable of its own, `PRESS_TOOLCHAIN=1`. Its package list is the list from Example 2.4, plus the GitHub command-line tool `gh`. It adds four things that a hand installation would not:

- a two-line wrapper at `/usr/local/bin/epubcheck` that runs the epubcheck jar with `java -jar`
- Real-ESRGAN and its upscaling models, on amd64 only
- `mesa-vulkan-drivers`, a software Vulkan for Real-ESRGAN to run on
- stylua and, on amd64, selene, the Lua tools that the press runs over its own filters

The variable `PRESS_TOOLCHAIN` tells press that it runs in the reference environment, and press keys its toolchain strictness on that variable. The press chose its own variable on purpose. The obvious choice, the ambient `CI` variable, has a trap: `CI=false` is truthy, because a check for a set variable finds the word `false` and counts it as set.

The epubcheck wrapper deserves its own warning, because it hides a failure that cost the first book real time.

::: {.warning}
> **Warning:** Do not trust Ubuntu's own `epubcheck` launcher inside a container. It needs binfmt_misc, which containers do not register, so the command exists, `which` finds it, and it dies with "Exec format error" only when it runs. Run the jar through `java -jar` instead, as the image's wrapper does.
:::

The press now reports a tool that is present but cannot run as a fault in the toolchain, not as a fault in your EPUB. That distinction is the reason the doctor has a `BROKEN` state. A missing validator and a broken validator call for different repairs, and neither one tells you anything about the book.[^binfmt]

### Pulling the image

The image is public. In the words of the press's documentation, "a book under any account pulls it with no package grant and no configured secret". On `hatter`, `docker` pulls it anonymously. On `printshop`, the reusable workflow authenticates the pull with the workflow's own `GITHUB_TOKEN`, which works for a public image, including on fork and Dependabot pull requests. Nobody has to grant your book access to anything.

The press publishes the image for two architectures, amd64 and arm64, and it tests each one before it pushes. Two kinds of tag point at it. The tag `:latest` follows the newest build. A tag of the form `:sha-` followed by a commit hash names the build from one commit of the press.

Neither tag is immutable, and a registry can move either one. The reusable workflow therefore pins the image by its `@sha256:` digest, a hash of the image's exact bytes. The release contract refuses a three-part press tag whose workflow names only a `sha-` tag. That digest is why a book pinned to `v3.0.2` builds with the same pandoc and the same TeX Live years from now.

### Building a book inside the image

You can run any target inside the image with Docker. Example 2.5 shows the form from the press's install guide, with `alice` building every edition of her book from its repository on `hatter`. The command mounts the book repository at `/book`, installs press inside the container, and runs `press all`.

**Example 2.5. Building every edition inside the toolchain image**

```
$ cd ~/alice
$ docker run --rm -v "$PWD":/book \
    ghcr.io/clintecker/press-toolchain:latest \
    bash -c "pip install --break-system-packages \
    'press @ git+https://github.com/clintecker/press@v3' \
    && cd /book && press all"
...
```

Two details in this command matter. Inside the image, `pip install` needs `--break-system-packages`, and the command fails without it. The `--rm` flag removes the container when the build ends. The artifacts stay behind in the *dist/* directory of your book repository, because that directory lives on the mounted volume.

The example uses `:latest`, which suits an experiment at your desk. When a local build must match CI exactly, use the digest that the reusable workflow names in place of `:latest`. Chapter 14 shows where to find it.

@fig:local-versus-container compares the two ways of building. On the left, `hatter` runs its own toolchain, which may lack epubcheck or one of the TeX packages the house design needs. On the right, the toolchain image carries everything at a pinned digest. The book repository sits between them, and either side can build from it.

<!-- art: ARCHETYPE topology. Three elements in a row, left to right. Left: a monitor icon labelled "hatter" in small sans, with "native toolchain" beneath it; under that, a small boxed list headed "may lack" in italic sans, listing in monospace, one per line: `epubcheck`, `wrapfig`, `lettrine`. Centre: a repository cylinder labelled "~/alice" in monospace, with "book repository" in small sans beneath it. Right: a plain box with a small crate icon, labelled "toolchain image" in small sans; inside the box, one line in small monospace: `ghcr.io/clintecker/press-toolchain@sha256:...`; beneath the box, in small sans, "Ubuntu 24.04, amd64 and arm64". Arrows: from the cylinder to the monitor, labelled "chapters and config"; from the monitor back to the cylinder, labelled "dist/"; from the crate box to the cylinder, labelled "mounted at /book" (a two-headed arrow, since the container reads the manuscript and writes dist/ through the same mount); a dashed arrow from the right edge into the crate box labelled "docker pull (anonymous)". Square corners for the cylinder's label box, rounded corners for the two machines. The reader should see first that the same repository feeds both machines, and that only the right-hand one carries a pinned digest. -->
![Building on the workstation versus building in the toolchain image](assets/woodcuts/02-03-local-versus-container.png){#fig:local-versus-container .diagram width=full-measure fig-alt="A topology diagram: the workstation hatter, which may lack epubcheck, wrapfig, and lettrine, and the toolchain image, pinned by an sha256 digest, both read the same book repository and write dist back into it."}

## Apple Silicon and other platforms

Apple Silicon is the maintainer's primary platform, and the Homebrew route in Example 2.3 is the one the install guide gives for it. The project's own continuous integration also runs Python 3.12 on macOS 15, so the Python half of press has a tested record on the Mac.[^macos]

Local container builds on Apple Silicon work too, because the press publishes an arm64 build of the toolchain image. The press's own full verification script, `scripts/verify.sh --full`, also runs natively on Apple Silicon for the same reason, so contributors to the press need no emulation either.

The arm64 image differs from the amd64 image in one respect. Real-ESRGAN publishes no arm64 binary, so the arm64 image carries no upscaler. On arm64, `press art enhance` resamples a plate instead of upscaling it. If you want the upscaled result, run that one target on an amd64 machine or in the amd64 image.

On Linux, the supported route is Debian or Ubuntu with the package list from Example 2.4, or the toolchain image on either architecture. CI runs every tested Python release on Ubuntu, and the image itself is Ubuntu 24.04, so Ubuntu has the strongest record of any platform.

Windows is not tested.

## The first run

With the package installed, the toolchain in place, and the doctor satisfied, you are ready to build. The procedure for a first run on a new machine is short.

To confirm a new installation:

1. Ask press for its version:
   `$ press --version`
2. Ask the doctor for its report, and read every line that is not `ok`:
   `$ press doctor`
3. Create a book, or change into an existing book repository:
   `$ cd ~/alice`
4. Build every edition and run every verifier:
   `$ press all`

Chapter 3, *The shape of a book repository*, explains how to create a new book with `press new`, and Chapter 7, *Building the editions*, explains what `press all` builds. For this chapter, the interesting part is what happens during step 4 on a machine that has never run LuaLaTeX before.

### The font scan

The first LuaLaTeX run on a fresh machine starts with a scan of every font the system can see. The scan takes several minutes, and during those minutes the build prints little or nothing. To a reasonable person watching the terminal, it looks exactly like a hang. It is not a hang, although it is a very convincing imitation of one.

::: {.sidebar}
> **The hang that isn't**
>
> The first time LuaLaTeX runs on a fresh machine, it scans the fonts before it sets a single page. The scan takes several minutes. During those minutes the build prints little, and the terminal sits still while the processor works.
>
> Every instinct a programmer has says that the build is stuck. In most programs, a build that prints nothing for minutes will print nothing ever again. The natural response is to interrupt it, start over, and watch the second attempt sit just as still.
>
> The press met this on its first book. It went into the press's scars list in two flat sentences: "First LuaLaTeX run on a fresh machine triggers a several-minute font scan that looks like a hang. It is not a hang." The quick start and the install guide both repeat the warning.
>
> The remedy is patience. Start the first build, make a cup of tea, and come back to a machine that is past its scan and at work on your book.
:::
The scan belongs to LuaLaTeX, and press does not hurry it. The press's documentation describes no other build timing, and this book does not invent one. A build that stays silent for several minutes on a fresh machine is almost certainly the scan, and the right response is to wait for it.

### After the first build

By the time `press all` finishes, the verifiers inspected each artifact as an object, the way a reader or a retailer will meet it. A green result on the first run tells you that the whole installation works together. No single `--version` can tell you that much. A red result means one verifier refused an artifact, and Chapter 8, *Verifying the artifacts*, explains how to read the refusal.

If the only complaint concerns epubcheck, you have two choices. Install it with Homebrew or apt as Examples 2.3 and 2.4 show, or accept the local warning and let the toolchain image run the strict gate. Either way, rerun `press doctor` after you change the toolchain. The report on your screen then describes the machine you actually have.

::: {.tip}
> **Tip:** Run `press doctor` again after every change to the toolchain, including a Homebrew upgrade. The report costs a few seconds, and it is the quickest way to learn that an upgrade broke a tool.
:::

The next chapter, *The shape of a book repository*, creates the `alice` book with `press new` and walks through every file it makes.

[^yaml]: YAML 1.1, the older revision that many libraries still read, treats those bare words as booleans. A metadata value of `no` would then arrive as false, which is a poor fate for a word in a title.

[^dev]: Celebrimbor is a development and CI dependency only. It is never a runtime dependency of a book, and it installs only on Python 3.11 or later.

[^binfmt]: The `Dockerfile`'s comment on Real-ESRGAN refers to the same trap as "the epubcheck/binfmt scar", so the lesson reached a second tool.

[^macos]: The macOS job once ran on `macos-14`. GitHub retired that runner partway through a release, and it cancelled every job there within a second with "configuration not supported". The job moved to `macos-15`.

<!-- index: press doctor; toolchain; toolchain image; pip; editable install; floating tag; immutable tag; extras; tui extra; pandoc; LuaLaTeX; latexmk; epubcheck; binfmt_misc; poppler; fonts-linuxlibertine; Libertinus; Homebrew; MacTeX; Apple Silicon; arm64; Real-ESRGAN; PRESS_TOOLCHAIN; font scan; exit status -->
