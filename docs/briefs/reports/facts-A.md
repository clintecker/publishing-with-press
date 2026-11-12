# Fact check: Appendix A, Command reference

File: `book/appendices/a-command-reference.md`, checked against
`docs/briefs/facts/facts-A.md` (17.1-17.6, the shared context, section 20)
and, as the writer's report declares for its descriptions and sessions, the
same fact base's slices facts-03, 06, 07, 08, 10, 11, 12, 13, 14, 15, 16, and D.

Sessions the writer captured from press 3.0.2 were rerun on fresh scratch
books made with `press new alice --author "Lewis Carroll" --owner
wonderland-press` under the session scratchpad (`.../scratchpad/cap/`),
never inside this repository, with `~/code/.pwp-venv/bin/press` (3.0.2,
an editable install of the press checkout). Nothing that spends money was
run (no `cover`, `illustrate`, `art commission`, `improve`, `research`, or
`aesthetic "<brief>"`). Reruns that match character for character, apart
from line wrapping (Drifted 1): `add`, `config get`, `config set trim`,
`config list --file`, `config unset --dry-run`, `config validate` (Example
A.4), `isbn status` (with the docs' block), `onix`, `pcn` (Example A.7),
`migrate status`, `desk` (exit 2), `figures` (Example A.6), `art accept`,
`wordcount`, `markdown`, `style`/`check` line formats (Example A.1),
`doctor` (Example A.5), `new`, `skills`, `workflows`, `--version`, bare
`press` (exit 2). Every synopsis line, flag, and default matches facts-A
17.2. Every flag 20.A.23 marks as absent from `--help` is present and
marked "Not listed by `--help`", and so is `verify-pages`; I confirmed each
against `press <cmd> --help`. Table A.19 matches 17.4 and Table A.20
matches 17.5.

**Status: fails; eight findings block.**

Counts: Unsupported 2, Contradicted 6, Drifted 13, Missing 4.

Worst finding: Contradicted 2. The `press source` entry tells the reader
that a book with no Git repository gets an empty archive. A rerun shows the
opposite: outside any Git repository, press 3.0.2 archives every file in
the book (14 files on a fresh scaffold). The reader is told an archive is
harmless when it holds the whole book. The fact base's own probe (facts-03
S5) is the source of the error and needs correcting too.

## 1. Unsupported

1. Line 167-168, `press art commission` example: `$ ls
   art/candidates/plate-white-rabbit` / `openai-1.png  openai-2.png`, and
   line 161, "A second run would add *openai-3.png* and *openai-4.png*". No
   fact file captures this listing, and it cannot be rerun without spending
   money. facts-11 8.3 gives only "Candidates are written to
   `art/candidates/<target, ":" replaced by "-">/<model>-<n>.png`. They
   number upward and never overwrite." It does not say that numbering starts
   at 1. Fix: cut the `ls` and its output, or show them as a pattern
   (`openai-<n>.png`). Soften line 161 to "A second run adds new candidates
   and never overwrites the first ones."
2. Line 1237, `press verify-print`: "so a code block in colour makes the
   verifier refuse it". I searched facts-08 6.1, facts-12, and facts-04. The
   files say that code is highlighted "in colour, in the PDF, EPUB, and web
   editions" (facts-04 l.474) and that the print check fails on colour
   (facts-08 6.1 item 11). Neither says the print interior highlights code.
   **My rerun confirms the claim.** A fresh scaffold with one Python fenced
   block failed `press verify-print` with exit 1 and `print profile: colored
   ink on pages [6] (...)`. The claim is true, but the writer's fact file
   does not support it. Fix: add the capture to the fact base, or soften to
   what the file says: "The interior must be single ink except on a colour
   profile; colour on any page makes the verifier refuse it."

## 2. Contradicted

1. Line 31, Table A.1, `--front`: "With `chapter`, this makes
   *book/chapters/00-preface.md* with the heading `# Preface
   {.unnumbered}`." facts-03 (`add.py`): "**`chapter --front`** creates
   `00-<slug>.md` with `{.unnumbered}`." The preface is only the docs'
   example (`press add chapter preface --front`). Rerun: `press add chapter
   x --front` made `book/chapters/00-x.md` with heading `# X
   {.unnumbered}`. On a scaffold, `press add chapter preface --front`
   refuses, because the template already has `00-preface.md`. Fix: "With
   `chapter`, this makes *book/chapters/00-<name>.md*, an unnumbered chapter
   before the numbered ones."
