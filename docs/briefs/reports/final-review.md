# Final review: first outside reader

Read in order, preface through colophon, as an author who wants to build a
book with press 3.0.2 and has not seen the plan. docs/prose-contract.md and
docs/vocabulary.md were read last, only to name the rule a finding breaks.
Line numbers are from the files as read on 2026-11-11. Where a contradiction
could be settled against the press source, the entry says which side the
code supports.

Severity: **blocks** (a reader is misled or stopped), **should**, **may**.

Counts: blocks 1, should 17, may 21 (tagged entries in sections 1 and 2;
section 5's nine missing items repeat four of them and add five untagged).

## 1. Where I got lost

### Steps I could not carry out from the text

**blocks.** `book/chapters/11-the-art-department.md:383-410`, Example 11.3,
"The shape of art/commissions.md". Every inner closing fence reads
` ```text ` (lines 388, 397, 403, 409), which is an opening fence with an
info string, not a closer. A reader who copies this shape writes a file whose
fenced blocks never close, and `press art commission` ("sends the first
fenced block of each section") gets one block that runs to the end of the
file. Fix: change the four inner closers to bare ` ``` `. (The outer
four-backtick fence is correct.)

**should.** `02-installing-press.md:55-71`. Example 2.1 runs
`python3 -m venv ~/.press-venv`; the paragraph after it says that on Debian
and Ubuntu this fails until `sudo apt-get install python3-venv`. The
prerequisite comes after the step that needs it. Prose contract: "a warning
before the step it protects". Fix: move the `python3-venv` paragraph and its
command above Example 2.1.

**should.** `02-installing-press.md:75` and `:124` (Table 2.2): "A floating
tag such as `v3` ... moves forward to the newest compatible release" and
"Use it for most books. You receive fixes within the major version." The tag
floats in CI. On `hatter` the venv keeps whatever `pip` built on install day,
and nothing in Chapter 2, Chapter 14, or Appendix A says how to move a
workstation to the next `v3.x.y`. Fix: one sentence and one command after
Table 2.2: "To take a new release on your workstation, run `pip install
--upgrade "press @ git+https://github.com/clintecker/press@v3"`; the floating
tag moves on GitHub, not in your environment."

**should.** `03-the-shape-of-a-book.md:21-37`, Table 3.1 presents `--author`,
`--publisher`, `--place`, `--owner`. Appendix A (`a-command-reference.md:803-806`)
says all four are "Not listed by `--help`". The same is true of the whole
`press art enhance` subcommand (`a-command-reference.md:179`), `--print`,
`--subject` on `press illustrate`, `--json`, `--dry-run`, `--file`, `--model`,
`--count`, `--photo`, `--rounds`, `--max-claims-per-file`, `--overwrite`,
`--write-docs`, and `press verify-pages`: about twenty entries. A reader who
follows the Preface's advice ("check `press --help` and Appendix A ...
against the version you run", `00-preface.md:139`) will conclude that half the
book's options were removed. Fix: a Tip in Chapter 3 at Table 3.1 and one at
Chapter 11's first synopsis: "`press <command> --help` prints the argument
grammar only; the options in this table are accepted but not listed."
Appendix A already carries the flag per entry; the chapters do not.

**should.** `04-writing-the-manuscript.md:235`, `05-figures-and-plates.md:368`,
`08-verifying-the-artifacts.md:172-174` all name *tex/title-page-print.tex*.
The file is first explained at `10-front-matter-index-authorities.md:219`.
At Chapter 5 a reader does not know whether it is a file the press writes or
one they write. Fix: at `05-figures-and-plates.md:368` add the appositive
"(a hand-written title page for the print interior only; Chapter 10)".

**should.** `b-configuration-reference.md:335`: "The press sends you to the
file or to the index workflow instead of the shell." There is no index
workflow. Chapter 15 lists the four workflows (`15-the-desk-and-the-machines.md:137-144`)
and none builds the index. The wording comes from the press's own
`press config list` help text, which the book copies without comment. Fix:
"The press's help text names an 'index workflow'; at the time of this writing
no such workflow ships, so edit the file by hand."

**should.** `c-messages.md:303`, remedy for `missing text sentinel in PDF`:
"Then check that no word in it breaks with a hyphen at the end of a line."
This is the only place in the book that says LuaLaTeX hyphenation can break a
sentinel. Chapter 3 (`:220-226`), Chapter 6 (`:365-382`) and Chapter 8
(`:492`, "three usual causes") all omit it, and the verifier folds whitespace
only (`verify_pdf.py:318`). A reader who picks a long phrase, sees it fail
after a reflow, and reads Chapter 8's three causes is stopped. Fix: add the
hyphen case as the fourth cause at `08-verifying-the-artifacts.md:492` and a
clause at `03-the-shape-of-a-book.md:222`: "prefer short words; a word
hyphenated at a line end breaks the match."

**should.** `06-checking-the-manuscript.md:451`: "Appendix C, *Messages and
refusals*, holds the full list." It does not. Absent from Appendix C:
`gen_index: curated terms match nothing`, `gen_authorities: the ledger does
not hold`, `front matter needs these config/metadata.yaml keys`, `coverwrap
needs assets/cover.jpg`, every intake refusal (`crop the source, do not
stretch it`, `the luminance key would leave a ghost`), `no commissions.md`,
`retail edition declared while registrations are absent or pending`, the
commerce gate's `order and inspect a copy`, `trim is not writable`, `the
appendices are full`, and all `press migrate` messages. Appendix C says so
only for intake (`c-messages.md:558`). Fix: either add those entries (they are
all quoted in the chapters already) or change Chapter 6's sentence to "holds
the checker's and verifiers' messages" and add a one-line pointer table at the
head of Appendix C for the generators, intake, and config refusals.

**should.** `14-continuous-integration.md:205`: "Chapter 2 also pairs the
digest with the three-part press tag that the book pins, `v3.0.2` here in
place of `v3`." Example 14.4 directly above (`:200`) still installs
`press@v3`. The sentence describes a command the example does not show. Fix:
change line 200 to `'press @ git+https://github.com/clintecker/press@v3.0.2'`.

**should.** `13-registrations.md:92`: `press isbn assign` "mints the lowest
unused publication number". Unused according to what? The book shows the
block in one book repository. A small press with several titles on one
10-pack (the reader the Preface names at `00-preface.md:13`) has no way, from
the text, to keep two book repositories from minting the same number. Fix:
state the rule (the press knows only this repository's two ISBNs) and the
practice (keep one spreadsheet, or set `registrations.isbn.print` by hand from
it in every book but the first).

### Terms and files that appear before the book explains them

**may.** `00-preface.md:127`: "By the press's own second law, such references
are a convention, the weakest kind of guard." The laws arrive in Chapter 1.
Fix: "By a rule Chapter 1 explains, such references are a convention".

**may.** `01-introduction.md:181` shows `¶ check ✓ style, source, jargon`
right after the text has said the checker has four passes (`:146`, `:198`).
Three names, four passes, no comment. Fix: a clause in Table 1.1's `check`
row: "the phase line names three of the four; the self-test has no word of
its own."

**may.** `01-introduction.md:189` and Table 1.1 `:203`: "7 editions agree
with the manuscript" against eight editions in Table 1.2. The arithmetic
(six reflowable editions plus the PDF when `pdftotext` is present) lands at
`08-verifying-the-artifacts.md:294`. Fix: add "(Chapter 8 explains which
seven)" to the table row.

**may.** `03-the-shape-of-a-book.md:392` uses `press add appendix` and
`--front` a page before the synopsis at `:413`. Fix: swap the order of the
subsections "Lexical order and zero padding" and "Adding a chapter", or add
"(the next section introduces the command)".

**may.** `04-writing-the-manuscript.md:317`: "The key `scene-break` in
*config/aesthetic.yaml* chooses how press draws it." The aesthetic is defined
at `05-figures-and-plates.md:77` and treated in Chapter 9. Fix: gloss it
here: "in *config/aesthetic.yaml*, the book's visual identity (Chapter 9)".

**may.** `05-figures-and-plates.md:97-114`: Example 5.2 puts the chart in the
Alice book's "own fifth chapter" and numbers it "Figure 5.1", on a page of
the manual's own Chapter 5, whose figures are also 5.x. I read it twice. Fix:
move the example to Carroll's seventh chapter ("Figure 7.1").

**may.** `07-building-the-editions.md:486`: *build/cover-fragment.html* is
named once and never explained. Fix: delete it from the list or add "the
cover block the landing page includes".

**may.** `08-verifying-the-artifacts.md:140` and footnote `[^8-fallback]`:
"unless a helper renderer is present" and "the other renderer" are never
named. Fix: name it or cut the clause; the reader only needs "`pdftoppm` at
120 dpi".

**may.** `09-the-house-design.md:357`: "The chapbook example that comes with
press" is the first and last mention of a second example book. Fix: "a second
gallery example, a book of verse under *examples/*".

**may.** `10-front-matter-index-authorities.md:214`: "Do not stack a third
`titlepage` environment" without saying what the first two are. Fix: "(the
generated cover plate and title page already use two)".

**may.** `09-the-house-design.md:299-302`, Example 9.1: `ink: '171717'` is
quoted and `muted: 5C5C5C` is bare, with no word on why. The reason (YAML
reads an all-digit value as an integer) appears only at
`16-inside-the-press.md:118`. Fix: one sentence after the example.

**may.** `06-checking-the-manuscript.md:54` and `c-messages.md:35` describe
the three unfinished markers without printing them ("the common abbreviations
for 'to do' and 'to be determined' ... followed by ... the verb 'write'").
Chapter 6 gives the reason in passing (the source checks read fenced code);
Appendix C, the lookup place, does not. Fix: in Appendix C, "This book cannot
print the markers, because the checker would refuse the page."

**may.** `03-the-shape-of-a-book.md:386`: the refusal is given as
`FileNotFoundError("no manuscript files found under book/")`. A reader sees
Python, not a message. Fix: quote the message text alone.

**may.** Appendix A's sessions describe a book with no cover
(`a-command-reference.md:466-471`, `:1250-1255`) while Chapter 12 opens "The
Alice book here is a 6 by 9 paperback with cover art in *assets/cover.jpg*"
(`12-the-print-pack.md:19`). The reference should match the book's final
state or say which day of the story it shows.

### Examples whose output does not match the text

**should.** `a-command-reference.md:588-596`, Example A.6, shows
`"kind": "plate"` for the White Rabbit, which Example 5.1 declares with no
class. `05-figures-and-plates.md:89` says "The report gives a bare image the
kind `figure`", and `figures.py` has `DEFAULT_KIND = "figure"`. Chapter 5 is
right; the appendix capture is not from a bare image. Fix: either give the
appendix plate a `.plate` class in a sentence before the example, or change
the captured value to `"figure"` and keep Chapter 5's warning beside it.

**may.** `14-continuous-integration.md:241`: `press migrate` "treats a pin
such as `@v1.20.0` as an immutable one". The Preface dates the first commit
2026-07-17 and 2.0.0 four days later; a `v1.20.0` reads as an invented
number. Fix: use `@v2.3.1`, a release the book names elsewhere.

## 2. Where the book contradicts itself

Each entry quotes both places.

**should.** Commissions run once, or again.
`11-the-art-department.md:22`: "a prompt for an image model that the book
keeps in *art/commissions.md*, and press runs each commission once."
`11-the-art-department.md:425`: "Candidates number upward and never
overwrite. A second run adds *openai-2.png* beside the first." Also `:234`:
"The command suits a single plate that you want to try again." Fix: at line
22, "and press runs a commission only when you ask it to; the build never
does."

**should.** Which registrations print on the copyright page.
`10-front-matter-index-authorities.md:172` (Table 10.4): "The press sets one
line for each registration number the book declares, such as 'ISBN (print)',
'ISBN (ebook)', and 'LCCN'." `13-registrations.md:273`: "The copyright page
carries one line for each ISBN the book declares and one for the LCCN. The
ISSN does not print there." `gen_front_matter.py:142-147` prints the two
ISBNs and the LCCN only; Chapter 13 is right. Fix: Table 10.4, "one line for
each ISBN and for the LCCN; the ISSN does not print."

**should.** Whether `press config validate` reads *config/aesthetic.yaml*.
`03-the-shape-of-a-book.md:279`: "The one exception is *config/aesthetic.yaml*,
which has no typed model of its own." Then Example 3.6 (`:369`) and Example
A.4 (`a-command-reference.md:415`) print `config/aesthetic.yaml: ok`, and
Table 3.6 (`:348`) routes `name` through `book-colors` to that file through
`press config`. `11-the-art-department.md:100`: "The press's config
validation does not cover *config/aesthetic.yaml*, so nothing catches a
misspelled key." `b-configuration-reference.md:9` repeats the second
statement. A reader cannot tell what `ok` on that line proves. Fix: one
sentence in Chapter 3 after Example 3.6: "`ok` for the aesthetic file means
only that it parsed as YAML; no key is checked."

**should.** The tokens a Web palette may name.
`09-the-house-design.md:275`: "The tokens a palette can name are `paper`,
`paper-warm`, `ink`, `ink-soft`, `cloth`, `cloth-deep`, `foil`,
`foil-bright`, `foil-deep`, `hairline`, `link`, and `ornament`."
`11-the-art-department.md:140`: "`{accent}` ... The command reads
`web-palette.accent`"; `b-configuration-reference.md:314`: "The cover prompts
also read `paper` and `accent`." `cover.py:101` reads `palette.get("accent")`.
Fix: add to Chapter 9's list, "and `accent`, which only the cover prompt
reads."

**should.** How many commands reach the network.
`13-registrations.md:238`, quoting the press: "the one command that reaches
the network; ordinary builds never do." `a-command-reference.md:729`: "It
reaches the network, as `press cover`, `press illustrate`, `press art
commission`, and `press research` do." The quotation is the press
documentation's overstatement, and the book repeats it without the
correction Appendix A later makes. Fix: at Chapter 13, after the quotation,
"(the one command among the registration targets; the art and operator
commands reach their own services)".

**should.** Why the tour commits before the first build.
`01-introduction.md:142`: "the source archive holds only the files Git tracks,
so the tour commits the scaffold before the first build."
`03-the-shape-of-a-book.md:566`: "Before `git init`, `press all` still builds
and verifies *alice-source.zip*. A book outside any repository is archived
whole." The reason given in Chapter 1 is false for the case Chapter 1
describes (a fresh directory, no repository). Fix: in Chapter 1, "so the tour
commits the scaffold first, which is the habit the Source edition rewards
once the book lives in a repository."

**should.** Example 14.4 against its own caption sentence (quoted under
section 1 above): `14-continuous-integration.md:200` installs `@v3`;
`:205` says `v3.0.2`.

**may.** The absolute and the exception. `01-introduction.md:92`: "The law
also forbids verifying without rebuilding." `08-verifying-the-artifacts.md:25`:
"Verifying without rebuilding is forbidden by construction." Then, seven
times (`06:473`, `07:339`, `08:210`, `08:433`, `08:439`, `16:78`, `16:178`):
"The one exception is `press verify-formats`, which reads an existing PDF".
The book is honest, but it states the absolute first and spends seven
paragraphs taking it back. Fix: qualify it once, at `01:92` ("with one stated
exception, Chapter 8"), and say the exception once, in Chapter 8.

**may.** Tenniel's year. `01-introduction.md:255`: "Tenniel's 1865 wood
engravings". `04-writing-the-manuscript.md:325` and
`e-glossary.md:183`: "Tenniel's 1866 array". Both can be defended (cut in
1865, published in the 1866 issue); the book should pick one or say so.

**may.** Two colophons. `10-front-matter-index-authorities.md:162`: "The
press calls the page after the title page the *colophon*, although most
readers know it as the copyright page." `00-preface.md:91`: "A Colophon at
the very end describes the animal on the cover." Only the glossary
(`e-glossary.md:96`) says these are two different things. Fix: move that
glossary sentence into Chapter 10 at line 162.

**may.** Ingram casewrap deltas. `12-the-print-pack.md:193`: "IngramSpark
sets deltas of its own: 0.4375in wide and 0.25in high for its dust jacket,
and -0.185in wide for its casewrap." Table 12.4 (`:210`) gives the Ingram
casewrap as 14.3305 by 10.5 in; the height needs a 0.25 in delta the text does
not name. (Every other number in Example 12.2, Example 12.3 and Table 12.4
checks: house 0.5 in spine, KDP 0.56, Lulu 0.5105, 12.75 by 9.25 wrap, and the
check digit 7.) Fix: "and -0.185in wide and 0.25in high for its casewrap".

**may.** Two timeouts. `16-inside-the-press.md:124`: "Its HTTP client gives
every request a 30-second timeout by default." `13-registrations.md:244`
(Table 13.4): "Timeout 10 seconds". Both are true (the lookup overrides the
default), but the book does not say so. Fix: "by default; `press lookup`
shortens it to 10 seconds".

**may.** Press figures and plates on disk. `05-figures-and-plates.md:22`
defines a *plate* as "an unnumbered illustration"; `:130-135` then says the
List of Plates "appears when *assets/woodcuts/* holds any image file" and the
checker refuses "a plate on disk under *assets/woodcuts/*" with no reference,
while `:319` tells you to keep numbered figures in the same directory. The
word covers two sets. Fix: at line 132, "any image file under
*assets/woodcuts/*, plate or figure".

## 3. Where the prose reads as machine-written

The book's own Example 15.5 names the diseases; measured against it, the
manuscript has the first three. Counts are over the sixteen chapters unless
noted.

**The maxim at the paragraph's end.** 138 paragraphs of three or more
sentences close on a sentence of nine words or fewer, and a large share are
coined sayings: "A convention asks people to avoid it and hopes." (`01:82`),
"Nobody tests the press on Windows." (`01:116`), "The cure is a habit."
(`06:498`), "The press stops at the link." (`12:493`), "Neither is an
artifact." (`03:639`), "It is the press checking itself." (`A:1043`). Chapter
1 alone has more than the two-per-chapter quota the editorial passes enforce.
(Disease 1; prose contract Pass 1, "a one-line closer".)

**Counting the words of a quotation before giving it.** "in one plain
sentence" (`01:24`), "Each law fits in a line" (`01:70`), "in one sentence"
(`01:92`, `02:341`, `13:21`, `14:108`, `15:22`, `15:394`, `16:23`, `D:5`),
"in one clause" (`01:97`, `14:30`), "in one line" (`01:118`), "in fewer
words" (`08:25`), "in five words" (`09:230`), "in eight words" (`09:314`), "in
three sentences" (`11:63`). Seventeen times. Once is a flourish; seventeen is
a tic, and it is the same move each time: announce brevity, then quote.

**"plainly" as a verb of attribution.** "says so plainly", "is plain about",
"puts it plainly", "states the reason plainly", "gives the rule plainly":
seventeen occurrences (`00:137`, `01:66`, `01:78`, `02:43`, `03:645`, `04:142`,
`04:419`, `05:323`, `06:75`, `10:380`, `11:320`, `12:49`, `12:88`, `14:394`,
`16:354`, and two more). Together with "The press calls / the press's word
for / in the press's own words" (twenty-three) and "In the words of"
(twenty-two across chapters), every third page stops to certify that the
next clause is a quotation.

**The staged reason.** "X matters more than it looks" (`07:420`, `11:57`),
"promises more than it does" (`05:180`), "That is less of a gap than it
looks" (`15:109`); "for a reason" / "on purpose" / "that is deliberate" as
a sentence or opener, eleven times (`02:47`, `02:277`, `05:216`, `05:250`,
`07:367`, `08:51`, `13:228`, `14:30`, `16:100` and others). The shape is: a
short claim that something is intentional, then the reason. Disease 3
(self-annotation) in a quieter dress.

**The staged contrast.** "An exit status of zero tells you that a program
finished. It tells you nothing about whether the PDF has a cover." (`01:90`)
is excellent once. The same shape opens Chapter 8 (`08:17`, "It tells you
nothing about the pages inside the PDF") and recurs as "says nothing about" /
"proves nothing" eight times (`05:216`, `06:376`, `08:454`, `13:74`, `14:215`,
`15:127`). Disease 2 (X-not-Y rhythm).

**Text about the document.** "broken here to fit the page", "folded to fit
the page", "cut to fit the page": thirty occurrences, eight of them in
Chapter 8. Prose contract Pass 1 forbids "text about the document itself";
the Preface's conventions (`00:110`) already cover `...`, and one more
sentence there would retire all thirty.

**The chapter-end handoff.** Nine of sixteen chapters end on one sentence
of the form "The next chapter, *X*, does Y" (`01`, `02`, `03`, `04`, `05`,
`06`, `08`, `09`, `10`). Chapters 7, 11, 12, 13, 14, 15, 16 do not, and read
better for it.

**Re-glossing the same ten terms in every chapter.** "the Telegraphic
edition (plain text)", "the Single-leaf edition (the self-contained HTML)",
*scar* defined three times, *verifier* three, *sentinel* four, *aesthetic*
four, *target* three, *floating tag* three, the eight edition names listed in
full five times (`00:125`, `01:262-271`, `03:615`, `07:45`, `16:74`).
docs/vocabulary.md asks for this ("First use of each term in a chapter is
italic and defined in the same sentence"); docs/prose-contract.md asks for the
opposite ("define a term once, in italic, then reuse it"). The two documents
disagree and the manuscript followed the first. For a book read front to
back it is padding of the most visible kind.

**Uniform table-cell openers.** Every cell of Table 3.1 begins "This option
sets"; every cell of Tables 3.3, 3.4, 9.1 and 9.6 begins "It is a" or "It
runs"; every option table in Appendix A begins "This sets / This prints";
Table 11.3 begins "The command takes" seven times. Disease 2 at the scale of
the table.

### The five worst, with a fix each

1. `09-the-house-design.md:314`: "The house documentation gives the rule in
   eight words: 'restate a whole section when you touch it.'" Fix: "The house
   documentation's rule is 'restate a whole section when you touch it.'"
   Apply the same cut to the other sixteen word counts.

2. `08-verifying-the-artifacts.md:17`: "A build that exits with status zero
   tells you that pandoc and LuaLaTeX stopped without complaint. It tells you
   nothing about the pages inside the PDF." Chapter 1 made this point in the
   same words. Fix: begin the chapter at "Press opens every artifact it
   makes, renders or unpacks it, and compares it with the manuscript before
   it calls the build good."

3. `07-building-the-editions.md:420`: "The check step matters more than it
   looks." Fix: delete the sentence; the paragraph stands on "The known-bad
   fixtures run in `press check` and `press all`, and not in a bare
   `press pdf`." Do the same at `11:57` and `15:109`.

4. `06-checking-the-manuscript.md:498`: "The cure is a habit. Let the
   checker's own status reach the `&&`, and read its output when it fails."
   Fix: "Let the checker's own status reach the `&&`, and read its output when
   it fails." The sidebar's previous sentence ("Every program does its job,
   and whatever the check guarded goes out.") is the line to end on.

5. `08-verifying-the-artifacts.md:162`, `:169`, `:181`, `:253`, `:313`, `:390`,
   `:420`, `:427`: "here broken across two lines to fit the page", "It appears
   here on three lines to fit the page", "broken here to fit the page" (eight
   times in one chapter). Fix: add to the Preface conventions, after the `...`
   entry: "A message shown on more than one line in this book is one line in
   the terminal." Then delete every instance in the chapters and Appendix C.

## 4. The period voice: where it slips, where it is strongest

### Slips

- "truthy" (`02:277`, `08:317`, `D:147`): a 2010s word in a 1999 manual.
  "reads as true" or "counts as set" in each place.
- `FileNotFoundError("...")` (`03:386`), `ProviderSpec.check_selection`
  (`12:51`), the pytest node id
  `tests/test_ci_posture.py::test_every_action_is_pinned_by_full_commit_sha`
  (`14:74`): source-level identifiers in author-facing chapters. Chapter 16 may
  name modules; Chapters 3 and 12 should quote the message or the rule.
- "at the time of this writing" appears 41 times. The Preface (`00:127`)
  promises it for version numbers; the chapters attach it to counts of
  skills, lines of code, flags, and bugs. Keep it for the version and the
  release; for the rest, the plain present tense carries the date the Preface
  already states.
- The editorial "we" appears in the Preface, then rarely ("We recommend",
  `02:47`; "In our experience", `04:163`; "We suggest", `05:290`, `09:365`)
  and vanishes for whole chapters. An O'Reilly-era manual uses it steadily or
  not at all. Either voice is fine; the switching is noticeable.
- `15:297`: "Before `alice` drafts a cover brief for Chapter 11's commissions,
  for example, `alice` opens the `cover-design` skill." Two `alice`s in one
  sentence; "she" is period-correct and the Preface established her.
- The agent material (Claude Code, the Workflow tool, "an agent reads before
  it writes", `claude -p`, `--permission-mode acceptEdits`) cannot be made to
  sound like 1999, and the book does the right thing by defining each term
  flatly. The one place it strains is `15:328-334`, where an entire modern
  command line is printed as an example the reader will never type. A
  sentence would do.

### Strongest

- The four laws (`01:68-108`), each with a scar beside it; "A convention asks
  people to avoid it and hopes" is the best sentence in Chapter 1.
- The dash law (`04:138-151`): "the rewrite is usually the better sentence."
- The ties (`04:413-419`): "A name broken between its initials stops looking
  like a name. None of these is an error a checker could catch in the
  manuscript, because the line breaks do not exist until the page does."
- Recto and verso (`05:172-174`): the trade explained in a paragraph, and the
  reason for `wrap-inner` follows from it without a push.
- The KOMA spelling trap (`09:53-59`): "The first mistake is silent, and the
  second costs paper."
- The spine arithmetic (`12:84-147`) and the quiet-zone sidebar (`12:253-259`):
  "The verifier was right about the pixels."
- "Why pending is a word" (`13:145-151`) and the footnote "The scaffold's
  default for the place is accurate, as far as it goes." (`13:319`).
- The footnotes generally: the printer's devil (`10:414`), roman numerals on
  cornerstones (`10:416`), the pilcrow (`01:309`), "Carroll ... never once
  missed a deadline" (`00:165`), "A counsel gives advice and does not sign the
  papers" (`15:402`).
- The Preface's "Where neither says anything, neither do we" (`00:7`).

## 5. What is missing, and what is padding

### Missing

1. **Taking a new release on the workstation** (section 1 above). The book
   explains the floating tag three times and never gives the `pip` command
   that follows it.
2. **A shared ISBN block across titles** (section 1 above). The Preface's
   small-press reader will hit this in the first year.
3. **Hyphenation and sentinels** in the chapters that teach sentinels
   (section 1 above).
4. **Which options `--help` hides**, said once where the options are taught.
5. **A symptom index.** Appendix C is organized by the command that prints
   the message. A reader with a blank page, a missing cover, a wrong spine,
   or a moved figure does not know which command's section to read. One
   table at the head of Appendix C ("What you see / Where to look") would
   serve the reader the Preface describes. Table 8.7 is the seed.
6. **The book's own numbers.** Appendix D says the press "states no number
   for how long a build takes". This manual is itself a press book of about
   130,000 words; its own `press all` time on `hatter` and in CI, its page
   count, and its `dist/` sizes would give the reader the scale that the
   three-chapter example (23 pages) cannot.
7. **Upgrading a scaffolded book's workflows.** Chapter 15 (`:146`) says no
   command refreshes *.claude/workflows/* after `press new`, and `press
   workflows` reports `DIFFERS`. It never says how to refresh them (copy from
   the path `press skills`/`press workflows` prints). One sentence.
8. **What `press config validate` proves for each file** (section 2 above).
9. **The reason to refuse KDP's free ISBN** (`13:50-52`): the warning gives
   none. One clause ("it names Amazon as the publisher of record and cannot
   follow the book to another printer").

### Padding

Retellings, by count across the chapters and appendixes:

- The verify-formats exception: 7 (`06:473`, `07:339`, `08:210`, `08:433`,
  `08:439`, `16:78`, `16:178`), plus the no-stale warning box four times
  (`03:627`, `07:343`, `08:453`, `16:180`).
- The first-run font scan: 6 (`01:173`, `02:367-377`, `03:537`, `07:214`,
  `A:909`, `D:124`).
- "`press all` does not build the print pack": 6 (`01:279`, `03:625`,
  `07:444`, `08:447`, `12:159`, `A:86`).
- The sentinel-at-chapter-opening warning: 4 boxes (`01:286`, `03:225`,
  `04:312`, `06:379`) plus `B:83` and `C:47`.
- The retired `macos-14` runner: 4 footnotes (`02:335`, `14:329`, `16:252`,
  `D:120`).
- Lulu's preflight (transparency, 602 PPI): 4 (`05:366`, `11:316`, `12:19`,
  `12:269`), plus the same tip twice (`05:371`, `12:272`).
- `CI=false`: 4 (`02:277`, `08:317`, `16:146`, `D:147`).
- The 11.5 percent cover: 3 (`01:94-102`, `08:27`, `16:226`); the jargon lint
  "twice": 3 (`06:299`, `15:303-309`, `16:100`); `fonts-linuxlibertine`: 3
  (`01:311`, `02:195-210`, `09:78`) plus `D:59`; `tocdepth`: 3; `hypcap`: 3;
  the `Popen` gate: 2 (`15:400`, `16:128-132`); the `Mr.` tie test: 2
  (`04:439`, `16:232`).
- Whole sections: Chapter 1's "How to read this book" (`01:297-305`) restates
  the Preface's "Organization of this book"; Chapter 16's "Trust receipts"
  (`16:254-268`) restates Chapter 14's "Receipts" (`14:211-225`) with the same
  twelve-layer list verbatim; Chapter 4's `:52-66` restates Chapter 3's
  sorting and `press add`; Appendix D restates about two thirds of Chapter 2.
- `press wordcount` on the fresh scaffold, verbatim twice (`01:162-166`,
  `03:543-547`); the HTML-comment caveat three times (`01:160`, `03:549`,
  `07:509`).

Cutting each retelling to a pointer would remove on the order of 8,000 to
10,000 words and make the chapters that remain read as a book rather than as
sixteen self-contained briefs. The chapters are each correct alone; together
they repeat.

## 6. The ten best passages (protect these)

1. `01-introduction.md:80-86`, the second law and its two examples: the
   height cap as a generator, `press check` as a checker, this book's style
   guide as a convention "now also exists as regular expressions".
2. `01-introduction.md:94-102`, sidebar "The cover that passed at 11.5
   percent": the whole philosophy of the press in three paragraphs.
3. `04-writing-the-manuscript.md:138-151`, the dash law and Example 4.3.
4. `04-writing-the-manuscript.md:413-419`, the ties and why no checker can
   catch them.
5. `05-figures-and-plates.md:172-174` and `:250`, recto and verso, and the
   rule that a wrapped plate cannot carry an `art:` comment (the single most
   useful gotcha in the book).
6. `06-checking-the-manuscript.md:491-499`, sidebar "The red check that went
   out green": "Every program does its job, and whatever the check guarded
   goes out."
7. `08-verifying-the-artifacts.md:216-230`, the three witnesses: "The press
   chooses the witness, so it tests a line that you never thought to
   protect."
8. `09-the-house-design.md:371-397`, "Why a design change is a new major":
   from a hyphenation penalty to the width of the spine in one paragraph.
9. `12-the-print-pack.md:84-147`, the four spine shapes, Example 12.2, and
   the correction of the press's own Lulu guide at `:143` and `:457`: the
   book reading its subject critically.
10. `15-the-desk-and-the-machines.md:370-396`, "Why the diseases are
    hard-coded": "None of them can see it, because each one reads only its
    own file." The chapter earns the right to diagnose the book's own prose.

Honorable mentions: `13:145-151` ("Why pending is a word"), `14:363` (rename
the CHANGELOG section when a tag fails), `11:492` (the Gemini key fails only
after OpenAI is paid), `16:116` (the dedication that contains "secret"), and
the colophon's cuttlefish.

## Status

- Blocks: 1 (Example 11.3's inner fences). Should: 17. May: 21.
- Worst three: the malformed commissions.md example (`11:383-410`); the
  floating tag that never floats on the workstation (`02:75`, `02:124`, no
  upgrade command anywhere); the sentinel hyphenation rule that lives only in
  Appendix C (`C:303`) while Chapters 3, 6, and 8 teach sentinels without it.
- Verdict as a reader: I could build, check, verify, and print a book from
  this manual, and I would trust its numbers; every spine, wrap, check-digit
  and margin figure I recomputed came out right. I would also notice by
  Chapter 8 that the same twelve facts were being told to me again in each
  chapter's own words, and that the prose has a metronome.
- The one change: one editing pass that deletes every second and later
  telling (section 5's list), the seventeen word-counted quotations, the
  thirty "to fit the page" asides, and the paragraph-closing maxims above two
  per chapter. The facts would be untouched and the book would be a fifth
  shorter and read as one voice.
