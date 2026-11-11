# Developmental edit: Chapter 2, Installing press

Desk: developmental editor. File: `book/chapters/02-installing-press.md`
(380 lines, read as the design's reader: an author who can use a shell and
does not know TeX). Line numbers refer to the file as read.

Status: DONE_WITH_CONCERNS. 1 block, 15 should.

## 1. Coverage

The seven A-heads from the brief are all present, in order, sentence case,
with prose between every pair of headings.

| A-head | Line | Does the section deliver? |
|---|---|---|
| What you need | 17 | Yes. Table 2.1 and the dependency paragraph name every part. |
| Installing the Python package | 41 | Mostly. Tag, editable, extras, and CI are all here. The install fails as written on the reference platform (see P1). |
| The system toolchain | 109 | Yes. macOS, Debian/Ubuntu, the tool table, and versions. |
| Running the doctor | 196 | Yes. Strongest section in the chapter. |
| The toolchain image | 258 | Yes for the image. The design's dev loop is missing (B1). |
| Apple Silicon and other platforms | 314 | Thin on "other". See S6. |
| The first run | 326 | Partly. The font scan is covered. The procedure has a gap (P2) and nothing shows what success looks like (S5). |

**B1 (block). `scripts/dev-render.sh` is missing.** The design row for
Chapter 2 lists "the toolchain image and `scripts/dev-render.sh`" as core
content. The chapter never mentions it. The writer reported the gap
correctly: facts-02 has no entry for it. This is a controller fix, not a
writer fix. Add a fact block to facts-02 from the script's header in the
press repository (`scripts/dev-render.sh`, lines 1 to 30). It runs press in
the pinned toolchain container, reads the image from `build.yml` so it
cannot drift from CI, defaults to the Alice example, takes `--book DIR`,
`--out DIR` (default `build/dev-render`), `--preview[=N]`, and `--shell`.
Its audience is the press-checkout developer, which matters for how much
space it earns here. Then have the writer add one B-head under "The
toolchain image", after "Building a book inside the image". That is the
place where line 307 now says "use the digest ... Chapter 14 shows where to
find it". dev-render.sh answers exactly the question that line defers. Budget
150 to 250 words.

"What is not tested" (design row, §2) is reached only in scattered pieces:
line 33 (newer Python), line 103 (other installers), line 324 (Windows).
The coverage is technically present. See S6 for the fix.

## 2. Path

**P1 (should, highest priority). The first install command fails on both
platforms the chapter documents.** Example 2.1 runs a bare `pip install`
against the system Python. On Ubuntu 24.04, which the chapter names as the
reference platform (line 192), and on a Homebrew Python, pip refuses with an
externally-managed-environment error. The chapter itself shows the symptom
at line 305: inside the image, "`pip install` needs
`--break-system-packages`, and the command fails without it". The reader
meets that failure on `hatter` before reaching line 305, with no remedy. The
section must tell the reader where the package goes (a virtual environment
per book, or per user) before Example 2.1, and Example 2.1 must show that
step. Facts-02 has no virtual-environment fact, and press's own `INSTALL.md`
and `README.md` say nothing about one. The controller must supply the fact
(the scaffolded `requirements.txt` and the book Makefile are the likely
sources) before the writer adds it. Do not let the writer invent the venv
path or command shape.

**P2 (should). The first-run procedure depends on Chapter 3.** Step 3 (line
336) says "Create a book, or change into an existing book repository" and
shows only `cd ~/alice`. At this point in the book `~/alice` does not exist.
The reader who follows the four steps in order types `press all` in a
directory that is not a book. Examples 2.2 (line 77) and 2.5 (line 296)
also `cd ~/alice` before any chapter has created it. The fix is a choice
for the writer. Either step 3 shows the scaffold command, or the procedure
stops at step 2 and hands steps 3 and 4 to Chapter 3 in the forward
pointer. If step 3 shows `press new`, it must also show `git init` and a
first commit (shared context A.26: the source zip needs tracked files), or
`press all` fails at the source edition on the reader's first run. In
Example 2.2, the `cd ~/alice` line does nothing for pip. Cut it, or say in
the prose why the reader is in the book directory.

**P3 (should). The doctor figure contradicts the advice two screens
later.** Figure `@fig:doctor-report` ends `not ready: claude`. Table 2.3
marks `claude` optional, and Table 2.4 says an optional tool's absence
leaves press able to build. Line 250 then recommends `press doctor && press
all`. On the machine in the figure, that line refuses to build a machine
that can build. The reader will ask why an optional tool blocks readiness,
and the chapter does not say. Facts B.14 lists "a broken optional tool fails
doctor" as bug-like, so the chapter must not present it as a rule. It still
must not leave the reader stranded. Two acceptable fixes: (a) after the
figure, one sentence that the report counts any broken tool against
readiness, so a broken `claude` must be repaired or removed from `PATH`
before the `&&` form works. That states the behavior without blessing it.
(b) Drop the `&&` recommendation at line 250 and keep only the grep
warning. Prefer (a), because a reader of Chapter 15 will meet the same
line.

