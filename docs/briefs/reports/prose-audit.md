# Whole-book prose audit (copyeditor)

Scope: every file in `book/chapters/` and `book/appendices/` (23 files, about
129,000 words). Read-only; nothing under `book/` was touched. Another editor
is changing the same files, so every item is quoted and gives its file and
paragraph-start line only as a locator at the time of the audit.

Method, stated plainly: `tools/ste_check.py` ran on every file (raw findings
below). I then extracted prose only (no fences, comments, tables, image lines,
captions, headings), split it into sentences, and ran the contract's tells as
regexes over all of it. I read the preface and most of Chapter 1 and Chapter 13
line by line, and read in context every sentence the scans flagged in all
other files, all 17 chapter endings, all headings, and every sentence over 30
words. I did not read the other chapters' unflagged sentences one by one, so a
defect that no scan, rhythm count, or ending check can see (a muddled
explanation, say) is outside this audit. The fact checker owns facts; none are
judged here.

## Status (five lines)

1. Total real findings: 56 (should: 53, may: 3). Zero in the contract's
   mechanical classes: no dash, no semicolon in author prose, no assistant
   vocabulary, no "not just X", no run-up, no stacked hedge, no `serves as`.
2. Three worst files: 01-introduction (9), then 03-the-shape-of-a-book and
   13-registrations (5 each); 12-the-print-pack follows with 4.
3. Three most common defects: sentence over 30 words (19), the two-sentence
   staged denial ("You do not X. The press Y.") (9), period-voice drift words (7).
4. Block: no single finding would be refused by `press check` or breaks a
   fact. By the copyeditor brief's severity rule, four items are
   one-sighting-class (one-line closers that repeat the paragraph:
   01-introduction "A warning in prose is not enough by itself.", 02-installing
   "Nobody has to grant your book access to anything.", 08-verifying "An index
   from yesterday's manuscript cannot reach today's PDF.", and the footnote
   "That is another scar." in 01). Each is a one-sentence deletion; fix before
   release as a matter of the brief, not because anything is broken.
5. The book is cleaner than the checker suggests: the checker printed 702
   findings across the 23 files, and 56 are real, because most of the raw
   output is `-ing` words in headings,
   "therefore"/"whether"/"verify"/"however" (period-correct or terms of art),
   art comments, and merged tables.

## 1. Checker findings: raw versus real

Raw counts per file are lines the checker printed, header excluded. Real
counts are the findings listed in section 1b.

| File | Raw | Real |
|---|---|---|
| 00-preface | 17 | 2 |
| 01-introduction | 51 | 9 |
| 02-installing-press | 46 | 3 |
| 03-the-shape-of-a-book | 46 | 5 |
| 04-writing-the-manuscript | 38 | 2 |
| 05-figures-and-plates | 29 | 1 |
| 06-checking-the-manuscript | 32 | 2 |
| 07-building-the-editions | 47 | 2 |
| 08-verifying-the-artifacts | 51 | 3 |
| 09-the-house-design | 35 | 3 |
| 10-front-matter-index-authorities | 20 | 2 |
| 11-the-art-department | 43 | 3 |
| 12-the-print-pack | 42 | 4 |
| 13-registrations | 14 | 5 |
| 14-continuous-integration | 24 | 0 |
| 15-the-desk-and-the-machines | 34 | 2 |
| 16-inside-the-press | 42 | 2 |
| a-command-reference | 22 | 1 |
| b-configuration-reference | 34 | 2 |
| c-messages | 8 | 2 |
| d-the-toolchain | 13 | 0 |
| e-glossary | 6 | 0 |
| z-colophon | 8 | 1 |

### 1a. Checker rules that are noise here (do not act on them)

- `ing-form` (185): headings and section titles ("Checking the manuscript"),
  plus "Writing", "Verifying" as noun phrases. None is a prose -ing rider.
- `word` (136): "therefore" (about 60) and "whether" (about 30) are kept by the
  contract's era rule; "verify" is the press's own target name; "enhance" is
  `press art enhance`; "landscape" is page orientation (11:65, 11:412) and
  appears in art comments; "identical" and "however" are fine in context.
- `paragraph-length` (76): the counter counts list items and footnotes as
  sentences. I found no prose paragraph over six sentences.
- `semicolon` (55) and many `sentence-length`: art comments, and quotations
  of press documentation or scaffold text (quoted, verbatim by the fidelity
  rule). I checked all 62 semicolons my scan found in prose: every one sits
  inside a quotation, a code span, or a quoted message. Author prose has none.
- `passive` (58): 40 are quoted ("Facts are stated once"), verb-as-adjective
  ("is malformed", "is green"), or table text. The 3 real hidden actors are in
  1b.
- `phrasal-verb`: "look at", "go through", "check out", "find out", "turn on"
  are ordinary and acceptable at the 80% rule.

### 1b. Real defects, by file (quote, rule, smallest fix)

Severity is "should" unless marked.

