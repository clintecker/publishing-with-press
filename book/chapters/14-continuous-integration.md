# Continuous integration and the release contract

::: {.in-this-chapter}
> **In this chapter:**
>
> - What a book's CI is
> - The reusable workflow
> - The composite action
> - The toolchain image
> - Receipts
> - Tags: floating and immutable
> - The release contract
> - Release builds
> - Pages
> - Moving between majors
:::

A book's CI does almost none of its own work. Its workflow file names one reusable workflow at one tag, and the press does the rest. This chapter follows the Alice book through that machinery. User `alice` pushes from the workstation `hatter` to the repository `wonderland-press/alice`, and the CI host `printshop` builds, verifies, and publishes the book. The later sections turn to the press's own tags, the workflow that proves each one, and the way a book moves from one major to the next.

## What a book's CI is

`press new` writes one CI file into every book repository, *.github/workflows/book.yml*. Example 3.12 in Chapter 3, *The shape of a book repository*, reproduces it whole. Its one job holds a single line:

```text
    uses: clintecker/press/.github/workflows/build.yml@v3
```

The book's own *CLAUDE.md* says that this file "is the whole file and should stay that way". The file decides two things: when CI runs, and what CI may touch. It runs on a push to any branch, on a tag that starts with `v`, on a pull request, and on demand through `workflow_dispatch`. It grants four permissions: `contents: write`, `packages: read`, `pages: write`, and `id-token: write`. Everything else belongs to the press.

The file is short because of the first law of the press: the press states each fact once. The way to build a book is a fact about the press, so it lives in the press. The book refers to it by tag. A book that copied the build steps into its own workflow would hold a second copy of them. That copy would go stale at the next release. The press's *CLAUDE.md*, which this book calls the maintainer's guide from here on, states the rule that "if a book needs machinery, the machinery belongs here".

@fig:ci-topology shows the machines that take part in one run. `alice` pushes from `hatter` to the repository. GitHub starts a run on `printshop`, which reads *book.yml* and follows it to the press's reusable workflow at `v3`. The runner pulls the toolchain image by its digest from the container registry, *ghcr.io*, and builds inside it. After a push to the default branch, `main`, the run deploys the Pages site. After a tag, it publishes a GitHub Release.