**P4 (should). Extras command.** Line 86 quotes `pip install 'press[tui]'`
two sections after line 43 says press is not on PyPI. That spelling resolves
against PyPI and fails, exactly as line 43 warns. The sentence that follows
tells the reader to assemble the right form themselves. Show the assembled
requirement in a short example, the Git-URL form with `[tui]` after the
name. The writer flagged this in their report. The form is standard pip
requirement syntax (PEP 508), so the controller can confirm it in one
command against the press repository. Then drop the PyPI-shaped quotation,
or keep it only as "the install documentation's shorthand".

**P5 (should). Undefined terms on the reader's path.** The following appear
before or without definition. Each needs either a defining clause or a
pointer.
- "scar" (line 253, "the rule against it is now a scar"). The reader does
  not know the press keeps a scars list until the sidebar at line 354. Move
  the definition forward or rephrase line 253.
- "release contract" (line 287) and "reusable workflow" (lines 283, 287,
  307). Both are Chapter 14 terms. Line 107 points to Chapter 14 for the
  composite action only. One clause at first use ("the workflow a book's CI
  calls") is enough.
- "target" (line 111) is defined in a sentence whose grammar hides the
  definition: "Press calls each command that builds, checks, or verifies a
  *target*". Restate it so the term is the object of the definition. The
  chapter also calls `press doctor` a target (line 198), which does not
  build, check an artifact, or verify one. Make the definition cover it or
  call the doctor a command.

**P6 (should). Line 194 states a wrong reason.** "Trust `printshop`,
because it ran the toolchain that proved the release." `printshop` is the
book's CI host. It did not prove the press release. It runs the same image,
pinned by the same digest, that the press's release contract proved. The
sentence must give that reason.

## 3. Proportion

**S1 (should). The font scan is told three times.** Line 345 tells it
(several minutes, looks like a hang, is not). The sidebar at 347 to 357
tells it again with the scars quotation. Line 358 tells it a third time ("A
build that stays silent for several minutes on a fresh machine is almost
certainly the scan"). Keep the sidebar. Cut line 345 to the one sentence
that introduces it, and let line 358 do only what it alone does: say that
press does not hurry the scan and that no other build timing is
documented. The design names this as the chapter's sidebar, so the
surrounding prose should set it up, not pre-empt it.

**S2 (should). The BROKEN rationale is given twice.** Line 240 explains why
the `BROKEN` state exists and promises the story later. Line 279 explains it
again after the warning at 276. Keep one explanation, at 279, where the
story is. At line 240, keep the mechanism (`--version`, `-v`, 15 seconds)
and the forward pointer only.

**S3 (should). Low-value paragraphs in "What you need".** Line 37 (MIT
licence, Beta classifier) does nothing for an author installing press. Cut
it or fold it into one clause elsewhere. Line 33 repeats the Python range
from Table 2.1's row two lines earlier. Keep the CI detail (five releases on
Ubuntu, 3.12 on macOS 15) and drop the restatement. Line 141's
headless-Chrome sentence tells the reader about a tool they will never
need. Cut it unless the writer can say why an author would meet it.

**S4 (should). Tag semantics are spread over two sections.** Line 60 gives
floating and immutable tags and the within-major design rule. Lines 285 to
287 give mutable and immutable image tags and the digest. They are the same
idea (what a pin buys you) applied to two things. Line 287's last sentence
already ties them together ("a book pinned to `v3.0.2` builds with the same
pandoc"). Line 60 should end by pointing forward to that sentence so the
reader sees one argument, not two.

**S5 (should). The first run is short where it matters most.** After two
thousand words of installation, "The first run" never shows the reader what
success looks like. Line 362 says "A green result on the first run tells you
that the whole installation works together", but the reader has not seen a
green result, the ready line from the doctor in context, or a `dist/`
listing. Add one short example: the doctor's last line on a ready machine
(`this machine can make books`, already in facts-02) and the `press all`
exit status. If facts-02 holds no captured `press all` output, elide it
with `...` and say in prose what the exit status means. Do not invent
output. Budget the words from S1 and S3.

**S6 (should). "Other platforms" is two paragraphs and a fragment.** Line
324, "Windows is not tested.", is a one-sentence paragraph that leaves the
Windows reader with nothing. Gather the "not tested" facts into one short
paragraph at the end of the A-head: Windows, Python above 3.14, installers
other than pip (line 103 can move here), and versions of pandoc and TeX
Live other than Ubuntu 24.04's. All four facts are in facts-02. That
paragraph is also the honest place to say the toolchain image is the route
whose bytes the press tests. Do not claim it works on a Windows host.

The bullet list at lines 266 to 269 is a list of things and earns its
bullets. No bullet sprawl elsewhere.

## 4. Opening and closing

The "In this chapter" box (lines 3 to 13) matches the seven A-heads exactly.

The orientation paragraph (line 15) has no heading above it and runs five
sentences. It says what (two halves, installed separately) and why (confirm
the machine before asking it to make a book). It is within the limit.

The close (line 370) is a one-sentence forward pointer to Chapter 3, after
a tip. That conforms. If P2 moves `press new` out of the procedure, this
pointer becomes the handoff for it, and should say so.

**S7 (should, markup).** The sidebar's closing `:::` (line 357) is followed
directly by the paragraph at line 358 with no blank line. Every other
fenced div in the chapter has one. Add the blank line. The pandoc reader is
tolerant here, but the house markup is not.

## 5. Numbered items

**S8 (should). Figure numbers will come out swapped.** The brief assigns
Figure 2.1 to `@fig:doctor-report` (file `02-01-doctor-report.png`) and
Figure 2.2 to `@fig:tools-in-the-build` (file `02-02-...`). The chapter
places tools-in-the-build at line 116, in "The system toolchain", and
doctor-report at line 222, in "Running the doctor". Figures number in order
of appearance, so the built book will print the data-flow as Figure 2.1 and
the doctor report as Figure 2.2. The file names and the brief will then
disagree with the caption numbers. The data-flow placement is the right one
for the reader: the tool table needs it. The cheapest fix is to swap the
two numbers in the brief and rename the two image files before the
illustrator delivers. That is a controller decision, and the writer should
not move the figure.

**S9 (should). Table 2.3's header overpromises.** The header reads
"Purpose, as the doctor prints it", and line 120 says the table gives each
purpose "in the words `press doctor` prints". Most cells then add a second
sentence the doctor does not print ("Nothing builds without it.", "It
reruns LuaLaTeX until the lists settle."). The cells also capitalize what
the doctor prints in lowercase. Either print the doctor's text verbatim, in
constant width, with the explanation in a third column, or rename the
column "Purpose" and drop "in the words" from line 120. A reader who
compares the table with Figure 2.1 will otherwise find the two disagree.

Every table (2.1 to 2.4), every example (2.1 to 2.5), and every figure is
referred to in prose before it appears. Each earns its place. Table 2.2 is
the weakest: its last two rows (the `tui` extra, the toolchain image) are
not install forms in the sense of the first four. Keep the table, but
consider moving the image row's guidance into the prose at line 260, where
the reader will look for it.

The art directives are complete and readable by an illustrator who has not
read the chapter. Figure 2.3's directive lists `wrapfig` as something
`hatter` may lack. Facts-02 never mentions wrapfig, and the prose at line
309 does not name it. The controller should confirm wrapfig is a real
dependency before the illustrator draws it, or the writer should drop it
from the directive.

## 6. Length

`press wordcount`: 5,309 against a target of 5,000. That is 6 percent over,
within the 15 percent band. The cuts in S1, S2, and S3 free roughly 250 to
350 words. The additions in B1, P1, P2, and S5 need about the same. The
chapter should land near its present length.

## Summary of findings

| ID | Severity | Line | Finding |
|---|---|---|---|
| B1 | block | 289 to 307 | `scripts/dev-render.sh` missing. Controller adds the fact, then the writer adds a B-head. |
| P1 | should | 47 to 56 | Bare `pip install` fails on Ubuntu 24.04 and Homebrew Python. Needs a venv fact from the controller. |
| P2 | should | 330 to 341 | Procedure assumes a book from Chapter 3. Also Examples 2.2 and 2.5. |
| P3 | should | 200, 250 | `not ready: claude` in the figure versus the `&&` advice. |
| P4 | should | 86 | `press[tui]` shown in a PyPI form that fails. |
| P5 | should | 111, 253, 283 to 307 | "target", "scar", "release contract", "reusable workflow" undefined. |
| P6 | should | 194 | `printshop` did not prove the release. |
| S1 | should | 345 to 358 | Font scan told three times. |
| S2 | should | 240, 279 | BROKEN rationale twice. |
| S3 | should | 33, 37, 141 | Licence paragraph, Python restatement, Chrome. |
| S4 | should | 60, 287 | Two halves of one pinning argument. |
| S5 | should | 360 to 364 | No picture of a successful first run. |
| S6 | should | 314 to 324 | "Other platforms" and "not tested" thin and scattered. |
| S7 | should | 357 | Missing blank line after the sidebar. |
| S8 | should | 116, 222 | Figures 2.1 and 2.2 will number in swapped order. |
| S9 | should | 120 to 135 | Table 2.3 claims the doctor's words and paraphrases them. |

Counted for the return: 1 block, 15 should (P1 to P6, S1 to S9).

## The one change

Fix P1 together with B1. The chapter's first command fails on the reference
platform, and the dev loop the design promises is missing. Both need a fact
the writer was not given, so both start with the controller adding to
facts-02. Then one writer pass can add the venv step before Example 2.1 and
the dev-render B-head under "The toolchain image".