**a-command-reference**

1. "`press all` builds neither the print interior nor the cover wrap, which `press print`, `press verify-print`, and `press coverwrap` make, unless print ordering is on, when the commerce gate builds them." Sentence over 30 words (31), tangled "unless ... when".
   Fix: "`press all` builds neither the print interior nor the cover wrap. `press print`, `press verify-print`, and `press coverwrap` make them, and the commerce gate builds them when print ordering is on."

**b-configuration-reference**

1. "If you write it as clauses joined by "or," (for example ...), it stacks on the title page, one clause to a line, and on the landing page." Sentence over 30 words (31).
   Fix: "If you write it as clauses joined by "or" (for example ...), it stacks one clause to a line on the title page and on the landing page."
2. "The presence of this file asks the press to generate the PDF's front matter: the title page, the copyright page (the press calls it the colophon), and the dedication, epigraph, and acknowledgments pages." Sentence over 30 words (33), two ideas.
   Fix: "...front matter: the title page, the copyright page, the dedication, the epigraph, and the acknowledgments. The press calls the copyright page the colophon."

**c-messages**

1. "The file still holds one of three unfinished markers: two placeholder abbreviations followed by the verb "write", or the Latin dummy copy of the typesetter." (31)
   Fix: "The file still holds one of three unfinished markers. Two are placeholder abbreviations followed by the verb "write", and the third is the Latin dummy copy of the typesetter."
2. "The manuscript witness line, the longest markup-free line of 40 or more characters in the manuscript, is absent from the edition." (32)
   Fix: "The edition lacks the manuscript witness line, the longest markup-free line of 40 or more characters in the manuscript."

**d-the-toolchain, e-glossary**: none. (e-glossary "glyph law" is a 31-word list sentence; a list, acceptable.)

**z-colophon**

1. "The pigment sepia was made from that ink" (hidden actor, past passive).
   Fix: "People once made the pigment sepia from that ink, and the pigment and the genus share the Greek name for the cuttlefish."

**00-preface**

1. "Warning : A short paragraph set off from the text that opens with the word Warning marks a step that can cost you work or send a broken artifact to a printer." (32, two ideas)
   Fix: "A short paragraph set off from the text and opened by the word Warning marks a step that can cost you work. The same step can send a broken artifact to a printer."
2. Duplicate sentence with Chapter 1 ("Where it came from"): "A *scar*, in the press's vocabulary, is a production failure turned into a guard." appears word for word in the preface (para 2) and in 01. Also "Neither book lives in the press repository" appears in both. 
   Fix: in 01, replace with "The preface defined a *scar*; this chapter shows several." or cut the repeated definition.
   (Four other preface entries run 31 to 36 words, but they are one-line definition-list entries; acceptable.)

**01-introduction**

1. "They are pandoc, LuaLaTeX, latexmk, the Libertinus fonts, epubcheck with a Java to run it, and poppler, a set of PDF tools whose `pdftoppm` renders a page as an image for the verifier." (33)
   Fix: "...epubcheck with a Java to run it, and poppler. Poppler is a set of PDF tools, and its `pdftoppm` renders a page as an image for the verifier."
2. "If a sentinel leaves the manuscript, the checker refuses with `sentinel not found in the manuscript:`, and if an edition lacks one, the verifier for that edition fails and names it." (31)
   Fix: split before "and if": "...manuscript:`. If an edition lacks one, the verifier for that edition fails and names it."
3. "A warning in prose is not enough by itself." One-line closer; the ROADMAP sentence before it already says so. (one-sighting class)
   Fix: delete.
4. Footnote: "That is another scar." One-line closer and a self-annotation. (one-sighting class)
   Fix: delete; the sentence before it already states the fact.
5. "The tour takes it from an empty directory to a full dist directory, using the commands from the press QUICKSTART with the Alice book's names in place." -ing rider.
   Fix: "The tour takes it from an empty directory to a full dist directory. It uses the commands from the press QUICKSTART, with the Alice book's names in place."
6. "Several of them appear later in this chapter." Stub text about the document.
   Fix: delete.
7. Heading "Facts are stated once", first sentence "The first law reads "Facts are stated once."" Heading repeated as first sentence.
   Fix: "*ARCHITECTURE.md* gives each kind of fact one home." and fold the quotation into the paragraph's last sentence, where "The law ends with an instruction" already quotes it.
8. "A release build refuses both draft values: it needs at least 2 sentinels and a floor of at least 24 pages." (may) Number under ten in prose; "two" unless it is a config value.
   Fix: "at least two sentinels".
9. "A verifier that inspects last week's PDF blesses last week's PDF." Period voice, see section 3.
   Fix: "passes".

**02-installing-press**

1. "Nobody has to grant your book access to anything." One-line closer after the quoted documentation. (one-sighting class)
   Fix: delete.
