# Checking the manuscript

::: {.in-this-chapter}
> **In this chapter:**
>
> - The four passes
> - Source checks
> - Checking the checkers
> - The style audit
> - The jargon lint and the watchlist
> - House rules
> - Sentinels and the page floor
> - Reading the output
> - Exit status and what depends on it
:::

Before a book goes to press, it passes through one command. That command is `press check`, and it runs before any edition exists. It finds the faults that a reader would see in print and stops the book before they reach the typesetter. `press all` and the CI build run it ahead of every edition, and a bare format target such as `press pdf` does not.

## The four passes

*The checker* is `press check`, the target that reads the manuscript and its configuration and refuses a book that breaks the house's law. It runs four passes in a fixed order and stops at the first pass that fails. A book with a missing chapter file therefore never reaches the style audit, and a book with an em dash never reaches the jargon lint.

Table 6.1 names the four passes in the order press runs them.

| Pass | Meaning |
|------------------|------------------------------------------------------------|
| Source checks | Press confirms that every chapter file exists and has a heading, that the metadata names the book, and that every configuration file has the right shape. |
| The checker self-test | Press runs its own rules over a set of files that must fail, and over one file that must pass, before it trusts those rules with your manuscript. |
| The style audit | Press reads every audited file for refused characters, refused phrases, bad headings, and long paragraphs. |
| The jargon lint | Press reads the chapter files against the watchlist and refuses any term with the rewrite status. |

Table: Table 6.1. The four passes of press check

The source checks come first, because the later passes read files that the source checks confirm are there. Press proves its rules second, before they read a line of yours. The two passes that read prose come last.

@fig:checker-guards-the-build shows the checker as `press all` runs it, between your files and the editions. Everything to the left of the large box is the manuscript and its configuration. Everything to the right is an edition, and `press all` builds none of it until all four passes succeed. A bare `press pdf`, `press epub`, or other format target goes straight to the build and runs none of the four passes. The `press verify` target builds the Print edition (PDF) the same way, without the checker, and then runs the PDF verifier.

