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

A working press installation needs four things. You need a Python interpreter and the press package itself. You also need the *toolchain*, the outside programs that press runs on your behalf: pandoc, LuaLaTeX, latexmk, the fonts, epubcheck, and the poppler utilities. Finally, you need Git, because press uses it to give a new book its identity and because every book lives in a Git repository. If you would rather not install the toolchain, you can skip it entirely. In its place, a container runtime pulls the *toolchain image*, a container image of the whole toolchain that the press builds and publishes.

Table 2.1 lists the parts and what each one does for you.

| Part | Meaning |
|------------------------------|--------------------------------------------------|
| Python 3.10 or later | The package declares `requires-python = ">=3.10"`. The press tests 3.10 through 3.14. |
| The press package | It gives you the `press` command, and pip installs its three Python dependencies with it. |
| The toolchain | Pandoc, LuaLaTeX, latexmk, fonts, epubcheck, and poppler do the conversion, typesetting, and inspection. |
| Git | Press reads your identity from it when it creates a book, and a book normally lives in a Git repository. |
| A container runtime (optional) | It lets you run the toolchain image instead of installing the toolchain on your own machine. |

Table: Table 2.1. What a press installation needs

The Python requirement is a floor. The tested range records only what the press's own tests run. At the time of this writing, the press's continuous integration (CI) runs all five Python releases from 3.10 to 3.14 on Ubuntu, plus Python 3.12 on macOS 15. A newer Python may work, but no test proves it yet. When you run `press doctor` on one, it says so.

The package has three runtime dependencies, and pip installs them for you. Pillow handles images, and pypdf reads the finished PDF so the verifiers can inspect it. The third, ruamel.yaml, reads every configuration file. Press uses ruamel.yaml as its one YAML library for two reasons. First, it reads YAML 1.2, so a bare `no`, `yes`, or `on` in your metadata stays a string.[^2-yaml] Second, its round-trip mode keeps your comments when press writes a value back into one of your files.

[^2-yaml]: YAML 1.1, the older revision of the language, treats those bare words as booleans. A metadata value of `no` would then arrive as false, which is a poor fate for a word in a title.

You do not need any of this to look around. Three commands work with no book and no toolchain at all: `press --version`, `press --help`, and `press` followed by any command name and `--help`. All three exit with status 0, so they are the right commands to run first on a new machine.

## Installing the Python package

The press is not on PyPI. Its install guide says: "Pip-from-git at a tag is the supported installation channel; the press is not published to PyPI". A plain `pip install press` does not install this press. Instead, you install press straight from its Git repository at a tag, and pip builds the package from that tag.

### Choosing where the package goes

Before you install anything, decide where the package will live. We recommend a virtual environment of its own, for a reason that belongs to Python and not to press. On Ubuntu 24.04, and with a Homebrew Python on macOS, the system Python refuses a bare `pip install` into its own site-packages directory. That rule comes from Python's packaging standards (PEP 668). The press's install guide does not mention virtual environments at all, so this advice is ours.

A virtual environment is a private directory with its own `pip` and its own `press`. Nothing you install there touches the system Python, and you can delete the directory to start over. Example 2.1 creates one at *~/.press-venv* on `hatter` and installs press into it.

### From Git at a tag

The supported channel is pip with a Git URL. In Example 2.1, `alice` creates the environment, activates it, installs the current major version, and asks the new command who it is.

On Debian and Ubuntu, the `venv` module comes in a separate package, `python3-venv`, which the press's package list does not include. Without it, `python3 -m venv` fails with a message that tells you to install it. We therefore add one package to the press's list for this book's advice:

```text
$ sudo apt-get install python3-venv
```

**Example 2.1. Installing press into a virtual environment**

```text
$ python3 -m venv ~/.press-venv
$ . ~/.press-venv/bin/activate
$ pip install \
    "press @ git+https://github.com/clintecker/press@v3"
...
$ press --version
...
```

The quotation marks matter. The requirement contains spaces, so the shell would otherwise split it into pieces that pip cannot read. Once the environment is active, `pip` and `press` both mean the copies inside *~/.press-venv*. In a new terminal, run the activation line again, or call the commands by their full paths, such as *~/.press-venv/bin/press*.