2. Lines 1098, `press source`: "A book with no Git repository still gets an
   archive, but it holds no files, so commit the manuscript before you rely
   on it." This comes from facts-03 S5 ("the probe saw `archived 0
   files`"), and the rerun contradicts it. On a fresh scaffold outside any
   Git repository (`git rev-parse` says "not a git repository"), `press
   source` printed `archived 14 files; excluded dirs ['.git',
   '__pycache__', 'build', 'dist']`, and `unzip -l` lists 14 files. `archived
   0 files` appears only when the book sits untracked *inside* another Git
   repository: I reproduced it that way, with one `skipped <file>
   (untracked; publication is for committed work)` line per file. The S5
   probe almost certainly ran inside a parent repository. Fix: "Inside a Git
   repository, it archives only the files Git tracks and skips each
   untracked file with a note, so commit the manuscript before you rely on
   the archive." Cut the no-Git sentence, or state the rerun: "Outside any
   Git repository, it archives every file in the book." Correct facts-03 S5
   too (and facts-02/03 20.A.26, which rest on the same inference).
3. Line 929, `press print`: "At the time of this writing, the print-safe pass
   copies only the JPEG files at the top of *assets/*, the images in
   *assets/woodcuts/*, and the logo. Keep every interior image in one of
   those places." This is facts-A 20.B.2, which the file lists under "Code
   behaviors that look like bugs. Do not document them as features" and marks
   "Unverified". It also contradicts line 925 in the same entry, "Every image
   goes through the print-safe pass". Fix: cut the two sentences. If the
   advice must stay, hedge it to the file's level: "A figure outside
   *assets/woodcuts/* and the top of *assets/* may be missing from the print
   interior (unverified); check the proof."
4. Line 722, `press lookup`: "It is the one command that reaches the
   network". facts-13 11.7 says this, but only of registration commands. The
   rest of the fact base and this appendix contradict it: `press cover` and
   `press illustrate` POST to OpenAI and `press art commission` to OpenAI and
   Gemini (facts-11 8.2), and `press research` runs with WebSearch and
   WebFetch (facts-15 14.1). Fix: "It is the one registrations command that
   reaches the network ('ordinary builds never do'), and it never issues a
   number."
5. Lines 1026 and 1036-1042, `press selftest`: "prints one line when all
   pass" / "a passing run prints one line", and the session shows only the
   success line, with no `...`. Rerun: before `Selftest passed: 29 checks,
   ...` the run printed about twenty lines (`scaffolded policy-proof ->
   ...`, `archived 14 files; ...`, `skipped escape.txt (symlink; never
   dereferenced)`, and more scaffold lines). facts-16 16.4 calls it "The
   success line", not the only line. (The rerun used the editable install;
   the scaffold checks are not repo-file checks, so a wheel should print them
   too.) Fix: "and ends with one line when all pass", and put a `...` line
   before the success line in the session.
6. Line 514, `press doctor`: "A broken optional tool also makes the machine
   not ready." This is 20.B.14 ("A broken *optional* tool fails doctor"),
   which the file lists among behaviours that look like bugs and are not to
   be documented as features. Fix: cut the sentence, or hedge it as
   behaviour at the time of this writing, not as design.

## 3. Drifted

1. Line wrapping in captured output. The brief allows only the slug change
   and `...` elision, but these sessions fold one real line into two or
   three: `art accept` (l.130-131), Example A.1 (l.223-228), Example A.2
   (l.345-346), `config list` (l.307-311), `desk` (l.494-495; the real
   output is one line, `press desk needs the optional interface: pip install
   'press[tui]'`, and the fold makes the `pip install` look like a separate
   message), `migrate status` (l.775-776), Example A.7 (l.883-884),
   `selftest` (l.1040-1041), `verify` (l.1171-1173), Example A.8
   (l.1197-1199), `pdf` (l.911-912), and Example A.9 (l.1292-1296). The
   writer's report says wraps use "a four-space continuation", but four of
   them have none (`verify`, A.8, `pdf`, A.9), so the reader cannot tell a
   continuation from a new line. Fix: print the lines unbroken (as the
   facts-B review asked), or at least indent every continuation the same
   way and say so in the session conventions on line 15.
2. Line 473, `press coverwrap`: `coverwrap needs assets/cover.jpg`. Rerun:
   `coverwrap needs assets/cover.jpg (the front board art)` (exit 1). facts-12
   10.5 quotes only the short form, but the session presents the line as
   output. Fix: print the full line.
3. Line 1237, `press verify-print`: `print profile: colored ink on pages
   [N]` is quoted as the message, but facts-08 6.1 gives `print profile:
   colored ink on pages [...] (a colored cover plate in a hand-authored
   tex/title-page.tex belongs on the wrap; supply tex/title-page-print.tex
   without it)`, and the rerun printed that. Fix: quote it as `print profile:
   colored ink on pages [...]` followed by "and advice on the title page", or
   quote it in full.
4. Line 13: "A command name press does not know does the same, after press
   suggests the nearest command it knows." Rerun: press prints the usage
   *first*, then `unknown target: verifyy` / ``did you mean `press verify`?
   (see `press --help`)``. With no near match (`press bogus`) there is no
   suggestion, only ``see `press --help` for the full command list``. facts-A
   17.4: "prints `unknown target: X` plus a suggestion". Fix: "A command name
   press does not know does the same, and then press names the nearest
   command it knows, when there is one."
5. Line 31, Table A.1, `--front` with `appendix`: "it takes the letter `a-`
   instead of counting down from `z-`." facts-03: "**`appendix --front`**
   counts up from `a`." Rerun: a second `--front` appendix got `b-foo.md`.
   Fix: "it counts up from `a-` instead of down from `z-`."
6. Line 25, `press add`: "A chapter takes the next free number". facts-03:
   "NN one past the highest existing chapter". With 01 and 03 present, the
   next is 04, not the free 02. Fix: "A chapter takes the number after the
   highest one in use".
7. Lines 141-153, `press art commission`: `--model`, `--count`, and
   `--photo` do not appear in the help grammar (facts-A 17.1: `art ...
   commission [targets] | accept <file> --as <target>`; confirmed by `press
   art --help`), but Table A.4 does not mark them, against the convention
   set on line 13. 20.A.23 leaves them out, so this is the file's omission
   carried over. Fix: add "Not listed by `--help`" to all three rows.
8. Lines 1293-1296, Example A.9: the path `/Users/alice/alice` is made up.
   The capture (facts-15 14.1) elides it as `…/demo`, and the rerun prints
   the real absolute path. The wrap also splits the path in the middle of
   the name (`.../workflows/` / `editorial-passes.js`). Fix: `pinned:
   .../alice/.claude/workflows/editorial-passes.js (matches installed press
   3.0.2)` and `invoke: Workflow({name: "editorial-passes", args: {root:
   ".../alice"}})`, each on one line.
9. Lines 1083-1084, `press skills`: the capture (facts-15 14.6) and the
   rerun separate the name and the path with a tab. The session uses two
   spaces. Fix: keep the tab, or say the columns are tab-separated.
10. Line 118, Table A.3, `--as cover`: "Its aspect ratio must be within 3
    percent of the trim's." 20.A.17: the check "reads `metadata.trim`
    (default 6×9), not the profile. A 5×8 book's cover is checked against
    1.5, not 1.6." The appendix's own `config list` entry (l.292) tells the
    reader that the trim comes from `print.profile`, so "the trim's" reads
    as the profile's. Fix: "within 3 percent of the legacy `trim` field's
    ratio (6 by 9 unless set), at the time of this writing, not the
    profile's".
11. Line 112, `press art accept`: "press refuses an opaque plate on a
    gradient or textured ground". facts-11 8.6 runs the flat-ground test
    only for a single-ink plate. "An opaque colour plate is flattened onto
    white with its colours unchanged." Fix: "press refuses an opaque
    single-ink plate on a gradient or textured ground".
12. Line 86, `press all`: "`press all` builds neither the print interior nor
    the cover wrap". 20.B.13: "builds neither `print` nor `coverwrap`, but
    the commerce release gate (ordering-enabled books only) does." Fix: add
    "unless print ordering is on, when the commerce gate builds them".
13. Line 299, Table A.7, `--json`: "with each field's path, file, kind,
    type, help, and whether it is required". The rerun's objects also carry
    `choices` and `manager`. Fix: add "its choices, and its manager", or
    write "with each field's path, file, kind, type, help, and more".

## 4. Missing

1. `press verify-print` (l.1237-1246): without a cover it prints `no
   assets/cover.jpg; interior verified, wrap not built` (facts-07 5.3). The
   session is only `...`; this line would give it real content.
2. `press render` (l.975-986): the writer's report says the page-image names
   are not stated, but facts-A 17.2 and facts-07 5.1 give
   `build/rendered-book/page-*.png`. The `ls` session could show
   `page-*.png` instead of `...`.
3. `press migrate` (l.765): a reader on v3 who runs `press migrate` (plan)
   is offered v4, which does not exist (20.B.21; facts-14 12.6 "Captured on
   a v3 book"). The entry need not show the plan, but a hedge such as "On
   press 3, the newest major, there is nothing to move to yet" would stop a
   reader from trusting the proposal.
4. `press isbn` (l.699-710): with no block configured, `status` prints `no
   registrations.isbn-block configured; set the prefix and size your ISBN
   agency gave you (e.g. prefix: 978-1-960780, size: 100)` (facts-13 11.2)
   and, on rerun, exits 1. That is what a first-time reader sees first. Also
   useful there: the block is set with two `press config set` calls
   (`registrations.isbn-block.prefix`, `.size`); a single `--json` set of
   `registrations.isbn-block` is refused with exit 3 (rerun).