2. "Press does not set type itself, and it does not check an EPUB against the retail rules itself. It prepares the manuscript, ..." Staged denial.
   Fix: "Press prepares the manuscript, decides what to build and in what order, and hands the work to older, specialized programs. It sets no type and checks no EPUB itself."
3. "This chapter describes it later." Stub text about the document.
   Fix: delete; Table 2.1 follows directly.

**03-the-shape-of-a-book**

1. "The press README gives the sequence as `cd my-book && git init && make all`, and the quick start in the press documentation ends with a first commit and a push." (31)
   Fix: end the sentence at "`make all`." Then "The quick start in the press documentation ends with a first commit and a push."
2. "You never type the year twice." One-line closer (restates the date paragraph).
   Fix: delete, or fold in: "...gives the title page its roman numerals, so you never type the year twice."
3. "For a field you cannot set from the shell, it adds a second line, starting with an arrow, that says where to go instead." -ing rider.
   Fix: "...it adds a second line that begins with an arrow and says where to go instead."
4. "The rule for `site-url` follows from the first law of the press: "Facts are stated once."" Formula repeated (see section 2, "repeated device").
   Fix: "The rule for `site-url` follows from the first law: the press states each fact once."
5. "it blesses artifacts that no longer match the manuscript." Period voice.
   Fix: "it passes artifacts".

**04-writing-the-manuscript**

1. "You never type a tie of your own. You type "Rev. ..."" Staged denial.
   Fix: "You type "Rev." and the filter adds the tie."
2. "The section "Tables" later in this chapter covers them." Stub text about the document.
   Fix: "Tables, below, covers them" is also meta; best is to delete and let the sentence before it stand: "...it probably wants to be a table."

**05-figures-and-plates**

1. "`press illustrate` adds a guardrail of its own to every commission" Period voice, see section 3.
   Fix: "adds a standing instruction of its own".

**06-checking-the-manuscript**

1. "In a book with a drop cap, a sentinel at the head of a chapter passes the checker, because the manuscript holds it whole, and then fails in the Print edition." (31)
   Fix: "...holds it whole. It then fails in the Print edition."
2. "the audit directories are left to the style audit." Hidden actor.
   Fix: "The jargon lint reads only the manuscript files. The style audit reads the audit directories."

**07-building-the-editions**

1. "The press does not allow this through its command line. Every verify target rebuilds the artifacts it verifies before it verifies them." Staged denial.
   Fix: "Every verify target rebuilds the artifacts it verifies before it verifies them, and the command line offers no way around that."
2. Footnote: "At the time of this writing, CI requires those tests to run, starting with version 3.0.2, and holds a coverage floor for each filter." -ing rider.
   Fix: "CI has required those tests since version 3.0.2 and holds a coverage floor for each filter."

**08-verifying-the-artifacts**

1. "You do not choose the witness. The press finds it, and it changes when you write a longer plain line." Staged denial.
   Fix: "The press chooses the witness, and it changes when you write a longer plain line."
2. "The verifier does not trust the zip that the builder wrote. It recomputes the member list from the same policy, `publication_members()`, and compares." Staged denial.
   Fix: "The verifier recomputes the member list from the same policy, `publication_members()`, and compares it with the zip the builder wrote."
3. "An index from yesterday's manuscript cannot reach today's PDF." One-line closer; the quoted architecture note before it says the same. (one-sighting class)
   Fix: delete.

**09-the-house-design**

1. "Table 9.4 gives the rest of each profile: its margins, its indent and leading, and the width of its *paper column*, the framed column that holds the text on the reader site." (32)
   Fix: "...and the width of its *paper column*. The paper column is the framed column that holds the text on the reader site."
2. "In the PDF it sets the links to the deep cloth red and restates the accent in the cloth red, though the header uses the accent nowhere, and it asks for the fairy-dust scene break." (35)
   Fix: "In the PDF it sets the links to the deep cloth red and restates the accent in the cloth red. The header uses the accent nowhere. It also asks for the fairy-dust scene break."
3. "The house text width is stated, and the other four are derived from Table 9.4" Hidden actor, two passives.
   Fix: "Table 9.4 states the house text width, and the press derives the other four from the trim width less the inner and outer margins."

**10-front-matter-index-authorities**

1. "You never mark up the manuscript for it. You list the terms a reader will look up, and the press finds them in the text." Staged denial.
   Fix: "You list the terms a reader will look up, and the press finds them in the text without any markup."
2. "The first law of the press reads "Facts are stated once."" Formula repeated (see section 2).
   Fix: "The first law is that the press states each fact once."

**11-the-art-department**

1-3. "guardrail" at three places ("appends a guardrail", "the text guardrail", "The command always appends a guardrail:"). Period voice, see section 3.
   Fix: gloss once ("a standing instruction the command adds to the prompt, which this book calls the *guardrail*") or rename to "standing instruction" throughout. (11:150 and 11:190 sit near each other; 11:226 repeats it.)

**12-the-print-pack**