![One CI run, from the workstation to the reader](assets/woodcuts/14-01-ci-topology.png){#fig:ci-topology .diagram width=full-measure fig-alt="A network diagram: the workstation hatter pushes to the repository wonderland-press/alice, the runner printshop calls the press's build.yml and pulls the toolchain image by digest from the container registry, and the run deploys a Pages site and publishes a release."}

<!-- art: ARCHETYPE topology, left to right, black and white. Left: a monitor icon, "hatter", with "alice" beneath in monospace. Center: a repository cylinder, "wonderland-press/alice". Right: a server box, "printshop", with "CI runner" beneath. Above it: a crate box, "container registry (ghcr.io)", holding "press-toolchain@sha256:...". Below it: two small boxes, "GitHub Pages" and "GitHub Release". Arrows, labeled in small italic sans: monitor to cylinder, "git push". Cylinder to runner, "uses build.yml@v3". Crate to runner, "pull image by digest". Runner to Pages, "deploy pages (main)". Runner to Release, dashed, "publish release (tags)". A dotted boundary labeled "GitHub" encloses everything but the monitor. The reader should see first that the push is the only arrow out of hatter. -->

Nothing inside the dotted boundary belongs to `alice`. The build job runs on `ubuntu-24.04` inside the toolchain image, and it installs press from the composite action. Every fact that the run needs comes from the book repository or from the press at a tag.

## The reusable workflow

The *reusable workflow* is *build.yml* in the press repository, the workflow file that a book's CI calls. Its trigger is `on: workflow_call: {}`, so it runs only when another workflow calls it. It declares no inputs and no secrets. A book therefore cannot pass it a target or a token, and every book runs `press all`.

The workflow grants privilege to each job separately, and it states the reason: "building a book executes book content, so the build job holds read permissions only; the release job alone can write, and only on tags." A chapter file can hold anything, and the build job runs pandoc and LuaLaTeX over it. If that content ever did something hostile, it would hold a token that can only read. Table 14.1 lists the three jobs.

| Job | When it runs | Meaning |
|------------|------------------|------------------------------------------------|
| `build` | every run | It runs on `ubuntu-24.04` inside the toolchain image with `contents: read` and `packages: read`. It installs press, runs `press all`, and uploads the artifacts. |
| `release` | a tag only | It alone holds `contents: write`. It turns the artifacts of the build job into a GitHub Release. |
| `deploy-pages` | a push to `main` | It needs the `github-pages` environment. It deploys the Pages upload bundle that the build job made. |

Table: Table 14.1. The jobs of the reusable workflow

GitHub calls a set of files that one job hands to another an artifact. This book keeps *artifact* for a file that the press names in *dist/*, so it calls GitHub's kind an *upload bundle*.

### The build job

The build job runs five steps in order:

1. It checks out the book repository with the checkout action, pinned by its full commit SHA.
2. It runs the composite action, `uses: clintecker/press@v3.0.2`, with the environment variable `PRESS_RELEASE` set from the ref.
3. A step named "Read book identity" asks the installed press for the book's slug, title, and site URL.
4. It uploads `dist/*` except *dist/site* and *dist/pages*, with `if-no-files-found: error`.
5. On a push to `main` only, it uploads the Pages upload bundle.

At the time of this writing, *build.yml* at the tag `v3.0.2` names the composite action at that same tag. The section "Tags: floating and immutable" later in this chapter explains why the two must agree. In step 2, the value of `PRESS_RELEASE` comes from the expression `startsWith(github.ref, 'refs/tags/v') && '1' || ''`. The expression yields `1` on a tag whose name starts with `v`, and an empty string on every other run. The section "Release builds" later in this chapter describes what the value changes.

Step 3 runs a short Python heredoc that begins with `from press import booklib`. Its comment explains the choice: "The slug law and normalization live in the press; this step asks the installed press instead of keeping a second copy". The step yields three outputs, `slug`, `title`, and `site_url`, and the release job reads them. A shell line could read the slug straight from *config/metadata.yaml*. It would then hold a second copy of the slug law, and the first law of the press forbids that.

In step 4, the setting `if-no-files-found: error` turns an upload with nothing to send into a failure.

### Actions pinned by commit

The workflow pins the checkout action and every other outside action to a commit SHA of 40 hexadecimal digits. GitHub has no ruleset that enforces this kind of pin, so the press enforces it with a test, `tests/test_ci_posture.py::test_every_action_is_pinned_by_full_commit_sha`. The composite action is the exception. The workflow pins it to the press's own immutable tag. The release contract proves that pin, as the section "The release contract" later in this chapter describes.

## The composite action

The *composite action* is *action.yml* at the top of the press repository. This one has two shell steps. The reusable workflow runs it in its second step, so a book never names it.

Example 14.1 shows the head of the action and its install step. It replaces the long description, the input's description, and a comment with `...`. It also breaks the two long `pip install` commands with a backslash, which the shell reads as the same command. Every other line is verbatim.

**Example 14.1. The head and the install step of action.yml**

```text
name: press
description: >-
  ...
inputs:
  command:
    ...
    default: all
runs:
  using: composite
  steps:
    - name: Install press
      shell: bash
      ...
      run: |
        python3 -m pip install --quiet \
          --break-system-packages \
          --require-hashes \
          -r "$GITHUB_ACTION_PATH/requirements-lock.txt"
        python3 -m pip install --quiet \
          --break-system-packages \
          --no-deps "$GITHUB_ACTION_PATH"
```

The description states the design: "Because GitHub materializes the action repository onto the runner, even a private book can use the press with no cross-repo token." The variable `GITHUB_ACTION_PATH` names that copy of the press, and the install step installs press from it. Nothing in the step fetches press from anywhere else.

### Self-checkout install

The maintainer's guide treats this install as law. The self-checkout install "keeps a private book working with no cross-repo token and pins the installed press to the exact action ref; do not replace it with pip-from-git." The first half of that sentence keeps a private book free of any credential for a second repository. The second half means the press that runs is the press at the ref the workflow named, with no second fetch to disagree with it.

::: {.warning}
> **Warning:** Do not replace the install step with a `pip install` from a Git URL, in the press or in a fork of it.
:::

### The hash lock

The first `pip install` in Example 14.1 installs the runtime dependencies before press itself, from the file *requirements-lock.txt*. That file is the *hash lock*. At the time of this writing, it pins three packages, `pillow==13.0.0`, `pypdf==6.21.4`, and `ruamel-yaml==0.19.1`, with 87 sha256 hashes. pip-compile produced it under Python 3.12.

With `--require-hashes`, pip refuses any file whose hash the lock does not list. The second `pip install` installs press with `--no-deps`, so pip resolves nothing fresh. The comment in the step gives the reason, and cites issue #194: "a pinned release resolves immutable dependency bytes, not whatever PyPI serves today". Without the lock, a book pinned to `v3.0.2` would get the same press every time and whatever Pillow PyPI served that day. Both commands carry `--break-system-packages`, because the Python inside the image belongs to Ubuntu 24.04, as Chapter 2, *Installing press*, explains.

The press regenerates the lock with *scripts/lock-deps.sh*, which runs pip-compile inside the pinned image. pip-compile keeps the pins that already exist. A security fix for one package is therefore a named upgrade, `scripts/lock-deps.sh --upgrade-package <name>`, and nothing else in the lock moves. Release 3.0.2 was one such upgrade.[^14-pillow]

### The run step

Example 14.2 shows the second step of the action, which runs the target. It elides the comment above the variable and a validation block.

**Example 14.2. The run step of action.yml**

```text
    - name: Run press
      shell: bash
      env:
        ...
        PRESS_COMMAND: ${{ inputs.command }}
      run: |
        ...
        read -r -a argv <<< "$PRESS_COMMAND"
        python3 -m press "${argv[@]}"
```

The input `command` names the target, and its default is `all`. The elided comment says why the input travels as the variable `PRESS_COMMAND`: "The input reaches the script as an environment value, never interpolated into shell text, so metacharacters are data." The elided block refuses any value that is not a lowercase target name followed by plain path and flag arguments. It exits with status 2. For the input `all && rm -rf dist`, the refusal would read:

```text
press action: refusing command input: all && rm -rf dist
targets are lowercase words with plain path/flag arguments;
shell syntax is not part of the grammar
```

A book cannot set the input at all, because the reusable workflow takes no inputs.

[^14-pillow]: The upgrade moved Pillow to 13.0.0 and closed forty-one advisories, five of them critical. The press's CHANGELOG for 3.0.2 records it as a one-package change made with `scripts/lock-deps.sh --upgrade-package pillow`.

## The toolchain image

Chapter 2 describes what the toolchain image holds and how to pull it. The press's workflow *toolchain.yml* builds `ghcr.io/clintecker/press-toolchain` from the press's *Dockerfile*. It builds amd64 on `ubuntu-24.04` and arm64 on `ubuntu-24.04-arm`, and it tests each image before it pushes. The workflow publishes two kinds of tag: `:latest`, and `:sha-` followed by a commit hash of the press.

Neither kind of tag is a pin, because both are mutable. A *digest* is `@sha256:` followed by 64 hexadecimal digits, and it pins the image's bytes. The maintainer's guide says so in a parenthesis: "a `sha-` tag alone is mutable and is refused".

### Where to find the digest

The digest appears in two places: the `image:` line of the press's *build.yml* at the tag your book pins, and the release receipt for that tag. The first is the easier one to read. Example 14.3 shows the container block of the build job at `v3.0.2`. It cuts the image line after `sha-`, because the full line runs to more than twice the width of this page.

**Example 14.3. The container block of the build job at v3.0.2**

```text
image: ghcr.io/clintecker/press-toolchain:sha-...
credentials:
  username: ${{ github.actor }}
  password: ${{ secrets.github_token }}
```

The full value of the image line names the image three ways at once. Broken at its punctuation, with the 64 digits of the digest split into two lines of 32, it reads:

```text
ghcr.io/clintecker/press-toolchain
:sha-0a3a99d676a11a7279085d818805c2473307a026
@sha256:
0d784ac08282a94e64b444efd86ee3bf
9eb45262a9e6e758fc656a2363b2ca04
```

The first line names the image in the container registry. The `sha-` tag tells a human reader which commit of the press built the image. The last three lines are the pin. Do not look for the digest in the release notes. The notes come from the CHANGELOG, and the digest lives in the workflow and the receipt.

The credentials block authenticates the pull with the workflow's own token. The image is public, since 2026-07-20 (issue #161), so "a book under any account pulls it with no package grant and no configured secret". That token works for a public image on fork and Dependabot pull requests too.

### A local build that matches CI

Example 2.6 in Chapter 2 builds the editions in the image at `:latest`, the form that the press's install guide gives. To match CI, replace `:latest` with the value of the `image:` line of *build.yml* at the three-part tag you pin. Example 14.4 shows the result. Its third line elides the two long values, which are the ones in Example 14.3.

**Example 14.4. Building on hatter in the image that CI uses**

```text
$ cd ~/alice
$ docker run --rm -v "$PWD":/book \
    ghcr.io/clintecker/press-toolchain:sha-...@sha256:... \
    bash -c "pip install --break-system-packages \
    'press @ git+https://github.com/clintecker/press@v3.0.2' \
    && cd /book && press all"
...
```

The documented recipe replaces the image and nothing else. Chapter 2 also pairs the digest with the three-part press tag that the book pins, `v3.0.2` here in place of `v3`. A local build installs press from Git, because only CI uses the self-checkout. The Python dependencies can therefore still differ from CI's, because pip resolves them fresh here.

::: {.tip}
> **Tip:** Read the digest from *build.yml* at the exact three-part tag you install. No release contract ever proved the image of one tag with the press of another.
:::

## Receipts

A green check says only that a job exited with status zero. The press asks for more before it names a release. A *trust receipt* is the record that one layer of the press's proof ran. The module *src/press/receipts.py* defines twelve layers, in order: collection, unit, property, component, damage, graph, scenario, integration, distribution, container, boundary, and release. It groups them into three release tiers, named quality, integration, and release.

The receipts form a chain. Verification requires "every layer present, contiguous, and linked to its predecessor", so a short chain cannot stand in for the layers it lacks. One of the press's product laws states the same idea from the other side: "A higher layer cannot erase missing proof below it." A passing integration run says nothing about a unit layer that never ran, and the chain makes that absence visible.

The last receipt in the chain is the *release receipt*. It names two digests: the digest of the built wheel and the pinned toolchain digest. Those two values tie the Python package and the image to one tag. The *release contract*, the workflow that proves a press tag, assembles this receipt, as the section "The release contract" later in this chapter describes.

The module's command line has four subcommands:

```text
python3 -m press.receipts emit|assemble|verify|verify-release
```

The press's CI calls these, and you do not need them. You open a receipt only to answer a question such as which toolchain digest a release used.

## Tags: floating and immutable

The press names its releases with the tag convention of GitHub Actions. A *floating tag* such as `v3` names a major and moves to the newest compatible release within it. An *immutable tag* such as `v3.0.2` names one release forever. The maintainer's guide adds that "immutability is enforced, not promised".

An immutable tag's *build.yml* must pin the composite action to that exact tag and the toolchain image to a digest that resolves. The same passage ends with the result: "a pinned book resolves the same pipeline, action, and toolchain bytes forever, while `vN` floats normally."

@fig:resolving-v3 follows the Alice book from its pin to the bytes. *book.yml* names *build.yml* at `v3`. At the time of this writing, the floating tag `v3` points at `v3.0.2`. The *build.yml* at that tag pins the composite action to `v3.0.2` and the image to its digest. A book pinned directly to `v3.0.2` enters the figure one box later and reaches the same bytes.

![How a book's pin at v3 resolves to fixed bytes](assets/woodcuts/14-02-resolving-v3.png){#fig:resolving-v3 .diagram width=full-measure fig-alt="A top-to-bottom flowchart: the book's pin at v3 follows the floating tag to the newest three-part tag, whose build.yml pins the composite action to itself and the toolchain image to a digest, so every run gets the same bytes."}

<!-- art: ARCHETYPE flowchart, top to bottom, black and white. Box 1, rounded: "book.yml", with monospace "uses: .../build.yml@v3". Arrow down, "floating tag". Box 2: "v3 resolves to the newest v3.x.y", with "v3.0.2 at the time of writing" in small italic. Arrow down. Box 3, heavy-ruled: "build.yml at v3.0.2". Two arrows fan from box 3 to two side-by-side boxes: "composite action", monospace "clintecker/press@v3.0.2", and "toolchain image", monospace "@sha256:0d784ac0...". Both converge on a double-ruled box: "the same bytes every time". At left, a small box "a book pinned @v3.0.2" with a dashed arrow into box 3. The reader should see first the single path from v3 to the double-ruled box. -->

### Where a book pins

A book names the press in two files. *book.yml* pins the reusable workflow for CI, and *requirements.txt* pins the press package for a local build. In a fresh book, both say `v3`. To freeze your book on one release, change both to the same immutable tag, such as `v3.0.2`. `press migrate`, described at the end of this chapter, reads both files and treats a pin such as `@v1.20.0` as an immutable one.

::: {.tip}
> **Tip:** When you pin an immutable tag, change *book.yml* and *requirements.txt* in the same commit. CI reads the first and your workstation reads the second, and a book pinned two ways builds two ways.
:::

### What a major promises

Design is part of what a tag promises. In the words of the maintainer's guide, "within a major, fixes may correct broken output but must not change typography or layout of a valid book; design and template changes require a new major." A book on `v3` therefore receives repairs as they come, and its valid pages keep their lines and breaks. A change of design waits for `v4`, and your book reaches it only when you move the pin.

### The press's tag grammar

The press accepts a narrow grammar for its own release tags, and `press selftest` proves the grammar against the cases in Table 14.2. A good tag is a `v` and three numeric parts, with nothing before or after. The grammar governs the press's tags only. Your book's CI treats any tag that starts with `v` as a release.

| Tag | Meaning |
|--------------|----------------------------------------------------------|
| `v1.0.0`, `v0.0.1`, `v10.20.30` | The press accepts these. Each has three numeric parts with no leading zero. |
| `v1.0`, `v1.0.0.0` | The press refuses these, because each has the wrong number of parts. |
| `v1.0.0-rc1` | The press refuses this. A prerelease suffix is not part of the grammar. |
| `v01.0.0` | The press refuses this, because a part has a leading zero. |
| `1.0.0`, `"v1.0.0 "` | The press refuses these. The first lacks the `v`, and the second carries a trailing space. |

Table: Table 14.2. The press's own release tag grammar

### What the platform enforces

Two kinds of guard protect the tags. The release contract proves what a tag pins, as the next section describes. The platform's rulesets, listed in the press's *SECURITY.md*, protect the tags themselves. Nobody can force-push or delete `main`. Nobody can move or delete an immutable tag `v*.*.*`. The floating tag moves only through *scripts/release.sh*.[^14-main]

::: {.warning}
> **Warning:** Never move a floating tag by hand, even when a release run stopped halfway. Rerun *scripts/release.sh* with the same tag instead. The script moves the floating tag only after the release contract proves the new tag.
:::

[^14-main]: `main` takes direct pushes by design, under issue #153. The press enforces its checks at the release boundary, the tag, where the release contract runs.

## The release contract

The release contract is *.github/workflows/release-contract.yml* in the press repository. It runs on every tag that matches `v[0-9]+.[0-9]+.[0-9]+`. It proves four things in order and then uploads the result:

1. The tag's *build.yml* must contain `uses: clintecker/press@${tag}`, and its image must match `press-toolchain:sha-...@sha256:` followed by 64 hexadecimal digits.
2. `docker manifest inspect` must succeed on that image.
3. The `quality`, `consumer`, and `desk` check runs on the tag's commit must succeed. The workflow waits for them up to 60 times 30 seconds, half an hour. The newest run of each name decides.
4. The workflow builds the wheel, downloads the upload bundles `receipt-quality` and `receipt-integration`, and runs `python3 -m press.receipts assemble`.
5. The workflow uploads the release receipt as the upload bundle `release-receipt`.

Step 1 is where the press refuses a `sha-` tag alone. An image line without the digest does not match the pattern, and the contract turns red. The pattern needs the `sha-` tag as well, so an image line that carries only the digest fails too. Step 2 catches the opposite mistake, a digest in the right form that names no image in the container registry.

Each of the three check runs proves a different thing. The `quality` run lints the press and runs the quality gate. The `consumer` run comes from the press's integration gate. That gate must "build the wheel, scaffold a stranger's book, run the whole `press all`, and prove tampering turns the verifier red". The `desk` run proves that a bare wheel refuses the desk and that the tui wheel runs it headless.[^14-macos]

### The release script

The press cuts a release with *scripts/release.sh*. The maintainer's guide calls it "the one release path and a resumable state machine". Before a run, the maintainer rolls the CHANGELOG's `[Unreleased]` section into a version section. The script then runs a preflight and five steps, which Table 14.3 lists.

| Step | Meaning |
|------------------|------------------------------------------------------|
| Preflight | The script requires a clean tree and a CHANGELOG section for the version. If the tag already exists on the remote, the script resumes it only when that tag's *build.yml* pins itself. |
| 1. Release commit | The script waits for the `consumer` check on HEAD. It rewrites `uses: clintecker/press@vX` in *build.yml* and `version = "..."` in *pyproject.toml*. Then it runs `press selftest`, commits "Release vX", and pushes `main`. |
| 2. Immutable tag | The script pushes the three-part tag. |
| 3. Release contract | The script waits for the `contract` check. If the check fails, the script stops, and the floating tag stays where it was. |
| 4. Float the major | The script moves the floating tag with `git push -f origin vN`. |
| 5. GitHub Release | The script publishes the release, titled `press vX`, with notes from the CHANGELOG. |

Table: Table 14.3. The steps of scripts/release.sh

@fig:release-state-machine draws the same run as states. The floating tag moves only after the contract proves the immutable tag. A failure at any state before that leaves every book on `v3` where it was.

![The states of one press release](assets/woodcuts/14-03-release-state-machine.png){#fig:release-state-machine .diagram width=full-measure fig-alt="A state diagram of a press release from the pushed commit through the tag, the checks, and the proof to the moved floating tag and the published release, with failure arcs to a stop and a rerun arc back."}

<!-- art: ARCHETYPE state machine, black and white, in two snaking rows. Top row, left to right: a start dot, then four circles in monospace, each with a short italic gloss: "pushed" (release commit on main), "tagged" (v3.0.2), "built" (checks run on the release commit), "verified" (newest run of each passes). The arc bends down at the right. Bottom row, right to left: "contract proved" (pins, digest, receipts), "floating tag moved" (v3), "release published", then a double circle "done". "pass" arcs join each state to the next. At the bottom left, a square box "stopped" with a 2 pt offset shadow. "fail" arcs run from "built", "verified", "contract proved", and "release published" into "stopped". A dashed arc "rerun release.sh" climbs from "stopped" back to "tagged". The reader should see first that v3 moves only after "contract proved". -->

### Recovery and other details

When a run stops, the recovery is the same command again. The maintainer's guide says that "rerunning after any failure is the recovery procedure". The preflight sees a tag that already exists, checks that its *build.yml* pins itself, and resumes from there. Before a run, `--check-tag` validates a tag against the grammar without touching the network. For a next release such as `v3.0.3`, the two commands are:

```text
$ scripts/release.sh --check-tag v3.0.3
$ scripts/release.sh v3.0.3
```

The script does not repin the toolchain digest. A new image reaches the press through a separate change to *build.yml*. For a new major, the maintainer also moves the requirements pin in the book template. That way, a book scaffolded after the release names the new major.

::: {.sidebar}
> **The release script that rewrote mypy**
>
> Step 1 of the release script rewrites one version string in *pyproject.toml*, the line `version = "..."`. An earlier version of the script found that string with a regular expression that had no anchor. The same file holds a `[tool.mypy]` table, and the table's `python_version` setting contains the text `version = "` as well. The script's comment records the result: the unanchored pattern "once rewrote [tool.mypy]'s python_version". A run meant to change the version of the press changed the Python version that mypy assumed.
>
> The repair has two parts. The pattern is now anchored, and it runs with `count=1`, so it changes the first match and stops. The comment sits beside the line it protects, where the next maintainer to edit the pattern will read it.
:::

[^14-macos]: The press also tests itself on macOS. During the 3.0.0 release, GitHub retired the `macos-14` runner. GitHub canceled the job that asked for it within a second, with "configuration not supported". The job moved to `macos-15`.

## Release builds

You release a book the same way the press releases itself, with a tag. The CI file triggers on any tag that starts with `v`, and the reusable workflow sets `PRESS_RELEASE=1` for it. The value turns on the release checks. The press demands its *release witnesses*, at least two sentinels and a `verify-min-pages` of 24 or more, as Chapter 6, *Checking the manuscript*, explains. For a book with print ordering turned on, the commerce gate also stops advising and enforces its findings, as Chapter 7, *Building the editions*, explains.

::: {.tip}
> **Tip:** Set two sentinels and a page floor of 24 or more before your first release tag. A fresh book's draft settings pass every push to `main`, and they fail on the first tag.
:::

### Release day

To release the Alice book as version 1.0.0:

1. Roll the `[Unreleased]` section of *CHANGELOG.md* into a section for version 1.0.0, and commit it on `main`.
2. Tag that commit and push both:

   ```text
   $ git tag v1.0.0
   $ git push origin main v1.0.0
   ```

3. Open the repository on GitHub and watch its Actions tab.

The push in step 2 starts two runs on `printshop`, one for the branch and one for the tag. The run for `main` builds and verifies the book, uploads the Pages upload bundle, and deploys the Pages site. The run for `v1.0.0` builds the book again under `PRESS_RELEASE=1`, and its release job then publishes the GitHub Release. The tag run builds the same commit, with the release checks turned on.

If you forgot the tip, the run for `main` passes and the run for the tag fails in the build job. The log shows the release refusal of Example 6.11, which for a fresh book begins this way:

```text
this is a release build (PRESS_RELEASE=1) and its witnesses ...
verify-sentinels has 0 entries; a release needs at least 2 ...
verify-min-pages is 1; a release needs at least 24
```

The press calls draft settings like these *vacuous witnesses*. To recover, set two sentinels and the page floor with `press config set`, as Chapter 3 shows. In the same commit on `main`, rename the CHANGELOG section from 1.0.0 to 1.0.1, because the release job looks for the section that matches the tag. A tag names one commit, so the fixed commit needs a tag of its own, such as `v1.0.1`. Push it, and the tag run starts again from the beginning.

### The release job

The release job runs only on a tag, and it holds `contents: write`. It does four things:

1. It refuses a tagged commit that is not on `main`.
2. It extracts the section headed `## [version]` for the tag from the book's *CHANGELOG.md*.
3. It appends a section headed "## Public downloads", with direct links to `${SITE_URL}/downloads/<name>` for each download.
4. It runs `gh release create` with every file in *dist/*, titled `"$TITLE $GITHUB_REF_NAME"`.

The CHANGELOG in step 2 is the book's own, never the press's. If the section is missing, the job stops. Its message begins `no CHANGELOG section for` and the tag's version, and it ends `roll [Unreleased] before tagging`.

For the Alice book, the release title is *Alice's Adventures in Wonderland v1.0.0*. The title comes from the `title` output of the build job's identity step and from the tag's name. The links in step 3 come from the same identity step, through its `site_url` output.

::: {.warning}
> **Warning:** Do not tag a commit on a branch other than `main`. The build job runs and passes. Then the release job refuses the tag, so the release never appears.
:::

## Pages

The Pages site is the Web site that GitHub Pages serves from the book's Pages bundle, *dist/pages/*. Chapter 3 describes what the bundle holds. It has the landing page, a copy of the reader site under *read/*, and every download under *downloads/*. With `site-url` set, it also has a sitemap and a *robots.txt*. `press all` verifies the bundle before CI uploads it, with the verifier that Chapter 8, *Verifying the artifacts*, describes.

Two jobs on `printshop` publish the bundle. The build job uploads the Pages upload bundle, but only on a push to the default branch. The job `deploy-pages` then runs, also only on a push to the default branch, in the `github-pages` environment. A pull request, a push to another branch, or a tag builds and verifies the whole book and deploys nothing. The site therefore always shows `main`.

GitHub also needs one setting that no file can make. Chapter 3 gives that one-time step for each book repository.

The release notes depend on the Pages site. Each link under "Public downloads" points into the site's *downloads/* directory, at `${SITE_URL}/downloads/<name>`. The GitHub Release also carries every file in *dist/* itself, from step 4 of the release job.

## Moving between majors

A book stays on its major until you move the pin. The press's migration guide says: "Old pins keep working". When you want the next major, `press migrate` moves the pin. Table 14.4 lists its subcommands.

| Command | Meaning |
|--------------------------|--------------------------------------------------|
| `press migrate` | It shows the plan, the same as `press migrate plan`. It is a dry run and writes nothing. |
| `press migrate apply` | It writes an exact backup and then rewrites the pins. |
| `press migrate status` | It reports the major the book pins and any migration it recorded. |
| `press migrate rollback` | It restores the exact pins from before the last `apply`. |

Table: Table 14.4. The press migrate subcommands

### What migrate rewrites

The target changes only the pin, and only in two places: *requirements.txt* and the workflow files in *.github/workflows/* whose names end in *.yml* or *.yaml*. It finds a pin with the pattern:

```text
(clintecker/press(?:/[\w./-]*?)?@v)(\d+)(\.\d+\.\d+)?
```

The pattern matches both `clintecker/press@v3` and the longer workflow path. The target refuses a pin that it finds anywhere else, and it leaves that pin as it is. It also refuses a book whose pins name two different majors, with the instruction "reconcile them before migrating".

The new pin is always the current major plus one. An immutable pin such as `@v1.20.0` becomes the floating tag of the new major, `@v2`. If you want an immutable pin on the new major, set it by hand after `apply`, in both files.

### The plan

The plan begins with the major the book pins and each pin it found, file by file. It then lists each rewrite, with the old pin beside the new one. A section headed "before you apply" points to the press's migration guide for what the new major changes. It also says that the plan leaves the manuscript, the config, and the accepted art alone.

The plan names any override that the design profile does not govern: *tex/title-page.tex*, *assets/web/reader.css*, *assets/web/extra.css*, and *config/aesthetic.yaml*. The press leaves these files alone, but it asks you to check them under the new major. The last line of the plan repeats the rule of the dry run.

### Apply and rollback

`press migrate apply` works in three steps. It writes *.press/migration-backup.json*, which holds the full bytes of every file it will change. It rewrites the pins. Then it writes *.press/migration-receipt.json*, which records `from_major`, `to_major`, `press_version`, and `sites`. `press migrate rollback` restores the exact bytes from the backup and removes both files. With nothing to undo, it says so:

```text
no migration to roll back (no .press/migration-backup.json)
```

The press holds this target to two invariants, `INV-migration-safe`, which is critical, and `INV-migration-preview`. The `press selftest` check `check_migration` proves both with a real plan, apply, and rollback on a scaffolded book.

### What each step up changes

Each major changes something different, and the plan says what. From `v1` to `v2`, a book that keeps the house profile builds "byte-for-byte as it did under v1". From `v2` to `v3`, the step is a design major, and the plan calls it "a re-proof of your PDF, not a quiet repin". The craft pass of `v3` moves glyphs and line breaks, and page counts may move with them. Before version 3.0.1, the plan told you, on `v2`, that your geometry would not change. That was true only of the step from `v1` to `v2`.[^14-migrate]

::: {.warning}
> **Warning:** Treat a move from `v2` to `v3` as a new proof of the book. Read every page of the new PDF before you tag a release on `v3`. Then check your sentinels and page floor against the new page count.
:::

Until you run `apply`, the book stays on its major. At the time of this writing, a book on `v3` resolves to `v3.0.2` and its image digest. When `v3` moves to a newer release, the book follows it, and only a pin of `v3.0.2` itself holds the book in place.

[^14-migrate]: The fix is in 3.0.1, under issue #262. The press's CHANGELOG records that the old message promised byte-for-byte geometry for a step that changes the design.