The part after the last `@` is a tag, and press uses two kinds. A *floating tag* such as `v3` names a major version and moves forward to the newest compatible release within it. An *immutable tag* has three parts, such as `v3.0.2`, and names exactly one release forever.

The press enforces that immutability at release time, so a three-part tag cannot quietly change under you. Within a major version, fixes may correct broken output, but they must not change the typography or layout of a valid book. A floating tag therefore gives you bug fixes without a redesign. The toolchain image carries the same idea one level down, as the section "The toolchain image" later in this chapter shows.

::: {.tip}
> **Tip:** Pin an immutable tag such as `v3.0.2` once a book goes to print. A reprint then builds with exactly the press that built the first printing, and a later fix cannot move a single line.
:::

### An editable install from a clone

Sometimes you want to read the press's source, follow its main branch, or test a fix before it reaches a tag. For that, clone the repository and install it in editable mode. An *editable install* points Python at the files in your clone, so a `git pull` changes the installed press with no reinstall. From the top of the clone, the command is `pip install -e .`, as the README gives it.

You can also install a clone that lives somewhere else by naming its path. The *requirements.txt* file that press writes into every new book carries a comment that recommends this form for day-to-day book work. In Example 2.2, `alice` keeps her clone of press under her home directory on `hatter` and installs it into the active environment.

**Example 2.2. An editable install of a press clone**

```text
$ git clone https://github.com/clintecker/press ~/src/press
...
$ pip install -e ~/src/press
...
```

An editable install follows whatever branch you check out, the good commits and the bad ones alike. For a book that must build the same way next spring, prefer a tag.

### The extras

The package defines two optional groups of dependencies, which pip calls *extras*. The `tui` extra adds Textual, the library that *the desk* needs. The desk is `press desk`, press's full-screen console in the terminal. The extra goes in square brackets after the package name, in pip's standard syntax. Example 2.3 shows it in both install forms, the Git URL and the editable clone.

**Example 2.3. Installing press with the tui extra**

```text
$ pip install \
    "press[tui] @ git+https://github.com/clintecker/press@v3"
...
$ pip install -e "$HOME/src/press[tui]"
...
```

In the second form the brackets follow the path, not the word `press`, because there the path names the package. The double quotes keep the shell from reading the brackets as a pattern, and they still let it expand `$HOME`.

The `dev` extra exists for people who work on the press itself. It adds the linters, the type checker, and the test runner with its plugins. It also adds celebrimbor, the press's quality framework.[^2-dev] None of it belongs in a book's environment, and a book never needs it to build.

[^2-dev]: Celebrimbor is a development and CI dependency only. It is never a runtime dependency of a book, and it installs only on Python 3.11 or later.

Table 2.2 collects the forms of installation and when each one fits.

| Form | When to use it |
|--------------------------------------------|------------------------------------------------|
| `pip install "press @ git+...@v3"` | Use it for most books. You receive fixes within the major version. |
| `pip install "press @ git+...@v3.0.2"` | Use it for a book in print. The press underneath it never changes. |
| `pip install -e .` in a clone | Use it to work on the press, or to try a fix before a release. |
| `pip install -e ~/src/press` | Use it to track a clone while you write, as the scaffold's comment suggests. |
| `press[tui]` in either form | Use it when you want the desk. |

Table: Table 2.2. Ways to install press

To take a new release on your workstation, run `pip install --upgrade "press @ git+https://github.com/clintecker/press@v3"`. The floating tag moves on GitHub, not in your environment.

### Installing in continuous integration

A book's CI does not use any of these commands. The *composite action*, the piece of the press that the reusable workflow runs to install it, installs press from the action's own checkout, never with pip from Git. That choice keeps a private book working without a token for a second repository, and it pins the installed press to the exact ref of the action. Chapter 14, *Continuous integration and the release contract*, covers the action in detail. The press on `printshop` and the press on `hatter` arrive by different roads, but both roads can start at the same tag.

## The system toolchain

The Python package is the smaller half of an installation. Press prepares the manuscript, decides what to build and in what order, and hands the work to older, specialized programs. It sets no type itself, and it checks no EPUB against the retail rules itself. A *target* is a press command that builds, checks, or verifies something, and most targets call at least one of these programs.