1. "For the interior, the pass caps the logomark at 1000 pixels on its long edge and each figure and plate at 1900 pixels, which is about 300 PPI at 6.3 inches." (31)
   Fix: "...at 1900 pixels. That is about 300 PPI at 6.3 inches."
2. "The commerce gate builds the interior and the wrap itself, computes the *edition manifest*, the JSON file the gate writes with the production facts and their hash, and then looks for a qualification." (33)
   Fix: "The commerce gate builds the interior and the wrap itself and computes the *edition manifest*. The manifest is the JSON file that holds the production facts and their hash. The gate then looks for a qualification."
3. "The press shows only the first twelve characters of the id: the gate prints `edition <first 12 characters> (<edition>)`, and `python3 -m press.edition verify` prints `identity` followed by the same twelve." (31)
   Fix: split at the colon: "The press shows only the first twelve characters of the id. The gate prints ..."
4. "You do not choose the id. The press computes it, and the commerce gate computes it each time it builds the edition manifest." Staged denial.
   Fix: "The press computes the id, and the commerce gate computes it again each time it builds the edition manifest."

**13-registrations**

1. "Example 13.5 shows the target in a fresh scaffold made with `press new alice --author "Lewis Carroll"`, before the changes of Chapters 3 and 10, and before you set any registration." (31)
   Fix: "...Carroll"`. The scaffold predates the changes of Chapters 3 and 10, and you have set no registration yet."
2. "Every route starts at the same block, so the copyright page cannot show a print ISBN that differs from the barcode's, or an EPUB ISBN that differs from the EPUB identifier." (31)
   Fix: split before "or": "...from the barcode's. It cannot show an EPUB ISBN that differs from the EPUB identifier either."
3. "It never contacts the Library of Congress. You copy the values into the form yourself, so the submission stays in your hands." Staged denial and closing clause.
   Fix: "You copy the values into the form yourself, because the press never contacts the Library of Congress."
4. "The press cannot buy any of these numbers, and it does not try. It checks the numbers you give it, ..." Staged denial (mild).
   Fix: "The press cannot buy any of these numbers. It checks the numbers you give it, ..." (drop "and it does not try").
5. "The first law of the press reads "Facts are stated once."" Formula repeated (see section 2).
   Fix: "The first law is that the press states each fact once."

**14-continuous-integration**: none.

**15-the-desk-and-the-machines**

1. "Every action press takes on a book starts as a `press` command, and you can type the command at the shell prompt or pick it from a list on the desk." (31)
   Fix: "Every action press takes on a book starts as a `press` command. You can type the command at the shell prompt or pick it from a list on the desk."
2. "Each claim is a verbatim fragment of 5 to 15 words with an assertion." (may) Number under ten in prose.
   Fix: "five to 15 words".

**16-inside-the-press**

1. "If you add a config field to the press, declare it in the model with its type and its default and in the CLI registry in *config_schema.py*, and read it from the `Book` everywhere." (34, instruction over 20)
   Fix: "If you add a config field to the press, declare it in the model, with its type and its default, and in the CLI registry in *config_schema.py*. Then read it from the `Book` everywhere."
2. "A change that broke any of them turns the contract red, and the floating major does not move." Period voice (may).
   Fix: "...fails the contract".

## 2. Book-wide patterns of agent prose

Counts are from the prose-only extraction (code, tables, comments, headings,
list entries and quotations excluded unless noted). "Quoted lead-ins" counts
sentences of the form "In the words of X", "The press states its reason:",
"reads:" and the like.

| File | Sent. >30 | Staged denial | Closer | -ing rider | Fwd signposts | Quoted lead-ins | Avg words/sent. |
|---|---|---|---|---|---|---|---|
| 00-preface | 1 | 0 | 0 | 0 | 0 | 1 | 17.7 |
| 01-introduction | 2 | 0 | 2 | 1 | 5 | 9 | 14.6 |
| 02-installing-press | 0 | 1 | 1 | 0 | 3 | 6 | 14.0 |
| 03-the-shape-of-a-book | 1 | 0 | 1 | 1 | 3 | 1 | 13.8 |
| 04-writing-the-manuscript | 0 | 1 | 0 | 0 | 5 | 1 | 15.3 |
| 05-figures-and-plates | 0 | 0 | 0 | 0 | 4 | 1 | 15.7 |
| 06-checking-the-manuscript | 1 | 0 | 0 | 0 | 4 | 2 | 14.2 |
| 07-building-the-editions | 0 | 1 | 0 | 1 | 3 | 3 | 14.4 |
| 08-verifying-the-artifacts | 0 | 2 | 1 | 0 | 4 | 6 | 13.6 |
| 09-the-house-design | 2 | 0 | 0 | 0 | 2 | 7 | 15.4 |
| 10-front-matter-index-authorities | 0 | 1 | 0 | 0 | 1 | 7 | 14.9 |
| 11-the-art-department | 0 | 0 | 0 | 0 | 3 | 0 | 13.9 |
| 12-the-print-pack | 3 | 1 | 0 | 0 | 3 | 4 | 14.0 |
| 13-registrations | 2 | 2 | 0 | 0 | 2 | 6 | 12.9 |
| 14-continuous-integration | 0 | 0 | 0 | 0 | 4 | 9 | 14.1 |
| 15-the-desk-and-the-machines | 1 | 0 | 0 | 0 | 3 | 7 | 13.3 |
| 16-inside-the-press | 1 | 0 | 0 | 0 | 3 | 11 | 13.6 |
| Appendixes a-e, z | 5 | 0 | 0 | 0 | 0 | 5 | n/a |

(Sentences over 30 in the table count only the ones I list with a fix; list
sentences, quoted ones and the in-chapter boxes are excluded. A few
parallel-list sentences run 31 to 34 words and I left them: the edition
lists at 04 "They are the Print edition (PDF)...", 07 "The others are the
Manuscript edition...", 07 "The press builds three editions for readers...",
and the honorific list at 04 "After an honorific, it ties...".)

Pattern by pattern:

- **Closing maxims.** Rare. Five one-line closers repeat the paragraph:
  01 "A warning in prose is not enough by itself."; 01 footnote "That is
  another scar."; 02 "Nobody has to grant your book access to anything.";
  03 "You never type the year twice."; 08 "An index from yesterday's
  manuscript cannot reach today's PDF." Fix for each is deletion (see 1b).
  Short final sentences that carry a fact ("Neither is an artifact." 03,
  "The guide does not say so." 12, "Let it finish." 03) are fine, and the
  last is the book's dry understatement working as intended.
- **Staged contrasts.** No "not just X, it's Y", no "This doesn't mean X. It
  means Y". The one live form is the two-sentence denial then affirmation:
  nine in author prose (list in 1b), all in 02, 04, 07, 08, 10, 12, 13. The
  quoted press sayings ("a label, not art direction", "enforced, not
  promised") are fidelity and stay. The 25 ", not" and 15 "rather than" /
  "instead of" contrasts I read are information (a fault in the toolchain, not
  in your EPUB), not staging.
- **Self-annotation.** 52 forward or backward pointers of the form 'the
  section "X" later in this chapter explains it'. The style guide (2.4)
  prescribes this form, so they are not defects as a class. They become
  uniform filler when they stand alone after a complete thought; I found
  three that carry no fact (02 "This chapter describes it later.", 04 "The
  section "Tables" later in this chapter covers them.", 01 "Several of them
  appear later in this chapter."). Delete those and leave the rest. One more
  is a candidate for trimming: 13 "Example 13.5 breaks two long lines to fit
  the page and omits the closing advice, which the next paragraph quotes."
  (keep; it protects fidelity).
- **Uniform sentence rhythm.** The average sentence is 12.9 to 17.7 words
  (chapters 13, 15, 03, 08, 16 are the shortest, 13.8 or less), under the
  contract's 16 to 22 and the style guide's 18 to 24 target. Variation is real
  (standard deviation 5.7 to 7.4; 12 to 29 percent of sentences are 8 words or
  under), so this is a may, not a defect. 40 paragraphs hold a run of four or
  more consecutive sentences within three words of each other; the heaviest
  are in 16-inside-the-press (7), 07 (4), and 03, 04, 05, 08, 11, 15 (3 each).
  Only the prose runs matter: the rest are the in-chapter lists and numbered
  steps. Worst prose run: 07 "An ordinary `press all` does not build the print
  interior, and it does not ..." (four sentences of 17 to 18 words, one idea
  each, in a row). Fix: join the second and third, and open the fourth with
  its condition.
- **Chapter endings.** Twelve of 16 chapters end on a one-sentence pointer
  ("The next chapter, *X*, ...", "Chapter N, *X*, ..."), in the same two
  shapes. The style guide allows it; the uniformity is a may. Vary two or
  three (02, 04, 05, 08 use the identical "The next chapter, *Title*, ..."
  frame).
- **One-sighting tells.** Zero hits for "not X but Y" family, run-ups ("Let's",
  "Here's the thing"), arguing with no one, inflated significance, `serves as`
  family, bold-label-colon list items in chapters (the appendix `**Cause.**`
  and `**Description.**` labels are reference format and fine), repeated-heading
  first sentence (one hit: 01 "Facts are stated once", see 1b), and 2
  `, which means` explanations that are not riders.
- **Hidden actors.** Three (09, 06, z-colophon, in 1b). The passive voice is
  otherwise almost entirely quoted or adjectival.
- **Contract word lists.** Assistant vocabulary: zero (every `key` is a YAML or
  API key; "landscape" is page orientation). Hedges: about 20 "usually",
  "often", "typically", all honest and each stating a real tendency, none
  stacked. Watchlist words (`gate`, `scaffold`, `surface`, `drift`, `ship`,
  `lands`) are in `jargon-allow`, so the lint passes them.
- **Repeated device (the book's own, not the model's).** Two repetitions
  worth a pass. First, the quotation-as-authority lead-in, about 80 times
  ("In the words of the maintainer's guide, "..."", "The press states its
  reason: "..."", "The press says plainly what ..."), densest in 16 (11), 14
  and 01 (9 each), 09, 10 and 15 (7 each), 02, 08 and 13 (6 each). It is
  faithful, but twelve to fifteen chapters in a row speak in the same
  introduction. Keep quotation where the exact wording matters (laws, error
  messages) and paraphrase the rest. Second, "The first law of the press
  reads "Facts are stated once."" opens paragraphs in 01, 03, 10, 13, 16 in
  nearly the same words; introduce it once (01) and refer to it by name after.

### The five worst examples overall, with fixes

1. 01-introduction, "A warning in prose is not enough by itself." One-line
   closer. Delete.
2. 08-verifying, "An index from yesterday's manuscript cannot reach today's
   PDF." Aphorism closer repeating the quoted note. Delete.
3. 02-installing, "Nobody has to grant your book access to anything." Closer
   repeating the quotation. Delete.
4. 08-verifying, "You do not choose the witness. The press finds it, and it
   changes when you write a longer plain line." Staged denial. "The press
   chooses the witness, and it changes when you write a longer plain line."
5. 12-print-pack, "You do not choose the id. The press computes it, ..."
   Same shape as 4 (the two are twins six chapters apart). "The press
   computes the id, and the commerce gate computes it again each time it
   builds the edition manifest."

## 3. Period voice drift (style guide section 3, 1999 manual register)

The register holds. No contraction in author prose (the only hits are inside
quoted regexes and a code span), no "I", no emoji, no "folks", "spin up", "deep
dive", "under the hood", or "out of the box". Spelling is consistent:
"Web site" throughout and never "website", "e-mail" (the one "email" is a
quoted YAML key in a code span), "filename" (the "file name" hits are the verb
"file names a section" and similar, not a spelling split), "appendixes" 17
against "appendices" 11 (the 11 are paths such as `book/appendices/`, which
stay), "toward", "Unix".
The dry understatement appears at least once every few pages ("Start the first
build, make a cup of tea", "We checked every chapter, and we expect that you
will find something anyway", "The guide does not say so."); no heading puns;
headings are sentence case. Admonitions are all under five sentences; chapter 5
has nine, one over the guide's three to eight.

What reads as 2026:

1. "blesses" ("A verifier that inspects last week's PDF blesses last week's
   PDF", 01; "it blesses artifacts that no longer match the manuscript", 03).
   Operations slang. Fix: "passes". (A third use, 08, is inside a quotation
   of the press's CLAUDE.md and stays.)
2. "guardrail" (05 once, 11 three times). The press's code word and an
   AI-product word. Fix: "standing instruction", or gloss once and keep.
3. "turns the contract red" (16, last paragraph of the Release section).
   Fix: "fails the contract". (The quoted scar "a red check once shipped as
   green" stays.)
4. Not defects, but noted so the squad can decide: "ratchet" (16, glossed in
   place), "hostile fixtures" (16, 14), "headless" (15 heading; 1999-correct
   in Java circles), "design tokens" (09, glossed), the whole of Chapter 15's
   subject (agents, prompts, models), and the colophon's honest line "Language
   models drafted the text". These are the subject or the truth, not voice;
   leave them.

## Sources and limits

- `docs/prose-contract.md`, `docs/squad/copyeditor.md`, `docs/style-guide.md`
  sections 2.3, 2.4, 3, 8.
- `tools/ste_check.py` run per file from the repository root; extraction and
  tell scans were ad hoc scripts kept outside the repository.
- Not checked: facts (fact checker), typography and figures (typographer),
  continuity (the other editor, who is changing the same files now, so line
  locators may have moved; quotations will find the sentences).

## Fixes applied

Applied 2026-11-11 by the copyeditor to `book/chapters/00` through `16` and `book/appendices/a` through `d`. `e-glossary.md` and `z-colophon.md` were not touched. `press check` passed afterwards, and each of the three sentinel phrases still appears exactly once.

| File | Before | After |
|---|---|---|
| a-command-reference.md | `press all` builds neither the print interior nor the cover wrap, which `press print`, `press verify-print`, and `press coverwrap` make, unless print ordering is on, when the commerce gate builds them. | `press all` builds neither the print interior nor the cover wrap. `press print`, `press verify-print`, and `press coverwrap` make them, and the commerce gate builds them when print ordering is on. |
| b-configuration-reference.md | ), it stacks on the title page, one clause to a line, and on the landing page. | ), it stacks on the title page, one clause to a line. It also stacks on the landing page. |
| b-configuration-reference.md | front matter: the title page, the copyright page (the press calls it the colophon), and the dedication, epigraph, and acknowledgments pages. | front matter: the title page, the copyright page, and the dedication, epigraph, and acknowledgments pages. The press calls the copyright page the colophon. |
| c-messages.md | one of three unfinished markers: two placeholder abbreviations followed by the verb "write", or the Latin dummy copy of the typesetter. | one of three unfinished markers. Two are placeholder abbreviations followed by the verb "write", and the third is the Latin dummy copy of the typesetter. |
| c-messages.md | **Cause.** The manuscript witness line, the longest markup-free line of 40 or more characters in the manuscript, is absent from the edition. | **Cause.** The edition lacks the manuscript witness line, the longest markup-free line of 40 or more characters in the manuscript. |
| 00-preface.md | A short paragraph set off from the text that opens with the word Warning marks a step that can cost you work or send a broken artifact to a printer. | A short paragraph set off from the text and opened by the word Warning marks a step that can cost you work. The same step can send a broken artifact to a printer. |
| 01-introduction.md | A *scar*, in the press's vocabulary, is a production failure turned into a guard. Several of them appear later in this chapter. | In the press's vocabulary, a production failure turned into a guard is a *scar*. |
| 01-introduction.md | Neither book lives in the press repository. The repository holds the machinery, and each book keeps its own repository. | The press repository holds only the machinery, and each book keeps its own repository. |
| 01-introduction.md | epubcheck with a Java to run it, and poppler, a set of PDF tools whose `pdftoppm` renders a page as an image for the verifier. | epubcheck with a Java to run it, and poppler. Poppler is a set of PDF tools, and its `pdftoppm` renders a page as an image for the verifier. |
| 01-introduction.md | the checker refuses with `sentinel not found in the manuscript:`, and if an edition lacks one, | the checker refuses with `sentinel not found in the manuscript:`. If an edition lacks one, |
| 01-introduction.md | A warning in prose is not enough by itself. | (deleted) |
| 01-introduction.md | That is another scar. | (deleted) |
| 01-introduction.md | The tour takes it from an empty directory to a full dist directory, using the commands from the press QUICKSTART with the Alice book's names in place. | The tour takes it from an empty directory to a full dist directory. It uses the commands from the press QUICKSTART, with the Alice book's names in place. |
| 01-introduction.md | last week's PDF blesses last week's PDF. | last week's PDF accepts last week's PDF. |
| 02-installing-press.md | Nobody has to grant your book access to anything. | (deleted) |
| 02-installing-press.md | Press does not set type itself, and it does not check an EPUB against the retail rules itself. It prepares the manuscript, decides what to build and in what order, and hands the work to older, specialized programs. | Press prepares the manuscript, decides what to build and in what order, and hands the work to older, specialized programs. It sets no type itself, and it checks no EPUB against the retail rules itself. |
| 02-installing-press.md | This chapter describes it later. | (deleted) |
| 03-the-shape-of-a-book.md | `cd my-book && git init && make all`, and the quick start in the press documentation ends | `cd my-book && git init && make all`. The quick start in the press documentation ends |
| 03-the-shape-of-a-book.md | gives the title page its roman numerals. You never type the year twice. | gives the title page its roman numerals, so you never type the year twice. |
| 03-the-shape-of-a-book.md | it adds a second line, starting with an arrow, that says where to go instead. | it adds a second line that begins with an arrow and says where to go instead. |
| 03-the-shape-of-a-book.md | it blesses artifacts that no longer match | it accepts artifacts that no longer match |
| 04-writing-the-manuscript.md | You never type a tie of your own. You type "Rev. Dodgson" and "p. 42", and the filter | You type "Rev. Dodgson" and "p. 42" with ordinary spaces, and the filter |
| 04-writing-the-manuscript.md | The section "Tables" later in this chapter covers them. | (deleted) |
| 06-checking-the-manuscript.md | passes the checker, because the manuscript holds it whole, and then fails in the Print edition. | passes the checker, because the manuscript holds it whole. It then fails in the Print edition. |
| 06-checking-the-manuscript.md | The jargon lint reads only the manuscript files, and the audit directories are left to the style audit. | The jargon lint reads only the manuscript files. The style audit reads the audit directories. |
| 07-building-the-editions.md | The press does not allow this through its command line. Every verify target rebuilds the artifacts it verifies before it verifies them. | Every verify target rebuilds the artifacts it verifies before it verifies them, and the command line offers no way around that. |
| 07-building-the-editions.md | CI requires those tests to run, starting with version 3.0.2, and holds | CI requires those tests to run from version 3.0.2 on and holds |
| 08-verifying-the-artifacts.md | You do not choose the witness. The press finds it, and it changes when you write a longer plain line. | You do not choose the witness: the press finds it. The witness changes when you write a longer plain line. |
| 08-verifying-the-artifacts.md | The verifier does not trust the zip that the builder wrote. It recomputes the member list from the same policy, `publication_members()`, and compares. | The verifier recomputes the member list from the same policy, `publication_members()`, and compares it with the zip the builder wrote. |
| 08-verifying-the-artifacts.md | An index from yesterday's manuscript cannot reach today's PDF. | (deleted) |
| 09-the-house-design.md | the width of its *paper column*, the framed column that holds the text on the reader site. | the width of its *paper column*. The paper column is the framed column that holds the text on the reader site. |
| 09-the-house-design.md | restates the accent in the cloth red, though the header uses the accent nowhere, and it asks for the fairy-dust scene break. | restates the accent in the cloth red. The header uses the accent nowhere. It also asks for the fairy-dust scene break. |
| 09-the-house-design.md | The house text width is stated, and the other four are derived from Table 9.4: the trim width less the inner and outer margins. | The figure takes the house text width as stated and derives the other four from Table 9.4: the trim width less the inner and outer margins. |
| 10-front-matter-index-authorities.md | You never mark up the manuscript for it. You list the terms a reader will look up, and the press finds them in the text. | You list the terms a reader will look up, and the press finds them in the text without any markup. |
| 12-the-print-pack.md | each figure and plate at 1900 pixels, which is about 300 PPI at 6.3 inches. | each figure and plate at 1900 pixels. That is about 300 PPI at 6.3 inches. |
| 12-the-print-pack.md | The commerce gate builds the interior and the wrap itself, computes the *edition manifest*, the JSON file the gate writes with the production facts and their hash, and then looks for a qualification. | The commerce gate builds the interior and the wrap itself and computes the *edition manifest*. The manifest is the JSON file the gate writes with the production facts and their hash. The gate then looks for a qualification. |
| 12-the-print-pack.md | You do not choose the id. The press computes it, and the commerce gate computes it each time | The press computes the id, and the commerce gate computes it again each time |
| 12-the-print-pack.md | the first twelve characters of the id: the gate prints | the first twelve characters of the id. The gate prints |
| 13-registrations.md | `press new alice --author "Lewis Carroll"`, before the changes of Chapters 3 and 10, and before you set any registration. | `press new alice --author "Lewis Carroll"`. The scaffold predates the changes of Chapters 3 and 10, and you have set no registration yet. |
| 13-registrations.md | a print ISBN that differs from the barcode's, or an EPUB ISBN that differs from the EPUB identifier. | a print ISBN that differs from the barcode's. It cannot show an EPUB ISBN that differs from the EPUB identifier either. |
| 13-registrations.md | It never contacts the Library of Congress. You copy the values into the form yourself, so the submission stays in your hands. | You copy the values into the form yourself, because the press never contacts the Library of Congress. |
| 13-registrations.md | The press cannot buy any of these numbers, and it does not try. | The press cannot buy any of these numbers. |
| 15-the-desk-and-the-machines.md | starts as a `press` command, and you can type the command | starts as a `press` command. You can type the command |
| 16-inside-the-press.md | declare it in the model with its type and its default and in the CLI registry in *config_schema.py*, and read it from the `Book` everywhere. | declare it in the model, with its type and its default, and in the CLI registry in *config_schema.py*. Then read it from the `Book` everywhere. |
| 16-inside-the-press.md | turns the contract red, and the floating major | fails the release contract, and the floating major |
| 05-figures-and-plates.md | "guardrail" (1 uses) | "guard" |
| 11-the-art-department.md | "guardrail" (5 uses) | "guard" |
| b-configuration-reference.md | "guardrail" (3 uses) | "guard" |

Declined, with reason:

- 01 #7 (heading "Facts are stated once" repeated as the first sentence), 03 #4, 10 #2, 13 #5 (the first-law formula repeated): the recurring first-law quotation stays by instruction.
- 01 #8 ("2 sentinels") and 15 #2 ("5 to 15 words"): "may" items, not "should".
- z-colophon #1 (hidden actor): the colophon is out of scope for this pass (another writer is editing it).
- Section 2 "may" patterns (the 07 rhythm run, the uniform chapter-ending pointers, the quotation lead-ins): not "should" findings, and the "In the words of X" lead-ins stay by instruction.

Changed from the audit's suggested wording:

- 2026 words: "blesses" became "accepts", "guardrail" became "guard" (all five uses in 11 and both in appendix B as well as the one in 05), and "turns the contract red" became "fails the release contract". The quoted CLAUDE.md "blesses" in 08 and 16 stays.
- 08 #1 keeps the sentinel "You do not choose the witness" and joins its affirmation with a colon instead of rewriting the sentence.
- 01 scar duplicate: the chapter keeps its own italic definition (vocabulary rule) but no longer repeats the preface word for word. The audit's suggested replacement held a semicolon.
- 02 #2 keeps "against the retail rules", 04 #1 keeps "Rev. Dodgson" and "p. 42", 07 footnote keeps "At the time of this writing" and uses no perfect tense, 09 #3 names the figure as the actor because the source does not say the press derives the widths, and B #1 keeps "or," verbatim without claiming one-clause-per-line on the landing page.