![The checker as press all runs it](assets/woodcuts/06-01-checker-guards-the-build.png){#fig:checker-guards-the-build .diagram width=full-measure fig-alt="A left-to-right diagram. Chapter and config files enter a box named press check that holds four smaller boxes in a row. A pass arrow leads on to the builds of press all, and a fail arrow drops to a stop box."}

<!-- art: ARCHETYPE pipeline, left to right. Left: two dog-eared file icons stacked, labeled in small monospace "book/chapters/*.md" and "config/*.yaml". Center: one large square-cornered box labeled "press all" in small italic above it and "press check" at its top. Inside it, four rounded process boxes in a row joined by small arrows, labeled in order "source checks", "checker self-test", "style audit", "jargon lint". Right: an arrow labeled "pass" in small italic runs from the large box to a vertical stack of three rounded boxes, "Print edition", "Circulating edition", "Chapter edition". From the bottom of the large box a second arrow labeled "fail" drops to a small rounded box with a 40% gray drop shadow, labeled "stop (nonzero exit)". The reader should see first that press all reaches its builds only through all four boxes. -->

The `press style` target runs the style audit alone, without the other three passes. It is the quicker command while you revise a single chapter.

::: {.tip}
> **Tip:** Run `press style` while you revise, and run `press check` before you commit. The second command runs the same audit, and it also proves the rules before it applies them.
:::

## Source checks

The first pass is `check_source`. It reads the manuscript as a set of files and the configuration as a set of facts, and it reads no sentence for style. Its faults are structural: a file that is not there, a chapter with no title, a key the book forgot to set.

For each chapter file, the source checks look for four faults. A file the book lists and the disk lacks is a missing source file. A file whose body runs under 80 characters is suspiciously short. Press refuses a file with no level-one heading, because it has no chapter title. Press also refuses a file that still holds one of three unfinished markers, and quotes the marker.

Two of the markers are placeholders: the common abbreviations for "to do" and "to be determined", each in capitals and followed by a colon, a space, and the verb "write". The third is the scrambled Latin that typesetters use for dummy copy, in its usual two-word opening. The source checks read fenced code for the markers too, so not even an example in a chapter can hold one.

The source checks then read *config/metadata.yaml*. The checker requires four keys: `title`, `author`, `description`, and `slug`. If one is absent, press refuses the book with `metadata missing <key>:` and the key's name. The `description` requirement surprises people, because a one-sentence blurb looks optional. The Alice book set its description with `press config set` on its first day, so it passes.

The rest of the first pass covers the book's other configuration. Table 6.2 lists what it reads after the chapter files and the metadata.

| Check | Meaning |
|------------------|------------------------------------------------------------|
| Registrations and commerce | Press validates any ISBN, LCCN, or ISSN the book declares, and it refuses a retail book whose ISBNs are missing or pending. Chapter 13, *Registrations*, describes the numbers. |
| Sentinels | Press confirms that each phrase in `verify-sentinels` appears in the manuscript. The section "Sentinels and the page floor" later in this chapter describes them. |
| Orphan plates | Press refuses a plate image that no chapter references. Chapter 5, *Figures, plates, and illustrations*, describes plates. |
| Figure placement | Press refuses a figure whose placement is not valid. Chapter 5 describes the placements. |
| Config file shapes | Press validates the shapes of *config/index-terms.yaml*, *config/authorities.yaml*, *config/front-matter.yaml*, and *config/house-rules.yaml*. |
| Print feasibility | Press compares the trim, the binding, and the ink against the provider's catalog and refuses a book the provider cannot print. Chapter 12, *The print pack*, describes the providers. |

Table: Table 6.2. What the source checks read besides the chapters

When every source check passes, press prints one line, `Source checks passed: N ordered Markdown files`, with the number of manuscript files it read, in order. In a fresh scaffold, the line reports 1, for the preface alone. The source checks do not read prose, so a chapter full of em dashes still passes them.

## Checking the checkers

Press calls the second pass, `check_the_checkers`, the *checker self-test*. It proves on every check that each rule can refuse something, and the press puts the reason plainly: "A rule that cannot fail is not a rule." It runs the style audit and the jargon lint over a set of files that the rules must refuse. If any of them gets through, the check fails.

A *known-bad fixture* is a Markdown file that the checker must reject. The press package carries 19 of them, and the checker also reads every Markdown file in your book's *tests/known-bad/* directory. Each fixture targets one rule, and every packaged fixture declares which rule must catch it.

### The expect comment

A fixture declares its rule with an HTML comment, as Example 6.1 shows. The text after the colon is the rule's name, and it must match part of the diagnostic that the rule prints. Give each fixture exactly one expect comment, because press reads the first one it finds.[^6-first-expect]

**Example 6.1. tests/known-bad/very-unique.md in the Alice book**

```text
<!-- expect: very unique -->
# Fixture

This sentence is very unique.
```

The match is generous. The expected text must appear as a substring of at least one diagnostic that the fixture draws, and case does not count. A rule labeled "very unique (unique does not grade)" therefore satisfies the expectation "very unique". If the fixture draws other diagnostics as well, press prints each one as a note, and the checker self-test still passes. A fixture with no expect comment needs only to draw some diagnostic, from any rule.

The press package also holds one *known-good fixture*, a file named *clean.md* that must draw no diagnostic at all. It catches the opposite fault from the known-bad set: a rule so broad that it refuses ordinary prose.

### What the checker self-test prints

@fig:fixture-round-trip follows one fixture through the checker self-test. The checker reads the fixture, collects every diagnostic it draws, and looks for the declared rule among them.

![A known-bad fixture's round trip through the checker self-test](assets/woodcuts/06-02-fixture-round-trip.png){#fig:fixture-round-trip .diagram width=full-measure fig-alt="A flowchart. A fixture file with an expect comment goes through the style audit and the jargon lint, then reaches a question about whether its rule fired. Yes leads to a pass, and no leads to a failure message."}

<!-- art: ARCHETYPE flowchart, top to bottom. Top: a dog-eared file icon labeled "tests/known-bad/very-unique.md", with its first line shown inside in small monospace: the HTML comment that holds "expect: very unique". Arrow down to a rounded process box "style audit and jargon lint". Arrow down to a diamond "did the declared rule fire?". From the diamond, an arrow labeled "Yes" in small italic runs right to a rectangle "fixture passes". An arrow labeled "No" runs down to a rectangle with a 40% gray drop shadow holding, in small monospace on two lines, "very-unique.md: expected rule 'very unique'" and "did not fire (no diagnostics at all)". The reader should see first the No branch, which is the failure that keeps a dead rule out of the checker. -->

The checker self-test has three ways to fail, and Example 6.2 gives the message for each, folded to fit the page. The text in angle brackets stands for the fixture's name, the rule, and the diagnostics.

**Example 6.2. The three checker self-test failures**

```text
<fixture>: expected rule '<rule>' did not fire (<up to 3
    others or "no diagnostics at all">)
<fixture>: no checker rejected a known-bad fixture (and it
    declares no expected rule)
<fixture>: a checker rejected the known-good fixture: ...
```

The first message is the common one. It names up to three diagnostics the fixture did draw, which usually shows you what went wrong. If your fixture expects "very unique" and draws only a curly-quote complaint, the fixture has a typing fault. Your rule never had a chance to fire. If the parenthesis says "no diagnostics at all", the rule does not work, or it is absent from *config/house-rules.yaml*.

When every fixture behaves, press prints one line that counts them, beginning `Checker self-test passed: 19 known-bad fixtures`. The count is 19 for a book with no fixtures of its own, and it rises by one for each file in *tests/known-bad/*.

### Writing a fixture

A book's fixtures go in *tests/known-bad/*, one rule to a file. Press judges them as book prose, under the book's own banned patterns. A fixture is the only way to show, on every check, that a pattern you added to *config/house-rules.yaml* still catches what you wrote it to catch.

To add a fixture for a banned pattern:

1. Create the directory, if the book does not have one yet:
   `$ mkdir -p tests/known-bad`
2. In your editor, write the fixture as *tests/known-bad/very-unique.md*, with one expect comment and one sentence that breaks the rule, as in Example 6.1.
3. Run the checker before you add the pattern:
   `$ press check`
   The checker self-test fails with `expected rule 'very unique' did not fire (no diagnostics at all)`. That failure shows that the fixture is read.
4. Add the pattern to `banned-patterns` in *config/house-rules.yaml*, as the section "House rules" later in this chapter describes.
5. Run the checker again. The checker self-test line now counts 20 fixtures.

Your banned patterns also apply to the packaged fixtures, since press judges those as book prose too. A packaged fixture can then draw a second diagnostic from a rule of yours, and press prints it as a note. A note count that rises after you add a rule means your rule matches text in one of the packaged fixtures.

::: {.tip}
> **Tip:** Write a fixture in the same commit as the banned pattern it tests. If the pattern is wrong, the checker self-test tells you before the pattern reads a single chapter.
:::

The fixtures run in `press check` and in `press all`, and a bare `press pdf` does not run them. A pattern you change between two runs of `press pdf` gets no test until the next full check.

[^6-first-expect]: The press documentation says the expect comment may sit anywhere in the file. The code reads the first expect comment it finds.

## The style audit

The third pass is `style_audit`. It reads every audited file line by line and refuses the characters, phrases, headings, and paragraphs that the house does not print. The audited files are the manuscript under *book/* and the audit directories.

The *audit directories* are the directories a book names under `audit-dirs` in *config/house-rules.yaml*, outside the manuscript, that the style audit reads with a lighter battery. Files there meet the universal battery described next. They do not meet the curly-quote rule, the glyph law, or the book's banned patterns. A heading fault or a long paragraph in an audit directory prints as a warning, where the same fault in a chapter is an error. The audit lists the warnings under `Editorial warnings:` and does not fail the check over them.

### The universal battery

Every audited file meets the *universal battery*, a set of rules the press applies to every book. Each rule has a packaged known-bad fixture that proves it. The audit refuses these phrases in a paragraph, so Example 6.3 gives them in fenced code, which the phrase rules skip. Each entry shows the pattern, then the diagnostic and the fixture.

**Example 6.3. The universal battery and its fixtures**

```text
U+2014
    contains em dash                em-dash.md
U+2013
    contains en dash                en-dash.md
\bin conclusion\b
    generic conclusion              in-conclusion.md
it is important to note
    throat-clearing phrase          throat-clearing-important.md
it is worth noting
    throat-clearing phrase          throat-clearing-worth.md
at its core
    fake-revelation phrase          at-its-core.md
the real question is
    fake-revelation phrase          real-question.md
let's (dive|delve|explore|break this down)
    chatbot signposting             lets-dive.md
without further ado
    chatbot signposting             without-further-ado.md
stands as a testament
    inflated significance           testament.md
vibrant tapestry
    inflated AI phrase              vibrant-tapestry.md
not only ... but also (within 120 characters)
    formulaic negative parallelism  negative-parallelism.md
(whitespace at the end of a line)
    trailing whitespace             trailing-whitespace.md
```

The negative parallelism rule allows up to 120 characters between its two halves. The dash rules match single characters. Two hyphens typed in prose pass the checker, but pandoc turns them into an en dash in the editions. The house law says to rewrite the sentence instead.

The universal battery skips fenced code for every rule except trailing whitespace, and it reads inline code. The audit refuses a space at the end of a line in an example as surely as one in a paragraph. Configure your editor to strip trailing whitespace on save, and the rule will never trouble you.

### Rules for book prose

The manuscript meets three more rules that the audit directories do not. The first refuses curly quotes. Pandoc's smart typography curls your straight quotes in every rendered edition except the Manuscript edition (the stitched Markdown), which keeps your characters as you typed them. A curly quote in a chapter file is usually a paste from a word processor.

The second is the *glyph law*, which limits book prose to ASCII and the accented Latin letters. Its diagnostic is `glyph U+XXXX is outside the print-font set`, with the code point in place of the four letters. Chapter 4, *Writing the manuscript*, gives the permitted ranges and the characters that surprise authors, the copyright sign first among them.

The third rule applies the book's own banned patterns, from *config/house-rules.yaml*. The section "House rules" later in this chapter describes them.

The book's banned patterns skip fenced code entirely, and they read inline code. A banned word between backticks in a paragraph therefore still draws its diagnostic.

### Headings and paragraphs

The audit reads every heading for two faults. If a heading begins with a number you typed, the audit prints `manual number in heading`. For a heading in title case, it prints `title-case heading:` followed by the heading's text. Chapter 4 describes the title-case test and the sentence-case rule that avoids it.

The *paragraph law* requires every paragraph to run under 190 words.[^6-law-date] For a paragraph that is not under 190 words, the audit prints a message of this form:

```text
paragraph 40 has 264 words (the law is under 190; split it)
```

The paragraph number counts from the top of the file. A tip, a warning, or a sidebar is one paragraph to the checker, however many paragraphs it shows on the page. Keep sidebars short for that reason, or the checker will refuse a block that looks innocent in the chapter file.

When the audit finds no error, it prints `Editorial checks passed: N Markdown files`.

[^6-law-date]: According to the press's CHANGELOG, press began to enforce the paragraph law in version 1.7.0.

## The jargon lint and the watchlist

The fourth pass runs the *jargon lint*, a separate program that reads the chapter files against a list of overused engineering terms.[^6-twocopies] Press runs it with the command in Example 6.4 and writes its full report to *build/jargon-report.txt*.

**Example 6.4. The command the fourth pass runs**

```text
python -m press.jargon_lint --fail-on rewrite [--allow T]... \
    <chapter files>
```

The jargon lint reads only the manuscript files, and the audit directories are left to the style audit. It skips fenced code, inline code, URLs, and blockquotes, so a term inside a quotation from another writer does not count against you. The `--include-quotes` option makes it read blockquotes as well.

### The watchlist

*The watchlist* is the jargon term list. It lives in the overused-jargon skill, as *references/watchlist.csv* in the skill's directory, and `press skills` prints each installed skill with its path. At the time of this writing it holds 53 terms. Each row gives the term, how it matches, its status, a category, a question, the uses it allows, and notes.

The status decides what the lint does with a sighting. Table 6.3 lists the four statuses and the level of each.

| Status | Level | Meaning |
|------------|-------|------------------------------------------------------|
| `allow` | 0 | This is the lowest level. No packaged term has this status. |
| `inspect` | 1 | The lint reports the sighting and asks a question. You decide whether the use is literal. |
| `rewrite` | 2 | The lint reports the sighting, and the check fails at the default threshold. |
| `ban` | 3 | This is the highest level, and it fails at any threshold up to `ban`. No packaged term has this status. |

Table: Table 6.3. Watchlist statuses

The packaged watchlist has 39 `inspect` terms and 14 `rewrite` terms. The `--fail-on` option sets the threshold, and it takes `none`, `inspect`, `rewrite`, or `ban`. The default is `rewrite`, and `press check` uses it, so an inspect term appears in the report and does not fail the check. The lint skips fenced code, so Example 6.5 can list the 14 rewrite terms where a paragraph cannot.

**Example 6.5. The rewrite terms in the packaged watchlist**

```text
load-bearing        blast radius        footgun
yak shaving         belt-and-suspenders belt and suspenders
smoking gun         seam                seams
substrate           cleanly             decisive
authoritative       genuinely
```

The inspect terms are more ordinary words that engineers overuse: spine, gate, scaffold, wiring, drift, surface, canonical, fallback, stale, churn, and others. Several of them are also the literal names of things in press. The watchlist therefore asks a question about each sighting and leaves the answer to you.

Example 6.6 shows three rows of the watchlist, folded to fit the page. In the file, each row is one line. The `question` column is the useful one, because it asks what the term stands for, and the answer is usually the sentence to write instead.

**Example 6.6. Three rows of the watchlist**

```text
load-bearing,phrase,rewrite,stock metaphor,"What depends on
  it, and what fails without it?",Literal structural use;
  direct quotation; deliberate house voice,user seed,Prefer
  the actual dependency and failure.
seam,word,rewrite,structural metaphor,Which two components
  or responsibilities meet here?,Literal material use;
  precise domain term; deliberate metaphor,user seed,Name
  the interface or shared responsibility.
gate,word,inspect,process shorthand,What condition must
  pass before what action?,Literal gate; logic gate;
  standard named domain concept,user seed,"May mean test,
  approval, deadline, flag, or authority."
```

### Reading the jargon report

Each sighting prints three lines: the location and the rule, the line of context, and the rule's question. Example 6.7 shows the form, with the context line abbreviated.

**Example 6.7. The form of a jargon sighting**

```text
path:line:col: rewrite: 'seam' [structural metaphor]
  <context line>
  Ask: Which two components or responsibilities meet here?
```

The lint matches whole terms only. Its word boundaries allow no match next to a word character or a hyphen, so the term "gate" never matches the word "gateway". When the lint finds no rewrite term, press prints `Jargon check passed: no rewrite-status terms (full audit in build/jargon-report.txt)`.

Read the report after a long revision anyway, because the inspect sightings are in it. Take each one in turn and answer its question. If the answer names a real thing in your subject, the term is literal, and it can stay. If the answer is a sentence the term stood in for, write that sentence. A rewrite term that is literal in your book belongs in `jargon-allow`, which the section "House rules" describes.

You can also run the lint by hand. The `--json` option prints the findings for another program, `--max-findings` caps them at a number (500 by default), and `--allow` takes one term and can repeat. If the watchlist itself is malformed, the lint exits with status 2.

::: {.warning}
> **Warning:** Do not edit the watchlist inside the installed press package to silence a term. The next install overwrites your edit. Add the term to `jargon-allow` in your book's house rules instead.
:::

[^6-twocopies]: The jargon lint exists twice. One copy lives in the press package, and a portable copy lives inside the overused-jargon skill, so that the skill works without press installed. A check in `press selftest` requires the two copies to match byte for byte, function by function, except for the function that parses the command line.

## House rules

*House rules* are the file *config/house-rules.yaml* in your book repository. The file is optional, and it has three keys: `banned-patterns`, `jargon-allow`, and `audit-dirs`. The source checks validate its shape before the style audit reads it. Example 6.8 shows the house rules of the Alice book.

**Example 6.8. config/house-rules.yaml in the Alice book**

```text
banned-patterns:
  "\\bvery unique\\b": "very unique (unique does not grade)"
jargon-allow:
  - seams
audit-dirs:
  - notes
```

Table 6.4 describes the three keys.

| Key | Meaning |
|------------------|------------------------------------------------------------|
| `banned-patterns` | Each entry maps a regular expression to a label. The style audit refuses any line of book prose that matches, and it prints the label. |
| `jargon-allow` | Each entry is a term the jargon lint must not refuse in this book. Press passes each one to the lint with `--allow`. |
| `audit-dirs` | Each entry names an audit directory, such as *notes*, that the style audit reads with its lighter battery. |

Table: Table 6.4. The keys of config/house-rules.yaml

### Banned patterns

A banned pattern is a regular expression, and press applies it exactly as written, case and all. The pattern in Example 6.8 catches "very unique" and misses "Very unique" at the start of a sentence. If you want both, write the pattern to match both, as in `\\b[Vv]ery unique\\b`. Double each backslash in the YAML file, because YAML reads the string first. The `\\b` in the file reaches the regular expression as `\b`, a word boundary.

A match prints as `<file>:<line>: <label>`. The label is your message to the author, so write it as advice. "very unique (unique does not grade)" tells the author what to fix and why. A bare "banned" tells the author only that something is wrong.

Press refuses a pattern that does not compile. Example 6.9 shows the message, folded to fit the page. The text in angle brackets holds the pattern and the error the regular-expression engine reported.

**Example 6.9. The refusal of a malformed pattern**

```text
config/house-rules.yaml: banned pattern '<p>' is not a valid
    regex (<exc>)
```

Banned patterns are where a book enforces its own voice: the stock phrases its editors will not print, the book's spelling of a recurring name, a word the author overuses.

::: {.tip}
> **Tip:** Give each banned pattern a distinct label, and use that label in its fixture's expect comment. The checker self-test then reports exactly which rule went dead.
:::

### Jargon allowances

The `jargon-allow` list tells the jargon lint which watchlist terms this book may use. Press folds the case of each entry, so one entry allows the term in any capitals. Use the list for terms that are literal in your subject. A book about a bridge has a real spine, and a book about a sewing machine has real seams. The list applies to the whole book, so a term you allow for one chapter passes in all of them.

### Audit directories

The Alice book names *notes*, a directory of research notes that never prints in the book. The section "The style audit" earlier in this chapter gives the rules an audit directory meets.

## Sentinels and the page floor

Two settings in *config/metadata.yaml* tell the verifiers what a finished book must contain. You set them before any edition exists, and the checker reads one of them. Chapter 8, *Verifying the artifacts*, shows how the verifiers prove both against the finished editions.

### Sentinels

A *sentinel* is a phrase in `verify-sentinels`, a fragment of your own prose that press looks for in the manuscript and in the editions it builds. Press checks each sentinel in four places: in the manuscript, in the Print edition's text, in each edition, and on the public reading site. The first of those four belongs to the checker. If a sentinel does not appear in the manuscript, the source checks refuse the book with `sentinel not found in the manuscript:` and the phrase.

The checker's part is the cheap one: it catches a sentinel that a revision removed, before you spend a build on it. The other three places are the verifiers' work. They catch the harder fault, a phrase that the manuscript holds and an edition lost on the way to the reader.

Matching is exact, including case. Press treats curly and straight quotes as equal, so a sentinel with a straight apostrophe matches the curled one that pandoc prints. Example 6.10 shows the sentinels of the Alice book, two fragments from the middles of Carroll's seventh and eleventh chapters.

**Example 6.10. Sentinels in config/metadata.yaml**

```text
verify-sentinels:
  - "Twinkle, twinkle, little bat"
  - "she made some tarts"
verify-min-pages: 24
```

The scaffold's template gives the rule for choosing them: "pick 2-4 phrases from your actual manuscript, each distinctive enough to appear exactly once (a whole memorable clause, not a common word)". A single common word appears in every book, so it proves nothing about yours.

::: {.warning}
> **Warning:** If your book sets a drop cap, do not choose a sentinel from the first words of a chapter. The drop cap splits and small-caps the opening word, and the Print edition's text no longer matches the phrase exactly. Choose a clause from the middle of a chapter.
:::

The house profile sets no drop cap, so the warning applies only once a book chooses one. In a book with a drop cap, a sentinel at the head of a chapter passes the checker, because the manuscript holds it whole, and then fails in the Print edition.

### The page floor

`verify-min-pages` is the Print edition's *page floor*, the fewest pages the PDF verifier accepts. A Print edition shorter than the floor fails verification, so the floor catches a build that ran to the end and set only part of the book.

The value has two defaults, and the difference matters. The book model's default is 40, while the scaffold's template writes 1, so a new book builds and verifies before it has a second page. The Alice book set its floor to 24 once its chapters existed.

### Draft settings and release builds

The scaffold's template calls two settings draft settings: an empty sentinel list and a one-page floor. A draft build accepts them, and a release build refuses them. Press calls the two settings the *release witnesses*. When the environment variable `PRESS_RELEASE` holds 1, press requires at least two sentinels and a page floor of at least 24. It refuses vacuous witnesses with the message in Example 6.11, folded to fit the page.

**Example 6.11. The release refusal**

```text
this is a release build (PRESS_RELEASE=1) and its witnesses
    are vacuous:
verify-sentinels has N entries; a release needs at least 2
    distinctive prose fragments
verify-min-pages is N; a release needs at least 24
```

The reusable workflow sets `PRESS_RELEASE=1` when it builds a tag that begins with `v`. Set both values before your first release tag, and the release build will never print Example 6.11 at you.

## Reading the output

A passing check prints a line for each pass. Example 6.12 shows a run on the press's own three-chapter Alice example, a sample book that holds Carroll's first three chapters and one appendix. It has no fixtures of its own, so its checker self-test counts 19. The example folds long lines to fit the page and shortens the paths in the notes.

**Example 6.12. A passing check on the press's own three-chapter Alice example**

```text
$ press check
Source checks passed: 4 ordered Markdown files
  note: em-dash.md also drew: - .../known-bad/em-dash.md:4:
    glyph U+2014 is outside the print-font set
  note: en-dash.md also drew: - .../known-bad/en-dash.md:4:
    glyph U+2013 is outside the print-font set
Checker self-test passed: 19 known-bad fixtures each tripped
    their declared rule, known-good fixture accepted, 2 extra
    diagnostics noted
Editorial checks passed: 4 Markdown files
Jargon check passed: no rewrite-status terms (full audit in
    build/jargon-report.txt)
```

The two note lines belong to the checker self-test, although they print before its summary line. Each says that a fixture drew a second diagnostic as well as the one it declared. The em dash lies outside the glyph law's ranges, so the em dash fixture draws the glyph diagnostic as well as the em dash rule. The en dash fixture does the same. The checker self-test counts these as the "2 extra diagnostics noted", and they do not fail it.

@fig:check-output shows the same run as it appears in a terminal on `hatter`, with the long lines wrapped at the window's edge.

![A passing check on the press's own three-chapter Alice example](assets/woodcuts/06-03-check-output.png){#fig:check-output .diagram width=full-measure fig-alt="A terminal window titled alice at hatter. It shows press check printing four summary lines, one per pass, with two indented note lines after the first."}

<!-- art: ARCHETYPE terminal. One boxed terminal window, black monospace on white, 72 columns wide, with a plain title bar reading "alice@hatter". Inside, each line exactly, long lines wrapped at 72 columns: "$ press check", then "Source checks passed: 4 ordered Markdown files", then "  note: em-dash.md also drew: - .../known-bad/em-dash.md:4: glyph U+2014 is outside the print-font set", then "  note: en-dash.md also drew: - .../known-bad/en-dash.md:4: glyph U+2013 is outside the print-font set", then "Checker self-test passed: 19 known-bad fixtures each tripped their declared rule, known-good fixture accepted, 2 extra diagnostics noted", then "Editorial checks passed: 4 Markdown files", then "Jargon check passed: no rewrite-status terms (full audit in build/jargon-report.txt)", then a bare "$". The reader should see first the four lines that begin with a pass name. -->

### Reading a failure

A failing pass prints a header and then one diagnostic to a line. The style audit's header is `Editorial checks failed:`, and each diagnostic below it begins with a hyphen, the filename, and a colon. Most diagnostics then give the line number, so your editor can jump to the line. The paragraph diagnostic gives the paragraph number instead. Example 6.13 shows the end of a failed check on the Alice book, folded to fit the page.

**Example 6.13. A failed style audit in the Alice book**

```text
Editorial checks failed:
  - book/chapters/01-down-the-rabbit-hole.md:12: very
    unique (unique does not grade)
  - book/chapters/01-down-the-rabbit-hole.md: paragraph 9
    has 212 words (the law is under 190; split it)
```

The jargon lint never ran in Example 6.13. The check stopped at the third pass, so a rewrite term in the same chapter would wait for the next run. Fix every diagnostic in a failure before you run the check again, because the pass after it may have more to say.

Table 6.5 collects the diagnostics you are most likely to meet. Appendix C, *Messages and refusals*, holds the full list.

| Diagnostic form | Meaning |
|------------------|------------------------------------------------------------|
| `metadata missing <key>:` | A required key is absent from *config/metadata.yaml*. Set it with `press config set`. |
| `unfinished marker '<phrase>'` | A chapter still holds a placeholder or dummy text. Write the chapter. |
| `sentinel not found in the manuscript: <s>` | A revision removed a sentinel's phrase. Restore the phrase or choose another sentinel. |
| `glyph U+XXXX is outside the print-font set` | A character outside the glyph law's ranges is in book prose. Replace it with an ASCII or accented Latin equivalent. |
| `title-case heading: <text>` | A heading is in title case. Rewrite it in sentence case. |
| `manual number in heading` | A heading begins with a number you typed. Delete the number. |
| `paragraph N has W words` | A paragraph is not under 190 words. Split it or cut it. |
| `<file>:<line>: <label>` | A line of book prose matches one of your banned patterns. The label says what to fix. |
| `path:line:col: rewrite: '<term>'` | A chapter holds a rewrite term from the watchlist. Answer the question the lint prints and rewrite the sentence. |

Table: Table 6.5. Diagnostics you are most likely to meet

## Exit status and what depends on it

When all four passes succeed, `press check` exits with status 0. When any pass fails, it stops there and exits with a nonzero status. That status is the checker's real output. The printed lines are for you, and the exit status is for every program that runs the checker on your behalf.

`press all` runs the checker's four passes before it builds any edition, and it stops at the first failure. A manuscript that fails the check therefore never reaches pandoc under `press all`. A bare format target builds without the checker, as the section "The four passes" describes.

Press also declares dependency edges between its targets. Each verify target rebuilds what it verifies before it inspects it, so a verifier does not bless an edition that the current manuscript did not produce. The one exception is `press verify-formats`, which includes an existing Print edition, *dist/alice.pdf*, in its cross-edition agreement check without rebuilding it. Chapter 8 describes the edges target by target.

A continuous-integration build reads the same status. The reusable workflow runs `press all`, so a failed check fails the CI job before any edition is built. Chapter 14, *Continuous integration and the release contract*, describes the workflow.

A shell reads the exit status too. In a chain joined with `&&`, each command runs only if the one before it exited with status 0. The chain in Example 6.14 commits only a manuscript that passes the check.

**Example 6.14. A commit chain that respects the check**

```text
$ press check && git commit -am "Revise chapter 6"
```

The chain works only if the checker's own status reaches the `&&`. When a shell runs a pipeline, the pipeline's status is the status of its last command, and the shell discards every earlier status.

::: {.warning}
> **Warning:** Do not put a pipe between `press check` and the `&&` in a commit chain. Run the check alone, and filter its output in a separate command if you want a shorter transcript.
:::

::: {.sidebar}
> **The red check that went out green**
>
> The press keeps a list of *scars*, the production failures it paid for once and turned into guards. One entry is two lines long: "Never pipe a check command into grep before `&&` in a commit chain; the pipeline exit code is grep's, and a red check once shipped as green."
>
> The mechanism needs no bug in any program. In such a chain, the checker can fail and say so, in plain text, on the terminal. Grep reads that text, finds a line it matches, perhaps an earlier pass's summary, and exits 0, as grep does. The shell sees a status of 0 at the `&&` and runs the next command. Every program does its job, and whatever the check guarded goes out.
>
> The cure is a habit. Let the checker's own status reach the `&&`, and read its output when it fails.
:::

Chapter 7, *Building the editions*, takes the manuscript that the checker passed and builds each edition from it.

<!-- index: press check; press style; source checks; checker self-test; known-bad fixture; known-good fixture; expect comment; style audit; universal battery; audit directories; glyph law; paragraph law; trailing whitespace; jargon lint; watchlist; jargon-allow; house rules; banned patterns; sentinel; verify-sentinels; page floor; verify-min-pages; release witnesses; PRESS_RELEASE; exit status -->
