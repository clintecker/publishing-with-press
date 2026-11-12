# Desk brief: STE80 editor

You edit one manuscript file, `book/chapters/07-building-the-editions.md`, so that every sentence in it obeys
the structural half of the prose contract: Pass 2 of the STE80 method at
80 percent, as `docs/skills/ste80-humanizer/SKILL.md` defines it, with the
three relaxations `docs/prose-contract.md` grants a 1999 technical book.
You change how sentences are built. You do not change what they say.

## Read first, in this order

1. `docs/prose-contract.md`, the whole file. Its prompt block is the law,
   and its relaxations stand: "however", "therefore", "whether", "should",
   and "we recommend" stay. The hard ceiling is 30 words, the target is
   16 to 22 on average, and the rhythm must vary.
2. `docs/skills/ste80-humanizer/SKILL.md`, the Pass 2 table (S1 to S15),
   the fidelity rules, and "When not to act". Then
   `docs/skills/ste80-humanizer/references/ste80-rules.md` for the
   examples. Pass 1 is already enforced by `press check` and a prior audit.
   Act on a Pass 1 tell only if you meet one.
3. `docs/vocabulary.md` (one term per thing) and `docs/style-guide.md`
   section 3 (voice) and section 8 (era touches).
4. The ratchet's leads for your file:
   `python3 tools/ste-ratchet.py --report | sed -n '/book/chapters/07-building-the-editions.md/,/^book/p'`.
   Leads, not verdicts. The sentence counter is right. The passive and
   "-ing" heuristics are often wrong, and you decide.

## Mode by passage

- **Humanize (Pass 2 at 80 percent)** for body prose, admonitions,
  footnotes, captions, table cells of running prose, and glossary entries.
- **Light** for the Preface, every sidebar (a blockquote with a bold
  title), every anecdote and war story, and every epigraph: fix only a
  sentence over 30 words, a sentence with three ideas, or a semicolon.
  Voice is the point of those passages.
- **Never** inside a code fence, a code span, a quotation in double
  quotes, a command, a path, a flag, a YAML key, a message the press
  prints, a figure identifier, a footnote label, or a heading.

## What to do, sentence by sentence

- One idea per sentence. Two linked facts may share one with "and" or
  "because". Three ideas is two sentences.
- Over 30 words is always split. Over 25 is split unless the split would
  break the meaning. Vary the length afterward. A row of ten-word
  sentences is the other failure.
- Name who acts: press, pandoc, LuaLaTeX, latexmk, the verifier, the
  checker, you. Keep a passive only when the actor is unknown or does not
  matter, and say so in the report if you kept more than two.
- Simple tenses. "has been" and "is being" become past or present.
- Put the action in the verb. "makes a decision" is "decides". Break an
  "-ing" chain into clauses with a subject.
- One exact verb for a phrasal verb when English has one that fits the
  voice ("examine", not "look at"), and keep the phrasal verb when the
  exact verb sounds like a form letter.
- At most three nouns in a row.
- One topic per paragraph and six sentences at most. Split a longer one
  at its turn of topic. Every paragraph must still be under 190 words,
  and a blockquote sidebar counts as one paragraph.
- A condition comes before its command. A warning comes before the step
  it protects.
- One term per thing, the term `docs/vocabulary.md` fixes.

## Fidelity, which outranks everything above

- Every fact stays, at its stated strength. "may fail" never becomes
  "fails". "In most cases" survives in some form.
- Numbers, names, dates, versions, identifiers, and quotations stay exact.
- Add nothing: no new example, reason, warning, or gloss.
- The three sentinel phrases must survive byte for byte wherever they
  stand: "You do not choose the witness", "On a fresh scaffold it
  succeeds", "the selftest skips the checks".
- Every term in `config/index-terms.yaml` must still occur in the book.
  If you reword a sentence that carries one of your file's index terms,
  keep the term's exact spelling in the new sentence.
- The markup law holds: ASCII, no em or en dashes, no semicolons in prose,
  straight quotes, no heading attributes added or removed, no fence
  touched, no line of code over 63 columns, image line then blank line
  then art comment, footnote labels `[^N-x]`.

## How to work

1. Read the whole file once as a reader.
2. Make a fact list for each paragraph you will change before you change
   it. After the change, check the paragraph against the list.
3. Edit the file in place. Do not reflow unchanged paragraphs.
4. Run `~/code/.pwp-venv/bin/press check` from the repository root. It
   must pass. Then rerun the ratchet report for your file. Its count must
   be at or below the baseline in `tools/ste-baseline.json`, and lower
   where the lead was real.
5. Write `docs/briefs/reports/ste-07.md`: the ratchet count before and
   after, one line per edit (line number, rule by its S number or contract
   name, the old sentence, the new sentence), the leads you declined with
   the reason, and the passives you kept with the reason.

Do not commit. Do not dispatch anyone. Do not touch any other file under
`book/` or `config/`.

Return: status, the count before and after, the number of edits, and
anything you are unsure you kept faithful.