@fig:tools-in-the-build shows where each tool sits. Pandoc reads every chapter file and runs the press's Lua filters over it. On the PDF branch, latexmk reruns LuaLaTeX until the cross-references and lists stop changing. On the other branches, pandoc's own writers produce the EPUB and the HTML. The verifiers then use epubcheck and the poppler utilities to inspect the finished artifacts.

![Where each tool in the toolchain sits in the build](assets/woodcuts/02-01-tools-in-the-build.png){#fig:tools-in-the-build .diagram width=full-measure fig-alt="A top-to-bottom flow: the manuscript passes through pandoc and its Lua filters, then splits into PDF, EPUB, and HTML branches that converge on a verify box reached by epubcheck, pdftoppm, and pdffonts."}

<!-- art: ARCHETYPE data-flow, top to bottom. Top: a dog-eared file icon, "the manuscript", with "book/chapters/*.md" in small monospace beneath. An arrow labeled "Lua filters" runs down to a rounded box, "pandoc". Three branches fan out below it. Left, PDF: an arrow labeled `latexmk` to a rounded box "LuaLaTeX", then down to a file icon "alice.pdf". Center, EPUB: an arrow labeled `pandoc` to a file icon "alice.epub". Right, HTML: an arrow labeled `pandoc` to a file icon "reader site". The branches converge on a rounded box with a 2 pt drop shadow, "verify". Its incoming arrows carry `pdftoppm` and `pdffonts` from the PDF and `epubcheck` from the EPUB. Tool names sit in monospace on arrows. The reader should see first one manuscript entering at the top, with each tool on an arrow. -->

### The tools press requires

Press keeps an exact list of the programs it expects, with a purpose for each. Table 2.3 gives that list, with each purpose exactly as `press doctor` prints it. Press requires the first eight tools. The last two are optional, and press builds books without them.

| Tool | What the doctor prints |
|------------------------|--------------------------------------------------------|
| `pandoc` (required) | `every build target` |
| `lualatex` (required) | `PDF and print builds` |
| `latexmk` (required) | `PDF and print builds (multi-pass convergence)` |
| `pdftoppm` (required) | `PDF verification renders` |
| `pdffonts` (required) | `font-embedding verification` |
| `pdfinfo` (required) | `PDF structure verification` |
| `pdftotext` (required) | `PDF text verification` |
| `git` (required) | `scaffolding identity and book repositories` |
| `epubcheck` (optional) | `the retail EPUB gate (softens to a warning locally)` |
| `claude` (optional) | `the operator: press improve, research, aesthetic briefs` |

Table: Table 2.3. External tools press checks for

Two of the entries need a word of explanation. The epubcheck program is the program that retail e-book channels run on an EPUB before they accept it. Press runs the same program so you learn about a rejection before a retailer tells you. On your own machine, a missing epubcheck softens that gate to a warning. The `claude` command drives the *operator*, the commands such as `press improve` that hand work to an agent. You need it only for those commands, and Chapter 15, *The operator's desk and the editorial machines*, describes them.

The doctor also looks for a few things outside the table. It looks for `realesrgan`, the optional upscaler behind `press art enhance`. It reports whether the `OPENAI_API_KEY` and `GEMINI_API_KEY` environment variables are set. It checks the Python version against the tested range, and it confirms that Pillow, pypdf, and ruamel.yaml import.

A few more programs help press without appearing in the doctor's report. The poppler utilities include `pdfimages`, which the doctor does not check. If `pdfimages` is absent, two checks soften to notes. Inside the toolchain image, `java` runs epubcheck. If `oxipng` or `pngcrush` is present, the `art enhance` target can use it to shrink a PNG further.

### Installing on macOS

On macOS, Homebrew supplies the whole toolchain. Example 2.4 shows the three commands from the press's install guide. The guide's comments say that the MacTeX cask brings lualatex, latexmk, and TeX Live, and that the epubcheck formula is "optional: the retail EPUB gate locally".

**Example 2.4. Installing the toolchain on macOS**

```text
$ brew install pandoc poppler
...
$ brew install --cask mactex-no-gui
...
$ brew install epubcheck
...
```

The MacTeX cask carries TeX Live, and TeX Live includes Libertinus, the typeface of the house PDF. In the install guide's words, "Fonts: TeX Live carries Libertinus for the PDF; nothing else to install."

The last command is optional, and we recommend it anyway. Without a local epubcheck, the retail gate softens to a warning on your machine. The install guide puts the benefit the other way round: a local epubcheck "hardens the EPUB gate before push; CI always runs it regardless." You will learn about an EPUB fault eventually, but without a local epubcheck you learn later and somewhere else. An EPUB fault that you see on your own machine costs you a minute, and the same fault that you first see in CI costs you a round trip.

### Installing on Debian and Ubuntu

On Debian and Ubuntu, the reference package list is the press's own *Dockerfile*, because that file builds the toolchain image that every CI build uses. Example 2.5 shows the list as a single `apt-get` command.

::: {.warning}
> **Warning:** Do not drop `fonts-linuxlibertine` from the command because the TeX packages look like enough. With `--no-install-recommends`, nothing else in the list installs the Libertine keyboard face.
:::

**Example 2.5. Installing the toolchain on Debian or Ubuntu**

```text
$ sudo apt-get install --no-install-recommends \
    make git pandoc python3 python3-pip poppler-utils \
    texlive-luatex texlive-latex-extra texlive-fonts-extra \
    fonts-linuxlibertine latexmk epubcheck
...
```

Most of these names explain themselves. The package `poppler-utils` holds the four poppler programs from Table 2.3. The package `texlive-latex-extra` holds lettrine, the LaTeX package that sets the large first letter of each chapter opening. The package `texlive-fonts-extra` holds the `yinit` foliate initials that the `ornate` chapter-opening style uses.

The package `fonts-linuxlibertine` is a scar. Ubuntu has no `fonts-libertinus` package, so the obvious name does not exist. The `--no-install-recommends` flag also drops the Libertine keyboard face. The press records both facts in its scars list, and the *Dockerfile* now names `fonts-linuxlibertine` explicitly.

Ubuntu's `epubcheck` package has one more trap, which appears only inside a container. The section "The toolchain image" later in this chapter explains it.

### Which versions

Press pins no version of pandoc or TeX Live by number. The press's compatibility guide states the rule: "the exact tool versions are whatever Ubuntu 24.04 shipped, frozen by the image digest". The toolchain image builds from Ubuntu 24.04, and its digest fixes the exact bytes. Ubuntu 24.04's pandoc and TeX Live are therefore the reference toolchain, and a book built in CI always uses them.

Your own machine may carry newer or older releases, and Homebrew moves forward on its own schedule. If a build on `hatter` disagrees with a build on `printshop`, trust `printshop`. It runs the same toolchain image, pinned by the same digest, that the press's *release contract*, the workflow that proves each press tag, proved. Then run the same build in the toolchain image on `hatter` to see the reference result on your own machine.

## Running the doctor

Once both halves are in place, ask press whether the machine is ready. The `press doctor` command checks every tool in Table 2.3, the extra items listed after it, and the Python environment. It prints one line for each check.

@fig:doctor-report shows the report from `hatter`. Most lines read `ok`. The `epubcheck` line reads `absent`, because `alice` did not install it. The `claude` line reads `BROKEN`, because on that run the command was present but could not run. The final line names the tool that keeps this machine from being ready.

![The press doctor report on hatter](assets/woodcuts/02-02-doctor-report.png){#fig:doctor-report .diagram width=full-measure fig-alt="A terminal window on hatter showing press doctor output: fifteen lines with a bracketed state at the left, mostly ok, with epubcheck absent and claude broken, and a final line that reads not ready: claude."}

<!-- art: ARCHETYPE terminal. A plain grayscale terminal window, thin 0.5 pt box, title bar "alice@hatter" in small sans, black monospace on white at 72 columns, long lines wrapped as a terminal wraps them. It shows the prompt line "$ press doctor", then the capture given under "Figure notes, Figure 2.2" in docs/briefs/reports/report-02.md, character for character, then a fresh "$" prompt. No bold, no color. The reader should see first the bracketed state column, then the absent and BROKEN lines, then the "not ready" line at the foot. -->

### Reading the report

Each line has three parts. A bracketed state comes first, set in a gutter seven characters wide so the states line up. The name of the tool or check comes next, and its purpose follows. For a broken tool, the purpose begins with the reason, as the `claude` line shows.

Table 2.4 lists the states you will meet most often.

| State | Meaning |
|----------------|--------------------------------------------------------|
| `ok` | The tool is present and answers, or the check passed. |
| `absent` | An optional tool is missing. Press builds books without it. |
| `MISSING` | A required tool is missing. Press cannot build at least one target until you install it. |
| `BROKEN` | The tool is present but fails both `--version` and `-v` within 15 s. |
| `unset` | An environment variable such as `OPENAI_API_KEY` is not set. |

Table: Table 2.4. States in the doctor's report

The `BROKEN` state catches a program that is present and still useless. The doctor does not stop at finding a file on your `PATH`. A tool that fails both probes counts as broken, whatever `which` says about it. The section "The toolchain image" later in this chapter tells the story of a program that exists and still cannot run.

The two API key lines report only whether each variable is set. They name the command that reads each key, `press art commission`, with the model it selects. Neither key matters until you generate art, the subject of Chapter 11, *The art department*.

The two `python` lines close the report. The first compares your interpreter with the tested range. On a Python outside it, the line reads `X.Y is outside the tested range 3.10 to 3.14 (see docs/COMPATIBILITY.md)`, with your version in place of `X.Y`. The second line confirms that the three runtime dependencies import.

### The last line and the exit status

The report ends with a line of its own. On a ready machine, that line reads `this machine can make books`. Otherwise, it begins `not ready:` and names the tools at fault. It then gives an install hint for macOS (`brew install pandoc mactex-no-gui poppler`) and, for Debian and Ubuntu, a pointer to the *Dockerfile*'s package list. The doctor exits with status 0 when the machine is ready and 1 otherwise.

A broken tool keeps the doctor from reporting the machine ready, even when the tool is optional. @fig:doctor-report shows the case: `claude` is optional, `press all` does not need it, and the doctor still reports `not ready: claude` and exits 1. The exit status therefore says less than the report does. Read the report itself, and do not chain a build on the doctor's exit status. To clear a broken optional tool, repair it or take it off your `PATH`.

::: {.warning}
> **Warning:** Never pipe `press doctor` or any other check into `grep` before an `&&` in a commit chain. The pipeline then reports grep's exit status, and the press's scars list records the result: "a red check once shipped as green."
:::

The doctor reports typed findings as well as printed lines. The desk reads the same findings and draws them as a panel, as Chapter 15 shows.

## The toolchain image

Installing the toolchain by hand works. The press also offers a second road, a ready-made Linux environment with every tool already in place. The toolchain image is `ghcr.io/clintecker/press-toolchain`, a container image that the press builds from its own *Dockerfile*. Every CI build of every book runs inside it.

### What the image holds

The image starts `FROM ubuntu:24.04` and sets one environment variable of its own, `PRESS_TOOLCHAIN=1`. Its package list is the list from Example 2.5, plus the GitHub command-line tool `gh`. Among other things, it adds these to a hand installation:

- a two-line wrapper at */usr/local/bin/epubcheck* that runs the epubcheck jar with `java -jar`
- Real-ESRGAN and its upscaling models, on amd64 only
- `mesa-vulkan-drivers`, a software Vulkan for Real-ESRGAN to run on
- stylua and, on amd64, selene, the Lua tools that the press runs over its own filters

The variable `PRESS_TOOLCHAIN` tells press that it runs in the reference environment. Press decides how strict its toolchain checks are from that variable. The press chose its own variable instead of the ambient `CI` (Chapter 8 says why).

The epubcheck wrapper deserves its own warning, because the Ubuntu launcher it replaces hides a failure.

::: {.warning}
> **Warning:** Do not trust Ubuntu's own `epubcheck` launcher inside a container. It needs binfmt_misc, which containers do not register. The command exists and `which` finds it, but it dies with "Exec format error" only when it runs. Run the jar through `java -jar` instead, as the image's wrapper does.
:::

The press's verifier draws the same line the doctor draws. It reports a present-but-unrunnable tool as a fault in the toolchain, not as a fault in your EPUB. A missing epubcheck and a broken epubcheck call for different repairs, and neither one tells you anything about the book.[^2-binfmt]

[^2-binfmt]: The *Dockerfile*'s comment on Real-ESRGAN refers to the same trap as "the epubcheck/binfmt scar", so the scar reached a second tool.

### Pulling the image

The image is public. In the words of the press's documentation, "a book under any account pulls it with no package grant and no configured secret". On `hatter`, `docker` pulls it anonymously. On `printshop`, the *reusable workflow*, the workflow file a book's CI calls, authenticates the pull with the workflow's own `GITHUB_TOKEN`. That token works for a public image, on fork and Dependabot pull requests as well.

The press publishes the image for two architectures, amd64 and arm64, and it tests each one before it pushes. Two kinds of tag point at it. The tag `:latest` follows the newest build. A tag of the form `:sha-` followed by a commit hash names the build from one commit of the press.

Neither tag is immutable, and the registry can move either one. The reusable workflow therefore pins the image by its `@sha256:` digest, a hash of the image's exact bytes. The release contract refuses a three-part tag whose workflow names only a `sha-` tag. That digest is why a book pinned to `v3.0.2` builds with the same pandoc and the same TeX Live years from now.

### Building a book inside the image

You can run any target inside the image with Docker. Example 2.6 shows the form from the press's install guide. In it, `alice` builds her book's editions from the top of its book repository on `hatter`, which Chapter 3 creates. The command mounts the book repository at `/book`, installs press inside the container, and runs `press all`.

**Example 2.6. Building the editions inside the toolchain image**

```text
$ cd ~/alice
$ docker run --rm -v "$PWD":/book \
    ghcr.io/clintecker/press-toolchain:latest \
    bash -c "pip install --break-system-packages \
    'press @ git+https://github.com/clintecker/press@v3' \
    && cd /book && press all"
...
```

Two details in this command matter. Inside the image, `pip install` needs `--break-system-packages`, because Ubuntu manages the image's Python and it refuses a bare install. The `--rm` flag removes the container when the build ends. The artifacts stay behind in the *dist/* directory of your book repository, because that directory lives on the mounted volume.

The example uses `:latest`, which suits an experiment on your own machine. When a local build must match CI exactly, replace `:latest` with the digest that the reusable workflow names. Then install the same three-part press tag that the book pins. Chapter 14 shows where to find the digest.

@fig:local-versus-container compares the two ways of building. On the left, `hatter` runs its own toolchain, which may lack epubcheck or the Java to run it. On the right, the toolchain image carries everything at a pinned digest. The book repository sits between them, and either side can build from it.

![Building on the workstation versus building in the toolchain image](assets/woodcuts/02-03-local-versus-container.png){#fig:local-versus-container .diagram width=full-measure fig-alt="A topology diagram: the workstation hatter, which may lack epubcheck and Java, and the toolchain image, pinned by an sha256 digest, both read the same book repository and write dist back into it."}

<!-- art: ARCHETYPE topology, three elements left to right. Left: a monitor icon, "hatter", with "native toolchain" beneath, and a small boxed list headed "may lack" in italic sans: `epubcheck`, `java` (one per line, monospace). Center: a repository cylinder, "~/alice" in monospace, "book repository" beneath. Right: a plain box with a small crate icon, "toolchain image", holding one monospace line `ghcr.io/clintecker/press-toolchain@sha256:...`, with "Ubuntu 24.04, amd64 and arm64" beneath. Arrows: cylinder to monitor, "chapters and config"; monitor to cylinder, "dist/"; crate to cylinder, two-headed, "mounted at /book"; a dashed arrow into the crate, "docker pull (anonymous)". The reader should see first that one repository feeds both machines, and only the right one carries a pinned digest. -->

### The developer's render loop

People who work on the press itself have one more way to use the image. The press checkout carries *scripts/dev-render.sh*, which builds a book on the exact bytes CI builds on. It runs press against a book inside the pinned toolchain image. It reads the toolchain image from the press's *build.yml*, so it always runs the same image the release contract pins.

The script mounts the press checkout read-only and runs `python -m press` straight from its *src/* directory. An edit to the press's source therefore takes effect on the next run with no reinstall. With no arguments, it builds the PDF of the press's own three-chapter Alice example. You can name other targets, such as `pdf epub web all`, and choose a book with `--book DIR`. The option `--out DIR` names the host directory for the artifacts, and the default is *build/dev-render*. After a PDF build, `--preview` rasterizes the pages to JPEG previews, and `--shell` opens a shell in the container instead of building.

The script lives in the press checkout, not in a book, and a book author never needs it. The press's own notes call it "the edit-render-look loop, not the proof", and `scripts/verify.sh --full` remains the gate before a press tag.

## Apple Silicon and other platforms

Apple Silicon is the maintainer's primary platform, and the macOS route in Example 2.4 serves it. The press's own CI also runs Python 3.12 on macOS 15, so the Python half of press has a tested record on the Mac.

Local container builds on Apple Silicon work too, because the press publishes an arm64 build of the toolchain image. The press's own full verification script, `scripts/verify.sh --full`, also runs natively on Apple Silicon for the same reason.

The arm64 image differs from the amd64 image in one respect. Real-ESRGAN publishes no upstream arm64 binary, so the arm64 image carries no upscaler. In the arm64 image, `press art enhance` resamples a plate instead of upscaling it.

The install guide states the supported platforms: "Supported platforms are Linux (the container's Ubuntu 24.04 is the reference) and macOS." On Linux, the route is Debian or Ubuntu with the package list from Example 2.5, or the toolchain image on either architecture. CI runs every tested Python release on Ubuntu, and the image itself is Ubuntu 24.04. Ubuntu therefore has the strongest record of any platform.

Outside those routes, the press makes no claim. It does not test Windows. It does not test a Python newer than 3.14, or a pandoc and TeX Live other than Ubuntu 24.04's. Pip is the only installer the press documents. Other Python installers may work, because press is an ordinary command-line package, but the press does not test them. The toolchain image is the one route whose exact bytes the press proves on every release.

## The first run

With the package installed, the toolchain in place, and the doctor's report read, confirm the installation before you make a book. Example 2.7 shows the two commands on `hatter`, after `alice` installed epubcheck and repaired `claude`. The last command prints the doctor's exit status.

**Example 2.7. Confirming a new installation**

```text
$ press --version
...
$ press doctor
...
this machine can make books
$ echo $?
0
```

The ready line and the status 0 together mean that no required tool is missing and no tool is broken. A machine in that state can build a book. It needs a book to build, and Chapter 3, *The shape of a book repository*, makes one.

### The font scan

On a machine where LuaLaTeX runs for the first time, the first PDF build holds a surprise.

::: {.sidebar}
> **The first-run font scan**
>
> The first LuaLaTeX run on a fresh machine starts with a font scan, and the scan lasts several minutes. Nothing about it looks like progress. It looks like a hang, and every instinct a programmer has says to interrupt the build and start over.
>
> Do not interrupt it. The press's scars list records the behavior: "First LuaLaTeX run on a fresh machine triggers a several-minute font scan that looks like a hang. It is not a hang." The quick start and the install guide both repeat the warning, so a new author meets it before the first build.
>
> Start the first build, make a cup of tea, and come back to a machine that is past its scan and at work on your book.
:::

### After the first build

Before `press all` finishes, the verifiers inspect each artifact as an object, the way a reader or a retailer will meet it. A green result on the first run tells you that the whole installation works together. No single `--version` can tell you that much. A red result means that a check or a verifier failed. Chapter 8, *Verifying the artifacts*, explains how to read the failure. Chapter 7, *Building the editions*, explains what `press all` builds, and the print interior and cover wrap are separate targets.

If the only complaint concerns epubcheck, you have two choices. Install it with Homebrew or apt as Examples 2.4 and 2.5 show, or accept the local warning and let the toolchain image run the strict gate.

::: {.tip}
> **Tip:** Run `press doctor` again after every change to the toolchain, including a Homebrew upgrade. It is the quickest way to learn that an upgrade broke a tool.
:::

The next chapter, *The shape of a book repository*, creates the Alice book with `press new` and describes every file it makes.
